"""Etap18: nowe indeksy i ograniczenia wyników, bez niepotwierdzonych relacji."""
from pathlib import Path
import datetime, openpyxl
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent;BASE=str(HERE.relative_to(ROOT))
w=openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
assert not any(r[0].value=='S217' for r in w['ZRODLA_I_SKANY'])
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
def row(sn,id):return next(r for r in w[sn] if r[0].value==id)
sources=[
('S217','Bełżec — publiczna inwentaryzacja BillionGraves336870','73 REKORDY; 7 NIEPRZEPISANYCH ZDJĘĆ OBEJRZANO','P28?; P29?; H045','BillionGraves','cemetery336870; 45 zdjęć; metadata74/lista73','https://billiongraves.com/cemetery/Be%C5%82%C5%BCec-Cmentarz-parafialny/336870','billiongraves/ui_response_4.json','Brak Mandziuków w73 rekordach i7 dodatkowo obejrzanych zdjęciach. Nie45/45 zdjęć. API total0 sprzeczne z73items; nie uznano za0wyników. Bardzo częściowa inwentaryzacja, H045 nadal otwarta. Nie kontaktowano kontrybutorów.'),
('S218','Tomaszów1924 — pełne oryginalne skorowidze U/M/Z','ODCZYT INDEKSÓW, NIE596AKTÓW','P05; P06; P26; P27; P28','APZ / Lubgens','88/639/0/-/49; album4780; U369,M81,Z146','https://fotolubgens.lubgens.eu/index.php?/category/4780','ksiegi/4780_064.jpg','Indeksy064–067,088–089,109–111, protokół112 iokładka001. Brak szukanych Chmielewskich i rodzinnegołącznika. Nie dowodzi braku rodzeństwa urodzonego poza parafią.'),
('S219','Tomaszów1925 — pełne oryginalne skorowidze M/Z','M77; Z180NUMEROWANYCH +2DOPISKI; U NIEOPUBLIKOWANE','P26; P27; P28; P05; P06','USC Tomaszów / Lubgens','album4328;021–022 M,047–051 Z','https://fotolubgens.lubgens.eu/index.php?/category/4328','ksiegi/4328_021.jpg','Brak szukanej rodziny. Protokół wymienia318U, lecz album nie zawiera ich skanów, zaczyna się odM. Nie przeszukano U1925. Dwa dopiskiZ poza numeracją uwzględniono osobno.'),
('S220','Tomaszów — uzupełnienie luki skorowidzów małżeństw1939–1942','PEŁNE INDEKSY OBOJGA MAŁŻONKÓW','P26; P27; P28; P12','USC Tomaszów / Lubgens','1939:89;1940:108+1dopisek;1941:68;1942:76+1dopisek','https://fotolubgens.lubgens.eu/index.php?/category/4352','ksiegi/1939_023.jpg','Bez Sabiny/Julianny/Emilii i bez nowego zidentyfikowanego rodzeństwa.343fizyczne wiersze przy341pozycjach numerowanych, nie343pełne akty.1940/030 oraz manifesty1940–42 użyte zsesji11, nie pobrane ponownie. Bez wniosku o małżeństwie poza tąparafią.'),
('S221','Pełne akty96/1940 i52/1941 — wyjaśnienie podobnych nazwisk','ODCZYT NOWOŻEŃCÓW I RODZICÓW; NIE NOWA RODZINA','P26/P27/P28 wykluczenie tropu','USC Tomaszów / Lubgens','96/1940:026.jpg;52/1941:014.jpg','https://fotolubgens.lubgens.eu/galleries/USC_Tomaszow_Lub/Tomaszow_UMZ_1940/026.jpg','ksiegi/1940_026.jpg','96/1940:Dymitro Małka/Janina Miszczyszyn17,c.Jana iJózefy zŻuków.52/1941:Edward Roman Ostasz/Wanda Chlebowska21,c.Bronisława iAnastazji zGoreckich. Błędne rozpoznawcze Chmielewska poprawiono z pełnych aktów. Zbieżność Miszczyszyn zrodowymP06 nie dowodzi pokrewieństwa. Nie dodano kandydatów ani relacji.')]
for sid,title,kind,persons,inst,sig,url,path,limit in sources:
 w['ZRODLA_I_SKANY'].append([sid,title,kind,'2026-11-06',persons,inst,sig,url,'ODCZYT W ZAKRESIE OPISANYM W OSTATNIEJ KOLUMNIE',BASE+'/zrodla/'+path,limit])
logs=[
('L194','Nowe źródło Bełżca — BillionGraves336870','Odczyt73wpisów listy; brakMandziuk.','Metadane74/lista73, API total0 niejest wynikiem0. Tylkofragment cmentarza.','S217; H045'),
('L195','Bełżec — siedem zdjęć nieprzepisanych','7oryginałów obejrzano; brakparyP28/P29. Emilia2001niejestP28zm.1979.','7/45zdjęć, niepełna inwentaryzacja; bezkontaktu iedycji.','S217'),
('L196','Tomaszów U1924','Pełny skorowidz369numerowanych urodzeń,064–067. BezChmielewskich rodziny.','Nieodczytano369aktów, nie obejmujeinnychparafii.','S218'),
('L197','Tomaszów M/Z1924','Pełne81M i146Z w indeksach; bezrodzinnegołącznika.','Nie596pełnychaktów U/M/Z.','S218'),
('L198','Tomaszów M/Z1925','77numerowanychM;180Z+2nienumerowane dopiski, pełnyodczyt indeksów.','U1925nieopublikowane wtym albumie,318wprotokole to nie318odczytów.','S219'),
('L199','Tomaszów M1939–1942 — luka między wcześniejszymi kwerendami','89/109/68/77fizycznychwierszy, oboje małżonków, brakidentyfikacji poszukiwanych.','Nie powtarzano1933–1938/1943–1944; w1940użyto starego030. Dwa podobne nazwiska sprawdzono wpełnychaktach.','S220; S221'),
('L200','Pełne akty96/1940 oraz52/1941','Janina Miszczyszyn iWanda Chlebowska, innirodzice. Rozpoznawcze Chmielewska skorygowane.','Beznowychkandydatów/relacji; samo Miszczyszyn nie potwierdza połączenia zP06.','S221; Q85'),
('L201','Zachowanie postępu naGitHub','Checkpoint d2eae7f zachowuje oryginały i zakres odczytu.','Nie dopisywano negatywnych kwerend do publicznej kroniki.','S217–S221')]
for id,scope,res,limit,src in logs:w['DZIENNIK_KWEREND'].append([id,now,scope,res,limit,src])
corrections=[
['Q85','KOREKTA ODCZYTU ROBOCZEGO','Podobne nazwiska zindeksów1940/1941 nie są Chmielewska','Pełne96/1940:Janina Miszczyszyn;52/1941:Wanda Chlebowska. Rodziceinni niżWincenty/Agnieszka.','WYSOKA — PEŁNE AKTY','S221','Nie tworzyć siostryCzesława zpodobnego pisma. Nie utożsamiać Janiny zC03.','https://fotolubgens.lubgens.eu/galleries/USC_Tomaszow_Lub/Tomaszow_UMZ_1941/014.jpg'],
['Q86','ZAKRES I LICZNIKI','Paginacja i protokół nie są liczbą odczytanych aktów','1942indeks76+1dopisek, nie46;1925Z180+2dopiski;1925U318 wprotokole bezskanów.','ODCZYT OBU STRON INDEKSÓW','S219; S220','Nie deklarować odczytu U1925 lub pełnych wszystkichaktów.','https://fotolubgens.lubgens.eu/index.php?/category/4328'],
['Q87','OGRANICZENIE API','BełżecBG:total0 nieoznacza pustej listy','73items i73winterfejsie; metadata74. Faktycznie obejrzano73rekordy i7nieprzepisanychzdjęć.','PUBLICZNY INTERFEJS I JSON','S217','Nie wykluczać Bełżca na podstawie częściowejinwentaryzacji.','https://billiongraves.com/cemetery/Be%C5%82%C5%BCec-Cmentarz-parafialny/336870']]
for r in corrections:w['KOREKTY_I_SPRZECZNOSCI'].append(r)
for id,path,src in [('F163','billiongraves/ui_response_4.json','S217'),('F164','billiongraves/untranscribed_downloads.json','S217'),('F165','ksiegi/4780_064.jpg','S218'),('F166','ksiegi/4328_021.jpg','S219'),('F167','ksiegi/1939_023.jpg','S220'),('F168','ksiegi/1940_026.jpg','S221'),('F169','ksiegi/1941_014.jpg','S221')]:
 w['PLIKI_DOWODOWE'].append([id,BASE+'/zrodla/'+path,'KOPIA PIERWOTNA / INDEKS / LOG',src,'Pełny zakres wZAKRES_ODCZYTU.md; pozostałe fotografie wmanifeście.','SHA256; zdjęcia iindeksy nie dowodzą nowych rodzinnychrelacji.'])
row('HIPOTEZY_OTWARTE','H045')[2].value+=' Etap18:S21773wpisy i7nieprzepisanych zdjęćBillionGravesBełżec336870 bezpary; zbiór45zdjęć jest niepełny. Nie wyklucza pochówku aniH045.'
row('HIPOTEZY_OTWARTE','H032')[2].value+=' Etap18:S218–S220 nie dały rodzinnegołącznika wnowych indeksach1924,1925M/Z i1939–1942M. S217tylkofragmentBełżca bezMandziuków; nie dowód bezdzietności.'
row('HIPOTEZY_OTWARTE','H019')[2].value+=' Etap18:pełneM1939–1942Tomaszów nie wskazały nazwiska poślubie Sabiny/Julianny; nie wyklucza ślubu wTczewie lub innejparafii.'
w['START']['A2']='Etap18: Polska, rodziny rodzeństwaCzesława. Nowe indeksy Tomaszowa1924/1925MZ i1939–1942M, Bełżec73wpisy i7zdjęć; nadal brak nowego potwierdzonego żyjącego krewnego. Raport badania/2026-11-06-sesja-18-polska-ksiegi/. Australia wstrzymana.'
w['ZRODLA_I_SKANY']['A2']='221 źródeł. Etap18:S217–S221. Zakres odczytu i ograniczenia wostatniej kolumnie; beznowychrelacji i beznowego potwierdzonego żyjącego krewnego.'
w['INSTRUKCJA_AGENTA']['A2']='Etap18: priorytet polscypotomkowie rodzeństwaCzesława. Nowe księgi iBełżec sprawdzone wzakresie STATUS.md. Bezponawiania pełnychindeksów; bezkontaktów. H017 nadalotwarta, S086jużpodaje nazwiskarodziców.'
w.save(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
print('Zapisano S217–S221,L194–L201,F163–F169,Q85–Q87; 23arkusze,221źródeł,97kandydatów,201kwerend.')
