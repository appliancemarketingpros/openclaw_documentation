---
title: Chrome Uzantısı
source_url: https://docs.openclaw.ai/tr/tools/chrome-extension
scraped_at: 2026-07-13
---

CapabilitiesTools

# Chrome uzantısı

OpenClaw Chrome uzantısı, bir aracının ayrı bir yönetilen tarayıcı başlatmadan ve Chrome'un engelleyici "Allow remote debugging?" istemi **olmadan** **oturum açtığınız Chrome sekmelerini** denetlemesini sağlar.

OpenClaw'ı bir telefondan (Telegram, WhatsApp vb.) kullandığınızda bu önemlidir: [`user` profili](</tr/tools/browser#profiles-openclaw-user-chrome>), Chrome'un uzaktan hata ayıklama bağlantı noktası üzerinden bağlanır; bu da siz uzaktayken kimsenin tıklayamayacağı bir masaüstü onay iletişim kutusu açar. Uzantı bunun yerine `chrome.debugger` API'sini kullanır; dolayısıyla sayfadaki tek bildirim, Chrome'un kapatılabilir "OpenClaw started debugging this browser" başlığıdır.

Bu, Anthropic'in Claude in Chrome ve OpenAI'ın Codex Chrome uzantılarında kullanılan yapıyla aynıdır.

## Nasıl çalışır?

Üç bölümden oluşur:

  * **Tarayıcı denetim hizmeti** (Gateway veya node ana makinesi): `browser` aracının çağırdığı API.
  * **Uzantı aktarım hizmeti** (local loopback WebSocket): denetim hizmetinin `127.0.0.1` üzerinde başlattığı küçük bir sunucu. OpenClaw'a bir Chrome DevTools Protocol uç noktası sunar ve uzantıyla iletişim kurar. Her iki taraf da ana makineye özgü yerel bir token ile kimlik doğrular (aşağıya bakın).
  * **OpenClaw Chrome uzantısı** (MV3): `chrome.debugger` ile sekmelere bağlanır, CDP trafiğini iletir ve **OpenClaw sekme grubunu** yönetir.


OpenClaw yalnızca **OpenClaw sekme grubundaki** sekmeleri görür ve denetler. Grup, onay sınırıdır: paylaşmak için bir sekmeyi gruba sürükleyin; erişimi anında iptal etmek için gruptan dışarı sürükleyin (veya araç çubuğu düğmesine tıklayın).

## Yükleme ve eşleştirme

  1. Paketlenmemiş uzantının yolunu yazdırın:

bashCopy code
[code]openclaw browser extension path
[/code]

  2. `chrome://extensions` sayfasını açın, **Developer mode** seçeneğini etkinleştirin, **Load unpacked** öğesine tıklayın ve yazdırılan dizini seçin.

  3. Eşleştirme dizesini yazdırın:

bashCopy code
[code]openclaw browser extension pair
[/code]

  4. OpenClaw araç çubuğu simgesine tıklayın ve eşleştirme dizesini açılır pencereye yapıştırın. Uzantı aktarım hizmetine bağlandığında rozet **ON** durumuna geçer.


Eşleştirme token'ı, ilk kullanımda oluşturulan ve durum dizininde `credentials/` altında (`0600` moduyla) saklanan **ana makineye özgü yerel bir gizli değerdir**. Tarayıcı çalıştıran her makine (Gateway ana makinesi ve her tarayıcı node ana makinesi) kendi token'ına sahiptir; dolayısıyla kimlik bilgilerinin makineler arasında taşınması gerekmez. Token'ı yenilemek için `browser-extension-relay.secret` dosyasını silin ve yeniden eşleştirin.

## Kullanım

Bir `browser` aracı çağrısında yerleşik `chrome` profilini seçin veya varsayılan yapın:

bashCopy code
[code]
    openclaw config set browser.defaultProfile chrome
[/code]

json5Copy code
[code]
    {  browser: {    profiles: {      chrome: { driver: "extension", color: "#FF4500" },    },  },}
[/code]

  * Bir sekmeyi paylaşma: ilgili sekmede OpenClaw araç çubuğu düğmesine tıklayın (sekme, OpenClaw sekme grubuna katılır) veya herhangi bir sekmeyi gruba sürükleyin.
  * Aracı ayrıca yeni sekmeler açabilir; bunlar otomatik olarak gruba eklenir.
  * Erişimi iptal etme: düğmeye tekrar tıklayın, sekmeyi gruptan dışarı sürükleyin veya Chrome'un hata ayıklama başlığını kapatın. Aracı, o sekmeye erişimini anında kaybeder.


## Uzak / makineler arası

Chrome'un Gateway ana makinesinde çalışması gerekmez. Üç topoloji desteklenir:

  * **Aynı ana makine** (Gateway ve Chrome tek bir makinede): o makinede `openclaw browser extension pair` komutuyla eşleştirin. Aktarım hizmetine yalnızca local loopback üzerinden erişilebilir.
  * **Uzak bir Gateway'e doğrudan bağlantı** (Chrome dizüstü bilgisayarınızda, Gateway bir VPS'de ve **dizüstü bilgisayarda başka hiçbir şey yok**): Gateway üzerinde `openclaw browser extension pair --gateway-url wss://your-gateway.example.com` komutunu çalıştırın. Komut bir `wss://…/browser/extension#<secret>` dizesi yazdırır; uzantıyı dizüstü bilgisayara yükleyip eşleştirin. Uzantı `wss://` üzerinden **doğrudan Gateway'e** bağlanır; dizüstü bilgisayarda OpenClaw kurulumu, Node, CLI veya açık bir gelen bağlantı noktası gerekmez. Bu, yönetilen barındırma yoludur.
  * **Bir tarayıcı node ana makinesi üzerinden** (Chrome, hâlihazırda bir OpenClaw node'u çalıştıran makinede): node üzerinde `pair` komutunu çalıştırıp yerel olarak eşleştirin; Gateway, tarayıcı eylemlerini mevcut kimliği doğrulanmış node bağlantısı üzerinden node'a vekâleten iletir.


Eşleştirme gizli değeri ana makine başınadır (doğrudan bağlantıda Gateway'e aittir) ve Gateway'in `/browser/extension` rotası tarafından doğrulanır. Doğrudan bağlantı yolu için Gateway'i TLS (`wss://`) üzerinden sunarak eşleştirme gizli değerinin ve CDP trafiğinin şifrelenmesini sağlayın. Gizli değer, eşleştirme dizesinin URL parçasında kalır ve WebSocket el sıkışması sırasında bir alt protokol kimlik bilgisi olarak sunulur; böylece normal proxy erişim günlükleri bu değeri istek URL'sinde almaz. Ters proxy'nin standart `Sec-WebSocket-Protocol` üstbilgisini koruduğundan emin olun.

## Tanılama

bashCopy code
[code]
    openclaw browser status --browser-profile chromeopenclaw browser doctor --browser-profile chrome
[/code]

`doctor`, uzantı açılır penceresinde **Connected** gösterilene kadar **Chrome uzantısı aktarım hizmeti** denetiminin başarısız olduğunu bildirir.

## Güvenlik modeli

  * Aktarım hizmeti yalnızca local loopback'e bağlanır; her iki WebSocket tarafının kimliği türetilmiş token ile doğrulanır ve uzantı tarafının kaynağının `chrome-extension://` olduğu denetlenir.
  * Doğrudan Gateway eşleştirmesi, aktarım token'ını istek URL'sinde kabul etmez; paketle birlikte gelen uzantı bunun yerine token'ı WebSocket alt protokol listesinde taşır.
  * Aracı yalnızca **OpenClaw sekme grubundaki** sekmeleri görebilir ve denetleyebilir. Diğer sekmeleriniz gizli kalır.
  * Uzaktan hata ayıklama istemini onayladığınızda oturum açılmış tarayıcınızın tamamını açığa çıkaran `user` (Chrome MCP) profiliyle karşılaştırıldığında uzantı, paylaşılan yüzeyi bir bakışta denetleyebileceğiniz bir sekme grubuyla sınırlar.


Profil modelinin tamamı ile yönetilen `openclaw` ve Chrome MCP `user` profilleri için ayrıca bkz. [Tarayıcı](</tr/tools/browser>).

Was this useful?YesNo

Open issue