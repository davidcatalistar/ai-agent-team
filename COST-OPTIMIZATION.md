# Arhitectura AI în maximum 100 EUR/lună

Verificat la **29 octombrie 2026**, din sursele oficiale enumerate mai jos. Prețurile publice USD nu reprezintă factura locală EUR/RON. Nu am acces la factura, planul activ, soldul sau limitele individuale ale contului.

## Decizia recomandată

**Un singur ChatGPT Plus, Codex inclus, 8 roluri reutilizabile la cerere și API opțional, limitat.** Începem prin capacitatea deja disponibilă. Nu cumpărăm câte un abonament pentru fiecare rol și nu menținem procese AI inactive în fundal. Un rol nu primește o cotă separată de cont.

Ținta normală de planificare este aproximativ **30–50 EUR/lună**, dacă factura abonamentului încape în 30 EUR și volumul API rămâne mic/moderat. Aceasta este o estimare, nu o promisiune de preț sau productivitate. Bugetul maxim rămâne 100 EUR; diferența nu trebuie consumată.

Până la aprobare: **0 EUR achiziții noi, API neactivat**. Utilizarea acestei sesiuni consumă capacitatea platformei; costul său monetar și tokenurile facturabile nu sunt vizibile aici. Nu am executat apeluri directe la OpenAI API și nu am cumpărat servicii.

## Plus, Pro, Codex și API

| Variantă | Preț public USD/lună | Ce oferă | Limite și implicație pentru acest proiect |
| --- | ---: | --- | --- |
| ChatGPT Plus | 20 | ChatGPT, reasoning, fișiere, analiză, Projects, tasks, custom GPTs și acces extins Work/Codex | Limite variabile; API facturat separat. Cea mai bună bază pentru lucru interactiv și programare moderată. [S1–S3] |
| Pro 100 | 100 | Funcții Pro, modele Pro, mai mult Work/Codex decât Plus | Nu are limită Codex de 5 ore conform documentației curente; există alte alocații/resetări. Prețul local brut și avantajul efectiv trebuie verificate; lasă prea puțină marjă pentru arhitectura mixtă. [S2–S3] |
| Pro 200 | 200 | Mai multă utilizare decât Pro 100 | Nu îl includem într-un plan de 100 EUR. Alocația veche pentru abonați eligibili este tranzitorie până la 29 octombrie 2026; nu proiectăm pe baza ei. [S2] |
| Pro 500 | 500 | Cea mai mare alocație Pro, Ultrafast eligibil | Mult peste bugetul planificat. Ultrafast consumă alocația mult mai repede. [S2–S3] |
| Codex cu autentificare ChatGPT | Inclus în planul eligibil; supliment de bază 0 | Web, CLI, IDE și integrări cloud, în funcție de plan | Work și Codex împart utilizarea. Nu este un al doilea abonament obligatoriu. Mesajele locale, cloud și alte funcții eligibile pot concura pentru aceeași alocație. [S3] |
| Plus + credite Work/Codex | 20 + pachetul cumpărat | Continuare după consumarea alocației incluse | Pachetele, prețul și disponibilitatea variază după cont/regiune/plan; prețul EUR/credit nu a fost verificat. Nu sunt credite API. Fără auto-reload sau achiziție fără aprobare. [S4] |
| Codex cu API key / API direct | Fără abonament ChatGPT obligatoriu; consum variabil | CLI/SDK/IDE, fluxuri programate și integrări proprii | Facturare separată per token/instrument/stocare. Modul Codex API key nu include funcțiile cloud precum review GitHub. Necesită cheie, billing și executor verificate. [S3, S5–S6] |

Pro nu înseamnă cote nelimitate pentru orice model sau instrument. Disponibilitatea modelului, suprafața Chat vs Work/Codex, viteza și regiunea contează. Plus este descris oficial drept potrivit pentru câteva sesiuni concentrate de programare pe săptămână; nu presupunem suficientă capacitate pentru dezvoltare continuă grea.

### Limitele Codex curente: estimări, nu promisiuni

[S3] publică estimări de **mesaje locale pe 5 ore** pentru Plus:

| Model Work/Codex | Interval estimativ |
| --- | ---: |
| GPT-6 Luna | 350–3.000 |
| GPT-6.1 Terra | 35–285 |
| GPT-6.1 Sol | 15–160 |
| GPT-6 Astra | 5–45 |

Taskurile cloud pot consuma mai mult; se pot aplica limite săptămânale. Nu multiplicăm intervalele cu 8 agenți și nu convertim alocația în dolari folosind tarifele API. Limitele și resetările reale se verifică în dashboard și, în CLI, prin `/status`.

Folosim **Standard**. Fast consumă alocația inclusă de 2,5 ori mai repede, iar creditele cumpărate de 2 ori; Ultrafast eligibil consumă alocația de 8 ori, respectiv creditele de 6 ori. Aceste multiplicatoare nu garantează aceeași creștere a vitezei. Generarea imaginilor consumă alocația de aproximativ 3–5 ori mai repede în medie. [S3]

La credite Work/Codex, tarifele Standard publicate sunt, per 1M input/cached/output: Luna **2,5 / 0,25 / 12,5 credite**; Terra **25 / 1,25 / 125**; Sol **50 / 2,5 / 250**; Astra **250 / 25 / 1.250**. Nu există tarif separat de cache-write în Codex credit billing. Costul în bani depinde de oferta reală de credite a contului. [S3–S4]

## Tarife API și alegerea modelului

Tarife **Standard, USD/1 milion tokenuri**, confirmate în [S6]. ID-urile sunt API, distincte de numele afișate în interfață. Accesul concret al unei chei personale nu este verificat.

| Model API | Input obișnuit | Cached input | Cache-write 30 min | Cache-write 12 h | Output |
| --- | ---: | ---: | ---: | ---: | ---: |
| `gpt-6-luna` | 0,10 | 0,01 | 0,125 | 0,25 | 0,50 |
| `gpt-6.1-terra` | 1,00 | 0,05 | 1,25 | 2,50 | 5,00 |
| `gpt-6.1-sol` | 2,00 | 0,10 | 2,50 | 5,00 | 10,00 |
| `gpt-6-astra` | 10,00 | 1,00 | 12,50 | 25,00 | 50,00 |

Rutare: calcule și validări deterministe întâi; Luna pentru clasificare/extragere și rezumate; Terra pentru sarcini delimitate de catalog, conținut și implementări care trec verificările; Sol pentru programare complexă, arhitectură și QA dificil; Astra numai după justificarea costului. În Codex folosim modelul disponibil adecvat; o corecție care eșuează pe Terra se poate escalada la Sol. Un model ieftin care provoacă multă refacere nu este o economie. Rutarea API se proiectează pe Responses API și se verifică pe cheia autorizată înainte de utilizare.

### Costuri care nu trebuie omise

- Reasoning se facturează ca output chiar dacă nu este vizibil. `max_output_tokens` include reasoning și output vizibil. [S8]
- Caching este implicit pe modelele suportate. Inputul obișnuit, cached și cache-write sunt categorii exclusive; nu le adunăm pentru același token. Economiile din cache se măsoară, nu se presupun. [S7]
- Peste 272K input tokens, modelele recomandate pot avea multiplicatoare pentru întregul request; nu folosim astfel de contexte în fluxul economic. Verificăm pagina modelului înainte de extindere. [S16]
- Web search: **10 USD/1.000 apeluri + tokenurile conținutului** la tariful modelului. Containere 1 GB: **0,03 USD/sesiune de 20 minute**, cu reguli specifice pentru sesiunile eligibile facturate pe minut. File search: **2,50 USD/1.000 apeluri**, plus **0,10 USD/GB/zi** peste primul GB gratuit. [S6]
- Fast API este 2× Standard; Sol Ultrafast este 6×. Regional processing eligibil poate adăuga 10%. Nu includem imagini, voce, stocare persistentă plătită sau astfel de moduri în scenariul de bază. [S6]
- Fiecare subagent, pas de instrument și retry poate produce consum suplimentar. 1 task comercial nu echivalează cu 1 apel API.

Batch oferă 50% reducere față de sincron, cu fereastră de finalizare de 24 ore; îl rezervăm clasificărilor de catalog și evaluărilor neurgente. Rate limits sunt comune organizației/proiectului/modelului, nu noi pentru fiecare rol; RPM/TPM efective depind de tier și se verifică în cont. [S10–S11]

## Buget lunar și scenarii

| Anvelopă | Plafon brut de planificare EUR | Regula |
| --- | ---: | --- |
| Un abonament ChatGPT cu Codex | 30 | Înlocuim cu factura reală; nu cumpărăm un al doilea abonament |
| API | 40 | Opțional, activare numai după aprobare; țintă uzuală 0–20 |
| Alte servicii / credite Work-Codex | 10 | Opțional, aceeași anvelopă comună; fără achiziții implicite |
| Rezervă nealocată | 20 | Taxe/curs/întârzieri/variații; nu este o cheltuială |
| **Total** | **100** | Toate abonamentele AI existente trebuie incluse |

Bugetul disponibil API devine `max(0, 100 − abonamente brute reale − alte costuri brute − rezerva păstrată)`, limitat și de plafonul API aprobat. Dacă abonamentul depășește 30 EUR, reducem API/opționalele. Dacă există deja Pro sau alte abonamente care depășesc totalul, arhitectura nu este încadrată până la o schimbare aprobată; nu anulăm nimic automat.

OpenAI oferă facturare localizată: EUR în SEE și RON pentru România; prețul exact se verifică în checkout/factură. Creditele API se cumpără în USD. Nu am verificat cursul, TVA-ul aplicabil sau reducerile contului. [S13]

### Scenariu API lunar moderat, reproductibil

Estimăm conservator toate tokenurile input la cache-write de 30 minute, fără economii de reutilizare. Outputul presupus include reasoning. Context sub 272K, Standard, fără suprataxe regionale.

| Apeluri | Input/apel | Output/apel | Calcul USD | Cost USD |
| --- | ---: | ---: | --- | ---: |
| 1.000 Luna | 4.000 | 500 | 4M × 0,125 + 0,5M × 0,50 | 0,75 |
| 200 Terra | 12.000 | 2.000 | 2,4M × 1,25 + 0,4M × 5 | 5,00 |
| 40 Sol | 30.000 | 8.000 | 1,2M × 2,50 + 0,32M × 10 | 6,20 |
| 200 web searches | — | — | 200 × 0,01 | 2,00 |
| 1M tokenuri suplimentare căutare, Luna | — | — | 1M × 0,125 | 0,125 |
| 20 containere 1 GB / 20 min | — | — | 20 × 0,03 | 0,60 |
| **Total: 1.240 apeluri model + tools** | | | | **14,675 ≈ 14,68** |

Pentru sensibilitate folosim **exclusiv ca ipoteză de planificare** factorul `1,30 EUR pentru fiecare USD de consum`, care combină orientativ conversia, taxele și marja. Nu este un curs verificat și nu substituie factura. Pentru abonament folosim anvelopa de 30 EUR separat.

| Volum ilustrativ | Plus + API: cost API la factorul ipotetic | Total cu anvelopa abonamentului | Decizie |
| --- | ---: | ---: | --- |
| Mic: 0,1× scenariul, 124 apeluri model | 1,91 EUR | 31,91 EUR | API poate rămâne 0 dacă lucrul încape în capacitatea inclusă |
| Moderat: 1× scenariul | 19,08 EUR | 49,08 EUR | Arhitectura recomandată, cu marjă |
| Intens: 5× scenariul, 6.200 apeluri model | 95,39 EUR | 125,39 EUR | Depășește bugetul; limităm volumul, folosim Batch sau mutăm activități potrivite în capacitatea inclusă |

API fără Plus are în aceste exemple numai costul variabil și eventualele costuri de executor; poate fi mai ieftin pentru fluxuri strict programate. Nu oferă automat experiența ChatGPT, funcțiile cloud Codex sau un executor permanent gratuit. Plus fără API rămâne opțiunea inițială cea mai simplă pentru cereri interactive.

Plus + credite poate păstra instrumentele cloud după epuizarea alocației. Comparăm **oferta reală în EUR/credit × consumul măsurat** cu API și cu valoarea funcțiilor incluse. Pachetul nu poate fi estimat corect dintr-un tarif public universal inexistent în sursa curentă. Promoțiile API pentru abonamente eligibile nu sunt presupuse în buget până nu sunt confirmate în cont. [S4–S5]

### Când ar merita Pro?

Diferența publică USD față de Plus este 80 pentru Pro 100, 180 pentru Pro 200 și 480 pentru Pro 500, înainte de localizare/taxe. Dacă suplimentele lunare pentru același volum se apropie de diferență, comparăm factura locală și productivitatea măsurată. Acesta este doar un prag de examinare: alocațiile Pro nu au o conversie garantată în taskuri sau dolari API.

Pro 100 poate fi analizat numai dacă prețul local brut plus toate celelalte cheltuieli și rezerva necesară încap în 100 EUR. În prezent nu avem această dovadă. Pro 200/500 nu sunt variante propuse pentru acest plafon. Nu schimbăm abonamentul și nu consumăm bugetul maxim pentru o cotă mai mare neutilizată.

## Controlul cheltuielilor și al execuției

1. Înregistrăm factura brută și moneda fiecărui abonament, data reînnoirii, soldul/consumul observabil și accesul. Până atunci totalul real este **necunoscut**, nu zero.
2. `ops/budget.json` și `ops/cost-ledger.csv` sunt registrul local. `scripts/budget_report.py` separă valori reale/estimări și verifică planul. Nu rezervă costul apelurilor și nu este un gateway care blochează API.
3. După aprobarea unui pilot API, folosim un singur proiect dedicat, cheie cu acces minim și auto-reload oprit. Configurăm **Enforce a hard limit** la proiect și, dacă este potrivit, organizație; alerte la 50/75/90%. Nu folosim doar alerte drept plafon. Oprirea poate întârzia. [S9]
4. Exemplu propus pentru pilot: maximum **10 EUR brut în 7 zile**, inclus în plafonul lunar API. La factorul ipotetic 1,30, un hard limit de **6 USD** înseamnă 7,80 EUR estimați, păstrând diferența pentru variații. Ajustăm după taxe/curs reale înainte de configurare. Minimum prepaid este 5 USD; auto-reload este pornit implicit la setup și trebuie debifat înainte de confirmarea unei cumpărări aprobate. [S12]
5. Runnerul ulterior trebuie să estimeze și să rezerve atomic costul maxim înaintea fiecărui request, inclusiv output/reasoning, tools și retries, apoi să reconcilieze utilizarea. Niciun apel când rezervarea depășește aprobarea sau datele de tarif lipsesc. Acest runner **nu este implementat/activat** în prima misiune.
6. Maximum o implementare activă, QA independent, două cicluri de remediere; retry tehnic doar pentru erori temporare și cel mult două reluări, cu backoff/Retry-After. Nu reluăm pe billing, credit sau hard-limit. Nu dublăm retry-urile SDK + orchestrator.
7. Datele permanente rămân în fișiere; delegăm doar context relevant. Refolosim rezultate cercetate și cerem un format scurt. Nu activăm 8 roluri pentru o sarcină pe care o rezolvă unul.

Pentru controlul plafonului de numerar, cumpărarea de credite și consumarea lor nu se înregistrează de două ori. Registrul de costuri urmărește cheltuiala brută/factura; detaliile de tokenuri sunt analiză separată. Creditele API și Work pot expira după 12 luni și pot avea sold negativ în situații de concurență/întârziere; evităm stocarea de credit neutilizat. [S4, S12]

## Livrare și următorii 7 zile

Arhitectura completă, cele 8 profiluri, handoff-ul și KPI sunt în [ARCHITECTURE.md](ARCHITECTURE.md). Planul zilnic, proprietarii, costurile și criteriile sunt în [IMPLEMENTATION-7-DAYS.md](IMPLEMENTATION-7-DAYS.md). Ziua 1 produce documentele și monitorul local; nu reprezintă finalizarea implementării site-ului sau a unui sistem AI permanent.

Prima prioritate comercială este ecomputer.ro. Mai întâi audit și backlog; apoi o singură felie de prototip într-un repository de proiect autorizat. Verificarea și pregătirea lansării sunt distincte de lansarea în producție, care necesită aprobare.

## Surse oficiale și limitele verificării

Toate sursele de mai jos au fost consultate la **2026-10-29**. Disponibilitatea concretă în cont și prețul checkoutului nu au fost verificate. Unele URL-uri istorice redirecționează către documentația nouă; folosim destinațiile efective.

| ID | Sursă | Date folosite |
| --- | --- | --- |
| S1 | [What is ChatGPT Plus?](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus) | 20 USD/lună, limite variabile, API separat |
| S2 | [About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers) | 100/200/500 USD, alocații, Ultrafast, tranziția Pro 200 |
| S3 | [Work & Codex pricing](https://learn.chatgpt.com/docs/pricing) | Codex inclus, cote comune, mesaje estimate, credit rates și viteză; destinație actuală a developers.openai.com/codex/pricing |
| S4 | [Credits for personal plans](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-personal-plans) | Prețuri dependente de cont, funcții eligibile, expirare, reload și solduri |
| S5 | [Managing billing for ChatGPT and API](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) | Sisteme separate, posibile promoții eligibile, fără a presupune acces |
| S6 | [API pricing](https://developers.openai.com/api/docs/pricing) | Tokenuri, tools, Batch, viteze și suprataxe |
| S7 | [Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) | Cache-write distinct și neaditiv, multiplicatoare și măsurare |
| S8 | [Reasoning](https://developers.openai.com/api/docs/guides/reasoning) | Reasoning output facturabil și max_output_tokens |
| S9 | [Spend limits](https://developers.openai.com/api/docs/guides/spend-limits) și [Managing projects](https://help.openai.com/en/articles/9186755-managing-projects-in-the-api-platform) | Hard limit configurabil vs alertă, întârzieri |
| S10 | [Batch](https://developers.openai.com/api/docs/guides/batch) | Reducere 50%, fereastră 24 h |
| S11 | [Rate limits](https://developers.openai.com/api/docs/guides/rate-limits) | Cote organizație/proiect/model, diferite de buget |
| S12 | [Prepaid API billing](https://help.openai.com/en/articles/8264644-setting-up-and-managing-prepaid-api-billing) | Minimum 5 USD, auto-reload implicit, expirare, oprire întârziată |
| S13 | [Multi-currency billing](https://help.openai.com/en/articles/10421635-multicurrency-billing) | EUR/RON disponibile, API credits USD |
| S14 | [ChatGPT pricing](https://chatgpt.com/pricing/) | Funcții Plus/Pro și limite aplicabile |
| S15 | [GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [Terra](https://developers.openai.com/api/docs/models/gpt-6.1-terra), [Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol) | ID-uri și adecvarea modelelor |
| S16 | Aceleași pagini individuale din S15 | Condiții de context lung; reverificare înainte de folosire |

Următoarea verificare a tarifelor: înainte de prima achiziție/API plătit și la schimbarea modelelor; revizuire regulată săptămânală în perioada pilot.
