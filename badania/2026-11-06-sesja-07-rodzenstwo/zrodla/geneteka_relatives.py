from pathlib import Path
import json,urllib.request,urllib.parse,http.cookiejar,concurrent.futures,datetime,hashlib
from lxml import html
p=Path('work/s07/geneteka');controls=json.loads((p/'controls.json').read_text());assert controls[0]['total']==1 and controls[2]['total']==0 and controls[4]['total']==1
base=controls[0]['parameters'];op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()));ui='https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=05ld&bdm=B&rid=B'
with op.open(ui,timeout=30) as z:z.read()
headers={'User-Agent':'Mozilla/5.0','Referer':ui,'X-Requested-With':'XMLHttpRequest'}
t=html.fromstring(Path('work/h017-s04/catalogues/geneteka.html').read_bytes());regions=[x.get('value') for x in t.xpath('//select[@name="w"]/option') if x.get('value')];jobs=[]
for reg in regions:
 for kind,end in [('B','1955'),('D','2005')]:jobs.append((reg+'_'+kind+'_parents_any_maiden',{**base,'w':reg,'bdm':kind,'rid':kind,'search_lastname2':'','from_date':'1928','to_date':end}))
for kind,end in [('B','1955'),('D','2005')]:
 for key,surname,name in [('father','Chmielewski','Czesław'),('mother','Poprawka','Janina')]:jobs.append(('05ld_'+kind+'_'+key,{**base,'w':'05ld','bdm':kind,'rid':kind,'search_lastname':surname,'search_name':name,'search_lastname2':'','search_name2':'','pair':'','from_date':'1928','to_date':end}))
def fetch(j):
 key,q=j;u='https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(q);r={'key':key,'url':u,'parameters':q,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with op.open(urllib.request.Request(u,headers=headers),timeout=30) as z:b=z.read();r.update(status=z.status,sha256=hashlib.sha256(b).hexdigest())
  f=p/(key+'.json');f.write_bytes(b);d=json.loads(b);r.update(total=d.get('recordsTotal'),rows=len(d.get('data',[])),path=str(f));r['complete']=r['total']==r['rows']
  if r['rows']:print(key,r['total'],r['rows'],json.dumps(d['data'],ensure_ascii=False)[:5500],flush=True)
 except Exception as e:r['error']=str(e);print(key,str(e),flush=True)
 return r
logs=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for r in pool.map(fetch,jobs):logs.append(r);(p/'relatives_queries.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
print('DONE',len(logs),'queries, rows',sum(r.get('rows',0) for r in logs),'incomplete',sum(not r.get('complete') for r in logs),flush=True)
