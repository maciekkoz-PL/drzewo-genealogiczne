from pathlib import Path
import json,urllib.request,http.cookiejar,datetime,hashlib
p=Path('work/s07/geneteka'); records=json.loads((p/'relatives_queries.json').read_text()); attempts=[]
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
ui='https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=05ld&bdm=D&rid=D'
with op.open(ui,timeout=30) as z:z.read()
for r in records:
 if not r.get('error'):continue
 a={'key':r['key'],'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'previous_error':r['error']}
 try:
  req=urllib.request.Request(r['url'],headers={'User-Agent':'Mozilla/5.0','Referer':ui,'X-Requested-With':'XMLHttpRequest'})
  with op.open(req,timeout=40) as z:b=z.read();a['status']=z.status
  f=p/(r['key']+'.json');f.write_bytes(b);d=json.loads(b)
  a.update(sha256=hashlib.sha256(b).hexdigest(),total=d.get('recordsTotal'),rows=len(d.get('data',[])),path=str(f));a['complete']=a['total']==a['rows']
  print(r['key'],a['total'],d.get('data'),flush=True)
 except Exception as e:a['error']=str(e);print(r['key'],a['error'],flush=True)
 attempts.append(a);(p/'retries.json').write_text(json.dumps(attempts,ensure_ascii=False,indent=2))
