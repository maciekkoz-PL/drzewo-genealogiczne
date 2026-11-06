from pathlib import Path
import urllib.request,http.cookiejar,json,datetime,hashlib,uuid
OUT=Path('work/s16/arolsen');OUT.mkdir(exist_ok=True)
logs=[];opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
def call(key,method,args):
    u='https://collections-server.arolsen-archives.org/ITS-WS.asmx/'+method
    log=dict(url=u,method='POST public index',params=args,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        req=urllib.request.Request(u,data=json.dumps(args).encode(),headers={'Content-Type':'application/json; charset=UTF-8','Referer':'https://collections.arolsen-archives.org/'})
        r=opener.open(req,timeout=30);raw=r.read();p=OUT/(key+'_'+method+'.json');p.write_bytes(raw);log.update(status=r.status,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),path=str(p))
        d=json.loads(raw).get('d')
        if isinstance(d,str):
            try:d=json.loads(d)
            except ValueError:pass
        print(key,method,'rows='+str(len(d)) if isinstance(d,list) else str(d)[:600],flush=True)
        return d
    except Exception as e:log['error']=str(e);print(key,e,flush=True)
    finally:logs.append(log);(OUT/'downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2)+'\n')
def query(key,q):
    uid=uuid.uuid4().hex[:20]
    if call(key,'BuildQueryGlobalForAngular',dict(uniqueId=uid,lang='en',archiveIds=[],strSearch=q,synSearch=True)) is None:return
    n=call(key,'GetCount',dict(uniqueId=uid,lang='en',searchType='person',useFilter=False))
    if str(n).isdigit() and 0<int(n)<=250:
        rows=call(key,'GetPersonList',dict(uniqueId=uid,lang='en',rowNum=0,orderBy='LastName',orderType='asc'))
        if isinstance(rows,list):
            for r in rows:print('PERSON',key,{k:r.get(k) for k in ['ObjId','FirstName','LastName','MaidenName','Dob','PlaceBirth']},flush=True)
    return n


query('surname1919','Chmielewski 1919')
query('anna1929','Anna Chmielewski 1929')
query('roman1946','Roman Chmielewski 1946')
query('ernest1947','Ernest Chmielewski 1947')
