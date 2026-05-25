---
title: Wykonywanie kodu
source_url: https://docs.openclaw.ai/pl/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` uruchamia izolowaną zdalną analizę w Pythonie w Responses API xAI. Jest rejestrowane przez dołączony Plugin `xai` (w ramach kontraktu `tools`) i wysyła żądania do tego samego punktu końcowego `https://api.x.ai/v1/responses`, którego używa `x_search`.

Właściwość | Wartość  
---|---  
Nazwa narzędzia | `code_execution`  
Plugin dostawcy | `xai` (dołączony, `enabledByDefault: true`)  
Uwierzytelnianie | profil uwierzytelniania xAI, `XAI_API_KEY` lub `plugins.entries.xai.config.webSearch.apiKey`  
Model domyślny | `grok-4-1-fast`  
Domyślny limit czasu | 30 sekund  
Domyślny `maxTurns` | nieustawione (xAI stosuje własny limit wewnętrzny)  
  
Różni się to od lokalnego [`exec`](</pl/tools/exec>):

  * `exec` uruchamia polecenia powłoki na Twoim komputerze lub sparowanym węźle.
  * `code_execution` uruchamia Python w zdalnym sandboxie xAI.


Używaj `code_execution` do:

  * Obliczeń.
  * Tworzenia tabel.
  * Szybkich statystyk.
  * Analiz w stylu wykresów.
  * Analizowania danych zwróconych przez `x_search` lub `web_search`.


**Nie** używaj go, gdy potrzebujesz lokalnych plików, swojej powłoki, repozytorium lub sparowanych urządzeń. Do tego użyj [`exec`](</pl/tools/exec>).

## Konfiguracja

* ### Provide an xAI API key

Uruchom `openclaw onboard --auth-choice xai-api-key` dla `code_execution` i `x_search`, albo ustaw `XAI_API_KEY` / skonfiguruj klucz w Pluginie xAI, gdy chcesz także, aby wyszukiwanie internetowe Grok używało tych samych danych uwierzytelniających:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

Albo przez konfigurację:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Enable and tune code_execution

Narzędzie jest sterowane przez `plugins.entries.xai.config.codeExecution.enabled`. Domyślnie jest wyłączone.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Restart the Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` pojawia się na liście narzędzi agenta, gdy Plugin xAI ponownie zarejestruje się z `enabled: true`.

## Jak go używać

Pytaj naturalnie i jasno określ intencję analizy:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

Narzędzie wewnętrznie przyjmuje pojedynczy parametr `task`, więc agent powinien wysłać pełne żądanie analizy i wszelkie dane w treści w jednym prompcie.

## Błędy

Gdy narzędzie działa bez uwierzytelniania, zwraca ustrukturyzowany błąd `missing_xai_api_key`, wskazujący profil uwierzytelniania, zmienną środowiskową i opcje konfiguracji. Błąd ma postać JSON, a nie rzuconego wyjątku, więc agent może samodzielnie go skorygować:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Limity

  * To jest zdalne wykonywanie xAI, a nie wykonywanie lokalnego procesu.
  * Traktuj wyniki jako tymczasową analizę, a nie trwałą sesję notebooka.
  * Nie zakładaj dostępu do lokalnych plików ani swojego obszaru roboczego.
  * Aby uzyskać świeże dane z X, najpierw użyj [`x_search`](</pl/tools/web#x_search>), a następnie przekaż wynik do `code_execution`.


## Powiązane

[**Exec tool** Lokalne wykonywanie poleceń powłoki na Twoim komputerze lub sparowanym węźle. ](</pl/tools/exec>) [**Exec approvals** Zasady zezwalania/odmawiania dla wykonywania poleceń powłoki. ](</pl/tools/exec-approvals>) [**Web tools** `web_search`, `x_search` i `web_fetch`. ](</pl/tools/web>) [**xAI provider** Modele Grok, wyszukiwanie web/x oraz konfiguracja wykonywania kodu. ](</pl/providers/xai>)

Was this useful?YesNo