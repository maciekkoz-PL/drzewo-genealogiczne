# S082 — wniosek o akt urodzenia bez znajomości PESEL ojca

Sprawdzono 5 listopada 2026 po odpowiedzi użytkownika. Rodzina nie ma dokumentu z danymi rodziców Bogusława; Marysia nie zna PESEL ojca. Użytkownik doprecyzował, że blokada występuje w formularzu internetowym. To relacja użytkownika o formularzu; nie oglądano jego zalogowanej sesji i nie wypełniano usługi.

## Co sprawdzono

1. [Gov.pl — odpis aktu stanu cywilnego](https://www.gov.pl/web/gov/uzyskaj-odpis-aktu-stanu-cywilnego-urodzenia-malzenstwa-zgonu), istniejące S047: dla odpisu urodzenia innej osoby podaje imię, nazwisko, miejsce i datę urodzenia, a PESEL wymienia jako dane dodatkowe. Numer aktu także jest informacją dodatkową. Potomkowie są uprawnieni do odpisu. Dostępne są tryby osobisty i listowny.
2. [USC Łódź — procedura KA-01137](https://lckm.uml.lodz.pl/procedura/KA-01137), S082: wniosek można złożyć osobiście albo listownie, USC w Łodzi, al. Piłsudskiego 100, 92-326 Łódź. Podano uprawnienie dzieci i dokument tożsamości do okazania przy osobistym składaniu.
3. [Oryginalny druk urodzenia DOCX](https://lckm.uml.lodz.pl/sites/default/files/procedura/USC_W_wniosek_odpis_aktu_urodzenia_220205_7.docx): pobrano plik 28 372 bajty, sprawdzono CRC i odczytano cały tekst XML. **Druk ma osobne pola PESEL wnioskodawcy i osoby, której akt dotyczy.** Nie należy twierdzić, że w druku nie ma pola PESEL. Samo pole nie przeczy opisowi gov.pl, który wymienia PESEL osoby poszukiwanej jako dodatkowy. W szkicu wskazano PESEL ojca jako nieznany i poproszono o wyszukanie według imion, nazwiska, daty i miejsca.

To potwierdza dostępną drogę złożenia wniosku bez używania blokującego formularza online; **nie jest dowodem odnalezienia aktu ani gwarancją zgodności daty rodzinnej z księgą**. Nie sprawdzono, czy internetowy formularz ma wariant bez PESEL. Nie wysłano żadnej wiadomości, nie składano wniosku i nie wniesiono opłaty.

## Korekta wcześniejszej informacji o opłacie

Gov.pl podaje ogólną stawkę 33 zł za odpis zupełny. Łódzka procedura i pobrany druk dodatkowo wskazują **39 zł za odpis zupełny aktu sporządzonego przed 1 stycznia 1946 r.** Dla aktu sporządzonego w 1943 r. właściwa wskazana stawka to 39 zł. Gdyby urodzenie zarejestrowano dopiero po wojnie, sam rok urodzenia nie rozstrzyga daty sporządzenia aktu. Przed zapłatą należy ustalić właściwą kategorię. Nie dokonano płatności.

## Materiały lokalne

- [Oryginalny druk USC](zrodla/S082_USC_Lodz_formularz_urodzenia.docx).
- [Odczyt wszystkich akapitów druku](S082_formularz_odczyt.txt).
- [Szkic pisma z nieznanym PESEL ojca](Wniosek_Boguslaw_BEZ_PESEL_SZKIC.docx) — niepodpisany, niewysłany, dane Marysi do samodzielnego wpisania.
- [Adresy pobrania, rozmiary i SHA-256](S082_pobrania.json).
- Oryginalne HTML obu procedur zachowano w zrodla; odpowiedzi narzędzia w S082_procedura_Lodz_odczyt.json i S082_weryfikacja_PESEL_gov_i_wyszukanie.json. Nie czytano ponownie innych dokumentów zamrożonej gałęzi.
