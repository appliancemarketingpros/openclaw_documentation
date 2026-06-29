---
title: Konventionen für Geheimnis-Platzhalter
source_url: https://docs.openclaw.ai/de/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Konventionen für Secret-Platzhalter

Verwenden Sie Platzhalter, die für Menschen lesbar sind, aber echten Secrets nicht ähneln.

## Empfohlener Stil

  * Bevorzugen Sie beschreibende Werte wie `example-openai-key-not-real` oder `example-discord-bot-token`.
  * Für Shell-Beispiele bevorzugen Sie `${OPENAI_API_KEY}` gegenüber inline tokenähnlichen Zeichenfolgen.
  * Halten Sie Beispiele offensichtlich unecht und auf den Zweck begrenzt (Provider, Kanal, Auth-Typ).


## Vermeiden Sie diese Muster in der Dokumentation

  * Wörtliche PEM-Header- oder Footer-Texte privater Schlüssel.
  * Präfixe, die Live-Zugangsdaten ähneln, zum Beispiel `sk-...`, `xoxb-...`, `AKIA...`.
  * Realistisch aussehende Bearer-Token, die aus Laufzeitprotokollen kopiert wurden.


## Beispiel

bashCopy code
[code]
    # Gutexport OPENAI_API_KEY="example-openai-key-not-real" # Besser (wenn es in der Dokumentation um Env-Verdrahtung geht)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue