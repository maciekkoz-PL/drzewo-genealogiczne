from pathlib import Path
import csv,datetime,hashlib,io,json,re,subprocess,openpyxl
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
BASE='4b4141e5ee76d2c8488b32cba581c6913ded5524'
def old(path):return subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx';a=openpyxl.load_workbook(io.BytesIO(old(book)));b=openpyxl.load_workbook(ROOT/book)
assert len(b.sheetnames)==23 and a.sheetnames==b.sheetnames
allowed={'RDZEN_RODZINY':{'P12':{9}},'KANDYDACI_I_HOMONIMY':{k:{7,8} for k in ['C69','C70','C71','C72']},'HIPOTEZY_OTWARTE':{k:{2,3,4} for k in ['H035','H036','H039']},'WIARYGODNOSC_OSOB':{k:{6,7,8} for k in ['P12','C69','C70','C71','C72']}}
allowed['KANDYDACI_I_HOMONIMY']['C75']={1,2,5,6,7,8,9};allowed['WIARYGODNOSC_OSOB']['C75']={1,2,4,5,6,7,8}
changes=[]
for name in a.sheetnames:
 av=list(a[name].values);bv=list(b[name].values);assert len(bv)>=len(av),name
 for n,r in enumerate(av):
  for col,val in enumerate(r):
   if val==bv[n][col]:continue
   assert (name=='ZRODLA_I_SKANY' and n==1 and col==0) or col in allowed.get(name,{}).get(r[0],set()),(name,n,col,val,bv[n][col])
   changes.append([name,n+1,col+1])
 ids=[r[0] for r in bv if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])];assert len(ids)==len(set(ids)),name
counts={}
for sheet,expected in [('ZRODLA_I_SKANY',204),('KANDYDACI_I_HOMONIMY',96),('DZIENNIK_KWEREND',176),('PLIKI_DOWODOWE',150),('RELACJE_ZRODLOWE',16)]:
 rows=[r for r in b[sheet].values if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])];assert len(rows)==expected,(sheet,len(rows));counts[sheet]=len(rows)
for row in b['ZRODLA_I_SKANY'].values:
 if isinstance(row[0],str) and re.fullmatch(r'S\d+',row[0]) and int(row[0][1:])>=195:assert (ROOT/row[9]).is_file(),row[9]
for row in b['PLIKI_DOWODOWE'].values:
 if isinstance(row[0],str) and re.fullmatch(r'F\d+',row[0]) and int(row[0][1:])>=139:assert (ROOT/row[1]).is_file(),row[1]
for sn,file in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
 expected=[['' if v is None else str(v) for v in r] for r in b[sn].values]
 with (ROOT/'badania/2026-11-06-trzy-poziomy'/file).open(newline='') as f:assert list(csv.reader(f))==expected,sn
for file in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:assert hashlib.sha256((ROOT/file).read_bytes()).digest()==hashlib.sha256(old(file)).digest(),file
d=json.loads((ROOT/'witryna/wiarygodnosc.json').read_text());prev=json.loads(old('witryna/wiarygodnosc.json'));ps={p['id']:p for p in d['people']}
assert len(d['people'])==71 and len(d['edges'])==96 and len(d['relations'])==96
assert d['edges'][:len(prev['edges'])]==prev['edges'] and d['relations'][:len(prev['relations'])]==prev['relations']
for before in prev['people']:
 for field in before:
  if before['id']=='P12' and field in ['note','missing']:continue
  if before['id'] in ['C69','C70','C71','C72'] and field in ['note','missing','source']:continue
  if before['id']=='C69' and field in ['addresses','locations']:continue
  if before['id']=='C71' and field in ['addresses','locations']:continue
  assert before[field]==ps[before['id']][field],(before['id'],field)
assert not any(i in ps for i in ['C80','C95','C96'])
imported=json.loads((HERE/'zrodla/hosting20_import.json').read_text())
remote_html=(HERE/'zrodla/hosting20.html').read_text()
remote=json.loads(remote_html.split('<script id="family-data" type="application/json">')[1].split('</script>')[0].replace('<\\/','</'))
remote_ps={p['id']:p for p in remote['people']}
for ident,fields in imported['imported_data_fields'].items():
 for key in fields:assert ps[ident][key]==remote_ps[ident][key],(ident,key)
assert hashlib.sha256((ROOT/imported['photo_path']).read_bytes()).hexdigest()==imported['photo_sha256']
for p in d['people']:
 for source in p.get('source',[]):assert source in d['sources'],(p['id'],source)
for edge,rel in zip(d['edges'],d['relations']):assert edge==[rel['a'],rel['b'],rel['kind']]
assert any(e==['C71','C79','identity_candidate'] for e in d['edges']) and any(e==['C72','C75','identity_candidate'] for e in d['edges'])
assert any(e==['P12','C69','identity_candidate'] for e in d['edges'])
for i in range(82,95):
 p=ps['C'+str(i)];assert p['level']==3 and p['name'].endswith('nazwisko niepodane') and 'Obecny stan życia nieustalony' in p['note']
 assert ['C79',p['id'],'family'] in d['edges']
 assert not any(e[1]==p['id'] and e[2] in ['document','parent'] for e in d['edges'])
assert not any(e[0]=='C81' and e[1] in ['C'+str(i) for i in range(82,95)] for e in d['edges'])
assert not any(e[0] in ['C'+str(i) for i in range(82,88)] and e[1] in ['C'+str(i) for i in range(88,95)] for e in d['edges'])
for i in ['C75','C79','C81']+['C'+str(i) for i in range(82,95)]:assert ps[i]['level']==3 and ps[i]['y']<ps['P01']['y']
html=(ROOT/'witryna/public/index.html').read_text();embedded=json.loads(html.split('<script id="family-data" type="application/json">')[1].split('</script>')[0].replace('<\\/','</'))
assert all(embedded[k]==d[k] for k in ['people','edges','sources','relations']) and len(embedded['news'])==9
assert not any(t in html.lower() for t in ['niewidom','blind','browser_state_private'])
params=json.loads((HERE/'zrodla/parametry_kwerend.json').read_text());assert len(params['web_queries'])==33 and len(params['firecrawl_searches'])==16 and len(params['firecrawl_scrapes_basic'])==3
gct=json.loads((HERE/'zrodla/gct_response_58.bin').read_bytes())['data'];assert gct['TotalHitCount']==3 and gct['TotalPageCount']==1
assert {x['LocationId'] for x in gct['SearchHits']}=={75607}
assert {x['PersonId'] for x in gct['SearchHits']}=={38035,940272,36197}
for r in gct['SearchHits']:
 assert r['DateOfBirth']==('1947-11-20' if r['PersonId']==940272 else None)
manifest=[]
for f in sorted((HERE/'zrodla').rglob('*')):
 if f.is_file():
  assert f.name!='browser_state_private.json';manifest.append(dict(path=str(f.relative_to(HERE)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(HERE/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline_commit=BASE,sheets=23,counts=counts,people=71,edges=96,news=9,old_rows_preserved_except_listed_cells=changes,original_zips_unchanged=True,audits_match=True,maternal_branch_unchanged=True,old_public_edges_and_relations_preserved=True,remote_version20_maps_photo_and_relationship_descriptions_preserved=True,unconfirmed_identifications_not_merged=True,no_invented_biological_roles=True,no_invented_surnames=True,current_life_not_claimed=True,source_files=len(manifest),source_bytes=sum(x['bytes'] for x in manifest),web_queries=33,firecrawl_searches=16,firecrawl_scrapes_basic=3)
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='old_rows_preserved_except_listed_cells'},ensure_ascii=False))
