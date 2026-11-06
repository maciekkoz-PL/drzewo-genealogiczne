from pathlib import Path
import json,urllib.request,urllib.parse,http.cookiejar,concurrent.futures,datetime,hashlib
from lxml import html
p=Path('work/s11/geneteka');p.mkdir(exist_ok=True)
base=json.loads(Path('work/s07/geneteka/controls.json').read_text())[0]['parameters']
base.update(search_lastname2='',search_name2='',pair='',start='0',length='100')
ui='https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=03lb&bdm=S&rid=S'
headers={'User-Agent':'Mozilla/5.0','Referer':ui,'X-Requested-With':'XMLHttpRequest'}
def fetch(job):
 key,q=job;u='https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(q)
 r=dict(key=key,url=u,parameters=q,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers=headers),timeout=35) as z:b=z.read();r['status']=z.status
  f=p/(key+'.json');f.write_bytes(b);d=json.loads(b);r.update(sha256=hashlib.sha256(b).hexdigest(),path=str(f),total=d.get('recordsTotal'),rows=len(d.get('data',[])));r['complete']=r['total']==r['rows']
  print(key,r['total'],r['rows'],flush=True)
 except Exception as e:r['error']=str(e);print(key,r['error'],flush=True)
 return r
control=fetch(('control_1936',{**base,'w':'05ld','bdm':'S','rid':'S','search_lastname':'Chmielewski','search_name':'Czesław','search_lastname2':'Poprawka','search_name2':'Janina','pair':'1','from_date':'1936','to_date':'1936'}))
(p/'control_log.json').write_text(json.dumps(control,ensure_ascii=False,indent=2))
assert control.get('rows')==1 and control.get('total')==1,control
t=html.fromstring(Path('work/h017-s04/catalogues/geneteka.html').read_bytes())
regions=[x.get('value') for x in t.xpath('//select[@name="w"]/option') if x.get('value')]
jobs=[]
for reg in regions:
 for person,surname,name,start in [('julianna','Chmielewska','Julianna','1923'),('sabina','Chmielewska','Sabina','1933'),('roman','Chmielewski','Roman','1935')]:
  jobs.append((reg+'_'+person+'_marriages',{**base,'w':reg,'bdm':'S','rid':'S','search_lastname':surname,'search_name':name,'from_date':start,'to_date':'1970'}))
logs=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for r in pool.map(fetch,jobs):logs.append(r);(p/'queries.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
print('DONE',len(logs),'queries; rows',sum(r.get('rows',0) for r in logs),'incomplete',sum(not r.get('complete') for r in logs))
