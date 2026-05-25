---
title: Cloudflare-KI-Gateway
source_url: https://docs.openclaw.ai/de/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway wird vor Provider-APIs geschaltet und ermöglicht Ihnen, Analysen, Caching und Steuerungen hinzuzufügen. Für Anthropic verwendet OpenClaw die Anthropic Messages API über Ihren Gateway-Endpunkt.

Eigenschaft | Wert  
---|---  
Provider | `cloudflare-ai-gateway`  
Basis-URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Standardmodell | `cloudflare-ai-gateway/claude-sonnet-4-6`  
API-Schlüssel | `CLOUDFLARE_AI_GATEWAY_API_KEY` (Ihr Provider-API-Schlüssel für Anfragen über das Gateway)  
  
Wenn Thinking für Anthropic-Messages-Modelle aktiviert ist, entfernt OpenClaw nachgestellte assistant-Prefill-Turns, bevor die Payload über Cloudflare AI Gateway gesendet wird. Anthropic lehnt Antwort-Prefilling mit erweitertem Thinking ab, während gewöhnliches Nicht-Thinking-Prefill weiterhin verfügbar bleibt.

## Erste Schritte

* ### Provider-API-Schlüssel und Gateway-Details festlegen

Führen Sie das Onboarding aus und wählen Sie die Authentifizierungsoption für Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Dabei werden Sie nach Ihrer Konto-ID, Gateway-ID und Ihrem API-Schlüssel gefragt.

* ### Ein Standardmodell festlegen

Fügen Sie das Modell zu Ihrer OpenClaw-Konfiguration hinzu:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Prüfen, ob das Modell verfügbar ist

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Nicht interaktives Beispiel

Für skriptgesteuerte oder CI-Setups übergeben Sie alle Werte auf der Befehlszeile:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Erweiterte Konfiguration

Authentifizierte Gateways

Wenn Sie die Gateway-Authentifizierung in Cloudflare aktiviert haben, fügen Sie den Header `cf-aig-authorization` hinzu. Dies gilt **zusätzlich zu** Ihrem Provider-API-Schlüssel.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Hinweis zur Umgebung

Wenn das Gateway als Daemon (launchd/systemd) ausgeführt wird, stellen Sie sicher, dass `CLOUDFLARE_AI_GATEWAY_API_KEY` für diesen Prozess verfügbar ist.

## Verwandte Themen

[**Modellauswahl** Auswahl von Providern, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**Problembehandlung** Allgemeine Problembehandlung und FAQ. ](</de/help/troubleshooting>)

Was this useful?YesNo