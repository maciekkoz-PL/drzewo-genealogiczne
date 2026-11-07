"""Jednorazowa migracja etapu 22 z 2e94415; poprzedni stan zachowany w Git."""
from pathlib import Path
import copy, datetime, json, re
import openpyxl
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
D=str(HERE.relative_to(ROOT)); w=openpyxl.load_workbook(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
assert not any(r[0]=='S274' for r in w['ZRODLA_I_SKANY'].values),'Migracja już wykonana'
def add(sn,values):
    s=w[sn];s.append(values)
    for c in s[s.max_row]:c._style=copy.copy(s.cell(s.max_row-1,c.column)._style)
def row(sn,id):return next(r for r in w[sn] if r[0].value==id)
def append(sn,id,col,value):
    c=row(sn,id)[col-1];c.value=(c.value or '')+' '+value
url='https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6209623'
for r in [
 ['S274','Przybyli do Łodzi1939, grupaIII; Agnieszka przy Napiórkowskiego112','ORYGINALNE SKANY; PRZEGLĄD KOLUMN I WYBRANE WPISY',now,'C102; C42?; P06?; C99?; P11?','APŁ / Szukaj w Archiwach','39/221/0/4.12/25446; obraz98/karta94/nr2246',url,'ODCZYT WZROKOWY; DOKŁADNY ZAKRES W JSON',D+'/zrodla/zakres_odczytu.json','Pobrano obrazy4–125(122). Nazwiska4–124,5techniczny,125pusty wycinek. Szczegóły wybranych21obrazów. AgnieszkaChmielewska,1kobieta,Chojny→Napiórkowskiego112,21X1939. Ten sam adres co S126, lecz bez wieku/nazwiska rodowego/rodziców. Nie utożsamiono zP06/C99, nie potwierdzono relacjiC42/P11. Obrazy1–3/126nieodczytane.'],
 ['S275','Kontrola trzech brzegowych skanów wcześniejszych ksiąg','ODCZYT OKŁADEK I POŚWIADCZENIA',now,'Nie dotyczy identyfikacji osoby','APŁ / Szukaj w Archiwach','25443obraz4;25444obrazy4/73','https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6209621','TRZY WSKAZANE OBRAZY',D+'/zrodla/III_1937_73.jpg','25443/4 i25444/4 to tytuły;25444/73poświadczenie200kart. Uzupełnia zakres S267/S268, nie oznacza odczytu pozostałych brzegów ani200nowych kart osobowych.'],
 ['S276','Dwie kwerendy nowego połączenia adresowego Napiórkowskiego/Chojny','WYNIKI WYSZUKIWARKI; BEZ ODCZYTU DOKUMENTÓW WYNIKOWYCH',now,'C102?; C42?','Wyszukiwarka internetowa','Dwie frazy zapisane wJSON','https://www.google.com/search?q=%22Chmielewska%22+%22Napi%C3%B3rkowskiego%22','BRAK NOWEGO RODZINNEGO IDENTYFIKATORA',D+'/zrodla/kwerendy_web.json','Wyniki prasowe i imiennicy bez połączenia z rodziną. Nie przeczytano pełnych PDF ani nie przypisano współczesnych osób. Nowy odczyt meldunku uzasadniał kontrolę tych konkretnych fraz.'],
 ['S277','Katalog ewidencji Chojen: rejestry przybyłych i opuszczających gminę1939','KATALOG BASIA I GRANICA DOSTĘPU SwA',now,'C102?','BASIA / APŁ','39/225/0/4/2139 i2140; SwA15351999/15352000','https://basia.famula.pl/skany.php?placeid=1677','ODCZYT KATALOGU; NIE KSZĄG',D+'/zrodla/katalog_Chojny.json','ListaBASIAwskazuje2139przybyli i2140opuszczający1939; bez treści wpisówAgnieszki. Bezpośrednie strony jednostek i zespołu zwróciły niedostępny portlet. Skorowidze2102–2104mają wcześniejsze daty1893–1910, nie zakładać pokrycia1939.']]:add('ZRODLA_I_SKANY',r)
add('KANDYDACI_I_HOMONIMY',['C102','Agnieszka Chmielewska — Napiórkowskiego112','21X1939;nr2246;karta94/obraz98;1kobieta;poprzednioChojny;bezDOB','Możliwa P06/C99; związek z C42 nieustalony','Łódź,Napiórkowskiego112','MOCNY TROP ADRESOWY — TOŻSAMOŚĆ I RELACJE OTWARTE','Dokładnie ten sam adres co zgonC42wS126. Nie podano nazwiska rodowego ani wieku; jeden budynek nie dowodzi pokrewieństwa.','S274; S126; S267','Dokument podający datę urodzenia/nazwisko rodowe Agnieszki lub skład rodziny. Sprawdzić załącznik2246/1939 i ewidencjęChojen. H052.',url])
add('HIPOTEZY_OTWARTE',['H052','C102=AgnieszkaMiszczyszynP06/C99? Czy ma relację z rodziną C42?','S274:Chojny→Napiórkowskiego112,21X1939. S126:ten sam adres dzieckaCzesława i rodziceCzesław/Janina zPoprawskich. Adres jest wspólny; osoby nie zostały utożsamione.','Załącznik2246/1939; karta ludnościChojen; akt/ewidencja z wiekiem, nazwiskiem rodowym i rodziną. Nie odczytano jeszcze tych dokumentów.','OTWARTA — KORELACJA ADRESÓW, BEZ DOWODU POKREWIEŃSTWA'])
append('HIPOTEZY_OTWARTE','H018',3,'Etap22/S274: AgnieszkaChmielewska(C102),21X1939,Chojny→Napiórkowskiego112, czyli adresC42. Nowy łącznik adresowy; brakDOB i nazwiska rodowego nie pozwala uznać jej zaP06 ani potwierdzić braterstwaC42. H052.')
append('HIPOTEZY_OTWARTE','H050',3,'Etap22:C102podNapiórkowskiego112 ma to samo imię/nazwisko, ale brak identyfikatora pozwalającego scalić zC99/P06; H052.')
append('HIPOTEZY_OTWARTE','H002',3,'Etap22:S274nowy tropAgnieszki i adresuC42; nadal nie znaleziono imieniaP11. C42zmarł jako niemowlę i nie mógł być ojcemPiotra.')
append('KANDYDACI_I_HOMONIMY','C42',7,'S274/C102: AgnieszkaChmielewska pod tym samym adresem21X1939. Zbieżność adresu bez ustalenia jej tożsamości i pokrewieństwa.')
append('KANDYDACI_I_HOMONIMY','C42',8,'S274; H052')
for scope,result,limit,src in [
 ('Pozyskanie25446/1939','Bezpośrednie API zwróciło HTML; zwykła nawigacja publicznej przeglądarki pozwoliła zapisać manifest126obrazów i pobrać122JPEG(4–125).','Metoda dostępu nie jest dowodem rodzinnym;1–3/126nieodczytane.','S274'),
 ('25446,nazwiska4–124','Przejrzano wskazany zakres i szczegóły21wybranychobrazów; trafienia wCSV.','Nie jest to pełny odczyt wszystkich rubryk; wpisy narodzin bez rodziców nie identyfikująP11.','S274'),
 ('25446,nr2246/1939','AgnieszkaChmielewska,Chojny→Napiórkowskiego112,21X1939. C102/H052.','Brak wieku,nazwiska rodowego,rodziców i relacji.','S274'),
 ('Porównanie zS126','Ponownie odczytano fragment oryginału: zgonC42przyNapiórkowskiego112; zgodny adres zC102.','S126to ten sam znany akt, nie nowe niezależne źródło. ZachowanoPoprawskich i nie potwierdzonoH018.','S126; S274'),
 ('Kontrola brzegów25443/25444','Odczytano tytuły4/4 i poświadczenie73.','Pozostałe brzegi nie są uznane za odczytane.','S275'),
 ('Dwie nowe kwerendy adresowo-imienne','Brak nowego rodzinnego identyfikatora; zachowano pełną odpowiedź wyszukiwarki.','Nie odczytano dokumentów prasowych z wyników; imiennicy nie scaleni.','S276'),
 ('Katalog ksiągChojen; trzy kwerendy bibliograficzne','BASIAwskazuje2139przybyli i2140opuszczający1939, dwa linki do jednostek.','StronySwAportletniedostępny; katalog nie jest wpisem osobowym.','S277')]:
    no=max(int(r[0][1:]) for r in w['DZIENNIK_KWEREND'].values if isinstance(r[0],str) and re.fullmatch(r'L\d+',r[0]))+1
    add('DZIENNIK_KWEREND',[f'L{no}',now,scope,result,limit,src])
row('ZADANIA_AGENTA','T57')[5].value='WYKONANY WSKAZANY ZAKRES:4–124nazwiska,21wybranych pełnych wpisów;S274; obrazy1–3/126nadal nieodczytane'
row('ZADANIA_AGENTA','T57')[8].value='S274; etap22/PLAN_KONTYNUACJI.md; H052'
add('ZADANIA_AGENTA',['T58',1,'NOWY ŁĄCZNIK ADRESOWY','APŁ / publiczna ewidencjaChojen','Nr2246/1939:AgnieszkaChmielewska→Napiórkowskiego112; ustalić dane osobowe, rodziny i dokładną teczkęzałącznika.','AKTYWNE — BEZ SCALENIA','Agent','Wspólny adresC42nie dowodzi, że toP06. Bez wysyłania zapytań/wniosków.','S274; S126; H052'])
for i,f in enumerate(sorted((HERE/'zrodla').iterdir()),279):
    source='S275' if f.name in ['III_1936_1937_4.jpg','III_1937_4.jpg','III_1937_73.jpg'] else 'S276' if f.name=='kwerendy_web.json' else 'S277' if f.name=='katalog_Chojny.json' else 'S274'
    add('PLIKI_DOWODOWE',[f'F{i}',str(f.relative_to(ROOT)),'SKAN / MANIFEST / ODCZYT / POCHODNE',source,'Etap22; dokładny zakres wJSON. SHA256wmanifest.json.','Oryginały wybranych wpisów; ZIPkolumn i wycinek2246są pochodnymi. Nie dowodzą pokrewieństwa.'])
w['START']['A2']=str(w['START']['A2'].value)+f' Etap22:S274–S276; AgnieszkaNapiórkowskiego112=C102/H052,ten sam adres coS126; brak nowej potwierdzonej relacji. Plan:{D}/PLAN_KONTYNUACJI.md.'
w['ZRODLA_I_SKANY']['A2']='277 źródeł; etap22:S274–S277. Nowa korelacja adresowa Napiórkowskiego112, bez potwierdzenia pokrewieństwa.'
w['KANDYDACI_I_HOMONIMY']['A2']='102 rekordy, w tym zachowane aliasy. C102: Agnieszka przy Napiórkowskiego112, niescalona zP06/C99.'
w.save(ROOT/'Marysia_KOMPLET_BAZA_2026-11-05.xlsx')
counts={sn:sum(isinstance(r[0],str) and bool(re.fullmatch(r'[A-Z]+-?\d+',r[0])) for r in w[sn].values) for sn in w.sheetnames}
(HERE/'LICZNIKI.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print({sn:counts[sn] for sn in ['ZRODLA_I_SKANY','KANDYDACI_I_HOMONIMY','DZIENNIK_KWEREND','PLIKI_DOWODOWE','ZADANIA_AGENTA']})
