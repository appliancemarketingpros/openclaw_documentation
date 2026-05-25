---
title: Panduan operasional Gateway
source_url: https://docs.openclaw.ai/id/gateway
scraped_at: 2026-05-25
---

Gunakan halaman ini untuk startup hari ke-1 dan operasi hari ke-2 layanan Gateway.

[**Pemecahan masalah mendalam** Diagnostik berbasis gejala dengan tangga perintah persis dan tanda tangan log. ](</id/gateway/troubleshooting>) [**Konfigurasi** Panduan penyiapan berorientasi tugas + referensi konfigurasi lengkap. ](</id/gateway/configuration>) [**Manajemen secret** Kontrak SecretRef, perilaku snapshot runtime, dan operasi migrasi/muat ulang. ](</id/gateway/secrets>) [**Kontrak rencana secret** Aturan target/jalur `secrets apply` yang persis dan perilaku profil autentikasi hanya-ref. ](</id/gateway/secrets-plan-contract>)

## Startup lokal 5 menit

* ### Mulai Gateway

bashCopy code
[code]
    openclaw gateway --port 18789# debug/trace dicerminkan ke stdioopenclaw gateway --port 18789 --verbose# hentikan paksa listener pada port yang dipilih, lalu mulaiopenclaw gateway --force
[/code]

* ### Verifikasi kesehatan layanan

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --follow
[/code]

Baseline sehat: `Runtime: running`, `Connectivity probe: ok`, dan `Capability: ...` yang sesuai dengan harapan Anda. Gunakan `openclaw gateway status --require-rpc` saat Anda membutuhkan bukti RPC cakupan-baca, bukan hanya keterjangkauan.

* ### Validasi kesiapan channel

bashCopy code
[code]
    openclaw channels status --probe
[/code]

Dengan gateway yang dapat dijangkau, ini menjalankan probe channel per akun secara live dan audit opsional. Jika gateway tidak dapat dijangkau, CLI kembali ke ringkasan channel khusus konfigurasi alih-alih output probe live.

## Model runtime

  * Satu proses selalu aktif untuk routing, control plane, dan koneksi channel.
  * Satu port multipleks untuk: 
    * Kontrol/RPC WebSocket
    * API HTTP, kompatibel OpenAI (`/v1/models`, `/v1/embeddings`, `/v1/chat/completions`, `/v1/responses`, `/tools/invoke`)
    * UI kontrol dan hook
  * Mode bind default: `loopback`.
  * Autentikasi diwajibkan secara default. Penyiapan shared-secret menggunakan `gateway.auth.token` / `gateway.auth.password` (atau `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`), dan penyiapan reverse-proxy non-loopback dapat menggunakan `gateway.auth.mode: "trusted-proxy"`.


## Endpoint kompatibel OpenAI

Permukaan kompatibilitas OpenClaw dengan dampak tertinggi sekarang adalah:

  * `GET /v1/models`
  * `GET /v1/models/{id}`
  * `POST /v1/embeddings`
  * `POST /v1/chat/completions`
  * `POST /v1/responses`


Mengapa rangkaian ini penting:

  * Sebagian besar integrasi Open WebUI, LobeChat, dan LibreChat mem-probe `/v1/models` terlebih dahulu.
  * Banyak pipeline RAG dan memori mengharapkan `/v1/embeddings`.
  * Klien agent-native semakin memilih `/v1/responses`.


Catatan perencanaan:

  * `/v1/models` mengutamakan agen: endpoint ini mengembalikan `openclaw`, `openclaw/default`, dan `openclaw/<agentId>`.
  * `openclaw/default` adalah alias stabil yang selalu dipetakan ke agen default yang dikonfigurasi.
  * Gunakan `x-openclaw-model` saat Anda menginginkan override provider/model backend; jika tidak, model normal dan penyiapan embedding agen yang dipilih tetap memegang kendali.


Semua ini berjalan pada port Gateway utama dan menggunakan batas autentikasi operator tepercaya yang sama seperti API HTTP Gateway lainnya.

### Prioritas port dan bind

Pengaturan | Urutan resolusi  
---|---  
Port Gateway | `--port` → `OPENCLAW_GATEWAY_PORT` → `gateway.port` → `18789`  
Mode bind | CLI/override → `gateway.bind` → `loopback`  
  
Layanan gateway yang diinstal mencatat `--port` yang diselesaikan dalam metadata supervisor. Setelah mengubah `gateway.port`, jalankan `openclaw doctor --fix` atau `openclaw gateway install --force` agar launchd/systemd/schtasks memulai proses pada port baru.

Startup Gateway menggunakan port dan bind efektif yang sama saat menyemai origin UI Kontrol lokal untuk bind non-loopback. Misalnya, `--bind lan --port 3000` menyemai `http://localhost:3000` dan `http://127.0.0.1:3000` sebelum validasi runtime berjalan. Tambahkan origin browser jarak jauh apa pun, seperti URL proxy HTTPS, ke `gateway.controlUi.allowedOrigins` secara eksplisit.

### Mode hot reload

`gateway.reload.mode` | Perilaku  
---|---  
`off` | Tidak ada muat ulang konfigurasi  
`hot` | Terapkan hanya perubahan yang aman-hot  
`restart` | Mulai ulang pada perubahan yang perlu restart  
`hybrid` (default) | Terapkan-hot saat aman, restart saat wajib  
  
## Kumpulan perintah operator

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --deep   # menambahkan pemindaian layanan tingkat sistemopenclaw gateway status --jsonopenclaw gateway installopenclaw gateway restartopenclaw gateway stopopenclaw secrets reloadopenclaw logs --followopenclaw doctor
[/code]

`gateway status --deep` adalah untuk penemuan layanan tambahan (LaunchDaemons/unit sistem systemd/schtasks), bukan probe kesehatan RPC yang lebih mendalam.

## Beberapa gateway (host yang sama)

Sebagian besar instalasi sebaiknya menjalankan satu gateway per mesin. Satu gateway dapat menampung beberapa agen dan channel.

Anda hanya membutuhkan beberapa gateway saat sengaja menginginkan isolasi atau bot penyelamat.

Pemeriksaan berguna:

bashCopy code
[code]
    openclaw gateway status --deepopenclaw gateway probe
[/code]

Yang perlu diharapkan:

  * `gateway status --deep` dapat melaporkan `Other gateway-like services detected (best effort)` dan mencetak petunjuk pembersihan saat instalasi launchd/systemd/schtasks yang usang masih ada.
  * `gateway probe` dapat memperingatkan tentang `multiple reachable gateways` saat lebih dari satu target menjawab.
  * Jika itu disengaja, isolasikan port, konfigurasi/state, dan root workspace per gateway.


Checklist per instans:

  * `gateway.port` unik
  * `OPENCLAW_CONFIG_PATH` unik
  * `OPENCLAW_STATE_DIR` unik
  * `agents.defaults.workspace` unik


Contoh:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/a.json OPENCLAW_STATE_DIR=~/.openclaw-a openclaw gateway --port 19001OPENCLAW_CONFIG_PATH=~/.openclaw/b.json OPENCLAW_STATE_DIR=~/.openclaw-b openclaw gateway --port 19002
[/code]

Penyiapan terperinci: [/gateway/multiple-gateways](</id/gateway/multiple-gateways>).

## Akses jarak jauh

Disarankan: Tailscale/VPN. Fallback: tunnel SSH.

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

Lalu hubungkan klien secara lokal ke `ws://127.0.0.1:18789`.

Lihat: [Gateway Jarak Jauh](</id/gateway/remote>), [Autentikasi](</id/gateway/authentication>), [Tailscale](</id/gateway/tailscale>).

## Supervisi dan siklus hidup layanan

Gunakan run yang diawasi untuk reliabilitas seperti produksi.

### macOS (launchd)

bashCopy code
[code]
    openclaw gateway installopenclaw gateway statusopenclaw gateway restartopenclaw gateway stop
[/code]

Gunakan `openclaw gateway restart` untuk restart. Jangan rangkai `openclaw gateway stop` dan `openclaw gateway start` sebagai pengganti restart.

Di macOS, `gateway stop` menggunakan `launchctl bootout` secara default — ini menghapus LaunchAgent dari sesi boot saat ini tanpa menyimpan status nonaktif, sehingga pemulihan otomatis KeepAlive tetap berfungsi setelah crash tak terduga dan `gateway start` mengaktifkan ulang dengan bersih. Untuk menekan auto-respawn secara persisten lintas reboot, berikan `--disable`: `openclaw gateway stop --disable`.

Label LaunchAgent adalah `ai.openclaw.gateway` (default) atau `ai.openclaw.<profile>` (profil bernama). `openclaw doctor` mengaudit dan memperbaiki drift konfigurasi layanan.

### Linux (pengguna systemd)

bashCopy code
[code]
    openclaw gateway installsystemctl --user enable --now openclaw-gateway[-<profile>].serviceopenclaw gateway status
[/code]

Untuk persistensi setelah logout, aktifkan lingering:

bashCopy code
[code]
    sudo loginctl enable-linger <user>
[/code]

Contoh user-unit manual saat Anda membutuhkan jalur instalasi kustom:

iniCopy code
[code]
    [Unit]Description=OpenClaw GatewayAfter=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

### Windows (native)

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --jsonopenclaw gateway restartopenclaw gateway stop
[/code]

Startup terkelola native Windows menggunakan Scheduled Task bernama `OpenClaw Gateway` (atau `OpenClaw Gateway (<profile>)` untuk profil bernama). Jika pembuatan Scheduled Task ditolak, OpenClaw fallback ke launcher Startup-folder per pengguna yang menunjuk ke `gateway.cmd` di dalam direktori state.

### Linux (layanan sistem)

Gunakan unit sistem untuk host multipengguna/selalu aktif.

bashCopy code
[code]
    sudo systemctl daemon-reloadsudo systemctl enable --now openclaw-gateway[-<profile>].service
[/code]

Gunakan body layanan yang sama seperti unit pengguna, tetapi instal di bawah `/etc/systemd/system/openclaw-gateway[-<profile>].service` dan sesuaikan `ExecStart=` jika biner `openclaw` Anda berada di tempat lain.

Jangan juga membiarkan `openclaw doctor --fix` menginstal layanan gateway tingkat pengguna untuk profil/port yang sama. Doctor menolak instalasi otomatis itu saat menemukan layanan gateway OpenClaw tingkat sistem; gunakan `OPENCLAW_SERVICE_REPAIR_POLICY=external` saat unit sistem memiliki siklus hidup.

## Jalur cepat profil dev

bashCopy code
[code]
    openclaw --dev setupopenclaw --dev gateway --allow-unconfiguredopenclaw --dev status
[/code]

Default mencakup state/konfigurasi terisolasi dan port gateway dasar `19001`.

## Referensi cepat protokol (tampilan operator)

  * Frame klien pertama harus berupa `connect`.
  * Gateway mengembalikan snapshot `hello-ok` (`presence`, `health`, `stateVersion`, `uptimeMs`, batas/kebijakan).
  * `hello-ok.features.methods` / `events` adalah daftar penemuan konservatif, bukan dump yang dihasilkan dari setiap rute helper yang dapat dipanggil.
  * Permintaan: `req(method, params)` → `res(ok/payload|error)`.
  * Event umum mencakup `connect.challenge`, `agent`, `chat`, `session.message`, `session.tool`, `sessions.changed`, `presence`, `tick`, `health`, `heartbeat`, event siklus hidup pairing/approval, dan `shutdown`.


Run agen terdiri dari dua tahap:

  1. Ack diterima segera (`status:"accepted"`)
  2. Respons penyelesaian final (`status:"ok"|"error"`), dengan event `agent` yang di-stream di antaranya.


Lihat dokumen protokol lengkap: [Protokol Gateway](</id/gateway/protocol>).

## Pemeriksaan operasional

### Liveness

  * Buka WS dan kirim `connect`.
  * Harapkan respons `hello-ok` dengan snapshot.


### Readiness

bashCopy code
[code]
    openclaw gateway statusopenclaw channels status --probeopenclaw health
[/code]

### Pemulihan gap

Event tidak diputar ulang. Pada gap urutan, segarkan state (`health`, `system-presence`) sebelum melanjutkan.

## Tanda tangan kegagalan umum

Pola | Kemungkinan masalah  
---|---  
`refusing to bind gateway ... without auth` | Bind non-loopback tanpa jalur autentikasi gateway yang valid  
`another gateway instance is already listening` / `EADDRINUSE` | Konflik port  
`Gateway start blocked: set gateway.mode=local` | Config disetel ke mode jarak jauh, atau stempel mode lokal hilang dari config yang rusak  
`unauthorized` during connect | Ketidakcocokan autentikasi antara klien dan gateway  
  
Untuk tangga diagnosis lengkap, gunakan [Pemecahan Masalah Gateway](</id/gateway/troubleshooting>).

## Jaminan keamanan

  * Klien protokol Gateway gagal cepat saat Gateway tidak tersedia (tanpa fallback saluran langsung implisit).
  * Frame pertama yang tidak valid/tidak tersambung ditolak dan ditutup.
  * Shutdown yang anggun memancarkan event `shutdown` sebelum socket ditutup.


* * *

Terkait:

  * [Pemecahan Masalah](</id/gateway/troubleshooting>)
  * [Proses Latar Belakang](</id/gateway/background-process>)
  * [Konfigurasi](</id/gateway/configuration>)
  * [Kesehatan](</id/gateway/health>)
  * [Doctor](</id/gateway/doctor>)
  * [Autentikasi](</id/gateway/authentication>)


## Terkait

  * [Konfigurasi](</id/gateway/configuration>)
  * [Pemecahan masalah Gateway](</id/gateway/troubleshooting>)
  * [Akses jarak jauh](</id/gateway/remote>)
  * [Manajemen rahasia](</id/gateway/secrets>)


Was this useful?YesNo