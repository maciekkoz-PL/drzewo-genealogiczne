from pathlib import Path
import urllib.request,json,hashlib,datetime,re,fitz
from lxml import html
p=Path('work/h017-s04/variants');logs=[]
jobs=json.loads((p/'downloads.json').read_text())
selected=[r for row in jobs for r in row.get('results',[]) if any('/'+n==r['url'][-len(n)-1:] for n in ['113129','60683','61362','101638','68950','68979','69867'])]
for r in selected:
 row=dict(r);row['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();key=r['url'].rsplit('/',1)[1]
 try:
  with urllib.request.urlopen(r['url'],timeout=30) as res:b=res.read()
  (p/(key+'.html')).write_bytes(b);t=html.fromstring(b);u=t.xpath('//meta[@name="citation_pdf_url"]/@content')[0].replace('http:','https:',1);row['pdf_url']=u
  with urllib.request.urlopen(u,timeout=45) as res:b=res.read();row.update(status=res.status,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/(key+'.pdf');f.write_bytes(b);d=fitz.open(f);row['pages']=len(d);hits=[];texts=[]
  for i,pg in enumerate(d):
   tx=pg.get_text();texts.append(tx)
   for m in re.finditer(r'Chmiel\w*',tx,re.I):hits.append({'page_pdf':i+1,'context':tx[max(0,m.start()-150):m.end()+350]})
  (p/(key+'.txt')).write_text('\n\f\n'.join(texts));row['hits']=hits
  print(key,json.dumps(hits,ensure_ascii=False),flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 logs.append(row);(p/'readings.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
