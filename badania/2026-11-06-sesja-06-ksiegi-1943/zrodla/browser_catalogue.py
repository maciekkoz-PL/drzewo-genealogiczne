from pathlib import Path
from playwright.sync_api import sync_playwright
import json,datetime
p=Path('work/s06/browser');p.mkdir(exist_ok=True);log=[]
with sync_playwright() as play:
 b=play.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(ignore_https_errors=True,viewport={'width':1440,'height':1000})
 page.on('response',lambda r:log.append({'url':r.url,'status':r.status,'type':r.request.resource_type}))
 try:
  page.goto('https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/165812',wait_until='domcontentloaded',timeout=30000)
  page.wait_for_timeout(3000)
  print(page.title(),page.locator('body').inner_text()[-4000:],flush=True)
  a=page.get_by_role('link',name='Lista jednostek (1076)',exact=True)
  if a.count():
   a.click(timeout=12000);page.wait_for_timeout(2000);print('AFTER',page.locator('body').inner_text()[-5000:],flush=True)
  (p/'fonds.html').write_text(page.content());(p/'fonds.txt').write_text(page.locator('body').inner_text());page.screenshot(path=str(p/'fonds.png'),full_page=True)
 except Exception as e:print(type(e).__name__,str(e)[:400],flush=True)
 (p/'requests.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'responses':log},ensure_ascii=False,indent=2));b.close()
