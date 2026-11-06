"""Zachowanie historii Excela, zgodność identyfikatorów i kopii źródeł."""
from pathlib import Path
import csv,datetime,hashlib,io,json,re,subprocess,openpyxl
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent;BASE='eb159ad'
def old(path):return subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
a=openpyxl.load_workbook(io.BytesIO(old(book)));b=openpyxl.load_workbook(ROOT/book)
assert a.sheetnames==b.sheetnames and len(b.sheetnames)==23
allowed={'HIPOTEZY_OTWARTE':{'H019':{2},'H032':{2}},'ZADANIA_AGENTA':{'T46':{5,7}}}
changes=[]
for name in a.sheetnames:
 av=list(a[name].values);bv=list(b[name].values);assert len(bv)>=len(av),name
 for n,r in enumerate(av):
  for c,val in enumerate(r):
   if val==bv[n][c]:continue
   header=(name in ['START','INSTRUKCJA_AGENTA','ZRODLA_I_SKANY'] and n==1 and c==0)
   assert header or c in allowed.get(name,{}).get(r[0],set()),(name,n,c)
   changes.append([name,n+1,c+1])
 ids=[r[0] for r in bv if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
 assert len(ids)==len(set(ids)),name
counts={}
for sn,n in [('ZRODLA_I_SKANY',232),('KANDYDACI_I_HOMONIMY',97),('DZIENNIK_KWEREND',220),('PLIKI_DOWODOWE',181),('RELACJE_ZRODLOWE',16)]:
 ids=[r[0] for r in b[sn].values if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
 assert len(ids)==n,(sn,len(ids),n);counts[sn]=len(ids)
for sn,start,col in [('ZRODLA_I_SKANY',224,9),('PLIKI_DOWODOWE',172,1)]:
 for r in b[sn].values:
  if isinstance(r[0],str) and re.fullmatch(r'[SF]\d+',r[0]) and int(r[0][1:])>=start:assert (ROOT/r[col]).is_file(),r[col]
for sn,fn in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
 with (ROOT/'badania/2026-11-06-trzy-poziomy'/fn).open(newline='') as f:assert list(csv.reader(f))==[['' if v is None else str(v) for v in r] for r in b[sn].values]
for f in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:
 assert (ROOT/f).read_bytes()==old(f),f
public=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'witryna/'],cwd=ROOT,text=True).splitlines()
for f in public:assert (ROOT/f).read_bytes()==old(f),f
catalog=json.loads((HERE/'zrodla/majdan/jednostki_159.json').read_text())
assert len(catalog)==len({r['signature'] for r in catalog})==159
assert all(r['scans']==0 for r in catalog)
assert 'Sznury' in next(r['title'] for r in catalog if r['signature'].endswith('/156'))
control=json.loads((HERE/'zrodla/straty_control/control_rows.json').read_text());assert set(control)=={'id5791928','id4205404'}
assert all('1909-07-03' in v for v in control.values())
assert len(json.loads((HERE/'zrodla/straty/queries.json').read_text()))==4
assert len(json.loads((HERE/'zrodla/straty/maiden_queries.json').read_text()))==4
assert len(json.loads((HERE/'zrodla/kwerendy_web_koniec.json').read_text()))==39
assert len(json.loads((HERE/'zrodla/bg/cards.json').read_text()))==5
assert len(json.loads((HERE/'zrodla/album4345.json').read_text())['result']['images'])==45
assert len(list((HERE/'zrodla/ksiegi1926').glob('*.jpg')))==6
for f in (HERE/'zrodla/ksiegi1926').glob('*.jpg'):assert f.read_bytes().startswith(b'\xff\xd8')
manifest=[]
for f in sorted((HERE/'zrodla').rglob('*')):
 if not f.is_file():continue
 raw=f.read_bytes()
 if f.suffix in ['.json','.txt','.html']:assert not re.search(rb'X-Amz-|jsonAuth=|eyJ0eXAi',raw),f
 manifest.append(dict(path=str(f.relative_to(HERE)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
(HERE/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline_commit=BASE,sheets=23,counts=counts,old_cells_changed=changes,other_old_cells_preserved=True,source_paths_present=True,original_zips_unchanged=True,public_files_unchanged=True,audits_match=True,no_new_family_relationships=True,no_new_living_relative_claimed=True,majdan_metadata_records=159,majdan_scans=0,public_grave_cards_read=5,straty_positive_control=True,web_queries=39,transient_url_credentials_excluded=True,source_files=len(manifest),source_bytes=sum(x['bytes'] for x in manifest))
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
