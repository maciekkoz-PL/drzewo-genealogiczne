"""Jednorazowe uzupełnienie etapu25. Starsze ustalenia i relacje pozostają zachowane."""
from pathlib import Path
import copy,datetime,json
import openpyxl
R=Path(__file__).resolve().parents[2];H=Path(__file__).resolve().parent;D=str(H.relative_to(R));Z=H/'zrodla'
w=openpyxl.load_workbook(R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx');now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
assert not any(r[0]=='S288' for r in w['ZRODLA_I_SKANY'].values),'Etap już zapisany'
def add(sn,values):
 s=w[sn];s.append(values)
 for c in s[s.max_row]:c._style=copy.copy(s.cell(s.max_row-1,c.column)._style)
def row(sn,id):return next(r for r in w[sn] if r[0].value==id)
u='https://photos.szukajwarchiwach.gov.pl/06821bda589e148b83e4bcdb96a57e8458eb31fc70674ec0460bb61d40310d2c_max'
sources=[
['S288','Agnieszka Chmielewska — Chełmońskiego9a → Chojny,1938','SKAN PIERWOTNY',now,'C103;H050;H052','APŁ / Szukaj w Archiwach','39/225/0/4/2137;obraz22;karta19;nr398',u,'ODCZYTANO WPIS I DATĘ ZNAKIEM POWTÓRZENIA',D+'/zrodla/ChojnyP1938_22.jpg','2m+3k;otrzymanie zgłoszenia21II1938(ditto po397),dowódA i zapis25III1938. Poprzednio Łódź,Chełmońskiego9a; nie podano adresu wChojnach. Brak wieku,rodowego,imion krewnych. C103nie utożsamiona zP06/C99/C102. Taka sama liczba osób jak C99nie dowodzi tożsamości ani pokrewieństwa.'],
['S289','Chojny2137/1938 — przegląd dostępnych nazwisk','SKANY PIERWOTNE / ODCZYT WZROKOWY',now,'Bolesław,Danuta Chmielewscy;EdwardPoprawka;odrzucony odczytChmielnicki','APŁ / SwA','39/225/0/4/2137;197obrazów','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/15351997','NAZWISKA5–155/157–195;WYBRANE RUBRYKI',D+'/zrodla/zakres_odczytu.json','190kolumn nazwisk,7obrazówtechnicznych;402oryginały obu ksiąg sprawdzonePIL/hash. Wybrane wpisy1016/1054/477/587wodczyty_wybrane.json. Chmielnicki477nie Chmielewski i nie Bogusław. Nie pełny indeks ani dowód braku nienazwanych członków grup. Bez nowych relacji.'],
['S290','Chojny2135/1937 — przegląd dostępnych nazwisk','SKANY PIERWOTNE / ODCZYT WZROKOWY',now,'Bronisława;MarianJanusz;BolesławChmielewscy — odrębne odczyty','APŁ / SwA','39/225/0/4/2135;205obrazów','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/15351995','NAZWISKA5–167/169–202;WYBRANE RUBRYKI',D+'/zrodla/zakres_odczytu.json','197kolumn nazwisk,8technicznych;wybrane pełne5/34/134/179. Brak nowego łącznika Agnieszki/Czesława zP11. Marian2957ma imiona MarianJanusz;odurodzenia nie oznacza dokładnej daty urodzenia. Inne odczyty685/234bezrodziców i wieku. Nie wyklucza nienazwanych domowników.'],
['S291','Przeszukiwalne zestawienie meldunków —55odczytów','OPRACOWANIE POCHODNE',now,'Wybrane trafienia i odrzucenie odczytu;nie lista krewnych','Opracowanie lokalne','IM001–IM055;CSV/HTML/Excel','https://github.com/maciekkoz-PL/drzewo-genealogiczne','47STARSZYCH +8NOWYCH',D+'/zrodla/indeks_wybranych_wpisow.csv','Nie pełny indeks. Obejmuje jawnie oznaczone błędne trafienie Chmielnicki477; nie tworzy kandydata. Wersje44i47zachowane.'],
['S292','Łódź — katalog wyjazdów1938 i nieruchomości Chełmońskiego','KATALOG / MANIFESTY;BEZ ODCZYTU TREŚCI',now,'Dalsza weryfikacja C103','BASIA / APŁ / SwA','39/221/0/4.12/25508;39/221/0/4.4/15575','https://www.basia.famula.pl/skany.php?placeid=967&arch=39&zespol=221&from=5500','USTALONO184i172OBRAZY;TREŚĆ JESZCZE NIEODCZYTANA',D+'/katalog','25508SwA6209685:opuszczającyŁódź1938,zespółIII. 15575SwA17669762:inwentarzChełmońskiego1931–1946,nieautomatyczniespismieszkańców. 203tytuły ksiąg kontroli ruchu wprzejrzanymBASIA;obie jednostki wolna. Nie dowodzi braku indeksu wszędzie. Manifesty pobrane publicznym sliderem/API.']]
for x in sources:add('ZRODLA_I_SKANY',x)
for id,scope,result,limit,src in [
('L288','Chojny2137/1938,obraz22,nr398','Agnieszka;2m+3k;Chełmońskiego9a;zgłoszenie21II1938. NowyC103.','Brak wieku,rodowego,imion domowników. C103niescalona zP06/C99/C102.','S288'),
('L289','Całe dostępne nazwiska2137/1938','190kolumn5–155/157–195;wybrane rubryki i techniczne. TrafieniaS289,477toChmielnicki.','Nie pełna transkrypcja wszystkich pól i nie dowód nieobecności.','S289'),
('L290','Całe dostępne nazwiska2135/1937','197kolumn5–167/169–202;Bronisława685,MarianJanusz2957,Bolesław234.','Brakrodziców/DOB/łącznikaP11. Nienazwaneosobygrupnierozstrzygnięte.','S290'),
('L291','Cyfrowe zestawienie odczytów','47→55wierszy;HTML/CSV iExcel;poprzedniewersjezachowane.','Nie pełny indeks,nie lista krewnych,nie niezależny dowód wobec skanów.','S291'),
('L292','KatalogBASIA Łódź,203tytułyKRL iChełmońskiego','Ustalono25508/6209685/184obrazy i15575/17669762/172obrazy. Zapisano zapytania beztrafienia oraz niepełne wariantyparametrów.','Katalog/manifestnie dowodzą obecności osoby. Treść obrazów jeszcze nieodczytana; nie mylić zDO86616.','S292')]:add('DZIENNIK_KWEREND',[id,now,scope,result,limit,src])
add('KANDYDACI_I_HOMONIMY',['C103','Agnieszka Chmielewska — Chełmońskiego9a','1938,nr398;karta19/obraz22;2m+3k;zgłoszenie21II1938;dowódA/zapis25III1938;bezDOB','MożliwaP06/C99/C102 — nie utożsamiono','Łódź,Chełmońskiego9a → Chojny(adresniepodany)','NOWY TROP MELDUNKOWY — BEZ RELACJI','Taka sama liczebność jakC99/1936jestposzlaką; brak imion domowników i wieku. Nie dowodzi,że toprababcia.','S288;S267;S274;S284','OdpowiednikwyjazdowyŁódź25508; karta z rodowym/datąurodzenia i rodziną;H050/H052.',u])
h=row('HIPOTEZY_OTWARTE','H052');h[2].value+=' Etap25:S288nowyC103,Agnieszka2m+3k,Chełmońskiego9a→Chojny,zgłoszenie21II1938;bezDOB/rodowego/składurodziny. Nie scalono zC102/P06/C99. NazwiskaChojen2135/1937i2137/1938wykonane;S290nie przynosiłącznikaP11.';h[3].value+=' SprawdzićŁódź25508/1938orazinwentarzChełmońskiego15575;S292katalog,treśćnieodczytana.'
h=row('HIPOTEZY_OTWARTE','H050');h[2].value+=' Etap25:S288/C103również2m+3k,leczinnyadresChełmońskiego9airok1938. BezDOB/rodowego nie scalać zC99/P06.'
t=row('ZADANIA_AGENTA','T58');t[5].value='AKTYWNE:Chojny1937/1938nazwiskazakończone(S289/S290). NowyC103/S288; potrzebnyodpowiednikwyjazdowyŁódź25508/1938,kartaludnościzDOB/rodowym i rodziną. S292katalog25508/15575ustalony.';t[8].value+=';S288;S289;S290;S291;S292;'+D+'/PLAN_KONTYNUACJI.md'
add('INSTRUKCJA_AGENTA',['G28','ETAP25 — CHOJNY1937/1938',f'C103/S288:Agnieszka2m+3k,Chełmońskiego9a→Chojny,21II1938. NieutożsamionazP06/C99/C102. Kolumnynazwisk2135/1937i2137/1938zakończone. Czytaj {D}/PLAN_KONTYNUACJI.md;następneŁódź25508/15575.'])
rows=json.loads((H/'indeks_dane.json').read_text());assert w['INDEKS_MELDUNKOW'].max_row==50
for n,r in enumerate(rows[47:],48):add('INDEKS_MELDUNKOW',[f'IM{n:03d}']+list(r.values()))
s=w['INDEKS_MELDUNKOW'];s['A2']='55odczytów;wybrane trafienia i odrzucenieChmielnicki;niepełnyindeks,nie lista krewnych.';s.auto_filter.ref=f'A3:H{s.max_row}'
for n in range(51,59):s.row_dimensions[n].height=85
files=sorted([p for p in Z.iterdir() if p.is_file()]+[p for p in (H/'katalog').iterdir() if p.is_file()])
for n,p in enumerate(files,383):
 src='S292' if p.parent.name=='katalog' else 'S291' if p.name=='indeks_wybranych_wpisow.csv' else 'S288;S289;S290'
 add('PLIKI_DOWODOWE',[f'F{n}',str(p.relative_to(R)),'SKAN / METADANE / POCHODNE',src,'Szczegóływzakres_odczytu.json;hashwmanifest.json.','25oryginałów;ZIPkolumnipochodneoznaczone. Beznowejrelacji.'])
w['START']['A2'].value+=f' Etap25:S288C103/Chełmońskiego9a;S289/S290nazwiskaChojen1938/1937zakończone;S291tabela55odczytów;S292katalogŁódź25508/15575. P11nadalnieustalony. {D}/STATUS.md.'
w['ZRODLA_I_SKANY']['A2']='292źródła;25arkuszy. Etap25:C103/Agnieszka/Chełmońskiego9a. Beznowejpotwierdzonejrelacji. S292tylkokatalog/manifesty.'
w['KANDYDACI_I_HOMONIMY']['A2']='103rekordy z zachowanymi aliasami. C103:AgnieszkaChełmońskiego9a,niescalona zP06/C99/C102.'
w.save(R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
print(dict(sources=292,logs=292,files=382+len(files),index=55,candidates=103,sheets=len(w.sheetnames)))
