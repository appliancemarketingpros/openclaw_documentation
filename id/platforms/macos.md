---
title: Aplikasi macOS
source_url: https://docs.openclaw.ai/id/platforms/macos
scraped_at: 2026-05-25
---

Aplikasi macOS adalah **pendamping bilah menu** untuk OpenClaw. Aplikasi ini menangani izin, mengelola/menautkan ke Gateway secara lokal (launchd atau manual), dan mengekspos kemampuan macOS ke agen sebagai Node.

## Apa yang dilakukannya

  * Menampilkan notifikasi native dan status di bilah menu.
  * Menangani prompt TCC (Notifications, Accessibility, Screen Recording, Microphone, Speech Recognition, Automation/AppleScript).
  * Menjalankan atau terhubung ke Gateway (lokal atau jarak jauh).
  * Mengekspos alat khusus macOS (Canvas, Camera, Screen Recording, `system.run`).
  * Memulai layanan host Node lokal dalam mode **jarak jauh** (launchd), dan menghentikannya dalam mode **lokal**.
  * Secara opsional menghosting **PeekabooBridge** untuk automasi UI.
  * Menginstal CLI global (`openclaw`) atas permintaan melalui npm, pnpm, atau bun (aplikasi lebih memilih npm, lalu pnpm, lalu bun; Node tetap menjadi runtime Gateway yang direkomendasikan).


## Mode lokal vs jarak jauh

  * **Lokal** (default): aplikasi menautkan ke Gateway lokal yang sedang berjalan jika ada; jika tidak, aplikasi mengaktifkan layanan launchd melalui `openclaw gateway install`.
  * **Jarak jauh** : aplikasi terhubung ke Gateway melalui SSH/Tailscale dan tidak pernah memulai proses lokal. Aplikasi memulai **layanan host Node** lokal agar Gateway jarak jauh dapat menjangkau Mac ini. Aplikasi tidak menjalankan Gateway sebagai proses turunan. Penemuan Gateway sekarang lebih memilih nama Tailscale MagicDNS daripada IP tailnet mentah, sehingga aplikasi Mac pulih lebih andal ketika IP tailnet berubah.


## Kontrol launchd

Aplikasi mengelola LaunchAgent per pengguna berlabel `ai.openclaw.gateway` (atau `ai.openclaw.<profile>` saat menggunakan `--profile`/`OPENCLAW_PROFILE`; `com.openclaw.*` lama tetap di-unload).

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.gatewaylaunchctl bootout gui/$UID/ai.openclaw.gateway
[/code]

Ganti label dengan `ai.openclaw.<profile>` saat menjalankan profil bernama.

Jika LaunchAgent belum diinstal, aktifkan dari aplikasi atau jalankan `openclaw gateway install`.

## Kemampuan Node (mac)

Aplikasi macOS menampilkan dirinya sebagai Node. Perintah umum:

  * Canvas: `canvas.present`, `canvas.navigate`, `canvas.eval`, `canvas.snapshot`, `canvas.a2ui.*`
  * Camera: `camera.snap`, `camera.clip`
  * Screen: `screen.snapshot`, `screen.record`
  * System: `system.run`, `system.notify`


Node melaporkan peta `permissions` sehingga agen dapat memutuskan apa yang diizinkan.

Layanan Node + IPC aplikasi:

  * Saat layanan host Node headless berjalan (mode jarak jauh), layanan tersebut terhubung ke Gateway WS sebagai Node.
  * `system.run` dieksekusi di aplikasi macOS (konteks UI/TCC) melalui soket Unix lokal; prompt + output tetap berada di dalam aplikasi.


Diagram (SCI):

CodeCopy code
[code]
    Gateway -> Node Service (WS)                 |  IPC (UDS + token + HMAC + TTL)                 v             Mac App (UI + TCC + system.run)
[/code]

## Persetujuan eksekusi (system.run)

`system.run` dikendalikan oleh **persetujuan eksekusi** di aplikasi macOS (Settings → Exec approvals). Keamanan + tanya + allowlist disimpan secara lokal di Mac dalam:

CodeCopy code
[code]
    ~/.openclaw/exec-approvals.json
[/code]

Contoh:

jsonCopy code
[code]
    {  "version": 1,  "defaults": {    "security": "deny",    "ask": "on-miss"  },  "agents": {    "main": {      "security": "allowlist",      "ask": "on-miss",      "allowlist": [{ "pattern": "/opt/homebrew/bin/rg" }]    }  }}
[/code]

Catatan:

  * Entri `allowlist` adalah pola glob untuk jalur biner yang telah di-resolve, atau nama perintah polos untuk perintah yang dipanggil melalui PATH.
  * Teks perintah shell mentah yang berisi sintaks kontrol atau ekspansi shell (`&&`, `||`, `;`, `|`, ```, `$`, `<`, `>`, `(`, `)`) diperlakukan sebagai allowlist miss dan memerlukan persetujuan eksplisit (atau memasukkan biner shell ke allowlist).
  * Memilih "Always Allow" di prompt menambahkan perintah tersebut ke allowlist.
  * Override environment `system.run` difilter (membuang `PATH`, `DYLD_*`, `LD_*`, `NODE_OPTIONS`, `PYTHON*`, `PERL*`, `RUBYOPT`, `SHELLOPTS`, `PS4`) lalu digabungkan dengan environment aplikasi.
  * Untuk pembungkus shell (`bash|sh|zsh ... -c/-lc`), override environment berskala permintaan dikurangi menjadi allowlist eksplisit kecil (`TERM`, `LANG`, `LC_*`, `COLORTERM`, `NO_COLOR`, `FORCE_COLOR`).
  * Untuk keputusan selalu-izinkan dalam mode allowlist, pembungkus dispatch yang dikenal (`env`, `nice`, `nohup`, `stdbuf`, `timeout`) menyimpan jalur executable internal, bukan jalur pembungkus. Jika pembukaan pembungkus tidak aman, tidak ada entri allowlist yang disimpan otomatis.


## Deep link

Aplikasi mendaftarkan skema URL `openclaw://` untuk tindakan lokal.

### `openclaw://agent`

Memicu permintaan `agent` Gateway. **OC_I18N_900004** Parameter kueri:

  * `message` (wajib)
  * `sessionKey` (opsional)
  * `thinking` (opsional)
  * `deliver` / `to` / `channel` (opsional)
  * `timeoutSeconds` (opsional)
  * `key` (kunci mode tanpa pengawasan opsional)


Keamanan:

  * Tanpa `key`, aplikasi meminta konfirmasi.
  * Tanpa `key`, aplikasi memberlakukan batas pesan pendek untuk prompt konfirmasi dan mengabaikan `deliver` / `to` / `channel`.
  * Dengan `key` yang valid, proses berjalan tanpa pengawasan (ditujukan untuk automasi pribadi).


## Alur onboarding (umum)

  1. Instal dan jalankan **OpenClaw.app**.
  2. Selesaikan checklist izin (prompt TCC).
  3. Pastikan mode **Lokal** aktif dan Gateway berjalan.
  4. Instal CLI jika Anda ingin akses terminal.


## Penempatan direktori state (macOS)

Hindari menaruh direktori state OpenClaw Anda di iCloud atau folder lain yang disinkronkan ke cloud. Jalur yang didukung sinkronisasi dapat menambah latensi dan kadang menyebabkan race file-lock/sinkronisasi untuk sesi dan kredensial.

Lebih pilih jalur state lokal yang tidak disinkronkan seperti: **OC_I18N_900005** Jika `openclaw doctor` mendeteksi state di bawah:

  * `~/Library/Mobile Documents/com~apple~CloudDocs/...`
  * `~/Library/CloudStorage/...`


perintah tersebut akan memperingatkan dan merekomendasikan pemindahan kembali ke jalur lokal.

## Alur kerja build dan dev (native)

  * `cd apps/macos && swift build`
  * `swift run OpenClaw` (atau Xcode)
  * Paketkan aplikasi: `scripts/package-mac-app.sh`


## Debug konektivitas Gateway (CLI macOS)

Gunakan CLI debug untuk menjalankan handshake dan logika penemuan Gateway WebSocket yang sama seperti yang digunakan aplikasi macOS, tanpa menjalankan aplikasi. **OC_I18N_900006** Opsi connect:

  * `--url <ws://host:port>`: override konfigurasi
  * `--mode <local|remote>`: resolve dari konfigurasi (default: konfigurasi atau lokal)
  * `--probe`: paksa health probe baru
  * `--timeout <ms>`: timeout permintaan (default: `15000`)
  * `--json`: output terstruktur untuk diffing


Opsi discovery:

  * `--include-local`: sertakan gateway yang akan difilter sebagai "local"
  * `--timeout <ms>`: jendela penemuan keseluruhan (default: `2000`)
  * `--json`: output terstruktur untuk diffing


## Plumbing koneksi jarak jauh (tunnel SSH)

Saat aplikasi macOS berjalan dalam mode **Jarak jauh** , aplikasi membuka tunnel SSH agar komponen UI lokal dapat berbicara dengan Gateway jarak jauh seolah-olah berada di localhost.

### Tunnel kontrol (port Gateway WebSocket)

  * **Tujuan:** health check, status, Web Chat, konfigurasi, dan panggilan control-plane lainnya.
  * **Port lokal:** port Gateway (default `18789`), selalu stabil.
  * **Port jarak jauh:** port Gateway yang sama di host jarak jauh.
  * **Perilaku:** tidak ada port lokal acak; aplikasi menggunakan kembali tunnel sehat yang ada atau memulainya ulang jika diperlukan.
  * **Bentuk SSH:** `ssh -N -L <local>:127.0.0.1:<remote>` dengan BatchMode + ExitOnForwardFailure + opsi keepalive.
  * **Pelaporan IP:** tunnel SSH menggunakan loopback, sehingga gateway akan melihat IP Node sebagai `127.0.0.1`. Gunakan transport **Direct (ws/wss)** jika Anda ingin IP klien asli muncul (lihat [akses jarak jauh macOS](</id/platforms/mac/remote>)).


Untuk langkah penyiapan, lihat [akses jarak jauh macOS](</id/platforms/mac/remote>). Untuk detail protokol, lihat [Protokol Gateway](</id/gateway/protocol>).

## Dokumen terkait

  * [Runbook Gateway](</id/gateway>)
  * [Gateway (macOS)](</id/platforms/mac/bundled-gateway>)
  * [Izin macOS](</id/platforms/mac/permissions>)
  * [Canvas](</id/platforms/mac/canvas>)


Was this useful?YesNo