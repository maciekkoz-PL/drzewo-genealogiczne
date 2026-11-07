from pathlib import Path
from copy import copy
from datetime import datetime, timezone
import hashlib
import json
import re
from openpyxl import load_workbook

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
SRC = BASE / 'zrodla'
BOOK = ROOT / 'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
NOW = datetime.now(timezone.utc).isoformat(timespec='seconds')

summary = {
    'checked_at': NOW,
    'municipal_url': 'https://www.cmentarzekomunalne.lodz.systkom.pl/mapa.html?gv=4427&cm=ZARZW',
    'ecmentarze_url': 'https://www.ecmentarze.pl/cmentarz/zarzew-lodz/grave/detail/4760181',
    'plot': 'XXXVI/15/36',
    'persons': [{'name': 'Czesław Chmielewski', 'death': '1981-01-16', 'birth': None}, {'name': 'Witold Chmielewski', 'death': '2003-08-22', 'birth': None}],
    'photos_found': False,
    'ecmentarze_data_origin': 'Zarząd Zieleni Miejskiej w Łodzi, 04.03.2026',
    'limit': 'Kontrola znanego grobu. Publikacja danych partnerskich nie jest niezależnym dowodem pokrewieństwa. Mapa eCmentarzy pokazuje orientacyjnie cmentarz.',
}
(SRC / 'rejestr_grobu.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))
fg = {
    'checked_at': NOW,
    'cards': [
        {'id': 270863680, 'name': 'Witold Chmielewski', 'death': '2003-08-22', 'url': 'https://www.findagrave.com/memorial/270863680/witold-chmielewski'},
        {'id': 270863681, 'name': 'Czesław Chmielewski', 'death': '1981-01-16', 'url': 'https://www.findagrave.com/memorial/270863681/czes%C5%82aw-chmielewski'},
    ],
    'shared_fields': {'birth': 'unknown', 'photos': 0, 'plot': 'Kwatera: XXXVI, Rząd: 15, Grób: 36', 'visible_linked_relatives': [], 'added': '2024-05-31', 'creator': 'woowoo'},
    'search_scope': {'witold': 'Pierwsza strona 20 z 26, potem dokładna karta; nie komplet wszystkich kart.', 'czeslaw': 'Wszystkie 3 wyniki zgonu 1981, jedna strona; potem dokładna karta.'},
    'limit': 'Nie ustalono niezależności od miejskiego wykazu. Ukryte szablony komunikatów edycji i wysyłki w HTML nie oznaczają wykonania działań. Wyłącznie odczyty GET; bez konta i kontaktu.',
}
(SRC / 'findagrave_odczyt.json').write_text(json.dumps(fg, ensure_ascii=False, indent=2))

w = load_workbook(BOOK)
before = {s.title: [[c.value for c in row] for row in s] for s in w}
assert w['ZRODLA_I_SKANY'].cell(w['ZRODLA_I_SKANY'].max_row, 1).value == 'S261'
assert w['DZIENNIK_KWEREND'].cell(w['DZIENNIK_KWEREND'].max_row, 1).value == 'L251'
assert w['PLIKI_DOWODOWE'].cell(w['PLIKI_DOWODOWE'].max_row, 1).value == 'F214'

def append(sheet, values):
    s = w[sheet]
    row = s.max_row + 1
    for col, value in enumerate(values, 1):
        c = s.cell(row, col, value)
        c._style = copy(s.cell(row - 1, col)._style)
        c.alignment = copy(s.cell(row - 1, col).alignment)
    s.row_dimensions[row].height = s.row_dimensions[row - 1].height

rows = [
    ('S262', 'Zarzew XXXVI/15/36 — kontrola rejestru i pochodzenia danych', 'REJESTR MIEJSKI / PARTNERSKI', 'Cmentarze Komunalne Łódź / eCmentarze', 'gv4427; ecmentarze4760181', summary['municipal_url'], 'rejestr_grobu.json', 'Czesław 16.01.1981 i Witold 22.08.2003 razem; obaj bez daty urodzenia. Brak zdjęcia. eCmentarze publikuje dane ZZM 04.03.2026; nie odrębny dowód genealogiczny. To kontrola S029/S122, nie nowy grób.'),
    ('S263', 'Dokładne karty Czesława i Witolda z Zarzewa w Find a Grave', 'DWIE KARTY REJESTRU WTÓRNEGO', 'Find a Grave', '270863680; 270863681', fg['cards'][0]['url'], 'findagrave_odczyt.json', 'Zgodne daty śmierci i XXXVI/15/36. Obie Birth unknown, Photos 0; brak widocznych relacji. Dodane 31.05.2024 przez tego samego autora. Nie ustalono niezależności od rejestru miasta. Lista Witolda tylko 20/26; dokładną kartę odczytano.'),
    ('S264', 'Czesław / Witold — nowe trzy kwerendy pierwotnego MSiG', 'ODPOWIEDZI NATYWNEJ WYSZUKIWARKI', 'Ministerstwo Sprawiedliwości', 'Witold Chmielewski; Witoldzie Chmielewskim; Czesławie Chmielewskim', 'https://wyszukiwarka-msig.ms.gov.pl/', 'msig_witold.json', 'Trzy puste listy w opisanych okresach; dodatnia kontrola spadku 50 wierszy. Nie dowodzi braku sprawy spadkowej. countPages=100 nie jest liczbą trafień. Brak danych łączących z rodziną.'),
]
for n, (sid, title, typ, inst, sig, url, filename, limits) in enumerate(rows, 215):
    path = SRC / filename
    assert path.exists()
    relative = str(path.relative_to(ROOT))
    append('ZRODLA_I_SKANY', (sid, title, typ, NOW, 'C10; C11; P03?; P11?', inst, sig, url, 'ODCZYTANO; GRANICE W OSTATNIEJ KOLUMNIE', relative, limits))
    append('PLIKI_DOWODOWE', ('F' + str(n), relative, typ, sid, title, 'SHA256 w manifest_zrodel.json'))
    append('DZIENNIK_KWEREND', ('L' + str(n + 37), NOW, title, limits, 'H005 nadal otwarta; bez nowej osoby, daty urodzenia lub relacji.', sid))

w['ZRODLA_I_SKANY']['A2'] = '264 źródła. Nowe odczyty prasy Tomasza i dokładnych kart pary z Zarzewa; nie uzyskano nowego łącznika rodzinnego.'
w['START']['A2'] = '07.11.2026: po kwerendzie Tomasza bieżący trop Czesław i Witold, Zarzew XXXVI/15/36, jako możliwi ojciec i brat Bogusława. 24 arkusze, 264 źródła, 254 zapisy kwerend, 217 wpisów plików. Find a Grave: dokładne karty bez urodzenia i zdjęć. H005 otwarta. Raport badania/2026-11-07-zarzew/STATUS.md; wcześniejsza prasa Tomasza w badania/2026-11-07-tomasz-prasa/. Bez kontaktów i opłat.'
hr = next(r for r in range(1, w['HIPOTEZY_OTWARTE'].max_row + 1) if w['HIPOTEZY_OTWARTE'].cell(r, 1).value == 'H005')
w['HIPOTEZY_OTWARTE'].cell(hr, 3).value += ' S262–S264: dokładne karty Find a Grave 270863680/270863681 mają Birth unknown i Photos 0; brak widocznych relacji. eCmentarze to dane partnerskie ZZM, nie niezależny dowód. 3 nowe kwerendy MSiG puste przy dodatniej kontroli.'
w['HIPOTEZY_OTWARTE'].cell(hr, 4).value = 'Zdjęcie wszystkich inskrypcji konkretnego grobu XXXVI/15/36 lub wpis księgi pochowanych. C10 porównać z urodzeniem P03 03.07.1909 i rodzicami Wincenty/Agnieszka. C11: rodzice i rodzinny łącznik z Bogusławem; ojcostwo Piotra sprawdzać osobno. M07 już istnieje, niewysłany. Nie przypisywać rocznika 1914 z agregatu.'

allowed = {('ZRODLA_I_SKANY', 2, 1), ('START', 2, 1), ('HIPOTEZY_OTWARTE', hr, 3), ('HIPOTEZY_OTWARTE', hr, 4)}
changes = []
for sn, old_rows in before.items():
    for r, row in enumerate(old_rows, 1):
        for c, value in enumerate(row, 1):
            if w[sn].cell(r, c).value != value:
                assert (sn, r, c) in allowed, (sn, r, c)
                changes.append([sn, r, c])
for sn, prefix in [('ZRODLA_I_SKANY', 'S'), ('DZIENNIK_KWEREND', 'L'), ('PLIKI_DOWODOWE', 'F')]:
    ids = [r[0] for r in w[sn].values if isinstance(r[0], str) and re.fullmatch(prefix + r'\d+', r[0])]
    assert len(ids) == len(set(ids))
w.save(BOOK)
check = load_workbook(BOOK)
assert check.sheetnames == list(before)
for sn in ['RDZEN_RODZINY', 'RODZINA_Z_RELACJI', 'RELACJE', 'KANDYDACI_I_HOMONIMY', 'ZDARZENIA_I_FAKTY', 'WIARYGODNOSC_OSOB', 'WIARYGODNOSC_RELACJI']:
    assert [[c.value for c in row] for row in check[sn]] == before[sn], sn
manifest = []
for path in sorted(SRC.iterdir()):
    if path.is_file():
        b = path.read_bytes()
        manifest.append({'path': str(path.relative_to(ROOT)), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()})
(BASE / 'manifest_zrodel.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
result = {'at': NOW, 'sheets': len(check.sheetnames), 'new_sources': 'S262–S264', 'new_logs': 'L252–L254', 'new_files': 'F215–F217', 'modified_old_cells': changes, 'family_sheets_unchanged': True, 'source_files': len(manifest), 'source_bytes': sum(x['bytes'] for x in manifest), 'site_unchanged': True}
(BASE / 'WALIDACJA.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps(result, ensure_ascii=False))
