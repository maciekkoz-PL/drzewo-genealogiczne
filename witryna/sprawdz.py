from playwright.sync_api import sync_playwright
from pathlib import Path
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=browser.new_page(viewport={'width':1440,'height':1100});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content((Path(__file__).resolve().parent/'public/index.html').read_text())
 page.locator('[data-id=P02]').click();assert page.locator('dialog').is_visible();assert 'Poprawk' in page.locator('#detail').inner_text()
 page.locator('[data-open=P03]').click();assert '1909' in page.locator('#detail').inner_text()
 page.locator('#close').click();page.locator('#fit').click();assert page.locator('.node').count()==13
 page.select_option('#period','all');assert page.locator('.entry').count()==7
 page.screenshot(path='/workspace/marysia-desktop.png',full_page=True)
 page.set_viewport_size({'width':390,'height':844});page.select_option('#people','P01');assert page.locator('dialog').is_visible()
 page.locator('#close').click();assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
 page.screenshot(path='/workspace/marysia-mobile.png',full_page=True);assert not errors,errors
 text=page.locator('#family-data').text_content()
 for private in ['Jankowska','04.01.1942','Piotr','policjant','1984','51.67956']:assert private not in text,private
 browser.close();print('PASS: 13 kart, dialogi i powiązania, kronika7wpisów, mobile390px, brak błędówJS, brak prywatnych pól')
