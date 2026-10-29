# ecomputer.ro — conectare finalizată

MVP: https://e-computer-mvp.wiggly-hare-3760.chatgpt.site/. Domenii conectate: https://ecomputer.ro/ și https://www.ecomputer.ro/.

## Realizat efectiv

Am configurat în Cloudflare cele două A pentru domeniul principal, CNAME www către custom-domains.chatgpt.site și cele patru TXT de validare furnizate de Sites. A și CNAME sunt DNS only. Vechile A și AAAA ale domeniului principal au fost eliminate; nameserverele adi.ns.cloudflare.com și patrick.ns.cloudflare.com au fost păstrate.

Sites confirmă pentru AMBELE domenii: status active, provider active, SSL active. Proiectul și accesul public existent au fost păstrate. Nu am modificat codul magazinului și nu am plasat comenzi.

Înregistrările MX și textul SPF au fost confirmate prin citire publică. Înregistrările de email, DKIM și subdomeniile fără legătură cu site-ul nu au fost modificate în configurare; verificarea publică a conservării a acoperit numai MX și textul SPF. Nu s-au testat trimiterea sau primirea emailurilor, DKIM sau DMARC.

## Propagare și limitări

Actualizare la 29 octombrie 2026, 21:41 ora României: două surse independente afișează MVP-ul demonstrativ la https://www.ecomputer.ro/. Interogarea CNAME www returnează acum ținta corectă custom-domains.chatgpt.site. Domeniul principal a returnat încă pagina veche sau 404 în citirile publice; un resolver recursiv păstrează IPv6-ul vechi cu TTL descrescător. Starea autoritativă AAAA nu a fost interogată separat. Aceste observații sunt compatibile cu propagarea, dar nu dovedesc singure cauza tuturor răspunsurilor. Dovezi: [verificarea publicării](ecomputer-release-followup.json).

Observațiile inițiale de la conectare:

Unele răspunsuri DNS și verificarea HTTP au continuat să indice vechiul hosting din cache. O interogare publică a confirmat deja cele două A corecte și eliminarea AAAA vechi; toate cele patru TXT au fost confirmate public. Interogarea CNAME a mai returnat temporar ținta veche ecomputer.ro, în timp ce tabelul Cloudflare confirmă noua țintă salvată, iar Sites confirmă www activ cu SSL activ. Nu declarăm propagare universală sau un termen fix.

## Cost și aprobare

Automatizarea a folosit 191 pași la tariful verificat de 0,016 USD/pas: 3,056 USD, rotunjit 3,06 USD. Consumul a fost reconciliat cu o scădere agregată de credit de aceeași valoare; soldurile exacte sunt păstrate în arhiva privată și nu sunt publicate. Nu s-au cumpărat credite și auto-reload este neconfigurat. Consumul prepaid este consemnat separat de achiziții pentru a evita dubla numărare. Conversia în EUR și totalul lunar al facturilor nu sunt cunoscute.

Conectarea a fost autorizată explicit de utilizator. Nu mai este necesară nicio intervenție pentru configurația DNS salvată; cache-urile externe pot continua să se actualizeze. Auditul și îmbunătățirile magazinului sunt amânate conform cererii utilizatorului.

Dovezi: [execuție și status Sites](ecomputer-domain-execution-evidence.json), [costuri](ecomputer-domain-costs.json), [MX/SPF](ecomputer-email-dns-evidence.json). Valorile exacte sunt în [configurație](../ops/ecomputer-domain-connection.json).

Continuarea cu citiri și documentare nu a produs o scădere suplimentară observată a soldului TinyFish; tariful Fetch confirmat este 0 USD/URL. Nu au fost pornite automatizări plătite noi. Costul ChatGPT/Codex al sesiunii rămâne nevizibil.
