---
title: Instal
source_url: https://docs.openclaw.ai/id/install
scraped_at: 2026-05-25
---

## Persyaratan sistem

  * **Node 24** (direkomendasikan) atau Node 22.16+ - skrip penginstal menanganinya secara otomatis
  * **macOS, Linux, atau Windows** \- Windows native dan WSL2 didukung; WSL2 lebih stabil. Lihat [Windows](</id/platforms/windows>).
  * `pnpm` hanya diperlukan jika Anda membangun dari sumber


## Direkomendasikan: skrip penginstal

Cara tercepat untuk menginstal. Skrip ini mendeteksi OS Anda, menginstal Node jika diperlukan, menginstal OpenClaw, dan menjalankan onboarding.

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

Untuk menginstal tanpa menjalankan onboarding:

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

Untuk semua flag dan opsi CI/otomasi, lihat [Internal penginstal](</id/install/installer>).

## Metode instalasi alternatif

### Penginstal prefiks lokal (`install-cli.sh`)

Gunakan ini saat Anda ingin OpenClaw dan Node disimpan di bawah prefiks lokal seperti `~/.openclaw`, tanpa bergantung pada instalasi Node tingkat sistem:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Penginstal ini mendukung instalasi npm secara default, ditambah instalasi git-checkout di bawah alur prefiks yang sama. Referensi lengkap: [Internal penginstal](</id/install/installer#install-clish>).

Sudah terinstal? Beralih antara instalasi paket dan git dengan `openclaw update --channel dev` dan `openclaw update --channel stable`. Lihat [Memperbarui](</id/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm, atau bun

Jika Anda sudah mengelola Node sendiri:

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

Pemecahan masalah: kesalahan build sharp (npm)

Jika `sharp` gagal karena libvips yang terinstal secara global:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### Dari sumber

Untuk kontributor atau siapa pun yang ingin menjalankan dari checkout lokal:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Atau lewati link dan gunakan `pnpm openclaw ...` dari dalam repo. Lihat [Penyiapan](</id/start/setup>) untuk alur kerja pengembangan lengkap.

### Instal dari GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Container dan manajer paket

[**Docker** Deployment ter-container atau headless. ](</id/install/docker>) [**Podman** Alternatif container rootless untuk Docker. ](</id/install/podman>) [**Nix** Instalasi deklaratif melalui Nix flake. ](</id/install/nix>) [**Ansible** Penyediaan fleet otomatis. ](</id/install/ansible>) [**Bun** Penggunaan hanya CLI melalui runtime Bun. ](</id/install/bun>)

## Verifikasi instalasi

bashCopy code
[code]
    openclaw --version      # konfirmasi CLI tersediaopenclaw doctor         # periksa masalah konfigurasiopenclaw gateway status # verifikasi Gateway berjalan
[/code]

Jika Anda ingin startup terkelola setelah instalasi:

  * macOS: LaunchAgent melalui `openclaw onboard --install-daemon` atau `openclaw gateway install`
  * Linux/WSL2: layanan pengguna systemd melalui perintah yang sama
  * Windows native: Scheduled Task terlebih dahulu, dengan fallback item login folder Startup per pengguna jika pembuatan tugas ditolak


## Hosting dan deployment

Deploy OpenClaw di server cloud atau VPS:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9pZC9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Perbarui, migrasikan, atau hapus instalasi [**Memperbarui** Jaga OpenClaw tetap terbaru. ](</id/install/updating>) [**Bermigrasi** Pindah ke mesin baru. ](</id/install/migrating>) [**Hapus instalasi** Hapus OpenClaw sepenuhnya. ](</id/install/uninstall>) Pemecahan masalah: `openclaw` tidak ditemukan Jika instalasi berhasil tetapi `openclaw` tidak ditemukan di terminal Anda: bashCopy code
[code]
    node -v           # Node terinstal?npm prefix -g     # Di mana paket global berada?echo "$PATH"      # Apakah direktori bin global ada di PATH?
[/code]

Jika `$(npm prefix -g)/bin` tidak ada di `$PATH` Anda, tambahkan ke file startup shell Anda (`~/.zshrc` atau `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Lalu buka terminal baru. Lihat [Penyiapan Node](</id/install/node>) untuk detail lebih lanjut. ](</id/install/northflank>) Was this useful?YesNo ](</id/install/render>)](</id/install/railway>)](</id/install/azure>)](</id/install/gcp>)](</id/install/hetzner>)](</id/install/kubernetes>)](</id/install/docker-vm-runtime>)](</id/vps>)