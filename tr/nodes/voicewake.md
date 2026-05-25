---
title: Sesle uyandırma
source_url: https://docs.openclaw.ai/tr/nodes/voicewake
scraped_at: 2026-05-25
---

OpenClaw, **uyandırma sözcüklerini Gateway’in sahibi olduğu tek bir genel liste** olarak ele alır.

  * **Düğüm başına özel uyandırma sözcükleri yoktur**.
  * **Herhangi bir düğüm/uygulama kullanıcı arayüzü listeyi düzenleyebilir** ; değişiklikler Gateway tarafından kalıcı hale getirilir ve herkese yayınlanır.
  * macOS ve iOS yerel **Sesle Uyandırma etkin/devre dışı** anahtarlarını korur (yerel kullanıcı deneyimi + izinler farklıdır).
  * Android şu anda Sesle Uyandırma’yı kapalı tutar ve Ses sekmesinde manuel mikrofon akışı kullanır.


## Depolama (Gateway ana makinesi)

Uyandırma sözcükleri gateway makinesinde şurada saklanır:

  * `~/.openclaw/settings/voicewake.json`


Biçim:

jsonCopy code
[code]
    { "triggers": ["openclaw", "claude", "computer"], "updatedAtMs": 1730000000000 }
[/code]

## Protokol

### Yöntemler

  * `voicewake.get` → `{ triggers: string[] }`
  * `{ triggers: string[] }` parametreleriyle `voicewake.set` → `{ triggers: string[] }`


Notlar:

  * Tetikleyiciler normalleştirilir (baştaki/sondaki boşluklar kırpılır, boş değerler atılır). Boş listeler varsayılanlara geri döner.
  * Güvenlik için sınırlar uygulanır (sayı/uzunluk üst sınırları).


### Yönlendirme yöntemleri (tetikleyici → hedef)

  * `voicewake.routing.get` → `{ config: VoiceWakeRoutingConfig }`
  * `{ config: VoiceWakeRoutingConfig }` parametreleriyle `voicewake.routing.set` → `{ config: VoiceWakeRoutingConfig }`


`VoiceWakeRoutingConfig` biçimi:

jsonCopy code
[code]
    {  "version": 1,  "defaultTarget": { "mode": "current" },  "routes": [{ "trigger": "robot wake", "target": { "sessionKey": "agent:main:main" } }],  "updatedAtMs": 1730000000000}
[/code]

Rota hedefleri tam olarak şunlardan birini destekler:

  * `{ "mode": "current" }`
  * `{ "agentId": "main" }`
  * `{ "sessionKey": "agent:main:main" }`


### Olaylar

  * `voicewake.changed` yükü `{ triggers: string[] }`
  * `voicewake.routing.changed` yükü `{ config: VoiceWakeRoutingConfig }`


Bunu kim alır:

  * Tüm WebSocket istemcileri (macOS uygulaması, WebChat vb.)
  * Tüm bağlı düğümler (iOS/Android) ve ayrıca düğüm bağlandığında ilk “geçerli durum” gönderimi olarak.


## İstemci davranışı

### macOS uygulaması

  * `VoiceWakeRuntime` tetikleyicilerini denetlemek için genel listeyi kullanır.
  * Sesle Uyandırma ayarlarında “Tetikleyici sözcükler”i düzenlemek `voicewake.set` çağrısı yapar ve ardından diğer istemcileri eşitlenmiş halde tutmak için yayına güvenir.


### iOS düğümü

  * `VoiceWakeManager` tetikleyici algılaması için genel listeyi kullanır.
  * Ayarlar’da Uyandırma Sözcükleri’ni düzenlemek `voicewake.set` çağrısı yapar (Gateway WS üzerinden) ve ayrıca yerel uyandırma sözcüğü algılamasını duyarlı tutar.


### Android düğümü

  * Sesle Uyandırma şu anda Android çalışma zamanı/Ayarlar’da devre dışıdır.
  * Android sesi, uyandırma sözcüğü tetikleyicileri yerine Ses sekmesinde manuel mikrofon yakalama kullanır.


## İlgili

  * [Konuşma modu](</tr/nodes/talk>)
  * [Ses ve sesli notlar](</tr/nodes/audio>)
  * [Medya anlama](</tr/nodes/media-understanding>)


Was this useful?YesNo