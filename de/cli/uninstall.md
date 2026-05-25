---
title: Deinstallation
source_url: https://docs.openclaw.ai/de/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Gateway-Dienst + lokale Daten deinstallieren (CLI bleibt erhalten).

Optionen:

  * `--service`: den Gateway-Dienst entfernen
  * `--state`: Status und Konfiguration entfernen
  * `--workspace`: Workspace-Verzeichnisse entfernen
  * `--app`: die macOS-App entfernen
  * `--all`: Dienst, Status, Workspace und App entfernen
  * `--yes`: Bestätigungsabfragen überspringen
  * `--non-interactive`: Abfragen deaktivieren; erfordert `--yes`
  * `--dry-run`: Aktionen ausgeben, ohne Dateien zu entfernen


Beispiele:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Hinweise:

  * Führen Sie zuerst `openclaw backup create` aus, wenn Sie vor dem Entfernen von Status oder Workspaces einen wiederherstellbaren Snapshot erstellen möchten.
  * `--all` ist eine Kurzform dafür, Dienst, Status, Workspace und App zusammen zu entfernen.
  * `--non-interactive` erfordert `--yes`.


## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Deinstallation](</de/install/uninstall>)


Was this useful?YesNo