"""Dopełnienie etapu26 po kontroli obrazów71–95; uruchamiać po zapisz.py."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
from openpyxl import load_workbook

R=Path(__file__).resolve().parents[2]
H=Path(__file__).resolve().parent
Z=H/'zrodla'
W=R/'work/s25'
X=R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
man=json.loads((R/'badania/2026-11-07-sesja-25-Chojny-1938/katalog/manifest_6209685.json').read_text())
url74=next(e['src'] for e in man['elementy'] if e['pozycja']==74)
shutil.copyfile(W/'LodzW1938_74.jpg',Z/'LodzW1938_74.jpg')
scope=json.loads((Z/'zakres_odczytu.json').read_text())
assert len(scope['lodz_wyjazdy']['oryginaly'])==70
scope['lodz_wyjazdy']['oryginaly'] += [
    {'obraz':i,'sha256':hashlib.sha256((W/f'LodzW1938_{i}.jpg').read_bytes()).hexdigest()}
    for i in range(71,96)
]
scope['lodz_wyjazdy']['zakres_obejrzany']='obrazy1–95/184; kolumny nazwisk/liczb osób; obrazy8 i74 pełne rubryki nr80 i1602'
scope['lodz_wyjazdy']['uwaga']='Oryginały obrazów8 i74 archiwizowane w repozytorium. Pozostałe93 pobrano i zahaszowano; przegląd kolumn nie jest pełną transkrypcją.'
scope['lodz_wyjazdy']['dodatkowy_wpis']={'obraz':74,'karta':71,'nr':1602,'osoba':'Czesław Chmielewski','osoby':'2m+1k','kierunek':'powiat Łask, gmina Buczek','adres_poczatkowy':'Limanowskiego42 [odczyt do kontroli]','wniosek':'Bez DOB, rodziców i imion grupy; nie utożsamiono zP03 ani C103/C104.'}
(Z/'zakres_odczytu.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')
files=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(Z.iterdir()) if p.is_file()]
(H/'manifest.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')
wb=load_workbook(X)
assert wb['ZRODLA_I_SKANY']['A298'].value=='S295'
assert wb['KANDYDACI_I_HOMONIMY']['A107'].value=='C104'
assert wb['INDEKS_MELDUNKOW']['A59'].value=='IM056'
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
wb['ZRODLA_I_SKANY']['G297']='39/221/0/4.12/25508; obrazy1–95/184'
wb['ZRODLA_I_SKANY']['I297']='KOLUMNY NAZWISK1–95; NR80 i1602 PEŁNE RUBRYKI'
wb['ZRODLA_I_SKANY']['K297']='Niepełna transkrypcja; 95 obrazów pobrano i zahaszowano, oryginały8 i74 zachowano w repozytorium.'
wb['DZIENNIK_KWEREND']['C297']='Łódź25508/1938 obrazy1–95; Chojny2137/1938 celowana wtórna kontrola obrazów5–22'
wb['DZIENNIK_KWEREND']['E297']='Zakres Łodzi95/184; przegląd nazwisk, nie pełnych rubryk. Niewymienieni w grupach pozostają nieznani.'
wb['ZADANIA_AGENTA']['F61']='AKTYWNE: S293/C104 wyjazd Władysława z Chełmońskiego9a do Chojen (2m+3k), zgodny z C103; H053 otwarta. Łódź25508 nazwiska1–95/184, C105/Czesław1602 nieutożsamiony zP03. Inwentarz15575 obrazy1–12/172.'
wb['ZRODLA_I_SKANY'].append(['S296','Łódź25508/1938, wyjazd Czesława Chmielewskiego nr1602','SKAN PIERWOTNY / ODCZYT PEŁNY',now,'Czesław Chmielewski;2m+1k','APŁ / SwA','39/221/0/4.12/25508;karta71/obraz74/nr1602',url74,'ORYGINAŁ ODCZYTANY',str((Z/'LodzW1938_74.jpg').relative_to(R)),'Z Limanowskiego42 [odczyt do kontroli] do powiatu Łask, gmina Buczek; bez DOB/rodziców/imion współdomowników. Nie utożsamiono z dziadkiem P03 ani grupą C103/C104.'])
wb['DZIENNIK_KWEREND'].append(['L296',now,'Łódź25508/1938 obrazy71–95, pełne rubryki obrazu74/nr1602','Czesław Chmielewski;2m+1k; Limanowskiego42 [kontrola]→Łask/Buczek.','Brak cech identyfikacyjnych P03; nie łączyć po samym imieniu/nazwisku. Nie jest to grupa Chełmońskiego9a.', 'S296;C105'])
wb['KANDYDACI_I_HOMONIMY'].append(['C105','Czesław Chmielewski — Limanowskiego42','1938,nr1602;karta71/obraz74;2m+1k;bezDOB/rodziców','Możliwy imiennik P03; nie utożsamiono','Łódź,Limanowskiego42 [odczyt do kontroli]→pow.Łask,gm.Buczek','OSOBNY TROP — BRAK IDENTYFIKACJI','Imię i nazwisko zgadzają się z dziadkiem, ale brak wieku, żony i dzieci; inny adres/grupa niżC103/C104.','S296','Dokument z datą urodzenia, rodzicami lub imionami współdomowników.',url74])
wb['INDEKS_MELDUNKOW'].append(['IM057','S296','39/221/0/4.12/25508',74,'1602','Czesław Chmielewski;2m+1k;Limanowskiego42 [kontrola]→Łask/Buczek. Nie utożsamiono zP03 ani zgrupąChełmońskiego9a.',url74,'Etap26;pełne rubryki,karta71;oryginał zachowany'])
wb['PLIKI_DOWODOWE'].append(['F430',str((Z/'LodzW1938_74.jpg').relative_to(R)),'ORYGINALNY SKAN','S296','Obraz74,karta71,nr1602,pełna strona','SHA256 w manifest.json; bez identyfikacji zP03'])
wb['ZRODLA_I_SKANY']['A2']='296źródeł;25arkuszy. Etap26:C103/C104 adres Chełmońskiego9a;C105 Czesław1602 osobny,bezutożsamienia zP03.'
wb['KANDYDACI_I_HOMONIMY']['A2']='105rekordów. C104 Władysław i C103 Agnieszka wspólny adres; C105 Czesław1602 nieutożsamiony zP03.'
wb['INDEKS_MELDUNKOW']['A2']='57wybranych odczytów; nie pełny indeks ani lista krewnych.'
wb['START']['A2']='Etap26: C103/C104 możliwe gospodarstwo przy Chełmońskiego9a; C105 odrębny Czesław1602. Brak potwierdzonego pokrewieństwa i imieniaP11.'
wb.save(X)
print('Dopełniono etap26:',url74)
