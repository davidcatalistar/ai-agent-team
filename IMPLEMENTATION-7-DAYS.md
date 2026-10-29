# Implementare în 7 zile

Ziua 1 = **29 octombrie 2026**. Datele sunt ținte de lucru, nu automatizări programate. Continuarea necesită o sesiune/executor activ; nu pretindem execuție între conversații. Costurile de mai jos sunt plafoane marginale opționale API, incluse în bugetul lunar, și rămân **0 EUR autorizat** până la aprobare.

| Zi / dată | Prioritate și responsabil | Acțiune concretă | Criteriu de finalizare | API brut maxim propus |
| --- | --- | --- | --- | ---: |
| 1 / 29 oct. | P0 Operations + Research + Data + QA | Verifică ofertele oficiale; livrează analiza, 8 profiluri, bugetul, backlogul și monitorul local în repository | Surse datate, calcule verificate, script testat, acces și necunoscute documentate | 0 EUR |
| 2 / 30 oct. | P0 Operations + Web + Business | Înregistrează factura abonamentului dacă este disponibilă; audit public ecomputer.ro și inventar repo/hosting/CMS; stabilește conversia comercială urmărită | Raport cu dovezi, maximum 10 probleme ordonate, acces separat confirmat pentru orice admin | ≤1 EUR |
| 3 / 31 oct. | P0 Web + Business + Content | Selectează tehnologia pe baza infrastructurii existente; scrie brief și criterii; începe o felie homepage–catalog–produs în repo separat autorizat | Specificație, date de test și previzualizare locală/mediu existent; fără a inventa stoc/prețuri | ≤2 EUR |
| 4 / 1 nov. | P0 Web + QA | Implementează vertical felia aleasă; după caz opțiuni RAM/SSD și coș; păstrează checkout ramburs în test | Un flux navigabil, patch și verificările relevante; dacă lipsesc date/acces, prototip static marcat explicit | ≤2 EUR |
| 5 / 2 nov. | P0 QA + Web | Verifică mobil, accesibilitate, validare, control admin și comenzi exclusiv de test unde există mediu; corectează defectele P0/P1 | Raport reproducibil, fără defecte critice nerezolvate în aria verificată; zonele netestate sunt marcate | ≤2 EUR |
| 6 / 3 nov. | P1 Automation + Data + Research | Selectează un proces repetitiv măsurat; automatizează raportul local de cost sau validarea catalogului; pilot API doar dacă aprobat | Dry-run, jurnal fără secrete, oprire la eroare, manual runbook; fără scheduler plătit nou | ≤2 EUR |
| 7 / 4 nov. | P0 Operations + QA | Recapitulează rezultate/costuri, compară modele pe sarcini acceptate, pregătește pachetul de livrare și backlogul următoarelor 14 zile | Raport cu KPI și dovezi, proiecție ≤100 EUR; propunere concretă de release numai dacă verificată | ≤1 EUR |
| **Total** | | | Pilot săptămânal inclus în anvelopa API de 40 EUR/lună | **≤10 EUR** |

Abonamentul se facturează conform ciclului existent; nu îl considerăm gratuit în această săptămână și nici nu îl achiziționăm automat. Costul marginal extern al lucrului inclus poate fi 0 EUR, dar consumă alocația contului. Ciclul de 7 zile traversează două luni; monitorul este lunar și trebuie actualizat la noiembrie. Pilotul are suplimentar plafon cumulat de 10 EUR pentru ambele luni.

## Ordinea executivă și dependențe

1. Finalizăm misiunea costuri/arhitectură și QA. Nu construim simultan un magazin înaintea brief-ului.
2. Auditul public poate continua fără admin. Lucrul asupra codului ecomputer.ro necesită repository-ul separat autorizat; lipsa lui nu blochează specificația și macheta locală.
3. Catalogul, prețurile, stocul și opțiunile RAM/SSD trebuie să provină din date confirmate. Până atunci folosim exemple clar marcate.
4. Nicio comandă, plată, campanie, migrare, modificare DNS sau lansare reală fără aprobarea necesară. Pregătim întâi rezultatul verificabil.
5. Pilotul API poate fi omis integral; fluxul interactiv prin capacitatea inclusă rămâne utilizabil. Nu condiționăm toate sarcinile de cumpărarea creditelor.

## Ce trebuie confirmat o singură dată când devine necesar

- Pentru încadrarea financiară reală: planul activ, suma brută și moneda facturii, alte abonamente AI și data reînnoirii. Nu sunt vizibile în această sesiune.
- Pentru API: aprobare explicită de cheltuială, acces prin mecanism securizat la proiect/billing și o cheie cu acces minim; fără chei trimise în conversație sau comise în Git.
- Pentru implementarea magazinului: repository-ul proiectului și accesul la un mediu de test, dacă acestea nu se pot descoperi prin instrumentele autorizate.

Nu solicităm parole și nu cerem reaprobare pentru operații deja autorizate. La acces lipsă documentăm blocajul și continuăm pașii independenți.

## Raport zilnic standard

```text
Realizat efectiv: <artefact / commit / dovezi>
Verificare: <comandă sau sursă; rezultat; limite>
Urmează: <un pas, un responsabil>
Cost: <real / estimat / necunoscut>; plafon rămas <dacă verificat>
Aprobare: <niciuna / acțiunea exactă, suma și motivul>
```

Revizuim săptămânal numărul de livrabile acceptate, costul pe livrabil, timpul de la ready la accepted, procentul acceptat la prima verificare și blocajele de acces. Ținte inițiale: 100% dintre taskurile declarate finalizate au dovezi, 0 depășiri de plafon și o singură implementare activă.
