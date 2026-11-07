"""Jednorazowe uzupełnienie o inwentarz Buczku; uruchamiać po zapisz.py."""
from pathlib import Path
from datetime import datetime, timezone
from openpyxl import load_workbook
R=Path(__file__).resolve().parents[2]
x=R/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx'
w=load_workbook(x)
assert w['ZRODLA_I_SKANY']['A300'].value=='S297'
assert w['DZIENNIK_KWEREND']['A302'].value=='L299'
assert w['PLIKI_DOWODOWE']['A437'].value=='F434'
t=datetime.now(timezone.utc).isoformat(timespec='seconds')
url='https://www.szukajwarchiwach.gov.pl/de/zespol?_Zespol_id_zespolu=71062&_Zespol_javax.portlet.action=zmienWidok&_Zespol_nameofjsp=jednostki&p_p_id=Zespol&p_p_lifecycle=1&p_p_mode=view&p_p_state=normal'
p='badania/2026-11-07-sesja-27-Lodz-1938/INWENTARZ_BUCZEK.md'
w['ZRODLA_I_SKANY'].append(['S298','Skorowidz rejestru mieszkańców gminy Buczek 1932–1939','INWENTARZ ARCHIWALNY',t,'Skorowidz mieszkańców, bez imiennych wpisów online','AP Łódź Oddział Sieradz / SwA','41/571/0/-/60',url,'OPIS JEDNOSTKI, 0 SKANÓW',p,'Może wskazać miejscowość i kartę, ale nie sprawdzono zawartości. Nie dowodzi obecności C105 lub Stanisławy.'])
w['ZRODLA_I_SKANY'].append(['S299','Rejestr mieszkańców wsi Buczek, Szadek, Wygwizdów, Lgów 1932–1939','INWENTARZ ARCHIWALNY',t,'Rejestr mieszkańców wsi, bez imiennych wpisów online','AP Łódź Oddział Sieradz / SwA','41/571/0/-/63',url,'OPIS JEDNOSTKI, 0 SKANÓW',p,'Tylko dla tych wsi; miejsce pobytu C105/Stanisławy w gminie nieznane. Inne rejestry /61,/62,/64–/67.'])
w['DZIENNIK_KWEREND'].append(['L300',t,'Inwentarz Akta gminy Buczek 41/571/0; dokładne sygnatury rejestrów 1932–1939 oraz wyszukiwanie kopii/indeksu','Zlokalizowano /60 skorowidz i /61–/67 rejestry wsi, w tym /63 dla Buczku; katalog podaje 0 skanów. Nie znaleziono nazwisk na kartach ani transkrypcji.','Katalog potwierdza istnienie źródła, nie obecność osób. Nie kontaktowano się z archiwum.',p+';S298;S299'])
w['PLIKI_DOWODOWE'].append(['F435',p,'DZIENNIK INWENTARZA','S298;S299;L300','Sygnatury 41/571/0/-/60, /63 i pozostałe rejestry wsi','Bez skanów ani potwierdzonego wpisu osobowego'])
w['START']['A2']='Etap27: cała Łódź25508 przejrzana po nazwiskach; Q101 Grabowa4; H054 Buczek otwarta. Znaleziono skorowidz mieszkańców Buczku 1932–1939 sygn.41/571/0/-/60 i rejestry /61–/67, bez skanów online. P11 nadal bez imienia.'
w.save(x)
