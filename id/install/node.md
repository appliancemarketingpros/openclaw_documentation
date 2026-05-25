---
title: Node.js
source_url: https://docs.openclaw.ai/id/install/node
scraped_at: 2026-05-25
---

OpenClaw memerlukan **Node 22.16 atau yang lebih baru**. **Node 24 adalah runtime default dan direkomendasikan** untuk instalasi, CI, dan alur kerja rilis. Node 22 tetap didukung melalui jalur LTS aktif. [skrip penginstal](</id/install#alternative-install-methods>) akan mendeteksi dan menginstal Node secara otomatis - halaman ini ditujukan saat Anda ingin menyiapkan Node sendiri dan memastikan semuanya terhubung dengan benar (versi, PATH, instalasi global).

## Periksa versi Anda

bashCopy code
[code]
    node -v
[/code]

Jika ini mencetak `v24.x.x` atau lebih tinggi, Anda menggunakan default yang direkomendasikan. Jika ini mencetak `v22.16.x` atau lebih tinggi, Anda menggunakan jalur Node 22 LTS yang didukung, tetapi kami tetap menyarankan peningkatan ke Node 24 saat memungkinkan. Jika Node belum terinstal atau versinya terlalu lama, pilih metode instalasi di bawah ini.

## Instal Node

### macOS

**Homebrew** (direkomendasikan):

bashCopy code
[code]
    brew install node
[/code]

Atau unduh penginstal macOS dari [nodejs.org](<https://nodejs.org/>).

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

Atau gunakan manajer versi (lihat di bawah).

### Windows

**winget** (direkomendasikan):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Atau unduh penginstal Windows dari [nodejs.org](<https://nodejs.org/>).

Using a version manager (nvm, fnm, mise, asdf)

Manajer versi memungkinkan Anda beralih antarversi Node dengan mudah. Opsi populer:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- cepat, lintas platform
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- banyak digunakan di macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- poliglot (Node, Python, Ruby, dll.)


Contoh dengan fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Pemecahan masalah

### `openclaw: command not found`

Ini hampir selalu berarti direktori bin global npm tidak ada di PATH Anda.

* ### Find your global npm prefix

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Check if it's on your PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

Cari `<npm-prefix>/bin` (macOS/Linux) atau `<npm-prefix>` (Windows) dalam output.

* ### Add it to your shell startup file

### macOS / Linux

Tambahkan ke `~/.zshrc` atau `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Lalu buka terminal baru (atau jalankan `rehash` di zsh / `hash -r` di bash).

### Windows

Tambahkan output dari `npm prefix -g` ke PATH sistem Anda melalui Settings → System → Environment Variables.

### Kesalahan izin pada `npm install -g` (Linux)

Jika Anda melihat kesalahan `EACCES`, ubah prefix global npm ke direktori yang dapat ditulis pengguna:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Tambahkan baris `export PATH=...` ke `~/.bashrc` atau `~/.zshrc` Anda agar permanen.

## Terkait

  * [Ikhtisar Instalasi](</id/install>) \- semua metode instalasi
  * [Memperbarui](</id/install/updating>) \- menjaga OpenClaw tetap terbaru
  * [Memulai](</id/start/getting-started>) \- langkah pertama setelah instalasi


Was this useful?YesNo