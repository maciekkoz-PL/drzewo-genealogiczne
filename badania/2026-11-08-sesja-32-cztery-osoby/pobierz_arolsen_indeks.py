from pathlib import Path
from urllib.request import build_opener,HTTPCookieProcessor,Request
from http.cookiejar import CookieJar
import json,uuid,datetime,hashlib
p=Path('badania/2026-11-08-sesja-32-cztery-osoby/zrodla/arolsen');op=build_opener(HTTPCookieProcessor(CookieJar()));logs=[]
def call(key,method,args):
 u='https://collections-server.arolsen-archives.org/ITS-WS.asmx/'+method;r={'url':u,'params':args,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with op.open(Request(u,data=json.dumps(args).encode(),headers={'Content-Type':'application/json; charset=UTF-8','Referer':'https://collections.arolsen-archives.org/'}),timeout=55) as f:b=f.read();r.update(status=f.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  (p/(key+'_'+method+'.json')).write_bytes(b);d=json.loads(b).get('d');d=json.loads(d) if isinstance(d,str) else d
  print(key,method,'rows',len(d) if isinstance(d,list) else d,flush=True);return d
 except Exception as e:r['error']=str(e);print(key,str(e),flush=True)
 finally:logs.append(r);(p/'requests_pages_complete.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
u=uuid.uuid4().hex[:20];call('pages','BuildQueryGlobalForAngular',{'uniqueId':u,'lang':'en','archiveIds':[],'strSearch':'Chmielewski','synSearch':True});count=call('pages','GetCount',{'uniqueId':u,'lang':'en','searchType':'person','useFilter':False})
allrows=[]
for offset in [0,1000,2000,3000,4000]:
 d=call('complete_offset'+str(offset),'GetPersonList',{'uniqueId':u,'lang':'en','rowNum':offset,'orderBy':'LastName','orderType':'asc'})
 if not isinstance(d,list):continue
 print('OFFSET',offset,'counter',d[0].get('Counter') if d else None,d[-1].get('Counter') if d else None,'first',[(x.get('ObjId'),x.get('LastName'),x.get('FirstName')) for x in d[:2]],flush=True)
 allrows+=d
(p/'all_pages.json').write_text(json.dumps(allrows,ensure_ascii=False,indent=2));print('COMBINED',len(allrows),'COUNT',count,flush=True)
