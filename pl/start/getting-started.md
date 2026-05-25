---
title: Pierwsze kroki
source_url: https://docs.openclaw.ai/pl/start/getting-started
scraped_at: 2026-05-25
---

Zainstaluj OpenClaw, uruchom onboarding i czatuj ze swoim asystentem AI — wszystko w około 5 minut. Na końcu będziesz mieć uruchomiony Gateway, skonfigurowane uwierzytelnianie i działającą sesję czatu.

## Czego potrzebujesz

  * **Node.js** — zalecany Node 24 (obsługiwany jest także Node 22.16+)
  * **Klucz API** od dostawcy modelu (Anthropic, OpenAI, Google itd.) — onboarding poprosi Cię o niego


## Szybka konfiguracja

* ### Zainstaluj OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Proces skryptu instalacyjnego](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Kreator przeprowadzi Cię przez wybór dostawcy modelu, ustawienie klucza API i konfigurację Gateway. Zajmuje to około 2 minut.

Pełną dokumentację znajdziesz w [Onboarding (CLI)](</pl/start/wizard>).

* ### Sprawdź, czy Gateway działa

bashCopy code
[code]
    openclaw gateway status
[/code]

Powinieneś zobaczyć, że Gateway nasłuchuje na porcie 18789.

* ### Otwórz panel

bashCopy code
[code]
    openclaw dashboard
[/code]

To otworzy Control UI w przeglądarce. Jeśli się ładuje, wszystko działa.

* ### Wyślij pierwszą wiadomość

Wpisz wiadomość w czacie Control UI, a powinieneś otrzymać odpowiedź AI.

Wolisz czatować z telefonu? Najszybszym kanałem do skonfigurowania jest [Telegram](</pl/channels/telegram>) (wystarczy token bota). Zobacz [Kanały](</pl/channels>), aby poznać wszystkie opcje.

Zaawansowane: zamontuj niestandardową kompilację Control UI

Jeśli utrzymujesz zlokalizowaną lub dostosowaną kompilację panelu, ustaw `gateway.controlUi.root` na katalog zawierający zbudowane statyczne zasoby i `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Następnie ustaw:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Uruchom ponownie Gateway i ponownie otwórz panel:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Co dalej

[**Połącz kanał** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo i inne. ](</pl/channels>) [**Parowanie i bezpieczeństwo** Kontroluj, kto może wysyłać wiadomości do Twojego agenta. ](</pl/channels/pairing>) [**Skonfiguruj Gateway** Modele, narzędzia, sandbox i ustawienia zaawansowane. ](</pl/gateway/configuration>) [**Przeglądaj narzędzia** Przeglądarka, exec, wyszukiwanie w sieci, Skills i Plugin. ](</pl/tools>)

Zaawansowane: zmienne środowiskowe

Jeśli uruchamiasz OpenClaw jako konto usługi albo chcesz użyć niestandardowych ścieżek:

  * `OPENCLAW_HOME` — katalog domowy do wewnętrznego rozwiązywania ścieżek
  * `OPENCLAW_STATE_DIR` — zastępuje katalog stanu
  * `OPENCLAW_CONFIG_PATH` — zastępuje ścieżkę pliku konfiguracyjnego


Pełna dokumentacja: [Zmienne środowiskowe](</pl/help/environment>).

## Powiązane

  * [Omówienie instalacji](</pl/install>)
  * [Omówienie kanałów](</pl/channels>)
  * [Konfiguracja](</pl/start/setup>)


Was this useful?YesNo