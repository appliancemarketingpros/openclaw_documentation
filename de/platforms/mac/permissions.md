---
title: macOS-Berechtigungen
source_url: https://docs.openclaw.ai/de/platforms/mac/permissions
scraped_at: 2026-05-25
---

Berechtigungen unter macOS sind fragil. TCC verknüpft eine Berechtigungsfreigabe mit der Codesignatur der App, der Bundle-ID und dem Pfad auf dem Datenträger. Wenn sich einer dieser Punkte ändert, behandelt macOS die App als neu und kann Prompts verwerfen oder ausblenden.

## Anforderungen für stabile Berechtigungen

  * Gleicher Pfad: Führen Sie die App von einem festen Ort aus (für OpenClaw: `dist/OpenClaw.app`).
  * Gleiche Bundle-ID: Das Ändern der Bundle-ID erzeugt eine neue Berechtigungsidentität.
  * Signierte App: Nicht signierte oder ad-hoc signierte Builds behalten Berechtigungen nicht bei.
  * Konsistente Signatur: Verwenden Sie ein echtes Apple-Development- oder Developer-ID-Zertifikat, damit die Signatur über Rebuilds hinweg stabil bleibt.


Ad-hoc-Signaturen erzeugen bei jedem Build eine neue Identität. macOS vergisst dadurch frühere Freigaben, und Prompts können vollständig verschwinden, bis die veralteten Einträge bereinigt werden.

## Wiederherstellungs-Checkliste, wenn Prompts verschwinden

  1. Beenden Sie die App.
  2. Entfernen Sie den App-Eintrag in Systemeinstellungen -> Datenschutz & Sicherheit.
  3. Starten Sie die App vom selben Pfad erneut und erteilen Sie die Berechtigungen erneut.
  4. Wenn der Prompt weiterhin nicht erscheint, setzen Sie TCC-Einträge mit `tccutil` zurück und versuchen Sie es erneut.
  5. Manche Berechtigungen erscheinen erst nach einem vollständigen Neustart von macOS wieder.


Beispiel-Resets (Bundle-ID bei Bedarf ersetzen):

bashCopy code
[code]
    sudo tccutil reset Accessibility ai.openclaw.macsudo tccutil reset ScreenCapture ai.openclaw.macsudo tccutil reset AppleEvents
[/code]

## Berechtigungen für Dateien und Ordner (Desktop/Dokumente/Downloads)

macOS kann außerdem Desktop, Dokumente und Downloads für Terminal-/Hintergrundprozesse einschränken. Wenn Datei-Lesevorgänge oder Verzeichnisauflistungen hängen bleiben, erteilen Sie Zugriff für denselben Prozesskontext, der Dateioperationen ausführt (zum Beispiel Terminal/iTerm, von LaunchAgent gestartete App oder SSH-Prozess).

Workaround: Verschieben Sie Dateien in den OpenClaw-Workspace (`~/.openclaw/workspace`), wenn Sie Berechtigungen pro Ordner vermeiden möchten.

Wenn Sie Berechtigungen testen, signieren Sie immer mit einem echten Zertifikat. Ad-hoc- Builds sind nur für schnelle lokale Läufe akzeptabel, bei denen Berechtigungen keine Rolle spielen.

## Verwandt

  * [macOS-App](</de/platforms/macos>)
  * [macOS-Signierung](</de/platforms/mac/signing>)


Was this useful?YesNo