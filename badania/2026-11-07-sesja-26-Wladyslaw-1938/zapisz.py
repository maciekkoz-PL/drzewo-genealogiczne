"""Zapis audytowalny etapu 26; uruchamiać tylko raz na bazie etapu 25."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
from openpyxl import load_workbook

R = Path(__file__).resolve().parents[2]
H = Path(__file__).resolve().parent
Z = H / 'zrodla'
Z.mkdir(exist_ok=True)
X = R / 'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
W = R / 'work/s25'
manifest = json.loads((R / 'badania/2026-11-07-sesja-25-Chojny-1938/katalog/manifest_6209685.json').read_text())
url8 = next(e['src'] for e in manifest['elementy'] if e['pozycja'] == 8)
unit = 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6209685'
shutil.copyfile(W / 'LodzW1938_8.jpg', Z / 'LodzW1938_8.jpg')
now = datetime.now(timezone.utc).isoformat(timespec='seconds')
scope = {
    'odczyt_utc': now,
    'lodz_wyjazdy': {
        'sygnatura': '39/221/0/4.12/25508', 'jednostka_swa': 6209685,
        'zakres_obejrzany': 'obrazy 1–70/184; kolumny nazwisk i liczb osób; obraz 8 pełne rubryki nr 80',
        'url_jednostki': unit, 'oryginaly': [
            {'obraz': i, 'sha256': hashlib.sha256((W / f'LodzW1938_{i}.jpg').read_bytes()).hexdigest()}
            for i in range(1, 71)
        ],
        'uwaga': 'Jedynie obraz 8 jest archiwizowany w repozytorium; przegląd kolumn nie oznacza pełnej transkrypcji wszystkich wpisów. Inne wpisy Chmielewskich nie mają rodzinnego identyfikatora.'
    },
    'chelmonskiego_inwentarz': {
        'sygnatura': '39/221/0/4.4/15575', 'jednostka_swa': 17669762,
        'zakres_obejrzany': 'obrazy 1–12/172; nieruchomości nr 1 i początek nr 3; nie osiągnięto nr 9a',
        'oryginaly': [
            {'obraz': i, 'sha256': hashlib.sha256((W / f'Chelmonskiego_{i}.jpg').read_bytes()).hexdigest()}
            for i in range(1, 13)
        ],
        'uwaga': 'Księga własności, nie automatycznie lista mieszkańców; zbadany zakres nie daje wyniku dla 9a.'
    },
    'chojny_przyjazdy_kontrola': {
        'sygnatura': '39/225/0/4/2137',
        'zakres': 'wtórna celowana kontrola kolumn nazwisk na obrazach 5–22 z archiwum etapu25',
        'wynik': 'Nie odczytano osobnego wpisu Władysława; nr 398 Agnieszki jest na obrazie22. To nie wyklucza niewymienionego członka grupy ani wpisu w innym zakresie.'
    },
    'interpretacja': 'Władysław nr80 i Agnieszka nr398 mają Chełmońskiego9a, kierunek Chojny i 2m+3k. Możliwe jedno gospodarstwo; różne daty i brak imion grupy nie pozwalają stwierdzić relacji, utożsamić z P06 ani znaleźć P11.'
}
(Z / 'zakres_odczytu.json').write_text(json.dumps(scope, ensure_ascii=False, indent=2) + '\n')
file_manifest = [
    {'path': str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
    for p in sorted(Z.iterdir()) if p.is_file()
]
(H / 'manifest.json').write_text(json.dumps(file_manifest, ensure_ascii=False, indent=2) + '\n')
wb = load_workbook(X)
assert wb['ZRODLA_I_SKANY']['A295'].value == 'S292'
assert wb['KANDYDACI_I_HOMONIMY']['A106'].value == 'C103'
assert wb['INDEKS_MELDUNKOW']['A58'].value == 'IM055'
append = lambda sh, row: wb[sh].append(row)
append('ZRODLA_I_SKANY', ['S293', 'Łódź25508/1938, wyjazd Władysława Chmielewskiego nr80', 'SKAN PIERWOTNY / ODCZYT PEŁNY', now, 'Władysław Chmielewski; grupa 2m+3k', 'APŁ / SwA', '39/221/0/4.12/25508; karta5/obraz8/nr80', url8, 'ORYGINAŁ ODCZYTANY', str((Z/'LodzW1938_8.jpg').relative_to(R)), 'Chełmońskiego9a→Chojny, ul. Zamen…13 [niepewny odczyt]; zgłoszenie10I1938, C25II, A21III, skreślenie10I. Brak wieku, imion grupy i relacji rodzinnej. S288 Agnieszka ma zgodny adres/kierunek/liczbę osób, lecz różne daty.'])
append('ZRODLA_I_SKANY', ['S294', 'Łódź25508/1938 — zakres pierwszych70 obrazów', 'SKANY PIERWOTNE / KOLUMNY NAZWISK', now, 'Wybrane imienniki; bez identyfikacji P11', 'APŁ / SwA', '39/221/0/4.12/25508; obrazy1–70/184', unit, 'KOLUMNY NAZWISK; NR80 PEŁNE RUBRYKI', str((Z/'zakres_odczytu.json').relative_to(R)), 'Nie pełna transkrypcja, nie dowód nieobecności rodziny w późniejszych obrazach. Wszystkie70 pobrano i zahaszowano; tylko obraz8 zachowano w repozytorium.'])
append('ZRODLA_I_SKANY', ['S295', 'Łódź15575/1931–1946, inwentarz Chełmońskiego — kontrola początku', 'SKANY PIERWOTNE / CZĘŚCIOWY ODCZYT', now, 'Nieruchomości Chełmońskiego1, początek3', 'APŁ / SwA', '39/221/0/4.4/15575; obrazy1–12/172', 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/17669762', 'OBRAZY1–12; NIE DOTARTO DO9a', str((Z/'zakres_odczytu.json').relative_to(R)), 'Inwentarz zawiera informacje o nieruchomości i właścicielu, nie automatycznie o lokatorach. Dla9a brak wyniku, gdyż zakres nie obejmuje numeru.'])
append('DZIENNIK_KWEREND', ['L293', now, 'Łódź25508/1938, obraz8/karta5/nr80; porównanie z S288', 'Władysław Chmielewski 2m+3k z Chełmońskiego9a do Chojen; zgodny adres/kierunek/liczba z Agnieszką nr398.', 'Daty nie są identyczne; nie podano relacji ani imion domowników. Nie utożsamiać z rodziną P03/P06/P11.', 'S293;S288;C103;C104;H053'])
append('DZIENNIK_KWEREND', ['L294', now, 'Łódź25508/1938 obrazy1–70; Chojny2137/1938 celowana wtórna kontrola obrazów5–22', 'Obejrzano nazwiska; nr80 Władysława najbliższy C103. W Chojnach przed nr398 brak osobnego odczytanego Władysława.', 'Zakres Łodzi tylko70/184; przegląd nazwisk, nie pełnych rubryk. Niewymienieni w grupach pozostają nieznani.', 'S294;S289;S293'])
append('DZIENNIK_KWEREND', ['L295', now, 'Inwentarz Chełmońskiego15575 obrazy1–12/172', 'Widziano formularz nieruchomości nr1 i początek nr3.', 'Nie dotarto do9a; nie interpretować jako negatywnego wyniku mieszkańców.', 'S295'])
append('KANDYDACI_I_HOMONIMY', ['C104', 'Władysław Chmielewski — Chełmońskiego9a', '1938,nr80;karta5/obraz8;2m+3k; zgłoszenie10I, dowódC25II,A21III;bezDOB', 'Możliwe wspólne gospodarstwo zC103, bez ustalonej relacji; nie przypisano doP06/P11', 'Łódź,Chełmońskiego9a→Chojny,ul.Zamen…13 [odczyt niepewny]', 'MOCNY TROP ADRESOWY — RODZINA NIEUDOWODNIONA', 'Ta sama ulica/numer, kierunek i skład liczbowy coS288; różne daty, brak imion pozostałych osób. Może dotyczyć jednej przeprowadzki, lecz nie jest dowodem małżeństwa/ojcostwa.', 'S293;S288;S294', 'Karta ewidencyjna, akty lub inny wpis wymieniający członków grupy i rodziców.', url8])
append('HIPOTEZY_OTWARTE', ['H053', 'Czy C104 Władysław i C103 Agnieszka należeli do jednego gospodarstwa? Czy któreś z nich to P05/P06?', 'S293 nr80: Władysław,2m+3k,Chełmońskiego9a→Chojny. S288 nr398: Agnieszka,2m+3k,z Chełmońskiego9a→Chojny. Zbieżność 3 cech mocna, ale daty zgłoszeń/rejestracji różne; brak wieku, rodowego, imion pozostałych osób i relacji. W księdze przyjazdów obraz5–22 nie odczytano osobnego Władysława. Nie scalić zP05/P06 ani nie ustalaćP11.', 'Indywidualna karta ludności lub akt podający małżonka, dzieci, datę urodzenia, nazwisko rodowe; sprawdzić dalsze obrazy Łódź25508 i zapisy adresu docelowego.', 'OTWARTA — MOCNY TROP GOSPODARSTWA, BEZ POTWIERDZONEGO POKREWIEŃSTWA'])
append('INDEKS_MELDUNKOW', ['IM056', 'S293', '39/221/0/4.12/25508', 8, '80', 'Władysław Chmielewski;2m+3k;Chełmońskiego9a→Chojny,Zamen…13[niepewny adres];zgłoszenie10I1938,C25II,A21III. Zbieżne zS288/C103, ale brak relacji i cech osobowych.', url8, 'Etap26; wszystkie rubryki nr80,karta5;oryginał zachowany'])
for i, path, typ, desc in [
    (427,Z/'LodzW1938_8.jpg','ORYGINALNY SKAN','Obraz8,karta5,nr80,pełna strona'),
    (428,Z/'zakres_odczytu.json','METADANE / OPRACOWANIE','70+12 obrazów; zakresy i SHA256; oryginał8 zachowany'),
    (429,H/'manifest.json','MANIFEST INTEGRALNOŚCI','SHA256 plików etapu26')]:
    append('PLIKI_DOWODOWE', [f'F{i}',str(path.relative_to(R)),typ,'S293;S294;S295',desc,'SHA256 w manifest.json; bez relacji rodzinnej'])
for row in wb['ZADANIA_AGENTA']:
    if row[0].value == 'T58':
        row[5].value = 'AKTYWNE: S293/C104 odnaleziony wyjazd Władysława z Chełmońskiego9a do Chojen (2m+3k), zgodny z C103; H053 bez potwierdzonej relacji. Łódź25508 nazwiska1–70/184; inwentarz15575 obrazy1–12/172.'
        row[8].value = str(row[8].value) + ';S293;S294;S295;H053;badania/2026-11-07-sesja-26-Wladyslaw-1938/PLAN_KONTYNUACJI.md'
wb['ZRODLA_I_SKANY']['A2'] = '295źródeł;25arkuszy. Etap26:Władysław/C104 i Agnieszka/C103 mają Chełmońskiego9a,Chojny,2m+3k; bez udowodnionej relacji.'
wb['KANDYDACI_I_HOMONIMY']['A2'] = '104rekordy. C104 Władysław Chełmońskiego9a; związek z C103 i rodziną P03/P06/P11 nieustalony.'
wb['INDEKS_MELDUNKOW']['A2'] = '56wybranych odczytów; nie pełny indeks ani lista krewnych.'
wb['START']['A2'] = 'Etap26: mocny trop jednego gospodarstwa C103/C104 przy Chełmońskiego9a; brak potwierdzonego pokrewieństwa i imienia P11. Zob. STATUS/PLAN etapu26.'
wb.save(X)
print('Etap26 zapisany:', now, url8)
