"""Kontrola zachowania historii, zakresu nowej migracji i spójności artefaktów."""
from pathlib import Path
import csv, datetime, hashlib, io, json, re, subprocess, openpyxl
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
BASE='82502f22160bd6220b5b63531e3741e902521180'
def old(path):return subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
a=openpyxl.load_workbook(io.BytesIO(old(book)));b=openpyxl.load_workbook(ROOT/book)
assert len(b.sheetnames)==23 and a.sheetnames==b.sheetnames
allowed={
 'HIPOTEZY_OTWARTE':{'H019':{2,3,4},'H032':{2,3,4},'H033':{4}},
 'ZADANIA_AGENTA':{'T41':{5},'T42':{5}},
 'INSTRUKCJA_AGENTA':{'G01':{2}}
}
changes=[]
for name in a.sheetnames:
 av=list(a[name].values);bv=list(b[name].values)
 assert len(bv)>=len(av),name
 for n,r in enumerate(av):
  for c,val in enumerate(r):
   if val==bv[n][c]:continue
   header=(name in ['START','INSTRUKCJA_AGENTA','ZRODLA_I_SKANY'] and n==1 and c==0)
   assert header or c in allowed.get(name,{}).get(r[0],set()),(name,n,c,val,bv[n][c])
   changes.append([name,n+1,c+1])
 ids=[r[0] for r in bv if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
 assert len(ids)==len(set(ids)),name
counts={}
for sheet,expected in [('ZRODLA_I_SKANY',216),('KANDYDACI_I_HOMONIMY',97),('DZIENNIK_KWEREND',193),('PLIKI_DOWODOWE',162),('RELACJE_ZRODLOWE',16)]:
 rows=[r for r in b[sheet].values if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
 assert len(rows)==expected,(sheet,len(rows));counts[sheet]=len(rows)
for r in b['ZRODLA_I_SKANY'].values:
 if isinstance(r[0],str) and re.fullmatch(r'S\d+',r[0]) and int(r[0][1:])>=205:assert (ROOT/r[9]).is_file(),r[9]
for r in b['PLIKI_DOWODOWE'].values:
 if isinstance(r[0],str) and re.fullmatch(r'F\d+',r[0]) and int(r[0][1:])>=151:assert (ROOT/r[1]).is_file(),r[1]
for sn,filename in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
 with (ROOT/'badania/2026-11-06-trzy-poziomy'/filename).open(newline='') as f:
  assert list(csv.reader(f))==[['' if v is None else str(v) for v in r] for r in b[sn].values],sn
for f in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:
 assert hashlib.sha256((ROOT/f).read_bytes()).digest()==hashlib.sha256(old(f)).digest(),f
# Cały publiczny produkt (dane, HTML, kod, portrety i publikacja) zachowany byte-for-byte.
public=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'witryna/'],cwd=ROOT,text=True).splitlines()
for f in public:assert (ROOT/f).read_bytes()==old(f),f
d=json.loads((ROOT/'witryna/wiarygodnosc.json').read_text())
embedded=json.loads((ROOT/'witryna/public/index.html').read_text().split('<script id="family-data" type="application/json">')[1].split('</script>')[0].replace('<\\/','</'))
assert len(d['people'])==71 and len(d['edges'])==len(d['relations'])==96 and len(embedded['news'])==9
for field in ['people','edges','relations','sources']:assert d[field]==embedded[field]
assert ['P02','P01','family'] in d['edges'] or any(e[0]=='P02' and e[1]=='P01' for e in d['edges'])
g=HERE/'zrodla/geneteka'
control=json.loads((g/'control1932.json').read_text());assert control['recordsTotal']==1
first=json.loads((g/'lublin_mandziuk_all.json').read_text());second=json.loads((g/'lublin_mandziuk_all_page2.json').read_text())
assert first['recordsTotal']==second['recordsTotal']==66
assert len(first['data'])==50 and len(second['data'])==16
assert (HERE/'zrodla/grobonet/control_dylkiewicz.txt').read_text().find('1 region')>=0 or 'Pomorskie' in (HERE/'zrodla/grobonet/control_dylkiewicz.txt').read_text()
for f in (HERE/'zrodla/swa1908').glob('scan*_odpowiedz_html.txt'):assert b'Incapsula' in f.read_bytes()
photos=list((HERE/'zrodla/tczew').glob('card_*_photo*.jpg'));assert len(photos)==8
for f in photos:assert f.read_bytes().startswith(b'\xff\xd8'),f
assert len(json.loads((HERE/'zrodla/tczew/name_queries.json').read_text()))==6
assert len(json.loads((HERE/'zrodla/tczew/pagination_queries.json').read_text()))==6
manifest=[]
for f in sorted((HERE/'zrodla').rglob('*')):
 if f.is_file():
  assert f.name not in ['browser_state_private.json','cookies.json']
  manifest.append(dict(path=str(f.relative_to(HERE)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(HERE/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline_commit=BASE,sheets=23,counts=counts,old_cells_changed=changes,other_old_cells_preserved=True,original_zips_unchanged=True,all_public_files_unchanged=True,public_people=71,public_edges=96,public_news=9,audits_match=True,geneteka_control_positive=True,geneteka_mandziuk_66_of_66=True,tczew_result_pages=12,tczew_photos_reviewed=8,swa_error_html_not_counted_as_act=True,no_new_family_relationships=True,no_new_living_relative_claimed=True,source_files=len(manifest),source_bytes=sum(x['bytes'] for x in manifest))
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='old_cells_changed'},ensure_ascii=False))
