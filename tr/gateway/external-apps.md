---
title: Harici uygulamalar için Gateway entegrasyonları
source_url: https://docs.openclaw.ai/tr/gateway/external-apps
scraped_at: 2026-06-29
---

ReferenceRPC and API

Harici uygulamalar bugün OpenClaw ile Gateway protokolü üzerinden konuşmalıdır. Bir betik, pano, CI işi, IDE eklentisi veya başka bir süreç ajan çalıştırmaları başlatmak, olayları akış olarak almak, sonuçları beklemek, işi iptal etmek veya Gateway kaynaklarını incelemek istediğinde Gateway WebSocket ve RPC yöntemlerini kullanın.

## Bugün neler mevcut

Yüzey | Durum | Ne için kullanılır  
---|---|---  
[Gateway protokolü](</tr/gateway/protocol>) | Hazır | WebSocket taşıması, bağlantı el sıkışması, yetki kapsamları, protokol sürümleme ve olaylar.  
[Gateway RPC başvurusu](</tr/reference/rpc>) | Hazır | Ajanlar, oturumlar, görevler, modeller, araçlar, yapıtlar ve onaylar için mevcut Gateway yöntemleri.  
[`openclaw agent`](</tr/cli/agent>) | Hazır | CLI'ya kabuk üzerinden çıkmanın yeterli olduğu tek seferlik betik entegrasyonu.  
[`openclaw message`](</tr/cli/message>) | Hazır | Betiklerden ileti veya kanal eylemleri gönderme.  
  
Kaynak ağacı, gelecekteki bir istemci kitaplığı için dahili paket çalışmaları içerir, ancak bu herkese açık bir kurulum yüzeyi değildir. Paketler yayımlanıp sürümlenene kadar bunu önizleme uygulama ayrıntısı olarak değerlendirin.

## Önerilen yol

  1. Bir Gateway çalıştırın veya keşfedin.
  2. [Gateway protokolü](</tr/gateway/protocol>) üzerinden bağlanın.
  3. [Gateway RPC başvurusu](</tr/reference/rpc>) içindeki belgelenmiş RPC yöntemlerini çağırın.
  4. Test ettiğiniz OpenClaw sürümünü sabitleyin.
  5. OpenClaw yükseltirken RPC başvurusunu yeniden kontrol edin.


Ajan çalıştırmaları için `agent` RPC ile başlayın ve terminal sonucu gerektiğinde bunu `agent.wait` ile eşleştirin. Kalıcı konuşma durumu için `sessions.*` yöntemlerini kullanın. UI entegrasyonları için Gateway olaylarına abone olun ve yalnızca uygulamanızın anladığı olay ailelerini işleyin.

## Uygulama kodu ve Plugin kodu

Kod OpenClaw dışında yaşadığında Gateway RPC kullanın:

  * Ajan çalıştırmalarını başlatan veya gözlemleyen Node betikleri
  * Bir Gateway çağıran CI işleri
  * panolar ve yönetim panelleri
  * IDE eklentileri
  * kanal Plugin'lerine dönüşmesi gerekmeyen harici köprüler
  * sahte veya gerçek Gateway taşımalarıyla entegrasyon testleri


Kod OpenClaw içinde çalıştığında Plugin SDK kullanın:

  * sağlayıcı Plugin'leri
  * kanal Plugin'leri
  * araç veya yaşam döngüsü kancaları
  * ajan donanımı Plugin'leri
  * güvenilir çalışma zamanı yardımcıları


Harici uygulamalar `openclaw/plugin-sdk/*` içe aktarmamalıdır; bu alt yollar OpenClaw tarafından yüklenen Plugin'ler içindir.

## İlgili

  * [Gateway protokolü](</tr/gateway/protocol>)
  * [Gateway RPC başvurusu](</tr/reference/rpc>)
  * [CLI agent komutu](</tr/cli/agent>)
  * [CLI message komutu](</tr/cli/message>)
  * [Ajan döngüsü](</tr/concepts/agent-loop>)
  * [Ajan çalışma zamanları](</tr/concepts/agent-runtimes>)
  * [Oturumlar](</tr/concepts/session>)
  * [Arka plan görevleri](</tr/automation/tasks>)
  * [ACP ajanları](</tr/tools/acp-agents>)
  * [Plugin SDK genel bakışı](</tr/plugins/sdk-overview>)


Was this useful?YesNo

Open issue