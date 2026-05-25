---
title: OpenCode Go
source_url: https://docs.openclaw.ai/nl/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go is de Go-catalogus binnen [OpenCode](</nl/providers/opencode>). Het gebruikt dezelfde `OPENCODE_API_KEY` als de Zen-catalogus, maar behoudt de runtime provider-id `opencode-go` zodat upstream routering per model correct blijft.

Eigenschap | Waarde  
---|---  
Runtime provider | `opencode-go`  
Auth | `OPENCODE_API_KEY`  
Bovenliggende setup | [OpenCode](</nl/providers/opencode>)  
  
## Ingebouwde catalogus

OpenClaw haalt de meeste Go-catalogusrijen uit het gebundelde Pi-modelregister en vult actuele upstream rijen aan terwijl het register wordt bijgewerkt. Voer `openclaw models list --provider opencode-go` uit voor de huidige modellenlijst.

De provider bevat:

Modelverwijzing | Naam  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (3x limieten)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Aan de slag

### Interactive

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### Set a Go model as default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### Non-interactive

* ### Pass the key directly

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Configuratievoorbeeld

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Geavanceerde configuratie

Routing behavior

OpenClaw verwerkt routering per model automatisch wanneer de modelverwijzing `opencode-go/...` gebruikt. Er is geen aanvullende providerconfiguratie vereist.

Runtime ref convention

Runtimeverwijzingen blijven expliciet: `opencode/...` voor Zen, `opencode-go/...` voor Go. Dit houdt upstream routering per model correct in beide catalogi.

Shared credentials

Dezelfde `OPENCODE_API_KEY` wordt gebruikt door zowel de Zen- als de Go-catalogus. Het invoeren van de sleutel tijdens de setup slaat referenties op voor beide runtimeproviders.

## Gerelateerd

[**OpenCode (parent)** Gedeelde onboarding, catalogusoverzicht en geavanceerde notities. ](</nl/providers/opencode>) [**Model selection** Providers, modelverwijzingen en failovergedrag kiezen. ](</nl/concepts/model-providers>)

Was this useful?YesNo