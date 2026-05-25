---
title: Pluginler
source_url: https://docs.openclaw.ai/tr/cli/plugins
scraped_at: 2026-05-25
---

Gateway Pluginlarını, hook paketlerini ve uyumlu bundle’ları yönetin.

[**Plugin sistemi** Plugin kurma, etkinleştirme ve sorun giderme için son kullanıcı kılavuzu. ](</tr/tools/plugin>) [**Pluginları yönet** Kurma, listeleme, güncelleme, kaldırma ve yayımlama için hızlı örnekler. ](</tr/plugins/manage-plugins>) [**Plugin bundle’ları** Bundle uyumluluk modeli. ](</tr/plugins/bundles>) [**Plugin manifesti** Manifest alanları ve yapılandırma şeması. ](</tr/plugins/manifest>) [**Güvenlik** Plugin kurulumları için güvenlik sıkılaştırması. ](</tr/gateway/security>)

## Komutlar

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

Yavaş kurulum, inceleme, kaldırma veya kayıt yenileme araştırması için komutu `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1` ile çalıştırın. İz, aşama sürelerini stderr’e yazar ve JSON çıktısını ayrıştırılabilir tutar. Bkz. [Hata ayıklama](</tr/help/debugging#plugin-lifecycle-trace>).

### Kurulum

bashCopy code
[code]
    openclaw plugins search "calendar"                   # search ClawHub pluginsopenclaw plugins install <package>                      # npm by defaultopenclaw plugins install clawhub:<package>              # ClawHub onlyopenclaw plugins install npm:<package>                  # npm onlyopenclaw plugins install npm-pack:<path.tgz>            # local npm pack through npm install semanticsopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # overwrite existing installopenclaw plugins install <package> --pin                # pin versionopenclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # local pathopenclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

Kurulum zamanı kurulumlarını test eden bakımcılar, korumalı ortam değişkenleriyle otomatik Plugin kurulum kaynaklarını geçersiz kılabilir. Bkz. [Plugin kurulum geçersiz kılmaları](</tr/plugins/install-overrides>).

`plugins search`, kurulabilir Plugin paketleri için ClawHub’ı sorgular ve kuruluma hazır paket adlarını yazdırır. Skills değil, code-plugin ve bundle-plugin paketlerini arar. ClawHub Skills için `openclaw skills search` kullanın.

Yapılandırma include’ları ve geçersiz yapılandırma onarımı

`plugins` bölümünüz tek dosyalı bir `$include` ile destekleniyorsa, `plugins install/update/enable/disable/uninstall` bu dahil edilen dosyaya yazar ve `openclaw.json` dosyasına dokunmaz. Kök include’lar, include dizileri ve kardeş geçersiz kılmaları olan include’lar düzleştirmek yerine kapalı şekilde başarısız olur. Desteklenen biçimler için [Yapılandırma include’ları](</tr/gateway/configuration>) bölümüne bakın.

Kurulum sırasında yapılandırma geçersizse, `plugins install` normalde kapalı şekilde başarısız olur ve önce `openclaw doctor --fix` çalıştırmanızı söyler. Gateway başlatma ve sıcak yeniden yükleme sırasında, geçersiz Plugin yapılandırması diğer geçersiz yapılandırmalar gibi kapalı şekilde başarısız olur; `openclaw doctor --fix` geçersiz Plugin girdisini karantinaya alabilir. Belgelenen tek kurulum zamanı istisnası, açıkça `openclaw.install.allowInvalidConfigRecovery` için katılım belirten Pluginlar için dar kapsamlı bir birlikte gelen Plugin kurtarma yoludur.

\--force ve yeniden kurulum ile güncelleme

`--force`, mevcut kurulum hedefini yeniden kullanır ve zaten kurulmuş bir Pluginı veya hook paketini yerinde üzerine yazar. Aynı kimliği yeni bir yerel yoldan, arşivden, ClawHub paketinden veya npm yapıtından bilinçli olarak yeniden kurarken kullanın. Zaten izlenen bir npm Pluginının rutin yükseltmeleri için `openclaw plugins update <id-or-npm-spec>` tercih edin.

Zaten kurulmuş bir Plugin kimliği için `plugins install` çalıştırırsanız OpenClaw durur ve normal bir yükseltme için sizi `plugins update <id-or-npm-spec>` komutuna veya mevcut kurulumu farklı bir kaynaktan gerçekten üzerine yazmak istediğinizde `plugins install <package> --force` komutuna yönlendirir.

\--pin kapsamı

`--pin` yalnızca npm kurulumlarına uygulanır. `git:` kurulumlarıyla desteklenmez; sabitlenmiş bir kaynak istediğinizde `git:github.com/acme/plugin@v1.2.3` gibi açık bir git ref kullanın. `--marketplace` ile desteklenmez, çünkü marketplace kurulumları npm spec yerine marketplace kaynak meta verilerini kalıcı hale getirir.

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install`, yerleşik tehlikeli kod tarayıcısındaki hatalı pozitifler için acil durum seçeneğidir. Yerleşik tarayıcı `critical` bulgular bildirdiğinde bile kurulumun devam etmesine izin verir, ancak Plugin `before_install` hook politika engellerini **atlatmaz** ve tarama başarısızlıklarını **atlatmaz**.

Bu CLI bayrağı Plugin kurulum/güncelleme akışlarına uygulanır. Gateway destekli skill bağımlılık kurulumları eşleşen `dangerouslyForceUnsafeInstall` istek geçersiz kılmasını kullanırken, `openclaw skills install` ayrı bir ClawHub skill indirme/kurma akışı olarak kalır.

ClawHub’da yayımladığınız bir Plugin bir kayıt taraması tarafından engellenirse [ClawHub](</tr/clawhub/security>) bölümündeki yayımlayıcı adımlarını kullanın.

Hook paketleri ve npm spec’leri

`plugins install`, `package.json` içinde `openclaw.hooks` sunan hook paketleri için de kurulum yüzeyidir. Paket kurulumu için değil, filtrelenmiş hook görünürlüğü ve hook başına etkinleştirme için `openclaw hooks` kullanın.

Npm spec’leri **yalnızca kayıt** içindir (paket adı + isteğe bağlı **tam sürüm** veya **dist-tag**). Git/URL/dosya spec’leri ve semver aralıkları reddedilir. Kabuğunuzda global npm kurulum ayarları olsa bile, bağımlılık kurulumları güvenlik için `--ignore-scripts` ile proje yerelinde çalışır. Yönetilen Plugin npm kökleri OpenClaw’ın paket düzeyi npm `overrides` değerlerini devralır, böylece ana makine güvenlik sabitlemeleri hoist edilmiş Plugin bağımlılıklarına da uygulanır.

Npm çözümlemesini açık hale getirmek istediğinizde `npm:<package>` kullanın. Çıplak paket spec’leri de başlatma geçişi sırasında doğrudan npm’den kurulur.

Çıplak spec’ler ve `@latest` kararlı hatta kalır. `2026.5.3-1` gibi OpenClaw tarih damgalı düzeltme sürümleri bu denetim için kararlı sürümlerdir. Npm bunlardan herhangi birini prerelease’e çözümlerse OpenClaw durur ve `@beta`/`@rc` gibi bir prerelease etiketi veya `@1.2.3-beta.4` gibi tam bir prerelease sürümüyle açıkça katılım yapmanızı ister.

Çıplak bir kurulum spec’i resmi bir Plugin kimliğiyle eşleşirse (örneğin `diffs`), OpenClaw katalog girdisini doğrudan kurar. Aynı ada sahip bir npm paketi kurmak için açık kapsamlı bir spec kullanın (örneğin `@scope/diffs`).

Git depoları

Doğrudan bir git deposundan kurmak için `git:<repo>` kullanın. Desteklenen biçimler arasında `git:github.com/owner/repo`, `git:owner/repo`, tam `https://`, `ssh://`, `git://`, `file://` ve `git@host:owner/repo.git` klon URL’leri bulunur. Kurulumdan önce bir dalı, etiketi veya commit’i checkout yapmak için `@<ref>` veya `#<ref>` ekleyin.

Git kurulumları geçici bir dizine klonlar, varsa istenen ref’i checkout eder, ardından normal Plugin dizin kurucusunu kullanır. Bu, manifest doğrulamasının, tehlikeli kod taramasının, paket yöneticisi kurulum işinin ve kurulum kayıtlarının npm kurulumları gibi davrandığı anlamına gelir. Kaydedilen git kurulumları, kaynak URL/ref bilgisiyle birlikte çözümlenen commit’i içerir; böylece `openclaw plugins update` kaynağı daha sonra yeniden çözümleyebilir.

Git’ten kurduktan sonra gateway yöntemleri ve CLI komutları gibi çalışma zamanı kayıtlarını doğrulamak için `openclaw plugins inspect <id> --runtime --json` kullanın. Plugin `api.registerCli` ile bir CLI kökü kaydettiyse, bu komutu doğrudan OpenClaw kök CLI üzerinden yürütün; örneğin `openclaw demo-plugin ping`.

Arşivler

Desteklenen arşivler: `.zip`, `.tgz`, `.tar.gz`, `.tar`. Yerel OpenClaw Plugin arşivleri, çıkarılan Plugin kökünde geçerli bir `openclaw.plugin.json` içermelidir; yalnızca `package.json` içeren arşivler OpenClaw kurulum kayıtlarını yazmadan önce reddedilir.

Dosya bir npm-pack tarball’ı olduğunda ve kayıt kurulumlarının kullandığı aynı yönetilen npm kökü kurulum yolunu test etmek istediğinizde `npm-pack:<path.tgz>` kullanın; buna `package-lock.json` doğrulaması, hoist edilmiş bağımlılık taraması ve npm kurulum kayıtları dahildir. Düz arşiv yolları hâlâ yerel arşivler olarak Plugin extensions kökü altında kurulur.

Claude marketplace kurulumları da desteklenir.

ClawHub kurulumları açık bir `clawhub:<package>` konumlayıcısı kullanır:

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

Çıplak npm uyumlu Plugin spec’leri başlatma geçişi sırasında varsayılan olarak npm’den kurulur:

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

Yalnızca npm çözümlemesini açık hale getirmek için `npm:` kullanın:

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw, kurulumdan önce ilan edilen Plugin API / minimum Gateway uyumluluğunu denetler. Seçilen ClawHub sürümü bir ClawPack yapıtı yayımladığında OpenClaw, sürümlendirilmiş npm-pack `.tgz` dosyasını indirir, ClawHub özet üst bilgisini ve yapıt özetini doğrular, ardından bunu normal arşiv yolu üzerinden kurar. ClawPack meta verisi olmayan eski ClawHub sürümleri hâlâ eski paket arşivi doğrulama yolu üzerinden kurulur. Kaydedilen kurulumlar, sonraki güncellemeler için ClawHub kaynak meta verilerini, yapıt türünü, npm bütünlüğünü, npm shasum değerini, tarball adını ve ClawPack özet bilgilerini saklar. Sürümlendirilmemiş ClawHub kurulumları, `openclaw plugins update` komutunun daha yeni ClawHub sürümlerini izleyebilmesi için sürümlendirilmemiş bir kayıtlı spec tutar; `clawhub:pkg@1.2.3` ve `clawhub:pkg@beta` gibi açık sürüm veya etiket seçicileri o seçiciye sabitlenmiş kalır.

#### Marketplace kısaltması

Marketplace adı Claude'un `~/.claude/plugins/known_marketplaces.json` konumundaki yerel kayıt defteri önbelleğinde varsa `plugin@marketplace` kısaltmasını kullanın:

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

Marketplace kaynağını açıkça geçirmek istediğinizde `--marketplace` kullanın:

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### Marketplace kaynakları

  * `~/.claude/plugins/known_marketplaces.json` içinden bir Claude bilinen-marketplace adı
  * yerel bir marketplace kökü veya `marketplace.json` yolu
  * `owner/repo` gibi bir GitHub depo kısaltması
  * `https://github.com/owner/repo` gibi bir GitHub depo URL'si
  * bir git URL'si


### Uzak marketplace kuralları

GitHub veya git üzerinden yüklenen uzak marketplace'ler için Plugin girdileri klonlanan marketplace deposunun içinde kalmalıdır. OpenClaw, bu depodan göreli yol kaynaklarını kabul eder ve uzak manifestlerden HTTP(S), mutlak yol, git, GitHub ve diğer yol olmayan Plugin kaynaklarını reddeder.

Yerel yollar ve arşivler için OpenClaw şunları otomatik algılar:

  * yerel OpenClaw Plugin'leri (`openclaw.plugin.json`)
  * Codex uyumlu paketler (`.codex-plugin/plugin.json`)
  * Claude uyumlu paketler (`.claude-plugin/plugin.json` veya varsayılan Claude bileşen düzeni)
  * Cursor uyumlu paketler (`.cursor-plugin/plugin.json`)


### Listeleme

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

Yalnızca etkin Plugin'leri göster.

Tablo görünümünden, kaynak/köken/sürüm/etkinleştirme meta verileriyle Plugin başına ayrıntı satırlarına geç.

Makine tarafından okunabilir envanter ile kayıt defteri tanılamaları ve paket bağımlılığı kurulum durumu.

`plugins search`, uzak ClawHub katalog aramasıdır. Yerel durumu incelemez, yapılandırmayı değiştirmez, paket kurmaz veya Plugin çalışma zamanı kodunu yüklemez. Arama sonuçları ClawHub paket adını, ailesini, kanalını, sürümünü, özetini ve `openclaw plugins install clawhub:<package>` gibi bir kurulum ipucunu içerir.

Paketlenmiş Docker imajı içinde paketli Plugin çalışması için, Plugin kaynak dizinini `/app/extensions/synology-chat` gibi eşleşen paketli kaynak yolunun üzerine bind-mount edin. OpenClaw bu bağlanmış kaynak katmanını `/app/dist/extensions/synology-chat` öncesinde keşfeder; düz kopyalanmış bir kaynak dizini etkisiz kalır, böylece normal paketli kurulumlar derlenmiş dist kullanmaya devam eder.

Çalışma zamanı hook hata ayıklaması için:

  * `openclaw plugins inspect <id> --runtime --json`, modül yüklemeli bir inceleme geçişinden kayıtlı hook'ları ve tanılamaları gösterir. Çalışma zamanı incelemesi hiçbir zaman bağımlılık kurmaz; eski bağımlılık durumunu temizlemek veya yapılandırmada başvurulan eksik indirilebilir Plugin'leri kurtarmak için `openclaw doctor --fix` kullanın.
  * `openclaw gateway status --deep --require-rpc`, erişilebilir Gateway'i, hizmet/süreç ipuçlarını, yapılandırma yolunu ve RPC sağlığını doğrular.
  * Paketlenmemiş konuşma hook'ları (`llm_input`, `llm_output`, `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `before_agent_finalize`, `agent_end`) `plugins.entries.<id>.hooks.allowConversationAccess=true` gerektirir.


Yerel bir dizini kopyalamaktan kaçınmak için `--link` kullanın (`plugins.load.paths` içine ekler):

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### Plugin dizini

Plugin kurulum meta verisi kullanıcı yapılandırması değil, makine tarafından yönetilen durumdur. Kurulumlar ve güncellemeler bunu etkin OpenClaw durum dizini altında `plugins/installs.json` dosyasına yazar. Üst düzey `installRecords` haritası, bozuk veya eksik Plugin manifestleri için kayıtlar dahil olmak üzere kurulum meta verisinin kalıcı kaynağıdır. `plugins` dizisi, manifestten türetilen soğuk kayıt defteri önbelleğidir. Dosya bir düzenlemeyin uyarısı içerir ve `openclaw plugins update`, kaldırma, tanılamalar ve soğuk Plugin kayıt defteri tarafından kullanılır.

OpenClaw yapılandırmada gönderilmiş eski `plugins.installs` kayıtları gördüğünde, çalışma zamanı okumaları bunları `openclaw.json` dosyasını yeniden yazmadan uyumluluk girdisi olarak ele alır. Açık Plugin yazmaları ve `openclaw doctor --fix`, yapılandırma yazmalarına izin veriliyorsa bu kayıtları Plugin dizinine taşır ve yapılandırma anahtarını kaldırır; yazmalardan biri başarısız olursa kurulum meta verisinin kaybolmaması için yapılandırma kayıtları tutulur.

### Kaldırma

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall`, Plugin kayıtlarını `plugins.entries` içinden, kalıcı Plugin dizininden, Plugin izin/ret listesi girdilerinden ve uygulanabiliyorsa bağlantılı `plugins.load.paths` girdilerinden kaldırır. `--keep-files` ayarlanmadığı sürece kaldırma işlemi, OpenClaw'un Plugin uzantıları kökü içindeyse izlenen yönetilen kurulum dizinini de kaldırır. Active Memory Plugin'leri için bellek yuvası `memory-core` değerine sıfırlanır.

### Güncelleme

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

Güncellemeler, yönetilen Plugin dizinindeki izlenen Plugin kurulumlarına ve `hooks.internal.installs` içindeki izlenen hook-pack kurulumlarına uygulanır.

Plugin kimliği ile npm spec çözümleme

Bir Plugin kimliği geçirdiğinizde OpenClaw, o Plugin için kaydedilmiş kurulum spec'ini yeniden kullanır. Bu, daha önce saklanan `@beta` gibi dist-tag'lerin ve tam sabitlenmiş sürümlerin sonraki `update <id>` çalıştırmalarında kullanılmaya devam ettiği anlamına gelir.

npm kurulumları için dist-tag veya tam sürüm içeren açık bir npm paket spec'i de geçirebilirsiniz. OpenClaw bu paket adını izlenen Plugin kaydına geri çözümler, kurulu Plugin'i günceller ve gelecekte kimlik tabanlı güncellemeler için yeni npm spec'ini kaydeder.

npm paket adını sürüm veya etiket olmadan geçirmek de izlenen Plugin kaydına geri çözümlenir. Bir Plugin tam bir sürüme sabitlenmişse ve onu kayıt defterinin varsayılan yayın hattına geri taşımak istiyorsanız bunu kullanın.

Beta kanalı güncellemeleri

`openclaw plugins update`, yeni bir spec geçirmediğiniz sürece izlenen Plugin spec'ini yeniden kullanır. `openclaw update` ayrıca etkin OpenClaw güncelleme kanalını bilir: beta kanalında, varsayılan hat npm ve ClawHub Plugin kayıtları önce `@beta` dener, ardından Plugin beta yayını yoksa kaydedilmiş varsayılan/en son spec'e geri döner. Bu geri dönüş bir uyarı olarak bildirilir ve çekirdek güncellemeyi başarısız yapmaz. Tam sürümler ve açık etiketler o seçiciye sabitlenmiş kalır.

Sürüm denetimleri ve bütünlük sapması

Canlı bir npm güncellemesinden önce OpenClaw, kurulu paket sürümünü npm kayıt defteri meta verilerine karşı denetler. Kurulu sürüm ve kaydedilmiş yapıt kimliği zaten çözümlenen hedefle eşleşiyorsa güncelleme indirme, yeniden kurma veya `openclaw.json` yeniden yazma olmadan atlanır.

Saklanan bir bütünlük karması varsa ve getirilen yapıt karması değişirse OpenClaw bunu npm yapıt sapması olarak ele alır. Etkileşimli `openclaw plugins update` komutu beklenen ve gerçek karmaları yazdırır ve devam etmeden önce onay ister. Etkileşimsiz güncelleme yardımcıları, çağıran açık bir devam politikası sağlamadıkça kapalı şekilde başarısız olur.

Güncellemede --dangerously-force-unsafe-install

`--dangerously-force-unsafe-install`, Plugin güncellemeleri sırasında yerleşik tehlikeli kod taraması yanlış pozitifleri için acil durum geçersiz kılması olarak `plugins update` üzerinde de kullanılabilir. Yine de Plugin `before_install` politika engellerini veya tarama hatası engellemesini atlamaz ve hook-pack güncellemelerine değil, yalnızca Plugin güncellemelerine uygulanır.

### İnceleme

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspect varsayılan olarak Plugin çalışma zamanını içe aktarmadan kimliği, yükleme durumunu, kaynağı, manifest yeteneklerini, politika bayraklarını, tanılamaları, kurulum meta verilerini, paket yeteneklerini ve algılanan MCP veya LSP sunucusu desteğini gösterir. Plugin modülünü yükleyip kayıtlı hook'ları, araçları, komutları, hizmetleri, Gateway yöntemlerini ve HTTP rotalarını eklemek için `--runtime` ekleyin. Çalışma zamanı incelemesi eksik Plugin bağımlılıklarını doğrudan bildirir; kurulumlar ve onarımlar `openclaw plugins install`, `openclaw plugins update` ve `openclaw doctor --fix` içinde kalır.

Plugin sahipli CLI komutları genellikle kök `openclaw` komut grupları olarak kurulur, ancak Plugin'ler `openclaw nodes` gibi bir çekirdek üst öğenin altında iç içe komutlar da kaydedebilir. `inspect --runtime`, `cliCommands` altında bir komut gösterdikten sonra bunu listelenen yolda çalıştırın; örneğin `demo-git` kaydeden bir Plugin `openclaw demo-git ping` ile doğrulanabilir.

Her Plugin, çalışma zamanında gerçekten kaydettiği şeye göre sınıflandırılır:

  * **düz-yetenek** — tek bir yetenek türü (ör. yalnızca sağlayıcı içeren bir plugin)
  * **hibrit-yetenek** — birden çok yetenek türü (ör. metin + konuşma + görseller)
  * **yalnızca-hook** — yalnızca hook'lar, yetenek veya yüzey yok
  * **yeteneksiz** — araçlar/komutlar/hizmetler var ancak yetenek yok


Yetenek modeli hakkında daha fazlası için [Plugin biçimleri](</tr/plugins/architecture#plugin-shapes>) bölümüne bakın.

### Doktor

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor`, plugin yükleme hatalarını, manifest/keşif tanılarını ve uyumluluk bildirimlerini raporlar. Her şey temiz olduğunda `No plugin issues detected.` yazdırır.

Yapılandırılmış bir plugin diskte mevcutsa ancak yükleyicinin yol güvenliği denetimleri tarafından engelleniyorsa, yapılandırma doğrulaması plugin girdisini korur ve bunu `present but blocked` olarak raporlar. `plugins.entries.<id>` veya `plugins.allow` yapılandırmasını kaldırmak yerine, yol sahipliği ya da herkes tarafından yazılabilir izinler gibi önceki engellenmiş-plugin tanısını düzeltin.

Eksik `register`/`activate` dışa aktarımları gibi modül biçimi hataları için, tanı çıktısına kompakt bir dışa aktarım biçimi özeti eklemek üzere `OPENCLAW_PLUGIN_LOAD_DEBUG=1` ile yeniden çalıştırın.

### Kayıt

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

Yerel plugin kaydı, kurulu plugin kimliği, etkinleştirme durumu, kaynak meta verileri ve katkı sahipliği için OpenClaw'ın kalıcı soğuk okuma modelidir. Normal başlatma, sağlayıcı sahip araması, kanal kurulum sınıflandırması ve plugin envanteri, plugin runtime modüllerini içe aktarmadan bunu okuyabilir.

Kalıcı kaydın mevcut, güncel veya eski olup olmadığını incelemek için `plugins registry` kullanın. Kalıcı plugin indeksi, yapılandırma ilkesi ve manifest/paket meta verilerinden yeniden oluşturmak için `--refresh` kullanın. Bu bir onarım yoludur, runtime etkinleştirme yolu değildir.

`openclaw doctor --fix`, kayıtla ilişkili yönetilen npm sapmalarını da onarır: yönetilen plugin npm kökü altında öksüz veya kurtarılmış bir `@openclaw/*` paketi paketlenmiş bir plugin'i gölgelerse, doctor bu eski paketi kaldırır ve başlatmanın paketlenmiş manifeste göre doğrulanması için kaydı yeniden oluşturur. Doctor ayrıca ana makine `openclaw` paketini, `peerDependencies.openclaw` bildiren yönetilen npm plugin'lerine yeniden bağlar; böylece `openclaw/plugin-sdk/*` gibi paket yerelindeki runtime içe aktarımları güncellemelerden veya npm onarımlarından sonra çözümlenir.

### Pazar Yeri

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

Pazar yeri listesi yerel bir pazar yeri yolunu, bir `marketplace.json` yolunu, `owner/repo` gibi bir GitHub kısaltmasını, bir GitHub repo URL'sini veya bir git URL'sini kabul eder. `--json`, çözümlenen kaynak etiketinin yanı sıra ayrıştırılmış pazar yeri manifestini ve plugin girdilerini yazdırır.

## İlgili

  * [Plugin oluşturma](</tr/plugins/building-plugins>)
  * [CLI başvurusu](</tr/cli>)
  * [ClawHub](</tr/clawhub>)


Was this useful?YesNo