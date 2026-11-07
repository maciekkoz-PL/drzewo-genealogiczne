"""Uzupełnienie już wykonanej migracji etapu22: częściowy odczyt nowej księgi."""
from pathlib import Path
import copy,datetime,hashlib,json,shutil,zipfile,re
import openpyxl
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent;W=ROOT/'work/s21'
Z=HERE/'chojny';Z.mkdir(exist_ok=True)
scope=dict(signature='39/225/0/4/2140',unit_id=15352000,manifest_images=196,
    name_columns_read=[[90,115]],orientation_full=[60,80,90,100,115],
    date_checks={'60':'7–10VII1939','80':'31VIII–5IX1939','90':'30IX–2X1939','100':'26–28X1939','115':'19–22XII1939'},
    result='W odczytanych nazwiskach90–115 nie zaobserwowano Chmielewskiej/Chmielewskiego. Nie znaleziono wpisu Agnieszki.',
    limitation='Tylko26obrazów nazwisk; orientacja dat z5obrazów. Nie jest to pełny odczyt wszystkich rubryk/księgi ani wykluczenie osoby. Pozostałe pobrane obrazy nieodczytane.',
    remaining='Przy dalszym przeglądzie pomijać nazwiska90–115; sprawdzić ewentualne zaległe/rejestrowane później wpisy, wcześniejszy zakres i księgę przybyłych2139.')
(Z/'zakres.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')
shutil.copy2(W/'Chojny1939_manifest.json',Z/'manifest_2140.json')
for n in scope['orientation_full']:shutil.copy2(W/f'Chojny1939_{n}.jpg',Z/f'Chojny1939_{n}.jpg')
for f in sorted(W.glob('Chojny_nazwiska_*.jpg')):shutil.copy2(f,Z/f.name)
m=json.loads((W/'Chojny1939_manifest.json').read_text());downloads=[]
for item in m['elementy']:
    f=W/f"Chojny1939_{item['pozycja']}.jpg"
    if f.exists():
        raw=f.read_bytes();downloads.append(dict(image=item['pozycja'],url=item['src'],bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),original_archived=(Z/f.name).exists()))
(Z/'pobrane_sha256.json').write_text(json.dumps(downloads,ensure_ascii=False,indent=2)+'\n')
files=[dict(path=str(f.relative_to(ROOT)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in sorted(Z.iterdir()) if f.is_file()]
assert len(files)==13
(HERE/'manifest_Chojny.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')
w=openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
assert not any(r[0]=='S278' for r in w['ZRODLA_I_SKANY'].values)
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
def add(sn,values):
    s=w[sn];s.append(values)
    for c in s[s.max_row]:c._style=copy.copy(s.cell(s.max_row-1,c.column)._style)
add('ZRODLA_I_SKANY',['S278','Chojny, rejestr opuszczających1939 — częściowy odczyt','ORYGINAŁY I POCHODNE KOLUMN',now,'C102?; P11?','APŁ / Szukaj w Archiwach','39/225/0/4/2140; nazwiska90–115; orientacja60/80/90/100/115','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/15352000','ODCZYT WSKAZANEGO ZAKRESU',str((Z/'zakres.json').relative_to(ROOT)),'Manifest196, pobrano38oryginałów; nazwiska26obrazów90–115 bez zaobserwowanego Chmielewski/Chmielewska. Orientacja dat30IX–22XII1939zbrzegów90/115. Brak wpisu Agnieszki w tym zakresie nie wyklucza jej; nie odczytano całej księgi.'])
for no,scope_,result,limit in [
    (276,'Pozyskanie manifestu Chojen2140','196obrazów; zwykła publiczna nawigacja i API; pobrano38JPEG.','Pobranie to nie odczyt;10pobranych obrazów poza zakresem90–115 i orientacją60/80nieodczytane.'),
    (277,'Chojny2140 — nazwiska90–115 i orientacja dat','Nie zaobserwowano Chmielewskiej/Chmielewskiego w26kolumnach; brak Agnieszki.','Zakres od30IXdo22XII1939 na obejrzanych brzegach. Bez wykluczenia C102; dalsze strony nieprzeczytane.')]:
    add('DZIENNIK_KWEREND',[f'L{no}',now,scope_,result,limit,'S278'])
for i,rec in enumerate(files,312):add('PLIKI_DOWODOWE',[f'F{i}',rec['path'],'ORYGINAŁ / METADANE / POCHODNE KOLUMN','S278','Zakres i granice wchojny/zakres.json; hashwmanifest_Chojny.json.','Kolumny są pochodne; pięć wskazanych skanów jest pełnymi oryginałami.'])
h=next(r for r in w['HIPOTEZY_OTWARTE'] if r[0].value=='H052');h[2].value+=' S278:częściowy przegląd nazwisk Chojen2140,obrazy90–115,bez Agnieszki; nie wyklucza osoby i nie obejmuje całej księgi.'
t=next(r for r in w['ZADANIA_AGENTA'] if r[0].value=='T58');t[5].value='AKTYWNE;S278nazwiskaChojen2140/90–115beztrafienia; pozostałe zakresy i2139nieodczytane'
w['ZRODLA_I_SKANY']['A2']='278 źródeł; etap22:S274–S278. Korelacja adresowa Napiórkowskiego112; częściowa kwerendaChojen bez nowego wpisu osoby.'
w.save(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
counts={sn:sum(isinstance(r[0],str) and bool(re.fullmatch(r'[A-Z]+-?\d+',r[0])) for r in w[sn].values) for sn in w.sheetnames}
(HERE/'LICZNIKI.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print('Pobrano',len(downloads),'oryginałów; zarchiwizowano',len(files),'plików;S278,L276–277,F312–324')
