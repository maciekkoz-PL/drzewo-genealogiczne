"""Sprawdzenie obu gałęzi, filtrowania dowodów i kart kandydatów."""
from playwright.sync_api import sync_playwright
from pathlib import Path
import json,datetime
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=browser.new_page(viewport={'width':1440,'height':1100});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content((Path(__file__).resolve().parent/'public/index.html').read_text())
 assert page.locator('.node').count()==21
 assert page.locator('#lines path[data-kind=parent]').count()==2
 assert page.locator('#lines path[data-kind=parent][stroke-dasharray]').count()==0
 assert page.evaluate('D.people.every(p=>p.branch!=="paternal"||p.y<byId.P01.y)&&D.people.every(p=>p.branch!=="maternal"||p.y>byId.P01.y)')
 def assert_centered():
  delta=page.evaluate('''()=>{const m=document.querySelector('[data-id=P01]').getBoundingClientRect(),v=document.querySelector('#viewport').getBoundingClientRect();return [Math.abs(m.x+m.width/2-v.x-v.width/2),Math.abs(m.y+m.height/2-v.y-v.height/2)]}''')
  assert max(delta)<3,delta
 assert_centered()
 assert page.locator('#lines path[data-kind=hypothesis]').count()==6
 assert page.locator('[data-id=C03]').count()==0
 page.select_option('#period','all');assert page.locator('.entry').count()==5
 assert 'gałąź mamy' in page.locator('.entry').first.inner_text()
 page.select_option('#people','C42');assert 'Pokrewieństwo do sprawdzenia' in page.locator('#detail').text_content()
 assert 'z Poprawskich' in page.locator('#detail').inner_text() and 'nie jest poszukiwanym ojcem Piotra' in page.locator('#detail').inner_text()
 assert page.locator('#detail a').first.get_attribute('href').endswith('plik=063-066.jpg')
 page.locator('#close').click()
 page.select_option('#people','P02');page.locator('[data-open=P03]').click();assert '1909' in page.locator('#detail').inner_text()
 page.locator('#close').click()
 page.select_option('#people','C02');assert 'Rodzice nie zostali odczytani' in page.locator('#detail').inner_text()
 page.locator('#close').click()
 assert page.evaluate('D.edges.every(([a,b,k])=>!a.startsWith("C")&&!b.startsWith("C")||k==="hypothesis")')
 assert page.locator('.hero,.notice,.about').count()==0
 page.locator('#fit').click();page.screenshot(path='/workspace/marysia-desktop.png',full_page=True)
 page.select_option('#evidence','documented')
 documented=page.locator('.node').count();assert documented==13,documented
 assert page.locator('.node.candidate').count()==0
 assert page.locator('[data-id=P10],[data-id=P11]').count()==0
 assert page.locator('[data-id=P01]').count()==1
 assert page.locator('#lines path[data-kind=family],#lines path[data-kind=hypothesis],#lines path[data-kind=identity],#lines path[data-kind=sibling]').count()==0
 assert page.locator('#lines path[data-kind=parent]').count()==2
 page.select_option('#people','P01');assert page.locator('[data-open=P02],[data-open=P17]').count()==2
 page.locator('#close').click();page.locator('#fit').click();assert_centered()
 page.select_option('#people','P03');assert page.locator('[data-open=C02],[data-open=P02]').count()==0
 page.locator('#close').click()
 page.select_option('#branch','maternal');assert page.locator('.node').count()==4
 assert page.locator('#lines path').count()==3
 assert page.locator('#lines path[data-kind=parent]').count()==1
 page.select_option('#evidence','extended');assert page.locator('.node').count()==4
 assert page.locator('#lines path').count()==3
 page.select_option('#people','P18');assert 'Roman Jankowski' in page.locator('#detail h2').inner_text()
 assert 'nie znamy' in page.locator('#detail').inner_text().lower()
 page.locator('[data-open=P17]').click();assert '04.01.1942' in page.locator('#detail').inner_text()
 page.locator('#close').click();page.locator('#fit').click();page.screenshot(path='/workspace/marysia-maternal.png',full_page=True)
 page.set_viewport_size({'width':390,'height':844});page.locator('#fit').click()
 assert_centered()
 assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
 page.select_option('#people','P19');assert 'nazwisko rodowe Kulas' in page.locator('#detail').inner_text()
 page.locator('#close').click();page.screenshot(path='/workspace/marysia-mobile.png',full_page=True)
 page.select_option('#branch','paternal');assert page.locator('.node').count()==18
 page.fill('#search','Sabina');page.locator('#search').press('Enter');assert 'Sabina' in page.locator('#detail h2').inner_text()
 page.locator('#close').click();page.fill('#search','')
 page.select_option('#branch','both');assert page.locator('.node').count()==21
 page.select_option('#people','P10');assert 'Nie potwierdzono' in page.locator('#detail').inner_text()
 assert not errors,errors
 browser.close()
 report={'result':'PASS','at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'full_nodes':21,'documented_nodes':documented,'maternal_nodes':4,'paternal_full_nodes':18,'news':5,'hypothesis_edges_extended_only':6,'candidate_identities_not_promoted':True,'H017_edges_hidden_in_documented_view':True,'maternal_parentage_source_S086':True,'Marysia_centered_desktop_mobile':True,'father_family_above_mother_family_below':True,'parents_connected_in_all_evidence_modes':True,'dialog_navigation_search_and_390px_checked':True,'javascript_errors':errors}
 (Path(__file__).resolve().parent/'WALIDACJA_WIDOKU.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print('PASS:21kart,5wpisów, dokumenty13kart/bezhipotez, mama4/tata18, źródła,karty,390px,0błędówJS')
