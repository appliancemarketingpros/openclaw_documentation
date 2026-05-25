---
title: Gateway AI Cloudflare
source_url: https://docs.openclaw.ai/pl/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway znajduje się przed interfejsami API dostawców i pozwala dodać analitykę, buforowanie oraz mechanizmy kontroli. W przypadku Anthropic OpenClaw używa Anthropic Messages API przez punkt końcowy Gateway.

Właściwość | Wartość  
---|---  
Dostawca | `cloudflare-ai-gateway`  
Bazowy URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Model domyślny | `cloudflare-ai-gateway/claude-sonnet-4-6`  
Klucz API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (klucz API dostawcy dla żądań przez Gateway)  
  
Gdy myślenie jest włączone dla modeli Anthropic Messages, OpenClaw usuwa końcowe tury wstępnego wypełniania asystenta przed wysłaniem ładunku przez Cloudflare AI Gateway. Anthropic odrzuca wstępne wypełnianie odpowiedzi z rozszerzonym myśleniem, natomiast zwykłe wstępne wypełnianie bez myślenia pozostaje dostępne.

## Pierwsze kroki

* ### Set the provider API key and Gateway details

Uruchom onboarding i wybierz opcję uwierzytelniania Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Zostaniesz poproszony o identyfikator konta, identyfikator gateway i klucz API.

* ### Set a default model

Dodaj model do konfiguracji OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Przykład nieinteraktywny

W konfiguracjach skryptowych lub CI przekaż wszystkie wartości w wierszu poleceń:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Konfiguracja zaawansowana

Authenticated gateways

Jeśli włączono uwierzytelnianie Gateway w Cloudflare, dodaj nagłówek `cf-aig-authorization`. Jest to **dodatkowe względem** klucza API dostawcy.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Environment note

Jeśli Gateway działa jako demon (launchd/systemd), upewnij się, że `CLOUDFLARE_AI_GATEWAY_API_KEY` jest dostępny dla tego procesu.

## Powiązane

[**Model selection** Wybór dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Troubleshooting** Ogólne rozwiązywanie problemów i FAQ. ](</pl/help/troubleshooting>)

Was this useful?YesNo