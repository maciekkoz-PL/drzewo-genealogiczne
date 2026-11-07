"""Migracja etapu21 na scalonej bazie 8bea235. Uruchomić raz."""
from pathlib import Path
import copy, datetime, json, openpyxl, re

ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
D=str(HERE.relative_to(ROOT)); BOOK=ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
w=openpyxl.load_workbook(BOOK); now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
assert len(w.sheetnames)==24
assert not any(r[0]=='S267' for r in w['ZRODLA_I_SKANY'].values), 'Migracja już wykonana.'
def add(sn,values):
    s=w[sn];s.append(values)
    for c in s[s.max_row]:
        p=s.cell(s.max_row-1,c.column);c._style=copy.copy(p._style);c.alignment=copy.copy(p.alignment)
def row(sn,id):
    return next(r for r in w[sn] if r[0].value==id)
def edit(sn,id,col,value):row(sn,id)[col-1].value=value

sources=[
 ('S267','Przybyli do Łodzi, grupa III, 1936–1937: Stocka12 i Grabowa20','ODCZYT ORYGINAŁÓW',
  'P03?; P06?; P11?; C98–C101','AP w Łodzi / Szukaj w Archiwach','39/221/0/4.12/25443; obrazy26/116/119; nr530/2591/2656',
  'https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6209620','transkrypcja_25443.csv',
  'Kolumny nazwisk5–202; pełne wskazane wpisy. Czesław Stocka12 zgadza się adresem ze ślubem1936; brak DOB/rodziców. Agnieszka i Czesław Grabowa20 z ChrzypskaWielkiego bez identyfikacji z P06/P03. Bezimienny chłopiec nie został uznany za P11.'),
 ('S268','Przybyli do Łodzi, grupa III, dalsza księga1937','PRZEGLĄD KOLUMN / WYBRANE WPISY',
  'P03?; P04?; P11?','AP w Łodzi / Szukaj w Archiwach','39/221/0/4.12/25444; obrazy5–72',
  'https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6209621','III_1937_manifest.json',
  'Pełne wybrane obrazy11,24,40,43,44,53,60,64,68; inni Chmielewscy, także Chmielecki/Chmielowski. Brak identyfikacji P11. Obrazy1–4,73–74 nieodczytane; nie deklarować kompletnej jednostki.'),
 ('S269','Księga wydanych dowodów, grupa III,1936–1937, PTG86615','PRZEGLĄD KOLUMN / CZTERY PEŁNE WPISY',
  'P03?; P04?; P06?; P27?','AP w Łodzi / Skanoteka PTG','PTG4119/4120/86615; nazwiska002–185; pełne021/076/081/134',
  'https://skanoteka.genealodzy.pl/index.php?op=pg&id=4119&se=4120&sy=86615&plik=001.jpg','ptg86615_downloads.json',
  'Nie zaobserwowano Czesława/Janiny/Agnieszki Chmielewskich w odczytanych kolumnach. Julianna13II1897 z081 ma inną datę niż P27(09XI1907); bez innych danych nie wyklucza wszystkich rodzinnych powiązań. Wacław1IV1917 z076 nie jest dzieckiem małżeństwa1936. Katalog186skanów nie dowodzi kompletności historycznej księgi.'),
 ('S270','Dokładne teczki załączników meldunkowych1936: nr530,2591,2656','METADANE KATALOGU, BEZ ODCZYTU TECZEK',
  'C98; C99; C100; C101','AP w Łodzi / Szukaj w Archiwach','39/221/0/4.12/26200 (501–1000);26204 (2501–3100)',
  'https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/36520475','aneks_26200_26204.json',
  'Katalog podaje0skanów obu jednostek. Druga: https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/36520496 . Dopasowano rok/grupę/przedział, nie sprawdzono zachowania konkretnego załącznika ani jego treści. Bez korespondencji.'),
 ('S271','Kontrole geograficzne nowych meldunków: Łężce / Chrzypsko','DWIE KWERENDY WEB / GRANICE DOSTĘPU',
  'C98?; C99?; C100?','Wyszukiwarka internetowa','Dwie zapisane frazy; dwie próby otwarcia jednostek SwA',
  'https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/36520496','kwerendy_web_zapis.json',
  'Brak nowego rodzinnego identyfikatora. Bibliografia Czesława i Doroty oraz współcześni imiennicy nie zostali przypisani rodzinie. Ponowne otwarcie stron jednostek InternalError. Wcześniejsze niezapisane odpowiedzi narzędzia nie są policzone jako nowe udokumentowane wyniki.'),
 ('S272','Księga wydanych dowodów, grupa III,1938–1939, PTG86616','PRZEGLĄD KOLUMN NAZWISK I POCZĄTKÓW IMION',
  'P03?; P04?; P06?','AP w Łodzi / Skanoteka PTG','PTG4119/4120/86616; obrazy002–247',
  'https://skanoteka.genealodzy.pl/index.php?op=pg&id=4119&se=4120&sy=86616&plik=001.jpg','ptg86616_downloads.json',
  'Pobrano248JPEG; ręcznie odczytano kolumny002–247(w tym przekładkę135;136początek1939). Nie zaobserwowano Czesława/Janiny/Agnieszki Chmielewskich w tych kolumnach. Nie odczytano pełnych rubryk pozostałych osób ani obrazów001/248. Brak wpisu nie wyklucza rodziny.'),
 ('S273','Przybyli do Łodzi, grupa III,1938','PRZEGLĄD NAZWISK I WYBRANYCH WPISÓW',
  'P03?; P04?; P11?','AP w Łodzi / Szukaj w Archiwach','39/221/0/4.12/25445; obrazy5–137; wybrane pełne wpisy wCSV',
  'https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6209622','trafienia_25445.csv',
  'Kolumny nazwisk5–137,138pieczęć. Odczytano wskazane wCSVszczegóły17obrazów. Brak DOB/rodziców potrzebnych do identyfikacji P11. RomanCzesław133 nie utożsamiony zP12. Jan1763 i WłodzimierzJan1784 to narodziny pod innymi adresami, bez rodziców. Obrazy1–4,139nieodczytane; nie wykluczać wszystkich dzieci rodziny.')]
for id,title,typ,persons,inst,sig,url,fn,note in sources:
    add('ZRODLA_I_SKANY',[id,title,typ,now,persons,inst,sig,url,'ŚCISŁY ZAKRES W UWAGACH',f'{D}/zrodla/{fn}',note])

candidates=[
 ['C98','Czesław Chmielewski — meldunek Stocka12','3III1936; nr530; 1mężczyzna; bezDOB','Możliwy P03 zS001','Łódź, Stocka12','NOWY TROP — NIE SCALONO','Zgodne imię, nazwisko i adres dwa miesiące przed ślubem. Brak DOB, zawodu i rodziców; wcześniejsza miejscowość niepewna.','S267; S001; S270','Dane osobowe w załączniku nr530/1936 lub inny identyfikator; H049.',sources[0][6]],
 ['C99','Agnieszka Chmielewska — meldunek Grabowa20','17XI1936; nr2591; grupa2m+3k; bezwieku','Możliwa P06, matka Czesława','ChrzypskoWielkie → Łódź, Grabowa20','HIPOTEZA — BRAK POKREWIEŃSTWA','Zbieżne imię/nazwisko i geografia z C100. Liczba osób nie podaje ich imion ani relacji. Nie wyprowadzono składu rodziny z samej liczebności.','S267; S270','Nazwisko rodowe, data urodzenia i członkowie gospodarstwa; H050.',sources[0][6]],
 ['C100','Czesław Chmielewski — meldunek Grabowa20','20XI1936; nr2656; 1mężczyzna; pobyt uznano za czasowy','Możliwy C98/P03; nieudowodnione','Łężce / Chrzypsko → Łódź, Grabowa20','HIPOTEZA — NIE SCALONO','Zbieżność wcześniejszej gminy zC99 i możliwym odczytemC98. Bez DOB nie rozstrzyga tożsamości ani relacji zAgnieszką.','S267; S270','Załącznik nr2656/1936 lub dokument z DOB/rodzicami; H051.',sources[0][6]],
 ['C101','Chmielewski, chłopiec bez imienia — pod nr2656','20XI1936;1mężczyzna;odurodzenia;bezDOB','Potencjalny trop dziecka, nie ustalono rodziców ani P11','Łódź, Grabowa20','WPIS OSOBOWY — TOŻSAMOŚĆ NIEZNANA','Kolejność pod C100 i powtórzone nazwisko/adres nie stanowią zapisu ojcostwa. Nie nadano imienia; nie policzono jako znalezionego brata Bogusława.','S267; S270','Własny akt urodzenia / załącznik podający rodziców i imię.',sources[0][6]]]
for r in candidates:add('KANDYDACI_I_HOMONIMY',r)
for r in [
 ['H049','Czesław Stocka12 (C98) = P03','S253nr530 zgadza się adresem zS001 i poprzedza ślub1936. Brak DOB/rodziców.','26200, nr530/1936; najpierw dostępne inne rekordy z identyfikatorem.','OTWARTA — MOCNY TROP ADRESOWY, NIE POTWIERDZENIE'],
 ['H050','Agnieszka Grabowa20 (C99) = P06','S253nr2591:2m+3k,ChrzypskoWielkie; zgodne imię/nazwisko, brak wieku/nazwiska panieńskiego.','26204,nr2591/1936; imiona towarzyszy i dane osobowe.','OTWARTA — NIE WNIOSKOWAĆ SKŁADU RODZINY Z LICZBY OSÓB'],
 ['H051','Czesław Grabowa20 (C100) = C98/P03; kim jest C101?','S253nr2656:20XI1936,Łężce/Chrzypsko,Grabowa20; pod nim chłopiec od urodzenia bez imienia.','26204,nr2656/1936 lub akt dziecka z danymi rodziców.','OTWARTA — BEZIMIENNE DZIECKO NIE JEST JESZCZE P11']]:add('HIPOTEZY_OTWARTE',r)

logs=[
 ('Kontrola alfabetu meldunków i dowodów','Ch należy do grupy III, obok H,I,J,L,Ł.','Wcześniejszy negatywny wynik grupyI(C) nie wyklucza Chmielewskich.','S267; S269; Q99'),
 ('25443 — kolumny5–202','Nowe wpisy Stocka12 i Grabowa20; pełne26/116/119.','Pozostałe rubryki nie są w całości odczytane; obrazy1–4nieodczytane.','S267'),
 ('Stocka12, nr530,3III1936','Czesław pod adresem ślubuS001; C98/H049.','Brak DOB i rodziców; nie potwierdzono P03 ani dzieci.','S267; S001'),
 ('Grabowa20, nr2591 i2656','Agnieszka z grupą2m+3k, Czesław i bezimienny chłopiec; C99–C101.','Nie stwierdzono relacji ani tego, że chłopiec toP11.','S267'),
 ('Dokładne załączniki1936','26200obejmuje530;26204obejmuje2591/2656; katalog0skanów.','To wskazanie teczek, nie odczyt ich zawartości; bez kontaktów.','S270'),
 ('25444 — dalsza księga1937','Kolumny5–72 i wybrane pełne wpisy; brakP11.','Nieodczytane1–4,73–74; Chmielecki/Chmielowski osobno.','S268'),
 ('PTG86615 — dowody1936–1937','Kolumny002–185; cztery pełne wpisy; bez dodatkowego identyfikatora rodziny.','Nie twierdzić, że wszystkie historyczne karty zachowano i zindeksowano.','S269'),
 ('PTG86616 — dowody1938–1939','248pobranychJPEG; odczytane kolumny002–247; bez poszukiwanych imionChmielewskich.','Brak pełnego odczytu pozostałych rubryk i001/248; to nie248aktówrodzinnych.','S272'),
 ('25445 — przybyli1938','Kolumny5–137, techniczny138; szczegóły17obrazów wCSV.','Żaden odczytany wpis nie podaje rodziców pozwalających ustalić P11.','S273'),
 ('Dwie kontrole geograficzne i dostęp SwA','Brak rodzinnego łącznika; strony aneksów InternalError.','Ponowiona kontrola po utracie niezapisanych odpowiedzi; nie liczyć jako niezależnych dowodów.','S271'),
 ('Scalenie postępów równoległej sesji','Zachowano nowe daneTomasza i roboczą decyzjęRomanP12=C69 zmain8bea235.','Etap21nie rozstrzyga rodzicówRomana ani nie cofa zmian strony.','DECYZJA_ROMAN_P12_C69; REL-018'),
 ('Zapis etapu21','Nowe źródłaS253–S273, cztery osobne tropy i trzy hipotezy; bez nowej relacji w drzewie.','Publiczna kronika pozostaje dla potwierdzonych przełomów; poszukiwania P11 nadal otwarte.','S267–S273; H049–H051')]
for i,(scope,result,limit,src) in enumerate(logs,257):add('DZIENNIK_KWEREND',[f'L{i}',now,scope,result,limit,src])

add('KOREKTY_I_SPRZECZNOSCI',['Q99','NIEWŁAŚCIWA GRUPA LITEROWA','Ch ≠ grupaI(C) w tych rejestrach','GrupaIII faktycznie zawiera Chmielewskich; katalogPTG86615 jawnie wymieniaCh.','Potwierdzone odczytem oryginalnych nazwisk','S267; S269','Nie używać ujemnych wyników grupyI25435/25436 jako wykluczenia rodziny. T50skorygowane.',sources[0][6]])
add('KOREKTY_I_SPRZECZNOSCI',['Q100','WNIOSKOWANIE Z KOLEJNOŚCI','C101 podC100 nie dowodzi ojcostwa','Wpis nie podaje imienia ani rodziców dziecka; liczebnośćC99nie wymienia członków rodziny.','Pewny zakres odczytu, niepewne pokrewieństwo','S267','Nie tworzyć relacji rodzic–dziecko ani nie ogłaszać odnalezieniaP11 bez dodatkowego dokumentu.',sources[0][6]])

edit('ZADANIA_AGENTA','T50',5,'Właściwa grupaIII:25443(1936–1937),25444(1937),25445(1938); zakresy odczytane zapisano w etapie21. Następna25446(1939),SwA6209623 — jeszcze nieodczytana.')
edit('ZADANIA_AGENTA','T50',6,'SKORYGOWANE Q99 — wykonany wskazany zakres grupyIII; brak identyfikacjiP11')
edit('ZADANIA_AGENTA','T50',8,'Ch znajduje się w grupieIII. GrupaI(C) nie jest ujemną kwerendą Chmielewskich. Nie powtarzać odczytanych kolumn.')
edit('ZADANIA_AGENTA','T50',9,'S267; S268; S273; Q99; PLAN_KONTYNUACJI etapu21')
for r in [
 ['T55',1,'IDENTYFIKACJA C98','APŁ / publiczne dokumenty','Sprawdzić dodatkowy identyfikator Czesława Stocka12; wskazana teczka26200,nr530/1936.','AKTYWNY TROP;0SKANÓW ANEKSU','Agent','Bez wysyłania zapytań/wniosków; zgodność adresu to za mało do scalenia.','S267; S270; H049'],
 ['T56',1,'RODZINA / DZIECKO GRABOWA20','APŁ / publiczne dokumenty','C99/C100/C101: szukać nazwiska rodowegoAgnieszki, dat i rodziców chłopca;26204nr2591/2656.','OTWARTE;0SKANÓW ANEKSU','Agent','Nie przyjmować, że Agnieszka jest matką Czesława ani chłopiec bratemBogusława.','S267; S270; H050; H051'],
 ['T57',2,'KOLEJNY ROCZNIK','APŁ SwA6209623','Przybyli1939,grupaIII25446: pozyskać manifest i odczytać nazwiska/rodzinne adresy.','NIE ODCZYTANO W ETAPIE21','Agent','Wpierw kontrola nieodczytanych brzegów poprzednich ksiąg. KwerendyDO po1938nie powtarzać.','S273; zakres_odczytu.json']]:add('ZADANIA_AGENTA',r)
edit('HIPOTEZY_OTWARTE','H002',3,row('HIPOTEZY_OTWARTE','H002')[2].value+' Etap21: C98Stocka12 i klasterC99–C101Grabowa20; brak imieniaP11 i dowodu pokrewieństwa. Aneksy26200/26204mają0skanów; H049–H051otwarte.')
edit('HIPOTEZY_OTWARTE','H017',3,row('HIPOTEZY_OTWARTE','H017')[2].value+' Etap21: meldunekC98Stocka12 wzmacnia tropP03w1936, lecz bezDOB/rodziców nie jest nowym dowodem identyfikacji rodziców wS086.')
add('INSTRUKCJA_AGENTA',['G24','UZUPEŁNIENIE ETAP21 — WĄTEK P11',f'Czytaj {D}/STATUS.md i PLAN_KONTYNUACJI.md. Ch w grupieIII(Q99); noweC98–C101/H049–H051tylko tropy. Zachowano równoległe daneTomasza i decyzjęRomana; żadnych nowych pewnych relacji. Bez korespondencji.'])
w['START']['A2']=str(w['START']['A2'].value)+f' Uzupełnienie etap21: S267–S273; meldunkiStocka12/Grabowa20, cztery niescalone tropy i korektaCh=III. Plan: {D}/PLAN_KONTYNUACJI.md.'
w['ZRODLA_I_SKANY']['A2']='273 źródeł. Etap21:S267–S273; każdy nowy wpis określa dokładny poziom odczytu i ograniczenia. Bez nowego potwierdzonego pokrewieństwa.'

registered={r[1] for r in w['PLIKI_DOWODOWE'].values if isinstance(r[1],str)}
file_no=221
for f in sorted((HERE/'zrodla').rglob('*')):
    if not f.is_file():continue
    path=str(f.relative_to(ROOT))
    if path in registered:continue
    name=f.name
    source='S267–S273'
    if '1936_1937' in name or '25443' in name:source='S267'
    elif '1937' in name or '25444' in name:source='S268'
    elif '86615' in name:source='S269'
    elif 'aneks_' in name:source='S270'
    elif 'web_' in name:source='S271'
    elif '86616' in name:source='S272'
    elif '1938' in name or '25445' in name:source='S273'
    add('PLIKI_DOWODOWE',[f'F{file_no}',path,'SKAN / METADANE / POCHODNE KOLUMN',source,
        'Dokładny zakres w ZAKRES_ODCZYTU.md; hashe w manifeście etapu21.',
        'ZIPkolumn zawiera pochodne szareJPEG; nie zastępuje pełnych oryginałów. Brak nowego pewnego powiązania.'])
    file_no+=1
w.save(BOOK)
counts={sn:len([r for r in w[sn].values if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]) for sn in
 ['ZRODLA_I_SKANY','KANDYDACI_I_HOMONIMY','HIPOTEZY_OTWARTE','DZIENNIK_KWEREND','PLIKI_DOWODOWE','KOREKTY_I_SPRZECZNOSCI','ZADANIA_AGENTA']}
(HERE/'LICZNIKI.json').write_text(json.dumps(dict(at_utc=now,sheets=len(w.sheetnames),counts=counts),ensure_ascii=False,indent=2)+'\n')
print(counts)
