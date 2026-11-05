# S081 — jakie skany USC Łódź są rzeczywiście opublikowane w SwA

Oficjalny [zespół USC Łódź 39/2736/0](https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/165812), identyfikator **165812**, nazwa obcojęzyczna **Standesamt Litzmannstadt**. W odczytanych opisach występowało 1076/1077 jednostek oraz 277 skanów; opis materiałów tradycyjnych podawał także 1057 jednostek. Są to różne pola/snapshoty katalogowe, nie dowód utraty konkretnych akt. Dostępność zespołu określono jako częściową.

## Sprawdzenie pełnego manifestu opublikowanych obrazów

Z publicznego JavaScript przeglądarki skanów odczytano metodę pobierania plików całego zespołu, następnie wykonano zwykłe żądanie GET:

`https://www.szukajwarchiwach.gov.pl/o/pliki-api/pliki/zespol/165812/0/300`

Wynik zachowano w `zrodla/SwA_USC_165812_277_manifest.json`. Odpowiedź podaje **277 wszystkich skanów i 277 elementów**. Metadane **każdego z 277** wskazują:

- sygnatura **39/2736/0/-/26**;
- tytuł: akty zgonów osób wyznania mojżeszowego, nr **1–530**, pierwopis;
- rok **1940**.

**W tym publicznym zestawie skanów nie ma skorowidza urodzeń H1 1943.** Jest to wynik kontroli wszystkich metadanych opublikowanych obrazów, a nie odczyt 277 stron księgi zgonów. Nie pobierano tych nieadekwatnych do celu akt zgonu. Nie oznacza to, że poszukiwanego skorowidza nie ma w magazynie, USC, w zasobie innej instytucji albo poza tym kanałem publikacji.

## Ograniczenia pozostałych prób

Karty listy jednostek zespołu zwracały błąd portletu lub HTML ochronny zamiast spisu. Nie przejrzano wszystkich 1076/1077 opisów jednostek. Nie zgadywano numeru aktu ani identyfikatora jednostki. Próba oficjalnego PDF `https://www.lodz.ap.gov.pl/pict_/cyfrowe.pdf` dała 404, mimo zachowanego wyniku wyszukiwarki; nie uznano PDF za pobrany.

Skanoteka id4852 ma osobny kanał publikacji. Jej tom **1943ax** nadal obejmuje **01.07–31.12.1943** według odczytanej strony tytułowej. Nie powtarzano odczytu dawniej sprawdzonych stron 08–12. Pełny manifest SwA nie zastępuje katalogu PTG i nie czyni tomu PTG całorocznym.

Dzienniki: `USC_SwA_*.json`, `USC_*proba*.json`, `USC_i_digitalizacja_pobrania.json`, `SwA_nowe_pobrania_przegladarka.json`, `wyszukiwanie_web_15.json`. Próba dodatkowej weryfikacji metadanych jednostki Romana 1919 (37825045) dała HTML WAF; szczegóły w dzienniku. Potwierdzony odczyt jego aktu i oryginał JPG pozostają S061.

Najkrótsza droga dowodowa do rodziców Bogusława to nadal **odpis zupełny jego aktu urodzenia**, złożony przez uprawnioną osobę. Przygotowano szkic lokalny; nie złożono wniosku ani opłaty.
