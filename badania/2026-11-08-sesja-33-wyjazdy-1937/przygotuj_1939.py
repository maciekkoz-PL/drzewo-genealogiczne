"""Utrwalenie zakończonego ręcznego odczytu; bez sieci i OCR."""
from pathlib import Path
import json, shutil
from przygotuj import archive_book, ROOT, Z

work = ROOT / 'work/s32/25509'
shutil.copy2(ROOT / 'work/s32/25509_manifest.json', Z / '25509_manifest.json')
scope = json.loads((work / 'scope33.json').read_text())
scope.pop('selected_to_read', None)
scope['technical_seen'] = [1, 2, 3, 5, 186, 187]
scope['full_selected'] = [4,13,18,22,39,43,68,74,115,117,119,123,133,151,157,162,165,179,183,185]
scope['full_selected_definition'] = 'Wybrane wiersze lub nagłówki/granice księgi, nie pełna transkrypcja wszystkich pól tych obrazów.'
scope['numbering_note'] = '187 pozycji manifestu, 181 obrazów z wpisami (4 i 6–185), 6 technicznych. Obraz5 jest dodatkową kartą tytułową, nie wpisami. 184 w karcie digitalizacji nie jest liczbą obrazów w manifeście. Puste strony182–201 opuszczono; jest201a. Ostatnie wpisy na obrazie185 mają zgłoszenie1XII1939; nie zakładać pokrycia całego grudnia.'
scope['recorded_date_boundary'] = 'Na początku zgłoszenia2I1939, na końcu1XII1939. Daty zgonów i późniejszych adnotacji mogą być inne.'
scope['result'] = 'Nowy zapis3693: Chmielewska, Stanisława i Zygm., 1m+1k, Grabowa4→Łask/Buczek, zgłoszenie6XI1939. Mocno odpowiada IM025/nr708 z tej samej ulicy/gminy/składu, lecz brak wieku i relacji. Nie ustalono P11 ani nowego pokrewieństwa. Nie rozpoznano nowego wpisu Czesława, Janiny lub Agnieszki Chmielewskich.'
data = [
 [13,'199','9','Chmielewski','Władysław','19I1939','M.Zamenhofa21','—','1m','Brak utożsamienia z C104.'],
 [18,'303','14','Chmielewski','Stanisław','30I1939','adres niepewny, końcówka8a','—','1m','Szerszy odczyt: Stanisław i1m, nie Stanisława. Robocza selekcja nazwisk nie była transkrypcją.'],
 [22,'408','18','Chmielewski','Antoni','8II1939','Krzemieniecka10?','Radogoszcz/Żeligowskiego58','3m+1k','Brak imion współdomowników i relacji.'],
 [39,'785','35','Chmielewski','Stanisław','15III1939','adres niepewny','—','1m','Szerszy odczyt wskazuje mężczyznę, nie Stanisławę z Grabowej4.'],
 [43,'881','39','Chmielewski','Roman','24III1939','Barwna1','—','1m','Nie ustalono P12 ani P11.'],
 [68,'1457','64','Chmielewski','Leon','16V1939','Piotrkowska130','—','1m','Nie jest Czesławem lub Bogusławem; brak relacji.'],
 [74,'1595','70','Chmielewski','Wincenty','26V1939','Smakowa5','Nowosolna/Stoki','2m+4k','Nie utożsamiono z P05; brak wieku i krewnych.'],
 [115,'2540','111','Chmielewski','Władysław','4VIII1939','Łuk...?64 (niepewne)','Brzeziny/Ujazd','1m','Nie utożsamiono z C104.'],
 [117,'2594','113','Chmielewski','Franciszek','9VIII1939','Braterska40','Brus, ulica niepewna6','1m+1k','Brak relacji między osobami.'],
 [119,'2639','115','Chmielewska?','Józefa','14VIII1939','Niska8','zmarła12VIII1939','1k','Kontrola: Józefa/1k, nie Józef/1m. Nie tworzyć mężczyzny na podstawie pierwszej selekcji.'],
 [123,'2722','119','Chmielewski','Józef','22VIII1939','Browarna2','Radogoszcz','2m+1k','Nie łączyć z Józefem z S238 ani P11.'],
 [133,'2952','129','Chmielewski','bez imienia (pł. męska)','19IX1939','Zgierska59','zgon31VIII1939? (dzień/miesiąc do kontroli)','1m','Wiek niepodany; nie nazywać automatycznie niemowlęciem. Osoba zmarła przed urodzeniem Piotra nie jest jego ojcem.'],
 [151,'3379','147','Chmielewski','Józef','11X1939','Smocza28','miejscowość niepewna','1m+1k','Bez utożsamienia z2722 lub P11.'],
 [157,'3503','153','Chmielewski','Zygmunt','21X1939','Radwańska60','—','1m','Nie scalać z Zygm. z3693: inny adres, brakDOB.'],
 [162,'3628','158','Chmielewski','Alfons','31X1939','Pomorska18','niepewny odczyt miejscowości','1m+2k','Brak daty urodzenia i imion współdomowników.'],
 [165,'3692','161','Chmielewski','Hipolit','6XI1939','Mikołajewskiej13','zmarł4XI1939','1m','Nie ojciec Piotra; brak relacji z następnym wpisem.'],
 [165,'3693','161','Chmielewska','Stanisława i Zygm.','6XI1939','Grabowa4','pow.Łask/gm.Buczek (wieś niepodana)','1m+1k','S320; mocne dopasowanie IM025/708: odwrotny kierunek, adres i liczebność. Zygm. bez pełnego imienia, wieku i roli. C109/H054, nie P11.'],
 [179,'4005','175','Chmielecki','Jerzy Stanisław','23XI1939','Narutowicza42','—','1m','Kontrola odmiennego nazwiska; nie Chmielewski.'],
 [183,'4097','179','Chmielewski','Zbigniew','30XI1939','Rę...36 (niepewne)','niepewny odczyt','1m','Szerszy odczyt imienia: Zbigniew, nie Włodzimierz. Brak rodzinnego łącznika.']
]
keys = ['image','entry','page','surname','given_name','notice_received','current_address','next_place_or_death','group','note']
archive_book('25509', 'S319', scope, [dict(zip(keys,r)) for r in data])

# Dodatkowo utrwalamy początek wcześniejszej księgi, aby nie sugerować pełnego roku.
p = Z / '25507_zakres.json'
s = json.loads(p.read_text())
s['full_selected'] = sorted(set(s['full_selected']+[5]))
s['recorded_date_boundary'] = 'Obraz5: strona2, nr776, zgłoszenie23III1937; końcówka obrazu147:31XII1937 oraz dopiski wcześniejszych dat. Księga jest kontynuacją1937 po25506, nie samodzielnym pełnym rokiem.'
p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
shutil.copy2(ROOT / 'work/s32/25507/005.jpg', Z / '25507_005.jpg')
