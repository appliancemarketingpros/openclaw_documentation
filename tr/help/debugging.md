---
title: Hata ayıklama
source_url: https://docs.openclaw.ai/tr/help/debugging
scraped_at: 2026-05-25
---

Akış çıktısı için hata ayıklama yardımcıları, özellikle bir sağlayıcı akıl yürütmeyi normal metne karıştırdığında.

## Çalışma zamanı hata ayıklama geçersiz kılmaları

**Yalnızca çalışma zamanına ait** yapılandırma geçersiz kılmaları (bellek, disk değil) ayarlamak için sohbette `/debug` kullanın. `/debug` varsayılan olarak devre dışıdır; `commands.debug: true` ile etkinleştirin. Bu, `openclaw.json` dosyasını düzenlemeden belirsiz ayarları değiştirmeniz gerektiğinde kullanışlıdır.

Örnekler:

CodeCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug unset messages.responsePrefix/debug reset
[/code]

`/debug reset` tüm geçersiz kılmaları temizler ve diskteki yapılandırmaya geri döner.

## Oturum iz çıktısı

Tam ayrıntılı modu açmadan tek bir oturumda Plugin'e ait iz/hata ayıklama satırlarını görmek istediğinizde `/trace` kullanın.

Örnekler:

textCopy code
[code]
    /trace/trace on/trace off
[/code]

Active Memory hata ayıklama özetleri gibi Plugin tanılamaları için `/trace` kullanın. Normal ayrıntılı durum/araç çıktısı için `/verbose` kullanmaya devam edin ve yalnızca çalışma zamanına ait yapılandırma geçersiz kılmaları için `/debug` kullanmaya devam edin.

## Plugin yaşam döngüsü izi

Plugin yaşam döngüsü komutları yavaş hissettirdiğinde ve Plugin meta verileri, keşif, kayıt defteri, çalışma zamanı aynası, yapılandırma mutasyonu ve yenileme işi için yerleşik bir aşama dökümüne ihtiyaç duyduğunuzda `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1` kullanın. İz isteğe bağlıdır ve stderr'e yazar; bu nedenle JSON komut çıktısı ayrıştırılabilir kalır.

Örnek:

bashCopy code
[code]
    OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1 openclaw plugins install tokenjuice --force
[/code]

Örnek çıktı:

textCopy code
[code]
    [plugins:lifecycle] phase="config read" ms=6.83 status=ok command="install"[plugins:lifecycle] phase="slot selection" ms=94.31 status=ok command="install" pluginId="tokenjuice"[plugins:lifecycle] phase="registry refresh" ms=51.56 status=ok command="install" reason="source-changed"
[/code]

CPU profiler'a başvurmadan önce Plugin yaşam döngüsü incelemesi için bunu kullanın. Komut bir kaynak checkout'ından çalışıyorsa `pnpm build` sonrasında oluşturulmuş çalışma zamanını `node dist/entry.js ...` ile ölçmeyi tercih edin; `pnpm openclaw ...` kaynak çalıştırıcısı ek yükünü de ölçer.

## CLI başlangıcı ve komut profilleme

Bir komut yavaş hissettirdiğinde depoya eklenmiş başlangıç benchmark'ını kullanın:

bashCopy code
[code]
    pnpm test:startup:bench:smokepnpm tsx scripts/bench-cli-startup.ts --preset real --case status --runs 3pnpm tsx scripts/bench-cli-startup.ts --preset real --cpu-prof-dir .artifacts/cli-cpu
[/code]

Normal kaynak çalıştırıcısı üzerinden tek seferlik profilleme için `OPENCLAW_RUN_NODE_CPU_PROF_DIR` ayarlayın:

bashCopy code
[code]
    OPENCLAW_RUN_NODE_CPU_PROF_DIR=.artifacts/cli-cpu pnpm openclaw status
[/code]

Kaynak çalıştırıcısı Node CPU profil bayraklarını ekler ve komut için bir `.cpuprofile` yazar. Komut koduna geçici enstrümantasyon eklemeden önce bunu kullanın.

Eşzamanlı dosya sistemi veya modül yükleyici işi gibi görünen başlangıç takılmaları için kaynak çalıştırıcısı üzerinden Node'un sync I/O iz bayrağını ekleyin:

bashCopy code
[code]
    OPENCLAW_TRACE_SYNC_IO=1 pnpm openclaw gateway --force
[/code]

`pnpm gateway:watch`, izlenen Gateway child için bu bayrağı varsayılan olarak devre dışı bırakır. İzleme modunda Node sync I/O iz çıktısını açıkça istediğinizde `OPENCLAW_TRACE_SYNC_IO=1` ayarlayın.

## Gateway izleme modu

Hızlı yineleme için Gateway'i dosya izleyicisi altında çalıştırın:

bashCopy code
[code]
    pnpm gateway:watch
[/code]

Varsayılan olarak bu, `openclaw-gateway-watch-main` adlı bir tmux oturumu (veya `openclaw-gateway-watch-dev-19001` gibi profile/porta özel bir varyant) başlatır ya da yeniden başlatır ve etkileşimli terminallerden otomatik olarak bağlanır. Etkileşimsiz kabuklar, CI ve agent exec çağrıları ayrık kalır ve bunun yerine bağlanma yönergelerini yazdırır. Gerektiğinde elle bağlanın:

bashCopy code
[code]
    tmux attach -t openclaw-gateway-watch-main
[/code]

tmux bölmesi ham izleyiciyi çalıştırır:

bashCopy code
[code]
    node scripts/watch-node.mjs gateway --force
[/code]

tmux istenmediğinde ön plan modunu kullanın:

bashCopy code
[code]
    pnpm gateway:watch:raw# orOPENCLAW_GATEWAY_WATCH_TMUX=0 pnpm gateway:watch
[/code]

tmux yönetimini korurken otomatik bağlanmayı devre dışı bırakın:

bashCopy code
[code]
    OPENCLAW_GATEWAY_WATCH_ATTACH=0 pnpm gateway:watch
[/code]

Başlangıç/çalışma zamanı etkin noktalarında hata ayıklarken izlenen Gateway CPU süresini profilleyin:

bashCopy code
[code]
    pnpm gateway:watch --benchmark
[/code]

İzleme sarmalayıcısı Gateway'i çağırmadan önce `--benchmark` seçeneğini tüketir ve `.artifacts/gateway-watch-profiles/` altında her Gateway child çıkışı için bir V8 `.cpuprofile` yazar. Geçerli profili boşaltmak için izlenen gateway'i durdurun veya yeniden başlatın, ardından Chrome DevTools ya da Speedscope ile açın:

bashCopy code
[code]
    npx speedscope .artifacts/gateway-watch-profiles/*.cpuprofile
[/code]

Profilleri başka bir yerde istediğinizde `--benchmark-dir <path>` kullanın. Benchmark yapılan child'ın varsayılan `--force` port temizliğini atlamasını ve Gateway portu zaten kullanımdaysa hızlıca başarısız olmasını istediğinizde `--benchmark-no-force` kullanın. Benchmark modu, varsayılan olarak sync-I/O iz spam'ini bastırır. Hem CPU profilleri hem de Node sync-I/O yığın izlerini açıkça istediğinizde `--benchmark` ile `OPENCLAW_TRACE_SYNC_IO=1` ayarlayın. Benchmark modunda bu iz blokları benchmark dizini altındaki `gateway-watch-output.log` dosyasına yazılır ve terminal bölmesinden filtrelenir; normal Gateway günlükleri görünür kalır.

tmux sarmalayıcısı `OPENCLAW_PROFILE`, `OPENCLAW_CONFIG_PATH`, `OPENCLAW_STATE_DIR`, `OPENCLAW_GATEWAY_PORT` ve `OPENCLAW_SKIP_CHANNELS` gibi yaygın gizli olmayan çalışma zamanı seçicilerini bölmeye taşır. Sağlayıcı kimlik bilgilerini normal profilinize/yapılandırmanıza koyun veya tek seferlik geçici sırlar için ham ön plan modunu kullanın. İzlenen Gateway başlangıç sırasında çıkarsa izleyici bir kez `openclaw doctor --fix --non-interactive` çalıştırır ve Gateway child'ı yeniden başlatır. Yalnızca geliştirmeye özel onarım geçişi olmadan özgün başlangıç hatasını istediğinizde `OPENCLAW_GATEWAY_WATCH_AUTO_DOCTOR=0` kullanın. Yönetilen tmux bölmesi ayrıca okunabilirlik için varsayılan olarak renkli Gateway günlükleri kullanır; ANSI çıktısını devre dışı bırakmak için `pnpm gateway:watch` başlatırken `FORCE_COLOR=0` ayarlayın.

İzleyici, `src/` altındaki derlemeyle ilgili dosyalarda, uzantı kaynak dosyalarında, uzantı `package.json` ve `openclaw.plugin.json` meta verilerinde, `tsconfig.json`, `package.json` ve `tsdown.config.ts` dosyalarında yeniden başlatılır. Uzantı meta verisi değişiklikleri gateway'i `tsdown` yeniden derlemesini zorlamadan yeniden başlatır; kaynak ve yapılandırma değişiklikleri yine önce `dist` derler.

`gateway:watch` sonrasına herhangi bir gateway CLI bayrağı ekleyin; her yeniden başlatmada aktarılırlar. Aynı izleme komutunu yeniden çalıştırmak adlı tmux bölmesini yeniden oluşturur ve ham izleyici, yinelenen izleyici üst süreçlerinin birikmek yerine değiştirilmesi için tek izleyici kilidini korumaya devam eder.

## Geliştirme profili + geliştirme gateway'i (--dev)

Durumu izole etmek ve hata ayıklama için güvenli, atılabilir bir kurulum başlatmak üzere geliştirme profilini kullanın. **İki** `--dev` bayrağı vardır:

  * **Global`--dev` (profil):** durumu `~/.openclaw-dev` altında izole eder ve varsayılan gateway portunu `19001` olarak ayarlar (türetilmiş portlar onunla birlikte kayar).
  * **`gateway --dev`: eksik olduğunda Gateway'e varsayılan bir yapılandırma + çalışma alanını otomatik oluşturmasını söyler** (ve [BOOTSTRAP.md](<http://BOOTSTRAP.md>) dosyasını atlar).


Önerilen akış (geliştirme profili + geliştirme bootstrap'i):

bashCopy code
[code]
    pnpm gateway:devOPENCLAW_PROFILE=dev openclaw tui
[/code]

Henüz global kurulumunuz yoksa CLI'yi `pnpm openclaw ...` üzerinden çalıştırın.

Bunun yaptıkları:

  1. **Profil yalıtımı** (global `--dev`)

     * `OPENCLAW_PROFILE=dev`
     * `OPENCLAW_STATE_DIR=~/.openclaw-dev`
     * `OPENCLAW_CONFIG_PATH=~/.openclaw-dev/openclaw.json`
     * `OPENCLAW_GATEWAY_PORT=19001` (tarayıcı/canvas buna göre kayar)
  2. **Geliştirme bootstrap'i** (`gateway --dev`)

     * Eksikse minimal bir yapılandırma yazar (`gateway.mode=local`, bind loopback).
     * `agent.workspace` değerini geliştirme çalışma alanına ayarlar.
     * `agent.skipBootstrap=true` değerini ayarlar ([BOOTSTRAP.md](<http://BOOTSTRAP.md>) yok).
     * Eksikse çalışma alanı dosyalarını tohumlar: `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`.
     * Varsayılan kimlik: **C3-PO** (protokol droidi).
     * Geliştirme modunda kanal sağlayıcılarını atlar (`OPENCLAW_SKIP_CHANNELS=1`).


Sıfırlama akışı (taze başlangıç):

bashCopy code
[code]
    pnpm gateway:dev:reset
[/code]

`--reset`, yapılandırmayı, kimlik bilgilerini, oturumları ve geliştirme çalışma alanını (`rm` değil, `trash` kullanarak) siler, ardından varsayılan geliştirme kurulumunu yeniden oluşturur.

## Ham akış günlükleme (OpenClaw)

OpenClaw, herhangi bir filtreleme/biçimlendirme öncesinde **ham asistan akışını** günlüğe yazabilir. Bu, akıl yürütmenin düz metin deltaları olarak mı (yoksa ayrı düşünme blokları olarak mı) geldiğini görmenin en iyi yoludur.

CLI üzerinden etkinleştirin:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream
[/code]

İsteğe bağlı yol geçersiz kılması:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream --raw-stream-path ~/.openclaw/logs/raw-stream.jsonl
[/code]

Eşdeğer env var'lar:

bashCopy code
[code]
    OPENCLAW_RAW_STREAM=1OPENCLAW_RAW_STREAM_PATH=~/.openclaw/logs/raw-stream.jsonl
[/code]

Varsayılan dosya:

`~/.openclaw/logs/raw-stream.jsonl`

## Ham parça günlükleme (pi-mono)

**Ham OpenAI uyumlu parçaları** bloklara ayrıştırılmadan önce yakalamak için pi-mono ayrı bir günlükleyici sunar:

bashCopy code
[code]
    PI_RAW_STREAM=1
[/code]

İsteğe bağlı yol:

bashCopy code
[code]
    PI_RAW_STREAM_PATH=~/.pi-mono/logs/raw-openai-completions.jsonl
[/code]

Varsayılan dosya:

`~/.pi-mono/logs/raw-openai-completions.jsonl`

> Not: Bu yalnızca pi-mono'nun `openai-completions` sağlayıcısını kullanan süreçler tarafından yayılır.

## Güvenlik notları

  * Ham akış günlükleri tam istemleri, araç çıktısını ve kullanıcı verilerini içerebilir.
  * Günlükleri yerel tutun ve hata ayıklamadan sonra silin.
  * Günlükleri paylaşırsanız önce sırları ve PII'yi temizleyin.


## VSCode'da hata ayıklama

Derleme sürecinin bir parçası olarak oluşturulan dosyaların çoğu karma adlarla sonuçlandığı için VSCode tabanlı IDE'lerde hata ayıklamayı etkinleştirmek üzere kaynak haritaları gerekir. Dahil edilen `launch.json` yapılandırmaları Gateway hizmetini hedefler, ancak başka amaçlar için hızla uyarlanabilir:

  1. **Gateway'i Yeniden Derle ve Hata Ayıkla** \- Yeni bir derleme oluşturduktan sonra Gateway hizmetinde hata ayıklar
  2. **Gateway'de Hata Ayıkla** \- Önceden var olan bir derlemenin Gateway hizmetinde hata ayıklar


### Kurulum

Varsayılan **Gateway'i Yeniden Derle ve Hata Ayıkla** yapılandırması kullanıma hazırdır; `/dist` klasörünü otomatik olarak siler ve hata ayıklama etkin olarak projeyi yeniden derler:

  1. Activity Bar'dan **Çalıştır ve Hata Ayıkla** panelini açın veya `Ctrl`+`Shift`+`D` tuşlarına basın
  2. IDE'de yapılandırma açılır menüsünde **Gateway'i Yeniden Derle ve Hata Ayıkla** seçili olduğundan emin olun ve ardından **Hata Ayıklamayı Başlat** düğmesine basın


Alternatif olarak - derleme ve hata ayıklama süreçlerini elle yönetmeyi tercih ediyorsanız:

  1. Bir terminal açın ve kaynak haritalarını etkinleştirin: 
     * **Linux/macOS** : `export OUTPUT_SOURCE_MAPS=1`
     * **Windows (PowerShell)** : `$env:OUTPUT_SOURCE_MAPS="1"`
     * **Windows (CMD)** : `set OUTPUT_SOURCE_MAPS=1`
  2. Aynı terminalde projeyi yeniden derleyin: `pnpm clean:dist && pnpm build`
  3. IDE'de **Çalıştır ve Hata Ayıkla** yapılandırma açılır menüsünde **Gateway'de Hata Ayıkla** seçeneğini seçin ve ardından **Hata Ayıklamayı Başlat** düğmesine basın


Artık TypeScript kaynak dosyalarınızda (`src/` dizini) kesme noktaları ayarlayabilirsiniz ve hata ayıklayıcı, kaynak haritaları aracılığıyla kesme noktalarını derlenmiş JavaScript'e doğru şekilde eşleyecektir. Değişkenleri inceleyebilecek, kodda adım adım ilerleyebilecek ve çağrı yığınlarını beklendiği gibi inceleyebileceksiniz.

### Notlar

  * **"Gateway'i Yeniden Derle ve Hata Ayıkla"** seçeneğini kullanıyorsanız - hata ayıklayıcı her başlatıldığında `/dist` klasörünü tamamen siler ve Gateway'i başlatmadan önce kaynak haritaları etkinleştirilmiş tam bir `pnpm build` çalıştırır
  * **"Gateway'de Hata Ayıkla"** seçeneğini kullanıyorsanız - hata ayıklama oturumları `/dist` klasörünü etkilemeden herhangi bir zamanda başlatılıp durdurulabilir, ancak hem hata ayıklamayı etkinleştirmek hem de derleme döngüsünü yönetmek için ayrı bir terminal süreci kullanmanız gerekir
  * Projenin diğer bölümlerinde hata ayıklamak için `args` için `launch.json` ayarlarını değiştirin
  * Başka görevler için oluşturulmuş OpenClaw CLI'yi kullanmanız gerekiyorsa (örn. hata ayıklama oturumunuz yeni bir auth token oluşturuyorsa `dashboard --no-open`), başka bir terminalde `node ./openclaw.mjs` olarak çalıştırabilir veya `alias openclaw-build="node $(pwd)/openclaw.mjs"` gibi bir shell alias oluşturabilirsiniz


## İlgili

  * [Sorun giderme](</tr/help/troubleshooting>)
  * [SSS](</tr/help/faq>)


Was this useful?YesNo