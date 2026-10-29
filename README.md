# AI Agent Team

Echipă de 8 specializări la cerere, coordonată de AI Operations Architect, cu plafon total de **100 EUR/lună**. Documentele definesc roluri și un flux de lucru; nu pornesc singure agenți permanenți.

**ecomputer.ro, 29 octombrie:** domeniul principal și www sunt active în Sites cu SSL activ. [www.ecomputer.ro](https://www.ecomputer.ro/) afișează MVP-ul demonstrativ; pentru domeniul fără www răspunsurile publice sunt încă neuniforme. [Conectare și costuri](reports/ecomputer-domain-connection.md), [verificarea publicării](reports/ecomputer-release-followup.json). Produsele și comenzile sunt demonstrative, fără plată sau livrare reală.

- [Analiza costurilor și sursele oficiale — 29 octombrie 2026](COST-OPTIMIZATION.md)
- [ecomputer.ro — MVP-ul nou furnizat de utilizator și verificările efectuate](reports/ecomputer-mvp-status.md)
- [Arhitectura și contractul între agenți](ARCHITECTURE.md)
- [Planul de implementare pe 7 zile](IMPLEMENTATION-7-DAYS.md)
- [Acces verificat și limitări](reports/CAPABILITIES.md)
- [Audit public ecomputer.ro și blocajul de disponibilitate](reports/ecomputer-audit.md)
- [Recuperarea vechiului hosting — document istoric, anulată](reports/ecomputer-recovery-runbook.md)
- [Registru operațional](ops/README.md)

În Codex, pornește o sesiune în acest repository și cere:

> Citește AGENTS.md, agents/operations-manager.md și IMPLEMENTATION-7-DAYS.md. Execută următoarea sarcină ready din ops/backlog.json folosind rolul potrivit. Verifică rezultatul, actualizează raportul și costurile. Nu cumpăra servicii, nu modifica abonamente și nu publica în producție fără aprobare. Dacă un acces lipsește, finalizează partea independentă și documentează blocajul.

Verificarea locală a bugetului, fără rețea sau apeluri AI:

```bash
python3 scripts/budget_report.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Recomandare: un singur Plus, Codex inclus, API opțional după aprobare. Valoarea abonamentului și consumul real al contului sunt încă necunoscute. `ops/budget.json` păstrează API dezactivat. Scriptul raportează registrul local; nu oprește traficul către furnizori.

Pentru ecomputer.ro, codul magazinului se lucrează într-un repository separat, conform profilului Web Architect. Acest repository păstrează coordonarea, costurile și livrabilele operaționale.
