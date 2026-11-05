# S064 — Geneteka, publiczne zapytania 5 listopada 2026

Odpowiedzi API zachowano jako pliki JSON. Pełne adresy zapytań GET, czas UTC i SHA-256 są w `pobrania.jsonl`. Interfejs: https://geneteka.genealodzy.pl/; endpoint: https://geneteka.genealodzy.pl/api/getAct.php . Nie utożsamiano osób na podstawie samego indeksu.

Uwaga techniczna: w części odpowiedzi liczba recordsTotal jest większa od długości data. To ogranicza kompletność wyników, także odpowiedzi bez rekordów. Pierwsza próba dla lubelskiego miała błędny kod 03lu; poprawiona próba 03lb jest w Geneteka_Czeslaw_1909.json. Nie traktować żadnego z tych wyników jako dowodu braku aktu.

| Plik | recordsTotal | Otrzymane wiersze |
| --- | ---: | ---: |
| [Geneteka_Czeslaw_1909.json](zrodla/Geneteka_Czeslaw_1909.json) | 0 | 0 |
| [Geneteka_Jozef_Poprawka_M_all.json](zrodla/Geneteka_Jozef_Poprawka_M_all.json) | 1 | 0 |
| [Geneteka_Lodz_Czeslaw_Janina_M_full.json](zrodla/Geneteka_Lodz_Czeslaw_Janina_M_full.json) | 1 | 1 |
| [Geneteka_Marianna_Poprawka_D.json](zrodla/Geneteka_Marianna_Poprawka_D.json) | 7 | 3 |
| [Geneteka_Poprawka_Kacprzak_M_all.json](zrodla/Geneteka_Poprawka_Kacprzak_M_all.json) | 0 | 0 |
| [Geneteka_Poprawka_Kacprzak_U.json](zrodla/Geneteka_Poprawka_Kacprzak_U.json) | 3 | 1 |
| [Geneteka_Warta_Poprawka_U_full.json](zrodla/Geneteka_Warta_Poprawka_U_full.json) | 6 | 4 |
| [Geneteka_Zygmunt_Poprawka_U.json](zrodla/Geneteka_Zygmunt_Poprawka_U.json) | 0 | 0 |
| [Lodzkie_Chmielewski_Poprawka_M.json](zrodla/Lodzkie_Chmielewski_Poprawka_M.json) | 1 | 0 |
| [Warta_Poprawka_Kacprzak_M.json](zrodla/Warta_Poprawka_Kacprzak_M.json) | 0 | 0 |
| [Warta_Poprawka_U.json](zrodla/Warta_Poprawka_U.json) | 6 | 5 |

Najważniejsze wskazania: Janina Poprawka 112/1910 Warta, Józef Poprawka 64/1918 Warta, Kazimiera Poprawka 13/1916 Kamionacz. Wszystkie trzy akty odczytano niezależnie na oryginalnych obrazach (S063/S065/S066). Pary rodziców mają rozbieżne wieki; C25/C26 nie uznano za potwierdzone rodzeństwo. Inne dzieci Poprawków w Warcie mają innych rodziców, w tym Antoniego i Franciszkę Wiśniewską; nie łączono rodzin.

Zapytania Zygmunt Poprawka i ślub Poprawka/Kacprzak nie dały nowych rozstrzygających dokumentów. Odnaleziony przez API ślub Czesława i Janiny 110/1936 odpowiada znanemu S001; nie jest nowym niezależnym świadectwem.
