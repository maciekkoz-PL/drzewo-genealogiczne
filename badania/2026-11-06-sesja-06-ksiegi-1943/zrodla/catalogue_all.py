from pathlib import Path
from playwright.sync_api import sync_playwright
from lxml import html
import json,re,datetime,urllib.parse
p=Path('work/s06/units');p.mkdir(exist_ok=True);allrows=[];logs=[]
with sync_playwright() as play:
 b=play.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(ignore_https_errors=True,viewport={'width':1440,'height':1000})
 page.goto('https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/165812',wait_until='domcontentloaded',timeout=30000)
 page.get_by_role('link',name='Lista jednostek (1076)',exact=True).click(timeout=12000)
 page.wait_for_timeout(1000)
 u=page.locator('a[href*="_Zespol_delta=200"]').first.get_attribute('href')
 for n in range(1,7):
  r=page.goto(u,wait_until='domcontentloaded',timeout=30000);page.wait_for_timeout(1000)
  raw=page.content();(p/f'page{n}.html').write_text(raw);tx=page.locator('body').inner_text();(p/f'page{n}.txt').write_text(tx);t=html.fromstring(raw)
  rows=[]
  for tr in t.xpath('//tr'):
   cells=[' '.join(td.text_content().split()) for td in tr.xpath('./td')]
   if cells and re.match(r'^39/2736/0/',cells[0]):
    links=tr.xpath('.//a/@href');rows.append({'signature':cells[0],'title':cells[1] if len(cells)>1 else '', 'dates':cells[2] if len(cells)>2 else '', 'scans':cells[3] if len(cells)>3 else '', 'url':links[0] if links else None,'all_cells':cells})
  logs.append({'page':n,'url':page.url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':r.status if r else None,'rows':len(rows)})
  allrows+=rows;(p/'units.json').write_text(json.dumps(allrows,ensure_ascii=False,indent=2));(p/'downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2));print('PAGE',n,'rows',len(rows),'TOTAL',len(allrows),flush=True)
  if not rows:break
  if n<6:
   nxt=[a.get('href') for a in t.xpath('//a[@href]') if f'_Zespol_cur={n+1}' in a.get('href','') and '_Zespol_delta=200' in a.get('href','')]
   if not nxt:print('NO NEXT LINK',flush=True);break
   u=urllib.parse.urljoin(page.url,nxt[0])
 b.close()
print('UNIQUE',len({r['signature'] for r in allrows}),flush=True)
