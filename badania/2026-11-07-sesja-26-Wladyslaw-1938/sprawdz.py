"""Walidacja etapu 26 wobec zachowanego stanu Git po etapie 25."""
from pathlib import Path
import hashlib
import io
import json
import subprocess
from openpyxl import load_workbook

R = Path(__file__).resolve().parents[2]
H = Path(__file__).resolve().parent
X = R / 'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
new = load_workbook(X)
old = load_workbook(io.BytesIO(subprocess.check_output(['git', 'show', '2824944:Marysia_KOMPLET_BAZA_2026-11-05.xlsx'], cwd=R)))
assert new.sheetnames == old.sheetnames and len(new.sheetnames) == 25
expected = {'ZRODLA_I_SKANY':('S',296), 'DZIENNIK_KWEREND':('L',296), 'KANDYDACI_I_HOMONIMY':('C',105), 'PLIKI_DOWODOWE':('F',430), 'INDEKS_MELDUNKOW':('IM',57)}
for sheet,(prefix,n) in expected.items():
    ids = [str(r[0]) for r in new[sheet].values if r[0] and str(r[0]).startswith(prefix) and str(r[0])[len(prefix):].isdigit()]
    assert len(ids)==n and len(ids)==len(set(ids)),(sheet,len(ids),n)
for sheet in old.sheetnames:
    for row in old[sheet]:
        for cell in row:
            other = new[sheet][cell.coordinate]
            if cell.value == other.value: continue
            allowed = cell.coordinate=='A2' and sheet in ('START','ZRODLA_I_SKANY','KANDYDACI_I_HOMONIMY','INDEKS_MELDUNKOW')
            allowed |= sheet=='ZADANIA_AGENTA' and old[sheet].cell(cell.row,1).value=='T58' and cell.column in (6,9)
            assert allowed,(sheet,cell.coordinate,cell.value,other.value)
assert [r[0] for r in new['HIPOTEZY_OTWARTE'].values if r[0]=='H053']==['H053']
z = H/'zrodla'
manifest = json.loads((H/'manifest.json').read_text())
assert len(manifest)==3
for e in manifest:
    p=R/e['path'];assert p.stat().st_size==e['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==e['sha256']
scope=json.loads((z/'zakres_odczytu.json').read_text())
assert len(scope['lodz_wyjazdy']['oryginaly'])==95 and len(scope['chelmonskiego_inwentarz']['oryginaly'])==12
assert scope['lodz_wyjazdy']['oryginaly'][7]['sha256']==hashlib.sha256((z/'LodzW1938_8.jpg').read_bytes()).hexdigest()
assert scope['lodz_wyjazdy']['oryginaly'][73]['sha256']==hashlib.sha256((z/'LodzW1938_74.jpg').read_bytes()).hexdigest()
for row in new['PLIKI_DOWODOWE'].values:
    if row[0] in ('F427','F428','F429','F430'):assert (R/row[1]).is_file()
assert new['INDEKS_MELDUNKOW']['A59'].value == 'IM056'
assert new['INDEKS_MELDUNKOW']['A60'].value == 'IM057'
print('PASS: 25 arkuszy; S/L296, C105, F430, IM057, H053; dwa oryginały i manifest zgodne; starsze komórki zachowane poza kontrolowanymi aktualizacjami.')
