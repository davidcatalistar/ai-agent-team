# Arhitectura echipei AI

## Scop și limite

Echipa are **8 roluri specializate, activate la cerere**, pentru un singur utilizator. Un rol este un set de instrucțiuni și responsabilități; nu implică un abonament separat, o cotă separată sau un proces permanent. Web Architect include implementarea software. Nu există un al nouălea rol de programator.

Bugetul total este de maximum **100 EUR/lună**, incluzând abonamentele, API și celelalte servicii AI, cu taxele și conversia valutară efectiv aplicate. Plafoanele și costurile observate se păstrează în registrul financiar. O sumă rezervată în plan nu reprezintă aprobare de cumpărare.

Regulile din `AGENTS.md` se aplică tuturor rolurilor. Achizițiile, modificările de abonament, operațiile asupra secretelor, publicarea în producție, ștergerile și celelalte acțiuni ireversibile cer aprobare explicită asupra rezultatului concret pregătit. Nu se presupun accesul, dreptul de scriere sau existența unei integrări.

## Roluri și rezultate

| Rol | Responsabilitate | Livrabil verificabil |
|---|---|---|
| [AI Operations Architect](agents/operations-manager.md) | Priorități, delegare, buget, acceptare după QA | Sarcină cu un proprietar; raport și decizie motivate |
| [Web Architect AI](agents/web-architect.md) | Audit, structură web, implementare software și integrare pentru ecomputer.ro | Specificație, modificări pe branch și previzualizare când accesul permite |
| [QA & Release Engineer](agents/qa-release-engineer.md) | Verificare independentă, teste relevante, evaluarea pregătirii pentru lansare | Verdict cu dovezi, defecte și limitări |
| [Automation Engineer](agents/automation-engineer.md) | Scripturi și fluxuri pentru procese repetabile | Dry-run, jurnalizare și oprire la eroare |
| [Research Analyst](agents/research-analyst.md) | Surse oficiale, comparații și incertitudini | Matrice de afirmații cu surse și data consultării |
| [Data & Finance Analyst](agents/data-finance-analyst.md) | Costuri, calcule și productivitate | Registru reconciliat și indicatori reproductibili |
| [Content & Growth Specialist](agents/content-growth.md) | Conținut comercial, SEO și experimente | Texte susținute de date și ipoteze măsurabile |
| [Business Analyst](agents/business-analyst.md) | Cerințe, procese și prioritizarea oportunităților | Brief, criterii de acceptare și backlog ordonat |

## Rutarea modelelor

Selectoarele de mai jos sunt cele verificate în mediul Work/Codex. Ele nu sunt identificatori API și nu stabilesc tarife API. Disponibilitatea se verifică din nou înaintea utilizării într-un mediu nou.

| Complexitate | Alegere inițială | Exemple |
|---|---|---|
| Redusă | GPT-6 Luna | Extragere din surse, clasificare, reformulare, rezumate scurte |
| Implementare software | GPT-6.1 Terra | Modificări în repository, scripturi, diagnostic tehnic |
| Ridicată | GPT-6.1 Sol | Decizii de arhitectură, analiză ambiguă, verificare tehnică dificilă |
| Excepțională | GPT-6 Astra | Escaladare rară după un blocaj documentat și evaluarea costului |

Calculul determinist și instrumentele de verificare au prioritate atunci când pot rezolva sarcina. Operations aprobă escaladarea de model în limita autorizației existente. Un model mai puternic nu înlocuiește sursele, testele sau accesul necesar.

## Flux operațional

1. Operations clarifică rezultatul, verifică accesul și aprobarea existentă, apoi stabilește criteriile și bugetul.
2. Business sau Research intervin numai dacă există o incertitudine relevantă. Nu sunt etape obligatorii pentru orice editare.
3. Un singur executant produce livrabilul și dovezile. Contextul transmis conține doar fișierele și informațiile necesare.
4. QA verifică o versiune fixă a livrabilului, independent de autor, față de criterii. Pentru cod se identifică branch-ul și commit-ul când acestea există.
5. Operations acceptă rezultatul pe baza verdictului și raportează realizat, următorul pas, cost și aprobarea necesară.

Există maximum **o sarcină de implementare activă**. QA poate lucra în paralel pe o versiune fixă. Cercetarea suplimentară în paralel se justifică printr-un livrabil diferit și un beneficiu real; nu se dublează aceeași analiză sau implementare.

Stări: `ready`, `running`, `qa`, `needs_changes`, `blocked`, `done`. `done` necesită criterii îndeplinite și dovezi. Lipsa accesului sau imposibilitatea verificării se raportează explicit; nu se maschează printr-un verdict pozitiv.

## Contract de delegare

```json
{
  "task_id": "WEB-001",
  "owner": "web_architect",
  "goal": "Pregătește auditul inițial pentru ecomputer.ro",
  "inputs": ["brief.md", "capabilities.md"],
  "artifact": "reports/ecomputer-audit.md",
  "acceptance": [
    "Constatări susținute de observații",
    "Backlog ordonat după impact și efort"
  ],
  "budget_eur_max": 0,
  "max_retries": 2,
  "allowed_actions": ["read", "local_write"],
  "status": "ready"
}
```

Căile din exemplu se înlocuiesc cu fișiere existente. `budget_eur_max: 0` permite numai capacitatea deja autorizată, fără cheltuieli externe suplimentare. API nu se activează implicit. Un buget mai mare nu autorizează singur o achiziție.

La predare, agentul adaugă: versiunea artefactului, criteriile verificate și dovezile, limitările, costul estimat separat de cel observat și următorul pas. Costul indisponibil se marchează `necunoscut`, nu `0`.

## Controlul consumului

- Maximum două încercări pentru remedierea aceluiași eșec; apoi diagnostic și decizie Operations. Nu există bucle nelimitate de autorevizuire.
- Se transmit fișiere relevante și rezumate scurte, evitând istoricul complet la fiecare delegare.
- QA verifică proporțional cu impactul: surse pentru cercetare, previzualizare pentru conținut și verificări funcționale pentru schimbările de comportament.
- Înaintea unui apel API autorizat, un executor care aplică bugetul rezervă costul maxim estimabil, inclusiv ieșirea și instrumentele plătite. Fără un cost suficient determinabil, sarcina se reduce sau se oprește pentru decizie.
- După execuție, rezervarea se reconciliază cu utilizarea observată. Se previn rezervările concurente care depășesc soldul.
- Alertele din dashboardul furnizorului nu sunt tratate drept plafon tehnic garantat. Un control descris aici este considerat implementat numai după verificarea codului și a comportamentului său.
- Capacitatea inclusă în abonament poate avea cost marginal extern zero, dar consumă limitele acestuia. Nu se numește utilizare nelimitată.

## Acces și automatizare

Registrul de capabilități consemnează aplicația, contul sau repository-ul, operațiile efectiv testate, data verificării și limitările. Citirea unui repository nu dovedește drept de scriere. Un document de arhitectură nu dovedește configurarea unui scheduler.

Execuția în fundal se declară funcțională numai după verificarea programării, autentificării, mediului de rulare, jurnalizării și opririi la buget. În lipsa lor, rolurile se activează în sesiunea curentă sau prin rulări manuale. Nu se promite monitorizare permanentă.

## Indicatori și raportare

| Indicator | Calcul sau condiție |
|---|---|
| Livrabile acceptate | Numărul sarcinilor `done` cu dovezi |
| Cost/livrabil | Costul atribuit sarcinilor împărțit la livrabilele acceptate; `n/a` când numitorul este zero |
| Acceptare la prima verificare | Livrabile acceptate fără corecție / livrabile verificate |
| Durata de execuție | Timpul dintre `ready` și acceptare; blocajele se arată separat |
| Blocaje de acces | Sarcini blocate de acces / sarcini începute |
| Respectarea bugetului | Cost observat + rezervări active <= plafonul autorizat disponibil |

Ținte inițiale: 100% dintre sarcinile `done` au dovezi, zero depășiri ale plafonului și cel mult o implementare activă. Nu se inventează un obiectiv de productivitate înainte de măsurarea primei săptămâni.

Raportul Operations conține patru rubrici: **realizat efectiv**, **ce urmează**, **cost estimat/observat**, **aprobare necesară**. Planul pe șapte zile este un livrabil separat; zilele planificate nu reprezintă joburi deja programate.
