from pathlib import Path
import json,urllib.request,urllib.parse,hashlib,datetime,concurrent.futures,sys
from lxml import html
base=Path('work/s11');jobs=json.loads(Path(sys.argv[1]).read_text());logs=[]
def get(job):
 key,url=job;r={'key':key,'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as z:b=z.read();r.update(status=z.status,final_url=z.url,sha256=hashlib.sha256(b).hexdigest(),size=len(b))
  ext='.pdf' if b.startswith(b'%PDF') else '.jpg' if b.startswith(b'\xff\xd8') else '.html';p=base/(key+ext);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);r['path']=str(p)
  if ext=='.html':
   t=html.fromstring(b,parser=html.HTMLParser(encoding='utf-8'));r['links']=[{'text':' '.join(a.text_content().split()),'url':urllib.parse.urljoin(r['final_url'],a.get('href'))} for a in t.xpath('//a[@href]')]
   for x in t.xpath('//script|//style'):x.drop_tree()
   p.with_suffix('.txt').write_text(' '.join(t.text_content().split()))
 except Exception as e:r['error']=str(e)
 print(key,r.get('status'),r.get('size'),r.get('error',''),flush=True);return r
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for r in pool.map(get,jobs):logs.append(r);Path(sys.argv[1]+'.results.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
