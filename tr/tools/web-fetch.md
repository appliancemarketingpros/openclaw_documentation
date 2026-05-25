---
title: Web'den getirme
source_url: https://docs.openclaw.ai/tr/tools/web-fetch
scraped_at: 2026-05-25
---

`web_fetch` aracı düz bir HTTP GET isteği yapar ve okunabilir içeriği çıkarır (HTML'i markdown veya metne dönüştürür). JavaScript **çalıştırmaz**.

JS ağırlıklı siteler veya oturum açma korumalı sayfalar için bunun yerine [Web Tarayıcısı](</tr/tools/browser>) kullanın.

## Hızlı başlangıç

`web_fetch` **varsayılan olarak etkindir** \-- yapılandırma gerekmez. Agent bunu hemen çağırabilir:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## Araç parametreleri

Getirilecek URL. Yalnızca `http(s)`.

Ana içerik çıkarıldıktan sonraki çıktı biçimi.

Çıktıyı bu kadar karakterle sınırlandırır.

## Nasıl çalışır?

* ### Fetch

Chrome benzeri bir User-Agent ve `Accept-Language` başlığıyla bir HTTP GET gönderir. Özel/iç ana makine adlarını engeller ve yönlendirmeleri yeniden denetler.

* ### Extract

HTML yanıtı üzerinde Readability (ana içerik çıkarma) çalıştırır.

* ### Fallback (optional)

Readability başarısız olursa ve Firecrawl yapılandırılmışsa, bot atlatma moduyla Firecrawl API üzerinden yeniden dener.

* ### Cache

Aynı URL'nin tekrar tekrar getirilmesini azaltmak için sonuçlar 15 dakika (yapılandırılabilir) önbelleğe alınır.

## Yapılandırma

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Firecrawl geri dönüşü

Readability çıkarımı başarısız olursa, `web_fetch` bot atlatma ve daha iyi çıkarım için [Firecrawl](</tr/tools/firecrawl>) ile geri dönüş yapabilir:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` SecretRef nesnelerini destekler. Eski `tools.web.fetch.firecrawl.*` yapılandırması `openclaw doctor --fix` tarafından otomatik olarak geçirilir.

Geçerli çalışma zamanı davranışı:

  * `tools.web.fetch.provider`, getirme geri dönüş sağlayıcısını açıkça seçer.
  * `provider` atlanırsa OpenClaw, kullanılabilir kimlik bilgilerinden hazır ilk web-getirme sağlayıcısını otomatik olarak algılar. Sandbox dışında çalışan `web_fetch`, `contracts.webFetchProviders` bildiren ve çalışma zamanında eşleşen bir sağlayıcı kaydeden kurulu plugin'leri kullanabilir. Bugün paketle gelen sağlayıcı Firecrawl'dır.
  * Sandbox içindeki `web_fetch` çağrıları paketle gelen sağlayıcılarla sınırlı kalır.
  * Readability devre dışıysa `web_fetch` doğrudan seçili sağlayıcı geri dönüşüne geçer. Kullanılabilir sağlayıcı yoksa kapalı şekilde başarısız olur.


## Güvenilen env proxy

Dağıtımınız `web_fetch` aracının güvenilen bir dışa giden HTTP(S) proxy üzerinden gitmesini gerektiriyorsa `tools.web.fetch.useTrustedEnvProxy: true` ayarlayın.

Bu modda OpenClaw, isteği göndermeden önce ana makine adına dayalı SSRF denetimlerini yine uygular; ancak yerel DNS sabitlemesi yapmak yerine proxy'nin DNS çözmesine izin verir. Bunu yalnızca proxy operatör denetimindeyse ve DNS çözümlemesinden sonra dışa giden politikayı uyguluyorsa etkinleştirin.

## Sınırlar ve güvenlik

  * `maxChars`, `tools.web.fetch.maxCharsCap` değerine sabitlenir
  * Yanıt gövdesi ayrıştırmadan önce `maxResponseBytes` ile sınırlandırılır; aşırı büyük yanıtlar bir uyarıyla kırpılır
  * Özel/iç ana makine adları engellenir
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` ve `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange`, güvenilen sahte IP proxy yığınları için dar kapsamlı açık katılımlardır; proxy'niz bu sentetik aralıklara sahip değilse ve kendi hedef politikasını uygulamıyorsa bunları ayarsız bırakın
  * Yönlendirmeler denetlenir ve `maxRedirects` ile sınırlandırılır
  * `useTrustedEnvProxy` açık bir katılımdır ve yalnızca DNS çözümlemesinden sonra dışa giden politikayı uygulamaya devam eden operatör denetimli proxy'ler için etkinleştirilmelidir
  * `web_fetch` en iyi çaba esaslıdır -- bazı siteler [Web Tarayıcısı](</tr/tools/browser>) gerektirir


## Araç profilleri

Araç profilleri veya izin listeleri kullanıyorsanız `web_fetch` ya da `group:web` ekleyin:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## İlgili

  * [Web Arama](</tr/tools/web>) \-- web'i birden çok sağlayıcıyla arayın
  * [Web Tarayıcısı](</tr/tools/browser>) \-- JS ağırlıklı siteler için tam tarayıcı otomasyonu
  * [Firecrawl](</tr/tools/firecrawl>) \-- Firecrawl arama ve kazıma araçları


Was this useful?YesNo