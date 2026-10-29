#!/usr/bin/env python3
"""Raport local, fără API. Estimările sunt costuri viitoare, încă neînregistrate.

CSV: date,category,provider,kind,amount,currency,eur_per_unit,reference.
kind este actual sau estimate; category este subscription, api sau optional.
Monede acceptate: EUR, USD, RON, GBP. Pentru monedele non-EUR cursul explicit
este EUR per unitate monetară. Nu înregistra aceeași factură și ca estimare.
Acest raport semnalează depășiri; nu poate opri apelurile sau facturarea externă.
"""

import argparse
import csv
from datetime import date
from decimal import Decimal, DecimalException, InvalidOperation
import json
from pathlib import Path
import re
import sys


FIELDS = ["date", "category", "provider", "kind", "amount", "currency", "eur_per_unit", "reference"]
CATEGORIES = ("subscription", "api", "optional")
CURRENCIES = {"EUR", "USD", "RON", "GBP"}
ZERO = Decimal("0")


def number(value, name, positive=False):
    if isinstance(value, bool) or value is None:
        raise ValueError(f"{name}: valoare numerică invalidă")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f"{name}: valoare numerică invalidă") from exc
    if not result.is_finite() or result < ZERO or (positive and result == ZERO):
        raise ValueError(f"{name}: trebuie o valoare finită {'pozitivă' if positive else 'nenegativă'}")
    return result


def load_budget(path):
    with Path(path).open(encoding="utf-8") as handle:
        budget = json.load(handle)
    if not isinstance(budget, dict):
        raise ValueError("Configurația trebuie să fie un obiect JSON")
    month = budget.get("month", "")
    if not isinstance(month, str) or not re.fullmatch(r"\d{4}-\d{2}", month):
        raise ValueError("month: folosește YYYY-MM")
    try:
        date.fromisoformat(month + "-01")
    except ValueError as exc:
        raise ValueError("month: lună invalidă") from exc
    if budget.get("currency") != "EUR":
        raise ValueError("Bugetul trebuie exprimat în EUR")
    cap = number(budget.get("monthly_cap_eur"), "monthly_cap_eur", positive=True)
    if cap > Decimal("100"):
        raise ValueError("monthly_cap_eur nu poate depăși 100 EUR")
    raw_allocations = budget.get("allocations_eur")
    if not isinstance(raw_allocations, dict) or set(raw_allocations) != {*CATEGORIES, "reserve"}:
        raise ValueError("allocations_eur: sunt necesare subscription, api, optional, reserve")
    allocations = {key: number(value, f"allocations_eur.{key}") for key, value in raw_allocations.items()}
    if sum(allocations.values(), ZERO) > cap:
        raise ValueError("Alocările planificate depășesc plafonul lunar")
    if type(budget.get("api_enabled")) is not bool or type(budget.get("ledger_complete")) is not bool:
        raise ValueError("api_enabled și ledger_complete trebuie să fie booleene")
    approved = number(budget.get("approved_api_eur"), "approved_api_eur")
    if approved > allocations["api"] or (not budget["api_enabled"] and approved != ZERO):
        raise ValueError("Aprobarea API depășește alocarea sau API este dezactivat")
    subscription_status = budget.get("subscription_status")
    if not isinstance(subscription_status, str) or subscription_status not in {"unknown", "verified"}:
        raise ValueError("subscription_status trebuie să fie unknown sau verified")
    budget.update(cap=cap, allocations=allocations, approved=approved)
    return budget


def read_ledger(path, month):
    totals = {kind: {category: ZERO for category in CATEGORIES} for kind in ("actual", "estimate")}
    counts = {kind: {category: 0 for category in CATEGORIES} for kind in ("actual", "estimate")}
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            raise ValueError("CSV: antet invalid; așteptat " + ",".join(FIELDS))
        for line_no, row in enumerate(reader, 2):
            prefix = f"CSV linia {line_no}"
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"{prefix}: număr invalid de câmpuri")
            row = {key: value.strip() for key, value in row.items()}
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["date"]):
                    raise ValueError("data trebuie să fie YYYY-MM-DD")
                date.fromisoformat(row["date"])
                if row["category"] not in CATEGORIES or row["kind"] not in totals:
                    raise ValueError("categorie sau kind invalid")
                if not row["provider"]:
                    raise ValueError("provider lipsește")
                if row["currency"] not in CURRENCIES:
                    raise ValueError("monedă nesuportată")
                amount = number(row["amount"], "amount")
                if row["currency"] == "EUR":
                    rate = number(row["eur_per_unit"] or "1", "eur_per_unit", positive=True)
                    if rate != Decimal("1"):
                        raise ValueError("cursul EUR trebuie să fie 1 sau gol")
                else:
                    rate = number(row["eur_per_unit"], "eur_per_unit", positive=True)
            except ValueError as exc:
                raise ValueError(f"{prefix}: {exc}") from exc
            if row["date"][:7] == month:
                totals[row["kind"]][row["category"]] += amount * rate
                counts[row["kind"]][row["category"]] += 1
    return totals, counts


def build_report(budget_path, ledger_path):
    budget = load_budget(budget_path)
    totals, counts = read_ledger(ledger_path, budget["month"])
    actual = sum(totals["actual"].values(), ZERO)
    estimate = sum(totals["estimate"].values(), ZERO)
    forecast = actual + estimate
    subscription_verified = budget["subscription_status"] == "verified" and counts["actual"]["subscription"] > 0
    complete = budget["ledger_complete"] and subscription_verified
    lines = [
        f"Raport local {budget['month']} — EUR",
        f"Plafon lunar: {budget['cap']:.2f}; alocare totală: {sum(budget['allocations'].values(), ZERO):.2f}",
        f"Cost observat în registru: {actual:.2f}",
        f"Estimări viitoare înregistrate: {estimate:.2f}",
        f"Previziune parțială (observat + estimări viitoare): {forecast:.2f}",
        "Abonament: " + ("verificat din registru" if subscription_verified else "unknown — factură/cost neconfirmat"),
        "Total facturat: " + ("registru declarat complet" if complete else "INCOMPLET; lipsa înregistrărilor nu dovedește cost zero"),
        f"API activat local: {budget['api_enabled']}; plafon aprobat: {budget['approved']:.2f}",
        "Categorie | Observat | Estimări viitoare | Alocare",
    ]
    alerts = []
    for category in CATEGORIES:
        observed = totals["actual"][category]
        future = totals["estimate"][category]
        allocation = budget["allocations"][category]
        lines.append(f"{category} | {observed:.2f} | {future:.2f} | {allocation:.2f}")
        if observed + future > allocation:
            alerts.append(f"{category}: costurile și estimările depășesc alocarea")
    lines.append(f"Rezervă planificată: {budget['allocations']['reserve']:.2f} (nu reprezintă cost)")
    if forecast > budget["cap"]:
        alerts.append("Costurile și estimările depășesc plafonul lunar")
    api_forecast = totals["actual"]["api"] + totals["estimate"]["api"]
    if api_forecast > budget["approved"]:
        alerts.append("API: costurile și estimările depășesc plafonul aprobat")
    if alerts:
        lines.extend("ALERTĂ: " + alert for alert in alerts)
    lines.append("Raportul nu execută și nu oprește apeluri API, achiziții sau facturarea externă.")
    return "\n".join(lines), bool(alerts)


def main(argv=None):
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget", type=Path, default=root / "ops/budget.json")
    parser.add_argument("--ledger", type=Path, default=root / "ops/cost-ledger.csv")
    args = parser.parse_args(argv)
    try:
        report, over_limit = build_report(args.budget, args.ledger)
    except (ValueError, OSError, csv.Error, DecimalException) as exc:
        print(f"EROARE: {exc}", file=sys.stderr)
        return 1
    print(report)
    return 2 if over_limit else 0


if __name__ == "__main__":
    sys.exit(main())
