# Audit public ecomputer.ro — WEB-001

**Decizie ulterioară a utilizatorului:** contractul de hosting s-a încheiat, iar vechiul site nu se recuperează. Construim un MVP nou de laptopuri SH/refurbished/noi. Auditul de mai jos rămâne dovadă istorică a paginii publice; prioritățile de recuperare sunt înlocuite de [starea MVP-ului nou](ecomputer-mvp-status.md).

Audit din **2026-10-29**, completat cu verificarea independentă QA din intervalul **13:34:50–13:35:12 UTC**. Responsabil: Web Architect AI. Arie: adresele publice accesibile fără autentificare.

## Concluzie executivă

**Prioritatea P0 este clarificarea și recuperarea disponibilității magazinului.** În observația publică efectuată de Operations, `https://ecomputer.ro/` redirecționează la `https://ecomputer.ro/cgi-sys/suspendedpage.cgi`, cu titlul **Account Suspended** și textul:

> This Account has been suspended.
>
> Contact your hosting provider for more information.

În această observație, vizitatorul nu ajunge la magazin. Nu putem evalua catalogul, paginile produselor sau cumpărarea prin adresa principală. Nu avem date de trafic, comenzi sau venituri pentru a cuantifica pierderile comerciale.

**Cauza suspendării este necunoscută.** Mesajul nu dovedește neplata, un incident de securitate, depășirea resurselor, ștergerea datelor sau pierderea backupurilor. Linkul de contact afișat nu dovedește cine deține contractul de hosting. Calea de suspendare nu identifică tehnologia magazinului.

## Dovadă și metodă

| Element | Observație transmisă de Operations |
| --- | --- |
| Intrare | `https://ecomputer.ro/` |
| Metodă | Extragere publică prin `tinyfish_fetch_content`, cu prospețime solicitată `ttl: 0` |
| Destinație finală | `https://ecomputer.ro/cgi-sys/suspendedpage.cgi` |
| Titlu | `Account Suspended` |
| Conținut material | Mesajul citat mai sus |
| Link extras | `https://www.awebdesign.ro/contact` |
| Data observației | 29 octombrie 2026; ora exactă a capturii inițiale nu a fost transmisă acestui rol |
| Limita probei | Un rezultat al adresei publice principale, dintr-un punct de acces; nu stabilește durata incidentului sau disponibilitatea din toate rețelele |

Operations păstrează captura sursei în [ecomputer-source-evidence.json](ecomputer-source-evidence.json). Web Architect nu a repetat cererea de rețea. QA a confirmat independent același mesaj pe https://www.ecomputer.ro/, http://ecomputer.ro/ și URL-ul HTTPS direct al paginii de suspendare; observațiile sunt în [ecomputer-qa-evidence.json](ecomputer-qa-evidence.json), iar verdictul în [QA-WEB-001.md](QA-WEB-001.md). Toate verificările provin din instrumentele disponibile în această sesiune; nu demonstrează starea din toate rețelele sau durata incidentului. Din aceste extrageri nu atribuim un cod HTTP, un scor de performanță, un rezultat de securitate sau o verificare vizuală pe mobil.

Proba tehnică separată `ecomputer-http-evidence.json` consemnează blocarea încercărilor urllib ale executorului local prin `Operation not permitted`. Aceasta este o limitare a mediului de execuție, **nu un răspuns al site-ului și nu o dovadă de indisponibilitate**. Concluzia publică de mai sus se bazează pe captura connectorului web.

## Ce este verificat și ce rămâne blocat

| Arie | Stare și limită |
| --- | --- |
| Acces la magazin prin adresa principală | Blocaj public observat: redirecționare la pagina de suspendare |
| Homepage, navigare, catalog, filtrare | Nu au putut fi auditate ca pagini ale magazinului |
| Produs, opțiuni RAM/SSD, coș | Neverificate |
| Checkout ramburs, validarea comenzii, confirmări | Neverificate; nu s-a plasat nicio comandă |
| Mobil, accesibilitate, viteză, SEO al magazinului | Neverificate; nu există scoruri sau constatări de UX inventate |
| Administrare produse/comenzi, hosting, DNS, cod și bază de date | Acces neconfirmat; nicio modificare efectuată |
| Stoc, prețuri, trafic, conversii, vânzări și backupuri | Date indisponibile |

Homepage, catalogul, RAM/SSD, coșul, rambursul și administrarea provin din brief-ul `agents/web-architect.md`. Sunt cerințe de analizat, **nu funcționalități confirmate pe site**. Un magazin temporar indisponibil nu justifică singur schimbarea platformei sau reconstrucția lui.

## Backlog prioritizat

Efortul este o estimare pentru munca de verificare/pregătire, nu durata garantată a intervenției furnizorului. Ordinea urmărește disponibilitatea, apoi continuitatea datelor și fluxul comercial.

| ID / prioritate | Acțiune și responsabil | Impact | Efort estimat / dependențe | Criteriu de acceptare |
| --- | --- | --- | --- | --- |
| INC-001 / **P0** | Operations + titular: citește notificarea de suspendare, starea serviciului și explicația din panoul/corespondența de hosting deja existente | Identifică problema reală și evită intervenții nepotrivite | 15–30 min dacă accesul există; depinde de accesul autorizat al titularului | Motiv și instrucțiuni ale furnizorului consemnate cu sursă; dacă lipsesc, cauza rămâne explicit necunoscută |
| INC-002 / **P0** | Web + Operations: inventariază backupurile existente și pregătește remedierea propusă pe baza cauzei confirmate | Protejează continuitatea magazinului și permite o decizie informată | 30–60 min de pregătire; depinde de INC-001 și acces read-only la informații despre backup/date | Plan concret cu operații, risc, cost și rollback; niciun restore, deploy, șters sau serviciu nou executat |
| INC-003 / **P0** | QA: după remedierea autorizată, reverifică adresa principală și paginile comerciale cunoscute | Confirmă că vizitatorul ajunge din nou la magazin | 15–30 min; depinde de reluarea serviciului | Pagini ale magazinului accesibile și redirecționări explicate, cu URL-uri, răspunsuri și data verificării; fără a declara rezolvat doar pentru un cod HTTP 200 |
| WEB-003 / **P1** | Web: inventariază codul, platforma, hostingul și mediul de test; păstrează repository separat pentru magazin | Permite modificări mentenabile și verificabile | 30–90 min; depinde de acces autorizat și documentație existentă | Platforma și repository-ul identificate din dovezi, pași de rulare documentați, fără secrete în Git |
| WEB-004 / **P1** | Web + Business + Data: confruntă produsele, prețurile, stocul și regulile RAM/SSD cu date confirmate | Reduce riscul de ofertă sau comandă incorectă | 1–2 ore pentru un eșantion delimitat; depinde de sursa catalogului | Eșantion trasabil și reguli de compatibilitate/preț/stoc explicite; lipsurile devin taskuri, nu date inventate |
| QA-WEB-001 / **P1** | QA + Web: auditează navigarea și fluxul produs → configurare → coș → checkout, inclusiv mobil | Verifică utilizarea și corectitudinea cumpărării | 1–3 ore pentru fluxul delimitat; depinde de INC-003, WEB-004 și mediu de test | Dovezi reproductibile, defecte prioritizate; comenzile exclusiv de test în mediu autorizat; nicio plată/comandă reală |
| AUTO-001 / **P2** | Automation: propune verificarea periodică a disponibilității, reutilizând infrastructura existentă dacă există | Reduce timpul până la observarea unui incident viitor | 30–60 min pentru propunere/dry-run; depinde de executor și destinație autorizate | Verificarea distinge magazinul de pagina de suspendare, are timeout/jurnal și cost estimat; nu se declară programată înainte de configurare și probă |

## Pași concreți de recuperare pregătiți

1. **Obține explicația exactă.** Titularul sau un instrument autorizat citește notificarea și starea serviciului din contul existent. Păstrăm în raport numai concluziile necesare, fără date personale, identificatori de cont sau credențiale în repository-ul public.
2. **Verifică read-only continuitatea datelor.** Notează dacă există backupuri, data lor și aria acoperită — fișiere, bază de date și configurație. Existența unui backup nu se presupune și nu se testează prin restore în producție.
3. **Pregătește o intervenție proporțională cu motivul confirmat.** Dacă furnizorul cere o acțiune, documentăm exact pașii, responsabilul, costul și riscul. Nu plătim facturi, nu schimbăm abonamente, nu mutăm hostingul, nu restaurăm și nu publicăm fără aprobarea acțiunii concrete.
4. **Reverifică după intervenția autorizată.** Testăm întâi adresa principală, apoi URL-uri reale de categorie/produs descoperite în magazin. Confirmăm conținutul și navigarea, nu doar răspunsul tehnic al domeniului.
5. **Reia auditul comercial.** După accesibilitate, verificăm pagina produsului, opțiunile, coșul, mobilul și checkoutul în condiții de test autorizate. Atunci putem alege prima îmbunătățire implementabilă.

Nu a fost contactat furnizorul și nu au fost trimise formulare sau mesaje. Accesul admin, cauza și remedierea efectivă rămân în afara dovezilor curente.

## Raport de execuție

**Realizat efectiv:** citite regulile repository-ului și brief-ul Web; analizată dovada publică transmisă de Operations; creat acest audit delimitat, cu incidentul observat, limite, 7 priorități și pașii de recuperare pregătiți.

**Urmează:** clarificarea notificării de hosting, conform [procedurii pregătite](ecomputer-recovery-runbook.md). QA a acceptat auditul public delimitat. Auditul complet al magazinului rămâne blocat până când paginile sunt accesibile.

**Cost:** nicio achiziție, nicio modificare de abonament și niciun apel direct la OpenAI API efectuat de acest rol. Costul monetar al utilizării platformei este necunoscut. Nu este propus un serviciu nou plătit pentru diagnostic.

**Aprobare necesară:** nicio aprobare suplimentară pentru acest raport. Următoarea intervenție de hosting se pregătește numai după cauza confirmată și accesul autorizat; orice achiziție, restore sau publicare în producție necesită aprobarea corespunzătoare conform `AGENTS.md`.
