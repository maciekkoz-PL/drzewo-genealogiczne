from pathlib import Path
import urllib.request,urllib.parse,http.cookiejar,json,hashlib,datetime,re
from lxml import html
p=Path('work/h017-s04/ipn');op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()));logs=[]
def get(key,url,q=None):
 row={'url':url,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with op.open(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  f=p/(key+'.html');f.write_bytes(b);row['path']=str(f);t=html.fromstring(b);row['actual_query']=t.xpath('//input[@name="fraza"]/@value')
  if q is not None:assert row['actual_query']==[q],'Criterion lost'
  for x in t.xpath('//script|//style'):x.drop_tree()
  text=' '.join(t.text_content().split());m=re.search(r'(?:Wyniki wyszukiwania|Results)\s+([\d ,]+)\s*-\s*([\d ,]+)\s+(?:z|of)\s+([\d,]+)',text)
  row['count_label']=m.group() if m else None;row['total']=int(m.group(3).replace(',','')) if m else None
  row['results']=[{'text':' '.join(e.text_content().split()),'links':e.xpath('.//a[contains(@href,"node")]/@href')} for e in t.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," views-row ")]')]
  print(key,row['actual_query'],row['count_label'],'rows',len(row['results']),flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 logs.append(row);(p/'english_dates_downloads_and_results.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2));return row
get('en_warm','https://inwentarz.ipn.gov.pl/en/search')
q='"25-04-1943"';base='https://inwentarz.ipn.gov.pl/en/search?'
first=get('en_dates_p0',base+urllib.parse.urlencode({'fraza':q}),q)
if not first.get('error') and first.get('results'):
 for n in range(1,min(12,(first.get('total',0)+9)//10)):
  row=get('en_dates_p'+str(n),base+urllib.parse.urlencode({'fraza':q,'page':n}),q)
  if row.get('error'):break
