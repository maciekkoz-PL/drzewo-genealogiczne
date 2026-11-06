# UWAGA ETAP12/Q79: historyczny zapis odczytu33lat był błędny; poprawny35lat, DOB22.07.1897. Nie uruchamiać tej migracji ponownie.
"""Jednorazowy zapis etapu11; poprzedni stan zachowany w Git 890fb62."""
from pathlib import Path
from copy import copy
import openpyxl,json,hashlib,datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[2]
STAGE=Path(__file__).resolve().parent
SRC=STAGE/'zrodla'
book=ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
w=openpyxl.load_workbook(book)
stamp=datetime.datetime.now(ZoneInfo('Europe/Warsaw')).isoformat(timespec='seconds')
def add(sn,row):
 s=w[sn];assert not any(r[0].value==row[0] for r in s),row[0]
 n=s.max_row+1;s.append(row)
 for col in range(1,s.max_column+1):
  a=s.cell(n-1,col);b=s.cell(n,col)
  if a.has_style:b._style=copy(a._style)
  b.hyperlink=None
 if s.auto_filter.ref:s.auto_filter.ref=f'A{1 if sn.startswith("HIPOTEZY") or sn.startswith("WIARYGODNOSC") else 3}:{openpyxl.utils.get_column_letter(s.max_column)}{n}'
def cells(sn,id):return next(r for r in w[sn] if r[0].value==id)
urls={
 'S149':'https://geneteka.genealodzy.pl/api/getAct.php',
 'S150':'https://regestry.lubgens.eu/viewpage.php?page_id=1057',
 'S151':'https://fotolubgens.lubgens.eu/picture.php?/324070/category/5159',
 'S152':'https://fotolubgens.lubgens.eu/picture.php?/367562/category/5903',
 'S153':'https://fotolubgens.lubgens.eu/picture.php?/284676/category/4343',
 'S154':'https://www.szukajwarchiwach.gov.pl/skan/-/skan/17e25d9765aeca0d9d9f7753bf08b7f96c6c5ac8a9d5abedefdf01f97849b7a4',
 'S155':'https://www.szukajwarchiwach.gov.pl/skan/-/skan/bc1bf37adce9ee64959695a97549d6eda47d3a23b95713a346195cc9d1ea3a6b',
 'S156':'https://www.szukajwarchiwach.gov.pl/skan/-/skan/fcc8392d62f1057e144f39b7eb6b3d70c707ed5796577414d930c7ee325be06e',
 'S157':'https://www.pznlodz.pl/historia/',
 'S158':'https://www.cmentarzekomunalne.lodz.systkom.pl/mapa.html?gv=5709&cm=ZARZW',
 'S159':'https://fotolubgens.lubgens.eu/index.php?/category/4295',
 'S160':'https://www.locateancestors.com/chmielewski-born-in-1919/'}
sources=[
 ('S149','Geneteka — małżeństwa Julianny, Sabiny i Romana, 21 regionów','PUBLICZNE ODPOWIEDZI API','P12; P26; P27','PTG Geneteka','63 zapytania S1923/1933/1935–1970; kontrola110/1936','geneteka/queries.json','229 zwróconych wierszy, często imię w polu rodzica lub współmałżonka. Mazowieckie Julianna:56/50; próba strony2 dała7 duplikatów, podział lat nadal niepełny. Nie uznawać za pełną kwerendę wszystkich aktów ani brak małżeństw.'),
 ('S150','Lubgens — nowe poszukiwania małżeństw i rodziny Emilii','INDEKSY I ZAPYTANIA','P12; P26; P27; P28; P30','Lubgens','Tomaszów s192/s193/s194; wyszukiwarka regionalna','lubgens/queries.json','Małżeństwa Julianna/Julia, Sabina, Roman; urodzenie Emilii22/1904 i zgony Julii. Pokrycie Tomaszowa ma luki1924,1933–1938,1943–1944. Indeksy nie zastępują odczytówS151–S156.'),
 ('S151','Julianna Chmielewska i Kazimierz Kaczor — ślub29/1924 Wożuczyn','SKAN PIERWOTNY — WYKLUCZENIE','C63; P27','USC Rachanie / Fotolubgens','29/1924; plik044.jpg; Piwigo324070/5159','wozuczyn_original.jpg','05.07.1924. Panna21, urodzona Józefówka, rodziceJózef/KatarzynaChadaj. To nie JuliannaP27 urodzona1907 zWincentego/Agnieszki.'),
 ('S152','Julianna Janina Chmielewska i Kazimierz Biesaga — ślub12/1939 Hrubieszów','SKAN PIERWOTNY — WYKLUCZENIE','C64; P27','USC Hrubieszów / Fotolubgens','12/1939; M007.jpg; Piwigo367562/5903','hrubieszow_original.jpg','Panna31, urodzona Dąbrowa, rodziceWładysław/Nazarena (rodowe matki niepewne). Inna osoba niżP27. Nie przypisano jej tego małżeństwa.'),
 ('S153','Emilia Chmielewska i Józef Mandziuk — małżeństwo74/1932','SKAN PIERWOTNY','P28; P29; P05; P30','USC Tomaszów Lubelski / Fotolubgens','74/1932; 019.jpg; Piwigo284676/4343','emilia1932_original.jpg','22.11.1932, godz.15; napisano „na dniu dzisiejszym”. Emilia28, panna, Rachanie, rodzice zmarliWincenty/JuliaJabłońska. Józef33, kawaler, MajdanGórny, Bartłomiej/MariannaRaczkiewicz. Nie20XI: to dzień trzeciej zapowiedzi. Nie ustalono dzieci.'),
 ('S154','Emilia Chmielewska — urodzenie22/1904 z adnotacją zgonu','SKAN PIERWOTNY','P28; P05; P30','AP Zamość / parafia Rachanie','88/628/0/-/29; SwA10504033; obraz7/38,id58207095,k8','Emilia1904_7.jpg','Urodzenie13/26.01.1904 godz.5, Rachanie; akt7/20.02.1904. Wincenty32,młynarz; JuliaJabłońska26. Adnotacja:27.02.1979 TomaszówLubelski, zgon76/1979; samego aktu zgonu nie odczytano.'),
 ('S155','Wincenty Chmielewski i Julianna Bartecka z Jabłońskich — ślub72/1901','SKAN PIERWOTNY','P05; P30; C05','AP Zamość / parafia Tomaszów Lubelski','88/639/0/-/26; SwA10504978; obraz69/99,id59125153,k149/p132','1901_69.jpg','06/19.11.1901; Wincenty28,kawaler,Rachanie, Piotr/Julia; Julianna22,wdowaBartecka,Wieprzów,Maciej/KatarzynaJabłońscy. ZS072/S154/S156 ustala wcześniejszą żonę i rodzinę, bez wyznaczania dokładnychDOB rodziców.'),
 ('S156','Julianna Chmielewska z Jabłońskich — zgon16/1905 Rachanie','SKAN PIERWOTNY','P30; P05','AP Zamość / parafia Rachanie','88/628/0/-/30; SwA10503949; obraz33/40,id58208630,k59','Julia1905_33.jpg','Zgon23.02/08.03.1905 o6rano Rachanie, akt24.02/09.03.1905. Lat28, urodzonaWieprzów, Maciej/Katarzyna zRaińskich, pozostawiła owdowiałegoWincentego. To odpowiada wdowieństwu wS072 z25.06.1905. Wiek nie wyznaczaDOB.'),
 ('S157','Publiczne historie i wyszukiwanie PZN oraz archiwum Józefa Szczurka','KWERENDA NEGATYWNA W OZNACZONYM ZAKRESIE','P31','PZN Łódź; PZN; Józef Szczurek','historia i2wyszukiwarki; indeks565odnośników biografii;12miesięcy kalendarza','web/pzn_history.json','Nie znaleziono identyfikacji Czesławy. Brak wyniku w witrynach nie dowodzi braku członkostwa. Nie badano prywatnej kartoteki członków ani całego archiwumPochodni; nie kontaktowano się zPZN.'),
 ('S158','Łódzkie cmentarze komunalne — Czesława1999 i Julianna1981','PUBLICZNY REJESTR POCHÓWKÓW','C62; C65; P31; P27; P12','ZZM Łódź / Systkom; eCmentarze','C62:ZarzewXLV-1-19; C65:XXVIII-10-10','municipal/searches.json','Czesława03.10.1999 bezDOB; eCmentarze4762340 bez fotografii, dane partnerskieZZM. Nie dowodzi, że to ciociaCzesia, ani że była żonąRomana. Roman/Sabina bezwyniku w3komunalnych bazach; Julianna06.12.1981 bezDOB nie utożsamiona zP27.'),
 ('S159','Fotolubgens — katalogi i wybrane skorowidze Tomaszowa1933–1944','KATALOGI; ODCZYT CZĘŚCIOWY SKOROWIDZÓW','P12; P26; P27','Fotolubgens / USC Tomaszów Lubelski','11albumów1933–1938,1940–1944; 649metadane obrazów','piwigo_1944_api.html','Wzrokowo sprawdzono początkowe sekcje nazwisk panów młodychC w1933–1938 i1943, bezRomana; nie wszystkie panny młode i nie1944. Kopie/skany próbne służyły lokalizacji, nie oznaczają odczytu wszystkich aktów. Dokładny zakres wraporcie.'),
 ('S160','Poszukiwania internetowe dalszych losów rodzeństwa i cioci Czesi','KWERENDY I REJESTR DOSTĘPU','P12; P26; P27; P28; P29; P31','Wyszukiwarka internetowa; Firecrawl; źródła publiczne','12zestawów po4zapytania + Firecrawl; stan06.11.2026','web/query_1.json','Nie znaleziono udokumentowanych małżonkówP12/P26/P27 ani ich dzieci. Wykluczające odczytyS151/S152 i rodzinaEmilii zapisane oddzielnie. LocateAncestors429; stareFamilySearch404, nie interpretować jako brak osoby.'),
]
for sid,title,typ,persons,inst,sig,path,limit in sources:
 add('ZRODLA_I_SKANY',[sid,title,typ,'2026-11-06',persons,inst,sig,urls[sid],'ODCZYTANO OBRAZ' if typ.startswith('SKAN') else 'ODCZYTANO W PODANYM ZAKRESIE',str((SRC/path).relative_to(ROOT)),limit])
add('RELACJE_ZRODLOWE',['REL-013','Bezpośrednie wiadomości użytkownika06.11.2026','P31; P32; P12?','Marysia pamięta ciocię Czesię: Czesławę Chmielewską zŁodzi; była niewidoma, miałaby dziś około100lat; miała/lub ma syna, który według wspomnienia całe życie mieszkał wNiemczech. Użytkownik dopuszcza wykorzystanie wskazówki zdrowotnej wbadaniach.','Pokrewieństwo nieznane; żonaRomana to wyłącznie pytanie/hipoteza. Nie znamyDOB,zgonu,rodowego,imienia/ojca syna. Nie wnioskować, że syn urodził się wNiemczech. Wskazówka zdrowotna pozostaje wprywatnej dokumentacji.'])
people=[
 ('P28','Emilia Chmielewska, po ślubie Mandziuk','przyrodnia siostra Czesława po ojcu','26.01.1904 Rachanie; ślub22.11.1932; zm.27.02.1979 TomaszówLubelski (adnotacja)','Rachanie; okoliceTomaszowaLubelskiego','zmarła','córkaWincentegoP05 iJuliiP30; żonaJózefaP29','SKANY I PORÓWNANIE CZTERECH AKTÓW','S153; S154; S155; S156; S072; S071','Ma inną matkę niżCzesław. Datazgonu z adnotacji, nie odczytanego aktu76/1979. Dzieci nieustalone.',urls['S154']),
 ('P29','Józef Mandziuk','mąż przyrodniej siostry Czesława','33lata przy ślubie22.11.1932; dokładneDOBnieustalone','MajdanGórny; parafiaTomaszówLubelski','nie ustalono daty zgonu','mążEmiliiP28; synBartłomieja iMariannyRaczkiewicz','SKAN PIERWOTNY','S153','Wariant indeksuMańdziuk zachowano. Brak dowodu dzieci; nie łączyć z muzykiem lub innymiJózefami po nazwisku.',urls['S153']),
 ('P30','Julianna / Julia Jabłońska, wcześniej Bartecka, następnie Chmielewska','pierwsza udokumentowana żonaWincentego','ślub19.11.1901; zm.08.03.1905; wiek22/26/28waktach','Wieprzów; Rachanie','zmarła','żonaP05, matkaP28; C05jestaliasem','SKANY PIERWOTNE','S155; S154; S156; S072','Nie jest matkąCzesława. Wiek zmienny, nie wyprowadzono dokładnegoDOB. Zachowano wcześniejszą formęBartecka i rodoweJabłońska.',urls['S156']),
]
for row in people:add('RDZEN_RODZINY',list(row))
add('RODZINA_Z_RELACJI',['P31','Czesława Chmielewska — ciocia Czesia','zapamiętana ciocia; dokładne pokrewieństwo nieznane','około100lat w2026 według wspomnienia; brak dokładnych dat','Łódź','życie/zgon nieustalone','matkaP32; byćmożeżonaP12 — wyłącznieH028','BEZPOŚREDNI PRZEKAZ RODZINNY','REL-013','Nazwisko rodowe nieznane. Niewidzenie to wskazówka identyfikacyjna dozwolona przez użytkownika wbadaniach, nie dowód członkostwaPZN. Nie utożsamiono zC62.',None])
add('RODZINA_Z_RELACJI',['P32','Syn cioci Czesi — imię nieznane','synP31 z przekazu','daty nieznane','Niemcy (wspomnienie:całeżycie)','nieustalony','synP31; ojciec nieustalony','PRZEKAZ RODZINNY','REL-013','Nie przypisano nazwiskaChmielewski, Romana jako ojca ani niemieckiego miejsca urodzenia. Nie poszukiwano prywatnego adresu/telefonu.',None])
rels=[
 ('R036','P05','P28','ojciec–córka','26.01.1904','SKAN PIERWOTNY','S154; S153','Wincenty,młynarzRachanie, wymieniony wurodzeniuEmilii; porównanoS155/S072.',urls['S154']),
 ('R037','P30','P28','matka–córka','26.01.1904','SKAN PIERWOTNY','S154; S153','Julia zJabłońskich wymieniona wurodzeniu iślubieEmilii.',urls['S154']),
 ('R038','P03','P28','rodzeństwo przyrodnie po ojcu','urodzenia1904/1909','WNIOSEK Z AKTÓW PIERWOTNYCH','S154; S155; S156; S072; S071','Ten sam ojciecWincenty zRachań; pierwsza żonaJulia zmarła przed ślubem1905zAgnieszką. Odrębne matkiEmilii iCzesława. H017nadalosobno.',urls['S154']),
 ('R039','P28','P29','małżonkowie','22.11.1932','SKAN PIERWOTNY','S153; S154','Akt74/1932; Emilia28RachanieWincenty/JuliaJabłońska zgodna z22/1904. Nie20listopada.',urls['S153']),
 ('R040','P05','P30','małżonkowie','19.11.1901','SKAN PIERWOTNY I PORÓWNANIE','S155; S156; S154; S072','WincentyRachanie synPiotra/Julii; JuliawdowaBartecka zJabłońskich; zgonprzed kolejnym ślubem1905. C05→P30.',urls['S155']),
 ('R041','P31','P32','matka–syn','daty nieznane','RELACJA RODZINNA','REL-013','Bezpośrednie wspomnienie użytkownika. Nie ustala ojca ani miejsca urodzenia syna.',None),
]
for r in rels:add('RELACJE',list(r))
for cid,name,data,question,place,status,reason,refs,nextstep,url in [
 ('C62','Czesława Chmielewska — Zarzew1999','zm.03.10.1999; brakDOB; XLV-1-19','czyto ciociaCzesiaP31?','ŁódźZarzew','NIEUTOŻSAMIONA','Imię/nazwisko/miasto zgodne; brakrodziny,DOB,fotografii i wskazówki identyfikacyjnej.','S158; REL-013','Ustalić niezależny identyfikator; nie dopisywaćzgonuP31.',urls['S158']),
 ('C63','Julianna Chmielewska — Kaczor','ślub29/1924; 21lat; Józef/KatarzynaChadaj','małżeństwoP27?','Wożuczyn; Józefówka','WYKLUCZONA JAKO P27','Innirodzice i miejsceu rodzenia niżWincenty/AgnieszkaRogoźno.','S151; S148','Nie dodawaćKazimierzaKaczora jako mężaP27.',urls['S151']),
 ('C64','Julianna Janina Chmielewska — Biesaga','ślub12/1939; 31lat; Władysław/Nazarena','małżeństwoP27?','Hrubieszów; Dąbrowa','WYKLUCZONA JAKO P27','Innirodzice, mimo podobnego rocznika i imienia.','S152; S148','Nie dodawaćKazimierzaBiesagi jako mężaP27.',urls['S152']),
 ('C65','Julianna Chmielewska — Zarzew1981','zm.06.12.1981; brakDOB; XXVIII-10-10','czytoP27?','ŁódźZarzew','NIEUTOŻSAMIONA','Samo nazwisko iimię nie identyfikuje siostryCzesława.','S158; S148','PotrzebnyDOB/rodzice lub późniejszyakt; nie dopisywać datyP27.','https://www.cmentarzekomunalne.lodz.systkom.pl/mapa.html?gv=3341&cm=ZARZW'),
]:add('KANDYDACI_I_HOMONIMY',[cid,name,data,question,place,status,reason,refs,nextstep,url])
r=cells('KANDYDACI_I_HOMONIMY','C05');r[3].value='wcześniejsza żonaWincentegoP05 → P30';r[5].value='ROZSTRZYGNIĘTO: P30; C05 ZACHOWANY JAKO ALIAS';r[6].value='Odczytano ślub72/1901, urodzenieEmilii22/1904 i zgon16/1905; zgodnirodziceWincentego iRachanie oraz wdowieństwo przedS072.';r[7].value+='; S155; S154; S156; S072';r[8].value='Nie dublowaćP30. Dalsi krewni i dzieci z wcześniejszego małżeństwaBarteckiej nieustaleni.'
for pid,extra in [('P03','; przyrodnia siostraEmiliaP28 po ojcu'),('P05','; córkaEmiliaP28 z pierwszą żonąJuliąP30')]:
 r=cells('RDZEN_RODZINY',pid);r[6].value+=extra;r[8].value+='; S154; S155; S156'
for sid in ['S006','S072']:
 r=cells('ZRODLA_I_SKANY',sid);r[10].value+=' Etap11: wcześniejsza żona ustalona jakoP30 poS155/S156/S154; dawne „nieodczytany” zachowuje stan historyczny, nie aktualny.'
events=[
 ('E060','26.01.1904','P28; P05; P30','urodzenie','Emilia urodzonaRachanie godz.5, Wincenty32młynarz/JuliaJabłońska26.','S154','Rejestracja20.02.1904; woryginale także13I/7IIstarego stylu.'),
 ('E061','22.11.1932','P28; P29','małżeństwo','EmiliaChmielewska iJózefMandziuk zawarli ślub74/1932Tomaszów.','S153','Data20XI występuje przy zapowiedziach, nie ślubie.'),
 ('E062','27.02.1979','P28','zgon — adnotacja','Przy urodzeniuEmilii wpisano zgonTomaszówLubelski, akt76/1979.','S154','Odczytano adnotację; brak oryginalnego aktu zgonu76/1979.'),
 ('E063','19.11.1901','P05; P30','małżeństwo','WincentyChmielewski iJuliannaBartecka zJabłońskich, akt72/1901Tomaszów.','S155','06.11jul./19.11greg.; wieki28/22 zapisane, nie traktować jakoDOB.'),
 ('E064','08.03.1905','P30; P05','zgon','JuliannaChmielewska zJabłońskich zmarłaRachanie godz.6, lat28; pozostawiła wdowcaWincentego.','S156','23.02jul./08.03greg.; rejestracja09.03greg., akt16/1905.'),
]
for eid,date,persons,kind,text,sid,note in events:add('ZDARZENIA_I_FAKTY',[eid,date,persons,kind,text,'SKAN PIERWOTNY — ADNOTACJA' if eid=='E062' else 'SKAN PIERWOTNY',sid,urls[sid],note])
add('HIPOTEZY_OTWARTE',['H028','Czy ciociaCzesiaP31 jest żonąRomanaP12?','REL-013potwierdza pamięć cioci,Łódź i syna wNiemczech, nie małżeństwo. Brak nazwiskar odowego/dat.','Aktmałżeństwa lub niezależny przekaz/nekrolog wymieniający męża i identyfikatoryP12. Nie przypisywać synaRomanowi.','OTWARTA — PRIORYTET Z NAJNOWSZEJ RELACJI'])
add('HIPOTEZY_ROZSTRZYGNIETE',['H029','CzyEmilia1904/1932jestprzyrodniąsiostrąCzesława?','POTWIERDZONO — P28; mążP29JózefMandziuk','Porównanieurodzenia,ślubu, pierwszego ślubuWincentego i zgonuJulii; Rachanie, rodziceWincentego,chronologia i zawód. H017wciążosobna.','S154; S153; S155; S156; S072; S071','2026-11-06'])
add('HIPOTEZY_OTWARTE',['H030','CzyCzesława1999ZarzewC62to ciociaCzesiaP31?','Tylkozgodneimię,nazwiskoiŁódź; rejestryZZMbezDOB i fotografii.','Druginiezależnyidentyfikator lub rodzinne rozpoznanie; brakdowodu na małżeństwoRoman.','OTWARTA — SŁABY TROP, NIE UTOŻSAMIAĆ'])
for qid,problem,known,refs,guard in [
 ('Q75','WiekWincentego iJulii waktach1901/1904/1905 nie tworzy dokładnychDOB','ZachowanoWincenty28/32/33 iJulia22/26/28. Zbieżnościrodziców,miejscowości,małżeństw iwdowieństwa służąidentyfikacji; nie wyrównywano wieku.','S155; S154; S156; S072','Nie obliczać dokładnychdat urodzenia rodzicówEmilii.'),
 ('Q76','CiociaCzesia to nie dowiedziona żonaRomana ani CzesławaJankowskaP25','P31to inna osoba znowego wspomnienia. SynP32ma nieustalonego ojca,imię inazwisko.','REL-013; H028; H030','Nie mieszać zmatczyną prababciąP25 ani zpochówkiemC62.'),
 ('Q77','Geneteka07mz: licznik56, wierszy50; strona2 i podziałlat niepełne','Zachowano surowe odpowiedzi;7wierszy strony2 toduplikaty. Podział1923–30 daje32/7,1931–70 daje24/5 beznagłówkówXHR.','S149','Nie ogłaszać pełnego przeszukania56rekordów; kontrolę110/1936wykonano zpełnymi nagłówkami.'),
 ('Q78','22listopada1932to dzień ślubuEmilii;20XI to zapowiedź','Nagłówek22XI i „na dniu dzisiejszym”; trzyzapowiedzi6,13,20XI.','S153','Nie zamieniać ostatniej zapowiedzi na datęmałżeństwa.'),
]:add('KOREKTY_I_SPRZECZNOSCI',[qid,'GRANICA / ROZBIEŻNOŚĆ',problem,known,'ŹRÓDŁO I OGRANICZENIE JAWNE',refs,guard,urls.get(refs.split(';')[0])])
logs=[
 ('L122','MałżeństwaP12/P26/P27:63zapytaniaGeneteka21regionów, kontrola1936','229wierszy odpowiedzi; brakjednoznacznegomałżeństwatrójki; nowytropEmilia74/1932.','Nieduża liczba wyników nie oznacza pełnegopokrycia lat. MazowieckieJulianna niepełne.','S149'),
 ('L123','Lubgens:wyszukiwanieJulianna/Julia,Sabina,Roman; indeksyTomaszowa1920–1942','Zlokalizowano ślubydo porównania; luki pokrycia oraz odrębnaEmilia.','Sama zbieżnośćimienia/rodowego nieprzesądza rodziców.','S150'),
 ('L124','OryginałyWożuczyn29/1924 iHrubieszów12/1939','Obie Julianny wykluczone jakoP27: inni rodzice.','Garbów26/1932FamilySearch404nieodczytany, nie wykluczony.','S151; S152'),
 ('L125','Emilia22/1904 i74/1932;72/1901 i16/1905; porównanieS072/S071','PotwierdzonoP28przyrodniąsiostrę i małżeństwoP29; pierwszażonaWincentegoP30,C05alias.','Brakdzieci. ZgonEmilii tylkozadnotacji76/1979. Wiekirozbieżne; nie wyprowadzonoDOB.','S153; S154; S155; S156; S072; S071'),
 ('L126','NowyprzekazciociaCzesia zŁodzi,~100lat,niewidzenie,syn wNiemczech','REL-013;P31/P32;H028żonaRomanaotwarta.','Wskazówkazdrowotna użyta wyłączniebadawczo; nieupubliczniać. Nieustalonyojciec syna.','REL-013'),
 ('L127','PZNŁódźhistoria+wyszukiwarka,PZNwyszukiwarka,Szczurekbiografieindeks i12kalendarzy','Nie znalezionoidentyfikacjiCzesławy.','Nieprzeczytanowszystkich565biografii ani całejPochodni. Wyniknie wyklucza członkostwaPZN. Bezkontaktu.','S157'),
 ('L128','CmentarzekomunalneŁodzi:Szczecińska,Doły,Zarzew;Czesława,Roman,Sabina,Julianna','C62Czesława03.10.1999 iC65Julianna06.12.1981 obiebezDOB. C62potwierdzonyteżpartnerskąkopiąeCmentarze.','NiecałaŁódź; brakwynikunie wyklucza pochówku. C62/P31 iC65/P27 nieutożsamione.','S158'),
 ('L129','KatalogiPiwigo1933–38/1940–44 iwybranesekcjeCskorowidzów','BrakRomanaChmielewskiegowpoczątkowychsekcjachC1933–38/1943.','Nie wszystkiepannymłode i niepełny1944. Odczytpróbnychstron to niepełneprzejrzenie ksiąg.','S159'),
 ('L130','Szerokiezapytania imion/DOB,organizacjiniewidomych,CzesiaŁódź,Emilia/Józef','Nie znaleziono udokumentowanych dzieciP12/P26/P27/P28/P29.','Hom onimowie niepołączeni; wynikwyszukiwarki niejestdowodemnieistnienia. ExactURLizapytaniazapisane.','S160'),
]
for lid,scope,result,limit,refs in logs:add('DZIENNIK_KWEREND',[lid,stamp,scope,result,limit,refs])
for fid,sid,path,title in [('F96','S153','emilia1932_original.jpg','Pełny oryginalny74/1932'),('F97','S154','Emilia1904_7.jpg','Pełny22/1904 i adnotacja76/1979'),('F98','S155','1901_69.jpg','Pełny72/1901'),('F99','S156','Julia1905_33.jpg','Pełnyzgon16/1905'),('F100','S151','wozuczyn_original.jpg','WykluczonaJulianna29/1924'),('F101','S152','hrubieszow_original.jpg','WykluczonaJulianna12/1939'),('F102','S149; S150; S157; S158; S159; S160','jobs1.json.results.json','Pełnyrejestr pobrań, kwerend i proweniencji wtym katalogu')]:
 add('PLIKI_DOWODOWE',[fid,str((SRC/path).relative_to(ROOT)),'SKAN / ODPOWIEDZI ŹRÓDŁOWE',sid,title,'SHA256 wmanifest_zrodel_sesji.json'])
for tid,task,refs in [('T34','Ustalić małżeństwoRomana i nazwiskar odowe/dat yciociCzesi; syn wNiemczech bezimienia, ojciecnieustalony.','P12; P31; P32; H028; H030'),('T35','Późniejsze losySabiny/Julianny: brak dowiedzionychmężów idzieci; zachować wykluczeniaC63/C64 i lukipokrycia.','P26; P27; S149; S150; S159'),('T36','PotomstwoEmilii/JózefaMandziuków: metryki1932 i adnotacja1979 znane; szukać publicznych późniejszych źródeł.','P28; P29; S153; S154')]:
 add('ZADANIA_AGENTA',[tid,1,'RODZEŃSTWO CZESŁAWA — NOWY PRIORYTET','publiczne źródła',task,'AKTYWNE — bezkontaktuzosobami iinstytucjami','Agent','Dokumentowaćrodziców/dat y, nie łączyć posamymnazwisku.',refs])
w['RDZEN_RODZINY']['A2']='17rekordów rdzenia. P28Emilia to przyrodnia siostraCzesława, P29jej mąż, P30pierwszażonaWincentego. Całaprzypisana gałąź doBogusława nadalH017.'
w['ZRODLA_I_SKANY']['A2']='160źródeł. Etap11: potwierdzoneEmilia/Józef oraz wcześniejszażonaWincentego. Czesia/żonaRomanaH028 nadalotwarta.'
w['KANDYDACI_I_HOMONIMY']['A2']='65rekordów, wtym zachowanealiasyC05→P30,C02→P27,C04→P26. C62/C65nieutożsamieni; C63/C64wykluczone jakoP27.'
w['START']['A2']='Etap11: priorytet rodzeństwoCzesława, współmałżonkowie/dzieci. PotwierdzonoEmilięP28 iJózefaP29; ciociaCzesiaP31 oraz synP32 zREL-013, ojciecnieustalony. H017,H019,H028,H030otwarte. 23arkusze.'
add('DRZEWO_SCHEMAT',['Rodzeństwo przyrodnieCzesława','EmiliaP28 — JózefMandziukP29','WspólnyojciecWincentyP05; matkaJul iaP30','S154; S155; S156; S072; S153. Dzieci nieustalone.',None,None,None])
add('DRZEWO_SCHEMAT',['CiociaCzesia','P31 → synP32, Niemcy','Matka–syn zREL-013; mążCzesi nieustalony','RomanP12jako mąż tylkoH028. Nie przypisywaćsyn aRomanowi. Zdrowie wprywatnych notatkach.',None,None,None])
w.save(book)
manifest=[]
for p in sorted(SRC.rglob('*')):
 if p.is_file():
  b=p.read_bytes();manifest.append(dict(path=str(p.relative_to(ROOT)),size=len(b),sha256=hashlib.sha256(b).hexdigest()))
(STAGE/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('ZapisanoP28–P32,S149–S160,R036–R041,E060–E064,L122–L130,F96–F102,Q75–Q78,T34–T36; H028/H030otwarte,H029rozstrzygnięta.')
