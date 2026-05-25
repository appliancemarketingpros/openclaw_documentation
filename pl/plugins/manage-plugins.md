---
title: Zarządzanie pluginami
source_url: https://docs.openclaw.ai/pl/plugins/manage-plugins
scraped_at: 2026-05-25
---

Większość przepływów pracy z Plugin to kilka poleceń: wyszukanie, instalacja, ponowne uruchomienie Gateway, weryfikacja i odinstalowanie, gdy Plugin nie jest już potrzebny.

## Lista Plugin

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Użyj `--json` w skryptach. Zawiera diagnostykę rejestru oraz statyczny `dependencyStatus` każdego Plugin, gdy pakiet Plugin deklaruje `dependencies` lub `optionalDependencies`.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` to zimne sprawdzenie inwentarza. Pokazuje, co OpenClaw może wykryć z konfiguracji, manifestów i rejestru Plugin; nie dowodzi, że już działający proces Gateway zaimportował środowisko uruchomieniowe Plugin.

## Instalowanie Plugin

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Po zainstalowaniu kodu Plugin uruchom ponownie Gateway obsługujący Twoje kanały:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Użyj `inspect --runtime`, gdy potrzebujesz dowodu, że Plugin zarejestrował powierzchnie środowiska uruchomieniowego, takie jak narzędzia, hooki, usługi, metody Gateway lub polecenia CLI należące do Plugin.

## Aktualizowanie Plugin

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Jeśli Plugin został zainstalowany z npm dist-tag, takiego jak `@beta`, późniejsze wywołania `update <plugin-id>` ponownie używają zapisanego tagu. Przekazanie jawnej specyfikacji npm przełącza śledzoną instalację na tę specyfikację dla przyszłych aktualizacji.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

Drugie polecenie przenosi Plugin z powrotem do domyślnej linii wydań rejestru, gdy wcześniej był przypięty do dokładnej wersji lub tagu.

Gdy `openclaw update` działa w kanale beta, rekordy Plugin npm i ClawHub z domyślnej linii najpierw próbują dopasowanego wydania Plugin `@beta`. Jeśli takie wydanie beta nie istnieje, OpenClaw wraca do zapisanej domyślnej/najnowszej specyfikacji. W przypadku Plugin npm OpenClaw wraca też wtedy, gdy pakiet beta istnieje, ale nie przechodzi walidacji instalacji. Dokładne wersje i jawne tagi, takie jak `@rc` lub `@beta`, są zachowywane.

## Odinstalowywanie Plugin

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

Odinstalowanie usuwa wpis konfiguracji Plugin, rekord indeksu Plugin, wpisy listy dozwolonych/zabronionych oraz połączone ścieżki ładowania, gdy ma to zastosowanie. Zarządzane katalogi instalacyjne są usuwane, chyba że przekażesz `--keep-files`.

W trybie Nix (`OPENCLAW_NIX_MODE=1`) polecenia instalacji, aktualizacji, odinstalowania, włączania i wyłączania Plugin są wyłączone. Zarządzaj tymi wyborami w źródle Nix dla instalacji; w przypadku nix-openclaw użyj najpierw agenta [Quick Start](<https://github.com/openclaw/nix-openclaw#quick-start>).

## Publikowanie Plugin

Możesz publikować zewnętrzne Plugin w [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>) lub w obu miejscach.

### Publikowanie w ClawHub

ClawHub to podstawowa publiczna powierzchnia odkrywania Plugin OpenClaw. Daje użytkownikom przeszukiwalne metadane, historię wersji i wyniki skanowania rejestru przed instalacją.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Użytkownicy instalują z ClawHub za pomocą:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

Forma bez prefiksu nadal najpierw sprawdza ClawHub.

### Publikowanie w [npmjs.com](<http://npmjs.com>)

Natywne Plugin npm muszą zawierać manifest Plugin oraz metadane punktu wejścia OpenClaw w `package.json`.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Użytkownicy instalują wyłącznie z npm za pomocą:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Jeśli ten sam pakiet jest również dostępny w ClawHub, `npm:` pomija wyszukiwanie w ClawHub i wymusza rozwiązywanie przez npm.

## Wybór źródła

  * **ClawHub** : użyj, gdy chcesz natywnego dla OpenClaw odkrywania, podsumowań skanowania, wersji i wskazówek instalacyjnych.
  * **[npmjs.com](<http://npmjs.com>)** : użyj, gdy już publikujesz pakiety JavaScript lub potrzebujesz przepływów pracy npm dist-tags/prywatnego rejestru.
  * **Git** : użyj, gdy chcesz instalować bezpośrednio z gałęzi, tagu lub commita.
  * **Ścieżka lokalna** : użyj, gdy rozwijasz lub testujesz Plugin na tej samej maszynie.


## Powiązane

  * [Plugin](</pl/tools/plugin>) \- omówienie i rozwiązywanie problemów
  * [`openclaw plugins`](</pl/cli/plugins>) \- pełna dokumentacja CLI
  * [ClawHub](</pl/clawhub/cli>) \- publikowanie i operacje rejestru
  * [Tworzenie Plugin](</pl/plugins/building-plugins>) \- tworzenie pakietu Plugin
  * [Manifest Plugin](</pl/plugins/manifest>) \- manifest i metadane pakietu


Was this useful?YesNo