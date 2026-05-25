---
title: Nadpisania instalacji Plugin
source_url: https://docs.openclaw.ai/pl/plugins/install-overrides
scraped_at: 2026-05-25
---

Nadpisania instalacji Plugin pozwalają opiekunom testować instalacje Plugin wykonywane podczas konfiguracji względem określonego pakietu npm albo lokalnego archiwum tarball utworzonego przez npm-pack. Są przeznaczone wyłącznie do walidacji E2E i pakietów. Zwykli użytkownicy powinni instalować Plugin za pomocą [`openclaw plugins install`](</pl/cli/plugins>).

## Środowisko

Nadpisania są wyłączone, chyba że ustawione są obie zmienne:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

Mapa nadpisań to JSON z kluczami według identyfikatora Plugin. Wartości obsługują:

  * `npm:<registry-spec>` dla pakietów z rejestru oraz dokładnych wersji lub tagów
  * `npm-pack:<path.tgz>` dla lokalnych archiwów tarball utworzonych przez `npm pack`


Względne ścieżki `npm-pack:` są rozwiązywane względem bieżącego katalogu roboczego.

## Zachowanie

Gdy przepływ wykonywany podczas konfiguracji żąda instalacji Plugin, którego identyfikator występuje w mapie, OpenClaw używa źródła z nadpisania zamiast katalogu, pakietu wbudowanego lub domyślnego źródła npm. Dotyczy to onboardingu i innych przepływów, które używają współdzielonego instalatora Plugin działającego podczas konfiguracji.

Nadpisania nadal wymuszają oczekiwany identyfikator Plugin. Archiwum tarball przypisane do `codex` musi zainstalować Plugin, którego identyfikator w manifeście to `codex`.

Nadpisania nie dziedziczą oficjalnego statusu zaufanego źródła. Nawet gdy wpis katalogu zwykle reprezentuje pakiet należący do OpenClaw, nadpisanie jest traktowane jako dane testowe dostarczone przez operatora.

Pliki `.env` w obszarze roboczym nie mogą włączać nadpisań instalacji. Ustaw te zmienne w zaufanej powłoce, zadaniu CI albo zdalnym poleceniu testowym, które uruchamia OpenClaw.

## E2E pakietu

Użyj izolowanego katalogu stanu, aby instalacje pakietów i rekordy instalacji nie dotykały Twojego zwykłego stanu OpenClaw:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Zweryfikuj zainstalowany pakiet w katalogu stanu:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

Dla E2E z aktywnym dostawcą pobierz rzeczywisty klucz API z zaufanej powłoki albo sekretu CI przed uruchomieniem polecenia testowego. Nie wypisuj kluczy; raportuj tylko źródło i to, czy klucz był obecny.

Was this useful?YesNo