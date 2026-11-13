# Audyt repozytorium przed kontynuacją badań

13 listopada 2026, UTC. Agent: OpenAI Codex. Pytanie użytkownika: odnaleźć informacje zapisane przez Claude Code gdziekolwiek w repozytorium `maciekkoz-PL/drzewo-genealogiczne`, zanim wznowimy badania lub aktualizację bazy.

**W dostępnych gałęziach i załącznikach nie odnaleziono oddzielnego raportu badawczego Claude Code ani nowych dowodów genealogicznych ponad stan etapu 32.** Znaleziono niepołączony z `main` PR nr 1 dotyczący organizacji pracy. Ten wynik dotyczy sprawdzonych zasobów GitHuba; nie rozstrzyga, co pozostało w niezapisanej rozmowie lub środowisku innego agenta.

## Gałęzie i rzeczywiste zmiany

| Gałąź | Commit w chwili audytu | Co zawiera ponad znany stan |
| --- | --- | --- |
| `main` | `08b5991c3aa4724215c23256ddc7ada4570caab5` | Ostatni zapis badań: etap 32. |
| `copilot/help-with-project` | ten sam `08b5991…` | Identyczne drzewo plików jak `main`; brak dodatkowych wyników. |
| `proposal/agent-handoff-2026-11-13` | ten sam `08b5991…` | Identyczne drzewo plików jak `main`; brak dodatkowych wyników. |
| `docs/agent-handoff-2026-11-13` | `93b2503251a504278b0ee49e9c622c35aec772ca` | Trzy commity, tylko zmieniony `README.md` i nowy `agent-inbox/README.md`. Nawigacja, podział ról agentów i reguły przekazywania odkryć; bez raportu z odkryciami, skanu, metryki lub zmiany Excela. |
| `work` | `edf13842388ed8405eca1aa10deda8b4f32737bb` | Jeden commit spoza historii `main`, z 6 listopada: adresy i odnośniki do map w kartach osób. Starsza podstawa danych: 47 osób zamiast 70 w bieżącym `main`. Nie jest nowszą bazą badań. |

Adresy z tego commitu `work` porównano z dzisiejszymi kartami w `main`: Rachanie/Rogóźno dla P05/P06, Socha dla P07, Stocka 12 dla P03/P04, Stara Gadka dla P09 oraz Napiórkowskiego 112 dla C42 są już obecne. W samym commicie nie zmieniono źródeł, połączeń ani ocen relacji. Nie ma podstaw do dopisywania tych informacji jako nowych odkryć lub do zastępowania bieżącego drzewa starszą wersją.

## Odnalezione miejsce przekazania

- [PR nr 1 — „Uporządkowanie README i bezpieczna skrzynka odkryć agentów”](https://github.com/maciekkoz-PL/drzewo-genealogiczne/pull/1), otwarty szkic. Lista zmienionych plików potwierdzona osobnym odczytem API.
- [Nowe README, dokładny commit](https://github.com/maciekkoz-PL/drzewo-genealogiczne/blob/93b2503251a504278b0ee49e9c622c35aec772ca/README.md).
- [Instrukcja skrzynki odkryć, dokładny commit](https://github.com/maciekkoz-PL/drzewo-genealogiczne/blob/93b2503251a504278b0ee49e9c622c35aec772ca/agent-inbox/README.md).

Przed dodaniem niniejszego audytu skrzynka zawierała **wyłącznie instrukcję README**, bez katalogu odkryć któregokolwiek agenta. PR nie ma komentarzy rozmowy, recenzji ani komentarzy do zmian. Nie scalono go w ramach audytu. Z nazwiska autora commitów nie można ustalić, w jakim narzędziu je utworzono: wszystkie dostępne zdarzenia przypisane są kontu użytkownika.

## Zakres kontroli

1. Porównano pełne listy pięciu gałęzi z `git ls-remote` i łącznika GitHub; sprawdzono również ostatnią stronę listy. Pobrano wszystkie gałęzie, nie tylko `main`.
2. Zinwentaryzowano **3627 różnych ścieżek** we wszystkich dostępnych gałęziach i historię **120 commitów**. Porównano wszystkie zmiany gałęzi spoza historii `main`, a nowe dokumenty przeczytano w całości.
3. Przeszukano **2337 różnych blobów plików tekstowych** pod kątem `Claude`, `Claude Code`, `Cloud Code` i `Anthropic`. Trafienia poza nowym README dotyczą komunikatu narzędzia MCP, opisów innych narzędzi lub historycznych osób o imieniu Claude; nie stanowią raportów badawczych agenta. Nie twierdzimy, że ponownie przepisano wszystkie archiwalne obrazy.
4. Sprawdzono wszystkie dostępne PR-y: jeden. Osobne zgłoszenia: zero. Komentarze do commitów: zero. Wydania i ich załączniki: zero. Artefakty GitHub Actions: zero. Wiki i Discussions są wyłączone, liczba forków: zero. Nie ma opublikowanych tagów ani notatek Git.
5. Zapisano wszystkie **87 zwróconych zdarzeń repozytorium**. Wszystkie **86 identyfikatorów commitów** z pól `head`/`before` są dostępne w pobranej historii; w tym zakresie nie pojawił się dodatkowy niepobrany commit. API zdarzeń jest ograniczonym rejestrem, nie gwarancją pełnej historii usuniętych zasobów.
6. Porównano znaczenie zmian danych drzewa z gałęzi `work` z jej rodzicem i bieżącym `main`. Odnotowano starszeństwo tej gałęzi, żeby uniknąć cofnięcia wyników późniejszych sesji.

Pliki audytowe zawierają inwentarze gałęzi, listę commitów, odpowiedzi GitHub/API i porównanie danych adresowych. Pełne, wcześniejsze źródła genealogiczne pozostają w dotychczasowych katalogach `badania/`.

## Przyczyna niewidoczności gałęzi

Lokalne `remote.origin.fetch` miało wartość `+refs/heads/main:refs/remotes/origin/main`. Zwykłe `git fetch --all` pobierało więc tylko `main`. Dodatkowe gałęzie wykryto przez `git ls-remote --heads origin`, a następnie pobrano jawnym refspecem wszystkich gałęzi. W tej kopii lokalnej ustawiono `+refs/heads/*:refs/remotes/origin/*`, aby kolejne pobrania obejmowały całość. To konfiguracja lokalnego repozytorium, nie zmiana danych rodzinnych ani ustawień serwisu GitHub.

## Wniosek dla badań

Nie ma nowego odkrycia do przeniesienia z tych gałęzi do Excela lub drzewa. Nadal obowiązuje stan etapu 32: rodzice Bogusława wymienieni w S086; H017 otwarta; brat P11 bez imienia; tożsamość Piotra P10/C19 niepotwierdzona; matka i pełne urodzenie Tomasza P09 nieustalone.

Lokalny, niezatwierdzony jeszcze pakiet etapu 33 z przeglądu ksiąg i wybranych dokumentów Arolsen jest pracą tej sesji. Nie był obecny w sprawdzonym zdalnym repozytorium i nie przypisano go Claude Code. Jego odczyty wymagają osobnego utrwalenia wraz z własnym zakresem źródłowym.

Jeżeli Claude Code rzeczywiście ustalił nowe relacje, potrzebny jest zapis z tamtej sesji lub wskazanie innego miejsca publikacji. Samo README o współpracy nie dowodzi wykonania badań. Kontynuację można oprzeć na już zabezpieczonych źródłach bez przypisywania nieodnalezionych odkryć rodzinie.
