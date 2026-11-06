from pathlib import Path
import json,urllib.request,urllib.parse,http.cookiejar,hashlib,datetime
p=Path('work/s07/geneteka');p.mkdir(exist_ok=True)
base={k:v[0] for k,v in json.loads(Path('work/boguslaw2/geneteka_template.json').read_text()).items()};base.pop('search_as',None);base.update(pair='1');base['search[value]']=''
for i in range(10):base[f'columns[{i}][name]']='';base[f'columns[{i}][search][value]']=''
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()));ui='https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=05ld&bdm=S&rid=S'
with op.open(ui,timeout=30) as z:z.read()
logs=[]
jobs=[('s1936_pair_current',base),('s1936_pair_without_maiden',{**base,'search_lastname2':''}),('s1936_negative_second',{**base,'search_lastname2':'','search_name2':'ZZZNieistniejace'}),('b1910_janina',{**base,'bdm':'B','rid':'B','search_lastname':'Poprawka','search_name':'Janina','search_lastname2':'','search_name2':'','pair':'','from_date':'1910','to_date':'1910'}),('b1910_parents',{**base,'bdm':'B','rid':'B','search_lastname':'Poprawka','search_name':'Józef','search_lastname2':'Kacprzak','search_name2':'Marianna','from_date':'1910','to_date':'1910'})]
for key,q in jobs:
 u='https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(q);r={'key':key,'url':u,'parameters':q,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with op.open(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','Referer':ui,'X-Requested-With':'XMLHttpRequest'}),timeout=30) as z:b=z.read();r.update(status=z.status,sha256=hashlib.sha256(b).hexdigest())
  (p/(key+'.json')).write_bytes(b);d=json.loads(b);r.update(total=d.get('recordsTotal'),rows=len(d.get('data',[])));print(key,r.get('total'),r.get('rows'),json.dumps(d.get('data',[])[:3],ensure_ascii=False)[:1600],flush=True)
 except Exception as e:r['error']=str(e);print(key,str(e),flush=True)
 logs.append(r);(p/'controls.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
