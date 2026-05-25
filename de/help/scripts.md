---
title: Skripte
source_url: https://docs.openclaw.ai/de/help/scripts
scraped_at: 2026-05-25
---

Das Verzeichnis `scripts/` enthält Hilfsskripte für lokale Workflows und Ops-Aufgaben. Verwenden Sie diese, wenn eine Aufgabe klar mit einem Skript verbunden ist; bevorzugen Sie andernfalls die CLI.

## Konventionen

  * Skripte sind **optional** , sofern sie nicht in Dokumentation oder Release-Checklisten referenziert werden.
  * Bevorzugen Sie CLI-Oberflächen, wenn sie vorhanden sind (Beispiel: Die Authentifizierungsüberwachung verwendet `openclaw models status --check`).
  * Gehen Sie davon aus, dass Skripte host-spezifisch sind; lesen Sie sie, bevor Sie sie auf einem neuen Rechner ausführen.


## Skripte zur Authentifizierungsüberwachung

Die Authentifizierungsüberwachung wird unter [Authentifizierung](</de/gateway/authentication>) behandelt. Die Skripte unter `scripts/` sind optionale Extras für systemd/Termux-Workflows auf Telefonen.

## GitHub-Lesehelfer

Verwenden Sie `scripts/gh-read`, wenn `gh` für repo-bezogene Leseaufrufe ein Installationstoken einer GitHub App verwenden soll, während das normale `gh` für Schreibaktionen bei Ihrer persönlichen Anmeldung bleibt.

Erforderliche Umgebungsvariablen:

  * `OPENCLAW_GH_READ_APP_ID`
  * `OPENCLAW_GH_READ_PRIVATE_KEY_FILE`


Optionale Umgebungsvariablen:

  * `OPENCLAW_GH_READ_INSTALLATION_ID`, wenn Sie die repo-basierte Suche nach der Installation überspringen möchten
  * `OPENCLAW_GH_READ_PERMISSIONS` als kommagetrennte Überschreibung für die Teilmenge der anzufordernden Leseberechtigungen


Reihenfolge der Repo-Auflösung:

  * `gh ... -R owner/repo`
  * `GH_REPO`
  * `git remote origin`


Beispiele:

  * `scripts/gh-read pr view 123`
  * `scripts/gh-read run list -R openclaw/openclaw`
  * `scripts/gh-read api repos/openclaw/openclaw/pulls/123`


## Beim Hinzufügen von Skripten

  * Halten Sie Skripte fokussiert und dokumentiert.
  * Fügen Sie einen kurzen Eintrag in der relevanten Dokumentation hinzu (oder erstellen Sie einen, falls er fehlt).


## Verwandte Themen

  * [Tests](</de/help/testing>)
  * [Live-Tests](</de/help/testing-live>)


Was this useful?YesNo