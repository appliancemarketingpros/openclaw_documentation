---
title: Plugins verwalten
source_url: https://docs.openclaw.ai/de/plugins/manage-plugins
scraped_at: 2026-05-25
---

Die meisten Plugin-Workflows bestehen aus wenigen Befehlen: suchen, installieren, den Gateway neu starten, prüfen und deinstallieren, wenn Sie das Plugin nicht mehr benötigen.

## Plugins auflisten

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Verwenden Sie `--json` für Skripte. Es enthält Registry-Diagnosen und den statischen `dependencyStatus` jedes Plugins, wenn das Plugin-Paket `dependencies` oder `optionalDependencies` deklariert.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` ist eine kalte Bestandsprüfung. Sie zeigt, was OpenClaw aus Konfiguration, Manifesten und der Plugin-Registry erkennen kann; sie belegt nicht, dass ein bereits laufender Gateway-Prozess die Plugin-Laufzeit importiert hat.

## Plugins installieren

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Starten Sie nach der Installation von Plugin-Code den Gateway neu, der Ihre Kanäle bereitstellt:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Verwenden Sie `inspect --runtime`, wenn Sie einen Nachweis benötigen, dass das Plugin Laufzeitoberflächen wie Tools, Hooks, Dienste, Gateway-Methoden oder Plugin-eigene CLI-Befehle registriert hat.

## Plugins aktualisieren

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Wenn ein Plugin über einen npm-Dist-Tag wie `@beta` installiert wurde, verwenden spätere Aufrufe von `update <plugin-id>` diesen aufgezeichneten Tag erneut. Die Übergabe einer expliziten npm-Spezifikation stellt die nachverfolgte Installation für künftige Aktualisierungen auf diese Spezifikation um.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

Der zweite Befehl verschiebt ein Plugin zurück auf die standardmäßige Release-Linie der Registry, wenn es zuvor auf eine exakte Version oder einen Tag festgelegt war.

Wenn `openclaw update` im Beta-Kanal ausgeführt wird, versuchen npm- und ClawHub- Plugin-Einträge auf der Standardlinie zuerst das passende Plugin-Release `@beta`. Wenn dieses Beta- Release nicht existiert, fällt OpenClaw auf die aufgezeichnete Standard-/Latest-Spezifikation zurück. Bei npm-Plugins fällt OpenClaw auch zurück, wenn das Beta-Paket existiert, aber die Installationsvalidierung nicht besteht. Exakte Versionen und explizite Tags wie `@rc` oder `@beta` bleiben erhalten.

## Plugins deinstallieren

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

Die Deinstallation entfernt den Konfigurationseintrag des Plugins, den Plugin-Indexeintrag, Allow-/Deny-List- Einträge und verknüpfte Ladepfade, sofern zutreffend. Verwaltete Installationsverzeichnisse werden entfernt, es sei denn, Sie übergeben `--keep-files`.

Im Nix-Modus (`OPENCLAW_NIX_MODE=1`) sind die Befehle zum Installieren, Aktualisieren, Deinstallieren, Aktivieren und Deaktivieren von Plugins deaktiviert. Verwalten Sie diese Auswahl stattdessen in der Nix-Quelle der Installation; verwenden Sie für nix-openclaw den agent-first [Quick Start](<https://github.com/openclaw/nix-openclaw#quick-start>).

## Plugins veröffentlichen

Sie können externe Plugins auf [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>) oder beiden veröffentlichen.

### Auf ClawHub veröffentlichen

ClawHub ist die primäre öffentliche Discovery-Oberfläche für OpenClaw-Plugins. Sie bietet Benutzern vor der Installation durchsuchbare Metadaten, Versionsverlauf und Registry-Scanergebnisse.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Benutzer installieren von ClawHub mit:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

Die Kurzform prüft weiterhin zuerst ClawHub.

### Auf [npmjs.com](<http://npmjs.com>) veröffentlichen

Native npm-Plugins müssen ein Plugin-Manifest und OpenClaw- Entrypoint-Metadaten in `package.json` enthalten.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Benutzer installieren reine npm-Plugins mit:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Wenn dasselbe Paket auch auf ClawHub verfügbar ist, überspringt `npm:` die ClawHub-Suche und erzwingt die npm-Auflösung.

## Quellenauswahl

  * **ClawHub** : Verwenden Sie dies, wenn Sie OpenClaw-native Discovery, Scan-Zusammenfassungen, Versionen und Installationshinweise möchten.
  * **[npmjs.com](<http://npmjs.com>)** : Verwenden Sie dies, wenn Sie bereits JavaScript-Pakete ausliefern oder npm- Dist-Tags/private Registry-Workflows benötigen.
  * **Git** : Verwenden Sie dies, wenn Sie direkt aus einem Branch, Tag oder Commit installieren möchten.
  * **Lokaler Pfad** : Verwenden Sie dies, wenn Sie ein Plugin auf demselben Rechner entwickeln oder testen.


## Verwandt

  * [Plugins](</de/tools/plugin>) \- Übersicht und Fehlerbehebung
  * [`openclaw plugins`](</de/cli/plugins>) \- vollständige CLI-Referenz
  * [ClawHub](</de/clawhub/cli>) \- Veröffentlichungs- und Registry-Operationen
  * [Plugins erstellen](</de/plugins/building-plugins>) \- ein Plugin-Paket erstellen
  * [Plugin-Manifest](</de/plugins/manifest>) \- Manifest- und Paketmetadaten


Was this useful?YesNo