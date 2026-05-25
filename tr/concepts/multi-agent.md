---
title: Çoklu ajan yönlendirmesi
source_url: https://docs.openclaw.ai/tr/concepts/multi-agent
scraped_at: 2026-05-25
---

Bir çalışan Gateway içinde birden çok _yalıtılmış_ ajan çalıştırın — her biri kendi çalışma alanı, durum dizini (`agentDir`) ve oturum geçmişiyle — ayrıca birden çok kanal hesabı (ör. iki WhatsApp) kullanın. Gelen iletiler bağlamalar üzerinden doğru ajana yönlendirilir.

Buradaki **ajan** , kişi başına tam kapsamdır: çalışma alanı dosyaları, kimlik doğrulama profilleri, model kayıt defteri ve oturum deposu. `agentDir`, bu ajan başına yapılandırmayı `~/.openclaw/agents/<agentId>/` konumunda tutan disk üzerindeki durum dizinidir. **Bağlama** , bir kanal hesabını (ör. bir Slack çalışma alanı veya bir WhatsApp numarası) bu ajanlardan birine eşler.

## "Tek ajan" nedir?

Bir **ajan** , kendine ait tam kapsamlı bir beyindir:

  * **Çalışma alanı** (dosyalar, [AGENTS.md/SOUL.md/USER.md](<http://AGENTS.md/SOUL.md/USER.md>), yerel notlar, persona kuralları).
  * Kimlik doğrulama profilleri, model kayıt defteri ve ajan başına yapılandırma için **durum dizini** (`agentDir`).
  * `~/.openclaw/agents/<agentId>/sessions` altında **oturum deposu** (sohbet geçmişi + yönlendirme durumu).


Kimlik doğrulama profilleri **ajan başınadır**. Her ajan kendi şuradan okur:

textCopy code
[code]
    ~/.openclaw/agents/<agentId>/agent/auth-profiles.json
[/code]

Skills, her ajan çalışma alanından ve `~/.openclaw/skills` gibi paylaşılan köklerden yüklenir, ardından yapılandırıldığında etkin ajan Skills izin listesine göre filtrelenir. Paylaşılan bir temel için `agents.defaults.skills`, ajan başına değiştirme için `agents.list[].skills` kullanın. Bkz. [Skills: ajan başına ve paylaşılan](</tr/tools/skills#per-agent-vs-shared-skills>) ve [Skills: ajan Skills izin listeleri](</tr/tools/skills#agent-skill-allowlists>).

Gateway **tek ajanı** (varsayılan) veya **birçok ajanı** yan yana barındırabilir.

## Yollar (hızlı harita)

  * Yapılandırma: `~/.openclaw/openclaw.json` (veya `OPENCLAW_CONFIG_PATH`)
  * Durum dizini: `~/.openclaw` (veya `OPENCLAW_STATE_DIR`)
  * Çalışma alanı: `~/.openclaw/workspace` (veya `~/.openclaw/workspace-<agentId>`)
  * Ajan dizini: `~/.openclaw/agents/<agentId>/agent` (veya `agents.list[].agentDir`)
  * Oturumlar: `~/.openclaw/agents/<agentId>/sessions`


### Tek ajan modu (varsayılan)

Hiçbir şey yapmazsanız OpenClaw tek bir ajan çalıştırır:

  * `agentId` varsayılan olarak **`main`** olur.
  * Oturumlar `agent:main:<mainKey>` olarak anahtarlanır.
  * Çalışma alanı varsayılan olarak `~/.openclaw/workspace` olur (veya `OPENCLAW_PROFILE` ayarlandığında `~/.openclaw/workspace-<profile>`).
  * Durum varsayılan olarak `~/.openclaw/agents/main/agent` olur.


## Ajan yardımcısı

Yeni bir yalıtılmış ajan eklemek için ajan sihirbazını kullanın:

bashCopy code
[code]
    openclaw agents add work
[/code]

Ardından gelen iletileri yönlendirmek için `bindings` ekleyin (veya sihirbazın yapmasına izin verin).

Şununla doğrulayın:

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

## Hızlı başlangıç

* ### Her ajan çalışma alanını oluşturun

Sihirbazı kullanın veya çalışma alanlarını elle oluşturun:

bashCopy code
[code]
    openclaw agents add codingopenclaw agents add social
[/code]

Her ajan, `SOUL.md`, `AGENTS.md` ve isteğe bağlı `USER.md` içeren kendi çalışma alanını, ayrıca ayrılmış bir `agentDir` ve `~/.openclaw/agents/<agentId>` altında oturum deposunu alır.

* ### Kanal hesapları oluşturun

Tercih ettiğiniz kanallarda ajan başına bir hesap oluşturun:

  * Discord: ajan başına bir bot, Message Content Intent'i etkinleştirin, her tokenı kopyalayın.
  * Telegram: BotFather üzerinden ajan başına bir bot, her tokenı kopyalayın.
  * WhatsApp: hesap başına her telefon numarasını bağlayın.

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account work
[/code]

Kanal kılavuzlarına bakın: [Discord](</tr/channels/discord>), [Telegram](</tr/channels/telegram>), [WhatsApp](</tr/channels/whatsapp>).

* ### Ajanları, hesapları ve bağlamaları ekleyin

Ajanları `agents.list` altına, kanal hesaplarını `channels.<channel>.accounts` altına ekleyin ve bunları `bindings` ile bağlayın (örnekler aşağıda).

* ### Yeniden başlatın ve doğrulayın

bashCopy code
[code]
    openclaw gateway restartopenclaw agents list --bindingsopenclaw channels status --probe
[/code]

## Birden çok ajan = birden çok kişi, birden çok kişilik

**Birden çok ajan** ile her `agentId` **tamamen yalıtılmış bir persona** olur:

  * **Farklı telefon numaraları/hesaplar** (kanal başına `accountId`).
  * **Farklı kişilikler** (`AGENTS.md` ve `SOUL.md` gibi ajan başına çalışma alanı dosyaları).
  * **Ayrı kimlik doğrulama + oturumlar** (açıkça etkinleştirilmedikçe çapraz konuşma yok).


Bu, **birden çok kişinin** tek bir Gateway sunucusunu paylaşmasına, AI "beyinlerini" ve verilerini yalıtılmış tutmasına olanak tanır.

## Ajanlar arası QMD bellek araması

Bir ajanın başka bir ajanın QMD oturum dökümlerini araması gerekiyorsa `agents.list[].memorySearch.qmd.extraCollections` altına ek koleksiyonlar ekleyin. `agents.defaults.memorySearch.qmd.extraCollections` değerini yalnızca her ajanın aynı paylaşılan döküm koleksiyonlarını devralması gerektiğinde kullanın.

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/workspaces/main",      memorySearch: {        qmd: {          extraCollections: [{ path: "~/agents/family/sessions", name: "family-sessions" }],        },      },    },    list: [      {        id: "main",        workspace: "~/workspaces/main",        memorySearch: {          qmd: {            extraCollections: [{ path: "notes" }], // resolves inside workspace -> collection named "notes-main"          },        },      },      { id: "family", workspace: "~/workspaces/family" },    ],  },  memory: {    backend: "qmd",    qmd: { includeDefaultMemory: false },  },}
[/code]

Ek koleksiyon yolu ajanlar arasında paylaşılabilir, ancak yol ajan çalışma alanının dışındaysa koleksiyon adı açık kalır. Çalışma alanının içindeki yollar ajan kapsamlı kalır, böylece her ajan kendi döküm arama kümesini korur.

## Tek WhatsApp numarası, birden çok kişi (DM bölme)

**Tek bir WhatsApp hesabında** kalırken **farklı WhatsApp DM'lerini** farklı ajanlara yönlendirebilirsiniz. Gönderen E.164 (ör. `+15551234567`) üzerinde `peer.kind: "direct"` ile eşleştirin. Yanıtlar yine aynı WhatsApp numarasından gelir (ajan başına gönderen kimliği yoktur).

Örnek:

json5Copy code
[code]
    {  agents: {    list: [      { id: "alex", workspace: "~/.openclaw/workspace-alex" },      { id: "mia", workspace: "~/.openclaw/workspace-mia" },    ],  },  bindings: [    {      agentId: "alex",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230001" } },    },    {      agentId: "mia",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230002" } },    },  ],  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551230001", "+15551230002"],    },  },}
[/code]

Notlar:

  * DM erişim denetimi, ajan başına değil **WhatsApp hesabı başına geneldir** (eşleştirme/izin listesi).
  * Paylaşılan gruplar için grubu bir ajana bağlayın veya [Yayın grupları](</tr/channels/broadcast-groups>) kullanın.


## Yönlendirme kuralları (iletiler ajanı nasıl seçer)

Bağlamalar **deterministiktir** ve **en özgül olan kazanır** :

* ### peer eşleşmesi

Tam DM/grup/kanal kimliği.

* ### parentPeer eşleşmesi

Thread devralma.

* ### guildId + roller

Discord rol yönlendirmesi.

* ### guildId

Discord.

* ### teamId

Slack.

* ### Bir kanal için accountId eşleşmesi

Hesap başına geri dönüş.

* ### Kanal düzeyi eşleşme

`accountId: "*"`.

* ### Varsayılan ajan

`agents.list[].default` değerine, yoksa ilk liste girdisine geri dönüş; varsayılan: `main`.

Eşitlik bozma ve AND semantiği

  * Aynı katmanda birden çok bağlama eşleşirse yapılandırma sırasındaki ilk bağlama kazanır.
  * Bir bağlama birden çok eşleşme alanı ayarlarsa (örneğin `peer` \+ `guildId`), belirtilen tüm alanlar zorunludur (`AND` semantiği).

Hesap kapsamı ayrıntısı

  * `accountId` atlayan bir bağlama yalnızca varsayılan hesapla eşleşir.
  * Tüm hesaplar genelinde kanal çapında geri dönüş için `accountId: "*"` kullanın.
  * Daha sonra aynı ajan için aynı bağlamayı açık bir hesap kimliğiyle eklerseniz OpenClaw mevcut yalnızca kanal bağlamasını çoğaltmak yerine hesap kapsamlı hale yükseltir.


## Birden çok hesap / telefon numarası

**Birden çok hesabı** destekleyen kanallar (ör. WhatsApp), her oturumu tanımlamak için `accountId` kullanır. Her `accountId` farklı bir ajana yönlendirilebilir, böylece tek bir sunucu oturumları karıştırmadan birden çok telefon numarasını barındırabilir.

`accountId` atlandığında kanal çapında varsayılan bir hesap istiyorsanız `channels.<channel>.defaultAccount` ayarlayın (isteğe bağlı). Ayarlanmadığında OpenClaw varsa `default` değerine, yoksa ilk yapılandırılmış hesap kimliğine (sıralanmış) geri döner.

Bu deseni destekleyen yaygın kanallar şunları içerir:

  * `whatsapp`, `telegram`, `discord`, `slack`, `signal`, `imessage`
  * `irc`, `line`, `googlechat`, `mattermost`, `matrix`, `nextcloud-talk`
  * `zalo`, `zalouser`, `nostr`, `feishu`


## Kavramlar

  * `agentId`: tek bir "beyin" (çalışma alanı, ajan başına kimlik doğrulama, ajan başına oturum deposu).
  * `accountId`: tek bir kanal hesabı örneği (ör. WhatsApp hesabı `"personal"` ile `"biz"`).
  * `binding`: gelen iletileri `(channel, accountId, peer)` ve isteğe bağlı guild/takım kimlikleriyle bir `agentId` değerine yönlendirir.
  * Doğrudan sohbetler `agent:<agentId>:<mainKey>` değerine daraltılır (ajan başına "main"; `session.mainKey`).


## Platform örnekleri

Ajan başına Discord botları

Her Discord bot hesabı benzersiz bir `accountId` değerine eşlenir. Her hesabı bir ajana bağlayın ve izin listelerini bot başına tutun.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "coding", workspace: "~/.openclaw/workspace-coding" },    ],  },  bindings: [    { agentId: "main", match: { channel: "discord", accountId: "default" } },    { agentId: "coding", match: { channel: "discord", accountId: "coding" } },  ],  channels: {    discord: {      groupPolicy: "allowlist",      accounts: {        default: {          token: "DISCORD_BOT_TOKEN_MAIN",          guilds: {            "123456789012345678": {              channels: {                "222222222222222222": { allow: true, requireMention: false },              },            },          },        },        coding: {          token: "DISCORD_BOT_TOKEN_CODING",          guilds: {            "123456789012345678": {              channels: {                "333333333333333333": { allow: true, requireMention: false },              },            },          },        },      },    },  },}
[/code]

  * Her botu guild'e davet edin ve Message Content Intent'i etkinleştirin.
  * Token'lar `channels.discord.accounts.<id>.token` içinde bulunur (varsayılan hesap `DISCORD_BOT_TOKEN` kullanabilir).

Ajan başına Telegram botları json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "alerts", workspace: "~/.openclaw/workspace-alerts" },    ],  },  bindings: [    { agentId: "main", match: { channel: "telegram", accountId: "default" } },    { agentId: "alerts", match: { channel: "telegram", accountId: "alerts" } },  ],  channels: {    telegram: {      accounts: {        default: {          botToken: "123456:ABC...",          dmPolicy: "pairing",        },        alerts: {          botToken: "987654:XYZ...",          dmPolicy: "allowlist",          allowFrom: ["tg:123456789"],        },      },    },  },}
[/code]

  * BotFather ile ajan başına bir bot oluşturun ve her token'ı kopyalayın.
  * Token'lar `channels.telegram.accounts.<id>.botToken` içinde bulunur (varsayılan hesap `TELEGRAM_BOT_TOKEN` kullanabilir).

Ajan başına WhatsApp numaraları

Gateway'i başlatmadan önce her hesabı bağlayın:

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account personalopenclaw channels login --channel whatsapp --account biz
[/code]

`~/.openclaw/openclaw.json` (JSON5):

jsCopy code
[code]
    {  agents: {    list: [      {        id: "home",        default: true,        name: "Home",        workspace: "~/.openclaw/workspace-home",        agentDir: "~/.openclaw/agents/home/agent",      },      {        id: "work",        name: "Work",        workspace: "~/.openclaw/workspace-work",        agentDir: "~/.openclaw/agents/work/agent",      },    ],  },   // Deterministic routing: first match wins (most-specific first).  bindings: [    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },     // Optional per-peer override (example: send a specific group to work agent).    {      agentId: "work",      match: {        channel: "whatsapp",        accountId: "personal",        peer: { kind: "group", id: "1203630...@g.us" },      },    },  ],   // Off by default: agent-to-agent messaging must be explicitly enabled + allowlisted.  tools: {    agentToAgent: {      enabled: false,      allow: ["home", "work"],    },  },   channels: {    whatsapp: {      accounts: {        personal: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/personal          // authDir: "~/.openclaw/credentials/whatsapp/personal",        },        biz: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/biz          // authDir: "~/.openclaw/credentials/whatsapp/biz",        },      },    },  },}
[/code]

## Yaygın desenler

### WhatsApp günlük + Telegram derin çalışma

Kanala göre ayırın: WhatsApp'ı hızlı bir gündelik ajana, Telegram'ı ise bir Opus ajanına yönlendirin.

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    { agentId: "chat", match: { channel: "whatsapp" } },    { agentId: "opus", match: { channel: "telegram" } },  ],}
[/code]

Notlar:

  * Bir kanal için birden fazla hesabınız varsa binding'e `accountId` ekleyin (örneğin `{ channel: "whatsapp", accountId: "personal" }`).
  * Geri kalanını chat üzerinde tutarken tek bir DM/grubu Opus'a yönlendirmek için o peer için bir `match.peer` binding'i ekleyin; peer eşleşmeleri her zaman kanal geneli kurallara göre önceliklidir.


### Aynı kanal, bir peer Opus'a

WhatsApp'ı hızlı ajanda tutun, ancak bir DM'yi Opus'a yönlendirin:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    {      agentId: "opus",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } },    },    { agentId: "chat", match: { channel: "whatsapp" } },  ],}
[/code]

Peer binding'leri her zaman önceliklidir, bu yüzden bunları kanal geneli kuralın üzerinde tutun.

### Bir WhatsApp grubuna bağlı aile ajanı

Özel bir aile ajanını tek bir WhatsApp grubuna bağlayın; mention gating ve daha sıkı bir araç ilkesiyle:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "family",        name: "Family",        workspace: "~/.openclaw/workspace-family",        identity: { name: "Family Bot" },        groupChat: {          mentionPatterns: ["@family", "@familybot", "@Family Bot"],        },        sandbox: {          mode: "all",          scope: "agent",        },        tools: {          allow: [            "exec",            "read",            "sessions_list",            "sessions_history",            "sessions_send",            "sessions_spawn",            "session_status",          ],          deny: ["write", "edit", "apply_patch", "browser", "canvas", "nodes", "cron"],        },      },    ],  },  bindings: [    {      agentId: "family",      match: {        channel: "whatsapp",        peer: { kind: "group", id: "120363999999999999@g.us" },      },    },  ],}
[/code]

Notlar:

  * Araç allow/deny listeleri **araçlardır** , skills değildir. Bir skill'in ikili dosya çalıştırması gerekiyorsa `exec`'in izinli olduğundan ve ikili dosyanın sandbox içinde mevcut olduğundan emin olun.
  * Daha sıkı gating için `agents.list[].groupChat.mentionPatterns` ayarlayın ve kanal için grup allowlist'lerini etkin tutun.


## Ajan başına sandbox ve araç yapılandırması

Her ajanın kendi sandbox'ı ve araç kısıtlamaları olabilir:

jsCopy code
[code]
    {  agents: {    list: [      {        id: "personal",        workspace: "~/.openclaw/workspace-personal",        sandbox: {          mode: "off",  // No sandbox for personal agent        },        // No tool restrictions - all tools available      },      {        id: "family",        workspace: "~/.openclaw/workspace-family",        sandbox: {          mode: "all",     // Always sandboxed          scope: "agent",  // One container per agent          docker: {            // Optional one-time setup after container creation            setupCommand: "apt-get update && apt-get install -y git curl",          },        },        tools: {          allow: ["read"],                    // Only read tool          deny: ["exec", "write", "edit", "apply_patch"],    // Deny others        },      },    ],  },}
[/code]

**Avantajlar:**

  * **Güvenlik izolasyonu** : güvenilmeyen ajanlar için araçları kısıtlayın.
  * **Kaynak denetimi** : belirli ajanları sandbox'a alırken diğerlerini host üzerinde tutun.
  * **Esnek ilkeler** : ajan başına farklı izinler.


Ayrıntılı örnekler için [Çok ajanlı sandbox ve araçlar](</tr/tools/multi-agent-sandbox-tools>) bölümüne bakın.

## İlgili

  * [ACP ajanları](</tr/tools/acp-agents>) — harici kodlama harness'larını çalıştırma
  * [Kanal yönlendirme](</tr/channels/channel-routing>) — mesajların ajanlara nasıl yönlendirildiği
  * [Presence](</tr/concepts/presence>) — ajan presence'ı ve kullanılabilirliği
  * [Session](</tr/concepts/session>) — session izolasyonu ve yönlendirme
  * [Alt ajanlar](</tr/tools/subagents>) — arka plan ajan çalıştırmaları başlatma


Was this useful?YesNo