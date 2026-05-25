---
title: Plugin giriş noktaları
source_url: https://docs.openclaw.ai/tr/plugins/sdk-entrypoints
scraped_at: 2026-05-25
---

Her Plugin varsayılan bir giriş nesnesi dışa aktarır. SDK, bunları oluşturmak için üç yardımcı sağlar.

Yüklü Plugin'ler için `package.json`, mümkün olduğunda çalışma zamanı yüklemesini derlenmiş JavaScript'e yönlendirmelidir:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["./src/index.ts"],    "runtimeExtensions": ["./dist/index.js"],    "setupEntry": "./src/setup-entry.ts",    "runtimeSetupEntry": "./dist/setup-entry.js"  }}
[/code]

`extensions` ve `setupEntry`, çalışma alanı ve git checkout geliştirmesi için geçerli kaynak girişleri olarak kalır. `runtimeExtensions` ve `runtimeSetupEntry`, OpenClaw yüklü bir paketi yüklediğinde tercih edilir ve npm paketlerinin çalışma zamanında TypeScript derlemesinden kaçınmasını sağlar. Açık çalışma zamanı girişleri gereklidir: `runtimeSetupEntry`, `setupEntry` gerektirir ve eksik `runtimeExtensions` veya `runtimeSetupEntry` çıktıları sessizce kaynağa geri dönmek yerine kurulumun/keşfin başarısız olmasına neden olur. Yüklü bir paket yalnızca bir TypeScript kaynak girişi bildirirse, OpenClaw mevcut olduğunda eşleşen derlenmiş `dist/*.js` eşini kullanır, ardından TypeScript kaynağına geri döner.

Tüm giriş yolları Plugin paket dizini içinde kalmalıdır. Çalışma zamanı girişleri ve çıkarımsanan derlenmiş JavaScript eşleri, dışarı kaçan bir `extensions` veya `setupEntry` kaynak yolunu geçerli kılmaz.

## `definePluginEntry`

**İçe aktarma:** `openclaw/plugin-sdk/plugin-entry`

Sağlayıcı Plugin'leri, araç Plugin'leri, kanca Plugin'leri ve mesajlaşma kanalı **olmayan** her şey için.

typescriptCopy code
[code]
     export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Short summary",  register(api) {    api.registerProvider({      /* ... */    });    api.registerTool({      /* ... */    });  },});
[/code]

Alan | Tür | Gerekli | Varsayılan  
---|---|---|---  
`id` | `string` | Evet | -  
`name` | `string` | Evet | -  
`description` | `string` | Evet | -  
`kind` | `string` | Hayır | -  
`configSchema` | `OpenClawPluginConfigSchema | () => OpenClawPluginConfigSchema` | Hayır | Boş nesne şeması  
`register` | `(api: OpenClawPluginApi) => void` | Evet | -  
  
  * `id`, `openclaw.plugin.json` manifestinizle eşleşmelidir.
  * `kind`, özel yuvalar içindir: `"memory"` veya `"context-engine"`.
  * `configSchema`, tembel değerlendirme için bir işlev olabilir.
  * OpenClaw bu şemayı ilk erişimde çözer ve belleğe alır; bu nedenle pahalı şema oluşturucuları yalnızca bir kez çalışır.


## `defineChannelPluginEntry`

**İçe aktarma:** `openclaw/plugin-sdk/channel-core`

`definePluginEntry` öğesini kanala özgü bağlantılarla sarmalar. Otomatik olarak `api.registerChannel({ plugin })` çağırır, isteğe bağlı bir kök yardım CLI metadata bağlantısı sunar ve `registerFull` işlemini kayıt moduna göre kapılar.

typescriptCopy code
[code]
     export default defineChannelPluginEntry({  id: "my-channel",  name: "My Channel",  description: "Short summary",  plugin: myChannelPlugin,  setRuntime: setMyRuntime,  registerCliMetadata(api) {    api.registerCli(/* ... */);  },  registerFull(api) {    api.registerGatewayMethod(/* ... */);  },});
[/code]

Alan | Tür | Gerekli | Varsayılan  
---|---|---|---  
`id` | `string` | Evet | -  
`name` | `string` | Evet | -  
`description` | `string` | Evet | -  
`plugin` | `ChannelPlugin` | Evet | -  
`configSchema` | `OpenClawPluginConfigSchema | () => OpenClawPluginConfigSchema` | Hayır | Boş nesne şeması  
`setRuntime` | `(runtime: PluginRuntime) => void` | Hayır | -  
`registerCliMetadata` | `(api: OpenClawPluginApi) => void` | Hayır | -  
`registerFull` | `(api: OpenClawPluginApi) => void` | Hayır | -  
  
  * `setRuntime`, çalışma zamanı başvurusunu saklayabilmeniz için kayıt sırasında çağrılır (genellikle `createPluginRuntimeStore` aracılığıyla). CLI metadata yakalama sırasında atlanır.
  * `registerCliMetadata`, `api.registrationMode === "cli-metadata"`, `api.registrationMode === "discovery"` ve `api.registrationMode === "full"` sırasında çalışır. Bunu kanalın sahip olduğu CLI tanımlayıcıları için standart yer olarak kullanın; böylece kök yardım etkinleştirmeden kalır, keşif anlık görüntüleri statik komut metadata'sını içerir ve normal CLI komut kaydı tam Plugin yüklemeleriyle uyumlu kalır.
  * Keşif kaydı etkinleştirmesizdir, içe aktarmasız değildir. OpenClaw anlık görüntüyü oluşturmak için güvenilen Plugin girişini ve kanal Plugin modülünü değerlendirebilir; bu nedenle üst düzey içe aktarmaları yan etkisiz tutun ve soketleri, istemcileri, işçileri ve servisleri yalnızca `"full"` yollarının arkasına koyun.
  * `registerFull` yalnızca `api.registrationMode === "full"` olduğunda çalışır. Yalnızca kurulum yüklemesi sırasında atlanır.
  * `definePluginEntry` gibi, `configSchema` tembel bir fabrika olabilir ve OpenClaw çözümlenen şemayı ilk erişimde belleğe alır.
  * Plugin'e ait kök CLI komutları için, komutun kök CLI ayrıştırma ağacından kaybolmadan tembel yüklenmiş kalmasını istediğinizde `api.registerCli(..., { descriptors: [...] })` tercih edin. Eşleştirilmiş düğüm özellik komutları için, komutun `openclaw nodes` altına yerleşmesi amacıyla `api.registerNodeCliFeature(...)` tercih edin. Diğer iç içe Plugin komutları için `parentPath` ekleyin ve komutları kayıtçıya geçirilen `program` nesnesi üzerinde kaydedin; OpenClaw Plugin'i çağırmadan önce bunu üst komuta çözer. Kanal Plugin'leri için, bu tanımlayıcıları `registerCliMetadata(...)` üzerinden kaydetmeyi tercih edin ve `registerFull(...)` öğesini yalnızca çalışma zamanı işlerine odaklı tutun.
  * `registerFull(...)` ayrıca Gateway RPC yöntemleri kaydediyorsa, bunları Plugin'e özgü bir önekte tutun. Ayrılmış çekirdek yönetici ad alanları (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) her zaman `operator.admin` öğesine zorlanır.


## `defineSetupPluginEntry`

**İçe aktarma:** `openclaw/plugin-sdk/channel-core`

Hafif `setup-entry.ts` dosyası için. Çalışma zamanı veya CLI bağlantısı olmadan yalnızca `{ plugin }` döndürür.

typescriptCopy code
[code]
     export default defineSetupPluginEntry(myChannelPlugin);
[/code]

OpenClaw, bir kanal devre dışı, yapılandırılmamış olduğunda veya ertelenmiş yükleme etkinleştirildiğinde tam giriş yerine bunu yükler. Bunun ne zaman önemli olduğunu görmek için [Kurulum ve Yapılandırma](</tr/plugins/sdk-setup#setup-entry>) bölümüne bakın.

Pratikte, `defineSetupPluginEntry(...)` öğesini dar kurulum yardımcı aileleriyle eşleştirin:

  * İçe aktarma açısından güvenli kurulum yama bağdaştırıcıları, arama notu çıktısı, `promptResolvedAllowFrom`, `splitSetupEntries` ve devredilmiş kurulum proxy'leri gibi çalışma zamanı açısından güvenli kurulum yardımcıları için `openclaw/plugin-sdk/setup-runtime`
  * İsteğe bağlı kurulum yüzeyleri için `openclaw/plugin-sdk/channel-setup`
  * Kurulum/yükleme CLI/arşiv/dokümantasyon yardımcıları için `openclaw/plugin-sdk/setup-tools`


Ağır SDK'ları, CLI kaydını ve uzun ömürlü çalışma zamanı servislerini tam girişte tutun.

Kurulum ve çalışma zamanı yüzeylerini ayıran paketlenmiş çalışma alanı kanalları bunun yerine `openclaw/plugin-sdk/channel-entry-contract` içinden `defineBundledChannelSetupEntry(...)` kullanabilir. Bu sözleşme, kurulum girişinin çalışma zamanı ayarlayıcısını sunmaya devam ederken kurulum açısından güvenli Plugin/gizli bilgi dışa aktarımlarını korumasını sağlar:

typescriptCopy code
[code]
     export default defineBundledChannelSetupEntry({  importMetaUrl: import.meta.url,  plugin: {    specifier: "./channel-plugin-api.js",    exportName: "myChannelPlugin",  },  runtime: {    specifier: "./runtime-api.js",    exportName: "setMyChannelRuntime",  },});
[/code]

Bu paketlenmiş sözleşmeyi yalnızca kurulum akışları tam kanal girişi yüklenmeden önce gerçekten hafif bir çalışma zamanı ayarlayıcısına ihtiyaç duyduğunda kullanın.

## Kayıt modu

`api.registrationMode`, Plugin'inizin nasıl yüklendiğini bildirir:

Mod | Ne zaman | Ne kaydedilmeli  
---|---|---  
`"full"` | Normal Gateway başlangıcı | Her şey  
`"discovery"` | Salt okunur yetenek keşfi | Kanal kaydı artı statik CLI tanımlayıcıları; giriş kodu yüklenebilir, ancak soketleri, işçileri, istemcileri ve servisleri atlayın  
`"setup-only"` | Devre dışı/yapılandırılmamış kanal | Yalnızca kanal kaydı  
`"setup-runtime"` | Çalışma zamanı mevcut kurulum akışı | Kanal kaydı artı yalnızca tam giriş yüklenmeden önce gereken hafif çalışma zamanı  
`"cli-metadata"` | Kök yardım / CLI metadata yakalama | Yalnızca CLI tanımlayıcıları  
  
`defineChannelPluginEntry` bu ayrımı otomatik olarak yönetir. Bir kanal için doğrudan `definePluginEntry` kullanıyorsanız, modu kendiniz denetleyin:

typescriptCopy code
[code]
    register(api) {  if (    api.registrationMode === "cli-metadata" ||    api.registrationMode === "discovery" ||    api.registrationMode === "full"  ) {    api.registerCli(/* ... */);    if (api.registrationMode === "cli-metadata") return;  }   api.registerChannel({ plugin: myPlugin });  if (api.registrationMode !== "full") return;   // Heavy runtime-only registrations  api.registerService(/* ... */);}
[/code]

Keşif modu etkinleştirmesiz bir kayıt defteri anlık görüntüsü oluşturur. OpenClaw'ın kanal yeteneklerini ve statik CLI tanımlayıcılarını kaydedebilmesi için yine de Plugin girişini ve kanal Plugin nesnesini değerlendirebilir. Keşifte modül değerlendirmesini güvenilir ancak hafif kabul edin: üst düzeyde ağ istemcileri, alt süreçler, dinleyiciler, veritabanı bağlantıları, arka plan işçileri, kimlik bilgisi okumaları veya diğer canlı çalışma zamanı yan etkileri olmamalıdır.

`"setup-runtime"` öğesini, tam paketlenmiş kanal çalışma zamanına yeniden girmeden yalnızca kurulum başlangıç yüzeylerinin var olması gereken pencere olarak ele alın. Kanal kaydı, kurulum açısından güvenli HTTP rotaları, kurulum açısından güvenli Gateway yöntemleri ve devredilmiş kurulum yardımcıları uygun seçeneklerdir. Ağır arka plan servisleri, CLI kayıtçıları ve sağlayıcı/istemci SDK başlatmaları hâlâ `"full"` içinde olmalıdır.

Özellikle CLI kayıtçıları için:

  * kayıtçı bir veya daha fazla kök komuta sahipse ve OpenClaw'ın gerçek CLI modülünü ilk çağrıda tembel yüklemesini istiyorsanız `descriptors` kullanın
  * bu tanımlayıcıların, kayıtçı tarafından sunulan her üst düzey komut kökünü kapsadığından emin olun
  * tanımlayıcı komut adlarını harf, sayı, kısa çizgi ve alt çizgiyle sınırlı tutun; harf veya sayıyla başlamalıdırlar; OpenClaw bu yapının dışındaki tanımlayıcı adlarını reddeder ve yardımı oluşturmadan önce açıklamalardan terminal kontrol dizilerini kaldırır
  * `commands` öğesini tek başına yalnızca hemen yüklenen uyumluluk yolları için kullanın


## Plugin şekilleri

OpenClaw, yüklenen plugin'leri kayıt davranışlarına göre sınıflandırır:

Şekil | Açıklama  
---|---  
**plain-capability** | Tek bir capability türü (örn. yalnızca provider)  
**hybrid-capability** | Birden fazla capability türü (örn. provider + konuşma)  
**hook-only** | Yalnızca hook'lar, capability yok  
**non-capability** | Araçlar/komutlar/servisler var ancak capability yok  
  
Bir plugin'in şeklini görmek için `openclaw plugins inspect <id>` kullanın.

## İlgili

  * [SDK Genel Bakış](</tr/plugins/sdk-overview>) \- kayıt API'si ve alt yol referansı
  * [Runtime Yardımcıları](</tr/plugins/sdk-runtime>) \- `api.runtime` ve `createPluginRuntimeStore`
  * [Kurulum ve Yapılandırma](</tr/plugins/sdk-setup>) \- manifest, kurulum girdisi, ertelenmiş yükleme
  * [Kanal Plugin'leri](</tr/plugins/sdk-channel-plugins>) \- `ChannelPlugin` nesnesini oluşturma
  * [Provider Plugin'leri](</tr/plugins/sdk-provider-plugins>) \- provider kaydı ve hook'lar


Was this useful?YesNo