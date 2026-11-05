from pathlib import Path
import urllib.request, urllib.parse, json, hashlib, datetime

p=Path('work/h017-s04/geneteka');p.mkdir(parents=True,exist_ok=True)
base={k:v[0] for k,v in json.loads(Path('work/boguslaw2/geneteka_template.json').read_text()).items()}
logs=[]
for key,changes in [
 ('control_1936',{}),
 ('ld_S_1900_1960',{'from_date':'1900','to_date':'1960'}),
 ('ld_B_1930_1960',{'bdm':'B','rid':'B','from_date':'1930','to_date':'1960'}),
 ('ld_D_1930_1990',{'bdm':'D','rid':'D','from_date':'1930','to_date':'1990'}),
]:
 q={**base,**changes};url='https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(q)
 row={'url':url,'params':q,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0','Referer':'https://geneteka.genealodzy.pl/'}),timeout=25) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/(key+'.json');f.write_bytes(b);row['path']=str(f);d=json.loads(b)
  print(key,{k:d.get(k) for k in ['recordsTotal','recordsFiltered']},'rows',len(d.get('data',[])),flush=True)
  for line in d.get('data',[]):print(line,flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 logs.append(row);(p/'control_downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
