---
title: Wskaźniki pisania
source_url: https://docs.openclaw.ai/pl/concepts/typing-indicators
scraped_at: 2026-05-25
---

Wskaźniki pisania są wysyłane do kanału czatu, gdy uruchomienie jest aktywne. Użyj `agents.defaults.typingMode`, aby kontrolować, **kiedy** zaczyna się pisanie, oraz `typingIntervalSeconds`, aby kontrolować, **jak często** jest odświeżane.

## Domyślne ustawienia

Gdy `agents.defaults.typingMode` jest **nieustawione** , OpenClaw zachowuje starsze działanie:

  * **Czaty bezpośrednie** : pisanie zaczyna się natychmiast po rozpoczęciu pętli modelu.
  * **Czaty grupowe ze wzmianką** : pisanie zaczyna się natychmiast.
  * **Czaty grupowe bez wzmianki** : pisanie zaczyna się dopiero wtedy, gdy tekst wiadomości zaczyna być strumieniowany.
  * **Uruchomienia Heartbeat** : pisanie zaczyna się po rozpoczęciu uruchomienia Heartbeat, jeśli rozpoznany cel Heartbeat jest czatem obsługującym pisanie, a pisanie nie jest wyłączone.


## Tryby

Ustaw `agents.defaults.typingMode` na jedną z wartości:

  * `never` \- brak wskaźnika pisania, kiedykolwiek.
  * `instant` \- rozpocznij pisanie **gdy tylko zacznie się pętla modelu** , nawet jeśli uruchomienie później zwróci tylko token cichej odpowiedzi.
  * `thinking` \- rozpocznij pisanie przy **pierwszej delcie rozumowania** (wymaga `reasoningLevel: "stream"` dla uruchomienia).
  * `message` \- rozpocznij pisanie przy **pierwszej niecichej delcie tekstu** (ignoruje cichy token `NO_REPLY`).


Kolejność „jak wcześnie się uruchamia”: `never` → `message` → `thinking` → `instant`

## Konfiguracja

Ustaw domyślne ustawienie na poziomie agenta:

json5Copy code
[code]
    {  agents: {    defaults: {      typingMode: "thinking",      typingIntervalSeconds: 6,    },  },}
[/code]

Nadpisz tryb lub tempo dla sesji:

json5Copy code
[code]
    {  session: {    typingMode: "message",    typingIntervalSeconds: 4,  },}
[/code]

## Uwagi

  * Tryb `message` nie pokaże pisania dla odpowiedzi wyłącznie cichych, gdy cały ładunek jest dokładnym cichym tokenem (na przykład `NO_REPLY` / `no_reply`, dopasowywanym bez rozróżniania wielkości liter).
  * `thinking` uruchamia się tylko wtedy, gdy uruchomienie strumieniuje rozumowanie (`reasoningLevel: "stream"`). Jeśli model nie emituje delt rozumowania, pisanie się nie rozpocznie.
  * Pisanie Heartbeat jest sygnałem żywotności dla rozpoznanego celu dostarczania. Zaczyna się przy starcie uruchomienia Heartbeat zamiast podążać za czasem strumienia `message` lub `thinking`. Ustaw `typingMode: "never"`, aby je wyłączyć.
  * Heartbeat nie pokazuje pisania, gdy `target: "none"`, gdy nie można rozpoznać celu, gdy dostarczanie czatu jest wyłączone dla Heartbeat, lub gdy kanał nie obsługuje pisania.
  * `typingIntervalSeconds` kontroluje **tempo odświeżania** , a nie czas rozpoczęcia. Domyślna wartość to 6 sekund.


## Powiązane

[**Obecność** Jak Gateway śledzi połączonych klientów i pokazuje ich na karcie Instances w macOS. ](</pl/concepts/presence>) [**Strumieniowanie i dzielenie na fragmenty** Zachowanie strumieniowania wychodzącego, granice fragmentów i dostarczanie specyficzne dla kanału. ](</pl/concepts/streaming>)

Was this useful?YesNo