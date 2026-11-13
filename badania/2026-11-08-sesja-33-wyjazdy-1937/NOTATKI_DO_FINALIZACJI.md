> Archiwum roboczych notatek sprzed zapisu Excela13XI2026. Aktualne wyniki i liczniki: [STATUS.md](STATUS.md). Dawne zdanie o niezmienionej bazie opisuje punkt kontrolny, nie stan po finalizacji.

# Stan roboczy po wznowieniu 13.11.2026

To nadal etap 33 rozpoczęty 8 XI; Excel nie został jeszcze zmieniony. Baza przed etapem33 ma identyczne SHA z bieżącym plikiem, ostatnie identyfikatory S317/L321/F471/IM062/C108/Q106. Root main nadal08b5991. Audyt GitHuba jest oddzielnie zatwierdzony i wysłany: afde786 na `codex/audyt-repo-2026-11-13`. Bieżąca lokalna gałąź wróciła do `work`.

## Odczyty zakończone, wymagają rejestracji w Excelu

- 25507: wszystkie142obrazy nazwisk5–103/105–147, 149JPG pobrane,30oryginałów w zrodla,24wiersze wCSV; S318. Początek23III1937, nie cały rok. Nie powtarzać. Skrypt przygotuj.py zakończony.
- 25509: wszystkie181obrazy nazwisk4/6–185,187JPG pobrane,26oryginałów w zrodla,19wierszy wCSV; S319. Zgłoszenia2I–1XII1939; nie cały grudzień. Skrypt przygotuj_1939.py zakończony.
- Nowy3693, obraz165,str161,6XI1939: **Chmielewska / Stanisława i Zygm.**,1m+1k, Grabowa4→Łask/Buczek, wieś niepodana. S320. Zestawiono z IM025/nr708/S274:14III1939Buczek→Grabowa4,1m+1k. Mocne dopasowanie grupy/adresu, bez wieku lub roli mężczyzny. Nie dowodzi relacji do C105/P03/P11. Dla C109 zapisać literalnie „Zygm.”; samodzielne nazwisko mężczyzny i rozwinięcie skrótu nie są podane oddzielnie. H054 pozostaje otwarta.
- Wybrane kontrole1939:183/nr4097 to **Zbigniew**, nie Włodzimierz.179/nr4005 to **Chmielecki Jerzy Stanisław**, nie Chmielewski.18/nr303 i39/nr785 to **Stanisław/1m**, nie Stanisława.119/nr2639to **Józefa/1k**, nie Józef. ZaktualizowaneCSV mają poprawne odczyty.
- Arolsen: nowy filtr na już pobranych4773pozycjach S313 daje43rekordy Zygm*/Sigm*,42DocID. Brak wpisanych pól Father/Mother w tej wybranej odpowiedzi indeksowej nie dowodzi braku danych w aktach. Pobrano i obejrzano6DocID/10obrazów:70634058,78640271,81787522,81978799,81979003,81991022. Proponowane S321, bez nowego połączenia rodzinnego.
- 70634058: Zygmund14V1910, klinikaGöttingen15X–3XI1941, wypisGr.Lengden; brak rodziców/żony/Łodzi.
- 78640271: Sigmund10V1926 w gospodarstwieOtłoczyn/GemeindeOttlotschin, spis21V1941; Anton24VII1896,Valerie17IV1887, dalejWanda/Wiktor i osoby z rolami Stieftochter/Schwägerin/Stiefsohn. Nie połączono z P11/„Zygm.”.
- 81787522: Zygmunt41lat, Ship-Agent, single, Poland→Chicago, nr61595/207598; rewers kartowania1950, dokładna data listy nieustalona. Nie przypisano rodzinie.
- 81978799: Zygmunt9IV1905 i Zygmunt15VIII1943/Pforzheim. Osobne numery kart DP126758/126759; Halina4V1914/karta126755. Sam układ nazwisk nie jest aktem rodzicielstwa.
- 81979003: transferEttlingen→Ingolstadt30VIII1946, wiersze45–47: Zygmunt41l.karta126758, Halina32l.126755, Zygmunt3l.126759. Numery kart łączą te osoby z81978799; nie dowodzą relacji z rodzinąMarysi. Rewers bez dodatkowych danych.
- 81991022: Zygmund118138 i Anna118139 przyG04854612; brakDOB/Łodzi/Stanisławy; rewers stemple1948/49. Nie utożsamiono z innymi Zygmuntami.

## S272 — nowy warunek wyszukiwania w dostępnej kopii

Ręcznie przejrzano nazwiska i początki imion obrazów136–247 (112) w **PTG86616**, szukając nowego „Zygm.”, nie powtarzając dotychczasowej kwerendy Czesława/Janiny/Agnieszki. Nie zaobserwowano Zygmunta Chmielewskiego w tym zakresie. Rok1938/2–134 nie został ponownie zbadany według tego kryterium. Podglądy19arkuszy w `work/s32/86616_zygm`, oryginały w `work/s21/ptg1938`. Nie przedstawiać tego jako braku osoby wŁodzi.

Obejrzano również1(strtytułowa) i248(poświadczenie254stron, data12VII1937), dotąd nieodczytane. Data poświadczenia to nie okres wpisów. Obraz247 kończy się nr2223/16X1939. WPTG248obrazów nie oznacza pełnej zgodności ze254numerowanymi stronami fizycznej księgi. Pozostałe rubryki odczytano tylko w10wybranych wierszach, nie wszystkich112obrazach.

Wybrane wiersze (data DOB jest pierwszym wierszem komórki, zwykle powyżej wysokości nazwiska; nie brać daty następnej osoby):

| Obraz/nr | Odczyt | DOB/miejsce | Wydanie/adres |
| --- | --- | --- | --- |
|186/1008|StefanChmielewski|1VII1898,m.Koło|18IV1939,Niecała9|
|193/1144|KrystynaChmielewska|28X1922,Łódź|6V1939,Oszmiańska18a|
|195/1197|WładysławaChmielewska|6XI1894,Dzierązna pow.sieradzki|12V1939,Niecała9|
|199/1275|Abram-MordkaChmielewski|1XII1892,Włoszczowa|22V1939,Zawadzka15|
|205/1398|Josek-HerszChmielewski|23III1903,Włoszczowa|5VI1939,Północna19|
|214/1576|AdamChmielewski|2IX1902,Łódź|26VI1939,Grodzieńska39?|
|214/1577|BronisławaChmielewska|10VIII1910,Łódź|26VI1939,Grodzieńska39?|
|221/1703|HelenaChmielewska|4VIII1919,RakowaGóra pow.radomszczański|10VII1939,Smocza28|
|232/1938|JudaChmielewski|4I1919,Włoszczowa|4VIII1939,Zawadzka35|
|239/2064|StanisławChmielewski|15II1912,Łódź|19VIII1939,Łączna57|

Brak podanych rodziców i nowej relacji doMarysi. Nie dopisywać małżeństwa Stefan/Władysława lub Adam/Bronisława na podstawie adresu i sąsiedztwa. Adam nie jest Adolfem; Abram-Mordka nie jest Adamem-Jerzym z szybkiej selekcji.

## Ważne nowe odpowiedzi z poczty — odczytano13XI, nie wysyłano wiadomości

Pełna prywatna kopia odpowiedzi i nagłówków jest w ignorowanym `work/audyt-github-2026-11-13/wiadomosci_PROJEKT_PRYWATNE.json`; do publicznego repo tylko minimalne wypisy bez danych kontaktowych żyjących. Zachowaćhash/IDwiadomości i daty źródłowe; nie publikować pełnych maili.

1. **C10/Zarzew**, Gmail1a1bf32ba460d34a,9XI2026 08:25+01. Odpowiedź: „Czesław Chmielewski urodził się18.02.1982r.” i „chyba nie chodzi o tego zmarłego”. To sprzeczne z pytaniem o zgon16I1981; **nie poprawiać samowolnie1982na1882, nie wpisywać tej daty jako DOB, nie zamykać H005**. Brak danychWitolda. ProponowaneS322 i korekta daty wymagającej wyjaśnienia.
2. **C62/CzesławaZarzew**, Gmail1a1bfa1f45186824,9XI10:27+01. Administracja podaje **20XI1922–3X1999**, więcej danych w karcie zgonu nie ma. Pytanie dotyczyXLV/1/19; wysłany8XI23:06followup jest cytowany w odpowiedzi. **To C62, nadal nie utożsamiona z ciociąP31**. Brakmęża,syna,nazwiskarodowego. ProponowaneS323. Nie dopisywaćDOB/zgonuP31.
3. **C17/JaninaSzczecińska**, Gmail1a1c058ebb54f1b1,9XI13:46+01. Administracja odpowiada „Niestety nie jest to ta osoba” na cytowane pytanie7XI11:52:55 oJaninęPoprawkę12V1910/rodziceJózef/Marianna i kandydata4III1992VIII/5/29. **C17 nie pasuje wg administracji**, brak odczytu ich metryki i konkretnych danych odmiennej osoby. Uaktualnić M09 — stary statusniewysłane nieaktualny; najlepiej sprawdzić pełnywątek/SENT. ProponowaneS324.
4. **WBP/Tomasz**, Gmail1a1c53d1f3d41b75,10XI12:34+01. Przeszukano „DziennikŁódzki WiadomościDnia” oraz „ExpressIlustrowany”, bez szukanej informacji. Odpowiedź nie wymienia numerów i stron; nie przypisywać jej pełnego pokrycia wszystkich lat. Nie jest dowodem braku zgonu/rodziny. ProponowaneS325.

## Uzupełnienie audytu: linki do sesji GitHub, treść niedostępna

Gmail13XIujawnił15powiadomień GitHub z9XI o sesjach w zadaniu `a67ca540-d0c4-42d1-b8b7-5b6f7b07ad5f`, m.in.:

- UpdatingClaude'sactionsinthelog, sessioncfb268aa-cf16-4919-9efd-daed04829560, ukończona.
- ReviewingClaude'scontributionsandprogress, sessionccf4325d-3944-4c7b-991f-d30b1c63b1bb, ukończona.
- CreatingfolderforClaudedziennik, session535e06b6-58ae-4380-9447-75d6ba143480, anulowana.

Dokładne linki w odczytanych powiadomieniach. Próba otwarcia pierwszego przez web zwróciła404. Łącznik GitHub nie obsługuje endpointów/tasks; brak narzędzia sesji agenta. Nie odczytano treści i nie wolno twierdzić, że w niej nie ma odkryć. To rozszerza audyt poza pliki/gałęzie; uzupełnić wysłany RAPORT.md osobnym commitem, zachowując pierwszy stan. Odpowiedź na dobrowolne pytanie o podsumowanieClaude nadal nie wpłynęła. Nie wysyłać promptów doCopilota ani wiadomości doosób bez zgody.
