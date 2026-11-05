"""Pobierz wskazane obrazy SwA z listy JSON url/path; tylko znane URL z manifestu.
Udane istniejące JPG są pomijane. Dziennik: work/browser_scan_<nazwa_zlecenia>/asset_network.json.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import urllib.request,urllib.error,urllib.parse,ssl,json
from http.cookiejar import CookieJar
import sys,datetime,hashlib
jobfile=Path(sys.argv[1]) if len(sys.argv)>1 else Path('work/swa_browser_images1.json')
base=Path('work/browser_scan_'+jobfile.stem);base.mkdir(parents=True,exist_ok=True)
network=[]
jobs=json.loads(jobfile.read_text());targets={j['url']:Path(j['path']) for j in jobs}
# Fetch intercepted browser resources through Python's normal TLS-verified,
# proxy-aware client. Browser certificate checks are not disabled.
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(CookieJar()))
with sync_playwright() as play:
 browser=play.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 context=browser.new_context(viewport={'width':1600,'height':1200})
 def read_route(route,request):
  host=urllib.parse.urlsplit(request.url).hostname or ''
  if not (host.endswith('szukajwarchiwach.gov.pl') or host.endswith('genealodzy.pl')):route.abort();return
  if request.method not in ('GET','HEAD'):route.abort();return
  headers={k:v for k,v in request.all_headers().items() if k.lower() not in ('accept-encoding','host','content-length')}
  headers['Accept-Encoding']='identity'
  req=urllib.request.Request(request.url,headers=headers,method=request.method)
  try:
   response=opener.open(req,timeout=20)
  except urllib.error.HTTPError as error:response=error
  except Exception as error:network.append({'url':request.url,'error':str(error)});route.abort();return
  body=response.read();rh={k:v for k,v in response.headers.items() if k.lower() not in ('transfer-encoding','content-length','connection','content-encoding')}
  network.append({'url':request.url,'status':response.status,'size':len(body),'type':response.headers.get('Content-Type'),'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(body).hexdigest()})
  if body.startswith(b'\xff\xd8\xff') and 'photos.szukajwarchiwach.gov.pl' in host:
   if request.url in targets:targets[request.url].write_bytes(body)
   (base/(urllib.parse.urlsplit(request.url).path.strip('/')+'.jpg')).write_bytes(body)
  route.fulfill(status=response.status,headers=rh,body=body)
 context.route('**/*',read_route)
 for job in jobs:
  target=Path(job['path']);target.parent.mkdir(parents=True,exist_ok=True)
  if target.exists() and target.read_bytes().startswith(b'\xff\xd8\xff'):
   print('POMINIĘTO ISTNIEJĄCY JPG',target,flush=True);continue
  key=target.stem;url=job['url']
  page=context.new_page()
  try:page.goto(url,wait_until='domcontentloaded',timeout=30000)
  except Exception as error:print(key,type(error).__name__,str(error)[:120])
  page.wait_for_timeout(3000)
  print(key,page.title(),page.locator('body').inner_text()[:600],flush=True)
  (base/(key+'_asset.html')).write_text(page.content())
  
  page.close()
 (base/'asset_network.json').write_text(json.dumps(network,ensure_ascii=False,indent=2))
 context.close();browser.close()
