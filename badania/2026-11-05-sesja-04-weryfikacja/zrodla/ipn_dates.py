from pathlib import Path
import urllib.request, urllib.parse, http.cookiejar, json, hashlib, datetime, re
from lxml import html

p=Path('work/h017-s04/ipn');logs=[]
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
def get(key,url,query=None):
 row={'url':url,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with opener.open(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/(key+'.html');f.write_bytes(b);row['path']=str(f);t=html.fromstring(b)
  row['actual_query']=t.xpath('//input[@name="fraza"]/@value')
  if query is not None:assert row['actual_query']==[query], 'Criterion lost in redirect'
  for bad in t.xpath('//script|//style'):bad.drop_tree()
  text=' '.join(t.text_content().split());m=re.search(r'Wyniki wyszukiwania\s+([\d ]+)\s*-\s*([\d ]+)\s+z\s+(\d+)',text)
  row['count_label']=m.group() if m else None
  e=t.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," views-row ")]')
  row['results']=[{'text':' '.join(x.text_content().split()),'links':x.xpath('.//a[contains(@href,"node")]/@href')} for x in e]
  print(key,row['count_label'],'rows',len(e),'query',row['actual_query'],flush=True)
  return row
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True);return row
 finally:logs.append(row);(p/'dates_downloads_and_results.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
get('dates_warm','https://inwentarz.ipn.gov.pl/szukaj')
q='"25-04-1943"'
first=get('dates_p0','https://inwentarz.ipn.gov.pl/szukaj?'+urllib.parse.urlencode({'fraza':q}),q)
if not first.get('error') and first.get('results'):
 total=int(first['count_label'].rsplit(' ',1)[-1]) if first.get('count_label') else 0
 for n in range(1,min(12,(total+9)//10)):
  r=get('dates_p'+str(n),'https://inwentarz.ipn.gov.pl/szukaj?'+urllib.parse.urlencode({'fraza':q,'page':n}),q)
  if r.get('error'):break
