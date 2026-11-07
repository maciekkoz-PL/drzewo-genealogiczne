from pathlib import Path
from copy import copy
from datetime import datetime, timezone
import hashlib
import json
import re
from lxml import html
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
SRC = BASE / 'zrodla'
BOOK = ROOT / 'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
NOW = datetime.now(timezone.utc).isoformat(timespec='seconds')

def rel(path):
    return str(path.relative_to(ROOT))

# This script records an already completed, bounded investigation, not new requests.
q = []
for tag, params in [
    ('results', {'query': 'Tomasz Chmielewski', 'AnnouncementSimpleSearch.RIGHT-01.search': 'szukaj »'}),
    ('tomasz_tresc', {'query': 'Tomasz Chmielewski', 'textSearch': 'true'}),
    ('tomasza_tresc', {'query': 'Tomasza Chmielewskiego', 'textSearch': 'true'}),
    ('nazwisko_2001', {'query': 'Chmielewski', 'startDay': '26', 'startMonth': '3', 'startYear': '2001', 'endDay': '31', 'endMonth': '11', 'endYear': '2001'}),
    ('kontrola', {'query': 'Ryszard Damski'}),
]:
    doc = html.fromstring((SRC / ('wyborcza_' + tag + '.html')).read_bytes())
    forms = doc.xpath('//form[@id="searchCommand"]')
    assert len(forms) == 1
    url = 'https://nekrologi.wyborcza.pl' + forms[0].get('action')
    for el in doc.xpath('//script|//style'):
        el.drop_tree()
    text = doc.text_content()
    result = [s.strip() for s in text.splitlines() if 'znalezion' in s]
    assert result
    q.append({'file': 'wyborcza_' + tag + '.html', 'parameters': params, 'url': url, 'result_messages': result})
q += [
    {'query': 'Chmielewski, bez dat', 'status': 'TIMEOUT przy pageSize=100; nie wynik zerowy'},
    {'file': 'wyborcza_query.html', 'status': 'Początkowy POST bez nazwy przycisku; ogólna strona, nie wynik kwerendy'},
]
(SRC / 'wyborcza_queries.json').write_text(json.dumps({'queries': q, 'limit': 'Nie ustalono kompletności archiwum w 2001 r.; boczne promowane ogłoszenia pominięto.'}, ensure_ascii=False, indent=2))

w = load_workbook(BOOK)
before = {s.title: [[c.value for c in row] for row in s] for s in w}
assert len(w.sheetnames) == 24
assert w['ZRODLA_I_SKANY'].cell(w['ZRODLA_I_SKANY'].max_row, 1).value == 'S252'
assert w['DZIENNIK_KWEREND'].cell(w['DZIENNIK_KWEREND'].max_row, 1).value == 'L245'
assert w['PLIKI_DOWODOWE'].cell(w['PLIKI_DOWODOWE'].max_row, 1).value == 'F205'

def append(sheet, values):
    s = w[sheet]
    row = s.max_row + 1
    for col, value in enumerate(values, 1):
        c = s.cell(row, col, value)
        c._style = copy(s.cell(row - 1, col)._style)
        c.alignment = copy(s.cell(row - 1, col).alignment)
    s.row_dimensions[row].height = s.row_dimensions[row - 1].height

sources = [('S253', 'WBP Łódź — trzy właściwe kwerendy pełnotekstowe Tomasza', 'WYNIKI NATYWNEGO FORMULARZA', NOW, 'Biblioteka Cyfrowa WBP w Łodzi', '20 / 0 / 3 obiekty; po jednej stronie', 'https://bc.wbp.lodz.pl/dlibra/results?q=%22Tomasz+Chmielewski%22&action=SimpleSearchAction&type=-6&p=0', 'ODCZYTANO PEŁNE LISTY WYNIKÓW', SRC / 'wbp_queries.json', 'Listy nie są odczytem całych roczników. Sześć wybranych numerów przeczytano w zakresie opisanym w S254–S259; OCR może pomijać nazwiska.')]
readings = {r['edition']: r for r in json.loads((SRC / 'readings.json').read_text())}
specs = [
    ('S254', '64048', 'Dziennik Łódzki 1975 nr 81 — para łyżwiarska', '1975-04-09', 's. 2', 'SKS Społem, Dorota Pela – Tomasz Chmielewski, klasa III. Obraz s. 2 obejrzano. Brak daty urodzenia i rodziców; nie utożsamiono z P09.'),
    ('S255', '51509', 'Dziennik Popularny 1977 nr 77 — para łyżwiarska', '1977-04-06', 's. 2', 'Dorota Pela – Tomasz Chmielewski, juniorzy w Gdańsku. Odczyt kontekstu z warstwy tekstowej. Brak łącznika rodzinnego.'),
    ('S256', '52322', 'Dziennik Popularny 1980 nr 6 — para łyżwiarska', '1980-01-08', 's. 2', 'Dorota Pela – Tomasz Chmielewski, brąz mistrzostw Polski. Odczyt kontekstu z warstwy tekstowej. Brak łącznika rodzinnego.'),
    ('S257', '52606', 'Dziennik Łódzki 1981 nr 8 — para łyżwiarska', '1981-01-12', 's. 8', 'Dorota Pela – Tomasz Chmielewski, piąte miejsce. Odczyt kontekstu z warstwy tekstowej. Nazwisko i klub nie identyfikują P09.'),
    ('S258', '64736', 'Odgłosy 1986 nr 2 — historyczny lekarz ZWZ', '1986-01-11', 's. 5', 'Dr Tomasz Chmielewski, naczelny lekarz łódzkiego ZWZ pod koniec 1940 r. Obejrzano obraz s. 5. Wykluczony jako urodzony w 1970/1971 P09; brak relacji z rodziną.'),
    ('S259', '75962', 'Nowy Łowiczanin 2001 nr 35 — sędzia po dacie śmierci P09', '2001-08-30', 's. 31–32', 'Sędzia Tomasz Chmielewski, mecz Pelikan–Legionovia, Łowicz 26.08.2001. Obejrzano obrazy s. 31–32. Aktywność po 26.04.2001 wyklucza P09 przy zgodności przekazu REL-018.'),
]
for sid, ed, title, date, pages, limits in specs:
    r = readings[ed]
    sources.append((sid, title, 'SKAN PRASY / WARSTWA TEKSTOWA', date, 'WBP Łódź', 'edycja ' + ed + '; ' + pages, r['pdf_url'], 'PRZESZUKANO TEKST; ODCZYTANO TRAFIENIA', SRC / (ed + '.pdf'), limits))
sources += [
    ('S260', 'Nekrologi Wyborczej — natywny formularz i kontrola dodatnia', 'FORMULARZ WYSZUKIWANIA', NOW, 'nekrologi.wyborcza.pl', '4 kwerendy docelowe; kontrola 2 nekrologi; 1 timeout', q[0]['url'], 'POPRAWNE PARAMETRY I ODCZYT KOMUNIKATÓW', SRC / 'wyborcza_queries.json', 'Brak wyników czterech kwerend; kontrola Ryszard Damski daje 2. Nie ustalono pokrycia 2001; timeout samego nazwiska nie jest zerem. Pierwszy niewłaściwy POST pominięty.'),
    ('S261', 'Tomasz — sześć pomocniczych kwerend prasowych i sportowych', 'WYNIKI WYSZUKIWARKI', NOW, 'Firecrawl / wyszukiwarki', '6 zapytań; odpowiedzi web_search_0…5.json', 'https://bc.wbp.lodz.pl/', 'ODCZYTANO WYNIKI; PIERWOTNA PRASA OSOBNO', SRC / 'web_search_0.json', 'Nie znaleziono źródła z rodzicami, DOB lub adresem P09. Wtórne wyniki sportowe nie rozstrzygają tożsamości. Kopie PDF odczytano osobno w S254–S259.'),
]
assert len(sources) == 9
for n, (sid, title, typ, date, institution, signature, url, check, path, limits) in enumerate(sources, 206):
    assert path.exists()
    append('ZRODLA_I_SKANY', (sid, title, typ, date, 'P09 — kwerenda; brak identyfikacji imienników', institution, signature, url, check, rel(path), limits))
    append('PLIKI_DOWODOWE', ('F' + str(n), rel(path), typ, sid, title, 'SHA256 w manifest_zrodel.json'))

logs = [
    ('L246', 'WBP — trzy pełne listy wyników', '20 / 0 / 3 obiekty, po jednej stronie; zapisano parametry i metadane.', 'Pokrycie OCR nie jest kompletem prasy.', 'S253'),
    ('L247', 'WBP — cztery numery 1975–1981 z parą łyżwiarską', 'Tomasz Chmielewski występuje z Dorotą Pelą; brak urodzenia, rodziców i adresu.', 'Nie utożsamiono sportowca z P09.', 'S254; S255; S256; S257'),
    ('L248', 'Odgłosy 1986 — kontekst historyczny', 'Lekarz ZWZ z 1940 r.; wykluczony jako P09.', 'Nie utworzono relacji z rodziną.', 'S258'),
    ('L249', 'Nowy Łowiczanin 2001 — data wydarzenia, nie tylko publikacji', 'Sędziowanie 26.08.2001, po śmierci P09. Odczyt i kontrola obrazu.', 'Wykluczenie dotyczy konkretnego sędziego i przyjętej daty REL-018.', 'S259'),
    ('L250', 'Nekrologi Wyborczej — właściwe wyszukiwanie', '4 kwerendy bez wyników, dodatnia kontrola 2; odrębna szeroka próba timeout.', 'Nie ustalono kompletności archiwum 2001. Boczna kolumna nie jest wynikiem.', 'S260'),
    ('L251', 'Tomasz — dodatkowe wyniki wyszukiwania web', '6 zapytań bez łącznika rodzinnego; źródła pierwotne odczytano osobno.', 'Nie jest to dowód nieistnienia nekrologu lub innych dokumentów.', 'S261'),
]
for lid, scope, result, limit, sids in logs:
    append('DZIENNIK_KWEREND', (lid, NOW, scope, result, limit, sids))
w['ZRODLA_I_SKANY']['A2'] = '261 źródeł. Tomasz: natywne wyszukiwanie prasy, sześć numerów i nekrologi. Brak nowego dokumentu identyfikującego P09.'
hrow = next(r for r in range(1, w['HIPOTEZY_OTWARTE'].max_row + 1) if w['HIPOTEZY_OTWARTE'].cell(r, 1).value == 'H048')
w['HIPOTEZY_OTWARTE'].cell(hrow, 3).value += ' Prasa i nekrologi S253–S261: 6 numerów, tekst 76 stron, bez nowej identyfikacji; sędzia z sierpnia 2001 i lekarz ZWZ 1940 to inne osoby.'

allowed = {('ZRODLA_I_SKANY', 2, 1), ('HIPOTEZY_OTWARTE', hrow, 3)}
changes = []
for sn, rows in before.items():
    for r, row in enumerate(rows, 1):
        for c, val in enumerate(row, 1):
            if w[sn].cell(r, c).value != val:
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
        manifest.append({'path': rel(path), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()})
(BASE / 'manifest_zrodel.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
(BASE / 'WALIDACJA.json').write_text(json.dumps({'at': NOW, 'sheets': len(check.sheetnames), 'new_sources': 'S253–S261', 'new_logs': 'L246–L251', 'new_files': 'F206–F214', 'modified_old_cells': changes, 'family_sheets_unchanged': True, 'manifest_files': len(manifest), 'manifest_bytes': sum(x['bytes'] for x in manifest), 'site_unchanged': True}, ensure_ascii=False, indent=2))
print(json.dumps({'sources': 261, 'logs': 251, 'files': 214, 'verified_old_cell_changes': changes, 'source_files': len(manifest)}, ensure_ascii=False))
