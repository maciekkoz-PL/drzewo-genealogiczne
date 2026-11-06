from pathlib import Path
from playwright.sync_api import sync_playwright
import json,datetime
out=Path('work/s16')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(ignore_https_errors=True);network=[]
 def capture(r):
  if 'gct.net.au' not in r.url:return
  rec=dict(url=r.url,status=r.status,type=r.request.resource_type,post_data=r.request.post_data)
  if r.request.resource_type in ['xhr','fetch']:
   try:
    raw=r.body();key='gct_response_'+str(len(network));(out/(key+'.bin')).write_bytes(raw);rec['saved']=key+'.bin'
   except Exception as e:rec['error']=str(e)
  network.append(rec)
 page.on('response',capture)
 try:
  response=page.goto('https://gct.net.au/family-history-search/',wait_until='domcontentloaded',timeout=45000)
  page.locator('#lastName').fill('Chmielewski');page.locator('#deceasedSearchForm button[type=submit]').click();page.wait_for_timeout(7000)
  text=page.locator('body').inner_text();(out/'gct_results.txt').write_text(text);(out/'gct_results.html').write_text(page.content());page.locator('.view-details-btn').first.click();page.wait_for_timeout(4000);print('DETAILIFRAMES',page.locator('iframe').evaluate_all('(es)=>es.map(e=>e.src)'));(out/'gct_details.html').write_text(page.content());print('HTTP',response.status,'RESULT',text[-13000:])
 except Exception as e:print('ERROR',str(e))
 (out/'gct_details_network.json').write_text(json.dumps(network,ensure_ascii=False,indent=2)+'\n');b.close()
