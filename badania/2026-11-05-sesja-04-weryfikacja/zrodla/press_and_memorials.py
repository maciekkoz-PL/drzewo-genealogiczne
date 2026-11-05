from pathlib import Path
import urllib.request,urllib.parse,datetime,hashlib,json,concurrent.futures
from lxml import html
p=Path('work/h017-s04/searches');p.mkdir(parents=True,exist_ok=True);logs=[]
jobs=[]
for key,q in [('wbp_boguslaw','"Bogusław Chmielewski"'),('wbp_janina_poprawka','"Janina Poprawka"'),('wbp_parents_pair','"Czesław Chmielewski" "Janina"'),('wbp_boguslaw_inflected','"Bogusława Chmielewskiego"')]:
 jobs.append((key,'https://bc.wbp.lodz.pl/dlibra/results?'+urllib.parse.urlencode({'q':q,'action':'SimpleSearchAction','type':'-6','p':'0'}),q))
for key,q in [('timenote_janina','Janina Chmielewska'),('timenote_czeslaw','Czesław Chmielewski'),('timenote_maiden','Janina Poprawka'),('timenote_boguslaw','Bogusław Chmielewski')]:
 jobs.append((key,'https://timenote.info/pl/search?'+urllib.parse.urlencode({'q':q}),q))
def fetch(job):
 key,u,q=job;row={'url':u,'query':q,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/(key+'.html');f.write_bytes(b);row['path']=str(f);t=html.fromstring(b)
  for x in t.xpath('//script|//style'):x.drop_tree()
  text=' '.join(t.text_content().split());(p/(key+'.txt')).write_text(text)
  if key.startswith('wbp'):
   row['links']=[{'text':' '.join(a.text_content().split()),'url':urllib.parse.urljoin(u,a.get('href'))} for a in t.xpath('//a[@href]') if any(s in a.get('href','') for s in ['/publication/','/doccontent','/edition/'])]
  else:
   row['rows']=[{'text':' '.join(x.text_content().split()),'links':x.xpath('.//a/@href')} for x in t.xpath('//tr') if 'Chmiel' in x.text_content() or 'Popraw' in x.text_content()]
   row['links']=[{'text':' '.join(a.text_content().split()),'url':urllib.parse.urljoin(u,a.get('href'))} for a in t.xpath('//a[@href]') if ('Chmiel' in a.get('href','') or 'Popraw' in a.get('href',''))]
  row['tail']=text[-1800:]
  print(key,'links',row.get('links',[])[:20],'rows',row.get('rows',[])[:10],flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for row in pool.map(fetch,jobs):
  logs.append(row);(p/'downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
