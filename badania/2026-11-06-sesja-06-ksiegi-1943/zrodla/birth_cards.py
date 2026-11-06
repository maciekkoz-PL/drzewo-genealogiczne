from pathlib import Path
from playwright.sync_api import sync_playwright
import json,datetime
p=Path('work/s06/birth_cards');p.mkdir(exist_ok=True);units=json.loads(Path('work/s06/units/units.json').read_text());selected=[u for u in units if u['signature'].rsplit('/',1)[-1] in ['986','990','997']];log=[]
with sync_playwright() as play:
 b=play.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(ignore_https_errors=True,viewport={'width':1440,'height':1000})
 for u in selected:
  n=u['signature'].rsplit('/',1)[-1]
  try:
   r=page.goto(u['url'],wait_until='domcontentloaded',timeout=30000);page.wait_for_timeout(1000)
   tx=page.locator('body').inner_text();(p/(n+'.txt')).write_text(tx);(p/(n+'.html')).write_text(page.content());page.screenshot(path=str(p/(n+'.png')),full_page=True);log.append({'signature':u['signature'],'url':page.url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':r.status if r else None,'text':tx});print(n,tx[-10000:],flush=True)
  except Exception as e:log.append({'signature':u['signature'],'error':str(e)});print(n,str(e),flush=True)
  (p/'readings.json').write_text(json.dumps(log,ensure_ascii=False,indent=2))
 b.close()
