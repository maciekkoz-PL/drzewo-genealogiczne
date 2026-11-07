"""Kontrola zmiany C42/kroniki i zachowania wcześniejszych 70 osób."""
from pathlib import Path
import datetime,json,subprocess
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
d=json.loads((ROOT/'witryna/wiarygodnosc.json').read_text())
old=json.loads(subprocess.check_output(['git','show','396e28e:witryna/wiarygodnosc.json'],cwd=ROOT))
assert d['edges']==old['edges'] and d['relations']==old['relations']
assert len(d['people'])==70 and len(d['news'])==10
for a,b in zip(old['people'],d['people']):
    if a['id']!='C42':assert a==b,a['id']
    else:
        assert {k:v for k,v in a.items() if k not in ['note','source']}=={k:v for k,v in b.items() if k not in ['note','source']}
        assert b['note'].startswith(a['note']) and b['source']==a['source']+['S284']
assert d['news'][1:]==old['news'][1:]
errors=[]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    for width in [1440,390]:
        page=browser.new_page(viewport={'width':width,'height':1000})
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.set_content((ROOT/'witryna/public/index.html').read_text())
        for branch in ['both','maternal','paternal']:
            page.select_option('#branch',branch);prior=set()
            for level in [1,2,3]:
                page.locator(f'#evidence [data-level="{level}"]').click()
                ids=set(page.locator('.node').evaluate_all('(ns)=>ns.map(n=>n.dataset.id)'))
                assert prior<=ids and 'P01' in ids;prior=ids
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
        page.select_option('#people','C42')
        text=page.locator('#detail').inner_text()
        assert 'Agnieszka' in text and '2246' in text and 'Poprawskich' in text
        assert '1947' in text and '29.09.1939' in text and 'Miszczyszyn' in d['news'][0]['body']
        assert page.locator('#detail a[href*="eab68475"]').count()==1
        page.locator('#close').click()
        assert page.evaluate('D.news.length')==10
        page.close()
    browser.close()
assert not errors,errors
r=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),widths=[1440,390],
    old_people_and_relations_preserved=True,C42_uncertainty_preserved=True,existing_news_updated=True,new_persons_or_edges=False,javascript_errors=errors)
(HERE/'WALIDACJA_STRONY.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(r)
