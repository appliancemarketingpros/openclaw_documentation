---
title: SATIR
source_url: https://docs.openclaw.ai/tr/channels/line
scraped_at: 2026-05-25
---

LINE, OpenClaw'a LINE Messaging API üzerinden bağlanır. Plugin, gateway üzerinde bir webhook alıcısı olarak çalışır ve kimlik doğrulama için channel access token + channel secret değerlerinizi kullanır.

Durum: indirilebilir Plugin. Doğrudan mesajlar, grup sohbetleri, medya, konumlar, Flex mesajları, şablon mesajlar ve hızlı yanıtlar desteklenir. Tepkiler ve ileti dizileri desteklenmez.

## Kurulum

Kanalı yapılandırmadan önce LINE'ı kurun:

bashCopy code
[code]
    openclaw plugins install @openclaw/line
[/code]

Yerel checkout (bir git repo'sundan çalıştırırken):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/line-plugin
[/code]

## Kurulum

  1. Bir LINE Developers hesabı oluşturun ve Console'u açın: <https://developers.line.biz/console/>
  2. Bir Provider oluşturun (veya seçin) ve bir **Messaging API** kanalı ekleyin.
  3. Kanal ayarlarından **Channel access token** ve **Channel secret** değerlerini kopyalayın.
  4. Messaging API ayarlarında **Use webhook** seçeneğini etkinleştirin.
  5. Webhook URL'sini gateway uç noktanıza ayarlayın (HTTPS gerekir):

CodeCopy code
[code]
    https://gateway-host/line/webhook
[/code]

Gateway, LINE'ın webhook doğrulamasına (GET) ve gelen olaylara (POST) yanıt verir. Özel bir path gerekiyorsa `channels.line.webhookPath` veya `channels.line.accounts.<id>.webhookPath` ayarlayın ve URL'yi buna göre güncelleyin.

Güvenlik notu:

  * LINE imza doğrulaması gövdeye bağlıdır (ham gövde üzerinde HMAC), bu nedenle OpenClaw doğrulamadan önce katı pre-auth gövde sınırları ve timeout uygular.
  * OpenClaw, webhook olaylarını doğrulanmış ham istek baytlarından işler. Upstream middleware tarafından dönüştürülmüş `req.body` değerleri, imza bütünlüğü güvenliği için yok sayılır.


## Yapılandırma

En küçük yapılandırma:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "pairing",    },  },}
[/code]

Herkese açık DM yapılandırması:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "open",      allowFrom: ["*"],    },  },}
[/code]

Env vars (yalnızca varsayılan hesap):

  * `LINE_CHANNEL_ACCESS_TOKEN`
  * `LINE_CHANNEL_SECRET`


Token/secret dosyaları:

json5Copy code
[code]
    {  channels: {    line: {      tokenFile: "/path/to/line-token.txt",      secretFile: "/path/to/line-secret.txt",    },  },}
[/code]

`tokenFile` ve `secretFile` normal dosyalara işaret etmelidir. Sembolik bağlantılar reddedilir.

Birden çok hesap:

json5Copy code
[code]
    {  channels: {    line: {      accounts: {        marketing: {          channelAccessToken: "...",          channelSecret: "...",          webhookPath: "/line/marketing",        },      },    },  },}
[/code]

## Erişim kontrolü

Doğrudan mesajlar varsayılan olarak pairing kullanır. Bilinmeyen gönderenler bir pairing kodu alır ve onaylanana kadar mesajları yok sayılır.

bashCopy code
[code]
    openclaw pairing list lineopenclaw pairing approve line &lt;CODE&gt;
[/code]

Allowlist'ler ve politikalar:

  * `channels.line.dmPolicy`: `pairing | allowlist | open | disabled`
  * `channels.line.allowFrom`: DM'ler için allowlist'e alınmış LINE kullanıcı ID'leri; `dmPolicy: "open"` için `["*"]` gerekir
  * `channels.line.groupPolicy`: `allowlist | open | disabled`
  * `channels.line.groupAllowFrom`: gruplar için allowlist'e alınmış LINE kullanıcı ID'leri
  * Grup başına geçersiz kılmalar: `channels.line.groups.<groupId>.allowFrom`
  * Statik gönderen erişim gruplarına `allowFrom`, `groupAllowFrom` ve grup başına `allowFrom` içinden `accessGroup:<name>` ile başvurulabilir.
  * Runtime notu: `channels.line` tamamen eksikse runtime, grup denetimleri için `groupPolicy="allowlist"` değerine geri döner (`channels.defaults.groupPolicy` ayarlanmış olsa bile).


LINE ID'leri büyük/küçük harfe duyarlıdır. Geçerli ID'ler şöyle görünür:

  * Kullanıcı: `U` \+ 32 hex chars
  * Grup: `C` \+ 32 hex chars
  * Oda: `R` \+ 32 hex chars


## Mesaj davranışı

  * Metin 5000 karakterde parçalara ayrılır.
  * Markdown biçimlendirmesi kaldırılır; kod blokları ve tablolar mümkün olduğunda Flex kartlarına dönüştürülür.
  * Streaming yanıtları arabelleğe alınır; agent çalışırken LINE tam parçaları bir yükleme animasyonuyla alır.
  * Medya indirmeleri `channels.line.mediaMaxMb` ile sınırlandırılır (varsayılan 10).
  * Gelen medya, agent'a iletilmeden önce `~/.openclaw/media/inbound/` altında kaydedilir; bu, diğer paketlenmiş kanal Plugin'leri tarafından kullanılan paylaşılan medya deposuyla eşleşir.


## Kanal verileri (zengin mesajlar)

Hızlı yanıtlar, konumlar, Flex kartları veya şablon mesajları göndermek için `channelData.line` kullanın.

json5Copy code
[code]
    {  text: "Here you go",  channelData: {    line: {      quickReplies: ["Status", "Help"],      location: {        title: "Office",        address: "123 Main St",        latitude: 35.681236,        longitude: 139.767125,      },      flexMessage: {        altText: "Status card",        contents: {          /* Flex payload */        },      },      templateMessage: {        type: "confirm",        text: "Proceed?",        confirmLabel: "Yes",        confirmData: "yes",        cancelLabel: "No",        cancelData: "no",      },    },  },}
[/code]

LINE Plugin ayrıca Flex mesaj ön ayarları için bir `/card` komutu sağlar:

CodeCopy code
[code]
    /card info "Welcome" "Thanks for joining!"
[/code]

## ACP desteği

LINE, ACP (Agent Communication Protocol) konuşma bağlamalarını destekler:

  * `/acp spawn <agent> --bind here`, geçerli LINE sohbetini bir alt ileti dizisi oluşturmadan bir ACP oturumuna bağlar.
  * Yapılandırılmış ACP bağlamaları ve aktif konuşmaya bağlı ACP oturumları, diğer konuşma kanallarında olduğu gibi LINE üzerinde çalışır.


Ayrıntılar için [ACP agent'ları](</tr/tools/acp-agents>) bölümüne bakın.

## Giden medya

LINE Plugin, agent mesaj aracı üzerinden resim, video ve ses dosyaları göndermeyi destekler. Medya, uygun önizleme ve izleme işlemleriyle LINE'a özgü teslimat path'i üzerinden gönderilir:

  * **Resimler** : otomatik önizleme oluşturma ile LINE resim mesajları olarak gönderilir.
  * **Videolar** : açık önizleme ve content-type işleme ile gönderilir.
  * **Ses** : LINE ses mesajları olarak gönderilir.


Giden medya URL'leri herkese açık HTTPS URL'leri olmalıdır. OpenClaw, URL'yi LINE'a teslim etmeden önce hedef hostname'i doğrular ve loopback, link-local ve private-network hedeflerini reddeder.

Genel medya gönderimleri, LINE'a özgü bir path kullanılamadığında mevcut yalnızca resim rotasına geri döner.

## Sorun giderme

  * **Webhook doğrulaması başarısız oluyor:** webhook URL'sinin HTTPS olduğundan ve `channelSecret` değerinin LINE console ile eşleştiğinden emin olun.
  * **Gelen olay yok:** webhook path'inin `channels.line.webhookPath` ile eşleştiğini ve gateway'in LINE'dan erişilebilir olduğunu doğrulayın.
  * **Medya indirme hataları:** medya varsayılan sınırı aşıyorsa `channels.line.mediaMaxMb` değerini yükseltin.


## İlgili

  * [Kanallara Genel Bakış](</tr/channels>) — desteklenen tüm kanallar
  * [Pairing](</tr/channels/pairing>) — DM kimlik doğrulaması ve pairing akışı
  * [Gruplar](</tr/channels/groups>) — grup sohbeti davranışı ve mention gating
  * [Kanal Yönlendirme](</tr/channels/channel-routing>) — mesajlar için oturum yönlendirme
  * [Güvenlik](</tr/gateway/security>) — erişim modeli ve hardening


Was this useful?YesNo