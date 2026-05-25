---
title: Routing wieloagentowy
source_url: https://docs.openclaw.ai/pl/concepts/multi-agent
scraped_at: 2026-05-25
---

Uruchom wiele _izolowanych_ agentów — każdy z własnym workspace, katalogiem stanu (`agentDir`) i historią sesji — oraz wiele kont kanałów (np. dwa konta WhatsApp) w jednym działającym Gateway. Wiadomości przychodzące są kierowane do właściwego agenta przez wiązania.

**Agent** oznacza tutaj pełny zakres dla danej persony: pliki workspace, profile uwierzytelniania, rejestr modeli i magazyn sesji. `agentDir` to katalog stanu na dysku, który przechowuje tę konfigurację per agent w `~/.openclaw/agents/<agentId>/`. **Wiązanie** mapuje konto kanału (np. workspace Slack albo numer WhatsApp) na jednego z tych agentów.

## Czym jest „jeden agent”?

**Agent** to w pełni wydzielony mózg z własnymi:

  * **Workspace** (pliki, [AGENTS.md/SOUL.md/USER.md](<http://AGENTS.md/SOUL.md/USER.md>), notatki lokalne, reguły persony).
  * **Katalogiem stanu** (`agentDir`) na profile uwierzytelniania, rejestr modeli i konfigurację per agent.
  * **Magazynem sesji** (historia czatu + stan routingu) pod `~/.openclaw/agents/<agentId>/sessions`.


Profile uwierzytelniania są **per agent**. Każdy agent czyta z własnego:

textCopy code
[code]
    ~/.openclaw/agents/<agentId>/agent/auth-profiles.json
[/code]

Skills są ładowane z workspace każdego agenta oraz współdzielonych katalogów głównych, takich jak `~/.openclaw/skills`, a następnie filtrowane według efektywnej listy dozwolonych Skills agenta, gdy jest skonfigurowana. Użyj `agents.defaults.skills` jako współdzielonej bazy i `agents.list[].skills` jako zamiany per agent. Zobacz [Skills: per agent a współdzielone](</pl/tools/skills#per-agent-vs-shared-skills>) oraz [Skills: listy dozwolonych Skills agenta](</pl/tools/skills#agent-skill-allowlists>).

Gateway może hostować **jednego agenta** (domyślnie) albo **wielu agentów** obok siebie.

## Ścieżki (szybka mapa)

  * Konfiguracja: `~/.openclaw/openclaw.json` (albo `OPENCLAW_CONFIG_PATH`)
  * Katalog stanu: `~/.openclaw` (albo `OPENCLAW_STATE_DIR`)
  * Workspace: `~/.openclaw/workspace` (albo `~/.openclaw/workspace-<agentId>`)
  * Katalog agenta: `~/.openclaw/agents/<agentId>/agent` (albo `agents.list[].agentDir`)
  * Sesje: `~/.openclaw/agents/<agentId>/sessions`


### Tryb pojedynczego agenta (domyślny)

Jeśli nic nie zrobisz, OpenClaw uruchamia jednego agenta:

  * `agentId` domyślnie ma wartość **`main`**.
  * Sesje są kluczowane jako `agent:main:<mainKey>`.
  * Workspace domyślnie ma wartość `~/.openclaw/workspace` (albo `~/.openclaw/workspace-<profile>`, gdy ustawiono `OPENCLAW_PROFILE`).
  * Stan domyślnie ma wartość `~/.openclaw/agents/main/agent`.


## Pomocnik agenta

Użyj kreatora agentów, aby dodać nowego izolowanego agenta:

bashCopy code
[code]
    openclaw agents add work
[/code]

Następnie dodaj `bindings` (albo pozwól kreatorowi to zrobić), aby kierować wiadomości przychodzące.

Zweryfikuj za pomocą:

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

## Szybki start

* ### Utwórz workspace każdego agenta

Użyj kreatora albo utwórz workspace ręcznie:

bashCopy code
[code]
    openclaw agents add codingopenclaw agents add social
[/code]

Każdy agent otrzymuje własny workspace z `SOUL.md`, `AGENTS.md` i opcjonalnym `USER.md`, a także dedykowany `agentDir` oraz magazyn sesji pod `~/.openclaw/agents/<agentId>`.

* ### Utwórz konta kanałów

Utwórz po jednym koncie per agent w preferowanych kanałach:

  * Discord: jeden bot per agent, włącz Message Content Intent, skopiuj każdy token.
  * Telegram: jeden bot per agent przez BotFather, skopiuj każdy token.
  * WhatsApp: połącz każdy numer telefonu per konto.

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account work
[/code]

Zobacz przewodniki po kanałach: [Discord](</pl/channels/discord>), [Telegram](</pl/channels/telegram>), [WhatsApp](</pl/channels/whatsapp>).

* ### Dodaj agentów, konta i wiązania

Dodaj agentów pod `agents.list`, konta kanałów pod `channels.<channel>.accounts` i połącz je za pomocą `bindings` (przykłady poniżej).

* ### Uruchom ponownie i zweryfikuj

bashCopy code
[code]
    openclaw gateway restartopenclaw agents list --bindingsopenclaw channels status --probe
[/code]

## Wielu agentów = wiele osób, wiele osobowości

Przy **wielu agentach** każdy `agentId` staje się **w pełni izolowaną personą** :

  * **Różne numery telefonu/konta** (per kanał `accountId`).
  * **Różne osobowości** (pliki workspace per agent, takie jak `AGENTS.md` i `SOUL.md`).
  * **Oddzielne uwierzytelnianie + sesje** (bez komunikacji między nimi, chyba że zostanie jawnie włączona).


Pozwala to **wielu osobom** współdzielić jeden serwer Gateway przy zachowaniu izolacji ich „mózgów” AI i danych.

## Wyszukiwanie pamięci QMD między agentami

Jeśli jeden agent powinien przeszukiwać transkrypcje sesji QMD innego agenta, dodaj dodatkowe kolekcje pod `agents.list[].memorySearch.qmd.extraCollections`. Używaj `agents.defaults.memorySearch.qmd.extraCollections` tylko wtedy, gdy każdy agent powinien dziedziczyć te same współdzielone kolekcje transkrypcji.

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/workspaces/main",      memorySearch: {        qmd: {          extraCollections: [{ path: "~/agents/family/sessions", name: "family-sessions" }],        },      },    },    list: [      {        id: "main",        workspace: "~/workspaces/main",        memorySearch: {          qmd: {            extraCollections: [{ path: "notes" }], // resolves inside workspace -> collection named "notes-main"          },        },      },      { id: "family", workspace: "~/workspaces/family" },    ],  },  memory: {    backend: "qmd",    qmd: { includeDefaultMemory: false },  },}
[/code]

Ścieżka dodatkowej kolekcji może być współdzielona między agentami, ale nazwa kolekcji pozostaje jawna, gdy ścieżka znajduje się poza workspace agenta. Ścieżki wewnątrz workspace pozostają ograniczone do agenta, więc każdy agent zachowuje własny zestaw wyszukiwania transkrypcji.

## Jeden numer WhatsApp, wiele osób (podział DM)

Możesz kierować **różne DM WhatsApp** do różnych agentów, pozostając przy **jednym koncie WhatsApp**. Dopasuj nadawcę E.164 (np. `+15551234567`) za pomocą `peer.kind: "direct"`. Odpowiedzi nadal przychodzą z tego samego numeru WhatsApp (brak tożsamości nadawcy per agent).

Przykład:

json5Copy code
[code]
    {  agents: {    list: [      { id: "alex", workspace: "~/.openclaw/workspace-alex" },      { id: "mia", workspace: "~/.openclaw/workspace-mia" },    ],  },  bindings: [    {      agentId: "alex",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230001" } },    },    {      agentId: "mia",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230002" } },    },  ],  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551230001", "+15551230002"],    },  },}
[/code]

Uwagi:

  * Kontrola dostępu DM jest **globalna per konto WhatsApp** (parowanie/lista dozwolonych), a nie per agent.
  * W przypadku współdzielonych grup powiąż grupę z jednym agentem albo użyj [grup broadcast](</pl/channels/broadcast-groups>).


## Reguły routingu (jak wiadomości wybierają agenta)

Wiązania są **deterministyczne** i wygrywa **najbardziej szczegółowe** :

* ### Dopasowanie peer

Dokładny identyfikator DM/grupy/kanału.

* ### Dopasowanie parentPeer

Dziedziczenie wątku.

* ### guildId + role

Routing według ról Discord.

* ### guildId

Discord.

* ### teamId

Slack.

* ### Dopasowanie accountId dla kanału

Rezerwowa obsługa per konto.

* ### Dopasowanie na poziomie kanału

`accountId: "*"`.

* ### Agent domyślny

Rezerwowo `agents.list[].default`, w przeciwnym razie pierwszy wpis listy, domyślnie: `main`.

Rozstrzyganie remisów i semantyka AND

  * Jeśli w tej samej warstwie pasuje wiele wiązań, wygrywa pierwsze w kolejności konfiguracji.
  * Jeśli wiązanie ustawia wiele pól dopasowania (na przykład `peer` \+ `guildId`), wymagane są wszystkie określone pola (semantyka `AND`).

Szczegóły zakresu konta

  * Wiązanie, które pomija `accountId`, pasuje tylko do konta domyślnego.
  * Użyj `accountId: "*"`, aby uzyskać rezerwową obsługę całego kanału dla wszystkich kont.
  * Jeśli później dodasz takie samo wiązanie dla tego samego agenta z jawnym identyfikatorem konta, OpenClaw ulepszy istniejące wiązanie wyłącznie kanałowe do zakresu konta zamiast je duplikować.


## Wiele kont / numerów telefonu

Kanały obsługujące **wiele kont** (np. WhatsApp) używają `accountId` do identyfikacji każdego logowania. Każde `accountId` może być kierowane do innego agenta, więc jeden serwer może hostować wiele numerów telefonu bez mieszania sesji.

Jeśli chcesz domyślne konto dla całego kanału, gdy `accountId` jest pominięte, ustaw `channels.<channel>.defaultAccount` (opcjonalnie). Gdy nie jest ustawione, OpenClaw wraca do `default`, jeśli istnieje, w przeciwnym razie do pierwszego skonfigurowanego identyfikatora konta (posortowanego).

Typowe kanały obsługujące ten wzorzec obejmują:

  * `whatsapp`, `telegram`, `discord`, `slack`, `signal`, `imessage`
  * `irc`, `line`, `googlechat`, `mattermost`, `matrix`, `nextcloud-talk`
  * `zalo`, `zalouser`, `nostr`, `feishu`


## Koncepcje

  * `agentId`: jeden „mózg” (workspace, uwierzytelnianie per agent, magazyn sesji per agent).
  * `accountId`: jedna instancja konta kanału (np. konto WhatsApp `"personal"` kontra `"biz"`).
  * `binding`: kieruje wiadomości przychodzące do `agentId` według `(channel, accountId, peer)` oraz opcjonalnie identyfikatorów gildii/zespołu.
  * Czaty bezpośrednie zwijają się do `agent:<agentId>:<mainKey>` („main” per agent; `session.mainKey`).


## Przykłady platform

Boty Discord per agent

Każde konto bota Discord mapuje się na unikatowy `accountId`. Powiąż każde konto z agentem i utrzymuj listy dozwolonych per bot.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "coding", workspace: "~/.openclaw/workspace-coding" },    ],  },  bindings: [    { agentId: "main", match: { channel: "discord", accountId: "default" } },    { agentId: "coding", match: { channel: "discord", accountId: "coding" } },  ],  channels: {    discord: {      groupPolicy: "allowlist",      accounts: {        default: {          token: "DISCORD_BOT_TOKEN_MAIN",          guilds: {            "123456789012345678": {              channels: {                "222222222222222222": { allow: true, requireMention: false },              },            },          },        },        coding: {          token: "DISCORD_BOT_TOKEN_CODING",          guilds: {            "123456789012345678": {              channels: {                "333333333333333333": { allow: true, requireMention: false },              },            },          },        },      },    },  },}
[/code]

  * Zaproś każdego bota do serwera i włącz Message Content Intent.
  * Tokeny znajdują się w `channels.discord.accounts.<id>.token` (konto domyślne może używać `DISCORD_BOT_TOKEN`).

Boty Telegrama dla poszczególnych agentów json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "alerts", workspace: "~/.openclaw/workspace-alerts" },    ],  },  bindings: [    { agentId: "main", match: { channel: "telegram", accountId: "default" } },    { agentId: "alerts", match: { channel: "telegram", accountId: "alerts" } },  ],  channels: {    telegram: {      accounts: {        default: {          botToken: "123456:ABC...",          dmPolicy: "pairing",        },        alerts: {          botToken: "987654:XYZ...",          dmPolicy: "allowlist",          allowFrom: ["tg:123456789"],        },      },    },  },}
[/code]

  * Utwórz po jednym bocie dla każdego agenta za pomocą BotFather i skopiuj każdy token.
  * Tokeny znajdują się w `channels.telegram.accounts.<id>.botToken` (konto domyślne może używać `TELEGRAM_BOT_TOKEN`).

Numery WhatsApp dla poszczególnych agentów

Połącz każde konto przed uruchomieniem Gateway:

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account personalopenclaw channels login --channel whatsapp --account biz
[/code]

`~/.openclaw/openclaw.json` (JSON5):

jsCopy code
[code]
    {  agents: {    list: [      {        id: "home",        default: true,        name: "Home",        workspace: "~/.openclaw/workspace-home",        agentDir: "~/.openclaw/agents/home/agent",      },      {        id: "work",        name: "Work",        workspace: "~/.openclaw/workspace-work",        agentDir: "~/.openclaw/agents/work/agent",      },    ],  },   // Deterministic routing: first match wins (most-specific first).  bindings: [    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },     // Optional per-peer override (example: send a specific group to work agent).    {      agentId: "work",      match: {        channel: "whatsapp",        accountId: "personal",        peer: { kind: "group", id: "1203630...@g.us" },      },    },  ],   // Off by default: agent-to-agent messaging must be explicitly enabled + allowlisted.  tools: {    agentToAgent: {      enabled: false,      allow: ["home", "work"],    },  },   channels: {    whatsapp: {      accounts: {        personal: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/personal          // authDir: "~/.openclaw/credentials/whatsapp/personal",        },        biz: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/biz          // authDir: "~/.openclaw/credentials/whatsapp/biz",        },      },    },  },}
[/code]

## Typowe wzorce

### Codzienna obsługa WhatsApp + głęboka praca w Telegramie

Podziel według kanału: kieruj WhatsApp do szybkiego agenta codziennego użytku, a Telegram do agenta Opus.

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    { agentId: "chat", match: { channel: "whatsapp" } },    { agentId: "opus", match: { channel: "telegram" } },  ],}
[/code]

Uwagi:

  * Jeśli masz wiele kont dla kanału, dodaj `accountId` do powiązania (na przykład `{ channel: "whatsapp", accountId: "personal" }`).
  * Aby skierować pojedynczą wiadomość DM/grupę do Opus, pozostawiając resztę na czacie, dodaj powiązanie `match.peer` dla tego peera; dopasowania peerów zawsze wygrywają z regułami obejmującymi cały kanał.


### Ten sam kanał, jeden peer do Opus

Pozostaw WhatsApp na szybkim agencie, ale skieruj jedną wiadomość DM do Opus:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    {      agentId: "opus",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } },    },    { agentId: "chat", match: { channel: "whatsapp" } },  ],}
[/code]

Powiązania peerów zawsze wygrywają, więc umieść je nad regułą obejmującą cały kanał.

### Agent rodzinny powiązany z grupą WhatsApp

Powiąż dedykowanego agenta rodzinnego z jedną grupą WhatsApp, z bramkowaniem przez wzmianki i ściślejszą polityką narzędzi:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "family",        name: "Family",        workspace: "~/.openclaw/workspace-family",        identity: { name: "Family Bot" },        groupChat: {          mentionPatterns: ["@family", "@familybot", "@Family Bot"],        },        sandbox: {          mode: "all",          scope: "agent",        },        tools: {          allow: [            "exec",            "read",            "sessions_list",            "sessions_history",            "sessions_send",            "sessions_spawn",            "session_status",          ],          deny: ["write", "edit", "apply_patch", "browser", "canvas", "nodes", "cron"],        },      },    ],  },  bindings: [    {      agentId: "family",      match: {        channel: "whatsapp",        peer: { kind: "group", id: "120363999999999999@g.us" },      },    },  ],}
[/code]

Uwagi:

  * Listy dozwolonych/zabronionych narzędzi są **narzędziami** , a nie Skills. Jeśli skill musi uruchomić plik binarny, upewnij się, że `exec` jest dozwolone, a plik binarny istnieje w piaskownicy.
  * Aby uzyskać ściślejsze bramkowanie, ustaw `agents.list[].groupChat.mentionPatterns` i pozostaw włączone listy dozwolonych grup dla kanału.


## Konfiguracja piaskownicy i narzędzi dla poszczególnych agentów

Każdy agent może mieć własne ograniczenia piaskownicy i narzędzi:

jsCopy code
[code]
    {  agents: {    list: [      {        id: "personal",        workspace: "~/.openclaw/workspace-personal",        sandbox: {          mode: "off",  // No sandbox for personal agent        },        // No tool restrictions - all tools available      },      {        id: "family",        workspace: "~/.openclaw/workspace-family",        sandbox: {          mode: "all",     // Always sandboxed          scope: "agent",  // One container per agent          docker: {            // Optional one-time setup after container creation            setupCommand: "apt-get update && apt-get install -y git curl",          },        },        tools: {          allow: ["read"],                    // Only read tool          deny: ["exec", "write", "edit", "apply_patch"],    // Deny others        },      },    ],  },}
[/code]

**Korzyści:**

  * **Izolacja bezpieczeństwa** : ogranicz narzędzia dla niezaufanych agentów.
  * **Kontrola zasobów** : uruchamiaj określonych agentów w piaskownicy, pozostawiając innych na hoście.
  * **Elastyczne polityki** : różne uprawnienia dla poszczególnych agentów.


Zobacz [Piaskownica i narzędzia dla wielu agentów](</pl/tools/multi-agent-sandbox-tools>), aby uzyskać szczegółowe przykłady.

## Powiązane

  * [Agenci ACP](</pl/tools/acp-agents>) — uruchamianie zewnętrznych harnessów kodujących
  * [Routing kanałów](</pl/channels/channel-routing>) — jak wiadomości są kierowane do agentów
  * [Obecność](</pl/concepts/presence>) — obecność i dostępność agenta
  * [Sesja](</pl/concepts/session>) — izolacja i routing sesji
  * [Podagenci](</pl/tools/subagents>) — uruchamianie agentów działających w tle


Was this useful?YesNo