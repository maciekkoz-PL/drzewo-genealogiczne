import json,urllib.request,urllib.parse,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
p=Path('badania/2026-11-07-zarzew/zrodla')
queries=[('witold','Witold Chmielewski','2003-08-22'),('witold_miejscownik','Witoldzie Chmielewskim','2003-08-22'),('czeslaw_miejscownik','Czesławie Chmielewskim','1996-01-01')]
def run(q):
 tag,phrase,date=q
 params={'entityName':'','krs':'','nip':'','textInPosition':'','textInBody':phrase,'signatureType':'A','signatureOfCase':'','signatureKRS':'','court':'','from':date,'to':'2026-11-07','page':'1'}
 u='https://wyszukiwarka-msig.ms.gov.pl/api/Monitor/Search?'+urllib.parse.urlencode(params)
 try:
  r=urllib.request.urlopen(u,timeout=40);d=json.load(r);rows=d.get('list',[])
  # The result list has no identifiers or addresses of unrelated private persons.
  result={'at':datetime.now(timezone.utc).isoformat(),'url':u,'params':params,'data':d}
  (p/('msig_'+tag+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2))
  print(json.dumps({'tag':tag,'list_count':len(rows),'data':d},ensure_ascii=False),flush=True)
 except Exception as e:print(tag,type(e).__name__,str(e),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(run,queries))
