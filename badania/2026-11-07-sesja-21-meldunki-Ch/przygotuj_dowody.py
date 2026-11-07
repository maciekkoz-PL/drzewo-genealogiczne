"""Utrwalenie pobranych skanów i dokładnego zakresu etapu 21 (bez sieci)."""
from pathlib import Path
from PIL import Image
import csv, datetime, hashlib, io, json, shutil, zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
Z = HERE / 'zrodla'
W = ROOT / 'work/s21'
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')

def dump(name, data):
    (Z/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

for src, dest in [(W/'III_1938_manifest.json', Z/'III_1938_manifest.json'),
                  (W/'ptg1938/downloads_all.json', Z/'ptg86616_downloads.json')]:
    shutil.copy2(src, dest)

selected = {
    'III_1937': [11,24,40,43,44,53,60,64,68],
    'III_1938': [9,10,12,14,31,32,34,47,60,82,83,89,105,110,123,127,137],
}
for key, nums in selected.items():
    for n in nums:
        shutil.copy2(W/f'{key}_{n}.jpg', Z/f'{key}_{n}.jpg')
for n in [21,76,81,134]:
    shutil.copy2(W/f'ptg/86615_{n:03}.jpg', Z/f'86615_{n:03}.jpg')

books = [
    ('25436', W, 'arrivals1937_nazwiska_*.jpg', None),
    ('25443', W, 'III_1936_1937_nazwiska_*.jpg', (5,202)),
    ('25444', W, 'III_1937_nazwiska_*.jpg', (5,72)),
    ('25445', W, 'III_1938_nazwiska_*.jpg', (5,138)),
    ('86615', W/'ptg', 'nazwiska_*.jpg', (2,185)),
    ('86616', W/'ptg1938', 'nazwiska_*.jpg', (2,247)),
]
contact_manifest = []
for book, parent, pattern, bounds in books:
    files = sorted(parent.glob(pattern))
    if not files:
        continue
    with zipfile.ZipFile(Z/f'kolumny_{book}.zip','w',compression=zipfile.ZIP_STORED) as archive:
        for f in files:
            lo,hi = map(int, f.stem.rsplit('_',2)[-2:])
            if bounds and (lo<bounds[0] or hi>bounds[1]):
                continue
            im = Image.open(f).convert('L')
            out = io.BytesIO(); im.save(out, format='JPEG', quality=80, optimize=True)
            raw = out.getvalue(); archive.writestr(f.name,raw)
            contact_manifest.append(dict(book=book,name=f.name,first=lo,last=hi,
                                         derivative=True,sha256=hashlib.sha256(raw).hexdigest()))
dump('kolumny_manifest.json',contact_manifest)

downloads=[]
for key, sig, manifest in [('III_1936_1937','25443','III_1936_1937_manifest.json'),
                         ('III_1937','25444','III_1937_manifest.json'),
                         ('III_1938','25445','III_1938_manifest.json')]:
    data=json.loads((W/manifest).read_text())
    for item in data['elementy']:
        n=item['pozycja']; f=W/f'{key}_{n}.jpg'
        if f.exists():
            raw=f.read_bytes()
            downloads.append(dict(book=sig,image=n,url=item['src'],local_work=str(f.relative_to(ROOT)),
                                  bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),jpeg=raw.startswith(b'\xff\xd8')))
dump('pobrane_SwA_sha256.json',downloads)
dump('zakres_odczytu.json',dict(at_utc=now,excel_baseline='8bea235',
    name_columns={'25436':[[5,52]],'25443':[[5,202]],'25444':[[5,72]],'25445':[[5,137]],
                  'PTG86615':[[2,185]],'PTG86616':[[2,247]]},
    technical_seen={'25443':[104,203],'25445':[138],'PTG86615':[1,186],'PTG86616':[135]},
    selected_full_fields={'25436':[71],'25443':[26,116,119],'25444':selected['III_1937'],
                          '25445':selected['III_1938'],'PTG86615':[21,76,81,134],'PTG86616':[]},
    limitation='Przegląd kolumn nazwisk nie jest odczytem wszystkich rubryk ani wszystkich aktów. Brak trafienia nie wyklucza rodziny. Nieodczytane obrazy poza zakresami pozostają nieodczytane.',
    new_proven_family_relationships=0))
dump('aneks_26200_26204.json',dict(at_utc=now,read_level='METADANE KATALOGU, NIE ZAWARTOŚĆ TECZEK',
    context='Odczyt listy jednostek serii308541, strona45, w poprzedniej części tej samej sesji. Ponowne otwarcie bezpośrednich stron jednostek: Internal Error; nie uzyskano nowych skanów.',
    units=[dict(signature='39/221/0/4.12/26200',year=1936,group='H,I,J,L,Ł (III; nazwiska Ch w rejestrze)',range=[501,1000],
                entries=[530],scans_in_catalog=0,url='https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/36520475'),
           dict(signature='39/221/0/4.12/26204',year=1936,group='H,I,J,L,Ł (III)',range=[2501,3100],
                entries=[2591,2656],scans_in_catalog=0,url='https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/36520496')],
    limitation='Dopasowanie rocznika, grupy i przedziału numerów wskazuje teczkę do kontroli; nie dowodzi, że konkretny załącznik się zachował lub poda rodziców. Żadnego zapytania nie wysłano.'))

rows=[
 [26,23,530,'Czesław Chmielewski','Stocka 12','3 III 1936','Poprzednia wieś/gmina niepewne; możliwe Łężce / Chrzypsko Wielkie. 1 mężczyzna.','C98 / H049: zgodny adres S001, brak DOB i rodziców.'],
 [116,13,2591,'Agnieszka Chmielewska','Grabowa 20','17 XI 1936','Chrzypsko Wielkie, pow. Międzychód, woj. poznańskie; 2 mężczyzn + 3 kobiety.','C99 / H050: brak wieku, nazwiska panieńskiego i imion towarzyszy.'],
 [119,16,2656,'Czesław Chmielewski','Grabowa 20','20 XI 1936','Gm. Chrzypsko, wieś Łężce; 1 mężczyzna; dopisek o uznaniu pobytu za czasowy.','C100 / H051: nie utożsamiono ze Stocką/P03.'],
 [119,16,'pod 2656','Chmielewski, bez imienia','Grabowa 20','20 XI 1936','1 mężczyzna, od urodzenia; nazwisko/adres powtórzone znakami.','C101: brak daty urodzenia i rodziców. Nie uznano za P11.'],
]
with (Z/'transkrypcja_25443.csv').open('w',newline='') as f:
    cw=csv.writer(f, lineterminator="\n");cw.writerow(['obraz','karta','nr','osoba','adres','data wpisu','odczyt','wniosek i ograniczenie']);cw.writerows(rows)

# Tylko odczytane szczegóły; pozostałe rubryki nie są transkrybowane.
hits=[
 [9,114,'Hipolit Chmielewski','Wólczańska 13','17 I 1938','1 m + 2 k; pow. Brzeziny, gm. Bratoszewice'],
 [10,133,'Roman Czesław Chmielewski','Zagajnikowa 57','17 I 1938','1 m + 2 k; Pabianice, Kościuszki 22; bez DOB'],
 [12,159,'Chmielewski, bez imion','Wólczańska 13','19 I 1938','Pięć kolejnych męskich wpisów od urodzenia; bez podanych relacji'],
 [14,222,'Kazimierz Chmielewski','m. Audryńskiego 8 [odczyt do kontroli]','24 I 1938','Radogoszcz; adres wcześniejszy niepewny'],
 [31,596,'Chmielewska, bez imienia','Limanowskiego 146','12 III 1938','Od urodzenia; 1 kobieta; bez rodziców'],
 [32,618,'Wacław Chmielewski','Źródlana 5','15 III 1938','Kutno; bez DOB'],
 [34,664,'Stanisław Chmielewski','Chłodna 18','19 III 1938','Kalisz; bez DOB'],
 [47,953,'Zdzisław Józef Chmielewski','Przędzalniana 285 [ostatnia cyfra do kontroli]','27 IV 1938','Od urodzenia; bez rodziców'],
 [60,1253,'Ludwik Chmielewski','Zagajnikowa 174','30 V 1938','1 m + 1 k; Długie, Kolszyn [odczyt do kontroli]'],
 [82,1763,'Jan Chmielewski','Polna 19','12 VIII 1938','Od urodzenia; bez rodziców'],
 [83,1784,'Włodzimierz Jan Chmielewski','Gdańska 34','17 VIII 1938','Od urodzenia; bez rodziców'],
 [89,1925,'Zygmunt Chmielewski','[adres do kontroli]','7 IX 1938','1 m + 2 k; Brzeziny / Gałkówek / Andrzejów; brak rodzinnego łącznika'],
 [105,2296,'Lucyna Wanda Chmielewska','Wileńska 7','15 X 1938','Kalisz, Częstochowska 53; bez DOB'],
 [110,2425,'Władysław Chmielowski','Nowo Zarzewska 21','29 X 1938','Inna pisownia; Chojny / Zenit; bez rodzinnego łącznika'],
 [123,2707,'Leokadia Chmielewska','Pomorska 147','26 XI 1938','Pow. konecki / Gowarczów; bez DOB'],
 [127,2805,'Chmielewski, imię niepewne','[adres do kontroli]','8 XII 1938','Pod nim Jerzy Chmielewski od urodzenia; nie określono relacji'],
 [137,3039,'Anna Chmielewska','św. Antoniego 8 [końcówka niepewna]','29 IV 1938 [późny wpis]','Ostrzeszów / Kobyla Góra / Przemysłowa 3; bez DOB'],
]
with (Z/'trafienia_25445.csv').open('w',newline='') as f:
    cw=csv.writer(f, lineterminator="\n");cw.writerow(['obraz','nr','imię i nazwisko','adres','data wpisu','zakres i ograniczenia']);cw.writerows(hits)
dump('kwerendy_web_zapis.json',dict(at_utc=now,queries=[
    dict(query='"Chmielewski" "Łężce"',result='Brak rodzinnego łącznika; dominują geografia, statystyki nazwisk i imiennicy.'),
    dict(query='"Chmielewski" "Chrzypsko" Czesław',result='Brak rodzinnego łącznika. Bibliografia regionalna wymienia Czesława i Dorotę bez identyfikacji z rodziną.')],
    warning='To zapis dwóch ponowionych kontroli geograficznych po utracie niezapisanej odpowiedzi narzędzia. Starszych wyszukiwań etapu21 bez zachowanych odpowiedzi nie liczono jako nowych udokumentowanych kwerend. Nie powtarzać tych ogólnych fraz.',
    direct_unit_open_results={'36520475':'Internal Error','36520496':'Internal Error'},
    no_new_family_link=True))
print('Utrwalono skany, kolumny, zakresy, katalog i transkrypcje:',now)
