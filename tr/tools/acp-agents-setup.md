---
title: ACP ajanları — kurulum
source_url: https://docs.openclaw.ai/tr/tools/acp-agents-setup
scraped_at: 2026-05-25
---

Genel bakış, operatör çalışma kitabı ve kavramlar için bkz. [ACP aracıları](</tr/tools/acp-agents>).

Aşağıdaki bölümler acpx harness yapılandırmasını, MCP köprüleri için Plugin kurulumunu ve izin yapılandırmasını kapsar.

Bu sayfayı yalnızca ACP/acpx rotasını ayarlarken kullanın. Yerel Codex app-server çalışma zamanı yapılandırması için [Codex harness](</tr/plugins/codex-harness>) sayfasını kullanın. OpenAI API anahtarları veya Codex OAuth model sağlayıcı yapılandırması için [OpenAI](</tr/providers/openai>) sayfasını kullanın.

Codex'in iki OpenClaw rotası vardır:

Rota | Yapılandırma/komut | Kurulum sayfası  
---|---|---  
Yerel Codex app-server | `/codex ...`, `openai/gpt-*` aracı ref'leri | [Codex harness](</tr/plugins/codex-harness>)  
Açık Codex ACP bağdaştırıcısı | `/acp spawn codex`, `runtime: "acp", agentId: "codex"` | Bu sayfa  
  
ACP/acpx davranışına açıkça ihtiyacınız yoksa yerel rotayı tercih edin.

## acpx harness desteği (güncel)

Geçerli acpx yerleşik harness takma adları:

  * `claude`
  * `codex`
  * `copilot`
  * `cursor` (Cursor CLI: `cursor-agent acp`)
  * `droid`
  * `gemini`
  * `iflow`
  * `kilocode`
  * `kimi`
  * `kiro`
  * `openclaw`
  * `opencode`
  * `pi`
  * `qwen`


OpenClaw acpx arka ucunu kullandığında, acpx yapılandırmanız özel aracı takma adları tanımlamıyorsa `agentId` için bu değerleri tercih edin. Yerel Cursor kurulumunuz ACP'yi hâlâ `agent acp` olarak sunuyorsa, yerleşik varsayılanı değiştirmek yerine acpx yapılandırmanızda `cursor` aracı komutunu geçersiz kılın.

Doğrudan acpx CLI kullanımı `--agent <command>` ile rastgele bağdaştırıcıları da hedefleyebilir, ancak bu ham kaçış yolu bir acpx CLI özelliğidir (normal OpenClaw `agentId` yolu değildir).

Model denetimi bağdaştırıcı yeteneğine bağlıdır. Codex ACP model ref'leri, başlatmadan önce OpenClaw tarafından normalleştirilir. Diğer harness'ler ACP `models` ile birlikte `session/set_model` desteğine ihtiyaç duyar; bir harness ne bu ACP yeteneğini ne de kendi başlangıç model bayrağını sunuyorsa, OpenClaw/acpx model seçimini zorlayamaz.

## Gerekli yapılandırma

Temel ACP tabanı:

json5Copy code
[code]
    {  acp: {    enabled: true,    // Optional. Default is true; set false to pause ACP dispatch while keeping /acp controls.    dispatch: { enabled: true },    backend: "acpx",    defaultAgent: "codex",    allowedAgents: [      "claude",      "codex",      "copilot",      "cursor",      "droid",      "gemini",      "iflow",      "kilocode",      "kimi",      "kiro",      "openclaw",      "opencode",      "pi",      "qwen",    ],    maxConcurrentSessions: 8,    stream: {      coalesceIdleMs: 300,      maxChunkChars: 1200,    },    runtime: {      ttlMinutes: 120,    },  },}
[/code]

İş parçacığı bağlama yapılandırması kanal bağdaştırıcısına özeldir. Discord için örnek:

json5Copy code
[code]
    {  session: {    threadBindings: {      enabled: true,      idleHours: 24,      maxAgeHours: 0,    },  },  channels: {    discord: {      threadBindings: {        enabled: true,        spawnSessions: true,      },    },  },}
[/code]

İş parçacığına bağlı ACP spawn çalışmıyorsa, önce bağdaştırıcı özellik bayrağını doğrulayın:

  * Discord: `channels.discord.threadBindings.spawnSessions=true`


Geçerli konuşma bağları alt iş parçacığı oluşturmayı gerektirmez. Etkin bir konuşma bağlamı ve ACP konuşma bağlarını sunan bir kanal bağdaştırıcısı gerektirir.

Bkz. [Yapılandırma Başvurusu](</tr/gateway/configuration-reference>).

## acpx arka ucu için Plugin kurulumu

Paketlenmiş kurulumlar ACP için resmi `@openclaw/acpx` çalışma zamanı Plugin'ini kullanır. ACP harness oturumlarını kullanmadan önce onu kurun ve etkinleştirin:

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

Kaynak checkout'ları `pnpm install` sonrasında yerel workspace Plugin'ini de kullanabilir.

Şununla başlayın:

textCopy code
[code]
    /acp doctor
[/code]

`acpx`'i devre dışı bıraktıysanız, `plugins.allow` / `plugins.deny` üzerinden reddettiyseniz veya paketlenmiş Plugin'e geri dönmek istiyorsanız, açık paket yolunu kullanın:

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

Geliştirme sırasında yerel workspace kurulumu:

bashCopy code
[code]
    openclaw plugins install ./path/to/local/acpx-plugin
[/code]

Ardından arka uç sağlığını doğrulayın:

textCopy code
[code]
    /acp doctor
[/code]

### acpx komutu ve sürüm yapılandırması

Varsayılan olarak `acpx` Plugin'i, Gateway başlatma sırasında gömülü ACP arka ucunu yoklar ve gateway `ready` sinyalinden önce bu yoklamayı bekler. Başlangıç yoklamasını atlayıp arka ucu bunun yerine tembel şekilde kaydetmek için `OPENCLAW_ACPX_RUNTIME_STARTUP_PROBE=0` ayarlayın. Açık isteğe bağlı yoklama için `/acp doctor` çalıştırın.

Plugin yapılandırmasında komutu veya sürümü geçersiz kılın:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "command": "../acpx/dist/cli.js",          "expectedVersion": "any"        }      }    }  }}
[/code]

  * `command` mutlak yol, göreli yol (OpenClaw workspace'inden çözümlenir) veya komut adı kabul eder.
  * `expectedVersion: "any"` katı sürüm eşleştirmesini devre dışı bırakır.
  * Özel `command` yolları Plugin yerel otomatik kurulumu devre dışı bırakır.


Bir yol veya bayrak değerinin tek bir argv belirteci olarak kalması gerektiğinde, yapılandırılmış argümanlarla tek bir ACP aracı komutunu geçersiz kılın:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "agents": {            "claude": {              "command": "node",              "args": ["/path/to/custom adapter.mjs", "--verbose"]            }          }        }      }    }  }}
[/code]

  * `agents.<id>.command`, ilgili ACP aracı için yürütülebilir dosya veya mevcut komut dizesidir.
  * `agents.<id>.args` isteğe bağlıdır. OpenClaw bunu geçerli acpx komut dizesi kayıt defterinden geçirmeden önce her dizi öğesi shell için alıntılanır.


Bkz. [Pluginler](</tr/tools/plugin>).

### Otomatik bağımlılık kurulumu

OpenClaw'u `npm install -g openclaw` ile global olarak kurduğunuzda, acpx çalışma zamanı bağımlılıkları (platforma özel ikili dosyalar) bir postinstall hook'u aracılığıyla otomatik olarak kurulur. Otomatik kurulum başarısız olursa gateway yine de normal şekilde başlar ve eksik bağımlılığı `openclaw acp doctor` üzerinden bildirir.

### Plugin araçları MCP köprüsü

Varsayılan olarak ACPX oturumları, OpenClaw Plugin kayıtlı araçlarını ACP harness'e **sunmaz**.

Codex veya Claude Code gibi ACP aracılarının bellek geri çağırma/depolama gibi kurulu OpenClaw Plugin araçlarını çağırmasını istiyorsanız, özel köprüyü etkinleştirin:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.pluginToolsMcpBridge true
[/code]

Bunun yaptığı:

  * ACPX oturum başlangıcına `openclaw-plugin-tools` adlı yerleşik bir MCP sunucusu enjekte eder.
  * Kurulu ve etkin OpenClaw Pluginleri tarafından zaten kaydedilmiş Plugin araçlarını sunar.
  * Özelliği açık ve varsayılan olarak kapalı tutar.


Güvenlik ve güven notları:

  * Bu, ACP harness araç yüzeyini genişletir.
  * ACP aracıları yalnızca gateway'de zaten etkin olan Plugin araçlarına erişim kazanır.
  * Bunu, söz konusu Pluginlerin OpenClaw'un içinde çalışmasına izin vermekle aynı güven sınırı olarak değerlendirin.
  * Etkinleştirmeden önce kurulu Pluginleri inceleyin.


Özel `mcpServers` eskisi gibi çalışmaya devam eder. Yerleşik Plugin araçları köprüsü, genel MCP sunucusu yapılandırmasının yerine geçmez; ek, isteğe bağlı bir kolaylıktır.

### OpenClaw araçları MCP köprüsü

Varsayılan olarak ACPX oturumları ayrıca yerleşik OpenClaw araçlarını MCP üzerinden **sunmaz**. Bir ACP aracısının `cron` gibi seçili yerleşik araçlara ihtiyaç duyması durumunda ayrı core-tools köprüsünü etkinleştirin:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.openClawToolsMcpBridge true
[/code]

Bunun yaptığı:

  * ACPX oturum başlangıcına `openclaw-tools` adlı yerleşik bir MCP sunucusu enjekte eder.
  * Seçili yerleşik OpenClaw araçlarını sunar. İlk sunucu `cron` sunar.
  * Çekirdek araç görünürlüğünü açık ve varsayılan olarak kapalı tutar.


### Çalışma zamanı zaman aşımı yapılandırması

`acpx` Plugin'i, gömülü çalışma zamanı turlarını varsayılan olarak 120 saniyelik zaman aşımıyla çalıştırır. Bu, Gemini CLI gibi daha yavaş harness'lerin ACP başlatma ve ilklendirmeyi tamamlaması için yeterli süre sağlar. Ana makineniz farklı bir çalışma zamanı sınırına ihtiyaç duyuyorsa bunu geçersiz kılın:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.timeoutSeconds 180
[/code]

Bu değeri değiştirdikten sonra gateway'i yeniden başlatın.

### Sağlık yoklama aracı yapılandırması

`/acp doctor` veya başlangıç yoklaması arka ucu denetlediğinde, paketli `acpx` Plugin'i bir harness aracısını yoklar. `acp.allowedAgents` ayarlanmışsa, varsayılan olarak ilk izin verilen aracıya; aksi takdirde `codex` değerine ayarlanır. Dağıtımınız sağlık denetimleri için farklı bir ACP aracısına ihtiyaç duyuyorsa, yoklama aracısını açıkça ayarlayın:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.probeAgent claude
[/code]

Bu değeri değiştirdikten sonra gateway'i yeniden başlatın.

## İzin yapılandırması

ACP oturumları etkileşimsiz çalışır; dosya yazma ve shell exec izin istemlerini onaylamak veya reddetmek için TTY yoktur. acpx Plugin'i izinlerin nasıl ele alınacağını denetleyen iki yapılandırma anahtarı sağlar:

Bu ACPX harness izinleri, OpenClaw exec onaylarından ve Claude CLI `--permission-mode bypassPermissions` gibi CLI arka ucu sağlayıcı atlatma bayraklarından ayrıdır. ACPX `approve-all`, ACP oturumları için harness düzeyinde acil durum anahtarıdır.

### `permissionMode`

Harness aracısının istem göstermeden hangi işlemleri gerçekleştirebileceğini denetler.

Değer | Davranış  
---|---  
`approve-all` | Tüm dosya yazmalarını ve shell komutlarını otomatik onaylar.  
`approve-reads` | Yalnızca okumaları otomatik onaylar; yazmalar ve exec istem gerektirir.  
`deny-all` | Tüm izin istemlerini reddeder.  
  
### `nonInteractivePermissions`

Bir izin istemi gösterilecek ancak etkileşimli TTY kullanılamayacaksa ne olacağını denetler (ACP oturumları için durum her zaman budur).

Değer | Davranış  
---|---  
`fail` | Oturumu `AcpRuntimeError` ile iptal eder. **(varsayılan)**  
`deny` | İzni sessizce reddeder ve devam eder (zarif bozulma).  
  
### Yapılandırma

Plugin yapılandırması üzerinden ayarlayın:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions fail
[/code]

Bu değerleri değiştirdikten sonra gateway'i yeniden başlatın.

## İlgili

  * [ACP aracıları](</tr/tools/acp-agents>) — genel bakış, operatör çalışma kitabı, kavramlar
  * [Alt aracılar](</tr/tools/subagents>)
  * [Çok aracılı yönlendirme](</tr/concepts/multi-agent>)


Was this useful?YesNo