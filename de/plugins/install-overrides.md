---
title: Überschreibungen für Plugin-Installationen
source_url: https://docs.openclaw.ai/de/plugins/install-overrides
scraped_at: 2026-05-25
---

Plugin-Installations-Overrides ermöglichen Maintainern, Plugin-Installationen zur Einrichtungszeit mit einem bestimmten npm-Paket oder einem lokalen `npm-pack`-Tarball zu testen. Sie sind nur für E2E- und Paketvalidierung gedacht. Normale Benutzer sollten Plugins mit [`openclaw plugins install`](</de/cli/plugins>) installieren.

## Umgebung

Overrides sind deaktiviert, sofern nicht beide Variablen gesetzt sind:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

Die Override-Map ist JSON, indiziert nach Plugin-ID. Werte unterstützen:

  * `npm:<registry-spec>` für Registry-Pakete und exakte Versionen oder Tags
  * `npm-pack:<path.tgz>` für lokale Tarballs, die von `npm pack` erzeugt wurden


Relative `npm-pack:`-Pfade werden vom aktuellen Arbeitsverzeichnis aus aufgelöst.

## Verhalten

Wenn ein Flow zur Einrichtungszeit die Installation eines Plugins anfordert, dessen ID in der Map enthalten ist, verwendet OpenClaw die Override-Quelle anstelle der Katalog-, gebündelten oder standardmäßigen npm-Quelle. Dies gilt für das Onboarding und andere Flows, die den gemeinsamen Plugin-Installer zur Einrichtungszeit verwenden.

Overrides erzwingen weiterhin die erwartete Plugin-ID. Ein Tarball, der `codex` zugeordnet ist, muss ein Plugin installieren, dessen Manifest-ID `codex` ist.

Overrides erben keinen offiziellen Status als vertrauenswürdige Quelle. Selbst wenn der Katalogeintrag normalerweise ein OpenClaw-eigenes Paket darstellt, wird ein Override als vom Operator bereitgestellte Testeingabe behandelt.

Workspace-`.env`-Dateien können Installations-Overrides nicht aktivieren. Setzen Sie diese Variablen in der vertrauenswürdigen Shell, dem CI-Job oder dem Remote-Testbefehl, der OpenClaw startet.

## Paket-E2E

Verwenden Sie ein isoliertes Zustandsverzeichnis, damit Paketinstallationen und Installationsdatensätze Ihren normalen OpenClaw-Zustand nicht berühren:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Überprüfen Sie das installierte Paket im Zustandsverzeichnis:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

Für Live-Provider-E2E laden Sie den echten API-Schlüssel aus einer vertrauenswürdigen Shell oder einem CI-Secret, bevor Sie den Testbefehl starten. Geben Sie keine Schlüssel aus; melden Sie nur die Quelle und ob der Schlüssel vorhanden war.

Was this useful?YesNo