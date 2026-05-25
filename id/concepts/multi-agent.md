---
title: Perutean multi-agen
source_url: https://docs.openclaw.ai/id/concepts/multi-agent
scraped_at: 2026-05-25
---

Jalankan beberapa agen _terisolasi_ — masing-masing dengan workspace, direktori state (`agentDir`), dan riwayat sesi sendiri — plus beberapa akun kanal (misalnya dua WhatsApp) dalam satu Gateway yang berjalan. Pesan masuk dirutekan ke agen yang tepat melalui binding.

Sebuah **agen** di sini adalah cakupan penuh per persona: file workspace, profil autentikasi, registri model, dan penyimpanan sesi. `agentDir` adalah direktori state di disk yang menyimpan konfigurasi per agen ini di `~/.openclaw/agents/<agentId>/`. Sebuah **binding** memetakan akun kanal (misalnya workspace Slack atau nomor WhatsApp) ke salah satu agen tersebut.

## Apa itu "satu agen"?

Sebuah **agen** adalah otak dengan cakupan penuh yang memiliki:

  * **Workspace** (file, [AGENTS.md/SOUL.md/USER.md](<http://AGENTS.md/SOUL.md/USER.md>), catatan lokal, aturan persona).
  * **Direktori state** (`agentDir`) untuk profil autentikasi, registri model, dan konfigurasi per agen.
  * **Penyimpanan sesi** (riwayat chat + state perutean) di bawah `~/.openclaw/agents/<agentId>/sessions`.


Profil autentikasi bersifat **per agen**. Setiap agen membaca dari miliknya sendiri:

textCopy code
[code]
    ~/.openclaw/agents/<agentId>/agent/auth-profiles.json
[/code]

Skills dimuat dari setiap workspace agen plus root bersama seperti `~/.openclaw/skills`, lalu difilter berdasarkan allowlist skill agen efektif saat dikonfigurasi. Gunakan `agents.defaults.skills` untuk baseline bersama dan `agents.list[].skills` untuk penggantian per agen. Lihat [Skills: per agen vs bersama](</id/tools/skills#per-agent-vs-shared-skills>) dan [Skills: allowlist skill agen](</id/tools/skills#agent-skill-allowlists>).

Gateway dapat menghosting **satu agen** (default) atau **banyak agen** berdampingan.

## Path (peta cepat)

  * Konfigurasi: `~/.openclaw/openclaw.json` (atau `OPENCLAW_CONFIG_PATH`)
  * Direktori state: `~/.openclaw` (atau `OPENCLAW_STATE_DIR`)
  * Workspace: `~/.openclaw/workspace` (atau `~/.openclaw/workspace-<agentId>`)
  * Direktori agen: `~/.openclaw/agents/<agentId>/agent` (atau `agents.list[].agentDir`)
  * Sesi: `~/.openclaw/agents/<agentId>/sessions`


### Mode satu agen (default)

Jika Anda tidak melakukan apa pun, OpenClaw menjalankan satu agen:

  * `agentId` default ke **`main`**.
  * Sesi diberi key sebagai `agent:main:<mainKey>`.
  * Workspace default ke `~/.openclaw/workspace` (atau `~/.openclaw/workspace-<profile>` saat `OPENCLAW_PROFILE` disetel).
  * State default ke `~/.openclaw/agents/main/agent`.


## Pembantu agen

Gunakan wizard agen untuk menambahkan agen terisolasi baru:

bashCopy code
[code]
    openclaw agents add work
[/code]

Lalu tambahkan `bindings` (atau biarkan wizard melakukannya) untuk merutekan pesan masuk.

Verifikasi dengan:

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

## Mulai cepat

* ### Buat setiap workspace agen

Gunakan wizard atau buat workspace secara manual:

bashCopy code
[code]
    openclaw agents add codingopenclaw agents add social
[/code]

Setiap agen mendapatkan workspace sendiri dengan `SOUL.md`, `AGENTS.md`, dan `USER.md` opsional, plus `agentDir` khusus dan penyimpanan sesi di bawah `~/.openclaw/agents/<agentId>`.

* ### Buat akun kanal

Buat satu akun per agen pada kanal pilihan Anda:

  * Discord: satu bot per agen, aktifkan Message Content Intent, salin setiap token.
  * Telegram: satu bot per agen melalui BotFather, salin setiap token.
  * WhatsApp: tautkan setiap nomor telepon per akun.

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account work
[/code]

Lihat panduan kanal: [Discord](</id/channels/discord>), [Telegram](</id/channels/telegram>), [WhatsApp](</id/channels/whatsapp>).

* ### Tambahkan agen, akun, dan binding

Tambahkan agen di bawah `agents.list`, akun kanal di bawah `channels.<channel>.accounts`, dan hubungkan keduanya dengan `bindings` (contoh di bawah).

* ### Mulai ulang dan verifikasi

bashCopy code
[code]
    openclaw gateway restartopenclaw agents list --bindingsopenclaw channels status --probe
[/code]

## Beberapa agen = beberapa orang, beberapa kepribadian

Dengan **beberapa agen** , setiap `agentId` menjadi **persona yang sepenuhnya terisolasi** :

  * **Nomor telepon/akun berbeda** (per kanal `accountId`).
  * **Kepribadian berbeda** (file workspace per agen seperti `AGENTS.md` dan `SOUL.md`).
  * **Autentikasi + sesi terpisah** (tidak ada percakapan silang kecuali diaktifkan secara eksplisit).


Ini memungkinkan **beberapa orang** berbagi satu server Gateway sambil menjaga "otak" AI dan data mereka tetap terisolasi.

## Pencarian memori QMD lintas agen

Jika satu agen harus mencari transkrip sesi QMD agen lain, tambahkan koleksi ekstra di bawah `agents.list[].memorySearch.qmd.extraCollections`. Gunakan `agents.defaults.memorySearch.qmd.extraCollections` hanya saat setiap agen harus mewarisi koleksi transkrip bersama yang sama.

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/workspaces/main",      memorySearch: {        qmd: {          extraCollections: [{ path: "~/agents/family/sessions", name: "family-sessions" }],        },      },    },    list: [      {        id: "main",        workspace: "~/workspaces/main",        memorySearch: {          qmd: {            extraCollections: [{ path: "notes" }], // resolves inside workspace -> collection named "notes-main"          },        },      },      { id: "family", workspace: "~/workspaces/family" },    ],  },  memory: {    backend: "qmd",    qmd: { includeDefaultMemory: false },  },}
[/code]

Path koleksi ekstra dapat dibagikan antar agen, tetapi nama koleksi tetap eksplisit saat path berada di luar workspace agen. Path di dalam workspace tetap bercakupan agen sehingga setiap agen mempertahankan set pencarian transkripnya sendiri.

## Satu nomor WhatsApp, beberapa orang (pemisahan DM)

Anda dapat merutekan **DM WhatsApp yang berbeda** ke agen yang berbeda sambil tetap berada pada **satu akun WhatsApp**. Cocokkan berdasarkan pengirim E.164 (seperti `+15551234567`) dengan `peer.kind: "direct"`. Balasan tetap berasal dari nomor WhatsApp yang sama (tidak ada identitas pengirim per agen).

Contoh:

json5Copy code
[code]
    {  agents: {    list: [      { id: "alex", workspace: "~/.openclaw/workspace-alex" },      { id: "mia", workspace: "~/.openclaw/workspace-mia" },    ],  },  bindings: [    {      agentId: "alex",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230001" } },    },    {      agentId: "mia",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230002" } },    },  ],  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551230001", "+15551230002"],    },  },}
[/code]

Catatan:

  * Kontrol akses DM bersifat **global per akun WhatsApp** (pairing/allowlist), bukan per agen.
  * Untuk grup bersama, bind grup ke satu agen atau gunakan [Grup broadcast](</id/channels/broadcast-groups>).


## Aturan perutean (bagaimana pesan memilih agen)

Binding bersifat **deterministik** dan **yang paling spesifik menang** :

* ### kecocokan peer

ID DM/grup/kanal persis.

* ### kecocokan parentPeer

Pewarisan thread.

* ### guildId + roles

Perutean role Discord.

* ### guildId

Discord.

* ### teamId

Slack.

* ### kecocokan accountId untuk kanal

Fallback per akun.

* ### Kecocokan tingkat kanal

`accountId: "*"`.

* ### Agen default

Fallback ke `agents.list[].default`, jika tidak ada entri daftar pertama, default: `main`.

Pemecahan seri dan semantik AND

  * Jika beberapa binding cocok pada tingkat yang sama, yang pertama dalam urutan konfigurasi menang.
  * Jika binding menetapkan beberapa field kecocokan (misalnya `peer` \+ `guildId`), semua field yang ditentukan diperlukan (semantik `AND`).

Detail cakupan akun

  * Binding yang menghilangkan `accountId` hanya cocok dengan akun default.
  * Gunakan `accountId: "*"` untuk fallback seluruh kanal di semua akun.
  * Jika nanti Anda menambahkan binding yang sama untuk agen yang sama dengan id akun eksplisit, OpenClaw meningkatkan binding khusus kanal yang ada menjadi bercakupan akun alih-alih menduplikasinya.


## Beberapa akun / nomor telepon

Kanal yang mendukung **beberapa akun** (misalnya WhatsApp) menggunakan `accountId` untuk mengidentifikasi setiap login. Setiap `accountId` dapat dirutekan ke agen yang berbeda, sehingga satu server dapat menghosting beberapa nomor telepon tanpa mencampur sesi.

Jika Anda menginginkan akun default seluruh kanal saat `accountId` dihilangkan, setel `channels.<channel>.defaultAccount` (opsional). Saat tidak disetel, OpenClaw fallback ke `default` jika ada, jika tidak ke id akun terkonfigurasi pertama (diurutkan).

Kanal umum yang mendukung pola ini meliputi:

  * `whatsapp`, `telegram`, `discord`, `slack`, `signal`, `imessage`
  * `irc`, `line`, `googlechat`, `mattermost`, `matrix`, `nextcloud-talk`
  * `zalo`, `zalouser`, `nostr`, `feishu`


## Konsep

  * `agentId`: satu "otak" (workspace, autentikasi per agen, penyimpanan sesi per agen).
  * `accountId`: satu instance akun kanal (misalnya akun WhatsApp `"personal"` vs `"biz"`).
  * `binding`: merutekan pesan masuk ke `agentId` berdasarkan `(channel, accountId, peer)` dan secara opsional id guild/team.
  * Chat langsung diciutkan ke `agent:<agentId>:<mainKey>` ("main" per agen; `session.mainKey`).


## Contoh platform

Bot Discord per agen

Setiap akun bot Discord dipetakan ke `accountId` unik. Bind setiap akun ke agen dan pertahankan allowlist per bot.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "coding", workspace: "~/.openclaw/workspace-coding" },    ],  },  bindings: [    { agentId: "main", match: { channel: "discord", accountId: "default" } },    { agentId: "coding", match: { channel: "discord", accountId: "coding" } },  ],  channels: {    discord: {      groupPolicy: "allowlist",      accounts: {        default: {          token: "DISCORD_BOT_TOKEN_MAIN",          guilds: {            "123456789012345678": {              channels: {                "222222222222222222": { allow: true, requireMention: false },              },            },          },        },        coding: {          token: "DISCORD_BOT_TOKEN_CODING",          guilds: {            "123456789012345678": {              channels: {                "333333333333333333": { allow: true, requireMention: false },              },            },          },        },      },    },  },}
[/code]

  * Undang setiap bot ke guild dan aktifkan Message Content Intent.
  * Token berada di `channels.discord.accounts.<id>.token` (akun default dapat menggunakan `DISCORD_BOT_TOKEN`).

Bot Telegram per agen json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "alerts", workspace: "~/.openclaw/workspace-alerts" },    ],  },  bindings: [    { agentId: "main", match: { channel: "telegram", accountId: "default" } },    { agentId: "alerts", match: { channel: "telegram", accountId: "alerts" } },  ],  channels: {    telegram: {      accounts: {        default: {          botToken: "123456:ABC...",          dmPolicy: "pairing",        },        alerts: {          botToken: "987654:XYZ...",          dmPolicy: "allowlist",          allowFrom: ["tg:123456789"],        },      },    },  },}
[/code]

  * Buat satu bot per agen dengan BotFather dan salin setiap token.
  * Token berada di `channels.telegram.accounts.<id>.botToken` (akun default dapat menggunakan `TELEGRAM_BOT_TOKEN`).

Nomor WhatsApp per agen

Tautkan setiap akun sebelum memulai Gateway:

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account personalopenclaw channels login --channel whatsapp --account biz
[/code]

`~/.openclaw/openclaw.json` (JSON5):

jsCopy code
[code]
    {  agents: {    list: [      {        id: "home",        default: true,        name: "Home",        workspace: "~/.openclaw/workspace-home",        agentDir: "~/.openclaw/agents/home/agent",      },      {        id: "work",        name: "Work",        workspace: "~/.openclaw/workspace-work",        agentDir: "~/.openclaw/agents/work/agent",      },    ],  },   // Deterministic routing: first match wins (most-specific first).  bindings: [    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },     // Optional per-peer override (example: send a specific group to work agent).    {      agentId: "work",      match: {        channel: "whatsapp",        accountId: "personal",        peer: { kind: "group", id: "1203630...@g.us" },      },    },  ],   // Off by default: agent-to-agent messaging must be explicitly enabled + allowlisted.  tools: {    agentToAgent: {      enabled: false,      allow: ["home", "work"],    },  },   channels: {    whatsapp: {      accounts: {        personal: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/personal          // authDir: "~/.openclaw/credentials/whatsapp/personal",        },        biz: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/biz          // authDir: "~/.openclaw/credentials/whatsapp/biz",        },      },    },  },}
[/code]

## Pola umum

### WhatsApp harian + kerja mendalam Telegram

Bagi berdasarkan kanal: arahkan WhatsApp ke agen harian yang cepat dan Telegram ke agen Opus.

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    { agentId: "chat", match: { channel: "whatsapp" } },    { agentId: "opus", match: { channel: "telegram" } },  ],}
[/code]

Catatan:

  * Jika Anda memiliki beberapa akun untuk satu kanal, tambahkan `accountId` ke binding (misalnya `{ channel: "whatsapp", accountId: "personal" }`).
  * Untuk mengarahkan satu DM/grup ke Opus sambil menjaga sisanya tetap di chat, tambahkan binding `match.peer` untuk peer tersebut; kecocokan peer selalu menang atas aturan seluruh kanal.


### Kanal yang sama, satu peer ke Opus

Pertahankan WhatsApp pada agen cepat, tetapi arahkan satu DM ke Opus:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    {      agentId: "opus",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } },    },    { agentId: "chat", match: { channel: "whatsapp" } },  ],}
[/code]

Binding peer selalu menang, jadi letakkan di atas aturan seluruh kanal.

### Agen keluarga yang diikat ke grup WhatsApp

Ikat agen keluarga khusus ke satu grup WhatsApp, dengan gating mention dan kebijakan tool yang lebih ketat:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "family",        name: "Family",        workspace: "~/.openclaw/workspace-family",        identity: { name: "Family Bot" },        groupChat: {          mentionPatterns: ["@family", "@familybot", "@Family Bot"],        },        sandbox: {          mode: "all",          scope: "agent",        },        tools: {          allow: [            "exec",            "read",            "sessions_list",            "sessions_history",            "sessions_send",            "sessions_spawn",            "session_status",          ],          deny: ["write", "edit", "apply_patch", "browser", "canvas", "nodes", "cron"],        },      },    ],  },  bindings: [    {      agentId: "family",      match: {        channel: "whatsapp",        peer: { kind: "group", id: "120363999999999999@g.us" },      },    },  ],}
[/code]

Catatan:

  * Daftar allow/deny tool adalah **tool** , bukan skills. Jika sebuah skill perlu menjalankan binary, pastikan `exec` diizinkan dan binary ada di sandbox.
  * Untuk gating yang lebih ketat, atur `agents.list[].groupChat.mentionPatterns` dan tetap aktifkan allowlist grup untuk kanal tersebut.


## Konfigurasi sandbox dan tool per agen

Setiap agen dapat memiliki sandbox dan pembatasan tool sendiri:

jsCopy code
[code]
    {  agents: {    list: [      {        id: "personal",        workspace: "~/.openclaw/workspace-personal",        sandbox: {          mode: "off",  // No sandbox for personal agent        },        // No tool restrictions - all tools available      },      {        id: "family",        workspace: "~/.openclaw/workspace-family",        sandbox: {          mode: "all",     // Always sandboxed          scope: "agent",  // One container per agent          docker: {            // Optional one-time setup after container creation            setupCommand: "apt-get update && apt-get install -y git curl",          },        },        tools: {          allow: ["read"],                    // Only read tool          deny: ["exec", "write", "edit", "apply_patch"],    // Deny others        },      },    ],  },}
[/code]

**Manfaat:**

  * **Isolasi keamanan** : batasi tool untuk agen yang tidak tepercaya.
  * **Kontrol sumber daya** : sandbox-kan agen tertentu sambil tetap menjalankan yang lain di host.
  * **Kebijakan fleksibel** : izin berbeda per agen.


Lihat [Sandbox dan tool multi-agen](</id/tools/multi-agent-sandbox-tools>) untuk contoh terperinci.

## Terkait

  * [Agen ACP](</id/tools/acp-agents>) — menjalankan harness pengodean eksternal
  * [Perutean kanal](</id/channels/channel-routing>) — cara pesan dirutekan ke agen
  * [Presence](</id/concepts/presence>) — presence dan ketersediaan agen
  * [Session](</id/concepts/session>) — isolasi dan perutean session
  * [Sub-agen](</id/tools/subagents>) — memulai proses agen latar belakang


Was this useful?YesNo