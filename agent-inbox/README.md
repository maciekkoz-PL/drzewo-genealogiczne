# Skrzynka odkryć zewnętrznych agentów

Każdy agent zapisuje odkrycia w osobnym katalogu `agent-inbox/YYYY-MM-DD-agent-nazwa-temat/` na własnej gałęzi Git i otwiera pull request. Nie edytuje `badania/`, głównego Excela, danych drzewa ani publikowanej strony.

W katalogu umieść `RAPORT.md` oraz dowody lub manifest linków. Każdy wpis powinien zawierać:
- ID odkrycia, datę UTC, nazwę agenta i pytanie badawcze;
- osobę/hipotezę i jej istniejący identyfikator (lub wyraźne oznaczenie NOWY KANDYDAT);
- dosłowny odczyt źródła, dokładny URL, archiwum, zespół/sygnaturę, akt, obraz/stronę;
- ścieżkę kopii, SHA-256 jeśli pobrano plik, datę dostępu;
- rozdzielenie faktu źródłowego od interpretacji i alternatywnych identyfikacji;
- sprawdzenie duplikatów i listę przeszukanych zakresów;
- ocenę: potwierdzone źródłem / prawdopodobne / hipoteza / odrzucone;
- proponowany następny krok, bez samodzielnego wpisu do kanonicznego drzewa.

Status początkowy: **DO WERYFIKACJI**. Dopiero po niezależnym odczycie dowodu agent prowadzący podejmuje decyzję o wpisie do rejestrów, Excela i drzewa. Odrzucone tropy zachowuj z uzasadnieniem. Nie dodawaj prywatnych danych żyjących osób do publicznego repozytorium.
