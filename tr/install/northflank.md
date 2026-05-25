---
title: Northflank
source_url: https://docs.openclaw.ai/tr/install/northflank
scraped_at: 2026-05-25
---

# Northflank

OpenClaw'ı Northflank üzerinde tek tıklamalı bir şablonla dağıtın ve web Control UI üzerinden erişin. Bu, "sunucuda terminal yok" için en kolay yoldur: Gateway'i Northflank sizin için çalıştırır.

## Nasıl başlanır

  1. Şablonu açmak için [OpenClaw'ı dağıtın](<https://northflank.com/stacks/deploy-openclaw>) bağlantısına tıklayın.
  2. Henüz yoksa [Northflank üzerinde bir hesap](<https://app.northflank.com/signup>) oluşturun.
  3. **OpenClaw'ı şimdi dağıt** seçeneğine tıklayın.
  4. Gerekli ortam değişkenini ayarlayın: `OPENCLAW_GATEWAY_TOKEN` (güçlü, rastgele bir değer kullanın).
  5. OpenClaw şablonunu derleyip çalıştırmak için **Stack'i dağıt** seçeneğine tıklayın.
  6. Dağıtımın tamamlanmasını bekleyin, ardından **Kaynakları görüntüle** seçeneğine tıklayın.
  7. OpenClaw hizmetini açın.
  8. Genel OpenClaw URL'sinde `/openclaw` yolunu açın ve yapılandırılmış paylaşılan gizli anahtarı kullanarak bağlanın. Bu şablon varsayılan olarak `OPENCLAW_GATEWAY_TOKEN` kullanır; bunu parola kimlik doğrulamasıyla değiştirirseniz onun yerine bu parolayı kullanın.


## Elde ettikleriniz

  * Barındırılan OpenClaw Gateway + Control UI
  * `openclaw.json`, ajan başına `auth-profiles.json`, kanal/sağlayıcı durumu, oturumlar ve çalışma alanının yeniden dağıtımlarda kalıcı olması için Northflank Volume (`/data`) üzerinden kalıcı depolama


## Bir kanal bağlayın

Kanal kurulum yönergeleri için `/openclaw` üzerindeki Control UI'yi kullanın veya SSH üzerinden `openclaw onboard` çalıştırın:

  * [Telegram](</tr/channels/telegram>) (en hızlısı — yalnızca bir bot token'ı)
  * [Discord](</tr/channels/discord>)
  * [Tüm kanallar](</tr/channels>)


## Sonraki adımlar

  * Mesajlaşma kanallarını kurun: [Kanallar](</tr/channels>)
  * Gateway'i yapılandırın: [Gateway yapılandırması](</tr/gateway/configuration>)
  * OpenClaw'ı güncel tutun: [Güncelleme](</tr/install/updating>)


Was this useful?YesNo