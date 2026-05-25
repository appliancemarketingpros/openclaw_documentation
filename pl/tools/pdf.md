---
title: Narzędzie PDF
source_url: https://docs.openclaw.ai/pl/tools/pdf
scraped_at: 2026-05-25
---

`pdf` analizuje jeden lub więcej dokumentów PDF i zwraca tekst.

Szybkie zachowanie:

  * Tryb natywny dostawcy dla dostawców modeli Anthropic i Google.
  * Tryb awaryjnego wyodrębniania dla innych dostawców (najpierw wyodrębnia tekst, a następnie obrazy stron, gdy jest to potrzebne).
  * Obsługuje pojedyncze (`pdf`) lub wielokrotne (`pdfs`) dane wejściowe, maksymalnie 10 plików PDF na wywołanie.


## Dostępność

Narzędzie jest rejestrowane tylko wtedy, gdy OpenClaw może rozpoznać konfigurację modelu obsługującego PDF dla agenta:

  1. `agents.defaults.pdfModel`
  2. awaryjnie `agents.defaults.imageModel`
  3. awaryjnie rozpoznany model sesji/domyślny agenta
  4. jeśli natywni dostawcy PDF są oparci na uwierzytelnianiu, preferuj ich przed ogólnymi kandydatami awaryjnymi obsługującymi obrazy


Jeśli nie można rozpoznać żadnego użytecznego modelu, narzędzie `pdf` nie jest udostępniane.

Uwagi dotyczące dostępności:

  * Łańcuch awaryjny uwzględnia uwierzytelnianie. Skonfigurowany `provider/model` liczy się tylko wtedy, gdy OpenClaw może faktycznie uwierzytelnić tego dostawcę dla agenta.
  * Natywni dostawcy PDF to obecnie **Anthropic** i **Google**.
  * Jeśli rozpoznany dostawca sesji/domyślny ma już skonfigurowany model vision/PDF, narzędzie PDF używa go ponownie przed przejściem awaryjnym do innych dostawców opartych na uwierzytelnianiu.


## Odwołanie do danych wejściowych

Jedna ścieżka lub URL do pliku PDF.

Wiele ścieżek lub URL-i do plików PDF, łącznie do 10.

Prompt analizy.

Filtr stron, taki jak `1-5` lub `1,3,7-9`.

Opcjonalne nadpisanie modelu w formie `provider/model`.

Limit rozmiaru na plik PDF w MB. Domyślnie `agents.defaults.pdfMaxBytesMb` lub `10`.

Uwagi dotyczące danych wejściowych:

  * `pdf` i `pdfs` są scalane i deduplikowane przed wczytaniem.
  * Jeśli nie podano żadnego wejścia PDF, narzędzie zgłasza błąd.
  * `pages` jest parsowane jako numery stron liczone od 1, deduplikowane, sortowane i ograniczane do skonfigurowanej maksymalnej liczby stron.
  * `maxBytesMb` domyślnie przyjmuje `agents.defaults.pdfMaxBytesMb` lub `10`.


## Obsługiwane odwołania do PDF

  * lokalna ścieżka pliku (w tym rozwinięcie `~`)
  * URL `file://`
  * URL `http://` i `https://`
  * zarządzane przez OpenClaw odwołania przychodzące, takie jak `media://inbound/<id>`


Uwagi dotyczące odwołań:

  * Inne schematy URI (na przykład `ftp://`) są odrzucane z `unsupported_pdf_reference`.
  * W trybie piaskownicy zdalne URL-e `http(s)` są odrzucane.
  * Przy włączonej polityce plików ograniczonej do obszaru roboczego lokalne ścieżki plików poza dozwolonymi katalogami głównymi są odrzucane.
  * Zarządzane odwołania przychodzące i odtworzone ścieżki w magazynie mediów przychodzących OpenClaw są dozwolone przy polityce plików ograniczonej do obszaru roboczego.


## Tryby wykonania

### Tryb natywny dostawcy

Tryb natywny jest używany dla dostawców `anthropic` i `google`. Narzędzie wysyła surowe bajty PDF bezpośrednio do API dostawcy.

Limity trybu natywnego:

  * `pages` nie jest obsługiwane. Jeśli jest ustawione, narzędzie zwraca błąd.
  * Wejście z wieloma plikami PDF jest obsługiwane; każdy PDF jest wysyłany jako natywny blok dokumentu / część PDF inline przed promptem.


### Tryb awaryjnego wyodrębniania

Tryb awaryjny jest używany dla dostawców nienatywnych.

Przepływ:

  1. Wyodrębnij tekst z wybranych stron (do `agents.defaults.pdfMaxPages`, domyślnie `20`).
  2. Jeśli długość wyodrębnionego tekstu jest mniejsza niż `200` znaków, renderuj wybrane strony do obrazów PNG i dołącz je.
  3. Wyślij wyodrębnioną zawartość wraz z promptem do wybranego modelu.


Szczegóły trybu awaryjnego:

  * Wyodrębnianie obrazów stron używa budżetu pikseli `4,000,000`.
  * Jeśli model docelowy nie obsługuje danych wejściowych obrazu i nie ma tekstu możliwego do wyodrębnienia, narzędzie zgłasza błąd.
  * Jeśli wyodrębnianie tekstu się powiedzie, ale wyodrębnianie obrazów wymagałoby vision w modelu tylko tekstowym, OpenClaw pomija wyrenderowane obrazy i kontynuuje z wyodrębnionym tekstem.
  * Awaryjne wyodrębnianie używa dołączonego Plugin `document-extract`. Plugin jest właścicielem `pdfjs-dist`; `@napi-rs/canvas` jest używany tylko wtedy, gdy dostępny jest awaryjny rendering obrazów.


## Konfiguracja

json5Copy code
[code]
    {  agents: {    defaults: {      pdfModel: {        primary: "anthropic/claude-opus-4-6",        fallbacks: ["openai/gpt-5.4-mini"],      },      pdfMaxBytesMb: 10,      pdfMaxPages: 20,    },  },}
[/code]

Zobacz [Odwołanie do konfiguracji](</pl/gateway/configuration-reference>), aby uzyskać pełne szczegóły pól.

## Szczegóły wyjścia

Narzędzie zwraca tekst w `content[0].text` oraz ustrukturyzowane metadane w `details`.

Typowe pola `details`:

  * `model`: rozpoznane odwołanie do modelu (`provider/model`)
  * `native`: `true` dla trybu natywnego dostawcy, `false` dla trybu awaryjnego
  * `attempts`: próby awaryjne, które zakończyły się niepowodzeniem przed sukcesem


Pola ścieżek:

  * pojedyncze wejście PDF: `details.pdf`
  * wiele wejść PDF: `details.pdfs[]` z wpisami `pdf`
  * metadane przepisywania ścieżki piaskownicy (gdy ma zastosowanie): `rewrittenFrom`


## Zachowanie błędów

  * Brak wejścia PDF: zgłasza `pdf required: provide a path or URL to a PDF document`
  * Zbyt wiele plików PDF: zwraca ustrukturyzowany błąd w `details.error = "too_many_pdfs"`
  * Nieobsługiwany schemat odwołania: zwraca `details.error = "unsupported_pdf_reference"`
  * Tryb natywny z `pages`: zgłasza czytelny błąd `pages is not supported with native PDF providers`


## Przykłady

Pojedynczy PDF:

jsonCopy code
[code]
    {  "pdf": "/tmp/report.pdf",  "prompt": "Summarize this report in 5 bullets"}
[/code]

Wiele plików PDF:

jsonCopy code
[code]
    {  "pdfs": ["/tmp/q1.pdf", "/tmp/q2.pdf"],  "prompt": "Compare risks and timeline changes across both documents"}
[/code]

Model awaryjny z filtrem stron:

jsonCopy code
[code]
    {  "pdf": "https://example.com/report.pdf",  "pages": "1-3,7",  "model": "openai/gpt-5.4-mini",  "prompt": "Extract only customer-impacting incidents"}
[/code]

## Powiązane

  * [Przegląd narzędzi](</pl/tools>) \- wszystkie dostępne narzędzia agenta
  * [Odwołanie do konfiguracji](</pl/gateway/config-agents#agent-defaults>) \- konfiguracja pdfMaxBytesMb i pdfMaxPages


Was this useful?YesNo