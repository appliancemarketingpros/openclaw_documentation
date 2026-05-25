---
title: Tarih ve saat
source_url: https://docs.openclaw.ai/tr/date-time
scraped_at: 2026-05-25
---

OpenClaw, **aktarım zaman damgaları için varsayılan olarak ana makine yerel saatini** ve **yalnızca sistem isteminde kullanıcı saat dilimini** kullanır. Araçların kendi yerel anlamlarını koruması için sağlayıcı zaman damgaları korunur (geçerli zaman `session_status` üzerinden kullanılabilir).

## İleti zarfları (varsayılan olarak yerel)

Gelen iletiler bir zaman damgasıyla sarılır (dakika hassasiyeti):

CodeCopy code
[code]
    [Provider ... 2026-01-05 16:26 PST] message text
[/code]

Bu zarf zaman damgası, sağlayıcı saat diliminden bağımsız olarak **varsayılan olarak ana makine yereldir**.

Bu davranışı geçersiz kılabilirsiniz:

json5Copy code
[code]
    {  agents: {    defaults: {      envelopeTimezone: "local", // "utc" | "local" | "user" | IANA timezone      envelopeTimestamp: "on", // "on" | "off"      envelopeElapsed: "on", // "on" | "off"    },  },}
[/code]

  * `envelopeTimezone: "utc"` UTC kullanır.
  * `envelopeTimezone: "local"` ana makine saat dilimini kullanır.
  * `envelopeTimezone: "user"` `agents.defaults.userTimezone` kullanır (ana makine saat dilimine geri döner).
  * Sabit bir bölge için açık bir IANA saat dilimi kullanın (ör. `"America/Chicago"`).
  * `envelopeTimestamp: "off"` zarf başlıklarından mutlak zaman damgalarını kaldırır.
  * `envelopeElapsed: "off"` geçen süre soneklerini kaldırır (`+2m` biçimi).


### Örnekler

**Yerel (varsayılan):**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 PST] hello
[/code]

**Kullanıcı saat dilimi:**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 CST] hello
[/code]

**Geçen süre etkin:**

CodeCopy code
[code]
    [WhatsApp +1555 +30s 2026-01-18T05:19Z] follow-up
[/code]

## Sistem istemi: geçerli tarih ve saat

Kullanıcı saat dilimi biliniyorsa sistem istemi, istem önbelleğe almayı kararlı tutmak için **yalnızca saat dilimi** içeren (saat/zaman biçimi olmayan) özel bir **Geçerli Tarih ve Saat** bölümü içerir:

CodeCopy code
[code]
    Time zone: America/Chicago
[/code]

Ajanın geçerli zamana ihtiyacı olduğunda `session_status` aracını kullanın; durum kartı bir zaman damgası satırı içerir.

## Sistem olayı satırları (varsayılan olarak yerel)

Ajan bağlamına eklenen kuyruğa alınmış sistem olayları, ileti zarflarıyla aynı saat dilimi seçimini kullanan bir zaman damgasıyla öneklenir (varsayılan: ana makine yerel).

CodeCopy code
[code]
    System: [2026-01-12 12:19:17 PST] Model switched.
[/code]

### Kullanıcı saat dilimini ve biçimini yapılandırma

json5Copy code
[code]
    {  agents: {    defaults: {      userTimezone: "America/Chicago",      timeFormat: "auto", // auto | 12 | 24    },  },}
[/code]

  * `userTimezone`, istem bağlamı için **kullanıcı yerel saat dilimini** ayarlar.
  * `timeFormat`, istemdeki **12 saat/24 saat gösterimini** denetler. `auto`, işletim sistemi tercihlerini izler.


## Zaman biçimi algılama (auto)

`timeFormat: "auto"` olduğunda OpenClaw, işletim sistemi tercihini (macOS/Windows) inceler ve yerel ayar biçimlendirmesine geri döner. Algılanan değer, yinelenen sistem çağrılarını önlemek için **işlem başına önbelleğe alınır**.

## Araç yükleri ve bağlayıcılar (ham sağlayıcı zamanı + normalleştirilmiş alanlar)

Kanal araçları **sağlayıcıya özgü zaman damgalarını** döndürür ve tutarlılık için normalleştirilmiş alanlar ekler:

  * `timestampMs`: epoch milisaniyesi (UTC)
  * `timestampUtc`: ISO 8601 UTC dizesi


Hiçbir şeyin kaybolmaması için ham sağlayıcı alanları korunur.

  * Slack: API'den epoch benzeri dizeler
  * Discord: UTC ISO zaman damgaları
  * Telegram/WhatsApp: sağlayıcıya özgü sayısal/ISO zaman damgaları


Yerel saate ihtiyacınız varsa bilinen saat dilimini kullanarak aşağı akışta dönüştürün.

## İlgili belgeler

  * [Sistem İstemi](</tr/concepts/system-prompt>)
  * [Saat Dilimleri](</tr/concepts/timezone>)
  * [İletiler](</tr/concepts/messages>)


Was this useful?YesNo