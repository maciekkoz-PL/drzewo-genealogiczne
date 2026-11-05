from pathlib import Path
import urllib.request,urllib.parse,datetime,hashlib,json,concurrent.futures,re
from lxml import html
p=Path('work/h017-s04/leads');p.mkdir(parents=True,exist_ok=True)
jobs=[]
for f in [Path('work/h017-s04/additional/WBP_Janina_query.html'),Path('work/h017-s04/searches/wbp_parents_pair.html'),Path('work/h017-s04/searches/wbp_boguslaw_inflected.html')]:
 t=html.fromstring(f.read_bytes())
 for a in t.xpath('//a[@href]'):
  u=a.get('href');tx=' '.join(a.text_content().split())
  if re.search(r'/edition/\d+$',u) and tx:
   key='wbp_'+u.rsplit('/',1)[1]
   if not any(x[0]==key for x in jobs):jobs.append((key,u,tx))
jobs += [
 ('timenote_janina1910','https://timenote.info/pl/Janina-Chmielewska-00.00.1910','Profile, birth year 1910'),
 ('swa_series140681','https://www.szukajwarchiwach.gov.pl/en/web/guest/seria?_Seria_delta=200&_Seria_id_serii=140681&_Seria_nameofjsp=jednostki&_Seria_resetCur=false&p_p_id=Seria&p_p_lifecycle=0&p_p_mode=view&p_p_state=normal&refererPlid=20136','German-period civil-register series'),
 ('swa_fonds165812','https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/165812','Full fonds catalogue, not scans manifest')]
logs=[]
def fetch(job):
 key,u,title=job;row={'key':key,'url':u,'title':title,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/(key+'.html');f.write_bytes(b);row['path']=str(f);t=html.fromstring(b)
  row['resource_links']=[{'text':' '.join(a.text_content().split()),'url':urllib.parse.urljoin(u,a.get('href'))} for a in t.xpath('//a[@href]') if any(s in a.get('href','').lower() for s in ['content','pdf','download','jednostka','export','csv'])]
  for x in t.xpath('//script|//style'):x.drop_tree()
  tx=' '.join(t.text_content().split());(p/(key+'.txt')).write_text(tx)
  print(key,row['status'],len(b),title,flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for row in pool.map(fetch,jobs):
  logs.append(row);(p/'downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
