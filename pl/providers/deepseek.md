---
title: DeepSeek
source_url: https://docs.openclaw.ai/pl/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) udostępnia zaawansowane modele AI z API zgodnym z OpenAI.

Właściwość | Wartość  
---|---  
Dostawca | `deepseek`  
Uwierzytelnianie | `DEEPSEEK_API_KEY`  
API | zgodne z OpenAI  
Bazowy URL | `https://api.deepseek.com`  
  
## Pierwsze kroki

* ### Uzyskaj klucz API

Utwórz klucz API na [platform.deepseek.com](<https://platform.deepseek.com/api_keys>).

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

To poprosi o klucz API i ustawi `deepseek/deepseek-v4-flash` jako model domyślny.

* ### Sprawdź, czy modele są dostępne

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

Aby sprawdzić dołączony statyczny katalog bez wymagania działającego Gateway, użyj:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

Konfiguracja nieinteraktywna

W przypadku instalacji skryptowych lub bez interfejsu przekaż wszystkie flagi bezpośrednio:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Wbudowany katalog

Ref modelu | Nazwa | Dane wejściowe | Kontekst | Maks. dane wyjściowe | Uwagi  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | tekst | 1,000,000 | 384,000 | Model domyślny; powierzchnia V4 obsługująca myślenie  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | tekst | 1,000,000 | 384,000 | Powierzchnia V4 obsługująca myślenie  
`deepseek/deepseek-chat` | DeepSeek Chat | tekst | 131,072 | 8,192 | Powierzchnia DeepSeek V3.2 bez myślenia  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | tekst | 131,072 | 65,536 | Powierzchnia V3.2 z włączonym rozumowaniem  
  
## Myślenie i narzędzia

Sesje myślenia DeepSeek V4 mają bardziej rygorystyczny kontrakt odtwarzania niż większość dostawców zgodnych z OpenAI: po użyciu narzędzi w turze z włączonym myśleniem DeepSeek oczekuje, że odtworzone komunikaty asystenta z tej tury będą zawierać `reasoning_content` w kolejnych żądaniach. OpenClaw obsługuje to wewnątrz Plugin DeepSeek, więc normalne wieloturowe użycie narzędzi działa z `deepseek/deepseek-v4-flash` i `deepseek/deepseek-v4-pro`.

Jeśli przełączysz istniejącą sesję z innego dostawcy zgodnego z OpenAI na model DeepSeek V4, starsze tury wywołań narzędzi asystenta mogą nie mieć natywnego DeepSeek `reasoning_content`. OpenClaw uzupełnia to brakujące pole w odtwarzanych komunikatach asystenta dla żądań myślenia DeepSeek V4, aby dostawca mógł zaakceptować historię bez wymagania `/new`.

Gdy myślenie jest wyłączone w OpenClaw (w tym wybór **None** w UI), OpenClaw wysyła do DeepSeek `thinking: { type: "disabled" }` i usuwa odtworzone `reasoning_content` z wychodzącej historii. Dzięki temu sesje z wyłączonym myśleniem pozostają na ścieżce DeepSeek bez myślenia.

Użyj `deepseek/deepseek-v4-flash` jako domyślnej szybkiej ścieżki. Użyj `deepseek/deepseek-v4-pro`, gdy chcesz silniejszy model V4 i możesz zaakceptować wyższy koszt lub opóźnienie.

## Testowanie live

Bezpośredni zestaw modeli live obejmuje DeepSeek V4 w nowoczesnym zestawie modeli. Aby uruchomić tylko bezpośrednie testy modeli DeepSeek V4:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

Ten test live sprawdza, czy oba modele V4 mogą ukończyć działanie oraz czy kolejne tury myślenia/narzędzi zachowują ładunek odtwarzania wymagany przez DeepSeek.

## Przykład konfiguracji

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## Powiązane

[**Wybór modelu** Wybieranie dostawców, refów modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Dokumentacja konfiguracji** Pełna dokumentacja konfiguracji agentów, modeli i dostawców. ](</pl/gateway/configuration-reference>)

Was this useful?YesNo