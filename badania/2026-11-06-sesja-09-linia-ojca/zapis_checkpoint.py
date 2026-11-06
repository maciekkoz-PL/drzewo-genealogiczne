from pathlib import Path
from copy import copy
import json, shutil, hashlib, re, datetime
import openpyxl

root=Path('badania/2026-11-06-sesja-09-linia-ojca')
src=root/'zrodla'
src.mkdir(parents=True,exist_ok=True)
for p in Path('work/s09').rglob('*'):
    if p.is_file() and '_preview' not in p.name and p.name!='checkpoint.py':
        out=src/p.relative_to('work/s09');out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
for folder in ['browser_scan_street_browser_jobs','browser_scan_map_browser_jobs','browser_scan_address_next_jobs','browser_scan_address_refine_jobs','browser_scan_address_property_jobs','browser_scan_map27_jobs','browser_scan_xiv_sample_jobs','swa_jednostka_17670063','swa_jednostka_6209611']:
    p=Path('work')/folder
    if not p.exists():continue
    for f in p.glob('*'):
        if f.suffix in ['.json','.html','.txt'] or (f.suffix=='.body' and f.stat().st_size<600000):
            out=src/'proweniencja'/folder/f.name;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,out)

book=Path('Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
w=openpyxl.load_workbook(book)
def add(sn,row):
    sh=w[sn];assert not any(r[0].value==row[0] for r in sh.iter_rows()),(sn,row[0]);n=sh.max_row+1
    sh.append(row)
    for col in range(1,sh.max_column+1):
        old=sh.cell(n-1,col);new=sh.cell(n,col)
        if old.has_style:new._style=copy(old._style)
        new.alignment=copy(old.alignment)
        if new.hyperlink:new.hyperlink=None
    sh.row_dimensions[n].height=None
    if sh.auto_filter.ref:sh.auto_filter.ref=f'A3:{openpyxl.utils.get_column_letter(sh.max_column)}{n}'

def source(sid,title,typ,people,inst,signature,url,level,path,limit):
    add('ZRODLA_I_SKANY',[sid,title,typ,'2026-11-06 — dostęp/odczyt',people,inst,signature,url,level,str(root/path),limit])

source('S136','Katalog USC Łódź: zakres tomu urodzeń816/1940 i zgonów6/1940','KATALOG / METADANE','C42 — poszukiwanie drugiego zapisu','AP Łódź / Szukaj w Archiwach','39/2736/0/-/816; 39/2736/0/-/6','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/43551161','ODCZYTANO METADANE W PRZEGLĄDARCE','zrodla/browser/cards.json','816: treść29.01–09.03.1940, akty1–600,0skanów wSwA. Nie odczytano aktu urodzenia. Zgony6 są chrześcijańskie,26 żydowskie;277skanów jednostki26 nie dotyczą całego rejestru chrześcijańskiego. Daty treści nie gwarantują daty urodzenia dziecka.')
source('S137','Skorowidze zgonów chrześcijańskich1940cq/cs i pierwszy akt1940ca','SKANY SKOROWIDZÓW / AKT KONTROLNY','C42 poszukiwany; homonimy Chmielewski','AP Łódź / PTG Skanoteka','39/2736/0/-/22; /24; /6; PTG4852; cqSkZ13–17,csSkZ012–014,ca001','https://skanoteka.genealodzy.pl/id4852-sy1940cq','ODCZYTANO OBRAZY W OPISANYM ZAKRESIE','zrodla/death1940','cq: częśćC od początku do przejściaD,01.02–31.08.1940; nie znaleziono niemowlęciaCzesława. cs tylko początek i środekC. Akt1 sporządzono08.02.1940, po parafialnym akcieC42. Brak wpisu nie wyklucza dziecka. Duplikat nie jest niezależną relacją rodzinną.')
source('S138','Dariusz Chmielewski: akt zgonu1896/1940 Łódź','SKAN PIERWOTNY','C58 — wykluczony jako dziecko pary Czesław/Janina','AP Łódź / PTG Skanoteka','39/2736/0/-/10; PTG4852/1940ce/1896-1897.jpg;1896','https://skanoteka.genealodzy.pl/index.php?op=pg&id=4852&sy=1940ce&kt=1&plik=1896-1897.jpg','ODCZYTANO OBRAZ, CZĘŚCIOWO NIEOSTRY','zrodla/death1940/ce_1896-1897_image.jpg','Ojciec Zygmunt, matka Danuta, nie Czesław i Janina. Nazwiska rodowego matki nie rozstrzygnięto. Brak podstaw do innego pokrewieństwa. Nie jest bratem Bogusława przez znanych rodziców.')
source('S139','Napiórkowskiego112: posesja i pieczęć XIV komisariatu','SKANY NIERUCHOMOŚCI','Adres zS126; bez zidentyfikowanej rodziny','AP Łódź / Szukaj w Archiwach','39/221/0/4.4/15874; SwA17670063; pozycje639–641, zwłaszcza640(k.638)','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/17670063','ODCZYTANO WYBRANE OBRAZY, NIE CAŁE706','zrodla/street/napior_640.jpg','Nr112 iXIV potwierdzone pieczęcią z1936; właściciele i budynki, brak listy lokatorów. Nie przypisano adresu rodzinie Bogusława ani właścicieli do drzewa. Manifest706obrazów nie oznacza ich odczytu.')
source('S140','Internet i katalogi: Napiórkowskiego112, komisariatXIV, dalsza ewidencja','KWERENDA / MANIFEST KATALOGOWY','C42; rodzina Chmielewskich — poszukiwanie','Wyszukiwarka; AP Łódź / SwA','39/221/0/4.12/25434; SwA6209611,1934–1935,158obrazów','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6209611','ODPOWIEDZI I MANIFEST; ODCZYT TYLKO WYSZCZEGÓLNIONYCH STRON','zrodla/web','Wyszukiwarka zwraca też ogólne wyniki. Bez potwierdzonego wpisu rodziny. Brak strony przez narzędzie lub HTML212b z kodem200 to nie dowód braku skanu. Własność posesji nie ustala mieszkańców.')
source('S141','Łódź św.Anna: publiczny katalog ksiąg — brak urodzeń1940','KATALOG','C42 — poszukiwanie urodzenia','PTG Metryki','2471d,id454;1940b=M,1940c=Z','https://metryki.genealodzy.pl/id454','ODCZYTANO KATALOG, NIE AKT URODZENIA','zrodla/anna_catalogue.html','W tym publicznym wykazie brak księgiU1940; nie wynika stąd niezachowanie ani nieistnienie aktu.1940b to małżeństwa, nie urodzenia.')
source('S142','Katalog rejestrów przybyłych1936–1939: zespółI, literyA,B,C,E','KATALOG PIERWOTNY','Chmielewski — poszukiwanie rodziny','AP Łódź / SwA','39/221/0/4.12/25435–25438','https://www.szukajwarchiwach.gov.pl/seria?_Seria_cur=11&_Seria_delta=100&_Seria_id_serii=308541&_Seria_nameofjsp=jednostki&_Seria_resetCur=false&p_p_id=Seria&p_p_lifecycle=0&p_p_mode=view&p_p_state=normal','ODCZYTANO TABELĘ KATALOGOWĄ','zrodla/xiv_catalogue/selected.json','Wcześniejszy plan błędnie przypisywał25435–25438 do komisariatuXI. To grupa literowa, nie dowód zameldowania rodziny. Najpierw kontrolować okładkę i rzeczywisty porządek wpisów.')

add('KANDYDACI_I_HOMONIMY',['C58','Dariusz Chmielewski','Zm.31.03.1940 Łódź; ur.luty1938; ojciecZygmunt, matkaDanuta; zgon1896/1940','sprawdzenie dziecka z nowego skorowidza','Łódź','WYKLUCZONY JAKO DZIECKO POSZUKIWANYCH RODZICÓW','S138 wymienia innych oboje rodziców; indeks nie wystarczał, odczytano akt.','S137; S138','Nie szukać dalej jako brata Bogusława. Ewentualne dalsze pokrewieństwo nie zostało ustalone.','https://skanoteka.genealodzy.pl/index.php?op=pg&id=4852&sy=1940ce&kt=1&plik=1896-1897.jpg'])
for row in w['HIPOTEZY_OTWARTE'].iter_rows():
    if row[0].value=='H018':
        row[2].value+=' Etap09: S137 bez drugiego wpisu C42; S139/S069 ustalają Napiórkowskiego112→XIV, nie mieszkańców. S141 nie udostępnia U1940.'
        row[3].value='Ewidencja rodziny: właściwa grupa liter nazwiska po1935; wcześniejXIV. UrodzenieC42 około26.01.1940 nadal nieodczytane. Porównać pełne dane rodziców zS001/S071/S063/S086.'

logs=[
('L108','Katalog1076jednostek ponownie wykorzystany; karty816 i6','Ustalono zakres treści816 i rozdział zgonów chrześcijańskich/żydowskich. WSwA0skanów6, wPTG dostępne obrazy.','Nie odczytano U1940; nie pobrano ponownie277obrazów żydowskich.','S081; S136'),
('L109','USC1940cq: tytuł,SkZ10,13–17; cs012–014; ca000b,001','Cała częśćC pierwopisu: Dariusz1896,Leo2617,Józef3339,Antonina4683. Dariusz odczytany oddzielnie. Akt1 z08.02.1940.','Nie znaleziono C42. cs późniejsza częśćC nieodczytana; nie twierdzić pełnej kontroli obu egzemplarzy ani całego roku.','S137'),
('L110','Zgon Dariusza1896/1940: oryginalny JPG i wycinek','RodziceZygmunt/Danuta, inna para. C58wykluczony w zadanej hipotezie.','Obraz nieostry, nazwisko rodowe matki niepewne; nie zgadywać.','S138'),
('L111','Napiórkowskiego: manifest706; wybrane363,367,600,637,639–641,680; S069ulice27–33','Nr112 znaleziono639–641, pieczęćXIV na640. S069poz27(k25): numeryparzyste92do końcaXIV.','Bez listy lokatorów; próbkowanie innych adresów jedynie do lokalizacji. Nie odczytano706skanów.','S139; S069'),
('L112','Nowe zapytania i katalogiXIV; manifest25434(1934–35)','Zidentyfikowano właściwy komisariat i konkretne księgi. Odpowiedzi oraz błędy zachowane.','Bez nowego łącznika rodzinnego. Późniejsze katalogi grupują nazwiska literami, nie wolno zakładać komisariatu z sąsiedztwa sygnatur.','S140'),
('L113','Katalog publiczny parafiiśw.Anny id454','1940b małżeństwa,1940c zgony; nie udostępniono tam U1940.','Nie oznacza braku aktu w zasobie parafii/USC. Nie wysłano zapytania do instytucji.','S141'),
]
for lid,scope,result,limit,refs in logs:add('DZIENNIK_KWEREND',[lid,'2026-11-06',scope,result,limit,refs])
add('KOREKTY_I_SPRZECZNOSCI',['Q68','ZAKRES KSIĘGI','277skanów39/2736/0/-/26 nie jest zbiorem chrześcijańskich zgonów1940','To zgony żydowskie1–530; chrześcijański tom1–608 ma sygnaturę6.','KATALOG','S081; S136','Nie szukać C42 w niewłaściwej jurysdykcji; parafialny66 nie jest numerem USC.','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/39122528'])
add('KOREKTY_I_SPRZECZNOSCI',['Q69','DOSTĘPNOŚĆ','Brak skanów wSwA nie oznacza braku publicznych obrazów wPTG','Chrześcijański tom6 i skorowidze22/24 dostępne wPTG1940ca/cq/cs. HTTP200/212b to strona techniczna.','ZWERYFIKOWANO','S136; S137','Sprawdzać treść i kanał, nie tylko kod HTTP lub licznik jednego portalu.','https://skanoteka.genealodzy.pl/id4852'])
add('KOREKTY_I_SPRZECZNOSCI',['Q70','SPROSTOWANIE PLANU','25435–25438 nie są opisane jako księgi komisariatuXI','Katalog wskazuje zespółI lit.A,B,C,E, lata1936–1939. Wcześniejsze etapy myliły grupę katalogową z komisariatem.','KATALOG PIERWOTNY','S142','Wybierać według roku i nazwiska, następnie sprawdzić okładkę; nie przenosić automatycznie jurysdykcjiStockiej.','https://www.szukajwarchiwach.gov.pl/seria?_Seria_cur=11&_Seria_delta=100&_Seria_id_serii=308541&_Seria_nameofjsp=jednostki&_Seria_resetCur=false&p_p_id=Seria&p_p_lifecycle=0&p_p_mode=view&p_p_state=normal'])
add('DZIENNIK_KWEREND',['L114','2026-11-06','Pierwotna tabela katalogowa308541, strona11:25435–25438','Potwierdzono grupęI lit.A,B,C,E. Skorygowano wcześniejsze wskazanie komisariatuXI.','Katalog nie jest wpisem osoby. Próba25434: odczytano1–4,80,155–158; kolejność chronologiczna, bez pełnej kwerendy nazwisk. Karta techniczna1 ma25343, okładka i karty3/158 poprawnie25434.','S142; S140'])
for fid,path,typ,refs,desc in [
('F80','zrodla/browser/cards.json','METADANE','S136','Karty816/6; próba karty posesji nieudana'),
('F81','zrodla/death1940','SKANY','S137; S138','Skorowidze, kontrolny akt1, akt1896 i odczyty'),
('F82','zrodla/street/napior_640.jpg','SKAN','S139','Pieczęć posesji112: XIV, k638'),
('F83','zrodla/street/ulice_27.jpg','SKAN','S069','Skorowidz1932 k25; Napiórkowskiego92do końcaXIV'),
('F84','zrodla/street/napior_manifest.json','MANIFEST','S139','706metadanych; obrazy tylko wybrane'),
('F85','zrodla/web','KWERENDY','S140','Dokładne zapytania, wyniki i próby dostępu'),
('F86','zrodla/anna_catalogue.html','KATALOG','S141','Brak publicznej pozycjiU1940'),
('F87','zrodla/xiv_catalogue/selected.json','KATALOG','S142','Wybór25435–25439 z zachowaniem pełnegoHTML'),
]:add('PLIKI_DOWODOWE',[fid,str(root/path),typ,refs,desc,'Zapisano, SHA256 w manifeście etapu09'])
w['ZRODLA_I_SKANY']['A2']='142 źródła. Etap09: S136–S142 — dalsze poszukiwania linii ojca; brak nowej potwierdzonej relacji. S135 i aktualizacje linii matki zachowane.'
w['KANDYDACI_I_HOMONIMY']['A2']='58 pozycji kandydatów/aliasów. C58Dariusz: odczytani inni rodzice; C42 pozostaje hipotezą.'
w.save(book)

manifest=[]
for p in sorted(src.rglob('*')):
    if p.is_file():
        b=p.read_bytes();manifest.append({'path':str(p),'size':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(root/'manifest_zrodel_sesji.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Zapisano etap09',len(manifest),'plików')
