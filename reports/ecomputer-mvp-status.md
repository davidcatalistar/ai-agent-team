# ecomputer.ro — versiunea MVP de lucru

Data verificării: 29 octombrie 2026. Utilizatorul a cerut reconstrucția de la zero, exclusiv laptopuri în categoriile **SH, refurbished și noi**, cu prioritate pentru un MVP rapid și îmbunătățibil. Contractul vechi de hosting s-a încheiat conform utilizatorului; recuperarea vechiului site a fost anulată explicit.

## Versiunea selectată

Utilizatorul a furnizat https://e-computer-mvp.wiggly-hare-3760.chatgpt.site/. Instrumentele native Sites confirmă proiectul `appgprj_6ae311b325008191a8acf9ff7dbe82b3`, acces **public**, versiunea **2** și rolul curent **owner**. Aceasta este versiunea de continuat. Prototipul static local din `/workspace/sites/ecomputer-rebuild` rămâne o alternativă nepublicată; nu a fost folosit pentru a suprascrie acest Site.

## Realizat și verificat efectiv

- Pagina publică descrie un catalog demonstrativ de laptopuri second hand, refurbished și noi, cu comenzi de test, fără plată sau livrare.
- Endpointul public `/api/products` răspunde cu **4 produse demonstrative**: 1 SH, 1 refurbished și 2 noi, plus `is_demo: true`.
- Inspecția nativă D1 confirmă bindingul `DB` și existența tabelului `orders`. Nu au fost citite rânduri de comenzi sau date personale.
- Identitatea proiectului și cerințele sunt păstrate în [projects.json](../ops/projects.json), iar observațiile în [ecomputer-mvp-evidence.json](ecomputer-mvp-evidence.json).

Nu am creat, modificat sau republicat Site-ul furnizat în această verificare. Existența tabelului de comenzi nu dovedește funcționarea completă a checkoutului. Extragerea paginii a capturat textul inițial de încărcare; nu îl folosim pentru a declara catalogul defect. Filtrele, configuratorul RAM/SSD, coșul, checkoutul și mobilul rămân de verificat pe versiunea găzduită înainte de a le declara validate.

## Urmează

1. Folosim Site-ul existent și îi păstrăm identitatea și accesul; nu construim un al doilea Site în paralel.
2. Verificăm interactiv căutarea, cele trei categorii, RAM/SSD unde sunt implementate, coșul și o comandă exclusiv de test, fără date personale reale. Acest pas nu a fost executat în verificarea curentă.
3. Înlocuim exemplele cu produse, prețuri, stoc și reguli de upgrade confirmate înaintea lansării comerciale. Validăm accesul de administrare și gestionarea comenzilor, fără a le presupune funcționale dintr-un link `/admin`.
4. Pregătim separat condițiile comerciale, livrarea și conectarea ecomputer.ro. DNS-ul domeniului nu a fost schimbat; orice schimbare se pregătește pentru aprobare.

## Cost și aprobare

Nicio achiziție, modificare de abonament, comandă, plată, publicare nouă sau cerere directă OpenAI API în această verificare. Costul monetar al sesiunii și costurile contului/hostingului nu sunt vizibile; nu le declarăm zero. API suplimentar rămâne neactivat. Nu este necesară aprobare suplimentară pentru aceste citiri și documente; cheltuielile noi și modificările DNS/producție necesită aprobarea acțiunii concrete.
