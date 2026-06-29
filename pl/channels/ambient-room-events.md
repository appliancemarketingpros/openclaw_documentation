---
title: Zdarzenia otoczenia w pomieszczeniu
source_url: https://docs.openclaw.ai/pl/channels/ambient-room-events
scraped_at: 2026-06-29
---

ChannelsConfiguration

Zdarzenia pokoju w tle pozwalają OpenClaw przetwarzać niewspomniane rozmowy w grupie lub kanale jako cichy kontekst. Agent może aktualizować pamięć i stan sesji, ale pokój pozostaje cichy, chyba że agent jawnie wywoła narzędzie `message`.

W przypadku zawsze aktywnych czatów grupowych jest to zalecany tryb: połącz `messages.groupChat.unmentionedInbound: "room_event"` z `messages.groupChat.visibleReplies: "message_tool"`. Użyj go, gdy agent ma słuchać, decydować, kiedy odpowiedź jest przydatna, i unikać starego wzorca promptu polegającego na odpowiadaniu `NO_REPLY`.

Obsługiwane obecnie: kanały gildii Discord, kanały Slack i kanały prywatne, wieloosobowe wiadomości DM Slack oraz grupy lub supergrupy Telegram. Inne kanały grupowe zachowują dotychczasowe zachowanie grupowe, chyba że ich strona kanału wskazuje obsługę zdarzeń pokoju w tle.

## Zalecana konfiguracja

Ustaw globalne zachowanie czatu grupowego:

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },}
[/code]

Następnie skonfiguruj sam pokój jako zawsze aktywny, wyłączając dla niego wymóg wzmianki. Kanał nadal musi być dozwolony przez swoją zwykłą wartość `groupPolicy`, listę dozwolonych pokojów oraz listę dozwolonych nadawców.

Po zapisaniu konfiguracji Gateway przeładowuje ustawienia `messages` na gorąco. Uruchom ponownie tylko wtedy, gdy obserwowanie plików lub przeładowywanie konfiguracji jest wyłączone.

## Co się zmienia

Przy `messages.groupChat.unmentionedInbound: "room_event"`:

  * niewspomniane dozwolone wiadomości grupowe lub kanałowe stają się cichymi zdarzeniami pokoju
  * wiadomości ze wzmianką pozostają żądaniami użytkownika
  * polecenia tekstowe i polecenia natywne pozostają żądaniami użytkownika
  * żądania przerwania lub zatrzymania pozostają żądaniami użytkownika
  * wiadomości bezpośrednie pozostają żądaniami użytkownika


Zdarzenia pokoju używają ścisłego widocznego dostarczania. Końcowy tekst asystenta jest prywatny. Agent musi wywołać `message(action=send)`, aby opublikować w pokoju.

## Przykład Discord

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },  channels: {    discord: {      groupPolicy: "allowlist",      guilds: {        "&lt;DISCORD_SERVER_ID&gt;": {          requireMention: false,          users: ["&lt;YOUR_DISCORD_USER_ID&gt;"],        },      },    },  },}
[/code]

Użyj konfiguracji Discord dla konkretnego kanału, gdy tylko jeden kanał ma działać w tle:

json5Copy code
[code]
    {  channels: {    discord: {      guilds: {        "&lt;DISCORD_SERVER_ID&gt;": {          channels: {            "&lt;DISCORD_CHANNEL_ID_OR_NAME&gt;": {              allow: true,              requireMention: false,            },          },        },      },    },  },}
[/code]

## Przykład Slack

Listy dozwolonych kanałów Slack opierają się przede wszystkim na identyfikatorach. Używaj identyfikatorów kanałów, takich jak `C12345678`, a nie `#channel-name`.

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },  channels: {    slack: {      groupPolicy: "allowlist",      channels: {        "&lt;SLACK_CHANNEL_ID&gt;": {          allow: true,          requireMention: false,        },      },    },  },}
[/code]

## Przykład Telegram

W przypadku grup Telegram bot musi widzieć zwykłe wiadomości grupowe. Jeśli `requireMention: false`, wyłącz tryb prywatności BotFather albo użyj innej konfiguracji Telegram, która dostarcza botowi pełny ruch grupowy.

json5Copy code
[code]
    {  messages: {    groupChat: {      unmentionedInbound: "room_event",      visibleReplies: "message_tool",      historyLimit: 50,    },  },  channels: {    telegram: {      groups: {        "&lt;TELEGRAM_GROUP_CHAT_ID&gt;": {          groupPolicy: "open",          requireMention: false,        },      },    },  },}
[/code]

Identyfikatory grup Telegram są zwykle liczbami ujemnymi, takimi jak `-1001234567890`. Odczytaj `chat.id` z `openclaw logs --follow`, przekaż wiadomość grupową do bota pomocniczego identyfikatorów albo sprawdź Bot API `getUpdates`.

## Polityka specyficzna dla agenta

Użyj nadpisania agenta, gdy kilku agentów współdzieli ten sam pokój, ale tylko jeden powinien traktować niewspomniane rozmowy jako kontekst w tle:

json5Copy code
[code]
    {  messages: {    groupChat: {      visibleReplies: "message_tool",    },  },  agents: {    list: [      {        id: "main",        groupChat: {          unmentionedInbound: "room_event",          mentionPatterns: ["@openclaw", "openclaw"],        },      },    ],  },}
[/code]

Wartość `agents.list[].groupChat.unmentionedInbound` specyficzna dla agenta nadpisuje `messages.groupChat.unmentionedInbound` dla tego agenta.

## Tryby widocznych odpowiedzi

`messages.groupChat.visibleReplies` domyślnie przyjmuje wartość `"automatic"` dla zwykłych żądań użytkownika w grupie lub kanale. Zachowaj tę wartość domyślną, gdy chcesz, aby końcowy tekst asystenta był publikowany widocznie bez wymagania jawnego wywołania narzędzia wiadomości.

W przypadku zawsze aktywnych pokojów w tle nadal zalecane jest `messages.groupChat.visibleReplies: "message_tool"`, szczególnie z modelami najnowszej generacji, niezawodnymi w używaniu narzędzi, takimi jak GPT 5.5. Pozwala to agentowi decydować, kiedy się odezwać, przez wywołanie narzędzia wiadomości. Jeśli model zwróci tekst końcowy bez wywołania narzędzia, OpenClaw zachowa ten tekst końcowy jako prywatny i zarejestruje metadane wstrzymanego dostarczenia.

Zdarzenia pokoju pozostają ścisłe nawet wtedy, gdy inne żądania grupowe używają odpowiedzi automatycznych. Niewspomniane zdarzenia pokoju w tle nadal wymagają `message(action=send)` dla widocznego wyjścia.

## Historia

`messages.groupChat.historyLimit` kontroluje globalną domyślną historię grupy. Kanały mogą ją nadpisać za pomocą `channels.<channel>.historyLimit`, a niektóre kanały obsługują również limity historii dla poszczególnych kont.

Ustaw `historyLimit: 0`, aby wyłączyć kontekst historii grupy.

Obsługiwane kanały zdarzeń pokoju zachowują ostatnie wiadomości pokoju w tle jako kontekst. Discord zachowuje historię zdarzeń pokoju do momentu powodzenia widocznego wysłania Discord, aby cichy kontekst nie został utracony przed dostarczeniem przez narzędzie wiadomości.

## Rozwiązywanie problemów

Jeśli pokój pokazuje pisanie lub użycie tokenów, ale nie ma widocznej wiadomości:

  1. Potwierdź, że pokój jest dozwolony przez listę dozwolonych kanału i listę dozwolonych nadawców.
  2. Potwierdź, że `requireMention: false` jest ustawione na oczekiwanym poziomie pokoju.
  3. Sprawdź, czy `messages.groupChat.unmentionedInbound` albo nadpisanie agenta ma wartość `"room_event"`.
  4. Sprawdź logi pod kątem metadanych wstrzymanego końcowego payloadu lub `didSendViaMessagingTool: false`.
  5. W przypadku zwykłych żądań grupowych zachowaj lub przywróć `messages.groupChat.visibleReplies: "automatic"`, jeśli chcesz, aby końcowe odpowiedzi były publikowane automatycznie. W przypadku pokojów w tle używających `message_tool` użyj modelu/runtime, który niezawodnie wywołuje narzędzia.


Jeśli pokoje w tle Telegram w ogóle się nie wyzwalają, sprawdź tryb prywatności BotFather i zweryfikuj, czy Gateway odbiera zwykłe wiadomości grupowe.

Jeśli pokoje w tle Slack się nie wyzwalają, sprawdź, czy kluczem kanału jest identyfikator kanału Slack oraz czy aplikacja ma wymagany zakres `channels:history` lub `groups:history` dla tego typu pokoju.

## Powiązane

  * [Grupy](</pl/channels/groups>)
  * [Discord](</pl/channels/discord>)
  * [Slack](</pl/channels/slack>)
  * [Telegram](</pl/channels/telegram>)
  * [Rozwiązywanie problemów z kanałami](</pl/channels/troubleshooting>)
  * [Dokumentacja konfiguracji kanałów](</pl/gateway/config-channels>)


Was this useful?YesNo

Open issue