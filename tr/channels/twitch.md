---
title: Twitch
source_url: https://docs.openclaw.ai/tr/channels/twitch
scraped_at: 2026-05-25
---

Twitch sohbet desteği, IRC bağlantısı üzerinden sağlanır. OpenClaw, kanallarda mesaj almak ve göndermek için bir Twitch kullanıcısı (bot hesabı) olarak bağlanır.

## Paketle birlikte gelen Plugin

Daha eski bir derlemedeyseniz veya Twitch'i hariç tutan özel bir kurulum kullanıyorsanız npm paketini doğrudan kurun:

### npm registry

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### Local checkout

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

Geçerli resmi yayın etiketini izlemek için yalın paketi kullanın. Tam sürümü yalnızca yeniden üretilebilir bir kurulum gerektiğinde sabitleyin.

Ayrıntılar: [Plugin'ler](</tr/tools/plugin>)

## Hızlı kurulum (başlangıç)

* ### Ensure plugin is available

Mevcut paketlenmiş OpenClaw sürümleri zaten bunu içerir. Daha eski/özel kurulumlar yukarıdaki komutlarla bunu elle ekleyebilir.

* ### Create a Twitch bot account

Bot için ayrılmış bir Twitch hesabı oluşturun (veya mevcut bir hesabı kullanın).

* ### Generate credentials

[Twitch Token Generator](<https://twitchtokengenerator.com/>) kullanın:

  * **Bot Token** seçin
  * `chat:read` ve `chat:write` kapsamlarının seçili olduğunu doğrulayın
  * **Client ID** ve **Access Token** değerlerini kopyalayın


* ### Find your Twitch user ID

Bir kullanıcı adını Twitch kullanıcı kimliğine dönüştürmek için <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/> adresini kullanın.

* ### Configure the token

  * Ortam: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (yalnızca varsayılan hesap)
  * Veya yapılandırma: `channels.twitch.accessToken`


İkisi de ayarlanmışsa yapılandırma önceliklidir (ortam geri dönüşü yalnızca varsayılan hesap içindir).

* ### Start the gateway

Gateway'i yapılandırılmış kanalla başlatın.

En küçük yapılandırma:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## Nedir

  * Gateway tarafından sahiplenilen bir Twitch kanalıdır.
  * Belirleyici yönlendirme: yanıtlar her zaman Twitch'e geri gider.
  * Her hesap, yalıtılmış bir oturum anahtarına eşlenir: `agent:<agentId>:twitch:<accountName>`.
  * `username`, botun hesabıdır (kimlik doğrulayan kişi); `channel`, katılınacak sohbet odasıdır.


## Kurulum (ayrıntılı)

### Kimlik bilgileri oluşturma

[Twitch Token Generator](<https://twitchtokengenerator.com/>) kullanın:

  * **Bot Token** seçin
  * `chat:read` ve `chat:write` kapsamlarının seçili olduğunu doğrulayın
  * **Client ID** ve **Access Token** değerlerini kopyalayın


### Botu yapılandırma

### Env var (default account only)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Config

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

Hem ortam hem de yapılandırma ayarlanmışsa yapılandırma önceliklidir.

### Erişim denetimi (önerilir)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

Kesin bir izin listesi için `allowFrom` tercih edin. Rol tabanlı erişim istiyorsanız bunun yerine `allowedRoles` kullanın.

**Kullanılabilir roller:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## Token yenileme (isteğe bağlı)

[Twitch Token Generator](<https://twitchtokengenerator.com/>) tarafından oluşturulan token'lar otomatik olarak yenilenemez; süresi dolduğunda yeniden oluşturun.

Otomatik token yenileme için [Twitch Developer Console](<https://dev.twitch.tv/console>) üzerinde kendi Twitch uygulamanızı oluşturun ve yapılandırmaya ekleyin:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

Bot, token'ları süresi dolmadan önce otomatik olarak yeniler ve yenileme olaylarını günlüğe kaydeder.

## Çoklu hesap desteği

Hesap başına token'larla `channels.twitch.accounts` kullanın. Paylaşılan desen için [Yapılandırma](</tr/gateway/configuration>) bölümüne bakın.

Örnek (iki kanalda bir bot hesabı):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## Erişim denetimi

### User ID allowlist (most secure)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### Role-based

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` kesin bir izin listesidir. Ayarlandığında yalnızca bu kullanıcı kimliklerine izin verilir. Rol tabanlı erişim istiyorsanız `allowFrom` değerini ayarlamayın ve bunun yerine `allowedRoles` yapılandırın.

### Disable @mention requirement

Varsayılan olarak `requireMention`, `true` değerindedir. Devre dışı bırakmak ve tüm mesajlara yanıt vermek için:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## Sorun giderme

Önce tanılama komutlarını çalıştırın:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

Bot does not respond to messages

  * **Erişim denetimini kontrol edin:** Kullanıcı kimliğinizin `allowFrom` içinde olduğundan emin olun veya test etmek için geçici olarak `allowFrom` değerini kaldırıp `allowedRoles: ["all"]` ayarlayın.
  * **Botun kanalda olduğunu kontrol edin:** Bot, `channel` içinde belirtilen kanala katılmalıdır.

Token issues

"Bağlanılamadı" veya kimlik doğrulama hataları:

  * `accessToken` değerinin OAuth erişim token'ı değeri olduğunu doğrulayın (genellikle `oauth:` ön ekiyle başlar)
  * Token'ın `chat:read` ve `chat:write` kapsamlarına sahip olduğunu kontrol edin
  * Token yenileme kullanıyorsanız `clientSecret` ve `refreshToken` değerlerinin ayarlandığını doğrulayın

Token refresh not working

Yenileme olayları için günlükleri kontrol edin:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

"token refresh disabled (no refresh token)" görürseniz:

  * `clientSecret` sağlandığından emin olun
  * `refreshToken` sağlandığından emin olun


## Yapılandırma

### Hesap yapılandırması

Bot kullanıcı adı.

`chat:read` ve `chat:write` içeren OAuth erişim token'ı.

Twitch Client ID (Token Generator veya uygulamanızdan).

Katılınacak kanal.

Bu hesabı etkinleştir.

İsteğe bağlı: otomatik token yenileme için.

İsteğe bağlı: otomatik token yenileme için.

Token sona erme süresi, saniye cinsinden.

Token'ın alındığı zaman damgası.

Kullanıcı kimliği izin listesi.

@mention gerektir.

### Sağlayıcı seçenekleri

  * `channels.twitch.enabled` \- Kanal başlangıcını etkinleştir/devre dışı bırak
  * `channels.twitch.username` \- Bot kullanıcı adı (basitleştirilmiş tek hesap yapılandırması)
  * `channels.twitch.accessToken` \- OAuth erişim token'ı (basitleştirilmiş tek hesap yapılandırması)
  * `channels.twitch.clientId` \- Twitch Client ID (basitleştirilmiş tek hesap yapılandırması)
  * `channels.twitch.channel` \- Katılınacak kanal (basitleştirilmiş tek hesap yapılandırması)
  * `channels.twitch.accounts.<accountName>` \- Çoklu hesap yapılandırması (yukarıdaki tüm hesap alanları)


Tam örnek:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## Araç eylemleri

Aracı `twitch` çağrısını şu eylemle yapabilir:

  * `send` \- Bir kanala mesaj gönder


Örnek:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## Güvenlik ve operasyon

  * **Token'ları parola gibi ele alın** — Token'ları asla git'e commit etmeyin.
  * **Uzun süre çalışan botlar için otomatik token yenileme kullanın**.
  * **Erişim denetimi için kullanıcı adları yerine kullanıcı kimliği izin listeleri kullanın**.
  * **Token yenileme olayları ve bağlantı durumu için günlükleri izleyin**.
  * **Token kapsamlarını en aza indirin** — Yalnızca `chat:read` ve `chat:write` isteyin.
  * **Takılırsanız** : Oturuma başka hiçbir sürecin sahip olmadığını doğruladıktan sonra Gateway'i yeniden başlatın.


## Sınırlar

  * Mesaj başına **500 karakter** (sözcük sınırlarında otomatik olarak parçalara bölünür).
  * Markdown, parçalara bölmeden önce kaldırılır.
  * Hız sınırlaması yoktur (Twitch'in yerleşik hız sınırlarını kullanır).


## İlgili

  * [Kanal Yönlendirme](</tr/channels/channel-routing>) — mesajlar için oturum yönlendirmesi
  * [Kanallara Genel Bakış](</tr/channels>) — desteklenen tüm kanallar
  * [Gruplar](</tr/channels/groups>) — grup sohbeti davranışı ve mention geçidi
  * [Eşleştirme](</tr/channels/pairing>) — DM kimlik doğrulaması ve eşleştirme akışı
  * [Güvenlik](</tr/gateway/security>) — erişim modeli ve sağlamlaştırma


Was this useful?YesNo