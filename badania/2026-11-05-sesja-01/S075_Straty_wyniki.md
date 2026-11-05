# S075 — nowe tropy w bazie strat IPN

Odczyt 5 listopada 2026. Publiczna wyszukiwarka: https://www.straty.pl/szukaj-osoby.php . Zapytania formularza POST służyły wyłącznie wyszukiwaniu i wyświetleniu istniejących danych; **nie składano kwestionariusza ani zgłoszenia**. Dokładne pola, data dostępu, kopie i skróty w `Straty_zapytania.json`, `Straty_zapytania_2.json` oraz `pobrania.jsonl`. Rekordy nie mają tu potwierdzonego trwałego adresu GET: aby odtworzyć szczegóły, wysłać do formularza wskazane pole `idNNN` albo ponowić zapytanie po nazwisku i dacie. Kopie HTML zachowują pełny wynik, w tym wartości pól `input`, których zwykły eksport tekstu nie pokazuje.

## C27 — Czesław, Łódź, 03.07.1909

**Rekord 5791928**, kopia `zrodla/Straty_id5791928.html`; wykonany POST `id5791928=Chmielewski`.

Baza podaje Czesława Chmielewskiego, ur. **03.07.1909**, mieszkańca Łodzi, polskiej narodowości. Opis wskazuje pracę przymusową dla **Fa. Krümpelmann (Łódź)**, miejsce pracy **OT-Einheit Stolpce, Białoruś** i nieobecność od **17.02.1944**. Wpis informuje o poszukiwaniu przez Gestapo z zarzutu naruszenia dyscypliny pracy. Źródło wskazane przez bazę: **IPN Ld 1/3503**, akta niemieckiej Tajnej Policji Państwowej, oddział w Łodzi.

To **opis indeksowy**, nie odczyt akt Gestapo. Wpis nie podaje rodziców ani Rogoźna. Data, imię, nazwisko i Łódź tworzą silnego kandydata do porównania z P03, ale nie dokonano scalenia. Nie przypisano rodzinie historii represji jako potwierdzonego faktu. Należy uzyskać obraz akt lub pełniejszy opis z rodzicami, miejscem urodzenia lub adresem.

## Rekord 4205404 i dokumenty Arolsen

**Rekord 4205404**, kopia `zrodla/Straty_id4205404.html`; wykonany POST `id4205404=Chmielewski` (wartość nazwiska z przycisku; identyfikatorem jest nazwa pola).

Baza grupuje **CHMIELEWSKI / CHMIELOWSKI, Czeslawo**, ur. **03.07.1909**, pobyt Caßdorf/Cassdorf w powiecie Fritzlar-Homberg w Hesji. Wskazuje:

- **70381403 / 2.1.1.1 / 2055 / 518**, rejestry ubezpieczenia społecznego i zatrudnienia;
- **70380716 / 2.1.1.1 / 2054 / 50**, dokumenty o obcokrajowcach w miejscowości.

Oba oryginały pobrano i odczytano jako **S076**. Drugi skan zawiera dwa zbliżone wpisy, z odmiennym miejscem urodzenia i statusem. Nie uznano grupowania w bazie za wystarczający dowód, że wszystkie zapisy dotyczą jednej osoby. Osobno zapisano C28 i C29.

## Zakres i wyniki pozostałych zapytań

1. Chmielewski + Czesław, bez daty: **46 wierszy**, z których dwa mają 03.07.1909. Funkcja wyszukiwarki uwzględnia warianty i ciągi znaków, nie tylko ścisłe imię. Wszystkie wartości w `Straty_wyniki_wiersze.json`.
2. Chmielewski + Bogusław + rok 1943: komunikat braku danych. Zapytanie bez roku dało **5 wierszy**: daty 1911, 1914, 1922 i dwa bez daty. Dwa ostatnie odczytano: **6107395** odsyła do księgi Mauthausen-Gusen, **IPN Ka 301/2 t.8 s.51**; **6184833** do ankiet woj. krakowskiego, pow. Oświęcim, **IPN BU 2448/489 s.1268–1269, IPN KR 1/1287, 1296**. Bez identyfikatorów rodzinnych nie uznano ich za P02 ani nie wykluczono samym brakiem daty. Nie dopisano nowych członków rodziny.
3. Chmielewska + Janina + rok 1910: jeden wynik — **Porowska, z domu Chmielewska, ur. 21.06.1910**, inna data i inne nazwisko panieńskie niż P04. Nie jest potwierdzeniem poszukiwanej Janiny.
4. Poprawka + Janina: brak danych spełniających kryteria.
5. Chmielewski + ojciec Czesław + matka Janina: brak danych spełniających kryteria.
6. Chmielewski + ojciec Wincenty + matka Agnieszka: brak danych spełniających kryteria.

**Żaden wynik zerowy nie jest dowodem braku osoby lub represji.** Baza ma nierówne pokrycie, część rekordów bez dat i rodziców, warianty pisowni i wtórne opisy. Nie zidentyfikowano tu aktu Bogusława ani jego rodzeństwa i nie ustalono ojca Piotra.
