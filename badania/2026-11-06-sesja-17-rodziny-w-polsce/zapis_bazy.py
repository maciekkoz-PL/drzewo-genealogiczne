"""Etap 17. Uzupełnienia prywatnego rejestru; bez tworzenia nowych relacji rodzinnych."""
from pathlib import Path
from zoneinfo import ZoneInfo
import csv, datetime, json, openpyxl, shutil

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BASE = str(HERE.relative_to(ROOT))
now = datetime.datetime.now(ZoneInfo('Europe/Warsaw')).isoformat(timespec='seconds')
w = openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
def row(sheet, ident):
    return next(r for r in w[sheet] if r[0].value == ident)
assert len(w.sheetnames) == 23
assert not any(r[0].value == 'S205' for r in w['ZRODLA_I_SKANY'])

# Zachowanie pobrań i dokładnych parametrów; HTML nie jest skanem aktu.
src = ROOT/'work/s17'
for f in src.rglob('*'):
    if not f.is_file() or f.suffix == '.py' or f.name.startswith('scan'):
        continue
    target = HERE/'zrodla'/f.relative_to(src)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(f, target)
for f in (src/'swa1908').glob('scan*.jpg'):
    shutil.copy2(f, HERE/'zrodla/swa1908'/(f.stem+'_odpowiedz_html.txt'))
(HERE/'zrodla/odczyt_S153_Q81.md').write_text(
    '# Ponowny odczyt S153 — 06.11.2026\n\n'
    'Istniejący skan: badania/2026-11-06-sesja-11-rodziny-rodzenstwa/zrodla/emilia74_crop.jpg. '
    'Ślub74/1932: świadek Marcin Przysucha, lat61, właściciel jadłodajni wTomaszowie. '
    'Wtekście dopełniacz Marcina, wpodpisie Marcin. Wcześniejsze Marian poprawiono Q81. '
    'Nieustalone pokrewieństwo świadka; Katarzyna zindeksu53/1908 nie została siostrą P29. '
    'Nazwa kolonii zamieszkaniaEmilii nadal wymaga weryfikacji; nie przypisano Bełżca. '
    'Nie pobierano ponownie istniejącego obrazu i nie tworzono nowej kopii oryginału.\n')

sources = [
 ('S205','MyHeritage — publiczny indeks pary Mandziuk/Chmielewska','FRAGMENTY WYSZUKIWARKI; PEŁNY REKORD NIEODCZYTANY','P28; P29','MyHeritage','Józef1897; Emilia1904; ślub1932','https://www.myheritage.com/names/j%C3%B3zef_mandziuk','kwerendy_01.json','Zgodne roczniki i ślub, ale brak autora i dzieci. Strona agreguje imienników. Zwykły dostęp Incapsula/pusta strona, Firecrawl basic bez treści. Nie przypisano Katarzyny lub zgonu1919 doP29.'),
 ('S206','Bełżec — wzmianki pary Emilia/Józef Mandziuk','FRAGMENTY INDEKSU; OBECNA STRONA ZAWIESZONA','P28?; P29?; H045','Parafia Bełżec','12–20.05.2021; archiwum05.2022 / niedziela05.06.2022','https://parafiabelzec.pl/intencje-mszalne-12-20-05-2021/','belzec_2022.html','BezDOB, krewnych i wskazania ofiarodawcy. Nie odczytano pełnych historycznych stron. Nie dowodzi miejsca pochówku/residence ani tożsamości zparąP28/P29; Nowakowie nie zostali powinowatymi.'),
 ('S207','Geneteka — Mandziuk/Emilia i późniejsze indeksy lubelskie','27 ŻĄDAŃ API Z POZYTYWNĄ KONTROLĄ','P28; P29; H032','PTG Geneteka','21regionówM1932–1970; lubelskie66/66MandziukM; B1932–1960; ChmielewskiB1920–1926','https://geneteka.genealodzy.pl/','geneteka/queries.json','Znany ślub74/1932 poprawnie zwrócony. 21regionów: tylko ten ślub. 66małżeństw w2stronach API, faktyczne lata1932–1945; brak dzieckaP28/P29. B Mandziuk0; Chmielewski31wierszy bez rodziny. Emilja daje ten sam rekord. Brak windeksie nie dowodzi bezdzietności; nie odczytano66aktów.'),
 ('S208','Lubgens Tomaszów — urodzenia1920–1923','PEŁNA TABELA INDEKSU1281POZYCJI','P05; P06; rodzeństwoP03?','Lubgens','par47,actu,decade192; latafaktyczne1920/21/22/23:304/316/338/323','https://regestry.lubgens.eu/druk_usz_v2_1.php?par=47&act=u&decade=192','tomaszow_birth192.html','Brak Chmiel… oraz pary Wincenty/Agnieszka. Nie obejmuje1924–1926ani całejdekady, nie odczytano1281oryginałów.'),
 ('S209','Monitor Polski1997poz581 — Sabina c.Franciszka','PDF; ODCZYT WSKAZANYCH POZYCJI','C97; P26 wykluczenie','Monitor Polski','1997poz581,strdruk1170,poz493/494','https://dziennikustaw.gov.pl/M1997060058101.pdf','MP1997_581.pdf','Czesław s.Jana i Sabina c.Franciszka. P26jest córkąWincentego — wykluczona. Odrębny dokument od staregoS043poz314; bez poszukiwania dzieci obcejpary.'),
 ('S210','Głos Nauczycielski1950nr4 — Emilia Mandziuk,Gończyce','PDF4STRONY; ODCZYT LISTU STR3','P28? NIEUTOŻSAMIONA','Głos Nauczycielski / JBC','1950nr4,str3','https://jbc.bj.uj.edu.pl/Content/992445/NDIGCZAS110934_1950_004.pdf','glos1950_4.pdf','Podpis EmiliaMandziuk,Gończyce,pow.Garwolin; brakDOB,męża,rodziców. Nie przypisano nauczycielstwa, miejscażycia ani listu P28.'),
 ('S211','Dzieje miejscowości — Tomaszów i Susiec','DWA PDF; WYSZUKANIE TEKSTU I ODCZYT TRAFIEŃ','P29? NIEUTOŻSAMIONY','Gmina Tomaszów Lubelski / gmina Susiec','Dwa opracowania; dokładne URL wdownloads_02.json','https://susiec.pl/images/publikacje/Dzieje_miejscowosci_Gminy_Susiec.pdf','downloads_02.json','JózefMandziuk:stodoła na szkołę Łosiniec1941, bezDOB/żony. Inni Mandziukowie niepowiązani. Nie dopisano współczesnych osób jako rodziny i nie deklarowano lekturycałości książek.'),
 ('S212','Przysucha/Mandziuk53/1908 — lokalizacja jednostki','INDEKS I MANIFEST; AKT NIEODCZYTANY','P29?; świadekS153','AP Zamość / Szukaj wArchiwach / Lubgens','88/639/0/-/33; unit10505176;162obrazy','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/10505176','swa1908/Tomaszow1908_api.json','Indeks MarcinPrzysucha/KatarzynaMandziuk53/1908. Pobrane90/110/130toHTMLIncapsula, nie skany. Pełnyakt nieodczytany; Katarzyna nie została siostrąP29. Kierunekpośredni, niski priorytet.'),
 ('S213','Grobonet Polska — poprawne formularze i kontrola','5KWEREND ORAZ 2PRÓBY KONTROLNE','P26; P27; P28; P29; P31','Grobonet','imie/nazw/rok_ur; pozytywna JuliannaDylkiewicz1907','https://grobonet.com/wyszukiwanie','grobonet/queries.json','EmiliaMandziuk0regionów;Józef1897, Sabina1917,Julianna1907także0. Czesława/Łódź0cmentarzy. KontrolaDylkiewicz1osoba. Jan/Siedlnicaodrzucone miasto, nie wynik0. Nie obejmuje wszystkich cmentarzy, brakiDOB/zmiany nazwisk; nie dowodzi życia.'),
 ('S214','Tczew — samymi imionami, pełna paginacja i fotografie','12STRON WYNIKÓW;4KARTY;8/8ZDJĘĆ OBEJRZANO','P26?; P27?; H019','GrobonetTczew:komunalny iśw.Józefa','Julianna/Sabina/Julia;41542,40862,42017,40032bezDOB','https://swjozeftczew.grobonet.com/wyszukiwarka','tczew/name_queries.json','Komunalny8/14/20;parafialny18/7/37. PrefiksJulia zawieraJuliana/Juliannę, nie sumować. Brak zgodnegoDOB. CzteryJulianny bezDOB także po8fotografiach; nie przypisano ichP27. SabinaŁuczak12.08.1916 iJuliannaDylkiewicz20.01.1907niepasują. Współpochówek nie dowodzi relacji.'),
 ('S215','Ponowny odczyt świadkaS153 — Marcin Przysucha','ODCZYT ISTNIEJĄCEGO SKANU; Q81','P28; P29; świadekS153','USC Tomaszów1932 / Lubgens','74/1932;284676/4343,019.jpg','https://fotolubgens.lubgens.eu/picture.php?/284676/category/4343','odczyt_S153_Q81.md','Wtekście Marcina i wpodpisie Marcin, nie Marian. Wiek61, właściciel jadłodajni. Bezpotwierdzenia pokrewieństwa; nazwa kolonii zamieszkaniaEmilii nadalnieustalona. Oryginalny skan pozostał wsesji11.'),
 ('S216','Szerokie wyszukiwanie polskich gałęzi i nieudane odczyty','REJESTR WYSZUKIWAREK I OGRANICZEŃ','P26; P27; P28; P29; P31','Wyszukiwarki / Firecrawl basic','kwerendy_01–04.json; logi pobrań','https://grobonet.com/','kwerendy_04.json','Szukano pełnychdat, rodziców, małżeństw, nekrologów i drzew. Nie znaleziono nowego żyjącego krewnego lub uzasadnionego adresata. Nie otwierano niepowiązanych people-search. eCmentarzeBełżec bezinwentaryzacji, brak realnejkwerendy osób. Częśćpowtórzonych fraz to kontrola tropu, nie niezależnydowód.')
]
sources[-1] = (*sources[-1][:-1], sources[-1][-1] + ' Końcowe poszerzenie: katalog ewidencji mieszkańców1926, unit10446043,88/24/0/-/245,34obrazy. Odczytano tylko metadane/manifest, nie skorowidz lub daneosobowe. DalszeArolsen/nauczycielka beznowegoidentyfikatora; znaneAPI niepowtórzone. kwerendy_05.json.')
for sid,title,kind,persons,inst,sig,url,path,limit in sources:
    w['ZRODLA_I_SKANY'].append([sid,title,kind,'2026-11-06',persons,inst,sig,url,'ZAKRES ODCZYTU I GRANICE W OSTATNIEJ KOLUMNIE',BASE+'/zrodla/'+path,limit])
w['ZRODLA_I_SKANY']['A2']='216 źródeł. Etap17: rodziny rodzeństwaCzesława wPolsce; brak nowego potwierdzonego żyjącego krewnego. Indeksy i fotografie nie są pełnymi aktami; ograniczenia wS205–S216.'

w['KANDYDACI_I_HOMONIMY'].append(['C97','Sabina Chmielewska — Monitor Polski1997poz581','odnotowana1997; DOBniepodana','córkaFranciszka; NIE P26','Polska; miejsceżycia niepodane','WYKLUCZONA JAKO P26','P26jest córkąWincentego; dokument wyraźnie wskazujeFranciszka.','S209','Nie przypisywać tejpary lub jej dzieci do rodzinyMarysi. Niepotwierdzone życie obecne.','https://dziennikustaw.gov.pl/M1997060058101.pdf'])
w['WIARYGODNOSC_OSOB'].append(['C97','Sabina Chmielewska — Monitor1997','brak relacji zMarysią','wykluczona jakoP26',None,None,'S209','Innyojciec:Franciszek zamiastWincentego.','Nie dodawać do drzewa rodzinnego; nie szukać jej potomków jako krewnychMarysi.'])
w['ZDARZENIA_I_FAKTY'].append(['E071','22.11.1932','P28; P29','świadek — korekta odczytu','Marcin Przysucha, lat61, właściciel jadłodajni wTomaszowie; nie Marian.','ISTNIEJĄCY SKAN PIERWOTNY — Q81','S153; S215','https://fotolubgens.lubgens.eu/picture.php?/284676/category/4343','Bezustanawiania pokrewieństwa świadka; nazwa koloniiEmilii wymaga weryfikacji.'])
hyps=[
 ['H045','Czy Emilia/Józef Mandziuk zBełżca toP28/P29?','S206fragmenty2021/2022wymieniająparę, bezdat/krewnych. Pełnehistoryczne strony nieodczytane.','Niezależny wpis nagrobny/nekrolog zDOB,DODlub rodziną; nie wnioskować powinowactwa zNowakami.','OTWARTA — NIE PRZYPISANO MIEJSCAŻYCIA,GROBU LUB DZIECI'],
 ['H046','Czy publiczna pozycjaMyHeritage doprowadzi do autora rodzinnego źródła lub potomkówP28/P29?','S205pasuje rocznikami1897/1904 iślubem1932. Brak pełnegorekordu, autora i nazwiskdzieci; stronaagregujeimienników.','Gdy będzie zwykły publiczny dostęp: ustalić odnośnikrekordu irodzajźródła/autora. Nie utożsamiać autora zpotomkiem bezpotwierdzenia; bezwiadomości.','OTWARTA — BRAK ODNALEZIONEGO ADRESATA DO KONTAKTU']]
for r in hyps:w['HIPOTEZY_OTWARTE'].append(r)
r=row('HIPOTEZY_OTWARTE','H032')
r[2].value+=' Etap17:S205indeks pary bezdzieci; S206Bełżec nieutożsamiony. S20721regionów i66małżeństw z2stron nie wskazały potomka; brakiindeksacji nie dowodzą bezdzietności. S213nie znalazł grobu wogólnym systemie.'
r[3].value='Publiczny nagrobek/nekrolog lub późniejsze źródło rodzinne zrelacją dziecka. Emilia:zgon27.02.1979, USC Tomaszów76/1979 znany zprzypisku, właściwyakt nieodczytany. H045/H046 do weryfikacji.'
r[4].value='AKTYWNA — POLSKA, DZIECI I WNUKI; BEZ KONTAKTÓW'
r=row('HIPOTEZY_OTWARTE','H019')
r[2].value+=' Etap17:S214pełne12stron dwóchcmentarzy, imionaJulianna/Sabina/Julia beznazwisk; brakzgodnegoDOB. CzteryJulianny bezDOB,4karty i8zdjęć nieustalajątożsamości. Nie wyklucza innych cmentarzy lub pomyłekbaz.'
r[3].value='Nowe źródło nazwiska poślubie/rodowego zrodzicami lub pełnąDOB, ewentualnie rodzinny wykaz ztamtejrozmowy. Nie ponawiać12stron i8zdjęć beznowejprzesłanki.'
r[4].value='OTWARTA — TCZEW NADAL NIEPOTWIERDZONY'
row('HIPOTEZY_OTWARTE','H033')[4].value='OTWARTA — WZNOWIĆ PO NOWYM IDENTYFIKATORZE; BIEŻĄCY PRIORYTET POLSKIE DZIECI RODZEŃSTWA'

logs=[
 ('L177','Zmiana kierunku po nowym poleceniu','PriorytetPolska:P26/P27/P28/P29; przerwano rozwijanieAustralii.','Brak automatycznej identyfikacji krewnych; niczego nie wysłano.','S205–S216'),
 ('L178','MyHeritage:para1897/1904 iślub1932','Dopasowanie wpublicznym indeksie.','Brakpełnego rekordu,dzieci,autora; Incapsula/pusta strona, basicbeztreści.','S205; H046'),
 ('L179','Bełżec2021/2022','Dwie indeksowane wzmianki paryEmilia/JózefMandziuk.','Stronazawieszona; pełnychwpisów nieodczytano. BrakDOB/potomków.','S206; H045'),
 ('L180','Geneteka:21regionów Mandziuk+EmiliaM1932–1970','Tylkoznany74/1932; pozytywnakontrola zwracawłaściwychrodziców.','Nie dowodzi braku dzieci, niecałe pokrycielat/parafii.','S207'),
 ('L181','LubelskieMandziukM1932–1970,paginacja iEmilja','66/66wierszy w2stronach, faktycznie1932–1945. Emilja=ten samznanyślub.','Brak dzieckaP28/P29; nie odczytano66oryginałów. Nie powtarzano21regionów dlaEmilja.','S207'),
 ('L182','Geneteka:B Mandziuk1932–1960 iChmielewski1920–1926','0 i31surowychwierszy; brak identyfikatorów szukanejrodziny.','Indeksyurodzeń o ograniczonympokryciu, nie dowód bezdzietności.','S207'),
 ('L183','LubgensTomaszówurodzenia,decade192','1281pozycji; lata1920–23:304/316/338/323; brakChmiel… iWincenty/Agnieszka.','Niecała dekada, nie1924–1926; nie1281odczytanychaktów.','S208; Q82'),
 ('L184','MonitorPolski581/1997,str1170,493/494','Sabina c.Franciszka wykluczona jakoP26c.Wincentego.','OdrębnyPDF odS043; nieprzypisano małżonka/dzieci rodzinieMarysi.','S209; C97; Q84'),
 ('L185','GłosNauczycielski1950nr4,str3','PodpisEmiliaMandziuk,Gończyce,pow.Garwolin.','BezDOB,męża irodziców; nieP28beznowegołącznika.','S210'),
 ('L186','DwaPDFregionalneTomaszów/Susiec','OdczyttrafieńMandziuk; JózefŁosiniec1941 bezidentyfikatorów.','Niepełnalektura; lokalniwspółcześniMandziukowie nieuznani za potomków.','S211'),
 ('L187','MarcinPrzysucha/KatarzynaMandziuk53/1908','Jednostka10505176,88/639/0/-/33,manifest162obrazów.','3pobrania90/110/130toHTMLIncapsula; aktu53nieodczytano, Katarzyny niepołączono zP29.','S212'),
 ('L188','GrobonetPolska:5właściwychkwerend','4wyniki0regionów, CzesławaŁódź0cmentarzy.','Niecała baza grobów,brakDOB/zmiany nazwisk. Nie dowodziżycia.','S213'),
 ('L189','KontrolaGrobonetu','JuliannaDylkiewicz1907:1osobaPomorskie.','JanMandziuk/Siedlnica nieznanemiasto, nie0. Formularzwypełniony właściwie.','S213; Q83'),
 ('L190','Tczew:2cmentarze,3imiona,12stronwyników','Pełnapaginacja. BrakzgodnegoDOB; SabinaŁuczak1916/Dylkiewicz20.01.1907inne.','JuliajestprefiksemJuliana/Julianny; niewolnosumować wyniku jako odrębnychkobiet.','S214; H019'),
 ('L191','Tczew:4kartybezDOB,8zdjęć,4kwerendynazwisk','Zdjęciaobejrzano, nadalbrakDOBJuliann irodzinnegołącznika.','NieprzeniesionodatJanaGriech naJuliannę; współpochówek nieoznacza relacji. Nie dodano kobiet do drzewa.','S214; S216'),
 ('L192','PonownyodczytS153 iutrwalenie postępów','ŚwiadekMarcin,nieMarian; Q81. PierwszepobraniazachowanowGitHube0236d1.','Nienowaosobarodziny. Niepublikowanonegatywnychkwerend jako przełomu; 71kart/96relacji/9wpisów bez zmian.','S153; S215')]
logs.append(('L193','Nowy katalog mieszkańców i końcowe poszerzenie','SkorowidzludnościniestałejTomaszowa1926,88/24/0/-/245,unit10446043,34obrazy.','Tylkometadane/manifest; nie odczytano nazwisk. Meldunkoweroot bezlistyTomaszowa niejest pełnąkwerendą. TeacherC73nadalnieutożsamiona; niepowtórzonoAPI ArolsenS181.','S216'))
for lid,scope,result,limit,source in logs:
    w['DZIENNIK_KWEREND'].append([lid,now,scope,result,limit,source])
corrections=[
 ['Q81','KOREKTA ODCZYTU','Świadek ślubu74/1932: Marcin, nie Marian','Tekst Marcina i podpis Marcin Przysucha,61,właściciel jadłodajni.','WYSOKA — ISTNIEJĄCY SKAN','S153; S215','Bez automatycznego powinowactwa zKatarzyną zindeksu1908.','https://fotolubgens.lubgens.eu/picture.php?/284676/category/4343'],
 ['Q82','ZAKRES INDEKSU','Lubgensdecade192 nie obejmuje całejdekady','1281wierszy tylko1920–1923, nie1924–1929.','PEŁNA TABELA INDEKSU','S208','Nie opisywać jako1281aktów lub wszystkichurodzeń1920–1926.','https://regestry.lubgens.eu/druk_usz_v2_1.php?par=47&act=u&decade=192'],
 ['Q83','BŁĄD KWERENDY KONTROLNEJ','GrobonetJan/Siedlnica niejestwynikiem0','Miastonieznanewformularzu; pozytywnakontrolaDylkiewicz1907zwróciła1osobę.','ODCZYT FORMULARZA','S213','Oddzielać odrzuconeparametry od prawdziwego negatywnegowyniku.','https://grobonet.com/wyszukiwanie'],
 ['Q84','WYKLUCZENIE HOMONIMU','Sabina zMP581/1997niejestP26','OjciecFranciszek zamiastWincentego.','WYSOKA — PDF','S209; C97','Nieprzypisywać medalowejpary/dzieci doMarysi; toinnyPDF niżS043.','https://dziennikustaw.gov.pl/M1997060058101.pdf']]
for r in corrections:w['KOREKTY_I_SPRZECZNOSCI'].append(r)

files=[('F151','kwerendy_01.json','S205; S206; S216'),('F152','belzec_2022.html','S206'),('F153','geneteka/queries.json','S207'),('F154','tomaszow_birth192.html','S208'),('F155','MP1997_581.pdf','S209'),('F156','glos1950_4.pdf','S210'),('F157','dzieje_tomaszow.pdf','S211'),('F158','dzieje_susiec.pdf','S211'),('F159','swa1908/Tomaszow1908_api.json','S212'),('F160','grobonet/queries.json','S213'),('F161','tczew/photo_downloads.json','S214'),('F162','odczyt_S153_Q81.md','S215')]
for ident,path,source in files:
    w['PLIKI_DOWODOWE'].append([ident,BASE+'/zrodla/'+path,'KOPIA / REJESTR ZAKRESU',source,'Pozostałe pliki i hashe wmanifest_zrodel_sesji.json; zakres odczytu wSTATUS.md.','SHA256 wmanifeście; nie każdy plik jest aktem.'])
tasks=[
 ['T43',1,'RODZINY W POLSCE','Publiczne źródła rodzinne/cmentarne','Emilia/Józef: potwierdzićdzieci/grób iocenićBełżec.','AKTYWNE — BRAK POTWIERDZONEGO POTOMKA','Agent','WymagaDOB/rodziców lub jawnejrelacji; bezkontaktów.','H032; H045; S206; S207; S213'],
 ['T44',1,'NAZWISKA SIÓSTR POŚLUBIE','Nowe publiczne indeksy/rodzinne dokumenty','Sabina/Julianna: małżeństwa i dzieci zidentyfikatorami; uwzględnić niepotwierdzonyTczew.','AKTYWNE — BEZ NOWYCH RELACJI','Agent','Nieponawiać12stron/8zdjęć; do4Juliann bezDOB potrzebne nowezródło.','H019; S214'],
 ['T45',2,'AUTOR RODZINNEGO ŹRÓDŁA','Zwykły publiczny dostępMyHeritage','Ustalićrekord/autora pasującejpary, jeśli dostępny; niezakładaćżeautor jest potomkiem.','OTWARTE — BRAK ADRESATA DO KONTAKTU','Agent','Niemnożyć językowych kopii i nieobchodzić blokad. Niczegoniewysyłać.','H046; S205']]
for r in tasks:w['ZADANIA_AGENTA'].append(r)
for ident in ['T41','T42']:
    row('ZADANIA_AGENTA',ident)[5].value='WSTRZYMANE — NAJNOWSZY PRIORYTET UŻYTKOWNIKA: RODZINA W POLSCE; WYNIKI ZACHOWANE'
w['START']['A2']='Etap17: priorytet rodziny rodzeństwaCzesława wPolsce, zwłaszcza dzieci/wnuki. Nie potwierdzono nowego żyjącego krewnego. 23arkusze,216źródeł,97kandydatów; raport i plan badania/2026-11-06-sesja-17-rodziny-w-polsce/. Starsze priorytety historyczne; Australia wstrzymana.'
w['INSTRUKCJA_AGENTA']['A2']='Aktualne polecenie06.11.2026: rodzina rodzeństwaCzesława wPolsce, dzieci iwnuki. Badania kontynuowane za zgodą użytkownika mimootwartejH017. Australia wstrzymana. Poniższe dawne priorytety są historyczne; bezkontaktów bezosobnejzgody.'
row('INSTRUKCJA_AGENTA','G01')[2].value='Potwierdzić żyjących krewnych wPolsce zgałęzi rodzeństwaCzesława:Sabina,Julianna,Emilia/Józef. Ustalaćdzieci iwnuki zidentyfikatorami, bezprzypisywania imienników. S086jużpodaje rodzicówBogusława, H017do dodatkowego potwierdzenia przezrodzinę. Bezwiadomości bezosobnejzgody.'
for sheet,filename in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
    with (ROOT/'badania/2026-11-06-trzy-poziomy'/filename).open('w',newline='') as f:
        csv.writer(f,lineterminator='\n').writerows([['' if v is None else v for v in r] for r in w[sheet].values])
w.save(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
print('Etap17 zapisany:216źródeł,97kandydatów,193kwerendy; drzewo publiczne bez zmian.')
