"""Finish previously incomplete public-result scopes, using working Polish URLs."""
from pathlib import Path
import urllib.request, urllib.parse, http.cookiejar
import hashlib, datetime, json, re
from lxml import html

p=Path('work/h017-s04/ipn');p.mkdir(parents=True,exist_ok=True)
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
logs=[]
def get(key, query, page=0):
    args={'fraza':query,'page':page}
    url='https://inwentarz.ipn.gov.pl/szukaj?'+urllib.parse.urlencode(args)
    row={'url':url,'params':args,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        with opener.open(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:
            b=response.read();row.update(status=response.status,final_url=response.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
        f=p/(key+'.html');f.write_bytes(b);row['path']=str(f)
        t=html.fromstring(b);row['actual_query']=t.xpath('//input[@name="fraza"]/@value')
        assert row['actual_query']==[query], 'Search criterion lost in response'
        for bad in t.xpath('//script|//style'):bad.drop_tree()
        text=' '.join(t.text_content().split())
        labels=re.findall(r'(?:Wyniki|Wynik|Results)[^\n]{0,90}',text)
        row['labels']=[s[:100] for s in labels[:5]]
        entries=t.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," views-row ")]')
        row['results']=[{'text':' '.join(e.text_content().split()),'links':e.xpath('.//a[contains(@href,"node")]/@href')} for e in entries]
        row['pager_links']=t.xpath('//a[contains(@href,"page=")]/@href')
        print(key,'rows',len(row['results']),'labels',row['labels'],flush=True)
        for e in row['results']:print(e['text'][:650],flush=True)
        return row
    except Exception as e:
        row['error']=str(e);print(key,'ERROR',str(e),flush=True);return row
    finally:
        logs.append(row);(p/'downloads_and_results.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))

for key,query in [('dob','"25-04-1943"'),('name','Chmielewski Bogusław')]:
    first=get(key+'_p0',query)
    if first.get('error') or not first.get('results'):continue
    page_numbers=[]
    for link in first['pager_links']:
        value=urllib.parse.parse_qs(urllib.parse.urlsplit(link).query).get('page',['0'])[0]
        if str(value).isdigit():page_numbers.append(int(value))
    limit=min(max(page_numbers,default=0),12)
    for number in range(1,limit+1):
        row=get(key+'_p'+str(number),query,number)
        if row.get('error'):break
