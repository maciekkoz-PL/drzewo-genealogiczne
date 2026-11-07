"""Archiwizacja lokalnego odczytu; bez sieci, bez wysyłania skanów."""
from pathlib import Path
import csv, datetime, hashlib, html, io, json, shutil, zipfile
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
Z=HERE/'zrodla';Z.mkdir(exist_ok=True);W=ROOT/'work/s23'
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
m=json.loads((ROOT/'work/s21/Chojny1939_manifest.json').read_text())
urls={e['pozycja']:e['src'] for e in m['elementy']}
shutil.copy2(ROOT/'work/s21/Chojny1939_manifest.json',Z/'manifest_Chojny2140.json')
full=[70,89,118,144,145,180,195];technical=[1,2,3,4,196]
for n in full+technical:
    shutil.copy2(ROOT/f'work/s21/Chojny1939_{n}.jpg',Z/f'Chojny1939_{n}.jpg')
for name in ['Agnieszka_1947.jpg','Marian_1496_1497.jpg','sprawdzenie_nazwisk.jpg']:
    shutil.copy2(W/name,Z/name)
scope=dict(at_utc=now,signature='39/225/0/4/2140',unit_id=15352000,total_images=196,
    name_columns_read=[[5,195]],previous_stage22_name_columns=[[90,115]],
    new_stage24_name_columns=[[5,89],[116,195]],technical_seen=technical,full_selected_this_stage=full,
    selected_name_details_only=[126,173],previous_full_selected=[60,80,90,100,115],
    method='Wzrokowo; wszystkie kolumny nazwisk 5–195, wybrane pełne rubryki. Nie OCR i nie pełna transkrypcja.',
    structure='Stałe wpisy5–117. Czasowe145–195, następnie118–144: obraz195 odsyła do strony166 naobrazie118. Obraz145 zaczyna numerację1. Dokument digitalizacji1: strony115–165i193–199niezapisane,245–250pogniecione.',
    result='Nr1947,AgnieszkaChmielewska,1kobieta,ŁódźNapiórkowskiego112,zgłoszenie29IX1939(znakpowtórzenia daty1941). Zbieżność zS274nr2246/21X1939. Nadal bez wieku,rodowego,rodziców i wcześniejszego adresu wChojnach.',
    limit='Nie wyklucza osób niewymienionych imiennie w grupach; obejrzano dostępne skany, nie wszystkie fizyczne karty. Brak dowodu P11/H017/H018/P06.',new_proven_family_relationships=0)
(Z/'zakres_odczytu.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')
downloads=[]
for n in range(1,197):
    p=ROOT/f'work/s21/Chojny1939_{n}.jpg';raw=p.read_bytes();Image.open(io.BytesIO(raw)).verify()
    downloads.append(dict(image=n,url=urls[n],bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),archived_original=n in full+technical))
(Z/'pobrane_sha256.json').write_text(json.dumps(downloads,ensure_ascii=False,indent=2)+'\n')
with (Z/'zakres_stron.csv').open('w',newline='') as f:
    c=csv.writer(f,lineterminator='\n');c.writerow(['obraz','nazwiska','wybrane_pelne_rubryki','oryginal'])
    for n in range(1,197):c.writerow([n,'ODCZYTANO' if 5<=n<=195 else 'TECHNICZNY','TAK' if n in full else 'NIE',urls[n]])
contacts=[]
with zipfile.ZipFile(Z/'kolumny_Chojny2140.zip','w',compression=zipfile.ZIP_STORED) as z:
    for p in sorted(W.glob('wyjazdy_*_*.jpg')):
        im=Image.open(p).convert('L');b=io.BytesIO();im.save(b,format='JPEG',quality=70,optimize=True)
        raw=b.getvalue();z.writestr(p.name,raw);contacts.append(dict(file=p.name,sha256=hashlib.sha256(raw).hexdigest(),derivative=True))
assert len(contacts)==29,len(contacts)
(Z/'kolumny_manifest.json').write_text(json.dumps(contacts,ensure_ascii=False,indent=2)+'\n')
hits=[dict(zrodlo='S284',sygnatura=scope['signature'],obraz=89,nr_wpisu='1947',
    odczyt_i_granice='Agnieszka Chmielewska; 1 kobieta; Chojny → Łódź, Napiórkowskiego 112; otrzymanie zgłoszenia 29 IX 1939 (ditto po dacie wpisu1941). Mocne dopasowanie do meldunku S274/2246,21X1939: imię,nazwisko,kierunek,adres,liczba osób. Nie podaje wieku,nazwiska rodowego,krewnych ani poprzedniego adresu wChojnach. C102/H052; nie utożsamiono zP06/C99.',
    oryginal=urls[89],pochodzenie='Etap24; pełne rubryki wpisu1947, karta86'),
    dict(zrodlo='S285',sygnatura=scope['signature'],obraz=70,nr_wpisu='1496',
    odczyt_i_granice='Marian Chmielewski; 4 mężczyzn i1kobieta; Chojny → Łódź,Bankowa31; zgłoszenie8VIII1939; C24VIII, A30VIII,skreślenie30VIII1939. Członkowie grupy nienazwani; brak wieku/rodziców/pokrewieństwa. Nie jest potwierdzonym krewnym Marysi; odrębny od1497.',
    oryginal=urls[70],pochodzenie='Etap24; pełne rubryki1496,karta67'),
    dict(zrodlo='S285',sygnatura=scope['signature'],obraz=70,nr_wpisu='1497',
    odczyt_i_granice='Marian Chmielewski; 1mężczyzna; Chojny → Łódź, ulica odczytana roboczo Zgórna10 (niepewne); zgłoszenie8VIII1939. Bez wieku/rodziców/pokrewieństwa; brak podstaw utożsamienia z1496 lubP11.',
    oryginal=urls[70],pochodzenie='Etap24; pełne rubryki1497,karta67')]
(Z/'odczyty_wybrane.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2)+'\n')
rows=json.loads((HERE.parent/'2026-11-07-sesja-23-Chojny-i-indeks/indeks_dane.json').read_text())+hits
with (Z/'indeks_wybranych_wpisow.csv').open('w',newline='') as f:
    c=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');c.writeheader();c.writerows(rows)
(HERE/'indeks_dane.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
cells=''.join('<tr>'+''.join('<td>'+html.escape(str(r[k]))+'</td>' for k in ['zrodlo','sygnatura','obraz','nr_wpisu','odczyt_i_granice'])+'<td><a href="'+html.escape(r['oryginal'],quote=True)+'">Skan</a></td></tr>' for r in rows)
old=(HERE.parent/'2026-11-07-sesja-23-Chojny-i-indeks/INDEKS.html').read_text()
page=old.split('<tbody>')[0].replace('etapów21–23','etapów21–24')+'<tbody>'+cells+'</tbody>'+old.split('</tbody>')[1]
(HERE/'INDEKS.html').write_text(page)
files=[dict(path=str(f.relative_to(ROOT)),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in sorted(Z.iterdir()) if f.is_file()]
(HERE/'manifest.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')
print(dict(source_files=len(files),downloaded=len(downloads),contacts=len(contacts),index_rows=len(rows)))
