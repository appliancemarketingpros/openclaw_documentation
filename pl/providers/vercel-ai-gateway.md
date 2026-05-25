---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/pl/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) udostępnia ujednolicone API do dostępu do setek modeli przez jeden endpoint.

Właściwość | Wartość  
---|---  
Dostawca | `vercel-ai-gateway`  
Uwierzytelnianie | `AI_GATEWAY_API_KEY`  
API | zgodne z Anthropic Messages  
Katalog modeli | automatycznie wykrywany przez `/v1/models`  
  
## Pierwsze kroki

* ### Ustaw klucz API

Uruchom onboarding i wybierz opcję uwierzytelniania AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Ustaw model domyślny

Dodaj model do konfiguracji OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Przykład nieinteraktywny

W przypadku konfiguracji skryptowych lub CI przekaż wszystkie wartości w wierszu poleceń:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Skrót identyfikatora modelu

OpenClaw akceptuje skrócone odwołania do modeli Vercel Claude i normalizuje je w czasie wykonywania:

Skrócony zapis wejściowy | Znormalizowane odwołanie do modelu  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Konfiguracja zaawansowana

Zmienna środowiskowa dla procesów daemon

Jeśli OpenClaw Gateway działa jako daemon (launchd/systemd), upewnij się, że `AI_GATEWAY_API_KEY` jest dostępny dla tego procesu.

Routing dostawcy

Vercel AI Gateway kieruje żądania do dostawcy nadrzędnego na podstawie prefiksu odwołania do modelu. Na przykład `vercel-ai-gateway/anthropic/claude-opus-4.6` jest kierowane przez Anthropic, natomiast `vercel-ai-gateway/openai/gpt-5.5` jest kierowane przez OpenAI, a `vercel-ai-gateway/moonshotai/kimi-k2.6` przez MoonshotAI. Twój pojedynczy `AI_GATEWAY_API_KEY` obsługuje uwierzytelnianie dla wszystkich dostawców nadrzędnych.

Poziomy myślenia

Opcje `/think` podążają za zaufanymi prefiksami modeli nadrzędnych, gdy OpenClaw zna kontrakt dostawcy nadrzędnego. `vercel-ai-gateway/anthropic/...` używa profilu myślenia Claude, w tym adaptacyjnych wartości domyślnych dla modeli Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` i odwołania w stylu Codex udostępniają `/think xhigh` tak samo jak bezpośredni dostawcy OpenAI/OpenAI Codex. Inne odwołania z przestrzenią nazw zachowują normalne poziomy rozumowania, chyba że ich metadane katalogu deklarują więcej.

## Powiązane

[**Wybór modelu** Wybieranie dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Rozwiązywanie problemów** Ogólne rozwiązywanie problemów i FAQ. ](</pl/help/troubleshooting>)

Was this useful?YesNo