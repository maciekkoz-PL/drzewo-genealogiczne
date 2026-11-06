from pathlib import Path
import json,csv,openpyxl
from copy import copy
p=Path('witryna/wiarygodnosc.json');d=json.loads(p.read_text());mapping={'C04':'P26','C02':'P27'}
urls={
'P26':'https://www.szukajwarchiwach.gov.pl/skan/-/skan/9d10d7cde36c6bc6600d52eb97d4ef1c0a384f9a98bbfd52bb23f9c62f65084e',
'P27':'https://www.szukajwarchiwach.gov.pl/skan/-/skan/9a130e8ffe855ef7ea744ffba5207c1d4c197eec550bc4925b0a7056e0dddf34'}
for person in d['people']:
 if person['id'] not in mapping:continue
 pid=mapping[person['id']];person['id']=pid
 person.update(role='Siostra Czesława',place='Rogoźno · parafia Tomaszów Lubelski',status='document',evidence='document',identityLevel=1,level=1,connectionLevel=2,
 classificationReason='Odczytany akt urodzenia i zgodni oboje rodzice z rodziną Czesława. H017 pozostaje odrębną oceną łącznika do Bogusława.',
 missing='Późniejszy ślub, nazwisko poślubne i dalsze losy. Związek z Tczewem nie został ustalony.',dataEvidence='Data urodzenia, rodzice i miejscowość z oryginalnego aktu; rodzeństwo z porównania metryk.')
 if pid=='P26':person.update(dates='14.07.1917 · data z aktu urodzenia',source=['S147','S071'],note='Akt 124/1917 podaje rodziców: Wincentego Chmielewskiego i Agnieszkę z Miszczyszynów. Ci sami rodzice i Rogoźno występują w akcie Czesława. Sabina jest jego siostrą; nie ustalono późniejszych losów ani pobytu w Tczewie.')
 else:person.update(dates='09.11.1907 · data gregoriańska',source=['S148','S071'],note='Akt 360/1907 podaje rodziców: Wincentego Chmielewskiego i Agnieszkę z Miszczyszynów z Rogoźna. Julianna jest siostrą Czesława. W tym akcie ojcu wpisano 30 lat, co różni się od pozostałych dokumentów; rozbieżność zachowano. Brak ustalenia późniejszego nazwiska i związku z Tczewem.')
for e in d['edges']:
 if e[1] in mapping:e[1]=mapping[e[1]];e[2]='document'
for r in d['relations']:
 if r['b'] not in mapping:continue
 pid=mapping[r['b']];r.update(id='R032' if pid=='P26' else 'R035',b=pid,kind='document',level=1,new_level=1,previous_status='hypothesis',exception=False,
 reason='Oryginalne akty podają tych samych oboje rodziców, nazwisko rodowe matki i Rogoźno. '+('W akcie Julianny wiek ojca jest rozbieżny; zapisano to w opisie i Q74.' if pid=='P27' else 'Wiek rodziców jest zgodny w przybliżeniu.'),
 missing='Brak wymogu kolejnego dokumentu dla tej relacji. Dalsze losy i Tczew pozostają nieustalone.',sources=('S147' if pid=='P26' else 'S148')+'; S071')
for rid,parent,pid,sid in [('R030','P05','P26','S147'),('R031','P06','P26','S147'),('R033','P05','P27','S148'),('R034','P06','P27','S148')]:
 d['edges'].append([parent,pid,'document']);d['relations'].append(dict(id=rid,a=parent,b=pid,kind='document',level=1,new_level=1,previous_status='new_document',exception=False,reason='Rodzic wymieniony bezpośrednio w odczytanym akcie urodzenia.',missing='Relacja udokumentowana aktem.',sources=sid))
d['sources']['S147']=dict(title='Sabina Chmielewska — akt urodzenia 124/1917',url=urls['P26'])
d['sources']['S148']=dict(title='Julianna Chmielewska — akt urodzenia 360/1907',url=urls['P27'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

audit=Path('badania/2026-11-06-trzy-poziomy')
with (audit/'AUDYT_OSOB.csv').open(newline='') as f:people=list(csv.DictReader(f));pf=list(people[0])
for r in people:
 if r['id'] in mapping:
  pid=mapping[r['id']];r.update(relation_ids='',previous_status='rozstrzygnięta kandydatura; alias '+pid,level='',identity_level='1',sources='S147' if pid=='P26' else 'S148',reason='Oryginał urodzenia odczytany; osoba występuje jako'+pid+'. Nie pokazywać drugiej karty aliasu.',missing='Późniejsze losy oraz Tczew nieustalone.')
 elif r['id'] in ['P03','P05','P06']:
  extra={'P03':'R032; R035','P05':'R030; R033','P06':'R031; R034'}[r['id']];r['relation_ids']+='; '+extra;r['sources']+='; S147; S148';r['reason']+=' Nowe metryki potwierdzają Sabinę i Juliannę w rodzinie.'
for pid in ['P26','P27']:
 x=next(x for x in d['people'] if x['id']==pid);rids='; '.join(r['id'] for r in d['relations'] if pid in [r['a'],r['b']])
 people.append(dict(id=pid,name=x['name'],relation_ids=rids,previous_status='nowy odczyt dokumentu; dawny alias'+('C04' if pid=='P26' else 'C02'),level='1',identity_level='1',sources='; '.join(x['source']),reason=x['classificationReason']+' '+x['note'],missing=x['missing']))
with (audit/'AUDYT_OSOB.csv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=pf);wr.writeheader();wr.writerows(people)
with (audit/'AUDYT_RELACJI.csv').open(newline='') as f:rf=next(csv.reader(f))
with (audit/'AUDYT_RELACJI.csv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=rf,extrasaction='ignore');wr.writeheader();wr.writerows(d['relations'])
w=openpyxl.load_workbook('Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
for sn,filename,intcols in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv',['level','identity_level']),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv',['level','new_level'])]:
 s=w[sn];styles=[copy(c._style) for c in s[2]];s.delete_rows(2,s.max_row)
 with (audit/filename).open(newline='') as f:rs=list(csv.DictReader(f));fields=list(rs[0])
 for r in rs:
  vals=[]
  for k in fields:
   v=r.get(k) or None
   if v is not None and k in intcols:v=int(v)
   if v is not None and k=='exception':v=v=='True'
   vals.append(v)
  s.append(vals)
  for c,style in zip(s[s.max_row],styles):c._style=copy(style)
 s.auto_filter.ref=f'A1:{openpyxl.utils.get_column_letter(s.max_column)}{s.max_row}'
w.save('Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
counts={}
for level in [1,2,3]:
 ids={x['id'] for x in d['people'] if x['level']<=level};rs=[r for r in d['relations'] if r['a'] in ids and r['b'] in ids and (r['level']<=level or level==1 and r.get('contextInDocumented'))]
 counts[str(level)]={'people':len(ids),'relations':len(rs),'contextual_links':sum(r['level']>level for r in rs)}
(audit/'LICZBY.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(counts,'audyt osób',len(people),'relacji',len(d['relations']))
