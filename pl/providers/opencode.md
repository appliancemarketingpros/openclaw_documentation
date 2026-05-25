---
title: OpenCode
source_url: https://docs.openclaw.ai/pl/providers/opencode
scraped_at: 2026-05-25
---

OpenCode udostępnia w OpenClaw dwa hostowane katalogi:

Katalog | Prefiks | Dostawca runtime  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Oba katalogi używają tego samego klucza API OpenCode. OpenClaw zachowuje rozdzielone identyfikatory dostawców runtime, aby routing upstream dla poszczególnych modeli pozostał poprawny, ale onboarding i dokumentacja traktują je jako jedną konfigurację OpenCode.

## Pierwsze kroki

### Katalog Zen

**Najlepsze do:** wyselekcjonowanego wielomodelowego proxy OpenCode (Claude, GPT, Gemini).

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Albo przekaż klucz bezpośrednio:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Ustaw model Zen jako domyślny

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Sprawdź, czy modele są dostępne

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Katalog Go

**Najlepsze do:** hostowanej przez OpenCode linii modeli Kimi, GLM i MiniMax.

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Albo przekaż klucz bezpośrednio:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
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

## Przykład konfiguracji

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Wbudowane katalogi

### Zen

Właściwość | Wartość  
---|---  
Dostawca runtime | `opencode`  
Przykładowe modele | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Właściwość | Wartość  
---|---  
Dostawca runtime | `opencode-go`  
Przykładowe modele | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Konfiguracja zaawansowana

Aliasy klucza API

`OPENCODE_ZEN_API_KEY` jest również obsługiwany jako alias dla `OPENCODE_API_KEY`.

Współdzielone poświadczenia

Wprowadzenie jednego klucza OpenCode podczas konfiguracji zapisuje poświadczenia dla obu dostawców runtime. Nie musisz przechodzić onboardingu osobno dla każdego katalogu.

Rozliczanie i panel

Logujesz się do OpenCode, dodajesz dane rozliczeniowe i kopiujesz swój klucz API. Rozliczanie i dostępność katalogów są zarządzane z panelu OpenCode.

Zachowanie odtwarzania Gemini

Odwołania OpenCode oparte na Gemini pozostają na ścieżce proxy-Gemini, więc OpenClaw zachowuje tam sanityzację sygnatur myślenia Gemini bez włączania natywnej walidacji odtwarzania Gemini ani przepisów bootstrap.

Zachowanie odtwarzania dla modeli innych niż Gemini

Odwołania OpenCode inne niż Gemini zachowują minimalną politykę odtwarzania zgodną z OpenAI.

## Powiązane

[**Wybór modelu** Wybór dostawców, odwołań do modeli i zachowania failover. ](</pl/concepts/model-providers>) [**Dokumentacja konfiguracji** Pełna dokumentacja konfiguracji agentów, modeli i dostawców. ](</pl/gateway/configuration-reference>)

Was this useful?YesNo