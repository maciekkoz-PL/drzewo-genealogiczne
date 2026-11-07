"""Porównanie wszystkich 24 arkuszy z bazą2e94415 i kontrola kopii źródeł."""
from pathlib import Path
import datetime, hashlib, io, json, re, subprocess, zipfile
import openpyxl
from PIL import Image
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
BASE='2e94415';book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
old=lambda p:subprocess.check_output(['git','show',f'{BASE}:{p}'],cwd=ROOT)
a=openpyxl.load_workbook(io.BytesIO(old(book)));b=openpyxl.load_workbook(ROOT/book)
assert a.sheetnames==b.sheetnames and len(b.sheetnames)==24
allowed={'HIPOTEZY_OTWARTE':{'H002':{2},'H018':{2},'H050':{2}},
         'KANDYDACI_I_HOMONIMY':{'C42':{6,7}},'ZADANIA_AGENTA':{'T57':{5,8}}}
changes=[];counts={}
for sn in a.sheetnames:
    av=list(a[sn].values);bv=list(b[sn].values);assert len(bv)>=len(av),sn
    for n,r in enumerate(av):
        for c,v in enumerate(r):
            if bv[n][c]==v:continue
            header=n==1 and c==0 and sn in ['START','ZRODLA_I_SKANY','KANDYDACI_I_HOMONIMY']
            assert header or c in allowed.get(sn,{}).get(r[0],set()),(sn,n,c)
            changes.append([sn,n+1,c+1])
    ids=[r[0] for r in bv if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
    assert len(ids)==len(set(ids)),sn
    counts[sn]=len(ids)
for sn,n in [('ZRODLA_I_SKANY',277),('KANDYDACI_I_HOMONIMY',102),('DZIENNIK_KWEREND',275),('PLIKI_DOWODOWE',311),('ZADANIA_AGENTA',58)]:
    assert counts[sn]==n,(sn,counts[sn],n)
for sn in ['RDZEN_RODZINY','RODZINA_Z_RELACJI','RELACJE','ZDARZENIA_I_FAKTY','DECYZJA_ROMAN_P12_C69','RELACJE_ZRODLOWE','KORESPONDENCJA']:
    if sn in a.sheetnames:assert list(a[sn].values)==list(b[sn].values),sn
for f in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:
    assert (ROOT/f).read_bytes()==old(f),f
for r in b['ZRODLA_I_SKANY'].values:
    if r[0] in ['S274','S275','S276','S277']:assert (ROOT/r[9]).is_file(),r
for r in b['PLIKI_DOWODOWE'].values:
    if isinstance(r[0],str) and re.fullmatch(r'F\d+',r[0]) and int(r[0][1:])>=279:assert (ROOT/r[1]).is_file()
files=json.loads((HERE/'manifest.json').read_text())
assert len(files)==33
for rec in files:
    f=ROOT/rec['path'];raw=f.read_bytes();assert hashlib.sha256(raw).hexdigest()==rec['sha256'],f
    if f.suffix in ['.json','.csv']:assert not re.search(rb'Bearer |X-Amz-|jsonAuth["=]|siwc_bypass',raw),f
    if f.suffix=='.jpg':Image.open(io.BytesIO(raw)).verify()
with zipfile.ZipFile(HERE/'zrodla/kolumny_25446.zip') as z:assert z.testzip() is None
s=json.loads((HERE/'zrodla/zakres_odczytu.json').read_text())
assert s['new_proven_family_relationships']==0 and s['name_columns_read']==[[4,124]]
assert 98 in s['full_selected'] and len(s['full_selected'])==21
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),baseline=BASE,
    sheets=24,counts=counts,old_cells_changed=changes,all_other_old_cells_preserved=True,
    original_zips_preserved=True,parallel_changes_preserved=True,new_confirmed_family_relationships=0,
    new_address_correlation=True,source_files=len(files),source_hashes_valid=True)
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
