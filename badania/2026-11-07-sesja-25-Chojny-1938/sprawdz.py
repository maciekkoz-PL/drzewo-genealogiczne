"""Kontrola dodatków etapu 25 oraz zgodności z poprzednią wersją Git."""
from pathlib import Path
import hashlib, json, subprocess, zipfile, io
import openpyxl
from PIL import Image
R=Path(__file__).resolve().parents[2]
H=Path(__file__).resolve().parent
Z=H/'zrodla'
X=R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
files=sorted([p for p in Z.iterdir() if p.is_file()]+[p for p in (H/'katalog').iterdir() if p.is_file()])
assert len(files)==44,len(files)
m=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in files]
(H/'manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
wb=openpyxl.load_workbook(X)
old=openpyxl.load_workbook(io.BytesIO(subprocess.check_output(['git','show','2c4712670064fc2df94089e63e74494686e96f76:Marysia_KOMPLET_BAZA_2026-11-05.xlsx'],cwd=R)))
assert len(wb.sheetnames)==25 and wb.sheetnames==old.sheetnames
ids={'ZRODLA_I_SKANY':('S',292),'DZIENNIK_KWEREND':('L',292),'PLIKI_DOWODOWE':('F',426),'KANDYDACI_I_HOMONIMY':('C',103),'INDEKS_MELDUNKOW':('IM',55)}
for s,(prefix,n) in ids.items():
 vals=[str(c.value) for row in wb[s].iter_rows(min_row=1) for c in row[:1] if c.value and str(c.value).startswith(prefix) and str(c.value)[len(prefix):].isdigit()]
 assert len(vals)==n and len(vals)==len(set(vals)),(s,len(vals),n)
for s in ['OSOBY_GLOWNE','OSOBY_KREWNI','RELACJE_RODZINNE','ZDARZENIA','RELACJE_USTNE','DOWODY_OSOB','DOWODY_RELACJI']:
 if s in wb:
  assert list(wb[s].values)==list(old[s].values),s
allow={'START':{'A2'},'ZRODLA_I_SKANY':{'A2'},'KANDYDACI_I_HOMONIMY':{'A2'},'INDEKS_MELDUNKOW':{'A2'},'HIPOTEZY_OTWARTE':{'C'+str(next(i for i,row in enumerate(old['HIPOTEZY_OTWARTE'].values,1) if row[0]=='H050')),'C'+str(next(i for i,row in enumerate(old['HIPOTEZY_OTWARTE'].values,1) if row[0]=='H052')),'D'+str(next(i for i,row in enumerate(old['HIPOTEZY_OTWARTE'].values,1) if row[0]=='H052'))},'ZADANIA_AGENTA':set()}
for s in old.sheetnames:
 a,b=old[s],wb[s]
 for row in a:
  for c in row:
   if c.value!=b[c.coordinate].value:
    permitted=c.coordinate in allow.get(s,set())
    if s=='ZADANIA_AGENTA' and a.cell(c.row,1).value=='T58' and c.column in (6,9):permitted=True
    assert permitted,(s,c.coordinate,str(c.value)[:70],str(b[c.coordinate].value)[:70])
assert len(m)==len([r for r in wb['PLIKI_DOWODOWE'].values if str(r[0]).startswith('F')])-382
paths={r[1] for r in wb['PLIKI_DOWODOWE'].values if str(r[0]).startswith('F')}
for v in m:assert v['path'] in paths,v['path']
for y,uid,n in [(1937,15351995,205),(1938,15351997,197)]:
 entries=json.loads((Z/'pobrane_sha256.json').read_text()); subset=[e for e in entries if e['year']==y]
 assert len(subset)==n and len({e['image'] for e in subset})==n
 original={e['image']:e for e in subset}
 for e in subset:
  if e['archived_original']:
   p=Z/f'ChojnyP{y}_{e["image"]}.jpg';b=p.read_bytes()
   assert hashlib.sha256(b).hexdigest()==e['sha256']
   Image.open(io.BytesIO(b)).verify()
 with zipfile.ZipFile(Z/f'kolumny_{y}.zip') as z:
  assert z.testzip() is None
  cm={e['file']:e for e in json.loads((Z/'kolumny_manifest.json').read_text()) if e['year']==y}
  assert sorted(z.namelist())==sorted(cm)
  for f in z.namelist():assert hashlib.sha256(z.read(f)).hexdigest()==cm[f]['sha256']
rows=json.loads((H/'indeks_dane.json').read_text());assert len(rows)==55
oldrows=json.loads((H.parent/'2026-11-07-sesja-24-Chojny-wyjazd/indeks_dane.json').read_text())
assert rows[:47]==oldrows
assert all(f'IM{i:03d}' in {r[0] for r in wb['INDEKS_MELDUNKOW'].values} for i in range(48,56))
assert len(rows)==(H/'INDEKS.html').read_text().count('<tr>')-1
print('PASS: 25 arkuszy, 292 źródła i kwerendy, 426 plików, 103 kandydatów, 55 wpisów; 402 oryginały zweryfikowane, 44 pliki zarejestrowane; starsze dane poza dozwolonymi dopiskami bez zmian.')
