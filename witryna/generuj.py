"""Publiczny widok z jawnie wybranymi polami; bez kopiowania prywatnego Excela."""
from pathlib import Path
import json,subprocess,datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[1];HERE=Path(__file__).resolve().parent
def person(id,name,role,dates,place,note,source,x,y,status='document'):
 return dict(id=id,name=name,role=role,dates=dates,place=place,note=note,source=source,x=x,y=y,status=status)
people=[
person('P05','Wincenty Chmielewski','Ojciec Czesława','Ślub: 25.06.1905','Rachanie → Rogoźno','Młynarz. Wiek podany w kolejnych aktach nie wyznacza dokładnej daty urodzenia. Przyporządkowanie tej gałęzi do Bogusława nadal sprawdzamy.',['S071','S072'],70,40),
person('P06','Agnieszka Miszczyszyn','Matka Czesława','Ślub: 25.06.1905','Rogoźno','Po ślubie Chmielewska. W aktach urodzeń Czesława i Romana podano tych samych obojga rodziców. Przyporządkowanie gałęzi do Bogusława nadal sprawdzamy.',['S071','S072'],350,40),
person('P07','Józef Poprawka','Ojciec Janiny','29 lat w akcie z 1910 r.','Socha · parafia Warta','Wyrobnik. Wiek pochodzi z aktu urodzenia córki, nie z jego własnego aktu urodzenia. Gałąź pozostaje objęta dodatkową weryfikacją.',['S063'],980,40),
person('P08','Marianna Kacprzak','Matka Janiny','27 lat w akcie z 1910 r.','Socha · parafia Warta','Po ślubie Poprawka. Nie znamy jej dokładnej daty urodzenia. Gałąź pozostaje objęta dodatkową weryfikacją.',['S063'],1260,40),
person('P12','Roman Chmielewski','Brat Czesława','Ur. 06.06.1919','Rogoźno','Syn Wincentego i Agnieszki Miszczyszyn. Braterstwo z Czesławem potwierdzono przez porównanie obu aktów urodzenia. Roman nie jest bratem Bogusława.',['S061','S071'],70,260),
person('P03','Czesław Chmielewski','Ojciec Bogusława — nazwisko w odpisie','Ur. 03.07.1909*','Rogoźno → Łódź','Odpis ślubu Bogusława wymienia ojca Czesława Chmielewskiego. Data 1909 pochodzi z osobnego aktu, powiązanego ze ślubem pary w 1936 r. *Dodatkowe potwierdzenie, że to dokładnie ta osoba, pozostaje otwarte (H017). Ślub z Janiną: 03.05.1936, Łódź, akt 110.',['S086','S001','S071'],490,260,'identity'),
person('P04','Janina Poprawka','Matka Bogusława — nazwisko w odpisie','Ur. 12.05.1910*','Socha → Łódź','Odpis ślubu Bogusława wymienia matkę Janinę, z domu Poprawkę. Data 1910 pochodzi z osobnego aktu, powiązanego ze ślubem pary w 1936 r. *Dodatkowe potwierdzenie, że to dokładnie ta osoba, pozostaje otwarte (H017). Po ślubie Chmielewska.',['S086','S001','S063'],840,260,'identity'),
person('P11','Brat Bogusława','Imię pozostaje nieznane','Daty nieustalone','', 'Według przekazu rodzinnego Bogusław miał brata, który był ojcem kuzyna Marysi. Brak dokumentu potwierdzającego tę relację. Nie przypisujemy mu imienia na podstawie grobów ani zbieżności nazwiska.',['REL'],140,510,'family'),
person('P02','Bogusław Kazimierz Chmielewski','Tata Marysi','25.04.1943 – 1988†','Łódź','Odpis ślubu potwierdza urodzenie 25.04.1943 w Łodzi i podaje rodziców: Czesława Chmielewskiego oraz Janinę Poprawkę. Ślub w Warszawie 13.11.1982; adnotacja rozwodu z 23.04.1985. †Zgon w 1988 r. pochodzi z przekazu rodzinnego i nadal wymaga dokumentu.',['S086','REL'],620,510),
person('P17','Maria Jankowska','Mama Marysi','Ur. 04.01.1942','Strzegowo · pow. mławski','Mama Marysi, zgodnie z potwierdzeniem rodziny. S086 podaje imię, nazwisko rodowe Jankowska, urodzenie oraz rodziców Romana Jankowskiego i Annę z domu Kulas. Ślub z Bogusławem: 13.11.1982 Warszawa; po ślubie Chmielewska, rozwód 23.04.1985. Macierzyństwo wobec Marysi i rodzeństwo pochodzą z przekazu rodzinnego: Maria najstarsza, Andrzej około 1946, Teresa około 1950. Maria żyje według przekazu; obecnie używane nazwisko nieustalone. Strzegowo pow. mławski jest odrębne od Strzegowej pow. olkuski.',['S086','REL-009','REL-011'],0,0,'document'),
person('P10','Piotr Chmielewski','Kuzyn Marysi — według przekazu','Ur. ok. 1969–1973†','', 'Syn nieznanego z imienia brata Bogusława — według relacji rodziny. †Przedział urodzenia to oszacowanie na podstawie przybliżonego wieku, a nie odczyt z aktu. Rodzina pamięta jego udział w mundurze policjanta w pogrzebie Tomasza w 2001 r. Nie potwierdzono, czy jest osobą opisaną w artykułach o policjancie z Łodzi. Pokrewieństwo nadal wymaga dokumentów.',['REL'],140,760,'family'),
person('P09','Tomasz Chmielewski','Przyrodni brat Marysi','Zm. 26.04.2001† · 30 lat','', 'Imię, nazwisko, dzień 26 IV i wiek odczytano z rodzinnych fotografii nagrobka. †Rok 2001 oraz relacja ojciec–syn z Bogusławem pochodzą z przekazu rodzinnego; rok na zdjęciu jest częściowo zasłonięty. Nie znamy dokładnej daty urodzenia.',['S027','REL'],510,760,'family'),
person('P01','Marysia','Córka Bogusława i Marii','Ur. ok. 1984†','','Rodzice Marysi to Bogusław Kazimierz Chmielewski i Maria Jankowska — potwierdzone przez rodzinę. Te połączenia są zawsze widoczne w drzewie. †Przybliżony rok urodzenia pochodzi z historii rodzinnej. Nie ustalono jej pełnego imienia i nazwiska.',['REL-011'],1080,1040,'family'),
person('C42','Czesław Chmielewski','Możliwy brat Bogusława','Zm. 03.02.1940 · 8 dni','Łódź','Odnaleziony akt zgonu 66/1940 parafii św. Anny w Łodzi wymienia rodziców: Czesława i Janinę z Poprawskich. Bogusław ma w swoim odpisie ślubu rodziców Czesława i Janinę Poprawkę. Podobne dane uzasadniają sprawdzenie, ale różnica nazwiska matki i brak dat urodzenia rodziców nie pozwalają jeszcze potwierdzić braterstwa. Linia w pełnym widoku oznacza tylko hipotezę. Dziecko zmarło jako niemowlę i nie jest poszukiwanym ojcem Piotra. Dokładna data urodzenia nie została odczytana z aktu.',['S126','S086'],1280,510,'candidate'),
person('P18','Roman Jankowski','Ojciec Marii · strona mamy','Zm. 29.05.2002‡ · 88 lat','Strzegowo · według rodziny','Ojciec Marii jest wskazany wprost w S086. Józef i Czesława Jankowscy są jego rodzicami według bezpośredniego potwierdzenia rodziny. Małżeństwo z Anną i dzieci Maria, Andrzej, Teresa pochodzą z przekazu rodzinnego. ‡Datę zgonu i wiek odczytano z dostarczonego zdjęcia nagrobka, zachowanego prywatnie. Urodzenie około 1913/1914 jest tylko wyliczeniem z wieku, miejsce urodzenia nieznane. Nie jest Romanem Chmielewskim P12.',['S086','S135','REL-009','REL-012'],0,0),
person('P19','Anna Kulas','Matka Marii · strona mamy','Zm. 28.09.1978‡ · 68 lat','Strzegowo · według rodziny','S086 wskazuje Annę i nazwisko rodowe Kulas jako matkę Marii. Jankowska po ślubie, małżeństwo z Romanem i dzieci Maria, Andrzej, Teresa — według przekazu. ‡Zgon i wiek odczytano z otrzymanego zdjęcia nagrobka, zachowanego prywatnie. Urodzenie około 1909/1910 tylko z wieku. Rodzice Józef i Konstancja Kulas pochodzą z przekazu. Nie utożsamiono Anny z Julianną Anną Kulas z indeksu 18/1910.',['S086','S135','REL-009','REL-010'],0,0),
person('C02','Julianna Chmielewska','Możliwa siostra Czesława','Ur. 1907 · akt 360','Tomaszów Lubelski','Kandydatka z indeksu urodzeń. Zbieżne nazwisko, parafia i epoka to jedyna dotychczasowa podstawa sprawdzenia. Rodzice nie zostali odczytani, więc pokrewieństwo z Czesławem pozostaje słabą hipotezą. Nie ustalono związku z Tczewem ani tego, czy to osoba wspominana przez rodzinę.',['S007'],0,0,'candidate'),
person('C04','Sabina Chmielewska','Możliwa siostra Czesława','Ur. 1917 · akt 124','Tomaszów Lubelski','Kandydatka z indeksu urodzeń. Rodzice nie zostali odczytani. Wspólne nazwisko i parafia nie potwierdzają siostrzeństwa z Czesławem. Nie ustalono związku z Tczewem ani tożsamości z siostrami ze wspomnienia rodziny.',['S009'],0,0,'candidate'),
person('C25','Józef Poprawka','Możliwy brat Janiny','Ur. 15.05.1918 · akt 64','Socha · parafia Warta','Akt urodzenia odczytano: rodzice Józef, lat 39, i Marianna z Kasprzaków, lat 28. Imiona, podobne nazwisko rodowe matki i Socha przypominają dane rodziców Janiny. Wiek matki nie zgadza się jednak z prostą kontynuacją aktu Janiny z 1910 r. Potrzebny dowód ciągłości rodziny; nie wykluczono homonimów lub drugiej żony. Braterstwo niepotwierdzone.',['S065','S063'],0,0,'candidate'),
person('C26','Kazimiera Poprawka','Możliwa siostra Janiny','Ur. 11.02.1916 · akt 13','Włyń · parafia Kamionacz','Akt urodzenia odczytano: rodzice Józef, lat 33, i Marianna Kacprzak, lat 27. Zgodność imion i nazwisk uzasadnia sprawdzenie siostrzeństwa z Janiną, ale rozbieżne wieki rodziców wymagają wyjaśnienia. Pokrewieństwo niepotwierdzone. Nie ustalono związku z Tczewem.',['S066','S063'],0,0,'candidate'),
person('C11','Witold Chmielewski','Możliwy brat · trop grobowy','Zm. 22.08.2003','Łódź · Zarzew','W miejskim rejestrze spoczywa w jednym grobie z Czesławem Chmielewskim zmarłym 16.01.1981 r. Nie znamy dat urodzenia ani pokrewieństwa tych osób i nie ustalono, że pochowany Czesław to ojciec Bogusława. Hipoteza o Witoldzie jako bracie Bogusława jest niepotwierdzona. Nie utożsamiamy go z nieznanym ojcem Piotra.',['S122'],0,0,'candidate')]

people += [
person('P20','Andrzej Jankowski','Brat Marii · przekaz rodzinny','Ur. około 1946†','','Według rodziny syn Romana Jankowskiego i Anny z domu Kulas, brat Marii i Teresy. †Rok orientacyjny z przekazu, nie z metryki. Nie ustalono dokładnej daty, miejsca urodzenia ani obecnego stanu życia.',['REL-009'],0,0,'family'),
person('P21','Teresa Jankowska','Siostra Marii · przekaz rodzinny','Ur. około 1950†','','Według rodziny córka Romana Jankowskiego i Anny z domu Kulas, siostra Marii i Andrzeja. †Rok orientacyjny z przekazu, nie z metryki. Dokładna data, miejsce urodzenia, obecne nazwisko i stan życia nieustalone.',['REL-009'],0,0,'family'),
person('P22','Józef Kulas','Ojciec Anny · według rodziny','Daty nieustalone','','Ojciec Anny i mąż Konstancji według przekazu rodzinnego. W Strzegowie odczytano indeksy urodzenia Józefa 55/1859 oraz ślubu Józefa Kulasa i Konstancji Gralewicz 16/1894. Nie odczytano tych aktów i nie dowiedziono tożsamości indeksowej pary z rodzicami Anny. Roku 1859 nie przypisujemy jako jego ustalonej daty urodzenia.',['REL-010','S129','S130'],0,0,'family'),
person('P23','Konstancja Kulas','Matka Anny · według rodziny','Daty nieustalone','','Matka Anny i żona Józefa według przekazu. Nazwisko rodowe Gralewicz jest propozycją z indeksów, nie ustaloną tożsamością Konstancji z rodziny. Indeks 60/1873 podaje Konstancję Gralewicz z Prusocina w parafii Strzegowo, rodziców Macieja i Teresę Dąbrowską. Brakuje własnego aktu Anny jako łącznika. Nie przypisano jej daty 1873 ani indeksowanych przodków jako pewnych.',['REL-010','S129','S131'],0,0,'family')]
people += [
person('P24','Józef Jankowski','Pradziadek Marysi · ojciec Romana','Zm. 30.09.1967‡ · 81 lat','Strzegowo · według rodziny','Pradziadek Marysi i ojciec Romana według bezpośredniego potwierdzenia rodziny. ‡Datę zgonu i wiek odczytano z dostarczonego zdjęcia nagrobka. Urodzenie około 1885/1886 to wyliczenie z wieku, nie dokładna data. Nazwiska rodowego i aktu ślubu Czesławy nie ustalono; sam wspólny nagrobek nie dokumentuje małżeństwa. Zdjęcie jest zachowane prywatnie.',['REL-012','S135'],540,1800,'family'),
person('P25','Czesława Jankowska','Prababcia Marysi · matka Romana','Zm. 03.01.1982‡ · 98 lat','Strzegowo · według rodziny','Prababcia Marysi i matka Romana według bezpośredniego potwierdzenia rodziny. ‡Datę zgonu i wiek odczytano z dostarczonego zdjęcia nagrobka. Urodzenie około 1883/1884 tylko z wieku. Jej nazwisko rodowe pozostaje nieustalone; nie odczytano własnych aktów. Zdjęcie potwierdza inskrypcję, a pokrewieństwo pochodzi od rodziny.',['REL-012','S135'],800,1800,'family'),
person('C45','Julianna Anna Kulas','Kandydatka do identyfikacji Anny','1910? · trop 18/1910','','Odczytano indeks urodzenia 18/1910 w parafii Strzegowo: Julianna Anna Kulas, rodzice Józef i Konstancja Gralewicz. Nie odczytano oryginalnego aktu ani nie ustalono, że to Anna Kulas/Jankowska, babcia Marysi. To osobny rekord. Linia oznacza możliwą tożsamość, a nie dodatkowe dziecko Anny.',['S132'],1820,1520,'candidate'),
]
layout={'P05': (560, 40),
 'P06': (820, 40),
 'P07': (1550, 40),
 'P08': (1810, 40),
 'C02': (20, 280),
 'C04': (280, 280),
 'P12': (540, 280),
 'P03': (800, 280),
 'P04': (1180, 280),
 'C25': (1440, 280),
 'C26': (1700, 280),
 'C11': (280, 560),
 'C42': (540, 560),
 'P11': (800, 560),
 'P02': (1080, 560),
 'P10': (800, 800),
 'P09': (1360, 800),
 'P01': (1080, 1040),
 'P17': (1080, 1280),
 'P20': (540, 1280),
 'P21': (800, 1280),
 'P18': (920, 1520),
 'P19': (1240, 1520),
 'C45': (1820, 1520),
 'P24': (540, 1800),
 'P25': (800, 1800),
 'P22': (1280, 1800),
 'P23': (1540, 1800)}
for p in people:
 if p['id'] in ['P17','P09']:p['status']='document'
 p['x'],p['y']=layout[p['id']]
 p['branch']='maternal' if p['id'] in ['P17','P18','P19','P20','P21','P22','P23','P24','P25','C45'] else 'both' if p['id']=='P01' else 'paternal'
 p['evidence']='hypothesis' if p['status']=='candidate' else 'family' if p['status']=='family' else 'document'
edges=[('P05','P03','document'),('P06','P03','document'),('P05','P12','document'),('P06','P12','document'),('P07','P04','document'),('P08','P04','document'),('P03','P02','identity'),('P04','P02','identity'),('P02','P01','family'),('P17','P01','family'),('P02','P09','family'),('P11','P10','family'),('P02','P11','sibling'),('P03','P04','marriage'),('P02','P17','marriage')]
edges += [('P18','P17','document'),('P19','P17','document'),('P03','C02','hypothesis'),('P03','C04','hypothesis'),('P04','C25','hypothesis'),('P04','C26','hypothesis'),('P02','C11','hypothesis'),('P02','C42','hypothesis')]
edges += [('P18','P19','family'),('P18','P20','family'),('P19','P20','family'),('P18','P21','family'),('P19','P21','family'),('P22','P19','family'),('P23','P19','family'),('P22','P23','family')]
edges=[(a,b,'parent' if (a,b) in [('P02','P01'),('P17','P01')] else 'family_marriage' if (a,b) in [('P18','P19'),('P22','P23')] else kind) for a,b,kind in edges]
edges += [('P24','P18','family'),('P25','P18','family'),('P19','C45','identity_candidate')]
sources={
'S086':dict(title='Odpis ślubu Bogusława, II-1592/1982',description='Fotografia przekazana przez rodzinę. Rodzice podani wprost; brak ich dat urodzenia. Dokument rodzinny nie jest publikowany.'),
'S001':dict(title='Ślub Czesława i Janiny, 110/1936',url='https://metryki.genealodzy.pl/index.php?id=424&kt=1&op=pg&plik=110-111.jpg&sy=1936b'),
'S071':dict(title='Urodzenie Czesława, 241/1909',url='https://www.szukajwarchiwach.gov.pl/skan/-/skan/6aa38cb05d670e37063fcdcdc8ce213457bd7672b1512d02656f2d1511cd3850'),
'S063':dict(title='Urodzenie Janiny Poprawki, 112/1910',url='https://skanoteka.genealodzy.pl/index.php?op=pg&id=485&sy=1910&kt=1&plik=111-114.jpg'),
'S061':dict(title='Urodzenie Romana, 226/1919',url='https://www.szukajwarchiwach.gov.pl/skan/-/skan/72ccf13401f1f049671583da77d2ba2fbe8052b0b23e9c32947409e8a47a15de'),
'S072':dict(title='Ślub Wincentego i Agnieszki, 73/1905',url='https://www.szukajwarchiwach.gov.pl/skan/-/skan/dbb6a2471faf0ab42508c0137fe95345b21621cb60c79d996476849a7c762a5e'),
'S027':dict(title='Fotografie nagrobka Tomasza',description='Fotografie rodzinne, niepublikowane w tym widoku.'),
'S126':dict(title='Zgon Czesława, 66/1940, Łódź św. Anna',url='https://metryki.genealodzy.pl/index.php?op=pg&id=454&sy=1940c&kt=1&plik=063-066.jpg',description='Akt w prawym dolnym rogu skanu. Potwierdza dane dziecka i zapis rodziców; jego pokrewieństwo z Bogusławem pozostaje do sprawdzenia.'),
'S007':dict(title='Indeks urodzeń: Julianna, 360/1907',url='https://regestry.lubgens.eu/druk_usz_v2_1.php?par=47&act=u&decade=190',description='Indeks, nie odczyt aktu. Rodzice i pokrewieństwo nieustalone.'),
'S009':dict(title='Indeks urodzeń: Sabina, 124/1917',url='https://regestry.lubgens.eu/druk_usz_v2_1.php?par=47&act=u&decade=191',description='Indeks, nie odczyt aktu. Rodzice i pokrewieństwo nieustalone.'),
'S065':dict(title='Urodzenie Józefa, 64/1918, Warta',url='https://skanoteka.genealodzy.pl/index.php?op=pg&id=485&sy=1918&kt=1&plik=063-066.jpg'),
'S066':dict(title='Urodzenie Kazimiery, 13/1916, Kamionacz',url='https://skanoteka.genealodzy.pl/index.php?op=pg&id=301&sy=1916&kt=1&plik=011-014.jpg'),
'S122':dict(title='Miejski rejestr: wspólny grób Czesława i Witolda',url='https://www.cmentarzekomunalne.lodz.systkom.pl/mapa.html?gv=4427&cm=ZARZW',description='Zarzew XXXVI-15-36. Współpochówek nie potwierdza pokrewieństwa.'),
'REL':dict(title='Przekaz rodzinny',description='Informacja od rodziny; nie zastępuje dokumentu potwierdzającego pokrewieństwo.')}
sources.update({'S128': {'title': 'Grób Jankowskich — przekazany odczyt czterech inskrypcji', 'description': 'Józef: 30.09.1967, 81 lat; Anna: 28.09.1978, 68 lat; Roman: 29.05.2002, 88 lat; Czesława: 03.01.1982, 98 lat. Ave Maria to napis religijny. Oczekuje na oryginalny JPEG; w tej sesji odczytano transkrypcję z pakietu. Nagrobek nie potwierdza pokrewieństwa ani nazwisk rodowych, lokalizacja Strzegowo pochodzi z przekazu. Fotografia nie jest publikowana.'}, 'REL-009': {'title': 'Przekaz rodzinny o rodzinie Jankowskich', 'description': 'Przekaz odtworzony w pakiecie: Roman i Anna ze Strzegowa, dzieci Maria, Andrzej około 1946 i Teresa około 1950. Bez metryk rodzeństwa i własnego ślubu pary.'}, 'REL-010': {'title': 'Przekaz rodzinny o Józefie i Konstancji Kulasach', 'description': 'Rodzice Anny według rodziny; brak aktu łączącego ich z parą Kulas/Gralewicz z indeksów.'}, 'S129': {'title': 'Indeks ślubu Kulas/Gralewicz, 16/1894, Strzegowo', 'url': 'https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=07mz&rid=5728&search_lastname=Kulas&search_lastname2=Gralewicz&from_date=1894&to_date=1894', 'description': 'Odczytano wiersz indeksu, nie oryginalny akt. Nie potwierdza tożsamości z rodzicami Anny.'}, 'S130': {'title': 'Indeks urodzenia Józefa Kulasa, 55/1859', 'url': 'https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=07mz&rid=5727&bdm=B&search_lastname=Kulas&from_date=1859&to_date=1859', 'description': 'Odczytano wiersz indeksu, nie oryginalny akt. Nie potwierdza tożsamości z rodzicami Anny.'}, 'S131': {'title': 'Indeks urodzenia Konstancji Gralewicz, 60/1873', 'url': 'https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=07mz&rid=5727&bdm=B&search_lastname=Gralewicz&from_date=1873&to_date=1873', 'description': 'Odczytano wiersz indeksu, nie oryginalny akt. Nie potwierdza tożsamości z rodzicami Anny.'}})
sources.update({'REL-011': {'title': 'Rodzice Marysi — potwierdzenie rodziny', 'description': 'Bogusław jest tatą Marysi, Maria jej mamą. Te znane rodzinie połączenia są stale widoczne w obu trybach, bez uzależnienia od pozyskania aktu Marysi.'}, 'S132': {'title': 'Indeks Julianny Anny Kulas, 18/1910, Strzegowo', 'url': 'https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=07mz&rid=5727&bdm=B&search_lastname=Kulas&from_date=1910&to_date=1910', 'description': 'Odczytano wiersz indeksu, nie oryginalny akt. Tożsamość z Anną Jankowską pozostaje niepotwierdzona.'}})
sources.update({'S128': {'title': 'Grób Jankowskich — wcześniejsza transkrypcja', 'description': 'Transkrypcję przekazaną w pakiecie porównano z dostarczonym później zdjęciem S135; daty i wiek są zgodne. To zapis wcześniejszego etapu.'}, 'S135': {'title': 'Fotografia nagrobka Jankowskich — odczytana, zachowana prywatnie', 'description': 'Józef: 30.09.1967, 81 lat; Anna: 28.09.1978, 68 lat; Roman: 29.05.2002, 88 lat; Czesława: 03.01.1982, 98 lat. Obraz otrzymano i odczytano. Ave Maria to napis religijny. Płyta nie podaje pokrewieństwa ani nazwisk rodowych. Zdjęcia nie publikujemy.'}, 'REL-012': {'title': 'Pradziadkowie Marysi — bezpośrednie potwierdzenie rodziny', 'description': 'Rodzina wskazała Józefa i Czesławę jako pradziadków Marysi; w omawianej gałęzi są rodzicami Romana Jankowskiego. Pokrewieństwo pochodzi z przekazu, nie z samego nagrobka.'}})
events=[
('309edd1da848f3ae1bd3446e6a247e2cc027524f','Uzupełniono rodzinę mamy i potwierdzenie pradziadków','Rodzina potwierdziła Józefa i Czesławę jako pradziadków Marysi, rodziców Romana. Dostarczone zdjęcie potwierdza cztery inskrypcje; wcześniejsze dane rodzeństwa Marii i linii Kulas zachowują swoje źródła.','uzupełnienie'),
('2843053','Odnaleziono akt możliwego brata Bogusława','Czesław zmarł w Łodzi 3 lutego 1940 r., mając osiem dni. Rodziców zapisano jako Czesława i Janinę z Poprawskich; pokrewieństwo z rodziną wymaga potwierdzenia.','ważny akt'),
('ea0d189','Potwierdzono nazwiska rodziców Bogusława','Jego odpis ślubu wskazuje Czesława Chmielewskiego i Janinę Poprawkę.','odkrycie'),
('e2b9c5c','Potwierdzono urodzenie Czesława i jego brata Romana','Akt z 1909 r. pozwolił ustalić datę urodzenia Czesława i potwierdzić wspólnych rodziców obu braci.','odkrycie'),
('4108653','Odnaleziono akt urodzenia Janiny Poprawki','Akt z 1910 r. wskazuje jej rodziców: Józefa Poprawkę i Mariannę Kacprzak.','odkrycie')]
news=[]
for commit,title,body,kind in events:
 stamp=subprocess.check_output(['git','show','-s','--format=%cI',commit],cwd=ROOT,text=True).strip()
 news.append(dict(at=stamp,title=title,body=body,kind=kind))
data=dict(people=people,edges=edges,sources=sources,news=news,updated=max(x['at'] for x in news),generated=datetime.datetime.now(datetime.timezone.utc).isoformat())
(HERE/'public').mkdir(exist_ok=True)
template=(HERE/'szablon.html').read_text()
(HERE/'public/index.html').write_text(template.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')).replace('__SCRIPT__',(HERE/'interakcje.js').read_text()))
print('Publiczny widok:',len(people),'osób,',len(news),'wpisów; znane dane rodzinne i rozdzielone poziomy dowodu.')
