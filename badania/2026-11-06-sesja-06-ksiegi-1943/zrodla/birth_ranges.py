from pathlib import Path
from playwright.sync_api import sync_playwright
from lxml import html
import json,re,datetime,sys
p=Path('work/s06/birth_ranges');p.mkdir(exist_ok=True);units=json.loads(Path('work/s06/units/units.json').read_text());selected=[u for u in units if u['signature'].rsplit('/',1)[-1] in (sys.argv[1:] or ['987','988','989','990'])];logs=json.loads((p/'readings.json').read_text()) if (p/'readings.json').exists() else []
with sync_playwright() as play:
 b=play.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(ignore_https_errors=True)
 page.goto('https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/165812',wait_until='domcontentloaded',timeout=30000)
 for u in selected:
  n=u['signature'].rsplit('/',1)[-1];r={'signature':u['signature'],'url':u['url'],'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  try:
   z=page.goto(u['url'],wait_until='domcontentloaded',timeout=30000);page.wait_for_timeout(2500);raw=page.content();(p/(n+'.html')).write_text(raw);t=html.fromstring(raw)
   for x in t.xpath('//script|//style'):x.drop_tree()
   tx=' '.join(t.text_content().split());(p/(n+'.txt')).write_text(tx);i=tx.find('Typ jednostki');r.update(status=z.status if z else None,metadata=tx[i:i+2800] if i>=0 else tx[-1000:]);print(n,r['metadata'],flush=True)
  except Exception as e:r['error']=str(e);print(n,str(e),flush=True)
  logs.append(r);(p/'readings.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
 b.close()
