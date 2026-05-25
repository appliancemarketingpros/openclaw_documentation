---
title: Cerebras
source_url: https://docs.openclaw.ai/pl/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) zapewnia szybkie wnioskowanie zgodne z OpenAI na niestandardowym sprzęcie do wnioskowania. OpenClaw zawiera dołączony Plugin dostawcy Cerebras ze statycznym katalogiem czterech modeli.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `cerebras`  
Plugin | dołączony, `enabledByDefault: true`  
Zmienna env uwierzytelniania | `CEREBRAS_API_KEY`  
Flaga onboardingu | `--auth-choice cerebras-api-key`  
Bezpośrednia flaga CLI | `--cerebras-api-key <key>`  
API | zgodne z OpenAI (`openai-completions`)  
Bazowy URL | `https://api.cerebras.ai/v1`  
Model domyślny | `cerebras/zai-glm-4.7`  
  
## Pierwsze kroki

* ### Uzyskaj klucz API

Utwórz klucz API w [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Uruchom onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Sprawdź, czy modele są dostępne

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

Lista powinna zawierać wszystkie cztery dołączone modele. Jeśli `CEREBRAS_API_KEY` nie zostanie rozwiązany, `openclaw models status --json` zgłosi brakujące poświadczenie w `auth.unusableProfiles`.

## Konfiguracja nieinteraktywna

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Wbudowany katalog

OpenClaw dostarcza statyczny katalog Cerebras, który odzwierciedla publiczny punkt końcowy zgodny z OpenAI. Wszystkie cztery modele mają kontekst 128k i maksymalnie 8192 tokeny wyjściowe.

Ref modelu | Nazwa | Rozumowanie | Uwagi  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | tak | Model domyślny; model rozumowania preview  
`cerebras/gpt-oss-120b` | GPT OSS 120B | tak | Produkcyjny model rozumowania  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | nie | Model preview bez rozumowania  
`cerebras/llama3.1-8b` | Llama 3.1 8B | nie | Produkcyjny model nastawiony na szybkość  
  
## Konfiguracja ręczna

Dołączony Plugin zwykle oznacza, że potrzebujesz tylko klucza API. Użyj jawnej konfiguracji `models.providers.cerebras`, gdy chcesz nadpisać metadane modelu albo działać w `mode: "merge"` względem statycznego katalogu:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Powiązane

[**Dostawcy modeli** Wybór dostawców, refów modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Tryby myślenia** Poziomy wysiłku rozumowania dla dwóch modeli Cerebras zdolnych do rozumowania. ](</pl/tools/thinking>) [**Dokumentacja konfiguracji** Domyślne ustawienia agenta i konfiguracja modeli. ](</pl/gateway/config-agents#agent-defaults>) [**FAQ modeli** Profile uwierzytelniania, przełączanie modeli i rozwiązywanie błędów „no profile”. ](</pl/help/faq-models>)

Was this useful?YesNo