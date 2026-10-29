# ecomputer.ro — MVP nou, numai laptopuri

**Reper actual:** continuăm Site-ul existent furnizat ulterior de utilizator: https://e-computer-mvp.wiggly-hare-3760.chatgpt.site/. Identitatea și verificările sunt în [ecomputer-mvp-status.md](ecomputer-mvp-status.md). Prototipul local menționat mai jos este o alternativă nepublicată, fără a înlocui Site-ul existent.

Data: **2026-10-29**. Scop actualizat după cererea explicită a utilizatorului: **construim repede de la zero**, apoi îmbunătățim incremental.

## Direcție și limite

Magazinul conține **exclusiv laptopuri**, în exact trei categorii: **SH, refurbished și noi**. Nu includem PC-uri, monitoare sau alte categorii. Contractul vechi de hosting este încheiat conform declarației utilizatorului; pagina publică de suspendare a fost observată separat. **Recuperarea vechiului site este abandonată la cererea sa** și nu blochează construcția nouă.

Web Architect implementează direct un MVP static în `/workspace/sites/ecomputer-rebuild`. Nu cerem catalogul real pentru a începe și nu solicităm parole. Folosim un catalog demonstrativ etichetat clar, fără a pretinde stocuri, prețuri ori compatibilități hardware comerciale confirmate.

## Livrabil imediat

- Homepage cu identitate ecomputer.ro și acces la cele trei categorii de laptopuri.
- Catalog cu **SH / refurbished / noi**, căutare, filtre, stare fără rezultate și resetare.
- Pagină produs, configurare RAM/SSD demonstrativă și preț actualizat coerent.
- Coș cu configurația aleasă, cantitate, eliminare și total corect.
- Checkout **ramburs DEMO**, cu validare și recapitulare; finalizarea afișează explicit o simulare.
- Interfață utilizabilă pe telefon și desktop, cu etichete accesibile și focus vizibil.

Nicio comandă reală, plată, email sau trimitere către terți. Testele folosesc date fictive. Nu colectăm date personale reale pentru demonstrație și nu includem administrare în producție.

## Acceptare QA în browser

1. Fluxul homepage → categorie → laptop → RAM/SSD → coș → checkout DEMO este navigabil fără erori blocante; cele trei categorii, căutarea și filtrele funcționează.
2. Opțiunile, prețurile demonstrative, cantitățile și totalurile sunt coerente; configurațiile distincte se disting în coș.
3. Datele invalide sunt respinse; confirmarea este numai de simulare, fără request de comandă reală. Marcajele DEMO sunt vizibile.
4. La aproximativ 360, 768 și 1440 px nu există overflow care împiedică utilizarea; controalele principale sunt accesibile cu tastatura. QA consemnează probele efectiv rulate și limitele lor.

## După MVP

Adăugăm incremental backend durabil, administrare autentificată, laptopuri/prețuri/stoc reale, reguli RAM/SSD confirmate și comenzi persistente. Identitatea comerciantului, condițiile de vânzare, livrarea, retururile, garanțiile și informarea privind datele personale rămân de confirmat înainte de lansare. Hostingul nou este de stabilit; **domeniul, DNS-ul și publicarea în producție se abordează după aprobarea release-ului concret**. Nu cumpărăm servicii.

## Responsabilități și cost

**Operations Architect** coordonează și acceptă; **Web Architect AI** implementează; **QA & Release Engineer** verifică independent versiunea fixată. Business Analyst, Content & Growth Specialist, Data & Finance Analyst, Research Analyst și Automation Engineer intervin numai pentru o nevoie concretă. O singură implementare activă.

Raportăm realizat, următorul pas, cost și aprobare necesară. Bugetul ecosistemului rămâne maximum **100 EUR/lună**; nu este autorizat niciun serviciu plătit nou. Costul monetar al platformei este necunoscut. Urmează previzualizarea MVP și QA; nicio aprobare suplimentară pentru brief sau lucrul local autorizat.
