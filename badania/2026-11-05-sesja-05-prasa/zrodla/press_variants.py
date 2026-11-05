from pathlib import Path
import urllib.request,urllib.parse,json,hashlib,datetime
from lxml import html
p=Path('work/h017-s04/variants');p.mkdir(exist_ok=True);logs=[]
for key,q in [('mother_declined','"Janiny Chmielewskiej"'),('father_declined','"Czesława Chmielewskiego"'),('father_reverse','"Chmielewski Czesław"'),('child_full','"Bogusław Kazimierz"')]:
 u='https://bc.wbp.lodz.pl/dlibra/results?'+urllib.parse.urlencode({'q':q,'action':'SimpleSearchAction','type':'-6','p':'0'})
 row={'key':key,'url':u,'query':q,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(u,timeout=30) as r:b=r.read();row.update(status=r.status,size=len(b),final_url=r.url,sha256=hashlib.sha256(b).hexdigest())
  (p/(key+'.html')).write_bytes(b);t=html.fromstring(b)
  row['results']=[{'title':' '.join(a.text_content().split()),'url':a.get('href')} for a in t.xpath('//a[@href]') if '/edition/' in a.get('href','') and a.get('href','').rsplit('/',1)[-1].isdigit() and a.text_content().strip()]
  for x in t.xpath('//script|//style'):x.drop_tree()
  (p/(key+'.txt')).write_text(' '.join(t.text_content().split()))
  print(key,json.dumps(row['results'],ensure_ascii=False),flush=True)
 except Exception as e:row['error']=str(e);print(key,str(e),flush=True)
 logs.append(row);(p/'downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
