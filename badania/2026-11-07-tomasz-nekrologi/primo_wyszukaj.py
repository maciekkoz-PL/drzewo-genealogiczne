from playwright.sync_api import sync_playwright
from pathlib import Path
import json
p=Path('badania/2026-11-07-tomasz-nekrologi/zrodla')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page();page.set_default_timeout(15000)
 page.goto('https://omnis-wbpl.primo.exlibrisgroup.com/discovery/search?vid=48OMNIS_WBPL:48OMNIS_WBPL',wait_until='domcontentloaded',timeout=45000)
 page.locator('#searchBar').fill('"Dziennik Łódzki"')
 page.locator('#searchBar').press('Enter');page.wait_for_timeout(6500)
 s=page.locator('body').inner_text();(p/'primo_dziennik_wyniki.txt').write_text(s)
 print('URL',page.url,flush=True);print(s[:16000],flush=True)
 links=page.locator('a[href]').evaluate_all('(els)=>els.map(x=>({text:x.innerText,url:x.href})).filter(x=>x.text.includes("Dziennik")||x.url.includes("fulldisplay"))')
 (p/'primo_dziennik_wyniki.json').write_text(json.dumps({'url':page.url,'links':links},ensure_ascii=False,indent=2));print('LINKS',json.dumps(links,ensure_ascii=False)[:7000],flush=True)
 b.close()
