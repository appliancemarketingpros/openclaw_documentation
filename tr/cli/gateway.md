---
title: Gateway
source_url: https://docs.openclaw.ai/tr/cli/gateway
scraped_at: 2026-05-25
---

Gateway, OpenClaw'ın WebSocket sunucusudur (kanallar, düğümler, oturumlar, hook'lar). Bu sayfadaki alt komutlar `openclaw gateway …` altında yer alır.

[**Bonjour discovery** Yerel mDNS + geniş alan DNS-SD kurulumu. ](</tr/gateway/bonjour>) [**Discovery overview** OpenClaw'ın Gateway'leri nasıl duyurduğu ve bulduğu. ](</tr/gateway/discovery>) [**Configuration** Üst düzey Gateway yapılandırma anahtarları. ](</tr/gateway/configuration>)

## Gateway'i Çalıştırma

Yerel bir Gateway süreci çalıştırın:

bashCopy code
[code]
    openclaw gateway
[/code]

Ön plan takma adı:

bashCopy code
[code]
    openclaw gateway run
[/code]

Startup behavior

  * Varsayılan olarak, `~/.openclaw/openclaw.json` içinde `gateway.mode=local` ayarlanmadıkça Gateway başlamayı reddeder. Geçici/geliştirme çalıştırmaları için `--allow-unconfigured` kullanın.
  * `openclaw onboard --mode local` ve `openclaw setup` komutlarının `gateway.mode=local` yazması beklenir. Dosya varsa ancak `gateway.mode` eksikse, bunu bozuk veya üzerine yazılmış bir yapılandırma olarak değerlendirin ve yerel modu örtük olarak varsaymak yerine onarın.
  * Dosya varsa ve `gateway.mode` eksikse, Gateway bunu şüpheli yapılandırma hasarı olarak değerlendirir ve sizin için "yereli tahmin etmeyi" reddeder.
  * Kimlik doğrulama olmadan loopback ötesine bağlanma engellenir (güvenlik koruması).
  * `SIGUSR1`, yetkilendirildiğinde süreç içi yeniden başlatmayı tetikler (`commands.restart` varsayılan olarak etkindir; manuel yeniden başlatmayı engellemek için `commands.restart: false` ayarlayın, gateway aracı/yapılandırma uygulama/güncelleme ise izinli kalır).
  * `SIGINT`/`SIGTERM` işleyicileri gateway sürecini durdurur, ancak özel terminal durumunu geri yüklemez. CLI'yi bir TUI veya raw-mode girişle sararsanız, çıkmadan önce terminali geri yükleyin.


### Seçenekler

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> WebSocket portu (varsayılan yapılandırma/env'den gelir; genellikle `18789`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> Token geçersiz kılma (süreç için `OPENCLAW_GATEWAY_TOKEN` değerini de ayarlar).

Kapanışta Tailscale serve/funnel yapılandırmasını sıfırla.

Yapılandırmada `gateway.mode=local` olmadan gateway başlatmaya izin ver. Başlatma korumasını yalnızca geçici/geliştirme bootstrap için atlar; yapılandırma dosyasını yazmaz veya onarmaz.

Eksikse geliştirme yapılandırması + çalışma alanı oluştur (`BOOTSTRAP.md` atlanır).

Geliştirme yapılandırmasını + kimlik bilgilerini + oturumları + çalışma alanını sıfırla (`--dev` gerektirir).

Başlamadan önce seçilen porttaki mevcut dinleyicileri sonlandır.

Ayrıntılı günlükler.

Konsolda yalnızca CLI backend günlüklerini göster (ve stdout/stderr'ı etkinleştir).

`--ws-log compact` için takma ad.

Ham model akışı olaylarını jsonl olarak günlüğe yaz.

## Gateway'i Yeniden Başlatma

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

`openclaw gateway restart --safe`, yeniden başlatmadan önce çalışan Gateway'den etkin OpenClaw işlerini ön denetimden geçirmesini ister. Kuyruğa alınmış işlemler, yanıt teslimi, gömülü çalıştırmalar veya görev çalıştırmaları etkinse, Gateway engelleyicileri bildirir, yinelenen güvenli yeniden başlatma isteklerini birleştirir ve etkin işler boşaldığında yeniden başlatır. Düz `restart`, uyumluluk için mevcut servis yöneticisi davranışını korur. `--force` yalnızca özellikle anında geçersiz kılma yolunu istediğinizde kullanın.

`openclaw gateway restart --safe --skip-deferral`, `--safe` ile aynı OpenClaw'a duyarlı koordineli yeniden başlatmayı çalıştırır, ancak etkin iş erteleme kapısını atlar; böylece Gateway, engelleyiciler raporlandığında bile yeniden başlatmayı hemen yayar. Bir erteleme takılmış bir görev çalıştırması tarafından sabitlendiğinde ve yalnızca `--safe` süresiz bekleyecekse bunu operatör kaçış yolu olarak kullanın. `--skip-deferral`, `--safe` gerektirir.

### Başlatma profilleme

  * Gateway başlatması sırasında aşama zamanlamalarını günlüğe yazmak için `OPENCLAW_GATEWAY_STARTUP_TRACE=1` ayarlayın; buna her aşama için `eventLoopMax` gecikmesi ve yüklü indeks, manifest kayıt defteri, başlatma planlaması ve owner-map işi için plugin arama tablosu zamanlamaları dahildir.
  * Harici QA koşumları için en iyi çabayla JSONL başlatma tanılama zaman çizelgesi yazmak üzere `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>` ile `OPENCLAW_DIAGNOSTICS=timeline` ayarlayın. Bayrağı yapılandırmada `diagnostics.flags: ["timeline"]` ile de etkinleştirebilirsiniz; yol yine env tarafından sağlanır. Olay döngüsü örneklerini dahil etmek için `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1` ekleyin.
  * Gateway başlatmasını karşılaştırmalı ölçmek için `pnpm test:startup:gateway -- --runs 5 --warmup 1` çalıştırın. Karşılaştırma ölçümü ilk süreç çıktısını, `/healthz`, `/readyz`, başlatma izleme zamanlamalarını, olay döngüsü gecikmesini ve plugin arama tablosu zamanlama ayrıntılarını kaydeder.


## Çalışan bir Gateway'i Sorgulama

Tüm sorgu komutları WebSocket RPC kullanır.

### Output modes

  * Varsayılan: insan tarafından okunabilir (TTY'de renkli).
  * `--json`: makine tarafından okunabilir JSON (biçimlendirme/spinner yok).
  * `--no-color` (veya `NO_COLOR=1`): insan düzenini korurken ANSI'yi devre dışı bırakır.


### Shared options

  * `--url <url>`: Gateway WebSocket URL'si.
  * `--token <token>`: Gateway token'ı.
  * `--password <password>`: Gateway parolası.
  * `--timeout <ms>`: zaman aşımı/bütçe (komuta göre değişir).
  * `--expect-final`: bir "final" yanıtı bekle (ajan çağrıları).


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789
[/code]

HTTP `/healthz` uç noktası bir canlılık yoklamasıdır: sunucu HTTP'ye yanıt verebildiğinde döner. HTTP `/readyz` uç noktası daha katıdır ve başlatma plugin sidecar'ları, kanallar veya yapılandırılmış hook'lar hâlâ yerleşirken kırmızı kalır. Yerel veya kimliği doğrulanmış ayrıntılı hazır olma yanıtları, olay döngüsü gecikmesi, olay döngüsü kullanımı, CPU çekirdek oranı ve bir `degraded` bayrağı içeren bir `eventLoop` tanılama bloğu içerir.

### `gateway usage-cost`

Oturum günlüklerinden kullanım-maliyeti özetlerini getir.

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --json
[/code]

### `gateway stability`

Çalışan bir Gateway'den son tanılama kararlılık kaydedicisini getir.

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> Dahil edilecek en fazla son olay sayısı (maks `1000`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> `payload.large` veya `diagnostic.memory.pressure` gibi tanılama olay türüne göre filtrele.

Çalışan Gateway'i çağırmak yerine kalıcı bir kararlılık paketini oku. Durum dizini altındaki en yeni paket için `--bundle latest` (veya yalnızca `--bundle`) kullanın ya da doğrudan bir paket JSON yolu geçin.

Kararlılık ayrıntılarını yazdırmak yerine paylaşılabilir bir destek tanılama zip'i yaz.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> `--export` için çıktı yolu.

Privacy and bundle behavior

  * Kayıtlar operasyonel meta verileri tutar: olay adları, sayımlar, bayt boyutları, bellek okumaları, kuyruk/oturum durumu, kanal/plugin adları ve redakte edilmiş oturum özetleri. Sohbet metni, webhook gövdeleri, araç çıktıları, ham istek veya yanıt gövdeleri, token'lar, çerezler, gizli değerler, host adları veya ham oturum kimliklerini tutmazlar. Kaydediciyi tamamen devre dışı bırakmak için `diagnostics.enabled: false` ayarlayın.
  * Ölümcül Gateway çıkışlarında, kapanma zaman aşımlarında ve yeniden başlatma başlatma hatalarında, kaydedicinin olayları varsa OpenClaw aynı tanılama anlık görüntüsünü `~/.openclaw/logs/stability/openclaw-stability-*.json` konumuna yazar. En yeni paketi `openclaw gateway stability --bundle latest` ile inceleyin; `--limit`, `--type` ve `--since-seq` paket çıktısına da uygulanır.


### `gateway diagnostics export`

Hata raporlarına eklenmek üzere tasarlanmış yerel bir tanılama zip'i yaz. Gizlilik modeli ve paket içerikleri için bkz. [Tanılama Dışa Aktarma](</tr/gateway/diagnostics>).

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

Kalıcı kararlılık paketi aramasını atla.

Yazılan yolu, boyutu ve manifesti JSON olarak yazdır.

Dışa aktarım bir manifest, Markdown özeti, yapılandırma şekli, temizlenmiş yapılandırma ayrıntıları, temizlenmiş günlük özetleri, temizlenmiş Gateway durum/sağlık anlık görüntüleri ve varsa en yeni kararlılık paketini içerir.

Paylaşılması amaçlanır. Hata ayıklamaya yardımcı olan güvenli OpenClaw günlük alanları, alt sistem adları, durum kodları, süreler, yapılandırılmış modlar, portlar, plugin kimlikleri, sağlayıcı kimlikleri, gizli olmayan özellik ayarları ve redakte edilmiş operasyonel günlük iletileri gibi operasyonel ayrıntıları tutar. Sohbet metnini, webhook gövdelerini, araç çıktılarını, kimlik bilgilerini, çerezleri, hesap/ileti tanımlayıcılarını, prompt/talimat metnini, host adlarını ve gizli değerleri çıkarır veya redakte eder. LogTape tarzı bir ileti kullanıcı/sohbet/araç payload metnine benzediğinde, dışa aktarım yalnızca bir iletinin çıkarıldığını ve bayt sayısını tutar.

### `gateway status`

`gateway status`, Gateway servisini (launchd/systemd/schtasks) ve bağlantı/kimlik doğrulama yeteneğine ilişkin isteğe bağlı bir yoklamayı gösterir.

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

Bağlantı yoklamasını atla (yalnızca hizmet görünümü).

Sistem düzeyi hizmetleri de tara.

Varsayılan bağlantı yoklamasını bir okuma yoklamasına yükselt ve bu okuma yoklaması başarısız olduğunda sıfır olmayan kodla çık. `--no-probe` ile birlikte kullanılamaz.

Durum semantiği

  * `gateway status`, yerel CLI yapılandırması eksik veya geçersiz olsa bile tanılama için kullanılabilir kalır.
  * Varsayılan `gateway status`, hizmet durumunu, WebSocket bağlantısını ve el sıkışma zamanında görünen kimlik doğrulama yeteneğini kanıtlar. Okuma/yazma/yönetici işlemlerini kanıtlamaz.
  * Tanılama yoklamaları, ilk kez cihaz kimlik doğrulaması için değişiklik yapmaz: varsa mevcut önbelleğe alınmış cihaz token'ını yeniden kullanırlar, ancak yalnızca durumu denetlemek için yeni bir CLI cihaz kimliği veya salt okunur cihaz eşleme kaydı oluşturmazlar.
  * `gateway status`, mümkün olduğunda yoklama kimlik doğrulaması için yapılandırılmış kimlik doğrulama SecretRef'lerini çözer.
  * Bu komut yolunda gerekli bir kimlik doğrulama SecretRef'i çözümlenmemişse, yoklama bağlantısı/kimlik doğrulaması başarısız olduğunda `gateway status --json` `rpc.authWarning` bildirir; `--token`/`--password` değerini açıkça iletin veya önce gizli kaynak bilgisini çözün.
  * Yoklama başarılı olursa, yanlış pozitifleri önlemek için çözümlenmemiş auth-ref uyarıları bastırılır.
  * Dinleyen bir hizmet yeterli olmadığında ve okuma kapsamlı RPC çağrılarının da sağlıklı olması gerektiğinde betiklerde ve otomasyonda `--require-rpc` kullanın.
  * `--deep`, ek launchd/systemd/schtasks kurulumları için en iyi çabayla bir tarama ekler. Birden çok Gateway benzeri hizmet algılandığında, insan çıktısı temizleme ipuçları yazdırır ve çoğu kurulumun makine başına bir Gateway çalıştırması gerektiği konusunda uyarır.
  * `--deep`, hizmet süreci harici bir süpervizör yeniden başlatması için temiz şekilde çıktığında yakın tarihli bir Gateway süpervizör yeniden başlatma devrini de bildirir.
  * `--deep`, yapılandırma doğrulamasını Plugin farkındalığı modunda (`pluginValidation: "full"`) çalıştırır ve yapılandırılmış Plugin manifest uyarılarını (örneğin eksik kanal yapılandırma metaverisi) yüzeye çıkarır; böylece kurulum ve güncelleme smoke denetimleri bunları yakalar. Varsayılan `gateway status`, Plugin doğrulamasını atlayan hızlı salt okunur yolu korur.
  * İnsan çıktısı, profil veya state-dir sapmasını tanılamaya yardımcı olmak için çözümlenmiş dosya günlük yolunu ve CLI-hizmet yapılandırma yolları/geçerlilik anlık görüntüsünü içerir.

Linux systemd kimlik doğrulama sapması denetimleri

  * Linux systemd kurulumlarında, hizmet kimlik doğrulama sapması denetimleri birimden hem `Environment=` hem de `EnvironmentFile=` değerlerini okur (`%h`, tırnaklı yollar, birden çok dosya ve isteğe bağlı `-` dosyaları dahil).
  * Sapma denetimleri, birleştirilmiş çalışma zamanı env değerini kullanarak `gateway.auth.token` SecretRef'lerini çözer (önce hizmet komutu env, sonra süreç env yedeği).
  * Token kimlik doğrulaması etkin olarak aktif değilse (açık `gateway.auth.mode` değeri `password`/`none`/`trusted-proxy` ise ya da mod ayarlanmamışken parolanın kazanabildiği ve hiçbir token adayının kazanamadığı durumda), token sapması denetimleri yapılandırma token çözümlemesini atlar.


### `gateway probe`

`gateway probe`, "her şeyin hata ayıklaması" komutudur. Her zaman şunları yoklar:

  * yapılandırılmış uzak gateway'iniz (ayarlanmışsa) ve
  * localhost (loopback), **uzak yapılandırılmış olsa bile**.


`--url` iletirseniz, bu açık hedef ikisinin de önüne eklenir. İnsan çıktısı hedefleri şöyle etiketler:

  * `URL (explicit)`
  * `Remote (configured)` veya `Remote (configured, inactive)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --json
[/code]

Yorumlama

  * `Reachable: yes`, en az bir hedefin WebSocket bağlantısını kabul ettiği anlamına gelir.
  * `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only`, yoklamanın kimlik doğrulama hakkında neyi kanıtlayabildiğini bildirir. Bu, erişilebilirlikten ayrıdır.
  * `Read probe: ok`, okuma kapsamlı ayrıntı RPC çağrılarının (`health`/`status`/`system-presence`/`config.get`) da başarılı olduğu anlamına gelir.
  * `Read probe: limited - missing scope: operator.read`, bağlantının başarılı olduğunu ancak okuma kapsamlı RPC'nin sınırlı olduğunu gösterir. Bu, tam hata olarak değil **düşük kaliteli** erişilebilirlik olarak bildirilir.
  * `Connect: ok` sonrasında `Read probe: failed`, Gateway'in WebSocket bağlantısını kabul ettiği, ancak takip eden okuma tanılamalarının zaman aşımına uğradığı veya başarısız olduğu anlamına gelir. Bu da erişilemeyen bir Gateway değil, **düşük kaliteli** erişilebilirliktir.
  * `gateway status` gibi, probe mevcut önbelleğe alınmış cihaz kimlik doğrulamasını yeniden kullanır ancak ilk kez cihaz kimliği veya eşleme durumu oluşturmaz.
  * Çıkış kodu yalnızca yoklanan hiçbir hedef erişilebilir değilse sıfır olmayan değerdir.

JSON çıktısı

Üst düzey:

  * `ok`: en az bir hedef erişilebilir.
  * `degraded`: en az bir hedef bağlantıyı kabul etti ancak tam ayrıntı RPC tanılamalarını tamamlamadı.
  * `capability`: erişilebilir hedefler arasında görülen en iyi yetenek (`read_only`, `write_capable`, `admin_capable`, `pairing_pending`, `connected_no_operator_scope` veya `unknown`).
  * `primaryTargetId`: şu sırayla etkin kazanan olarak ele alınacak en iyi hedef: açık URL, SSH tüneli, yapılandırılmış uzak ve ardından local loopback.
  * `warnings[]`: `code`, `message` ve isteğe bağlı `targetIds` içeren en iyi çabayla uyarı kayıtları.
  * `network`: geçerli yapılandırmadan ve host ağından türetilen local loopback/tailnet URL ipuçları.
  * `discovery.timeoutMs` ve `discovery.count`: bu yoklama geçişi için kullanılan gerçek keşif bütçesi/sonuç sayısı.


Hedef başına (`targets[].connect`):

  * `ok`: bağlantı + düşük kalite sınıflandırmasından sonraki erişilebilirlik.
  * `rpcOk`: tam ayrıntı RPC başarısı.
  * `scopeLimited`: ayrıntı RPC, eksik operator kapsamı nedeniyle başarısız oldu.


Hedef başına (`targets[].auth`):

  * `role`: varsa `hello-ok` içinde bildirilen kimlik doğrulama rolü.
  * `scopes`: varsa `hello-ok` içinde bildirilen verilmiş kapsamlar.
  * `capability`: o hedef için yüzeye çıkarılan kimlik doğrulama yeteneği sınıflandırması.

Yaygın uyarı kodları

  * `ssh_tunnel_failed`: SSH tüneli kurulumu başarısız oldu; komut doğrudan yoklamalara geri döndü.
  * `multiple_gateways`: birden fazla hedef erişilebilirdi; bir kurtarma botu gibi izole profilleri kasıtlı olarak çalıştırmıyorsanız bu olağandışıdır.
  * `auth_secretref_unresolved`: yapılandırılmış bir kimlik doğrulama SecretRef'i, başarısız bir hedef için çözümlenemedi.
  * `probe_scope_limited`: WebSocket bağlantısı başarılı oldu, ancak okuma yoklaması eksik `operator.read` nedeniyle sınırlıydı.


#### SSH üzerinden uzak (Mac uygulaması eşdeğeri)

macOS uygulamasındaki "Remote over SSH" modu, uzak gateway'in (yalnızca loopback'e bağlı olabilir) `ws://127.0.0.1:<port>` adresinden erişilebilir olmasını sağlamak için yerel port yönlendirme kullanır.

CLI eşdeğeri:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` veya `user@host:port` (port varsayılanı `22`).

Çözümlenmiş keşif uç noktasından (`local.` artı varsa yapılandırılmış geniş alan etki alanı) ilk keşfedilen gateway host'unu SSH hedefi olarak seçin. Yalnızca TXT ipuçları yoksayılır.

Yapılandırma (isteğe bağlı, varsayılanlar olarak kullanılır):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

Düşük düzey RPC yardımcısı.

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

Temelde, son yükten önce ara olayları akış olarak veren ajan tarzı RPC'ler içindir.

Makine tarafından okunabilir JSON çıktısı.

## Gateway hizmetini yönetin

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### Bir wrapper ile kurma

Yönetilen hizmetin başka bir yürütülebilir üzerinden başlaması gerektiğinde `--wrapper` kullanın; örneğin bir secrets manager shim'i veya run-as yardımcısı. Wrapper normal Gateway argümanlarını alır ve sonunda bu argümanlarla `openclaw` veya Node'u exec etmekten sorumludur.

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

Wrapper'ı ortam üzerinden de ayarlayabilirsiniz. `gateway install`, yolun yürütülebilir bir dosya olduğunu doğrular, wrapper'ı hizmet `ProgramArguments` içine yazar ve sonraki zorunlu yeniden kurulumlar, güncellemeler ve doctor onarımları için hizmet ortamında `OPENCLAW_WRAPPER` değerini kalıcı hale getirir.

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

Kalıcı bir wrapper'ı kaldırmak için, yeniden kurarken `OPENCLAW_WRAPPER` değerini temizleyin:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

Komut seçenekleri

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

Yaşam döngüsü davranışı

  * Yönetilen bir hizmeti yeniden başlatmak için `gateway restart` kullanın. Yeniden başlatma yerine `gateway stop` ve `gateway start` komutlarını zincirlemeyin.
  * macOS'ta `gateway stop` varsayılan olarak `launchctl bootout` kullanır; bu, LaunchAgent'ı kalıcı bir devre dışı bırakma oluşturmadan geçerli önyükleme oturumundan kaldırır — KeepAlive otomatik kurtarması gelecekteki çökmeler için etkin kalır ve `gateway start`, manuel `launchctl enable` gerektirmeden temiz şekilde yeniden etkinleştirir. Gateway bir sonraki açık `gateway start` komutuna kadar yeniden doğmasın diye KeepAlive ve RunAtLoad'u kalıcı olarak bastırmak için `--disable` iletin; manuel durdurmanın yeniden başlatmalardan veya sistem yeniden başlatmalarından sonra da korunması gerektiğinde bunu kullanın.
  * `gateway restart --safe`, çalışan Gateway'den etkin OpenClaw çalışmalarını ön denetimden geçirmesini ve yanıt teslimi, gömülü çalıştırmalar ve görev çalıştırmaları boşalana kadar yeniden başlatmayı ertelemesini ister. `--safe`, `--force` veya `--wait` ile birleştirilemez.
  * `gateway restart --wait 30s`, o yeniden başlatma için yapılandırılmış yeniden başlatma boşaltma bütçesini geçersiz kılar. Çıplak sayılar milisaniyedir; `s`, `m` ve `h` gibi birimler kabul edilir. `--wait 0` süresiz bekler.
  * `gateway restart --safe --skip-deferral`, OpenClaw farkındalıklı güvenli yeniden başlatmayı çalıştırır ancak erteleme geçidini atlar; böylece engelleyiciler bildirilse bile Gateway yeniden başlatmayı hemen yayar. Takılmış görev çalıştırma ertelemeleri için operatör kaçış yoludur; `--safe` gerektirir.
  * `gateway restart --force`, etkin çalışma boşaltmasını atlar ve hemen yeniden başlatır. Operatör listelenen görev engelleyicilerini zaten incelediğinde ve Gateway'i hemen geri istediğinde bunu kullanın.
  * Yaşam döngüsü komutları betikleme için `--json` kabul eder.

Kurulum sırasında kimlik doğrulama ve SecretRefs

  * Token kimlik doğrulaması bir token gerektirdiğinde ve `gateway.auth.token` SecretRef tarafından yönetildiğinde, `gateway install` SecretRef'in çözümlenebilir olduğunu doğrular ancak çözümlenen token'ı hizmet ortamı meta verilerine kalıcı olarak yazmaz.
  * Token kimlik doğrulaması bir token gerektiriyorsa ve yapılandırılmış token SecretRef'i çözümlenemiyorsa, kurulum yedek düz metni kalıcı olarak yazmak yerine kapalı şekilde başarısız olur.
  * `gateway run` üzerinde parola kimlik doğrulaması için satır içi `--password` yerine `OPENCLAW_GATEWAY_PASSWORD`, `--password-file` veya SecretRef destekli `gateway.auth.password` tercih edin.
  * Çıkarımsal kimlik doğrulama modunda, yalnızca kabuktaki `OPENCLAW_GATEWAY_PASSWORD` kurulum token gereksinimlerini gevşetmez; yönetilen bir hizmet kurarken kalıcı yapılandırma (`gateway.auth.password` veya yapılandırma `env`) kullanın.
  * Hem `gateway.auth.token` hem de `gateway.auth.password` yapılandırılmışsa ve `gateway.auth.mode` ayarlanmamışsa, mod açıkça ayarlanana kadar kurulum engellenir.


## Gateway'leri keşfet (Bonjour)

`gateway discover`, Gateway işaretçilerini (`_openclaw-gw._tcp`) tarar.

  * Çok noktaya yayın DNS-SD: `local.`
  * Tek noktaya yayın DNS-SD (Geniş Alan Bonjour): bir etki alanı seçin (örnek: `openclaw.internal.`) ve bölünmüş DNS + bir DNS sunucusu kurun; bkz. [Bonjour](</tr/gateway/bonjour>).


Yalnızca Bonjour keşfi etkin olan Gateway'ler (varsayılan) işaretçiyi duyurur.

Geniş alan keşif kayıtları şu TXT ipuçlarını içerebilir:

  * `role` (Gateway rol ipucu)
  * `transport` (aktarım ipucu, ör. `gateway`)
  * `gatewayPort` (WebSocket bağlantı noktası, genellikle `18789`)
  * `sshPort` (yalnızca tam keşif modu; istemciler, yoksa SSH hedeflerini varsayılan olarak `22` kabul eder)
  * `tailnetDns` (varsa MagicDNS ana makine adı)
  * `gatewayTls` / `gatewayTlsSha256` (TLS etkin + sertifika parmak izi)
  * `cliPath` (yalnızca tam keşif modu)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

Makine tarafından okunabilir çıktı (biçimlendirmeyi/döndürücüyü de devre dışı bırakır).

Örnekler:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Gateway çalışma kitabı](</tr/gateway>)


Was this useful?YesNo