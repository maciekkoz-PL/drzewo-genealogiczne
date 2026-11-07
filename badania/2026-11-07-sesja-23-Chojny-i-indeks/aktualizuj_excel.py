"""Jednorazowa migracja z16b2f73; zachowanie wszystkich wcześniejszych rekordów."""
from pathlib import Path
import copy, datetime, json, re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
D=str(HERE.relative_to(ROOT));w=openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
assert not any(r[0]=='S280' for r in w['ZRODLA_I_SKANY'].values),'Migracja już wykonana'
def add(sn,values):
    s=w[sn];s.append(values)
    for c in s[s.max_row]:c._style=copy.copy(s.cell(s.max_row-1,c.column)._style)
def row(sn,id):return next(r for r in w[sn] if r[0].value==id)
for r in [
 ['S280','Próba lokalnego OCR na znanym meldunku Agnieszki','TEST METODY; NIE NOWY DOWÓD GENEALOGICZNY',now,'Brak nowych danych osób','Tesseract / tessdata_fast / skanAPŁS274','25446,obraz98,znanynr2246','https://github.com/tesseract-ocr/tessdata_fast/tree/65727574dfcd264acbb0c3e07860e4e9e9b22185','NIEUDANY ODCZYT AUTOMATYCZNY',D+'/zrodla/benchmark_OCR.json','Polski model/psm6nie odczytał znanej AgnieszkiChmielewskiej. Brak nazwiska wOCRnie wyklucza strony/osoby. Próba zewnętrznegoHTRodrzucona przedwysłaniem pliku; brak wynikuFirecrawl. Kontynuowano lokalny odczyt wzrokowy.'],
 ['S281','Dokumenty meldunkowe1939,teczka26219:nr1401–...','METADANE KATALOGU',now,'C102?;H052','APŁ / SzukajwArchiwach','39/221/0/4.12/26219;1939;0skanów','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/36520704','ODCZYT LISTY JEDNOSTEK; NIE ZAWARTOŚCI',D+'/zrodla/aneks_26219.json','Tytuł:literyH,I,J,L,Ł,grupaIIIjakS267/S269. Dolna granica1401,górna niepodana; teczka możliwa dla2246/1939. Nie dowiedziono zachowania załącznikaAgnieszki; brak nowych dat/rodziców. Strona jednostki portletniedostępny.'],
 ['S282','Chojny2139,przybyli1939:przegląd nazwisk i wybrane pełne wpisy','ORYGINALNE SKANY / ODCZYT WZROKOWY',now,'Nie zidentyfikowano C102 aniP11','APŁ / SzukajwArchiwach','39/225/0/4/2139;SwA15351999;197obrazów','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/15351999','NAZWISKA5–85/87–196;SZCZEGÓŁY WYBRANYCH11',D+'/zrodla/zakres_odczytu.json','Pobrano193oryginały4–196. Przeczytano191kolumn nazwisk(2pary powtórek38/39i186/187);4tytuł/86puste. Obraz172,karta181,nr526:FranciszkaChmielewska,zWidawy,powŁask,20VII1939,pobytczasowy. Obraz76,karta73,nr1707:TadeuszPoprawka,zŁodziTargowa12,19VII1939,2m+1k. Bez wieku/rodziców; nie przypisano rodzinie. Obraz151to początek części pobytówczasowych;196odsyła do strony140. Brzegi1–3/197nieodczytane. Nie jest pełną transkrypcją ani wykluczeniem członków grup niewymienionych imiennie.'],
 ['S283','Przeszukiwalne zestawienie wybranych odczytów meldunkowych','OPRACOWANIE POCHODNE;44WIERSZE',now,'Tropy i imiennicy zS267/S273/S274/S282','Opracowanie lokalne','CSV + HTML + arkuszINDEKS_MELDUNKOW','https://github.com/maciekkoz-PL/drzewo-genealogiczne','SCALENIE WCZEŚNIEJSZYCH ODCZYTÓW',D+'/zrodla/indeks_wybranych_wpisow.csv','Nie nowy dowód, nie niezależne potwierdzenie, nie indeks wszystkich mieszkańców/ksiąg. Część wierszy obejmuje kilka wpisów. Zachowano niepewności; każdy wiersz ma sygnaturę,obraz,linkoryginału i pochodzenie. Brak wyniku wyszukiwania nie jest wykluczeniem osoby.']]:add('ZRODLA_I_SKANY',r)
logs=[
 ('LokalnyOCRznanego wpisuS274/2246','Nie odzyskano znanego imienia i nazwiska; zachowano wynik i hashmodelu.','Nie można użyćOCRdo odrzucania stron. Firecrawl:automatyczna odmowa wysyłki; pliku nie wysłano.','S280'),
 ('Katalog aneksów1939dla2246','Odczytano listę:26217nr1–700,26218nr701–1400,26219nr1401–...;0skanów.','Dopasowanie robocze,brak górnejgranicy; zawartość teczki nieodczytana.','S281'),
 ('Chojny2139/1939:191kolumn nazwisk','Obrazy5–85/87–196przeczytane;11wybranychpełnych. AgnieszkiC102niezidentyfikowano.','Nie pełny odczyt wszystkich rubryk; nazwisko domu/grupy nie wymienia wszystkich członków.1–3/197nieodczytane.','S282'),
 ('Chojny2139:1707i526','TadeuszPoprawka,zTargowej12,2m+1k;FranciszkaChmielewska,zWidawy,pobytczasowy.','Brak daturodzenia/rodziców/łącznikówrodzinnych; nie dopisano kandydatów do drzewa.','S282'),
 ('Cyfrowa tabela odczytów','44wiersze z3ksiągŁodzi iChojen;CSV/HTML/nowyarkuszINDEKS_MELDUNKOW.','Indeks wybranych trafień, nie całej populacji; dawne źródła nie stają się nowymi niezależnymi dowodami.','S283')]
for scope,result,limit,src in logs:
    n=max(int(r[0][1:]) for r in w['DZIENNIK_KWEREND'].values if isinstance(r[0],str) and re.fullmatch(r'L\d+',r[0]))+1
    add('DZIENNIK_KWEREND',[f'L{n}',now,scope,result,limit,src])
c=row('HIPOTEZY_OTWARTE','H052')[2];c.value+=' Etap23:S281teczka26219możliwa dla2246/1939,górna granica niepodana,0skanów. S282Chojny2139nazwiska5–85/87–196bezidentyfikacjiAgnieszki; nie wyklucza niewymienionych członków grup. H052nadalotwarta.'
row('ZADANIA_AGENTA','T58')[5].value='AKTYWNE:2139nazwiska5–85/87–196wykonane(S282);2140pozostaje częściowo90–115(S278). Teczkazałączników26219możliwa(S281),bezskanów/górnejgranicy.'
row('ZADANIA_AGENTA','T58')[8].value='S274;S126;H052;S278;S281;S282;etap23/PLAN_KONTYNUACJI.md'
add('INSTRUKCJA_AGENTA',['G26','ETAP23 — CYFROWY REJESTR ODCZYTÓW',f'Czytaj {D}/STATUS.md iPLAN_KONTYNUACJI.md. LokalnyOCRnie działa na próbie; brakHTRzewnętrznego. ArkuszINDEKS_MELDUNKOWma44wiersze wybranych trafień,nie pełnyindeks. Chojny2139nazwiska5–85/87–196wykonane; nie powtarzać. Brak nowej potwierdzonej relacji.'])
for n,f in enumerate(sorted((HERE/'zrodla').iterdir()),329):
    src='S280' if f.name in ['benchmark_OCR.json','tesseract_psm6.txt','proba_OCR_wycinek_pochodny.png'] else 'S281' if f.name.startswith(('s23','aneks_')) else 'S283' if f.name=='indeks_wybranych_wpisow.csv' else 'S282'
    add('PLIKI_DOWODOWE',[f'F{n}',str(f.relative_to(ROOT)),'SKAN / ODCZYT / METADANE / POCHODNE',src,'Etap23;dokładny zakres wzakres_odczytu.json; hashe wmanifest.json.','Wybrane oryginały;kolumnyZIPiwycinekOCRsą pochodnymi. Brak nowej relacji.'])
ss=w.create_sheet('INDEKS_MELDUNKOW');ss.append(['Wybrane wpisy meldunkowe — nie pełny indeks']);ss.append(['44wiersze; imiennicy/tropy, nie lista krewnych. Odczyty niepewne zachowano. S283to opracowanie.'])
data=json.loads((HERE/'indeks_dane.json').read_text());ss.append(['IDwiersza','Źródło','Sygnatura','Obraz','Nrwpisu','Odczyt i ograniczenia','URLoryginału','Pochodzenie odczytu'])
for n,r in enumerate(data,1):ss.append([f'IM{n:03d}']+list(r.values()))
ss.freeze_panes='F4';ss.auto_filter.ref=f'A3:H{ss.max_row}'
for col,width in zip('ABCDEFGH',[12,12,28,10,20,105,65,65]):ss.column_dimensions[col].width=width
for rr in ss.iter_rows(min_row=3):
    for c in rr:c.alignment=Alignment(vertical='top',wrap_text=True)
    if rr[0].row==3:
        for c in rr:c.font=Font(bold=True,color='FFFFFF');c.fill=PatternFill('solid',fgColor='233A50')
for rr in ss.iter_rows(min_row=4):ss.row_dimensions[rr[0].row].height=75
w['START']['A2']=str(w['START']['A2'].value)+f' Etap23:S280–S283,Chojny2139przejrzane wkolumnachnazwisk;brak nowej relacji. Cyfrowyindeks44wiersze:{D}/INDEKS.html.'
w['ZRODLA_I_SKANY']['A2']='283źródła;25arkuszy. Etap23:próbaOCR,katalog26219,Chojny2139,pochodnyindeks44wiersze. Braknowegopotwierdzonegopokrewieństwa.'
w.save(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
print({'sources':283,'sheets':len(w.sheetnames),'index_rows':len(data),'new_family_links':0})
