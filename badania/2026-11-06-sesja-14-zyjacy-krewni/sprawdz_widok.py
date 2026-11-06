from pathlib import Path
import datetime,hashlib,json,sys
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
live='--live' in sys.argv
html=ROOT/'witryna/public/index.html'
url='https://korzenie-marysi.maciekkoz187874.chatgpt.site' if live else html.as_uri()
local=html.read_bytes()
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    page=browser.new_page(ignore_https_errors=live,viewport={'width':1440,'height':1100})
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    if live:
        response=page.goto(url,wait_until='networkidle')
        assert response.status==200 and response.body()==local
    else:
        page.set_content(local.decode(),wait_until='networkidle')
    assert page.evaluate('D.people.length')==51 and page.evaluate('D.edges.length')==75 and page.evaluate('D.news.length')==7
    assert page.locator('#lines path[data-kind=parent]').count()==2
    assert page.locator('#lines path[data-kind=hypothesis_marriage]').count()==0
    page.select_option('#people','P09');text=page.locator('#detail').inner_text()
    assert 'żony ani dzieci' in text and 'pewności' in text;page.locator('#close').click()
    page.select_option('#people','P10');text=page.locator('#detail').inner_text()
    assert 'głównym tropem' in text and 'nie potwierdzono' in text
    assert page.evaluate('D.people.find(p=>p.id==="P10").source.includes("REL-016")')
    page.locator('#close').click()
    page.locator('#evidence [data-level="3"]').click()
    page.select_option('#people','C19');text=page.locator('#detail').inner_text()
    assert 'głównym tropem' in text.lower() and 'niepotwierdzone' in text and 'rodziców' in text
    assert page.locator('#detail a[href*="wiadomosci.wp.pl"]').count()==1
    page.locator('#close').click()
    assert page.locator('#lines path[data-kind=hypothesis_marriage]').count()==1
    page.select_option('#people','P31');assert page.locator('#detail a[href*="maps"]').count()>0;page.locator('#close').click()
    page.select_option('#people','P32');assert 'Nie znamy jego imienia' in page.locator('#detail').inner_text();page.locator('#close').click()
    page.select_option('#branch','maternal');assert page.locator('#lines path[data-kind=parent]').count()>=1
    page.select_option('#branch','both')
    page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    assert not errors,errors
    browser.close()
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),url=url,html_sha256=hashlib.sha256(local).hexdigest(),people=51,edges=75,news=7,Piotr_main_candidate_not_confirmed=True,Tomasz_uncertainty_visible=True,P10_C19_separate=True,parent_lines=2,maps_and_maternal_branch_preserved=True,mobile_no_overflow=True,js_errors=errors)
if live:report.update(http_status=200,live_matches_local=True,chromium_ignore_https_errors=True,network_note='Chromium wymaga pominięcia weryfikacji CA w środowisku wykonawczym; test treści i interakcji nie jest niezależnym audytem certyfikatu.')
else:report.update(local_html_injected=True,network_note='Polityka Chromium blokuje file://; lokalny HTML załadowano przez set_content, bez zmiany strony.')
(HERE/('WALIDACJA_PUBLICZNA.json' if live else 'WALIDACJA_UI.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
