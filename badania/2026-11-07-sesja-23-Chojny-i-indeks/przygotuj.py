"""Utrwalenie etapu23; lokalne pliki, bez sieci ani przekazywania skanów."""
from pathlib import Path
from PIL import Image
import csv, datetime, hashlib, html, io, json, shutil, zipfile

ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
W=ROOT/'work/s23'; Z=HERE/'zrodla'; Z.mkdir(exist_ok=True)
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
s=json.loads((W/'scope.json').read_text())
s.update(at_utc=now,signature='39/225/0/4/2139',unit_id=15351999,
    read_method='Wzrokowy przegląd kolumn nazwisk i wybranych pełnych wpisów; nie OCR.',
    limitation='Nie pełna transkrypcja. Nazwiska5–85 i87–196; techniczne4/86. Brzegi1–3/197nieodczytane. Brak trafienia nie wyklucza osoby niewymienionej z imienia w grupie.',
    result='FranciszkaChmielewska,20VII1939,zWidawy,pobytczasowy; TadeuszPoprawka,19VII1939,zTargowej12. Bez rodzinnego łącznika. AgnieszkiC102nie zidentyfikowano.',
    new_proven_family_relationships=0)
(Z/'zakres_odczytu.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
shutil.copy2(W/'Chojny_przybyli1939_manifest.json',Z/'Chojny2139_manifest.json')
for n in sorted(set(s['full_selected']+[4])):
    shutil.copy2(W/f'ChojnyP1939_{n}.jpg',Z/f'ChojnyP1939_{n}.jpg')
for n in ['s23catalog18tail','s23annex26219','s23catalog18','s23annexsearch2']:
    shutil.copy2(W/f'{n}.json',Z/f'{n}.json')
annex=dict(at_utc=now,level='METADANE; NIE ODCZYT ZAŁĄCZNIKA',
    signature='39/221/0/4.12/26219',title='Dokumenty do rejestru mieszkańców m. Łodzi, litery H, I, J, L, Ł, nr 1401-...',
    year=1939,scans=0,url='https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/36520704',
    target='Nr2246/1939,AgnieszkaChmielewska,C102,H052; grupaIIIjakwS267/S269/Q99.',
    limitation='Katalog nie podaje górnej granicy. Dopasowanie robocze roku/grupy/dolnej granicy; zawartość i zachowanie konkretnego załącznika niepotwierdzone. Strona jednostki: portlet niedostępny. Żadnej wiadomości nie wysłano.')
(Z/'aneks_26219.json').write_text(json.dumps(annex,ensure_ascii=False,indent=2)+'\n')
shutil.copy2(W/'tesseract_psm6.txt',Z/'tesseract_psm6.txt')
shutil.copy2(W/'proba_kolumny.png',Z/'proba_OCR_wycinek_pochodny.png')
benchmark=dict(at_utc=now,input='S274,25446,obraz98; znany wpis2246/AgnieszkaChmielewska',
    transformation='Wycinek(100,250,950,2400); oryginał etapu22/zrodla/III_1939_98.jpg',
    command='tesseract proba_kolumny.png tesseract_psm6 --tessdata-dir /workspace/genealogy-tools/tessdata -l pol --psm 6',
    model_url='https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/65727574dfcd264acbb0c3e07860e4e9e9b22185/pol.traineddata',
    model_sha256='c4476cdbc0e33d898d32345122b7be1cbf85ace15f920f06c7714756e1ef79b2',
    result='NIEUDANA PRÓBA; nie odzyskano znanego imienia/nazwiska. Nie używać braku słowa jako wykluczenia strony/osoby.',
    external_test='Wysyłka próbnegoPDFdoFirecrawl/GoogleStorageodrzucona przez automatycznąkontrolęzgody. Nie wysłano pliku; nie ponawiano inną drogą. Wynik zewnętrznegoHTRnie istnieje.')
(Z/'benchmark_OCR.json').write_text(json.dumps(benchmark,ensure_ascii=False,indent=2)+'\n')
der=[]
with zipfile.ZipFile(Z/'kolumny_Chojny2139.zip','w',compression=zipfile.ZIP_STORED) as a:
    for f in sorted(W.glob('kolumny_*.jpg')):
        im=Image.open(f).convert('L');b=io.BytesIO();im.save(b,format='JPEG',quality=70,optimize=True)
        raw=b.getvalue();a.writestr(f.name,raw)
        der.append(dict(file=f.name,sha256=hashlib.sha256(raw).hexdigest(),derivative=True))
(Z/'kolumny_manifest.json').write_text(json.dumps(der,ensure_ascii=False,indent=2)+'\n')
m=json.loads((W/'Chojny_przybyli1939_manifest.json').read_text())
download=[]; urls={e['pozycja']:e['src'] for e in m['elementy']}
with (Z/'zakres_stron.csv').open('w',newline='') as f:
    c=csv.writer(f,lineterminator="\n");c.writerow(['obraz','kolumna_nazwisk','wybrane_pelne_pola','uwagi','oryginal'])
    for n in range(1,198):
        read=any(a<=n<=b for a,b in s['name_columns_read'])
        c.writerow([n,'ODCZYTANO' if read else 'TECHNICZNY' if n in s['technical_seen'] else 'NIE ODCZYTANO',
            'TAK' if n in s['full_selected'] else 'NIE',
            'powtórzona treść' if n in [39,187] else 'pobyt czasowy; nowa numeracja' if n==151 else '',urls[n]])
for e in m['elementy']:
    n=e['pozycja'];f=W/f'ChojnyP1939_{n}.jpg'
    if f.exists():
        raw=f.read_bytes();download.append(dict(image=n,url=e['src'],bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),archived_original=(Z/f.name).exists()))
assert len(download)==193
(Z/'pobrane_sha256.json').write_text(json.dumps(download,ensure_ascii=False,indent=2)+'\n')

# Zestawienie istniejących odczytów, nie nowy dowód ani indeks wszystkich mieszkańców.
rows=[]
def add(source,signature,image_no,entry,description,link,origin):
    rows.append(dict(zrodlo=source,sygnatura=signature,obraz=int(image_no),nr_wpisu=str(entry),odczyt_i_granice=description,oryginal=link,pochodzenie=origin))
base21=ROOT/'badania/2026-11-07-sesja-21-meldunki-Ch/zrodla'
base22=ROOT/'badania/2026-11-07-sesja-22-Napiorkowskiego/zrodla'
for fn,source,sig,manifest in [
    ('transkrypcja_25443.csv','S267','39/221/0/4.12/25443','III_1936_1937_manifest.json'),
    ('trafienia_25445.csv','S273','39/221/0/4.12/25445','III_1938_manifest.json')]:
    links={e['pozycja']:e['src'] for e in json.loads((base21/manifest).read_text())['elementy']}
    for r in csv.DictReader((base21/fn).open()):
        n=int(r['obraz']);desc='; '.join(f'{k}: {v}' for k,v in r.items() if k not in ['obraz','nr','karta'])
        add(source,sig,n,r['nr'],desc,links[n],str((base21/fn).relative_to(ROOT)))
links={e['pozycja']:e['src'] for e in json.loads((base22/'III_1939_manifest.json').read_text())['elementy']}
for r in csv.DictReader((base22/'trafienia_25446.csv').open()):
    n=int(r['obraz']);add('S274','39/221/0/4.12/25446',n,'Patrz odczyt',r['odczyt roboczy i ograniczenia'],links[n],str((base22/'trafienia_25446.csv').relative_to(ROOT)))
for r in s['hits']:
    desc=f"{r['given_name']} {r['surname']}; {r['notice_date']}; poprzednio {r['previous_place']}; {r['male']}m+{r['female']}k. {r['limitation']}"
    add('S282',s['signature'],r['image'],r['entry'],desc,urls[r['image']],'Etap23,wybrane pełne wpisy')
with (Z/'indeks_wybranych_wpisow.csv').open('w',newline='') as f:
    c=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");c.writeheader();c.writerows(rows)
cells=''.join('<tr>'+''.join('<td>'+html.escape(str(r[k]))+'</td>' for k in ['zrodlo','sygnatura','obraz','nr_wpisu','odczyt_i_granice'])+'<td><a href="'+html.escape(r['oryginal'],quote=True)+'">Skan</a></td></tr>' for r in rows)
page='''<!doctype html><html lang="pl"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Wybrane wpisy meldunkowe</title><style>body{font:16px system-ui;margin:24px;max-width:1400px}input{font:inherit;padding:10px;width:min(90%,650px)}table{border-collapse:collapse;margin-top:20px}td,th{padding:10px;border:1px solid #ccc;text-align:left;vertical-align:top}tr[hidden]{display:none}</style><h1>Wybrane wpisy meldunkowe</h1><p>Roboczy indeks trafień z etapów21–23. Zawiera odczyty niepewne, imienników oraz kilka osób w niektórych wierszach. Nie jest pełnym indeksem ksiąg ani listą krewnych. Brak wyniku nie wyklucza osoby.</p><label>Szukaj nazwiska, adresu lub numeru: <input id="q" type="search"></label><p id="count"></p><table><thead><tr><th>Źródło</th><th>Sygnatura</th><th>Obraz</th><th>Nr</th><th>Odczyt i ograniczenia</th><th>Oryginał</th></tr></thead><tbody>'''+cells+'''</tbody></table><script>const q=document.querySelector('#q'),rr=[...document.querySelectorAll('tbody tr')];function norm(s){return s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').replace(/ł/g,'l').toLowerCase()}function run(){let n=0;for(const r of rr){r.hidden=!norm(r.textContent).includes(norm(q.value));if(!r.hidden)n++}document.querySelector('#count').textContent=n+' z '+rr.length+' wierszy'}q.addEventListener('input',run);run()</script></html>'''
(HERE/'INDEKS.html').write_text(page)
(HERE/'indeks_dane.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
files=[]
for f in sorted(Z.iterdir()):
    if f.is_file():files.append(dict(path=str(f.relative_to(ROOT)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(HERE/'manifest.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')
print({'archived_source_files':len(files),'downloaded_originals':len(download),'index_rows':len(rows),'family_links':0})
