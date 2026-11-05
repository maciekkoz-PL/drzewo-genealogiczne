from pathlib import Path
import urllib.request,json,hashlib,concurrent.futures,datetime,re,fitz
from lxml import html
p=Path('work/h017-s04/leads');out=p/'pdf';out.mkdir(exist_ok=True)
jobs=[]
for f in p.glob('wbp_*.html'):
 t=html.fromstring(f.read_bytes());u=t.xpath('//meta[@name="citation_pdf_url"]/@content')
 if u:jobs.append((f.stem,u[0].replace('http:','https:',1)))
def read(job):
 key,u=job;row={'key':key,'url':u,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(u,timeout=40) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=out/(key+'.pdf');f.write_bytes(b);d=fitz.open(f);row['pages']=len(d);hits=[];texts=[]
  for i,page in enumerate(d):
   tx=page.get_text();texts.append(tx)
   for m in re.finditer(r'Chmiel\w*|Popraw\w*',tx,re.I):
    context=tx[max(0,m.start()-200):m.end()+350]
    hits.append({'page_pdf':i+1,'context':context})
  (out/(key+'.txt')).write_text('\n\f\n'.join(texts));row['hits']=hits
  print(key,len(b),len(d),'hits',len(hits),flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 return row
logs=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for row in pool.map(read,jobs):
  logs.append(row);(out/'readings.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
