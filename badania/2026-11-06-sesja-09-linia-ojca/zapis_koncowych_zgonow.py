from pathlib import Path
exec(Path('work/s09/checkpoint.py').read_text().split("source('S136'")[0])
source('S145','Józef Chmielewski — zgon3339/1940, inni rodzice','SKAN PIERWOTNY','C60 — wykluczony jako brat Bogusława','AP Łódź / PTG Skanoteka','39/2736/0/-/12; PTG4852/1940cg/3338-3339.jpg;3339','https://skanoteka.genealodzy.pl/index.php?op=pg&id=4852&sy=1940cg&kt=1&plik=3338-3339.jpg','ODCZYTANO OBRAZ','zrodla/death1940/act_3339_image.jpg','Ur.21.04.1901Pet r ikau/Piotrków; zm.11.05.1940Łódź. OjciecLeonardChmielewski, matkaWiktoriaWitkowska. To inna para niżCzesław/Janina i Wincenty/Agnieszka. Nie badano jego potomków jako krewnych Marysi.')
source('S146','Antonina Chmielewska zOrlików — zgon4683/1940','SKAN PIERWOTNY','C61 — wykluczona jako siostra Bogusława','AP Łódź / PTG Skanoteka','39/2736/0/-/14; PTG4852/1940ci/4682-4683.jpg;4683','https://skanoteka.genealodzy.pl/index.php?op=pg&id=4852&sy=1940ci&kt=1&plik=4682-4683.jpg','ODCZYTANO OBRAZ I SKORYGOWANO NR INDEKSU','zrodla/death1940/antonina_4683_image.jpg','Ur.05.05.1869Piaskowice, zm.30.06.1940Łódź; rodziceKazimierzOrlik/Katarzyna. Wdowa poJózefieChmielewskim, zgłasza synZygmunt. To nie dziecko Czesława/Janiny. Prawidłowy nr4683, nie4689: ten drugi akt dotyczy JózefaGoździa i jest tylko kontrolą błędu.')
for cid,name,data,reason,refs,url in [
('C60','Józef Chmielewski','21.04.1901Piotrków–11.05.1940Łódź; rodziceLeonardChmielewski/WiktoriaWitkowska','Oboje rodzice inni niż wS086; nie brat Bogusława. Brak podstaw do dalszego pokrewieństwa.','S137; S145','https://skanoteka.genealodzy.pl/index.php?op=pg&id=4852&sy=1940cg&kt=1&plik=3338-3339.jpg'),
('C61','Antonina Chmielewska zOrlików','05.05.1869Piaskowice–30.06.1940Łódź; ojciecKazimierzOrlik, matkaKatarzyna; wdowa poJózefie','Nie jest dzieckiem Czesława/Janiny. Dane1869 i rodzice wykluczają hipotezę siostryBogusława. SynZygmunt nie został połączony z innymi Zygmuntami.','S137; S146','https://skanoteka.genealodzy.pl/index.php?op=pg&id=4852&sy=1940ci&kt=1&plik=4682-4683.jpg'),
]:add('KANDYDACI_I_HOMONIMY',[cid,name,data,'Kontrola nowych wpisów skorowidzaC1940','Łódź','WYKLUCZONY/A JAKO RODZEŃSTWO BOGUSŁAWA',reason,refs,'Nie prowadzić tej osoby jako nowego krewnego bez odrębnych dowodów.',url])
for lid,scope,result,limit,refs in [
('L117','Oryginał3339/1940 zPTG1940cg','Józef1901, rodziceLeonard/Wiktoria; C60wykluczony jako bratBogusława.','Nie badano dalszych losów niezwiązanej rodziny.','S145'),
('L118','Kontrola nrAntoniny:1940cqSkZ15, próbny4689, następnieprawidłowy4683','Prawidłowyakt4683: Antonina1869zOrlików; C61wykluczona jako siostraBogusława. Poprawiono wcześniejszy odczyt numeru.','4689JózefGoźdź, nie Antonina. Zachowano jako kontrolębłędu, nie dowód rodzinny.','S137; S146'),
]:add('DZIENNIK_KWEREND',[lid,'2026-11-06',scope,result,limit,refs])
add('KOREKTY_I_SPRZECZNOSCI',['Q73','KOREKTA NR AKTU','Antonina wSkZ15 ma4683, nie4689','Odczyt obu aktów:4689toJózefGoźdź;4683AntoninaChmielewska zOrlików.','SKANY PIERWOTNE','S137; S146','Nie utrwalać numeru z pobieżnego indeksu bez porównania treści aktu.','https://skanoteka.genealodzy.pl/index.php?op=pg&id=4852&sy=1940ci&kt=1&plik=4682-4683.jpg'])
for fid,path,sid,title in [('F91','zrodla/death1940/act_3339_image.jpg','S145','Józef3339, inni rodzice'),('F92','zrodla/death1940/antonina_4683_image.jpg','S146','Antonina4683, ur.1869')]:
    add('PLIKI_DOWODOWE',[fid,str(root/path),'SKAN PIERWOTNY',sid,title,'ODCZYTANO, SHA256 w manifeście'])
w['ZRODLA_I_SKANY']['A2']='146 źródeł. Etap09: S136–S146; cztery zgony indeksowe odczytane, bez potwierdzonego rodzeństwa Bogusława.'
w['KANDYDACI_I_HOMONIMY']['A2']='61 pozycji kandydatów/aliasów. C58/C60/C61 wykluczeni w hipotezie rodzeństwa, C59Leo pozostaje słabym tropem; C42 nadal hipotezą.'
# Uzupełnij audyt wszystkich rekordów po równoległym dodaniu jego arkuszy.
import csv
audit=Path('badania/2026-11-06-trzy-poziomy/AUDYT_OSOB.csv')
with audit.open(newline='') as f:rows=list(csv.DictReader(f));fields=list(rows[0])
extra=[
{'id':'C59','name':'Leo Chmielewski','relation_ids':'','previous_status':'pominięty; tożsamość matki nieustalona','level':'','identity_level':'1','sources':'S144; S067','reason':'Akt dziecka odczytany; brak rodowego iDOBJaniny oraz danych ojca. Zgodne imię i nazwisko matki nie wystarczają do powiązania zP04. Nie dodano krawędzi do rodziny.','missing':'U1612/1940 z pełnymi danymi matki; H025otwarta.'},
{'id':'C60','name':'Józef Chmielewski','relation_ids':'','previous_status':'pominięty; wykluczony jako bratBogusława','level':'','identity_level':'1','sources':'S145','reason':'OjciecLeonard, matkaWiktoria; nie Czesław/Janina. Nie dodano homonimu do drzewa.','missing':'Brak podstaw do rodzinnego połączenia.'},
{'id':'C61','name':'Antonina Chmielewska zOrlików','relation_ids':'','previous_status':'pominięta; wykluczona jako siostraBogusława','level':'','identity_level':'1','sources':'S146','reason':'Urodzona1869, rodziceKazimierzOrlik/Katarzyna; nie dziecko Czesława/Janiny.','missing':'Brak podstaw do rodzinnego połączenia.'},
]
for r in extra:
    assert r['id'] not in {x['id'] for x in rows};rows.append(r)
    vals=[int(r[k]) if k in ['level','identity_level'] and r[k] else r[k] or None for k in fields]
    add('WIARYGODNOSC_OSOB',vals)
with audit.open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader();wr.writerows(rows)
w.save(book)
manifest=[]
for p in sorted(src.rglob('*')):
    if p.is_file():
        b=p.read_bytes();manifest.append({'path':str(p),'size':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(root/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Zapisano4odczytanezgony i audyt82rekordów; bez nowych relacji')
