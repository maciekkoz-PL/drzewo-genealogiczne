"""Utrwalenie już odczytanych skanów; bez sieci. Nie jest automatycznym OCR."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil, zipfile
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
Z = HERE / 'zrodla'
Z.mkdir(exist_ok=True)

def archive_book(book, source, scope, rows):
    work = ROOT / 'work/s32' / book
    manifest = json.loads((Z / f'{book}_manifest.json').read_text())
    entries = manifest['elementy']
    urls = {int(x['pozycja']): x['src'] for x in entries}
    assert len(urls) == len(entries)
    downloads = []
    for n in sorted(urls):
        f = work / f'{n:03}.jpg'
        with Image.open(f) as im:
            im.verify()
        downloads.append(dict(image=n, url=urls[n], bytes=f.stat().st_size,
                              sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
    scope.update(at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source=source, downloaded=len(downloads),
        limitation='Przegląd nazwisk i imion, nie pełna transkrypcja. Wybrane wiersze odczytane szerzej. Data kolumny6 to otrzymanie zgłoszenia; nie automatycznie dzień przeprowadzki. Liczba osób nie podaje relacji ani imion współdomowników.',
        new_proven_family_relationships=0)
    selected = sorted(set(scope['full_selected'] + scope['technical_seen']))
    for n in selected:
        shutil.copy2(work / f'{n:03}.jpg', Z / f'{book}_{n:03}.jpg')
    for row in rows:
        row.update(source=source, signature=scope['unit'], url=urls[row['image']],
            limitation='Brak identyfikacji z rodziną Marysi; brak daty urodzenia i danych rodziców w odczytanym wierszu. Odczyty z pytajnikiem pozostają niepewne.')
    (Z / f'{book}_wybrane_odczyty.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    with (Z / f'{book}_wybrane_odczyty.csv').open('w', newline='') as out:
        keys = list(dict.fromkeys(k for r in rows for k in r))
        writer = csv.DictWriter(out, keys, lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)
    (Z / f'{book}_zakres.json').write_text(json.dumps(scope, ensure_ascii=False, indent=2) + '\n')
    (Z / f'{book}_pobrane_sha256.json').write_text(json.dumps(downloads, ensure_ascii=False, indent=2) + '\n')
    with zipfile.ZipFile(Z / f'{book}_kolumny_nazwisk.zip', 'w', compression=zipfile.ZIP_STORED) as out:
        for f in sorted((work / 'contact').glob('*.jpg')):
            out.write(f, f.name)
    with (Z / f'{book}_zakres_stron.csv').open('w', newline='') as out:
        writer = csv.writer(out, lineterminator='\n')
        writer.writerow(['obraz', 'nazwiska_i_imiona', 'wybrane_wiersze_szerzej', 'url'])
        for n in sorted(urls):
            read = any(a <= n <= b for a, b in scope['name_columns_read'])
            writer.writerow([n, 'ODCZYTANO' if read else 'TECHNICZNY' if n in scope['technical_seen'] else 'NIE ODCZYTANO',
                             'TAK' if n in scope['full_selected'] else 'NIE', urls[n]])
    print(dict(book=book, downloaded=len(downloads), names=sum(b-a+1 for a,b in scope['name_columns_read']),
               selected_originals=len(selected), selected_rows=len(rows)))

if __name__ == '__main__':
    work = ROOT / 'work/s32/25507'
    scope = json.loads((work / 'scope33.json').read_text())
    scope['full_selected'] = [5,15,16,25,33,37,40,43,57,63,67,91,92,97,98,118,125,126,127,129,131,139,147]
    scope['full_selected_definition'] = 'Wybrane wiersze lub nagłówki/granice księgi, nie pełna transkrypcja wszystkich pól tych obrazów.'
    scope['recorded_date_boundary'] = 'Obraz5: strona2, nr776, zgłoszenie23III1937; końcówka obrazu147:31XII1937 oraz dopiski wcześniejszych dat. Księga jest kontynuacją1937 po25506, nie samodzielnym pełnym rokiem.'
    scope['result'] = 'Nie rozpoznano nowego wpisu Czesława, Janiny ani Agnieszki Chmielewskich. Nie ustalono imienia P11. Osoby wybrane pozostają niepołączonymi imiennikami, a Chmielnicki/Szymon jest kontrolą odmiennego nazwiska.'
    scope['numbering_note'] = '149 pozycji manifestu. Karta digitalizacji mówi146skanów; manifest zawiera też techniczne plansze. Rozpoznano142obrazy z wpisami i7technicznych. Księga ma dwie paginacje; nie jest to149kart imiennych. Późniejsze dopiski nie zawsze zachowują chronologię.'
    data = [
        [15,'1025','12','Chmielewska?','Stanisława','16IV1937','Piotrkowska209?','—','1k','Końcówka nazwiska i numer domu niepewne.'],
        [16,'1040','13','Chmielewski','Julian Szczepan','17IV1937','Franciszkańska80','—','1m','Nie scalać automatycznie z2130 mimo dwóch zgodnych imion.'],
        [25,'1257','22','Chmielewski','Jerzy','7V1937','Dobra4','Łódź/Radogoszcz/MarysinIII','1m+4k','Brak imion czterech kobiet i relacji.'],
        [33,'1429','30','Chmielewska?','Walentyna','20V1937','6Sierpnia83','—','1k','Końcówka nazwiska niepewna; nie scalać z2905.'],
        [37,'1533','34','Chmielewski','Ignacy','31V1937','ulica niepewna,79','Radogoszcz','1m','Nie jest Czesławem.'],
        [40,'1594','37','Chmielewska?','Danuta','4VI1937','Krzemieniecka5','zmarła3VI1937','1k','Zapis zgonu, nie kierunek podróży; końcówka nazwiska niepewna.'],
        [43,'1669','40','Chmielewska?','Ludwika','10VI1937','Zarzewska8','Skarżysko-Kamienna','1k','Końcówka nazwiska niepewna.'],
        [43,'1671','40','Chmielewska?','Franciszka','10VI1937','Przędzalniana3','—','1k','Końcówka nazwiska niepewna.'],
        [57,'1978','54','Chmielewski','Jan Gabryel','2VII1937','Paderewskiego19','b.a.','1m','Nie ustalono pokrewieństwa.'],
        [63,'2130','60','Chmielewski','Julian Szczepan','12VII1937','Franciszkańska202','b.a.','1m','Nie scalać automatycznie z1040.'],
        [67,'2203','64','Chmielewski','Włodzimierz Bog...','15VII1937','Rzgowska48/50','zmarł14VII1937','1m','Drugie imię niepełne. Nie może być ojcem Piotra urodzonego około1971.'],
        [91,'2759','88','Chmielewska?','Eleonora','6IX1937','Felsztyńskiego22','—','1k','Końcówka nazwiska niepewna.'],
        [92,'2777','89','Chmielewska?','Apolonia','7IX1937','Milionowa13?','zmarła7IX1937','1k','Nazwisko i adres do kontroli.'],
        [92,'2779','89','Chmielewska?','Wiktoryja','8IX1937','BolesławaLimanowskiego114','—','1k','Końcówka nazwiska niepewna.'],
        [97,'2905','94','Chmielewska?','Walentyna','20IX1937','Polna10','Brus/StareRokicie','1k','Nie scalać z1429 bez dodatkowego identyfikatora.'],
        [98,'2922','95','Chmielewski','Ludwik','22IX1937','ul.Dr...6 (niepewne)','Wilno/Długie/...11Listopada18','1m+1k','Odczyt miejscowości/ulicy niepełny; kobieta bez imienia i relacji.'],
        [118,'3350','15 (II)','Chmielewski','Stanisław','26X1937','Napiórkowskiego1','Warszawa,adres niepewny','1m','Numer1, nie112 zC42.'],
        [125,'3528','22 (II)','Chmielewski','Józef','12XI1937','Łagiewnicka46','—','2m+2k','Liczebność nie określa członków rodziny.'],
        [126,'3553','23 (II)','Chmielewska','Stanisława','15XI1937','Bednarska,braknumeru','Gdynia','1k','Nie ustalono pokrewieństwa.'],
        [127,'3570','24 (II)','Chmielewski','Jerzy','16XI1937','Karolewska31','zmarł13XI1937','1m','Nie utożsamiono zJerzym1257. Ten zmarły nie może być ojcem Piotra około1971.'],
        [129,'3603','26 (II)','Chmielewski','Franciszek','18XI1937','ulica niepewna,21','Łódź/Brus','1m','Brak daty urodzenia.'],
        [129,'3623','26 (II)','Chmielnicki','Szymon','20XI1937','Zarzewska44','Warszawa','1m','KONTROLA ODCZYTU: odmienne nazwisko; nie Chmielewski.'],
        [131,'3669','28 (II)','Chmielewska?','Irena','22XI1937','ulica niepewna,24','jak wyżej (bez pewnego odczytu)','2k','Dwie kobiety nie dowodzą relacji matka-córka; końcówka nazwiska niepewna.'],
        [139,'3848','36 (II)','Chmielewski?','Kolman','14XII1937','ulica niepewna,50','b.ad.','1m','Nie jest Czesławem; końcówka nazwiska i adres niepewne.']
    ]
    keys=['image','entry','page','surname','given_name','notice_received','current_address','next_place_or_death','group','note']
    archive_book('25507','S318',scope,[dict(zip(keys,r)) for r in data])
