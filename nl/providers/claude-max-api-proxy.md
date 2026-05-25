---
title: Claude Max API-proxy
source_url: https://docs.openclaw.ai/nl/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** is een communitytool die je Claude Max/Pro-abonnement beschikbaar maakt als een OpenAI-compatibel API-eindpunt. Hierdoor kun je je abonnement gebruiken met elke tool die de OpenAI API-indeling ondersteunt.

## Waarom dit gebruiken?

Benadering | Kosten | Beste voor  
---|---|---  
Anthropic API | Betalen per token (~$15/M invoer, $75/M uitvoer voor Opus) | Productie-apps, hoog volume  
Claude Max-abonnement | $200/maand vast tarief | Persoonlijk gebruik, ontwikkeling, onbeperkt gebruik  
  
Als je een Claude Max-abonnement hebt en dit met OpenAI-compatibele tools wilt gebruiken, kan deze proxy de kosten voor sommige workflows verlagen. API-sleutels blijven het duidelijkere beleidspad voor productiegebruik.

## Hoe het werkt

CodeCopy code
[code]
    Your App → claude-max-api-proxy → Claude Code CLI → Anthropic (via subscription)     (OpenAI format)              (converts format)      (uses your login)
[/code]

De proxy:

  1. Accepteert aanvragen in OpenAI-indeling op `http://localhost:3456/v1/chat/completions`
  2. Zet ze om naar Claude Code CLI-opdrachten
  3. Geeft reacties terug in OpenAI-indeling (streaming ondersteund)


## Aan de slag

* ### Installeer de proxy

Vereist Node.js 20+ en Claude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Verify Claude CLI is authenticatedclaude --version
[/code]

* ### Start de server

bashCopy code
[code]
    claude-max-api# Server runs at http://localhost:3456
[/code]

* ### Test de proxy

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # List modelscurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### Configureer OpenClaw

Wijs OpenClaw naar de proxy als aangepast OpenAI-compatibel eindpunt:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Ingebouwde catalogus

Model-ID | Koppelt aan  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Geavanceerde configuratie

Opmerkingen voor proxy-achtige OpenAI-compatibiliteit

Dit pad gebruikt dezelfde proxy-achtige OpenAI-compatibele route als andere aangepaste `/v1`-backends:

  * Native aanvraagvorming die alleen voor OpenAI geldt, is niet van toepassing
  * Geen `service_tier`, geen Responses `store`, geen prompt-cache-hints en geen payloadvorming voor OpenAI-redeneercompatibiliteit
  * Verborgen OpenClaw-attributieheaders (`originator`, `version`, `User-Agent`) worden niet geïnjecteerd op de proxy-URL

Automatisch starten op macOS met LaunchAgent

Maak een LaunchAgent om de proxy automatisch uit te voeren:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Links

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## Opmerkingen

  * Dit is een **communitytool** , niet officieel ondersteund door Anthropic of OpenClaw
  * Vereist een actief Claude Max/Pro-abonnement met geauthenticeerde Claude Code CLI
  * De proxy draait lokaal en verzendt geen gegevens naar servers van derden
  * Streamingreacties worden volledig ondersteund


## Gerelateerd

[**Anthropic-provider** Native OpenClaw-integratie met Claude CLI of API-sleutels. ](</nl/providers/anthropic>) [**OpenAI-provider** Voor OpenAI/Codex-abonnementen. ](</nl/providers/openai>) [**Modelselectie** Overzicht van alle providers, modelverwijzingen en failovergedrag. ](</nl/concepts/model-providers>) [**Configuratie** Volledige configuratiereferentie. ](</nl/gateway/configuration>)

Was this useful?YesNo