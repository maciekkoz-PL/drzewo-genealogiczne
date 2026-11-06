from pathlib import Path
import urllib.request,json,hashlib,datetime,concurrent.futures,sys
from lxml import html
p=Path('work/s07');jobs=json.loads(Path(sys.argv[1]).read_text());logs=[]
def fetch(j):
 k,u=j;r={'key':k,'url':u,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as z:b=z.read();r.update(status=z.status,final_url=z.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/(k+('.pdf' if b.startswith(b'%PDF') else '.html'));f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b);r['path']=str(f)
  if not b.startswith(b'%PDF'):
   t=html.fromstring(b);r['links']=[{'text':' '.join(a.text_content().split()),'url':urllib.parse.urljoin(r['final_url'],a.get('href'))} for a in t.xpath('//a[@href]')]
   for x in t.xpath('//script|//style'):x.drop_tree()
   f.with_suffix('.txt').write_text(' '.join(t.text_content().split()))
 except Exception as e:r['error']=str(e)
 print(k,r.get('status'),r.get('size'),r.get('error',''),flush=True);return r
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for r in pool.map(fetch,jobs):logs.append(r);Path(sys.argv[1]+'.results.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
