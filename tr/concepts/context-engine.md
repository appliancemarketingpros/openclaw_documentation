---
title: Bağlam motoru
source_url: https://docs.openclaw.ai/tr/concepts/context-engine
scraped_at: 2026-05-25
---

Bir **bağlam motoru** , OpenClaw'ın her çalışma için model bağlamını nasıl oluşturacağını denetler: hangi iletilerin dahil edileceği, eski geçmişin nasıl özetleneceği ve alt ajan sınırları boyunca bağlamın nasıl yönetileceği.

OpenClaw, yerleşik bir `legacy` motoruyla gelir ve varsayılan olarak bunu kullanır - çoğu kullanıcının bunu değiştirmesi gerekmez. Bir Plugin motorunu yalnızca farklı derleme, Compaction veya oturumlar arası hatırlama davranışı istediğinizde kurup seçin.

## Hızlı başlangıç

* ### Hangi motorun etkin olduğunu denetleyin

bashCopy code
[code]
    openclaw doctor# or inspect config directly:cat ~/.openclaw/openclaw.json | jq '.plugins.slots.contextEngine'
[/code]

* ### Bir Plugin motoru kurun

Bağlam motoru Plugin'leri, diğer OpenClaw Plugin'leri gibi kurulur.

### npm'den

bashCopy code
[code]
    openclaw plugins install @martian-engineering/lossless-claw
[/code]

### Yerel bir yoldan

bashCopy code
[code]
    openclaw plugins install -l ./my-context-engine
[/code]

* ### Motoru etkinleştirin ve seçin

json5Copy code
[code]
    // openclaw.json{  plugins: {    slots: {      contextEngine: "lossless-claw", // must match the plugin's registered engine id    },    entries: {      "lossless-claw": {        enabled: true,        // Plugin-specific config goes here (see the plugin's docs)      },    },  },}
[/code]

Kurup yapılandırdıktan sonra Gateway'i yeniden başlatın.

* ### legacy'ye geri dönün (isteğe bağlı)

`contextEngine` değerini `"legacy"` olarak ayarlayın (veya anahtarı tamamen kaldırın - `"legacy"` varsayılandır).

## Nasıl çalışır

OpenClaw her model istemi çalıştırdığında, bağlam motoru dört yaşam döngüsü noktasında yer alır:

1\. Alma

Oturuma yeni bir ileti eklendiğinde çağrılır. Motor, iletiyi kendi veri deposunda saklayabilir veya dizine ekleyebilir.

2\. Derleme

Her model çalıştırmasından önce çağrılır. Motor, token bütçesine sığan sıralı bir ileti kümesi (ve isteğe bağlı bir `systemPromptAddition`) döndürür.

3\. Sıkıştırma

Bağlam penceresi dolduğunda veya kullanıcı `/compact` çalıştırdığında çağrılır. Motor, yer açmak için eski geçmişi özetler.

4\. Tur sonrası

Bir çalışma tamamlandıktan sonra çağrılır. Motor durumu kalıcı hale getirebilir, arka plan Compaction'ı tetikleyebilir veya dizinleri güncelleyebilir.

Paketli ACP dışı Codex koşum takımı için OpenClaw, derlenen bağlamı Codex geliştirici talimatlarına ve geçerli tur istemine yansıtarak aynı yaşam döngüsünü uygular. Codex, yerel iş parçacığı geçmişine ve yerel sıkıştırıcısına sahip olmaya devam eder.

### Alt ajan yaşam döngüsü (isteğe bağlı)

OpenClaw iki isteğe bağlı alt ajan yaşam döngüsü kancası çağırır:

Bir alt çalışma başlamadan önce paylaşılan bağlam durumunu hazırlar. Kanca üst/alt oturum anahtarlarını, `contextMode` değerini (`isolated` veya `fork`), kullanılabilir transkript kimliklerini/dosyalarını ve isteğe bağlı TTL'yi alır. Bir geri alma tanıtıcısı döndürürse, hazırlık başarılı olduktan sonra oluşturma başarısız olduğunda OpenClaw bunu çağırır.

Bir alt ajan oturumu tamamlandığında veya süpürüldüğünde temizlik yapar.

### Sistem istemi eklemesi

`assemble` yöntemi bir `systemPromptAddition` dizesi döndürebilir. OpenClaw bunu çalışma için sistem isteminin başına ekler. Bu, motorların statik çalışma alanı dosyaları gerektirmeden dinamik hatırlama rehberliği, alma talimatları veya bağlam duyarlı ipuçları eklemesini sağlar.

## legacy motoru

Yerleşik `legacy` motoru, OpenClaw'ın özgün davranışını korur:

  * **Alma** : işlem yapmaz (oturum yöneticisi ileti kalıcılığını doğrudan yönetir).
  * **Derleme** : geçişli (çalışma zamanındaki mevcut temizle → doğrula → sınırla işlem hattı bağlam derlemesini yönetir).
  * **Sıkıştırma** : eski iletilerin tek bir özetini oluşturan ve son iletileri olduğu gibi tutan yerleşik özetleme Compaction'ına devreder.
  * **Tur sonrası** : işlem yapmaz.


legacy motoru araç kaydetmez veya `systemPromptAddition` sağlamaz.

`plugins.slots.contextEngine` ayarlanmadığında (veya `"legacy"` olarak ayarlandığında), bu motor otomatik olarak kullanılır.

## Plugin motorları

Bir Plugin, Plugin API'sini kullanarak bir bağlam motoru kaydedebilir:

tsCopy code
[code]
     export default function register(api) {  api.registerContextEngine("my-engine", (ctx) => ({    info: {      id: "my-engine",      name: "My Context Engine",      ownsCompaction: true,    },     async ingest({ sessionId, message, isHeartbeat }) {      // Store the message in your data store      return { ingested: true };    },     async assemble({ sessionId, messages, tokenBudget, availableTools, citationsMode }) {      // Return messages that fit the budget      return {        messages: buildContext(messages, tokenBudget),        estimatedTokens: countTokens(messages),        systemPromptAddition: buildMemorySystemPromptAddition({          availableTools: availableTools ?? new Set(),          citationsMode,        }),      };    },     async compact({ sessionId, force }) {      // Summarize older context      return { ok: true, compacted: true };    },  }));}
[/code]

`ctx` fabrikası, ilk yaşam döngüsü kancası çalışmadan önce Plugin'lerin ajan başına veya çalışma alanı başına durumu başlatabilmesi için isteğe bağlı `config`, `agentDir` ve `workspaceDir` değerlerini içerir.

Ardından yapılandırmada etkinleştirin:

json5Copy code
[code]
    {  plugins: {    slots: {      contextEngine: "my-engine",    },    entries: {      "my-engine": {        enabled: true,      },    },  },}
[/code]

### ContextEngine arayüzü

Zorunlu üyeler:

Üye | Tür | Amaç  
---|---|---  
`info` | Özellik | Motor kimliği, adı, sürümü ve Compaction'a sahip olup olmadığı  
`ingest(params)` | Yöntem | Tek bir iletiyi saklar  
`assemble(params)` | Yöntem | Bir model çalışması için bağlam oluşturur (`AssembleResult` döndürür)  
`compact(params)` | Yöntem | Bağlamı özetler/azaltır  
  
`assemble`, şunları içeren bir `AssembleResult` döndürür:

Modele gönderilecek sıralı iletiler.

Motorun derlenen bağlamdaki toplam token sayısına ilişkin tahmini. OpenClaw bunu Compaction eşiği kararları ve tanılama raporlaması için kullanır.

Sistem isteminin başına eklenir.

Koşucunun önleyici taşma ön kontrolleri için hangi token tahminini kullanacağını denetler. Varsayılan değer `"assembled"`'dır; bu, yalnızca derlenen istemin tahmininin denetlendiği anlamına gelir - pencerelenmiş, kendi kendine yeterli bir bağlam döndüren motorlar için uygundur. Derlenen görünümünüz yalnızca alttaki transkriptte taşma riskini gizleyebildiğinde `"preassembly_may_overflow"` olarak ayarlayın; bu durumda koşucu, önleyici olarak Compaction yapıp yapmayacağına karar verirken derlenen tahmin ile derleme öncesi (pencerelenmemiş) oturum geçmişi tahmininin maksimumunu alır. Her iki durumda da döndürdüğünüz iletiler yine modelin gördükleridir - `promptAuthority` yalnızca ön kontrolü etkiler.

`compact` bir `CompactResult` döndürür. Compaction etkin transkripti döndürdüğünde, `result.sessionId` ve `result.sessionFile` bir sonraki yeniden denemenin veya turun kullanması gereken ardıl oturumu tanımlar.

İsteğe bağlı üyeler:

Üye | Tür | Amaç  
---|---|---  
`bootstrap(params)` | Yöntem | Bir oturum için motor durumunu başlatır. Motor bir oturumu ilk gördüğünde bir kez çağrılır (ör. geçmişi içe aktarma).  
`ingestBatch(params)` | Yöntem | Tamamlanmış bir turu toplu olarak alır. Bir çalışma tamamlandıktan sonra, o turdaki tüm iletilerle bir kez çağrılır.  
`afterTurn(params)` | Yöntem | Çalışma sonrası yaşam döngüsü işi (durumu kalıcı hale getirme, arka plan Compaction'ı tetikleme).  
`prepareSubagentSpawn(params)` | Yöntem | Başlamadan önce bir alt oturum için paylaşılan durumu ayarlar.  
`onSubagentEnded(params)` | Yöntem | Bir alt ajan sona erdikten sonra temizlik yapar.  
`dispose()` | Yöntem | Kaynakları serbest bırakır. Gateway kapatılırken veya Plugin yeniden yüklenirken çağrılır - oturum başına değil.  
  
### ownsCompaction

`ownsCompaction`, Pi'nin yerleşik deneme içi otomatik Compaction'ının çalışma için etkin kalıp kalmayacağını denetler:

ownsCompaction: true

Motor Compaction davranışına sahiptir. OpenClaw, bu çalışma için Pi'nin yerleşik otomatik Compaction'ını devre dışı bırakır ve motorun `compact()` uygulaması `/compact`, taşma kurtarma Compaction'ı ve `afterTurn()` içinde yapmak istediği her türlü proaktif Compaction'dan sorumludur. OpenClaw yine de istem öncesi taşma korumasını çalıştırabilir; tam transkriptin taşacağını öngördüğünde kurtarma yolu, başka bir istem göndermeden önce etkin motorun `compact()` yöntemini çağırır.

ownsCompaction: false veya ayarlanmamış

Pi'nin yerleşik otomatik Compaction'ı istem yürütme sırasında yine çalışabilir, ancak etkin motorun `compact()` yöntemi `/compact` ve taşma kurtarma için yine çağrılır.

Bu, iki geçerli Plugin deseni olduğu anlamına gelir:

### Sahiplenme modu

Kendi Compaction algoritmanızı uygulayın ve `ownsCompaction: true` olarak ayarlayın.

### Devretme modu

`ownsCompaction: false` olarak ayarlayın ve OpenClaw'ın yerleşik Compaction davranışını kullanmak için `compact()` yönteminin `openclaw/plugin-sdk/core` içinden `delegateCompactionToRuntime(...)` çağırmasını sağlayın.

İşlem yapmayan bir `compact()`, etkin sahiplenmeyen bir motor için güvenli değildir; çünkü o motor yuvası için normal `/compact` ve taşma kurtarma Compaction yolunu devre dışı bırakır.

## Yapılandırma başvurusu

json5Copy code
[code]
    {  plugins: {    slots: {      // Select the active context engine. Default: "legacy".      // Set to a plugin id to use a plugin engine.      contextEngine: "legacy",    },  },}
[/code]

## Compaction ve bellekle ilişki

Compaction

Compaction, bağlam motorunun sorumluluklarından biridir. Eski motor, OpenClaw'ın yerleşik özetlemesine yetki devreder. Plugin motorları herhangi bir compaction stratejisini uygulayabilir (DAG özetleri, vektör geri getirme vb.).

Bellek Plugin'leri

Bellek Plugin'leri (`plugins.slots.memory`) bağlam motorlarından ayrıdır. Bellek Plugin'leri arama/geri getirme sağlar; bağlam motorları modelin ne göreceğini kontrol eder. Birlikte çalışabilirler - bir bağlam motoru, derleme sırasında bellek Plugin verilerini kullanabilir. Etkin bellek istemi yolunu isteyen Plugin motorları, etkin bellek istemi bölümlerini başa eklenmeye hazır bir `systemPromptAddition` değerine dönüştüren `openclaw/plugin-sdk/core` içindeki `buildMemorySystemPromptAddition(...)` öğesini tercih etmelidir. Bir motor daha düşük düzeyli kontrole ihtiyaç duyarsa, `buildActiveMemoryPromptSection(...)` aracılığıyla `openclaw/plugin-sdk/memory-host-core` üzerinden ham satırları yine de çekebilir.

Oturum budama

Eski araç sonuçlarını bellekte kırpma işlemi, hangi bağlam motorunun etkin olduğundan bağımsız olarak çalışmaya devam eder.

## İpuçları

  * Motorunuzun doğru yüklendiğini doğrulamak için `openclaw doctor` kullanın.
  * Motorları değiştiriyorsanız, mevcut oturumlar geçerli geçmişleriyle devam eder. Yeni motor gelecekteki çalıştırmalar için devralır.
  * Motor hataları günlüğe kaydedilir ve tanılamalarda gösterilir. Bir Plugin motoru kaydolamazsa veya seçilen motor kimliği çözümlenemezse, OpenClaw otomatik olarak geri dönmez; Plugin'i düzeltene veya `plugins.slots.contextEngine` değerini tekrar `"legacy"` olarak değiştirene kadar çalıştırmalar başarısız olur.
  * Geliştirme için, yerel bir Plugin dizinini kopyalamadan bağlamak üzere `openclaw plugins install -l ./my-engine` kullanın.


## İlgili

  * [Compaction](</tr/concepts/compaction>) \- uzun konuşmaları özetleme
  * [Bağlam](</tr/concepts/context>) \- ajan dönüşleri için bağlamın nasıl oluşturulduğu
  * [Plugin Mimarisi](</tr/plugins/architecture>) \- bağlam motoru Plugin'lerini kaydetme
  * [Plugin manifesti](</tr/plugins/manifest>) \- Plugin manifest alanları
  * [Plugin'ler](</tr/tools/plugin>) \- Plugin genel bakışı


Was this useful?YesNo