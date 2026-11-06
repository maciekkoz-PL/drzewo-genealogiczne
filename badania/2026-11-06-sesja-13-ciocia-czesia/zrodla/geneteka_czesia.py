from pathlib import Path
import json,urllib.request,urllib.parse,datetime,hashlib,concurrent.futures,re
from lxml import html
p=Path('work/s13/geneteka');p.mkdir(exist_ok=True)
base=json.loads(Path('work/s07/geneteka/controls.json').read_text())[0]['parameters']
base.update(search_name='',search_lastname='Chmielewski',search_lastname2='',search_name2='Czesława',pair='1',start='0',length='50',from_date='1920',to_date='1970')
headers={'User-Agent':'Mozilla/5.0','Referer':'https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=05ld&bdm=S&rid=S','X-Requested-With':'XMLHttpRequest'}
def fetch(job):
 key,q=job;u='https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(q);row=dict(key=key,url=u,parameters=q,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers=headers),timeout=35) as r:b=r.read();row['status']=r.status
  (p/(key+'.json')).write_bytes(b);d=json.loads(b);row.update(total=d.get('recordsTotal'),rows=len(d.get('data',[])),sha256=hashlib.sha256(b).hexdigest())
  row['complete']=row['total']==row['rows'];print(key,row['total'],row['rows'],flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 return row
control=fetch(('kontrola_drugie_imie_Janina',{**base,'w':'05ld','search_name2':'Janina','search_lastname2':'Poprawka','from_date':'1936','to_date':'1936'}))
(p/'kontrola.json').write_text(json.dumps(control,ensure_ascii=False,indent=2))
assert control.get('total')==1 and control.get('rows')==1,control
h=html.fromstring(Path('work/h017-s04/catalogues/geneteka.html').read_bytes())
regions=[a.get('value') for a in h.xpath('//select[@name="w"]/option') if a.get('value')]
jobs=[(reg+'_Chmielewski_Czeslawa',{**base,'w':reg}) for reg in regions];rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for row in ex.map(fetch,jobs):rows.append(row);(p/'queries.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('DONE',len(rows),'returned',sum(x.get('rows',0) for x in rows),'total',sum(x.get('total',0) for x in rows),'incomplete',[x['key'] for x in rows if not x.get('complete')])
