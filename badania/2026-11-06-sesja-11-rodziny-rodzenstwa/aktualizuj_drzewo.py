"""Jednorazowa redakcja publiczna: bez wskazówki zdrowotnej z REL-013."""
from pathlib import Path
from copy import copy
import csv,json,openpyxl
ROOT=Path(__file__).resolve().parents[2];site=ROOT/'witryna';audit=ROOT/'badania/2026-11-06-trzy-poziomy'
d=json.loads((site/'wiarygodnosc.json').read_text())
common=dict(status='document',branch='paternal',evidence='document',identityLevel=1,level=1,connectionLevel=2,
 classificationReason='Własny odczytany akt i porównanie dokumentów tej rodziny. H017 dotyczy odrębnie połączenia konkretnych dat rodziców z Bogusławem.',
 dataEvidence='Daty i lokalne relacje podano z dokładnymi odnośnikami do dokumentów.')
p30=next(p for p in d['people'] if p['id']=='C05')
p30.update(common,id='P30',name='Julia / Julianna Jabłońska',role='Pierwsza żona Wincentego',dates='Ślub: 19.11.1901 · zm. 08.03.1905',place='Wieprzów → Rachanie',
 note='Przed ślubem z Wincentym była wdową Bartecką. Matka Emilii, przyrodniej siostry Czesława. Jej zgon poprzedza ślub Wincentego z Agnieszką w 1905 r. Nie jest matką Czesława. Wiek w kolejnych aktach jest zmienny; dokładna data urodzenia pozostaje nieustalona.',
 source=['S155','S154','S156','S072'],missing='Własny akt urodzenia i dalsze losy wcześniejszej rodziny Barteckich.',x=280,y=40)
for p in [
 dict(common,id='P28',name='Emilia Chmielewska',role='Przyrodnia siostra Czesława',dates='26.01.1904 — 27.02.1979‡',place='Rachanie · Tomaszów Lubelski',
 note='Córka Wincentego Chmielewskiego i Julii z Jabłońskich. Emilia i Czesław mają wspólnego ojca, lecz inne matki. 22 listopada 1932 r. wyszła za Józefa Mandziuka. ‡Data i miejsce zgonu pochodzą z adnotacji przy urodzeniu; samego aktu zgonu 76/1979 nie odczytano. Dzieci pozostają nieustalone.',
 source=['S154','S153','S155','S156','S071','S072'],missing='Dokumenty dzieci oraz oryginalny akt zgonu 76/1979.',x=-260,y=280),
 dict(common,id='P29',name='Józef Mandziuk',role='Mąż Emilii',dates='33 lata przy ślubie 22.11.1932',place='Majdan Górny · parafia Tomaszów Lubelski',
 note='Rolnik, kawaler w chwili ślubu z Emilią Chmielewską. Syn Bartłomieja i Marianny z Raczkiewiczów. W indeksie występuje także zapis Mańdziuk. Dokładne daty jego urodzenia i śmierci oraz dzieci małżeństwa nie zostały ustalone.',
 source=['S153'],missing='Własny akt urodzenia, późniejsze losy i dokumenty dzieci.',x=-520,y=280),
 dict(id='P31',name='Czesława Chmielewska',role='Ciocia Czesia · pokrewieństwo nieustalone',dates='Około 100 lat w 2026 r.†',place='Łódź — przekaz rodzinny',
 note='Marysia pamięta ciocię Czesię z Łodzi i jej syna mieszkającego w Niemczech. Dokładne pokrewieństwo z Marysią oraz nazwisko rodowe Czesi są nieznane. Możliwość, że była żoną Romana Chmielewskiego, pozostaje hipotezą. †Wiek jest orientacyjnym wspomnieniem, nie ustaloną datą urodzenia. Nie potwierdzono daty zgonu.',
 source=['REL-013'],x=-800,y=280,status='family',branch='paternal',evidence='family',identityLevel=2,level=2,connectionLevel=3,
 classificationReason='Osoba zapamiętana przez rodzinę; dokładne miejsce w gałęzi ojca pozostaje nieustalone.',dataEvidence='Imię, nazwisko, Łódź, orientacyjny wiek i informacja o synu pochodzą ze wspomnienia rodziny.',missing='Nazwisko rodowe, daty oraz dokument lub jednoznaczny przekaz ustalający męża i dokładne pokrewieństwo.'),
 dict(id='P32',name='Syn cioci Czesi',role='Imię i nazwisko nieustalone',dates='Daty nieznane',place='Niemcy — przekaz rodzinny',
 note='Według rodzinnego wspomnienia syn Czesławy Chmielewskiej mieszkał całe życie w Niemczech. Nie znamy jego imienia, nazwiska, dat ani ojca. Nie przypisano go Romanowi Chmielewskiemu i nie ustalono, że urodził się w Niemczech.',
 source=['REL-013'],x=-800,y=560,status='family',branch='paternal',evidence='family',identityLevel=2,level=2,connectionLevel=3,
 classificationReason='Istnienie i relacja z Czesią pochodzą z rodzinnego wspomnienia; osoba nie została niezależnie zidentyfikowana.',dataEvidence='Wyłącznie przekaz rodzinny, bez dokumentu.',missing='Imię, nazwisko i niezależny dokument lub rodzinne potwierdzenie identyfikatorów oraz ojca.'),
]:d['people'].append(p)
for p in d['people']:
 if p['id']=='P05':
  p['note']+=' Pierwszą żoną była Julia z Jabłońskich, matka Emilii; po jej śmierci poślubił Agnieszkę.';p['source']+=['S155','S154','S156']
 if p['id']=='P03':p['note']+=' Emilia Chmielewska, po ślubie Mandziuk, jest jego przyrodnią siostrą po ojcu.';p['source']+=['S154','S155','S156']
for e in d['edges']:
 if e[1]=='C05':e[1]='P30';e[2]='marriage'
for r in d['relations']:
 if r['b']=='C05':r.update(id='R040',b='P30',kind='marriage',level=1,new_level=1,previous_status='hypothesis',reason='Odczytano ślub 72/1901 oraz zgon Julii przed kolejnym ślubem Wincentego. Rodzice Wincentego, Rachanie i chronologia wskazują tę samą osobę.',missing='Małżeństwo i lokalna identyfikacja udokumentowane. H017 dotyczy dalszego łącznika do Bogusława.',sources='S155; S156; S154; S072')
newrels=[
 ('R036','P05','P28','document',1,'Ojciec wymieniony bezpośrednio w urodzeniu Emilii 22/1904; młynarz Wincenty z Rachań.','S154; S155; S072'),
 ('R037','P30','P28','document',1,'Julia z Jabłońskich wymieniona jako matka w urodzeniu i późniejszym ślubie Emilii.','S154; S153'),
 ('R038','P03','P28','document',1,'Rodzeństwo przyrodnie po Wincentym: Emilia z pierwszą żoną Julią, Czesław z drugą żoną Agnieszką. Porównano małżeństwa, urodzenia i zgon Julii.','S154; S155; S156; S072; S071'),
 ('R039','P28','P29','marriage',1,'Małżeństwo Emilii i Józefa Mandziuka potwierdza akt 74/1932, 22 listopada. Emilia zgodna z urodzeniem 22/1904 przez rodziców, wiek i Rachanie.','S153; S154'),
 ('R041','P31','P32','family',2,'Rodzina pamięta, że Czesia miała syna mieszkającego w Niemczech. Nie ustalono jego ojca, imienia ani nazwiska.','REL-013'),
 ('V066','P12','P31','hypothesis_marriage',3,'Użytkownik pyta, czy ciocia Czesia mogła być żoną Romana. Nie ma jeszcze dokumentu ani pewnego przekazu potwierdzającego małżeństwo. H028 pozostaje otwarta.','REL-013; H028')]
for rid,a,b,kind,level,reason,refs in newrels:
 d['edges'].append([a,b,kind]);d['relations'].append(dict(id=rid,a=a,b=b,kind=kind,level=level,new_level=level,exception=False,previous_status='new_document' if level==1 else 'new_family_report',reason=reason,
 missing='Brak wymogu dodatkowego aktu dla tej udokumentowanej relacji.' if level==1 else 'Dokument lub jednoznaczne rodzinne potwierdzenie identyfikatorów i tej relacji.',sources=refs))
url={
 'S153':'https://fotolubgens.lubgens.eu/picture.php?/284676/category/4343',
 'S154':'https://www.szukajwarchiwach.gov.pl/skan/-/skan/17e25d9765aeca0d9d9f7753bf08b7f96c6c5ac8a9d5abedefdf01f97849b7a4',
 'S155':'https://www.szukajwarchiwach.gov.pl/skan/-/skan/bc1bf37adce9ee64959695a97549d6eda47d3a23b95713a346195cc9d1ea3a6b',
 'S156':'https://www.szukajwarchiwach.gov.pl/skan/-/skan/fcc8392d62f1057e144f39b7eb6b3d70c707ed5796577414d930c7ee325be06e'}
for sid,title in [('S153','Emilia i Józef Mandziuk — ślub 74/1932'),('S154','Emilia — urodzenie 22/1904 i adnotacja zgonu'),('S155','Wincenty i Julianna — ślub 72/1901'),('S156','Julianna Chmielewska — zgon 16/1905')]:d['sources'][sid]=dict(title=title,url=url[sid])
d['sources']['REL-013']=dict(title='Ciocia Czesia i jej syn — wspomnienie rodziny',description='Marysia pamięta Czesławę Chmielewską z Łodzi oraz jej syna mieszkającego w Niemczech. Dokładne pokrewieństwo oraz mąż Czesi pozostają nieustalone. Wiek około 100 lat w 2026 r. jest orientacyjny.')
(site/'wiarygodnosc.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (audit/'AUDYT_OSOB.csv').open(newline='') as f:prs=list(csv.DictReader(f));pf=list(prs[0])
for r in prs:
 if r['id']=='C05':r.update(relation_ids='',previous_status='alias P30 po odczycie aktu',level='',identity_level='1',sources='S155; S154; S156; S072',reason='Tożsamość wcześniejszej żony rozstrzygnięta, karta publiczna P30. Alias nie jest drugą osobą.',missing='Dalsze losy wcześniejszej rodziny.')
 if r['id'] in ['P03','P05']:
  r['relation_ids']+='; '+('R038' if r['id']=='P03' else 'R036; R040');r['sources']+='; S154; S155; S156';r['reason']+=' Nowy łańcuch aktów potwierdza Emilię i pierwsze małżeństwo Wincentego.'
for pid in ['P28','P29','P30','P31','P32']:
 p=next(p for p in d['people'] if p['id']==pid)
 prs.append(dict(id=pid,name=p['name'],relation_ids='; '.join(r['id'] for r in d['relations'] if pid in [r['a'],r['b']]),previous_status='nowy akt' if p['level']==1 else 'nowy przekaz rodzinny',level=str(p['level']),identity_level=str(p['identityLevel']),sources='; '.join(p['source']),reason=p['classificationReason']+' '+p['note'],missing=p['missing']))
for cid,name,identity,sources,reason in [('C62','Czesława Chmielewska — Zarzew1999','3','S158','Nieutożsamiona z P31; brak DOB i rodziny.'),('C63','Julianna Chmielewska — Kaczor','1','S151; S148','Wykluczona jako P27 przez innych rodziców.'),('C64','Julianna Janina Chmielewska — Biesaga','1','S152; S148','Wykluczona jako P27 przez innych rodziców.'),('C65','Julianna Chmielewska — Zarzew1981','3','S158; S148','Nieutożsamiona z P27; brak DOB i rodziców.')]:prs.append(dict(id=cid,name=name,relation_ids='',previous_status='kandydat poza publicznym drzewem',level='',identity_level=identity,sources=sources,reason=reason,missing='Nie tworzyć publicznego połączenia bez dowodu.'))
with (audit/'AUDYT_OSOB.csv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=pf);wr.writeheader();wr.writerows(prs)
with (audit/'AUDYT_RELACJI.csv').open(newline='') as f:rf=next(csv.reader(f))
with (audit/'AUDYT_RELACJI.csv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=rf,extrasaction='ignore');wr.writeheader();wr.writerows(d['relations'])
w=openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
for sn,filename in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
 s=w[sn];styles=[copy(c._style) for c in s[2]];s.delete_rows(2,s.max_row)
 with (audit/filename).open(newline='') as f:rows=list(csv.DictReader(f));fields=list(rows[0])
 for r in rows:
  values=[]
  for key in fields:
   val=r[key] or None
   if val is not None and key in ['level','identity_level','new_level']:val=int(val)
   if val is not None and key=='exception':val=val=='True'
   values.append(val)
  s.append(values)
  for c,style in zip(s[s.max_row],styles):c._style=copy(style)
 s.auto_filter.ref=f'A1:{openpyxl.utils.get_column_letter(s.max_column)}{s.max_row}'
w.save(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
counts={}
for level in [1,2,3]:
 ids={p['id'] for p in d['people'] if p['level']<=level};rs=[r for r in d['relations'] if r['a'] in ids and r['b'] in ids and (r['level']<=level or level==1 and r.get('contextInDocumented'))]
 counts[str(level)]=dict(people=len(ids),relations=len(rs),contextual_links=sum(r['level']>level for r in rs))
(audit/'LICZBY.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(counts,'audyt',len(prs),len(d['relations']))
