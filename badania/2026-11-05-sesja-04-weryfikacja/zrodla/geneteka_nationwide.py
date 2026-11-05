"""Check competing couples and parent-pair records in every offered region.

Uses the complete public DataTables request format that passed a positive
control. Two concurrent read-only requests; no corrections or messages posted.
"""
from pathlib import Path
import urllib.request, urllib.parse, http.cookiejar
import json, hashlib, datetime, concurrent.futures
from lxml import html

p=Path('work/h017-s04/geneteka/nationwide');p.mkdir(parents=True,exist_ok=True)
base={k:v[0] for k,v in json.loads(Path('work/boguslaw2/geneteka_template.json').read_text()).items()}
base['search[value]']=''
for i in range(10):base[f'columns[{i}][name]']='';base[f'columns[{i}][search][value]']=''
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
ui='https://geneteka.genealodzy.pl/index.php?op=gt&lang=pol&w=05ld&bdm=S&rid=S&search_lastname=Chmielewski&search_name=Czes%C5%82aw&search_lastname2=Poprawka&search_name2=Janina&search_as=1&from_date=1936&to_date=1936'
with opener.open(ui,timeout=25) as response:response.read()
headers={'User-Agent':'Mozilla/5.0','Referer':ui,'X-Requested-With':'XMLHttpRequest'}
def fetch(key,query):
    url='https://geneteka.genealodzy.pl/api/getAct.php?'+urllib.parse.urlencode(query)
    row={'url':url,'params':query,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        with opener.open(urllib.request.Request(url,headers=headers),timeout=25) as r:
            b=r.read();row.update(status=r.status,final_url=r.url,size=len(b),sha256=hashlib.sha256(b).hexdigest())
        f=p/(key+'.json');f.write_bytes(b);row['path']=str(f)
        data=json.loads(b);row.update(recordsTotal=data.get('recordsTotal'),recordsFiltered=data.get('recordsFiltered'),rows=len(data.get('data',[])))
        if row['recordsTotal'] is not None:row['complete_response']=row['recordsTotal']==row['rows']
        else:row['complete_response']=False
    except Exception as e:row['error']=str(e)
    return row

logs=[]
def save(row):
    logs.append(row);(p/'downloads.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
    if row.get('error') or row.get('recordsTotal') or not row.get('complete_response'):
        print(Path(row.get('path','unknown')).name,'total',row.get('recordsTotal'),'rows',row.get('rows'),'error',row.get('error'),flush=True)
control=fetch('positive_control_1936',base);save(control)
assert control.get('recordsTotal')==1 and control.get('rows')==1, 'Positive control failed; do not trust negatives or continue batch'
single=base.copy()
for key in ['search_lastname2','search_name2','search_as']:single.pop(key,None)
for key,change in [
 ('ld_D1988_fixed',{'bdm':'D','rid':'D','search_name':'','from_date':'1988','to_date':'1988'}),
 ('ld_B_Boguslaw1942_1944_fixed',{'bdm':'B','rid':'B','search_name':'Bogusław','from_date':'1942','to_date':'1944'}),
]:save(fetch(key,{**single,**change}))

tree=html.fromstring(Path('work/h017-s04/catalogues/geneteka.html').read_bytes())
regions=[(x.get('value'),x.text_content()) for x in tree.xpath('//select[@name="w"]/option') if x.get('value')]
jobs=[]
for region,label in regions:
    for kind,lo,hi in [('S','1880','1960'),('B','1930','1960'),('D','1930','1990')]:
        query={**base,'bdm':kind,'rid':kind,'w':region,'from_date':lo,'to_date':hi}
        jobs.append((region+'_'+kind+'_'+lo+'_'+hi,query))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    futures=[pool.submit(fetch,key,query) for key,query in jobs]
    for f in concurrent.futures.as_completed(futures):save(f.result())
print('DONE requests',len(logs),'regions',len(regions),'incomplete',sum(not x.get('complete_response',False) for x in logs),'rows',sum(x.get('rows',0) for x in logs),flush=True)
