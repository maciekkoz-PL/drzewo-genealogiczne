from pathlib import Path
import urllib.request, urllib.parse, datetime, json, hashlib
from lxml import html

p=Path('work/h017-s04/catalogues');p.mkdir(parents=True,exist_ok=True)
logs=[]
urls=[
 ('geneteka.html','https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=05ld'),
 ('ipn_polish_5355242.html','https://inwentarz.ipn.gov.pl/node/5355242'),
 ('ipn_home.html','https://inwentarz.ipn.gov.pl/'),
]
for name,url in urls:
 row={'url':url,'path':str(p/name),'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=25) as response:
   b=response.read();row.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'),size=len(b),sha256=hashlib.sha256(b).hexdigest())
  (p/name).write_bytes(b)
  t=html.fromstring(b)
  if name.startswith('geneteka'):
   print('REGIONS',[(o.get('value'),o.text_content()) for o in t.xpath('//select[@name="w"]/option')],flush=True)
   print('SCRIPTS',[urllib.parse.urljoin(url,s) for s in t.xpath('//script/@src')],flush=True)
  else:print(name,' '.join(t.xpath('//body//text()'))[:700],flush=True)
 except Exception as e:row['error']=str(e)
 logs.append(row);(p/'downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2));print(json.dumps(row,ensure_ascii=False),flush=True)
