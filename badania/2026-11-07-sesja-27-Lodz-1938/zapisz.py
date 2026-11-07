"""Jednorazowy zapis etapu 27. Git zachowuje poprzednią wersję skoroszytu."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import shutil
from openpyxl import load_workbook

R = Path(__file__).resolve().parents[2]
D = Path(__file__).resolve().parent
SRC = D / 'zrodla'
SRC.mkdir(exist_ok=True)
manifest = json.loads((R/'badania/2026-11-07-sesja-25-Chojny-1938/katalog/manifest_6209685.json').read_text())
scope = []
for n in range(96,185):
    p = R/f'work/s25/LodzW1938_{n}.jpg'
    assert p.exists(), p
    scope.append({'obraz': n, 'url': manifest['elementy'][n-1]['src'], 'sha256': sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size})
(SRC/'zakres_odczytu_96-184.json').write_text(json.dumps({'jednostka':'39/221/0/4.12/25508','zakres':scope,'uwaga':'Odczytano kolumny nazwisk obrazów 96-182; 183-184 to zakończenie księgi/okładka. Pozostałe oryginały poza 126 są tylko robocze i mogą zostać usunięte po kontroli SHA.'},ensure_ascii=False,indent=2)+'\n')
shutil.copy2(R/'work/s25/LodzW1938_126.jpg', SRC/'LodzW1938_126.jpg')
url = manifest['elementy'][125]['src']
x = R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
w = load_workbook(x)
assert w['ZRODLA_I_SKANY']['A299'].value == 'S296'
assert w['DZIENNIK_KWEREND']['A300'].value == 'L297'
assert w['KOREKTY_I_SPRZECZNOSCI']['A103'].value == 'Q100'
assert w['INDEKS_MELDUNKOW']['A28'].value == 'IM025'
assert 'Grabowa7' in w['INDEKS_MELDUNKOW']['F28'].value
t = datetime.now(timezone.utc).isoformat(timespec='seconds')
base = 'badania/2026-11-07-sesja-27-Lodz-1938/'
w['INDEKS_MELDUNKOW']['F28'] = w['INDEKS_MELDUNKOW']['F28'].value.replace('Grabowa7','Grabowa4')
w['INDEKS_MELDUNKOW']['H28'] = base+'KOREKTA_GRABOWA.md; poprzedni odczyt stage22 zachowany jako historyczny'
w['KOREKTY_I_SPRZECZNOSCI'].append(['Q101','BŁĘDNY NUMER DOMU W ODCZYCIE IM025','Grabowa 7 w starszym indeksie/CSV','Ponowny odczyt S274, obraz31, karta27, nr708: Grabowa 4.','POTWIERDZONE ZE SKANU','S274;IM025','Zmieniono bieżący indeks IM025; historyczny CSV etapu22 zachowany; nie tworzyć związku z C105 wyłącznie po Buczku.',w['INDEKS_MELDUNKOW']['G28'].value])
w['ZRODLA_I_SKANY'].append(['S297','Łódź25508/1938, wyjazd Edwarda Stanisława Chmielewskiego nr2800','SKAN PIERWOTNY / ODCZYT PEŁNY',t,'Edward Stanisław Chmielewski;2m+1k','APŁ / SwA','39/221/0/4.12/25508;karta123/obraz126/nr2800',url,'ORYGINAŁ ODCZYTANY',base+'zrodla/LodzW1938_126.jpg','Grupa 2 mężczyzn+1 kobieta; kierunek Piaseczna 23 (odczyt adresu do kontroli). Brak DOB, relacji i imion pozostałych osób; nie utożsamiać z rodziną P03/P11.'])
w['DZIENNIK_KWEREND'].append(['L298',t,'Łódź25508/1938, obrazy96–184, przegląd nazwisk; pełna kontrola nr2800 z obrazu126','Wiele wpisów Chmielewskich, m.in. Edward Stanisław z grupą2m+1k; brak dokumentu powiązania z P03/P11.','Obrazy183–184 to zakończenie/okładka. Kolumny nazwisk całej jednostki obejrzane; nie każdy wpis transkrybowany w pełni.',base+'STATUS.md;S297'])
w['DZIENNIK_KWEREND'].append(['L299',t,'Ponowny odczyt S274 i porównanie z C105/S296, korytarz Łask/Buczek','Stanisława Chmielewska przybyła z gm.Buczek do Grabowej4 w III1939; Czesław 1938 wyjechał do gm.Buczek.','Zbieżność gminy i nazwiska jest hipotezą, nie dowodem wspólnego gospodarstwa, małżeństwa ani rodzicielstwa.',base+'KOREKTA_GRABOWA.md;H054'])
w['KANDYDACI_I_HOMONIMY'].append(['C106','Edward Stanisław Chmielewski — wyjazd 1938','nr2800;karta123/obraz126;2m+1k;bez daty urodzenia i relacji','Nie utożsamiono z rodziną Bogusława','Łódź→Piaseczna23 [adres docelowy do kontroli]','OSOBNY TROP — BRAK IDENTYFIKACJI','Grupa ma 2m+1k, lecz nie wiadomo, kim byli pozostali; sam rok i nazwisko nie wystarczają.', 'S297','Indywidualna karta ludności lub akt z imionami domowników i rodzicami.',url])
w['HIPOTEZY_OTWARTE'].append(['H054','Czy Stanisława z IM025/S274 i Czesław C105/S296 należeli do jednego gospodarstwa w Buczku?','C105 wyjazd Łódź→Łask/Buczek w 1938, grupa2m+1k. Stanisława z Buczku do Łodzi/Grabowa4 w III1939, grupa1m+1k. Różne daty i wielkości grup, brak imion towarzyszy, wieku, relacji; nie utożsamiać z P03 ani P11.','Karty pobytu/stałe księgi ludności Buczku, adresy w Łodzi, akt podający małżonka i dzieci.','OTWARTA — TYLKO KORYTARZ GEOGRAFICZNY'])
w['INDEKS_MELDUNKOW'].append(['IM058','S297','39/221/0/4.12/25508',126,'2800','Edward Stanisław Chmielewski;2m+1k;wyjazd do Piasecznej23 [odczyt do kontroli]; brak wieku, krewnych, relacji.',url,base+'zrodla/LodzW1938_126.jpg; karta123'])
w['PLIKI_DOWODOWE'].append(['F432',base+'zrodla/LodzW1938_126.jpg','ORYGINAŁ SKANU','S297','APŁ 39/221/0/4.12/25508, obraz126, nr2800','SHA256 w zakresie_odczytu_96-184.json'])
w['PLIKI_DOWODOWE'].append(['F433',base+'zrodla/zakres_odczytu_96-184.json','MANIFEST SHA256','L298','Obrazy96–184/184','Nie transkrybowano wszystkich rubryk'])
w['PLIKI_DOWODOWE'].append(['F434',base+'KOREKTA_GRABOWA.md','KOREKTA ODCZYTU','Q101','S274 Grabowa4 zamiast7','Bieżący indeks poprawiony, stary CSV zachowany'])
w['START']['A2']='Etap27: cała księga Łódź25508 przejrzana w kolumnach nazwisk; C106 Edward Stanisław osobny trop. Q101: Stanisława/S274 Grabowa4, nie7. H054 Buczek otwarta. P11 nadal bez imienia i dowodu.'
w.save(x)
print('Zapisano etap27',url)
