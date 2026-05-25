---
title: Qwen
source_url: https://docs.openclaw.ai/pl/providers/qwen
scraped_at: 2026-05-25
---

OpenClaw traktuje teraz Qwen jako wbudowanego dostawcę pierwszej klasy z kanonicznym id `qwen`. Wbudowany dostawca obsługuje punkty końcowe Qwen Cloud / Alibaba DashScope oraz Coding Plan i utrzymuje działanie starszych id `modelstudio` jako aliasu zgodności.

  * Dostawca: `qwen`
  * Preferowana zmienna środowiskowa: `QWEN_API_KEY`
  * Akceptowane także dla zgodności: `MODELSTUDIO_API_KEY`, `DASHSCOPE_API_KEY`
  * Styl API: zgodny z OpenAI


## Pierwsze kroki

Wybierz typ planu i wykonaj kroki konfiguracji.

### Coding Plan (subskrypcja)

**Najlepsze dla:** dostępu opartego na subskrypcji przez Qwen Coding Plan.

* ### Uzyskaj klucz API

Utwórz lub skopiuj klucz API z [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Uruchom onboarding

Dla punktu końcowego **globalnego** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

Dla punktu końcowego **chińskiego** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### Ustaw model domyślny

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standard (płatność za użycie)

**Najlepsze dla:** dostępu z płatnością za użycie przez standardowy punkt końcowy Model Studio, w tym modeli takich jak `qwen3.6-plus`, które mogą nie być dostępne w Coding Plan.

* ### Uzyskaj klucz API

Utwórz lub skopiuj klucz API z [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Uruchom onboarding

Dla punktu końcowego **globalnego** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Dla punktu końcowego **chińskiego** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### Ustaw model domyślny

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

## Typy planów i punkty końcowe

Plan | Region | Wybór uwierzytelniania | Punkt końcowy  
---|---|---|---  
Standard (płatność za użycie) | Chiny | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
Standard (płatność za użycie) | Global | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (subskrypcja) | Chiny | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (subskrypcja) | Global | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
  
Dostawca automatycznie wybiera punkt końcowy na podstawie wybranego uwierzytelniania. Kanoniczne wybory używają rodziny `qwen-*`; `modelstudio-*` pozostaje wyłącznie dla zgodności. Możesz nadpisać to niestandardową wartością `baseUrl` w konfiguracji.

## Wbudowany katalog

OpenClaw obecnie dostarcza ten wbudowany katalog Qwen. Skonfigurowany katalog jest świadomy punktu końcowego: konfiguracje Coding Plan pomijają modele, o których wiadomo, że działają tylko na punkcie końcowym Standard.

Odwołanie do modelu | Wejście | Kontekst | Uwagi  
---|---|---|---  
`qwen/qwen3.5-plus` | tekst, obraz | 1,000,000 | Model domyślny  
`qwen/qwen3.6-plus` | tekst, obraz | 1,000,000 | Preferuj punkty końcowe Standard, gdy potrzebujesz tego modelu  
`qwen/qwen3-max-2026-01-23` | tekst | 262,144 | Linia Qwen Max  
`qwen/qwen3-coder-next` | tekst | 262,144 | Kodowanie  
`qwen/qwen3-coder-plus` | tekst | 1,000,000 | Kodowanie  
`qwen/MiniMax-M2.5` | tekst | 1,000,000 | Rozumowanie włączone  
`qwen/glm-5` | tekst | 202,752 | GLM  
`qwen/glm-4.7` | tekst | 202,752 | GLM  
`qwen/kimi-k2.5` | tekst, obraz | 262,144 | Moonshot AI przez Alibaba  
  
## Kontrolki myślenia

Dla modeli Qwen Cloud z włączonym rozumowaniem wbudowany dostawca mapuje poziomy myślenia OpenClaw na flagę żądania najwyższego poziomu DashScope `enable_thinking`. Wyłączone myślenie wysyła `enable_thinking: false`; inne poziomy myślenia wysyłają `enable_thinking: true`.

## Dodatki multimodalne

Plugin `qwen` udostępnia także możliwości multimodalne w punktach końcowych DashScope **Standard** (nie w punktach końcowych Coding Plan):

  * **Rozumienie wideo** przez `qwen-vl-max-latest`
  * **Generowanie wideo Wan** przez `wan2.6-t2v` (domyślnie), `wan2.6-i2v`, `wan2.6-r2v`, `wan2.6-r2v-flash`, `wan2.7-r2v`


Aby używać Qwen jako domyślnego dostawcy wideo:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## Konfiguracja zaawansowana

Rozumienie obrazów i wideo

Dołączony Plugin Qwen rejestruje rozumienie multimediów dla obrazów i wideo w punktach końcowych DashScope **Standard** (nie w punktach końcowych Coding Plan).

Właściwość | Wartość  
---|---  
Model | `qwen-vl-max-latest`  
Obsługiwane dane wejściowe | Obrazy, wideo  
  
Rozumienie multimediów jest automatycznie rozwiązywane na podstawie skonfigurowanego uwierzytelniania Qwen — dodatkowa konfiguracja nie jest potrzebna. Upewnij się, że używasz punktu końcowego Standard (pay-as-you-go) do obsługi rozumienia multimediów.

Dostępność Qwen 3.6 Plus

`qwen3.6-plus` jest dostępny w punktach końcowych Model Studio Standard (pay-as-you-go):

  * Chiny: `dashscope.aliyuncs.com/compatible-mode/v1`
  * Globalnie: `dashscope-intl.aliyuncs.com/compatible-mode/v1`


Jeśli punkty końcowe Coding Plan zwracają błąd „unsupported model” dla `qwen3.6-plus`, przełącz się na Standard (pay-as-you-go) zamiast pary punktu końcowego i klucza Coding Plan.

Dołączony katalog Qwen w OpenClaw nie ogłasza `qwen3.6-plus` w punktach końcowych Coding Plan, ale jawnie skonfigurowane wpisy `qwen/qwen3.6-plus` w `models.providers.qwen.models` są respektowane dla baseUrls Coding Plan, więc możesz włączyć ten model, jeśli Aliyun udostępni go w Twojej subskrypcji. Nadrzędne API nadal decyduje, czy wywołanie się powiedzie.

Plan możliwości

Plugin `qwen` jest pozycjonowany jako dom dostawcy dla pełnej powierzchni Qwen Cloud, a nie tylko modeli do kodowania/tekstu.

  * **Modele tekstu/czatu:** dołączone teraz
  * **Wywoływanie narzędzi, dane wyjściowe ustrukturyzowane, myślenie:** dziedziczone z transportu zgodnego z OpenAI
  * **Generowanie obrazów:** planowane na warstwie Plugin dostawcy
  * **Rozumienie obrazów/wideo:** dołączone teraz w punkcie końcowym Standard
  * **Mowa/audio:** planowane na warstwie Plugin dostawcy
  * **Osadzenia pamięci/ponowne rankingowanie:** planowane przez powierzchnię adaptera osadzeń
  * **Generowanie wideo:** dołączone teraz przez współdzieloną możliwość generowania wideo

Szczegóły generowania wideo

W przypadku generowania wideo OpenClaw mapuje skonfigurowany region Qwen na odpowiadający host DashScope AIGC przed przesłaniem zadania:

  * Globalnie/Intl: `https://dashscope-intl.aliyuncs.com`
  * Chiny: `https://dashscope.aliyuncs.com`


Oznacza to, że zwykły `models.providers.qwen.baseUrl` wskazujący hosty Qwen Coding Plan lub Standard nadal utrzymuje generowanie wideo we właściwym regionalnym punkcie końcowym wideo DashScope.

Obecne dołączone limity generowania wideo Qwen:

  * Do **1** wideo wyjściowego na żądanie
  * Do **1** obrazu wejściowego
  * Do **4** wideo wejściowych
  * Do **10 sekund** czasu trwania
  * Obsługuje `size`, `aspectRatio`, `resolution`, `audio` i `watermark`
  * Tryb obrazu/wideo referencyjnego obecnie wymaga **zdalnych adresów URL http(s)**. Lokalne ścieżki plików są odrzucane z góry, ponieważ punkt końcowy wideo DashScope nie akceptuje przesłanych lokalnych buforów dla tych referencji.

Zgodność użycia strumieniowania

Natywne punkty końcowe Model Studio ogłaszają zgodność użycia strumieniowania we współdzielonym transporcie `openai-completions`. OpenClaw opiera to teraz na możliwościach punktu końcowego, więc identyfikatory niestandardowych dostawców zgodnych z DashScope kierowane na te same natywne hosty dziedziczą to samo zachowanie użycia strumieniowania zamiast wymagać konkretnie wbudowanego identyfikatora dostawcy `qwen`.

Zgodność natywnego użycia strumieniowania dotyczy zarówno hostów Coding Plan, jak i hostów zgodnych z DashScope Standard:

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Regiony punktów końcowych multimodalnych

Powierzchnie multimodalne (rozumienie wideo i generowanie wideo Wan) używają punktów końcowych DashScope **Standard** , a nie punktów końcowych Coding Plan:

  * Globalny/Intl bazowy adres URL Standard: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * Chiński bazowy adres URL Standard: `https://dashscope.aliyuncs.com/compatible-mode/v1`

Konfiguracja środowiska i demona

Jeśli Gateway działa jako demon (launchd/systemd), upewnij się, że `QWEN_API_KEY` jest dostępny dla tego procesu (na przykład w `~/.openclaw/.env` lub przez `env.shellEnv`).

## Powiązane

[**Wybór modelu** Wybór dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Generowanie wideo** Wspólne parametry narzędzia wideo i wybór dostawcy. ](</pl/tools/video-generation>) [**Alibaba (ModelStudio)** Starszy dostawca ModelStudio i uwagi dotyczące migracji. ](</pl/providers/alibaba>) [**Rozwiązywanie problemów** Ogólne rozwiązywanie problemów i FAQ. ](</pl/help/troubleshooting>)

Was this useful?YesNo