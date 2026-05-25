---
title: IRC
source_url: https://docs.openclaw.ai/tr/channels/irc
scraped_at: 2026-05-25
---

IRC'yi OpenClaw'u klasik kanallarda (`#room`) ve doğrudan mesajlarda kullanmak istediğinizde kullanın. IRC, paketle birlikte gelen bir Plugin olarak sunulur, ancak ana yapılandırmada `channels.irc` altında yapılandırılır.

## Hızlı başlangıç

  1. `~/.openclaw/openclaw.json` içinde IRC yapılandırmasını etkinleştirin.
  2. En az şunları ayarlayın:

json5Copy code
[code]
    {  channels: {    irc: {      enabled: true,      host: "irc.example.com",      port: 6697,      tls: true,      nick: "openclaw-bot",      channels: ["#openclaw"],    },  },}
[/code]

Bot koordinasyonu için özel bir IRC sunucusunu tercih edin. Bilerek herkese açık bir IRC ağı kullanıyorsanız yaygın seçenekler arasında Libera.Chat, OFTC ve Snoonet bulunur. Bot veya sürü arka kanal trafiği için tahmin edilebilir herkese açık kanallardan kaçının.

  3. Gateway'i başlatın/yeniden başlatın:

bashCopy code
[code]
    openclaw gateway run
[/code]

## Güvenlik varsayılanları

  * IRC, OpenClaw operatörü tarafından yönetilen ileri proxy yönlendirmesinin dışında ham TCP/TLS soketleri kullanır. Tüm çıkış trafiğinin bu ileri proxy üzerinden geçmesini gerektiren dağıtımlarda, doğrudan IRC çıkışı açıkça onaylanmadıkça `channels.irc.enabled=false` ayarlayın.
  * `channels.irc.dmPolicy` varsayılan olarak `"pairing"` değerini kullanır.
  * `channels.irc.groupPolicy` varsayılan olarak `"allowlist"` değerini kullanır.
  * `groupPolicy="allowlist"` ile izin verilen kanalları tanımlamak için `channels.irc.groups` ayarlayın.
  * Düz metin aktarımı bilerek kabul etmiyorsanız TLS (`channels.irc.tls=true`) kullanın.


## Erişim denetimi

IRC kanalları için iki ayrı "kapı" vardır:

  1. **Kanal erişimi** (`groupPolicy` \+ `groups`): botun bir kanaldan mesaj kabul edip etmeyeceği.
  2. **Gönderen erişimi** (`groupAllowFrom` / kanal başına `groups["#channel"].allowFrom`): o kanal içinde botu kimin tetikleyebileceği.


Yapılandırma anahtarları:

  * DM izin listesi (DM gönderen erişimi): `channels.irc.allowFrom`
  * Grup gönderen izin listesi (kanal gönderen erişimi): `channels.irc.groupAllowFrom`
  * Kanal başına denetimler (kanal + gönderen + bahsetme kuralları): `channels.irc.groups["#channel"]`
  * `channels.irc.groupPolicy="open"` yapılandırılmamış kanallara izin verir (**varsayılan olarak yine de bahsetme kapılıdır**)


İzin listesi girdileri kararlı gönderen kimlikleri (`nick!user@host`) kullanmalıdır. Yalnız nick eşleştirmesi değişkendir ve yalnızca `channels.irc.dangerouslyAllowNameMatching: true` olduğunda etkinleştirilir.

### Yaygın tuzak: `allowFrom` DM'ler içindir, kanallar için değil

Şuna benzer günlükler görürseniz:

  * `irc: drop group sender alice!ident@host (policy=allowlist)`


...bu, gönderenin **grup/kanal** mesajları için izinli olmadığı anlamına gelir. Bunu şu yollardan biriyle düzeltin:

  * `channels.irc.groupAllowFrom` ayarlayarak (tüm kanallar için genel), veya
  * kanal başına gönderen izin listeleri ayarlayarak: `channels.irc.groups["#channel"].allowFrom`


Örnek (`#tuirc-dev` içindeki herkesin botla konuşmasına izin ver):

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": { allowFrom: ["*"] },      },    },  },}
[/code]

## Yanıt tetikleme (bahsetmeler)

Bir kanala izin verilmiş olsa (`groupPolicy` \+ `groups` üzerinden) ve gönderene izin verilmiş olsa bile, OpenClaw grup bağlamlarında varsayılan olarak **bahsetme kapısı** kullanır.

Bu, mesaj botla eşleşen bir bahsetme deseni içermediği sürece `drop channel … (missing-mention)` gibi günlükler görebileceğiniz anlamına gelir.

Botun bir IRC kanalında **bahsetmeye gerek kalmadan** yanıt vermesini sağlamak için o kanalda bahsetme kapısını devre dışı bırakın:

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": {          requireMention: false,          allowFrom: ["*"],        },      },    },  },}
[/code]

Ya da **tüm** IRC kanallarına izin vermek (kanal başına izin listesi olmadan) ve yine de bahsetmeler olmadan yanıt vermek için:

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "open",      groups: {        "*": { requireMention: false, allowFrom: ["*"] },      },    },  },}
[/code]

## Güvenlik notu (herkese açık kanallar için önerilir)

Herkese açık bir kanalda `allowFrom: ["*"]` değerine izin verirseniz herkes botu yönlendirebilir. Riski azaltmak için o kanalın araçlarını kısıtlayın.

### Kanaldaki herkes için aynı araçlar

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          tools: {            deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],          },        },      },    },  },}
[/code]

### Gönderen başına farklı araçlar (sahip daha fazla yetki alır)

`"*"` için daha sıkı, kendi nick'iniz için daha gevşek bir ilke uygulamak üzere `toolsBySender` kullanın:

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          toolsBySender: {            "*": {              deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],            },            "id:eigen": {              deny: ["gateway", "nodes", "cron"],            },          },        },      },    },  },}
[/code]

Notlar:

  * `toolsBySender` anahtarları IRC gönderen kimliği değerleri için `id:` kullanmalıdır: daha güçlü eşleştirme için `id:eigen` veya `id:eigen!~eigen@174.127.248.171`.
  * Eski, öneksiz anahtarlar hâlâ kabul edilir ve yalnızca `id:` olarak eşleştirilir.
  * İlk eşleşen gönderen ilkesi kazanır; `"*"` joker geri dönüşüdür.


Grup erişimi ile bahsetme kapısı (ve bunların nasıl etkileştiği) hakkında daha fazla bilgi için bkz.: [/channels/groups](</tr/channels/groups>).

## NickServ

Bağlandıktan sonra NickServ ile kimlik doğrulamak için:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        enabled: true,        service: "NickServ",        password: "your-nickserv-password",      },    },  },}
[/code]

Bağlanırken isteğe bağlı tek seferlik kayıt:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        register: true,        registerEmail: "bot@example.com",      },    },  },}
[/code]

Tekrarlanan REGISTER denemelerini önlemek için nick kaydedildikten sonra `register` değerini devre dışı bırakın.

## Ortam değişkenleri

Varsayılan hesap şunları destekler:

  * `IRC_HOST`
  * `IRC_PORT`
  * `IRC_TLS`
  * `IRC_NICK`
  * `IRC_USERNAME`
  * `IRC_REALNAME`
  * `IRC_PASSWORD`
  * `IRC_CHANNELS` (virgülle ayrılmış)
  * `IRC_NICKSERV_PASSWORD`
  * `IRC_NICKSERV_REGISTER_EMAIL`


`IRC_HOST` bir çalışma alanı `.env` dosyasından ayarlanamaz; bkz. [Çalışma alanı `.env` dosyaları](</tr/gateway/security>).

## Sorun giderme

  * Bot bağlanıyor ancak kanallarda hiç yanıt vermiyorsa `channels.irc.groups` değerini **ve** bahsetme kapısının mesajları düşürüp düşürmediğini (`missing-mention`) doğrulayın. Ping'ler olmadan yanıt vermesini istiyorsanız kanal için `requireMention:false` ayarlayın.
  * Oturum açma başarısız olursa nick kullanılabilirliğini ve sunucu parolasını doğrulayın.
  * Özel bir ağda TLS başarısız olursa ana makine/bağlantı noktası ve sertifika kurulumunu doğrulayın.


## İlgili

  * [Kanallara Genel Bakış](</tr/channels>) — desteklenen tüm kanallar
  * [Eşleme](</tr/channels/pairing>) — DM kimlik doğrulaması ve eşleme akışı
  * [Gruplar](</tr/channels/groups>) — grup sohbeti davranışı ve bahsetme kapısı
  * [Kanal Yönlendirme](</tr/channels/channel-routing>) — mesajlar için oturum yönlendirme
  * [Güvenlik](</tr/gateway/security>) — erişim modeli ve güçlendirme


Was this useful?YesNo