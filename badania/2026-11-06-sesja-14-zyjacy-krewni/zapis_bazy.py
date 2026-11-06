"""Jednorazowy zapis etapu 14 ze stanu 028e3b3. Bez scalania kandydatów."""
from pathlib import Path
from zoneinfo import ZoneInfo
import datetime, json, csv, openpyxl

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BASE = str(HERE.relative_to(ROOT))
w = openpyxl.load_workbook(ROOT / 'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
assert len(w.sheetnames) == 23
assert not any(r[0].value == 'S175' for r in w['ZRODLA_I_SKANY'])
now = datetime.datetime.now(ZoneInfo('Europe/Berlin')).isoformat(timespec='seconds')
def row(sheet, ident):
    return next(r for r in w[sheet] if r[0].value == ident)

w['RELACJE_ZRODLOWE'].append(['REL-015', 'Odpowiedź użytkownika 06.11.2026', 'P09',
 'Na pytanie, czy Tomasz miał żonę lub dzieci: „Nie wiemy na 100%, ale raczej nie.”',
 'Rodzinne przypuszczenie, nie dowód bezdzietności ani stanu cywilnego. Nie utworzono małżonki ani dziecka.'])
w['RELACJE_ZRODLOWE'].append(['REL-016', 'Wiadomość i odpowiedź użytkownika 06.11.2026', 'P10; C19',
 'Użytkownik: „Myślę że ten jeden policjant z Łodzi znaleziony to właśnie on”. Na pytanie o jednostkę, stopień i stanowisko: „Nie mamy o nim żadnych wiadomości niestety”.',
 'Ocena użytkownika wzmacnia priorytet tropu, ale nie dostarcza niezależnego identyfikatora. Nie jest rozpoznaniem na zdjęciu ani potwierdzeniem miejsca służby. Nie pytać ponownie o te same szczegóły bez nowego źródła.'])
r = row('RODZINA_Z_RELACJI', 'P09')
r[8].value += '; REL-015'
r[9].value += ' Według nowej odpowiedzi rodzina przypuszcza, że nie miał żony ani dzieci, lecz nie ma pewności. Brak potomstwa pozostaje niepotwierdzony (H034).'
r = row('RODZINA_Z_RELACJI', 'P10')
r[8].value = 'REL-003; REL-016; S034 (kandydat C19)'
r[9].value = 'Widziany w mundurze policjanta na pogrzebie Tomasza w 2001 r.; kontakt utracony. Użytkownik uważa C19 za prawdopodobną identyfikację, ale rodzina nie zna jego jednostki, stopnia ani stanowiska. Stan życia i miejsce zamieszkania w 2026 r. niepotwierdzone. Główny kierunek dalszych badań publicznych; bez wiadomości do osób i instytucji bez osobnej zgody.'
r = row('KANDYDACI_I_HOMONIMY', 'C19')
r[5].value = 'GŁÓWNY TROP — SŁUŻBA W 2010 POTWIERDZONA, TOŻSAMOŚĆ P10 I STAN ŻYCIA W 2026 NIE'
r[6].value = 'S034: mł. asp., kierownik referatu III wydziału dochodzeniowo-śledczego; kontekst I Komisariatu w Łodzi. REL-016: użytkownik przypuszcza, że to kuzyn; brak dodatkowych identyfikatorów.'
r[7].value = 'S034; S035; S175; REL-016'
r[8].value = 'Potrzebne rozpoznanie rodzinne z dodatkowym szczegółem albo dokument łączący z ojcem P11. Artykuł nie podaje DOB ani rodziców. Brak nowych wzmianek nie dowodzi zgonu; dostępność strony nie dowodzi, że osoba żyje. Bez kontaktowania komisariatu lub krewnych bez osobnej zgody.'
r = row('KANDYDACI_I_HOMONIMY', 'C20')
r[7].value += '; S179'
r[8].value += ' Dwie nowe odczytane publikacje z 2019 r. potwierdzają aktywność w Szkole Policji, nie pokrewieństwo i nie tożsamość z C19.'
r = row('KANDYDACI_I_HOMONIMY', 'C21')
r[8].value = 'Brak rodzinnego łącznika. Sama inna miejscowość nie jest definitywnym wykluczeniem (możliwa zmiana miejsca służby), lecz nie uzasadnia scalenia z C19/P10.'
r = row('HIPOTEZY_OTWARTE', 'H003')
r[2].value = 'REL-003 + S034: zgodne imię, nazwisko, Łódź i zawód. REL-016: użytkownik uważa, że to ta sama osoba, ale nie ma dodatkowych wiadomości. 44 zapytania etapu14 i Firecrawl nie przyniosły niezależnego rodzinnego identyfikatora.'
r[3].value = 'Nowe publiczne źródło biograficzne identyfikujące ojca lub rozpoznanie rodzinne oparte na dodatkowym szczególe. Nie ponawiać pytania o jednostkę/stopień; rodzina nie zna. Bez wysyłania wiadomości bez odrębnej zgody.'
r[4].value = 'GŁÓWNY TROP — TOŻSAMOŚĆ P10=C19 OTWARTA; OBECNY STAN ŻYCIA NIEPOTWIERDZONY'
w['HIPOTEZY_OTWARTE'].append(['H034', 'Czy Tomasz P09 miał żonę lub dzieci?',
 'REL-015: według rodziny raczej nie, ale bez pewności. Nie mamy dokumentu stanu cywilnego ani źródła wskazującego dziecko.',
 'Nowy dokument lub jednoznaczny przekaz rodzinny. Nie dopisywać potomstwa i nie uznawać bezdzietności za fakt; nie szukać ponownie znanego grobu.',
 'OTWARTA — RODZINNE PRZYPUSZCZENIE, NIŻSZY PRIORYTET NIŻ PIOTR'])
sources = [
 ('S175', 'Żyjący krewni linii ojca — zapytania i profil łódzkiego Piotra', 'KWERENDY PUBLICZNE; BRAK IDENTYFIKACJI RODZINNEJ', 'P10; P11; P31; P32; P12; P26; P27; P28; P29', 'Wyszukiwarka internetowa; Firecrawl; WP', '44 zapytania w 11 zestawach + 1 Firecrawl; ponowny odczyt S034', 'https://wiadomosci.wp.pl/zlodzieje-ukradli-mu-wozek-inwalidzki-6032729591685761a', 'web/kwerendy_i_odczyty.json', 'Artykuł 12.03.2010 potwierdza historyczną pracę funkcjonariusza C19, bez DOB i rodziców. Brak nowego potwierdzonego żyjącego krewnego. Część zapytań zawęża wcześniejsze tropy; nie są to niezależne dowody. Nie podążano za wynikami o przypadkowych sportowcach, uczniach, firmach ani bazach adresowych.'),
 ('S176', 'Tomaszów Lubelski — pełne indeksy małżeństw 1943 i 1944', 'ODCZYT OBRAZÓW SKOROWIDZÓW', 'P12; P26; P27', 'USC Tomaszów Lubelski / Fotolubgens', '1943:023–024.jpg,85 pozycji; 1944:033–034.jpg,114 pozycji; razem199, oboje małżonków', 'https://fotolubgens.lubgens.eu/galleries/USC_Tomaszow_Lub/Tomaszow_UMZ_1944/034.jpg', 'ponownie_uzyte_pliki.json', 'Nie znaleziono ślubu Romana, Sabiny ani Julianny Chmielewskich. Uzupełnia etap11, który nie przeczytał całych obu indeksów. Indeks1944 jest w033–034, nie w027–031 (tam akty). Nie jest to odczyt199pełnych aktów ani dowód bezżenności. Nowe033 nie pobierano: wykorzystano istniejącą kopię.'),
 ('S177', 'Tomaszów Lubelski — ślub 17/1943, kontrola niejasnej nazwy w indeksie', 'SKAN PIERWOTNY — KONTROLA ODCZYTU', 'P27? — brak związku', 'USC Tomaszów Lubelski / Fotolubgens', '005.jpg;17/1943;23.04.1943', 'https://fotolubgens.lubgens.eu/galleries/USC_Tomaszow_Lub/Tomaszow_UMZ_1943/005.jpg', 'tomaszow_1943_005.jpg', 'W indeksie słabo czytelne nazwisko Ireny. Oryginał: Jerzy Zygmunt Sasin i Irena Wiśniewska. Nie Chmielewska; nie nowa siostra Czesława. Bez nowego kandydata lub relacji.'),
 ('S178', 'Poznańska e-kartoteka — Sabina, sygn.14325 karta365', 'INDEKS + NIEUDANY DOSTĘP DO SKANU', 'P26? — NIEUTOŻSAMIONA', 'e-kartoteka / AP Poznań / Szukaj w Archiwach', 'Indeks Sabina Chmielewski karta365; URL obrazu w rejestrze', 'https://e-kartoteka.net/pl/search?signature=14325', 'poznan_sabina_365_odpowiedz.html', 'Indeks nie podaje dat i rodziców. Pozostałe Wincenty/Roman w tej samej sygnaturze nie stanowią jednej rodziny. URL obrazu zwrócił HTTP200, ale212bajtów HTML ochrony, nie obraz; brak odczytu karty i brak identyfikacji z Sabiną1917. Nie obchodzić ograniczeń dostępu.'),
 ('S179', 'Piotr Chmielewski — dwie oficjalne wzmianki Szkoły Policji w Katowicach 2019', 'PUBLICZNE KOMUNIKATY ZAWODOWE', 'C20', 'Szkoła Policji w Katowicach', '31.07.2019 odznaka;16.10.2019 medalion za wieloletnią pracę', 'https://spkatowice.policja.gov.pl/spk/aktualnosci/94351,Dzien-Edukacji-Narodowej-2019.html', 'web/kwerendy_i_odczyty.json', 'Obie publikacje odczytano; podinsp.Piotr Chmielewski, szkoła. Nie podają rodziców ani połączenia z rodziną Marysi. Nie nowa identyfikacja: C20 istniał już przed tym etapem. Drugi dokładny URL w raporcie/rejestrze.'),
 ('S180', 'Tomaszów Lubelski — granice publicznej bazy cmentarza parafialnego', 'ODCZYT WIZYTÓWKI; NIE SPIS POCHÓWKÓW', 'P28; P29', 'eCmentarze; Grobonet', 'Lwowska81b: brak inwentaryzacji; Grobonet403 w narzędziu', 'https://www.ecmentarze.pl/cmentarze/cmentarz-parafialny-tomaszow-lubelski-lwowska', 'web/kwerendy_i_odczyty.json', 'Wizytówka wyraźnie nie ma spisu zmarłych ani wpisów dodanych przez rodzinę. To nie negatywny wynik dla Emilii. Baza komunalna i cztery groby Józefa były już sprawdzone w S161 — nie powtarzano kwerend osób. Nie wysłano zapytania do kancelarii.')
]
for sid,title,typ,persons,inst,sig,url,path,limit in sources:
    w['ZRODLA_I_SKANY'].append([sid,title,typ,'2026-11-06',persons,inst,sig,url,'ODCZYTANO W PODANYM ZAKRESIE',BASE+'/zrodla/'+path,limit])
w['ZRODLA_I_SKANY']['A2'] = '180 źródeł. Etap14: żyjący krewni po ojcu; Piotr głównym tropem, bez nowej potwierdzonej identyfikacji rodzinnej.'
logs = [
 ('L145','Przegląd znanych najbliższych krewnych po ojcu i nowa odpowiedź o Tomaszu','P10 znany z relacji; P32 bez imienia. REL-015: Tomasz raczej bez żony/dzieci, ale niepewne.','Nie potwierdzono aktualnego stanu życia żadnej nowej osoby; nie przyjęto bezdzietności jako faktu.','REL-003; REL-013; REL-014; REL-015'),
 ('L146','44 zapytania web i1 Firecrawl o Piotra, Czesię, syna i potomków rodzeństwa','Brak nowego identyfikatora rodzinnego. Użytkownik uważa C19 za kuzyna; nie zna jednostki ani stopnia.','Nie utożsamiono autorów wiadomości policyjnych, funkcjonariusza SW, sportowców lub przypadkowych rodzin. Powtórzenia starego artykułu nie są nowym źródłem.','S175; REL-016'),
 ('L147','Pełny odczyt indeksu małżeństw Tomaszowa1943','85 pozycji, oboje małżonków, bez ślubu P12/P26/P27.','Nie85pełnych aktów. Wcześniej odczytano tylko początekC; teraz uzupełniono pozostałą część i panny.','S176'),
 ('L148','Lokalizacja i pełny odczyt indeksu małżeństw Tomaszowa1944','114 pozycji033–034.jpg, oboje małżonków, brak badanej trójki.','029–031 to akty103–114, nie indeks. Odczyt indeksu nie wyklucza ślubu poza Tomaszowem.','S176'),
 ('L149','Kontrola słabo czytelnego nazwiska Ireny w pozycji68 indeksu1943','Akt17/1943: Irena Wiśniewska/Jerzy Zygmunt Sasin; nie nazwisko Chmielewska.','Brak podstaw do tworzenia krewnej lub potomków tej pary w badanym drzewie.','S177'),
 ('L150','Sabina w poznańskiej kartotece14325/365; kontrola skanu','Odczyt indeksu, pobranie zwróciło212bajtów strony ochrony mimoHTTP200.','Nie odczytano karty i nie potwierdzono dat/rodziców. Alfabetyczne sąsiedztwo Wincentego/Romana nie dowodzi pokrewieństwa.','S178'),
 ('L151','Dwie dodatkowe publikacje służbowe C20 Katowice2019','Potwierdzają historyczną pracę C20 w szkole; brak rodziców.','Nie utożsamiono C20 zP10/C19. To nie aktualny dowód życia w2026.','S179'),
 ('L152','Kontrola zakresu cmentarza parafialnego TomaszówLwowska','Wizytówka bez spisu pochówków; Grobonet403 w narzędziu.','Nie uznano braku inwentaryzacji za brak grobu. Nie powtarzano osób zS161 i znanego grobu Tomasza.','S180')
]
for lid,scope,result,limit,src in logs: w['DZIENNIK_KWEREND'].append([lid,now,scope,result,limit,src])
files = [
 ('F117','web/kwerendy_i_odczyty.json','S175; S178; S179; S180','Dokładne zapytania i odpowiedzi; części wyników nie uznano za krewnych'),
 ('F118','piotr2010_wp.html','S034; S175','Kopia artykułu z2010, bez identyfikacji rodzinnej'),
 ('F119','tomaszow_1944_034.jpg','S176','Indeks1944 pozycje74–114 i koniec'),
 ('F120','ponownie_uzyte_pliki.json','S176','Ścieżki i SHA starych kopii023/024/033 użytych bez ponownego pobierania'),
 ('F121','tomaszow_1943_005.jpg','S177','Akt17/1943, IrenaWiśniewska/Sasin'),
 ('F122','poznan_sabina_365_odpowiedz.html','S178','HTML212bajtów zamiast skanu — zachowana nieudana próba'),
 ('F123','indeksy1943_44_pobrania.json','S176','Rejestr nowych029–031, które zawierają akty, nie indeks'),
 ('F124','pobrania_2.json','S176; S177','Skuteczne pobrania034/1944 i005/1943 zUA/Referer po pierwszym403')
]
for fid,path,src,note in files:
    w['PLIKI_DOWODOWE'].append([fid,BASE+'/zrodla/'+path,'KOPIA / REJESTR',src,note,'SHA256 w manifest_zrodel_sesji.json'])
w['ZADANIA_AGENTA'].append(['T39',1,'ŻYJĄCY KREWNI LINII OJCA','Źródła publiczne i przekaz rodzinny',
 'Priorytet P10/C19: nowy identyfikator rodzinny, potem P32 przez identyfikację matki; następnie potomkowie P12/P26/P27/P28.',
 'AKTYWNE — bez nowego potwierdzonego żyjącego krewnego w etapie14.', 'Agent',
 'Nie ponawiać44zapytań, indeksów1943/1944 ani pytań o Piotra (rodzina nie ma wiadomości). Tomasz raczej bez dzieci, niepewne. Bez kontaktów bez osobnej zgody.',
 'REL-015; REL-016; S175–S180; H002; H003; H028; H032; H033; H034'])

f = ROOT/'witryna/wiarygodnosc.json'
d = json.loads(f.read_text()); people = {p['id']:p for p in d['people']}
people['P09']['note'] += ' Według najnowszego rodzinnego wspomnienia raczej nie miał żony ani dzieci, ale nie ma co do tego pewności.'
people['P09']['source'].append('REL-015')
people['P10']['note'] += ' Według oceny przekazanej w tej rozmowie łódzki policjant opisany w2010r. jest głównym tropem. Rodzina nie zna jego jednostki ani stopnia. Aktualnego stanu życia i miejsca pobytu nie potwierdzono.'
people['P10']['source'] = ['REL-003','REL-016']
people['C19']['role'] = 'Główny trop dotyczący kuzyna Piotra'
people['C19']['note'] = 'Artykuł z12.03.2010 opisuje młodszego aspiranta Piotra Chmielewskiego, kierownika referatu III wydziału dochodzeniowo-śledczego, w kontekście I Komisariatu w Łodzi. Użytkownik przypuszcza, że to kuzyn Marysi. Artykuł nie podaje rodziców ani daty urodzenia; rodzina nie zna szczegółów jego służby. Tożsamość z kuzynem i aktualny stan życia pozostają niepotwierdzone.'
people['C19']['source'] = ['S034','REL-016']
people['C19']['missing'] = 'Dodatkowy identyfikator rodzinny lub źródło wskazujące ojca; sama zgodność nazwiska, miasta i zawodu nie rozstrzyga tożsamości.'
d['sources']['REL-003'] = {'title':'Przekaz rodzinny: kuzyn Piotr i pogrzeb Tomasza w2001r.','url':None}
d['sources']['REL-015'] = {'title':'Przekaz06.11.2026: niepewna informacja o braku żony i dzieci Tomasza','url':None}
d['sources']['REL-016'] = {'title':'Ocena rodziny06.11.2026: łódzki policjant głównym tropem, bez dodatkowych danych','url':None}

relation = next(x for x in d['relations'] if x['id']=='V048')
relation.update({'reason': 'Zgodne imię, nazwisko, Łódź i zawód. Użytkownik uważa tę identyfikację za główny trop (REL-016), ale nie zna dalszych szczegółów. Brak niezależnego rodzinnego identyfikatora.', 'missing': 'Dodatkowy szczegół rozpoznany przez rodzinę albo źródło wskazujące ojca; nie ustalono tożsamości z kuzynem ani aktualnego stanu życia.', 'sources': 'REL-003; REL-016; S034; S035'})
r = row('WIARYGODNOSC_RELACJI','V048')
for idx,key in [(5,'reason'),(6,'missing'),(7,'sources')]: r[idx].value = relation[key]
f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
for ident in ['P09','P10','C19']:
    r = row('WIARYGODNOSC_OSOB',ident); p=people[ident]
    r[6].value = '; '.join(p['source']); r[7].value = p['classificationReason']+' '+p['note']; r[8].value = p['missing']
for sn,file in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
    with (ROOT/'badania/2026-11-06-trzy-poziomy'/file).open('w',newline='') as out:
        csv.writer(out,lineterminator='\n').writerows([['' if v is None else v for v in r] for r in w[sn].values])
w.save(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
print('Zapisano etap14:180źródeł; REL-015/016; bez nowych osób i relacji, kronika bez nowego przełomu.')
