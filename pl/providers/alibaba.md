---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/pl/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw zawiera wbudowany Plugin `alibaba`, który rejestruje dostawcę generowania wideo dla modeli Wan w Alibaba Model Studio (międzynarodowa nazwa DashScope). Plugin jest domyślnie włączony; wystarczy ustawić klucz API.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `alibaba`  
Plugin | wbudowany, `enabledByDefault: true`  
Zmienne środowiskowe uwierzytelniania | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (wygrywa pierwsze dopasowanie)  
Flaga onboardingu | `--auth-choice alibaba-model-studio-api-key`  
Bezpośrednia flaga CLI | `--alibaba-model-studio-api-key <key>`  
Domyślny model | `alibaba/wan2.6-t2v`  
Domyślny bazowy URL | `https://dashscope-intl.aliyuncs.com`  
  
## Pierwsze kroki

* ### Ustaw klucz API

Użyj onboardingu, aby zapisać klucz dla dostawcy `alibaba`:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

Albo przekaż klucz bezpośrednio podczas instalacji/onboardingu:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

Albo wyeksportuj dowolną z akceptowanych zmiennych środowiskowych przed uruchomieniem Gateway:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Ustaw domyślny model wideo

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Sprawdź, czy dostawca jest skonfigurowany

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

Lista powinna zawierać wszystkie pięć wbudowanych modeli Wan. Jeśli `MODELSTUDIO_API_KEY` nie zostanie rozpoznany, `openclaw models status --json` zgłosi brakujące poświadczenie w `auth.unusableProfiles`.

## Wbudowane modele Wan

Odwołanie do modelu | Tryb  
---|---  
`alibaba/wan2.6-t2v` | Tekst-na-wideo (domyślny)  
`alibaba/wan2.6-i2v` | Obraz-na-wideo  
`alibaba/wan2.6-r2v` | Referencja-na-wideo  
`alibaba/wan2.6-r2v-flash` | Referencja-na-wideo (szybki)  
`alibaba/wan2.7-r2v` | Referencja-na-wideo  
  
## Możliwości i limity

Wbudowany dostawca odzwierciedla limity API wideo Wan w DashScope. Wszystkie trzy tryby mają ten sam limit liczby filmów i maksymalny czas trwania na żądanie; różni się tylko kształt danych wejściowych.

Tryb | Maks. liczba filmów wyjściowych | Maks. liczba obrazów wejściowych | Maks. liczba filmów wejściowych | Maks. czas trwania | Obsługiwane ustawienia sterujące  
---|---|---|---|---|---  
Tekst-na-wideo | 1 | n/d | n/d | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Obraz-na-wideo | 1 | 1 | n/d | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Referencja-na-wideo | 1 | n/d | 4 | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Gdy żądanie pomija `durationSeconds`, dostawca wysyła akceptowaną przez DashScope wartość domyślną **5 sekund**. Ustaw `durationSeconds` jawnie w [narzędziu generowania wideo](</pl/tools/video-generation>), aby wydłużyć czas do 10 s.

## Konfiguracja zaawansowana

Zastąp bazowy URL DashScope

Dostawca domyślnie używa międzynarodowego punktu końcowego DashScope. Aby wskazać punkt końcowy regionu Chin, ustaw:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

Dostawca usuwa końcowe ukośniki przed konstruowaniem URL-i zadań AIGC.

Priorytet zmiennych środowiskowych uwierzytelniania

OpenClaw rozpoznaje klucz API Alibaba ze zmiennych środowiskowych w tej kolejności, wybierając pierwszą niepustą wartość:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Skonfigurowane wpisy `auth.profiles` (ustawione przez `openclaw models auth login`) zastępują rozpoznawanie zmiennych środowiskowych. Zobacz [Profile uwierzytelniania w FAQ modeli](</pl/help/faq-models#what-is-an-auth-profile>), aby poznać rotację profili, czas odnowienia i mechanikę zastępowania.

Relacja z Plugin Qwen

Oba wbudowane Pluginy komunikują się z DashScope i akceptują pokrywające się klucze API. Używaj:

  * identyfikatorów `alibaba/wan*.*`, aby korzystać z dedykowanego dostawcy wideo Wan opisanego na tej stronie.
  * identyfikatorów `qwen/*` dla czatu Qwen, embeddingów i rozumienia multimediów (zobacz [Qwen](</pl/providers/qwen>)).


Jednorazowe ustawienie `MODELSTUDIO_API_KEY` uwierzytelnia oba Pluginy, ponieważ lista zmiennych środowiskowych uwierzytelniania celowo się pokrywa; nie musisz onboardować każdego Pluginu osobno.

## Powiązane

[**Generowanie wideo** Wspólne parametry narzędzia wideo i wybór dostawcy. ](</pl/tools/video-generation>) [**Qwen** Konfiguracja czatu, embeddingów i rozumienia multimediów Qwen przy tym samym uwierzytelnianiu DashScope. ](</pl/providers/qwen>) [**Dokumentacja konfiguracji** Domyślne ustawienia agentów i konfiguracja modeli. ](</pl/gateway/config-agents#agent-defaults>) [**FAQ modeli** Profile uwierzytelniania, przełączanie modeli i rozwiązywanie błędów „brak profilu”. ](</pl/help/faq-models>)

Was this useful?YesNo