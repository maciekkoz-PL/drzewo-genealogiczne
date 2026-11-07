from playwright.sync_api import sync_playwright
from pathlib import Path
import json
p=Path('badania/2026-11-07-tomasz-nekrologi/zrodla')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page();page.set_default_timeout(12000)
 for tag,ident in [('dziennik','991001051609708836'),('express','991001051299708836')]:
  u='https://omnis-wbpl.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma'+ident+'&context=L&vid=48OMNIS_WBPL:48OMNIS_WBPL&lang=pl&search_scope=MyInstitution&adaptor=Local%20Search%20Engine&tab=LibraryCatalog'
  page.goto(u,wait_until='domcontentloaded',timeout=45000);page.wait_for_timeout(6000)
  s=page.locator('body').inner_text();(p/('primo_'+tag+'_egzemplarze_start.txt')).write_text(s)
  print(tag,s[-10500:],flush=True)
  buttons=page.locator('button').evaluate_all('(els)=>els.map(x=>({text:x.innerText,label:x.getAttribute("aria-label")})).filter(x=>x.text||x.label)')
  (p/('primo_'+tag+'_egzemplarze_start.json')).write_text(json.dumps({'url':page.url,'buttons':buttons},ensure_ascii=False,indent=2));print('BUTTONS',json.dumps(buttons,ensure_ascii=False)[-5500:],flush=True)
 b.close()
