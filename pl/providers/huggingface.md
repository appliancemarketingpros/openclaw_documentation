---
title: Hugging Face (inferencja)
source_url: https://docs.openclaw.ai/pl/providers/huggingface
scraped_at: 2026-05-25
---

[Hugging Face Inference Providers](<https://huggingface.co/docs/inference-providers>) oferują zgodne z OpenAI chat completions przez jedno API routera. Otrzymujesz dostęp do wielu modeli (DeepSeek, Llama i innych) za pomocą jednego tokenu. OpenClaw używa **punktu końcowego zgodnego z OpenAI** (tylko chat completions); dla text-to-image, embeddingów lub mowy używaj bezpośrednio [klientów HF inference](<https://huggingface.co/docs/api-inference/quicktour>).

  * Provider: `huggingface`
  * Auth: `HUGGINGFACE_HUB_TOKEN` lub `HF_TOKEN` (token fine-grained z uprawnieniem **Make calls to Inference Providers**)
  * API: zgodne z OpenAI (`https://router.huggingface.co/v1`)
  * Billing: pojedynczy token HF; [cennik](<https://huggingface.co/docs/inference-providers/pricing>) jest zgodny ze stawkami dostawców i obejmuje darmowy poziom.


## Pierwsze kroki

* ### Utwórz token fine-grained

Przejdź do [Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) i utwórz nowy token fine-grained.

* ### Uruchom onboarding

Wybierz **Hugging Face** z listy dostawców, a następnie podaj klucz API, gdy pojawi się monit:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### Wybierz domyślny model

Z listy **Default Hugging Face model** wybierz model, którego chcesz używać. Lista jest ładowana z Inference API, gdy masz prawidłowy token; w przeciwnym razie pokazywana jest lista wbudowana. Twój wybór jest zapisywany jako model domyślny.

Możesz też ustawić lub zmienić model domyślny później w konfiguracji:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### Zweryfikuj, że model jest dostępny

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### Konfiguracja nieinteraktywna

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

To ustawi `huggingface/deepseek-ai/DeepSeek-R1` jako model domyślny.

## Identyfikatory modeli

Model ref mają postać `huggingface/<org>/<model>` (identyfikatory w stylu Hub). Poniższa lista pochodzi z **GET** `https://router.huggingface.co/v1/models`; twój katalog może zawierać więcej.

Model | Ref (dodaj prefiks `huggingface/`)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## Konfiguracja zaawansowana

Wykrywanie modeli i lista rozwijana w onboardingu

OpenClaw wykrywa modele, wywołując bezpośrednio **punkt końcowy Inference** :

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(Opcjonalnie: wyślij `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` albo `$HF_TOKEN`, aby uzyskać pełną listę; niektóre punkty końcowe zwracają podzbiór bez auth.) Odpowiedź ma styl OpenAI: `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }`.

Gdy skonfigurujesz klucz API Hugging Face (przez onboarding, `HUGGINGFACE_HUB_TOKEN` albo `HF_TOKEN`), OpenClaw używa tego GET do wykrywania dostępnych modeli chat-completion. Podczas **interaktywnej konfiguracji** , po podaniu tokenu zobaczysz listę rozwijaną **Default Hugging Face model** wypełnioną danymi z tej listy (albo z wbudowanego katalogu, jeśli żądanie się nie powiedzie). W czasie działania (np. przy uruchamianiu Gateway), gdy klucz jest obecny, OpenClaw ponownie wywołuje **GET** `https://router.huggingface.co/v1/models`, aby odświeżyć katalog. Lista jest scalana z katalogiem wbudowanym (dla metadanych takich jak okno kontekstu i koszt). Jeśli żądanie się nie powiedzie albo nie ustawiono klucza, używany jest tylko katalog wbudowany.

Nazwy modeli, aliasy i sufiksy polityk

  * **Nazwa z API:** Wyświetlana nazwa modelu jest **uzupełniana z GET /v1/models** , gdy API zwraca `name`, `title` albo `display_name`; w przeciwnym razie jest wyprowadzana z identyfikatora modelu (np. `deepseek-ai/DeepSeek-R1` staje się „DeepSeek R1”).
  * **Nadpisanie nazwy wyświetlanej:** Możesz ustawić własną etykietę per model w konfiguracji, tak aby była wyświetlana w CLI i UI dokładnie tak, jak chcesz:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **Sufiksy polityk:** Dołączona dokumentacja i helpery Hugging Face w OpenClaw obecnie traktują te dwa sufiksy jako wbudowane warianty polityk:

    * **`:fastest`** — najwyższa przepustowość.
    * **`:cheapest`** — najniższy koszt na token wyjściowy.

Możesz dodać je jako osobne wpisy w `models.providers.huggingface.models` albo ustawić `model.primary` z tym sufiksem. Możesz też ustawić domyślną kolejność dostawców w [ustawieniach Inference Provider](<https://hf.co/settings/inference-providers>) (bez sufiksu = użyj tej kolejności).

  * **Scalanie konfiguracji:** Istniejące wpisy w `models.providers.huggingface.models` (np. w `models.json`) są zachowywane podczas scalania konfiguracji. Oznacza to, że wszelkie własne `name`, `alias` albo opcje modeli ustawione w tym miejscu zostaną zachowane.


Środowisko i konfiguracja daemona

Jeśli Gateway działa jako daemon (launchd/systemd), upewnij się, że `HUGGINGFACE_HUB_TOKEN` albo `HF_TOKEN` jest dostępne dla tego procesu (na przykład w `~/.openclaw/.env` albo przez `env.shellEnv`).

Config: DeepSeek R1 z fallbackiem Qwen json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

Config: Qwen z wariantami cheapest i fastest json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

Config: DeepSeek + Llama + GPT-OSS z aliasami json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

Config: Wiele modeli Qwen i DeepSeek z sufiksami polityk json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## Powiązane

[**Wybór modelu** Przegląd wszystkich dostawców, model ref i zachowania failoveru. ](</pl/concepts/model-providers>) [**Wybór modelu** Jak wybierać i konfigurować modele. ](</pl/concepts/models>) [**Dokumentacja Inference Providers** Oficjalna dokumentacja Hugging Face Inference Providers. ](<https://huggingface.co/docs/inference-providers>) [**Konfiguracja** Pełna dokumentacja konfiguracji. ](</pl/gateway/configuration>)

Was this useful?YesNo