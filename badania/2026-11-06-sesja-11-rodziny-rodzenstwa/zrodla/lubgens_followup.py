from pathlib import Path
import urllib.request,urllib.parse,json,datetime,hashlib
from lxml import html
p=Path('work/s11/lubgens');p.mkdir(exist_ok=True);log=[]
jobs=[('emilia_birth','Chmielew','Emilia','1902','',False),('julia_death','Chmielew','Julia','1901','',False),('wincenty_death','Chmielew','Wincenty','1919','',False)]
for key,surname,name,start,parish,notes in jobs:
 q={('urodz' if 'birth' in key else 'zgony'):'1','parafia':parish,'nazwisko':surname,'imie':name,'rok_od':start,'rok_do':('1905' if key in ['emilia_birth','julia_death'] else '1932'),'wildmode':'1','sort1':'5','sort2':'1','sort3':'3'}
 if notes:q['uwagi']='1'
 url='https://regestry.lubgens.eu/viewpage.php?page_id=1057';r=dict(key=key,url=url,method='POST',parameters=q,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 try:
  with urllib.request.urlopen(urllib.request.Request(url,data=urllib.parse.urlencode(q).encode(),headers={'User-Agent':'Mozilla/5.0','Content-Type':'application/x-www-form-urlencoded'}),timeout=40) as z:b=z.read();r['status']=z.status
  (p/(key+'.html')).write_bytes(b);r.update(size=len(b),sha256=hashlib.sha256(b).hexdigest())
  t=html.fromstring(b,parser=html.HTMLParser(encoding='utf-8'))
  rows=[]
  for tr in t.xpath('//tr'):
   cells=[' '.join(x.text_content().split()) for x in tr.xpath('./td')]
   if len(cells)>3 and any('chmielew' in x.lower() for x in cells):rows.append({'cells':cells,'links':[(a.text_content(),a.get('href')) for a in tr.xpath('.//a[@href]')]})
  r['matches']=rows;print(key,'bytes',len(b),'rows',len(rows),json.dumps(rows,ensure_ascii=False)[:18000],flush=True)
  for x in t.xpath('//script|//style'):x.drop_tree()
  (p/(key+'.txt')).write_text(' '.join(t.text_content().split()))
 except Exception as e:r['error']=str(e);print(key,str(e),flush=True)
 log.append(r);(p/'birth_death_queries.json').write_text(json.dumps(log,ensure_ascii=False,indent=2))
