from playwright.sync_api import sync_playwright
from pathlib import Path
import json
p=Path('badania/2026-11-07-tomasz-dalsze/zrodla')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page();page.set_default_timeout(8000)
 try:
  page.goto('https://rejestry-notarialne.pl/37',wait_until='domcontentloaded',timeout=30000);page.wait_for_timeout(3500)
  page.locator('select').select_option('2');page.wait_for_timeout(600)
  s=page.locator('body').inner_text();(p/'rs_formularz_dane_tekst.txt').write_text(s)
  fields=page.locator('input,select').evaluate_all('(els)=>els.filter(e=>e.type!=="hidden").map(e=>({tag:e.tagName,id:e.id,name:e.name,type:e.type,required:e.required,color:getComputedStyle(e).backgroundColor,classes:e.className,title:e.title,options:e.tagName==="SELECT"?Array.from(e.options).map(o=>({value:o.value,text:o.text})):undefined}))')
  (p/'rs_formularz_dane_pola.json').write_text(json.dumps(fields,ensure_ascii=False,indent=2))
  print('BODY',s[-4500:],flush=True);print('FIELDS',json.dumps(fields,ensure_ascii=False),flush=True)
  page.screenshot(path='/tmp/rs-dane.png',full_page=True)
 except Exception as e:print(type(e).__name__,str(e),flush=True)
 b.close()
