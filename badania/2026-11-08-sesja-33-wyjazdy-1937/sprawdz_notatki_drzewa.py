"""Sprawdzenie, że nowe odpowiedzi nie zmieniają tożsamości i pokrewieństwa."""
from pathlib import Path
import json,datetime
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[2];D=Path(__file__).resolve().parent
old=json.loads((R/'work/s33_site_curated_before.json').read_text());new=json.loads((R/'witryna/wiarygodnosc.json').read_text())
assert old['edges']==new['edges']and old['relations']==new['relations']
assert old.get('news')==new.get('news')
by={x['id']:x for x in new['people']};before={x['id']:x for x in old['people']}
assert set(by)==set(before)and len(by)==70
assert by['P31']['dates']==before['P31']['dates']
assert by['C10']['dates']=='zm. 16.01.1981'and'1982'not in by['C10']['dates']
for id in by:
    if id not in ['P31','C10']:assert by[id]==before[id],id
with sync_playwright()as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    errors=[]
    for width,height in [(1440,1100),(390,844)]:
        page=browser.new_page(viewport={'width':width,'height':height});page.on('pageerror',lambda e:errors.append(str(e)))
        page.set_content((R/'witryna/public/index.html').read_text())
        assert page.locator('#evidence [data-level="2"]').get_attribute('aria-pressed')=='true'
        for level in [1,2,3]:
            page.locator(f'#evidence [data-level="{level}"]').click()
            ids=set(page.locator('.node').evaluate_all('(ns)=>ns.map(n=>n.dataset.id)'))
            expected={x['id']for x in new['people']if x['level']<=level}
            assert ids==expected,(width,level)
            assert page.locator('#lines path[data-kind=parent]').count()==2
        page.select_option('#people','P31');text=page.locator('#detail').inner_text()
        assert '20.11.1922'in text and 'osobnej kandydatki C62'in text and 'te daty nie są przypisane'in text
        assert page.locator('#detail a[href*="odpowiedzi_instytucji_wypisy.json"]').count()>=1
        page.locator('#close').click();page.select_option('#people','C10');text=page.locator('#detail').inner_text()
        assert 'sprzeczną'in text and 'Daty nie przyjęto'in text
        page.locator('#close').click()
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
        assert page.evaluate('D.news.length')==10
        page.close()
    browser.close();assert not errors,errors
out=dict(passed=True,at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),widths=[1440,390],people=70,news=10,relations_unchanged=True,all_other_people_unchanged=True,p31_dates_not_replaced_by_candidate=True,c10_invalid_birth_date_not_accepted=True,source_links_in_dialogs=True,javascript_errors=errors)
(D/'WALIDACJA_DRZEWA.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
