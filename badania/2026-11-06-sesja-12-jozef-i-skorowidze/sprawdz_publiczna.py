from pathlib import Path
import json,hashlib,datetime
from playwright.sync_api import sync_playwright
root=Path('/workspace/drzewo-genealogiczne')
out=root/'badania/2026-11-06-sesja-12-jozef-i-skorowidze'
url='https://korzenie-marysi.maciekkoz187874.chatgpt.site'
local=(root/'witryna/public/index.html').read_bytes()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(ignore_https_errors=True,viewport={'width':1440,'height':1100})
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 res=page.goto(url,wait_until='networkidle')
 print('HTTP',res.status)
 assert res.status==200 and res.body()==local
 assert page.evaluate('D.people.length')==51 and page.evaluate('D.news.length')==7
 assert page.locator('[data-id="P28"]').count()==1
 page.select_option('#people','P29')
 assert '22.07.1897' in page.locator('#detail').inner_text()
 assert '35 lat' in page.locator('#detail').inner_text()
 assert page.locator('#detail a[href*="c07a9fd88a54463d"]').count()==1
 assert page.locator('#detail a[href*="maps"]').count()>0
 page.locator('#close').click()
 assert page.locator('#lines path[data-kind=parent]').count()==2
 page.set_viewport_size({'width':390,'height':844})
 assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
 assert not errors,errors
 b.close()
meta={"project_id":"appgprj_6aeccd5dcec48191950b70bad04d3017","url":"https://korzenie-marysi.maciekkoz187874.chatgpt.site","access_mode":"public","version_number":16,"version_id":"appgprj_6aeccd5dcec48191950b70bad04d3017~appgver_fbb7c90843d48191bf68493b45aae388","deployment_id":"appgdep_6aedd7f1dc108191b8f29b5b749c237a","status":"succeeded","source_commit_sha":"3159846bfdb8a1faba707559ba50f9f7f22870fd","updated_at":"2026-11-06T13:37:01.135382+00:00"}
meta.update(html_sha256=hashlib.sha256(local).hexdigest(),http_status=200,live_matches_local=True)
for dest in [root/'witryna/publikacja.json',out/'PUBLIKACJA.json']: dest.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),url=url,http_status=200,live_matches_local=True,people=51,news=7,jozef_birth_and_age_verified=True,parent_lines=2,maps_preserved=True,js_errors=errors,mobile_no_overflow=True,chromium_ignore_https_errors=True,network_note='Chromium wymaga pominięcia weryfikacji CA w środowisku wykonawczym. Wcześniejsza próba urllib w tym środowisku zwróciła HTTP403; tej metody nie powtarzano dla wersji16.')
(out/'WALIDACJA_PUBLICZNA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))

