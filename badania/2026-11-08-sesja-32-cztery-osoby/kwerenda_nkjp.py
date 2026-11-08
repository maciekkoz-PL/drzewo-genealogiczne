from pathlib import Path
from urllib.request import build_opener,HTTPCookieProcessor,Request
from urllib.parse import urlencode,urljoin
from http.cookiejar import CookieJar
from lxml import html
import json,time,datetime,hashlib,concurrent.futures
root=Path('badania/2026-11-08-sesja-32-cztery-osoby/zrodla/nkjp_verified');root.mkdir(parents=True,exist_ok=True)
def run(job):
 key,q=job;p=root/key;p.mkdir(exist_ok=True);op=build_opener(HTTPCookieProcessor(CookieJar()));logs=[]
 def fetch(tag,u,data=None):
  rec={'tag':tag,'url':u,'params':data,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  try:
   with op.open(Request(u,data=urlencode(data).encode() if data is not None else None,headers={'User-Agent':'Mozilla/5.0','Referer':'https://nkjp.pl/poliqarp/'}),timeout=30) as r:b=r.read();rec.update(status=r.status,final_url=r.url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
   (p/(tag+'.html')).write_bytes(b);t=html.fromstring(b)
   for x in t.xpath('//script|//style'):x.getparent().remove(x)
   tx='\n'.join(s.strip() for s in t.text_content().splitlines() if s.strip());(p/(tag+'.txt')).write_text(tx)
   return b,t,tx
  except Exception as e:rec['error']=str(e);return b'',None,''
  finally:logs.append(rec);(p/'requests.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
 fetch('start','https://nkjp.pl/poliqarp/')
 fetch('settings','https://nkjp.pl/poliqarp/settings/',{'random_sample_size':'100','show_in_match':'s','show_in_context':'s','left_context_width':'20','right_context_width':'20','wide_context_width':'150','results_per_page':'100','next':''})
 valid=False
 for trial in range(2):
  b,t,tx=fetch('submit'+str(trial),'https://nkjp.pl/poliqarp/query/',{'query':q,'corpus':'nkjp1800'})
  for n in range(10):
   if t is not None:
    value=t.xpath('//input[@name="query"]/@value')
    if value==[q] and 'Results' in tx:valid=True;break
    if value and value!=[q]:print(key,'STALE QUERY REJECTED',repr(value),flush=True);break
   time.sleep(2);b,t,tx=fetch('poll'+str(trial)+'_'+str(n),'https://nkjp.pl/poliqarp/nkjp1800/query/')
  if valid:break
 if not valid:
  (p/'summary.json').write_text(json.dumps({'query':q,'valid':False}));print(key,'INVALID/INCOMPLETE',flush=True);return
 result_text=tx[tx.find('Results'):tx.find('Results')+150];print(key,result_text,flush=True)
 refs=[];lasttext=tx;pages=0
 for pn in range(5):
  pages+=1;refs+=t.xpath('//th/a[@rel]/@href')
  nxt=t.xpath('//a[contains(text(),"Next")]/@href')
  if not nxt:break
  b,t,tx=fetch('page'+str(pn+1),urljoin('https://nkjp.pl',nxt[0]));lasttext=tx
  if t is None or t.xpath('//input[@name="query"]/@value')!=[q]:break
 refs=list(dict.fromkeys(refs));contexts=[]
 for j,ref in enumerate(refs[:300]):
  b,t,tx=fetch('context'+str(j),urljoin('https://nkjp.pl',ref));contexts.append({'ref':ref,'file':'context'+str(j)+'.txt','text':tx})
  if j%25==0:print(key,'contexts',j+1,'of',len(refs),flush=True)
 summary={'query':q,'valid':True,'result_text':result_text,'pages':pages,'refs':len(refs),'contexts':len(contexts),'last_page_text':lasttext,'results':contexts}
 (p/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(key,'DONE',len(refs),len(contexts),flush=True)
queries=[('tomasz','[orth="Tomasz.*"] [orth="Chmielewsk.*"] meta source="Dziennik Łódzki"'),('piotr','[orth="Piotr.*"] [orth="Chmielewsk.*"] meta source="Dziennik Łódzki"'),('witold','[orth="Witold.*"] [orth="Chmielewsk.*"] meta source="Dziennik Łódzki"'),('boguslaw','[orth="Bogusław.*"] [orth="Chmielewsk(i|iego|iemu|im)"] meta source="Dziennik Łódzki"')]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(run,queries))
