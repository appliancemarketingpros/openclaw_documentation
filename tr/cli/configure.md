---
title: Yapılandır
source_url: https://docs.openclaw.ai/tr/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

Mevcut bir kurulumda hedefli değişiklikler için etkileşimli istem: kimlik bilgileri, cihazlar, agent varsayılanları, Gateway, kanallar, plugins, Skills ve sağlık kontrolleri.

Tam kılavuzlu ilk çalıştırma yolculuğu için `openclaw onboard`, yalnızca temel yapılandırma/çalışma alanı için `openclaw setup` ve yalnızca kanal hesabı kurulumu gerektiğinde `openclaw channels add` kullanın.

Configure bir sağlayıcı kimlik doğrulama seçimiyle başladığında, varsayılan model ve izin listesi seçicileri bu sağlayıcıyı otomatik olarak tercih eder. Volcengine ve BytePlus gibi eşleşmiş sağlayıcılar için aynı tercih, bunların kodlama planı varyantlarıyla da eşleşir (`volcengine-plan/*`, `byteplus-plan/*`). Tercih edilen sağlayıcı filtresi boş bir liste oluşturacaksa configure, boş bir seçici göstermek yerine filtresiz kataloğa geri döner.

Web araması için `openclaw configure --section web`, bir sağlayıcı seçmenizi ve kimlik bilgilerini yapılandırmanızı sağlar. Bazı sağlayıcılar sağlayıcıya özgü takip istemleri de gösterir:

  * **Grok** , aynı `XAI_API_KEY` ile isteğe bağlı `x_search` kurulumu sunabilir ve bir `x_search` modeli seçmenizi sağlayabilir.
  * **Kimi** , Moonshot API bölgesini (`api.moonshot.ai` veya `api.moonshot.cn`) ve varsayılan Kimi web arama modelini sorabilir.


İlgili:

  * Gateway yapılandırma başvurusu: [Yapılandırma](</tr/gateway/configuration>)
  * Config CLI: [Config](</tr/cli/config>)


## Seçenekler

  * `--section <section>`: tekrarlanabilir bölüm filtresi


Kullanılabilir bölümler:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


Notlar:

  * Gateway’in nerede çalışacağını seçmek her zaman `gateway.mode` değerini günceller. İhtiyacınız olan tek şey buysa diğer bölümler olmadan "Devam" seçebilirsiniz.
  * Yerel yapılandırma yazmalarından sonra configure, seçilen kurulum yolu gerektiriyorsa seçili indirilebilir plugins’i yükler. Uzak gateway yapılandırması yerel plugin paketlerini yüklemez.
  * Kanal odaklı hizmetler (Slack/Discord/Matrix/Microsoft Teams), kurulum sırasında kanal/oda izin listeleri için istem gösterir. Adlar veya kimlikler girebilirsiniz; sihirbaz mümkün olduğunda adları kimliklere çözer.
  * Daemon yükleme adımını çalıştırırsanız, token kimlik doğrulaması bir token gerektiriyorsa ve `gateway.auth.token` SecretRef tarafından yönetiliyorsa configure SecretRef’i doğrular, ancak çözümlenmiş düz metin token değerlerini supervisor hizmet ortamı meta verilerine kalıcı olarak yazmaz.
  * Token kimlik doğrulaması bir token gerektiriyorsa ve yapılandırılmış token SecretRef çözümlenemiyorsa configure, daemon yüklemesini uygulanabilir düzeltme rehberliğiyle engeller.
  * Hem `gateway.auth.token` hem de `gateway.auth.password` yapılandırılmışsa ve `gateway.auth.mode` ayarlanmamışsa configure, mode açıkça ayarlanana kadar daemon yüklemesini engeller.


## Örnekler

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Yapılandırma](</tr/gateway/configuration>)


Was this useful?YesNo