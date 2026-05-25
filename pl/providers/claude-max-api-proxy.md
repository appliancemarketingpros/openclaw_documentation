---
title: Proxy API Claude Max
source_url: https://docs.openclaw.ai/pl/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** to narzędzie społeczności, które udostępnia Twoją subskrypcję Claude Max/Pro jako endpoint API kompatybilny z OpenAI. Pozwala to używać subskrypcji z dowolnym narzędziem obsługującym format API OpenAI.

## Dlaczego warto tego używać?

Podejście | Koszt | Najlepsze do  
---|---|---  
API Anthropic | Opłata za token (~$15/M wejścia, $75/M wyjścia dla Opus) | Aplikacje produkcyjne, duży wolumen  
Subskrypcja Claude Max | $200/miesiąc ryczałtowo | Użycie osobiste, rozwój, nieograniczone użycie  
  
Jeśli masz subskrypcję Claude Max i chcesz używać jej z narzędziami kompatybilnymi z OpenAI, ten proxy może obniżyć koszt niektórych przepływów pracy. Klucze API pozostają bardziej jednoznaczną ścieżką polityki dla zastosowań produkcyjnych.

## Jak to działa

CodeCopy code
[code]
    Twoja aplikacja → claude-max-api-proxy → Claude Code CLI → Anthropic (przez subskrypcję)   (format OpenAI)              (konwertuje format)         (używa Twojego logowania)
[/code]

Proxy:

  1. Przyjmuje żądania w formacie OpenAI pod `http://localhost:3456/v1/chat/completions`
  2. Konwertuje je na polecenia Claude Code CLI
  3. Zwraca odpowiedzi w formacie OpenAI (obsługiwany streaming)


## Pierwsze kroki

* ### Install the proxy

Wymaga Node.js 20+ oraz Claude Code CLI.

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Zweryfikuj, że Claude CLI jest uwierzytelnioneclaude --version
[/code]

* ### Start the server

bashCopy code
[code]
    claude-max-api# Serwer działa pod http://localhost:3456
[/code]

* ### Test the proxy

bashCopy code
[code]
    # Health checkcurl http://localhost:3456/health # Wyświetl modelecurl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### Configure OpenClaw

Skieruj OpenClaw na proxy jako niestandardowy endpoint kompatybilny z OpenAI:

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## Wbudowany katalog

ID modelu | Mapuje do  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## Zaawansowana konfiguracja

Uwagi dotyczące trasy proxy w stylu OpenAI-compatible

Ta ścieżka używa tej samej trasy proxy w stylu OpenAI-compatible co inne niestandardowe backendy `/v1`:

  * Natywne kształtowanie żądań tylko dla OpenAI nie ma zastosowania
  * Brak `service_tier`, brak `store` dla Responses, brak wskazówek prompt-cache i brak kształtowania ładunków zgodności z rozumowaniem OpenAI
  * Ukryte nagłówki atrybucji OpenClaw (`originator`, `version`, `User-Agent`) nie są wstrzykiwane na URL proxy

Auto-start na macOS przez LaunchAgent

Utwórz LaunchAgent, aby uruchamiać proxy automatycznie:

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## Linki

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## Uwagi

  * To **narzędzie społeczności** , nieobsługiwane oficjalnie przez Anthropic ani OpenClaw
  * Wymaga aktywnej subskrypcji Claude Max/Pro z uwierzytelnionym Claude Code CLI
  * Proxy działa lokalnie i nie wysyła danych do żadnych zewnętrznych serwerów
  * Odpowiedzi streamingowe są w pełni obsługiwane


## Powiązane

[**Anthropic provider** Natywna integracja OpenClaw z Claude CLI albo kluczami API. ](</pl/providers/anthropic>) [**OpenAI provider** Dla subskrypcji OpenAI/Codex. ](</pl/providers/openai>) [**Model selection** Przegląd wszystkich providerów, referencji modeli i zachowania failover. ](</pl/concepts/model-providers>) [**Configuration** Pełna dokumentacja konfiguracji. ](</pl/gateway/configuration>)

Was this useful?YesNo