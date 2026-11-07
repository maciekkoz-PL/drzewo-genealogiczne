from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime, timezone
import json,re
out=Path('badania/2026-11-07-tomasz-dalsze/zrodla')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(viewport={'width':390,'height':844}); page.set_default_timeout(10000)
 page.goto('https://www.wirtualnycmentarz.pl/',wait_until='domcontentloaded',timeout=30000)
 def cookies():
  reject=page.get_by_role('button',name=re.compile('odrzu',re.I))
  if reject.count() and reject.first.is_visible():reject.first.click()
 cookies();page.get_by_role('button',name='Wejście na cmentarz',exact=True).click();page.wait_for_timeout(7000)
 page.locator('button.noShadow').first.click();page.wait_for_timeout(1000)
 for i,q in enumerate(['Chmielewski','Tomasz Chmielewski','Nowak']):
  inp=page.locator('input[type="text"]:not([readonly]):visible').first
  inp.fill(q);cookies()
  with page.expect_response(lambda r:'/api/funerals/datatables/graveyard' in r.url,timeout=20000) as ri:
   page.mouse.click(336,102)
  r=ri.value;d=r.json()
  print(q,'STATUS',r.status,'KEYS',list(d),flush=True)
  payload=d.get('data',{})
  print('PAYLOAD_KEYS',list(payload) if isinstance(payload,dict) else 'list',flush=True)
  records=payload if isinstance(payload,list) else payload.get('data',payload.get('items',payload.get('rows',[])))
  if not isinstance(records,list):records=[]
  print('DATA_LENGTH',len(records),'RECORD_KEYS',list(records[0]) if records and isinstance(records[0],dict) else [],flush=True)
  safe={'url':r.url,'at':datetime.now(timezone.utc).isoformat(),'query':q,'status':r.status,'response_keys':list(d),'counts':{k:v for k,v in (payload.items() if isinstance(payload,dict) else d.items()) if k in ('recordsTotal','recordsFiltered','draw','total','filtered')},'records':[]}
  for record in (records if i < 2 else []):
   if isinstance(record,dict):safe['records'].append({k:v for k,v in record.items() if k in ['id','name','surname','date_of_birth','date_of_death','url','slug']})
  safe['returned_rows']=len(records)
  if i == 2:safe['control']='Kontrola techniczna; bez archiwizowania danych niepowiązanych osób.'
  (out/f'wirtualny_api_{i}.json').write_text(json.dumps(safe,ensure_ascii=False,indent=2))
  print('COUNTS',safe['counts'],flush=True)
  page.wait_for_timeout(700)
 page.screenshot(path='/tmp/wirtualny-api.png',full_page=True)
 b.close()
