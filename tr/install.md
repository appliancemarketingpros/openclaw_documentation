---
title: Kurulum
source_url: https://docs.openclaw.ai/tr/install
scraped_at: 2026-05-25
---

## Sistem gereksinimleri

  * **Node 24** (önerilir) veya Node 22.16+ - yükleyici betiği bunu otomatik olarak halleder
  * **macOS, Linux veya Windows** \- hem yerel Windows hem de WSL2 desteklenir; WSL2 daha kararlıdır. Bkz. [Windows](</tr/platforms/windows>).
  * Kaynaktan derleme yapıyorsanız yalnızca `pnpm` gerekir


## Önerilen: yükleyici betiği

Kurulumun en hızlı yolu. İşletim sisteminizi algılar, gerekirse Node kurar, OpenClaw'ı kurar ve ilk kurulumu başlatır.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

İlk kurulumu çalıştırmadan kurmak için:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

Tüm bayraklar ve CI/otomasyon seçenekleri için bkz. [Yükleyici ayrıntıları](</tr/install/installer>).

## Alternatif kurulum yöntemleri

### Yerel önek yükleyicisi (`install-cli.sh`)

OpenClaw ve Node'un, sistem geneline kurulu bir Node'a bağımlı olmadan `~/.openclaw` gibi yerel bir önek altında tutulmasını istediğinizde bunu kullanın:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Varsayılan olarak npm kurulumlarını ve aynı önek akışı altında git-checkout kurulumlarını destekler. Tam başvuru: [Yükleyici ayrıntıları](</tr/install/installer#install-clish>).

Zaten kurulu mu? Paket ve git kurulumları arasında `openclaw update --channel dev` ve `openclaw update --channel stable` ile geçiş yapın. Bkz. [Güncelleme](</tr/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm veya bun

Node'u zaten kendiniz yönetiyorsanız:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Troubleshooting: sharp build errors (npm)

`sharp`, global olarak kurulmuş libvips nedeniyle başarısız olursa:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### Kaynaktan

Katkıda bulunanlar veya yerel bir checkout'tan çalıştırmak isteyen herkes için:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Alternatif olarak link adımını atlayıp repo içinden `pnpm openclaw ...` kullanabilirsiniz. Tam geliştirme iş akışları için bkz. [Kurulum](</tr/start/setup>).

### GitHub main dalından kurulum

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Kapsayıcılar ve paket yöneticileri

[**Docker** Kapsayıcılı veya başsız dağıtımlar. ](</tr/install/docker>) [**Podman** Docker'a root yetkisi gerektirmeyen kapsayıcı alternatifi. ](</tr/install/podman>) [**Nix** Nix flake ile bildirimsel kurulum. ](</tr/install/nix>) [**Ansible** Otomatik filo hazırlama. ](</tr/install/ansible>) [**Bun** Bun çalışma zamanı üzerinden yalnızca CLI kullanımı. ](</tr/install/bun>)

## Kurulumu doğrulama

bashCopy code
[code]
    openclaw --version      # CLI'nin kullanılabilir olduğunu doğrulayınopenclaw doctor         # yapılandırma sorunlarını denetleyinopenclaw gateway status # Gateway'in çalıştığını doğrulayın
[/code]

Kurulumdan sonra yönetilen başlangıç istiyorsanız:

  * macOS: `openclaw onboard --install-daemon` veya `openclaw gateway install` ile LaunchAgent
  * Linux/WSL2: aynı komutlarla systemd kullanıcı hizmeti
  * Yerel Windows: önce Zamanlanmış Görev, görev oluşturma reddedilirse kullanıcı başına Startup klasörü oturum açma öğesi yedeği


## Barındırma ve dağıtım

OpenClaw'ı bir bulut sunucusuna veya VPS'ye dağıtın:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii90ci9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Güncelleme, taşıma veya kaldırma [**Updating** OpenClaw'ı güncel tutun. ](</tr/install/updating>) [**Migrating** Yeni bir makineye taşıyın. ](</tr/install/migrating>) [**Uninstall** OpenClaw'ı tamamen kaldırın. ](</tr/install/uninstall>) Sorun giderme: `openclaw` bulunamadı Kurulum başarılı olduysa ancak terminalinizde `openclaw` bulunamıyorsa: bashCopy code
[code]
    node -v           # Node kurulu mu?npm prefix -g     # Global paketler nerede?echo "$PATH"      # Global bin dizini PATH içinde mi?
[/code]

`$(npm prefix -g)/bin`, `$PATH` içinde değilse bunu kabuk başlangıç dosyanıza (`~/.zshrc` veya `~/.bashrc`) ekleyin: bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Ardından yeni bir terminal açın. Daha fazla ayrıntı için bkz. [Node kurulumu](</tr/install/node>). ](</tr/install/northflank>) Was this useful?YesNo ](</tr/install/render>)](</tr/install/railway>)](</tr/install/azure>)](</tr/install/gcp>)](</tr/install/hetzner>)](</tr/install/kubernetes>)](</tr/install/docker-vm-runtime>)](</tr/vps>)