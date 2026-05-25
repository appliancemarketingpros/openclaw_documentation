---
title: Internal penginstal
source_url: https://docs.openclaw.ai/id/install/installer
scraped_at: 2026-05-25
---

OpenClaw mengirimkan tiga skrip penginstal, disajikan dari `openclaw.ai`.

Skrip | Platform | Fungsinya  
---|---|---  
`install.sh` | macOS / Linux / WSL | Menginstal Node jika diperlukan, menginstal OpenClaw melalui npm (default) atau git, dan dapat menjalankan onboarding.  
`install-cli.sh` | macOS / Linux / WSL | Menginstal Node + OpenClaw ke prefiks lokal (`~/.openclaw`) dengan mode npm atau git checkout. Tidak memerlukan root.  
`install.ps1` | Windows (PowerShell) | Menginstal Node jika diperlukan, menginstal OpenClaw melalui npm (default) atau git, dan dapat menjalankan onboarding.  
  
## Perintah cepat

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

### Alur ([install.sh](<http://install.sh>))

* ### Detect OS

Mendukung macOS dan Linux (termasuk WSL). Jika macOS terdeteksi, menginstal Homebrew jika belum ada.

* ### Ensure Node.js 24 by default

Memeriksa versi Node dan menginstal Node 24 jika diperlukan (Homebrew di macOS, skrip penyiapan NodeSource di Linux apt/dnf/yum). OpenClaw masih mendukung Node 22 LTS, saat ini `22.16+`, untuk kompatibilitas.

* ### Ensure Git

Menginstal Git jika belum ada.

* ### Install OpenClaw

  * Metode `npm` (default): instalasi npm global
  * Metode `git`: clone/perbarui repo, instal dependensi dengan pnpm, build, lalu instal wrapper di `~/.local/bin/openclaw`


* ### Post-install tasks

  * Menyegarkan layanan Gateway yang dimuat secara upaya terbaik (`openclaw gateway install --force`, lalu restart)
  * Menjalankan `openclaw doctor --non-interactive` pada upgrade dan instalasi git (upaya terbaik)
  * Mencoba onboarding bila sesuai (TTY tersedia, onboarding tidak dinonaktifkan, dan pemeriksaan bootstrap/config lolos)
  * Mengatur default `SHARP_IGNORE_GLOBAL_LIBVIPS=1`


### Deteksi checkout sumber

Jika dijalankan di dalam checkout OpenClaw (`package.json` \+ `pnpm-workspace.yaml`), skrip menawarkan:

  * gunakan checkout (`git`), atau
  * gunakan instalasi global (`npm`)


Jika tidak ada TTY yang tersedia dan tidak ada metode instalasi yang ditetapkan, default-nya adalah `npm` dan menampilkan peringatan.

Skrip keluar dengan kode `2` untuk pemilihan metode yang tidak valid atau nilai `--install-method` yang tidak valid.

### Contoh ([install.sh](<http://install.sh>))

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

Flags reference Flag | Deskripsi  
---|---  
`--install-method npm|git` | Pilih metode instalasi (default: `npm`). Alias: `--method`  
`--npm` | Pintasan untuk metode npm  
`--git` | Pintasan untuk metode git. Alias: `--github`  
`--version <version|dist-tag|spec>` | Versi npm, dist-tag, atau spesifikasi paket (default: `latest`)  
`--beta` | Gunakan dist-tag beta jika tersedia, jika tidak fallback ke `latest`  
`--git-dir <path>` | Direktori checkout (default: `~/openclaw`). Alias: `--dir`  
`--no-git-update` | Lewati `git pull` untuk checkout yang sudah ada  
`--no-prompt` | Nonaktifkan prompt  
`--no-onboard` | Lewati onboarding  
`--onboard` | Aktifkan onboarding  
`--dry-run` | Cetak tindakan tanpa menerapkan perubahan  
`--verbose` | Aktifkan output debug (`set -x`, log npm level notice)  
`--help` | Tampilkan penggunaan (`-h`)  
Environment variables reference Variabel | Deskripsi  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Metode instalasi  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | Versi npm, dist-tag, atau spesifikasi paket  
`OPENCLAW_BETA=0|1` | Gunakan beta jika tersedia  
`OPENCLAW_GIT_DIR=<path>` | Direktori checkout  
`OPENCLAW_GIT_UPDATE=0|1` | Aktifkan/nonaktifkan pembaruan git  
`OPENCLAW_NO_PROMPT=1` | Nonaktifkan prompt  
`OPENCLAW_NO_ONBOARD=1` | Lewati onboarding  
`OPENCLAW_DRY_RUN=1` | Mode dry run  
`OPENCLAW_VERBOSE=1` | Mode debug  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Level log npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Kontrol perilaku sharp/libvips (default: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Alur ([install-cli.sh](<http://install-cli.sh>))

* ### Install local Node runtime

Mengunduh tarball Node LTS didukung yang dipin (versinya disematkan di dalam skrip dan diperbarui secara independen) ke `<prefix>/tools/node-v<version>` dan memverifikasi SHA-256.

* ### Ensure Git

Jika Git belum ada, mencoba instalasi melalui apt/dnf/yum di Linux atau Homebrew di macOS.

* ### Install OpenClaw under prefix

  * Metode `npm` (default): menginstal di bawah prefiks dengan npm, lalu menulis wrapper ke `<prefix>/bin/openclaw`
  * Metode `git`: clone/memperbarui checkout (default `~/openclaw`) dan tetap menulis wrapper ke `<prefix>/bin/openclaw`


* ### Refresh loaded gateway service

Jika layanan Gateway sudah dimuat dari prefiks yang sama, skrip menjalankan `openclaw gateway install --force`, lalu `openclaw gateway restart`, dan memeriksa kesehatan Gateway secara upaya terbaik.

### Contoh ([install-cli.sh](<http://install-cli.sh>))

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

Flags reference Flag | Deskripsi  
---|---  
`--prefix <path>` | Prefiks instalasi (default: `~/.openclaw`)  
`--install-method npm|git` | Pilih metode instalasi (default: `npm`). Alias: `--method`  
`--npm` | Pintasan untuk metode npm  
`--git`, `--github` | Pintasan untuk metode git  
`--git-dir <path>` | Direktori checkout Git (default: `~/openclaw`). Alias: `--dir`  
`--version <ver>` | Versi OpenClaw atau dist-tag (default: `latest`)  
`--node-version <ver>` | Versi Node (default: `22.22.0`)  
`--json` | Emit event NDJSON  
`--onboard` | Jalankan `openclaw onboard` setelah instalasi  
`--no-onboard` | Lewati onboarding (default)  
`--set-npm-prefix` | Di Linux, paksa prefiks npm ke `~/.npm-global` jika prefiks saat ini tidak dapat ditulis  
`--help` | Tampilkan penggunaan (`-h`)  
Environment variables reference Variabel | Deskripsi  
---|---  
`OPENCLAW_PREFIX=<path>` | Prefiks instalasi  
`OPENCLAW_INSTALL_METHOD=git|npm` | Metode instalasi  
`OPENCLAW_VERSION=<ver>` | Versi OpenClaw atau dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Versi Node  
`OPENCLAW_GIT_DIR=<path>` | Direktori checkout Git untuk instalasi git  
`OPENCLAW_GIT_UPDATE=0|1` | Aktifkan/nonaktifkan pembaruan git untuk checkout yang sudah ada  
`OPENCLAW_NO_ONBOARD=1` | Lewati orientasi awal  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Level log npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Kontrol perilaku sharp/libvips (default: `1`)  
  
* * *

## install.ps1

### Alur (install.ps1)

* ### Ensure PowerShell + Windows environment

Memerlukan PowerShell 5+.

* ### Ensure Node.js 24 by default

Jika tidak ada, mencoba instalasi melalui winget, lalu Chocolatey, lalu Scoop. Node 22 LTS, saat ini `22.16+`, tetap didukung untuk kompatibilitas.

* ### Install OpenClaw

  * Metode `npm` (default): instalasi npm global menggunakan `-Tag` yang dipilih, dijalankan dari direktori sementara penginstal yang dapat ditulis sehingga shell yang dibuka di folder terlindungi seperti `C:\` tetap berfungsi
  * Metode `git`: clone/perbarui repo, instal/build dengan pnpm, dan instal wrapper di `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Post-install tasks

  * Menambahkan direktori bin yang diperlukan ke PATH pengguna jika memungkinkan
  * Menyegarkan layanan gateway yang dimuat dengan upaya terbaik (`openclaw gateway install --force`, lalu restart)
  * Menjalankan `openclaw doctor --non-interactive` pada upgrade dan instalasi git (upaya terbaik)


* ### Handle failures

Instalasi `iwr ... | iex` dan scriptblock melaporkan error penghentian tanpa menutup sesi PowerShell saat ini. Instalasi langsung `powershell -File` / `pwsh -File` tetap keluar non-zero untuk otomatisasi.

### Contoh (install.ps1)

### Default

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Git install

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### GitHub main via npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Custom git directory

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Dry run

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Debug trace

powershellCopy code
[code]
    # install.ps1 belum memiliki flag -Verbose khusus.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Flags reference Flag | Deskripsi  
---|---  
`-InstallMethod npm|git` | Metode instalasi (default: `npm`)  
`-Tag <tag|version|spec>` | dist-tag, versi, atau spesifikasi paket npm (default: `latest`)  
`-GitDir <path>` | Direktori checkout (default: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Lewati orientasi awal  
`-NoGitUpdate` | Lewati `git pull`  
`-DryRun` | Cetak tindakan saja  
Environment variables reference Variabel | Deskripsi  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Metode instalasi  
`OPENCLAW_GIT_DIR=<path>` | Direktori checkout  
`OPENCLAW_NO_ONBOARD=1` | Lewati orientasi awal  
`OPENCLAW_GIT_UPDATE=0` | Nonaktifkan git pull  
`OPENCLAW_DRY_RUN=1` | Mode dry run  
  
* * *

## CI dan otomatisasi

Gunakan flag/variabel lingkungan non-interaktif untuk eksekusi yang dapat diprediksi.

### install.sh (non-interactive npm)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (non-interactive git)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (skip onboarding)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Pemecahan masalah

Why is Git required?

Git diperlukan untuk metode instalasi `git`. Untuk instalasi `npm`, Git tetap diperiksa/diinstal untuk menghindari kegagalan `spawn git ENOENT` saat dependensi menggunakan URL git.

Why does npm hit EACCES on Linux?

Beberapa setup Linux mengarahkan prefiks global npm ke path milik root. `install.sh` dapat mengalihkan prefiks ke `~/.npm-global` dan menambahkan ekspor PATH ke file rc shell (jika file tersebut ada).

sharp/libvips issues

Skrip menggunakan default `SHARP_IGNORE_GLOBAL_LIBVIPS=1` untuk menghindari sharp dibuild terhadap libvips sistem. Untuk menimpanya:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Instal Git for Windows, buka ulang PowerShell, jalankan ulang penginstal.

Windows: "openclaw is not recognized"

Jalankan `npm config get prefix` dan tambahkan direktori tersebut ke PATH pengguna Anda (tidak perlu sufiks `\bin` di Windows), lalu buka ulang PowerShell.

Windows: how to get verbose installer output

`install.ps1` saat ini tidak mengekspos switch `-Verbose`. Gunakan tracing PowerShell untuk diagnostik tingkat skrip:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw not found after install

Biasanya ini masalah PATH. Lihat [pemecahan masalah Node.js](</id/install/node#troubleshooting>).

## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Memperbarui](</id/install/updating>)
  * [Menghapus instalasi](</id/install/uninstall>)


Was this useful?YesNo