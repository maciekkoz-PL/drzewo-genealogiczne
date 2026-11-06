**Aktualny audyt — wersja17:**96rekordówosób i75relacji. Dodano pominięte wpublicznymdrzewie C66–C68, uzupełniono P31/P32 oREL-014. Liczby widocznych kart/linii bez zmiany:17/27,28/41,51/75. PrzypuszczenieRoman↔Czesia nadal wyłącznie poziom3. Nie dodano potwierdzonego męża ani ojca syna. [Walidacja](../2026-11-06-sesja-13-ciocia-czesia/WALIDACJA.json), [publikacja](../2026-11-06-sesja-13-ciocia-czesia/PUBLIKACJA.json). Poprzednie opisy historyczne poniżej.

**Aktualny audyt — wersja16:**93rekordy osób (w tym aliasy i pominięci kandydaci) oraz75relacji wizualizacji. Poziomy:17/27(w tym2łącznikiH017),28/41,51/75. Emilia P28/Józef P29/Julia P30 udokumentowani; Czesia P31 i syn P32 z przekazu, V066 Roman↔Czesia tylko hipoteza. C05aliasP30. Zachowano mapy z wersji14. [Walidacja Excel/CSV/JSON/HTML](../2026-11-06-sesja-11-rodziny-rodzenstwa/WALIDACJA_SPOJNOSCI_PUBLIKACJI.json), [strona publiczna](../2026-11-06-sesja-11-rodziny-rodzenstwa/WALIDACJA_PUBLICZNA.json). Poniższe liczby historyczne opisują wcześniejsze wersje.

**Aktualizacja po dwóch aktach sióstr Czesława (wersja12):** P26/P27 zastępują na stronie C04/C02, aliasy zachowane w bazie. Audyt:84rekordy osób i69relacji. Poziomy:14/22(wtym2łącznikiH017),23/35,47/69. [Potwierdzenie zgodności](../2026-11-06-sesja-10-siostry-czeslawa/WALIDACJA_SPOJNOSCI_PUBLIKACJI.json). Historyczne liczby poniżej pozostają opisem poprzedniego stanu.

**Korekta filtra:** własne akty osób nie są ukrywane przez H017. Widok udokumentowany:12osób i16linii, w tym2przerywane łączniki identyfikacji w toku. [Wyjaśnienie](KOREKTA_FILTRA.md).

# Trzy poziomy wiarygodności

Audyt bazuje na 8f4d7c5cc5f035ff51c776d0e16e9f1d6b3e56b8. Zachowano21dotychczasowych arkuszy i dodano dwa arkusze audytu (łącznie23), bez zmiany historycznych rekordów. Pełne tabele: [osoby](AUDYT_OSOB.csv), [relacje](AUDYT_RELACJI.csv). Identyfikatory V oznaczają wyłącznie krawędzie wizualizacji, nie potwierdzone relacje produkcyjne.

Poziom osoby dotyczy pokazania jej w kontekście rodziny. Tożsamość źródłowa jest odrębna: akt C25/C26/C42 nie potwierdza ich relacji. P03/P04 i starsza linia ojca pojawiają się od poziomu2 z powodu H017; lokalne krawędzie z aktów pozostają udokumentowane. P09, P10/P11, P20–P25 i powiązania rodzinne: poziom2 z przekazu. Nie ma arbitralnych procentów. Wyjątek P01/P02/P17 i dwóch linii rodzicielskich pozostaje na poziomie1, jawnie rodzinny.

Poziom3: indeksowa para C56/C57, rodzice C46–C49 i siedmioro dzieci, osobne od P22/P23 i Anny P19. Dopasowania P22=C56, P23=C57, P19=C45 pozostają hipotezamiH024/H020. Zgodność obojga rodziców indeksów wspiera indeksowe grupowanie, ale brak odczytu aktów i łącznika Anny wyklucza awans do2. Strzegowo mazowieckie, nie Strzegowa olkuska.

Dodano również źródłowe tropy C05,C06,C10,C19,C27–C29. Pozostałe pominięte rekordy są indywidualnie opisane w audycie, w tym wykluczenia i aliasy. Nie usunięto żadnego dawnego źródła/hipotezy.

Najstarsze pokolenie poziomu1: rodzice Marii Roman/Anna. Poziomu2: Wincenty/Agnieszka i Józef/Marianna oraz Józef/Czesława Jankowscy i rodzinni Józef/Konstancja Kulas. Poziomu3: Andrzej Kulas/Antonina Konopka oraz Maciej Gralewicz/Teresa Dąbrowska.

## Wynik i publikacja

| Widok obu gałęzi | Osoby | Relacje | Najstarsze pokolenie |
| --- | --- | --- | --- |
| 1 — tylko udokumentowane | 5 | 5 | Roman Jankowski i Anna Kulas, rodzice Marii |
| 2 — także prawdopodobne (domyślny) | 21 | 29 | Pradziadkowie Marysi po obu stronach |
| 3 — także przypuszczenia | 47 | 65 | C46–C49: Andrzej Kulas, Antonina Konopka, Maciej Gralewicz, Teresa Dąbrowska |

Dodano do wizualizacji 19 osób: C05,C06,C10,C19,C27–C29,C46–C57. Pozostałe istniejące osoby zachowane. Nowe połączenia obejmują indeksową parę i dzieci/rodziców, hipotetyczne identyfikacje oraz dotychczas niewizualizowane relacje rejestru; nie awansowano ich do potwierdzonych relacji w produkcyjnym arkuszu RELACJE. Każdy przypadek w tabelach audytowych.

Klasyfikacje istniejących kart: P01/P02/P17/P18/P19 poziom1; P03/P04/P05/P06/P07/P08/P12 poziom2 z powodu H017, mimo udokumentowanych lokalnych danych; P09/P10/P11/P20–P25 poziom2 z przekazów rodzinnych i fotografii; dotychczasowe C02/C04/C11/C25/C26/C42/C45 poziom3 jako relacje niepotwierdzone. Tożsamość z aktu C25/C26/C42 pozostaje odrębnie oznaczona1. Nowe widoczne kandydatury i starsze indeksy poziom3. Relacje z aktów zachowują1; R007/R008 jako przyporządkowanie konkretnych kart mają2 z H017, R009/R017 zachowują wyjątek1 zREL-011; pozostałe relacje rodzinne2, hipotezy i indeksowe3.

[Commit implementacji](https://github.com/maciekkoz-PL/drzewo-genealogiczne/commit/1a8223e01148dfa439e2523d780dabe59762d45d). Testy Chromium1440/390px przeszły: trzy poziomy, wszystkie filtry gałęzi, kumulatywność, stałe linie rodziców, brak przepełnienia telefonu i błędówJS, szczegółowe karty najstarszego pokolenia. [Publikacja wersji9](PUBLIKACJA.json): succeeded, HTTP200 i identyczny hash HTML. Hosting otrzymał2pliki bez prywatnych dokumentów i zdjęć.

Uzupełnienie po scaleniu7b96ccd: audyt zawiera dodatkowoC59/C60/C61 z etapu09 linii ojca, z podaniem źródeł i powodu pominięcia. Karty publiczne i liczby widocznych osób bez zmian. [Kontrola aktów](../2026-11-06-sesja-09-linia-ojca/CZTERY_ZGONY_1940.md).
