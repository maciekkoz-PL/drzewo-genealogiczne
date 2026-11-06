"""Kontrola zachowania poprzedniej bazy i rozdzielenia australijskiej hipotezy."""
from pathlib import Path
import csv,datetime,hashlib,io,json,re,subprocess,openpyxl
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
BASE='1b2a1a7d9d38137a9dbf59f571b01cd4c19336f1'
def old(path):return subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
a=openpyxl.load_workbook(io.BytesIO(old(book)));b=openpyxl.load_workbook(ROOT/book)
assert a.sheetnames==b.sheetnames and len(b.sheetnames)==23
allowed={'RDZEN_RODZINY':{'P12':{9},'P05':{9}},'WIARYGODNOSC_OSOB':{'P12':{7,8}}}
changes=[]
for name in a.sheetnames:
 av=list(a[name].values);bv=list(b[name].values);assert len(bv)>=len(av),name
 for n,row in enumerate(av):
  for col,value in enumerate(row):
   if value==bv[n][col]:continue
   assert (name=='ZRODLA_I_SKANY' and n==1 and col==0) or col in allowed.get(name,{}).get(row[0],set()),(name,n,col,value,bv[n][col])
   changes.append([name,n+1,col+1])
 ids=[r[0] for r in bv if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
 assert len(ids)==len(set(ids)),name
counts={}
for sheet,expected in [('ZRODLA_I_SKANY',194),('KANDYDACI_I_HOMONIMY',78),('DZIENNIK_KWEREND',164),('PLIKI_DOWODOWE',138),('RELACJE_ZRODLOWE',16)]:
 rows=[r for r in b[sheet].values if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
 assert len(rows)==expected,(sheet,len(rows));counts[sheet]=len(rows)
for row in b['ZRODLA_I_SKANY'].values:
 if isinstance(row[0],str) and re.fullmatch(r'S\d+',row[0]) and int(row[0][1:])>=181:assert (ROOT/row[9]).is_file(),row[9]
for row in b['PLIKI_DOWODOWE'].values:
 if isinstance(row[0],str) and re.fullmatch(r'F\d+',row[0]) and int(row[0][1:])>=125:assert (ROOT/row[1]).is_file(),row[1]
for sn,file in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
 expected=[['' if v is None else str(v) for v in r] for r in b[sn].values]
 with (ROOT/'badania/2026-11-06-trzy-poziomy'/file).open(newline='') as f:actual=list(csv.reader(f))
 assert actual==expected,sn
for file in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:
 assert hashlib.sha256((ROOT/file).read_bytes()).digest()==hashlib.sha256(old(file)).digest(),file
data=json.loads((ROOT/'witryna/wiarygodnosc.json').read_text());before=json.loads(old('witryna/wiarygodnosc.json'))
assert data['edges'][:len(before['edges'])]==before['edges']
assert data['relations'][:len(before['relations'])]==before['relations']
assert len(data['people'])==55 and len(data['edges'])==79 and len(data['relations'])==79
bp={p['id']:p for p in before['people']};p={p['id']:p for p in data['people']}
for ident,v in bp.items():
 for field in v:
  if ident=='P12' and field in ['note','missing']:continue
  assert v[field]==p[ident][field],(ident,field)
for ident in ['C69','C70','C71','C72']:
 assert p[ident]['level']==p[ident]['connectionLevel']==p[ident]['identityLevel']==3
 assert p[ident]['branch']=='paternal' and p[ident]['status']=='candidate'
 assert p[ident]['y']<p['P01']['y']
assert 'nie ustalono, czy obecnie żyje' in p['C71']['note'].lower() and 'nie ustalono, czy obecnie żyje' in p['C72']['note'].lower()
rels={r['id']:r for r in data['relations']}
assert rels['V067']['a']=='P12' and rels['V067']['b']=='C69' and rels['V067']['kind']=='identity_candidate' and rels['V067']['level']==3
for ident in ['R042','R043','R044']:assert rels[ident]['level']==1
assert not any(e[0]=='P12' and e[1] in ['C70','C71','C72'] for e in data['edges'])
assert not any(e[0]=='C70' and e[1] in ['C71','C72'] for e in data['edges'])
for person in data['people']:
 for src in person.get('source',[]):assert src in data['sources'],(person['id'],src)
for edge,rel in zip(data['edges'],data['relations']):
 assert edge==[rel['a'],rel['b'],rel['kind']],(edge,rel['id'])
html=(ROOT/'witryna/public/index.html').read_text()
embedded=json.loads(html.split('<script id="family-data" type="application/json">')[1].split('</script>')[0].replace('<\\/','</'))
assert all(embedded[k]==data[k] for k in ['people','edges','sources','relations'])
assert len(embedded['news'])==8 and 'Australijski trop' in embedded['news'][0]['title']
assert not any(t in html.lower() for t in ['niewidom','blind','browser_state_private'])
query_count=0
for file in (HERE/'zrodla/web').glob('*.json'):
 obj=json.loads(file.read_text());query_count+=sum(len(v.get('queries',[])) for v in obj['calls'].values())
assert query_count==76,query_count
manifest=[]
for f in sorted((HERE/'zrodla').rglob('*')):
 if f.is_file():
  assert f.name!='browser_state_private.json'
  manifest.append(dict(path=str(f.relative_to(HERE)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(HERE/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report=dict(result='PASS',baseline_commit=BASE,at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sheets=23,counts=counts,new_sources=14,new_candidates=10,queries=76,firecrawl_queries=1,people=55,edges=79,news=8,old_rows_preserved_except_listed_cells=changes,old_zip_bytes_unchanged=True,audits_match=True,old_public_people_and_edges_preserved=True,maternal_branch_unchanged=True,P12_C69_not_merged=True,current_life_not_claimed=True,source_files=len(manifest),source_bytes=sum(x['bytes'] for x in manifest))
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
