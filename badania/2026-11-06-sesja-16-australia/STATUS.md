# Etap 16 — australijscy bracia i dalsze pokolenia

Stan 06.11.2026. Kontynuowano poszukiwania potomków rodzeństwa dziadka Czesława. **Znaleziono rodzinne ogłoszenie z konkretnymi imionami dalszej rodziny Raya. Nie potwierdzono jeszcze, że cała gałąź jest rodziną Marysi, ani aktualnego życia każdej wymienionej osoby.**

## Co udało się ustalić

| Osoba / rekord | Nowy dowód | Co nadal wymaga potwierdzenia |
| --- | --- | --- |
| C75 Ernest (Ernie) Chmielewski | **20.11.1947–27.11.2024**, pełne ogłoszenie i rejestr GCT; pogrzeb06.12.2024 | Tożsamość z synem emigranta C72 jest bardzo prawdopodobna (H036), lecz rekordy pozostają osobno. |
| C79 Ray / Raymond (Chima) Chmielewski | **06.10.1946–19.11.2020**, nekrolog podpisany przez **brata Erniego i Rene** | Tożsamość z Romanem C71 jest bardzo prawdopodobna (H040). Brak dokumentu łączącego imiona Roman/Raymond i bezpośrednio podającego rodziców. |
| Rodzina C79 | Żona **Rose**; trzy pary **Michelle/Chris, Simone/Nikki, Nicole/Dean**; wnuki **Rebecca, Robert, Max, Ebony, Tori, Marcus, Stella** | Nazwiska i daty niepodane. W każdej parze nie ustalono, kto jest dzieckiem Raya, a kto jego partnerem; wnukom nie przypisano rodziców. Ogłoszenie z2020 nie jest aktualnym dowodem życia. |
| C95 Roman Chmielewski z cmentarza | Zgon **21.01.1997**, **77lat**, pochówek24.01.1997 | Prawdopodobny emigrant C69 (H041), ale rejestr nie podaje daty urodzenia ani rodziców. |
| C96 Anna Theresia Chmielewski z cmentarza | Zgon **07.02.1987**, **57lat**, pochówek11.02.1987 | Prawdopodobna Anna C70 (H042), ale rejestr nie podaje daty urodzenia ani nazwiska rodowego. |

**Główna luka H035 pozostaje:** brat Czesława P12 i emigrant C69 mają zgodne pełne imię/nazwisko i datę06.06.1919, ale nie znaleziono rodziców emigranta. Zapis jego miejsca urodzenia nadal brzmi „Pol./Rezegno”; nie poprawiono go na Rogóźno. Nowe pokolenia australijskie nie zastępują dowodu tej tożsamości. Rodzice P12 z aktu226/1919 to Wincenty i Agnieszka z Miszczyszynów (S061).

## Dokładne źródła i odczyty

**S195 — [ogłoszenie Ernesta,6259122](https://www.mytributes.com.au/notice/funeral-notices/chmielewski-ernest-ernie/6259122/).** Pełna treść odczytana narzędziem web: daty20.11.1947–27.11.2024, Geelong Advertiser, data zamieszczenia online29.11.2024, pogrzeb06.12.2024 w Tuckers Highton, następnie prywatna kremacja. Nie podaje rodziców lub potomków. Wcześniejszy indeks Ryerson S187 wskazuje druk30.11.2024 — zachowano ten zapis historyczny, nie zmieniono daty indeksu na datę internetową. Zwykły urllib w tej sesji nadal403; poprawny pełny odczyt przez narzędzie web nie oznacza, że pobrano oryginalny HTML tym samym sposobem. Kopia odpowiedzi: `zrodla/ernest_6259122.txt`, pełna odpowiedź także w `kwerendy_i_odczyty_01.json`.

**S196 — [nekrolog Raya od brata,5589602](https://www.dailytelegraph.com.au/tributes/notice/death-notices/chmielewski-ray/5589602/).** Geelong Advertiser25.11.2020. Pełna data06.10.1946–19.11.2020; podpis Ernie/Rene i wyraźne określenie Erniego jako brata. Odczyt Firecrawl **basic**, HTTP200, bez logowania lub obchodzenia ograniczeń. Kopia `zrodla/ray_5589602.md`. **Rene C80 nie otrzymała/otrzymał domyślnego nazwiska, płci ani statusu małżonka**; samo współpodpisanie nekrologu tego nie dokumentuje.

**S197 — [rodzinne ogłoszenie Raya,5589271](https://www.mytributes.com.au/notice/funeral-notices/raymond-chima-chmielewski/5589271/).** Geelong Advertiser25.11.2020; pogrzeb27.11.2020 o10.00 w Allambe Memorial Park, Nerang, Queensland. Wprost wymienia żonę Rose, trzy pary dzieci i ich partnerów, siedmioro wnuków oraz prawnuki bez imion. Zapisano każdą nazwaną osobę odrębnie, **bez nadawania nazwiska Chmielewski**. Nie utożsamiono Nikki z Nicole. Linie sześciu osób z kręgu dzieci i ich partnerów są ogólnymi relacjami rodzinnymi, nie sześcioma pewnymi liniami biologicznego rodzicielstwa. Rose nie została automatycznie matką dzieci Raya. Kopia `zrodla/ray_5589271.md`.

**S198 — [ogłoszenie znajomych Raya,5588385](https://www.dailytelegraph.com.au/tributes/notice/death-notices/chmielewski-ray/5588385/).** Geelong Advertiser21.11.2020, zgon19.11.2020. Duncan/Nancy, Buck, Arthur, Mac, Nick to znajomi; nie dodano ich jako krewnych. Kopia `zrodla/ray_5588385.md`. Ogłoszenia S196–S198 dotyczą zgodnego nazwiska, zgonu i kontekstu Geelong; wariant Raymond pochodzi z S197, a pełna data urodzenia z S196. Nie są trzema niezależnymi dowodami polskich rodziców.

**S199 — [Geelong Cemeteries Trust, formularz Family History Search](https://gct.net.au/family-history-search/).** Wprowadzono nazwisko Chmielewski, wszystkie lokalizacje. Właściwe zapytanie formularza: `POST https://gct.net.au/wp-admin/admin-ajax.php`, `action=deceased_search&siteId=&pageNo=1&pageSize=5&surname=Chmielewski`. **3/3wyniki**, jedna strona. Oryginalna odpowiedź JSON: `zrodla/gct_response_58.bin`; wyrenderowany formularz `gct_results.html/.txt`; parametry i status200 w `gct_network.json`.

| PersonId | Osoba | Data urodzenia | Zgon | Wiek | Pozycja |
| --- | --- | --- | --- | --- | --- |
| 38035 | Roman Chmielewski C95 | brak |21.01.1997|77|WST-LAWN-05-808-518-02|
| 940272 | Ernest Chmielewski C75 |20.11.1947|27.11.2024|77|WST-LAWN-05-808-518-03|
| 36197 | Anna Theresia Chmielewski C96 | brak |07.02.1987|57|WST-LAWN-05-808-518-01|

Wszyscy: **Geelong Western Public Cemetery, Lawn05, Grave518, LocationId75607**. Wiek Romana77lat w1997 pasuje do osoby urodzonej06.06.1919, ale pozwala na przedział roczny, nie dokładną datę. To samo dotyczy wieku Anny57lat przed jej możliwymi urodzinami19lutego1987. **Wspólny grób nie dowodzi samodzielnie małżeństwa lub ojcostwa.** Nie podano zdjęcia (`PrimaryImageUrl` puste), imion rodziców lub miejsca urodzenia. Funkcja Details&Map otworzyła publiczny widok z referencjami Anna172189, Roman174027, Ernest1045451; HTML/mapę zapisano w `gct_public_map.html/.txt/.json`. Nie używano funkcji email/SMS. Publiczny rejestr nie ujawnia właścicieli prawa do grobu i nie próbowano uzyskać ich danych.

## Pozostałe kwerendy i ograniczenia

- **S200, Arolsen:** cztery nowe zapytania, odpowiednio **137/1/3/1wierszy**: nazwisko+1919 bez imienia, Anna1929, Roman1946, Ernest1947. W137wierszach z synonimami jedyny Roman i jedyna data06.06.1919 to znany Doc81766762. Nie odnaleziono nowego dokumentu z rodzicami. Wyszukiwarka może zwracać osoby z całego pasującego dokumentu, więc przy Roman1946 wystąpił także ojciec1919 i znany starszy imiennik81673879. To nie137odczytanych aktów. Zachowane parametry i odpowiedzi w `zrodla/arolsen/`.
- **S201, Tuckers:** nowy aktualny serwis ma inny mechanizm niż dawny WordPress. Odczytano prawidłowe parametry publicznego formularza; `Search=Chmielewski`, `funeralType=Past`, `brandCode=162` zwróciły **Results[]/Total0**. Ten wynik nie zaprzecza pogrzebowi z2024, potwierdzonemu S195. Próba publicznego CDX Wayback zakończyła się timeoutem, bez odczytu archiwalnej karty i bez kontaktu z zakładem.
- **S202, BDM Victoria:** [oficjalna instrukcja](https://www.bdm.vic.gov.au/search-your-family-history) podaje30lat od **rejestracji**, nie daty śmierci, dla historycznych zgonów. Aplikacja `my.rio.bdm.vic.gov.au/efamily-history/-` zwróciła200, lecz nie wyświetliła formularza; jej żądanie `efam/me` miało401. Nie obchodzono logowania. Nie przeczytano wpisu zgonu Anny1987 ani Romana1997. Nie kupowano dokumentów. Queensland403; Allambe503/timeout; AncestryAnna1987 i Find a GraveRoman403. Potencjalny zgon Romana1997 nie jest jeszcze dostępny tylko dlatego, że znamy jego datę; ewentualna dostępność zależy od daty rejestracji.
- **S203, Blue Circle1983:** pobrano pełny PDF **40 975 372bajty,390stron**. Odczytano trafienia na fizycznych stronach81,162,362; E.Chmielewski w golfie i ErnieChmie-lowski/Chmei-lowski w podpisie zmianyA, Waurn Ponds. Nie potwierdzono tożsamości z C75 i nie przypisano mu zawodu. **42to punkty,26handicap — nie wiek.** Nie deklarowano przeczytania wszystkich390stron. Pełny plik i tekst zapisane lokalnie.
- **S204, internet:** **33zapytania web,16wyszukiwań Firecrawl i3pełne odczyty Firecrawl basic**. Parametry: `parametry_kwerend.json`, całe odpowiedzi w `kwerendy_i_odczyty_01–04.json`. Początkowe próby częściowo pokrywały etap15; nie są niezależnym rozszerzeniem dowodu. Firecrawl wskazał konkretne nowe ogłoszenia. Nie przypisano krewnych z przypadkowych profili w Geelong ani nazwiska Riedlberger z niepasującej biografii1926–2020.
- **S204, Australian Cemeteries Index:** pierwszy parametr `surname` nie wypełnił formularza — nie uznano go za wynik. Poprawny `family_name=Chmielewski&search=Search` dał **9inskrypcji**, bez szukanej trójki. To ograniczony indeks; właściwy rejestr GCT dał wynik dodatni. Nie wyciągnięto wniosku, że grobu nie ma.
- Kontrola znanego oryginału S061 miała nowy cel: sprawdzenie późniejszego dopisku o emigracji/zgonie. Brak takiej adnotacji w widocznym marginesie; nie zmieniono wcześniejszego odczytu, nie powielano pliku. Nie wracano do przeczytanych skorowidzów Tomaszowa, grobu Tomasza ani pytań do rodziny o Piotra.

## Zmiany w bazie i drzewie

23arkusze zachowane. Dodano **S195–S204** (204źródła), **C79–C96** (96kandydatów łącznie), **R045–R059**, **E067–E070**, **H040–H044**, **L165–L176**, **F139–F150**, **T41/T42**, identyfikacje **V068/V069**. H035, H036 i H039 uzupełniono aktualną oceną; nie usunięto wcześniejszych źródeł. C75 otrzymał dokładne daty z nowego źródła, zamiast dawnego statusu samego indeksu. **Nie dodano P33, nie scalono P12/C69, C71/C79, C72/C75, C69/C95 lub C70/C96.** Q81 i REL-017 pozostają wolne.

Publiczne drzewo: **71kart,96relacji,9krótkich wpisów**. Nowe karty tylko na poziomie3; Rene oraz dwa nieutożsamione rekordy grobowe są poza kartami, a trop grobu opisano przy C69/C70. Wnuki są połączone z Rayem ogólnymi relacjami z treścią „wnuk/wnuczka”; brak zgadywanych rodziców. Układ i znane linie rodziców Marysi zachowane. [Plan dalszej pracy](PLAN_KONTYNUACJI.md). Wyniki kontroli i rzeczywista publikacja zostaną zapisane w plikach WALIDACJA/PUBLIKACJA tego katalogu.

**Scalenie zastanej witryny20:** źródło `3107418e9907d79245967fcd0948de825ae88fac` zawierało nowsze opisy relacji, mapy Berri/Mildura i portretC69. Zachowano te zmiany oraz obraz zS183. Zaktualizowano etykiety nowych relacji, aby nie nazywały partnerów dzieci synami/córkami i nie myliły wnuków z dziećmi. Snapshot i hash importu są w `zrodla/hosting20.html` oraz `hosting20_import.json`. Nie zastąpiono nowszej witryny starym szablonem.

Przed publikacją pojawił się jeszcze commit hostingu `12fe36549adda951315891e1910bf20820d03f4e`, dodający portret synaRomana zS184 i obsługę kadruSVG. Tę zmianę również scalono; oba portrety i aktualne dane są zachowane, bez nadpisania zastanych zmian. Metadane w `zrodla/hosting_son_import.json`.
