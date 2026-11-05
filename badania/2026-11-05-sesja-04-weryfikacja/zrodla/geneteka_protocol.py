from pathlib import Path
import urllib.request, urllib.parse, http.cookiejar, json, datetime, hashlib

p=Path('work/h017-s04/geneteka');logs=[]
base={k:v[0] for k,v in json.loads(Path('work/boguslaw2/geneteka_template.json').read_text()).items()}
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
ui='https://geneteka.genealodzy.pl/index.php?'+urllib.parse.urlencode({k:v for k,v in base.items() if not (k.startswith('columns[') or k.startswith('order[') or k.startswith('search['))})
def request(key,url,headers):
 row={'url':url,'headers':headers,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with opener.open(urllib.request.Request(url,headers=headers),timeout=25) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/(key+('.html' if key=='ui' else '.json'));f.write_bytes(b);row['path']=str(f)
  if key!='ui':
   d=json.loads(b);print(key,d.get('recordsTotal'),'rows',len(d.get('data',[])),flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 logs.append(row);(p/'protocol_downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
request('ui',ui,{'User-Agent':'Mozilla/5.0'})
q=base.copy();q['search[value]']=''
for i in range(10):q[f'columns[{i}][name]']='';q[f'columns[{i}][search][value]']=''
request('control_full_xhr','https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(q),{'User-Agent':'Mozilla/5.0','Referer':ui,'X-Requested-With':'XMLHttpRequest'})
request('control_research_ua','https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(base),{'User-Agent':'Mozilla/5.0 (genealogical source verification; read-only)'})
