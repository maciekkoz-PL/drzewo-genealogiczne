# Gałąź matki Marysi — scalenie 6 listopada 2026

Scalono suplement `Marysia_LINIA_MATKI_repo_ready_2026-11-06.zip` z aktualnym `main` **b86519ced59d9ad205a79307763b9cb5572ddc31**. Zachowano wszystkie21arkuszy, poprzednie badania i oba oryginalne ZIP-y. Nie zastąpiono repo ani bazy plikami pakietu. Oryginalne dane przekazania w [dane/linia_matki.json](dane/linia_matki.json) i CSV pozostają bez zmian; [mapowanie ID](MAPOWANIE_ID.json) odróżnia je od produkcyjnych identyfikatorów.

## Co scalono i dodano

- **P17 Maria Jankowska**, **P18 Roman Jankowski**, **P19 Anna Kulas** już istnieli. Nie utworzono duplikatów. R018/R019 nadal dokumentują rodziców Marii z **S086**. P12 pozostaje Romanem Chmielewskim.
- P17: zachowano DOB04.01.1942 i ślub13.11.1982 Warszawa oraz rozwód23.04.1985 zS086. Maria żyje według przekazu pakietu. Jej macierzyństwo wobec P01 nadal stanowi przekaz, nie rubryka dzieci w odpisie.
- **P20 Andrzej Jankowski (około1946)** i **P21 Teresa Jankowska (około1950)**: rodzeństwo Marii i dzieci Romana/Anny według **REL-009**. Maria najstarsza. Nieznane dokładne daty, miejsca i stan życia Andrzeja/Teresy; nie zgadywano nazwiska obecnego Teresy.
- **P22 Józef Kulas**, **P23 Konstancja Kulas**: rodzice Anny wyłącznie według **REL-010**. Nie przypisano im dokumentalnie dat1859/1873 ani rodowego Gralewicz. Indeksowe kandydatury **C56/C57** są odrębne i powiązane pytaniem H024.
- **C43 Józef Jankowski**, **C44 Czesława Jankowska**: osobne osoby z przekazanego odczytu nagrobka, bez potwierdzonego pokrewieństwa z Romanem i bez przypisanego im małżeństwa.
- **C45 Julianna Anna Kulas1910** pozostaje kandydatką, nie P19. C46–C49 to starszy kontekst indeksowy (Andrzej Kulas, Antonina Konopka, Maciej Gralewicz, Teresa Dąbrowska). C50–C55 to pozostałe dzieci pary indeksowej. Nie dodano im potwierdzonych relacji w drzewie rodziny.
- Nowe rejestry: **S127–S134**, **REL-009/010**, **R020–R027** (wszystkie nowe relacje rodzinne, nie urzędowe), **E046–E052**, **H020–H024**, **Q62–Q67**, **L104/L105**, **F75–F78**, **T29–T33**. Istniejące R017–R019 zachowane.

S086 to urzędowy odpis znany z wcześniejszego odczytu fotografii. W tej sesji porównano jego odczyt w repo; oryginalnego dokumentu ponownie nie oglądano. **S128 jest transkrypcją z pakietu, nie lokalnie obejrzaną fotografią.** S129–S133 to odczytane w tej sesji indeksy, nie akty. Rozróżnienie nie zmienia się przez umieszczenie danych w XLSX.

## Grób — cztery inskrypcje z przekazanego odczytu

| ID | Napis | Data śmierci | Wiek | Tylko przybliżony rok urodzenia |
| --- | --- | --- | --- | --- |
| C43 | Józef Jankowski | 30.09.1967 | 81 | około1885/1886 |
| P19 | Anna Jankowska | 28.09.1978 | 68 | około1909/1910 |
| P18 | Roman Jankowski | 29.05.2002 | 88 | około1913/1914 |
| C44 | Czesława Jankowska | 03.01.1982 | 98 | około1883/1884 |

„Ave Maria” jest napisem religijnym, nie piątą osobą. Nagrobek nie podaje rodowego Kulas ani więzi czworga zmarłych. Przypisanie Romana i Anny do znanych rodziców Marii opiera się na przekazie rodzinnym wraz zS086; samo wspólne nazwisko nie wystarcza. Strzegowo i pochówek tam pochodzą zREL-009; nie ustalono niezależnie cmentarza, pola i numeru grobu. Wiek nie stanowi dokładnej daty urodzenia.

## Indeksy i geografia

[Kontrola indeksów](KONTROLA_INDEKSOW.md) i surowe odpowiedzi w `zrodla/` potwierdzają, że wiersze16/1894,55/1859,60/1873 i18/1910 występują w Genetece dla **Strzegowa, mazowieckie**. Przy Konstancji60/1873 podano **Prusocin**. Katalog id1541 dotyczy **Strzegowej, pow. olkuski**, i nie może być używany zamiennie. Nie odczytano skanów ani nie wymyślano linków. Oryginalny pakiet zachowuje historyczne zastrzeżenia; aktualny stan po kontroli jest tutaj i w rejestrze.

H020: Anna ≠ automatycznie Julianna Anna1910. H021/H022: Józef/Czesława nie są ustalonymi rodzicami Romana. H023: brak własnego aktu ślubu Romana/Anny. H024: brak utożsamienia rodzinnych Józefa/Konstancji z parą indeksową16/1894. Pozostawiono też dotychczasowe H017–H019 oraz wcześniejsze wyniki gałęzi ojca.

## Brakujące fotografie i akty

**Oczekuje na oryginalny JPEG** `4F72A452-6F93-446F-A30E-F0B58131AEC5.jpeg`. Nie było go w ZIP ani w załącznikach tej sesji. Nie zapisano zdjęcia, fikcyjnego pliku ani sumy kontrolnej obrazu. Drugie oznaczenie `284E7A1D-779E-49D3-BC27-905353012A2C.jpeg` i diagram `Drzewo_Marysi_Matka.png` także nie są dostępne. Brakuje również oryginalnego obrazuS086. [Opis braków](zdjecia/README.md). Po otrzymaniu obrazy zapisać wyłącznie prywatnie w `zdjecia/` i dopiero wtedy dodać rzeczywiste hashe.

Najważniejsze dokumenty do uzyskania/odczytania:

1. Własny ślub Romana Jankowskiego i Anny Kulas oraz akt urodzenia Anny: łącznik tożsamości i rodziców. Nie przyjmować roku/parafii ślubu na podstawie wspólnych dzieci.
2. Akt urodzenia lub ślubu Romana z rodzicami; akty zgonu Romana29.05.2002, Anny28.09.1978, Józefa30.09.1967 i Czesławy03.01.1982 (daty poszukiwawcze pochodzą z transkrypcji).
3. Oryginały16/1894,55/1859,60/1873,18/1910 i, w dalszej kolejności, siedmiu indeksowanych urodzeń. Najpierw dowód łączący Annę; nie rozwijać starszych przodków kosztem celu.
4. Akty Andrzeja i Teresy potwierdzające rodziców, dokładne daty i relację do Marii. Akt urodzenia Marii04.01.1942 może dodatkowo uzupełnić identyfikatory rodziców; jej rodzice są już wskazani wS086.
5. Akt urodzenia Marysi, jeżeli celem będzie urzędowe udokumentowanie macierzyństwa P17. Dotychczasowe braki linii ojca pozostają w dawnych planach.

Nie wysłano wiadomości, wniosków ani nie poniesiono opłat. Publiczny widok otrzymuje wyłącznie ręcznie wybrane opisy, bez XLSX, ZIP, transkrypcji całej dokumentacji, fotografii rodzinnych i skanów USC. Stan publikacji zostanie zapisany osobno w `PUBLIKACJA.json`; wygenerowanie HTML samo nie oznacza wdrożenia.

Następne wolne ID po tej sesji: **P24, S135, C58, R028, E053, L106, Q68, F79, H025, REL-011, T34**. P13–P16 zachowują historyczną rezerwację.

## Zapis i publikacja

[Commit badań eeea4ee](https://github.com/maciekkoz-PL/drzewo-genealogiczne/commit/eeea4ee13194fced879518918962ea5ecd94ed36), [commit publicznego widoku b034a80](https://github.com/maciekkoz-PL/drzewo-genealogiczne/commit/b034a80). Oba zapisane na `main`. [Publikacja wersji 6](PUBLIKACJA.json) zakończyła się statusem `succeeded`; [kontrola URL](WALIDACJA_URL.json) zwróciła HTTP 200 i identyczny hash HTML. Publicznie 25 kart, 6 wpisów; 13 kart w widoku udokumentowanym. Hosting otrzymał tylko `dist/index.html` i istniejącą konfigurację. Kontrole danych/składni przeszły; renderowania w przeglądarce nie testowano w tej sesji, ponieważ brak narzędzia `cua_repl.js` wymaganego przez instrukcję Sites. Skrypt regresji zaktualizowano do nowych liczebności.
