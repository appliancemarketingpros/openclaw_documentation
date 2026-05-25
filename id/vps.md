---
title: Server Linux
source_url: https://docs.openclaw.ai/id/vps
scraped_at: 2026-05-25
---

Jalankan OpenClaw Gateway di server Linux atau VPS cloud mana pun. Halaman ini membantu Anda memilih penyedia, menjelaskan cara kerja deployment cloud, dan membahas penyetelan Linux generik yang berlaku di mana saja.

## Pilih penyedia

[**Railway** [**Northflank** [**DigitalOcean** [**Oracle Cloud** [**Fly.io** [**Hetzner** [**Hostinger** [**GCP** [**Azure** [**exe.dev** [**Raspberry Pi** **AWS (EC2 / Lightsail / tingkat gratis)** juga berfungsi dengan baik. Panduan video dari komunitas tersedia di [x.com/techfrenAJ/status/2014934471095812547](<https://x.com/techfrenAJ/status/2014934471095812547>) (sumber daya komunitas -- mungkin menjadi tidak tersedia). Cara kerja penyiapan cloud

  * **Gateway berjalan di VPS** dan memiliki status + ruang kerja.
  * Anda terhubung dari laptop atau ponsel melalui **UI Kontrol** atau **Tailscale/SSH**.
  * Perlakukan VPS sebagai sumber kebenaran dan **cadangkan** status + ruang kerja secara teratur.
  * Default yang aman: pertahankan Gateway di loopback dan akses melalui tunnel SSH atau Tailscale Serve. Jika Anda mengikat ke `lan` atau `tailnet`, wajibkan `gateway.auth.token` atau `gateway.auth.password`.

Halaman terkait: [Akses jarak jauh Gateway](</id/gateway/remote>), [Hub platform](</id/platforms>). Perkuat akses admin terlebih dahulu Sebelum menginstal OpenClaw di VPS publik, tentukan cara Anda ingin mengelola mesin itu sendiri.

  * Jika Anda ingin akses admin hanya melalui Tailnet, instal Tailscale terlebih dahulu, gabungkan VPS ke tailnet Anda, verifikasi sesi SSH kedua melalui IP Tailscale atau nama MagicDNS, lalu batasi SSH publik.
  * Jika Anda tidak menggunakan Tailscale, terapkan penguatan yang setara untuk jalur SSH Anda sebelum mengekspos layanan tambahan.
  * Ini terpisah dari akses Gateway. Anda masih dapat mempertahankan OpenClaw tetap terikat ke loopback dan menggunakan tunnel SSH atau Tailscale Serve untuk dasbor.

Opsi Gateway khusus Tailscale tersedia di [Tailscale](</id/gateway/tailscale>). Agen perusahaan bersama di VPS Menjalankan satu agen untuk tim adalah penyiapan yang valid ketika setiap pengguna berada dalam batas kepercayaan yang sama dan agen hanya digunakan untuk bisnis.

  * Pertahankan pada runtime khusus (VPS/VM/container + pengguna/akun OS khusus).
  * Jangan masuk ke runtime tersebut dengan akun Apple/Google pribadi atau profil browser/pengelola kata sandi pribadi.
  * Jika pengguna saling bermusuhan, pisahkan berdasarkan gateway/host/pengguna OS.

Detail model keamanan: [Keamanan](</id/gateway/security>). Menggunakan node dengan VPS Anda dapat mempertahankan Gateway di cloud dan memasangkan **node** di perangkat lokal Anda (Mac/iOS/Android/tanpa antarmuka grafis). Node menyediakan kemampuan layar/kamera/canvas lokal dan `system.run` sementara Gateway tetap berada di cloud. Dokumentasi: [Node](</id/nodes>), [CLI Node](</id/cli/nodes>). Penyetelan startup untuk VM kecil dan host ARM Jika perintah CLI terasa lambat pada VM berdaya rendah (atau host ARM), aktifkan cache kompilasi modul Node: bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF'export NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

  * `NODE_COMPILE_CACHE` meningkatkan waktu startup perintah berulang.
  * `OPENCLAW_NO_RESPAWN=1` menghindari overhead startup tambahan dari jalur respawn mandiri.
  * Eksekusi perintah pertama menghangatkan cache; eksekusi berikutnya lebih cepat.
  * Untuk detail khusus Raspberry Pi, lihat [Raspberry Pi](</id/install/raspberry-pi>).

Daftar periksa penyetelan systemd (opsional) Untuk host VM yang menggunakan `systemd`, pertimbangkan:

  * Tambahkan env layanan untuk jalur startup yang stabil: 
    * `OPENCLAW_NO_RESPAWN=1`
    * `NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache`
  * Pertahankan perilaku restart tetap eksplisit: 
    * `Restart=always`
    * `RestartSec=2`
    * `TimeoutStartSec=90`
  * Utamakan disk berbasis SSD untuk jalur status/cache guna mengurangi penalti cold-start I/O acak.

Untuk jalur standar `openclaw onboard --install-daemon`, edit unit pengguna: bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Jika Anda sengaja menginstal unit sistem sebagai gantinya, edit `openclaw-gateway.service` melalui `sudo systemctl edit openclaw-gateway.service`. Cara kebijakan `Restart=` membantu pemulihan otomatis: [systemd dapat mengotomatiskan pemulihan layanan](<https://www.redhat.com/en/blog/systemd-automate-recovery>). Untuk perilaku OOM Linux, pemilihan korban proses anak, dan diagnostik `exit 137`, lihat [tekanan memori Linux dan OOM kill](</id/platforms/linux#memory-pressure-and-oom-kills>). Terkait

  * [Ikhtisar instalasi](</id/install>)
  * [DigitalOcean](</id/install/digitalocean>)
  * [Fly.io](</id/install/fly>)
  * [Hetzner](</id/install/hetzner>)

](</id/install/raspberry-pi>) Was this useful?YesNo ](</id/install/exe-dev>)](</id/install/azure>)](</id/install/gcp>)](</id/install/hostinger>)](</id/install/hetzner>)](</id/install/fly>)](</id/install/oracle>)](</id/install/digitalocean>)](</id/install/northflank>)](</id/install/railway>)