---
title: Przeglądarka
source_url: https://docs.openclaw.ai/pl/cli/browser
scraped_at: 2026-05-25
---

# `openclaw browser`

Zarządzaj powierzchnią sterowania przeglądarką OpenClaw i uruchamiaj akcje przeglądarki (cykl życia, profile, karty, migawki, zrzuty ekranu, nawigacja, dane wejściowe, emulacja stanu i debugowanie).

Powiązane:

  * Narzędzie przeglądarki + API: [Narzędzie przeglądarki](</pl/tools/browser>)


## Typowe flagi

  * `--url <gatewayWsUrl>`: adres URL WebSocket Gateway (domyślnie z konfiguracji).
  * `--token <token>`: token Gateway (jeśli wymagany).
  * `--timeout <ms>`: limit czasu żądania (ms).
  * `--expect-final`: czekaj na końcową odpowiedź Gateway.
  * `--browser-profile <name>`: wybierz profil przeglądarki (domyślnie z konfiguracji).
  * `--json`: dane wyjściowe czytelne maszynowo (tam, gdzie obsługiwane).


## Szybki start (lokalnie)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

Agenci mogą uruchomić tę samą kontrolę gotowości za pomocą `browser({ action: "doctor" })`.

## Szybkie rozwiązywanie problemów

Jeśli `start` kończy się błędem `not reachable after start`, najpierw sprawdź gotowość CDP. Jeśli `start` i `tabs` działają, ale `open` lub `navigate` kończy się niepowodzeniem, płaszczyzna sterowania przeglądarką jest sprawna, a przyczyną niepowodzenia jest zwykle polityka SSRF nawigacji.

Minimalna sekwencja:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

Szczegółowe wskazówki: [Rozwiązywanie problemów z przeglądarką](</pl/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## Cykl życia

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

Uwagi:

  * `doctor --deep` dodaje test migawki na żywo. Jest przydatny, gdy podstawowa gotowość CDP jest prawidłowa, ale potrzebujesz dowodu, że bieżącą kartę można zbadać.
  * W przypadku profili `attachOnly` i zdalnych profili CDP `openclaw browser stop` zamyka aktywną sesję sterowania i czyści tymczasowe nadpisania emulacji nawet wtedy, gdy OpenClaw nie uruchomił samodzielnie procesu przeglądarki.
  * W przypadku lokalnych zarządzanych profili `openclaw browser stop` zatrzymuje uruchomiony proces przeglądarki.
  * `openclaw browser start --headless` dotyczy tylko tego żądania uruchomienia i tylko wtedy, gdy OpenClaw uruchamia lokalną zarządzaną przeglądarkę. Nie przepisuje `browser.headless` ani konfiguracji profilu i nie ma efektu dla już działającej przeglądarki.
  * Na hostach Linux bez `DISPLAY` lub `WAYLAND_DISPLAY` lokalne zarządzane profile działają automatycznie w trybie headless, chyba że `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless=false` lub `browser.profiles.<name>.headless=false` jawnie żąda widocznej przeglądarki.


## Jeśli brakuje polecenia

Jeśli `openclaw browser` jest nieznanym poleceniem, sprawdź `plugins.allow` w `~/.openclaw/openclaw.json`.

Gdy `plugins.allow` jest obecne, jawnie wymień dołączony Plugin przeglądarki, chyba że konfiguracja ma już główny blok `browser`:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

Jawny główny blok `browser`, na przykład `browser.enabled=true` lub `browser.profiles.<name>`, również aktywuje dołączony Plugin przeglądarki przy restrykcyjnej liście dozwolonych Plugin.

Powiązane: [Narzędzie przeglądarki](</pl/tools/browser#missing-browser-command-or-tool>)

## Profile

Profile to nazwane konfiguracje routingu przeglądarki. W praktyce:

  * `openclaw`: uruchamia dedykowaną instancję Chrome zarządzaną przez OpenClaw lub dołącza do niej (izolowany katalog danych użytkownika).
  * `user`: steruje istniejącą zalogowaną sesją Chrome przez Chrome DevTools MCP.
  * niestandardowe profile CDP: wskazują lokalny lub zdalny punkt końcowy CDP.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

Użyj konkretnego profilu:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## Karty

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

`tabs` zwraca najpierw `suggestedTargetId`, a następnie stabilny `tabId`, taki jak `t1`, opcjonalną etykietę i surowy `targetId`. Agenci powinni przekazywać `suggestedTargetId` z powrotem do `focus`, `close`, migawek i akcji. Możesz przypisać etykietę za pomocą `open --label`, `tab new --label` lub `tab label`; etykiety, identyfikatory kart, surowe identyfikatory celów i unikatowe prefiksy identyfikatorów celów są akceptowane. Gdy Chromium zastępuje bazowy surowy cel podczas nawigacji lub przesłania formularza, OpenClaw zachowuje stabilny `tabId`/etykietę przy zastępczej karcie, gdy może potwierdzić dopasowanie. Surowe identyfikatory celów pozostają zmienne; preferuj `suggestedTargetId`.

## Migawka / zrzut ekranu / akcje

Migawka:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

Zrzut ekranu:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

Uwagi:

  * `--full-page` służy tylko do przechwytywania stron; nie można go łączyć z `--ref` ani `--element`.
  * Profile `existing-session` / `user` obsługują zrzuty ekranu strony i zrzuty ekranu `--ref` z danych wyjściowych migawki, ale nie obsługują zrzutów ekranu CSS `--element`.
  * `--labels` nakłada na zrzut ekranu bieżące odwołania migawki.
  * `snapshot --urls` dołącza wykryte miejsca docelowe linków do migawek AI, aby agenci mogli wybierać bezpośrednie cele nawigacji zamiast zgadywać wyłącznie na podstawie tekstu linku.


Nawigacja/kliknięcie/wpisywanie (automatyzacja UI oparta na odwołaniach):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
[/code]

Odpowiedzi akcji zwracają bieżący surowy `targetId` po wywołanej akcją wymianie strony, gdy OpenClaw może potwierdzić kartę zastępczą. Skrypty nadal powinny przechowywać i przekazywać `suggestedTargetId`/etykiety w długotrwałych przepływach pracy.

Pomocniki plików i okien dialogowych:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --accept
[/code]

Zarządzane profile Chrome zapisują zwykłe pobrania wywołane kliknięciem w katalogu pobrań OpenClaw (`/tmp/openclaw/downloads` domyślnie lub w skonfigurowanym tymczasowym katalogu głównym). Użyj `waitfordownload` lub `download`, gdy agent musi poczekać na konkretny plik i zwrócić jego ścieżkę; te jawne mechanizmy oczekiwania przejmują następne pobranie.

## Stan i pamięć

Widok + emulacja:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

Ciasteczka + pamięć:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## Debugowanie

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Istniejąca sesja Chrome przez MCP

Użyj wbudowanego profilu `user` lub utwórz własny profil `existing-session`:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser --browser-profile chrome-live tabs
[/code]

Ta ścieżka jest dostępna tylko na hoście. W przypadku Docker, serwerów headless, Browserless lub innych konfiguracji zdalnych użyj zamiast tego profilu CDP.

Obecne ograniczenia `existing-session`:

  * akcje sterowane migawkami używają odwołań, a nie selektorów CSS
  * `browser.actionTimeoutMs` ustawia domyślnie obsługiwane żądania `act` na 60000 ms, gdy wywołujący pomijają `timeoutMs`; `timeoutMs` dla pojedynczego wywołania nadal ma pierwszeństwo.
  * `click` to tylko kliknięcie lewym przyciskiem
  * `type` nie obsługuje `slowly=true`
  * `press` nie obsługuje `delayMs`
  * `hover`, `scrollintoview`, `drag`, `select`, `fill` i `evaluate` odrzucają nadpisania limitu czasu dla pojedynczych wywołań
  * `select` obsługuje tylko jedną wartość
  * `wait --load networkidle` nie jest obsługiwane
  * przesyłanie plików wymaga `--ref` / `--input-ref`, nie obsługuje CSS `--element` i obecnie obsługuje jeden plik naraz
  * haki okien dialogowych nie obsługują `--timeout`
  * zrzuty ekranu obsługują przechwytywanie stron i `--ref`, ale nie CSS `--element`
  * `responsebody`, przechwytywanie pobrań, eksport PDF i akcje wsadowe nadal wymagają zarządzanej przeglądarki lub surowego profilu CDP


## Zdalne sterowanie przeglądarką (proxy hosta węzła)

Jeśli Gateway działa na innej maszynie niż przeglądarka, uruchom **host węzła** na maszynie, która ma Chrome/Brave/Edge/Chromium. Gateway będzie pośredniczyć w akcjach przeglądarki do tego węzła (oddzielny serwer sterowania przeglądarką nie jest wymagany).

Użyj `gateway.nodes.browser.mode`, aby kontrolować automatyczny routing, oraz `gateway.nodes.browser.node`, aby przypiąć konkretny węzeł, jeśli połączonych jest kilka.

Bezpieczeństwo + konfiguracja zdalna: [Narzędzie przeglądarki](</pl/tools/browser>), [Dostęp zdalny](</pl/gateway/remote>), [Tailscale](</pl/gateway/tailscale>), [Bezpieczeństwo](</pl/gateway/security>)

## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Przeglądarka](</pl/tools/browser>)


Was this useful?YesNo