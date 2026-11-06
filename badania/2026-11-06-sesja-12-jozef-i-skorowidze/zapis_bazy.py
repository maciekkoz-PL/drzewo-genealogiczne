"""Jednorazowy zapis etapu12, stan wejściowy7322882. Nie uruchamiać ponownie."""
from pathlib import Path
import json, datetime, openpyxl
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
book=ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
w=openpyxl.load_workbook(book)
assert len(w.sheetnames)==23
def find(sn,id):
    return next(row for row in w[sn] if row[0].value==id)
assert not any(r[0].value=='S161' for r in w['ZRODLA_I_SKANY'])
stamp=datetime.datetime.now(ZoneInfo('Europe/Warsaw')).isoformat(timespec='seconds')
base=str(HERE.relative_to(ROOT))
birth='https://www.szukajwarchiwach.gov.pl/skan/-/skan/c07a9fd88a54463d6f84d279f3c376a637f7814d3f5de061aa28a624503618d2'
p=find('RDZEN_RODZINY','P29')
p[3].value='22.07.1897 greg.; 10.07.1897 jul.; Majdan Górny; 35 lat przy ślubie22.11.1932'
p[8].value='S153; S165; S166'
p[9].value='Akt195/1897: Bartłomiej35/MariannaRaczkiewicz30. Rodzice i miejscowość zgodni ze ślubem74/1932. Korekta Q79: odczyt wieku33 był błędny; w oryginale35. Nie ustalono zgonu ani dzieci.'
p[10].value=birth
s=find('ZRODLA_I_SKANY','S153');s[10].value=s[10].value.replace('Józef33','Józef35')+' Korekta odczytu wieku Q79; oryginał zachowany.'
sources=[
('S161','Tomaszów — publiczna wyszukiwarka cmentarza komunalnego','BAZA POCHÓWKÓW; WYNIK OGRANICZONY','P28; P29','Grobonet / Polskie Cmentarze','Emilia Mandziuk/Mańdziuk, Józef Mandziuk; dodatkowo nazwisko i imię osobno','https://tomaszow.grobonet.com/grobonet/start.php','grobonet_start.html','Brak Emilii pod nazwiskiem Mandziuk/Mańdziuk. Osiem wyników Józefa, cztery bezDOB; odczytano cztery karty. Żaden nie jest utożsamiony zP29. Tylko cmentarz komunalny, nie parafialny i nie wszystkie okoliczne miejscowości.'),
('S162','Garbów — lokalizacja alegat1932','KATALOG I PRZEGLĄD ZAŁĄCZNIKÓW','P27','Fotolubgens USC Garbów','Kategoria5395; alegatyparafiiGarbów1932 kat6445,42zdjęcia','https://fotolubgens.lubgens.eu/index.php?/category/6445','garbow1932.html','To alegaty, nie księga małżeństw1932. Przejrzano fotografie i nagłówki załączników; nie odnaleziono czytelnego dokumentu oznaczonego26/1932 dla Julianny/BronisławaPochronia. Nie rozstrzyga kandydatury ani nie dowodzi braku aktu.'),
('S163','Tomaszów — pełne skorowidze małżeństw1933–1938','ODCZYT SKOROWIDZÓW; NIE WSZYSTKICH AKTÓW','P12; P26; P27','Fotolubgens / USC Tomaszów','12obrazów; 614pozycji skorowidzów obu małżonków','https://fotolubgens.lubgens.eu/index.php?/category/4376','1933_024.jpg','Wzrokowo przejrzano oboje małżonków:1933poz1–86,1934poz1–90,1935poz1–106,1936poz1–108,1937poz1–122,1938poz1–102. Nie odnaleziono Romana ani Julianny/SabinyChmielewskich. Skorowidz może zawierać opuszczenia; to nie pełna lektura aktów ani wynik dla innych parafii/lat.'),
('S164','Dalsze zapytania internetowe o Emilię, Józefa i Czesię','KWERENDY','P28; P29; P31','Publiczna wyszukiwarka internetowa','3zestawy po4zapytania; parametry i ograniczenia zachowane','https://polskie-cmentarze.com/','web_queries.json','Nie uzyskano dokumentu identyfikującego Czesię lub dzieci pary. Część odpowiedzi zarchiwizowana; środkowy zestaw ma tylko zapis zapytań i wyniku, bez surowej odpowiedzi. Nie jest podstawą nowych relacji.'),
('S165','Lubgens — Józef Mandziuk195/1897 i informacja o ślubie','INDEKS; NASTĘPNIE SPRAWDZONY ORYGINAŁ','P29; P28','Lubgens','U1897/195Tomaszów; kwerenda1897–1901 Mandziuk/Mańdziuk','https://regestry.lubgens.eu/viewpage.php?page_id=1057','lubgens_jozef.json','Indeks wskazuje1897 i dopisek o ślubie zEmiliąChmielewską1932. To uwaga indeksu, nie odczytana adnotacja na tej kopii aktu. Tożsamość sprawdzono niezależnie przez oboje rodziców i MajdanGórny wS153/S166.'),
('S166','Józef Mandziuk — urodzenie195/1897','SKAN PIERWOTNY','P29','AP Zamość / SwA; Tomaszów Lubelski','88/639/0/-/22; SwA10503472; obraz27/97; id59123412; karta48',birth,'Jozef1897_27.jpg','Urodzony10/22VII1897godz20 MajdanGórny; akt/chrzest13/25VII1897godz14. OjciecBartłomiejMandziuk35, matkaMariannaRaczkiewicz30. Dwoje rodziców i wieś zgodne ze ślubem74/1932; ślub podaje35lat. Nie ustalono daty zgonu, potomstwa ani dalszych losów.')]
for sid,title,typ,people,inst,sig,url,file,note in sources:
    w['ZRODLA_I_SKANY'].append([sid,title,typ,'2026-11-06',people,inst,sig,url,'ODCZYTANO W PODANYM ZAKRESIE',base+'/zrodla/'+file,note])
w['ZRODLA_I_SKANY']['A2']='166źródeł. Etap12: akt urodzenia JózefaMandziuka; korekta wieku35; zapis ograniczonych wyników negatywnych.'
w['ZDARZENIA_I_FAKTY'].append(['E065','22.07.1897','P29','urodzenie','JózefMandziuk ur.MajdanGórny, godz20; rodziceBartłomiej35 iMariannaRaczkiewicz30.','SKAN PIERWOTNY','S166',birth,'10VIIjul./22VIIgreg.; akt/chrzest13/25VII1897godz14. Zgodność rodziców i wsi ze ślubem1932.'])
w['KOREKTY_I_SPRZECZNOSCI'].append(['Q79','KOREKTA ODCZYTU','JózefMandziuk: w ślubie74/1932 jest35lat, nie33','Ponowny odczyt oryginału: „lat trzydzieści pięć mającym”. Urodzenie22VII1897 zgodne z wiekiem35 wXI1932. To błąd wcześniejszego odczytu, nie sprzeczność dokumentów.','POPRAWIONO; HISTORIA W GIT','S153; S165; S166','PoprawionoP29/S153, audyty i stronę. Historyczny zapis etapu11 zachowany z korektą i w Git.','https://fotolubgens.lubgens.eu/picture.php?/284676/category/4343'])
logs=[
('L131','GrobonetTomaszów: EmiliaMandziuk/Mańdziuk, Józef; szerzejMandziuk iEmilia','Nie znalezionoEmilii;8Józefów,4kartybezDOB odczytane, bez identyfikacjiP29.','Tylko cmentarz komunalny; brak nie wyklucza pochówku w okolicy.','S161'),
('L132','Garbów: katalog5395 i42fotografie alegat1932kat6445','Nie odnaleziono dokumentu26/1932 dlaJulianny/Bronisława.','To alegaty, nie pełna księga ślubów. Nie wykluczaP27.','S162'),
('L133','Tomaszów1933–1938:614pozycji skorowidzów; przeczytano oboje małżonków','Nie odnalezionoRomana/Julianny/SabinyChmielewskich.','Zasadne poszerzenie poprzedniego odczytu samychsekcjiC panów młodych. Nie wszystkieakty, możliwe błędy skorowidza.','S159; S163'),
('L134','12zapytań internetowych oEmilię/Józefa/Czesię i lokalizacjębaz','Beznowych relacji. Zlokalizowano wyszukiwarkę komunalną; brak potwierdzenia parafialnej.','Dokładne zapytania w pliku; jeden zestaw bezsurowej odpowiedzi. Nie przypisywać rodzin z wyników po samym nazwisku.','S164'),
('L135','LubgensU1897–1901 JózefMandziuk/Mańdziuk','U195/1897Tomaszów z informacją o ślubieEmilia1932.','Dodatnia wskazówka; wymagała S166. Ślub35lat, poprawiono wcześniejszyodczyt33.','S165; S166; S153'),
('L136','SwA10503472:97metadanych, obrazy40/45lokalizacyjne i27docelowy','Odczytano195/1897:22VII1897,MajdanGórny,Bartłomiej/MariannaRaczkiewicz.','Pierwsze212bajtoweHTML nie były obrazami; normalny publiczny podgląd przyniósłJPG. Bez adnotacji zgonu.','S166')]
for lid,scope,result,limit,src in logs:w['DZIENNIK_KWEREND'].append([lid,stamp,scope,result,limit,src])
w['HIPOTEZY_ROZSTRZYGNIETE'].append(['H031','CzyJózefMandziuk195/1897 jest mężemEmiliiP28?','POTWIERDZONO — P29','Zgodneoboje rodziceBartłomiej/MariannaRaczkiewicz iMajdanGórny; wiek35 w1932 pasuje do1897. Uwagaindeksu oEmilii wspiera, lecz nie zastępuje porównaniaaktów.','S153; S165; S166','2026-11-06'])
w['HIPOTEZY_OTWARTE'].append(['H032','CzyEmiliaP28/JózefP29 mieli dzieci i jakie?','Nie mamy źródła wskazującego dziecko tej pary. Znamy ślub1932 i tożsamość obojga.','Późniejsze akty, nekrologi lub dane pochówku z jawną relacją; brakwpisuEmilii wjednejbazie nie wyklucza rodziny.','OTWARTA — NIE DOPISYWAĆ POTOMSTWA PO NAZWISKU'])
w['ZADANIA_AGENTA'].append(['T37',1,'POTOMSTWO RODZEŃSTWA','Publicznearchiwa/rejestry','Sprawdzić dzieciEmilii/Józefa po ślubie1932; dalszelosyP12/P26/P27 iCzesięP31.','OTWARTE; kontynuować poza614odczytanymi pozycjami1933–1938.','Agent','Bez wniosków, wiadomości i płatności. Nowy dobryidentyfikatorP29:22VII1897.','S166; S163; H032; H028; H030'])
for fid,file,src,note in [('F103','Jozef1897_27.jpg','S166','Oryginalna strona z aktem195/1897'),('F104','lubgens_jozef.json','S165','Parametry i wyniki obu pisowni nazwiska'),('F105','fetch_2.json','S161; S162','Proweniencja grobów i katalogu'),('F106','garbow1932.html','S162','42metadane alegat; fotografie lokalnie'),('F107','fetch_4.json','S163','Noweobrazy, pozostałeponownieodczytane zS159'),('F108','web_queries.json','S164','Zapytania i zakres archiwizacji odpowiedzi')]:
    w['PLIKI_DOWODOWE'].append([fid,base+'/zrodla/'+file,'SKAN / REJESTR DOSTĘPU',src,note,'SHA256 wmanifest_zrodel_sesji.json'])
# Audyt osoby: zmiana danych, bez zmiany poziomu lub pokrewieństwa.
for row in w['WIARYGODNOSC_OSOB']:
    if row[0].value=='P29':
        for c in row:
            if isinstance(c.value,str):c.value=c.value.replace('33 lata przy ślubie 22.11.1932','22.07.1897 · Majdan Górny; 35 lat przy ślubie1932').replace('33lata','35lat').replace('Józef33','Józef35')
w.save(book)
print('Zapisano S161–S166, E065, L131–L136, Q79, H031/H032, T37; 23arkusze.')
