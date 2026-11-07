# Tomasz P09 — kontynuacja z 7 listopada 2026

**Nie uzyskano nowej daty urodzenia, danych matki ani adresu Tomasza.** Przeprowadzono nowe, bezpośrednie kwerendy baz grobowych i oficjalnej wyszukiwarki MSiG. Znany grób w Starej Gadce nie został przeniesiony do innej lokalizacji; celem było uzupełnienie danych rejestrowych, nie ponowne szukanie cmentarza.

## Wyniki źródłowe

| Źródło | Faktycznie odczytany zakres | Wynik i granica |
| --- | --- | --- |
| S245 — BillionGraves globalnie | 6 wyników ścisłego imienia i nazwiska, jedna strona. Dodatkowo pierwsze20 wyników wariantu rozszerzonego. | Żaden ścisły wynik nie zgadza się z26.04.2001. Wyłączenie Exact przy imieniu zwraca też zupełnie inne imiona i146stron; nie odczytano146stron ani wszystkich kart/zdjęć. |
| S246 — Find a Grave | Pełna lista30wpisów na dwóch stronach,20+10, z datami i linkami. | Brak daty26.04.2001. Tomasz z Zarzewa zmarł04.03.1980 — to inna osoba. Wpisy to nie30pewnie odrębnych osób lub30odczytanych metryk. |
| S247 — Grobonet | Lista11regionów z wynikami; w regionie łódzkim1rekord, odczytany po przejściu do Rawy Mazowieckiej. Osobno formularz serwisu archidiecezji. | Wynik z Rawy:17.01.1914–12.06.1992, nieP09. Serwis o nazwie „Cmentarze Archidiecezji Łódzkiej” ma w formularzu tylko Bełchatów; nie potraktowano go jako spisu Starej Gadki. Nie odczytano wszystkich regionów. |
| S248 — BillionGraves, cmentarz292271 | Wszystkie23wpisy GPS i2OtherHeadstones z list dostępnych dla znanego cmentarza; licznik17obrazów. | Brak Tomasza na tej ograniczonej liście. To nie pełny spis cmentarza i nie17odczytanych inskrypcji. Brak rekordu online nie przeczy znanemu pochówkowi. |
| S249 — oficjalne MSiG | Rzeczywiste GET do publicznego API używanego przez formularz MS; daty2001-04-26–2026-11-07. Fraza bez cudzysłowów dała4pozycje, odczytano treść wszystkich4. | Upadłości2004,2019,2020,2023, bez łącznika zP09. Nie przypisano żadnej jego rodzinie. Ostatnie dwa ogłoszenia dotyczą tej samej sygnatury warszawskiej, więc nie są dwiema osobami. Wariant odmieniony „Tomaszu Chmielewskim” bez wyników. Nie jest to dowód braku jakiejkolwiek sprawy spadkowej. |

**Ważna korekta sposobu szukania MSiG:** cudzysłowy przy frazie dały pustą listę, a fraza bez cudzysłowów —4trafienia. Dlatego wcześniejszej pustej listy nie uznano za końcowy wynik. `SearchCount` oznacza liczbę stron, nie osób; odpowiedź1nie oznacza jednego trafienia. Dodatnia kontrola „spadku” zwróciła50wierszy pierwszej strony. Parametry i odpowiedzi zapisano. Próba strony0zwróciła400; poprawna numeracja zaczyna się od1.

Szczegóły czterech ogłoszeń:2004poz.961(sygn.V GU47/03,V GU48/03,V GUp1/04),2019poz.57704(V GU314/19,V GUp319/19),2020poz.40086 i2023poz.31372(obieXIX GU953/20,XIX GUp1020/20). Nie zachowano w repo pełnych tekstów z numerami PESEL, adresami domowymi ani zestawieniami zadłużenia niepowiązanych osób; zachowano metadane, dokładne URL i ocenę braku rodzinnego łącznika.

**S252 — dodatkowe źródła web:**12nowych zapytań, parametry w`zrodla/search_00.json`–`search_11.json`. Znaleziony tag„Tomasz C.”z2001po odczycie okazał się dotyczyć dymisji prorektorów19.11.2001, nie śmierci Tomasza. Innych anonimowych zdarzeń nie przypisanoP09. Nie powtarzano wcześniej zakończonej listy15kwerend. Firecrawl Interact zwrócił`INVALID_ARGUMENT`bez uruchomionej sesji; odczyt BG wykonano normalnym formularzem w Chromium. Strona MS w Chromium miała timeout; jej publiczny formularz i kod klienta pozwoliły wykonać właściwe odczyty API. iMSiG przekierował do Google, więc nie udawano wykonania natywnej kwerendy tego komercyjnego serwisu.

## Konkretny następny dokument

**S250:** oficjalna [strona Archidiecezji Łódzkiej](https://www.archidiecezja.lodz.pl/strona/cmentarze) podaje dla cmentarza pw. św. Maksymiliana Kolbego: **Gadka Stara, ul. Czartoryskiego62, tel.605631485**, kierownik **Małgorzata Lik**. Dane z katalogu zewnętrznego z innym nazwiskiem kierownika i starszym numerem nie są traktowane jako aktualny kontakt. Zapisano służbowy kontakt I16. Nie zadzwoniono ani nie wysłano wiadomości.

**S251:** pierwotne rozporządzenie z01.08.2001, Dz.U.90poz.1013, §3 przewidywało w księdze wieczystej osób pochowanych m.in.datę/miejsce urodzenia oraz imiona i nazwiska rodziców; §16 — przechowywanie bezterminowe. To wskazówka do zapytania o księgę, **nie dowód zawartości indywidualnego wpisu Tomasza**. Zmarł w kwietniu, a rozporządzenie powstało później i wchodziło w życie po14dniach od ogłoszenia. Nie zakładać, że jego wcześniejszy wpis ma komplet tych rubryk. Nie obiecywać dostępu do całej dokumentacji ani stosować nieaktualnego pierwotnego brzmienia jako dzisiejszej porady prawnej.

Przygotowano [niewysłane zapytanie o wpis](ZAPYTANIE_KSIEGA_POCHOWANYCH_NIEWYSLANE.md), z podaniem znanych dat i GPS, bez domysłów o przyczynie śmierci i bez żądania kontaktu do żyjącego dysponenta. Jego celem jest uzyskanie DOB, danych rodziców, daty pochówku i oznaczenia aktu zgonu, o ile są zachowane. Nadal dostępny jest wcześniejszy niewysłany wniosek o odpis USC.

## Zapis

Dodano S245–S252,L238–L245,F198–F205,I16,T54 i doprecyzowano H048. Bez nowej osoby, relacji, rodzinnego faktu lub zmiany daty. OryginalneZIPy i24arkusze zachowane; oba audytyCSV i pliki publicznego drzewa pozostały bez zmian. Nie ma nowego odkrycia do kroniki i nie ma potrzeby kolejnej publikacji strony. Poprzednia wersja24 zawiera aktualne daneTomasza.

Nie kontaktowano osób ani instytucji, nie zakładano kont, nie składano wniosków lub zamówień i nie dokonywano opłat. Brak nowego identyfikatora nie uzasadnia powtarzania tych samych list w kolejnej sesji.
