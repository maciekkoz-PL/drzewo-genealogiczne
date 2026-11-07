from pathlib import Path
from datetime import datetime,timezone
import json,urllib.request,urllib.parse,concurrent.futures
p=Path('badania/2026-11-07-tomasz-dalsze/zrodla');p.mkdir(parents=True,exist_ok=True)
base={'entityName':'','krs':'','nip':'','textInPosition':'','textInBody':'','signatureType':'A','signatureOfCase':'','signatureKRS':'','court':'','from':'2001-04-26','to':'2026-11-07','page':'1'}
qs=['Tomasza Chmielewskiego','Chmielewskim 2001','Chmielewski 26.04.2001','Chmielewski 26 kwietnia 2001','Chmielewski 1971','Chmielewski 1970']
def run(job):
 i,q=job;params={**base,'textInBody':q};u='https://wyszukiwarka-msig.ms.gov.pl/api/Monitor/Search?'+urllib.parse.urlencode(params)
 d={'query':q,'url':u,'params':params,'at':datetime.now(timezone.utc).isoformat()}
 try:
  r=urllib.request.urlopen(u,timeout=35);data=json.load(r);d.update(status=r.status,data=data)
  print(i,q,'rows',len(data.get('list',[])),json.dumps(data.get('list',[])[:12],ensure_ascii=False)[:5500],flush=True)
 except Exception as e:d['error']=str(e);print(i,type(e).__name__,str(e),flush=True)
 (p/('msig_'+str(i)+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));return d
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(run,enumerate(qs)))
