import copy
from contextlib import redirect_stderr
import csv
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location("budget_report", Path(__file__).with_name("budget_report.py"))
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
DEFAULT = json.loads((Path(__file__).resolve().parents[1] / "ops/budget.json").read_text())


class BudgetReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.budget_path = Path(self.temp.name) / "budget.json"
        self.ledger_path = Path(self.temp.name) / "ledger.csv"

    def report(self, rows=(), budget=None):
        self.budget_path.write_text(json.dumps(budget or DEFAULT), encoding="utf-8")
        with self.ledger_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(MODULE.FIELDS)
            writer.writerows(rows)
        return MODULE.build_report(self.budget_path, self.ledger_path)

    def test_empty_ledger_is_incomplete_not_free(self):
        text, alarm = self.report()
        self.assertFalse(alarm)
        self.assertIn("INCOMPLET", text)
        self.assertIn("unknown", text)

    def test_conversion_and_future_estimates_are_separate(self):
        text, alarm = self.report([
            ["2026-10-01", "optional", "test", "actual", "2", "USD", "0.9", "sample"],
            ["2026-10-02", "optional", "test", "estimate", "3", "EUR", "", "future sample"],
            ["2026-09-30", "optional", "test", "actual", "99", "EUR", "", "other month"],
        ])
        self.assertFalse(alarm)
        self.assertIn("Cost observat în registru: 1.80", text)
        self.assertIn("Estimări viitoare înregistrate: 3.00", text)
        self.assertIn("estimări viitoare): 4.80", text)

    def test_over_total_and_api_approval_are_detected(self):
        text, alarm = self.report([
            ["2026-10-01", "api", "test", "actual", "101", "EUR", "", "sample"]
        ])
        self.assertTrue(alarm)
        self.assertIn("depășesc plafonul lunar", text)
        self.assertIn("depășesc plafonul aprobat", text)

    def test_invalid_money_currency_category_date_and_rate_are_rejected(self):
        base = ["2026-10-01", "optional", "test", "actual", "1", "EUR", "", "sample"]
        for index, value in [(4, "NaN"), (4, "Infinity"), (4, "-1"), (5, "BAD"), (1, "reserve"), (0, "2026-02-30"), (6, "2")]:
            with self.subTest(index=index, value=value):
                row = base.copy()
                row[index] = value
                with self.assertRaises(ValueError):
                    self.report([row])
        base[5] = "USD"
        with self.assertRaises(ValueError):
            self.report([base])

    def test_plan_cannot_exceed_100_or_hide_excess_allocation(self):
        for cap, reserve in [("101", "20"), ("100", "21")]:
            with self.subTest(cap=cap, reserve=reserve):
                budget = copy.deepcopy(DEFAULT)
                budget["monthly_cap_eur"] = cap
                budget["allocations_eur"]["reserve"] = reserve
                with self.assertRaises(ValueError):
                    self.report(budget=budget)

    def test_verified_subscription_needs_actual_row(self):
        budget = copy.deepcopy(DEFAULT)
        budget.update(subscription_status="verified", ledger_complete=True)
        text, _ = self.report(budget=budget)
        self.assertIn("INCOMPLET", text)
        text, alarm = self.report([
            ["2026-10-01", "subscription", "test", "actual", "25", "EUR", "", "invoice sample"]
        ], budget=budget)
        self.assertFalse(alarm)
        self.assertIn("registru declarat complet", text)

    def test_invalid_subscription_type_is_rejected(self):
        budget = copy.deepcopy(DEFAULT)
        budget["subscription_status"] = []
        with self.assertRaises(ValueError):
            self.report(budget=budget)

    def test_cli_reports_numeric_overflow_without_traceback(self):
        self.report()
        with self.ledger_path.open("a", newline="", encoding="utf-8") as handle:
            csv.writer(handle).writerow([
                "2026-10-01", "optional", "test", "actual", "1e1000000", "USD", "2", "invalid sample"
            ])
        error = io.StringIO()
        with redirect_stderr(error):
            code = MODULE.main(["--budget", str(self.budget_path), "--ledger", str(self.ledger_path)])
        self.assertEqual(code, 1)
        self.assertIn("EROARE:", error.getvalue())
        self.assertNotIn("Traceback", error.getvalue())


if __name__ == "__main__":
    unittest.main()
