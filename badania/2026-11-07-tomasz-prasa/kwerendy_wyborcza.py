import urllib.request,urllib.parse,http.cookiejar,json,concurrent.futures
from pathlib import Path
from lxml import html
from datetime import datetime,timezone
p=Path('badania/2026-11-07-tomasz-prasa/zrodla')
jobs=[('nazwisko_kontrola',{'query':'Chmielewski'}),('tomasza_tresc',{'query':'Tomasza Chmielewskiego','textSearch':'true'}),('nazwisko_2001',{'query':'Chmielewski','startDay':'26','startMonth':'3','startYear':'2001','endDay':'31','endMonth':'11','endYear':'2001'})]
def run(job):
 tag,extra=job; data={'page':'1','pageStep':'0','_textSearch':'on','city':'','gazetaAreaCode':'','startDay':'','startMonth':'','startYear':'','endDay':'','endMonth':'','endYear':'','pageSize':'100','AnnouncementSearch.LEFT-01.search':'szukaj »',**extra}
 op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
 r=op.open(urllib.request.Request('https://nekrologi.wyborcza.pl/0,10.html',data=urllib.parse.urlencode(data).encode(),headers={'User-Agent':'Mozilla/5.0'}),timeout=55)
 b=r.read();(p/('wyborcza_'+tag+'.html')).write_bytes(b)
 t=html.fromstring(b)
 links=[{'text':' '.join(a.text_content().split()),'url':urllib.parse.urljoin(r.url,a.get('href'))} for a in t.xpath('//a[@href]') if ',11,,' in a.get('href','') or ',11,' in a.get('href','')]
 for x in t.xpath('//script|//style'):x.drop_tree()
 text=t.text_content();(p/('wyborcza_'+tag+'.txt')).write_text(text)
 lines=[s.strip() for s in text.splitlines() if any(x in s for x in ['znalezion','Chmielew','Tomasz','2001','archiw'])]
 d={'tag':tag,'params':data,'url':r.url,'at':datetime.now(timezone.utc).isoformat(),'lines':lines,'links':links};print(json.dumps(d,ensure_ascii=False),flush=True);return d
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:results=list(ex.map(run,jobs))
(p/'wyborcza_variants.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
