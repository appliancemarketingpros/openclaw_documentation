---
title: Yükleyicinin iç işleyişi
source_url: https://docs.openclaw.ai/tr/install/installer
scraped_at: 2026-05-25
---

OpenClaw, `openclaw.ai` üzerinden sunulan üç yükleyici betiğiyle gelir.

Betik | Platform | Ne yapar  
---|---|---  
`install.sh` | macOS / Linux / WSL | Gerektiğinde Node kurar, OpenClaw’ı npm (varsayılan) veya git üzerinden kurar ve onboarding çalıştırabilir.  
`install-cli.sh` | macOS / Linux / WSL | Node + OpenClaw’ı npm veya git checkout modlarıyla yerel bir öneke (`~/.openclaw`) kurar. Root gerekmez.  
`install.ps1` | Windows (PowerShell) | Gerektiğinde Node kurar, OpenClaw’ı npm (varsayılan) veya git üzerinden kurar ve onboarding çalıştırabilir.  
  
## Hızlı komutlar

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### Akış ([install.sh](<http://install.sh>))

* ### Detect OS

macOS ve Linux’u (WSL dahil) destekler. macOS algılanırsa ve Homebrew eksikse Homebrew kurar.

* ### Ensure Node.js 24 by default

Node sürümünü denetler ve gerekirse Node 24 kurar (macOS’ta Homebrew, Linux apt/dnf/yum üzerinde NodeSource kurulum betikleri). OpenClaw uyumluluk için hâlâ şu anda `22.16+` olan Node 22 LTS’yi destekler.

* ### Ensure Git

Eksikse Git kurar.

* ### Install OpenClaw

  * `npm` yöntemi (varsayılan): global npm kurulumu
  * `git` yöntemi: repoyu klonlar/günceller, bağımlılıkları pnpm ile kurar, derler, ardından sarmalayıcıyı `~/.local/bin/openclaw` konumuna kurar


* ### Post-install tasks

  * Yüklü bir Gateway servisini en iyi çabayla yeniler (`openclaw gateway install --force`, ardından yeniden başlatma)
  * Yükseltmelerde ve git kurulumlarında `openclaw doctor --non-interactive` çalıştırır (en iyi çaba)
  * Uygun olduğunda onboarding yapmayı dener (TTY mevcutsa, onboarding devre dışı değilse ve bootstrap/config denetimleri geçerse)
  * `SHARP_IGNORE_GLOBAL_LIBVIPS=1` varsayılanını kullanır


### Kaynak checkout algılama

Bir OpenClaw checkout içinde çalıştırılırsa (`package.json` \+ `pnpm-workspace.yaml`), betik şunları sunar:

  * checkout kullan (`git`), veya
  * global kurulum kullan (`npm`)


TTY yoksa ve kurulum yöntemi ayarlanmamışsa, varsayılan olarak `npm` kullanır ve uyarır.

Betik, geçersiz yöntem seçimi veya geçersiz `--install-method` değerleri için `2` koduyla çıkar.

### Örnekler ([install.sh](<http://install.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Skip onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main via npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Dry run

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Flags reference Bayrak | Açıklama  
---|---  
`--install-method npm|git` | Kurulum yöntemini seçer (varsayılan: `npm`). Takma ad: `--method`  
`--npm` | npm yöntemi için kısayol  
`--git` | git yöntemi için kısayol. Takma ad: `--github`  
`--version <version|dist-tag|spec>` | npm sürümü, dist-tag veya paket belirtimi (varsayılan: `latest`)  
`--beta` | Varsa beta dist-tag kullanır, yoksa `latest` değerine geri döner  
`--git-dir <path>` | Checkout dizini (varsayılan: `~/openclaw`). Takma ad: `--dir`  
`--no-git-update` | Mevcut checkout için `git pull` atlar  
`--no-prompt` | İstemleri devre dışı bırakır  
`--no-onboard` | Onboarding’i atlar  
`--onboard` | Onboarding’i etkinleştirir  
`--dry-run` | Değişiklik uygulamadan eylemleri yazdırır  
`--verbose` | Hata ayıklama çıktısını etkinleştirir (`set -x`, npm notice-level günlükleri)  
`--help` | Kullanımı gösterir (`-h`)  
Environment variables reference Değişken | Açıklama  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Kurulum yöntemi  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | npm sürümü, dist-tag veya paket belirtimi  
`OPENCLAW_BETA=0|1` | Varsa beta kullan  
`OPENCLAW_GIT_DIR=<path>` | Checkout dizini  
`OPENCLAW_GIT_UPDATE=0|1` | git güncellemelerini aç/kapat  
`OPENCLAW_NO_PROMPT=1` | İstemleri devre dışı bırak  
`OPENCLAW_NO_ONBOARD=1` | Onboarding’i atla  
`OPENCLAW_DRY_RUN=1` | Kuru çalıştırma modu  
`OPENCLAW_VERBOSE=1` | Hata ayıklama modu  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm günlük düzeyi  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | sharp/libvips davranışını denetler (varsayılan: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Akış ([install-cli.sh](<http://install-cli.sh>))

* ### Install local Node runtime

Sabitlenmiş desteklenen bir Node LTS tarball dosyasını (sürüm betiğe gömülüdür ve bağımsız olarak güncellenir) `<prefix>/tools/node-v<version>` konumuna indirir ve SHA-256 doğrular.

* ### Ensure Git

Git eksikse, Linux’ta apt/dnf/yum veya macOS’ta Homebrew üzerinden kurmayı dener.

* ### Install OpenClaw under prefix

  * `npm` yöntemi (varsayılan): önek altına npm ile kurar, ardından sarmalayıcıyı `<prefix>/bin/openclaw` konumuna yazar
  * `git` yöntemi: bir checkout’u klonlar/günceller (varsayılan `~/openclaw`) ve yine sarmalayıcıyı `<prefix>/bin/openclaw` konumuna yazar


* ### Refresh loaded gateway service

Bir Gateway servisi aynı önekten zaten yüklenmişse, betik `openclaw gateway install --force`, ardından `openclaw gateway restart` çalıştırır ve Gateway sağlığını en iyi çabayla yoklar.

### Örnekler ([install-cli.sh](<http://install-cli.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Custom prefix + version

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### Automation JSON output

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Run onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Flags reference Bayrak | Açıklama  
---|---  
`--prefix <path>` | Kurulum öneki (varsayılan: `~/.openclaw`)  
`--install-method npm|git` | Kurulum yöntemini seçer (varsayılan: `npm`). Takma ad: `--method`  
`--npm` | npm yöntemi için kısayol  
`--git`, `--github` | git yöntemi için kısayol  
`--git-dir <path>` | Git checkout dizini (varsayılan: `~/openclaw`). Takma ad: `--dir`  
`--version <ver>` | OpenClaw sürümü veya dist-tag (varsayılan: `latest`)  
`--node-version <ver>` | Node sürümü (varsayılan: `22.22.0`)  
`--json` | NDJSON olayları yayar  
`--onboard` | Kurulumdan sonra `openclaw onboard` çalıştırır  
`--no-onboard` | Onboarding’i atlar (varsayılan)  
`--set-npm-prefix` | Linux’ta, geçerli önek yazılabilir değilse npm önekini `~/.npm-global` olmaya zorlar  
`--help` | Kullanımı gösterir (`-h`)  
Environment variables reference Değişken | Açıklama  
---|---  
`OPENCLAW_PREFIX=<path>` | Kurulum öneki  
`OPENCLAW_INSTALL_METHOD=git|npm` | Kurulum yöntemi  
`OPENCLAW_VERSION=<ver>` | OpenClaw sürümü veya dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Node sürümü  
`OPENCLAW_GIT_DIR=<path>` | Git kurulumları için Git checkout dizini  
`OPENCLAW_GIT_UPDATE=0|1` | Mevcut checkout'lar için git güncellemelerini aç/kapat  
`OPENCLAW_NO_ONBOARD=1` | Onboarding'i atla  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm günlük düzeyi  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | sharp/libvips davranışını denetle (varsayılan: `1`)  
  
* * *

## install.ps1

### Akış (install.ps1)

* ### PowerShell + Windows ortamını doğrula

PowerShell 5+ gerektirir.

* ### Varsayılan olarak Node.js 24'ü doğrula

Eksikse winget, ardından Chocolatey, ardından Scoop üzerinden kurmayı dener. Node 22 LTS, şu anda `22.16+`, uyumluluk için desteklenmeye devam eder.

* ### OpenClaw'ı kur

  * `npm` yöntemi (varsayılan): seçilen `-Tag` kullanılarak global npm kurulumu; `C:\` gibi korumalı klasörlerde açılan kabukların da çalışması için yazılabilir bir yükleyici geçici dizininden başlatılır
  * `git` yöntemi: repoyu klonlar/günceller, pnpm ile kurar/derler ve sarmalayıcıyı `%USERPROFILE%\.local\bin\openclaw.cmd` konumuna kurar


* ### Kurulum sonrası görevler

  * Mümkün olduğunda gerekli bin dizinini kullanıcı PATH'ine ekler
  * Yüklü bir Gateway hizmetini en iyi çabayla yeniler (`openclaw gateway install --force`, ardından yeniden başlatma)
  * Yükseltmelerde ve git kurulumlarında `openclaw doctor --non-interactive` çalıştırır (en iyi çabayla)


* ### Hataları işle

`iwr ... | iex` ve scriptblock kurulumları, geçerli PowerShell oturumunu kapatmadan sonlandırıcı hata bildirir. Doğrudan `powershell -File` / `pwsh -File` kurulumları otomasyon için yine sıfır olmayan kodla çıkar.

### Örnekler (install.ps1)

### Varsayılan

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Git kurulumu

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### npm üzerinden GitHub main

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Özel git dizini

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Deneme çalıştırması

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Hata ayıklama izi

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Bayrak başvurusu Bayrak | Açıklama  
---|---  
`-InstallMethod npm|git` | Kurulum yöntemi (varsayılan: `npm`)  
`-Tag <tag|version|spec>` | npm dist-tag, sürüm veya paket belirtimi (varsayılan: `latest`)  
`-GitDir <path>` | Checkout dizini (varsayılan: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Onboarding'i atla  
`-NoGitUpdate` | `git pull` işlemini atla  
`-DryRun` | Yalnızca eylemleri yazdır  
Ortam değişkenleri başvurusu Değişken | Açıklama  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Kurulum yöntemi  
`OPENCLAW_GIT_DIR=<path>` | Checkout dizini  
`OPENCLAW_NO_ONBOARD=1` | Onboarding'i atla  
`OPENCLAW_GIT_UPDATE=0` | git pull'u devre dışı bırak  
`OPENCLAW_DRY_RUN=1` | Deneme çalıştırması modu  
  
* * *

## CI ve otomasyon

Öngörülebilir çalıştırmalar için etkileşimsiz bayraklar/ortam değişkenleri kullanın.

### install.sh (etkileşimsiz npm)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (etkileşimsiz git)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (onboarding'i atla)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Sorun giderme

Git neden gerekli?

Git, `git` kurulum yöntemi için gereklidir. `npm` kurulumlarında, bağımlılıklar git URL'leri kullandığında `spawn git ENOENT` hatalarını önlemek için Git yine de denetlenir/kurulur.

npm Linux'ta neden EACCES'e takılıyor?

Bazı Linux kurulumları npm global önekini root'a ait yollara yönlendirir. `install.sh`, öneki `~/.npm-global` olarak değiştirebilir ve PATH dışa aktarımlarını kabuk rc dosyalarına ekleyebilir (bu dosyalar mevcut olduğunda).

sharp/libvips sorunları

Betikler, sharp'ın sistem libvips'e karşı derlenmesini önlemek için varsayılan olarak `SHARP_IGNORE_GLOBAL_LIBVIPS=1` kullanır. Geçersiz kılmak için:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Git for Windows'ı kurun, PowerShell'i yeniden açın, yükleyiciyi yeniden çalıştırın.

Windows: "openclaw is not recognized"

`npm config get prefix` komutunu çalıştırın ve bu dizini kullanıcı PATH'inize ekleyin (Windows'ta `\bin` son eki gerekmez), ardından PowerShell'i yeniden açın.

Windows: ayrıntılı yükleyici çıktısı nasıl alınır

`install.ps1` şu anda bir `-Verbose` anahtarı sunmaz. Betik düzeyi tanılamalar için PowerShell izlemeyi kullanın:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

kurulumdan sonra openclaw bulunamadı

Genellikle bir PATH sorunudur. Bkz. [Node.js sorun giderme](</tr/install/node#troubleshooting>).

## İlgili

  * [Kurulum genel bakışı](</tr/install>)
  * [Güncelleme](</tr/install/updating>)
  * [Kaldırma](</tr/install/uninstall>)


Was this useful?YesNo