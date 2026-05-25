---
title: macOS uygulaması
source_url: https://docs.openclaw.ai/tr/platforms/macos
scraped_at: 2026-05-25
---

macOS uygulaması, OpenClaw için **menü çubuğu eşlikçisi** dir. İzinlerin sahibidir, Gateway'i yerel olarak yönetir/ona bağlanır (launchd veya manuel) ve macOS yeteneklerini ajana bir node olarak sunar.

## Ne yapar

  * Menü çubuğunda yerel bildirimleri ve durumu gösterir.
  * TCC istemlerinin sahibidir (Bildirimler, Erişilebilirlik, Ekran Kaydı, Mikrofon, Konuşma Tanıma, Otomasyon/AppleScript).
  * Gateway'i çalıştırır veya ona bağlanır (yerel ya da uzak).
  * Yalnızca macOS'a özgü araçları sunar (Canvas, Kamera, Ekran Kaydı, `system.run`).
  * **remote** modda (launchd) yerel node ana makine hizmetini başlatır ve **local** modda durdurur.
  * İsteğe bağlı olarak UI otomasyonu için **PeekabooBridge** barındırır.
  * İstek üzerine global CLI'yi (`openclaw`) npm, pnpm veya bun üzerinden kurar (uygulama önce npm'i, sonra pnpm'i, sonra bun'ı tercih eder; Node önerilen Gateway runtime'ı olmaya devam eder).


## Yerel ve uzak mod

  * **Local** (varsayılan): uygulama, varsa çalışan yerel bir Gateway'e bağlanır; yoksa `openclaw gateway install` ile launchd hizmetini etkinleştirir.
  * **Remote** : uygulama SSH/Tailscale üzerinden bir Gateway'e bağlanır ve hiçbir zaman yerel bir süreç başlatmaz. Uygulama, uzak Gateway'in bu Mac'e erişebilmesi için yerel **node ana makine hizmetini** başlatır. Uygulama Gateway'i alt süreç olarak başlatmaz. Gateway keşfi artık ham tailnet IP'leri yerine Tailscale MagicDNS adlarını tercih eder, böylece Mac uygulaması tailnet IP'leri değiştiğinde daha güvenilir şekilde toparlanır.


## Launchd denetimi

Uygulama `ai.openclaw.gateway` etiketli kullanıcı başına bir LaunchAgent yönetir (`--profile`/`OPENCLAW_PROFILE` kullanırken `ai.openclaw.<profile>`; eski `com.openclaw.*` yine de unload edilir).

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.gatewaylaunchctl bootout gui/$UID/ai.openclaw.gateway
[/code]

Adlandırılmış bir profil çalıştırırken etiketi `ai.openclaw.<profile>` ile değiştirin.

LaunchAgent kurulu değilse uygulamadan etkinleştirin veya `openclaw gateway install` çalıştırın.

## Node yetenekleri (mac)

macOS uygulaması kendini bir node olarak sunar. Yaygın komutlar:

  * Canvas: `canvas.present`, `canvas.navigate`, `canvas.eval`, `canvas.snapshot`, `canvas.a2ui.*`
  * Kamera: `camera.snap`, `camera.clip`
  * Ekran: `screen.snapshot`, `screen.record`
  * Sistem: `system.run`, `system.notify`


Node, ajanların neye izin verildiğine karar verebilmesi için bir `permissions` eşlemesi bildirir.

Node hizmeti + uygulama IPC'si:

  * Başsız node ana makine hizmeti çalışırken (remote mod), Gateway WS'ye bir node olarak bağlanır.
  * `system.run`, yerel Unix soketi üzerinden macOS uygulamasında (UI/TCC bağlamı) yürütülür; istemler + çıktı uygulama içinde kalır.


Diyagram (SCI):

CodeCopy code
[code]
    Gateway -> Node Service (WS)                 |  IPC (UDS + token + HMAC + TTL)                 v             Mac App (UI + TCC + system.run)
[/code]

## Exec onayları (system.run)

`system.run`, macOS uygulamasındaki **Exec onayları** tarafından denetlenir (Ayarlar → Exec onayları). Güvenlik + sorma + izin listesi Mac'te yerel olarak şurada saklanır:

CodeCopy code
[code]
    ~/.openclaw/exec-approvals.json
[/code]

Örnek:

jsonCopy code
[code]
    {  "version": 1,  "defaults": {    "security": "deny",    "ask": "on-miss"  },  "agents": {    "main": {      "security": "allowlist",      "ask": "on-miss",      "allowlist": [{ "pattern": "/opt/homebrew/bin/rg" }]    }  }}
[/code]

Notlar:

  * `allowlist` girdileri, çözümlenen ikili yolları için glob desenleri veya PATH üzerinden çağrılan komutlar için yalın komut adlarıdır.
  * Kabuk denetimi veya genişletme sözdizimi (`&&`, `||`, `;`, `|`, ```, `$`, `<`, `>`, `(`, `)`) içeren ham kabuk komutu metni izin listesi kaçırması olarak değerlendirilir ve açık onay gerektirir (veya kabuk ikilisinin izin listesine alınmasını).
  * İstemde "Always Allow" seçildiğinde bu komut izin listesine eklenir.
  * `system.run` ortam geçersiz kılmaları filtrelenir (`PATH`, `DYLD_*`, `LD_*`, `NODE_OPTIONS`, `PYTHON*`, `PERL*`, `RUBYOPT`, `SHELLOPTS`, `PS4` bırakılır) ve ardından uygulamanın ortamıyla birleştirilir.
  * Kabuk sarmalayıcıları (`bash|sh|zsh ... -c/-lc`) için istek kapsamlı ortam geçersiz kılmaları küçük ve açık bir izin listesine indirgenir (`TERM`, `LANG`, `LC_*`, `COLORTERM`, `NO_COLOR`, `FORCE_COLOR`).
  * İzin listesi modundaki her zaman izin ver kararları için bilinen dağıtım sarmalayıcıları (`env`, `nice`, `nohup`, `stdbuf`, `timeout`) sarmalayıcı yolları yerine iç yürütülebilir yolları kalıcı hale getirir. Açma işlemi güvenli değilse otomatik olarak hiçbir izin listesi girdisi kalıcı hale getirilmez.


## Derin bağlantılar

Uygulama yerel eylemler için `openclaw://` URL şemasını kaydeder.

### `openclaw://agent`

Bir Gateway `agent` isteğini tetikler. **OC_I18N_900004** Sorgu parametreleri:

  * `message` (gerekli)
  * `sessionKey` (isteğe bağlı)
  * `thinking` (isteğe bağlı)
  * `deliver` / `to` / `channel` (isteğe bağlı)
  * `timeoutSeconds` (isteğe bağlı)
  * `key` (isteğe bağlı gözetimsiz mod anahtarı)


Güvenlik:

  * `key` olmadan uygulama onay ister.
  * `key` olmadan uygulama, onay istemi için kısa bir mesaj sınırı uygular ve `deliver` / `to` / `channel` değerlerini yok sayar.
  * Geçerli bir `key` ile çalışma gözetimsizdir (kişisel otomasyonlar için tasarlanmıştır).


## Onboarding akışı (tipik)

  1. **OpenClaw.app** 'i kurun ve başlatın.
  2. İzin kontrol listesini tamamlayın (TCC istemleri).
  3. **Local** modun etkin olduğundan ve Gateway'in çalıştığından emin olun.
  4. Terminal erişimi istiyorsanız CLI'yi kurun.


## Durum dizini yerleşimi (macOS)

OpenClaw durum dizininizi iCloud'a veya bulutla eşitlenen diğer klasörlere koymaktan kaçının. Eşitleme destekli yollar gecikme ekleyebilir ve oturumlar ile kimlik bilgileri için zaman zaman dosya kilidi/eşitleme yarışlarına neden olabilir.

Şunun gibi yerel, eşitlenmeyen bir durum yolunu tercih edin: **OC_I18N_900005** `openclaw doctor` durumu şuraların altında algılarsa:

  * `~/Library/Mobile Documents/com~apple~CloudDocs/...`
  * `~/Library/CloudStorage/...`


uyarır ve yerel bir yola geri taşımayı önerir.

## Build ve geliştirme iş akışı (yerel)

  * `cd apps/macos && swift build`
  * `swift run OpenClaw` (veya Xcode)
  * Uygulamayı paketle: `scripts/package-mac-app.sh`


## Gateway bağlantısını hata ayıklama (macOS CLI)

macOS uygulamasını başlatmadan, uygulamanın kullandığı aynı Gateway WebSocket el sıkışmasını ve keşif mantığını çalıştırmak için debug CLI'yi kullanın. **OC_I18N_900006** Bağlantı seçenekleri:

  * `--url <ws://host:port>`: yapılandırmayı geçersiz kıl
  * `--mode <local|remote>`: yapılandırmadan çözümle (varsayılan: yapılandırma veya local)
  * `--probe`: yeni bir sağlık yoklamasını zorla
  * `--timeout <ms>`: istek zaman aşımı (varsayılan: `15000`)
  * `--json`: karşılaştırma için yapılandırılmış çıktı


Keşif seçenekleri:

  * `--include-local`: "local" olarak filtrelenecek gateway'leri dahil et
  * `--timeout <ms>`: genel keşif penceresi (varsayılan: `2000`)
  * `--json`: karşılaştırma için yapılandırılmış çıktı


## Uzak bağlantı tesisatı (SSH tünelleri)

macOS uygulaması **Remote** modda çalıştığında, yerel UI bileşenlerinin uzak bir Gateway ile localhost'taymış gibi konuşabilmesi için bir SSH tüneli açar.

### Denetim tüneli (Gateway WebSocket bağlantı noktası)

  * **Amaç:** sağlık kontrolleri, durum, Web Chat, yapılandırma ve diğer denetim düzlemi çağrıları.
  * **Yerel bağlantı noktası:** Gateway bağlantı noktası (varsayılan `18789`), her zaman kararlı.
  * **Uzak bağlantı noktası:** uzak ana makinedeki aynı Gateway bağlantı noktası.
  * **Davranış:** rastgele yerel bağlantı noktası yoktur; uygulama mevcut sağlıklı bir tüneli yeniden kullanır veya gerekirse yeniden başlatır.
  * **SSH şekli:** BatchMode + ExitOnForwardFailure + keepalive seçenekleriyle `ssh -N -L <local>:127.0.0.1:<remote>`.
  * **IP raporlama:** SSH tüneli loopback kullanır, bu yüzden gateway node IP'sini `127.0.0.1` olarak görür. Gerçek istemci IP'sinin görünmesini istiyorsanız **Direct (ws/wss)** aktarımını kullanın (bkz. [macOS uzaktan erişim](</tr/platforms/mac/remote>)).


Kurulum adımları için bkz. [macOS uzaktan erişim](</tr/platforms/mac/remote>). Protokol ayrıntıları için bkz. [Gateway protokolü](</tr/gateway/protocol>).

## İlgili dokümanlar

  * [Gateway runbook](</tr/gateway>)
  * [Gateway (macOS)](</tr/platforms/mac/bundled-gateway>)
  * [macOS izinleri](</tr/platforms/mac/permissions>)
  * [Canvas](</tr/platforms/mac/canvas>)


Was this useful?YesNo