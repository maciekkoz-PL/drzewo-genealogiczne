"""Rejestr negatywnych kwerend adresowych po dopelnij.py; uruchamiać raz."""
from pathlib import Path
from datetime import datetime, timezone
from openpyxl import load_workbook
R=Path(__file__).resolve().parents[2]
X=R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
p='badania/2026-11-07-sesja-26-Wladyslaw-1938/DODATEK_WYSZUKIWARKI.md'
w=load_workbook(X)
assert w['DZIENNIK_KWEREND']['A299'].value=='L296'
assert w['PLIKI_DOWODOWE']['A433'].value=='F430'
t=datetime.now(timezone.utc).isoformat(timespec='seconds')
w['DZIENNIK_KWEREND'].append(['L297',t,'Publiczna wyszukiwarka: dokładne frazy Chełmońskiego9a+Chmielewski/Chmielewska, Zamenhofa13+Chojny, Limanowskiego42+Chmielewski','Brak niezależnego identyfikatora rodziny w obejrzanych wynikach; Opoczno27586624 to inna miejscowość.','Wyszukiwarka nie jest pełnym inwentarzem; warianty i mylące trafienia zapisano dokładnie.',p])
w['PLIKI_DOWODOWE'].append(['F431',p,'DZIENNIK NEGATYWNYCH KWEREND','L297','Sześć dokładnych fraz i odrzucone wyniki','Bez wniosku o nieobecności dokumentów'])
w['START']['A2']='Etap26: C103/C104 możliwe gospodarstwo Chełmońskiego9a; C105 osobny Czesław1602. Brak pokrewieństwa P11. Kwerenda L297 bez nowego łącznika.'
w.save(X)
