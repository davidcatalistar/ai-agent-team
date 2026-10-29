# QA independent — OPS-001

Data: **2026-10-29**. Verdict: **accepted**, după remedierea și reverificarea observațiilor. Nu există defecte blocante deschise în aria verificată. Acest verdict acceptă documentația și monitorul local; nu validează un runner API, un scheduler sau lansarea magazinului.

## Aria verificată

- AGENTS.md, README.md, COST-OPTIMIZATION.md, ARCHITECTURE.md și IMPLEMENTATION-7-DAYS.md.
- Cele 8 profiluri din agents/, contractul de task, backlogul, configurația și registrul de costuri.
- scripts/budget_report.py, testele, inventarul accesului, raportul executiv și .gitignore.
- Afirmațiile de preț/limite au fost confruntate cu extrasele oficiale citite în misiune de Operations și Research. Nu am reluat inutil toate cererile web. Situația concretă a contului, factura, TVA-ul și cursul rămân neverificate.

## Comenzi și rezultate

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/budget_report.py
```

**8 teste trecute** la reverificarea finală; rularea monitorului pe registrul inițial a returnat exit 0 și a afișat explicit: abonament `unknown`, total `INCOMPLET`, API dezactivat și plafon API aprobat 0 EUR. Zero rânduri în registru nu sunt prezentate drept dovadă a unui cost lunar zero.

Probe independente suplimentare prin Python, pe fișiere temporare: număr greșit de câmpuri CSV, `kind` invalid, curs `NaN` și dată cu format invalid au fost respinse cu ValueError. Inspecția codului confirmă că nu există cereri de rețea sau operații de facturare. Scriptul semnalează depășirile; nu este un control al traficului API.

Verificare mecanică a linkurilor Markdown relative: **0 destinații lipsă** în momentul verificării. Număr de profiluri în agents/: **8**. .gitignore exclude __pycache__, bytecode și fișierele .env.

## Verificări de fond

| Criteriu | Rezultat |
| --- | --- |
| Buget lunar 30 + 40 + 10 + 20 | **100 EUR**, cu rezervă distinctă de cost |
| Autorizație API vs plan | **0 EUR aprobat**, API dezactivat; plafonul de 40 EUR nu este tratat ca achiziție aprobată |
| Scenariu API | 0,75 + 5 + 6,20 + 2 + 0,125 + 0,60 = **14,675 USD** |
| Sensibilitate la factorul ipotetic 1,30 EUR/USD | Costuri API 1,91 / 19,08 / 95,39 EUR; totaluri cu anvelopa de 30 EUR: **31,91 / 49,08 / 125,39 EUR** |
| Volum intens | Depășirea este recunoscută și cere reducerea volumului; nu este prezentată ca încadrată |
| Plan 7 zile | 29 octombrie–4 noiembrie 2026, 7 date consecutive; plafoane API însumate **10 EUR**; traversarea a două luni este explicată |
| Plus/Pro/Codex/API | Plus 20 USD; Pro 100/200/500; Codex inclus și API separat; prețurile locale și soldurile personale nu sunt inventate |
| Limite | Estimări locale Codex/5 h marcate ca estimări; cote comune, posibile limite săptămânale; fără promisiune de capacitate nelimitată |
| Costuri API secundare | Cache-write, reasoning, tools, viteză, taxe/curs și retries tratate separat; fără dublarea creditelor cumpărate și consumate |
| Control cheltuieli | Hard limit configurabil descris cu întârzierea de aplicare; nu se confundă cu o alertă |
| Specializări | Exact 8 roluri; Web include implementarea; o singură implementare activă și QA independent |
| Execuție reală vs plan | Nu sunt promise procese permanente, scheduler activ, acces admin ecomputer.ro sau API activ |
| Costul sesiunii | Este declarat necunoscut, fără a afirma că tokenurile platformei au costat 0 EUR |

## Observații și limite

1. **Corectat în timpul QA:** OPS-001 folosea `in_review`, în timp ce arhitectura definește `qa`; Operations a aliniat starea la `qa`. Poate fi mutat în `done` după acceptare și salvarea dovezii finale.
2. **P3, corectat și reverificat:** `subscription_status: []` provoca TypeError. Codul verifică acum tipul string; proba independentă prin CLI a returnat exit **1**, mesaj `EROARE` și niciun traceback. Există test de regresie.
3. **P3, corectat și reverificat:** `amount=1e1000000` provoca decimal.Overflow netratat. CLI tratează acum DecimalException; proba independentă a returnat exit **1**, mesaj `EROARE` și niciun traceback. Există test de regresie. Nu a fost introdusă o limită artificială pentru sumele financiare normale.

Nu am verificat accesul cheii API, billingul contului, costurile toolurilor platformei, o publicare GitHub ulterioară sau site-ul ecomputer.ro. Niciun astfel de rezultat nu face parte din verdictul pozitiv.

Realizat efectiv: inspecție independentă, rularea testelor și a raportului, probe negative, verificarea calculelor/linkurilor și acest raport. Urmează: salvarea pachetului în repository și auditul public ecomputer.ro. Achiziții/apeluri directe API efectuate de QA: **niciunul**; consumul monetar al sesiunii este indisponibil. Aprobare suplimentară necesară pentru QA: **niciuna**.
