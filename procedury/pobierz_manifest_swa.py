from playwright.sync_api import sync_playwright
from pathlib import Path
import urllib.request,urllib.error,urllib.parse,ssl,json
from http.cookiejar import CookieJar
import argparse,datetime,hashlib
parser=argparse.ArgumentParser(description='Publiczny manifest skanów SwA dla znanego ID jednostki lub zespołu; tylko GET/HEAD.')
parser.add_argument('id',type=int)
parser.add_argument('--kind',choices=['jednostka','zespol'],default='jednostka')
parser.add_argument('--count',type=int,default=200)
parser.add_argument('--offset',type=int,default=0)
parser.add_argument('--output',required=True)
args=parser.parse_args()
base=Path(f'work/swa_{args.kind}_{args.id}');base.mkdir(parents=True,exist_ok=True)
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
  rec={'url':request.url,'status':response.status,'size':len(body),'type':response.headers.get('Content-Type'),'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(body).hexdigest()}
  if '/o/pliki-api/' in request.url or request.resource_type=='script' or 'json' in response.headers.get('Content-Type',''):
   out=base/(hashlib.sha256(request.url.encode()).hexdigest()[:16]+'.body');out.write_bytes(body);rec['body_path']=str(out)
  network.append(rec)
  route.fulfill(status=response.status,headers=rh,body=body)
 context.route('**/*',read_route)
 param='zespolid' if args.kind=='zespol' else 'jednostkaid'
 back=f'https://www.szukajwarchiwach.gov.pl/{args.kind}/-/{args.kind}/{args.id}'
 page=context.new_page()
 url=f'https://www.szukajwarchiwach.gov.pl/swa-slider/?{param}={args.id}&jezyk=pl_PL&returnTo='+urllib.parse.quote(back,safe='')
 try:page.goto(url,wait_until='domcontentloaded',timeout=35000)
 except Exception as error:print(type(error).__name__,str(error)[:150])
 page.wait_for_timeout(3000)
 try:page.get_by_role('button',name='Nie',exact=True).click(timeout=1500)
 except Exception:pass
 try:
  response=page.evaluate('async u => {let r=await fetch(u,{headers:{Accept:"application/json"}});return {status:r.status,text:await r.text()}}',f'/o/pliki-api/pliki/{args.kind}/{args.id}/{args.offset}/{args.count}')
  data=json.loads(response['text'])
  assert data[args.kind+'_id']==args.id
  assert isinstance(data['elementy'],list)
  output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
  output.write_text(json.dumps(data,ensure_ascii=False,indent=2))
  print('Zapisano',len(data['elementy']),'z',data.get('liczbaWszystkichSkanow'),'elementów. Offset',args.offset)
 except Exception as error:
  (base/'niepoprawna_odpowiedz.txt').write_text(response.get('text','') if 'response' in locals() else str(error))
  print('Nie uzyskano potwierdzonego manifestu:',str(error)[:200])
 finally:
  (base/'network.json').write_text(json.dumps(network,ensure_ascii=False,indent=2))
 context.close();browser.close()
