from pathlib import Path
import urllib.request,urllib.parse,concurrent.futures,json,datetime,re,hashlib,fitz
from lxml import html
p=Path('/workspace/drzewo-genealogiczne/badania/2026-11-07-tomasz-prasa/zrodla');p.mkdir(exist_ok=True)
ids=['51509','64048','52322','52606','64736','75962']
t=html.fromstring((p/'wbp_tomasz.html').read_bytes());links={a.get('href').rsplit('/',1)[-1]:a.get('href') for a in t.xpath('//a[@href]') if '/edition/' in a.get('href','') and a.get('href','').rsplit('/',1)[-1].isdigit()}
def read(id):
 row={'edition':id,'url':links[id],'at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(links[id],timeout=20);data=r.read();(p/f'edition_{id}.html').write_bytes(data);t=html.fromstring(data);urls=t.xpath('//meta[@name="citation_pdf_url"]/@content')
  if not urls:row['status']='no PDF URL';row['local_only']='sieci lokalnej' in t.text_content();return row
  u=urls[0].replace('http:','https:',1);row['pdf_url']=u;r=urllib.request.urlopen(u,timeout=25);data=r.read();assert data.startswith(b'%PDF'),data[:40];(p/f'{id}.pdf').write_bytes(data);d=fitz.open(stream=data,filetype='pdf');row['pages']=len(d);row['bytes']=len(data);row['sha256']=hashlib.sha256(data).hexdigest();texts=[];hits=[]
  for n,pg in enumerate(d,1):
   tx=pg.get_text();texts.append(tx)
   for m in re.finditer(r'Chmielew\w*',tx,re.I):hits.append({'page_pdf':n,'context':tx[max(0,m.start()-450):m.end()+650]})
  row['hits']=hits;(p/f'{id}.txt').write_text('\n\f\n'.join(texts));row['status']='PDF downloaded and text searched'
 except Exception as e:row['error']=str(e)
 print(id,json.dumps(row,ensure_ascii=False),flush=True);return row
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(read,ids))
(p/'readings.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
