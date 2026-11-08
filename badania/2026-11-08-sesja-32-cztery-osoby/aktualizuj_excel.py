"""Utrwalenie etapu32. Uruchamiać raz na bazie fce13f2; bez połączeń z siecią."""
from pathlib import Path
from copy import copy
import openpyxl,json,hashlib,datetime,re
R=Path(__file__).resolve().parents[2];D=Path(__file__).resolve().parent;Z=D/'zrodla';p=R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx';w=openpyxl.load_workbook(p);now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds');rel=lambda q:str(q.relative_to(R));edits=[]
def find(sn,id):
 rows=[r for r in w[sn].iter_rows() if r[0].value==id]
 assert len(rows)==1,(sn,id,len(rows));return rows[0]
def setv(sn,id,col,value):
 c=find(sn,id)[col-1];old=c.value
 if old!=value:edits.append({'sheet':sn,'id':id,'cell':c.coordinate,'before':old,'after':value});c.value=value

def add(sn,values):
 s=w[sn];assert not any(r[0].value==values[0]for r in s.iter_rows()),(sn,values[0]);n=s.max_row+1
 for j,v in enumerate(values,1):
  c=s.cell(n,j,v);prev=s.cell(n-1,j);c._style=copy(prev._style);c.alignment=copy(prev.alignment);c.number_format=prev.number_format
 s.row_dimensions[n].height=75 if sn not in ['PLIKI_DOWODOWE','INDEKS_MELDUNKOW'] else 60
 if s.auto_filter.ref:s.auto_filter.ref=f'A3:{openpyxl.utils.get_column_letter(s.max_column)}{n}'
assert not any(r[0].value=='S309'for r in w['ZRODLA_I_SKANY'].iter_rows()),'Etap32 już zapisany; nie dodawać drugi raz'
u='https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6209683';m=json.loads((Z/'25506_manifest.json').read_text());urls={x['pozycja']:x['src']for x in m['elementy']}
sources=[
['S309','Wyjazdy Łódź, grupaIII,1936–1937 — kompletny przegląd nazwisk','SKANY PIERWOTNE / ŚCISŁY ZAKRES',now,'P03? P11?; odrębne C107/C108','APŁ / Szukaj w Archiwach','39/221/0/4.12/25506;205obrazów;198z wpisami',u,'NAZWISKA5–103,105–203; WYBRANE PEŁNE WIERSZE',rel(Z/'25506_kolumny_nazwisk.zip'),'Pobrano205prawidłowychJPG, nazwiska198rozłożonychstron. Pełne rubryki tylko według zakresu. Brak nowej relacji. S310/S311 są wpisami tej samej księgi, nie trzema niezależnymi źródłami.'],
['S310','Czesław Chmielewski, Stocka12, zgłoszenie27VI1936','WPIS W S309 / SKAN PIERWOTNY',now,'C107; możliwy C98/P03','APŁ','39/221/0/4.12/25506, obraz82, str79,nr1823',urls[82],'ODCZYTANO PEŁNY WIERSZ I NAGŁÓWKI',rel(Z/'25506_082.jpg'),'Stocka12;1m; Poznańskie/ChrzypskoMałe;27VI1936 data otrzymaniazgłoszenia; uznano pob. za czasowy. BrakDOB/żony/rodziców. Mocne dopasowanie adresuC98/S001, nie dowód pokrewieństwa ani fizycznej podróży tego dnia.'],
['S311','Czesław Chmielewski, Żeromskiego67,21X1936','WPIS W S309 / SKAN PIERWOTNY',now,'C108 — nieutożsamiony','APŁ','39/221/0/4.12/25506, obraz138,str35,nr3154',urls[138],'ODCZYTANO PEŁNY WIERSZ',rel(Z/'25506_138.jpg'),'1m; następne miejsce b.a.; brakDOB i krewnych. Nie scalić z C98/C100/C107/P03 wyłącznie po imieniu/nazwisku i roku.'],
['S312','NKJP/Poliqarp — DziennikŁódzki, Tomasz/Piotr/Witold','NATYWNE ZAPYTANIA I KONTEKSTY PRASOWE',now,'P09/P10 — kwerenda; imiennicy','NKJP, korpusnkjp1800','Tomasz3;Piotr8(7artykułów);Witold0','https://nkjp.pl/poliqarp/','ODCZYTANO WSZYSTKIE11ZWROCONYCH KONTEKSTÓW',rel(Z/'nkjp_verified'),'TrzyTomasze: kinoTomi2001/2005 i pięciobój2004, po zgonieP09. Piotr to kolarz, bez rodzinnegołącznika. Korpus nie jest kompletemgazet/nekrologów. Błędy szerszychzapytan nie są zerami. URL kontekstu jest zależny odsesji; zachowano metadane artykułów.'],
['S313','Arolsen — pełne4773pozycje indeksu Chmielewski z wariantami','PUBLICZNY INDEKS; NIE4773SKANY',now,'P02/P03/P04/P11 — kwerenda','ArolsenArchives','BuildQueryGlobalForAngular;GetPersonList rowNum0,1000,2000,3000,4000','https://collections.arolsen-archives.org/en/search/','POBRANO4773/4773POZYCJE; FILTR DAT/MIEJSC/RODZICÓW',rel(Z/'arolsen/zakres.json'),'Brak zgodnego imienia iDOBBogusława. PięćdokumentówCzesława3VII1909 już wS075–S077. Counter jestlokalny dla strony; 4773nieoznacza odrębnychludzi. Odczyt nowych obrazów tylko S314/S315; nie brak osób wcałymarchiwum.'],
['S314','Jan Chmielewski — błędnyrok1943 w indeksie Arolsen','DWA OBRAZY PIERWOTNE + INDEKS',now,'Jan1903 — nie dziecko1943','ArolsenArchives','DocID70592196;StammrollePole,Nienhagen,wiersz40','https://collections.arolsen-archives.org/en/document/70592196','ODCZYTANO OBA POWIĄZANE OBRAZY',rel(Z/'arolsen_jan1943/Arolsen_D70592196_001.jpg'),'Indeks03/08/1943,Litzmannstadt. Oryginał8.3.03 oraz pobytod6.4.40: rok1903, nie1943. Brak rodziców irodzinnegołącznika. Q105.'],
['S315','Witold20IV1936Końskie — dwa wykazy Kempten/Durach','DWA SKANY PIERWOTNE TEJ SAMEJ PODSTAWY',now,'Witoldniezidentyfikowany; nieC11/P11','ArolsenArchives','DocID69969056(25II1948),69969547(27III1947)','https://collections.arolsen-archives.org/en/document/69969056','ODCZYTANO OBA OBRAZY',rel(Z/'arolsen_witold1936/Arolsen_D69969056.jpg'),'PodająKońskie, nie rodziców. Józef/Józefa w sąsiednichwierszach nie sąprzezto potwierdzonymirodzicami. ŹródłaArbeitsamtKempten, nie niezależneakty. Bez utożsamienia zWitoldemZarzew.'],
['S316','ArcinsysHessen —21wyników Chmielewski i kontrolowane warianty','NATYWNY KATALOG ARCHIWALNY',now,'Czesław1909 — kwerenda; brak identyfikatora','HessischesLandesarchiv / Arcinsys','21trafieńnazwiska;1–20 i21','https://arcinsys.hessen.de/arcinsys/einfachesuche.action','ODCZYTANO21OPISÓW; NIE CAŁE AKTA',rel(Z/'arcinsys/queries.json'),'Chmielowski/Chmiel*Czes*/FritzlarAusländer: jawnybraktrafień. Caßdorf iHomberg tylko pierwsze20, nie całość; Homberg/Ohm toinne miejsce. Nie odnaleziono rodziny.'],
['S317','ChrzypskoWielkie — zespół gminny92/60/0','METADANE KATALOGOWE, NIE EWIDENCJA OSÓB',now,'Trop geograficznyC107, nieidentyfikacjaP03','APwPoznaniu,OddziałwGnieźnie','92/60/0;1924–1954;0skanów','https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/22441','ODCZYTANO OPIS; SPISJEDNOSTEKPORTLETNIEDOSTĘPNY',rel(Z/'Chrzypsko_zespol_92_60.json'),'Opis wymienia84–85ewidencjaruchu1945–1947, nie potwierdza imiennego tomu1936.102na liście/101wopisie nie przesądza faktycznej zawartości. Bezskanów irodzinnegołącznika.']]
for s in sources:add('ZRODLA_I_SKANY',s)
# Correct duplicates and residual pre-merge references without deleting old IDs.
pdf='badania/2026-11-07-sesja-31-prasa-1976/zrodla/Dziennik_Popularny_1976_nr126.pdf'
setv('ZRODLA_I_SKANY','S041',9,'OCR I OBRAZ STR7 ODCZYTANE; PEŁNY PDF POZYSKANY WETAPIE31')
setv('ZRODLA_I_SKANY','S041',10,pdf)
setv('ZRODLA_I_SKANY','S041',11,find('ZRODLA_I_SKANY','S041')[10].value+' Etap32/Q104: S306 to ponowny odczyt tego samego źródła; lokalnyPDF z etapu31 jest dostępny. Brak nowej identyfikacjiP02.')
setv('ZRODLA_I_SKANY','S306',2,'ALIAS S041 — ponowny odczyt i lokalne pozyskanie PDF,3VI1976')
setv('ZRODLA_I_SKANY','S306',3,'DUPLIKAT BIBLIOGRAFICZNY S041 / KOPIA LOKALNA')
setv('ZRODLA_I_SKANY','S306',11,find('ZRODLA_I_SKANY','S306')[10].value+' Q104: ten sam numer/strona/ogłoszenie już wS041/C22/Q14/L13. Nie liczyć jako nowe lub niezależne odkrycie.')
setv('DZIENNIK_KWEREND','L307',5,find('DZIENNIK_KWEREND','L307')[4].value+' Etap32/Q104: ponowny odczytS041 i uzyskanie lokalnegoPDF, nie noweogłoszenie.')
setv('PLIKI_DOWODOWE','F440',4,'S041;S306(ALIAS);L307;Q104')
setv('ZRODLA_I_SKANY','S307',9,'OPIS ZESPOŁU + KOMPLETNY MANIFEST283SKANÓW; SPISY8–199NIEODCZYTANE')
setv('ZRODLA_I_SKANY','S307',10,rel(Z/'referendum_1946_manifest.json'))
setv('ZRODLA_I_SKANY','S307',11,find('ZRODLA_I_SKANY','S307')[10].value+' Etap32: wszystkie283publiczne obrazy mają sygnaturę39/639/0/-/1 Sprawyorganizacyjne; żaden niejest skanemspisów8–199. Nie wyciągać wniosku o nieobecności rodziny.')
# S238 remains the same legal source; new access/reading is a log, not a new S-ID.
setv('ZRODLA_I_SKANY','S238',2,'MSW2015poz14 — tekstowy odczyt pozycji748, Piotr synJózefa')
setv('ZRODLA_I_SKANY','S238',3,'URZĘDOWY DOKUMENT / ODCZYT TEKSTOWY, BEZ BINARNEGO PDF')
setv('ZRODLA_I_SKANY','S238',8,'https://e-dziennik.msw.gov.pl/DUM_MSW/2015/14/oryginal/akt.pdf')
setv('ZRODLA_I_SKANY','S238',9,'ETAP32: TEKST POZ748 I NAGŁÓWEK; NIE ODCZYT WSZYSTKICH45STRON')
setv('ZRODLA_I_SKANY','S238',10,rel(Z/'MSW2015_14_odczyt_Firecrawl.md'))
setv('ZRODLA_I_SKANY','S238',11,'Etap20:pozycjaPiotra nieodczytana,503/502. Etap32:Firecrawl odczytał45stronicowy dokumentdo kopii tekstowej; sprawdzono poz748:CHMIELEWSKIPiotr,s.Józefa, wczęścibrązowejodznaki ochronyprzeciwpożarowej. BrakDOB,jednostki,Łodzi irodzinnegołącznika. Nie jest ustalonymP10/C19; Józef nie jest ustalonymP11. Lokalnego binarnegoPDF nieuzyskano; numer fizycznej strony niepotwierdzony.')
for id in ['H049','H050','H051']:
 setv('HIPOTEZY_OTWARTE',id,3,find('HIPOTEZY_OTWARTE',id)[2].value.replace('S253nr','S267nr'))
setv('HIPOTEZY_OTWARTE','H049',3,find('HIPOTEZY_OTWARTE','H049')[2].value+' Etap32:S310/C107,nr1823,27VI1936,Stocka12→ChrzypskoMałe;1m;dopisekczasowości. Zgodnyadres/przedział,brakDOB/rodziny; mocniejsze dopasowanie,niezamknięciehipotezy.')
setv('HIPOTEZY_OTWARTE','H051',3,find('HIPOTEZY_OTWARTE','H051')[2].value+' S310dodajeC107/Stocka12iChrzypskoMałe,27VI1936. Zbieżnyregion nieustala tożsamościC100/C98ani rodzicówC101.')
setv('HIPOTEZY_OTWARTE','H003',3,find('HIPOTEZY_OTWARTE','H003')[2].value+' Etap32:S238odczytpoz748Piotr,s.Józefa; brakDOB,jednostki,Łodzi iłącznikazC19. ImieniaJózefnieprzyjęto dlaP11.')
setv('HIPOTEZY_OTWARTE','H002',3,find('HIPOTEZY_OTWARTE','H002')[2].value+' Etap32:C107/S310potwierdza wpisCzesławaStocka12,nieimiębrata; C108osobny. IndeksArolsen4773iNKJPbeznowejrelacji.')
setv('KANDYDACI_I_HOMONIMY','C98',8,find('KANDYDACI_I_HOMONIMY','C98')[7].value+';S310;C107')
setv('KANDYDACI_I_HOMONIMY','C98',7,find('KANDYDACI_I_HOMONIMY','C98')[6].value+' Etap32:C107ma ten samadresStocka12iimię,27VI1936,ChrzypskoMałe. BrakDOB/rodziny; możliwetożsamość,bezscalenia.')
add('KANDYDACI_I_HOMONIMY',['C107','CzesławChmielewski — Stocka12, wyjazdy1936','nr1823;27VI1936;obraz82,str79;1m;bezDOB','MożliwyC98/P03;nieutożsamiony','Stocka12→Poznańskie/ChrzypskoMałe','MOCNY TROP ADRESOWY; BRAK NOWEJ RELACJI','Adres iimię odpowiadająC98iS001; dopisekuznania pobytuzaczasowy. NiepodajeJaniny/dzieci/rodziców.','S309;S310;S267;S001','DokumentzDOB/rodzicami lub żoną;H049/H051.',urls[82]])
add('KANDYDACI_I_HOMONIMY',['C108','CzesławChmielewski — Żeromskiego67,1936','nr3154;21X1936;obraz138,str35;1m;bezDOB','Nieutożsamiony zP03/C98/C100/C107','Łódź,Żeromskiego67; następne miejsceb.a.','OSOBNY WPIS — TOŻSAMOŚĆ OTWARTA','Ta samaksięga/imię/nazwisko nieustala tożsamości; bezwieku irodziny.','S309;S311','Indywidualnakarta lubakt rodzinnyzidentyfikatorami.',urls[138]])
for id,src,n,nr,text in [('IM059','S310',82,'1823','Czesław Chmielewski;Stocka12;Poznańskie/ChrzypskoMałe;27VI1936,dataotrzymaniazgłoszenia;1m;uznanopob.zaczasowy.BrakDOB/rodziny.C107/H049.'),('IM060','S311',138,'3154','CzesławChmielewski;Żeromskiego67;b.a.;21X1936;1m;bezDOB/rodziny.C108,bezutożsamieniazP03.'),('IM061','S309',110,'2492','CzesławaChmielewska;Włodzimierska17→Łódź/Szczawin;20VIII1936;1k;bezDOB.NieidentyfikujeP31/Czesi.'),('IM062','S309',178,'201','JaninaSylwiaChmielińska;Pomorska50→Toruń;22I1937;1k.InnenazwiskoniżP04.')]:
 add('INDEKS_MELDUNKOW',[id,src,'39/221/0/4.12/25506',n,nr,text,urls[n],rel(Z/'25506_wybrane_odczyty.csv')])
for values in [
['Q104','DUPLIKAT ŹRÓDŁA','S306/etap31 ogłoszenieUŁ1976nazwano nowym','Ten sam dokument był jużS041/C22/Q14/L13. Etap31pozyskał lokalnyPDF i ponownie odczytałstr7. ZachowanoS306jakoalias.','PEWNE — IDENTYCZNY URL/NUMER/OGŁOSZENIE','S041;S306;L307','Nie liczyćponownie; S041uaktualniono okopię. TożsamośćP02niepotwierdzona.',find('ZRODLA_I_SKANY','S041')[7].value],
['Q105','BŁĄD PUBLICZNEGO INDEKSU AROLSEN','DocID70592196 podaje wAPI03/08/1943','Skanwiersz40:8.3.03,Litzmannstadt,pobytod6.4.40. Rok1903,nie1943.','WYSOKA — ODCZYT ORYGINAŁU I CHRONOLOGIA','S313;S314','Nie szukać tegoJana jako dziecka1943; przechowaćrównież błędnyindeks.','https://collections.arolsen-archives.org/en/document/70592196'],
['Q106','NAPRAWA ODESŁAŃ PO SCALENIU','H049/H050/H051 cytowały staryS253','Po scaleniu etapu21 meldunki25443sąS267; obecnyS253dotyczyTomasza/WBP. Poprawiono3referencje wewnątrztekstów, zachowując logzmian.','PEWNE — PORÓWNANIE REJESTRU I MAPOWANIA','S267;S253;SCALENIE_HISTORII etapu21','Stosować aktualneS267dla nr530/2591/2656; nie zamieniaćlegalnychodnośnikówS253wbadaniuTomasza.',rel(R/'badania/2026-11-07-sesja-21-meldunki-Ch/SCALENIE_HISTORII.md')]
]:add('KOREKTY_I_SPRZECZNOSCI',values)
logs=[
('AudytS041/S306 oraz numeracji meldunków','Ogłoszenie1976jużznane;S306aliasS041. NaprawionoS253→S267wH049–H051.','Beznowegoźródła rodzinnego; IDhistorycznezachowane.','Q104;Q106;S041;S306;S267'),
('Referendum1946,kompletny manifest283','Wszystkie283obrazy należądo39/639/0/-/1Sprawyorganizacyjne.','Spisów8–199nieodczytano; niebrakrodziny.','S307'),
('NKJPnkjp1800,DziennikŁódzki;Tomasz/Piotr/Witold','3/8/0;odczytano11kontekstów,kino/ pięciobój/kolarstwo.','Korpuswybrany; niepełne roczniki.BłędyBogusława/szerszychzapytańnie sązerem.','S312'),
('ArolsenChmielewski,synSearch:true,rowNum0–4000','Pobrano4773pozycje:1000+1000+1000+1000+773.','Nie4773osób/skanów; daty1909jużznane,brakidentyfikacjiP02/P11.','S313;S075;S076;S077;S078'),
('OryginałArolsen70592196,obaobrazy','Indeks1943niezgodnyz8.3.03i pobytem1940; dorosłyJan1903.','Brakrodziców;nieprzyjętodo rodziny.','S314;Q105'),
('Arolsen69969056/69969547,Witold1936','Obalistypodają20IV1936Końskie,Durach/Kempten.','Niepodająrodziców;obokJózef/Józefa nieznaczyrodzice.NiepołączonozC11.','S315'),
('ArcinsysHessen,nazwisko21opisy i warianty','21wynikówChmielewskiprzeczytane,brakrodzinnegoidentyfikatora.','Caßdorf/Homberg tylko pierwsze20; braktrafieńwariantówniewykluczaakt.','S316'),
('25506,205pobranychJPG,198kolumnnazwisk','NoweC107/Stocka12iC108/Żeromskiego67; Czesława2492niezidentyfikowana.','BrakimieniaP11/rodzicówPiotra; niepełnatranskr.opozostałychrubryk.','S309;S310;S311'),
('25506obraz82,str79,nr1823,27VI1936','Czesław,Stocka12,1m,Poznańskie/ChrzypskoMałe,dopisekczasowości.','BrakDOB/żony/rodziców.Datazgłoszenianiejestdowodemfizycznejpodróży.','S310;C107;H049;H051'),
('25506obraz138,str35,nr3154,21X1936','Czesław,Żeromskiego67,1m,b.a.','NieutożsamionozC107/C98/C100/P03.','S311;C108'),
('Chrzypsko:4kwerendykatalogowe i opis92/60/0','0skanów,opis84–85ewidencjaruchu1945–1947;Portletlistyniedostępny.','Nieodczytanoewidencjiosóbani niedowiedzionozachowaniaksięgi1936.2ogólnefrazyczęściowopowtarzałyetap21po nowymS310;nieliczyćjako nowyłącznik.','S317'),
('S238MSW2015poz14:nowa dostępnośćprzezFirecrawl','Poz748PiotrChmielewski,s.Józefa,brązowaodznakaochronyprzeciwpożarowej;kopiatekstowa45stron.','Odczytwiersza/nagłówka,niewszystkich45stron.BrakDOB/jednostki/Łodzi.JózefniejestustalonymP11.','S238;H003'),
('Kontrola odpowiedzi nawysłane zapytania','Gmailinboxafter2026/11/07,domenyzzm.lodz.pl/franciszkanie.pl/wbp.lodz.pl:brakwiadomości.','Ograniczeniedodat/sprawdzanychnadawców;niepełny audytpoczty.Niewysłanonowychwiadomości.','M10;TOM-D05')]
for k,(scope,result,limit,src)in enumerate(logs,309):add('DZIENNIK_KWEREND',[f'L{k}',now,scope,result,limit,src+';'+rel(D/'STATUS.md')])
# Register selected local evidence, hashes are also in a complete file manifest.
files=[('baza_przed_etapem32.xlsx','Git:fce13f2','ARCHIWUM BAZY'),('zrodla/25506_manifest.json','S309','MANIFEST PUBLICZNYCH SKANÓW'),('zrodla/25506_pobrane_sha256.json','S309','205 KONTROLI SHA'),('zrodla/25506_kolumny_nazwisk.zip','S309','198 ZBADANYCH KOLUMN; POCHODNE'),('zrodla/25506_wybrane_odczyty.csv','S309;S310;S311','TRANSKRYPCJE WYBRANYCH WIERSZY'),('zrodla/25506_zakres_odczytu.json','S309','DOKŁADNY ZAKRES'),('zrodla/referendum_1946_manifest.json','S307','KOMPLET283METADANYCH'),('zrodla/arolsen/all_pages.json','S313','4773POZYCJE INDEKSU'),('zrodla/arolsen/zakres.json','S313','ZAKRES POBRANIA'),('zrodla/nkjp_verified/tomasz/summary.json','S312','3 KONTEKSTY TOMASZA'),('zrodla/nkjp_verified/piotr/summary.json','S312','8KONTEKSTÓW PIOTRA'),('zrodla/arcinsys/queries.json','S316','ZAPYTANIA I LOG'),('zrodla/Chrzypsko_zespol_92_60.json','S317','ODCZYT KATALOGU'),('zrodla/MSW2015_14_odczyt_Firecrawl.md','S238','KOPIA TEKSTOWA PDF; NIE BINARNY PDF'),('zrodla/MSW2015_Firecrawl_metadane.json','S238','METADANE POZYSKANIA')]
for n in [1,2,4,5,82,104,110,138,178,203,204,205]:files.append((f'zrodla/25506_{n:03}.jpg','S310'if n==82 else('S311'if n==138 else'S309'),'ORYGINALNY SKAN'))
for f in sorted((Z/'arolsen_jan1943').glob('*.jpg')):files.append((str(f.relative_to(D)),'S314','ORYGINALNY SKAN'))
for f in sorted((Z/'arolsen_witold1936').glob('*.jpg')):files.append((str(f.relative_to(D)),'S315','ORYGINALNY SKAN'))
for k,(sub,src,typ)in enumerate(files,441):
 f=D/sub;assert f.exists(),f;add('PLIKI_DOWODOWE',[f'F{k}',rel(f),typ,src,sub,'SHA256 '+hashlib.sha256(f.read_bytes()).hexdigest()])
setv('ZADANIA_AGENTA','T55',6,find('ZADANIA_AGENTA','T55')[5].value+' Etap32:S310nr1823Stocka12/ChrzypskoMałe;25506nazwiskazakończone. NadalbrakDOB/rodziny.')
setv('ZADANIA_AGENTA','T55',9,find('ZADANIA_AGENTA','T55')[8].value+';S309;S310;C107;'+rel(D/'PLAN_KONTYNUACJI.md'))
add('INSTRUKCJA_AGENTA',['G29','ETAP32 — CZTERY OSOBY / BEZ POWTÓREK',rel(D/'STATUS.md')+'; '+rel(D/'PLAN_KONTYNUACJI.md')+'. S310C107Stocka12/ChrzypskoMałe;C108osobny. Arolsen4773indekspobrany;25506nazwiska198obrazówzakończone;S306aliasS041;H049–51referencjeS267naprawione. S238Piotr,s.Józefa,niezidentyfikowanyP10. Braknowejrelacji;bezkorespondencji.'])
w['ZRODLA_I_SKANY']['A2']='317 rekordów źródeł; S306 aliasS041. Etap32: C107 Stocka12/ChrzypskoMałe; bez nowej relacji rodzinnej.'
w['KANDYDACI_I_HOMONIMY']['A2']='108 rekordów; C107 Stocka12 i C108 Żeromskiego67 to osobne wpisy Czesława bez potwierdzenia tożsamości.'
w['INDEKS_MELDUNKOW']['A2']='62 wybrane odczyty; nie pełny indeks ani lista krewnych. IM059–IM062: etap32.'
tmp=p.with_name(p.stem+'.etap32.tmp.xlsx');w.save(tmp);openpyxl.load_workbook(tmp).close();tmp.replace(p)
(D/'ZMIANY_KOMOREK.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
(D/'LICZNIKI.json').write_text(json.dumps({'at_utc':now,'sheets':len(w.sheetnames),'source_records':317,'last_ids':{'source':'S317','log':'L321','candidate':'C108','correction':'Q106','file':f'F{440+len(files)}','meldunkowy':'IM062'},'changed_existing_cells':len(edits),'new_proven_relationships':0},ensure_ascii=False,indent=2)+'\n')
print('Zapisano etap32:',len(sources),'źródeł,',len(logs),'logów,',len(files),'plików;',len(edits),'kontrolowanych zmian komórek')
