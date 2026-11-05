# Stan przygotowania środowiska — 2026-11-05

Projekt jest bazą wiedzy genealogicznej rodziny Marysi. Nie wymaga budowy ani uruchamiania aplikacji. Nie rozpoczęto badań genealogicznych.

## Sprawdzone możliwości
- Python 3.12.14.
- Odczyt tekstu PDF przez pypdf 6.10.0 i pdfplumber 0.11.9.
- Renderowanie PDF do obrazu przez PyMuPDF 1.26.6.
- Zapis i odczyt syntetycznego XLSX przez pandas 2.2.3 i openpyxl 3.1.5.
- xlrd 2.0.1 jest dostępny; pliku XLS nie testowano.
- Tesseract: systemowe eng/osd; dodatkowo pol/deu/rus/lat z oficjalnego tessdata_fast. Wszystkie dodatkowe modele uruchomiono na syntetycznym obrazie i sprawdzono rozpoznanie roku. To nie potwierdza jakości odczytu dokumentów historycznych.
- Odczyt GitHub i HTTPS do PyPI działały przez proxy.

## Pliki i odtwarzanie
Skrypt scripts/przygotuj-ocr.sh sprawdza dostępność bibliotek w bazowym obrazie i pobiera dodatkowe modele OCR. Nie instaluje bibliotek Python ani Tesseract w nowym, pustym systemie. Modele są przechowywane poza repozytorium w /workspace/genealogy-tools/tessdata; nie są wersjonowane. Skrypt wykonano z powodzeniem w tej instancji. Instrukcje kolejnych sesji zawiera instrukcje-srodowiska.md.

## Sieć i ograniczenia
Podczas testów strony główne Szukaj w Archiwach, Geneteki, Metryk, FamilySearch i Polony zwracały proxy CONNECT 403. Nie były to wyniki wyszukiwania osób.
Domeny z domeny-archiwow.json, install_script oraz start_skill zapisano w projekcie konfiguracji środowiska (revision 2). Ponowny odczyt potwierdził zapis. Aktywna polityka bieżącej instancji nadal nie zawiera tych domen. Zapis projektu konfiguracji nie oznacza zastosowania ani publikacji.
Użytkownik powinien przejrzeć i zapisać zmiany w ustawieniach, a następnie opublikować środowisko. Po zastosowaniu zmian trzeba ponowić test dostępu. Przekierowania i hosty skanów mogą wymagać kolejnych domen.
W bieżącej sesji brak narzędzia przeglądarki i wyszukiwarki internetowej. Dostęp HTTP nie gwarantuje obsługi JavaScript, CAPTCHA, kont i płatnych zasobów.
OCR wymaga kontroli wzrokowej, szczególnie dla rękopisów, starych krojów i uszkodzonych skanów.

## Kontynuacja
Czytaj README, historię Git i dotychczasowe ustalenia. Rozpoczynaj badania wyłącznie po zleceniu. Zapisuj dokładne źródła, sygnatury, daty dostępu, fakty, hipotezy i sprzeczności. Nie wnioskuj o tożsamości tylko z nazwiska.
