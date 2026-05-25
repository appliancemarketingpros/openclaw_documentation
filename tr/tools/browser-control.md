---
title: Tarayıcı kontrol API'si
source_url: https://docs.openclaw.ai/tr/tools/browser-control
scraped_at: 2026-05-25
---

Kurulum, yapılandırma ve sorun giderme için bkz. [Tarayıcı](</tr/tools/browser>). Bu sayfa, yerel denetim HTTP API'si, `openclaw browser` CLI'si ve betik kalıpları (anlık görüntüler, ref'ler, beklemeler, hata ayıklama akışları) için referanstır.

## Denetim API'si (isteğe bağlı)

Yalnızca yerel entegrasyonlar için Gateway küçük bir loopback HTTP API'si sunar:

  * Durum/başlat/durdur: `GET /`, `POST /start`, `POST /stop`
  * Sekmeler: `GET /tabs`, `POST /tabs/open`, `POST /tabs/focus`, `DELETE /tabs/:targetId`
  * Anlık görüntü/ekran görüntüsü: `GET /snapshot`, `POST /screenshot`
  * Eylemler: `POST /navigate`, `POST /act`
  * Kancalar: `POST /hooks/file-chooser`, `POST /hooks/dialog`
  * İndirmeler: `POST /download`, `POST /wait/download`
  * İzinler: `POST /permissions/grant`
  * Hata ayıklama: `GET /console`, `POST /pdf`
  * Hata ayıklama: `GET /errors`, `GET /requests`, `POST /trace/start`, `POST /trace/stop`, `POST /highlight`
  * Ağ: `POST /response/body`
  * Durum: `GET /cookies`, `POST /cookies/set`, `POST /cookies/clear`
  * Durum: `GET /storage/:kind`, `POST /storage/:kind/set`, `POST /storage/:kind/clear`
  * Ayarlar: `POST /set/offline`, `POST /set/headers`, `POST /set/credentials`, `POST /set/geolocation`, `POST /set/media`, `POST /set/timezone`, `POST /set/locale`, `POST /set/device`


Tüm uç noktalar `?profile=<name>` kabul eder. `POST /start?headless=true`, kalıcı tarayıcı yapılandırmasını değiştirmeden yerel yönetilen profiller için tek seferlik başsız başlatma ister; yalnızca bağlanma, uzak CDP ve mevcut oturum profilleri bu geçersiz kılmayı reddeder, çünkü OpenClaw bu tarayıcı süreçlerini başlatmaz.

Paylaşılan gizli anahtarlı Gateway kimlik doğrulaması yapılandırılmışsa tarayıcı HTTP rotaları da kimlik doğrulaması gerektirir:

  * `Authorization: Bearer <gateway token>`
  * `x-openclaw-password: <gateway password>` veya bu parolayla HTTP Basic kimlik doğrulaması


Notlar:

  * Bu bağımsız loopback tarayıcı API'si güvenilir proxy veya Tailscale Serve kimlik başlıklarını **kullanmaz**.
  * `gateway.auth.mode`, `none` veya `trusted-proxy` ise bu loopback tarayıcı rotaları kimlik taşıyan bu modları devralmaz; bunları yalnızca loopback olarak tutun.


### `/act` hata sözleşmesi

`POST /act`, rota düzeyi doğrulama ve ilke hataları için yapılandırılmış bir hata yanıtı kullanır:

jsonCopy code
[code]
    { "error": "<message>", "code": "ACT_*" }
[/code]

Geçerli `code` değerleri:

  * `ACT_KIND_REQUIRED` (HTTP 400): `kind` eksik veya tanınmıyor.
  * `ACT_INVALID_REQUEST` (HTTP 400): eylem yükü normalleştirme veya doğrulamadan geçemedi.
  * `ACT_SELECTOR_UNSUPPORTED` (HTTP 400): `selector`, desteklenmeyen bir eylem türüyle kullanıldı.
  * `ACT_EVALUATE_DISABLED` (HTTP 403): `evaluate` (veya `wait --fn`) yapılandırma tarafından devre dışı bırakıldı.
  * `ACT_TARGET_ID_MISMATCH` (HTTP 403): üst düzey veya toplu `targetId`, istek hedefiyle çakışıyor.
  * `ACT_EXISTING_SESSION_UNSUPPORTED` (HTTP 501): eylem, mevcut oturum profilleri için desteklenmiyor.


Diğer çalışma zamanı hataları hâlâ `code` alanı olmadan `{ "error": "<message>" }` döndürebilir.

### Playwright gereksinimi

Bazı özellikler (navigate/act/AI anlık görüntüsü/rol anlık görüntüsü, öğe ekran görüntüleri, PDF) Playwright gerektirir. Playwright yüklü değilse bu uç noktalar açık bir 501 hatası döndürür.

Playwright olmadan çalışmaya devam edenler:

  * ARIA anlık görüntüleri
  * Sekme başına CDP WebSocket kullanılabilir olduğunda rol tarzı erişilebilirlik anlık görüntüleri (`--interactive`, `--compact`, `--depth`, `--efficient`). Bu, inceleme ve ref keşfi için bir yedektir; Playwright birincil eylem motoru olmaya devam eder.
  * Sekme başına CDP WebSocket kullanılabilir olduğunda yönetilen `openclaw` tarayıcısı için sayfa ekran görüntüleri
  * `existing-session` / Chrome MCP profilleri için sayfa ekran görüntüleri
  * Anlık görüntü çıktısından `existing-session` ref tabanlı ekran görüntüleri (`--ref`)


Hâlâ Playwright gerektirenler:

  * `navigate`
  * `act`
  * Playwright'ın yerel AI anlık görüntü biçimine bağlı AI anlık görüntüleri
  * CSS seçici öğe ekran görüntüleri (`--element`)
  * tam tarayıcı PDF dışa aktarımı


Öğe ekran görüntüleri `--full-page` seçeneğini de reddeder; rota `fullPage is not supported for element screenshots` döndürür.

`Playwright is not available in this gateway build` görürseniz paketlenmiş Gateway çekirdek tarayıcı çalışma zamanı bağımlılığını içermiyor demektir. OpenClaw'ı yeniden yükleyin veya güncelleyin, ardından gateway'i yeniden başlatın. Docker için aşağıda gösterildiği gibi Chromium tarayıcı ikililerini de yükleyin.

#### Docker Playwright kurulumu

Gateway'iniz Docker'da çalışıyorsa `npx playwright` kullanmayın (npm geçersiz kılma çakışmaları). Özel imajlar için Chromium'u imaja dahil edin:

bashCopy code
[code]
    OPENCLAW_INSTALL_BROWSER=1 ./scripts/docker/setup.sh
[/code]

Mevcut bir imaj için bunun yerine paketlenmiş CLI üzerinden yükleyin:

bashCopy code
[code]
    docker compose run --rm openclaw-cli \  node /app/node_modules/playwright-core/cli.js install chromium
[/code]

Tarayıcı indirmelerini kalıcı yapmak için `PLAYWRIGHT_BROWSERS_PATH` değerini ayarlayın (örneğin `/home/node/.cache/ms-playwright`) ve `/home/node` yolunun `OPENCLAW_HOME_VOLUME` veya bir bind mount ile kalıcı olduğundan emin olun. OpenClaw, Linux'ta kalıcı Chromium'u otomatik algılar. Bkz. [Docker](</tr/install/docker>).

## Nasıl çalışır (dahili)

Küçük bir loopback denetim sunucusu HTTP isteklerini kabul eder ve CDP üzerinden Chromium tabanlı tarayıcılara bağlanır. Gelişmiş eylemler (tıklama/yazma/anlık görüntü/PDF), CDP'nin üzerinde Playwright üzerinden çalışır; Playwright eksik olduğunda yalnızca Playwright dışı işlemler kullanılabilir. Aracı, yerel/uzak tarayıcılar ve profiller altta serbestçe değişirken tek bir kararlı arayüz görür.

## CLI hızlı başvuru

Tüm komutlar belirli bir profili hedeflemek için `--browser-profile <name>`, makine tarafından okunabilir çıktı için `--json` kabul eder.

Temeller: durum, sekmeler, aç/odakla/kapat bashCopy code
[code]
    openclaw browser statusopenclaw browser startopenclaw browser start --headless # tek seferlik yerel yönetilen başsız başlatmaopenclaw browser stop            # yalnızca bağlanma/uzak CDP üzerinde emülasyonu da temizleropenclaw browser tabsopenclaw browser tab             # geçerli sekme için kısayolopenclaw browser tab newopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://example.comopenclaw browser focus abcd1234openclaw browser close abcd1234
[/code]

İnceleme: ekran görüntüsü, anlık görüntü, konsol, hatalar, istekler bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref 12        # veya role ref'leri için --ref e12openclaw browser screenshot --labelsopenclaw browser snapshotopenclaw browser snapshot --format aria --limit 200openclaw browser snapshot --interactive --compact --depth 6openclaw browser snapshot --efficientopenclaw browser snapshot --labelsopenclaw browser snapshot --urlsopenclaw browser snapshot --selector "#main" --interactiveopenclaw browser snapshot --frame "iframe#main" --interactiveopenclaw browser console --level erroropenclaw browser errors --clearopenclaw browser requests --filter api --clearopenclaw browser pdfopenclaw browser responsebody "**/api" --max-chars 5000
[/code]

Eylemler: gezin, tıkla, yaz, sürükle, bekle, değerlendir bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser resize 1280 720openclaw browser click 12 --double           # veya rol ref'leri için e12openclaw browser click-coords 120 340        # görüntü alanı koordinatlarıopenclaw browser type 23 "hello" --submitopenclaw browser press Enteropenclaw browser hover 44openclaw browser scrollintoview e12openclaw browser drag 10 11openclaw browser select 9 OptionA OptionBopenclaw browser download e12 report.pdfopenclaw browser waitfordownload report.pdfopenclaw browser upload /tmp/openclaw/uploads/file.pdfopenclaw browser fill --fields '[{"ref":"1","type":"text","value":"Ada"}]'openclaw browser dialog --acceptopenclaw browser wait --text "Done"openclaw browser wait "#main" --url "**/dash" --load networkidle --fn "window.ready===true"openclaw browser evaluate --fn '(el) => el.textContent' --ref 7openclaw browser highlight e12openclaw browser trace startopenclaw browser trace stop
[/code]

Durum: çerezler, depolama, çevrimdışı, başlıklar, coğrafi konum, cihaz bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url "https://example.com"openclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set theme darkopenclaw browser storage session clearopenclaw browser set offline onopenclaw browser set headers --headers-json '{"X-Debug":"1"}'openclaw browser set credentials user pass            # kaldırmak için --clearopenclaw browser set geo 37.7749 -122.4194 --origin "https://example.com"openclaw browser set media darkopenclaw browser set timezone America/New_Yorkopenclaw browser set locale en-USopenclaw browser set device "iPhone 14"
[/code]

Notlar:

  * `upload` ve `dialog` **hazırlama** çağrılarıdır; bunları seçiciyi/iletişim kutusunu tetikleyen tıklama/basma işleminden önce çalıştırın.
  * `click`/`type`/vb., `snapshot` içinden bir `ref` gerektirir (sayısal `12`, rol ref'i `e12` veya eyleme geçirilebilir ARIA ref'i `ax12`). CSS seçiciler eylemler için kasıtlı olarak desteklenmez. Görünür görüntü alanı konumu tek güvenilir hedef olduğunda `click-coords` kullanın.
  * İndirme, izleme ve yükleme yolları OpenClaw geçici kökleriyle sınırlıdır: `/tmp/openclaw{,/downloads,/uploads}` (yedek: `${os.tmpdir()}/openclaw/...`).
  * `upload`, `--input-ref` veya `--element` üzerinden dosya girişlerini doğrudan da ayarlayabilir.


OpenClaw, aynı URL gibi değiştirme sekmesini kanıtlayabildiğinde veya form gönderiminden sonra tek bir eski sekme tek bir yeni sekmeye dönüştüğünde, kararlı sekme kimlikleri ve etiketleri Chromium ham hedef değişiminden sonra da korunur. Ham hedef kimlikleri hâlâ değişkendir; betiklerde `tabs` içinden `suggestedTargetId` tercih edin.

Anlık görüntü bayraklarına kısa bakış:

  * `--format ai` (Playwright ile varsayılan): sayısal ref'lerle AI anlık görüntüsü (`aria-ref="<n>"`).
  * `--format aria`: `axN` ref'lerine sahip erişilebilirlik ağacı. Playwright kullanılabilir olduğunda OpenClaw, takip eden eylemlerin bunları kullanabilmesi için ref'leri arka uç DOM kimlikleriyle canlı sayfaya bağlar; aksi halde çıktıyı yalnızca inceleme amaçlı kabul edin.
  * `--efficient` (veya `--mode efficient`): kompakt rol anlık görüntüsü ön ayarı. Bunu varsayılan yapmak için `browser.snapshotDefaults.mode: "efficient"` ayarlayın (bkz. [Gateway yapılandırması](</tr/gateway/configuration-reference#browser>)).
  * `--interactive`, `--compact`, `--depth`, `--selector`, `ref=e12` ref'leriyle bir rol anlık görüntüsünü zorlar. `--frame "<iframe>"`, rol anlık görüntülerini bir iframe ile sınırlar.
  * `--labels`, üzerine ref etiketleri bindirilmiş yalnızca görüntü alanı ekran görüntüsü ekler (`MEDIA:<path>` yazdırır).
  * `--urls`, keşfedilen bağlantı hedeflerini AI anlık görüntülerine ekler.


## Anlık görüntüler ve ref'ler

OpenClaw iki "anlık görüntü" stilini destekler:

  * **AI anlık görüntüsü (sayısal ref'ler)** : `openclaw browser snapshot` (varsayılan; `--format ai`)

    * Çıktı: sayısal ref'ler içeren bir metin anlık görüntüsü.
    * Eylemler: `openclaw browser click 12`, `openclaw browser type 23 "hello"`.
    * Dahili olarak ref, Playwright'ın `aria-ref` değeri üzerinden çözümlenir.
  * **Rol anlık görüntüsü (`e12` gibi rol ref'leri)**: `openclaw browser snapshot --interactive` (veya `--compact`, `--depth`, `--selector`, `--frame`)

    * Çıktı: `[ref=e12]` (ve isteğe bağlı `[nth=1]`) içeren rol tabanlı liste/ağaç.
    * Eylemler: `openclaw browser click e12`, `openclaw browser highlight e12`.
    * Dahili olarak ref, `getByRole(...)` (çoğaltmalar için ayrıca `nth()`) üzerinden çözümlenir.
    * Üzerine `e12` etiketleri bindirilmiş bir görüntü alanı ekran görüntüsü eklemek için `--labels` ekleyin.
    * Bağlantı metni belirsiz olduğunda ve aracının somut gezinme hedeflerine ihtiyacı olduğunda `--urls` ekleyin.
  * **ARIA anlık görüntüsü (`ax12` gibi ARIA referansları)**: `openclaw browser snapshot --format aria`

    * Çıktı: yapılandırılmış düğümler olarak erişilebilirlik ağacı.
    * Eylemler: anlık görüntü yolu, referansı Playwright ve Chrome arka uç DOM kimlikleri üzerinden bağlayabildiğinde `openclaw browser click ax12` çalışır.
  * Playwright kullanılamıyorsa ARIA anlık görüntüleri inceleme için yine de yararlı olabilir, ancak referanslar eyleme dönüştürülemeyebilir. Eylem referanslarına ihtiyacınız olduğunda `--format ai` veya `--interactive` ile yeniden anlık görüntü alın.

  * Ham-CDP yedek yolunun Docker kanıtı: `pnpm test:docker:browser-cdp-snapshot`, Chromium'u CDP ile başlatır, `browser doctor --deep` çalıştırır ve rol anlık görüntülerinin bağlantı URL'lerini, imleçle yükseltilmiş tıklanabilir öğeleri ve iframe metadata'sını içerdiğini doğrular.


Referans davranışı:

  * Referanslar **gezinmeler arasında kararlı değildir** ; bir şey başarısız olursa `snapshot` komutunu yeniden çalıştırın ve yeni bir referans kullanın.
  * `/act`, değiştirme sekmesini kanıtlayabildiğinde eylemle tetiklenen değiştirmeden sonra geçerli ham `targetId` değerini döndürür. Devam komutları için kararlı sekme kimliklerini/etiketlerini kullanmaya devam edin.
  * Rol anlık görüntüsü `--frame` ile alındıysa rol referansları bir sonraki rol anlık görüntüsüne kadar bu iframe kapsamındadır.
  * Bilinmeyen veya eskimiş `axN` referansları, Playwright'ın `aria-ref` seçicisine düşmek yerine hızlıca başarısız olur. Bu olduğunda aynı sekmede yeni bir anlık görüntü çalıştırın.


## Bekleme güçlendirmeleri

Yalnızca süre/metinden daha fazlasını bekleyebilirsiniz:

  * URL bekleme (glob'lar Playwright tarafından desteklenir): 
    * `openclaw browser wait --url "**/dash"`
  * Yükleme durumunu bekleme: 
    * `openclaw browser wait --load networkidle`
  * JS koşulunu bekleme: 
    * `openclaw browser wait --fn "window.ready===true"`
  * Bir seçicinin görünür olmasını bekleme: 
    * `openclaw browser wait "#main"`


Bunlar birleştirilebilir:

bashCopy code
[code]
    openclaw browser wait "#main" \  --url "**/dash" \  --load networkidle \  --fn "window.ready===true" \  --timeout-ms 15000
[/code]

## Hata ayıklama iş akışları

Bir eylem başarısız olduğunda (ör. "not visible", "strict mode violation", "covered"):

  1. `openclaw browser snapshot --interactive`
  2. `click <ref>` / `type <ref>` kullanın (etkileşimli modda rol referanslarını tercih edin)
  3. Hâlâ başarısız olursa: Playwright'ın neyi hedeflediğini görmek için `openclaw browser highlight <ref>`
  4. Sayfa garip davranıyorsa: 
     * `openclaw browser errors --clear`
     * `openclaw browser requests --filter api --clear`
  5. Derin hata ayıklama için bir trace kaydedin: 
     * `openclaw browser trace start`
     * sorunu yeniden üretin
     * `openclaw browser trace stop` (`TRACE:<path>` yazdırır)


## JSON çıktısı

`--json`, betikleme ve yapılandırılmış araçlar içindir.

Örnekler:

bashCopy code
[code]
    openclaw browser status --jsonopenclaw browser snapshot --interactive --jsonopenclaw browser requests --filter api --jsonopenclaw browser cookies --json
[/code]

JSON içindeki rol anlık görüntüleri `refs` ve küçük bir `stats` bloğu (satırlar/karakterler/referanslar/etkileşimli) içerir; böylece araçlar yük boyutu ve yoğunluğu hakkında akıl yürütebilir.

## Durum ve ortam ayarları

Bunlar "site X gibi davransın" iş akışları için yararlıdır:

  * Çerezler: `cookies`, `cookies set`, `cookies clear`
  * Depolama: `storage local|session get|set|clear`
  * Çevrimdışı: `set offline on|off`
  * Başlıklar: `set headers --headers-json '{"X-Debug":"1"}'` (eski `set headers --json '{"X-Debug":"1"}'` desteklenmeye devam eder)
  * HTTP basic auth: `set credentials user pass` (veya `--clear`)
  * Coğrafi konum: `set geo <lat> <lon> --origin "https://example.com"` (veya `--clear`)
  * Medya: `set media dark|light|no-preference|none`
  * Saat dilimi / yerel ayar: `set timezone ...`, `set locale ...`
  * Cihaz / görüntü alanı: 
    * `set device "iPhone 14"` (Playwright cihaz hazır ayarları)
    * `set viewport 1280 720`


## Güvenlik ve gizlilik

  * openclaw tarayıcı profili oturum açılmış oturumlar içerebilir; bunu hassas kabul edin.
  * `browser act kind=evaluate` / `openclaw browser evaluate` ve `wait --fn`, sayfa bağlamında rastgele JavaScript çalıştırır. Prompt injection bunu yönlendirebilir. İhtiyacınız yoksa `browser.evaluateEnabled=false` ile devre dışı bırakın.
  * Oturum açma ve bot karşıtı notlar (X/Twitter vb.) için bkz. [Tarayıcı oturumu + X/Twitter gönderisi](</tr/tools/browser-login>).
  * Gateway/Node ana makinesini özel tutun (loopback veya yalnızca tailnet).
  * Uzak CDP uç noktaları güçlüdür; bunları tünelleyin ve koruyun.


Katı mod örneği (özel/dahili hedefleri varsayılan olarak engelleyin):

json5Copy code
[code]
    {  browser: {    ssrfPolicy: {      dangerouslyAllowPrivateNetwork: false,      hostnameAllowlist: ["*.example.com", "example.com"],      allowedHostnames: ["localhost"], // optional exact allow    },  },}
[/code]

## İlgili

  * [Tarayıcı](</tr/tools/browser>) \- genel bakış, yapılandırma, profiller, güvenlik
  * [Tarayıcı oturumu](</tr/tools/browser-login>) \- sitelerde oturum açma
  * [Tarayıcı Linux sorun giderme](</tr/tools/browser-linux-troubleshooting>)
  * [Tarayıcı WSL2 sorun giderme](</tr/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo