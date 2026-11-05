# Stan badań — etap 04, 05.11.2026

Rodzice Bogusława Kazimierza Chmielewskiego, urodzonego 25.04.1943 w Łodzi, są wymienieni w fotografii jego odpisu małżeństwa II-1592/1982: **Czesław Chmielewski i Janina Poprawka** (S086). To bezpośredni dowód dokumentarny nazwisk rodziców. Nie ma podstaw do przypisywania mu statystycznego wyniku „99%”.

Dodatkowo sprawdzamy, czy są dokładnie parą z aktu 110/1936, z datami urodzenia 03.07.1909 i 12.05.1910 (H017). Zgodność obojga imion, nazwisk, rzadkiego nazwiska rodowego i Łodzi jest mocna. S086 nie zawiera dat urodzenia rodziców. Nowe wyszukiwanie nie znalazło konkurencyjnej pary w dostępnych indeksach, ale nie zastępuje dokumentu łączącego daty rodziców z synem. H017 pozostaje otwarta; pozostałe gałęzie wstrzymane.

## Wykonane badania

- **S106 Geneteka:** naprawiono odczyt API. Dawny zestaw parametrów zwracał count>0 przy pustym data nawet dla znanego ślubu 1936. Pełne parametry DataTables, rozgrzana sesja i nagłówek X-Requested-With dały prawidłowy wynik kontrolny. Zmieniono kilka elementów jednocześnie; nie ustalono osobnej przyczyny błędu. Zapisano kontrolę i wszystkie zapytania.
- 66 zapytań: kontrola znanego aktu, korekta dawnego S083, Bogusław 1942–1944 Łódź oraz 63 zapytania (21 regionów × śluby 1880–1960, urodzenia 1930–1960, zgony 1930–1990) o parę Czesław Chmielewski–Janina Poprawka. Odpowiedzi mają kompletne data względem count. Jedynym trafieniem pary jest ślub 110/1936.
- Dalsze 21 zapytań o same nazwiska małżonków Chmielewski–Poprawka, śluby 1880–1960, również wskazuje wyłącznie ten akt. To **unikat w przeszukanych indeksach**, a nie dowód unikalności w całej ludności Polski. Regiony: 01ds,02kp,03lb,04ls,05ld,06mp,07mz,71wa,08op,09pk,10pl,11pm,12sl,13sk,14wm,15wp,16zp,21uk,22br,23lt,25po.
- **Korekta S083:** jeden wynik zgonu nazwiska Chmielewski w 1988 to Helena Chmielewska, akt 14, Petrykozy, miejsce zgonu szpital Opoczno. Nie Bogusław. Bez dopisania jej do rodziny.
- **S107 IPN:** przeczytano wszystkie 50 wyników zapytania nazwiskowego Chmielewski Bogusław, pięć stron. Brak zidentyfikowanego ojca Marysi. Dostępna teraz pełna karta C33: IPN Ld 0216/10 t.1/29, OM-0102/76, Skierniewice 1975–1976, 1 tom/9 stron. Katalog nie podaje DOB, rodziców ani adresu; nie oglądano dziewięciu stron akt. C33 nadal niezidentyfikowany. Próby wyszukania daty przekierowują do formularza bez kryterium — **nie są ujemnymi wynikami kwerendy**. Nie ukończono dawnego zbioru 73 wyników daty.
- **S108 Timenote:** wyszukiwarki nazwiskowe i listy dni urodzenia/zgonu. Pierwsze strony zwracają 20 Janin, 20 Czesławów i 10 Bogusławów; to odczytane strony, nie gwarancja całego zasobu. Brak zidentyfikowanego P02/P03/P04. Janina 10.08.1916–04.03.1992 ma grób na Majdanku w Lublinie. **Nie przypisywać tej daty urodzenia C17 ze Szczecińskiej w Łodzi**, mimo tego samego dnia śmierci! Nowy profil Janiny ur. 1910, zm. 2001 wymaga odczytu; nie pobrano go przed blokadą.
- **S109 WBP:** bezpośrednia wyszukiwarka pełnotekstowa działa. „Bogusław Chmielewski” daje znany S041 (ogłoszenie studenta UŁ 1976), bez nowej identyfikacji. „Janina Poprawka” bez trafień; „Janina Chmielewska” 11 wydań; połączenie fraz „Czesław Chmielewski” i „Janina” 5 wydań; „Bogusława Chmielewskiego” Kronika Miasta Łodzi 2010/4. Zapisano listy i linki. **Nie pobrano ani nie przeczytano tych nowych gazet**, brak dowodu rodzinnego z samych trafień OCR.
- **S110 WGM:** publiczna karta sw.1319650 Janiny Chmielewskiej ur. ok.1910 dotyczy ślubu 17.11.1935 Postoliska, akt64; inne dane rodzinne. Nie utożsamiono z Janiną Poprawką ze ślubu 1936. Nie korzystano z płatnego dostępu.

## Ograniczenia techniczne i zapis

Wcześniejsze próby narzędzia web z polem search_query zamiast system2_search_query zachowano w JSON. Nie traktować ich jako udokumentowanych ujemnych odpowiedzi na wszystkie żądane zapytania. Późniejsze zapytania używają prawidłowego pola; oznaczenia plików zachowano. Surowe pliki są kopiami odpowiedzi, a nie dowodami tożsamości.

Kolejne pobieranie (skrypt new_leads.py: gazety, profil 1910 i katalogi SwA) **nie zostało uruchomione**: automatyczna kontrola zatwierdzania zgłosiła limit użycia i brak możliwości wykonania kontroli, nie ocenę niebezpieczeństwa. Nie obchodzono blokady. Kopie dotychczas pobranych materiałów zachowano z SHA256. Nie kontaktowano osób ani instytucji, nie składano wniosków, nie płacono.
