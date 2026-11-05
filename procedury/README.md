# Odtwarzanie dostępu do publicznych skanów

Uruchamiać z katalogu głównego repozytorium. Potrzebne Python 3, `playwright`, Chromium, `lxml`; do bazy `openpyxl`. W tej sesji Chromium znajdował się w `/usr/bin/chromium`. W innym środowisku należy dostosować ścieżkę. Skrypty nie pobierają danych logowania, nie wysyłają wiadomości i nie składają wniosków. Nie należy dodawać dowolnych/zgadywanych identyfikatorów.

## SwA — manifesty

Karty jednostek często zwracały błąd portletu. Publiczna przeglądarka korzysta jednak z GET `/o/pliki-api/pliki/jednostka/ID/OFFSET/LICZBA` oraz `/zespol/ID/OFFSET/LICZBA`. Użycie tych metod potwierdzono w publicznym JavaScript oficjalnego serwisu. Odpowiedzi mogą zamiast JSON zawierać HTML ochronny z HTTP 200 — nie są wtedy dokumentem ani wynikiem negatywnym.

```bash
python procedury/pobierz_manifest_swa.py 10505094 --count 200 --output work/manifest1909.json
python procedury/pobierz_manifest_swa.py 165812 --kind zespol --count 300 --output work/manifestUSC.json
```

**Nie ponawiać tych przykładów bez potrzeby:** kompletne odpowiedzi już są w `badania/2026-11-05-sesja-01/zrodla/`. Dla 165812 wszystkie 277 skanów to zgony 1940, bez urodzeń H1 1943. Dla jednostek o większej liczbie obrazów porównać `len(elementy)` z `liczbaWszystkichSkanow` i użyć następnego offsetu. Nie uznawać pierwszych 100 obrazów za cały tom 129-obrazowy.

W tym środowisku Chromium nie ufał certyfikatowi pośredniczącego proxy. Zastosowano transport: przeglądarka wykonuje zwykłe żądania, a Python `urllib` realizuje je z **normalną weryfikacją TLS** i przekazuje odpowiedź do przeglądarki. Nie wyłączano TLS, nie rozwiązywano CAPTCHA, nie logowano się. Skrypty dopuszczają tylko GET/HEAD w domenach archiwalnych. Przycisk „Nie” na pytaniu o nową przeglądarkę zmienia tylko lokalną preferencję bieżącego, tymczasowego profilu.

## SwA — obrazy

Z manifestu wybierać dokładne pole `src` i `pozycja`, a nie zgadywać hash. Plik zlecenia:

```json
[
  {"url": "DOKŁADNE_POLE_SRC_Z_MANIFESTU", "path": "work/wybrany_skan.jpg"}
]
```

```bash
python procedury/pobierz_obrazy_swa.py work/zlecenie.json
```

Pobranie uznawane jest za JPG dopiero po sprawdzeniu sygnatury bajtowej. Istniejące JPG są pomijane. Dziennik zawiera URL, czas UTC, rozmiar i SHA-256. Przenosząc nowy dowód do `badania/`, przenieść również dziennik, dopisać S/F/L oraz dokładny zakres **odczytu wzrokowego**. Samo pobranie nie jest odczytem. Stare nieudane odpowiedzi zachowano z końcówką `.odpowiedz.html`.

## Arolsen

```bash
python procedury/pobierz_arolsen.py ZNANY_DOCID --outdir work/arolsen --log work/arolsen_pobrania.jsonl
```

Przykładowe znane DocID: 70380716, 70381403, 70380976, 70381086, 70431406. **Wszystkie już pobrano i odczytano — używać lokalnych kopii.** Skrypt pobiera stronę dokumentu, wskazany tam JPG i publiczny indeks `GetPersonListByDocId`; pomija istniejące pliki. Nie wywołuje usług zamawiania dokumentów.

Wyszukiwanie globalne wymaga zachowania zwykłych ciasteczek pomiędzy `BuildQueryGlobalForAngular`, `GetCount` i `GetPersonList`. Dokładne parametry sprawdzonych zapytań znajdują się w plikach `Arolsen_*zapytania*.json`. Brak ciasteczek dawał pozornie pustą listę. Pola indeksu bywają niepełne lub mają przestawione nazwiska; data API 07/03/1909 w odczytanych dokumentach oznacza 3 lipca, co zweryfikowano na obrazie.

## Straty i IPN

Straty używa formularza POST do **wyszukiwania i podglądu**; to odrębne od kwestionariusza zgłaszania nowych danych. W kopiach HTML dane wyników są często w wartościach `input`, więc sam `text_content()` je pomija. Rekordy 5791928/4205404 są zachowane lokalnie wraz z polami POST. Nie dopisywać rekordów do bazy serwisu.

Inwentarz IPN miewa przekierowania kasujące parametry lub pętle językowe. Zawsze sprawdzić końcowy URL, wpisane kryteria i licznik wyników. Poprawne konkretne opisy: `/en/node/3896102` (C27, 91 stron akt nieodczytanych), `/en/node/5543826` (C30, inna data), `/en/node/5237877` (C31, inna data). Nie naciskać opcji dodania do formalnej kwerendy ani wysyłki bez zatwierdzenia.

Skrypty SwA powstały z pomocników rzeczywiście użytych w sesji; sprawdzono ich składnię i interfejs argumentów. Zmiana ścieżki Chromium lub mechanizmu serwisu może wymagać aktualizacji. Nie traktować awarii skryptu jako dowodu braku archiwaliów.
