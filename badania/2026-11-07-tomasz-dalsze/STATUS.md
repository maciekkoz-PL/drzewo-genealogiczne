# Tomasz Chmielewski — dalsze kwerendy, 7 listopada 2026

**Nie uzyskano nowego potwierdzonego faktu o Tomaszu P09.** Nowe odczyty nie ustaliły matki, dokładnej daty urodzenia, adresu ani okoliczności śmierci. Przygotowano konkretne zapytanie do biblioteki o nekrolog, lecz **nie wysłano wiadomości**.

Punkt odniesienia: rodzinne REL-018 — Tomasz, syn Bogusława Kazimierza Chmielewskiego, przyrodni brat Marysi po ojcu, mieszkał w Łodzi, zmarł 26.04.2001 w wieku 30 lat. Jego grób w Starej Gadce jest już znany i sfotografowany. Warunkowy przedział urodzenia 27.04.1970–26.04.1971 wynika z wieku, nie zastępuje pełnej daty. Nie przypisano mu Marii Jankowskiej jako matki. Nie opublikowano prywatnych informacji o uzależnieniach ani nie przypisano ich imiennikom.

## TOM-D01 — dodatkowe formy nazwiska w MSiG

Przeszukano oficjalną wyszukiwarkę Ministerstwa Sprawiedliwości, pole `textInBody`, daty publikacji 26.04.2001–07.11.2026. Odczytano rzeczywiste odpowiedzi API i treść sześciu dodatkowych ogłoszeń.

| Zapytanie | Wynik |
|---|---|
| Tomasza Chmielewskiego | 9 ogłoszeń; następna strona pusta. |
| Chmielewskim 2001 | 0. |
| Chmielewski 26.04.2001 | 0. |
| Chmielewski 26 kwietnia 2001 | 0. |
| Chmielewski 1971 | 0. |
| Chmielewski 1970 | 0. |

Trzy z dziewięciu ogłoszeń pokrywały się z poprzednią kwerendą. Sześć nowych odczytów: ID **8783968, 1137092, 319713, 12435507, 19372515, 19396597**. Dotyczą spraw upadłościowych: TASA/Darłowo i sąd w Koszalinie, sprawy z Legnicy, Warszawy i Kielc. W żadnym odczytanym ogłoszeniu nie znaleziono rodzinnego łącznika z P09 ani daty zgonu 26.04.2001. Nie przypisano tych postępowań Tomaszowi z rodziny. Treści niektórych ogłoszeń zawierają identyfikatory innych osób; zachowano wyłącznie bezpieczną metrykę publikacji i ocenę, bez ich PESEL i adresów.

**Ograniczenie:** `countPages: 100` zwracane przez API nie jest wiarygodną liczbą stron trafień. Dziewięć pozycji wynika z faktycznej listy na stronie 1 i pustej strony 2. Zera opisują konkretne ciągi wyszukiwania, nie wszystkie możliwe ogłoszenia spadkowe w Polsce. Wcześniejsze kwerendy formy podstawowej i „Tomaszu Chmielewskim” są w osobnych pakietach, nie policzono ich ponownie.

Źródła: [oficjalna wyszukiwarka MSiG](https://wyszukiwarka-msig.ms.gov.pl/), `zrodla/msig_*.json`, `kwerenda_msig.py`.

## TOM-D02 — Rejestr Spadkowy: sprawdzono warunki, nie wykonano kwerendy osoby

Odczytano [oficjalną wyszukiwarkę](https://rejestry-notarialne.pl/37), wybrano w zwykłej przeglądarce „Podstawowe dane identyfikujące spadkodawcę” i obejrzano formularz. Według legendy żółte pola są opcjonalne; w tym formularzu żółte są imiona ojca i matki. Nazwisko, imię, dokładna data urodzenia i data zgonu są pozostałymi polami wymaganymi przez interfejs. DOM nie oznacza ich standardowym atrybutem `required`, więc sama wartość tego atrybutu nie rozstrzyga walidacji.

Dokładnej daty urodzenia i PESEL Tomasza nie znamy. **Nie wysłano zapytania, nie wpisywano wymyślonej daty, nie rozwiązywano reCAPTCHA. To nie jest wynik „0 wpisów”.** Zrzut formularza: [pola rejestru](zrodla/rejestr_spadkowy_pola.png).

Publiczny indeks wskazuje, gdzie znajdują się dokumenty; nie udostępnia ich treści ani wykazu spadkobierców. Obejmuje akty poświadczenia dziedziczenia sporządzone po 01.03.2009 i sądowe stwierdzenia nabycia spadku wydane po 08.09.2016. Śmierć w 2001 r. sama w sobie nie wyklucza późniejszej sprawy, ale nie oznacza też, że stara sprawa trafiła do tego indeksu.

## TOM-D03 — Wirtualny Cmentarz: rzeczywiste wyszukiwanie i dodatnia kontrola

W [publicznym serwisie wspomnień](https://www.wirtualnycmentarz.pl/cmentarz) uruchomiono natywną wyszukiwarkę „Ludzie”. Po wpisaniu tekstu kliknięto przycisk lupy; samo naciśnięcie Enter nie uruchamiało żądania. Nie interpretowano pustego panelu ani błędów nawigacji jako zerowych wyników.

Odczytano odpowiedzi endpointu `api/funerals/datatables/graveyard` wywołane przez zwykły interfejs. Zakres domyślny: `main` i `catacombs` (osoby; bez cmentarza zwierząt), `start=0`, `length=25`, bez ograniczenia miejsca pochówku.

| Zapytanie | recordsFiltered | Znaczenie |
|---|---:|---|
| Chmielewski | 0 | Brak wyniku w tym serwisie. |
| Tomasz Chmielewski | 0 | Brak wyniku w tym serwisie. |
| Nowak | 6 | Dodatnia kontrola działania formularza; obejmuje też dopasowanie części nazwiska. |

Każda odpowiedź miała HTTP 200; ogólna liczba wpisów w podanym zakresie wynosiła 1329. Zera nie wymagają przeglądania kolejnych stron. Dane osób z dodatniej kontroli pominięto w archiwum jako niepowiązane z rodziną. Nie zakładano konta, nie dodawano nagrobków i nie kontaktowano się z autorami wpisów. Zapis zapytań: `zrodla/wirtualny_api_0.json`–`2.json`; odtwarzalny przebieg: `kwerenda_wirtualny_cmentarz.py`.

Próba odczytu serwisu Ogrody Pamięci zakończyła się błędem połączenia narzędzia `ERR_TUNNEL_CONNECTION_FAILED`; nie wykonano tam kwerendy osoby i nie odnotowano zera.

## TOM-D04 — Academica: brak dostępu do katalogu w tej sesji

Próbowano odczytać `https://academica.edu.pl/` i `/search` przez scraper, zwykły HTTP oraz zwykłą przeglądarkę. Scraper zwrócił błąd silników lub timeout, przeglądarka komunikat o przekroczeniu czasu połączenia upstream. **Nie odczytano katalogu i nie stwierdzono, że rocznika 2001 tam nie ma.**

Odczytano natomiast [oficjalne zasady BUŁ](https://www.lib.uni.lodz.pl/academica): materiały publiczne można czytać zdalnie, a objęte ochroną wyłącznie na dedykowanych terminalach, z aktywnym kontem bibliotecznym; na terminalach nie można pobierać ani drukować przeglądanych materiałów. Nie potwierdzono w ten sposób obecności konkretnych numerów Dziennika z 2001. Nie tworzono kont i nie obchodzono ograniczeń.

## TOM-D05 — gotowe zapytanie do WBP, niewysłane

Poprzedni pakiet TOM-N01 ustalił konkretne woluminy **„Dziennik Łódzki – Wiadomości Dnia”, wydanie A, sygnatura 77-G**: kwiecień 2001, nr 78–101; maj 2001, nr 102–126. Ich status to „na półce, tylko na miejscu”, nie znaleziony skan. Odsyłacz cyfrowy nie udostępnił rocznika 2001. [Dokładne dane egzemplarzy](../2026-11-07-tomasz-nekrologi/zrodla/PRASA_2001_KONKRETNE_EGZEMPLARZE.json).

Na [oficjalnej stronie katalogu WBP, w sekcji pomocy](https://omnis-wbpl.primo.exlibrisgroup.com/discovery/search?vid=48OMNIS_WBPL:48OMNIS_WBPL) zweryfikowano adres Działu Informacji Naukowej, Regionaliów i Bibliografii: **informacja@wbp.lodz.pl**. Sprawdzono, że w Gmail nie ma wcześniejszego zapytania o ten nekrolog do sprawdzanych adresów biblioteki. Utworzono **jeden szkic w Gmail** i odczytano go ponownie, sprawdzając odbiorcę, treść i etykietę `DRAFT`.

[Szkic w Gmail](https://mail.google.com/mail/u/?authuser=maciekkoz%40gmail.com#all/1a1b556ed7fa7fe2) prosi o poszukiwanie nekrologu, zawiadomienia o pogrzebie albo podziękowania w wydaniach **27.04–07.05.2001** oraz informację o możliwości otrzymania kopii z datą i numerem gazety. W razie odpłatności prosi najpierw o warunki i wycenę, przed rozpoczęciem płatnej pracy. Pełna kopia: [ZAPYTANIE_WBP_NIEWYSLANE.txt](ZAPYTANIE_WBP_NIEWYSLANE.txt).

**Nie wysłano tego zapytania.** Użytkownik otrzymał osobne pytanie o wysłanie do nowego odbiorcy, z linkiem do konkretnego szkicu. Dotychczasowa zgoda obejmowała wiadomość do cmentarza Zarzew, nie tę bibliotekę. Do czasu odpowiedzi szkic pozostaje niewysłany; nie zlecono płatnej usługi ani nie wysłano wniosków USC.

## TOM-D06 — pomocnicze wyszukiwania web i zakres zmian

Wykonano 12 nowych zapytań web: dostępność roczników w Academica, indeks spadkowy, sądowe warianty nazwiska i zapisy daty śmierci oraz serwisy pamięci. Warianty z „2001” dopasowywały też niezwiązane dokumenty, dawny akt z 1819 r., listy referendarzy i sprawy upadłościowe. Nie uzyskano niezależnego łącznika rodzinnego. Dokładny wykaz zapytań i wyników: [rejestr](zrodla/rejestr_kwerend_web.json); kopie odpowiedzi `search_*.json`. Wyniki web nie są dowodem przeczytania wskazanych dokumentów; rzeczywiste odczyty wymieniono powyżej.

Pakiet ma wyłącznie **lokalne oznaczenia TOM-D01–TOM-D06**. Nie zmienia głównego Excela, numeracji S/L/F, osób ani witryny, aby nie kolidować z równoległym wątkiem. Nie opublikowano nowej wersji drzewa, bo nie znaleziono nowego faktu biograficznego. Nie dopisano mieszkania po ojcu jako własności Tomasza ani sprawy spadkowej jako ustalonego faktu.

Najbardziej konkretny materiał do następnego odczytu pozostaje papierowy nekrolog w potwierdzonych woluminach gazety; wiadomość do biblioteki jest przygotowana do oceny. Dokładną datę urodzenia i matkę mogą wskazać także akt zgonu lub księga pochowanych znanego cmentarza. Ich wcześniejsze szkice już istnieją — nie powielono ich w tej kwerendzie.
