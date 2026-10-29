# Operare și costuri

1. Citește AGENTS.md și ARCHITECTURE.md; selectează un task ready din backlog.json.
2. Completează task-template.json pentru delegare; nu trimite întregul istoric fiecărui rol.
3. Menține o singură implementare activă. QA verifică livrabilul concret.
4. La acceptare, salvează dovezi, costuri și următorul pas; apoi actualizează backlogul.

## Monitorul local

Din rădăcina repository-ului:

```bash
python3 scripts/budget_report.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

`budget.json` conține anvelopele lunare, nu cheltuieli executate. `cost-ledger.csv` pornește gol: lipsa rândurilor nu dovedește cheltuieli zero. Urmează schema și documentația din script când adaugi date. Nu salva date personale sau facturi în acest repository public.

Actualizează lunar perioada. Înregistrează sume brute, inclusiv taxele aplicabile; pentru monede diferite de EUR, un curs explicit `eur_per_unit` din documentul de plată. Marchează rândurile `actual` sau `estimate`. Înlocuiește estimarea aferentă când apare factura, pentru a evita dublarea.

Pentru credite prepaid, în registrul plafonului de numerar înregistrează achiziția brută o singură dată; nu adăuga din nou consumul acelorași credite drept cheltuială. Consumul tokenurilor se reconciliază separat în dashboard. Pentru pay-as-you-go fără prepaid, urmărește și costurile acumulate nefacturate într-o estimare distinctă, apoi înlocuiește-le cu factura.

Setează confirmarea completitudinii numai după reconcilierea tuturor abonamentelor și serviciilor din luna respectivă. Un raport incomplet nu este o autorizare de cheltuială.

Scriptul nu face cereri de rețea, nu colectează automat facturi, nu rezervă costul apelurilor și nu oprește traficul API. Pentru un runner ulterior sunt necesare rezervare atomică, reconciliere, limite furnizor și verificări fail-closed. `api_enabled=false` documentează starea propusă, nu controlează alte aplicații sau chei existente.

## Raport și acces

Folosește cele patru elemente: realizat efectiv, urmează, cost estimat/real și aprobare necesară. Reîmprospătează reports/CAPABILITIES.md când o integrare este verificată. Nu considera simpla apariție a unui tool drept permisiune pentru toate acțiunile.
