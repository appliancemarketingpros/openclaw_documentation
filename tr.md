---
title: OpenClaw
source_url: https://docs.openclaw.ai/tr
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"EXFOLIATE! EXFOLIATE!"_ — Bir uzay ıstakozu, muhtemelen

**Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo ve daha fazlasında yapay zeka aracıları için her işletim sisteminde çalışan Gateway.**

Bir mesaj gönderin, cebinizden bir aracı yanıtı alın. Yerleşik kanallar, paketli kanal Plugin'leri, WebChat ve mobil düğümler genelinde tek bir Gateway çalıştırın.

[**Başlayın** OpenClaw'ı kurun ve Gateway'i dakikalar içinde çalıştırın. ](</tr/start/getting-started>) [**İlk Kurulumu Çalıştırın** `openclaw onboard` ve eşleştirme akışlarıyla rehberli kurulum. ](</tr/start/wizard>) [**Control UI'ı Açın** Sohbet, yapılandırma ve oturumlar için tarayıcı panosunu başlatın. ](</tr/web/control-ui>)

## OpenClaw nedir?

OpenClaw, favori sohbet uygulamalarınızı ve kanal yüzeylerinizi — Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo ve daha fazlası gibi yerleşik kanallar ile paketli veya harici kanal Plugin'leri — Pi gibi yapay zeka kodlama aracılarına bağlayan **kendi barındırdığınız bir Gateway** 'dir. Kendi makinenizde (veya bir sunucuda) tek bir Gateway süreci çalıştırırsınız ve bu süreç mesajlaşma uygulamalarınız ile her zaman erişilebilir bir yapay zeka asistanı arasında köprü olur.

**Kimler için?** Verilerinin kontrolünden vazgeçmeden veya barındırılan bir hizmete bağlı kalmadan, her yerden mesaj gönderebilecekleri kişisel bir yapay zeka asistanı isteyen geliştiriciler ve ileri düzey kullanıcılar için.

**Onu farklı kılan nedir?**

  * **Kendi barındırdığınız** : donanımınızda, sizin kurallarınızla çalışır
  * **Çok kanallı** : tek bir Gateway, yerleşik kanalları ve paketli ya da harici kanal Plugin'lerini aynı anda sunar
  * **Aracı odaklı** : araç kullanımı, oturumlar, bellek ve çok aracılı yönlendirme özellikleriyle kodlama aracıları için geliştirilmiştir
  * **Açık kaynak** : MIT lisanslı, topluluk odaklı


**Neye ihtiyacınız var?** Node 24 (önerilir) veya uyumluluk için Node 22 LTS (`22.16+`), seçtiğiniz sağlayıcıdan bir API anahtarı ve 5 dakika. En iyi kalite ve güvenlik için mevcut en güçlü son nesil modeli kullanın.

## Nasıl çalışır?
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway; oturumlar, yönlendirme ve kanal bağlantıları için tek doğruluk kaynağıdır.

## Temel yetenekler

[**Çok kanallı Gateway** Tek bir Gateway süreciyle Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat ve daha fazlası. ](</tr/channels>) [**Plugin kanalları** Paketli Plugin'ler, normal güncel sürümlerde Matrix, Nostr, Twitch, Zalo ve daha fazlasını ekler. ](</tr/tools/plugin>) [**Çok aracılı yönlendirme** Aracı, çalışma alanı veya gönderici başına yalıtılmış oturumlar. ](</tr/concepts/multi-agent>) [**Medya desteği** Görsel, ses ve belge gönderip alın. ](</tr/nodes/images>) [**Web Control UI** Sohbet, yapılandırma, oturumlar ve düğümler için tarayıcı panosu. ](</tr/web/control-ui>) [**Mobil düğümler** Canvas, kamera ve ses özellikli iş akışları için iOS ve Android düğümlerini eşleştirin. ](</tr/nodes>)

## Hızlı başlangıç

* ### OpenClaw'ı kurun

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### İlk kurulumu yapın ve hizmeti kurun

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Sohbet edin

Tarayıcınızda Control UI'ı açın ve bir mesaj gönderin:

bashCopy code
[code]
    openclaw dashboard
[/code]

Ya da bir kanal bağlayın ([Telegram](</tr/channels/telegram>) en hızlısıdır) ve telefonunuzdan sohbet edin.

Tam kurulum ve geliştirme ortamı kurulumu mu gerekiyor? [Başlangıç](</tr/start/getting-started>) bölümüne bakın.

## Pano

Gateway başladıktan sonra tarayıcı Control UI'ını açın.

  * Yerel varsayılan: <http://127.0.0.1:18789/>
  * Uzaktan erişim: [Web yüzeyleri](</tr/web>) ve [Tailscale](</tr/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Yapılandırma (isteğe bağlı)

Yapılandırma `~/.openclaw/openclaw.json` konumunda bulunur.

  * **Hiçbir şey yapmazsanız** , OpenClaw paketli Pi ikilisini gönderici başına oturumlarla RPC modunda kullanır.
  * Bunu daha sıkı sınırlamak istiyorsanız, `channels.whatsapp.allowFrom` ve (gruplar için) bahsetme kurallarıyla başlayın.


Örnek:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Buradan başlayın

[**Dokümantasyon merkezleri** Kullanım durumuna göre düzenlenmiş tüm dokümanlar ve kılavuzlar. ](</tr/start/hubs>) [**Yapılandırma** Temel Gateway ayarları, belirteçler ve sağlayıcı yapılandırması. ](</tr/gateway/configuration>) [**Uzaktan erişim** SSH ve tailnet erişim desenleri. ](</tr/gateway/remote>) [**Kanallar** Feishu, Microsoft Teams, WhatsApp, Telegram, Discord ve daha fazlası için kanala özel kurulum. ](</tr/channels/telegram>) [**Düğümler** Eşleştirme, Canvas, kamera ve cihaz eylemleriyle iOS ve Android düğümleri. ](</tr/nodes>) [**Yardım** Yaygın düzeltmeler ve sorun giderme başlangıç noktası. ](</tr/help>)

## Daha fazla bilgi edinin

[**Tam özellik listesi** Eksiksiz kanal, yönlendirme ve medya yetenekleri. ](</tr/concepts/features>) [**Çok aracılı yönlendirme** Çalışma alanı yalıtımı ve aracı başına oturumlar. ](</tr/concepts/multi-agent>) [**Güvenlik** Belirteçler, izin listeleri ve güvenlik denetimleri. ](</tr/gateway/security>) [**Sorun giderme** Gateway tanılama ve yaygın hatalar. ](</tr/gateway/troubleshooting>) [**Hakkında ve katkılar** Projenin kökenleri, katkıda bulunanlar ve lisans. ](</tr/reference/credits>)

Was this useful?YesNo