# Uzupełnienie projektu „Drzewo genealogiczne Marysi” — linia matki

**Stan przekazania:** 6 listopada 2026. Pakiet jest suplementem do istniejącego prywatnego repozytorium `maciekkoz-PL/drzewo-genealogiczne`. Nie zastępuje bieżących plików na gałęzi `main`. Zawiera odtworzone ustalenia z rozmów 2–5 listopada, oględziny zdjęcia nagrobka oraz informacje odczytane z dokumentacji na GitHubie. **Nie jest potwierdzeniem źródłowym wszystkich zawartych hipotez.**

## Gdzie umieścić wyniki

- Trwała notatka tego uzupełnienia: `badania/2026-11-06-linia-matki/README.md`.
- Pliki źródłowe CSV i JSON: `badania/2026-11-06-linia-matki/dane/`.
- Oryginalne fotografie po ich otrzymaniu: `badania/2026-11-06-linia-matki/zdjecia/` (nie umieszczać w publicznej witrynie).
- Bazę `Marysia_KOMPLET_BAZA_2026-11-05.xlsx` uzupełnij **scalając, a nie zastępując** aktualne już 21 arkuszy i istniejące rekordy. Sprawdź bieżącą liczbę arkuszy przed modyfikacją.
- Zaktualizuj `ZBADANE_ZRODLA.md`, `Marysia_INSTRUKCJA_DLA_AGENTA.md`, `README.md` tylko w zakresie rzeczywistej nowej wiedzy i odsyłaczy; nie kasuj dotychczasowych badań. 
- Do publicznego drzewa dopisz potwierdzoną / rodzinną gałąź matki zgodnie z `witryna/README.md` i schematem `witryna/generuj.py`. **Nie publikuj zdjęć rodzinnych i skanów USC.** Nie publikuj hipotez jako ustalonych przodków.

## Ważne mapowanie istniejących rekordów

- `P01` — Marysia, centralna osoba w repo.
- `P17` — **Maria Jankowska**, ur. 4 stycznia 1942, Strzegowo — jest **już w repo**; nie twórz nowego rekordu dla tej samej osoby. Jej rodzice Roman Jankowski i Anna z domu Kulas są podani wprost w fotografii odpisu ślubu `S086`.
- `P12` — **Roman Chmielewski**, brat Czesława, **nie** Roman Jankowski (dziadek ze strony matki). Szczególne ryzyko kolizji imion.
- Nowe identyfikatory `MAT-Pnn`, `MAT-Rnn`, `MAT-IDX-nn` w danych są **tymczasowe**. Nadawaj nowe niezajęte produkcyjne identyfikatory zgodnie z aktualnym rejestrem (nie zakładaj, że P18 lub S127 są wolne).

## Źródło urzędowe S086 — dokument dotyczący OBOJGA rodziców

Fotografia **odpisu skróconego aktu małżeństwa II-1592/1982** (Warszawa, ślub 13.11.1982; rozwód 23.04.1985; odpis wydany 01.08.2002). Odczyt w repo:
`badania/2026-11-05-sesja-02-rodzice/S086_ODPIS_MALZENSTWA_RODZICE.md`

- Żona: **Maria Jankowska**, ur. **04.01.1942 w Strzegowie**, ojciec **Roman Jankowski**, matka **Anna z domu Kulas**. Po ślubie nazwisko Chmielewska.
- Mąż: Bogusław Kazimierz Chmielewski, ur. 25.04.1943 w Łodzi, rodzice Czesław i Janina z domu Poprawka. Ta linia była już badana i **nie jest przedmiotem duplikowania**.
- **Granica dowodu:** S086 urzędowo podaje rodziców Marii. Nie jest aktem urodzenia Marysi i nie wykazuje jej w rubryce dzieci; jej macierzyństwo to odrębny przekaz rodzinny.

## Maternalna gałąź — poziomy pewności

**Dokument (S086):**
```
Roman Jankowski ── Anna z domu Kulas
                   │
                   └─ Maria Jankowska (04.01.1942 Strzegowo) ── Bogusław Kazimierz Chmielewski
                                                                    │
                                                                 Marysia (relacja rodzinna)
```
Relacja Roman–Anna jako małżonkowie jest przekazem rodzinnym, a ich rodzicielstwo wobec Marii wynika wprost z S086. Relacja Marysi do Marii i Bogusława pochodzi z przekazu rodzinnego.

**Przekaz rodzinny:** Roman i Anna żyli i zostali pochowani w Strzegowie. Ich dzieci: Maria (najstarsza, ur. 1942), Andrzej (~1946), Teresa (~1950). Anna z domu Kulas była ze Strzegowa i miała liczne rodzeństwo. Brak sprawdzonych metryk Andrzeja i Teresy; nie znamy ich aktualnego stanu życia ani dokładnych dat.

**Przekaz rodzinny + indeksy:** Za pradziadków Marysi podano Józefa Kulasa i Konstancję Kulas; dopasowanie nazwiska rodowego **Gralewicz** oraz ślubu w 1894 r. pochodzi z indeksów, nie z odczytanych aktów. Nie wolno bezpośrednio utożsamiać indeksowej Julianny Anny Kulas (1910) z Anną Jankowską z domu Kulas, matką Marii.

**Hipoteza z lokalizacji grobu:** Józef Jankowski (zm. 1967) i Czesława Jankowska (zm. 1982), umieszczeni na tym samym grobie co Roman i Anna, **mogą** być przodkami Romana, ale nie wynika to z tablicy. Nie przypisuj im automatycznie rodzicielstwa ani małżeństwa.

## Fotografia grobu Strzegowo — odczyt bez spekulacji

Zdjęcie użytkownika (oryginalne oznaczenie w Bibliotece projektu `4F72A452-6F93-446F-A30E-F0B58131AEC5.jpeg`; drugie przesłanie `284E7A1D-779E-49D3-BC27-905353012A2C.jpeg` wygląda identycznie). Na płycie:

| Inskrypcja | Wiek | Data śmierci | Wynikający przybliżony rok urodzenia |
|---|---:|---|---|
| Józef JANKOWSKI | 81 | 30.09.1967 | ~1885/1886 |
| Anna JANKOWSKA | 68 | 28.09.1978 | ~1909/1910 |
| Roman JANKOWSKI | 88 | 29.05.2002 | ~1913/1914 |
| Czesława JANKOWSKA | 98 | 03.01.1982 | ~1883/1884 |

Na płycie jest napis `Ave Maria` — to **nie piąta osoba**. Zapis wieku nie wyznacza dnia urodzenia. Tablica nie podaje nazwisk rodowych ani stopnia pokrewieństwa czworga zmarłych. Miejsce „Strzegowo” pochodzi z relacji rodziny, a nie z geotagu obrazu. Cmentarz/parafia/pole/numer grobu nie zostały w tej paczce niezależnie sprawdzone.

**Zdjęcie nie jest fizycznie w tym ZIP:** narzędzia umożliwiły odczyt i podgląd zdjęcia, lecz nie udostępniły jego oryginalnych bajtów do eksportu. Codex nie ma dostępu do Biblioteki ChatGPT na podstawie samej nazwy. Instrukcja brakującego załącznika: `zdjecia/README.md`. **Nie twierdź, że zdjęcie zostało przekazane, dopóki nie znajduje się w repo.**

## Metryki Kulas/Gralewicz — z wcześniejszego etapu, do ponownej kontroli

| Akt wg wcześniejszego indeksu | Osoby | Uwagi |
|---|---|---|
| 16/1894, małżeństwo, Strzegowo (do weryfikacji geograficznej) | Józef Kulas i Konstancja Gralewicz | Z wcześniejszej rozmowy; **brak skanu** |
| 55/1859, urodzenie, Strzegowo (do weryfikacji) | Józef Kulas | Rodzice Andrzej Kulas i Antonina Konopka podani z indeksu |
| 60/1873, urodzenie, miejsce do weryfikacji | Konstancja Gralewicz | Rodzice Maciej Gralewicz i Teresa Dąbrowska z indeksu; w starym diagramie Prusocin |
| 18/1910, urodzenie | Julianna Anna Kulas | Kandydatka na Annę z domu Kulas — **brak dowodu tożsamości** |

Indeksowane dzieci pary Józef–Konstancja w dotychczasowym opracowaniu: Władysław (1895), Marianna (1898), Józef (1901), Zofia (1904), Stanisława (1906), Julianna Anna (1910), Jan Piotr (1913). Brak zweryfikowanych numerów metryk dla większości. Ich połączenie z babcią Marysi pozostaje do sprawdzenia.

**UWAGA GEOGRAFICZNA:** `Strzegowo` w powiecie mławskim (mazowieckie) i `Strzegowa` w powiecie olkuskim (małopolskie) to odrębne miejscowości i zespoły archiwalne. Rekord indeksowy ze Strzegowej nie potwierdza pochodzenia ze Strzegowa. Wcześniejsze opracowanie mogło niejawnie pomieszać miejsca. Codex ma zweryfikować **konkretną parafię, zespół, rok, nr aktu i rodziców** przed awansowaniem jakiejkolwiek osoby z indeksu.

Pomocnicze katalogi, **nie bezpośrednie cytaty do aktów**:
- Geneteka: https://geneteka.genealodzy.pl/
- Szukaj w Archiwach, zespół gmina Strzegowo 1781–1825 (nie zawiera 1894): https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/91322
- Katalog metryk Strzegowa (pow. olkuski, ODRĘBNA miejscowość): https://skanoteka.genealodzy.pl/id1541

## Zadania badawcze / kryteria zakończenia

1. Weryfikacja S086 i powiązanie **istniejącej P17** z nowymi rekordami Romana i Anny; bez duplikatu P17.
2. Opracowanie 4 inskrypcji grobu, wydzielenie osobnych osób Józefa i Czesławy i opis potencjalnego, nie potwierdzonego pokrewieństwa.
3. Wpisanie przekazu rodzinnego o rodzeństwie Marii, z dokładną adnotacją „około”, bez szacowania nieznanych dat na siłę.
4. Weryfikacja parafii i numerów 16/1894, 55/1859, 60/1873, 18/1910, a przede wszystkim zdobycie łączącego aktu urodzenia lub ślubu **Anny Kulas/Jankowskiej**. Dopiero on pozwala zestawić ją z indeksem Julianny Anny.
5. Poszukanie własnego aktu ślubu Romana i Anny oraz aktów urodzenia/zgony Józefa i Czesławy Jankowskich, aby rozstrzygnąć ich pokrewieństwo z Romanem.
6. Najpierw rejestr źródeł i baza; potem, zgodnie z obecną polityką repozytorium, zaktualizować `witryna/generuj.py` i publiczną stronę. Nie wprowadzać hipotetycznych praprzodków jako pewnych.
7. Podać raport `które rekordy dodano`, `które scalono`, `które nierozstrzygnięte`, `których plików fotograficznych nadal brakuje`, z dokładnymi nowymi ID i linkami do commitów.

Ograniczenie zakresu: użytkownik priorytetowo bada przodków maksymalnie do **pradziadków Marysi** i szuka współcześnie żyjących krewnych. Dane o pra-pra przodkach z indeksów można archiwizować jako kontekst, lecz nie rozwijać ich w nieskończoność kosztem tego celu.
