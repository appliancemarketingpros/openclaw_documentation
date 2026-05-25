---
title: OpenCode Go
source_url: https://docs.openclaw.ai/pl/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go to katalog Go w ramach [OpenCode](</pl/providers/opencode>). Używa tego samego `OPENCODE_API_KEY` co katalog Zen, ale zachowuje identyfikator providera runtime `opencode-go`, aby routing upstream per model pozostał poprawny.

Właściwość | Wartość  
---|---  
Provider runtime | `opencode-go`  
Auth | `OPENCODE_API_KEY`  
Konfiguracja nadrzędna | [OpenCode](</pl/providers/opencode>)  
  
## Wbudowany katalog

OpenClaw pobiera większość wierszy katalogu Go z dołączonego rejestru modeli Pi i uzupełnia bieżące wiersze upstream, dopóki rejestr nie nadrobi zaległości. Uruchom `openclaw models list --provider opencode-go`, aby zobaczyć bieżącą listę modeli.

Provider zawiera:

Referencja modelu | Nazwa  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (3x limits)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Pierwsze kroki

### Interaktywnie

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### Ustaw model Go jako domyślny

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Sprawdź, czy modele są dostępne

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### Nieinteraktywnie

* ### Przekaż klucz bezpośrednio

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Sprawdź, czy modele są dostępne

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Przykład konfiguracji

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Konfiguracja zaawansowana

Zachowanie routingu

OpenClaw automatycznie obsługuje routing per model, gdy referencja modelu używa `opencode-go/...`. Nie jest wymagana dodatkowa konfiguracja providera.

Konwencja referencji runtime

Referencje runtime pozostają jawne: `opencode/...` dla Zen, `opencode-go/...` dla Go. Dzięki temu routing upstream per model pozostaje poprawny w obu katalogach.

Współdzielone poświadczenia

To samo `OPENCODE_API_KEY` jest używane zarówno przez katalog Zen, jak i Go. Wprowadzenie klucza podczas konfiguracji zapisuje poświadczenia dla obu providerów runtime.

## Powiązane

[**OpenCode (nadrzędny)** Wspólny onboarding, przegląd katalogu i uwagi zaawansowane. ](</pl/providers/opencode>) [**Wybór modelu** Wybór providerów, referencji modeli i zachowania failover. ](</pl/concepts/model-providers>)

Was this useful?YesNo