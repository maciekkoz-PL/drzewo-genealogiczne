from pathlib import Path
from playwright.sync_api import sync_playwright
import json,datetime,hashlib
p=Path('work/s11/rach_normal');p.mkdir(exist_ok=True);log=[]
with sync_playwright() as play:
 b=play.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(ignore_https_errors=True)
 for key,uid in [('Emilia1904',10504033),('Julia1905',10503949)]:
  url=f'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/{uid}'
  r=dict(key=key,url=url,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
  try:
   resp=page.goto(url,wait_until='domcontentloaded',timeout=30000);page.wait_for_timeout(1500)
   raw=page.content();(p/(key+'.html')).write_text(raw);r['page_status']=resp.status
   api=f'/o/pliki-api/pliki/jednostka/{uid}/0/300'
   result=page.evaluate('async u=>{let r=await fetch(u,{headers:{Accept:"application/json"}});return {status:r.status,text:await r.text()}}',api)
   (p/(key+'_api.json')).write_text(result['text']);r.update(api_status=result['status'],sha256=hashlib.sha256(result['text'].encode()).hexdigest(),size=len(result['text']))
   d=json.loads(result['text']);r['images']=len(d.get('elementy',[]))
  except Exception as e:r['error']=str(e)[:500]
  print(r,flush=True);log.append(r);(p/'log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2))
 b.close()
