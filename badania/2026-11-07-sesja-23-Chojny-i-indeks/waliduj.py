from pathlib import Path
import datetime, hashlib, io, json, re, subprocess, zipfile
import openpyxl
from PIL import Image
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
BASE='16b2f73995982cf961bf87b078c9121d2cc18c5a';book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
old=lambda p:subprocess.check_output(['git','show',f'{BASE}:{p}'],cwd=ROOT)
a=openpyxl.load_workbook(io.BytesIO(old(book)));b=openpyxl.load_workbook(ROOT/book)
assert b.sheetnames==a.sheetnames+['INDEKS_MELDUNKOW']
changed=[];counts={}
for sn in a.sheetnames:
    av=list(a[sn].values);bv=list(b[sn].values);assert len(bv)>=len(av)
    for n,r in enumerate(av):
        for c,v in enumerate(r):
            if bv[n][c]==v:continue
            allowed=(n==1 and c==0 and sn in ['START','ZRODLA_I_SKANY']) or (sn=='HIPOTEZY_OTWARTE' and r[0]=='H052' and c==2) or (sn=='ZADANIA_AGENTA' and r[0]=='T58' and c in [5,8])
            assert allowed,(sn,n,c);changed.append([sn,n+1,c+1])
    ids=[r[0] for r in bv if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
    assert len(ids)==len(set(ids)),sn
    counts[sn]=len(ids)
for sn in ['RDZEN_RODZINY','RODZINA_Z_RELACJI','RELACJE','KANDYDACI_I_HOMONIMY','ZDARZENIA_I_FAKTY','DECYZJA_ROMAN_P12_C69','RELACJE_ZRODLOWE','SZKICE_GMAIL']:
    assert list(a[sn].values)==list(b[sn].values),sn
for sn,n in [('ZRODLA_I_SKANY',283),('DZIENNIK_KWEREND',283),('PLIKI_DOWODOWE',355),('KANDYDACI_I_HOMONIMY',102),('INSTRUKCJA_AGENTA',26)]:assert counts[sn]==n,(sn,counts[sn])
assert b['INDEKS_MELDUNKOW'].max_row==47
for f in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip','witryna/dane.json','witryna/index.html']:
    if (ROOT/f).exists():assert (ROOT/f).read_bytes()==old(f),f
for rec in json.loads((HERE/'manifest.json').read_text()):
    f=ROOT/rec['path'];raw=f.read_bytes();assert hashlib.sha256(raw).hexdigest()==rec['sha256']
    if f.suffix in ['.json','.csv','.txt']:assert not re.search(rb'Bearer |X-Amz-|jsonAuth["=]|siwc_bypass|uploadRef|signedUrl',raw),f
    if f.suffix in ['.png','.jpg']:Image.open(io.BytesIO(raw)).verify()
with zipfile.ZipFile(HERE/'zrodla/kolumny_Chojny2139.zip') as z:assert z.testzip() is None and len(z.namelist())==32
s=json.loads((HERE/'zrodla/zakres_odczytu.json').read_text());assert s['name_columns_read']==[[5,85],[87,196]] and len(s['full_selected'])==11
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page();page.set_content((HERE/'INDEKS.html').read_text());assert page.locator('tbody tr').count()==44
    page.locator('#q').fill('Agnieszka');assert page.locator('tbody tr:visible').count()==2
    page.locator('#q').fill('Widawa');assert page.locator('tbody tr:visible').count()==1
    page.locator('#q').fill('Łódź');upper=page.locator('tbody tr:visible').count()
    page.locator('#q').fill('lodz');assert page.locator('tbody tr:visible').count()==upper and upper>0
    browser.close()
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline=BASE,sheets=25,counts=counts,old_cells_changed=changed,
    all_other_old_cells_preserved=True,all_person_and_relationship_sheets_preserved=True,original_zips_preserved=True,
    source_files=27,source_hashes_valid=True,index_rows=44,index_browser_filter='PASS; Agnieszka2,Widawa1,Łódź=lodz',
    new_family_relationships=0,public_tree_unchanged=True,external_HTR_performed=False)
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
