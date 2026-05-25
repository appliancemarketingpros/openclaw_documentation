---
title: Together AI
source_url: https://docs.openclaw.ai/pl/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) zapewnia dostęp do czołowych modeli open-source, w tym Llama, DeepSeek, Kimi i innych, przez ujednolicone API.

Właściwość | Wartość  
---|---  
Dostawca | `together`  
Uwierzytelnianie | `TOGETHER_API_KEY`  
API | Zgodne z OpenAI  
Bazowy URL | `https://api.together.xyz/v1`  
  
## Pierwsze kroki

* ### Uzyskaj klucz API

Utwórz klucz API na stronie [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Ustaw domyślny model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Przykład nieinteraktywny

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Wbudowany katalog

OpenClaw dostarcza ten dołączony katalog Together:

Referencja modelu | Nazwa | Dane wejściowe | Kontekst | Uwagi  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | tekst, obraz | 262,144 | Model domyślny; rozumowanie włączone  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | tekst | 202,752 | Uniwersalny model tekstowy  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | tekst | 131,072 | Szybki model instrukcyjny  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | tekst, obraz | 10,000,000 | Multimodalny  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | tekst, obraz | 20,000,000 | Multimodalny  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | tekst | 131,072 | Ogólny model tekstowy  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | tekst | 131,072 | Model rozumujący  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | tekst | 262,144 | Dodatkowy model tekstowy Kimi  
  
## Generowanie wideo

Dołączony plugin `together` rejestruje także generowanie wideo przez współdzielone narzędzie `video_generate`.

Właściwość | Wartość  
---|---  
Domyślny model wideo | `together/Wan-AI/Wan2.2-T2V-A14B`  
Tryby | tekst na wideo, referencja pojedynczego obrazu  
Obsługiwane parametry | `aspectRatio`, `resolution`  
  
Aby używać Together jako domyślnego dostawcy wideo:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Uwaga dotycząca środowiska

Jeśli Gateway działa jako daemon (launchd/systemd), upewnij się, że `TOGETHER_API_KEY` jest dostępny dla tego procesu (na przykład w `~/.openclaw/.env` lub przez `env.shellEnv`).

Rozwiązywanie problemów

  * Sprawdź, czy klucz działa: `openclaw models list --provider together`
  * Jeśli modele się nie pojawiają, potwierdź, że klucz API jest ustawiony we właściwym środowisku dla procesu Gateway.
  * Referencje modeli używają formatu `together/<model-id>`.


## Powiązane

[**Wybór modelu** Reguły dostawcy, referencje modeli i zachowanie przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Generowanie wideo** Parametry współdzielonego narzędzia generowania wideo i wybór dostawcy. ](</pl/tools/video-generation>) [**Dokumentacja konfiguracji** Pełny schemat konfiguracji, w tym ustawienia dostawcy. ](</pl/gateway/configuration-reference>) [**Together AI** Panel Together AI, dokumentacja API i cennik. ](<https://together.ai>)

Was this useful?YesNo