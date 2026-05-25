---
title: Reguły powiadomień push Matrixa dla cichych podglądów
source_url: https://docs.openclaw.ai/pl/channels/matrix-push-rules
scraped_at: 2026-05-25
---

Gdy `channels.matrix.streaming` ma wartość `"quiet"`, OpenClaw edytuje jedno zdarzenie podglądu w miejscu i oznacza sfinalizowaną edycję niestandardową flagą treści. Klienci Matrix wysyłają powiadomienie o końcowej edycji tylko wtedy, gdy reguła powiadomień push dla danego użytkownika pasuje do tej flagi. Ta strona jest przeznaczona dla operatorów, którzy samodzielnie hostują Matrix i chcą zainstalować tę regułę dla każdego konta odbiorcy.

Jeśli chcesz tylko standardowego zachowania powiadomień Matrix, użyj `streaming: "partial"` albo pozostaw streaming wyłączony. Zobacz [Konfiguracja kanału Matrix](</pl/channels/matrix#streaming-previews>).

## Wymagania wstępne

  * użytkownik odbiorcy = osoba, która powinna otrzymać powiadomienie
  * użytkownik bota = konto OpenClaw Matrix wysyłające odpowiedź
  * użyj tokena dostępu użytkownika odbiorcy do poniższych wywołań API
  * dopasuj `sender` w regule push do pełnego MXID użytkownika bota
  * konto odbiorcy musi mieć już działające pushery — reguły cichego podglądu działają tylko wtedy, gdy standardowe dostarczanie powiadomień push Matrix działa poprawnie


## Kroki

* ### Skonfiguruj ciche podglądy

json5Copy code
[code]
    {channels: {matrix: {  streaming: "quiet",},},}
[/code]

* ### Uzyskaj token dostępu odbiorcy

Jeśli to możliwe, użyj ponownie tokena istniejącej sesji klienta. Aby wygenerować nowy:

bashCopy code
[code]
    curl -sS -X POST \"https://matrix.example.org/_matrix/client/v3/login" \-H "Content-Type: application/json" \--data '{"type": "m.login.password","identifier": { "type": "m.id.user", "user": "@alice:example.org" },"password": "REDACTED"}'
[/code]

* ### Sprawdź, czy istnieją pushery

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushers"
[/code]

Jeśli nie zostaną zwrócone żadne pushery, napraw standardowe dostarczanie powiadomień push Matrix dla tego konta przed kontynuowaniem.

* ### Zainstaluj regułę push override

OpenClaw oznacza sfinalizowane, tekstowe edycje podglądu za pomocą `content["com.openclaw.finalized_preview"] = true`. Zainstaluj regułę, która dopasowuje ten znacznik oraz MXID bota jako nadawcę:

bashCopy code
[code]
    curl -sS -X PUT \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname" \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \-H "Content-Type: application/json" \--data '{"conditions": [  { "kind": "event_match", "key": "type", "pattern": "m.room.message" },  {    "kind": "event_property_is",    "key": "content.m\\.relates_to.rel_type",    "value": "m.replace"  },  {    "kind": "event_property_is",    "key": "content.com\\.openclaw\\.finalized_preview",    "value": true  },  { "kind": "event_match", "key": "sender", "pattern": "@bot:example.org" }],"actions": [  "notify",  { "set_tweak": "sound", "value": "default" },  { "set_tweak": "highlight", "value": false }]}'
[/code]

Zastąp przed uruchomieniem:

  * `https://matrix.example.org`: bazowy URL twojego homeservera
  * `$USER_ACCESS_TOKEN`: token dostępu użytkownika odbiorcy
  * `openclaw-finalized-preview-botname`: identyfikator reguły unikalny dla każdego bota i odbiorcy (wzorzec: `openclaw-finalized-preview-<botname>`)
  * `@bot:example.org`: MXID twojego bota OpenClaw, a nie odbiorcy


* ### Zweryfikuj

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname"
[/code]

Następnie przetestuj streamowaną odpowiedź. W trybie cichym pokój pokazuje cichy podgląd wersji roboczej i wysyła powiadomienie po zakończeniu bloku lub tury.

Aby później usunąć regułę, wykonaj `DELETE` dla tego samego URL reguły, używając tokena odbiorcy.

## Uwagi dotyczące wielu botów

Reguły push są indeksowane według `ruleId`: ponowne wykonanie `PUT` dla tego samego identyfikatora aktualizuje pojedynczą regułę. Jeśli wiele botów OpenClaw powiadamia tego samego odbiorcę, utwórz jedną regułę dla każdego bota z odrębnym dopasowaniem nadawcy.

Nowe reguły `override` zdefiniowane przez użytkownika są wstawiane przed domyślnymi regułami wyciszającymi, więc nie jest potrzebny dodatkowy parametr kolejności. Reguła wpływa tylko na tekstowe edycje podglądu, które można sfinalizować w miejscu; awaryjne obsługi mediów i awaryjne obsługi nieaktualnych podglądów używają standardowego dostarczania Matrix.

## Uwagi dotyczące homeservera

Synapse

Nie jest wymagana żadna specjalna zmiana w `homeserver.yaml`. Jeśli standardowe powiadomienia Matrix już docierają do tego użytkownika, token odbiorcy i powyższe wywołanie `pushrules` są głównym krokiem konfiguracji.

Jeśli uruchamiasz Synapse za reverse proxy lub workerami, upewnij się, że `/_matrix/client/.../pushrules/` poprawnie dociera do Synapse. Dostarczaniem powiadomień push zajmuje się główny proces albo `synapse.app.pusher` / skonfigurowane workery pushera — upewnij się, że działają poprawnie.

Reguła używa warunku reguły push `event_property_is` (MSC3758, reguła push v1.10), który został dodany do Synapse w 2023 roku. Starsze wydania Synapse akceptują wywołanie `PUT pushrules/...`, ale po cichu nigdy nie dopasowują warunku — zaktualizuj Synapse, jeśli po sfinalizowanej edycji podglądu nie przychodzi powiadomienie.

Tuwunel

Ten sam przepływ co w Synapse; dla znacznika sfinalizowanego podglądu nie jest potrzebna żadna konfiguracja specyficzna dla Tuwunel.

Jeśli powiadomienia znikają, gdy użytkownik jest aktywny na innym urządzeniu, sprawdź, czy włączono `suppress_push_when_active`. Tuwunel dodał tę opcję w wersji 1.4.2 (wrzesień 2025) i może ona celowo wyciszać powiadomienia push do innych urządzeń, gdy jedno urządzenie jest aktywne.

## Powiązane

  * [Konfiguracja kanału Matrix](</pl/channels/matrix>)
  * [Koncepcje streamingu](</pl/concepts/streaming>)


Was this useful?YesNo