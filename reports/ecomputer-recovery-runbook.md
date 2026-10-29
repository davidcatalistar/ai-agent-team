# ecomputer.ro — recuperare disponibilitate și reluare audit

**ANULAT / ISTORIC:** utilizatorul a precizat că vechiul contract de hosting s-a încheiat și a cerut explicit «Nu mai salvăm nimic, îl construim de la zero». Pașii de recuperare de mai jos nu mai reprezintă planul activ. Continuăm [MVP-ul nou](ecomputer-mvp-status.md), fără restaurarea sau modificarea vechiului site.

Data: 2026-10-29. Acțiunile de mai jos sunt pregătite; panoul de hosting, mesajele furnizorului și backupurile nu au fost accesate în această sesiune.

## Ce este confirmat

Citirea publică a https://ecomputer.ro/ a ajuns la https://ecomputer.ro/cgi-sys/suspendedpage.cgi și a afișat «Account Suspended», «This Account has been suspended. Contact your hosting provider for more information.» Dovada este în [ecomputer-source-evidence.json](ecomputer-source-evidence.json). Cauza suspendării și starea fișierelor/bazei de date rămân necunoscute.

Pagina conține linkul https://www.awebdesign.ro/contact. Acesta este un contact afișat de pagina publică; identitatea furnizorului contractual trebuie confirmată din cont/documente înaintea oricărei comunicări sau plăți.

## Pași în ordinea dependențelor

| Pas | Responsabil | Acțiune | Dovadă / condiție de ieșire |
| --- | --- | --- | --- |
| 1 | Proprietar cont hosting; Operations după acces autorizat | Consultă notificarea din contul oficial și motivul suspendării. Confirmă domeniul și furnizorul din contul existent | Motiv exact, dată, condiții de reactivare și acțiuni necesare, fără parole/copii integrale de facturi în Git |
| 2 | Web + proprietar hosting | Inspectează numai în citire existența și datele backupurilor, configurația disponibilă și notificările/logurile relevante | Inventar al datelor recuperabile și procedură propusă. Nu efectua restore, ștergeri, schimbări DNS sau migrare |
| 3 | Operations + furnizor, numai dacă mesajul este autorizat | Pregătește rezolvarea cauzei confirmate și costul exact, dacă există | Acțiune concretă verificabilă pentru aprobare. Nu presupune neplată sau compromitere |
| 4 | Proprietar / administrator autorizat | Execută numai reactivarea sau remedierea aprobată | Confirmare din cont; fără achiziții implicite |
| 5 | QA | Reverifică răspunsul public HTTPS și destinația finală pentru domeniul principal și varianta www | Pagina dorită este disponibilă fără redirecționare spre suspendedpage; statusul HTTP se verifică unde instrumentul îl expune |
| 6 | Web + QA | Reia auditul homepage, categorii, produse, mobil și flux coș/checkout fără comandă reală | Dovezi pe paginile efectiv disponibile, backlog revizuit și teste marcate complet/limitat |

Nu recomandăm reconstruirea magazinului înainte de a afla ce cod, date și backupuri există și care este scopul comercial actual. Dacă site-ul afișează altceva în browserul proprietarului, comparăm URL-ul exact și ora înainte de a concluziona că problema este universală.

## Mesaj pregătit pentru suport — NETRIMIS

> Bună ziua. La verificarea publică din 29 octombrie 2026, accesarea https://ecomputer.ro/ redirecționează către /cgi-sys/suspendedpage.cgi și afișează «Account Suspended». Vă rog să confirmați motivul exact, data suspendării, starea datelor și a backupurilor existente, precum și pașii și eventualele costuri necesare pentru reactivare. Vă rog să nu ștergeți, restaurați sau migrați datele fără acordul proprietarului contului.

Mesajul se trimite doar prin canalul oficial al contului confirmat, de către proprietar sau după autorizarea explicită a comunicării. Nu a fost contactat nimeni în această misiune.

## Cost și intervenție necesară

Achiziții și apeluri directe OpenAI API: niciunul. Costul sesiunii și orice eventual cost de hosting/remediere nu sunt vizibile și nu sunt estimate fără ofertă. Pentru diagnosticarea cauzei este indispensabil accesul autorizat la notificarea contului de hosting sau comunicarea motivului exact de către proprietar. Nu sunt necesare parole în conversație. Orice plată, restore, migrare sau publicare se pregătește întâi pentru aprobare.
