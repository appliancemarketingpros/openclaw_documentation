---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/pl/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud jest dostarczany jako dołączony plugin dostawcy w OpenClaw. Zapewnia dostęp do wersji zapoznawczej Tencent Hy3 przez punkt końcowy TokenHub (`tencent-tokenhub`) przy użyciu API zgodnego z OpenAI.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `tencent-tokenhub`  
Plugin | dołączony, `enabledByDefault: true`  
Zmienna env auth | `TOKENHUB_API_KEY`  
Flaga onboardingu | `--auth-choice tokenhub-api-key`  
Bezpośrednia flaga CLI | `--tokenhub-api-key <key>`  
API | zgodne z OpenAI (`openai-completions`)  
Domyślny bazowy URL | `https://tokenhub.tencentmaas.com/v1`  
Globalny bazowy URL | `https://tokenhub-intl.tencentmaas.com/v1` (override)  
Domyślny model | `tencent-tokenhub/hy3-preview`  
  
## Szybki start

* ### Utwórz klucz API TokenHub

Utwórz klucz API w Tencent Cloud TokenHub. Jeśli wybierzesz ograniczony zakres dostępu dla klucza, uwzględnij **Hy3 preview** w dozwolonych modelach.

* ### Uruchom onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Bezpośrednia flagaCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Tylko envCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Zweryfikuj model

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Konfiguracja nieinteraktywna

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Wbudowany katalog

Referencja modelu | Nazwa | Wejście | Kontekst | Maks. wyjście | Uwagi  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | text | 256,000 | 64,000 | Domyślny; z obsługą rozumowania  
  
Hy3 preview to duży model językowy MoE Tencent Hunyuan do rozumowania, wykonywania instrukcji w długim kontekście, kodu i przepływów pracy agentów. Przykłady Tencent zgodne z OpenAI używają `hy3-preview` jako identyfikatora modelu i obsługują standardowe wywoływanie narzędzi chat-completions oraz `reasoning_effort`.

## Ceny warstwowe

Dołączony katalog zawiera metadane kosztów warstwowych skalujące się wraz z długością okna wejściowego, więc szacunki kosztów są wypełniane bez ręcznych nadpisań.

Zakres tokenów wejściowych | Stawka wejściowa | Stawka wyjściowa | Odczyt z cache  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
Stawki są podane za milion tokenów w USD, zgodnie z informacjami Tencent. Nadpisuj ceny w `models.providers.tencent-tokenhub` tylko wtedy, gdy potrzebujesz innej powierzchni.

## Konfiguracja zaawansowana

Nadpisanie punktu końcowego

OpenClaw domyślnie używa punktu końcowego Tencent Cloud `https://tokenhub.tencentmaas.com/v1`. Tencent dokumentuje również międzynarodowy punkt końcowy TokenHub:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Nadpisuj punkt końcowy tylko wtedy, gdy wymaga tego Twoje konto TokenHub lub region.

Dostępność środowiska dla demona

Jeśli Gateway działa jako usługa zarządzana (launchd, systemd, Docker), `TOKENHUB_API_KEY` musi być widoczny dla tego procesu. Ustaw go w `~/.openclaw/.env` albo przez `env.shellEnv`, aby środowiska launchd, systemd lub Docker exec mogły go odczytać.

## Powiązane

[**Dostawcy modeli** Wybieranie dostawców, referencji modeli i zachowania failover. ](</pl/concepts/model-providers>) [**Dokumentacja konfiguracji** Pełny schemat konfiguracji obejmujący ustawienia dostawców. ](</pl/gateway/configuration>) [**Tencent TokenHub** Strona produktu Tencent Cloud TokenHub. ](<https://cloud.tencent.com/product/tokenhub>) [**Karta modelu Hy3 preview** Szczegóły i benchmarki Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo