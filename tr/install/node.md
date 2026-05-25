---
title: Node.js
source_url: https://docs.openclaw.ai/tr/install/node
scraped_at: 2026-05-25
---

OpenClaw, **Node 22.16 veya daha yeni bir sürüm** gerektirir. **Node 24, kurulumlar, CI ve sürüm iş akışları için varsayılan ve önerilen çalışma zamanıdır**. Node 22, aktif LTS hattı üzerinden desteklenmeye devam eder. [Kurulum betiği](</tr/install#alternative-install-methods>), Node'u otomatik olarak algılayıp kurar - bu sayfa, Node'u kendiniz kurmak ve her şeyin doğru bağlandığından emin olmak istediğiniz durumlar içindir (sürümler, PATH, global kurulumlar).

## Sürümünüzü kontrol edin

bashCopy code
[code]
    node -v
[/code]

Bu komut `v24.x.x` veya daha yüksek bir sürüm yazdırırsa önerilen varsayılandasınız. `v22.16.x` veya daha yüksek bir sürüm yazdırırsa desteklenen Node 22 LTS yolundasınız, ancak uygun olduğunda Node 24'e yükseltmenizi yine de öneririz. Node kurulu değilse veya sürüm çok eskiyse aşağıdan bir kurulum yöntemi seçin.

## Node'u kurun

### macOS

**Homebrew** (önerilir):

bashCopy code
[code]
    brew install node
[/code]

Alternatif olarak macOS kurulum aracını [nodejs.org](<https://nodejs.org/>) adresinden indirin.

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

Alternatif olarak bir sürüm yöneticisi kullanın (aşağıya bakın).

### Windows

**winget** (önerilir):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Alternatif olarak Windows kurulum aracını [nodejs.org](<https://nodejs.org/>) adresinden indirin.

Bir sürüm yöneticisi kullanma (nvm, fnm, mise, asdf)

Sürüm yöneticileri, Node sürümleri arasında kolayca geçiş yapmanızı sağlar. Popüler seçenekler:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- hızlı, platformlar arası
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- macOS/Linux üzerinde yaygın olarak kullanılır
  * [**mise**](<https://mise.jdx.dev/>) \- çok dilli (Node, Python, Ruby vb.)


fnm ile örnek:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Sorun giderme

### `openclaw: command not found`

Bu neredeyse her zaman npm'in global bin dizininin PATH'inizde olmadığı anlamına gelir.

* ### Global npm prefix değerini bulun

bashCopy code
[code]
    npm prefix -g
[/code]

* ### PATH'inizde olup olmadığını kontrol edin

bashCopy code
[code]
    echo "$PATH"
[/code]

Çıktıda `<npm-prefix>/bin` (macOS/Linux) veya `<npm-prefix>` (Windows) arayın.

* ### Kabuk başlangıç dosyanıza ekleyin

### macOS / Linux

`~/.zshrc` veya `~/.bashrc` dosyasına ekleyin:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Ardından yeni bir terminal açın (veya zsh içinde `rehash` / bash içinde `hash -r` çalıştırın).

### Windows

`npm prefix -g` çıktısını Ayarlar → Sistem → Ortam Değişkenleri üzerinden sistem PATH'inize ekleyin.

### `npm install -g` üzerinde izin hataları (Linux)

`EACCES` hataları görürseniz npm'in global prefix değerini kullanıcı tarafından yazılabilir bir dizine taşıyın:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Kalıcı hale getirmek için `export PATH=...` satırını `~/.bashrc` veya `~/.zshrc` dosyanıza ekleyin.

## İlgili

  * [Kuruluma Genel Bakış](</tr/install>) \- tüm kurulum yöntemleri
  * [Güncelleme](</tr/install/updating>) \- OpenClaw'u güncel tutma
  * [Başlarken](</tr/start/getting-started>) \- kurulumdan sonraki ilk adımlar


Was this useful?YesNo