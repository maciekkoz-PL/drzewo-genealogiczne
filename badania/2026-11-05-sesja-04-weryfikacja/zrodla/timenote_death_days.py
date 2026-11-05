from pathlib import Path
import urllib.request,urllib.parse,json,datetime,hashlib,concurrent.futures
from lxml import html
p=Path('work/h017-s04/timenote');p.mkdir(parents=True,exist_ok=True);logs=[]
def fetch(day):
 u='https://timenote.info/pl/person/list/day/'+day;row={'url':u,'date_parameter':day,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/('day_'+day+'.html');f.write_bytes(b);row['path']=str(f);t=html.fromstring(b)
  row['matching_rows']=[]
  for x in t.xpath('//tr'):
   text=' '.join(x.text_content().split())
   if 'Chmiel' in text:
    row['matching_rows'].append({'text':text,'links':x.xpath('.//a/@href')})
  row['forms']=[{'action':x.get('action'),'method':x.get('method'),'fields':x.xpath('.//input/@name')} for x in t.xpath('//form')]
  print(day,'status',row['status'],'matches',row['matching_rows'],flush=True)
 except Exception as e:row['error']=str(e);print(day,str(e),flush=True)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for row in pool.map(fetch,['19810116','19940522','20011218','19910612']):
  logs.append(row);(p/'death_days_downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
