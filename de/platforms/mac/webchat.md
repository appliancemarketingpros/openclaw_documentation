---
title: Webchat (macOS)
source_url: https://docs.openclaw.ai/de/platforms/mac/webchat
scraped_at: 2026-05-25
---

Die macOS-Menüleisten-App bettet die WebChat-Benutzeroberfläche als native SwiftUI-Ansicht ein. Sie verbindet sich mit dem Gateway und verwendet standardmäßig die **Hauptsitzung** für den ausgewählten Agenten (mit einem Sitzungsumschalter für andere Sitzungen).

  * **Lokaler Modus** : verbindet sich direkt mit dem lokalen Gateway-WebSocket.
  * **Remote-Modus** : leitet den Gateway-Steuerport über SSH weiter und verwendet diesen Tunnel als Datenebene.


## Starten und Debugging

  * Manuell: Lobster-Menü → "Chat öffnen".

  * Für Tests automatisch öffnen:

bashCopy code
[code]dist/OpenClaw.app/Contents/MacOS/OpenClaw --webchat
[/code]

  * Logs: `./scripts/clawlog.sh` (Subsystem `ai.openclaw`, Kategorie `WebChatSwiftUI`).


## Wie es verdrahtet ist

  * Datenebene: Gateway-WS-Methoden `chat.history`, `chat.send`, `chat.abort`, `chat.inject` und Events `chat`, `agent`, `presence`, `tick`, `health`.
  * `chat.history` gibt für die Anzeige normalisierte Transkriptzeilen zurück: Inline-Direktiven-Tags werden aus sichtbarem Text entfernt, Tool-Call-XML-Nutzdaten im Klartext (einschließlich `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` sowie abgeschnittener Tool-Call-Blöcke) und durchgesickerte ASCII-/Full-width-Modellsteuerungstoken werden entfernt, reine Silent-Token-Assistant-Zeilen wie exakt `NO_REPLY` / `no_reply` werden ausgelassen, und zu große Zeilen können durch Platzhalter ersetzt werden.
  * Sitzung: standardmäßig die primäre Sitzung (`main` oder `global`, wenn der Scope global ist). Die Benutzeroberfläche kann zwischen Sitzungen wechseln.
  * Onboarding verwendet eine eigene Sitzung, um die Ersteinrichtung getrennt zu halten.


## Sicherheitsoberfläche

  * Der Remote-Modus leitet nur den Gateway-WebSocket-Steuerport über SSH weiter.


## Bekannte Einschränkungen

  * Die Benutzeroberfläche ist für Chat-Sitzungen optimiert (keine vollständige Browser-Sandbox).


## Verwandt

  * [WebChat](</de/web/webchat>)
  * [macOS-App](</de/platforms/macos>)


Was this useful?YesNo