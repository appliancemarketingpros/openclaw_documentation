---
title: Copot pemasangan
source_url: https://docs.openclaw.ai/id/install/uninstall
scraped_at: 2026-05-25
---

Dua jalur:

  * **Jalur mudah** jika `openclaw` masih terinstal.
  * **Penghapusan layanan manual** jika CLI sudah hilang tetapi layanannya masih berjalan.


## Jalur mudah (CLI masih terinstal)

Direkomendasikan: gunakan uninstaller bawaan:

bashCopy code
[code]
    openclaw uninstall
[/code]

Non-interaktif (otomasi / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Langkah manual (hasilnya sama):

  1. Hentikan layanan gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Copot layanan gateway (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Hapus status + config:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Jika Anda menyetel `OPENCLAW_CONFIG_PATH` ke lokasi kustom di luar direktori status, hapus file itu juga.

  4. Hapus workspace Anda (opsional, menghapus file agen):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Hapus instalasi CLI (pilih yang Anda gunakan):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Jika Anda menginstal aplikasi macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Catatan:

  * Jika Anda menggunakan profile (`--profile` / `OPENCLAW_PROFILE`), ulangi langkah 3 untuk setiap direktori status (default-nya `~/.openclaw-<profile>`).
  * Dalam mode remote, direktori status berada di **host gateway** , jadi jalankan langkah 1-4 di sana juga.


## Penghapusan layanan manual (CLI tidak terinstal)

Gunakan ini jika layanan gateway tetap berjalan tetapi `openclaw` hilang.

### macOS (launchd)

Label default adalah `ai.openclaw.gateway` (atau `ai.openclaw.<profile>`; `com.openclaw.*` lama mungkin masih ada):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Jika Anda menggunakan profile, ganti label dan nama plist dengan `ai.openclaw.<profile>`. Hapus semua plist `com.openclaw.*` lama jika ada.

### Linux (unit pengguna systemd)

Nama unit default adalah `openclaw-gateway.service` (atau `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Scheduled Task)

Nama task default adalah `OpenClaw Gateway` (atau `OpenClaw Gateway (<profile>)`). Skrip task berada di bawah direktori status Anda.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Jika Anda menggunakan profile, hapus nama task yang cocok dan `~\.openclaw-<profile>\gateway.cmd`.

## Instalasi normal vs checkout source

### Instalasi normal ([install.sh](<http://install.sh>) / npm / pnpm / bun)

Jika Anda menggunakan `https://openclaw.ai/install.sh` atau `install.ps1`, CLI diinstal dengan `npm install -g openclaw@latest`. Hapus dengan `npm rm -g openclaw` (atau `pnpm remove -g` / `bun remove -g` jika Anda menginstalnya dengan cara itu).

### Checkout source (git clone)

Jika Anda menjalankan dari checkout repo (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Copot layanan gateway **sebelum** menghapus repo (gunakan jalur mudah di atas atau penghapusan layanan manual).
  2. Hapus direktori repo.
  3. Hapus status + workspace seperti ditunjukkan di atas.


## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Panduan migrasi](</id/install/migrating>)


Was this useful?YesNo