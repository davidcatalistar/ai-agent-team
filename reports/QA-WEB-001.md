# QA independent — WEB-001, audit public ecomputer.ro

Verificat la **2026-10-29 13:35:12 UTC**, cu revizuirea documentelor la **13:36 UTC**. Responsabil: QA & Release Engineer.

**Verdict: accepted pentru auditul public delimitat, păstrat ca istoric verificat.** Dovezile susțin constatarea paginii de suspendare la momentul capturii. Acest verdict nu declară magazinul funcțional, securizat sau pregătit pentru producție. Utilizatorul a decis ulterior construirea unui magazin nou de la zero și a anulat direcția de recuperare.

## Verificare independentă executată

Am folosit o singură cerere `tinyfish_fetch_content`, cu trei URL-uri, `ttl: 0`, extragere Markdown și metadate. Exclusiv citire publică; fără autentificare, formulare, comenzi, acces admin sau automatizare browser. Captura relevantă este în [ecomputer-qa-evidence.json](ecomputer-qa-evidence.json).

| URL solicitat | URL final returnat de extractor | Rezultat observat |
| --- | --- | --- |
| `https://www.ecomputer.ro/` | `https://www.ecomputer.ro/cgi-sys/suspendedpage.cgi` | Titlu `Account Suspended`; mesajul de mai jos |
| `https://ecomputer.ro/cgi-sys/suspendedpage.cgi` | Același URL | Același titlu și mesaj |
| `http://ecomputer.ro/` | `http://ecomputer.ro/cgi-sys/suspendedpage.cgi` | Același titlu și mesaj |

Textul comun observat:

> Account Suspended
>
> This Account has been suspended.
>
> Contact your hosting provider for more information.

Rezultatele sunt concordante cu observația inițială Operations pentru `https://ecomputer.ro/`, păstrată în [ecomputer-source-evidence.json](ecomputer-source-evidence.json). Nu a fost observat un catalog sau un flux de cumpărare prin aceste intrări.

Extractorul nu a returnat coduri HTTP, antete, detalii TLS sau întregul lanț de redirecționare. URL-ul final HTTP de mai sus este transcris ca rezultat al instrumentului; nu este un test complet al politicii HTTPS/HSTS. Nu am efectuat o verificare vizuală, Lighthouse sau test pe dispozitive mobile.

## Revizuirea auditului Web

Am citit [ecomputer-audit.md](ecomputer-audit.md), dovada sursă Operations și înregistrarea separată a limitării executorului.

- Concluzia principală este susținută de conținutul public, inclusiv prin verificarea QA separată a variantei `www` și a paginii de suspendare.
- Cele **7 priorități** sunt delimitate, au responsabili, impact, efort estimat, dependențe și criterii de acceptare. Ordinea P0 disponibilitate/cauză/continuitate înaintea auditului comercial este justificată de blocajul observat.
- Din dovada publică, raportul nu atribuie suspendarea neplății, unui atac, resurselor sau pierderii datelor. Linkul de contact nu este folosit drept dovadă a titularului contractului de hosting. Precizarea ulterioară a utilizatorului este separată mai jos de această observație publică.
- Platforma magazinului, stocul, prețurile, traficul și pierderile comerciale nu sunt inventate. Cerințele RAM/SSD, coș și ramburs sunt corect separate de funcționalități observate.
- Mobilul, accesibilitatea, viteza, SEO, produsele, coșul, checkoutul, administrarea, codul, baza de date și backupurile sunt marcate neverificate.
- Nu există propunere de achiziție, schimbare de platformă sau restaurare executată automat. Remedierea este condiționată de cauza confirmată, acces și aprobările aplicabile.
- Linkurile Markdown relative ale auditului au **0 destinații lipsă** la verificarea finală; am validat sintactic ambele fișiere JSON cu dovezi.

Fișierul [ecomputer-http-evidence.json](ecomputer-http-evidence.json) arată `Operation not permitted` pentru urllib în executor. Acesta este tratat corect drept limitare a mediului local, nu răspuns al site-ului și nu dovadă suplimentară de indisponibilitate.

## Limite și decizie

Observațiile reprezintă conținutul văzut de instrument la momentul capturii. Nu stabilesc durata incidentului, disponibilitatea din toate rețelele, cauza, starea contractului, proprietarul hostingului, integritatea datelor sau posibilitatea restaurării. Nu au fost testate pagini interne necunoscute ori operații administrative.

Nu există defecte blocante deschise în auditul delimitat. După remedierea autorizată trebuie reverificate conținutul magazinului și fluxurile reale disponibile, nu doar un cod HTTP de succes.

## Reverificare locală a integrării finale

Am revizuit ulterior versiunea integrată a auditului, [procedura de recuperare](ecomputer-recovery-runbook.md), [raportul Operations](OPERATIONS-WEB-001.md), inventarul CAPABILITIES, README și ops/backlog.json. Verdictul **accepted** se menține pentru documentele pregătite.

- Procedura descrie pași viitori și inspecții read-only; nu afirmă că hostingul, backupurile sau datele au fost accesate ori recuperate.
- Mesajul pentru suport este marcat **NETRIMIS**, iar contactarea este condiționată de autorizare. Identitatea furnizorului contractual rămâne neconfirmată.
- Costul remedierii este declarat necunoscut până la cauză și ofertă confirmate. Nu sunt pretinse plăți, comenzi, achiziții, restaurări, migrări, modificări DNS sau deploy-uri efectuate.
- WEB-001 este `done` cu rezultatul limitat explicit la auditul public. INC-001 și WEB-005 sunt `blocked` pentru lipsa accesului la hosting, respectiv a paginilor comerciale. Statusurile nu prezintă magazinul ca remediat.
- Toate cele **6 fișiere JSON** locale sunt valide sintactic; verificarea globală a linkurilor relative Markdown a găsit **0 destinații lipsă**.

Nu am repetat cererile de rețea sau testele neschimbate ale monitorului de buget pentru această reverificare documentară.

## Precizare ulterioară a utilizatorului

Operations a transmis precizarea utilizatorului: **perioada contractului de hosting s-a încheiat**. Aceasta este informație furnizată de utilizator și trebuie păstrată separat de dovada paginii publice. Notificarea exactă a furnizorului, starea fișierelor/bazei de date și existența ori retenția backupurilor nu au fost verificate prin acces autorizat. Captura publică stabilește mesajul afișat, fără să confirme singură expirarea contractului.

Întrebarea despre salvarea nameserverelor și recuperarea site-ului a fost ulterior înlocuită de decizia utilizatorului de a construi de la zero. Prezentul QA nu afirmă că nameserverele au fost inventariate, modificate sau că datele site-ului au fost recuperate.

## Direcția finală stabilită de utilizator

Instrucțiunea cea mai recentă este: **«Nu mai salvăm nimic, îl construim de la zero»**. Recuperarea și ghidurile aferente sunt **superseded**, fără alte recomandări sau acțiuni de recuperare. Auditul și capturile rămân dovezi istorice ale observațiilor publice, fără a condiționa construcția noului magazin de restabilirea celui vechi.

QA pentru noua aplicație va evalua livrabilul nou, într-un ciclu separat. Acest verdict nu acoperă viitoarea implementare sau lansare. DNS și producția rămân în afara acțiunilor executate aici.

**Realizat efectiv:** confirmare publică independentă pe trei URL-uri, dovadă JSON, revizuirea auditului și a documentelor, verificarea linkurilor și acest verdict istoric. **Urmează:** implementarea noului magazin de la zero, apoi QA al noii aplicații. **Cost:** nicio achiziție, modificare de abonament sau apel direct OpenAI API; costul monetar al sesiunii este necunoscut. **Aprobare necesară:** niciuna pentru închiderea acestui QA; lansarea și modificările DNS vor necesita aprobarea aplicabilă.
