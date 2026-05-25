---
title: ClickClack
source_url: https://docs.openclaw.ai/pl/channels/clickclack
scraped_at: 2026-05-25
---

ClickClack łączy OpenClaw z samodzielnie hostowanym obszarem roboczym ClickClack przez natywne tokeny botów ClickClack.

Użyj tego, gdy chcesz, aby agent OpenClaw pojawiał się jako użytkownik bota ClickClack. ClickClack obsługuje niezależne boty usługowe i boty należące do użytkowników; boty należące do użytkowników zachowują `owner_user_id` i otrzymują tylko przyznane przez Ciebie zakresy tokena.

## Szybka konfiguracja

Utwórz token bota w ClickClack:

bashCopy code
[code]
    clickclack admin bot create \  --workspace <workspace_id_or_slug> \  --name "OpenClaw" \  --handle openclaw \  --scopes bot:write \  --plain
[/code]

Dla bota należącego do użytkownika dodaj `--owner <user_id>`.

Skonfiguruj OpenClaw:

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      token: { source: "env", provider: "default", id: "CLICKCLACK_BOT_TOKEN" },      workspace: "default",      defaultTo: "channel:general",      agentId: "clickclack-bot",      replyMode: "model",    },  },}
[/code]

Następnie uruchom:

bashCopy code
[code]
    export CLICKCLACK_BOT_TOKEN="ccb_..."openclaw gateway
[/code]

## Wiele botów

Każde konto otwiera własne połączenie ClickClack w czasie rzeczywistym i używa własnego tokena bota.

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      defaultAccount: "service",      accounts: {        service: {          token: { source: "env", provider: "default", id: "CLICKCLACK_SERVICE_BOT_TOKEN" },          workspace: "default",          defaultTo: "channel:general",          agentId: "service-bot",          replyMode: "model",        },        peter: {          token: { source: "env", provider: "default", id: "CLICKCLACK_PETER_BOT_TOKEN" },          workspace: "default",          defaultTo: "dm:usr_...",          agentId: "peter-bot",          replyMode: "model",        },      },    },  },}
[/code]

`replyMode: "model"` używa `api.runtime.llm.complete` bezpośrednio do krótkich odpowiedzi bota. Gdy konto ustawia `agentId`, OpenClaw wymaga jawnego bitu zaufania `plugins.entries.clickclack.llm.allowAgentIdOverride`, aby Plugin mógł uruchamiać uzupełnienia dla tego agenta bota. Nie włączaj go, jeśli używasz tylko domyślnej trasy agenta.

## Cele

  * `channel:<name-or-id>` wysyła do kanału obszaru roboczego. Cele bez prefiksu domyślnie używają `channel:`.
  * `dm:<user_id>` tworzy lub ponownie używa bezpośredniej rozmowy z tym użytkownikiem.
  * `thread:<message_id>` odpowiada w istniejącym wątku.


Przykłady:

bashCopy code
[code]
    openclaw message send --channel clickclack --target channel:general --message "hello"openclaw message send --channel clickclack --target dm:usr_123 --message "hello"openclaw message send --channel clickclack --target thread:msg_123 --message "following up"
[/code]

## Uprawnienia

Zakresy tokenów ClickClack są egzekwowane przez API ClickClack.

  * `bot:read`: odczyt danych obszaru roboczego/kanału/wiadomości/wątku/DM/czasu rzeczywistego/profilu.
  * `bot:write`: `bot:read` oraz wiadomości w kanałach, odpowiedzi w wątkach, DM i przesyłanie plików.
  * `bot:admin`: `bot:write` oraz tworzenie kanałów.


OpenClaw potrzebuje tylko `bot:write` do zwykłego czatu agenta.

## Rozwiązywanie problemów

  * `ClickClack is not configured`: ustaw `channels.clickclack.token` lub `CLICKCLACK_BOT_TOKEN`.
  * `workspace not found`: ustaw `workspace` na identyfikator obszaru roboczego lub slug zwrócony przez ClickClack.
  * Brak przychodzących odpowiedzi: potwierdź, że token ma dostęp do odczytu w czasie rzeczywistym i że bot nie odpowiada na własne wiadomości.
  * Wysyłanie do kanału kończy się niepowodzeniem: sprawdź, czy bot jest członkiem obszaru roboczego i ma `bot:write`.


Was this useful?YesNo