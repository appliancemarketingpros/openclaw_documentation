---
title: Usunięcie BlueBubbles i ścieżka imsg iMessage
source_url: https://docs.openclaw.ai/pl/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# Usunięcie BlueBubbles i ścieżka imsg dla iMessage

OpenClaw nie dostarcza już kanału BlueBubbles. Obsługa iMessage działa teraz przez dołączony Plugin `imessage`, który uruchamia [`imsg`](<https://github.com/steipete/imsg>) lokalnie albo przez wrapper SSH i komunikuje się przez JSON-RPC po stdin/stdout.

Jeśli Twoja konfiguracja nadal zawiera `channels.bluebubbles`, zmigruj ją do `channels.imessage`. Starszy URL dokumentacji `/channels/bluebubbles` przekierowuje do [Migracja z BlueBubbles](</pl/channels/imessage-from-bluebubbles>), gdzie znajduje się pełna tabela tłumaczenia konfiguracji i lista kontrolna przełączenia.

## Co się zmieniło

  * W obsługiwanej ścieżce iMessage w OpenClaw nie ma serwera HTTP BlueBubbles, trasy Webhook, hasła REST ani środowiska uruchomieniowego Plugin BlueBubbles.
  * OpenClaw odczytuje i obserwuje Wiadomości przez `imsg` na Macu, na którym zalogowano się w Messages.app.
  * Podstawowe wysyłanie, odbieranie, historia i multimedia używają standardowych powierzchni `imsg` oraz uprawnień macOS.
  * Zaawansowane akcje, takie jak odpowiedzi w wątkach, tapbacki, edycja, cofnięcie wysłania, efekty, potwierdzenia odczytu, wskaźniki pisania i zarządzanie grupami, wymagają `imsg launch` z dostępnym mostkiem prywatnego API.
  * Gateway w systemach Linux i Windows nadal mogą używać iMessage przez ustawienie `channels.imessage.cliPath` na wrapper SSH, który uruchamia `imsg` na zalogowanym Macu.


## Co zrobić

  1. Zainstaluj i zweryfikuj `imsg` na Macu z Wiadomościami:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. Przyznaj uprawnienia Pełnego dostępu do dysku oraz Automatyzacji kontekstowi procesu, który uruchamia `imsg` i OpenClaw.

  3. Przetłumacz starą konfigurację:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Uruchom ponownie Gateway i zweryfikuj:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Przetestuj wiadomości DM, grupy, załączniki oraz wszelkie akcje prywatnego API, od których zależysz, zanim usuniesz stary serwer BlueBubbles.


## Uwagi dotyczące migracji

  * `channels.bluebubbles.serverUrl` i `channels.bluebubbles.password` nie mają odpowiednika w iMessage.
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, katalogi główne załączników, limity rozmiaru multimediów, dzielenie na części i przełączniki akcji mają odpowiedniki w iMessage.
  * `channels.imessage.includeAttachments` nadal jest domyślnie wyłączone. Ustaw je jawnie, jeśli oczekujesz, że przychodzące zdjęcia, notatki głosowe, filmy lub pliki trafią do agenta.
  * Przy `groupPolicy: "allowlist"` skopiuj stary blok `groups`, w tym dowolny wpis wieloznaczny `"*"`. Listy dozwolonych nadawców grupowych i rejestr grup to oddzielne bramki.
  * Powiązania ACP dopasowane do `channel: "bluebubbles"` muszą zostać zmienione na `channel: "imessage"`.
  * Stare klucze sesji BlueBubbles nie stają się kluczami sesji iMessage. Zatwierdzenia parowania są przenoszone według uchwytu, ale historia rozmów pod kluczami sesji BlueBubbles nie jest przenoszona.


## Zobacz też

  * [Migracja z BlueBubbles](</pl/channels/imessage-from-bluebubbles>)
  * [iMessage](</pl/channels/imessage>)
  * [Informacje o konfiguracji - iMessage](</pl/gateway/config-channels#imessage>)


Was this useful?YesNo