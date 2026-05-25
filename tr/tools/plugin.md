---
title: Pluginler
source_url: https://docs.openclaw.ai/tr/tools/plugin
scraped_at: 2026-05-25
---

Pluginler OpenClaw’a yeni yetenekler ekler: kanallar, model sağlayıcıları, ajan yürütme ortamları, araçlar, Skills, konuşma, gerçek zamanlı transkripsiyon, gerçek zamanlı ses, medya anlama, görüntü oluşturma, video oluşturma, web getirme, web arama ve daha fazlası. Bazı pluginler **çekirdek** tir (OpenClaw ile birlikte gelir), diğerleri **haricidir**. Çoğu harici plugin [ClawHub](</tr/clawhub>) üzerinden yayımlanır ve keşfedilir. Npm, doğrudan kurulumlar ve bu geçiş tamamlanırken OpenClaw’a ait geçici bir plugin paketi kümesi için desteklenmeye devam eder.

## Hızlı başlangıç

Kopyala-yapıştır kurulum, listeleme, kaldırma, güncelleme ve yayımlama örnekleri için [Pluginleri yönet](</tr/plugins/manage-plugins>) bölümüne bakın.

* ### Nelerin yüklendiğini görün

bashCopy code
[code]
    openclaw plugins list
[/code]

* ### Bir plugin kurun

bashCopy code
[code]
    # Search ClawHub pluginsopenclaw plugins search "calendar" # From ClawHubopenclaw plugins install clawhub:openclaw-codex-app-server # From npmopenclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm-pack:./openclaw-plugin-1.2.3.tgz # From gitopenclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0 # From a local directory or archiveopenclaw plugins install ./my-pluginopenclaw plugins install ./my-plugin.tgz
[/code]

* ### Gateway’i yeniden başlatın

bashCopy code
[code]
    openclaw gateway restart
[/code]

Ardından yapılandırma dosyanızda `plugins.entries.\<id\>.config` altında yapılandırın.

* ### Sohbet-yerel yönetim

Çalışan bir Gateway’de, yalnızca sahibin kullanabildiği `/plugins enable` ve `/plugins disable` Gateway yapılandırma yeniden yükleyicisini tetikler. Gateway, plugin çalışma zamanı yüzeylerini süreç içinde yeniden yükler ve yeni ajan dönüşleri araç listesini yenilenmiş kayıt defterinden yeniden oluşturur. `/plugins install` plugin kaynak kodunu değiştirir; bu yüzden Gateway, geçerli sürecin zaten içe aktarılmış modülleri güvenle yeniden yükleyebileceğini varsaymak yerine yeniden başlatma ister.

* ### Plugini doğrulayın

bashCopy code
[code]
    openclaw plugins inspect <plugin-id> --runtime --json # If the plugin registered a CLI root, run one command from that root.openclaw <plugin-command> --help
[/code]

Kayıtlı araçları, hizmetleri, gateway yöntemlerini, hook’ları veya plugine ait CLI komutlarını kanıtlamanız gerektiğinde `--runtime` kullanın. Düz `inspect`, soğuk bir manifest/kayıt defteri denetimidir ve plugin çalışma zamanını içe aktarmaktan özellikle kaçınır.

Sohbet-yerel denetimi tercih ediyorsanız `commands.plugins: true` etkinleştirin ve şunları kullanın:

textCopy code
[code]
    /plugin install clawhub:<package>/plugin show <plugin-id>/plugin enable <plugin-id>
[/code]

Kurulum yolu CLI ile aynı çözümleyiciyi kullanır: yerel yol/arşiv, açık `clawhub:<pkg>`, açık `npm:<pkg>`, açık `npm-pack:<path.tgz>`, açık `git:<repo>` veya npm üzerinden yalın paket belirtimi.

Yapılandırma geçersizse kurulum normalde kapalı şekilde başarısız olur ve sizi `openclaw doctor --fix` komutuna yönlendirir. Tek kurtarma istisnası, `openclaw.install.allowInvalidConfigRecovery` seçeneğine katılan pluginler için dar kapsamlı bir birlikte gelen plugini yeniden kurma yoludur. Gateway başlatılırken, geçersiz plugin yapılandırması diğer geçersiz yapılandırmalar gibi kapalı şekilde başarısız olur. Hatalı plugin yapılandırmasını o plugin girdisini devre dışı bırakıp geçersiz yapılandırma yükünü kaldırarak karantinaya almak için `openclaw doctor --fix` çalıştırın; normal yapılandırma yedeği önceki değerleri korur. Bir kanal yapılandırması artık keşfedilemeyen bir plugine başvuruyor, ancak aynı eski plugin kimliği plugin yapılandırmasında veya kurulum kayıtlarında kalıyorsa, Gateway başlatma uyarıları günlüğe yazar ve diğer tüm kanalları engellemek yerine o kanalı atlar. Eski kanal/plugin girdilerini kaldırmak için `openclaw doctor --fix` çalıştırın; eski-plugin kanıtı olmayan bilinmeyen kanal anahtarları doğrulamada yine başarısız olur, böylece yazım hataları görünür kalır. `plugins.enabled: false` ayarlanmışsa eski plugin başvuruları eylemsiz kabul edilir: Gateway başlatma, plugin keşif/yükleme işini atlar ve `openclaw doctor`, devre dışı plugin yapılandırmasını otomatik kaldırmak yerine korur. Eski plugin kimliklerinin kaldırılmasını istiyorsanız doctor temizliğini çalıştırmadan önce pluginleri yeniden etkinleştirin.

Plugin bağımlılığı kurulumu yalnızca açık kurulum/güncelleme veya doctor onarım akışları sırasında gerçekleşir. Gateway başlatma, yapılandırma yeniden yükleme ve çalışma zamanı incelemesi paket yöneticilerini çalıştırmaz ya da bağımlılık ağaçlarını onarmaz. Yerel pluginlerin bağımlılıkları zaten kurulu olmalıdır; npm, git ve ClawHub pluginleri ise OpenClaw’ın yönettiği plugin kökleri altına kurulur. npm bağımlılıkları OpenClaw’ın yönettiği npm kökü içinde yukarı taşınabilir; kurulum/güncelleme, güvenmeden önce bu yönetilen kökü tarar ve kaldırma işlemi npm tarafından yönetilen paketleri npm üzerinden kaldırır. Harici pluginler ve özel yükleme yolları yine `openclaw plugins install` üzerinden kurulmalıdır. Çalışma zamanı kodunu içe aktarmadan veya bağımlılıkları onarmadan her görünür plugin için statik `dependencyStatus` değerini görmek üzere `openclaw plugins list --json` kullanın. Kurulum zamanı yaşam döngüsü için [Plugin bağımlılığı çözümleme](</tr/plugins/dependency-resolution>) bölümüne bakın.

### Engellenen plugin yolu sahipliği

Plugin tanılamaları `blocked plugin candidate: suspicious ownership (... uid=1000, expected uid=0 or root)` diyor ve yapılandırma doğrulaması `plugin present but blocked` ile devam ediyorsa, OpenClaw plugin dosyalarının onları yükleyen süreçten farklı bir Unix kullanıcısına ait olduğunu bulmuştur. Plugin yapılandırmasını yerinde bırakın; dosya sistemi sahipliğini düzeltin veya OpenClaw’ı durum dizininin sahibi olan aynı kullanıcı olarak çalıştırın.

Docker kurulumlarında resmi imaj `node` (uid `1000`) olarak çalışır; bu yüzden ana makinede bind-mount edilen OpenClaw yapılandırma ve çalışma alanı dizinleri normalde uid `1000` tarafından sahiplenilmelidir:

bashCopy code
[code]
    sudo chown -R 1000:1000 /path/to/openclaw-config /path/to/openclaw-workspace
[/code]

OpenClaw’ı bilerek root olarak çalıştırıyorsanız yönetilen plugin kökünü root sahipliğine onarın:

bashCopy code
[code]
    sudo chown -R root:root /path/to/openclaw-config/npm
[/code]

Sahipliği düzelttikten sonra kalıcı plugin kayıt defterinin onarılmış dosyalarla eşleşmesi için `openclaw doctor --fix` veya `openclaw plugins registry --refresh` komutunu yeniden çalıştırın.

Npm kurulumlarında `latest` veya dist-tag gibi değişebilir seçiciler kurulumdan önce çözümlenir ve ardından OpenClaw’ın yönettiği npm kökünde doğrulanmış kesin sürüme sabitlenir. npm tamamlandıktan sonra OpenClaw, kurulu `package-lock.json` girdisinin hâlâ çözümlenen sürüm ve bütünlükle eşleştiğini doğrular. npm farklı paket meta verisi yazarsa, kurulum başarısız olur ve farklı bir plugin yapıtını kabul etmek yerine yönetilen paket geri alınır. Yönetilen npm kökleri ayrıca OpenClaw’ın paket düzeyi npm `overrides` değerlerini miras alır; böylece paketlenmiş ana sistemi koruyan güvenlik sabitlemeleri yukarı taşınmış harici plugin bağımlılıklarına da uygulanır.

Kaynak checkout’ları pnpm çalışma alanlarıdır. Birlikte gelen pluginler üzerinde çalışmak için OpenClaw’ı klonlarsanız `pnpm install` çalıştırın; OpenClaw ardından birlikte gelen pluginleri `extensions/<id>` konumundan yükler, böylece düzenlemeler ve pakete yerel bağımlılıklar doğrudan kullanılır. Düz npm kök kurulumları paketlenmiş OpenClaw içindir, kaynak checkout geliştirmesi için değildir.

## Plugin türleri

OpenClaw iki plugin biçimini tanır:

Biçim | Nasıl çalışır | Örnekler  
---|---|---  
**Yerel** | `openclaw.plugin.json` \+ çalışma zamanı modülü; süreç içinde yürütülür | Resmi pluginler, topluluk npm paketleri  
**Paket** | Codex/Claude/Cursor uyumlu düzen; OpenClaw özelliklerine eşlenir | `.codex-plugin/`, `.claude-plugin/`, `.cursor-plugin/`  
  
Her ikisi de `openclaw plugins list` altında görünür. Paket ayrıntıları için [Plugin Paketleri](</tr/plugins/bundles>) bölümüne bakın.

Yerel bir plugin yazıyorsanız [Plugin Oluşturma](</tr/plugins/building-plugins>) ve [Plugin SDK Genel Bakışı](</tr/plugins/sdk-overview>) ile başlayın.

## Paket giriş noktaları

Yerel plugin npm paketleri `package.json` içinde `openclaw.extensions` bildirmelidir. Her girdi paket dizini içinde kalmalı ve okunabilir bir çalışma zamanı dosyasına ya da `src/index.ts` ile `dist/index.js` gibi çıkarımlanan yerleşik JavaScript eş dosyasına sahip bir TypeScript kaynak dosyasına çözümlenmelidir. Paketlenmiş kurulumlar bu JavaScript çalışma zamanı çıktısını göndermelidir. TypeScript kaynak yedeği npm paketleri için değil, kaynak checkout’ları ve yerel geliştirme yolları içindir; OpenClaw’ın yönettiği plugin köküne kurulmuş npm paketleri için değildir.

Global uzantı köküne bırakılan izlenmeyen dizinler yerel kaynak checkout’ları olarak değerlendirilir ve TypeScript girişlerini doğrudan yükleyebilir. `installPath` veya `sourcePath` dahil bir kurulum kaydı tarafından hâlâ adlandırılan dizinler yönetilen olarak kalır ve global tarama onları görse bile derlenmiş-çıktı gereksinimini korur. Yönetilen bir kurulumu bilinçli olarak izlenmeyen yerel checkout’a dönüştürüyorsanız önce kaldırma veya doctor temizliği ile eski kurulum kaydını kaldırın.

Yönetilen paket uyarısı `requires compiled runtime output for TypeScript entry ...` diyorsa paket, OpenClaw’ın çalışma zamanında ihtiyaç duyduğu JavaScript dosyaları olmadan yayımlanmıştır. Bu, yerel yapılandırma sorunu değil bir plugin paketleme sorunudur. Yayımcı derlenmiş JavaScript’i yeniden yayımladıktan sonra plugini güncelleyin veya yeniden kurun ya da düzeltilmiş bir paket kullanılabilir olana kadar o plugini devre dışı bırakın/kaldırın.

Yayımlanmış çalışma zamanı dosyaları kaynak girdilerle aynı yollarda bulunmadığında `openclaw.runtimeExtensions` kullanın. Varsa `runtimeExtensions`, her `extensions` girdisi için tam olarak bir girdi içermelidir. Eşleşmeyen listeler, sessizce kaynak yollara geri dönmek yerine kurulumu ve plugin keşfini başarısız kılar. `openclaw.setupEntry` de yayımlıyorsanız yerleşik JavaScript eş dosyası için `openclaw.runtimeSetupEntry` kullanın; bildirildiğinde bu dosya zorunludur.

jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "openclaw": {    "extensions": ["./src/index.ts"],    "runtimeExtensions": ["./dist/index.js"]  }}
[/code]

## Resmi pluginler

### Geçiş sırasında OpenClaw’a ait npm paketleri

ClawHub, çoğu plugin için birincil dağıtım yoludur. Mevcut paketlenmiş OpenClaw sürümleri zaten birçok resmi plugini birlikte getirir, bu nedenle normal kurulumlarda bunlar için ayrı npm kurulumu gerekmez. OpenClaw’a ait her plugin ClawHub’a taşınana kadar OpenClaw, eski/özel kurulumlar ve doğrudan npm iş akışları için npm üzerinde bazı `@openclaw/*` plugin paketlerini göndermeye devam eder.

Npm bir `@openclaw/*` plugin paketini deprecated olarak bildirirse, bu paket sürümü daha eski bir harici paket hattındandır. Daha yeni bir npm paketi yayımlanana kadar güncel OpenClaw’daki birlikte gelen plugini veya yerel checkout’u kullanın.

Plugin | Paket | Belgeler  
---|---|---  
Discord | `@openclaw/discord` | [Discord](</tr/channels/discord>)  
Feishu | `@openclaw/feishu` | [Feishu](</tr/channels/feishu>)  
Matrix | `@openclaw/matrix` | [Matrix](</tr/channels/matrix>)  
Mattermost | `@openclaw/mattermost` | [Mattermost](</tr/channels/mattermost>)  
Microsoft Teams | `@openclaw/msteams` | [Microsoft Teams](</tr/channels/msteams>)  
Nextcloud Talk | `@openclaw/nextcloud-talk` | [Nextcloud Talk](</tr/channels/nextcloud-talk>)  
Nostr | `@openclaw/nostr` | [Nostr](</tr/channels/nostr>)  
Synology Chat | `@openclaw/synology-chat` | [Synology Chat](</tr/channels/synology-chat>)  
Tlon | `@openclaw/tlon` | [Tlon](</tr/channels/tlon>)  
WhatsApp | `@openclaw/whatsapp` | [WhatsApp](</tr/channels/whatsapp>)  
Zalo | `@openclaw/zalo` | [Zalo](</tr/channels/zalo>)  
Zalo Personal | `@openclaw/zalouser` | [Zalo Personal](</tr/plugins/zalouser>)  
  
### Çekirdek (OpenClaw ile birlikte gelir)

Model sağlayıcıları (varsayılan olarak etkin)

`anthropic`, `byteplus`, `cloudflare-ai-gateway`, `github-copilot`, `google`, `huggingface`, `kilocode`, `kimi-coding`, `minimax`, `mistral`, `qwen`, `moonshot`, `nvidia`, `openai`, `opencode`, `opencode-go`, `openrouter`, `qianfan`, `synthetic`, `together`, `venice`, `vercel-ai-gateway`, `volcengine`, `xiaomi`, `zai`

Bellek Plugin'leri

  * `memory-core` \- paketle gelen bellek araması (`plugins.slots.memory` üzerinden varsayılan)
  * `memory-lancedb` \- otomatik geri çağırma/yakalama özellikli LanceDB destekli uzun süreli bellek (`plugins.slots.memory = "memory-lancedb"` ayarlayın)


OpenAI uyumlu embedding kurulumu, Ollama örnekleri, geri çağırma sınırları ve sorun giderme için [Memory LanceDB](</tr/plugins/memory-lancedb>) bölümüne bakın.

Konuşma sağlayıcıları (varsayılan olarak etkin)

`elevenlabs`, `microsoft`

Diğer

  * `browser` \- tarayıcı aracı, `openclaw browser` CLI, `browser.request` gateway yöntemi, tarayıcı runtime'ı ve varsayılan tarayıcı denetim servisi için paketle gelen tarayıcı Plugin'i (varsayılan olarak etkin; değiştirmeden önce devre dışı bırakın)
  * `copilot-proxy` \- VS Code Copilot Proxy köprüsü (varsayılan olarak devre dışı)


Üçüncü taraf Plugin'ler mi arıyorsunuz? [ClawHub](</tr/clawhub>) bölümüne bakın.

## Yapılandırma

json5Copy code
[code]
    {  plugins: {    enabled: true,    allow: ["voice-call"],    deny: ["untrusted-plugin"],    load: { paths: ["~/Projects/oss/voice-call-plugin"] },    entries: {      "voice-call": { enabled: true, config: { provider: "twilio" } },    },  },}
[/code]

Alan | Açıklama  
---|---  
`enabled` | Ana anahtar (varsayılan: `true`)  
`allow` | Plugin izin listesi (isteğe bağlı)  
`bundledDiscovery` | Paketle gelen Plugin keşif modu (varsayılan `allowlist`)  
`deny` | Plugin engel listesi (isteğe bağlı; engel kazanır)  
`load.paths` | Ek Plugin dosyaları/dizinleri  
`slots` | Özel slot seçicileri (örn. `memory`, `contextEngine`)  
`entries.\<id\>` | Plugin başına anahtarlar + yapılandırma  
  
`plugins.allow` özeldir. Boş değilken, `tools.allow` `"*"` veya belirli bir Plugin'e ait araç adı içerse bile yalnızca listelenen Plugin'ler yüklenebilir veya araç sunabilir. Bir araç izin listesi Plugin araçlarına başvuruyorsa, sahip Plugin kimliklerini `plugins.allow` içine ekleyin veya `plugins.allow` değerini kaldırın; `openclaw doctor` bu yapı hakkında uyarır.

Yeni yapılandırmalar için `plugins.bundledDiscovery` varsayılan olarak `"allowlist"` olur; bu nedenle kısıtlayıcı bir `plugins.allow` envanteri, runtime web araması sağlayıcı keşfi dahil olmak üzere atlanmış paketle gelen sağlayıcı Plugin'lerini de engeller. Doctor, eski kısıtlayıcı izin listesi yapılandırmalarını geçiş sırasında `"compat"` ile damgalar; böylece operatör daha katı moda geçene kadar yükseltmeler eski paketle gelen sağlayıcı davranışını korur. Boş bir `plugins.allow` hâlâ ayarlanmamış/açık olarak değerlendirilir.

`/plugins enable` veya `/plugins disable` ile yapılan yapılandırma değişiklikleri, süreç içinde Gateway Plugin yeniden yüklemesini tetikler. Yeni ajan dönüşleri, araç listesini yenilenmiş Plugin kayıt defterinden yeniden oluşturur. Kurulum, güncelleme ve kaldırma gibi kaynak değiştiren işlemler yine Gateway sürecini yeniden başlatır; çünkü zaten içe aktarılmış Plugin modülleri yerinde güvenli biçimde değiştirilemez.

`openclaw plugins list` yerel bir Plugin kayıt defteri/yapılandırma anlık görüntüsüdür. Orada bir Plugin'in `enabled` olması, kalıcı kayıt defterinin ve geçerli yapılandırmanın Plugin'in katılmasına izin verdiği anlamına gelir. Bu, zaten çalışan uzak bir Gateway'in aynı Plugin koduna yeniden yüklendiğini veya yeniden başlatıldığını kanıtlamaz. Sarmalayıcı süreçleri olan VPS/kapsayıcı kurulumlarında, yeniden başlatmaları veya yeniden yükleme tetikleyen yazmaları gerçek `openclaw gateway run` sürecine gönderin ya da yeniden yükleme bir hata bildirdiğinde çalışan Gateway'e karşı `openclaw gateway restart` kullanın.

Plugin durumları: devre dışı, eksik ve geçersiz

  * **Devre dışı** : Plugin vardır, ancak etkinleştirme kuralları onu kapatmıştır. Yapılandırma korunur.
  * **Eksik** : yapılandırma, keşfin bulamadığı bir Plugin kimliğine başvurur.
  * **Geçersiz** : Plugin vardır, ancak yapılandırması bildirilen şemayla eşleşmez. Gateway başlatması yalnızca o Plugin'i atlar; `openclaw doctor --fix`, geçersiz girdiyi devre dışı bırakıp yapılandırma yükünü kaldırarak karantinaya alabilir.


## Keşif ve öncelik

OpenClaw Plugin'leri şu sırayla tarar (ilk eşleşme kazanır):

* ### Yapılandırma yolları

`plugins.load.paths` \- açık dosya veya dizin yolları. OpenClaw'ın kendi paketlenmiş paketle gelen Plugin dizinlerine geri işaret eden yollar yok sayılır; bu eski takma adları kaldırmak için `openclaw doctor --fix` çalıştırın.

* ### Çalışma alanı Plugin'leri

`\<workspace\>/.openclaw/<plugin-root>/*.ts` ve `\<workspace\>/.openclaw/<plugin-root>/*/index.ts`.

* ### Genel Plugin'ler

`~/.openclaw/<plugin-root>/*.ts` ve `~/.openclaw/<plugin-root>/*/index.ts`.

* ### Paketle gelen Plugin'ler

OpenClaw ile gönderilir. Birçoğu varsayılan olarak etkindir (model sağlayıcıları, konuşma). Diğerleri açık etkinleştirme gerektirir.

Paketli kurulumlar ve Docker imajları normalde paketle gelen Plugin'leri derlenmiş `dist/extensions` ağacından çözer. Paketle gelen bir Plugin kaynak dizini, örneğin `/app/extensions/synology-chat`, eşleşen paketli kaynak yolunun üzerine bind mount edilirse, OpenClaw bu bağlı kaynak dizinini paketle gelen bir kaynak katmanı olarak değerlendirir ve paketli `/app/dist/extensions/synology-chat` paketinden önce keşfeder. Bu, her paketle gelen Plugin'i yeniden TypeScript kaynağına geçirmeden bakımcı kapsayıcı döngülerinin çalışmasını sağlar. Kaynak katmanı mount'ları mevcut olduğunda bile paketli dist paketlerini zorlamak için `OPENCLAW_DISABLE_BUNDLED_SOURCE_OVERLAYS=1` ayarlayın.

### Etkinleştirme kuralları

  * `plugins.enabled: false` tüm Plugin'leri devre dışı bırakır ve Plugin keşif/yükleme işini atlar
  * `plugins.deny` her zaman izne üstün gelir
  * `plugins.entries.\<id\>.enabled: false` o Plugin'i devre dışı bırakır
  * Çalışma alanı kaynaklı Plugin'ler **varsayılan olarak devre dışıdır** (açıkça etkinleştirilmelidir)
  * Paketle gelen Plugin'ler, üzerine yazılmadıkça yerleşik varsayılan-açık kümesini izler
  * Özel slotlar, seçilen Plugin'i o slot için zorla etkinleştirebilir
  * Bazı paketle gelen opt-in Plugin'ler, yapılandırma sağlayıcı model ref'i, kanal yapılandırması veya harness runtime'ı gibi Plugin'e ait bir yüzeyi adlandırdığında otomatik olarak etkinleştirilir
  * Eski Plugin yapılandırması `plugins.enabled: false` etkinken korunur; eski kimliklerin kaldırılmasını istiyorsanız doctor temizliğini çalıştırmadan önce Plugin'leri yeniden etkinleştirin
  * OpenAI ailesi Codex rotaları ayrı Plugin sınırlarını korur: `openai-codex/*` OpenAI Plugin'ine aittir; paketle gelen Codex app-server Plugin'i ise kurallı `openai/*` ajan ref'leri, açık provider/model `agentRuntime.id: "codex"` veya eski `codex/*` model ref'leri tarafından seçilir


## Runtime hook'larında sorun giderme

Bir Plugin `plugins list` içinde görünüyor, ancak `register(api)` yan etkileri veya hook'ları canlı sohbet trafiğinde çalışmıyorsa önce şunları kontrol edin:

  * `openclaw gateway status --deep --require-rpc` çalıştırın ve etkin Gateway URL'sinin, profilin, yapılandırma yolunun ve sürecin düzenlediğiniz değerler olduğunu doğrulayın.
  * Plugin kurulumundan/yapılandırma/kod değişikliklerinden sonra canlı Gateway'i yeniden başlatın. Sarmalayıcı kapsayıcılarda PID 1 yalnızca bir supervisor olabilir; alt `openclaw gateway run` sürecini yeniden başlatın veya sinyal gönderin.
  * Hook kayıtlarını ve tanılamaları doğrulamak için `openclaw plugins inspect <id> --runtime --json` kullanın. `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `llm_input`, `llm_output`, `before_agent_finalize` ve `agent_end` gibi paketle gelmeyen konuşma hook'ları `plugins.entries.<id>.hooks.allowConversationAccess=true` gerektirir.
  * Model değiştirme için `before_model_resolve` tercih edin. Ajan dönüşlerinde model çözümlemesinden önce çalışır; `llm_output` yalnızca bir model denemesi asistan çıktısı ürettikten sonra çalışır.
  * Etkili oturum modelinin kanıtı için `openclaw sessions` veya Gateway oturum/durum yüzeylerini kullanın ve sağlayıcı yüklerini hata ayıklarken Gateway'i `--raw-stream --raw-stream-path <path>` ile başlatın.


### Yavaş Plugin aracı kurulumu

Araçlar hazırlanırken ajan dönüşleri takılıyor gibi görünüyorsa izleme günlüklemesini etkinleştirin ve Plugin araç factory zamanlama satırlarını kontrol edin:

bashCopy code
[code]
    openclaw config set logging.level traceopenclaw logs --follow
[/code]

Şunu arayın:

textCopy code
[code]
    [trace:plugin-tools] factory timings ...
[/code]

Özet, toplam factory süresini ve en yavaş Plugin araç factory'lerini listeler; Plugin kimliği, bildirilen araç adları, sonuç şekli ve aracın isteğe bağlı olup olmadığı buna dahildir. Tek bir factory en az 1 sn sürdüğünde veya toplam Plugin araç factory hazırlığı en az 5 sn sürdüğünde yavaş satırlar uyarılara yükseltilir.

OpenClaw, aynı etkili istek bağlamıyla yinelenen çözümlemeler için başarılı Plugin araç factory sonuçlarını önbelleğe alır. Önbellek anahtarı etkili runtime yapılandırmasını, çalışma alanını, ajan/oturum kimliklerini, sandbox ilkesini, tarayıcı ayarlarını, teslim bağlamını, istekte bulunan kimliğini ve sahiplik durumunu içerir; bu nedenle bu güvenilir alanlara bağımlı factory'ler bağlam değiştiğinde yeniden çalıştırılır.

Zamanlamaya bir Plugin hakimse runtime kayıtlarını inceleyin:

bashCopy code
[code]
    openclaw plugins inspect <plugin-id> --runtime --json
[/code]

Ardından o Plugin'i güncelleyin, yeniden kurun veya devre dışı bırakın. Plugin yazarları pahalı bağımlılık yüklemesini araç factory'si içinde yapmak yerine araç yürütme yolunun arkasına taşımalıdır.

### Yinelenen kanal veya araç sahipliği

Belirtiler:

  * `channel already registered: <channel-id> (<plugin-id>)`
  * `channel setup already registered: <channel-id> (<plugin-id>)`
  * `plugin tool name conflict (<plugin-id>): <tool-name>`


Bunlar, birden fazla etkin Plugin'in aynı kanala, kurulum akışına veya araç adına sahip olmaya çalıştığı anlamına gelir. En yaygın neden, artık aynı kanal kimliğini sağlayan paketle gelen bir Plugin'in yanına harici bir kanal Plugin'i kurulmuş olmasıdır.

Hata ayıklama adımları:

  * Her etkin Plugin'i ve kökenini görmek için `openclaw plugins list --enabled --verbose` çalıştırın.
  * Şüpheli her Plugin için `openclaw plugins inspect <id> --runtime --json` çalıştırın ve `channels`, `channelConfigs`, `tools` ile tanılamaları karşılaştırın.
  * Plugin paketlerini kurduktan veya kaldırdıktan sonra kalıcı metadata'nın geçerli kurulumu yansıtması için `openclaw plugins registry --refresh` çalıştırın.
  * Kurulum, kayıt defteri veya yapılandırma değişikliklerinden sonra Gateway'i yeniden başlatın.


Düzeltme seçenekleri:

  * Bir Plugin aynı kanal kimliği için bilerek başka birinin yerine geçiyorsa, tercih edilen Plugin düşük öncelikli Plugin kimliğiyle `channelConfigs.<channel-id>.preferOver` bildirmelidir. Bkz. [/plugins/manifest#replacing-another-channel-plugin](</tr/plugins/manifest#replacing-another-channel-plugin>).
  * Yinelenme kazara oluştuysa bir tarafı `plugins.entries.<plugin-id>.enabled: false` ile devre dışı bırakın veya eski Plugin kurulumunu kaldırın.
  * Her iki Plugin'i de açıkça etkinleştirdiyseniz OpenClaw bu isteği korur ve çakışmayı bildirir. Kanal için tek bir sahip seçin veya runtime yüzeyinin belirsiz olmaması için Plugin'e ait araçları yeniden adlandırın.


## Plugin slotları (özel kategoriler)

Bazı kategoriler özeldir (bir seferde yalnızca biri etkin):

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-core", // or "none" to disable      contextEngine: "legacy", // or a plugin id    },  },}
[/code]

Slot | Neyi denetler | Varsayılan  
---|---|---  
`memory` | Etkin bellek Plugin'i | `memory-core`  
`contextEngine` | Etkin bağlam motoru | `legacy` (yerleşik)  
  
## CLI başvurusu

bashCopy code
[code]
    openclaw plugins list                       # compact inventoryopenclaw plugins list --enabled            # only enabled pluginsopenclaw plugins list --verbose            # per-plugin detail linesopenclaw plugins list --json               # machine-readable inventoryopenclaw plugins search <query>            # search ClawHub plugin catalogopenclaw plugins inspect <id>              # static detailopenclaw plugins inspect <id> --runtime    # registered hooks/tools/CLI/gateway methodsopenclaw plugins inspect <id> --json       # machine-readableopenclaw plugins inspect --all             # fleet-wide tableopenclaw plugins info <id>                 # inspect aliasopenclaw plugins doctor                    # diagnosticsopenclaw plugins registry                  # inspect persisted registry stateopenclaw plugins registry --refresh        # rebuild persisted registryopenclaw doctor --fix                      # repair plugin registry state openclaw plugins install <package>         # install from npm by defaultopenclaw plugins install clawhub:<pkg>     # install from ClawHub onlyopenclaw plugins install npm:<pkg>         # install from npm onlyopenclaw plugins install git:<repo>        # install from gitopenclaw plugins install git:<repo>@<ref>  # install from git refopenclaw plugins install <spec> --force    # overwrite existing installopenclaw plugins install <path>            # install from local pathopenclaw plugins install -l <path>         # link (no copy) for devopenclaw plugins install <plugin> --marketplace <source>openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <spec> --pin      # record exact resolved npm specopenclaw plugins install <spec> --dangerously-force-unsafe-installopenclaw plugins update <id-or-npm-spec> # update one pluginopenclaw plugins update <id-or-npm-spec> --dangerously-force-unsafe-installopenclaw plugins update --all            # update allopenclaw plugins uninstall <id>          # remove config and plugin index recordsopenclaw plugins uninstall <id> --keep-filesopenclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json # Verify runtime registrations after install.openclaw plugins inspect <id> --runtime --json # Run plugin-owned CLI commands directly from the OpenClaw root CLI.openclaw <plugin-command> --help openclaw plugins enable <id>openclaw plugins disable <id>
[/code]

Birlikte gelen Plugin'ler OpenClaw ile sunulur. Birçoğu varsayılan olarak etkindir (örneğin birlikte gelen model sağlayıcıları, birlikte gelen konuşma sağlayıcıları ve birlikte gelen tarayıcı Plugin'i). Diğer birlikte gelen Plugin'ler yine de `openclaw plugins enable <id>` gerektirir.

`--force`, mevcut kurulu bir Plugin'in veya hook paketinin üzerine yerinde yazar. İzlenen npm Plugin'lerinin rutin yükseltmeleri için `openclaw plugins update <id-or-npm-spec>` kullanın. Yönetilen bir kurulum hedefinin üzerine kopyalamak yerine kaynak yolunu yeniden kullanan `--link` ile desteklenmez.

`plugins.allow` zaten ayarlıysa, `openclaw plugins install` kurulu Plugin kimliğini etkinleştirmeden önce bu izin listesine ekler. Aynı Plugin kimliği `plugins.deny` içinde mevcutsa, kurulum bu eski deny girişini kaldırır; böylece açık kurulum yeniden başlatmadan sonra hemen yüklenebilir olur.

OpenClaw, Plugin envanteri, katkı sahipliği ve başlatma planlaması için soğuk okuma modeli olarak kalıcı bir yerel Plugin kayıt defteri tutar. Kurulum, güncelleme, kaldırma, etkinleştirme ve devre dışı bırakma akışları, Plugin durumunu değiştirdikten sonra bu kayıt defterini yeniler. Aynı `plugins/installs.json` dosyası, üst düzey `installRecords` içinde kalıcı kurulum meta verilerini ve `plugins` içinde yeniden oluşturulabilir manifest meta verilerini tutar. Kayıt defteri eksik, eski veya geçersizse, `openclaw plugins registry --refresh` manifest görünümünü, Plugin çalışma zamanı modüllerini yüklemeden kurulum kayıtlarından, yapılandırma politikasından ve manifest/paket meta verilerinden yeniden oluşturur.

Nix modunda (`OPENCLAW_NIX_MODE=1`), Plugin yaşam döngüsü değiştiricileri devre dışıdır. Bunun yerine kurulum için Plugin paket seçimini ve yapılandırmayı Nix kaynağı üzerinden yönetin; nix-openclaw için ajan öncelikli [Hızlı Başlangıç](<https://github.com/openclaw/nix-openclaw#quick-start>) ile başlayın. `openclaw plugins update <id-or-npm-spec>` izlenen kurulumlara uygulanır. Bir dist-tag veya tam sürüm içeren bir npm paket belirtimi geçirmek, paket adını izlenen Plugin kaydına geri çözer ve gelecekteki güncellemeler için yeni belirtimi kaydeder. Paket adını sürümsüz geçirmek, tam sabitlenmiş bir kurulumu kayıt defterinin varsayılan yayın hattına geri taşır. Kurulu npm Plugin'i çözümlenen sürümle ve kaydedilen artifact kimliğiyle zaten eşleşiyorsa, OpenClaw indirme, yeniden kurma veya yapılandırmayı yeniden yazma yapmadan güncellemeyi atlar. `openclaw update` beta kanalında çalıştığında, varsayılan hat npm ve ClawHub Plugin kayıtları önce `@beta` dener ve Plugin beta yayını yoksa varsayılan/latest'e geri döner. Tam sürümler ve açık etiketler sabitlenmiş kalır.

`--pin` yalnızca npm içindir. `--marketplace` ile desteklenmez, çünkü marketplace kurulumları npm belirtimi yerine marketplace kaynak meta verilerini kalıcı hale getirir.

`--dangerously-force-unsafe-install`, yerleşik tehlikeli kod tarayıcısından gelen yanlış pozitifler için son çare geçersiz kılmadır. Plugin kurulumlarının ve Plugin güncellemelerinin yerleşik `critical` bulgularını aşarak devam etmesine izin verir, ancak yine de Plugin `before_install` politika engellerini veya tarama hatası engellemesini atlamaz. Kurulum taramaları, paketlenmiş test mock'larını engellememek için `tests/`, `__tests__/`, `*.test.*` ve `*.spec.*` gibi yaygın test dosyalarını ve dizinlerini yok sayar; bildirilmiş Plugin çalışma zamanı giriş noktaları bu adlardan birini kullansa bile yine de taranır.

Bu CLI bayrağı yalnızca Plugin kurulum/güncelleme akışları için geçerlidir. Gateway destekli skill bağımlılık kurulumları bunun yerine eşleşen `dangerouslyForceUnsafeInstall` istek geçersiz kılmasını kullanırken, `openclaw skills install` ayrı ClawHub skill indirme/kurulum akışı olarak kalır.

ClawHub'da yayımladığınız bir Plugin bir tarama tarafından gizlenir veya engellenirse, ClawHub panosunu açın ya da ClawHub'dan tekrar kontrol etmesini istemek için `clawhub package rescan <name>` çalıştırın. `--dangerously-force-unsafe-install` yalnızca kendi makinenizdeki kurulumları etkiler; ClawHub'dan Plugin'i yeniden taramasını istemez veya engellenmiş bir yayını herkese açık yapmaz.

Uyumlu paketler aynı Plugin listeleme/inceleme/etkinleştirme/devre dışı bırakma akışına katılır. Geçerli çalışma zamanı desteği; paket Skills'lerini, Claude command-skills'lerini, Claude `settings.json` varsayılanlarını, Claude `.lsp.json` ve manifestte bildirilen `lspServers` varsayılanlarını, Cursor command-skills'lerini ve uyumlu Codex hook dizinlerini içerir.

`openclaw plugins inspect <id>` ayrıca algılanan paket yeteneklerini ve paket destekli Plugin'ler için desteklenen veya desteklenmeyen MCP ve LSP sunucu girişlerini bildirir.

Marketplace kaynakları, `~/.claude/plugins/known_marketplaces.json` içinden bir Claude bilinen marketplace adı, yerel bir marketplace kökü veya `marketplace.json` yolu, `owner/repo` gibi bir GitHub kısaltması, bir GitHub repo URL'si ya da bir git URL'si olabilir. Uzak marketplace'ler için Plugin girişleri klonlanan marketplace repo'su içinde kalmalı ve yalnızca göreli yol kaynakları kullanmalıdır.

Tam ayrıntılar için [`openclaw plugins` CLI referansına](</tr/cli/plugins>) bakın.

## Plugin API genel bakışı

Yerel Plugin'ler, `register(api)` gösteren bir giriş nesnesi dışa aktarır. Eski Plugin'ler hâlâ eski bir takma ad olarak `activate(api)` kullanabilir, ancak yeni Plugin'ler `register` kullanmalıdır.

typescriptCopy code
[code]
    export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  register(api) {    api.registerProvider({      /* ... */    });    api.registerTool({      /* ... */    });    api.registerChannel({      /* ... */    });  },});
[/code]

OpenClaw, giriş nesnesini yükler ve Plugin etkinleştirme sırasında `register(api)` çağırır. Yükleyici eski Plugin'ler için hâlâ `activate(api)` kullanmaya geri döner, ancak birlikte gelen Plugin'ler ve yeni harici Plugin'ler `register` öğesini genel sözleşme olarak ele almalıdır.

`api.registrationMode`, bir Plugin'e girişinin neden yüklendiğini söyler:

Mod | Anlam  
---|---  
`full` | Çalışma zamanı etkinleştirme. Araçları, hook'ları, hizmetleri, komutları, rotaları ve diğer canlı yan etkileri kaydedin.  
`discovery` | Salt okunur yetenek keşfi. Sağlayıcıları ve meta verileri kaydedin; güvenilir Plugin giriş kodu yüklenebilir, ancak canlı yan etkileri atlayın.  
`setup-only` | Hafif bir kurulum girişi üzerinden kanal kurulum meta verisi yükleme.  
`setup-runtime` | Çalışma zamanı girişine de ihtiyaç duyan kanal kurulum yüklemesi.  
`cli-metadata` | Yalnızca CLI komut meta verisi toplama.  
  
Soketler, veritabanları, arka plan worker'ları veya uzun ömürlü istemciler açan Plugin girişleri bu yan etkileri `api.registrationMode === "full"` ile korumalıdır. Keşif yüklemeleri, etkinleştirme yüklemelerinden ayrı olarak önbelleğe alınır ve çalışan Gateway kayıt defterinin yerini almaz. Keşif etkinleştirme yapmaz, ancak import-free değildir: OpenClaw, snapshot oluşturmak için güvenilir Plugin girişini veya kanal Plugin modülünü değerlendirebilir. Modül üst düzeylerini hafif ve yan etkisiz tutun; ağ istemcilerini, alt süreçleri, dinleyicileri, kimlik bilgisi okumalarını ve hizmet başlatmayı tam çalışma zamanı yollarının arkasına taşıyın.

Yaygın kayıt yöntemleri:

Yöntem | Kaydettiği şey  
---|---  
`registerProvider` | Model sağlayıcısı (LLM)  
`registerChannel` | Sohbet kanalı  
`registerTool` | Ajan aracı  
`registerHook` / `on(...)` | Yaşam döngüsü hook'ları  
`registerSpeechProvider` | Metinden konuşmaya / STT  
`registerRealtimeTranscriptionProvider` | Streaming STT  
`registerRealtimeVoiceProvider` | Çift yönlü gerçek zamanlı ses  
`registerMediaUnderstandingProvider` | Görüntü/ses analizi  
`registerImageGenerationProvider` | Görüntü oluşturma  
`registerMusicGenerationProvider` | Müzik oluşturma  
`registerVideoGenerationProvider` | Video oluşturma  
`registerWebFetchProvider` | Web fetch / scrape sağlayıcısı  
`registerWebSearchProvider` | Web arama  
`registerHttpRoute` | HTTP uç noktası  
`registerCommand` / `registerCli` | CLI komutları  
`registerContextEngine` | Bağlam motoru  
`registerService` | Arka plan hizmeti  
  
Türlendirilmiş yaşam döngüsü hook'ları için hook koruma davranışı:

  * `before_tool_call`: `{ block: true }` sonlandırıcıdır; daha düşük öncelikli işleyiciler atlanır.
  * `before_tool_call`: `{ block: false }` no-op'tur ve önceki bir engellemeyi temizlemez.
  * `before_install`: `{ block: true }` sonlandırıcıdır; daha düşük öncelikli işleyiciler atlanır.
  * `before_install`: `{ block: false }` no-op'tur ve önceki bir engellemeyi temizlemez.
  * `message_sending`: `{ cancel: true }` sonlandırıcıdır; daha düşük öncelikli işleyiciler atlanır.
  * `message_sending`: `{ cancel: false }` no-op'tur ve önceki bir iptali temizlemez.


Yerel Codex app-server, Codex'e özgü araç olaylarını bu hook yüzeyine geri köprüler. Plugin'ler yerel Codex araçlarını `before_tool_call` aracılığıyla engelleyebilir, sonuçları `after_tool_call` aracılığıyla gözlemleyebilir ve Codex `PermissionRequest` onaylarına katılabilir. Köprü henüz Codex'e özgü araç argümanlarını yeniden yazmaz. Kesin Codex çalışma zamanı destek sınırı [Codex harness v1 destek sözleşmesi](</tr/plugins/codex-harness-runtime#v1-support-contract>) içinde yer alır.

Tam türlendirilmiş hook davranışı için bkz. [SDK genel bakışı](</tr/plugins/sdk-overview#hook-decision-semantics>).

## İlgili

  * [Plugin oluşturma](</tr/plugins/building-plugins>) \- kendi Plugin'inizi oluşturun
  * [Plugin paketleri](</tr/plugins/bundles>) \- Codex/Claude/Cursor paket uyumluluğu
  * [Plugin bildirimi](</tr/plugins/manifest>) \- bildirim şeması
  * [Araçları kaydetme](</tr/plugins/building-plugins#registering-agent-tools>) \- bir Plugin'e aracı araçları ekleyin
  * [Plugin iç işleyişi](</tr/plugins/architecture>) \- yetenek modeli ve yükleme hattı
  * [ClawHub](</tr/clawhub>) \- üçüncü taraf Plugin keşfi


Was this useful?YesNo