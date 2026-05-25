---
title: Gateway
source_url: https://docs.openclaw.ai/id/cli/gateway
scraped_at: 2026-05-25
---

Gateway adalah server WebSocket OpenClaw (saluran, node, sesi, hook). Subperintah di halaman ini berada di bawah `openclaw gateway …`.

[**Bonjour discovery** Penyiapan mDNS lokal + DNS-SD area luas. ](</id/gateway/bonjour>) [**Discovery overview** Cara OpenClaw mengiklankan dan menemukan Gateway. ](</id/gateway/discovery>) [**Configuration** Kunci konfigurasi Gateway tingkat atas. ](</id/gateway/configuration>)

## Jalankan Gateway

Jalankan proses Gateway lokal:

bashCopy code
[code]
    openclaw gateway
[/code]

Alias latar depan:

bashCopy code
[code]
    openclaw gateway run
[/code]

Startup behavior

  * Secara default, Gateway menolak untuk dimulai kecuali `gateway.mode=local` diatur di `~/.openclaw/openclaw.json`. Gunakan `--allow-unconfigured` untuk eksekusi ad-hoc/pengembangan.
  * `openclaw onboard --mode local` dan `openclaw setup` diharapkan menulis `gateway.mode=local`. Jika file ada tetapi `gateway.mode` tidak ada, perlakukan itu sebagai konfigurasi yang rusak atau tertimpa dan perbaiki, alih-alih mengasumsikan mode lokal secara implisit.
  * Jika file ada dan `gateway.mode` tidak ada, Gateway memperlakukan itu sebagai kerusakan konfigurasi yang mencurigakan dan menolak untuk "menebak lokal" untuk Anda.
  * Binding di luar loopback tanpa autentikasi diblokir (batas pengaman keselamatan).
  * `SIGUSR1` memicu mulai ulang dalam proses saat diotorisasi (`commands.restart` diaktifkan secara default; atur `commands.restart: false` untuk memblokir mulai ulang manual, sementara penerapan/pembaruan alat/konfigurasi Gateway tetap diizinkan).
  * Handler `SIGINT`/`SIGTERM` menghentikan proses Gateway, tetapi tidak memulihkan status terminal khusus apa pun. Jika Anda membungkus CLI dengan TUI atau input raw-mode, pulihkan terminal sebelum keluar.


### Opsi

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> Port WebSocket (default berasal dari konfigurasi/env; biasanya `18789`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> Override token (juga mengatur `OPENCLAW_GATEWAY_TOKEN` untuk proses).

Reset konfigurasi serve/funnel Tailscale saat dimatikan.

Izinkan Gateway dimulai tanpa `gateway.mode=local` dalam konfigurasi. Hanya melewati pengaman startup untuk bootstrap ad-hoc/pengembangan; tidak menulis atau memperbaiki file konfigurasi.

Buat konfigurasi pengembangan + workspace jika tidak ada (melewati [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).

Reset konfigurasi pengembangan + kredensial + sesi + workspace (memerlukan `--dev`).

Matikan listener yang sudah ada pada port yang dipilih sebelum memulai.

Log verbose.

Hanya tampilkan log backend CLI di konsol (dan aktifkan stdout/stderr).

Alias untuk `--ws-log compact`.

Catat event stream model mentah ke jsonl.

## Mulai Ulang Gateway

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

`openclaw gateway restart --safe` meminta Gateway yang berjalan melakukan preflight pekerjaan OpenClaw aktif sebelum memulai ulang. Jika operasi antrean, pengiriman balasan, eksekusi tertanam, atau eksekusi tugas sedang aktif, Gateway melaporkan pemblokirnya, menggabungkan permintaan mulai ulang aman yang duplikat, dan memulai ulang setelah pekerjaan aktif selesai. `restart` biasa mempertahankan perilaku service-manager yang sudah ada untuk kompatibilitas. Gunakan `--force` hanya saat Anda secara eksplisit menginginkan jalur override langsung.

`openclaw gateway restart --safe --skip-deferral` menjalankan mulai ulang terkoordinasi yang sama dan sadar OpenClaw seperti `--safe`, tetapi melewati gerbang penundaan pekerjaan aktif sehingga Gateway langsung memancarkan mulai ulang meskipun pemblokir dilaporkan. Gunakan ini sebagai pintu keluar operator saat penundaan tertahan oleh eksekusi tugas yang macet dan `--safe` saja akan menunggu tanpa batas. `--skip-deferral` memerlukan `--safe`.

### Profiling startup

  * Atur `OPENCLAW_GATEWAY_STARTUP_TRACE=1` untuk mencatat timing fase selama startup Gateway, termasuk penundaan `eventLoopMax` per fase dan timing tabel lookup plugin untuk indeks terinstal, registry manifest, perencanaan startup, dan pekerjaan owner-map.
  * Atur `OPENCLAW_DIAGNOSTICS=timeline` dengan `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>` untuk menulis timeline diagnostik startup JSONL best-effort bagi harness QA eksternal. Anda juga dapat mengaktifkan flag dengan `diagnostics.flags: ["timeline"]` dalam konfigurasi; path tetap disediakan env. Tambahkan `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1` untuk menyertakan sampel event-loop.
  * Jalankan `pnpm test:startup:gateway -- --runs 5 --warmup 1` untuk mengukur startup Gateway. Benchmark mencatat output proses pertama, `/healthz`, `/readyz`, timing trace startup, penundaan event-loop, dan detail timing tabel lookup plugin.


## Kueri Gateway yang berjalan

Semua perintah kueri menggunakan RPC WebSocket.

### Output modes

  * Default: mudah dibaca manusia (berwarna di TTY).
  * `--json`: JSON yang dapat dibaca mesin (tanpa styling/spinner).
  * `--no-color` (atau `NO_COLOR=1`): nonaktifkan ANSI sambil mempertahankan tata letak manusia.


### Shared options

  * `--url <url>`: URL WebSocket Gateway.
  * `--token <token>`: token Gateway.
  * `--password <password>`: kata sandi Gateway.
  * `--timeout <ms>`: timeout/anggaran (bervariasi per perintah).
  * `--expect-final`: tunggu respons "final" (panggilan agen).


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789
[/code]

Endpoint HTTP `/healthz` adalah probe liveness: ia mengembalikan respons setelah server dapat menjawab HTTP. Endpoint HTTP `/readyz` lebih ketat dan tetap merah saat sidecar plugin startup, saluran, atau hook yang dikonfigurasi masih dalam proses stabil. Respons readiness detail yang lokal atau terautentikasi menyertakan blok diagnostik `eventLoop` dengan penundaan event-loop, utilisasi event-loop, rasio inti CPU, dan flag `degraded`.

### `gateway usage-cost`

Ambil ringkasan biaya penggunaan dari log sesi.

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --json
[/code]

### `gateway stability`

Ambil perekam stabilitas diagnostik terbaru dari Gateway yang berjalan.

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> Jumlah maksimum event terbaru yang akan disertakan (maks `1000`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> Filter menurut jenis event diagnostik, seperti `payload.large` atau `diagnostic.memory.pressure`.

Baca bundle stabilitas yang dipersistenkan alih-alih memanggil Gateway yang berjalan. Gunakan `--bundle latest` (atau cukup `--bundle`) untuk bundle terbaru di bawah direktori state, atau teruskan langsung path JSON bundle.

Tulis zip diagnostik dukungan yang dapat dibagikan alih-alih mencetak detail stabilitas.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> Path output untuk `--export`.

Privacy and bundle behavior

  * Rekaman menyimpan metadata operasional: nama event, jumlah, ukuran byte, pembacaan memori, status antrean/sesi, nama saluran/plugin, dan ringkasan sesi yang disunting. Rekaman tidak menyimpan teks chat, body webhook, output alat, body request atau respons mentah, token, cookie, nilai rahasia, hostname, atau id sesi mentah. Atur `diagnostics.enabled: false` untuk menonaktifkan perekam sepenuhnya.
  * Pada keluarnya Gateway yang fatal, timeout shutdown, dan kegagalan startup restart, OpenClaw menulis snapshot diagnostik yang sama ke `~/.openclaw/logs/stability/openclaw-stability-*.json` saat perekam memiliki event. Periksa bundle terbaru dengan `openclaw gateway stability --bundle latest`; `--limit`, `--type`, dan `--since-seq` juga berlaku untuk output bundle.


### `gateway diagnostics export`

Tulis zip diagnostik lokal yang dirancang untuk dilampirkan ke laporan bug. Untuk model privasi dan isi bundle, lihat [Ekspor Diagnostik](</id/gateway/diagnostics>).

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

Lewati lookup bundle stabilitas yang dipersistenkan.

Cetak path yang ditulis, ukuran, dan manifest sebagai JSON.

Ekspor berisi manifest, ringkasan Markdown, bentuk konfigurasi, detail konfigurasi tersanitasi, ringkasan log tersanitasi, snapshot status/kesehatan Gateway tersanitasi, dan bundle stabilitas terbaru saat ada.

Ini dimaksudkan untuk dibagikan. Ekspor menyimpan detail operasional yang membantu debugging, seperti field log OpenClaw yang aman, nama subsistem, kode status, durasi, mode yang dikonfigurasi, port, id plugin, id provider, pengaturan fitur non-rahasia, dan pesan log operasional yang disunting. Ekspor menghilangkan atau menyunting teks chat, body webhook, output alat, kredensial, cookie, identifier akun/pesan, teks prompt/instruksi, hostname, dan nilai rahasia. Saat pesan bergaya LogTape tampak seperti teks payload pengguna/chat/alat, ekspor hanya menyimpan bahwa sebuah pesan dihilangkan beserta jumlah byte-nya.

### `gateway status`

`gateway status` menampilkan layanan Gateway (launchd/systemd/schtasks) ditambah probe opsional untuk kemampuan konektivitas/autentikasi.

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

Lewati probe konektivitas (tampilan layanan saja).

Pindai juga layanan tingkat sistem.

Tingkatkan probe konektivitas default menjadi probe baca dan keluar dengan non-zero ketika probe baca tersebut gagal. Tidak dapat digabungkan dengan `--no-probe`.

Semantik status

  * `gateway status` tetap tersedia untuk diagnostik bahkan ketika konfigurasi CLI lokal hilang atau tidak valid.
  * `gateway status` default membuktikan status layanan, koneksi WebSocket, dan kapabilitas autentikasi yang terlihat pada waktu handshake. Ini tidak membuktikan operasi baca/tulis/admin.
  * Probe diagnostik tidak melakukan mutasi untuk autentikasi perangkat pertama kali: probe menggunakan ulang token perangkat yang sudah ada di cache jika tersedia, tetapi tidak membuat identitas perangkat CLI baru atau catatan pemasangan perangkat read-only hanya untuk memeriksa status.
  * `gateway status` menyelesaikan SecretRefs autentikasi yang dikonfigurasi untuk autentikasi probe jika memungkinkan.
  * Jika SecretRef autentikasi wajib tidak terselesaikan dalam jalur perintah ini, `gateway status --json` melaporkan `rpc.authWarning` ketika konektivitas/autentikasi probe gagal; teruskan `--token`/`--password` secara eksplisit atau selesaikan sumber secret terlebih dahulu.
  * Jika probe berhasil, peringatan auth-ref yang tidak terselesaikan disembunyikan untuk menghindari positif palsu.
  * Gunakan `--require-rpc` dalam skrip dan otomatisasi ketika layanan yang mendengarkan saja tidak cukup dan Anda juga memerlukan panggilan RPC cakupan-baca yang sehat.
  * `--deep` menambahkan pemindaian best-effort untuk instalasi launchd/systemd/schtasks tambahan. Ketika beberapa layanan mirip gateway terdeteksi, keluaran manusia mencetak petunjuk pembersihan dan memperingatkan bahwa sebagian besar penyiapan sebaiknya menjalankan satu Gateway per mesin.
  * `--deep` juga melaporkan handoff restart supervisor Gateway terbaru ketika proses layanan keluar dengan bersih untuk restart supervisor eksternal.
  * `--deep` menjalankan validasi konfigurasi dalam mode sadar-plugin (`pluginValidation: "full"`) dan menampilkan peringatan manifes plugin yang dikonfigurasi (misalnya metadata konfigurasi channel yang hilang) sehingga pemeriksaan smoke instalasi dan pembaruan menangkapnya. `gateway status` default mempertahankan jalur read-only cepat yang melewati validasi plugin.
  * Keluaran manusia menyertakan path log file yang terselesaikan plus snapshot path/validitas konfigurasi CLI-vs-layanan untuk membantu mendiagnosis drift profil atau state-dir.

Pemeriksaan drift autentikasi systemd Linux

  * Pada instalasi systemd Linux, pemeriksaan drift autentikasi layanan membaca nilai `Environment=` dan `EnvironmentFile=` dari unit (termasuk `%h`, path yang dikutip, beberapa file, dan file opsional `-`).
  * Pemeriksaan drift menyelesaikan SecretRefs `gateway.auth.token` menggunakan env runtime gabungan (env perintah layanan terlebih dahulu, lalu fallback env proses).
  * Jika autentikasi token tidak aktif secara efektif (`gateway.auth.mode` eksplisit berupa `password`/`none`/`trusted-proxy`, atau mode tidak disetel saat kata sandi dapat menang dan tidak ada kandidat token yang dapat menang), pemeriksaan token-drift melewati penyelesaian token konfigurasi.


### `gateway probe`

`gateway probe` adalah perintah "debug semuanya". Perintah ini selalu memprobe:

  * gateway remote yang Anda konfigurasi (jika disetel), dan
  * localhost (loopback) **bahkan jika remote dikonfigurasi**.


Jika Anda meneruskan `--url`, target eksplisit tersebut ditambahkan sebelum keduanya. Keluaran manusia melabeli target sebagai:

  * `URL (explicit)`
  * `Remote (configured)` atau `Remote (configured, inactive)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --json
[/code]

Interpretasi

  * `Reachable: yes` berarti setidaknya satu target menerima koneksi WebSocket.
  * `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only` melaporkan apa yang dapat dibuktikan probe tentang autentikasi. Ini terpisah dari keterjangkauan.
  * `Read probe: ok` berarti panggilan RPC detail cakupan-baca (`health`/`status`/`system-presence`/`config.get`) juga berhasil.
  * `Read probe: limited - missing scope: operator.read` berarti koneksi berhasil tetapi RPC cakupan-baca terbatas. Ini dilaporkan sebagai keterjangkauan **terdegradasi** , bukan kegagalan penuh.
  * `Read probe: failed` setelah `Connect: ok` berarti Gateway menerima koneksi WebSocket, tetapi diagnostik baca lanjutan kehabisan waktu atau gagal. Ini juga merupakan keterjangkauan **terdegradasi** , bukan Gateway yang tidak dapat dijangkau.
  * Seperti `gateway status`, probe menggunakan ulang autentikasi perangkat yang sudah ada di cache tetapi tidak membuat identitas perangkat pertama kali atau status pemasangan.
  * Exit code bernilai non-zero hanya ketika tidak ada target yang diprobe yang dapat dijangkau.

Keluaran JSON

Tingkat atas:

  * `ok`: setidaknya satu target dapat dijangkau.
  * `degraded`: setidaknya satu target menerima koneksi tetapi tidak menyelesaikan diagnostik RPC detail penuh.
  * `capability`: kapabilitas terbaik yang terlihat di seluruh target yang dapat dijangkau (`read_only`, `write_capable`, `admin_capable`, `pairing_pending`, `connected_no_operator_scope`, atau `unknown`).
  * `primaryTargetId`: target terbaik untuk diperlakukan sebagai pemenang aktif dalam urutan ini: URL eksplisit, tunnel SSH, remote yang dikonfigurasi, lalu local loopback.
  * `warnings[]`: catatan peringatan best-effort dengan `code`, `message`, dan `targetIds` opsional.
  * `network`: petunjuk URL local loopback/tailnet yang diturunkan dari konfigurasi saat ini dan jaringan host.
  * `discovery.timeoutMs` dan `discovery.count`: anggaran/jumlah hasil discovery aktual yang digunakan untuk lintasan probe ini.


Per target (`targets[].connect`):

  * `ok`: keterjangkauan setelah koneksi + klasifikasi terdegradasi.
  * `rpcOk`: keberhasilan RPC detail penuh.
  * `scopeLimited`: RPC detail gagal karena cakupan operator yang hilang.


Per target (`targets[].auth`):

  * `role`: peran autentikasi yang dilaporkan dalam `hello-ok` jika tersedia.
  * `scopes`: cakupan yang diberikan yang dilaporkan dalam `hello-ok` jika tersedia.
  * `capability`: klasifikasi kapabilitas autentikasi yang ditampilkan untuk target tersebut.

Kode peringatan umum

  * `ssh_tunnel_failed`: penyiapan tunnel SSH gagal; perintah beralih kembali ke probe langsung.
  * `multiple_gateways`: lebih dari satu target dapat dijangkau; ini tidak biasa kecuali Anda sengaja menjalankan profil terisolasi, seperti bot penyelamat.
  * `auth_secretref_unresolved`: SecretRef autentikasi yang dikonfigurasi tidak dapat diselesaikan untuk target yang gagal.
  * `probe_scope_limited`: koneksi WebSocket berhasil, tetapi probe baca dibatasi oleh `operator.read` yang hilang.


#### Remote lewat SSH (paritas app Mac)

Mode "Remote over SSH" app macOS menggunakan port-forward lokal sehingga gateway remote (yang mungkin hanya terikat ke loopback) menjadi dapat dijangkau di `ws://127.0.0.1:<port>`.

Padanan CLI:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` atau `user@host:port` (port default ke `22`).

Pilih host gateway pertama yang ditemukan sebagai target SSH dari endpoint discovery yang terselesaikan (`local.` plus domain wide-area yang dikonfigurasi, jika ada). Petunjuk TXT-only diabaikan.

Konfigurasi (opsional, digunakan sebagai default):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

Helper RPC tingkat rendah.

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

Terutama untuk RPC bergaya agen yang men-stream event perantara sebelum payload final.

Keluaran JSON yang dapat dibaca mesin.

## Kelola layanan Gateway

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### Instal dengan wrapper

Gunakan `--wrapper` ketika layanan terkelola harus dimulai melalui executable lain, misalnya shim pengelola secret atau helper run-as. Wrapper menerima argumen Gateway normal dan bertanggung jawab untuk pada akhirnya mengeksekusi `openclaw` atau Node dengan argumen tersebut.

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

Anda juga dapat menyetel wrapper melalui environment. `gateway install` memvalidasi bahwa path adalah file executable, menulis wrapper ke `ProgramArguments` layanan, dan menyimpan `OPENCLAW_WRAPPER` di environment layanan untuk reinstall paksa, pembaruan, dan perbaikan doctor berikutnya.

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

Untuk menghapus wrapper yang disimpan, kosongkan `OPENCLAW_WRAPPER` saat menginstal ulang:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

Opsi perintah

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

Perilaku siklus hidup

  * Gunakan `gateway restart` untuk memulai ulang layanan terkelola. Jangan merangkai `gateway stop` dan `gateway start` sebagai pengganti mulai ulang.
  * Di macOS, `gateway stop` menggunakan `launchctl bootout` secara default, yang menghapus LaunchAgent dari sesi boot saat ini tanpa menyimpan penonaktifan — pemulihan otomatis KeepAlive tetap aktif untuk crash berikutnya dan `gateway start` mengaktifkan ulang dengan bersih tanpa `launchctl enable` manual. Berikan `--disable` untuk menekan KeepAlive dan RunAtLoad secara persisten agar gateway tidak muncul kembali sampai `gateway start` eksplisit berikutnya; gunakan ini saat penghentian manual harus bertahan melewati reboot atau mulai ulang sistem.
  * `gateway restart --safe` meminta Gateway yang berjalan untuk melakukan preflight pekerjaan OpenClaw aktif dan menunda mulai ulang sampai pengiriman balasan, run tertanam, dan run tugas selesai dikosongkan. `--safe` tidak dapat digabungkan dengan `--force` atau `--wait`.
  * `gateway restart --wait 30s` menimpa anggaran drain mulai ulang yang dikonfigurasi untuk mulai ulang tersebut. Angka polos adalah milidetik; unit seperti `s`, `m`, dan `h` diterima. `--wait 0` menunggu tanpa batas.
  * `gateway restart --safe --skip-deferral` menjalankan mulai ulang aman yang sadar OpenClaw tetapi melewati gerbang penundaan sehingga Gateway memancarkan mulai ulang segera meskipun pemblokir dilaporkan. Pintu keluar operator untuk penundaan run tugas yang macet; memerlukan `--safe`.
  * `gateway restart --force` melewati drain pekerjaan aktif dan memulai ulang segera. Gunakan saat operator sudah memeriksa pemblokir tugas yang tercantum dan ingin gateway kembali sekarang.
  * Perintah siklus hidup menerima `--json` untuk scripting.

Autentikasi dan SecretRefs pada waktu instalasi

  * Saat autentikasi token memerlukan token dan `gateway.auth.token` dikelola SecretRef, `gateway install` memvalidasi bahwa SecretRef dapat di-resolve tetapi tidak menyimpan token yang di-resolve ke metadata lingkungan layanan.
  * Jika autentikasi token memerlukan token dan SecretRef token yang dikonfigurasi tidak ter-resolve, instalasi gagal tertutup alih-alih menyimpan plaintext fallback.
  * Untuk autentikasi kata sandi pada `gateway run`, pilih `OPENCLAW_GATEWAY_PASSWORD`, `--password-file`, atau `gateway.auth.password` yang didukung SecretRef daripada `--password` inline.
  * Dalam mode autentikasi tersimpul, `OPENCLAW_GATEWAY_PASSWORD` yang hanya ada di shell tidak melonggarkan persyaratan token instalasi; gunakan konfigurasi tahan lama (`gateway.auth.password` atau config `env`) saat menginstal layanan terkelola.
  * Jika `gateway.auth.token` dan `gateway.auth.password` sama-sama dikonfigurasi dan `gateway.auth.mode` belum diatur, instalasi diblokir sampai mode diatur secara eksplisit.


## Temukan gateway (Bonjour)

`gateway discover` memindai beacon Gateway (`_openclaw-gw._tcp`).

  * Multicast DNS-SD: `local.`
  * Unicast DNS-SD (Wide-Area Bonjour): pilih domain (contoh: `openclaw.internal.`) dan siapkan split DNS + server DNS; lihat [Bonjour](</id/gateway/bonjour>).


Hanya gateway dengan penemuan Bonjour yang diaktifkan (default) yang mengiklankan beacon.

Record penemuan wide-area dapat menyertakan petunjuk TXT ini:

  * `role` (petunjuk peran gateway)
  * `transport` (petunjuk transport, mis. `gateway`)
  * `gatewayPort` (port WebSocket, biasanya `18789`)
  * `sshPort` (hanya mode penemuan penuh; klien menetapkan default target SSH ke `22` saat ini tidak ada)
  * `tailnetDns` (hostname MagicDNS, bila tersedia)
  * `gatewayTls` / `gatewayTlsSha256` (TLS diaktifkan + fingerprint sertifikat)
  * `cliPath` (hanya mode penemuan penuh)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

Output yang dapat dibaca mesin (juga menonaktifkan gaya/spinner).

Contoh:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## Terkait

  * [Referensi CLI](</id/cli>)
  * [Runbook Gateway](</id/gateway>)


Was this useful?YesNo