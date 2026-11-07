import urllib.request,urllib.parse,http.cookiejar,json,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
from lxml import html
p=Path('badania/2026-11-07-tomasz-nekrologi/zrodla');p.mkdir(parents=True,exist_ok=True)
base=json.loads(Path('badania/2026-11-06-sesja-07-rodzenstwo/zrodla/geneteka/controls.json').read_text())[0]['parameters']
base={**base,'search_lastname':'Chmielewski','search_name':'Tomasz','search_lastname2':'','search_name2':'','pair':'','from_date':'2001','to_date':'2001','bdm':'D','rid':'D','start':'0','length':'50'}
ui='https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=05ld&bdm=D&rid=D'
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
b=op.open(ui,timeout=30).read();t=html.fromstring(b)
regions=[{'id':o.get('value'),'name':' '.join(o.text_content().split())} for o in t.xpath('//select[@name="w"]/option') if o.get('value')]
print('REGIONS',regions,flush=True)
headers={'User-Agent':'Mozilla/5.0','Referer':ui,'X-Requested-With':'XMLHttpRequest'}
def query(tag,params):
 u='https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(params)
 r={'key':tag,'parameters':params,'url':u,'at':datetime.now(timezone.utc).isoformat()}
 try:
  z=op.open(urllib.request.Request(u,headers=headers),timeout=30);d=json.load(z);r.update(status=z.status,total=d.get('recordsTotal'),filtered=d.get('recordsFiltered'),rows=d.get('data'),count=len(d.get('data',[])))
  if 'data' not in d:r['unexpected']=d
 except Exception as e:r['error']=str(e)
 return r
c=query('control_1936',{**base,'w':'05ld','bdm':'S','rid':'S','search_name':'Czesław','search_name2':'Janina','search_lastname2':'Poprawka','pair':'1','from_date':'1936','to_date':'1936'})
(p/'geneteka_kontrola.json').write_text(json.dumps(c,ensure_ascii=False,indent=2));print('CONTROL',c.get('total'),c.get('count'),c.get('error'),flush=True)
assert c.get('count')==1,c
logs=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for r in ex.map(lambda x:query(x['id'],{**base,'w':x['id']}),regions):
  logs.append(r);print(r['key'],r.get('total'),r.get('count'),json.dumps(r.get('rows'),ensure_ascii=False)[:1300],r.get('error'),flush=True)
(p/'geneteka_tomasz_2001.json').write_text(json.dumps({'regions':regions,'queries':logs,'limit':'Kwerenda publicznych indeksów zgonów roku 2001; brak wyniku nie jest przeszukaniem nieudostępnionych aktów USC ani wszystkich parafii.'},ensure_ascii=False,indent=2))
