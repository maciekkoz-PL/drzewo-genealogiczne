# Publiczne drzewo Marysi

Adres: https://korzenie-marysi.maciekkoz187874.chatgpt.site

Użytkownik 05.11.2026 wybrał publiczny link z minimalnymi danymi osób żyjących. Repozytorium badań pozostaje prywatne. Hosting otrzymuje tylko statyczny plik strony i konfigurację; nie otrzymuje Excela, ZIP, fotografii rodzinnych, dzienników ani pełnej historii repozytorium badań.

`public/index.html` jest samodzielnym plikiem — zawiera wygląd, dane i interakcje, działa również po pobraniu. Strona nie pobiera bibliotek, fontów, analityki ani prywatnych plików z zewnętrznych serwisów. Źródła publicznych skanów otwierają się dopiero po kliknięciu. Meta robots noindex nie stanowi zabezpieczenia dostępu: witryna jest publiczna.

## Aktualizacja po kolejnej sesji

1. Najpierw zaktualizować badania i Excel. Potem ręcznie zaktualizować wybrane, publiczne dane `generuj.py`. Nie eksportować automatycznie wszystkich pól Excela: zawierają dane żyjących osób, adresy i hipotezy o homonimach.
2. Do `events` dopisać istotny wynik, rzeczywisty commit zapisujący badania, tytuł, prosty opis i kategorię. Daty/godziny pobierane są z Git i opisane jako czas zapisu, nie dokładny moment odkrycia. Wpisy są sortowane po czasie; filtr ostatnich7dni używa bieżącego czasu odwiedzającego. Cała kronika pozostaje dostępna.
3. `python witryna/generuj.py`. Powstanie pełny `witryna/public/index.html`. Test przeglądarkowy: `python witryna/sprawdz.py` (Chromium/Playwright; w tym środowisku wymaga profilu wykonania umożliwiającego uruchomienie przeglądarki). W teście dostosować liczby osób/wpisów po świadomym rozszerzeniu drzewa. Sprawdzić telefon, dialogi, źródła i jawność H017 oraz brak danych osób żyjących.
4. Zapisać wygenerowany HTML, generator i zmiany w prywatnym GitHubie. Osobne repozytorium hostingu: lokalnie `/workspace/marysia-site`, gałąź `main`, zdalny adres poniżej. Do jego `dist/index.html` skopiować WYŁĄCZNIE publiczny HTML. Zachować `.openai/hosting.json` z dokładnym istniejącym project_id; nie tworzyć nowej witryny. W razie utraty katalogu odtworzyć z repozytorium hostingu.
5. Push do repozytorium hostingu przy użyciu świeżego krótkotrwałego poświadczenia Sites (nie zapisywać tokenu w plikach/config ani w repo). Z aktualnego commitu przygotować TAR zawierający `.openai/hosting.json` i `dist/`. Obsługiwany format konfiguracji to `{"project_id":"…","static":{"directory":"dist"}}`.
6. Sites `save_site_version` z pełnym SHA wypchniętego commitu i lokalnym archiwum TAR, potem `deploy_site_version` z ID zapisanej wersji; publiczny dostęp już ustawiony zgodnie z życzeniem użytkownika. Sprawdzić `get_deployment_status` i rzeczywisty URL. Sam push do GitHuba ani repozytorium hostingu nie publikuje strony. Zapisać metadane wersji bez poświadczeń.

Repozytorium źródłowe hostingu:
`https://git.chatgpt-team.site/1985edeb-fc15-4121-9520-e4220a158d72/appgprj_6aeccd5dcec48191950b70bad04d3017.git`

## Granice widoku

- 13 kart osób z dwóch podstawowych arkuszy, z ręczną redakcją dla publikacji. Nie dodano homonimów ani kandydatów do drzewa.
- Marysia tylko z imienia; mama bez nazwiska i dat; kuzyn bez imienia, zawodu i dat. Nieznany brat Bogusława pozostaje bez imienia. Dane osób urodzonych na początku XXw. pochodzą z historycznych aktów.
- Własny odpis Bogusława dokumentuje nazwiska rodziców. Przypisanie dokładnych dat1909/1910 i starszej gałęzi nadal H017: komunikat na stronie, bursztynowe krawędzie, gwiazdki przy datach i szczegółowy opis kart.
- Daty zgonu Bogusława oraz częściowo Tomasza mają status rodzinnego przekazu. Pole nazwiska przyszłych dzieci w odpisie ślubu nie zostało użyte jako dowód pochodzenia Marysi.
- Badania i aktualizacje wymagają kolejnej aktywnej sesji. Nie uruchomiono harmonogramu, nie wysyłano wiadomości ani zaproszeń.

Sprawdzono w Chromium widok1440px i390px, otwieranie kart i przechodzenie po powiązaniach, filtrowanie kroniki, brak błędów JavaScript i brak wybranych prywatnych pól w osadzonym JSON.
