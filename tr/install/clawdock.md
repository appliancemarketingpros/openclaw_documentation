---
title: ClawDock
source_url: https://docs.openclaw.ai/tr/install/clawdock
scraped_at: 2026-05-25
---

ClawDock, Docker tabanlı OpenClaw kurulumları için küçük bir shell-yardımcı katmanıdır.

Daha uzun `docker compose ...` çağrıları yerine `clawdock-start`, `clawdock-dashboard` ve `clawdock-fix-token` gibi kısa komutlar sağlar.

Docker'ı henüz kurmadıysanız [Docker](</tr/install/docker>) ile başlayın.

## Kurulum

Standart yardımcı yolunu kullanın:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

ClawDock'u daha önce `scripts/shell-helpers/clawdock-helpers.sh` konumundan kurduysanız, yeni `scripts/clawdock/clawdock-helpers.sh` yolundan yeniden kurun. Eski ham GitHub yolu kaldırıldı.

## Neler sunar

### Temel işlemler

Komut | Açıklama  
---|---  
`clawdock-start` | Gateway'i başlat  
`clawdock-stop` | Gateway'i durdur  
`clawdock-restart` | Gateway'i yeniden başlat  
`clawdock-status` | Konteyner durumunu denetle  
`clawdock-logs` | Gateway günlüklerini takip et  
  
### Konteyner erişimi

Komut | Açıklama  
---|---  
`clawdock-shell` | Gateway konteyneri içinde bir shell aç  
`clawdock-cli <command>` | OpenClaw CLI komutlarını Docker'da çalıştır  
`clawdock-exec <command>` | Konteynerde rastgele bir komut yürüt  
  
### Web arayüzü ve eşleştirme

Komut | Açıklama  
---|---  
`clawdock-dashboard` | Denetim arayüzü URL'sini aç  
`clawdock-devices` | Bekleyen cihaz eşleştirmelerini listele  
`clawdock-approve <id>` | Bir eşleştirme isteğini onayla  
  
### Kurulum ve bakım

Komut | Açıklama  
---|---  
`clawdock-fix-token` | Konteyner içindeki Gateway token'ını yapılandır  
`clawdock-update` | Çek, yeniden oluştur ve yeniden başlat  
`clawdock-rebuild` | Yalnızca Docker imajını yeniden oluştur  
`clawdock-clean` | Konteynerleri ve birimleri kaldır  
  
### Yardımcı araçlar

Komut | Açıklama  
---|---  
`clawdock-health` | Gateway sağlık denetimi çalıştır  
`clawdock-token` | Gateway token'ını yazdır  
`clawdock-cd` | OpenClaw proje dizinine atla  
`clawdock-config` | `~/.openclaw` konumunu aç  
`clawdock-show-config` | Yapılandırma dosyalarını gizlenmiş değerlerle yazdır  
`clawdock-workspace` | Çalışma alanı dizinini aç  
  
## İlk kullanım akışı

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

Tarayıcı eşleştirme gerektiğini söylüyorsa:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Yapılandırma ve gizli bilgiler

ClawDock, [Docker](</tr/install/docker>) içinde açıklanan aynı Docker yapılandırma ayrımıyla çalışır:

  * imaj adı, portlar ve Gateway token'ı gibi Docker'a özgü değerler için `<project>/.env`
  * ortam değişkeni destekli sağlayıcı anahtarları ve bot token'ları için `~/.openclaw/.env`
  * saklanan sağlayıcı OAuth/API anahtarı kimlik doğrulaması için `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
  * davranış yapılandırması için `~/.openclaw/openclaw.json`


`.env` dosyalarını ve `openclaw.json` dosyasını hızlıca incelemek istediğinizde `clawdock-show-config` kullanın. Yazdırılan çıktıda `.env` değerlerini gizler.

## İlgili

[**Docker** OpenClaw için standart Docker kurulumu. ](</tr/install/docker>) [**Docker VM runtime** Güçlendirilmiş yalıtım için Docker tarafından yönetilen VM runtime'ı. ](</tr/install/docker-vm-runtime>) [**Güncelleme** OpenClaw paketini ve yönetilen hizmetleri güncelleme. ](</tr/install/updating>)

Was this useful?YesNo