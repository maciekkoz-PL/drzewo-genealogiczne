"""Regression of actual UI in Chromium for the three cumulative evidence levels."""
from pathlib import Path
import json,datetime
from playwright.sync_api import sync_playwright
HERE=Path(__file__).resolve().parent
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 for width,height in [(1440,1100),(390,844)]:
  page.close();page=b.new_page(viewport=dict(width=width,height=height));page.on('pageerror',lambda e:errors.append(str(e)));page.set_content((HERE/'public/index.html').read_text())
  assert page.locator('#evidence [data-level="2"]').get_attribute('aria-pressed')=='true'
  for branch in ['both','maternal','paternal']:
   page.select_option('#branch',branch);prior=set()
   for level in [1,2,3]:
    page.locator(f'#evidence [data-level="{level}"]').click()
    ids=set(page.locator('.node').evaluate_all('(ns)=>ns.map(n=>n.dataset.id)'))
    assert prior<=ids;prior=ids;assert 'P01' in ids,(width,branch,level,ids,errors)
    expected=page.evaluate('([l,branch])=>D.people.filter(p=>p.level<=l&&(branch==="both"||p.branch==="both"||p.branch===branch)).length',[level,branch])
    assert len(ids)==expected,(width,branch,level,len(ids),expected)
    if branch in ['both','paternal']:
     assert {'P26','P27'}<=ids and not {'C02','C04'}&ids,(width,branch,level,ids)
     for id,sid in [('P26','S147'),('P27','S148')]:
      page.select_option('#people',id)
      detail=page.locator('#detail').inner_text()
      assert 'Wincent' in detail and 'Agniesz' in detail and sid in page.evaluate('(id)=>D.people.find(p=>p.id===id).source',id)
      page.locator('#close').click()
    if branch in ['both','paternal'] and level==1:
     assert {'P03','P04','P05','P06','P07','P08','P12'}<=ids
     assert page.locator('#lines path[data-kind=identity]').count()==2
    assert page.locator('#lines path[data-kind=parent]').count()==(2 if branch=='both' else 1)
    for line in page.locator('#lines path').all():
     lev=int(line.get_attribute('data-level'));assert lev<=level or (line.get_attribute('data-kind')=='identity' and level==1)
     assert line.get_attribute('stroke-dasharray')=={1:None,2:'6 5',3:'2 6'}[lev]
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(width,branch,level)
    page.select_option('#people','P01');assert 'wyjątek rodzinny' in page.locator('#detail').inner_text();page.locator('#close').click()
  page.select_option('#branch','maternal');page.locator('#evidence [data-level="3"]').click()
  for id in ['C46','C47','C48','C49','C45','C56','C57']:
   page.select_option('#people',id);assert 'Potrzebny dowód' in page.locator('#detail').inner_text();page.locator('#close').click()
  assert page.locator('[data-id=P19]').count()==1 and page.locator('[data-id=C45]').count()==1
 assert not errors,errors
 assert page.evaluate('D.news.length')==7
 assert page.evaluate('D.people.length')==51
 assert page.evaluate('D.relations.length')==75
 assert page.evaluate('D.people.some(p=>p.id==="P30")&&!D.people.some(p=>p.id==="C05")')
 assert page.evaluate('D.relations.find(r=>r.id==="V066").level')==3
 assert page.evaluate('D.relations.find(r=>r.id==="R041").a')=='P31'
 assert not page.evaluate('D.relations.some(r=>r.a==="P12"&&r.b==="P32")')
 assert page.evaluate('D.relations.filter(r=>["R030","R031","R032","R033","R034","R035"].includes(r.id)).every(r=>r.level===1)')
 b.close()
report={'result':'PASS','at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'widths':[1440,390],'all_levels_and_both_branches':True,'cumulative':True,'parent_exception_preserved':True,'line_styles_checked':True,'sources_and_dialogs_checked':True,'javascript_errors':errors}
(HERE/'WALIDACJA_TRZECH_POZIOMOW.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(report)
