# QA documentar — statutul MVP ecomputer

Data: **29 octombrie 2026**. Verdict: **accepted pentru consistența documentelor și a dovezilor JSON**. Acest verdict nu acceptă funcționalitatea UI, configuratorul, coșul sau checkoutul ca testate.

## Aria verificată

Am citit [ecomputer-mvp-status.md](ecomputer-mvp-status.md), [ecomputer-mvp-evidence.json](ecomputer-mvp-evidence.json), [projects.json](../ops/projects.json) și stările relevante din backlog. Verificarea a fost locală, fără cereri de rețea, fără execuția testelor aplicației și fără modificări asupra Site-ului.

| Afirmație | Rezultat al controlului local |
| --- | --- |
| Proiectul selectat | ID identic în raport, evidence și projects: `appgprj_6ae311b325008191a8acf9ff7dbe82b3` |
| Versiunea de continuat | URL-ul public furnizat de utilizator, `https://e-computer-mvp.wiggly-hare-3760.chatgpt.site/`; corespunde dovezii după normalizarea slashului final |
| Metadate observate | Versiune **2**, rol **owner**, acces **public**, consemnate coerent din inspecția nativă făcută de Operations |
| Catalog din dovada endpointului | **4 produse**, cu **4 ID-uri distincte** și `is_demo: true` |
| Distribuția categoriilor | **1** `Laptop second hand`, **1** `Laptop refurbished`, **2** `Laptop nou` |
| Bază de date | Dovada overview conține binding `DB`, tabel `orders` și `rows_read: false`; nu pretinde citirea ori crearea unei comenzi |
| Prototipul local | `/workspace/sites/ecomputer-rebuild` este marcat alternativă **nepublicată**, fără a înlocui Site-ul furnizat |
| Recuperarea vechiului site | Anulată conform utilizatorului; INC-001 are starea `superseded` |
| JSON și linkuri | Evidence, projects și backlog valide sintactic; **0 linkuri relative lipsă** în raportul de statut |

Raportul separă corect cele patru produse din versiunea găzduită de catalogul de șase exemple al prototipului alternativ. Metadatele sunt verificate aici prin confruntarea artefactelor Operations, fără o a doua inspecție a serviciului.

## Ce nu este validat

Textul inițial «Se încarcă produsele…» extras din homepage nu dovedește un defect de randare. Existența specificațiilor fixe RAM/SSD și a tabelului `orders` nu dovedește implementarea configuratorului sau funcționarea checkoutului.

Căutarea, filtrele/categoriile interactive, configurarea RAM/SSD, coșul, validarea, persistența, mobilul și o comandă exclusiv de test pe Site-ul găzduit rămân **pending**. Testele browser pentru prototipul local nu au fost finalizate și nu se transferă automat versiunii publice. Nu au fost accesate rânduri de comenzi sau date personale în această verificare și nu a fost plasată o comandă.

Nu există în documentele revizuite o afirmație că Site-ul a fost modificat, republicat, conectat la domeniul ecomputer.ro sau verificat pentru lansare comercială.

**Realizat efectiv:** control factual documentar, numărarea produselor/categoriilor din dovada JSON, verificarea identității proiectului și a linkurilor. **Urmează:** QA interactiv al versiunii găzduite și continuarea aceluiași proiect. **Cost:** nicio achiziție sau cerere directă OpenAI API; costul monetar al sesiunii este necunoscut. **Aprobare necesară:** niciuna pentru acest control local; cheltuielile noi și schimbările DNS/producție se tratează separat.
