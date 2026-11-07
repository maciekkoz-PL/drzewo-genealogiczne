from pathlib import Path
from copy import copy
from datetime import datetime, timezone
import hashlib
import json
from openpyxl import load_workbook

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
SRC = BASE / 'zrodla'
BOOK = ROOT / 'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
NOW = datetime.now(timezone.utc).isoformat(timespec='seconds')
sent = json.loads((SRC / 'mail_2026-11-07_wyslany.json').read_text())
old = json.loads((SRC / 'mail_2026-11-04_wyslany.json').read_text())
assert sent['id'] == '1a1b439e5f868475' and 'SENT' in sent['labels']
assert sent['to'] == ['ckzarzew@zzm.lodz.pl'] and not sent['cc'] and not sent['bcc']
assert 'SENT' in old['labels'] and sent['thread_id'] == old['thread_id']
w = load_workbook(BOOK)
before = {s.title: [[c.value for c in row] for row in s] for s in w}
assert w['ZRODLA_I_SKANY'].cell(w['ZRODLA_I_SKANY'].max_row, 1).value == 'S264'

def append(sn, vals):
    s = w[sn]
    nr = s.max_row + 1
    for n, val in enumerate(vals, 1):
        c = s.cell(nr, n, val)
        c._style = copy(s.cell(nr - 1, n)._style)
    s.row_dimensions[nr].height = s.row_dimensions[nr - 1].height

def row(sn, ident):
    return next(n for n in range(1, w[sn].max_row + 1) if w[sn].cell(n, 1).value == ident)

allowed = set()
def change(sn, nr, col, val):
    allowed.add((sn, nr, col))
    w[sn].cell(nr, col).value = val

contact_url = 'https://www.cmentarzekomunalne.lodz.systkom.pl/kontakt.html'
append('ZRODLA_I_SKANY', ('S265', 'Oficjalny aktualny kontakt administracji Zarzewa', 'STRONA ADMINISTRATORA', NOW, 'C10; C11 — korespondencja', 'Cmentarze Komunalne Łódź', 'Zarzew, Przybyszewskiego 325', contact_url, 'ODCZYTANO OFICJALNY KONTAKT', str((SRC / 'kontakt.html').relative_to(ROOT)), 'ckzarzew@zzm.lodz.pl, 42 628 72 47. Zwykły odczyt strony www; adres nie pochodzi z agregatora.'))
append('ZRODLA_I_SKANY', ('S266', 'Gmail — wcześniejszy list i wysłane uzupełnienie do Zarzewa', 'KORESPONDENCJA WYCHODZĄCA / ODCZYT PO WYSŁANIU', sent['email_ts'], 'C10; C11; P03?; P11?', 'Gmail / administracja Zarzewa', sent['id'] + '; thread ' + sent['thread_id'], sent['display_url'], 'WYSŁANO I ODCZYTANO PONOWNIE: SENT', str((SRC / 'mail_2026-11-07_wyslany.json').relative_to(ROOT)), 'M03 faktycznie wysłano 04.11; Q98 koryguje dawny opis. Dziś wysłano M10 na polecenie użytkownika. M07 pozostał szkicem. Brak nowego potwierdzenia genealogicznego; brak odpowiedzi w odczytanym wcześniejszym wątku.'))
for ident, filename, sid, description in [('F218', 'kontakt.html', 'S265', 'Oficjalny adres administracji'), ('F219', 'mail_2026-11-04_wyslany.json', 'S266', 'Odczyt wcześniejszej wysyłki M03'), ('F220', 'mail_2026-11-07_wyslany.json', 'S266', 'Odczyt po wysłaniu M10; etykieta SENT')]:
    append('PLIKI_DOWODOWE', (ident, str((SRC / filename).relative_to(ROOT)), 'KOPIA / POTWIERDZENIE', sid, description, 'SHA256 w manifest_zrodel.json'))
append('DZIENNIK_KWEREND', ('L255', NOW, 'Weryfikacja oficjalnego adresu Zarzewa', 'Potwierdzono ckzarzew@zzm.lodz.pl na stronie administratora.', 'Adres do konkretnej kwerendy; nie nowe dane osoby.', 'S265'))
append('DZIENNIK_KWEREND', ('L256', NOW, 'Wysłanie jednego uzupełnienia w istniejącym wątku Zarzewa', 'Na bieżące polecenie użytkownika wysłano M10; odczyt po wysyłce potwierdza SENT i odbiorcę. Ustalono też wcześniejszą wysyłkę M03, Q98.', 'Bez odpowiedzi administracji nie ustalono urodzeń ani pokrewieństwa. Bez zamawiania płatnej usługi.', 'S266'))
append('KOREKTY_I_SPRZECZNOSCI', ('Q98', 'KOREKTA STATUSU KORESPONDENCJI', 'M03 oznaczony jako SZKIC – NIE WYSŁANO.', 'Odczyt Gmail potwierdza SENT 04.11.2026 22:02:22 UTC. Dzisiejsze M10 jest uzupełnieniem w tym samym wątku.', 'POTWIERDZONE ODCZYTEM GMAIL', 'S266', 'Nie wysyłać ponownie M03 ani zastąpionego szkicu M07; odróżniać szkic od rzeczywistej wysyłki.', old['display_url']))
append('SZKICE_GMAIL', ('M10', 'Zarzew — uzupełnienie wątku o Czesława i Witolda', 'ckzarzew@zzm.lodz.pl', 'Urodzenie, rodzice, zapis pokrewieństwa i istniejące zdjęcie', 'WYSŁANO 07.11.2026 — POTWIERDZONO SENT', sent['display_url'], 'Bieżące polecenie użytkownika; odpowiedź do wiadomości M03 z 04.11. M07 nie wysłano. S266.'))
sn = 'SZKICE_GMAIL'
change(sn, row(sn, 'M03'), 5, 'WYSŁANO 04.11.2026 — POTWIERDZONO W GMAIL 07.11')
change(sn, row(sn, 'M03'), 7, 'Q98: dawny status szkicu był błędny; wysłano 04.11.2026. W tym samym wątku wysłano uzupełnienie M10 dnia 07.11. S266.')
change(sn, row(sn, 'M07'), 5, 'SZKIC NIEWYSŁANY — ZASTĄPIONY UZUPEŁNIENIEM M10')
change(sn, row(sn, 'M07'), 7, 'Pozostaje w Gmail bez zmiany. Nie wysyłać powtórnie; M10 wysłano w istniejącym wątku M03. S266.')
sn = 'KONTAKTY_URZEDOWE'
change(sn, row(sn, 'I03'), 7, 'S046; S265')
change(sn, row(sn, 'I03'), 8, contact_url)
sn = 'ZADANIA_AGENTA'
change(sn, row(sn, 'T14'), 6, 'ZAPYTANIE WYSŁANE — M03 04.11, UZUPEŁNIENIE M10 07.11; OCZEKIWANIE NA ODPOWIEDŹ')
change(sn, row(sn, 'T14'), 9, 'S029; S122; S263; S266; M03; M10')
change(sn, row(sn, 'T51'), 6, 'M10 WYSŁANO 07.11 — OCZEKIWANIE NA DANE; M07 ZASTĄPIONY')
change(sn, row(sn, 'T51'), 8, 'Współpochówek nie dowodzi ojcostwa Piotra; rocznik 1914 niepotwierdzony. Jedno uzupełnienie wysłano na bieżące polecenie użytkownika, bez nowej relacji.')
change(sn, row(sn, 'T51'), 9, 'S029; S122; S263; S266; H005; M10')
sn = 'HIPOTEZY_OTWARTE'
hr = row(sn, 'H005')
change(sn, hr, 3, w[sn].cell(hr, 3).value + ' S266: 07.11 wysłano uzupełnienie do administracji, pytając o urodzenie, rodziców i relację; oczekiwanie na odpowiedź. M03 był już wysłany 04.11; M07 zastąpiony przez M10.')
change('ZRODLA_I_SKANY', 2, 1, '266 źródeł. Zapytanie do Zarzewa wysłane 07.11 jako uzupełnienie wątku z 04.11; brak nowego potwierdzenia rodzinnego.')
change('START', 2, 1, '07.11.2026: Zarzew XXXVI/15/36 — wysłano M10, uzupełnienie wcześniejszego M03 z 04.11. Adres oficjalny; SENT sprawdzono po wysyłce. H005 otwarta, oczekiwanie na odpowiedź. 24 arkusze, 266 źródeł, 256 zapisów kwerend, 220 wpisów plików. Q98 koryguje stary status M03; M07 zastąpiony, nadal niewysłany. Raport badania/2026-11-07-zarzew-mail/STATUS.md.')

changes = []
for sn, rows in before.items():
    for r, vals in enumerate(rows, 1):
        for c, val in enumerate(vals, 1):
            if w[sn].cell(r, c).value != val:
                assert (sn, r, c) in allowed, (sn, r, c)
                changes.append([sn, r, c])
w.save(BOOK)
check = load_workbook(BOOK)
assert check.sheetnames == list(before)
for sn in ['RDZEN_RODZINY', 'RODZINA_Z_RELACJI', 'RELACJE', 'KANDYDACI_I_HOMONIMY', 'ZDARZENIA_I_FAKTY', 'WIARYGODNOSC_OSOB', 'WIARYGODNOSC_RELACJI']:
    assert [[c.value for c in row] for row in check[sn]] == before[sn]
manifest = []
for p in sorted(SRC.iterdir()):
    if p.is_file():
        b = p.read_bytes()
        manifest.append({'path': str(p.relative_to(ROOT)), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()})
(BASE / 'manifest_zrodel.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
result = {'at': NOW, 'sheets': len(check.sheetnames), 'sent_message_id': sent['id'], 'recipient_verified': True, 'sent_label_verified': True, 'modified_old_cells': changes, 'family_sheets_unchanged': True, 'new_sources': 'S265–S266', 'new_logs': 'L255–L256', 'new_files': 'F218–F220', 'new_mail': 'M10', 'correction': 'Q98', 'source_files': len(manifest)}
(BASE / 'WALIDACJA.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps({'verified_sent': sent['id'], 'sources': 266, 'logs': 256, 'files': 220, 'source_files': len(manifest)}, ensure_ascii=False))
