---
title: Pemecahan Masalah
source_url: https://docs.openclaw.ai/id/gateway/troubleshooting
scraped_at: 2026-05-25
---

Halaman ini adalah runbook mendalam. Mulai dari [/help/troubleshooting](</id/help/troubleshooting>) jika Anda menginginkan alur triase cepat terlebih dahulu.

## Tangga perintah

Jalankan ini terlebih dahulu, dalam urutan ini:

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctoropenclaw channels status --probe
[/code]

Sinyal sehat yang diharapkan:

  * `openclaw gateway status` menampilkan `Runtime: running`, `Connectivity probe: ok`, dan baris `Capability: ...`.
  * `openclaw doctor` tidak melaporkan masalah konfigurasi/layanan yang memblokir.
  * `openclaw channels status --probe` menampilkan status transport per akun secara langsung dan, jika didukung, hasil probe/audit seperti `works` atau `audit ok`.


## Instalasi split brain dan pelindung konfigurasi yang lebih baru

Gunakan ini ketika layanan gateway tiba-tiba berhenti setelah pembaruan, atau log menunjukkan bahwa satu biner `openclaw` lebih lama daripada versi yang terakhir menulis `openclaw.json`.

OpenClaw menandai penulisan konfigurasi dengan `meta.lastTouchedVersion`. Perintah baca-saja masih dapat memeriksa konfigurasi yang ditulis oleh OpenClaw yang lebih baru, tetapi mutasi proses dan layanan menolak untuk melanjutkan dari biner yang lebih lama. Tindakan yang diblokir mencakup memulai, menghentikan, memulai ulang, menghapus instalasi layanan gateway, instalasi ulang layanan paksa, startup gateway mode layanan, dan pembersihan port `gateway --force`.

bashCopy code
[code]
    which openclawopenclaw --versionopenclaw gateway status --deepopenclaw config get meta.lastTouchedVersion
[/code]

* ### Perbaiki PATH

Perbaiki `PATH` agar `openclaw` mengarah ke instalasi yang lebih baru, lalu jalankan ulang tindakannya.

* ### Instal ulang layanan gateway

Instal ulang layanan gateway yang dimaksud dari instalasi yang lebih baru:

bashCopy code
[code]
    openclaw gateway install --forceopenclaw gateway restart
[/code]

* ### Hapus wrapper usang

Hapus paket sistem usang atau entri wrapper lama yang masih menunjuk ke biner `openclaw` lama.

## Symlink skill dilewati sebagai pelarian jalur

Gunakan ini ketika log menyertakan:

textCopy code
[code]
    Skipping escaped skill path outside its configured root: ... reason=symlink-escape
[/code]

OpenClaw memperlakukan setiap root skill sebagai batas penahanan. Symlink di bawah `~/.agents/skills`, `<workspace>/.agents/skills`, `<workspace>/skills`, atau `~/.openclaw/skills` dilewati ketika target aslinya mengarah ke luar root tersebut kecuali target tersebut dipercaya secara eksplisit.

Periksa tautannya:

bashCopy code
[code]
    ls -l ~/.agents/skills/<name>realpath ~/.agents/skills/<name>openclaw config get skills.load
[/code]

Jika target tersebut disengaja, konfigurasikan root skill langsung dan target symlink yang diizinkan:

json5Copy code
[code]
    {  skills: {    load: {      extraDirs: ["~/Projects/manager/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],    },  },}
[/code]

Lalu mulai sesi baru atau tunggu watcher skills menyegarkan. Mulai ulang gateway jika proses yang sedang berjalan dibuat sebelum perubahan konfigurasi.

Jangan gunakan target luas seperti `~`, `/`, atau seluruh folder proyek yang disinkronkan. Pertahankan `allowSymlinkTargets` terbatas pada root skill nyata yang berisi direktori `SKILL.md` tepercaya.

Terkait:

  * [Konfigurasi Skills](</id/tools/skills-config#symlinked-sibling-repos>)
  * [Contoh konfigurasi](</id/gateway/configuration-examples#symlinked-sibling-skill-repo>)


## Penggunaan tambahan Anthropic 429 diperlukan untuk konteks panjang

Gunakan ini ketika log/kesalahan menyertakan: `HTTP 429: rate_limit_error: Extra usage is required for long context requests`.

bashCopy code
[code]
    openclaw logs --followopenclaw models statusopenclaw config get agents.defaults.models
[/code]

Cari:

  * Model Anthropic Opus/Sonnet yang dipilih memiliki `params.context1m: true`.
  * Kredensial Anthropic saat ini tidak memenuhi syarat untuk penggunaan konteks panjang.
  * Permintaan gagal hanya pada sesi panjang/jalankan model yang membutuhkan jalur beta 1M.


Opsi perbaikan:

* ### Nonaktifkan context1m

Nonaktifkan `context1m` untuk model tersebut agar kembali ke jendela konteks normal.

* ### Gunakan kredensial yang memenuhi syarat

Gunakan kredensial Anthropic yang memenuhi syarat untuk permintaan konteks panjang, atau beralih ke kunci API Anthropic.

* ### Konfigurasikan model fallback

Konfigurasikan model fallback agar eksekusi berlanjut ketika permintaan konteks panjang Anthropic ditolak.

Terkait:

  * [Anthropic](</id/providers/anthropic>)
  * [Penggunaan token dan biaya](</id/reference/token-use>)
  * [Mengapa saya melihat HTTP 429 dari Anthropic?](</id/help/faq-first-run#why-am-i-seeing-http-429-ratelimiterror-from-anthropic>)


## Backend lokal yang kompatibel dengan OpenAI lulus probe langsung tetapi eksekusi agen gagal

Gunakan ini ketika:

  * `curl ... /v1/models` berfungsi
  * panggilan langsung kecil `/v1/chat/completions` berfungsi
  * Eksekusi model OpenClaw gagal hanya pada giliran agen normal

bashCopy code
[code]
    curl http://127.0.0.1:1234/v1/modelscurl http://127.0.0.1:1234/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"<id>","messages":[{"role":"user","content":"hi"}],"stream":false}'openclaw infer model run --model <provider/model> --prompt "hi" --jsonopenclaw logs --follow
[/code]

Cari:

  * panggilan kecil langsung berhasil, tetapi eksekusi OpenClaw gagal hanya pada prompt yang lebih besar
  * kesalahan `model_not_found` atau 404 meskipun `/v1/chat/completions` langsung berfungsi dengan id model polos yang sama
  * kesalahan backend tentang `messages[].content` yang mengharapkan string
  * peringatan `incomplete turn detected ... stopReason=stop payloads=0` yang sesekali muncul dengan backend lokal yang kompatibel dengan OpenAI
  * crash backend yang hanya muncul dengan jumlah token prompt yang lebih besar atau prompt runtime agen penuh


Tanda umum

  * `model_not_found` dengan server lokal bergaya MLX/vLLM → verifikasi `baseUrl` menyertakan `/v1`, `api` adalah `"openai-completions"` untuk backend `/v1/chat/completions`, dan `models.providers.<provider>.models[].id` adalah id lokal provider yang polos. Pilih dengan prefiks provider sekali, misalnya `mlx/mlx-community/Qwen3-30B-A3B-6bit`; pertahankan entri katalog sebagai `mlx-community/Qwen3-30B-A3B-6bit`.
  * `messages[...].content: invalid type: sequence, expected a string` → backend menolak bagian konten Chat Completions terstruktur. Perbaikan: setel `models.providers.<provider>.models[].compat.requiresStringContent: true`.
  * `validation.keys` atau kunci pesan yang diizinkan seperti `["role","content"]` → backend menolak metadata replay bergaya OpenAI pada pesan Chat Completions. Perbaikan: setel `models.providers.<provider>.models[].compat.strictMessageKeys: true`.
  * `incomplete turn detected ... stopReason=stop payloads=0` → backend menyelesaikan permintaan Chat Completions tetapi tidak mengembalikan teks asisten yang terlihat pengguna untuk giliran tersebut. OpenClaw mencoba ulang giliran kosong yang kompatibel dengan OpenAI dan aman untuk replay satu kali; kegagalan persisten biasanya berarti backend mengeluarkan konten kosong/non-teks atau menekan teks jawaban akhir.
  * permintaan kecil langsung berhasil, tetapi eksekusi agen OpenClaw gagal dengan crash backend/model (misalnya Gemma pada beberapa build `inferrs`) → transport OpenClaw kemungkinan sudah benar; backend gagal pada bentuk prompt runtime agen yang lebih besar.
  * kegagalan berkurang setelah menonaktifkan tools tetapi tidak hilang → skema tool adalah bagian dari tekanan, tetapi masalah yang tersisa masih berupa kapasitas model/server upstream atau bug backend.

Opsi perbaikan

  1. Setel `compat.requiresStringContent: true` untuk backend Chat Completions yang hanya menerima string.
  2. Setel `compat.strictMessageKeys: true` untuk backend Chat Completions ketat yang hanya menerima `role` dan `content` pada setiap pesan.
  3. Setel `compat.supportsTools: false` untuk model/backend yang tidak dapat menangani permukaan skema tool OpenClaw secara andal.
  4. Kurangi tekanan prompt jika memungkinkan: bootstrap workspace lebih kecil, riwayat sesi lebih pendek, model lokal lebih ringan, atau backend dengan dukungan konteks panjang yang lebih kuat.
  5. Jika permintaan kecil langsung terus berhasil sementara giliran agen OpenClaw masih crash di dalam backend, perlakukan itu sebagai batasan server/model upstream dan ajukan repro di sana dengan bentuk payload yang diterima.


Terkait:

  * [Konfigurasi](</id/gateway/configuration>)
  * [Model lokal](</id/gateway/local-models>)
  * [Endpoint yang kompatibel dengan OpenAI](</id/gateway/configuration-reference#openai-compatible-endpoints>)


## Tidak ada balasan

Jika channel aktif tetapi tidak ada yang menjawab, periksa routing dan kebijakan sebelum menghubungkan ulang apa pun.

bashCopy code
[code]
    openclaw statusopenclaw channels status --probeopenclaw pairing list --channel <channel> [--account <id>]openclaw config get channelsopenclaw logs --follow
[/code]

Cari:

  * Pairing tertunda untuk pengirim DM.
  * Pembatasan mention grup (`requireMention`, `mentionPatterns`).
  * Ketidakcocokan allowlist channel/grup.


Tanda umum:

  * `drop guild message (mention required` → pesan grup diabaikan hingga ada mention.
  * `pairing request` → pengirim membutuhkan persetujuan.
  * `blocked` / `allowlist` → pengirim/channel difilter oleh kebijakan.


Terkait:

  * [Pemecahan masalah channel](</id/channels/troubleshooting>)
  * [Grup](</id/channels/groups>)
  * [Pairing](</id/channels/pairing>)


## Konektivitas UI kontrol dasbor

Ketika dasbor/UI kontrol tidak dapat terhubung, validasi URL, mode auth, dan asumsi konteks aman.

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --followopenclaw doctoropenclaw gateway status --json
[/code]

Cari:

  * URL probe dan URL dasbor yang benar.
  * Ketidakcocokan mode auth/token antara klien dan gateway.
  * Penggunaan HTTP ketika identitas perangkat diperlukan.


Tanda koneksi / auth

  * `device identity required` → konteks tidak aman atau auth perangkat hilang.
  * `origin not allowed` → `Origin` browser tidak ada dalam `gateway.controlUi.allowedOrigins` (atau Anda terhubung dari origin browser non-loopback tanpa allowlist eksplisit).
  * `device nonce required` / `device nonce mismatch` → klien tidak menyelesaikan alur auth perangkat berbasis challenge (`connect.challenge` \+ `device.nonce`).
  * `device signature invalid` / `device signature expired` → klien menandatangani payload yang salah (atau timestamp usang) untuk handshake saat ini.
  * `AUTH_TOKEN_MISMATCH` dengan `canRetryWithDeviceToken=true` → klien dapat melakukan satu retry tepercaya dengan token perangkat yang di-cache.
  * Retry token yang di-cache tersebut menggunakan kembali set cakupan yang di-cache dan disimpan dengan token perangkat yang dipasangkan. Pemanggil `deviceToken` eksplisit / `scopes` eksplisit tetap mempertahankan set cakupan yang diminta.
  * `AUTH_SCOPE_MISMATCH` → token perangkat dikenali, tetapi cakupan yang disetujui tidak mencakup permintaan koneksi ini; pairing ulang atau setujui kontrak cakupan yang diminta alih-alih merotasi token gateway bersama.
  * Di luar jalur retry tersebut, prioritas auth koneksi adalah token/kata sandi bersama eksplisit terlebih dahulu, lalu `deviceToken` eksplisit, lalu token perangkat tersimpan, lalu token bootstrap.
  * Pada jalur UI Kontrol Tailscale Serve asinkron, upaya gagal untuk `{scope, ip}` yang sama diserialkan sebelum limiter mencatat kegagalan. Karena itu, dua retry buruk bersamaan dari klien yang sama dapat menampilkan `retry later` pada percobaan kedua alih-alih dua ketidakcocokan biasa.
  * `too many failed authentication attempts (retry later)` dari klien loopback dengan origin browser → kegagalan berulang dari `Origin` ternormalisasi yang sama dikunci sementara; origin localhost lain menggunakan bucket terpisah.
  * `unauthorized` berulang setelah retry tersebut → token bersama/token perangkat bergeser; segarkan konfigurasi token dan setujui ulang/rotasi token perangkat jika diperlukan.
  * `gateway connect failed:` → target host/port/url salah.


### Peta cepat kode detail auth

Gunakan `error.details.code` dari respons `connect` yang gagal untuk memilih tindakan berikutnya:

Kode detail | Makna | Tindakan yang direkomendasikan  
---|---|---  
`AUTH_TOKEN_MISSING` | Klien tidak mengirim token bersama yang diperlukan. | Tempel/tetapkan token di klien dan coba lagi. Untuk jalur dasbor: `openclaw config get gateway.auth.token` lalu tempelkan ke pengaturan Control UI.  
`AUTH_TOKEN_MISMATCH` | Token bersama tidak cocok dengan token autentikasi gateway. | Jika `canRetryWithDeviceToken=true`, izinkan satu kali percobaan ulang tepercaya. Percobaan ulang token yang di-cache menggunakan kembali cakupan tersetujui yang tersimpan; pemanggil `deviceToken` / `scopes` eksplisit mempertahankan cakupan yang diminta. Jika masih gagal, jalankan [daftar periksa pemulihan pergeseran token](</id/cli/devices#token-drift-recovery-checklist>).  
`AUTH_DEVICE_TOKEN_MISMATCH` | Token per perangkat yang di-cache sudah usang atau dicabut. | Putar/setujui ulang token perangkat menggunakan [CLI perangkat](</id/cli/devices>), lalu sambungkan ulang.  
`AUTH_SCOPE_MISMATCH` | Token perangkat valid, tetapi peran/cakupan yang disetujui tidak mencakup permintaan koneksi ini. | Pasangkan ulang perangkat atau setujui kontrak cakupan yang diminta; jangan perlakukan ini sebagai pergeseran token bersama.  
`PAIRING_REQUIRED` | Identitas perangkat memerlukan persetujuan. Periksa `error.details.reason` untuk `not-paired`, `scope-upgrade`, `role-upgrade`, atau `metadata-upgrade`, dan gunakan `requestId` / `remediationHint` saat ada. | Setujui permintaan tertunda: `openclaw devices list` lalu `openclaw devices approve <requestId>`. Peningkatan cakupan/peran menggunakan alur yang sama setelah Anda meninjau akses yang diminta.  
  
Pemeriksaan migrasi autentikasi perangkat v2:

bashCopy code
[code]
    openclaw --versionopenclaw doctoropenclaw gateway status
[/code]

Jika log menampilkan kesalahan nonce/tanda tangan, perbarui klien yang tersambung dan verifikasi:

* ### Wait for connect.challenge

Klien menunggu `connect.challenge` yang diterbitkan gateway.

* ### Sign the payload

Klien menandatangani payload yang terikat pada tantangan.

* ### Send the device nonce

Klien mengirim `connect.params.device.nonce` dengan nonce tantangan yang sama.

Jika `openclaw devices rotate` / `revoke` / `remove` ditolak secara tidak terduga:

  * sesi token perangkat berpasangan hanya dapat mengelola perangkat **miliknya sendiri** kecuali pemanggil juga memiliki `operator.admin`
  * `openclaw devices rotate --scope ...` hanya dapat meminta cakupan operator yang sudah dimiliki sesi pemanggil


Terkait:

  * [Konfigurasi](</id/gateway/configuration>) (mode autentikasi gateway)
  * [Control UI](</id/web/control-ui>)
  * [Perangkat](</id/cli/devices>)
  * [Akses jarak jauh](</id/gateway/remote>)
  * [Autentikasi proxy tepercaya](</id/gateway/trusted-proxy-auth>)


## Layanan gateway tidak berjalan

Gunakan ini saat layanan sudah terpasang tetapi proses tidak tetap berjalan.

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --followopenclaw doctoropenclaw gateway status --deep   # also scan system-level services
[/code]

Cari:

  * `Runtime: stopped` dengan petunjuk kode keluar.
  * Ketidakcocokan konfigurasi layanan (`Config (cli)` vs `Config (service)`).
  * Konflik port/listener.
  * Instalasi launchd/systemd/schtasks tambahan saat `--deep` digunakan.
  * Petunjuk pembersihan `Other gateway-like services detected (best effort)`.


Common signatures

  * `Gateway start blocked: set gateway.mode=local` atau `existing config is missing gateway.mode` → mode gateway lokal belum diaktifkan, atau file konfigurasi tertimpa dan kehilangan `gateway.mode`. Perbaikan: tetapkan `gateway.mode="local"` dalam konfigurasi Anda, atau jalankan ulang `openclaw onboard --mode local` / `openclaw setup` untuk menandai ulang konfigurasi mode lokal yang diharapkan. Jika Anda menjalankan OpenClaw melalui Podman, jalur konfigurasi default adalah `~/.openclaw/openclaw.json`.
  * `refusing to bind gateway ... without auth` → bind non-loopback tanpa jalur autentikasi gateway yang valid (token/kata sandi, atau trusted-proxy jika dikonfigurasi).
  * `another gateway instance is already listening` / `EADDRINUSE` → konflik port.
  * `Other gateway-like services detected (best effort)` → ada unit launchd/systemd/schtasks yang usang atau berjalan paralel. Sebagian besar penyiapan sebaiknya mempertahankan satu gateway per mesin; jika Anda memang membutuhkan lebih dari satu, isolasikan port + konfigurasi/status/workspace. Lihat [/gateway#multiple-gateways-same-host](</id/gateway#multiple-gateways-same-host>).
  * `System-level OpenClaw gateway service detected` dari doctor → ada unit sistem systemd sementara layanan tingkat pengguna tidak ada. Hapus atau nonaktifkan duplikat sebelum mengizinkan doctor memasang layanan pengguna, atau tetapkan `OPENCLAW_SERVICE_REPAIR_POLICY=external` jika unit sistem adalah supervisor yang dimaksud.
  * `Gateway service port does not match current gateway config` → supervisor terpasang masih mengunci `--port` lama. Jalankan `openclaw doctor --fix` atau `openclaw gateway install --force`, lalu mulai ulang layanan gateway.


Terkait:

  * [Eksekusi latar belakang dan alat proses](</id/gateway/background-process>)
  * [Konfigurasi](</id/gateway/configuration>)
  * [Doctor](</id/gateway/doctor>)


## Gateway menolak konfigurasi tidak valid

Gunakan ini saat startup Gateway gagal dengan `Invalid config` atau log hot reload mengatakan ia melewati edit yang tidak valid.

bashCopy code
[code]
    openclaw logs --followopenclaw config fileopenclaw config validateopenclaw doctor
[/code]

Cari:

  * `Invalid config at ...`
  * `config reload skipped (invalid config): ...`
  * `Config write rejected: ...`
  * File `openclaw.json.rejected.*` bertanda waktu di sebelah konfigurasi aktif
  * File `openclaw.json.clobbered.*` bertanda waktu jika `doctor --fix` memperbaiki edit langsung yang rusak


What happened

  * Konfigurasi tidak lolos validasi saat startup, hot reload, atau penulisan milik OpenClaw.
  * Startup Gateway gagal tertutup alih-alih menulis ulang `openclaw.json`.
  * Hot reload melewati edit eksternal yang tidak valid dan mempertahankan konfigurasi runtime saat ini tetap aktif.
  * Penulisan milik OpenClaw menolak payload yang tidak valid/destruktif sebelum commit dan menyimpan `.rejected.*`.
  * `openclaw doctor --fix` memiliki perbaikan. Ia dapat menghapus prefiks non-JSON atau memulihkan salinan terakhir yang diketahui baik sambil mempertahankan payload yang ditolak sebagai `.clobbered.*`.

Inspect and repair bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".clobbered.* "$CONFIG".rejected.* 2>/dev/null | headdiff -u "$CONFIG" "$(ls -t "$CONFIG".clobbered.* 2>/dev/null | head -n 1)"openclaw config validateopenclaw doctor
[/code]

Common signatures

  * `.clobbered.*` ada → doctor mempertahankan edit eksternal yang rusak saat memperbaiki konfigurasi aktif.
  * `.rejected.*` ada → penulisan konfigurasi milik OpenClaw gagal pada pemeriksaan skema atau penimpaan sebelum commit.
  * `Config write rejected:` → penulisan mencoba menghapus bentuk yang diperlukan, mengecilkan file secara tajam, atau mempertahankan konfigurasi tidak valid.
  * `config reload skipped (invalid config):` → edit langsung gagal validasi dan diabaikan oleh Gateway yang sedang berjalan.
  * `Invalid config at ...` → startup gagal sebelum layanan Gateway dijalankan.
  * `missing-meta-vs-last-good`, `gateway-mode-missing-vs-last-good`, atau `size-drop-vs-last-good:*` → penulisan milik OpenClaw ditolak karena kehilangan bidang atau ukuran dibandingkan cadangan terakhir yang diketahui baik.
  * `Config last-known-good promotion skipped` → kandidat berisi placeholder rahasia yang disamarkan seperti `***`.

Fix options

  1. Jalankan `openclaw doctor --fix` agar doctor memperbaiki konfigurasi berprefiks/tertimpakan atau memulihkan terakhir yang diketahui baik.
  2. Salin hanya kunci yang dimaksud dari `.clobbered.*` atau `.rejected.*`, lalu terapkan dengan `openclaw config set` atau `config.patch`.
  3. Jalankan `openclaw config validate` sebelum memulai ulang.
  4. Jika Anda mengedit secara manual, pertahankan konfigurasi JSON5 lengkap, bukan hanya objek parsial yang ingin Anda ubah.


Terkait:

  * [Config](</id/cli/config>)
  * [Konfigurasi: hot reload](</id/gateway/configuration#config-hot-reload>)
  * [Konfigurasi: validasi ketat](</id/gateway/configuration#strict-validation>)
  * [Doctor](</id/gateway/doctor>)


## Peringatan probe Gateway

Gunakan ini saat `openclaw gateway probe` menjangkau sesuatu, tetapi masih mencetak blok peringatan.

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --jsonopenclaw gateway probe --ssh user@gateway-host
[/code]

Cari:

  * `warnings[].code` dan `primaryTargetId` dalam output JSON.
  * Apakah peringatan terkait fallback SSH, beberapa gateway, cakupan hilang, atau ref autentikasi yang belum terselesaikan.


Tanda umum:

  * `SSH tunnel failed to start; falling back to direct probes.` → penyiapan SSH gagal, tetapi perintah tetap mencoba target langsung yang dikonfigurasi/loopback.
  * `multiple reachable gateways detected` → lebih dari satu target menjawab. Biasanya ini berarti penyiapan multi-gateway yang disengaja atau listener usang/duplikat.
  * `Read-probe diagnostics are limited by gateway scopes (missing operator.read)` → koneksi berhasil, tetapi RPC detail dibatasi cakupan; pasangkan identitas perangkat atau gunakan kredensial dengan `operator.read`.
  * `Gateway accepted the WebSocket connection, but follow-up read diagnostics failed` → koneksi berhasil, tetapi set RPC diagnostik lengkap kehabisan waktu atau gagal. Perlakukan ini sebagai Gateway yang dapat dijangkau dengan diagnostik terdegradasi; bandingkan `connect.ok` dan `connect.rpcOk` dalam output `--json`.
  * `Capability: pairing-pending` atau `gateway closed (1008): pairing required` → gateway menjawab, tetapi klien ini masih memerlukan pemasangan/persetujuan sebelum akses operator normal.
  * teks peringatan SecretRef `gateway.auth.*` / `gateway.remote.*` yang belum terselesaikan → materi autentikasi tidak tersedia di jalur perintah ini untuk target yang gagal.


Terkait:

  * [Gateway](</id/cli/gateway>)
  * [Beberapa Gateway pada host yang sama](</id/gateway#multiple-gateways-same-host>)
  * [Akses jarak jauh](</id/gateway/remote>)


## Kanal tersambung, pesan tidak mengalir

Jika status kanal tersambung tetapi alur pesan berhenti, fokus pada kebijakan, izin, dan aturan pengiriman khusus kanal.

bashCopy code
[code]
    openclaw channels status --probeopenclaw pairing list --channel <channel> [--account <id>]openclaw status --deepopenclaw logs --followopenclaw config get channels
[/code]

Cari:

  * Kebijakan DM (`pairing`, `allowlist`, `open`, `disabled`).
  * Allowlist grup dan persyaratan penyebutan.
  * Izin/cakupan API kanal yang hilang.


Tanda umum:

  * `mention required` → pesan diabaikan oleh kebijakan penyebutan grup.
  * `pairing` / jejak persetujuan tertunda → pengirim belum disetujui.
  * `missing_scope`, `not_in_channel`, `Forbidden`, `401/403` → masalah autentikasi/izin kanal.


Terkait:

  * [Pemecahan masalah kanal](</id/channels/troubleshooting>)
  * [Discord](</id/channels/discord>)
  * [Telegram](</id/channels/telegram>)
  * [WhatsApp](</id/channels/whatsapp>)


## Pengiriman Cron dan Heartbeat

Jika cron atau heartbeat tidak berjalan atau tidak terkirim, verifikasi status penjadwal terlebih dahulu, lalu target pengiriman.

bashCopy code
[code]
    openclaw cron statusopenclaw cron listopenclaw cron runs --id <jobId> --limit 20openclaw system heartbeat lastopenclaw logs --follow
[/code]

Cari:

  * Cron aktif dan wake berikutnya tersedia.
  * Status riwayat eksekusi job (`ok`, `skipped`, `error`).
  * Alasan Heartbeat dilewati (`quiet-hours`, `requests-in-flight`, `cron-in-progress`, `lanes-busy`, `alerts-disabled`, `empty-heartbeat-file`, `no-tasks-due`).


Common signatures

  * `cron: scheduler disabled; jobs will not run automatically` → cron dinonaktifkan.
  * `cron: timer tick failed` → tick penjadwal gagal; periksa kesalahan file/log/runtime.
  * `heartbeat skipped` dengan `reason=quiet-hours` → di luar jendela jam aktif.
  * `heartbeat skipped` dengan `reason=empty-heartbeat-file` → `HEARTBEAT.md` ada tetapi hanya berisi baris kosong / header markdown, sehingga OpenClaw melewati panggilan model.
  * `heartbeat skipped` dengan `reason=no-tasks-due` → `HEARTBEAT.md` berisi blok `tasks:`, tetapi tidak ada tugas yang jatuh tempo pada tick ini.
  * `heartbeat: unknown accountId` → id akun tidak valid untuk target pengiriman heartbeat.
  * `heartbeat skipped` dengan `reason=dm-blocked` → target heartbeat dipetakan ke tujuan bergaya DM sementara `agents.defaults.heartbeat.directPolicy` (atau override per agen) diatur ke `block`.


Terkait:

  * [Heartbeat](</id/gateway/heartbeat>)
  * [Tugas terjadwal](</id/automation/cron-jobs>)
  * [Tugas terjadwal: pemecahan masalah](</id/automation/cron-jobs#troubleshooting>)


## Node dipasangkan, tool gagal

Jika sebuah node dipasangkan tetapi tool gagal, isolasi status foreground, izin, dan persetujuan.

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>openclaw logs --followopenclaw status
[/code]

Cari:

  * Node online dengan kemampuan yang diharapkan.
  * Pemberian izin OS untuk kamera/mikrofon/lokasi/layar.
  * Persetujuan exec dan status allowlist.


Tanda umum:

  * `NODE_BACKGROUND_UNAVAILABLE` → aplikasi node harus berada di foreground.
  * `*_PERMISSION_REQUIRED` / `LOCATION_PERMISSION_REQUIRED` → izin OS hilang.
  * `SYSTEM_RUN_DENIED: approval required` → persetujuan exec tertunda.
  * `SYSTEM_RUN_DENIED: allowlist miss` → perintah diblokir oleh allowlist.


Terkait:

  * [Persetujuan exec](</id/tools/exec-approvals>)
  * [Pemecahan masalah Node](</id/nodes/troubleshooting>)
  * [Nodes](</id/nodes>)


## Tool peramban gagal

Gunakan ini ketika aksi tool peramban gagal meskipun gateway itu sendiri sehat.

bashCopy code
[code]
    openclaw browser statusopenclaw browser start --browser-profile openclawopenclaw browser profilesopenclaw logs --followopenclaw doctor
[/code]

Cari:

  * Apakah `plugins.allow` diatur dan menyertakan `browser`.
  * Jalur executable peramban yang valid.
  * Keterjangkauan profil CDP.
  * Ketersediaan Chrome lokal untuk profil `existing-session` / `user`.


Plugin / executable signatures

  * `unknown command "browser"` atau `unknown command 'browser'` → plugin peramban bawaan dikecualikan oleh `plugins.allow`.
  * tool peramban hilang / tidak tersedia saat `browser.enabled=true` → `plugins.allow` mengecualikan `browser`, sehingga plugin tidak pernah dimuat.
  * `Failed to start Chrome CDP on port` → proses peramban gagal diluncurkan.
  * `browser.executablePath not found` → jalur yang dikonfigurasi tidak valid.
  * `browser.cdpUrl must be http(s) or ws(s)` → URL CDP yang dikonfigurasi menggunakan skema yang tidak didukung seperti `file:` atau `ftp:`.
  * `browser.cdpUrl has invalid port` → URL CDP yang dikonfigurasi memiliki port yang buruk atau di luar rentang.
  * `Playwright is not available in this gateway build; '<feature>' is unsupported.` → instalasi gateway saat ini tidak memiliki dependensi runtime peramban inti; instal ulang atau perbarui OpenClaw, lalu mulai ulang gateway. Snapshot ARIA dan tangkapan layar halaman dasar masih dapat berfungsi, tetapi navigasi, snapshot AI, tangkapan layar elemen dengan selector CSS, dan ekspor PDF tetap tidak tersedia.

Chrome MCP / existing-session signatures

  * `Could not find DevToolsActivePort for chrome` → existing-session Chrome MCP belum dapat terhubung ke direktori data peramban yang dipilih. Buka halaman inspect peramban, aktifkan remote debugging, biarkan peramban tetap terbuka, setujui prompt attach pertama, lalu coba lagi. Jika status masuk tidak diperlukan, gunakan profil terkelola `openclaw`.
  * `No Chrome tabs found for profile="user"` → profil attach Chrome MCP tidak memiliki tab Chrome lokal yang terbuka.
  * `Remote CDP for profile "<name>" is not reachable` → endpoint CDP jarak jauh yang dikonfigurasi tidak dapat dijangkau dari host gateway.
  * `Browser attachOnly is enabled ... not reachable` atau `Browser attachOnly is enabled and CDP websocket ... is not reachable` → profil attach-only tidak memiliki target yang dapat dijangkau, atau endpoint HTTP merespons tetapi CDP WebSocket tetap tidak dapat dibuka.

Element / screenshot / upload signatures

  * `fullPage is not supported for element screenshots` → permintaan tangkapan layar mencampur `--full-page` dengan `--ref` atau `--element`.
  * `element screenshots are not supported for existing-session profiles; use ref from snapshot.` → panggilan tangkapan layar Chrome MCP / `existing-session` harus menggunakan tangkapan halaman atau `--ref` snapshot, bukan CSS `--element`.
  * `existing-session file uploads do not support element selectors; use ref/inputRef.` → hook unggahan Chrome MCP memerlukan ref snapshot, bukan selector CSS.
  * `existing-session file uploads currently support one file at a time.` → kirim satu unggahan per panggilan pada profil Chrome MCP.
  * `existing-session dialog handling does not support timeoutMs.` → hook dialog pada profil Chrome MCP tidak mendukung override timeout.
  * `existing-session type does not support timeoutMs overrides.` → hilangkan `timeoutMs` untuk `act:type` pada profil `profile="user"` / existing-session Chrome MCP, atau gunakan profil peramban terkelola/CDP saat timeout kustom diperlukan.
  * `existing-session evaluate does not support timeoutMs overrides.` → hilangkan `timeoutMs` untuk `act:evaluate` pada profil `profile="user"` / existing-session Chrome MCP, atau gunakan profil peramban terkelola/CDP saat timeout kustom diperlukan.
  * `response body is not supported for existing-session profiles yet.` → `responsebody` masih memerlukan peramban terkelola atau profil CDP mentah.
  * override viewport / dark-mode / locale / offline yang usang pada profil attach-only atau CDP jarak jauh → jalankan `openclaw browser stop --browser-profile <name>` untuk menutup sesi kontrol aktif dan melepas status emulasi Playwright/CDP tanpa memulai ulang seluruh gateway.


Terkait:

  * [Peramban (dikelola OpenClaw)](</id/tools/browser>)
  * [Pemecahan masalah peramban](</id/tools/browser-linux-troubleshooting>)


## Jika Anda meningkatkan versi dan sesuatu tiba-tiba rusak

Sebagian besar kerusakan setelah peningkatan versi adalah drift konfigurasi atau default yang lebih ketat kini diterapkan.

1\. Auth and URL override behavior changed bashCopy code
[code]
    openclaw gateway statusopenclaw config get gateway.modeopenclaw config get gateway.remote.urlopenclaw config get gateway.auth.mode
[/code]

Yang harus diperiksa:

  * Jika `gateway.mode=remote`, panggilan CLI mungkin menargetkan remote sementara layanan lokal Anda baik-baik saja.
  * Panggilan `--url` eksplisit tidak fallback ke kredensial tersimpan.


Tanda umum:

  * `gateway connect failed:` → target URL salah.
  * `unauthorized` → endpoint dapat dijangkau tetapi autentikasi salah.

2\. Bind and auth guardrails are stricter bashCopy code
[code]
    openclaw config get gateway.bindopenclaw config get gateway.auth.modeopenclaw config get gateway.auth.tokenopenclaw gateway statusopenclaw logs --follow
[/code]

Yang harus diperiksa:

  * Bind non-loopback (`lan`, `tailnet`, `custom`) memerlukan jalur autentikasi gateway yang valid: autentikasi token/kata sandi bersama, atau deployment `trusted-proxy` non-loopback yang dikonfigurasi dengan benar.
  * Kunci lama seperti `gateway.token` tidak menggantikan `gateway.auth.token`.


Tanda umum:

  * `refusing to bind gateway ... without auth` → bind non-loopback tanpa jalur autentikasi gateway yang valid.
  * `Connectivity probe: failed` saat runtime berjalan → gateway hidup tetapi tidak dapat diakses dengan auth/url saat ini.

3\. Pairing and device identity state changed bashCopy code
[code]
    openclaw devices listopenclaw pairing list --channel <channel> [--account <id>]openclaw logs --followopenclaw doctor
[/code]

Yang harus diperiksa:

  * Persetujuan perangkat yang tertunda untuk dasbor/node.
  * Persetujuan pairing DM yang tertunda setelah perubahan kebijakan atau identitas.


Tanda umum:

  * `device identity required` → autentikasi perangkat belum terpenuhi.
  * `pairing required` → pengirim/perangkat harus disetujui.


Jika konfigurasi layanan dan runtime masih tidak cocok setelah pemeriksaan, instal ulang metadata layanan dari direktori profil/status yang sama:

bashCopy code
[code]
    openclaw gateway install --forceopenclaw gateway restart
[/code]

Terkait:

  * [Autentikasi](</id/gateway/authentication>)
  * [Exec latar belakang dan tool proses](</id/gateway/background-process>)
  * [Pairing milik Gateway](</id/gateway/pairing>)


## Terkait

  * [Doctor](</id/gateway/doctor>)
  * [FAQ](</id/help/faq>)
  * [Runbook Gateway](</id/gateway>)


Was this useful?YesNo