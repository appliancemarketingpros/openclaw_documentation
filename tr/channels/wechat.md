---
title: WeChat
source_url: https://docs.openclaw.ai/tr/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw, WeChat'e Tencent'in harici `@tencent-weixin/openclaw-weixin` kanal Plugin'i üzerinden bağlanır.

Durum: harici Plugin. Doğrudan sohbetler ve medya desteklenir. Grup sohbetleri mevcut Plugin yetenek meta verileri tarafından duyurulmaz.

## Adlandırma

  * **WeChat** , bu belgelerde kullanıcıya gösterilen addır.
  * **Weixin** , Tencent paketinin ve Plugin kimliğinin kullandığı addır.
  * `openclaw-weixin`, OpenClaw kanal kimliğidir.
  * `@tencent-weixin/openclaw-weixin`, npm paketidir.


CLI komutlarında ve yapılandırma yollarında `openclaw-weixin` kullanın.

## Nasıl çalışır

WeChat kodu OpenClaw çekirdek deposunda yer almaz. OpenClaw genel kanal Plugin sözleşmesini sağlar, harici Plugin ise WeChat'e özgü çalışma zamanını sağlar:

  1. `openclaw plugins install`, `@tencent-weixin/openclaw-weixin` paketini kurar.
  2. Gateway, Plugin manifestini keşfeder ve Plugin giriş noktasını yükler.
  3. Plugin, `openclaw-weixin` kanal kimliğini kaydeder.
  4. `openclaw channels login --channel openclaw-weixin`, QR ile oturum açmayı başlatır.
  5. Plugin, hesap kimlik bilgilerini OpenClaw durum dizini altında depolar.
  6. Gateway başladığında Plugin, yapılandırılmış her hesap için Weixin izleyicisini başlatır.
  7. Gelen WeChat iletileri kanal sözleşmesi üzerinden normalleştirilir, seçilen OpenClaw aracısına yönlendirilir ve Plugin'in giden yolu üzerinden geri gönderilir.


Bu ayrım önemlidir: OpenClaw çekirdeği kanaldan bağımsız kalmalıdır. WeChat oturum açma, Tencent iLink API çağrıları, medya yükleme/indirme, bağlam belirteçleri ve hesap izleme harici Plugin'in sorumluluğundadır.

## Kurulum

Hızlı kurulum:

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

Elle kurulum:

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

Kurulumdan sonra Gateway'i yeniden başlatın:

bashCopy code
[code]
    openclaw gateway restart
[/code]

## Oturum açma

QR ile oturum açmayı Gateway'in çalıştığı aynı makinede çalıştırın:

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

QR kodunu telefonunuzdaki WeChat ile tarayın ve oturum açmayı onaylayın. Başarılı bir taramadan sonra Plugin hesap belirtecini yerel olarak kaydeder.

Başka bir WeChat hesabı eklemek için aynı oturum açma komutunu yeniden çalıştırın. Birden çok hesap için doğrudan ileti oturumlarını hesaba, kanala ve gönderene göre yalıtın:

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## Erişim denetimi

Doğrudan iletiler, kanal Plugin'leri için normal OpenClaw eşleştirme ve izin listesi modelini kullanır.

Yeni gönderenleri onaylayın:

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

Tam erişim denetimi modeli için bkz. [Eşleştirme](</tr/channels/pairing>).

## Uyumluluk

Plugin, başlangıçta ana makinedeki OpenClaw sürümünü denetler.

Plugin hattı | OpenClaw sürümü | npm etiketi  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
Plugin, OpenClaw sürümünüzün çok eski olduğunu bildirirse OpenClaw'u güncelleyin veya eski Plugin hattını kurun:

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## Yan süreç

WeChat Plugin'i, Tencent iLink API'yi izlerken yardımcı işi Gateway'in yanında çalıştırabilir. #68451 numaralı sorunda bu yardımcı yol, OpenClaw'un genel eski Gateway temizliğinde bir hatayı ortaya çıkardı: bir alt süreç, üst Gateway sürecini temizlemeye çalışabiliyor ve systemd gibi süreç yöneticileri altında yeniden başlatma döngülerine neden olabiliyordu.

Geçerli OpenClaw başlangıç temizliği mevcut süreci ve onun üst süreçlerini hariç tutar; bu nedenle bir kanal yardımcısı, kendisini başlatan Gateway'i sonlandırmamalıdır. Bu düzeltme geneldir; çekirdekte WeChat'e özgü bir yol değildir.

## Sorun giderme

Kurulumu ve durumu denetleyin:

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

Kanal kurulu görünüyor ancak bağlanmıyorsa Plugin'in etkin olduğunu doğrulayın ve yeniden başlatın:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

WeChat etkinleştirildikten sonra Gateway tekrar tekrar yeniden başlıyorsa hem OpenClaw'u hem de Plugin'i güncelleyin:

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

Başlangıç, kurulu Plugin paketinin `requires compiled runtime output for TypeScript entry` gerektirdiğini bildirirse npm paketi, OpenClaw'un ihtiyaç duyduğu derlenmiş JavaScript çalışma zamanı dosyaları olmadan yayımlanmıştır. Plugin yayımcısı düzeltilmiş bir paket yayımladıktan sonra güncelleyin/yeniden kurun veya Plugin'i geçici olarak devre dışı bırakın/kaldırın.

Geçici olarak devre dışı bırakma:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## İlgili belgeler

  * Kanal genel bakışı: [Sohbet Kanalları](</tr/channels>)
  * Eşleştirme: [Eşleştirme](</tr/channels/pairing>)
  * Kanal yönlendirme: [Kanal Yönlendirme](</tr/channels/channel-routing>)
  * Plugin mimarisi: [Plugin Mimarisi](</tr/plugins/architecture>)
  * Kanal Plugin SDK'sı: [Kanal Plugin SDK'sı](</tr/plugins/sdk-channel-plugins>)
  * Harici paket: [@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo