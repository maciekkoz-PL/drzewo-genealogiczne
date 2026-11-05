# S078 — zakres wyszukiwania Arolsen i niezidentyfikowany Bogusław

Publiczna wyszukiwarka: https://collections.arolsen-archives.org/en/search/ . Zbadano zwykłe pliki JavaScript serwisu, a następnie użyto tych samych publicznych metod wyszukiwania: `BuildQueryGlobalForAngular`, `GetCount`, `GetPersonList`, a dla znanych dokumentów `GetPersonListByDocId`. Nie logowano się, nie składano zapytania archiwalnego, nie wysyłano wiadomości. POST był odczytem wyników wyszukiwarki.

Dokładne parametry i odpowiedzi zapisano w `Arolsen_zapytania*.json`, `Arolsen_Czeslaw_zapytania_poprawne.json` oraz `zrodla/Arolsen_*GetPersonList.json`. Serwis potrzebuje zachowania ciasteczek zwykłej sesji między zbudowaniem zapytania a pobraniem wyników. Pierwsze odpowiedzi bez ich zachowania dawały pustą listę; **nie są miarodajnym wynikiem negatywnym**. Późniejsze zapytania z CookieJar:

| Zapytanie | Liczba wg GetCount / pobrane wiersze | Wynik |
|---|---|---|
| Czeslaw Chmielewski | 75 / 75 | Cztery dodatkowe wiersze z datą 03.07.1909; jeden znany, trzy nowe dokumenty S077. Lista 75 nie obejmowała wszystkich odmiennych pisowni znanych z S076. |
| Czeskowo | 6 / 6 | Jeden wpis odpowiada C28 z S076; pozostałe dotyczą innej rodziny/miejscowości i innych dat. |
| Boguslaw Chmielewski | 8 / 8 | Siedem wierszy z datami 1911, 1912, 1914, 1922; jeden bez daty — DocID 70593973. Nie odnaleziono wpisu rozpoznanego jako P02. |
| Janina Poprawka | 0 / 0 | Brak wyniku w tym zapytaniu, nie wykluczenie osoby lub dokumentów pod nazwiskiem męża/inną pisownią. |
| Janina Chmielewska | 56 / 56 | Nie zidentyfikowano P04. Wpis z samym rokiem 1910 sprawdzono na oryginale 87875186: inny ojciec i miejsce urodzenia. Szczegóły poniżej. |
| Chmielewski (bez imienia) | 4773 / nie pobrano | Przekroczono czas pobrania listy. Nie traktować 4773 jako przejrzanych osób. |

## DocID 70593973

[Strona dokumentu](https://collections.arolsen-archives.org/en/document/70593973); kopia `zrodla/Arolsen_D70593973.jpg`, metadane i URL obrazu w `Arolsen_pobrania_3.jsonl`.

Lista DP w Celle, ITS 071, wiersz **22**: **Chmielewski Boguslav**, historyczny adres **Fritzenwiese 27**, adnotacja **„nicht erschienen”**. Na stronie brak daty urodzenia, rodziców i danych łączących z Łodzią. **Nie jest zidentyfikowanym ojcem Marysi.** Nie użyto historycznego adresu do szukania obecnych mieszkańców ani kontaktu.

Nie uznano podobieństwa nazwiska za dowód i nie dopisano nowej relacji. Jeśli dojdzie dokument podający Bogusława w obozie/DP w Celle lub inne zgodne identyfikatory, można wrócić do tej konkretnej karty. Bez nowego punktu zaczepienia priorytet ma akt urodzenia z 1943 i ewidencja łódzka.

## DocID 87875186 — C32, Janina z rokiem 1910

[Strona dokumentu](https://collections.arolsen-archives.org/en/document/87875186); lokalny oryginał `zrodla/Arolsen_D87875186.jpg`, indeks i HTML obok; pobrania w `Arolsen_pobrania_Janina.jsonl`. Pierwsze pobranie obrazu przekroczyło czas; pojedyncze ponowienie zakończyło się poprawnym JPG. Nie traktowano pierwszej awarii jako braku dokumentu.

Wiersz Janiny znajduje się w dolnej części listy transportowej. Nagłówek kolumny brzmi „Imię ojca”; w wierszu **Janina, nazwisko zapisywane Chmielewski/Chmielenski, ojciec Jan, rok 1910**. Miejsce urodzenia odczytano niepewnie jako **[Łotowice?]**, nie Socha. Dokładnego dnia/miesiąca nie ma. Nie używano niepewnego miejsca do szukania nowej rodziny.

P04 ma w pierwotnych aktach 1910 i 1936 ojca **Józefa** i pochodzenie **Socha**. C32 pozostaje odrębnym zapisem; **nie przyjęto tożsamości z P04**. Różnice są podstawą odrzucenia tej identyfikacji w obecnym stanie, nie założenia, że lista transportowa jest nieomylna. Nie stworzono relacji rodzinnej.
