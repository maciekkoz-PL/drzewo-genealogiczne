# Etap 35 — Chrzypsko i trop meldunkowy

13.11.2026. Nie ustalono imienia brata Bogusława ani rodziców właściwego Piotra. Nie dodano relacji rodzinnej do drzewa. Nie wysłano wiadomości ani wniosku.

## Nowy odczyt całego inwentarza

S317 opisywało zespół gminny Chrzypska 92/60/0 ogólnie. Tym razem udało się odczytać **wszystkie 102 wiersze listy jednostek**, z pełnymi sygnaturami, datami, tytułami i adresami. S326 jest tym szczegółowym odczytem tego samego zespołu, nie niezależnym świadectwem rodzinnym. Wszystkie 102 jednostki mają w tabeli zero skanów. Zapis: [CSV](zrodla/inwentarz_102.csv), [surowe tabele](zrodla/tables_all.json), [tekst listy](zrodla/units_all.txt).

| Sygnatura | Dokładny tytuł | Daty | Rekord |
| --- | --- | --- | --- |
| 92/60/0/3.4/84 | Ewidencja i kontrola ruchu ludności | 1945–1946 | [1895417](https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/1895417) |
| 92/60/0/3.4/85 | Ewidencja i kontrola ruchu ludności | 1947 | [1895418](https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/1895418) |
| 92/60/0/4.1/89 | Sprawy ewidencji i ruchu ludności | 1951 | [1914116](https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/1914116) |
| 92/60/0/2.1/14 | Statystyki handlu, przemysłu, zakładów, ludności, gruntów na 1 I 1939 | 1939 | [1895345](https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/1895345) |

Karty85,89,14 otworzyły się w przeglądarce: dokumentacja aktowa, zero skanów, brak dodatkowej treści opisu. Karta84 zwróciła niedostępny portlet; jej tytuł i daty pochodzą z poprawnie odczytanej tabeli. Nie ustalono, czy teczki84–85/89 zawierają imienne księgi lub tylko sprawy administracyjne. Nie należy obiecywać, że są tam Chmielewscy. Statystyka1939 również nie jest automatycznie spisem mieszkańców.

Przejrzano też pozostałe tytuły. W części przedwojennej nie ma jednostki nazwanej księgą meldunkową z1936. Są m.in. Bezrobocie1937–1938 (sygn.30), księgi podatkowe oraz wybory. Brak takiego tytułu w tym inwentarzu nie rozstrzyga o zachowaniu ksiąg w innych zespołach. Zespół nie daje obecnie skanów do sprawdzenia chłopca C101 z1936. Nie utożsamiono C98/C100/C107 z P03 ani C99 z P06.

## Drugi zbadany zasób i wyniki negatywne

S327: pobrano publiczny plik [AGOFF nmdatadb](https://neumark.agoff.de/nmdatadb), 356577 bajtów, SHA256 w logu. Po rozkodowaniu encji przeszukano Chmielew…, Chmielow… i Chrzypsk…. Brak pierwszych dwóch rdzeni. Trzy wiersze Chrzypska dotyczą Franciscy Grzesiak/Ziolett1858 i Paula Lucha1864, ze źródłem Postzustellungsurkunden. Nie są połączeniem z badaną rodziną. To sprawdzenie jednego pliku, nie pełnych zasobów AGOFF. [Zakres](zrodla/agoff_zakres.json).

Kwerendy nazwiska z Chrzypskiem i Łężcami nie dostarczyły nowego rodzinnego identyfikatora. Wyniki geograficzne dotyczą też miejscowości na Opolszczyźnie; nie utożsamiono ich z miejscowością z meldunku. Nie rozszerzano przypadkowych rodzin imienników.

## Odtworzenie dostępu

Bezpośrednie warianty parametrów portletu zawodziły. Skuteczna droga w jednej sesji Chromium: otworzyć opis zespołu22441, kliknąć link zawierający `nameofjsp=jednostki`, następnie wybrać rzeczywisty link „200” z otwartej listy. Surowe408odnośników to cztery odnośniki na jednostkę, **102unikalne URL**, nie408jednostek. Zachowano logi nieudanych prób. Nie powtarzać teraz sprawdzenia dostępności tylko z powodu wcześniejszego komunikatu o niedostępnym portlecie.

## Plan kontynuacji i otwarte pytania

1. Trop Stocka12 → ChrzypskoMałe, C98/C107, pozostaje porównaniem adresowym; potrzebne DOB, rodzice lub żona. Nie przyjmować rodzinnego związku z wpisami Grabowa20 na podstawie samej geografii.
2. C101 nie ma imienia, DOB ani podanych rodziców. Najbardziej rozstrzygające byłyby załączniki zgłoszenia2656/1936 lub własny akt dziecka. Nie nazywać go odnalezionym bratem Bogusława.
3. W Chrzypsku trzy teczki ewidencji są powojenne i bez skanów. Ich zawartość imienna jest niepotwierdzona. Ewentualne sprawdzenie fizyczne powinno najpierw ustalić charakter dokumentacji; kontakt pozostaje niewykonany i wymaga osobnego polecenia.
4. Dalsza droga online powinna dotyczyć innego zachowanego zespołu lub dokumentu osobistego łączącego adres z datą urodzenia. Nie ponawiać przeglądu102tytułów ani AGOFFnmdatadb bez zmiany zakresu lub kryterium.
5. P10/C19, P11 oraz H017 nadal otwarte; S238/Piotr syn Józefa pozostaje innym nieustalonym identyfikacyjnie wpisem. Tomasz ma dane zREL018, bez ustalonej matki. Nie dodawać wpisu o przełomie do kroniki.

Excel: dopisano S326–S327, L339–L341 i pliki dowodowe. Wszystkie wcześniejsze komórki zachowano; kopia bazy sprzed zmian i wynik walidacji są w tym katalogu. Dokładne frazy w [rejestrze kwerend](KWERENDY.md).
