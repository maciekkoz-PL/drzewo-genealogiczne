from pathlib import Path
import json,hashlib,datetime
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
url='https://korzenie-marysi.maciekkoz187874.chatgpt.site'
local=(ROOT/'witryna/public/index.html').read_bytes()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(ignore_https_errors=True,viewport={'width':1440,'height':1100});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 r=page.goto(url,wait_until='networkidle')
 assert r.status==200 and r.body()==local
 assert page.evaluate('D.people.length')==51 and page.evaluate('D.news.length')==7
 assert page.evaluate('D.people.find(p=>p.id==="P31").source.includes("REL-014")')
 page.select_option('#people','P31');t=page.locator('#detail').inner_text();assert 'sprzed 2000 r.' in t and 'hipotezy' in t and 'Roman' in t
 assert page.locator('#detail a[href*="maps"]').count()>0
 page.locator('#close').click()
 assert page.locator('#lines path[data-kind=parent]').count()==2
 assert page.locator('#lines path[data-kind=hypothesis_marriage]').count()==0
 page.locator('#evidence [data-level="3"]').click();assert page.locator('#lines path[data-kind=hypothesis_marriage]').count()==1
 page.select_option('#people','P32');assert 'Nie znamy jego imienia' in page.locator('#detail').inner_text();page.locator('#close').click()
 page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
 assert not errors,errors;b.close()
meta={"project_id":"appgprj_6aeccd5dcec48191950b70bad04d3017","url":"https://korzenie-marysi.maciekkoz187874.chatgpt.site","access_mode":"public","version_number":17,"version_id":"appgprj_6aeccd5dcec48191950b70bad04d3017~appgver_864f14c4047881918543fd43b4b645a4","deployment_id":"appgdep_6aedde7640588191a1975a30f116d86f","status":"succeeded","source_commit_sha":"74aecbc9ecb0d950ad0f3ec2cf76c65fdb774c0b","updated_at":"2026-11-06T14:04:51.041615+00:00"}
meta.update(html_sha256=hashlib.sha256(local).hexdigest(),http_status=200,live_matches_local=True)
for file in [HERE/'PUBLIKACJA.json',ROOT/'witryna/publikacja.json']:file.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),url=url,http_status=200,live_matches_local=True,people=51,news=7,Czesia_report_updated=True,son_not_assigned_to_Roman=True,hypothesis_only_on_level3=True,parent_lines=2,maps_preserved=True,js_errors=errors,mobile_no_overflow=True,chromium_ignore_https_errors=True,network_note='Chromium w środowisku wykonawczym wymaga pominięcia weryfikacji CA; sprawdzenie treści i interakcji nie stanowi niezależnego audytu certyfikatu.')
(HERE/'WALIDACJA_PUBLICZNA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))

