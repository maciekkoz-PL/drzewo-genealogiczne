from pathlib import Path
from lxml import html
import json,urllib.request,urllib.parse,hashlib,datetime,concurrent.futures,re
p=Path('work/s13/szczurek');p.mkdir(parents=True,exist_ok=True)
index=Path('badania/2026-11-06-sesja-11-rodziny-rodzenstwa/zrodla/szczurek_bioindex.html')
h=html.fromstring(index.read_bytes().decode('utf-16'));jobs=[];seen=set()
for a in h.xpath('//a[@href]'):
 u=a.get('href').replace('http://','https://')
 if re.search(r'/biop\d{4}\.html$',u) and u not in seen:jobs.append(dict(url=u,title=' '.join(a.text_content().split())));seen.add(u)
(p/'zaplanowany_zakres.json').write_text(json.dumps(jobs,ensure_ascii=False,indent=2))
print('Planned',len(jobs),flush=True)
def run(j):
 row=dict(j,utc=datetime.datetime.now(datetime.timezone.utc).isoformat());key=urllib.parse.urlsplit(j['url']).path.strip('/').replace('.html','')
 try:
  with urllib.request.urlopen(urllib.request.Request(j['url'],headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r:b=r.read();row.update(status=r.status,size=len(b),final_url=r.url,sha256=hashlib.sha256(b).hexdigest())
  (p/(key+'.html')).write_bytes(b)
  enc='utf-16' if b.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8'
  doc=html.fromstring(b.decode(enc,errors='replace'))
  for n in doc.xpath('//script|//style'):n.drop_tree()
  txt=' '.join(doc.text_content().split());(p/(key+'.txt')).write_text(txt)
  row['hits']=[dict(term=m.group(),context=txt[max(0,m.start()-180):m.end()+220]) for m in re.finditer(r'chmielew\w*|czesław[ayę]?|czeslaw[ayę]?|czesi[aę]',txt,re.I)]
  row['chmielewski_hits']=[v for v in row['hits'] if v['term'].lower().startswith('chmielew')]
  if row['chmielewski_hits']:print('HIT',j['title'],json.dumps(row['chmielewski_hits'],ensure_ascii=False)[:1800],flush=True)
 except Exception as e:row['error']=str(e)
 return row
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for row in ex.map(run,jobs):
  rows.append(row)
  if len(rows)%40==0:print('Done',len(rows),'errors',sum('error'in r for r in rows),flush=True)
  (p/'odczyty.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('Finished',len(rows),'errors',sum('error'in r for r in rows),flush=True)
