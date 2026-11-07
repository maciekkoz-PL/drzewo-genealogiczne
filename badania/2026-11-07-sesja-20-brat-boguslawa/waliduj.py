"""Walidacja zachowania historii, zakresu dowodów i kopii źródeł etapu20."""
from pathlib import Path
import csv,datetime,hashlib,io,json,re,subprocess,openpyxl
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent;BASE='e8cce5c'
def old(path):return subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
a=openpyxl.load_workbook(io.BytesIO(old(book)));b=openpyxl.load_workbook(ROOT/book)
assert a.sheetnames==b.sheetnames and len(b.sheetnames)==23
allowed={'HIPOTEZY_OTWARTE':{'H002':{2,3,4},'H003':{2},'H005':{2}},'ZADANIA_AGENTA':{'T06':{5},'T14':{5},'T47':{5},'T48':{5}},'INSTRUKCJA_AGENTA':{'G01':{2},'G23':{2}}}
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
for sn,n in [('ZRODLA_I_SKANY',239),('KANDYDACI_I_HOMONIMY',97),('DZIENNIK_KWEREND',232),('PLIKI_DOWODOWE',192),('RELACJE_ZRODLOWE',17),('ZADANIA_AGENTA',51),('KOREKTY_I_SPRZECZNOSCI',97)]:
 ids=[r[0] for r in b[sn].values if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
 assert len(ids)==n,(sn,len(ids),n);counts[sn]=len(ids)
for sn,start,col in [('ZRODLA_I_SKANY',233,9),('PLIKI_DOWODOWE',182,1)]:
 for r in b[sn].values:
  if isinstance(r[0],str) and re.fullmatch(r'[SF]\d+',r[0]) and int(r[0][1:])>=start:assert (ROOT/r[col]).is_file(),r[col]
for sn,fn in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
 with (ROOT/'badania/2026-11-06-trzy-poziomy'/fn).open(newline='') as f:assert list(csv.reader(f))==[['' if v is None else str(v) for v in r] for r in b[sn].values]
for f in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:
 assert (ROOT/f).read_bytes()==old(f),f
public=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'witryna/'],cwd=ROOT,text=True).splitlines()
for f in public:assert (ROOT/f).read_bytes()==old(f),f
for sn in ['RDZEN_RODZINY','RODZINA_Z_RELACJI','RELACJE','KANDYDACI_I_HOMONIMY','ZDARZENIA_I_FAKTY','WIARYGODNOSC_OSOB','WIARYGODNOSC_RELACJI']:
 assert list(a[sn].values)==list(b[sn].values),sn
z=HERE/'zrodla';q=json.loads((z/'kwerendy_web.json').read_text());assert len(q['queries'])==20 and len(q['additional_native_queries'])==4
s=json.loads((z/'bg_zarzew/zakres.json').read_text());assert s['initial_loaded_items']=={'1':200,'5':7} and s['collection_totals']=={'1':829,'5':7}
for fn in ['mp1999_99','mp1995_725','mp1995_726']:assert (z/f'odznaczenia/{fn}.pdf').read_bytes().startswith(b'%PDF-')
for fn in ['mp1999_99_page1','mp1995_725_page2']:assert (z/f'odznaczenia/{fn}.png').read_bytes().startswith(b'\x89PNG')
assert 's. Zbigniewa' in (z/'odznaczenia/mp1999_99.txt').read_text()
assert 'Chmielewski Piotr s. Jana' in (z/'odznaczenia/mp1995_725.txt').read_text()
assert 'Page 2 of 2' in (z/'bg_global/janina_exact1910_page2.txt').read_text()
assert 'Page 1 of 1' in (z/'bg_global/witold_exact.txt').read_text()
assert json.loads((z/'msw_dostep.json').read_text())['download_status']==503
assert not (z/'odznaczenia/msw2015_14.pdf').exists()
manifest=[]
for f in sorted(z.rglob('*')):
 if not f.is_file():continue
 raw=f.read_bytes()
 if f.suffix in ['.json','.txt','.html']:assert not re.search(rb'X-Amz-|jsonAuth["=]|eyJ0eXAi|Bearer ',raw),f
 manifest.append(dict(path=str(f.relative_to(HERE)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
(HERE/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline_commit=BASE,sheets=23,counts=counts,old_cells_changed=changes,other_old_cells_preserved=True,source_paths_present=True,original_zips_unchanged=True,public_files_unchanged=True,audits_match=True,no_new_family_relationships=True,no_new_living_relative_claimed=True,bg_cemetery_search_incomplete=True,bg_year_filter_not_reliable=True,unrelated_award_recipients_not_merged=True,transient_url_credentials_excluded=True,source_files=len(manifest),source_bytes=sum(x['bytes'] for x in manifest))
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
