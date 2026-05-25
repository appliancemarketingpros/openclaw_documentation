---
title: Eşleştirme
source_url: https://docs.openclaw.ai/tr/channels/pairing
scraped_at: 2026-05-25
---

"Eşleştirme", OpenClaw'ın açık erişim onayı adımıdır. İki yerde kullanılır:

  1. **DM eşleştirme** (botla kimin konuşmasına izin verildiği)
  2. **Node eşleştirme** (hangi cihazların/node'ların gateway ağına katılmasına izin verildiği)


Güvenlik bağlamı: [Güvenlik](</tr/gateway/security>)

## 1) DM eşleştirme (gelen sohbet erişimi)

Bir kanal `pairing` DM ilkesiyle yapılandırıldığında, bilinmeyen göndericiler kısa bir kod alır ve siz onaylayana kadar iletileri **işlenmez**.

Varsayılan DM ilkeleri burada belgelenmiştir: [Güvenlik](</tr/gateway/security>)

`dmPolicy: "open"` yalnızca etkin DM izin listesi `"*"` içerdiğinde herkese açıktır. Kurulum ve doğrulama, herkese açık yapılandırmalar için bu joker karakteri gerektirir. Mevcut durum, somut `allowFrom` girdileriyle `open` içeriyorsa, çalışma zamanı yine de yalnızca bu göndericileri kabul eder ve eşleştirme deposu onayları `open` erişimini genişletmez.

Eşleştirme kodları:

  * 8 karakter, büyük harf, belirsiz karakter yok (`0O1I`).
  * **1 saat sonra sona erer**. Bot, eşleştirme iletisini yalnızca yeni bir istek oluşturulduğunda gönderir (gönderici başına yaklaşık saatte bir).
  * Bekleyen DM eşleştirme istekleri varsayılan olarak **kanal başına 3** ile sınırlıdır; ek istekler biri sona erene veya onaylanana kadar yok sayılır.


### Bir göndericiyi onaylama

bashCopy code
[code]
    openclaw pairing list telegramopenclaw pairing approve telegram &lt;CODE&gt;
[/code]

Henüz komut sahibi yapılandırılmamışsa, bir DM eşleştirme kodunu onaylamak `commands.ownerAllowFrom` ayarını da onaylanan göndericiye, örneğin `telegram:123456789`, başlatır. Bu, ilk kurulumlara ayrıcalıklı komutlar ve exec onayı istemleri için açık bir sahip verir. Bir sahip var olduktan sonra, sonraki eşleştirme onayları yalnızca DM erişimi verir; daha fazla sahip eklemez.

Desteklenen kanallar: `discord`, `feishu`, `googlechat`, `imessage`, `irc`, `line`, `matrix`, `mattermost`, `msteams`, `nextcloud-talk`, `nostr`, `openclaw-weixin`, `signal`, `slack`, `synology-chat`, `telegram`, `twitch`, `whatsapp`, `zalo`, `zalouser`.

### Yeniden kullanılabilir gönderici grupları

Aynı güvenilir gönderici kümesi birden çok ileti kanalına veya hem DM hem de grup izin listelerine uygulanacaksa üst düzey `accessGroups` kullanın.

Statik gruplar `type: "message.senders"` kullanır ve kanal izin listelerinden `accessGroup:<name>` ile başvurulur:

json5Copy code
[code]
    {  accessGroups: {    operators: {      type: "message.senders",      members: {        discord: ["discord:123456789012345678"],        telegram: ["987654321"],        whatsapp: ["+15551234567"],      },    },  },  channels: {    telegram: { dmPolicy: "allowlist", allowFrom: ["accessGroup:operators"] },    whatsapp: { groupPolicy: "allowlist", groupAllowFrom: ["accessGroup:operators"] },  },}
[/code]

Erişim grupları burada ayrıntılı olarak belgelenmiştir: [Erişim grupları](</tr/channels/access-groups>)

### Durumun bulunduğu yer

`~/.openclaw/credentials/` altında saklanır:

  * Bekleyen istekler: `<channel>-pairing.json`
  * Onaylanmış izin listesi deposu: 
    * Varsayılan hesap: `<channel>-allowFrom.json`
    * Varsayılan olmayan hesap: `<channel>-<accountId>-allowFrom.json`


Hesap kapsamı davranışı:

  * Varsayılan olmayan hesaplar yalnızca kendi kapsamlı izin listesi dosyalarını okur/yazar.
  * Varsayılan hesap, kanal kapsamlı kapsamsız izin listesi dosyasını kullanır.


Bunları hassas kabul edin (asistanınıza erişimi denetlerler).

## 2) Node cihaz eşleştirme (iOS/Android/macOS/headless Node'lar)

Node'lar Gateway'e `role: node` ile **cihaz** olarak bağlanır. Gateway, onaylanması gereken bir cihaz eşleştirme isteği oluşturur.

### Telegram üzerinden eşleştirme (iOS için önerilir)

`device-pair` plugin'ini kullanıyorsanız, ilk cihaz eşleştirmesini tamamen Telegram içinden yapabilirsiniz:

  1. Telegram'da botunuza şunu yazın: `/pair`
  2. Bot iki iletiyle yanıt verir: bir yönerge iletisi ve ayrı bir **kurulum kodu** iletisi (Telegram'da kopyalayıp yapıştırması kolaydır).
  3. Telefonunuzda OpenClaw iOS uygulamasını açın → Ayarlar → Gateway.
  4. QR kodunu tarayın veya kurulum kodunu yapıştırıp bağlanın.
  5. Telegram'a dönün: `/pair pending` (istek kimliklerini, rolü ve kapsamları gözden geçirin), ardından onaylayın.


Kurulum kodu, şunları içeren base64 kodlu bir JSON yüküdür:

  * `url`: Gateway WebSocket URL'si (`ws://...` veya `wss://...`)
  * `bootstrapToken`: ilk eşleştirme el sıkışması için kullanılan kısa ömürlü, tek cihazlık bootstrap token'ı


Bu bootstrap token'ı yerleşik eşleştirme bootstrap profilini taşır:

  * birincil devredilen `node` token'ı `scopes: []` olarak kalır
  * devredilen herhangi bir `operator` token'ı bootstrap izin listesiyle sınırlı kalır: `operator.approvals`, `operator.read`, `operator.talk.secrets`, `operator.write`
  * bootstrap kapsam denetimleri rol önekli yapılır, tek bir düz kapsam havuzu değildir: operator kapsam girdileri yalnızca operator isteklerini karşılar ve operator olmayan roller yine de kapsamları kendi rol önekleri altında istemelidir
  * sonraki token döndürme/iptal işlemleri hem cihazın onaylı rol sözleşmesiyle hem de çağıran oturumun operator kapsamlarıyla sınırlı kalır


Kurulum kodunu geçerli olduğu sürece parola gibi ele alın.

Tailscale, herkese açık veya başka uzak mobil eşleştirme için Tailscale Serve/Funnel veya başka bir `wss://` Gateway URL'si kullanın. Düz metin `ws://` kurulum kodları yalnızca loopback, özel LAN adresleri, `.local` Bonjour ana makineleri ve Android emülatör ana makinesi için kabul edilir. Tailnet CGNAT adresleri, `.ts.net` adları ve herkese açık ana makineler, QR/kurulum kodu verilmeden önce yine kapalı başarısız olur.

### Bir Node cihazını onaylama

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <requestId>openclaw devices reject <requestId>
[/code]

Açık bir onay, onaylayan eşleştirilmiş cihaz oturumu yalnızca eşleştirme kapsamıyla açıldığı için reddedildiğinde, CLI aynı isteği `operator.admin` ile yeniden dener. Bu, mevcut admin yetenekli eşleştirilmiş cihazın yeni bir Control UI/tarayıcı eşleştirmesini `devices/paired.json` dosyasını elle düzenlemeden kurtarmasına olanak tanır. Gateway yeniden denenen bağlantıyı yine doğrular; `operator.admin` ile kimlik doğrulaması yapamayan token'lar engelli kalır.

Aynı cihaz farklı kimlik doğrulama ayrıntılarıyla yeniden denerse (örneğin farklı rol/kapsamlar/genel anahtar), önceki bekleyen istek geçersiz kılınır ve yeni bir `requestId` oluşturulur.

### İsteğe bağlı güvenilir-CIDR Node otomatik onayı

Cihaz eşleştirme varsayılan olarak elle yapılır. Sıkı denetlenen Node ağları için, açık CIDR'ler veya tam IP'lerle ilk Node otomatik onayını etkinleştirebilirsiniz:

json5Copy code
[code]
    {  gateway: {    nodes: {      pairing: {        autoApproveCidrs: ["192.168.1.0/24"],      },    },  },}
[/code]

Bu yalnızca istenen kapsamı olmayan yeni `role: node` eşleştirme isteklerine uygulanır. Operator, tarayıcı, Control UI ve WebChat istemcileri yine elle onay gerektirir. Rol, kapsam, metadata ve genel anahtar değişiklikleri yine elle onay gerektirir.

### Node eşleştirme durumu depolaması

`~/.openclaw/devices/` altında saklanır:

  * `pending.json` (kısa ömürlü; bekleyen istekler sona erer)
  * `paired.json` (eşleştirilmiş cihazlar + token'lar)


### Notlar

  * Eski `node.pair.*` API'si (CLI: `openclaw nodes pending|approve|reject|remove|rename`) ayrı, gateway sahipli bir eşleştirme deposudur. WS Node'ları yine cihaz eşleştirme gerektirir.
  * Eşleştirme kaydı, onaylanmış roller için kalıcı doğruluk kaynağıdır. Etkin cihaz token'ları bu onaylanmış rol kümesiyle sınırlı kalır; onaylanmış roller dışındaki başıboş bir token girdisi yeni erişim oluşturmaz.


## İlgili belgeler

  * Güvenlik modeli + prompt injection: [Güvenlik](</tr/gateway/security>)
  * Güvenli güncelleme (doctor çalıştırın): [Güncelleme](</tr/install/updating>)
  * Kanal yapılandırmaları: 
    * Telegram: [Telegram](</tr/channels/telegram>)
    * WhatsApp: [WhatsApp](</tr/channels/whatsapp>)
    * Signal: [Signal](</tr/channels/signal>)
    * iMessage: [iMessage](</tr/channels/imessage>)
    * Discord: [Discord](</tr/channels/discord>)
    * Slack: [Slack](</tr/channels/slack>)


Was this useful?YesNo