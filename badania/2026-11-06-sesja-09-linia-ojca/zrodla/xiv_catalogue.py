from pathlib import Path
from playwright.sync_api import sync_playwright
from lxml import html
import json,datetime,hashlib
p=Path('work/s09/xiv_catalogue');p.mkdir(exist_ok=True);logs=[]
jobs=[('registry','https://www.szukajwarchiwach.gov.pl/seria?_Seria_cur=11&_Seria_delta=100&_Seria_id_serii=308541&_Seria_nameofjsp=jednostki&_Seria_resetCur=false&p_p_id=Seria&p_p_lifecycle=0&p_p_mode=view&p_p_state=normal')]
with sync_playwright() as play:
 b=play.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(ignore_https_errors=True)
 page.goto('https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/165812',wait_until='domcontentloaded',timeout=30000)
 for key,url in jobs:
  r={'key':key,'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  try:
   resp=page.goto(url,wait_until='domcontentloaded',timeout=30000);page.wait_for_timeout(1800);raw=page.content();(p/(key+'.html')).write_text(raw);t=html.fromstring(raw)
   for x in t.xpath('//script|//style'):x.drop_tree()
   tx=' '.join(t.text_content().split());(p/(key+'.txt')).write_text(tx);i=tx.find('Typ jednostki');r.update(status=resp.status if resp else None,size=len(raw),sha256=hashlib.sha256(raw.encode()).hexdigest(),metadata=tx[i:i+3000] if i>=0 else tx[-700:]);print(key,r['metadata'],flush=True)
  except Exception as e:r['error']=str(e);print(key,str(e),flush=True)
  logs.append(r);(p/'cards.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
 b.close()
