from pathlib import Path
import urllib.request,urllib.parse,json,datetime,hashlib
from http.cookiejar import CookieJar
from lxml import html
p=Path('work/s07/municipal');p.mkdir(parents=True,exist_ok=True);logs=[]
base='https://www.cmentarzekomunalne.lodz.systkom.pl'
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(CookieJar()))
with op.open(base+'/szukaj.html',timeout=30) as r:b=r.read()
page=html.fromstring(b)
for key,name in [('witold','Witold'),('czeslaw','Czesław'),('janina','Janina'),('boguslaw','Bogusław')]:
 csrf=page.xpath('//input[@name="_csrf"]/@value')
 if not csrf:print('NO CSRF — no request sent',flush=True);break
 data={'lastName':'Chmielewski','wholeLastName':'true','_wholeLastName':'on','firstName':name,'yearOfBirthFrom':'1800','yearOfBirthTo':'2026','yearOfDeathFrom':'1800','yearOfDeathTo':'2026','cementary':['SZCZE','ZARZW','CDOLY'],'_cementary':['on','on','on'],'_csrf':csrf[0]}
 # Feminine surname must be searched explicitly with exact matching.
 if key=='janina':data['lastName']='Chmielewska'
 row={'key':key,'url':base+'/szukaj','method':'POST — public read-only search','parameters':{k:v for k,v in data.items() if k!='_csrf'},'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(base+'/szukaj',data=urllib.parse.urlencode(data,doseq=True).encode(),headers={'User-Agent':'Mozilla/5.0','Referer':base+'/szukaj.html'})
  with op.open(req,timeout=40) as r:b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
  (p/(key+'.html')).write_bytes(b);page=html.fromstring(b)
  rows=[]
  for tr in page.xpath('//tr'):
   cells=[' '.join(c.text_content().split()) for c in tr.xpath('./td')]
   if cells:rows.append({'cells':cells,'links':[urllib.parse.urljoin(base,a) for a in tr.xpath('.//a/@href')]})
  row['rows']=rows
  for x in page.xpath('//script|//style'):x.drop_tree()
  (p/(key+'.txt')).write_text(' '.join(page.text_content().split()));print(key,json.dumps(rows,ensure_ascii=False),flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 logs.append(row);(p/'searches.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
