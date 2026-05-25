---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/de/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

The [Vercel AI Gateway](<https://vercel.com/ai-gateway>) stellt eine einheitliche API bereit, um über einen einzigen Endpoint auf Hunderte von Modellen zuzugreifen.

Eigenschaft | Wert  
---|---  
Provider | `vercel-ai-gateway`  
Authentifizierung | `AI_GATEWAY_API_KEY`  
API | mit Anthropic Messages kompatibel  
Modellkatalog | automatisch über `/v1/models` erkannt  
  
## Erste Schritte

* ### API-Schlüssel festlegen

Führen Sie das Onboarding aus und wählen Sie die Authentifizierungsoption für AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Standardmodell festlegen

Fügen Sie das Modell Ihrer OpenClaw-Konfiguration hinzu:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Prüfen, ob das Modell verfügbar ist

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Nicht interaktives Beispiel

Für Skript- oder CI-Setups übergeben Sie alle Werte über die Befehlszeile:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Kurzschreibweise für Modell-IDs

OpenClaw akzeptiert Vercel-Claude-Modell-Refs in Kurzschreibweise und normalisiert sie zur Laufzeit:

Eingabe in Kurzschreibweise | Normalisierte Modell-Ref  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Erweiterte Konfiguration

Umgebungsvariable für Daemon-Prozesse

Wenn der OpenClaw Gateway als Daemon (launchd/systemd) läuft, stellen Sie sicher, dass `AI_GATEWAY_API_KEY` für diesen Prozess verfügbar ist.

Provider-Routing

Vercel AI Gateway leitet Anfragen anhand des Modell-Ref-Präfixes an den Upstream-Provider weiter. Beispielsweise wird `vercel-ai-gateway/anthropic/claude-opus-4.6` über Anthropic geroutet, während `vercel-ai-gateway/openai/gpt-5.5` über OpenAI und `vercel-ai-gateway/moonshotai/kimi-k2.6` über MoonshotAI geroutet wird. Ihr einzelner `AI_GATEWAY_API_KEY` übernimmt die Authentifizierung für alle Upstream-Provider.

Thinking-Stufen

`/think`-Optionen folgen vertrauenswürdigen Upstream-Modellpräfixen, wenn OpenClaw den Upstream-Provider-Vertrag kennt. `vercel-ai-gateway/anthropic/...` verwendet das Claude-Thinking-Profil, einschließlich adaptiver Standardwerte für Claude-4.6-Modelle. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` und Codex-artige Refs stellen `/think xhigh` genau wie die direkten OpenAI/OpenAI-Codex-Provider bereit. Andere namespacete Refs behalten die normalen Reasoning-Stufen bei, sofern ihre Katalogmetadaten nicht mehr deklarieren.

## Verwandte Themen

[**Modellauswahl** Provider, Modell-Refs und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Fehlerbehebung** Allgemeine Fehlerbehebung und FAQ. ](</de/help/troubleshooting>)

Was this useful?YesNo