from pathlib import Path
import datetime,hashlib,io,json,re,subprocess,zipfile
import openpyxl
from PIL import Image
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
BASE='0fe719edf7baf23c5ce8eaef9337256849713797';book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
prior=lambda p:subprocess.check_output(['git','show',f'{BASE}:{p}'],cwd=ROOT)
a=openpyxl.load_workbook(io.BytesIO(prior(book)));b=openpyxl.load_workbook(ROOT/book)
assert a.sheetnames==b.sheetnames
changed=[];counts={}
for sn in a.sheetnames:
 av=list(a[sn].values);bv=list(b[sn].values);assert len(bv)>=len(av)
 for i,r in enumerate(av):
  for j,v in enumerate(r):
   if bv[i][j]==v:continue
   allowed=(i==1 and j==0 and sn in ['START','ZRODLA_I_SKANY','INDEKS_MELDUNKOW']) or (sn=='KANDYDACI_I_HOMONIMY' and r[0]=='C102' and j in [2,6,7]) or (sn=='HIPOTEZY_OTWARTE' and r[0]=='H052' and j in [2,3]) or (sn=='ZADANIA_AGENTA' and r[0]=='T58' and j in [5,8])
   assert allowed,(sn,i,j);changed.append([sn,i+1,j+1])
 ids=[r[0] for r in bv if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
 assert len(ids)==len(set(ids)),sn;counts[sn]=len(ids)
for sn in ['RDZEN_RODZINY','RODZINA_Z_RELACJI','RELACJE','ZDARZENIA_I_FAKTY','RELACJE_ZRODLOWE','WIARYGODNOSC_OSOB','WIARYGODNOSC_RELACJI','SZKICE_GMAIL','DECYZJA_ROMAN_P12_C69']:
 assert list(a[sn].values)==list(b[sn].values),sn
for sn,n in [('ZRODLA_I_SKANY',287),('DZIENNIK_KWEREND',287),('PLIKI_DOWODOWE',382),('KANDYDACI_I_HOMONIMY',102),('INSTRUKCJA_AGENTA',27),('INDEKS_MELDUNKOW',47)]:assert counts[sn]==n,(sn,counts[sn])
for f in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:
 if (ROOT/f).exists():assert (ROOT/f).read_bytes()==prior(f)
manifest=json.loads((HERE/'manifest.json').read_text())+json.loads((HERE/'katalog_manifest.json').read_text());assert len(manifest)==27
for rec in manifest:
 raw=(ROOT/rec['path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==rec['sha256']
 if rec['path'].endswith('.jpg'):Image.open(io.BytesIO(raw)).verify()
with zipfile.ZipFile(HERE/'zrodla/kolumny_Chojny2140.zip') as z:assert len(z.namelist())==29 and z.testzip() is None
scope=json.loads((HERE/'zrodla/zakres_odczytu.json').read_text());assert scope['name_columns_read']==[[5,195]] and len(scope['full_selected_this_stage'])==7
assert len(json.loads((HERE/'zrodla/pobrane_sha256.json').read_text()))==196
for uid,count in [(15351995,205),(15351997,197)]:
 m=json.loads((HERE/f'katalog/manifest_{uid}.json').read_text());assert m['liczbaWszystkichSkanow']==count and len(m['elementy'])==count
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=browser.new_page()
 page.set_content((HERE/'INDEKS.html').read_text());assert page.locator('tbody tr').count()==47
 page.locator('#q').fill('1947');assert page.locator('tbody tr:visible').count()==1
 page.locator('#q').fill('1496');assert page.locator('tbody tr:visible').count()==2
 browser.close()
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline=BASE,counts=counts,old_cells_changed=changed,all_other_old_cells_preserved=True,all_person_relationship_sheets_preserved=True,original_packages_preserved=True,source_files=27,hashes_valid=True,index_rows=47,older_arrival_manifests=[205,197],older_arrival_scans_read=0,new_proven_family_relationships=0)
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
