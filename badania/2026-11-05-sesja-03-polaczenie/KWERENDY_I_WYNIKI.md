# Kwerendy etapu 03 — po otrzymaniu odpisu S086

Data: **05.11.2026**. Jedyny cel: **H017**, dodatkowa identyfikacja rodziców wymienionych w S086 z parą ślubu 110/1936. Imiona i nazwiska rodziców są już udokumentowane; nie wracano do pytania o samo brzmienie imion, datę ani miejsce ślubu Bogusława.

## Dokumenty i indeksy

- [Arolsen — dokładny zakres i wyniki wszystkich nowych odczytów](AROLSEN_ODCZYTY.md): osiem dokumentów Janin, sześć Czesławów, łącznie **35 obrazów**. Wszystkie zachowano. DocID 89014476 nie udostępnił treści ani obrazu; tego dokumentu nie odczytano.
- Dwa nowe publiczne wyszukiwania API: **`Chmielewski 1910` = 90**, **`Poprawka` = 190**. Całe zwrócone listy indeksowe sprawdzono pod kątem danych Janiny. [Parametry i odpowiedzi](zrodla/arolsen_queries), [wykonany skrypt](kwerenda_arolsen.py). Brak zidentyfikowanej P04. To nie odczyt 280 obrazów ani dowód nieobecności osoby w archiwum.
- [S096 — obwieszczenie o książkach meldunkowych](S096_EWIDENCJA_LODNOSCI.md): pobrano cały ośmiostronicowy numer, odczytano konkretny blok na s. 6. Nie przeszukano całego rocznika.
- S097 — ustalono bibliografię Janik 2012, s. 187–195; odczytano spis treści. Pełny PDF wydawcy 404; treści artykułu nie pozyskano. Parametry kodowania URL i błędy w [dzienniku](zrodla/population/downloads.jsonl).
- [S105 — oryginalny druk Warszawy](S105_WNIOSEK_I_AKTA_1982.md) i S054 art. 26/45/60: odczytano procedurę i cały tekst druku. Przygotowano niepodpisany, niewysłany szkic pisma; nie wysłano zapytań ani wniosków.

## Dokładne frazy wyszukiwarki — nie powtarzać bez nowej przesłanki

Pełne zwrócone odpowiedzi są w plikach `h017_*.json`. Brak rozpoznanej rodziny w tych wynikach oznacza tylko brak dodatkowego łącznika w przeglądniętej odpowiedzi. Wyszukiwarka potrafi zwracać wyniki przybliżone mimo cudzysłowów; nie zgłoszono fałszywego wyniku „0 rekordów genealogicznych”.

Frazy dotyczące dokumentacji ludności i katalogów:

1. `"Litzmannstadt" "Einwohnermeldeamt"`
2. `"Łódź" "księgi meldunkowe" "1945"`
3. `"Łódź" "ewidencja ludności" "1940" "1945"`
4. `"Litzmannstadt" "Meldekartei"`
5. `"Janik" "Ewidencja ludności" "2012"`
6. `"Łódź" "kartoteka meldunkowa" "1945"`
7. `"Ewidencja ludności" "187–195"`
8. `"Rocznik Łódzki" "2012" "pdf" "Janik"`
9. `"Łódź" "akta meldunkowe" "1939-1945"`
10. `"Litzmannstadt" "Einwohnermeldeamt" "Archiv"`
11. `"Łódź" "Ewidencja dowodów osobistych" "nazwiska"`
12. `"Rocznik Łódzki" "59" site:roczniklodzki.uni.lodz.pl`
13. `site.lodz.ap.gov.pl "ewidencja" "1945" "Łodzi"`
14. `"Prezydium Policji w Łodzi" "ewidencja"`
15. `"Litzmannstadt" "Melderegister" Archiv`
16. `"Zarząd Miejski w Łodzi" "1945" "ewidencja ludności"`
17. `"Łódź" "książki meldunkowe" "1946"`
18. `"Miejska Rada Narodowa i Zarząd Miejski w Łodzi" "meldunkowe"`
19. `"Zarząd Miejski w Łodzi 1939-1945" "Melde"`
20. `"księgi meldunkowe" "Łodzi" "1943"`

Frazy dotyczące tożsamości i drogi do dokumentu:

21. `"Chmielewska" "12 maja 1910"`
22. `"Janina" "Poprawka" "Bogusław"`
23. `site.warszawa19115.pl "akta zbiorowe" "kopii"`
24. `Warszawa wydanie kopii dokumentu akta zbiorowe rejestracji stanu cywilnego`
25. `"Czesław Chmielewski" "Janina" "Bogusław" "Poprawka"`
26. `"Chmielewska" "12 V 1910"`
27. `"Bogusław Kazimierz Chmielewski" "1943" "1943"` — w wykonanym zapytaniu rok powtórzono; nie jest to nowy odrębny zakres dat. Nie ponawiać wariantów pełnych imion bez nowego źródła.

Przejrzano nowe wskazane opisy zespołów **39/222/0** i **39/646/0**. Nie znaleziono imiennej jednostki rodziny; opis ksiąg repatriantów nie stanowi dowodu, że rodzina była repatriowana. Nie rozpoczynano czytania przypadkowych obcych rodzin.

Otwieranie stron i wyszukiwanie w treści objęło bibliografię APŁ, spis Rocznika 59, PDF Kuriera 1946 (hasła księgi/meldunk/1939), ELI 2026/393 i warszawską procedurę. Niedostępne przez narzędzie były niektóre pełne PDF, publiczny opis Arolsen `2-1-7-1_10010013` i API Wayback dla starego `ewidencja_ludnosci.pdf`. Nie przypisywano im odczytanej treści.

## Co celowo pozostawiono bez powtórzenia

Nie pobierano ponownie 277 metadanych zgonów Łodzi 1940, nie czytano drugi raz stron C skorowidza 1943ax, znanych pięciu list Czesława 03.07.1909 ani nie szukano znanego grobu Tomasza. Dawne próby IPN, prasy 1988 i niedostępnych katalogów pozostają w poprzednim dzienniku z ograniczeniami. Dalszych przodków, rodzeństwa i Piotra nie badano.
