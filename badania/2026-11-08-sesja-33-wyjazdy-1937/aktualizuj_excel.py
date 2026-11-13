"""Jednorazowy zapis etapu33 na bazie08b5991; bez sieci i bez nowych relacji."""
from pathlib import Path
from copy import copy
import datetime, hashlib, json, re
import openpyxl

D=Path(__file__).resolve().parent;R=D.parents[1];Z=D/'zrodla'
P=R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx';B=D/'baza_przed_etapem33.xlsx'
assert hashlib.sha256(P.read_bytes()).hexdigest()==hashlib.sha256(B.read_bytes()).hexdigest(),'Baza zmieniła się od kopii; nie nadpisywać zmian innej sesji.'
w=openpyxl.load_workbook(P);now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds');edits=[]
rel=lambda p:str(p.relative_to(R))
def find(sn,id):
    rr=[r for r in w[sn].iter_rows()if r[0].value==id];assert len(rr)==1,(sn,id,len(rr));return rr[0]
def cell(sn,address,value,id=None):
    c=w[sn][address]
    if c.value!=value:edits.append(dict(sheet=sn,id=id,cell=address,before=c.value,after=value));c.value=value
def setv(sn,id,col,value):cell(sn,find(sn,id)[col-1].coordinate,value,id)
def appendv(sn,id,col,addition):setv(sn,id,col,(find(sn,id)[col-1].value or '')+addition)
def add(sn,values):
    s=w[sn];assert not any(r[0].value==values[0]for r in s.iter_rows()),(sn,values[0]);n=s.max_row+1
    for j,v in enumerate(values,1):
        c=s.cell(n,j,v);old=s.cell(n-1,j);c._style=copy(old._style);c.alignment=copy(old.alignment);c.number_format=old.number_format
    s.row_dimensions[n].height=75 if sn not in ['PLIKI_DOWODOWE','INDEKS_MELDUNKOW'] else 60
    if s.auto_filter.ref:s.auto_filter.ref=f'A3:{openpyxl.utils.get_column_letter(s.max_column)}{n}'
assert not any(r[0].value=='S318'for r in w['ZRODLA_I_SKANY'].iter_rows())
urls={}
for book in ['25507','25509']:
    urls[book]={x['pozycja']:x['src']for x in json.loads((Z/f'{book}_manifest.json').read_text())['elementy']}
sources=[
 ['S318','Wyjazdy Łodzi, grupaIII: kontynuacja1937','SKANY PIERWOTNE; PRZEGLĄD NAZWISK',now,'P03/P04/P11 — kwerenda; niepołączeni imiennicy','AP Łódź / SwA','39/221/0/4.12/25507;149obrazów,142z wpisami','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6209684','NAZWISKA5–103 i105–147;24WYBRANE WIERSZE',rel(Z/'25507_zakres.json'),'Początek23III1937, nie cały rok. Brak nowej relacji lub imieniaP11. Nie czytano wszystkich rubryk142obrazów. Pełne granice,CSV,SHAi kolumny wpakiecie.'],
 ['S319','Wyjazdy Łodzi, grupaIII,1939 — dostępna księga','SKANY PIERWOTNE; PRZEGLĄD NAZWISK',now,'C109;H054;P11 — bez identyfikacji','AP Łódź / SwA','39/221/0/4.12/25509;187obrazów,181z wpisami','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6209686','NAZWISKA4 i6–185;19WYBRANYCH WIERSZY',rel(Z/'25509_zakres.json'),'Zgłoszenia2I–1XII1939, nie pełny grudzień. Techniczne1,2,3,5,186,187 obejrzane. Wpis3693wydzielony jakoS320z tej samej księgi; nie niezależne źródła.'],
 ['S320','Stanisława i Zygm. — Grabowa4→Buczek,6XI1939','KONKRETNY WPIS W S319',now,'C109;Stanisława zIM025?;H054','AP Łódź','39/221/0/4.12/25509,obraz165,str161,nr3693',urls['25509'][165],'ODCZYTANO WIERSZ I NAGŁÓWKI',rel(Z/'25509_165.jpg'),'Literalnie Chmielewska / Stanisława i Zygm.;1m+1k;pow.Łask/gm.Buczek;Grabowa4. Mocne dopasowanie odwrotnego kierunku/adresu/liczebności doIM025/708. BrakDOB/relacji; nie ustalono rozwinięcia skrótu ani oddzielnego nazwiska mężczyzny. Nie dowodzi C105=P03 lub C109=P11.'],
 ['S321','Arolsen — nowy trop Zygm.,6DocID/10obrazów','ORYGINAŁY + PONOWNE UŻYCIE INDEKSU S313',now,'Nieutożsamieni Zygmuntowie; C109/P11 — kwerenda','Arolsen Archives','70634058;78640271;81787522;81978799;81979003;81991022','https://collections.arolsen-archives.org/en/document/81979003','ODCZYTANO WYBRANE WIERSZE WSZYSTKICH10OBRAZÓW',rel(Z/'arolsen_zygmunt_odczyty.json'),'Filtr już pobranych4773pozycji daje43rekordy/42DocID, nie43osoby. Dwa dokumenty łączą kartyDP126758/126755/126759:Zygmunt1905,Halina1914,Zygmunt1943; nie jest to dowód relacji zMarysią. Pozostałe bez rodzinnego łącznika. Brak wypełnionych pól rodziców w indeksie nie wyklucza danych w aktach.']]
mail=json.loads((Z/'odpowiedzi_instytucji_wypisy.json').read_text())
titles={'S322':'Zarzew: sprzeczna data urodzenia Czesława w odpowiedzi','S323':'Zarzew: Czesława20XI1922–3X1999, XLV/1/19','S324':'Szczecińska: odmowa zgodności Janiny z porównywanym rekordem1910','S325':'WBP: negatywny wynik kwerendy prasowej Tomasza'}
for m in mail:
    sources.append([m['source'],titles[m['source']],'ODPOWIEDŹ INSTYTUCJI / WYPIS REDAKCYJNY',m['received_original'],m['people'],m['institution'],'Gmail message '+m['gmail_message_id'],m['url'],'ODCZYTANO CAŁĄ ODPOWIEDŹ; BEZ ODPISU AKTU',rel(Z/'odpowiedzi_instytucji_wypisy.json'),m['interpretation_and_limits']+' Oryginalnybodyhash i dataodczytu wewypisie; pełna prywatna kopia nie jest publikowana.'])
for s in sources:add('ZRODLA_I_SKANY',s)
setv('ZRODLA_I_SKANY','S272',9,'ETAP21:NAZWISKA2–247; ETAP33:NOWE KRYTERIUM ZYGM.136–247;10PEŁNYCH WIERSZY;1/248OBEJRZANO')
setv('ZRODLA_I_SKANY','S272',10,rel(Z/'S272_zakres_nowego_kryterium.json'))
appendv('ZRODLA_I_SKANY','S272',11,' Etap33:112obrazów1939ponownie pod nowym kryteriumZygm.; nie zaobserwowano trafienia. Wybrane10wierszy zDOB/adresem bez relacji. 1938nie powtórzono. Koniec16X1939; poświadczenie254stron nie dowodzi pełnego odwzorowania w248obrazachPTG. Daty sąsiednich osób nie są przenoszone między wierszami.')
appendv('ZRODLA_I_SKANY','S032',11,' Etap33:S324/9XI2026 administracja nie potwierdza tożsamości z JaninąPoprawką12V1910; nie podała odmiennych cech. Nie dopisywać zgonuP04.')
appendv('ZRODLA_I_SKANY','S158',11,' Etap33:S323/odpowiedź9XI2026 podaje DOB20XI1922 i ten samzgon3X1999. To daneC62, nie potwierdzonejP31; bez męża/syna/nazwiska rodowego.')

add('KANDYDACI_I_HOMONIMY',['C109','Zygm. — osoba we wspólnym wpisie ze Stanisławą Chmielewską','6XI1939,nr3693;bezDOB,wieku i roli','Osoba z wpisu; nieustalony związek zP11','Grabowa4→pow.Łask/gm.Buczek','NIEUTOŻSAMIONY — SKRÓT IMIENIA','Nazwisko nagłówka wspólnego wpisu toChmielewska. Zygmunt/Chmielewski są wariantami poszukiwawczymi, nie pełnym potwierdzonym imieniem/nazwiskiem tej osoby.','S320;S319;S274;H054','Dokument z pełnym imieniem, wiekiem i relacją; nie przypisywać automatycznie Stanisławie roli matki.',urls['25509'][165]])
setv('KANDYDACI_I_HOMONIMY','C10',6,'ODPOWIEDŹ Z DATĄ SPRZECZNĄ Z CHRONOLOGIĄ — DO WYJAŚNIENIA')
appendv('KANDYDACI_I_HOMONIMY','C10',7,' S322podaje18II1982jako urodzenie, choć pytano o zgon16I1981. Nie przyjętoDOB, nie poprawiono na1882; możliwa omyłka lub inny rekord.')
appendv('KANDYDACI_I_HOMONIMY','C10',8,';S322;Q107')
setv('KANDYDACI_I_HOMONIMY','C10',9,'Wyjaśnić niespójną odpowiedź9XI2026 lub uzyskać niezależny dokument dla właściwego grobu. C10/P03 i C11/P11 nadal niepotwierdzeni; bez nowego kontaktu bez osobnej zgody.')
setv('KANDYDACI_I_HOMONIMY','C17',6,'NIEZGODNA Z JANINĄ POPRAWKĄ12V1910 WEDŁUG ADMINISTRACJI')
appendv('KANDYDACI_I_HOMONIMY','C17',7,' S324/9XI2026: „Niestety nie jest to ta osoba” na pytanie z dokładnymDOB12V1910, rodzicami i nazwiskiemPoprawka. Nie podano alternatywnych danych zmarłej.')
appendv('KANDYDACI_I_HOMONIMY','C17',8,';S324')
setv('KANDYDACI_I_HOMONIMY','C17',9,'Nie utożsamiać z opisaną Janiną1910/P04. To wykluczenie administracyjne konkretnego porównania, nie odczyt aktu; H017 pozostaje osobną kwestią.')
setv('KANDYDACI_I_HOMONIMY','C62',3,'20.11.1922–03.10.1999; XLV/1/19; DOB z odpowiedzi administracji9XI2026')
setv('KANDYDACI_I_HOMONIMY','C62',6,'DATY Z EWIDENCJI CMENTARZA; TOŻSAMOŚĆ Z P31 OTWARTA')
appendv('KANDYDACI_I_HOMONIMY','C62',7,' S323podajeDOB20XI1922i zgon3X1999; innych danych w karcie zgonu administracja nie ma. Brak imienia męża/syna i nazwiska rodowego.')
appendv('KANDYDACI_I_HOMONIMY','C62',8,';S323;H055')
setv('KANDYDACI_I_HOMONIMY','C62',9,'Potwierdzić C62=P31 dodatkowym identyfikatorem rodzinnym, małżeństwem lub niezależnym przekazem. Nie przenosićDOB/zgonu naP31 i nie tworzyć relacji zRomanem lub synem zNiemiec.')

appendv('HIPOTEZY_OTWARTE','H002',3,' Etap33: C109„Zygm.”z3693ma zgodny adres i kierunek grupyStanisławy/IM025, lecz bezDOB lub relacji. Nadal brak imieniaP11. Nowe księgi nie ustaliły brata; nie scalić C109zP11.')
appendv('HIPOTEZY_OTWARTE','H054',3,' Etap33:S320,nr3693,6XI1939:Chmielewska/Stanisława iZygm.,1m+1k,Grabowa4→Łask/Buczek. Mocne dopasowanie odwrotnej drogi do708/IM025; nowy skrót imienia, nie relacja ani tożsamość zC105/P03/P11.')
setv('HIPOTEZY_OTWARTE','H054',5,'OTWARTA — MOCNE DOPASOWANIE GRUPY1939; ZWIĄZEK Z C105 I RODZINĄ NIEPOTWIERDZONY')
appendv('HIPOTEZY_OTWARTE','H005',3,' Etap33:S322,odpowiedź9XI2026 podaje18II1982jako urodzenie Czesława, sprzeczne ze zgonem1981w pytaniu. Nie przyjęto tej daty i nie poprawiono roku na1882. Brak danychWitolda; hipotezy nie zamknięto.')
appendv('HIPOTEZY_OTWARTE','H033',3,' S323dajeC62DOB20XI1922,nie tożsamość zP31; H055wydziela to porównanie. Brak męża i nazwiska rodowego nadal uniemożliwia potwierdzenie wariantu żony brata.')
add('HIPOTEZY_OTWARTE',['H055','Czy C62, Czesława20XI1922–3X1999, to ciocia Czesia P31?','S323: administracjaZarzewa podajeDOB i zgon dlaXLV/1/19. Imię,nazwisko,Łódź i przybliżone pokolenie pasują do przekazu, ale nie ma danych męża, syna, nazwiska rodowego ani innego rodzinnego identyfikatora. Nie potwierdzono pokrewieństwa.','Niezależny identyfikator rodzinny/aktmałżeństwa/odczyt własnego dokumentu z nazwiskiemrodowym i danymi męża. Nie wybierać Romana na podstawie przypuszczenia.','OTWARTA — OSOBNE REKORDY C62 I P31'])

for x in [
 ['Q107','SPRZECZNOŚĆ DATY W ODPOWIEDZI INSTYTUCJI','C10zgon16I1981 vs odpowiedź o urodzeniu18II1982','S322podaje1982dosłownie. Nie wpisano tej daty doDOB i nie zastąpiono jej1882. Możliwa omyłka/odmiennyrekord wymaga sprawdzenia.','PEWNA SPRZECZNOŚĆ; PRAWIDŁOWE DOB NIEUSTALONE','S322;S029;S122;H005','Nie zamykaćH005 ani nie utożsamiaćC10zP03 na podstawie niespójnej daty.',mail[0]['url']],
 ['Q108','NIEAKTUALNY STATUS KORESPONDENCJI','M09w bazie nadal SZKIC-NIEWYSŁANO','Pełnywątek zawiera SENT7XI2026 10:52:55UTC,ID1a1b5a3d597e4565; odpowiedź9XIwyklucza porównywaną Janinę. M11/Czesława8XI także już wysłany w historii, nie w tej sesji.','POTWIERDZONE LABEL SENT I ODPOWIEDZIĄ','S324;S323;M09;M11','Nie wysyłać powtórnie; ta sesja wyłącznie odczytała i uzupełniła rejestr.',mail[2]['url']],
 ['Q109','NIEAKTUALNY ZAKRES ZADANIA T58','T58wciąż podawało25508nazwiska1–95/184 i15575obrazy1–12','Etap27ukończył25508/1–184; etap28skorowidz15575nie dał odsyłacza do9a. Poprawiono stan zadania bez zmiany dawnych raportów.','POTWIERDZONE RAPORTAMI ETAPÓW27/28','S297;S300;T58','Nie rozpoczynać ponownie dawnych zakresów bez nowego kryterium.','badania/2026-11-07-sesja-28-Chelmonskiego/STATUS.md']]:add('KOREKTY_I_SPRZECZNOSCI',x)
add('ZDARZENIA_I_FAKTY',['E076','1922-11-20','C62','URODZENIE — DANE Z EWIDENCJI CMENTARNEJ','AdministracjaZarzewa podała20XI1922dlaCzesławy zXLV/1/19,zmarłej3X1999.','ODPOWIEDŹ INSTYTUCJI; NIE AKT URODZENIA','S323',mail[1]['url'],'DotyczyC62,nie potwierdzonej ciociP31.'])
add('ZDARZENIA_I_FAKTY',['E077','2026-11-09','C17;P04','WERYFIKACJA KANDYDATKI','AdministracjaSzczecińskiej stwierdziła brak zgodności kandydata4III1992z opisaną JaninąPoprawką12V1910.','ODPOWIEDŹ ADMINISTRACJI; BEZ ALTERNATYWNYCH DANYCH','S324',mail[2]['url'],'Nie jest to akt zgonu ani rozstrzygnięcieH017.'])
add('ZDARZENIA_I_FAKTY',['E078','1939-11-06','C109','OTRZYMANIE ZGŁOSZENIA WYJAZDU','Wpis3693:Chmielewska/Stanisława iZygm.,1m+1k,Grabowa4→Łask/Buczek.','ODCZYT WIERSZA; BEZ RELACJI RODZINNEJ','S320',urls['25509'][165],'Data otrzymania zgłoszenia,nie automatycznie dzień fizycznej podróży.'])

im=63
for book,src in [('25507','S318'),('25509','S319')]:
    for r in json.loads((Z/f'{book}_wybrane_odczyty.json').read_text()):
        ss='S320'if book=='25509'and r['entry']=='3693'else src
        text=f"{r['surname']} / {r['given_name']}; zgłoszenie{r['notice_received']}; {r['current_address']}→{r['next_place_or_death']}; {r['group']}. {r['note']} Brak potwierdzonej relacji z rodziną."
        add('INDEKS_MELDUNKOW',[f'IM{im:03}',ss,f'39/221/0/4.12/{book}',r['image'],r['entry'],text,r['url'],rel(Z/f'{book}_wybrane_odczyty.csv')]);im+=1
for r in json.loads((Z/'S272_wybrane_odczyty.json').read_text()):
    text=f"{r['name']}; ur.{r['dob']},{r['birthplace']}; dowód{r['identity_document_date']},{r['address']}. Nieutożsamiony z rodziną; bez wskazanych rodziców."
    add('INDEKS_MELDUNKOW',[f'IM{im:03}','S272','PTG4119/4120/86616',r['image'],r['entry'],text,r['url'],rel(Z/'S272_wybrane_odczyty.csv')]);im+=1
assert im==116

appendv('SZKICE_GMAIL','M03',7,' Etap33: odpowiedź9XIw tym samymwątku, S322; data urodzenia jest sprzeczna z pytaniem o zgon1981.')
setv('SZKICE_GMAIL','M10',5,'ODPOWIEDŹ9XI2026 ODEBRANA — NIESPÓJNA DATA, Q107')
appendv('SZKICE_GMAIL','M10',7,' S322:18II1982w odpowiedzi,bez danychWitolda. Bez nowej wysyłki w tej sesji.')
setv('SZKICE_GMAIL','M09',5,'WYSŁANO7XI2026; ODPOWIEDŹ9XI: NIEZGODNA KANDYDATKA')
setv('SZKICE_GMAIL','M09',6,'https://mail.google.com/mail/#all/1a1b5a3d597e4565')
appendv('SZKICE_GMAIL','M09',7,' Etap33/Q108: pełnywątek potwierdzaSENT10:52:55UTC; S324nie potwierdza Janiny1910. Nie wysłano ponownie.')
add('SZKICE_GMAIL',['M11','Zarzew — historyczne uzupełnienie o Czesławę1999','ckzarzew@zzm.lodz.pl','Dane Czesławy zXLV/1/19','WYSŁANO8XI2026; ODPOWIEDŹ9XI ODEBRANA','https://mail.google.com/mail/#all/1a1bd32bf7193992','Odczytany13XIrekordSENT22:06:21UTC,nie nowa wysyłka. S323:20XI1922–3X1999,bez innych danych. P31nie utożsamiona.'])
appendv('ZADANIA_AGENTA','T55',6,' Etap33:25507nazwiska142obrazy i25509nazwiska181obrazów zakończone; C109/Zygm.bez relacji. Nie powtarzać zakończonych kryteriów.')
setv('ZADANIA_AGENTA','T58',6,'Etapy27/28zakończone:25508nazwiska1–184; skorowidz15575bez odsyłacza do9a. C102/C103/C104/C105iH052/H053nadal bez pełnych identyfikatorów; nie wracać automatycznie do1–95 lub1–12.')
appendv('ZADANIA_AGENTA','T58',9,';S297;S300;Q109')
for row in [
 ['T60',2,'NOWY SKRÓT IMIENIA','Ewidencja ludności/Buczek','Ustalić pełne imię, nazwisko i wiek osobyZygm.z3693, bez przypisania doP11.','S320/H054;S272nowe kryterium136–247beztrafienia. RejestryBuczkuS298/S299bezskanów.','Agent','Wspólny zapis nie określa roli syna/męża; wieś nieznana.','S320;S272;H054;C109'],
 ['T61',1,'SPRZECZNA DATA ZARZEW','Istniejąca odpowiedź i niezależne dokumenty','Wyjaśnić właściwy rekord iDOB C10, zanim wykluczymy lub utożsamimy dziadka; nadal sprawdzaćWitolda osobno.','S322:18II1982sprzeczne zgon1981; brak prawidłowegoDOB i danychWitolda.','Agent','Nie poprawiać na1882bez źródła. Nowe kontakty tylko po osobnympoleceniu.','S322;Q107;H005'],
 ['T62',2,'C62 PO NOWYM DOB','Dokumenty rodzinne/już dostępne źródła','Porównać20XI1922z ciociąP31; ustalić nazwisko rodowe, męża lub syna.','H055otwarta;S323bez tych danych. S208urodzeniaTomaszowa1920–23już bezChmiel…; nie tworzyć siostry z wieku.','Agent','Sama zgodność imienia, miasta i pokolenia nie identyfikuje. PriorytetP11zachowany.','S323;H055;H033;S208'],
 ['T63',2,'TOMASZ — WBP ODPOWIEDŹ','Dostępne źródła inne niż powtórna ta sama prośba','Uwzględnić negatywną odpowiedźWBP i kontynuować dokumenty własneTomasza.','10XI2026:bez znalezionej wzmianki; brak pełnegoDOB/matki.','Agent','Nie ponawiać wysłanej kwerendy; nie przypisywać odpowiedzi pełnego pokrycia prasy lub braku rodziny.','S325;P09;TOM-D05']]:add('ZADANIA_AGENTA',row)

logs=[
 ('25507:149pobrań,142obrazy nazwisk5–103/105–147; wybrane24wiersze','Brak rozpoznanego Czesława/Janiny/Agnieszki i imieniaP11.','23III–31XII1937 plus dopiski; nie pełna transkrypcja wszystkich rubryk.','S318'),
 ('25509:187pobrań,181obrazy nazwisk4/6–185;19wybranychwierszy','Nowy3693:Stanisława iZygm.Grabowa4→Buczek.','2I–1XII1939,nie cały grudzień; bez nowej relacji rodzinnej.','S319;S320'),
 ('Porównanie3693/6XI1939z708/14III1939,IM025','Zgodne nazwisko wpisu,Stanisława,Grabowa4,Buczek,1m+1k; nowy skrót Zygm.','Nie ustala wieku/roli ani C105=P03/C109=P11.','S320;S274;H054'),
 ('Arolsen:nowy filtr naS313,43rekordy/42DocID;6nowychDocID/10obrazów','Numery kartDPłączą dwa spisy Zygmunta1905/Haliny1914/Zygmunta1943.','Brak połączenia zMarysią; indeksniepodaje rodziców,nie oznacza to braku w aktach.','S321;S313'),
 ('S272:nowywarunekZygm.,112obrazów136–247;10wybranychwierszy;1/248','Nie zaobserwowano ZygmuntaChmielewskiego; odczytano inneDOB/adresy.','Nie ponowiono1938pod nowym kryterium. Koniec16X1939.248obrazów vs poświadczenie254stron; nie pełna fizyczna księga.','S272'),
 ('14kwerend web Buczek/Grabowa4/Zygmunt oraz dwóch katalogowych ID','Brak nowego rodzinnego identyfikatora;6209050to1916–21;22561683Portletniedostępny.','Nie odczytano kart osób tych jednostek. Nie powtarzano już ustalonego inwentarzaBuczku.','S320;H054;S298;S299'),
 ('NowyDOB C62:4ścisłe kwerendy+2katalogowe; kontrola staregoS208','Brak identyfikatora rodziny z web. Lubgensodświeżenie503; użyto istniejącej dokumentacjiS208.','Nie szukano ponownie1281indeksów nazwiska; wybrany album1922jest prawosławny,nie przyjęto go za katolicki.','S323;S208'),
 ('Pełne wątkiGmailM03/M10/M11 iM09;4noweodpowiedzi','Potwierdzono historyczne SENTM09iM11oraz odpowiedzi9/10XI.','Wyłącznie odczyt; nie wysłano nowych wiadomości. Do publicznej kopii tylko wypisy bez prywatnych kontaktów.','S322;S323;S324;S325;Q108'),
 ('Zarzew:całaodpowiedź9XI08:25+01 i cytowanydokładnywniosek','DosłownieDOB18II1982dlaCzesława; chronologiczna sprzeczność zgon1981.','Nie poprawiono na1882ani nie ustawionoDOB.C11nadalbez danych.','S322;Q107;H005'),
 ('Zarzew:CzesławaXLV/1/19,odpowiedź9XI10:27+01','C62:20XI1922–3X1999; administracja nie ma więcej danych w karcie.','Nie jest to potwierdzenieC62=P31ani męża/syna.','S323;H055'),
 ('Szczecińska:Janina4III1992VIII/5/29,odpowiedź9XI','Administracja nie potwierdza tożsamości zJaninąPoprawką12V1910z pytania.','Nie ujawniono alternatywnych identyfikatorów; H017nie rozstrzygnięto.','S324;C17;Q108'),
 ('WBP:odpowiedź10XI12:34+01','Przeszukano DziennikŁódzkiWiadomościDnia oraz ExpressIlustrowany bez szukanej informacji.','Bez wykazu numerów/stron; nie dowodzi braku nekrologu w całej prasie ani braku krewnych.','S325;P09'),
 ('AudytGitHub:5gałęzi,120commitów,3627ścieżek,2337blobówtekstowych,PR/załączniki','PR1tylkodokumentacja;inboxprzed audytemtylkoREADME;workstarsze mapyobecne wmain.','Stan sprzed własnych commitów audytu. Raport na codex/audyt-repo-2026-11-13,nie nowe dowody genealogiczne.','https://github.com/maciekkoz-PL/drzewo-genealogiczne/blob/codex/audyt-repo-2026-11-13/agent-inbox/2026-11-13-codex-audyt-github/RAPORT.md'),
 ('15powiadomieńGitHub o sesjach jednegozadania;14completed/1cancelled','Ustalono linki ReviewingClaude/UpdatingClaudeslog/Creatingfolder; treści sesji nie odczytano.','Dostępne web i autoryzowanyGETzwracają404. Zakończenie sesji nie jest potwierdzeniem commita lub odkrycia.','https://github.com/maciekkoz-PL/drzewo-genealogiczne/blob/codex/audyt-repo-2026-11-13/agent-inbox/2026-11-13-codex-audyt-github/UZUPELNIENIE_SESJE_AGENTOW.md'),
 ('Kontrola powtórek i miejsca na dysku','Usunięto wyłącznie odtwarzalne,ignorowane kopie z potwierdzonymiSHA; zakres porzadkowanie_cache.json.','Zachowane wszystkie zatwierdzone pliki,wybraneoryginały,przejrzane kolumny i kompletURL/SHA.','S318;S319;porzadkowanie_cache.json')]
for i,(scope,result,limit,src)in enumerate(logs,322):add('DZIENNIK_KWEREND',[f'L{i}',now,scope,result,limit,src+';'+rel(D/'STATUS.md')])

files=[(B,'Git:08b5991','ARCHIWUM STANU BAZY')]
for f in sorted(Z.rglob('*')):
    if not f.is_file():continue
    name=f.name
    src='S318'if name.startswith('25507')else'S320;S319'if name=='25509_165.jpg'else'S319'if name.startswith('25509')else'S272'if name.startswith(('86616','S272'))else'S321;S313'if name.startswith('arolsen')or'arolsen_zygmunt'in f.parts else'S322;S323;S324;S325'if name.startswith('odpowiedzi_instytucji')else'S322;S323;S324'if name.startswith('potwierdzone_wysylki')else'L327;L328;L336'
    files.append((f,src,'ORYGINALNY SKAN'if f.suffix.lower()=='.jpg'else'KOPIA/INDEKS/ZAKRES LUB LOG'))
for i,(f,src,typ)in enumerate(files,472):add('PLIKI_DOWODOWE',[f'F{i}',rel(f),typ,src,f.name,'SHA256 '+hashlib.sha256(f.read_bytes()).hexdigest()])
add('INSTRUKCJA_AGENTA',['G30','ETAP33 — KSIĘGI I ODPOWIEDZI; AUDYT GITHUB',rel(D/'STATUS.md')+';'+rel(D/'PLAN_KONTYNUACJI.md')+'. S320/C109Zygm.bez relacji. S323/C62maDOB20XI1922,nieP31. S324/C17niepasujedoJaniny1910. S322/C10data1982sprzeczna,bezsamowolnejkorekty;Witoldbezrodziców. M09/M11wysłanewhistorii,nieponawiać. P11nadalbezimienia. Fetchwszystkichgałęzi;powiadomieniasesjizlinkaminieodczytane404. Braknowychkontaktów.'])
cell('START','A2','Etap33(8–13XI2026): nowyZygm.zGrabowej4bezrelacji; C62DOB20XI1922,nieutożsamionazCzesią; C17niezgodnazJaniną1910; odpowiedźoCzesławie1982sprzeczna. P11nadalbezimienia. Aktualnyraporti plan:badania/2026-11-08-sesja-33-wyjazdy-1937/.')
cell('INSTRUKCJA_AGENTA','A2','Etap33: najpierwSTATUS iPLAN_KONTYNUACJI z8–13XI2026. Źródła doS325; noweodpowiedzi nie są nową relacją. P11/P10/P09priorytet; beznowychkontaktów. Starszeinstrukcjeponiżejzachowująhistorię.')
cell('ZRODLA_I_SKANY','A2','325 rekordów źródeł; nie325niezależnychdowodów. S320wpiswS319, S306aliasS041. Etap33beznowegopokrewieństwa.')
cell('KANDYDACI_I_HOMONIMY','A2','109 rekordów; C109toZygm.beztożsamości. C62maDOBzadministracji,niejestprzeztoP31. C17niepasujedoJaniny1910; C10datawodpowiedziniespójna.')
cell('INDEKS_MELDUNKOW','A2','115wybranychodczytów; niepełnyindeks inielistakrewnych. IM063–115:księgi25507/25509oraz10wybranychdowodówS272.')
tmp=P.with_name(P.stem+'.etap33.tmp.xlsx');w.save(tmp);openpyxl.load_workbook(tmp).close();tmp.replace(P)
(D/'ZMIANY_KOMOREK.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
counts={}
for sn,pat in [('ZRODLA_I_SKANY',r'S\d+'),('DZIENNIK_KWEREND',r'L\d+'),('KANDYDACI_I_HOMONIMY',r'C\d+'),('PLIKI_DOWODOWE',r'F\d+'),('INDEKS_MELDUNKOW',r'IM\d+')]:counts[sn]=sum(isinstance(r[0],str)and bool(re.fullmatch(pat,r[0]))for r in w[sn].values)
(D/'LICZNIKI.json').write_text(json.dumps(dict(at_utc=now,sheets=len(w.sheetnames),counts=counts,changed_existing_cells=len(edits),last_source='S325',last_log='L336',last_file=f'F{471+len(files)}',last_candidate='C109',last_correction='Q109',last_meldunkowy='IM115',new_proven_family_relationships=0),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False));print('Zapisano',len(edits),'zmian istniejących komórek; bez nowych relacji rodzinnych.')
