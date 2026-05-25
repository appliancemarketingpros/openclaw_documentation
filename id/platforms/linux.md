---
title: Aplikasi Linux
source_url: https://docs.openclaw.ai/id/platforms/linux
scraped_at: 2026-05-25
---

Gateway didukung sepenuhnya di Linux. **Node adalah runtime yang direkomendasikan**. Bun tidak direkomendasikan untuk Gateway (bug WhatsApp/Telegram).

Aplikasi pendamping Linux native direncanakan. Kontribusi dipersilakan jika Anda ingin membantu membuatnya.

## Jalur cepat pemula (VPS)

  1. Instal Node 24 (direkomendasikan; Node 22 LTS, saat ini `22.16+`, masih berfungsi untuk kompatibilitas)
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. Dari laptop Anda: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. Buka `http://127.0.0.1:18789/` dan autentikasi dengan rahasia bersama yang dikonfigurasi (token secara default; kata sandi jika Anda menetapkan `gateway.auth.mode: "password"`)


Panduan server Linux lengkap: [Server Linux](</id/vps>). Contoh VPS langkah demi langkah: [exe.dev](</id/install/exe-dev>)

## Instalasi

  * [Memulai](</id/start/getting-started>)
  * [Instalasi & pembaruan](</id/install/updating>)
  * Alur opsional: [Bun (eksperimental)](</id/install/bun>), [Nix](</id/install/nix>), [Docker](</id/install/docker>)


## Gateway

  * [Runbook Gateway](</id/gateway>)
  * [Konfigurasi](</id/gateway/configuration>)


## Instalasi layanan Gateway (CLI)

Gunakan salah satu dari ini:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Atau:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Atau:

CodeCopy code
[code]
    openclaw configure
[/code]

Pilih **Layanan Gateway** saat diminta.

Perbaiki/migrasikan:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Kontrol sistem (unit pengguna systemd)

OpenClaw menginstal layanan **pengguna** systemd secara default. Gunakan layanan **sistem** untuk server bersama atau yang selalu aktif. `openclaw gateway install` dan `openclaw onboard --install-daemon` sudah merender unit kanonis saat ini untuk Anda; tulis secara manual hanya saat Anda membutuhkan pengaturan sistem/manajer-layanan khusus. Panduan layanan lengkap tersedia di [runbook Gateway](</id/gateway>).

Pengaturan minimal:

Buat `~/.config/systemd/user/openclaw-gateway[-<profile>].service`:

CodeCopy code
[code]
    [Unit]Description=OpenClaw Gateway (profile: <profile>, v<version>)After=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

Aktifkan:

CodeCopy code
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
[/code]

## Tekanan memori dan penghentian OOM

Di Linux, kernel memilih korban OOM saat cgroup host, VM, atau kontainer kehabisan memori. Gateway bisa menjadi korban yang buruk karena memiliki sesi berumur panjang dan koneksi kanal. Karena itu OpenClaw mengarahkan proses anak sementara agar dihentikan sebelum Gateway jika memungkinkan.

Untuk spawn proses anak Linux yang memenuhi syarat, OpenClaw memulai anak melalui wrapper `/bin/sh` singkat yang menaikkan `oom_score_adj` milik anak menjadi `1000`, lalu menjalankan perintah sebenarnya dengan `exec`. Ini adalah operasi tanpa hak istimewa karena anak hanya meningkatkan kemungkinan penghentian OOM untuk dirinya sendiri.

Permukaan proses anak yang tercakup meliputi:

  * proses anak perintah yang dikelola supervisor,
  * proses anak shell PTY,
  * proses anak server stdio MCP,
  * proses browser/Chrome yang diluncurkan OpenClaw.


Wrapper hanya untuk Linux dan dilewati saat `/bin/sh` tidak tersedia. Ini juga dilewati jika env anak menetapkan `OPENCLAW_CHILD_OOM_SCORE_ADJ=0`, `false`, `no`, atau `off`.

Untuk memverifikasi proses anak:

bashCopy code
[code]
    cat /proc/<child-pid>/oom_score_adj
[/code]

Nilai yang diharapkan untuk anak yang tercakup adalah `1000`. Proses Gateway harus mempertahankan skor normalnya, biasanya `0`.

Ini tidak menggantikan penyesuaian memori normal. Jika VPS atau kontainer berulang kali menghentikan anak, tingkatkan batas memori, kurangi konkurensi, atau tambahkan kontrol sumber daya yang lebih kuat seperti `MemoryMax=` systemd atau batas memori tingkat kontainer.

## Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [Server Linux](</id/vps>)
  * [Raspberry Pi](</id/install/raspberry-pi>)


Was this useful?YesNo