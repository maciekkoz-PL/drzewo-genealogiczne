from playwright.sync_api import sync_playwright
from pathlib import Path
import json,re
p=Path('badania/2026-11-07-tomasz-nekrologi/zrodla')
u='https://omnis-wbpl.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma991001051609708836&context=L&vid=48OMNIS_WBPL:48OMNIS_WBPL&lang=pl&search_scope=MyInstitution&adaptor=Local%20Search%20Engine&tab=LibraryCatalog'
log=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page();page.set_default_timeout(10000)
 page.goto(u,wait_until='domcontentloaded',timeout=45000);page.wait_for_timeout(6500)
 for i in range(21):
  s=page.locator('body').inner_text();idx=s.find('EGZEMPLARZE W TEJ LOKALIZACJI');part=s[idx:] if idx>=0 else s[-3000:]
  more=page.get_by_role('button',name='Pokaż więcej',exact=True)
  r={'iteration':i,'visible_more':more.count()>0 and more.first.is_visible(),'items':re.findall(r'\b(?:19|20)\d\d\s*-\s*nr[^\n]*',part),'text_length':len(part)}
  log.append(r);print(json.dumps(r,ensure_ascii=False),flush=True)
  (p/'primo_dziennik_egzemplarze_koniec.txt').write_text(part)
  if not r['visible_more'] or i==20:break
  more.first.click();page.wait_for_timeout(1000)
 (p/'primo_dziennik_egzemplarze_paginacja.json').write_text(json.dumps({'url':u,'steps':log,'fully_loaded':not log[-1]['visible_more'],'limit':'Odczyt wykazu egzemplarzy, nie zawartości gazet; brak zamówień.'},ensure_ascii=False,indent=2))
 print('FINAL',part[-4500:],flush=True)
 b.close()
