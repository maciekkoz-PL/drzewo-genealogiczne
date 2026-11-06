from pathlib import Path
import datetime,hashlib,json,sys
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
live='--live' in sys.argv;html=ROOT/'witryna/public/index.html';local=html.read_bytes()
url='https://korzenie-marysi.maciekkoz187874.chatgpt.site' if live else html.as_uri()
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=browser.new_page(ignore_https_errors=live,viewport={'width':1440,'height':1100})
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 if live:
  response=page.goto(url,wait_until='networkidle');assert response.status==200 and response.body()==local
 else:page.set_content(local.decode(),wait_until='networkidle')
 assert page.evaluate('D.people.length')==55 and page.evaluate('D.edges.length')==79 and page.evaluate('D.news.length')==8
 counts=[]
 for level,persons,edges in [(1,17,27),(2,28,41),(3,55,79)]:
  page.locator(f'#evidence [data-level="{level}"]').click()
  assert page.locator('.node').count()==persons,(level,page.locator('.node').count())
  assert page.locator('#lines path').count()==edges,(level,page.locator('#lines path').count())
  assert page.locator('#lines path[data-kind=parent]').count()==2
  assert page.locator('.node[data-id="C69"]').count()==(1 if level==3 else 0)
  counts.append(dict(level=level,people=persons,edges=edges))
 assert page.locator('#lines path[data-kind=identity_candidate]').count()>=1
 for ident in ['C69','C70','C71','C72']:
  page.select_option('#people',ident);text=page.locator('#detail').inner_text()
  assert 'H035' in text or 'hipotezy' in text.lower() or 'hipotezą' in text.lower() or 'wymaga dowodu' in text
  assert page.locator('#detail a[href*="arolsen"],#detail a[href*="naa.gov.au"]').count()>0
  if ident in ['C71','C72']:assert 'Nie ustalono, czy obecnie żyje.' in text
  page.locator('#close').click()
 # Nowe karty nie nakładają się na żadne istniejące karty.
 overlaps=page.evaluate('''()=>{const nodes=[...document.querySelectorAll('.node')];return nodes.filter(n=>['C69','C70','C71','C72'].includes(n.dataset.id)).flatMap(a=>nodes.filter(b=>b!==a).filter(b=>{const x=a.getBoundingClientRect(),y=b.getBoundingClientRect();return x.left<y.right&&x.right>y.left&&x.top<y.bottom&&x.bottom>y.top}).map(b=>[a.dataset.id,b.dataset.id]))}''')
 assert not overlaps,overlaps
 page.select_option('#people','P31');assert page.locator('#detail a[href*="maps"]').count()>0;page.locator('#close').click()
 page.select_option('#branch','maternal');assert page.locator('#lines path[data-kind=parent]').count()>=1 and page.locator('.node[data-id="C69"]').count()==0
 page.select_option('#branch','both');page.set_viewport_size({'width':390,'height':844})
 assert page.evaluate('document.documentElement.scrollWidth<=innerWidth') and not errors,errors
 browser.close()
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),url=url,html_sha256=hashlib.sha256(local).hexdigest(),people=55,edges=79,news=8,levels=counts,P12_C69_separate=True,current_life_uncertainty_visible=True,source_links_present=True,new_cards_no_overlap=True,parent_lines=2,maps_and_maternal_branch_preserved=True,mobile_no_overflow=True,js_errors=errors)
if live:report.update(http_status=200,live_matches_local=True,chromium_ignore_https_errors=True,network_note='Chromium wymaga pominięcia weryfikacji CA w środowisku; test treści i interakcji nie jest audytem certyfikatu.')
else:report.update(local_html_injected=True,network_note='Lokalny HTML załadowano przez set_content; file:// blokowane przez politykę środowiska.')
(HERE/('WALIDACJA_PUBLICZNA.json' if live else 'WALIDACJA_UI.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
