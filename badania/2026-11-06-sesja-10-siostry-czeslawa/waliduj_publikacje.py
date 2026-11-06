"""Sprawdza zgodność audytów Excel/CSV, danych drzewa i kopii HTML."""
from pathlib import Path
import csv, json, re, datetime
import openpyxl

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
audit = ROOT / 'badania/2026-11-06-trzy-poziomy'
w = openpyxl.load_workbook(ROOT / 'Marysia_KOMPLET_BAZA_2026-11-05.xlsx', read_only=True, data_only=True)
norm = lambda v: '' if v is None else str(v)
counts = {}
for sheet, filename in [('WIARYGODNOSC_OSOB', 'AUDYT_OSOB.csv'), ('WIARYGODNOSC_RELACJI', 'AUDYT_RELACJI.csv')]:
    with (audit / filename).open(newline='') as f:
        rows = list(csv.reader(f))
    excel = [[norm(c) for c in row] for row in w[sheet].values]
    assert rows == excel, sheet
    counts[sheet] = len(rows) - 1
d = json.loads((ROOT / 'witryna/wiarygodnosc.json').read_text())
html = (ROOT / 'witryna/public/index.html').read_text()
rendered = json.loads(re.search(r'<script id="family-data" type="application/json">(.*?)</script>', html, re.S).group(1))
for key in ['people', 'edges', 'relations', 'sources']:
    assert d[key] == rendered[key], key
assert len(rendered['news']) == 6
assert len(d['people']) == 47 and len(d['relations']) == 69
people = {p['id']: p for p in d['people']}
assert {'P26', 'P27'} <= people.keys() and not {'C02', 'C04'} & people.keys()
rels = {r['id']: r for r in d['relations']}
for rid in ['R030', 'R031', 'R032', 'R033', 'R034', 'R035']:
    assert rels[rid]['level'] == 1
for rid in ['R007', 'R008']:
    assert rels[rid]['level'] == 2 and rels[rid]['contextInDocumented']
calculated = {}
for level in [1, 2, 3]:
    ids = {p['id'] for p in d['people'] if p['level'] <= level}
    rs = [r for r in d['relations'] if r['a'] in ids and r['b'] in ids and (r['level'] <= level or level == 1 and r.get('contextInDocumented'))]
    calculated[str(level)] = dict(people=len(ids), relations=len(rs), contextual_links=sum(r['level'] > level for r in rs))
assert calculated == json.loads((audit / 'LICZBY.json').read_text())
report = dict(result='PASS', at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), audit_rows=counts, level_counts=calculated, html_matches_json=True, H017_context_preserved=True)
(HERE / 'WALIDACJA_SPOJNOSCI_PUBLIKACJI.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
