> **Wynik po późniejszej fotografii użytkownika:** S086 potwierdził rodziców Bogusława jako Czesława Chmielewskiego i Janinę Poprawkę. Poniższy opis zachowuje kwerendy wykonane przed otrzymaniem tego dokumentu, gdy dowodu jeszcze nie było. [Odczyt i ograniczenia](S086_ODPIS_MALZENSTWA_RODZICE.md); [aktualny plan](PLAN_KONTYNUACJI.md).

# Kwerenda: połączenie Bogusława z rodzicami — 5 listopada 2026

## Wynik i zakres

**Nie znaleziono dokumentu łączącego Bogusława Kazimierza Chmielewskiego z Czesławem Chmielewskim i Janiną Poprawką ani wskazującego innych rodziców.** R007/R008 nadal są relacjami rodzinnymi, H001 pozostaje otwarta. Zgodnie z nowym poleceniem wznowiono wyłącznie poszukiwania dotyczące identyfikacji Bogusława i jego pochodzenia. Nie rozwijano przodków, rodzeństwa ani wojennych losów domniemanej starszej gałęzi.

## Nowe informacje użytkownika — relacje, nie odpisy

- REL-005: „Bogdan” był przejęzyczeniem; chodzi o Bogusława Kazimierza, ojca Marysi. Nie dodano osoby Bogdan ani nowego imienia do danych P02.
- REL-006: zmarł w **1988 w Łodzi**; kilka lat wcześniej ożenił się i rozwiódł z mamą Marysi. Po rozwodzie pracował i mieszkał w Łodzi z nową partnerką. Partnerka pochowała go w grobie swojej rodziny, **bez jego imienia i nazwiska na nagrobku**. Brak inskrypcji był już zapisany w pierwotnym G17 — dzisiejsza wiadomość potwierdza wcześniejszy przekaz. Wpisu w księdze pochówków nadal nie odczytano.
- Nazwisko Podgórskich i cmentarz Kurczaki pochodzą ze starszego REL-002; najnowsza odpowiedź nie podaje nazwiska partnerki ani oznaczenia grobu. Nie uznano ich za nowo potwierdzone identyfikatory.
- Nadal brak urzędowego potwierdzenia daty i miejsca urodzenia 25.04.1943 Łódź. Pytanie o miasto i przybliżony rok małżeństwa później rozstrzygnęła fotografia S086:13.11.1982 Warszawa. Nie pytać ponownie.

## 1. Wyszukiwarki i prasa

Zachowano dokładne parametry nowych wywołań wyszukiwarki oraz ich pełne odpowiedzi w [kwerendy_web.json](kwerendy_web.json). Sprawdzano pełne imiona, odmiany „Bogusława Chmielewskiego”, „Bogusławie Chmielewskim”, kilka zapisów daty urodzenia, rok śmierci 1988, Łódź, nekrologi, ogłoszenia spadkowe oraz katalogi. Nie zidentyfikowano wpisu rodzicielstwa. Część wyników to dopasowania przybliżone — samo wystąpienie oddzielnych imion i nazwisk nie jest dopasowaniem osoby.

Wyszukiwanie prasowe objęło zapytania dla 1987–1989 i osobno 1988 w domenie Biblioteki Cyfrowej WBP Łódź. **Nie przejrzano wszystkich numerów gazet z 1988 r.** Bezpośrednie próby otwarcia dwóch stron wyszukiwania d Libra i PDF S041 dały HTTP 503. Zapisy: [wbp_probe.json](zrodla/wbp_probe.json). Nie jest to negatywny wynik pełnego przeszukania prasy.

S041, Dziennik Popularny 126/1976, strona 7, ogłoszenie 10859 g: publiczna kopia OCR w narzędziu potwierdza „Bogusław Chmielewski, Fibaków 7”, zgubiony indeks UŁ. Brak danych rodziców i daty urodzenia. Nadal **nie utożsamiono z P02**. Nie uznano ponownego odczytu tego samego ogłoszenia za nowe niezależne źródło. Oryginalnego PDF nie udało się w tej próbie pobrać lokalnie; nie deklarowano oględzin skanu ani kontroli jego całej strony.

## 2. S083 — Geneteka: bezpośrednie pytania o P02

Interfejs https://geneteka.genealodzy.pl/; pełne URL i parametry DataTables: [geneteka_direct_log.json](zrodla/geneteka_direct_log.json). Kod województwa 05ld, nazwisko Chmielewski, wszystkie parafie indeksu danego typu:

| Zakres | records Total / records Filtered | Zwrócone wiersze |
|---|---:|---:|
| Zgony 1988, bez imienia | 1 / 1 | 0 |
| Zgony 1975–1990, imię Bogusław | 0 / 0 | 0 |
| Urodzenia 1942–1944, imię Bogusław | 0 / 0 | 0 |

Odpowiedź „1 rekord, 0 wierszy” pozostaje **niekompletna**. Nie znamy tożsamości wskazywanej licznikiem osoby. Nie twierdzimy, że sprawdzono treść tego rekordu. Wyniki zerowe dotyczą konkretnych zapytań w opublikowanym indeksie i nie dowodzą braku aktów w USC lub parafii.

## 3. IPN — rozszerzenie S080, trop C33

Pobrano pierwszą stronę zapytania bez cudzysłowów `Chmielewski Bogusław`: **10 z 50** wyników. Pozostałych 40 nie odczytano. Takie zapytanie zwraca również wpisy, w których słowa dotyczą różnych osób. Nie przypisywano rodzinie takich zapisów.

Ze starej listy 9 wyników ponownie wyodrębniono jednostkę **IPN Ld 0216/10 t.1/29**, sygnatura postępowania **OM-0102/76**, lata 1975–1976, WUSW Skierniewice, opis wskazuje „Chmielewski Bogusław; Kalisiak Lucyna; Mendrygał Czesław i inni”. To **C33 — trop do identyfikacji P02**, nie potwierdzony ojciec Marysi. Tytuł wyniku nie zawiera daty urodzenia ani rodziców. Samodzielna karta https://inwentarz.ipn.gov.pl/en/node/5355242 była niedostępna; nie odczytano akt ani pełnego opisu tej karty. Nie łączyć Czesława Mendrygała z domniemanym ojcem.

Zapytanie dokładną datą `"25-04-1943"` dało **73 wyniki**, ale odczytano tylko pierwszą stronę **10/73**, z innymi osobami. Nie oznacza to wykluczenia P02 w całym inwentarzu. Dalszy skrypt napotkał HTTP 503 i timeout; po powtarzających się błędach przerwano kolejkę żądań do tego serwisu.

Pierwsza próba odwróconej frazy `"Bogusław Chmielewski"` straciła kryterium: pole `fraza` w HTML było puste, licznik 3 019 133. **To nie jest wykonane wyszukiwanie tej osoby.** Zapisano ten błąd i nie wyciągnięto wniosku negatywnego. Pliki `ipn_searches.json`, `ipn_reverse.html`, `ipn_dob.html`, `ipn_noquote.html`, `ipn_503_stop.json` w zrodla. Późniejsze próby pełnej karty przez publiczne URL PL/EN także były niedostępne.

## 4. Arolsen — rozszerzenie S078 bez rozwijania innej gałęzi

Zapytania publicznej wyszukiwarki z CookieJar, bez logowania, składania kwerend i kontaktu z archiwum:

| Zapytanie | Licznik / otrzymane wiersze | Zakres odczytu |
|---|---:|---|
| Chmielewski 1909 — kontrola działania tokenu roku | 75 / 75 | Techniczny test: zawiera znane już rekordy 03.07.1909. Nie pobierano ponownie skanów tej gałęzi. |
| Chmielewski 1943 | 49 / 49 | Odczytano wszystkie wiersze indeksu, nie ich 49 obrazów; brak pasującego P02. |
| Boguslaw 1943 — bez nazwiska | 90 / 90 | Odczytano wszystkie wiersze indeksu; brak daty 25.04.1943 i brak zidentyfikowanego P02. |
| Chmielewski 25.04.1943 | 0 / bez pobierania listy | **Nie jest wiarygodnym wykluczeniem** — kontrola pełnej daty także nie działa. |
| Chmielewski 03.07.1909 — kontrola pełnej daty | 0 / bez pobierania listy | Błędnie pusty wynik mimo znanych rekordów; zapis z kropkami nie sprawdza skutecznie dokładnej daty. |

**Rok jest tokenem wyszukiwania ogólnego, nie ścisłym filtrem urodzenia.** Niektóre wyniki mają rok 1943 jedynie w opisie dokumentu. Nie oznaczono ich jako osób urodzonych w 1943. Oba nowe zestawy nie wskazują rodziców P02; nie tworzono relacji ani rodzin z innych nazwisk. Pełne parametry i SHA-256: [arolsen_dob_log.json](zrodla/arolsen_dob_log.json) i [arolsen_given1943_log.json](zrodla/arolsen_given1943_log.json).

## 5. S084 — baza nekrologów

Odczytano sekcję „Chmielewski Bogusław” z https://www.nekrologi-baza.pl/zlista/49. Są trzy wpisy: zgon 28.12.2010; 27 lat, zgon w 1941; 73 lata, zgon 03.01.2026. **Nie zidentyfikowano wpisu P02 z 1988**; zakres tej bazy nie jest pełnym rejestrem zgonów Łodzi. Nie przypisano rodzinie tych osób.

W narzędziu otwarcie po starym identyfikatorze wyniku raz zwróciło inny PDF. Zapisano to jako błąd odwołania, następnie poprawnie wyszukano pełnym URL i pobrano HTML. Nie wykorzystano błędnej odpowiedzi do wniosku genealogicznego.

## 6. S085 — alternatywne przechowywanie i katalogi

Pobrano urzędowy wykaz Landesarchiv Berlin https://landesarchiv-berlin.de/formulare/StandesaemterOstgebiete.pdf, stan 15.11.2021, 54 strony. Wyszukano w warstwie tekstowej Litzmannstadt, Lodz, Lodsch i Gollantsch; odczytano odpowiadające wiersze. Odsyłacze Litzmannstadt/Hohensalza dotyczą wpisu Gollantsch, Krs. Wongrowitz/Eichenbrück. **Nie uzyskano wskazania konkretnego tomu urodzeń miasta Łodzi H 1 1943.** Nie oznacza to braku takiej księgi w innych zbiorach albo nowszym zasobie. Nie przeczytano pełnej treści wszystkich 54 stron.

Próby publicznego wyszukiwania rekordów FamilySearch i Geneanet były niedostępne. Nie przedstawiono ich jako przeszukanych baz. Wyszukiwanie alternatyw GenBaza i katalogu BaSIA nie dostarczyło aktu; BaSIA odczytano wyłącznie na poziomie listy zespołów, bez przeglądu jednostek. Nie ponawiano przeglądu 277 znanych metadanych Sw A ani stron C skorowidza 1943 ax, gdyż to ten sam zbadany zakres.

Oficjalny wykaz cmentarzy archidiecezji, S028, ponownie sprawdzono wyłącznie pod kątem linku do publicznej wyszukiwarki Kurczaków. W odczytanym HTML znaleziono linki wyszukiwarek Piotrkowa i Tomaszowa; nie ma takiego odnośnika dla Kurczaków. Nie jest to dowód, że żaden niezależny indeks nie istnieje. Nie kontaktowano się z kancelarią.

## Zapis i granice

Kopie odpowiedzi i źródeł wraz z manifestem SHA-256 są w zrodla. Ścieżki `work/boguslaw2` w oryginalnych dziennikach oznaczają miejsce pobrania; odpowiadające bajtowo identyczne kopie repozytorium wskazuje manifest. Pisma przygotowane wcześniej pozostają niewysłane. Nie wysłano wiadomości, nie zamówiono akt, nie wniesiono opłat. Czesław/Janina pozostają hipotezą; badanie ich dalszych rodzin jest wstrzymane.
