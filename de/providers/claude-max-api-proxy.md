---
title: Claude Max API proxy
source_url: https://docs.openclaw.ai/de/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** ist ein Community-Tool, das Ihr Claude-Max-/Pro-Abo als OpenAI-kompatiblen API-Endpunkt bereitstellt. Dadurch können Sie Ihr Abo mit jedem Tool verwenden, das das OpenAI-API-Format unterstützt.

## Warum das verwenden?

Ansatz | Kosten | Am besten geeignet für  
---|---|---  
Anthropic API | Zahlung pro Token (~$15/M Input, $75/M Output für Opus) | Produktions-Apps, hohes Volumen  
Claude-Max-Abo | $200/Monat pauschal | Persönliche Nutzung, Entwicklung, unbegrenzte Nutzung  
  
Wenn Sie ein Claude-Max-Abo haben und es mit OpenAI-kompatiblen Tools nutzen möchten, kann dieser Proxy für einige Workflows die Kosten senken. API keys bleiben der klarere Richtlinienpfad für den produktiven Einsatz.

## So funktioniert es

textCopy code
[code]
    Ihre App → claude-max-api-proxy → Claude Code CLI → Anthropic (über Abo)   (OpenAI-Format)             (Format wird konvertiert)   (verwendet Ihren Login)
[/code]

Der Proxy:

  1. akzeptiert Requests im OpenAI-Format unter `http://localhost:3456/v1/chat/completions`
  2. konvertiert sie in Befehle für Claude Code CLI
  3. gibt Antworten im OpenAI-Format zurück (Streaming wird unterstützt)


## Erste Schritte

* ### Den Proxy installieren

Erfordert Node.js 20+ und Claude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Prüfen, ob Claude CLI authentifiziert istclaude --version
[/code]

* ### Den Server starten

bashCopy code
[code]
    claude-max-api# Der Server läuft unter http://localhost:3456
[/code]

* ### Den Proxy testen

bashCopy code
[code]
    # Health-Checkcurl http://localhost:3456/health # Modelle auflistencurl http://localhost:3456/v1/models # Chat-Completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### OpenClaw konfigurieren

OpenClaw auf den Proxy als benutzerdefinierten OpenAI-kompatiblen Endpunkt zeigen lassen:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Eingebauter Katalog

Modell-ID | Entspricht  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Erweiterte Konfiguration

Hinweise zum proxyartigen OpenAI-kompatiblen Pfad

Dieser Pfad verwendet dieselbe proxyartige OpenAI-kompatible Route wie andere benutzerdefinierte `/v1`-Backends:

  * Native, nur für OpenAI gedachte Request-Formung wird nicht angewendet
  * Kein `service_tier`, kein Responses-`store`, keine Prompt-Cache-Hinweise und keine OpenAI-Reasoning-kompatible Payload-Formung
  * Versteckte OpenClaw-Zuordnungs-Header (`originator`, `version`, `User-Agent`) werden auf der Proxy-URL nicht injiziert

Automatischer Start unter macOS mit LaunchAgent

Erstellen Sie einen LaunchAgent, um den Proxy automatisch auszuführen:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Links

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## Hinweise

  * Dies ist ein **Community-Tool** , das weder offiziell von Anthropic noch von OpenClaw unterstützt wird
  * Erfordert ein aktives Claude-Max-/Pro-Abo mit authentifizierter Claude Code CLI
  * Der Proxy läuft lokal und sendet keine Daten an Drittserver
  * Streaming-Antworten werden vollständig unterstützt


## Verwandt

[**Anthropic provider** Native OpenClaw-Integration mit Claude CLI oder API keys. ](</de/providers/anthropic>) [**OpenAI provider** Für OpenAI-/Codex-Abos. ](</de/providers/openai>) [**Model selection** Überblick über alle Provider, Modell-Referenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**Configuration** Vollständige Konfigurationsreferenz. ](</de/gateway/configuration>)

Was this useful?YesNo