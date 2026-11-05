from pathlib import Path
import urllib.request,urllib.parse,http.cookiejar,json,hashlib,datetime,concurrent.futures
from lxml import html
p=Path('work/h017-s04/geneteka/surname_pairs');p.mkdir(parents=True,exist_ok=True)
successful=json.loads(Path('work/h017-s04/geneteka/protocol_downloads.json').read_text())[1]
base={k:v[0] for k,v in urllib.parse.parse_qs(urllib.parse.urlsplit(successful['url']).query,keep_blank_values=True).items()}
base.update(search_name='',search_name2='',from_date='1880',to_date='1960')
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
ui=successful['headers']['Referer']
with op.open(ui,timeout=25) as r:r.read()
headers=successful['headers'];logs=[]
regions=html.fromstring(Path('work/h017-s04/catalogues/geneteka.html').read_bytes()).xpath('//select[@name="w"]/option/@value')
def fetch(region,start=0):
 q={**base,'w':region,'start':str(start)};u='https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(q);row={'url':u,'params':q,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with op.open(urllib.request.Request(u,headers=headers),timeout=25) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/(region+'_S_'+str(start)+'.json');f.write_bytes(b);row['path']=str(f);d=json.loads(b);row.update(recordsTotal=d.get('recordsTotal'),rows=len(d.get('data',[])))
  print(region,'total',row['recordsTotal'],'rows',row['rows'],flush=True)
  for x in d.get('data',[]):print(x[:9],flush=True)
 except Exception as e:row['error']=str(e);print(region,str(e),flush=True)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for row in pool.map(fetch,regions):
  logs.append(row);(p/'downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
  if row.get('recordsTotal',0)>50:
   for off in range(50,row['recordsTotal'],50):
    logs.append(fetch(row['params']['w'],off));(p/'downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
print('DONE',len(logs),'requests','rows',sum(x.get('rows',0) for x in logs),flush=True)
