---
title: Farklar
source_url: https://docs.openclaw.ai/tr/tools/diffs
scraped_at: 2026-05-25
---

`diffs`, değişiklik içeriğini aracılar için salt okunur bir diff yapıtına dönüştüren kısa yerleşik sistem rehberliği ve eşlik eden bir beceriye sahip isteğe bağlı bir Plugin aracıdır.

Şunlardan birini kabul eder:

  * `before` ve `after` metni
  * birleşik bir `patch`


Şunları döndürebilir:

  * kanvas sunumu için bir gateway görüntüleyici URL'si
  * ileti teslimi için işlenmiş bir dosya yolu (PNG veya PDF)
  * tek çağrıda her iki çıktı


Etkinleştirildiğinde Plugin, sistem istemi alanına kısa kullanım rehberliği ekler ve aracının daha kapsamlı yönergelere ihtiyaç duyduğu durumlar için ayrıntılı bir beceriyi de kullanıma sunar.

## Hızlı başlangıç

* ### Plugin'i yükleyin

bashCopy code
[code]
    openclaw plugins install diffs
[/code]

* ### Plugin'i etkinleştirin

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,      },    },  },}
[/code]

* ### Bir mod seçin

### view

Kanvas öncelikli akışlar: aracılar `diffs` aracını `mode: "view"` ile çağırır ve `details.viewerUrl` değerini `canvas present` ile açar.

### file

Sohbet dosyası teslimi: aracılar `diffs` aracını `mode: "file"` ile çağırır ve `details.filePath` değerini `message` ile `path` veya `filePath` kullanarak gönderir.

### both

Birleşik: aracılar tek çağrıda iki yapıtı da almak için `diffs` aracını `mode: "both"` ile çağırır.

## Yerleşik sistem rehberliğini devre dışı bırakın

`diffs` aracını etkin tutup yerleşik sistem istemi rehberliğini devre dışı bırakmak istiyorsanız `plugins.entries.diffs.hooks.allowPromptInjection` değerini `false` olarak ayarlayın:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        hooks: {          allowPromptInjection: false,        },      },    },  },}
[/code]

Bu, Plugin'i, aracı ve eşlik eden beceriyi kullanılabilir tutarken diffs Plugin'inin `before_prompt_build` kancasını engeller.

Hem rehberliği hem de aracı devre dışı bırakmak istiyorsanız bunun yerine Plugin'i devre dışı bırakın.

## Tipik aracı iş akışı

* ### diffs'i çağırın

Aracı, `diffs` aracını girdiyle çağırır.

* ### Ayrıntıları okuyun

Aracı, yanıttaki `details` alanlarını okur.

* ### Sunun

Aracı ya `details.viewerUrl` değerini `canvas present` ile açar, `details.filePath` değerini `message` ile `path` veya `filePath` kullanarak gönderir ya da ikisini birden yapar.

## Girdi örnekleri

### Öncesi ve sonrası

jsonCopy code
[code]
    {  "before": "# Hello\n\nOne",  "after": "# Hello\n\nTwo",  "path": "docs/example.md",  "mode": "view"}
[/code]

### Yama

jsonCopy code
[code]
    {  "patch": "diff --git a/src/example.ts b/src/example.ts\n--- a/src/example.ts\n+++ b/src/example.ts\n@@ -1 +1 @@\n-const x = 1;\n+const x = 2;\n",  "mode": "both"}
[/code]

## Araç girdi başvurusu

Belirtilmediği sürece tüm alanlar isteğe bağlıdır.

Özgün metin. `patch` atlandığında `after` ile birlikte gereklidir.

Güncellenmiş metin. `patch` atlandığında `before` ile birlikte gereklidir.

Birleşik diff metni. `before` ve `after` ile karşılıklı olarak dışlayıcıdır.

Öncesi ve sonrası modu için görüntülenecek dosya adı.

Öncesi ve sonrası modu için dil geçersiz kılma ipucu. Bilinmeyen değerler düz metne geri döner.

Görüntüleyici başlığı geçersiz kılma değeri.

Çıktı modu. Varsayılan olarak Plugin varsayılanı `defaults.mode` kullanılır. Kullanımdan kaldırılmış diğer ad: `"image"`, `"file"` gibi davranır ve geriye dönük uyumluluk için hâlâ kabul edilir.

Görüntüleyici teması. Varsayılan olarak Plugin varsayılanı `defaults.theme` kullanılır.

Diff düzeni. Varsayılan olarak Plugin varsayılanı `defaults.layout` kullanılır.

Tam bağlam kullanılabilir olduğunda değişmemiş bölümleri genişletin. Yalnızca çağrı başına seçenek (Plugin varsayılan anahtarı değildir).

İşlenmiş dosya biçimi. Varsayılan olarak Plugin varsayılanı `defaults.fileFormat` kullanılır.

PNG veya PDF işleme için kalite ön ayarı.

Cihaz ölçeği geçersiz kılma değeri (`1`-`4`).

CSS pikseli cinsinden en büyük işleme genişliği (`640`-`2400`).

Görüntüleyici ve bağımsız dosya çıktıları için saniye cinsinden yapıt TTL değeri. En fazla 21600.

Görüntüleyici URL kaynağı geçersiz kılma değeri. Plugin `viewerBaseUrl` değerini geçersiz kılar. Sorgu/hash olmadan `http` veya `https` olmalıdır.

Eski girdi diğer adları

Geriye dönük uyumluluk için hâlâ kabul edilir:

  * `format` -> `fileFormat`
  * `imageFormat` -> `fileFormat`
  * `imageQuality` -> `fileQuality`
  * `imageScale` -> `fileScale`
  * `imageMaxWidth` -> `fileMaxWidth`

Doğrulama ve sınırlar

  * `before` ve `after` her biri en fazla 512 KiB.
  * `patch` en fazla 2 MiB.
  * `path` en fazla 2048 bayt.
  * `lang` en fazla 128 bayt.
  * `title` en fazla 1024 bayt.
  * Yama karmaşıklığı sınırı: en fazla 128 dosya ve toplam 120000 satır.
  * `patch` ile `before` veya `after` birlikte reddedilir.
  * İşlenmiş dosya güvenlik sınırları (PNG ve PDF için geçerlidir): 
    * `fileQuality: "standard"`: en fazla 8 MP (8.000.000 işlenmiş piksel).
    * `fileQuality: "hq"`: en fazla 14 MP (14.000.000 işlenmiş piksel).
    * `fileQuality: "print"`: en fazla 24 MP (24.000.000 işlenmiş piksel).
    * PDF için ayrıca en fazla 50 sayfa sınırı vardır.


## Çıktı ayrıntıları sözleşmesi

Araç, `details` altında yapılandırılmış meta veriler döndürür.

Görüntüleyici alanları

Görüntüleyici oluşturan modlar için ortak alanlar:

  * `artifactId`
  * `viewerUrl`
  * `viewerPath`
  * `title`
  * `expiresAt`
  * `inputKind`
  * `fileCount`
  * `mode`
  * `context` (`agentId`, `sessionId`, `messageChannel`, kullanılabilir olduğunda `agentAccountId`)

Dosya alanları

PNG veya PDF işlendiğinde dosya alanları:

  * `artifactId`
  * `expiresAt`
  * `filePath`
  * `path` (ileti aracı uyumluluğu için `filePath` ile aynı değer)
  * `fileBytes`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`

Uyumluluk diğer adları

Mevcut çağıranlar için ayrıca döndürülür:

  * `format` (`fileFormat` ile aynı değer)
  * `imagePath` (`filePath` ile aynı değer)
  * `imageBytes` (`fileBytes` ile aynı değer)
  * `imageQuality` (`fileQuality` ile aynı değer)
  * `imageScale` (`fileScale` ile aynı değer)
  * `imageMaxWidth` (`fileMaxWidth` ile aynı değer)


Mod davranışı özeti:

Mod | Döndürülenler  
---|---  
`"view"` | Yalnızca görüntüleyici alanları.  
`"file"` | Yalnızca dosya alanları, görüntüleyici yapıtı yok.  
`"both"` | Görüntüleyici alanları ve dosya alanları. Dosya işleme başarısız olursa görüntüleyici yine de `fileError` ve `imageError` diğer adıyla döner.  
  
## Daraltılmış değişmemiş bölümler

  * Görüntüleyici `N unmodified lines` gibi satırlar gösterebilir.
  * Bu satırlardaki genişletme denetimleri koşulludur ve her girdi türü için garanti edilmez.
  * Genişletme denetimleri, işlenmiş diff genişletilebilir bağlam verisine sahip olduğunda görünür; bu, öncesi ve sonrası girdisi için tipiktir.
  * Birçok birleşik yama girdisinde, atlanan bağlam gövdeleri ayrıştırılmış yama hunk'larında kullanılamaz; bu nedenle satır genişletme denetimleri olmadan görünebilir. Bu beklenen davranıştır.
  * `expandUnchanged` yalnızca genişletilebilir bağlam olduğunda uygulanır.


## Plugin varsayılanları

Plugin genelindeki varsayılanları `~/.openclaw/openclaw.json` içinde ayarlayın:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          defaults: {            fontFamily: "Fira Code",            fontSize: 15,            lineSpacing: 1.6,            layout: "unified",            showLineNumbers: true,            diffIndicators: "bars",            wordWrap: true,            background: true,            theme: "dark",            fileFormat: "png",            fileQuality: "standard",            fileScale: 2,            fileMaxWidth: 960,            mode: "both",            ttlSeconds: 21600,          },        },      },    },  },}
[/code]

Desteklenen varsayılanlar:

  * `fontFamily`
  * `fontSize`
  * `lineSpacing`
  * `layout`
  * `showLineNumbers`
  * `diffIndicators`
  * `wordWrap`
  * `background`
  * `theme`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`
  * `mode`
  * `ttlSeconds`


Açık araç parametreleri bu varsayılanları geçersiz kılar.

### Kalıcı görüntüleyici URL yapılandırması

Bir araç çağrısı `baseUrl` iletmediğinde döndürülen görüntüleyici bağlantıları için Plugin'e ait geri dönüş değeri. Sorgu/hash olmadan `http` veya `https` olmalıdır.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          viewerBaseUrl: "https://gateway.example.com/openclaw",        },      },    },  },}
[/code]

## Güvenlik yapılandırması

`false`: görüntüleyici rotalarına local loopback dışı istekler reddedilir. `true`: belirteçli yol geçerliyse uzak görüntüleyicilere izin verilir.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          security: {            allowRemoteViewer: false,          },        },      },    },  },}
[/code]

## Yapıt yaşam döngüsü ve depolama

  * Yapıtlar geçici alt klasör altında depolanır: `$TMPDIR/openclaw-diffs`.
  * Görüntüleyici yapıt meta verileri şunları içerir: 
    * rastgele yapıt kimliği (20 onaltılık karakter)
    * rastgele belirteç (48 onaltılık karakter)
    * `createdAt` ve `expiresAt`
    * depolanan `viewer.html` yolu
  * Belirtilmediğinde varsayılan yapıt TTL değeri 30 dakikadır.
  * Kabul edilen en büyük görüntüleyici TTL değeri 6 saattir.
  * Temizleme, yapıt oluşturulduktan sonra fırsat buldukça çalışır.
  * Süresi dolan yapıtlar silinir.
  * Geri dönüş temizliği, meta veriler eksik olduğunda 24 saatten eski bayat klasörleri kaldırır.


## Görüntüleyici URL'si ve ağ davranışı

Görüntüleyici rotası:

  * `/plugins/diffs/view/{artifactId}/{token}`


Görüntüleyici varlıkları:

  * `/plugins/diffs/assets/viewer.js`
  * `/plugins/diffs/assets/viewer-runtime.js`


Görüntüleyici belgesi bu varlıkları görüntüleyici URL'sine göre çözer; bu nedenle isteğe bağlı bir `baseUrl` yol öneki, iki varlık isteği için de korunur.

URL oluşturma davranışı:

  * Araç çağrısı `baseUrl` sağlanmışsa sıkı doğrulamadan sonra kullanılır.
  * Aksi halde Plugin `viewerBaseUrl` yapılandırılmışsa kullanılır.
  * Her iki geçersiz kılma da yoksa görüntüleyici URL'si varsayılan olarak local loopback `127.0.0.1` değerine ayarlanır.
  * Gateway bağlama modu `custom` ise ve `gateway.customBindHost` ayarlıysa bu host kullanılır.


`baseUrl` kuralları:

  * `http://` veya `https://` olmalıdır.
  * Sorgu ve hash reddedilir.
  * Kaynak ve isteğe bağlı temel yola izin verilir.


## Güvenlik modeli

Görüntüleyici güçlendirmesi

  * Varsayılan olarak yalnızca loopback.
  * Sıkı ID ve token doğrulamalı tokenleştirilmiş görüntüleyici yolları.
  * Görüntüleyici yanıtı CSP: 
    * `default-src 'none'`
    * betikler ve varlıklar yalnızca self kaynağından
    * dışarıya giden `connect-src` yok
  * Uzaktan erişim etkinleştirildiğinde uzak erişim kaçırmaları sınırlanır: 
    * 60 saniyede 40 hata
    * 60 saniyelik kilitleme (`429 Too Many Requests`)

Dosya işleme güçlendirmesi

  * Ekran görüntüsü tarayıcı istek yönlendirmesi varsayılan olarak reddet şeklindedir.
  * Yalnızca `http://127.0.0.1/plugins/diffs/assets/*` içindeki yerel görüntüleyici varlıklarına izin verilir.
  * Harici ağ istekleri engellenir.


## Dosya modu için tarayıcı gereksinimleri

`mode: "file"` ve `mode: "both"` Chromium uyumlu bir tarayıcı gerektirir.

Çözümleme sırası:

* ### Yapılandırma

OpenClaw yapılandırmasında `browser.executablePath`.

* ### Ortam değişkenleri

  * `OPENCLAW_BROWSER_EXECUTABLE_PATH`
  * `BROWSER_EXECUTABLE_PATH`
  * `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`


* ### Platform geri dönüşü

Platform komutu/yolu keşfi geri dönüşü.

Yaygın hata metni:

  * `Diff PNG/PDF rendering requires a Chromium-compatible browser...`


Chrome, Chromium, Edge veya Brave yükleyerek ya da yukarıdaki çalıştırılabilir yol seçeneklerinden birini ayarlayarak düzeltin.

## Sorun giderme

Girdi doğrulama hataları

  * `Provide patch or both before and after text.` — hem `before` hem de `after` ekleyin veya `patch` sağlayın.
  * `Provide either patch or before/after input, not both.` — girdi modlarını karıştırmayın.
  * `Invalid baseUrl: ...` — isteğe bağlı yol içeren, sorgu/hash içermeyen `http(s)` origin kullanın.
  * `{field} exceeds maximum size (...)` — yük boyutunu azaltın.
  * Büyük patch reddi — patch dosyası sayısını veya toplam satır sayısını azaltın.

Görüntüleyici erişilebilirliği

  * Görüntüleyici URL'si varsayılan olarak `127.0.0.1` adresine çözümlenir.
  * Uzaktan erişim senaryolarında şunlardan birini yapın: 
    * Plugin `viewerBaseUrl` ayarını yapın veya
    * araç çağrısı başına `baseUrl` geçirin veya
    * `gateway.bind=custom` ve `gateway.customBindHost` kullanın
  * `gateway.trustedProxies`, aynı ana makinedeki bir proxy için loopback içeriyorsa (örneğin Tailscale Serve), iletilmiş istemci IP başlıkları olmayan ham loopback görüntüleyici istekleri tasarım gereği kapalı başarısız olur.
  * Bu proxy topolojisi için: 
    * yalnızca bir eke ihtiyacınız olduğunda `mode: "file"` veya `mode: "both"` tercih edin ya da
    * paylaşılabilir bir görüntüleyici URL'sine ihtiyacınız olduğunda bilinçli olarak `security.allowRemoteViewer` etkinleştirin ve Plugin `viewerBaseUrl` ayarını yapın veya proxy/herkese açık bir `baseUrl` geçirin
  * `security.allowRemoteViewer` ayarını yalnızca harici görüntüleyici erişimi istediğinizde etkinleştirin.

Değiştirilmemiş satırlar satırında genişletme düğmesi yok

Bu, patch girdisi için patch genişletilebilir bağlam taşımadığında olabilir. Bu beklenen bir durumdur ve görüntüleyici hatasına işaret etmez.

Artefakt bulunamadı

  * Artefakt TTL nedeniyle süresi doldu.
  * Token veya yol değişti.
  * Temizleme eski verileri kaldırdı.


## Operasyonel rehberlik

  * Canvas içinde yerel etkileşimli incelemeler için `mode: "view"` tercih edin.
  * Ek gerektiren dışa dönük sohbet kanalları için `mode: "file"` tercih edin.
  * Dağıtımınız uzak görüntüleyici URL'leri gerektirmedikçe `allowRemoteViewer` devre dışı kalsın.
  * Hassas diff'ler için açık ve kısa `ttlSeconds` ayarlayın.
  * Gerekli olmadığında diff girdisinde gizli bilgiler göndermekten kaçının.
  * Kanalınız görüntüleri agresif biçimde sıkıştırıyorsa (örneğin Telegram veya WhatsApp), PDF çıktısını (`fileFormat: "pdf"`) tercih edin.


## İlgili

  * [Tarayıcı](</tr/tools/browser>)
  * [Pluginler](</tr/tools/plugin>)
  * [Araçlara genel bakış](</tr/tools>)


Was this useful?YesNo