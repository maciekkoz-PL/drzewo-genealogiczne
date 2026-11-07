"""Jednorazowy zapis etapu24, bez zmiany udowodnionych relacji."""
from pathlib import Path
import copy,datetime,json,re
import openpyxl
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent;D=str(HERE.relative_to(ROOT))
w=openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx');now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
assert not any(r[0]=='S284' for r in w['ZRODLA_I_SKANY'].values),'Już zapisano'
def row(sn,id):return next(r for r in w[sn] if r[0].value==id)
def add(sn,values):
 s=w[sn];s.append(values)
 for c in s[s.max_row]:c._style=copy.copy(s.cell(s.max_row-1,c.column)._style)
u='https://photos.szukajwarchiwach.gov.pl/eab684755647743f6205556058602f4cd106a0e3edcef7f104e6b6484c62cf27_max'
sources=[
 ['S284','Agnieszka Chmielewska — wyjazd z Chojen do Napiórkowskiego112','SKAN PIERWOTNY',now,'C102;H052','AP Łódź / Szukaj w Archiwach','39/225/0/4/2140;obraz89;karta86;nr1947',u,'ODCZYTANO WPIS I KONTEKST DATY',D+'/zrodla/Chojny1939_89.jpg','1kobieta; otrzymanie zgłoszenia29IX1939,ditto po1941. Łódź,Napiórkowskiego112. Zgodność zS274/2246/21X1939: imię,nazwisko,kierunek,adres,liczba osób. Mocne dopasowanie dwóch zapisów przeprowadzki, nie genealogiczne połączenie zP06/C99/C42. Brak wieku,rodowego,krewnych i wcześniejszej ulicy wChojnach.'],
 ['S285','Chojny2140 — zakończony przegląd nazwisk i wpisy Marianów','SKANY PIERWOTNE / ODCZYT WZROKOWY',now,'P11 nieustalony; dwa odrębne wpisy Marianów','AP Łódź / Szukaj w Archiwach','39/225/0/4/2140;196obrazów','https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/15352000','NAZWISKA5–195;WYBRANE PEŁNE POLA',D+'/zrodla/zakres_odczytu.json','Uzupełniono5–89/116–195;wcześniej90–115. Techniczne1–4/196obejrzane; pełne70/89/118/144/145/180/195. Marian1496:4m+1k,Bankowa31;1497:1m,ulica roboczoZgórna10(niepewna);zgłoszenia8VIII1939. Bezrodziców/DOB/pokrewieństwa. Czasowe145–195→118–144;niezapisane fizyczne strony wgmetryki1. Nie pełna transkrypcja ani wykluczenie nienazwanych osób grup.'],
 ['S286','Przeszukiwalne zestawienie meldunków —47wierszy','OPRACOWANIE POCHODNE',now,'Wybrane trafienia, nie lista krewnych','Opracowanie lokalne','CSV/HTML/INDEKS_MELDUNKOW;IM001–IM047','https://github.com/maciekkoz-PL/drzewo-genealogiczne','44STARSZE +3NOWE WIERSZE',D+'/zrodla/indeks_wybranych_wpisow.csv','S283wersja44wiersze zachowana. DodanoS284/1947,S285/1496i1497. Nie pełny indeks, nie niezależne źródło wobec skanów.']]
for r in sources:add('ZRODLA_I_SKANY',r)
for id,scope,result,limit,src in [
 ('L284','Chojny2140,obraz89,nr1947','AgnieszkaChmielewska,1kobieta,doŁodziNapiórkowskiego112;zgłoszenie29IX1939. OdpowiednikS274/2246.','Bez wieku,rodowego,rodziców i poprzedniej ulicy. H052 otwarta, P11 nieustalony.','S284;S274'),
 ('L285','Chojny2140:pozostałe nazwiska5–89/116–195','Zakończono dostępne kolumny5–195;Marian1496i1497bezrodzinnegołącznika; rozdzielono części stałe/czasowe.','Nie pełna transkrypcja wszystkich pól; osoby grup nienazwane. Techniczne1–4/196.','S285'),
 ('L286','Cyfrowa tabela odczytów','Rozszerzono44→47wierszy;staraHTML/CSVzachowana wsesji23.','Nie pełny indeks;Marianowie nieprzypisani do rodziny.','S286')]:add('DZIENNIK_KWEREND',[id,now,scope,result,limit,src])
c=row('KANDYDACI_I_HOMONIMY','C102')
for j,t in [(2,' Drugi dokument:S284,wyjazdChojny,nr1947,karta86/obraz89,zgłoszenie29IX1939,1kobieta,ten sam adres.'),(6,' S284mocno koreluje zS274 po imieniu,nazwisku,kierunku,adresie i liczbieosób; nie dodaje wieku/rodowego ani pokrewieństwa.'),(7,';S284')]:c[j].value+=t
h=row('HIPOTEZY_OTWARTE','H052');h[2].value+=' Etap24:S284nr1947,29IX1939,1kobieta→ŁódźNapiórkowskiego112. Mocny odpowiednikS274/2246; dwa rejestry jednej przeprowadzki. Brak łącznika osobowego zP06/C99/C42;H052nadalotwarta. S285nazwiska2140/5–195zakończone.'
h[3].value+=' S284nie podaje wcześniejszej ulicy wChojnach; teraz katalog wcześniejszych przyjazdów1937–1938/karty ludności.'
t=row('ZADANIA_AGENTA','T58');t[5].value='AKTYWNE:znaleziono wyjazdC102nr1947/29IX1939(S284). Nazwiska2139i2140wykonane wopisanym zakresie. Potrzebna karta z wiekiem/rodowym; sprawdzić wcześniejsze przyjazdyChojen i26219(S281).';t[8].value+=';S284;S285;S286;'+D+'/PLAN_KONTYNUACJI.md'
add('INSTRUKCJA_AGENTA',['G27','ETAP24 — ODPOWIEDNIK WYJAZDOWY',f'S284/1947:karta86,29IX1939,Agnieszka→Napiórkowskiego112; mocne dopasowanieS274,bezpotwierdzeniaP06/C42. Chojny2140nazwiska5–195wykonane; nie powtarzać. Czytaj {D}/PLAN_KONTYNUACJI.md.'])
for n,f in enumerate(sorted((HERE/'zrodla').iterdir()),356):
 src='S286' if f.name=='indeks_wybranych_wpisow.csv' else 'S284;S285' if f.name in ['Chojny1939_89.jpg','Agnieszka_1947.jpg','odczyty_wybrane.json'] else 'S285'
 add('PLIKI_DOWODOWE',[f'F{n}',str(f.relative_to(ROOT)),'SKAN / METADANE / POCHODNE',src,'Zakres wzakres_odczytu.json;hashwmanifest.json.','12oryginałów;wycinki/ZIPsą pochodnymi;beznowejrelacji.'])
data=json.loads((HERE/'indeks_dane.json').read_text());assert w['INDEKS_MELDUNKOW'].max_row==47
for n,r in enumerate(data[44:],45):add('INDEKS_MELDUNKOW',[f'IM{n:03d}']+list(r.values()))
s=w['INDEKS_MELDUNKOW'];s['A2']='47wierszy; wybrane odczyty, imiennicy/tropy, nie lista krewnych. Wersja44zachowana w etapie23.';s.auto_filter.ref=f'A3:H{s.max_row}'
for n in range(48,51):s.row_dimensions[n].height=75
w['START']['A2'].value+=f' Etap24:S284drugi zapis Agnieszki,Chojny→Napiórkowskiego112;S285nazwiska2140/5–195zakończone;S286tabela47wierszy. Braknowejrelacji. {D}/STATUS.md.'
w['ZRODLA_I_SKANY']['A2']='286źródeł;25arkuszy. Etap24:drugi zapis AgnieszkiC102/wyjazdChojny1947/1939;bez potwierdzeniaP06/C42/P11.'
w.save(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
print(dict(sources=286,logs=286,files=378,index=47,sheets=len(w.sheetnames)))
