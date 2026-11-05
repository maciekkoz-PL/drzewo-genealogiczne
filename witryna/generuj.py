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
person('P17','Mama Marysi','Dane osobowe ograniczone','', '', 'Małżeństwo z Bogusławem dokumentuje odpis z 1982 r. Macierzyństwo wobec Marysi wynika z kontekstu przekazu rodzinnego. W publicznym widoku nie publikujemy jej nazwiska ani daty urodzenia.',['S086','REL'],1030,510,'family'),
person('P10','Kuzyn Marysi','Według przekazu rodzinnego','', '', 'Syn nieznanego z imienia brata Bogusława — według relacji rodziny. Tożsamość i pokrewieństwo nie zostały potwierdzone dokumentami. Dane żyjącej osoby pominięto.',['REL'],140,760,'family'),
person('P09','Tomasz Chmielewski','Przyrodni brat Marysi','Zm. 26.04.2001† · 30 lat','', 'Imię, nazwisko, dzień 26 IV i wiek odczytano z rodzinnych fotografii nagrobka. †Rok 2001 oraz relacja ojciec–syn z Bogusławem pochodzą z przekazu rodzinnego; rok na zdjęciu jest częściowo zasłonięty. Nie znamy dokładnej daty urodzenia.',['S027','REL'],510,760,'family'),
person('P01','Marysia','Od niej zaczyna się ta opowieść','', '', 'Córka Bogusława według przekazu rodzinnego. Publiczny widok zawiera tylko imię, bez daty urodzenia, nazwiska i miejsca zamieszkania.',['REL'],970,760,'family')]
edges=[('P05','P03','document'),('P06','P03','document'),('P05','P12','document'),('P06','P12','document'),('P07','P04','document'),('P08','P04','document'),('P03','P02','identity'),('P04','P02','identity'),('P02','P01','family'),('P17','P01','family'),('P02','P09','family'),('P11','P10','family'),('P02','P11','sibling'),('P03','P04','marriage'),('P02','P17','marriage')]
sources={
'S086':dict(title='Odpis ślubu Bogusława, II-1592/1982',description='Fotografia przekazana przez rodzinę. Rodzice podani wprost; brak ich dat urodzenia. Dokument rodzinny nie jest publikowany.'),
'S001':dict(title='Ślub Czesława i Janiny, 110/1936',url='https://metryki.genealodzy.pl/index.php?id=424&kt=1&op=pg&plik=110-111.jpg&sy=1936b'),
'S071':dict(title='Urodzenie Czesława, 241/1909',url='https://www.szukajwarchiwach.gov.pl/skan/-/skan/6aa38cb05d670e37063fcdcdc8ce213457bd7672b1512d02656f2d1511cd3850'),
'S063':dict(title='Urodzenie Janiny Poprawki, 112/1910',url='https://skanoteka.genealodzy.pl/index.php?op=pg&id=485&sy=1910&kt=1&plik=111-114.jpg'),
'S061':dict(title='Urodzenie Romana, 226/1919',url='https://www.szukajwarchiwach.gov.pl/skan/-/skan/72ccf13401f1f049671583da77d2ba2fbe8052b0b23e9c32947409e8a47a15de'),
'S072':dict(title='Ślub Wincentego i Agnieszki, 73/1905',url='https://www.szukajwarchiwach.gov.pl/skan/-/skan/dbb6a2471faf0ab42508c0137fe95345b21621cb60c79d996476849a7c762a5e'),
'S027':dict(title='Fotografie nagrobka Tomasza',description='Fotografie rodzinne, niepublikowane w tym widoku.'),
'REL':dict(title='Przekaz rodzinny',description='Informacja od rodziny; nie zastępuje dokumentu potwierdzającego pokrewieństwo.')}
events=[
('263d204','Gazeta o Janinie czeka na odczyt','Ustalono, że numer „Głosu Robotniczego” z 24.05.1957 jest dostępny tylko w sieci biblioteki. To otwarty trop, bez potwierdzenia tożsamości.','trop'),
('7d5d35c','Sprawdzono kolejne publikacje','Przeszukano teksty 21 PDF-ów i zweryfikowano obrazy trzech fragmentów. Odróżniono homonimów; brak dodatkowego połączenia z datami rodziców.','badania'),
('54a0177','Jedna pasująca para w przeszukanych indeksach','Kontrola 21 regionów Geneteki wskazała tylko parę Czesław Chmielewski–Janina Poprawka ze ślubu w Łodzi w 1936 r. Zakres indeksów jest niepełny.','badania'),
('ea0d189','Dokument wskazał rodziców taty Marysi','Odpis ślubu Bogusława wymienia Czesława Chmielewskiego i Janinę Poprawkę. Nazwiska są potwierdzone; dodatkowa identyfikacja pary z 1936 r. pozostaje otwarta.','odkrycie'),
('e2b9c5c','Potwierdzono datę urodzenia Czesława','Odczytano akt 241/1909: 3 lipca 1909, Rogoźno. Porównanie z aktem Romana potwierdziło, że mieli tych samych rodziców.','odkrycie'),
('4108653','Odnaleziono akt urodzenia Janiny Poprawki','Akt 112/1910 wskazuje urodzenie 12 maja 1910 we wsi Socha, parafia Warta, oraz rodziców Józefa Poprawkę i Mariannę Kacprzak.','odkrycie'),
('33c52a6','Odczytano akt Romana Chmielewskiego','Urodzony 6 czerwca 1919 w Rogoźnie, syn Wincentego i Agnieszki. Późniejsze porównanie aktów potwierdziło braterstwo z Czesławem.','odkrycie')]
news=[]
for commit,title,body,kind in events:
 stamp=subprocess.check_output(['git','show','-s','--format=%cI',commit],cwd=ROOT,text=True).strip()
 news.append(dict(at=stamp,title=title,body=body,kind=kind))
data=dict(people=people,edges=edges,sources=sources,news=news,updated=max(x['at'] for x in news),generated=datetime.datetime.now(datetime.timezone.utc).isoformat())
(HERE/'public').mkdir(exist_ok=True)
template=(HERE/'szablon.html').read_text()
(HERE/'public/index.html').write_text(template.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')))
print('Publiczny widok:',len(people),'osób,',len(news),'wpisów; bez danych prywatnych żyjących osób.')
