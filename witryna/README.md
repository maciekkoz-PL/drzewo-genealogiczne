# Drzewo Marysi

Adres: https://korzenie-marysi.maciekkoz187874.chatgpt.site

Użytkownik 05.11.2026 wybrał publiczny link, a następnie wyraźnie dopuścił publikację znanych danych żyjących krewnych. Nowsza decyzja zastępuje początkowe ograniczenie do anonimowych kart mamy i kuzyna. Repozytorium badań pozostaje prywatne. Hosting otrzymuje tylko statyczny plik strony i konfigurację; nie otrzymuje Excela, ZIP, fotografii rodzinnych, dzienników ani pełnej historii repozytorium badań.

`public/index.html` jest samodzielnym plikiem — zawiera wygląd, dane i interakcje, działa również po pobraniu. Strona nie pobiera bibliotek, fontów, analityki ani prywatnych plików z zewnętrznych serwisów. Źródła publicznych skanów otwierają się dopiero po kliknięciu. Meta robots noindex nie stanowi zabezpieczenia dostępu: witryna jest publiczna.

## Aktualizacja po kolejnej sesji

1. Najpierw zaktualizować badania i Excel. Potem ręcznie zaktualizować wybrane, publiczne dane `generuj.py`. Nie eksportować automatycznie wszystkich pól Excela: zawierają również robocze dane, adresy i hipotezy o homonimach, które wymagają redakcji przed pokazaniem w drzewie.
2. **Przy każdym ważnym odkryciu w tej samej sesji aktualizować drzewo i krótkie wpisy pod nim, a następnie opublikować stronę pod dotychczasowym adresem.** Użytkownik przypomniał tę zasadę06.11.2026 po odnalezieniu aktu66/1940. Do `events` dopisać przełomowe odkrycie: nową osobę potwierdzoną dokumentem, rozstrzygnięte pokrewieństwo lub odnaleziony ważny akt. Ważny akt może dotyczyć osoby o jeszcze niepotwierdzonym związku z rodziną: wtedy krótki wpis i karta muszą jasno nazywać niepewność, a karty nie łączyć potwierdzoną relacją. Sam wynik indeksu, przypuszczenie bez dokumentu, pojedyncza kwerenda, liczba skanów i awaria nie są wpisem do kroniki. Łączyć powiązane ustalenia w jeden krótki wpis. Zachować proste drzewo i krótką kronikę, bez ozdobnego wstępu. Dla wpisu podać rzeczywisty commit zapisujący badania, tytuł, prosty opis i kategorię. Daty/godziny pobierane są z Git i opisane jako czas zapisu, nie dokładny moment odkrycia. Wpisy są sortowane po czasie; filtr ostatnich7dni używa bieżącego czasu odwiedzającego. Cała kronika pozostaje dostępna.
3. `python witryna/generuj.py`. Powstanie pełny `witryna/public/index.html`. Test przeglądarkowy: `python witryna/sprawdz.py` (Chromium/Playwright; w tym środowisku wymaga profilu wykonania umożliwiającego uruchomienie przeglądarki). W teście dostosować liczby osób/wpisów po świadomym rozszerzeniu drzewa. Sprawdzić telefon, dialogi, źródła i jawność H017 oraz poprawność publikowanych danych krewnych.
4. Zapisać wygenerowany HTML, generator i zmiany w prywatnym GitHubie. Osobne repozytorium hostingu: lokalnie `/workspace/marysia-site`, gałąź `main`, zdalny adres poniżej. Do jego `dist/index.html` skopiować WYŁĄCZNIE publiczny HTML. Zachować `.openai/hosting.json` z dokładnym istniejącym project_id; nie tworzyć nowej witryny. W razie utraty katalogu odtworzyć z repozytorium hostingu.
5. Push do repozytorium hostingu przy użyciu świeżego krótkotrwałego poświadczenia Sites (nie zapisywać tokenu w plikach/config ani w repo). Z aktualnego commitu przygotować TAR zawierający `.openai/hosting.json` i `dist/`. Obsługiwany format konfiguracji to `{"project_id":"…","static":{"directory":"dist"}}`.
6. Sites `save_site_version` z pełnym SHA wypchniętego commitu i lokalnym archiwum TAR, potem `deploy_site_version` z ID zapisanej wersji; publiczny dostęp już ustawiony zgodnie z życzeniem użytkownika. Sprawdzić `get_deployment_status` i rzeczywisty URL. Sam push do GitHuba ani repozytorium hostingu nie publikuje strony. Zapisać metadane wersji bez poświadczeń.

Repozytorium źródłowe hostingu:
`https://git.chatgpt-team.site/1985edeb-fc15-4121-9520-e4220a158d72/appgprj_6aeccd5dcec48191950b70bad04d3017.git`

## Granice widoku

- 14 kart:13wcześniejszych osób oraz osobna karta C42, z wyraźnym statusem „Pokrewieństwo do sprawdzenia”, bez linii łączącej ją z rodziną. Dane wybrane ręcznie, bez automatycznego eksportu homonimów i kandydatów z Excela.
- Marysia: imię i przybliżony rok urodzenia z przekazu (pełne imię/nazwisko nieustalone). Maria Jankowska: dane z odpisu, z odrębnym statusem macierzyństwa. Piotr Chmielewski: imię/nazwisko, oszacowanie daty i kontekst rodzinny; bez połączenia z kandydatem z prasy. Nieznany brat Bogusława pozostaje bez imienia.
- Własny odpis Bogusława dokumentuje nazwiska rodziców. Przypisanie dokładnych dat1909/1910 i starszej gałęzi nadal H017: komunikat na stronie, bursztynowe krawędzie, gwiazdki przy datach i szczegółowy opis kart.
- Daty zgonu Bogusława oraz częściowo Tomasza mają status rodzinnego przekazu. Pole nazwiska przyszłych dzieci w odpisie ślubu nie zostało użyte jako dowód pochodzenia Marysi.
- Badania i aktualizacje wymagają kolejnej aktywnej sesji. Nie uruchomiono harmonogramu, nie wysyłano wiadomości ani zaproszeń.

Sprawdzono w Chromium widok1440px i390px, otwieranie kart i przechodzenie po powiązaniach, filtrowanie kroniki, brak błędów JavaScript i obecność znanych danych krewnych wraz z oznaczeniami niepewności.

Aktualny układ: samo drzewo, krótkie oznaczenia dowodów i cztery ważne wpisy. Najnowszy dotyczy odczytanego aktu66/1940 i nie potwierdza jeszcze braterstwa. Szczegóły są w kartach osób; nagłówek pokazuje datę wygenerowania strony.
