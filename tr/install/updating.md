---
title: Güncelleniyor
source_url: https://docs.openclaw.ai/tr/install/updating
scraped_at: 2026-05-25
---

OpenClaw'ı güncel tutun.

## Önerilen: `openclaw update`

Güncellemenin en hızlı yolu. Kurulum türünüzü (npm veya git) algılar, en son sürümü getirir, `openclaw doctor` çalıştırır ve Gateway'i yeniden başlatır.

bashCopy code
[code]
    openclaw update
[/code]

Kanalları değiştirmek veya belirli bir sürümü hedeflemek için:

bashCopy code
[code]
    openclaw update --channel betaopenclaw update --channel devopenclaw update --tag mainopenclaw update --dry-run   # preview without applying
[/code]

`openclaw update`, `--verbose` kabul etmez. Güncelleme tanılamaları için planlanan eylemleri önizlemek üzere `--dry-run`, yapılandırılmış sonuçlar için `--json` veya kanal ve kullanılabilirlik durumunu incelemek için `openclaw update status --json` kullanın. Kurucunun kendi `--verbose` bayrağı vardır, ancak bu bayrak `openclaw update` kapsamına dahil değildir.

`--channel beta` betayı tercih eder, ancak beta etiketi eksikse veya en son kararlı sürümden daha eskiyse çalışma zamanı kararlı/en son sürüme geri döner. Tek seferlik bir paket güncellemesi için ham npm beta dist-tag değerini istiyorsanız `--tag beta` kullanın.

Yönetilen plugin'ler için beta kanalı geri dönüşü bir uyarıdır: plugin betası mevcut olmadığı için bir plugin kayıtlı varsayılan/en son sürümünü kullanırken çekirdek güncellemesi yine de başarılı olabilir.

Kanal anlamları için [Geliştirme kanalları](</tr/install/development-channels>) bölümüne bakın.

## npm ve git kurulumları arasında geçiş yapın

Kurulum türünü değiştirmek istediğinizde kanalları kullanın. Güncelleyici durumunuzu, yapılandırmanızı, kimlik bilgilerinizi ve çalışma alanınızı `~/.openclaw` içinde tutar; yalnızca CLI ve Gateway'in hangi OpenClaw kod kurulumunu kullandığını değiştirir.

bashCopy code
[code]
    # npm package install -> editable git checkoutopenclaw update --channel dev # git checkout -> npm package installopenclaw update --channel stable
[/code]

Tam kurulum modu geçişini önizlemek için önce `--dry-run` ile çalıştırın:

bashCopy code
[code]
    openclaw update --channel dev --dry-runopenclaw update --channel stable --dry-run
[/code]

`dev` kanalı bir git checkout sağlar, onu derler ve global CLI'yi bu checkout'tan yükler. `stable` ve `beta` kanalları paket kurulumlarını kullanır. Gateway zaten kuruluysa, `openclaw update` servis metaverilerini yeniler ve `--no-restart` geçmediğiniz sürece yeniden başlatır.

## Alternatif: kurucuyu yeniden çalıştırın

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

İlk kurulumu atlamak için `--no-onboard` ekleyin. Kurucu üzerinden belirli bir kurulum türünü zorlamak için `--install-method git --no-onboard` veya `--install-method npm --no-onboard` geçin.

`openclaw update`, npm paket kurulum aşamasından sonra başarısız olursa kurucuyu yeniden çalıştırın. Kurucu eski güncelleyiciyi çağırmaz; global paket kurulumunu doğrudan çalıştırır ve kısmen güncellenmiş bir npm kurulumunu kurtarabilir.

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm
[/code]

Kurtarmayı belirli bir sürüme veya dist-tag'e sabitlemek için `--version` ekleyin:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm --version <version-or-dist-tag>
[/code]

## Alternatif: manuel npm, pnpm veya bun

bashCopy code
[code]
    npm i -g openclaw@latest
[/code]

Denetimli kurulumlar için `openclaw update` tercih edin, çünkü paket değişimini çalışan Gateway servisiyle koordine edebilir. Yönetilen bir Gateway çalışırken manuel güncelleme yaparsanız, paket yöneticisi tamamlanır tamamlanmaz Gateway'i yeniden başlatın; böylece eski süreç, değiştirilmiş paket dosyalarından hizmet vermeyi sürdürmez.

`openclaw update` global bir npm kurulumunu yönettiğinde, hedefi önce geçici bir npm önekine yükler, paketlenmiş `dist` envanterini doğrular ve ardından temiz paket ağacını gerçek global öneke taşır. Bu, npm'in yeni bir paketi eski paketten kalan bayat dosyaların üzerine yerleştirmesini önler. Kurulum komutu başarısız olursa OpenClaw `--omit=optional` ile bir kez yeniden dener. Bu yeniden deneme, yerel isteğe bağlı bağımlılıkların derlenemediği host'larda yardımcı olurken, geri dönüş de başarısız olursa özgün hatayı görünür tutar.

bashCopy code
[code]
    pnpm add -g openclaw@latest
[/code]

bashCopy code
[code]
    bun add -g openclaw@latest
[/code]

### Gelişmiş npm kurulum konuları

Read-only package tree

OpenClaw, global paket dizini geçerli kullanıcı tarafından yazılabilir olsa bile, paketlenmiş global kurulumları çalışma zamanında salt okunur olarak ele alır. Plugin paket kurulumları, kullanıcı yapılandırma dizini altındaki OpenClaw'a ait npm/git köklerinde bulunur ve Gateway başlangıcı OpenClaw paket ağacını değiştirmez.

Bazı Linux npm kurulumları, global paketleri `/usr/lib/node_modules/openclaw` gibi root'a ait dizinlerin altına yükler. OpenClaw bu düzeni destekler, çünkü plugin kurulum/güncelleme komutları bu global paket dizininin dışına yazar.

Hardened systemd units

Açık plugin kurulumları, plugin güncellemeleri ve doctor temizliği değişikliklerini kalıcı hale getirebilsin diye OpenClaw'a yapılandırma/durum köklerine yazma erişimi verin:

iniCopy code
[code]
    ReadWritePaths=/var/lib/openclaw /home/openclaw/.openclaw /tmp
[/code]

Disk-space preflight

Paket güncellemelerinden ve açık plugin kurulumlarından önce OpenClaw, hedef birim için elinden gelen en iyi disk alanı denetimini dener. Düşük alan, denetlenen yolla birlikte bir uyarı üretir, ancak güncellemeyi engellemez; çünkü dosya sistemi kotaları, snapshot'lar ve ağ birimleri denetimden sonra değişebilir. Asıl paket yöneticisi kurulumu ve kurulum sonrası doğrulama yetkili olmaya devam eder.

## Otomatik güncelleyici

Otomatik güncelleyici varsayılan olarak kapalıdır. `~/.openclaw/openclaw.json` içinde etkinleştirin:

json5Copy code
[code]
    {  update: {    channel: "stable",    auto: {      enabled: true,      stableDelayHours: 6,      stableJitterHours: 12,      betaCheckIntervalHours: 1,    },  },}
[/code]

Kanal | Davranış  
---|---  
`stable` | `stableDelayHours` kadar bekler, ardından `stableJitterHours` boyunca deterministik jitter ile uygular (yayılmış dağıtım).  
`beta` | Her `betaCheckIntervalHours` aralığında denetler (varsayılan: saatlik) ve hemen uygular.  
`dev` | Otomatik uygulama yoktur. `openclaw update` komutunu manuel kullanın.  
  
Gateway ayrıca başlangıçta bir güncelleme ipucu günlüğe yazar (`update.checkOnStart: false` ile devre dışı bırakın). Sürüm düşürme veya olay kurtarma için, `update.auto.enabled` yapılandırılmış olsa bile otomatik uygulamaları engellemek üzere Gateway ortamında `OPENCLAW_NO_AUTO_UPDATE=1` ayarlayın. `update.checkOnStart` da devre dışı bırakılmadığı sürece başlangıç güncelleme ipuçları çalışmaya devam edebilir.

Canlı Gateway denetim düzlemi işleyicisi üzerinden istenen paket yöneticisi güncellemeleri, paket değişiminden sonra ertelenmeyen ve bekleme süresi olmayan bir güncelleme yeniden başlatmasını zorlar. Bu, eski bellek içi sürecin, zaten değiştirilmiş bir paket ağacından parçaları lazy-load edecek kadar uzun süre ortada kalmasını önler. Shell `openclaw update`, servisi güncelleme etrafında durdurup yeniden başlatabildiği için denetimli kurulumlarda tercih edilen yol olmaya devam eder.

## Güncellemeden sonra

### Doctor'ı çalıştırın

bashCopy code
[code]
    openclaw doctor
[/code]

Yapılandırmayı taşır, DM ilkelerini denetler ve Gateway sağlığını kontrol eder. Ayrıntılar: [Doctor](</tr/gateway/doctor>)

### Gateway'i yeniden başlatın

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Doğrulayın

bashCopy code
[code]
    openclaw health
[/code]

## Geri alma

### Bir sürüme sabitleyin (npm)

bashCopy code
[code]
    npm i -g openclaw@<version>openclaw doctoropenclaw gateway restart
[/code]

### Bir commit'e sabitleyin (kaynak)

bashCopy code
[code]
    git fetch origingit checkout "$(git rev-list -n 1 --before=\"2026-01-01\" origin/main)"pnpm install && pnpm buildopenclaw gateway restart
[/code]

En son sürüme dönmek için: `git checkout main && git pull`.

## Takılırsanız

  * `openclaw doctor` komutunu yeniden çalıştırın ve çıktıyı dikkatle okuyun.
  * Kaynak checkout'larında `openclaw update --channel dev` için güncelleyici gerektiğinde `pnpm`'i otomatik olarak bootstraps eder. Bir pnpm/corepack bootstrap hatası görürseniz `pnpm`'i manuel yükleyin (veya `corepack`'i yeniden etkinleştirin) ve güncellemeyi yeniden çalıştırın.
  * Denetleyin: [Sorun giderme](</tr/gateway/troubleshooting>)
  * Discord'da sorun: <https://discord.gg/clawd>


## İlgili

  * [Kurulum genel bakışı](</tr/install>): tüm kurulum yöntemleri.
  * [Doctor](</tr/gateway/doctor>): güncellemelerden sonra sağlık denetimleri.
  * [Geçiş](</tr/install/migrating>): ana sürüm geçiş kılavuzları.


Was this useful?YesNo