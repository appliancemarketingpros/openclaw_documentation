---
title: Honcho belleği
source_url: https://docs.openclaw.ai/tr/concepts/memory-honcho
scraped_at: 2026-05-25
---

[Honcho](<https://honcho.dev>), OpenClaw'a AI-native bellek ekler. Konuşmaları özel bir hizmette kalıcılaştırır ve zaman içinde kullanıcı ile aracı modelleri oluşturur; böylece aracınıza çalışma alanı Markdown dosyalarının ötesine geçen oturumlar arası bağlam sağlar.

## Sağladıkları

  * **Oturumlar arası bellek** \-- konuşmalar her turdan sonra kalıcılaştırılır, böylece bağlam oturum sıfırlamaları, Compaction ve kanal geçişleri boyunca korunur.
  * **Kullanıcı modelleme** \-- Honcho her kullanıcı için (tercihler, gerçekler, iletişim tarzı) ve aracı için (kişilik, öğrenilmiş davranışlar) bir profil tutar.
  * **Semantik arama** \-- yalnızca geçerli oturumda değil, geçmiş konuşmalardaki gözlemler üzerinde arama yapar.
  * **Çoklu aracı farkındalığı** \-- üst aracılar, oluşturulan alt aracıları otomatik olarak izler; üst aracılar alt oturumlara gözlemci olarak eklenir.


## Kullanılabilir araçlar

Honcho, aracının konuşma sırasında kullanabileceği araçlar kaydeder:

**Veri alma (hızlı, LLM çağrısı yok):**

Araç | Ne yapar  
---|---  
`honcho_context` | Oturumlar arasında tam kullanıcı temsili  
`honcho_search_conclusions` | Saklanan sonuçlar üzerinde semantik arama  
`honcho_search_messages` | Oturumlar arasında mesaj bulur (gönderen, tarih ile filtreler)  
`honcho_session` | Geçerli oturum geçmişi ve özeti  
  
**Soru-cevap (LLM destekli):**

Araç | Ne yapar  
---|---  
`honcho_ask` | Kullanıcı hakkında soru sorar. Gerçekler için `depth='quick'`, sentez için `'thorough'`  
  
## Başlarken

Plugin'i kurun ve kurulumu çalıştırın:

bashCopy code
[code]
    openclaw plugins install @honcho-ai/openclaw-honchoopenclaw honcho setupopenclaw gateway --force
[/code]

Kurulum komutu API kimlik bilgilerinizi ister, config'i yazar ve isteğe bağlı olarak mevcut çalışma alanı bellek dosyalarını taşır.

## Yapılandırma

Ayarlar `plugins.entries["openclaw-honcho"].config` altında bulunur:

json5Copy code
[code]
    {  plugins: {    entries: {      "openclaw-honcho": {        config: {          apiKey: "your-api-key", // self-hosted için atlayın          workspaceId: "openclaw", // bellek yalıtımı          baseUrl: "https://api.honcho.dev",        },      },    },  },}
[/code]

Self-hosted örnekler için `baseUrl` değerini yerel sunucunuza yöneltin (örneğin `http://localhost:8000`) ve API anahtarını atlayın.

## Mevcut belleği taşıma

Mevcut çalışma alanı bellek dosyalarınız varsa (`USER.md`, `MEMORY.md`, `IDENTITY.md`, `memory/`, `canvas/`), `openclaw honcho setup` bunları algılar ve taşımayı önerir.

## Nasıl çalışır

Her AI turundan sonra konuşma Honcho'ya kalıcılaştırılır. Hem kullanıcı hem de aracı mesajları gözlemlenir; bu da Honcho'nun zaman içinde modellerini oluşturup iyileştirmesine olanak tanır.

Konuşma sırasında Honcho araçları hizmeti `before_prompt_build` aşamasında sorgular ve model prompt'u görmeden önce ilgili bağlamı enjekte eder. Bu, doğru tur sınırlarını ve ilgili geri çağırmayı sağlar.

## Honcho ve yerleşik bellek

| Yerleşik / QMD | Honcho  
---|---|---  
**Depolama** | Çalışma alanı Markdown dosyaları | Özel hizmet (yerel veya barındırılan)  
**Oturumlar arası** | Bellek dosyaları aracılığıyla | Otomatik, yerleşik  
**Kullanıcı modelleme** | Manuel (`MEMORY.md` içine yazarak) | Otomatik profiller  
**Arama** | Vektör + anahtar kelime (hibrit) | Gözlemler üzerinde semantik  
**Çoklu aracı** | İzlenmez | Üst/alt farkındalığı  
**Bağımlılıklar** | Yok (yerleşik) veya QMD ikili dosyası | Plugin kurulumu  
  
Honcho ile yerleşik bellek sistemi birlikte çalışabilir. QMD yapılandırıldığında, Honcho'nun oturumlar arası belleği yanında yerel Markdown dosyalarında arama yapmak için ek araçlar kullanılabilir olur.

## CLI komutları

bashCopy code
[code]
    openclaw honcho setup                        # API anahtarını yapılandır ve dosyaları taşıopenclaw honcho status                       # Bağlantı durumunu kontrol etopenclaw honcho ask <question>               # Kullanıcı hakkında Honcho'ya sorgu yapopenclaw honcho search <query> [-k N] [-d D] # Bellek üzerinde semantik arama
[/code]

## Daha fazla okuma

  * [Plugin source code](<https://github.com/plastic-labs/openclaw-honcho>)
  * [Honcho documentation](<https://docs.honcho.dev>)
  * [Honcho OpenClaw integration guide](<https://docs.honcho.dev/v3/guides/integrations/openclaw>)
  * [Memory](</tr/concepts/memory>) \-- OpenClaw bellek genel bakışı
  * [Context Engines](</tr/concepts/context-engine>) \-- Plugin bağlam motorlarının nasıl çalıştığı


## İlgili

  * [Memory overview](</tr/concepts/memory>)
  * [Builtin memory engine](</tr/concepts/memory-builtin>)
  * [QMD memory engine](</tr/concepts/memory-qmd>)


Was this useful?YesNo