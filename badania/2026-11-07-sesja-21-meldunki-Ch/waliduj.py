"""Kontrola historii Excelu, identyfikatorów, źródeł i niezmienności drzewa."""
from pathlib import Path
import csv, datetime, hashlib, io, json, re, subprocess, zipfile
import openpyxl
from PIL import Image

ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent;BASE='c5b551d'
def old(path):return subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
book='Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
a=openpyxl.load_workbook(io.BytesIO(old(book))); b=openpyxl.load_workbook(ROOT/book)
assert a.sheetnames==b.sheetnames and len(b.sheetnames)==24
allowed={'HIPOTEZY_OTWARTE':{'H002':{2},'H017':{2}},'ZADANIA_AGENTA':{'T50':{4,5,7,8}}}
changes=[]; counts={}
for sn in a.sheetnames:
    av=list(a[sn].values);bv=list(b[sn].values)
    assert len(bv)>=len(av),sn
    for n,r in enumerate(av):
        for c,v in enumerate(r):
            if v==bv[n][c]:continue
            header=sn in ['START','ZRODLA_I_SKANY'] and n==1 and c==0
            assert header or c in allowed.get(sn,{}).get(r[0],set()),(sn,n+1,c+1)
            changes.append([sn,n+1,c+1])
    ids=[r[0] for r in bv if isinstance(r[0],str) and re.fullmatch(r'[A-Z]+-?\d+',r[0])]
    assert len(ids)==len(set(ids)),sn
    counts[sn]=len(ids)
for sn,n in [('ZRODLA_I_SKANY',259),('KANDYDACI_I_HOMONIMY',101),('DZIENNIK_KWEREND',257),
             ('KOREKTY_I_SPRZECZNOSCI',99),('ZADANIA_AGENTA',57),('RELACJE_ZRODLOWE',18)]:
    assert counts[sn]==n,(sn,counts[sn],n)
for sn in ['RDZEN_RODZINY','RODZINA_Z_RELACJI','RELACJE','ZDARZENIA_I_FAKTY','WIARYGODNOSC_OSOB',
           'WIARYGODNOSC_RELACJI','DECYZJA_ROMAN_P12_C69','RELACJE_ZRODLOWE']:
    assert list(a[sn].values)==list(b[sn].values),sn
for sn,fn in [('WIARYGODNOSC_OSOB','AUDYT_OSOB.csv'),('WIARYGODNOSC_RELACJI','AUDYT_RELACJI.csv')]:
    with (ROOT/'badania/2026-11-06-trzy-poziomy'/fn).open(newline='') as f:
        assert list(csv.reader(f))==[['' if v is None else str(v) for v in r] for r in b[sn].values]
for path in subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'witryna/'],cwd=ROOT,text=True).splitlines():
    assert (ROOT/path).read_bytes()==old(path),path
for path in ['Marysia_PAKIET_ZRODEL_2026-11-05.zip','Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip']:
    assert (ROOT/path).read_bytes()==old(path),path
for sn,prefix,start,col in [('ZRODLA_I_SKANY','S',253,9),('PLIKI_DOWODOWE','F',206,1)]:
    for r in b[sn].values:
        if isinstance(r[0],str) and re.fullmatch(prefix+r'\d+',r[0]) and int(r[0][1:])>=start:
            assert (ROOT/r[col]).is_file(),r[col]
srcids={r[0] for r in b['ZRODLA_I_SKANY'].values}
for r in b['KANDYDACI_I_HOMONIMY'].values:
    if r[0] not in ['C98','C99','C100','C101']:continue
    for s in re.findall(r'\bS\d+\b',r[7]):assert s in srcids,s
    assert r[3] and r[5] and r[8]
scope=json.loads((HERE/'zrodla/zakres_odczytu.json').read_text())
assert scope['new_proven_family_relationships']==0
assert scope['name_columns']['PTG86616']==[[2,247]]
assert scope['name_columns']['25445']==[[5,137]]
contacts=json.loads((HERE/'zrodla/kolumny_manifest.json').read_text())
for group in ['25443','25444','25445','86615','86616']:
    with zipfile.ZipFile(HERE/f'zrodla/kolumny_{group}.zip') as z:
        assert z.testzip() is None
        for rec in [x for x in contacts if x['book']==group]:
            assert hashlib.sha256(z.read(rec['name'])).hexdigest()==rec['sha256']
manifest=[]
for f in sorted((HERE/'zrodla').rglob('*')):
    if not f.is_file():continue
    raw=f.read_bytes()
    if f.suffix in ['.json','.csv','.txt','.html']:
        assert not re.search(rb'X-Amz-|jsonAuth["=]|Bearer |eyJ0eXAi',raw),f
    if f.suffix=='.jpg':
        assert raw.startswith(b'\xff\xd8');Image.open(io.BytesIO(raw)).verify()
    manifest.append(dict(path=str(f.relative_to(HERE)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
(HERE/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report=dict(result='PASS',at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            baseline_commit=BASE,sheets=24,counts=counts,old_cells_changed=changes,
            all_other_old_cells_preserved=True,original_zips_unchanged=True,public_tree_unchanged=True,
            parallel_tomasz_and_roman_preserved=True,new_family_relationships=0,
            source_files=len(manifest),source_bytes=sum(x['bytes'] for x in manifest),
            source_paths_and_new_candidate_references_valid=True,transient_credentials_excluded=True)
(HERE/'WALIDACJA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
