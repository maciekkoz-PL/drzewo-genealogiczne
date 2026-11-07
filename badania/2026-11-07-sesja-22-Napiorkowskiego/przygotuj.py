"""Utrwalenie odczytu etapu 22. Bez sieci i bez zmiany wcześniejszych źródeł."""
from pathlib import Path
from PIL import Image
import csv, datetime, hashlib, io, json, shutil, zipfile

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
W=ROOT/'work/s21'; Z=HERE/'zrodla'
Z.mkdir(exist_ok=True)
scope=json.loads((W/'scope1939.json').read_text())
scope.update(at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    signature='39/221/0/4.12/25446', unit_id=6209623,
    read_limitation='Nazwiska na obrazach 4–124; 5 i 125 techniczne. Szczegóły tylko wybranych wpisów. Nie jest to pełna transkrypcja księgi. Obrazy 1–3 i 126 nieodczytane.',
    new_proven_family_relationships=0,
    new_address_correlation='Agnieszka Chmielewska nr2246/1939, Napiórkowskiego112, ten sam adres co S126. Bez identyfikacji z P06/C99 i bez dowodu pokrewieństwa z C42.')
(Z/'zakres_odczytu.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')
shutil.copy2(W/'III_1939_manifest.json',Z/'III_1939_manifest.json')
for n in scope['full_selected']:
    shutil.copy2(W/f'III_1939_{n}.jpg',Z/f'III_1939_{n}.jpg')
for name in ['III_1936_1937_4.jpg','III_1937_4.jpg','III_1937_73.jpg']:
    shutil.copy2(W/name,Z/name)
shutil.copy2(W/'98_wiersz.jpg',Z/'2246_wycinek_pochodny.jpg')

derivatives=[]
with zipfile.ZipFile(Z/'kolumny_25446.zip','w',compression=zipfile.ZIP_STORED) as a:
    for f in sorted(W.glob('III_1939_nazwiska_*.jpg')):
        im=Image.open(f).convert('L'); b=io.BytesIO(); im.save(b,format='JPEG',quality=80,optimize=True)
        raw=b.getvalue();a.writestr(f.name,raw)
        derivatives.append(dict(file=f.name,sha256=hashlib.sha256(raw).hexdigest(),derivative=True))
(Z/'kolumny_manifest.json').write_text(json.dumps(derivatives,ensure_ascii=False,indent=2)+'\n')
manifest=json.loads((W/'III_1939_manifest.json').read_text())
downloads=[]
for item in manifest['elementy']:
    n=item['pozycja']; f=W/f'III_1939_{n}.jpg'
    if not f.exists():continue
    raw=f.read_bytes()
    downloads.append(dict(image=n,url=item['src'],bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
        archived_original=(Z/f.name).exists(),working_file=str(f.relative_to(ROOT))))
assert len(downloads)==122
(Z/'pobrane_sha256.json').write_text(json.dumps(downloads,ensure_ascii=False,indent=2)+'\n')
with (Z/'trafienia_25446.csv').open('w',newline='') as f:
    c=csv.writer(f);c.writerow(['obraz','odczyt roboczy i ograniczenia'])
    c.writerows(scope['hits'].items())
files=[]
for f in sorted(Z.iterdir()):
    if f.is_file():
        raw=f.read_bytes();files.append(dict(path=str(f.relative_to(ROOT)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
(HERE/'manifest.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')
print(len(files),'plików; pobrane oryginały:',len(downloads))
