from pathlib import Path
import datetime,hashlib,json,sys
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
live='--live' in sys.argv;html=ROOT/'witryna/public/index.html';local=html.read_bytes();url='https://korzenie-marysi.maciekkoz187874.chatgpt.site' if live else html.as_uri()
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=browser.new_page(ignore_https_errors=live,viewport={'width':1440,'height':1100});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 if live:
  response=page.goto(url,wait_until='networkidle');assert response.status==200 and response.body()==local
 else:
  page.route('https://marysia-local.invalid/assets/**',lambda r:r.fulfill(path=str(ROOT/'witryna/public/assets'/r.request.url.rsplit('/',1)[1])))
  page.set_content(local.decode().replace('<head>','<head><base href="https://marysia-local.invalid/">',1),wait_until='networkidle')
 assert page.evaluate('D.people.length')==71 and page.evaluate('D.edges.length')==96 and page.evaluate('D.news.length')==9
 counts=[]
 for level,persons,edges in [(1,17,27),(2,28,41),(3,71,96)]:
  page.locator(f'#evidence [data-level="{level}"]').click();assert page.locator('.node').count()==persons
  assert page.locator('#lines path').count()==edges and page.locator('#lines path[data-kind=parent]').count()==2
  assert page.locator('.node[data-id="C79"]').count()==(1 if level==3 else 0);counts.append(dict(level=level,people=persons,edges=edges))
 page.wait_for_function('document.querySelector(\'.node[data-id="C69"] img\')?.naturalWidth>0')
 page.select_option('#people','C69');assert page.locator('#detail .person-photo img').count()==1 and page.locator('#detail a[href*="maps"]').count()>0;page.locator('#close').click()
 page.select_option('#people','C71');assert page.locator('#detail a[href*="maps"]').count()>0;page.locator('#close').click()
 for ident in ['C75','C79','C81','C82','C84','C86','C88','C94']:
  page.select_option('#people',ident);s=page.locator('#detail').inner_text()
  assert page.locator('#detail a[href*="mytributes"],#detail a[href*="dailytelegraph"],#detail a[href*="gct.net.au"]').count()>0
  if ident in ['C82','C84','C86']:assert 'kto w tej parze' in s and 'Obecny stan życia nieustalony' in s
  if ident in ['C88','C94']:assert 'nie podaje' in s and 'Obecny stan życia nieustalony' in s
  if ident=='C79':assert 'Michelle/Chris' in s and 'Rebecca' in s and 'niepotwierdzone' in s
  if ident=='C79':
   assert page.locator('#detail .related button[data-open="C82"]').inner_text().startswith('dziecko lub partner dziecka:')
   assert page.locator('#detail .related button[data-open="C88"]').inner_text().startswith('wnuk lub wnuczka:')
   assert page.locator('#detail .related button[data-open="C81"]').inner_text().startswith('żona')
  if ident=='C75':assert '27.11.2024' in s and 'osobno' in s
  page.locator('#close').click()
 overlaps=page.evaluate('''()=>{const ns=[...document.querySelectorAll('.node')];return ns.filter(n=>n.dataset.id==='C75'||(+n.dataset.id.slice(1)>=79&&n.dataset.id.startsWith('C'))).flatMap(a=>ns.filter(b=>b!==a).filter(b=>{const x=a.getBoundingClientRect(),y=b.getBoundingClientRect();return x.left<y.right&&x.right>y.left&&x.top<y.bottom&&x.bottom>y.top}).map(b=>[a.dataset.id,b.dataset.id]))}''');assert not overlaps,overlaps
 for a,b in [('C71','C79'),('C72','C75')]:assert page.locator(f'#lines path[data-from="{a}"][data-to="{b}"][data-kind=identity_candidate]').count()==1
 for i in range(82,95):assert page.locator(f'#lines path[data-from="C79"][data-to="C{i}"][data-kind=family]').count()==1
 page.select_option('#people','P31');assert page.locator('#detail a[href*="maps"]').count()>0;page.locator('#close').click()
 page.select_option('#branch','maternal');assert page.locator('#lines path[data-kind=parent]').count()>=1 and page.locator('.node[data-id="C79"]').count()==0
 page.select_option('#branch','both');page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth') and not errors,errors
 browser.close()
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),url=url,html_sha256=hashlib.sha256(local).hexdigest(),people=71,edges=96,news=9,levels=counts,separate_identifications_visible=True,generic_family_links_for_uncertain_roles=True,relationship_labels_do_not_invent_biological_roles=True,current_life_uncertainty_visible=True,source_links_present=True,new_cards_no_overlap=True,parent_lines=2,maps_and_maternal_branch_preserved=True,roman_portrait_loaded=True,remote_v20_features_preserved=True,mobile_no_overflow=True,js_errors=errors)
if live:report.update(http_status=200,live_matches_local=True,chromium_ignore_https_errors=True,network_note='Chromium wymaga pominięcia weryfikacji CA w środowisku; test treści i interakcji nie jest audytem certyfikatu.')
else:report.update(local_html_injected=True,network_note='HTML wczytano przez set_content; lokalny obraz podano przez kontrolowaną trasę Playwright. file:// jest blokowane w środowisku.')
(HERE/('WALIDACJA_PUBLICZNA.json' if live else 'WALIDACJA_UI.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
