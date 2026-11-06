from pathlib import Path
from playwright.sync_api import sync_playwright
import json,datetime
OUT=Path('work/s16');logs=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 for key,url in [('tuckers','https://www.tuckers.com.au/funerals/past-funerals/'),('bdm','https://my.rio.bdm.vic.gov.au/efamily-history/-')]:
  page=b.new_page(ignore_https_errors=True);network=[]
  page.on('response',lambda r:network.append(dict(url=r.url,status=r.status,type=r.request.resource_type)))
  try:
   r=page.goto(url,wait_until='domcontentloaded',timeout=45000);page.wait_for_timeout(4000)
   print(key,'HTTP',r.status,page.locator('body').inner_text()[:11500],flush=True)
   (OUT/(key+'_browser.html')).write_text(page.content());(OUT/(key+'_browser.txt')).write_text(page.locator('body').inner_text())
   print('INPUTS',key,page.locator('input').evaluate_all('(els)=>els.map(e=>({id:e.id,name:e.name,type:e.type,placeholder:e.placeholder}))'),flush=True)
   print('SELECTS',key,page.locator('select').evaluate_all('(els)=>els.map(e=>({id:e.id,name:e.name,html:e.outerHTML}))'),flush=True)
   if key=='tuckers':
    page.get_by_placeholder('Try searching for a name').fill('Chmielewski');page.wait_for_timeout(3500)
    (OUT/'tuckers_results.html').write_text(page.content());(OUT/'tuckers_results.txt').write_text(page.locator('body').inner_text());print('TUCKERSRESULT',page.locator('body').inner_text()[4500:13000],flush=True)
  except Exception as e:print(key,'ERROR',str(e),flush=True)
  (OUT/(key+'_network.json')).write_text(json.dumps(network,ensure_ascii=False,indent=2)+'\n');page.close()
 b.close()
