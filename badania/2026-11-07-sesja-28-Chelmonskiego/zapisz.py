"""Jednorazowy zapis negatywnej kontroli inwentarza Chełmońskiego 9a."""
from datetime import datetime, timezone
from pathlib import Path
from openpyxl import load_workbook

root = Path(__file__).resolve().parents[2]
book = root / 'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
wb = load_workbook(book)
assert wb['ZRODLA_I_SKANY']['A302'].value == 'S299'
assert wb['DZIENNIK_KWEREND']['A303'].value == 'L300'
assert wb['PLIKI_DOWODOWE']['A438'].value == 'F435'
now = datetime.now(timezone.utc).isoformat(timespec='seconds')
report = 'badania/2026-11-07-sesja-28-Chelmonskiego/STATUS.md'
photo = 'badania/2026-11-07-sesja-28-Chelmonskiego/zrodla/Chelmonskiego_3.jpg'
url = 'https://photos.szukajwarchiwach.gov.pl/5cf79db31b685da912c5432260bfa3c21a46caa67c0ccaf3433440b56048868c_max'
wb['ZRODLA_I_SKANY'].append([
    'S300', 'Skorowidz nieruchomości ul. Chełmońskiego, obraz 3',
    'ORYGINAŁ ARCHIWALNY', now, '9;9a bez odsyłacza do strony',
    'AP Łódź / Szukaj w Archiwach', '39/221/0/4.4/15575, obraz 3',
    url, 'ODCZYTANO SKOROWIDZ', photo,
    'Nie jest spisem mieszkańców; brak odsyłacza nie wyklucza zamieszkania pod 9a.'
])
wb['DZIENNIK_KWEREND'].append([
    'L301', now, 'Kontrola skorowidza inwentarza Chełmońskiego 9a i cyfrowych kart adresu',
    'Obraz 3: 9;9a bez numeru strony. Obraz 4: opis nieruchomości, nie lista lokatorów. Nie znaleziono osobnej cyfrowej karty mieszkańców adresu.',
    'Brak nowego imienia lub relacji; H053 i P11 otwarte. Nie wnioskować o nieistnieniu domowników.',
    report + ';S300;H053'
])
wb['PLIKI_DOWODOWE'].append([
    'F436', photo, 'SKAN ORYGINALNY', 'S300;L301',
    'Skorowidz 9;9a, bez wskazanej strony',
    'SHA256 ad521190fa03b11e98512efd99552542c73ab74bec7c0ba866a34ad48e68f41c'
])
wb['START']['A2'] = 'Etap28: inwentarz nieruchomości Chełmońskiego 9a nie ma w skorowidzu wskazanej strony; nie jest spisem domowników. H053/P11 otwarte. Etap27: Łódź25508 sprawdzona po nazwiskach, Grabowa4 skorygowana, rejestry Buczku bez skanów.'
wb.save(book)
