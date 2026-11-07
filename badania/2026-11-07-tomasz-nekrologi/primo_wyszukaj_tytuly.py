from playwright.sync_api import sync_playwright
from pathlib import Path
import urllib.parse,json
p=Path('badania/2026-11-07-tomasz-nekrologi/zrodla')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page();page.set_default_timeout(10000)
 for tag,title in [('dziennik','Dziennik Łódzki - Wiadomości Dnia'),('express','Express Ilustrowany')]:
  u='https://omnis-wbpl.primo.exlibrisgroup.com/discovery/search?'+urllib.parse.urlencode({'query':'title,exact,'+title,'tab':'LibraryCatalog','search_scope':'MyInstitution','vid':'48OMNIS_WBPL:48OMNIS_WBPL','offset':'0'})
  page.goto(u,wait_until='domcontentloaded',timeout=45000);page.wait_for_timeout(6000)
  s=page.locator('body').inner_text();(p/('primo_'+tag+'_tytul.txt')).write_text(s)
  links=page.locator('a[href]').evaluate_all('(els)=>els.map(x=>({text:x.innerText,url:x.href})).filter(x=>x.text&&x.url.includes("fulldisplay"))')
  (p/('primo_'+tag+'_tytul.json')).write_text(json.dumps({'url':page.url,'links':links},ensure_ascii=False,indent=2))
  print(tag,s[:7800],flush=True);print('LINKS',json.dumps(links,ensure_ascii=False)[:6500],flush=True)
 b.close()
