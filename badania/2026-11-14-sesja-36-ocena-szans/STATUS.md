# Etap 36 — ograniczone sprawdzenie dokumentów i ocena dalszej pracy

14.11.2026. Użytkownik zwrócił uwagę na koszt kolejnych bezskutecznych sesji. Nowe sprawdzenie ograniczono do **trzech dokumentów Arolsen, sześciu obrazów**, wybranych z wcześniej pobranego indeksu S313. Nie uruchamiano nowych kwerend wyszukiwarek internetowych ani nowych zleceń archiwalnych. Nie odnaleziono brata Bogusława ani nowego połączenia z Piotrem.

## Co faktycznie odczytano

**S328 — DocID82491868, wykaz poszukiwanych polskich dzieci S.L.No.1003C, 9VIII1948.** Sprawdzono nagłówek pierwszej strony i sześć wpisów20–25 na stronie2. Zdzisława1V1931/Łódź ma rodziców Jana i Natalię; Krystyna5VIII1928 — Feliksa i Genowefę; Ryszard(Longin)9XI1940 — Longina i Irenę (nazwisko ojca niepewne). Dla Czesławy30V1932 podano tylko matkę Juliannę, dla Piotra25VI1929 tylko matkę Czesławę, dla Stanisławy Kazimiery17XI1944 tylko matkę Zofię. Wiersze dotyczą różnych rodzin. Nie ma zapisu pary Czesław/Janina. **Pustej rubryki ojca nie potraktowano jako wykluczenia przyrodniego rodzeństwa.** Piotr1929 nie odpowiada wiekowi P10, ale nie wskazuje też, kto jest P11. Nie powiązano matki Czesławy z ciocią Czesią.

**S329 — DocID66782464, obie strony karty Zenona5VIII1937.** W polach rodziców: Adam Chmielewski i Maria z domu Przybyłowicz. Dopisek wyraźnie wymienia ojca Adama, matkę Marię i siostrę Krystynę. Miejscowość wpisano jako KUSNICA, prowincję POZNAN; nie wybrano konkretnej współczesnej wsi. Oboje rodzice mają inne imiona niż rodzice Bogusława. Nie ma podstaw do identyfikacji jako jego biologicznego brata według znanych danych.

**S330 — DocID66782345, obie strony karty Tadeusza18IV1935, Opoczno/prowincja Łódź.** W indeksie imię zapisano jako Jadensz. Ojciec Władysław Chmielewski, matka Kazimiera z domu Chmiel. Również nie pasuje do brata po Czesławie lub Janinie. Nie rozwijano odrębnej rodziny Władysława/Kazimiery. Pierwszy GET zwrócił503; jedno ponowienie dało200 i dwa obrazy. Błąd503 nie był wynikiem genealogicznym.

Pełne odczyty potrzebnych rubryk: [ODCZYTY.json](zrodla/ODCZYTY.json). [Dobór i zakres](zrodla/DOBOR_I_ZAKRES.json) zawiera SHA indeksu i konkretne wiersze, z których wybrano dokumenty. Nie jest to nowy przegląd wszystkich4773pozycji ani wszystkich dokumentów dzieci. Nie dodano tych osób do drzewa rodziny.

## Źródła i lokalne oryginały

- https://collections.arolsen-archives.org/en/document/82491868 — dwa obrazy wykazu, sygnatura6.3.1.2.
- https://collections.arolsen-archives.org/en/document/66782464 — karta DP Zenona, sygnatura3.1.1.1.
- https://collections.arolsen-archives.org/en/document/66782345 — karta DP Tadeusza, sygnatura3.1.1.1.

[Manifest lokalnych oryginałów](zrodla/manifest_lokalnych_oryginalow.json) podaje dokładne URL każdego obrazu, SHA256, rozmiar i lokalną ścieżkę. Dziewięć plików HTML/JPG przechowano w `work/s36/oryginaly/`, poza publicznym repozytorium. Repo zawiera odczyt danych potrzebnych do porównania oraz dane do odtworzenia kopii. Przy zmianie środowiska należy pobrać te konkretne URL, zamiast ponawiać wyszukiwanie nazwiska.

Zapytanie do poczty dotyczące rodzinnych odpowiedzi po12XI zwróciło0wiadomości; dokładny zakres w [DOSTEP.json](zrodla/DOSTEP.json). To wynik konkretnego zapytania, nie audyt całej poczty. Nie wysłano wiadomości, nie złożono wniosku ani nie wniesiono opłaty.

## Ocena opłacalności następnego kroku

**Rekomendacja: przerwa w szerokich kwerendach internetowych do uzyskania nowego identyfikatora rodzinnego.** Ostatnie sesje przynosiły głównie opisy katalogowe, wyniki negatywne i imienników. W tej sesji oryginały pozwoliły porównać rzeczywistych rodziców dzieci, ale nie dały rodzinnego łącznika. Nie ma podstaw, by obiecywać przełom po kolejnej serii samych nazwisk. Nie stwierdzono wyczerpania wszystkich istniejących źródeł; ocena dotyczy uzasadnienia kolejnych wydatków przy obecnych danych.

Najbardziej wartościowym dokumentem pozostaje **odpis zupełny aktu urodzenia Bogusława Kazimierza Chmielewskiego, 25IV1943, Łódź**. S086 już podaje jego rodziców Czesława Chmielewskiego i Janinę Poprawkę. Nowy dokument może dostarczyć dat, wieku, pochodzenia lub adresu rodziców i pomóc domknąć H017. Zakres historycznego aktu jest jeszcze nieznany. Sam akt urodzenia nie musi wymieniać rodzeństwa.

Brak PESEL nie zamyka drogi osobistej/listownej. Wcześniej odczytano urzędowy formularz Warszawy z polem „PESEL (jeśli jest znany)” i sprawdzono procedurę Łodzi: [S105, gotowy niewysłany szkic](../2026-11-05-sesja-03-polaczenie/S105_WNIOSEK_I_AKTA_1982.md), [S082, procedura Łodzi](../2026-11-05-sesja-01/S082_USC_bez_PESEL.md). Nie tworzono kolejnego szkicu. W istniejącej dokumentacji jest też rozbieżność kategorii opłaty33/39zł dla historycznego aktu; nie wybrano stawki i nie zapłacono.

## Plan kontynuacji bez powtórek

1. Po otrzymaniu dokumentu Bogusława odczytać wszystkie rubryki i przypiski. Porównać rodziców z Czesławem3VII1909/Rogoźno i Janiną12V1910/Socha. Nie dopisywać danych, których akt nie zawiera.
2. Jeżeli dokument poda adres rodzinny, sprawdzić odpowiadającą mu ewidencję gospodarstwa pod kątem imion dzieci. Dopiero wtedy wybierać konkretną teczkę lub nowy zakres skanów. H002 pozostaje otwarta; brat mógł być przyrodni.
3. Aneksy1936 nr530 i2656, teczki26200/26204, pozostają źródłami bez skanów (S270). Wpis C101 nie ma imienia ani podanych rodziców. Zawartości aneksów i tożsamości rodziny nie potwierdzono; nie zamawiać przypadkowych teczek na podstawie samego nazwiska. Kontakt wymaga osobnego polecenia.
4. Nowa informacja rodzinna lub dokument identyfikujący właściwego Piotra może wznowić kierunek H003. Nie ponawiać ogólnych fraz policyjnych, znanego grobu Tomasza, wykazu S238 ani katalogu102jednostek Chrzypska.
5. S328–S330 są już odczytane. Brak wpisanych rodziców w indeksie S313 nie oznacza braku rodziców na oryginale — te trzy dokumenty pokazują granicę danych indeksowych. Nie traktować pustych pól jak wyników wykluczających.

Excel, dziennik kwerend i dwa zalecenia w hipotezach zaktualizowano. Zmiany wcześniejszych komórek są w osobnym rejestrze; kopia sprzed etapu i walidacja zachowane. Publiczne drzewo i kronika pozostają bez nowego wpisu, ponieważ nie przybył potwierdzony fakt rodzinny.
