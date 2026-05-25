---
title: Skills (macOS)
source_url: https://docs.openclaw.ai/de/platforms/mac/skills
scraped_at: 2026-05-25
---

Die macOS-App stellt OpenClaw Skills über das Gateway bereit; sie parst Skills nicht lokal.

## Datenquelle

  * `skills.status` (Gateway) gibt alle Skills plus Berechtigungsstatus und fehlende Anforderungen zurück (einschließlich Allowlist-Blockierungen für gebündelte Skills).
  * Anforderungen werden aus `metadata.openclaw.requires` in jeder `SKILL.md` abgeleitet.


## Installationsaktionen

  * `metadata.openclaw.install` definiert Installationsoptionen (brew/node/go/uv).
  * Die App ruft `skills.install` auf, um Installer auf dem Gateway-Host auszuführen.
  * Eingebaute Findings vom Typ `critical` für gefährlichen Code blockieren `skills.install` standardmäßig; verdächtige Findings erzeugen weiterhin nur Warnungen. Das gefährliche Override existiert auf der Gateway-Anfrage, aber der Standardablauf der App bleibt fail-closed.
  * Wenn jede Installationsoption `download` ist, stellt das Gateway alle Download- Optionen bereit.
  * Andernfalls wählt das Gateway einen bevorzugten Installer anhand der aktuellen Installationspräferenzen und Host-Binärdateien aus: Homebrew zuerst, wenn `skills.install.preferBrew` aktiviert ist und `brew` existiert, dann `uv`, dann der konfigurierte Node-Manager aus `skills.install.nodeManager`, danach weitere Fallbacks wie `go` oder `download`.
  * Labels für Node-Installationen spiegeln den konfigurierten Node-Manager wider, einschließlich `yarn`.


## Env/API-Schlüssel

  * Die App speichert Schlüssel in `~/.openclaw/openclaw.json` unter `skills.entries.<skillKey>`.
  * `skills.update` patcht `enabled`, `apiKey` und `env`.


## Remote-Modus

  * Installations- und Konfigurationsupdates erfolgen auf dem Gateway-Host (nicht auf dem lokalen Mac).


## Verwandt

  * [Skills](</de/tools/skills>)
  * [macOS-App](</de/platforms/macos>)


Was this useful?YesNo