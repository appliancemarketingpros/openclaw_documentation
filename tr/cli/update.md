---
title: Güncelle
source_url: https://docs.openclaw.ai/tr/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

OpenClaw'u güvenli şekilde güncelleyin ve stable/beta/dev kanalları arasında geçiş yapın.

**npm/pnpm/bun** ile yüklediyseniz (global kurulum, git meta verisi yok), güncellemeler [Güncelleme](</tr/install/updating>) bölümündeki paket yöneticisi akışıyla yapılır.

## Kullanım

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Seçenekler

  * `--no-restart`: başarılı bir güncellemeden sonra Gateway hizmetini yeniden başlatmayı atlar. Gateway'i yeniden başlatan paket yöneticisi güncellemeleri, komut başarılı olmadan önce yeniden başlatılan hizmetin beklenen güncellenmiş sürümü bildirdiğini doğrular.
  * `--channel <stable|beta|dev>`: güncelleme kanalını ayarlar (git + npm; yapılandırmada kalıcı olur).
  * `--tag <dist-tag|version|spec>`: yalnızca bu güncelleme için paket hedefini geçersiz kılar. Paket kurulumlarında `main`, `github:openclaw/openclaw#main` ile eşlenir.
  * `--dry-run`: yapılandırma yazmadan, kurulum yapmadan, plugin'leri eşitlemeden veya yeniden başlatmadan planlanan güncelleme eylemlerini (kanal/tag/hedef/yeniden başlatma akışı) önizler.
  * `--json`: çekirdek güncelleme başarılı olduktan sonra bozuk veya yüklenemeyen yönetilen plugin'lerin onarım gerektirdiği durumlarda `postUpdate.plugins.warnings`, bir plugin'in beta sürümü olmadığında beta kanalı plugin yedekleme ayrıntıları ve güncelleme sonrası plugin eşitlemesi sırasında npm plugin yapıtı sapması algılandığında `postUpdate.plugins.integrityDrifts` dahil olmak üzere makine tarafından okunabilir `UpdateRunResult` JSON çıktısı yazdırır.
  * `--timeout <seconds>`: adım başına zaman aşımı (varsayılan 1800 s).
  * `--yes`: onay istemlerini atlar (örneğin sürüm düşürme onayı).


`openclaw update` komutunda `--verbose` bayrağı yoktur. Planlanan kanal/tag/kurulum/yeniden başlatma eylemlerini önizlemek için `--dry-run`, makine tarafından okunabilir sonuçlar için `--json` ve yalnızca kanal ile kullanılabilirlik ayrıntılarına ihtiyacınız olduğunda `openclaw update status --json` kullanın. Bir güncelleme sırasında Gateway günlüklerinde hata ayıklıyorsanız, konsol ayrıntı düzeyi ile dosya günlük düzeyi ayrıdır: Gateway `--verbose` terminal/WebSocket çıktısını etkilerken dosya günlükleri yapılandırmada `logging.level: "debug"` veya `"trace"` gerektirir. Bkz. [Gateway günlükleri](</tr/gateway/logging>).

## `update status`

Etkin güncelleme kanalını + git tag/branch/SHA bilgisini (kaynak checkout'ları için) ve güncelleme kullanılabilirliğini gösterir.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Seçenekler:

  * `--json`: makine tarafından okunabilir durum JSON'u yazdırır.
  * `--timeout <seconds>`: kontroller için zaman aşımı (varsayılan 3 s).


## `update wizard`

Bir güncelleme kanalı seçmek ve güncellemeden sonra Gateway'in yeniden başlatılıp başlatılmayacağını onaylamak için etkileşimli akış (varsayılan yeniden başlatmaktır). Git checkout olmadan `dev` seçerseniz, bir tane oluşturmayı teklif eder.

Seçenekler:

  * `--timeout <seconds>`: her güncelleme adımı için zaman aşımı (varsayılan `1800`)


## Ne yapar

Kanalları açıkça değiştirdiğinizde (`--channel ...`), OpenClaw kurulum yöntemini de uyumlu tutar:

  * `dev` → bir git checkout olduğundan emin olur (varsayılan: `~/openclaw`, `OPENCLAW_GIT_DIR` ile geçersiz kılınabilir), bunu günceller ve global CLI'yi bu checkout'tan kurar.
  * `stable` → `latest` kullanarak npm'den kurar.
  * `beta` → npm dist-tag `beta` değerini tercih eder, ancak beta eksikse veya mevcut stable sürümden eskiyse `latest` değerine geri döner.


Gateway çekirdek otomatik güncelleyicisi (yapılandırma ile etkinleştirildiğinde), CLI güncelleme yolunu canlı Gateway istek işleyicisinin dışında başlatır. Kontrol düzlemi `update.run` paket yöneticisi güncellemeleri, paket değişiminden sonra ertelenmeyen ve bekleme süresi olmayan bir güncelleme yeniden başlatmasını zorunlu kılar; çünkü eski Gateway süreci hâlâ yeni paket tarafından kaldırılmış dosyalara işaret eden bellek içi parçalara sahip olabilir.

Paket yöneticisi kurulumlarında `openclaw update`, paket yöneticisini çağırmadan önce hedef paket sürümünü çözümler. npm global kurulumları aşamalı kurulum kullanır: OpenClaw yeni paketi geçici bir npm prefix içine kurar, oradaki paketlenmiş `dist` envanterini doğrular, ardından bu temiz paket ağacını gerçek global prefix içine taşır. Doğrulama başarısız olursa güncelleme sonrası doctor, plugin eşitlemesi ve yeniden başlatma işleri şüpheli ağaçtan çalıştırılmaz. Kurulu sürüm zaten hedefle eşleşse bile komut global paket kurulumunu yeniler, ardından plugin eşitlemesini, çekirdek komut tamamlama yenilemesini ve yeniden başlatma işlerini çalıştırır. Bu, paketlenmiş yan bileşenleri ve kanalın sahip olduğu plugin kayıtlarını kurulu OpenClaw derlemesiyle uyumlu tutarken tam plugin komutu tamamlama yeniden oluşturmalarını açık `openclaw completion --write-state` çalıştırmalarına bırakır.

Yerel yönetilen bir Gateway hizmeti kuruluysa ve yeniden başlatma etkinse, paket yöneticisi güncellemeleri paket ağacını değiştirmeden önce çalışan hizmeti durdurur, ardından hizmet meta verilerini güncellenmiş kurulumdan yeniler, hizmeti yeniden başlatır ve başarı bildirmeden önce yeniden başlatılan Gateway'in beklenen sürümü bildirdiğini doğrular. macOS'ta güncelleme sonrası kontrol, LaunchAgent'ın etkin profil için yüklü/çalışıyor olduğunu ve yapılandırılmış loopback portunun sağlıklı olduğunu da doğrular. Plist kuruluysa ancak launchd bunu denetlemiyorsa, OpenClaw LaunchAgent'ı otomatik olarak yeniden bootstrap eder, ardından sağlık/sürüm/kanal hazırlık kontrollerini yeniden çalıştırır. Yeni bir bootstrap, RunAtLoad işini doğrudan yükler; bu nedenle güncelleme kurtarması yeni başlatılan Gateway için hemen `kickstart -k` çalıştırmaz. Gateway yine de sağlıklı hâle gelmezse komut sıfır olmayan kodla çıkar ve yeniden başlatma günlük yolunun yanı sıra açık yeniden başlatma, yeniden kurulum ve paket geri alma talimatlarını yazdırır. `--no-restart` ile paket değiştirme yine çalışır, ancak yönetilen hizmet durdurulmaz veya yeniden başlatılmaz; bu nedenle çalışan Gateway siz manuel olarak yeniden başlatana kadar eski kodu kullanmaya devam edebilir.

## Git checkout akışı

### Kanal seçimi

  * `stable`: en son beta olmayan tag'i checkout eder, ardından derleme ve doctor çalıştırır.
  * `beta`: en son `-beta` tag'ini tercih eder, ancak beta eksikse veya daha eskiyse en son stable tag'e geri döner.
  * `dev`: `main` branch'ini checkout eder, ardından fetch ve rebase yapar.


### Güncelleme adımları

* ### Temiz worktree doğrulaması

Commit edilmemiş değişiklik olmamasını gerektirir.

* ### Kanal değiştir

Seçilen kanala (tag veya branch) geçer.

* ### Upstream getir

Yalnızca dev.

* ### Ön kontrol derlemesi (yalnızca dev)

TypeScript derlemesini geçici bir worktree içinde çalıştırır. Uç commit başarısız olursa, en yeni derlenebilir commit'i bulmak için 10 commit'e kadar geriye gider. Bu ön kontrolde lint de çalıştırmak için `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` ayarlayın; kullanıcı güncelleme makineleri çoğu zaman CI çalıştırıcılarından daha küçük olduğundan lint kısıtlı seri modda çalışır.

* ### Rebase

Seçilen commit üzerine rebase yapar (yalnızca dev).

* ### Bağımlılıkları kur

Repo paket yöneticisini kullanır. pnpm checkout'ları için güncelleyici, bir pnpm workspace içinde `npm run build` çalıştırmak yerine isteğe bağlı olarak `pnpm` bootstrap eder (önce `corepack`, ardından geçici `npm install pnpm@11` yedeğiyle).

* ### Control UI derle

Gateway'i ve Control UI'ı derler.

* ### Doctor çalıştır

Son güvenli güncelleme kontrolü olarak `openclaw doctor` çalışır.

* ### Plugin'leri eşitle

Plugin'leri etkin kanala eşitler. Dev paketlenmiş plugin'leri kullanır; stable ve beta npm kullanır. İzlenen plugin kurulumlarını günceller.

Beta güncelleme kanalında, varsayılan/latest hattını izleyen kayıtlı npm ve ClawHub plugin kurulumları önce bir plugin `@beta` sürümünü dener. Plugin'in beta sürümü yoksa OpenClaw kaydedilmiş varsayılan/latest spec değerine geri döner ve bunu uyarı olarak bildirir. npm plugin'leri için OpenClaw beta paket mevcut olsa bile kurulum doğrulaması başarısız olduğunda da geri döner. Bu plugin yedekleme uyarıları çekirdek güncellemesini başarısız yapmaz. Kesin sürümler ve açık tag'ler yeniden yazılmaz.

## `--update` kısayolu

`openclaw --update`, `openclaw update` olarak yeniden yazılır (shell'ler ve başlatıcı betikler için kullanışlıdır).

## İlgili

  * `openclaw doctor` (git checkout'larında önce update çalıştırmayı teklif eder)
  * [Geliştirme kanalları](</tr/install/development-channels>)
  * [Güncelleme](</tr/install/updating>)
  * [CLI başvurusu](</tr/cli>)


Was this useful?YesNo