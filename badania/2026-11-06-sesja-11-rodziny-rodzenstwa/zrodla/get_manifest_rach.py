from playwright.sync_api import sync_playwright
from pathlib import Path
import urllib.request,urllib.error,urllib.parse,ssl,json
from http.cookiejar import CookieJar
base=Path('work/s11/rach_mani');base.mkdir(parents=True,exist_ok=True)
network=[]
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
  import hashlib
  rec={'url':request.url,'status':response.status,'size':len(body),'type':response.headers.get('Content-Type')}
  if '/o/pliki-api/' in request.url or request.resource_type=='script' or 'json' in response.headers.get('Content-Type',''):
   out=base/(hashlib.sha256(request.url.encode()).hexdigest()[:16]+'.body');out.write_bytes(body);rec['body_path']=str(out)
  network.append(rec)
  route.fulfill(status=response.status,headers=rh,body=body)
 context.route('**/*',read_route)
 for key,uid in [('Emilia1904',10504033),('Julia1905',10503949)]:
  url=f'https://www.szukajwarchiwach.gov.pl/swa-slider/?jednostkaid={uid}&jezyk=pl_PL&returnTo=https%3A%2F%2Fwww.szukajwarchiwach.gov.pl%2Fjednostka%2F-%2Fjednostka%2F{uid}'
  page=context.new_page()
  try:page.goto(url,wait_until='domcontentloaded',timeout=35000)
  except Exception as error:print(key,type(error).__name__,str(error)[:120])
  page.wait_for_timeout(4000)
  try:
   page.get_by_role('button',name='Nie',exact=True).click(timeout=1500)
  except Exception:pass
  try:
   result=page.evaluate('async u => {let r=await fetch(u,{headers:{Accept:"application/json"}});return {status:r.status,text:(await r.text()).slice(0,600)}}',f'/o/pliki-api/pliki/jednostka/{uid}/0/300')
   print('API',key,result,flush=True)
  except Exception as error:print('API ERROR',key,str(error)[:200],flush=True)
  text=page.locator('body').inner_text()
  (base/(key+'_tls.html')).write_text(page.content());(base/(key+'_tls.txt')).write_text(text)
  page.screenshot(path=str(base/(key+'_tls.png')),full_page=True)
  print(key,page.title(),text[:800],flush=True)
  page.close()
 (base/'tls_network.json').write_text(json.dumps(network,ensure_ascii=False,indent=2))
 context.close();browser.close()
