---
title: Gateway operasyon kılavuzu
source_url: https://docs.openclaw.ai/tr/gateway
scraped_at: 2026-05-25
---

Bu sayfayı Gateway hizmetinin 1. gün başlatması ve 2. gün operasyonları için kullanın.

[**Derin sorun giderme** Kesin komut basamakları ve günlük imzalarıyla belirti odaklı tanılama. ](</tr/gateway/troubleshooting>) [**Yapılandırma** Görev odaklı kurulum kılavuzu + tam yapılandırma başvurusu. ](</tr/gateway/configuration>) [**Gizli bilgiler yönetimi** SecretRef sözleşmesi, çalışma zamanı anlık görüntü davranışı ve migrate/reload işlemleri. ](</tr/gateway/secrets>) [**Gizli bilgiler planı sözleşmesi** Kesin `secrets apply` hedef/yol kuralları ve yalnızca ref auth-profile davranışı. ](</tr/gateway/secrets-plan-contract>)

## 5 dakikalık yerel başlatma

* ### Gateway’i başlat

bashCopy code
[code]
    openclaw gateway --port 18789# debug/trace mirrored to stdioopenclaw gateway --port 18789 --verbose# force-kill listener on selected port, then startopenclaw gateway --force
[/code]

* ### Hizmet sağlığını doğrula

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --follow
[/code]

Sağlıklı temel durum: Beklediğinizle eşleşen `Runtime: running`, `Connectivity probe: ok` ve `Capability: ...`. Yalnızca erişilebilirlik değil, okuma kapsamlı RPC kanıtı gerektiğinde `openclaw gateway status --require-rpc` kullanın.

* ### Kanal hazır olma durumunu doğrula

bashCopy code
[code]
    openclaw channels status --probe
[/code]

Erişilebilir bir Gateway ile bu, hesap başına canlı kanal yoklamaları ve isteğe bağlı denetimler çalıştırır. Gateway erişilemezse CLI, canlı yoklama çıktısı yerine yalnızca yapılandırmaya dayalı kanal özetlerine geri döner.

## Çalışma zamanı modeli

  * Yönlendirme, denetim düzlemi ve kanal bağlantıları için sürekli açık tek süreç.
  * Şunlar için tek çoğullamalı port: 
    * WebSocket denetimi/RPC
    * HTTP API’leri, OpenAI uyumlu (`/v1/models`, `/v1/embeddings`, `/v1/chat/completions`, `/v1/responses`, `/tools/invoke`)
    * Denetim kullanıcı arayüzü ve hook’lar
  * Varsayılan bağlama modu: `loopback`.
  * Kimlik doğrulama varsayılan olarak gereklidir. Paylaşılan gizli bilgi kurulumları `gateway.auth.token` / `gateway.auth.password` (veya `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`) kullanır ve local loopback olmayan ters proxy kurulumları `gateway.auth.mode: "trusted-proxy"` kullanabilir.


## OpenAI uyumlu uç noktalar

OpenClaw’ın en yüksek getirili uyumluluk yüzeyi artık şudur:

  * `GET /v1/models`
  * `GET /v1/models/{id}`
  * `POST /v1/embeddings`
  * `POST /v1/chat/completions`
  * `POST /v1/responses`


Bu kümenin neden önemli olduğu:

  * Çoğu Open WebUI, LobeChat ve LibreChat entegrasyonu önce `/v1/models` yoklar.
  * Birçok RAG ve bellek hattı `/v1/embeddings` bekler.
  * Ajan yerel istemciler giderek daha fazla `/v1/responses` tercih eder.


Planlama notu:

  * `/v1/models` ajan önceliklidir: `openclaw`, `openclaw/default` ve `openclaw/<agentId>` döndürür.
  * `openclaw/default`, her zaman yapılandırılmış varsayılan ajana eşlenen kararlı takma addır.
  * Bir arka uç sağlayıcı/model geçersiz kılması istediğinizde `x-openclaw-model` kullanın; aksi halde seçilen ajanın normal model ve embedding kurulumu denetimde kalır.


Bunların tümü ana Gateway portunda çalışır ve Gateway HTTP API’sinin geri kalanıyla aynı güvenilir operatör kimlik doğrulama sınırını kullanır.

### Port ve bağlama önceliği

Ayar | Çözümleme sırası  
---|---  
Gateway portu | `--port` → `OPENCLAW_GATEWAY_PORT` → `gateway.port` → `18789`  
Bağlama modu | CLI/geçersiz kılma → `gateway.bind` → `loopback`  
  
Kurulu Gateway hizmetleri çözümlenen `--port` değerini gözetmen metaverisine kaydeder. `gateway.port` değiştirildikten sonra launchd/systemd/schtasks süreci yeni portta başlatsın diye `openclaw doctor --fix` veya `openclaw gateway install --force` çalıştırın.

Gateway başlatması, local loopback olmayan bağlamalar için yerel Denetim kullanıcı arayüzü origin’lerini tohumlarken aynı etkin portu ve bağlamayı kullanır. Örneğin, `--bind lan --port 3000`, çalışma zamanı doğrulaması çalışmadan önce `http://localhost:3000` ve `http://127.0.0.1:3000` değerlerini tohumlar. HTTPS proxy URL’leri gibi uzak tarayıcı origin’lerini `gateway.controlUi.allowedOrigins` içine açıkça ekleyin.

### Sıcak yeniden yükleme modları

`gateway.reload.mode` | Davranış  
---|---  
`off` | Yapılandırma yeniden yüklemesi yok  
`hot` | Yalnızca sıcak-güvenli değişiklikleri uygula  
`restart` | Yeniden yükleme gerektiren değişikliklerde yeniden başlat  
`hybrid` (varsayılan) | Güvenliyse sıcak uygula, gerektiğinde yeniden başlat  
  
## Operatör komut kümesi

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --deep   # adds a system-level service scanopenclaw gateway status --jsonopenclaw gateway installopenclaw gateway restartopenclaw gateway stopopenclaw secrets reloadopenclaw logs --followopenclaw doctor
[/code]

`gateway status --deep`, daha derin bir RPC sağlık yoklaması için değil, ek hizmet keşfi (LaunchDaemons/systemd sistem birimleri/schtasks) içindir.

## Birden fazla Gateway (aynı ana makine)

Çoğu kurulum makine başına bir Gateway çalıştırmalıdır. Tek bir Gateway birden fazla ajan ve kanalı barındırabilir.

Yalnızca bilinçli olarak yalıtım veya kurtarma botu istediğinizde birden fazla Gateway gerekir.

Yararlı denetimler:

bashCopy code
[code]
    openclaw gateway status --deepopenclaw gateway probe
[/code]

Beklenecekler:

  * `gateway status --deep`, eski launchd/systemd/schtasks kurulumları hâlâ duruyorsa `Other gateway-like services detected (best effort)` bildirebilir ve temizlik ipuçları yazdırabilir.
  * Birden fazla hedef yanıt verdiğinde `gateway probe`, `multiple reachable gateways` hakkında uyarabilir.
  * Bu bilinçliyse portları, yapılandırma/durumu ve çalışma alanı köklerini Gateway başına yalıtın.


Örnek başına kontrol listesi:

  * Benzersiz `gateway.port`
  * Benzersiz `OPENCLAW_CONFIG_PATH`
  * Benzersiz `OPENCLAW_STATE_DIR`
  * Benzersiz `agents.defaults.workspace`


Örnek:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/a.json OPENCLAW_STATE_DIR=~/.openclaw-a openclaw gateway --port 19001OPENCLAW_CONFIG_PATH=~/.openclaw/b.json OPENCLAW_STATE_DIR=~/.openclaw-b openclaw gateway --port 19002
[/code]

Ayrıntılı kurulum: [/gateway/multiple-gateways](</tr/gateway/multiple-gateways>).

## Uzak erişim

Tercih edilen: Tailscale/VPN. Geri dönüş: SSH tüneli.

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

Ardından istemcileri yerel olarak `ws://127.0.0.1:18789` adresine bağlayın.

Bkz.: [Uzak Gateway](</tr/gateway/remote>), [Kimlik doğrulama](</tr/gateway/authentication>), [Tailscale](</tr/gateway/tailscale>).

## Gözetim ve hizmet yaşam döngüsü

Üretim benzeri güvenilirlik için gözetimli çalıştırmaları kullanın.

### macOS (launchd)

bashCopy code
[code]
    openclaw gateway installopenclaw gateway statusopenclaw gateway restartopenclaw gateway stop
[/code]

Yeniden başlatmalar için `openclaw gateway restart` kullanın. Yeniden başlatma yerine `openclaw gateway stop` ve `openclaw gateway start` komutlarını zincirlemeyin.

macOS’ta `gateway stop` varsayılan olarak `launchctl bootout` kullanır; bu, kalıcı bir devre dışı bırakma yapmadan LaunchAgent’ı geçerli önyükleme oturumundan kaldırır, böylece KeepAlive otomatik kurtarması beklenmeyen çökmelerden sonra hâlâ çalışır ve `gateway start` temiz biçimde yeniden etkinleştirir. Yeniden başlatmalar arasında otomatik yeniden doğmayı kalıcı olarak bastırmak için `--disable` geçirin: `openclaw gateway stop --disable`.

LaunchAgent etiketleri `ai.openclaw.gateway` (varsayılan) veya `ai.openclaw.<profile>` (adlandırılmış profil) şeklindedir. `openclaw doctor` hizmet yapılandırması sapmasını denetler ve onarır.

### Linux (systemd kullanıcı)

bashCopy code
[code]
    openclaw gateway installsystemctl --user enable --now openclaw-gateway[-<profile>].serviceopenclaw gateway status
[/code]

Oturum kapattıktan sonra kalıcılık için lingering’i etkinleştirin:

bashCopy code
[code]
    sudo loginctl enable-linger <user>
[/code]

Özel kurulum yolu gerektiğinde manuel kullanıcı birimi örneği:

iniCopy code
[code]
    [Unit]Description=OpenClaw GatewayAfter=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

### Windows (yerel)

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --jsonopenclaw gateway restartopenclaw gateway stop
[/code]

Yerel Windows yönetimli başlangıcı `OpenClaw Gateway` adlı bir Zamanlanmış Görev kullanır (veya adlandırılmış profiller için `OpenClaw Gateway (<profile>)`). Zamanlanmış Görev oluşturma reddedilirse OpenClaw, durum dizini içindeki `gateway.cmd` dosyasını işaret eden kullanıcı başına Başlangıç klasörü başlatıcısına geri döner.

### Linux (sistem hizmeti)

Çok kullanıcılı/sürekli açık ana makineler için bir sistem birimi kullanın.

bashCopy code
[code]
    sudo systemctl daemon-reloadsudo systemctl enable --now openclaw-gateway[-<profile>].service
[/code]

Kullanıcı birimiyle aynı hizmet gövdesini kullanın, ancak bunu `/etc/systemd/system/openclaw-gateway[-<profile>].service` altına kurun ve `openclaw` ikiliniz başka bir yerdeyse `ExecStart=` değerini ayarlayın.

Aynı profil/port için `openclaw doctor --fix` komutunun ayrıca kullanıcı düzeyinde bir Gateway hizmeti kurmasına izin vermeyin. Doctor, sistem düzeyinde bir OpenClaw Gateway hizmeti bulduğunda bu otomatik kurulumu reddeder; yaşam döngüsünün sahibi sistem birimiyse `OPENCLAW_SERVICE_REPAIR_POLICY=external` kullanın.

## Geliştirme profili hızlı yolu

bashCopy code
[code]
    openclaw --dev setupopenclaw --dev gateway --allow-unconfiguredopenclaw --dev status
[/code]

Varsayılanlar yalıtılmış durum/yapılandırma ve temel Gateway portu `19001` içerir.

## Protokol hızlı başvurusu (operatör görünümü)

  * İlk istemci karesi `connect` olmalıdır.
  * Gateway `hello-ok` anlık görüntüsünü döndürür (`presence`, `health`, `stateVersion`, `uptimeMs`, sınırlar/politika).
  * `hello-ok.features.methods` / `events`, çağrılabilir her yardımcı rotanın üretilmiş dökümü değil, temkinli bir keşif listesidir.
  * İstekler: `req(method, params)` → `res(ok/payload|error)`.
  * Yaygın olaylar arasında `connect.challenge`, `agent`, `chat`, `session.message`, `session.tool`, `sessions.changed`, `presence`, `tick`, `health`, `heartbeat`, eşleştirme/onay yaşam döngüsü olayları ve `shutdown` bulunur.


Ajan çalıştırmaları iki aşamalıdır:

  1. Anında kabul edildi onayı (`status:"accepted"`)
  2. Arada akışla gelen `agent` olaylarıyla nihai tamamlama yanıtı (`status:"ok"|"error"`).


Tam protokol belgelerine bakın: [Gateway Protokolü](</tr/gateway/protocol>).

## Operasyonel denetimler

### Canlılık

  * WS açın ve `connect` gönderin.
  * Anlık görüntü içeren `hello-ok` yanıtı bekleyin.


### Hazır olma

bashCopy code
[code]
    openclaw gateway statusopenclaw channels status --probeopenclaw health
[/code]

### Boşluk kurtarma

Olaylar yeniden oynatılmaz. Sıra boşluklarında devam etmeden önce durumu yenileyin (`health`, `system-presence`).

## Yaygın hata imzaları

İmza | Olası sorun  
---|---  
`refusing to bind gateway ... without auth` | Geçerli bir Gateway kimlik doğrulama yolu olmadan loopback dışı bağlama  
`another gateway instance is already listening` / `EADDRINUSE` | Bağlantı noktası çakışması  
`Gateway start blocked: set gateway.mode=local` | Yapılandırma uzak moda ayarlanmış veya hasarlı bir yapılandırmada yerel mod damgası eksik  
`unauthorized` sırasında connect | İstemci ile Gateway arasında kimlik doğrulama uyuşmazlığı  
  
Tam tanılama merdivenleri için [Gateway Sorun Giderme](</tr/gateway/troubleshooting>) sayfasını kullanın.

## Güvenlik garantileri

  * Gateway kullanılamadığında Gateway protokol istemcileri hızla başarısız olur (örtük doğrudan kanal yedeği yoktur).
  * Geçersiz/bağlanmayan ilk çerçeveler reddedilir ve kapatılır.
  * Zarif kapatma, soket kapanmadan önce `shutdown` olayını yayar.


* * *

İlgili:

  * [Sorun Giderme](</tr/gateway/troubleshooting>)
  * [Arka Plan Süreci](</tr/gateway/background-process>)
  * [Yapılandırma](</tr/gateway/configuration>)
  * [Sağlık](</tr/gateway/health>)
  * [Doctor](</tr/gateway/doctor>)
  * [Kimlik Doğrulama](</tr/gateway/authentication>)


## İlgili

  * [Yapılandırma](</tr/gateway/configuration>)
  * [Gateway sorun giderme](</tr/gateway/troubleshooting>)
  * [Uzaktan erişim](</tr/gateway/remote>)
  * [Gizli bilgiler yönetimi](</tr/gateway/secrets>)


Was this useful?YesNo