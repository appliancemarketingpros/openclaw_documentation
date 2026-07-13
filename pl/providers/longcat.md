---
title: LongCat
source_url: https://docs.openclaw.ai/pl/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) udostępnia hostowany interfejs API dla LongCat-2.0 — modelu rozumującego stworzonego z myślą o programowaniu i zadaniach agentowych. OpenClaw udostępnia oficjalny plugin `longcat` dla punktu końcowego LongCat zgodnego z OpenAI.

Właściwość | Wartość  
---|---  
Dostawca | `longcat`  
Uwierzytelnianie | `LONGCAT_API_KEY`  
API | Chat Completions zgodne z OpenAI  
Bazowy adres URL | `https://api.longcat.chat/openai`  
Model | `longcat/LongCat-2.0`  
Kontekst | 1 048 576 tokenów  
Maks. długość wyjścia | 131 072 tokeny  
Dane wejściowe | Tekst  
  
## Instalowanie pluginu

Zainstaluj oficjalny pakiet, a następnie uruchom ponownie Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Pierwsze kroki

* ### Utwórz klucz API

Zaloguj się na [platformie API LongCat](<https://longcat.chat/platform/>) i utwórz klucz na stronie [kluczy API](<https://longcat.chat/platform/api_keys>).

* ### Uruchom konfigurację początkową

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Zweryfikuj model

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

Konfiguracja początkowa dodaje hostowany katalog i wybiera `longcat/LongCat-2.0`, jeśli nie skonfigurowano jeszcze modelu głównego.

### Konfiguracja nieinteraktywna

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Sposób rozumowania

LongCat udostępnia binarne sterowanie myśleniem. OpenClaw odwzorowuje włączone poziomy myślenia na `thinking: { type: "enabled" }`, a `/think off` na `thinking: { type: "disabled" }`. LongCat obecnie nie dokumentuje `reasoning_effort`, dlatego OpenClaw go nie wysyła.

LongCat zwraca tok rozumowania w polu `reasoning_content`. OpenClaw zachowuje to pole podczas ponownego odtwarzania tur wywołań narzędzi przez asystenta, dzięki czemu wieloturowe sesje agenta zachowują oczekiwany przez dostawcę format wiadomości.

## Cennik

Wbudowany katalog korzysta z cennika LongCat w modelu płatności za użycie, podanego w USD za milion tokenów: 0,75 USD za niebuforowane dane wejściowe, 0,015 USD za buforowane dane wejściowe i 2,95 USD za dane wyjściowe. LongCat może oferować tymczasowe rabaty; wiążącymi źródłami są [strona z cennikiem](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) oraz Twoje rozliczenia.

## Samodzielnie hostowany LongCat-2.0

Dostawca `longcat` korzysta z hostowanego interfejsu API LongCat. Aby użyć otwartych wag dostępnych w [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>), udostępnij model za pośrednictwem środowiska uruchomieniowego zgodnego z OpenAI i zamiast tego użyj istniejącego dostawcy [vLLM](</pl/providers/vllm>) lub [SGLang](</pl/providers/sglang>) w OpenClaw.

Zachowaj dokładny identyfikator modelu używany przez środowisko uruchomieniowe w katalogu dostawcy hostowanego samodzielnie; nie kieruj lokalnego wdrożenia przez `longcat/LongCat-2.0`.

## Rozwiązywanie problemów

Klucz działa w powłoce, ale nie w Gateway

Procesy Gateway zarządzane przez demona nie dziedziczą wszystkich zmiennych powłoki interaktywnej. Umieść `LONGCAT_API_KEY` w `~/.openclaw/.env`, skonfiguruj go podczas konfiguracji początkowej lub użyj zatwierdzonego odwołania do sekretu.

Żądania kończą się błędem 402 lub 429

`402` oznacza, że konto nie ma wystarczającego limitu tokenów. `429` oznacza, że klucz API osiągnął limit częstotliwości żądań. Sprawdź [wykorzystanie LongCat](<https://longcat.chat/platform/usage>) i ponów żądania ograniczone limitem po upływie okresu oczekiwania określonego przez dostawcę.

Model nie jest wyświetlany

Uruchom `openclaw plugins list` i upewnij się, że plugin `longcat` jest włączony, a następnie uruchom `openclaw models list --provider longcat`.

## Powiązane materiały

[**Dostawcy modeli** Konfiguracja dostawców, odwołania do modeli i działanie mechanizmu przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Dokumentacja API LongCat** Punkty końcowe hostowanego API, uwierzytelnianie, limity i przykłady. ](<https://longcat.chat/platform/docs/>) [**Karta modelu LongCat-2.0** Architektura, wskazówki dotyczące wdrażania i szczegóły modelu. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Sekrety** Przechowuj dane uwierzytelniające dostawcy bez osadzania zwykłego tekstu w konfiguracji. ](</pl/gateway/secrets>)

Was this useful?YesNo

Open issue