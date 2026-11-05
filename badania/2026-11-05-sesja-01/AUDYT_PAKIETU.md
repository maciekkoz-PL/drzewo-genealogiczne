# Audyt pakietu przekazania — 5 listopada 2026

Stan początkowy: commit `dfca86aa67c4ac40f1f5c355ac9e251e7f325b7f`. Przeczytano całą instrukcję (335 wierszy), wszystkie 16 arkuszy bazy głównej, README pakietu i tekst raportu HTML. Wszystkie komórki wszystkich arkuszy dziewięciu wcześniejszych XLSX odczytano programowo, porównano unikalne wiersze i adresy URL. Historyczne pliki nie zastępują bazy głównej.

## Integralność i identyfikatory

- ZIP: 22 pliki, kontrola CRC bez błędów; pełny manifest z SHA-256 w `manifest_pakietu.json`. Obie główne kopie MD/XLSX w ZIP są bajtowo identyczne z plikami w katalogu repozytorium.
- Baza główna: 56 źródeł S001–S056, 11 osób P01–P11, 24 kandydatów C01–C24, 12 relacji R001–R012, 28 zdarzeń, 28 zadań, 24 korekty i 19 wpisów dziennika. Brak powtórzonych ID wewnątrz poszczególnych tabel. Brak formuł. Adresy URL były zwykłym tekstem, bez obiektów hiperłączy.
- REL-001, REL-002 i REL-003 występują jako źródła, ale nie miały własnego rejestru. Dodano rejestr pochodzenia tych oznaczeń. Są to streszczenia przekazów odziedziczone z pakietu; oryginalnych rozmów ani dokumentów USC nie ma w repozytorium.
- Starsze bazy używały P12–P16 dla obecnych C01–C05 oraz R01–R15 w odmiennym znaczeniu. Nie przenosić ich identyfikatorów bez mapowania. Nowe rekordy należy interpretować w kontekście wersji pliku.
- F01–F06 podawały same nazwy plików, F07 pomijał katalog `raport_z_poprzedniej_sesji/`. Uzupełniono ścieżki w tabeli plików. Trzy kadry aktu 110 były w ZIP, ale brakowało ich w tabeli; dodano je.
- Raport HTML wspomina wcześniejszy plik `Marysia_rejestr_rodziny_2026-11-04_V_potencjalne_powiazania.xlsx`, którego nie ma w ZIP. Nie można uznać tej wersji za przeanalizowany załącznik. Dziewięć faktycznie dostarczonych historycznych plików jest dostępnych.

## Kontrola treści oryginalnych obrazów

Obejrzano pełny obraz małżeństwa 110/1936, jego kadry, okładkę i stronę tytułową skorowidza 1943ax oraz wszystkie trzy fotografie nagrobka Tomasza. Potwierdzono dane krytyczne: oboje małżonkowie Stocka 12; Czesław robotnik, 26 lat; Janina 25 lat; imiona i nazwiska rodziców; tytuł skorowidza 1 lipca–31 grudnia 1943. Fotografie Tomasza nie odsłaniają całego roku zgonu. Współrzędne miejsca pochodzą z przekazu zapisanego w pakiecie; nie wykonano niezależnego pomiaru lokalizacji. Nie poszukiwano ponownie grobu Tomasza.

Małżeństwo z 1936 nie potwierdza pochodzenia Bogusława. Wzmianki zawodowe policjanta nie potwierdzają pokrewieństwa Piotra. Zbieżne nazwiska w grobach i indeksach pozostają odrębnymi tożsamościami.

## Odnośniki i dostępność

Sprawdzono 45 unikalnych adresów przypisanych do wszystkich 56 rekordów źródeł. Surowe wyniki HTTP i klasyfikację zachowano w `audyt_http.jsonl` i `audyt_url.json`. Sam kod HTTP 200 nie jest potwierdzeniem dostępu do treści.

- S024 (`ewidencja_ludnosci.pdf`) zwraca 404. Należy odnaleźć aktualną kopię opracowania; nie twierdzić, że w tej sesji przeczytano ten PDF.
- S035 (BIP I KP Łódź) i S041 (PDF prasy) zwróciły 503 podczas tej próby. To problem dostępu, bez wyniku genealogicznego.
- S010, S020, S022 w bezpośrednim HTTP zwracają stronę ochronną. Firecrawl odczytuje katalog zespołu, ale karty jednostek Stockiej i Czesława zwróciły komunikat „Portlety jest tymczasowo niedostępny”. Nie przejrzano 85 skanów Stockiej.
- S051 przekierowuje do logowania Facebooka; nie odczytano treści grupy.
- Katalog USC Łódź w Skanotece pokazuje dla 1943 tylko tom 1943ax. Nie znaleziono w tym katalogu osobnego tomu pierwszego półrocza. Nie oznacza to braku księgi w zasobie archiwum/USC.
- Indeksy Lubgens zawierają dokładniejsze odnośniki, pominięte w przekazaniu: Roman 226/1919 i Janina 160/1913 mają linki do konkretnych skanów. Indeks Czesława 241/1909 ma link do jednostki 10505094. Te odnośniki wykorzystano w dalszych badaniach.

Szkice Gmail: ich aktualnego stanu nie sprawdzano w skrzynce; status w bazie jest wyłącznie stanem odziedziczonym z pakietu. W tej sesji nie wysłano wiadomości ani wniosków.
