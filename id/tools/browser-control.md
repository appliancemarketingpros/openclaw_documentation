---
title: API kontrol peramban
source_url: https://docs.openclaw.ai/id/tools/browser-control
scraped_at: 2026-05-25
---

Untuk penyiapan, konfigurasi, dan pemecahan masalah, lihat [Browser](</id/tools/browser>). Halaman ini adalah referensi untuk API HTTP kontrol lokal, CLI `openclaw browser`, dan pola skrip (snapshot, ref, tunggu, alur debug).

## API Kontrol (opsional)

Hanya untuk integrasi lokal, Gateway mengekspos API HTTP loopback kecil:

  * Status/mulai/hentikan: `GET /`, `POST /start`, `POST /stop`
  * Tab: `GET /tabs`, `POST /tabs/open`, `POST /tabs/focus`, `DELETE /tabs/:targetId`
  * Snapshot/tangkapan layar: `GET /snapshot`, `POST /screenshot`
  * Tindakan: `POST /navigate`, `POST /act`
  * Hook: `POST /hooks/file-chooser`, `POST /hooks/dialog`
  * Unduhan: `POST /download`, `POST /wait/download`
  * Izin: `POST /permissions/grant`
  * Debugging: `GET /console`, `POST /pdf`
  * Debugging: `GET /errors`, `GET /requests`, `POST /trace/start`, `POST /trace/stop`, `POST /highlight`
  * Jaringan: `POST /response/body`
  * Status: `GET /cookies`, `POST /cookies/set`, `POST /cookies/clear`
  * Status: `GET /storage/:kind`, `POST /storage/:kind/set`, `POST /storage/:kind/clear`
  * Pengaturan: `POST /set/offline`, `POST /set/headers`, `POST /set/credentials`, `POST /set/geolocation`, `POST /set/media`, `POST /set/timezone`, `POST /set/locale`, `POST /set/device`


Semua endpoint menerima `?profile=<name>`. `POST /start?headless=true` meminta peluncuran headless sekali jalan untuk profil terkelola lokal tanpa mengubah konfigurasi browser yang disimpan; profil attach-only, CDP jarak jauh, dan existing-session menolak override itu karena OpenClaw tidak meluncurkan proses browser tersebut.

Jika autentikasi gateway shared-secret dikonfigurasi, rute HTTP browser juga memerlukan autentikasi:

  * `Authorization: Bearer <gateway token>`
  * `x-openclaw-password: <gateway password>` atau autentikasi HTTP Basic dengan kata sandi tersebut


Catatan:

  * API browser loopback mandiri ini **tidak** menggunakan header identitas trusted-proxy atau Tailscale Serve.
  * Jika `gateway.auth.mode` adalah `none` atau `trusted-proxy`, rute browser loopback ini tidak mewarisi mode pembawa identitas tersebut; pertahankan agar hanya loopback.


### Kontrak error `/act`

`POST /act` menggunakan respons error terstruktur untuk validasi tingkat rute dan kegagalan kebijakan:

jsonCopy code
[code]
    { "error": "<message>", "code": "ACT_*" }
[/code]

Nilai `code` saat ini:

  * `ACT_KIND_REQUIRED` (HTTP 400): `kind` hilang atau tidak dikenali.
  * `ACT_INVALID_REQUEST` (HTTP 400): payload tindakan gagal dinormalisasi atau divalidasi.
  * `ACT_SELECTOR_UNSUPPORTED` (HTTP 400): `selector` digunakan dengan jenis tindakan yang tidak didukung.
  * `ACT_EVALUATE_DISABLED` (HTTP 403): `evaluate` (atau `wait --fn`) dinonaktifkan oleh konfigurasi.
  * `ACT_TARGET_ID_MISMATCH` (HTTP 403): `targetId` tingkat atas atau batch bertentangan dengan target permintaan.
  * `ACT_EXISTING_SESSION_UNSUPPORTED` (HTTP 501): tindakan tidak didukung untuk profil existing-session.


Kegagalan runtime lain mungkin masih mengembalikan `{ "error": "<message>" }` tanpa kolom `code`.

### Persyaratan Playwright

Beberapa fitur (navigate/act/snapshot AI/snapshot peran, tangkapan layar elemen, PDF) memerlukan Playwright. Jika Playwright tidak terpasang, endpoint tersebut mengembalikan error 501 yang jelas.

Yang tetap berfungsi tanpa Playwright:

  * Snapshot ARIA
  * Snapshot aksesibilitas bergaya peran (`--interactive`, `--compact`, `--depth`, `--efficient`) saat WebSocket CDP per tab tersedia. Ini adalah fallback untuk inspeksi dan penemuan ref; Playwright tetap menjadi mesin tindakan utama.
  * Tangkapan layar halaman untuk browser `openclaw` terkelola saat WebSocket CDP per tab tersedia
  * Tangkapan layar halaman untuk profil `existing-session` / Chrome MCP
  * Tangkapan layar berbasis ref `existing-session` (`--ref`) dari output snapshot


Yang masih memerlukan Playwright:

  * `navigate`
  * `act`
  * Snapshot AI yang bergantung pada format snapshot AI native Playwright
  * Tangkapan layar elemen dengan selector CSS (`--element`)
  * ekspor PDF browser penuh


Tangkapan layar elemen juga menolak `--full-page`; rute mengembalikan `fullPage is not supported for element screenshots`.

Jika Anda melihat `Playwright is not available in this gateway build`, Gateway paket tidak memiliki dependensi runtime browser inti. Pasang ulang atau perbarui OpenClaw, lalu mulai ulang gateway. Untuk Docker, pasang juga binary browser Chromium seperti ditunjukkan di bawah.

#### Instalasi Docker Playwright

Jika Gateway Anda berjalan di Docker, hindari `npx playwright` (konflik override npm). Untuk image kustom, masukkan Chromium ke dalam image:

bashCopy code
[code]
    OPENCLAW_INSTALL_BROWSER=1 ./scripts/docker/setup.sh
[/code]

Untuk image yang sudah ada, pasang melalui CLI bawaan sebagai gantinya:

bashCopy code
[code]
    docker compose run --rm openclaw-cli \  node /app/node_modules/playwright-core/cli.js install chromium
[/code]

Untuk mempertahankan unduhan browser, tetapkan `PLAYWRIGHT_BROWSERS_PATH` (misalnya, `/home/node/.cache/ms-playwright`) dan pastikan `/home/node` dipertahankan melalui `OPENCLAW_HOME_VOLUME` atau bind mount. OpenClaw mendeteksi otomatis Chromium yang dipertahankan di Linux. Lihat [Docker](</id/install/docker>).

## Cara kerjanya (internal)

Server kontrol loopback kecil menerima permintaan HTTP dan terhubung ke browser berbasis Chromium melalui CDP. Tindakan lanjutan (klik/ketik/snapshot/PDF) melewati Playwright di atas CDP; saat Playwright tidak ada, hanya operasi non-Playwright yang tersedia. Agen melihat satu antarmuka stabil sementara browser dan profil lokal/jarak jauh dapat berganti bebas di bawahnya.

## Referensi cepat CLI

Semua perintah menerima `--browser-profile <name>` untuk menargetkan profil tertentu, dan `--json` untuk output yang dapat dibaca mesin.

Basics: status, tabs, open/focus/close bashCopy code
[code]
    openclaw browser statusopenclaw browser startopenclaw browser start --headless # one-shot local managed headless launchopenclaw browser stop            # also clears emulation on attach-only/remote CDPopenclaw browser tabsopenclaw browser tab             # shortcut for current tabopenclaw browser tab newopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://example.comopenclaw browser focus abcd1234openclaw browser close abcd1234
[/code]

Inspection: screenshot, snapshot, console, errors, requests bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref 12        # or --ref e12openclaw browser screenshot --labelsopenclaw browser snapshotopenclaw browser snapshot --format aria --limit 200openclaw browser snapshot --interactive --compact --depth 6openclaw browser snapshot --efficientopenclaw browser snapshot --labelsopenclaw browser snapshot --urlsopenclaw browser snapshot --selector "#main" --interactiveopenclaw browser snapshot --frame "iframe#main" --interactiveopenclaw browser console --level erroropenclaw browser errors --clearopenclaw browser requests --filter api --clearopenclaw browser pdfopenclaw browser responsebody "**/api" --max-chars 5000
[/code]

Actions: navigate, click, type, drag, wait, evaluate bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser resize 1280 720openclaw browser click 12 --double           # or e12 for role refsopenclaw browser click-coords 120 340        # viewport coordinatesopenclaw browser type 23 "hello" --submitopenclaw browser press Enteropenclaw browser hover 44openclaw browser scrollintoview e12openclaw browser drag 10 11openclaw browser select 9 OptionA OptionBopenclaw browser download e12 report.pdfopenclaw browser waitfordownload report.pdfopenclaw browser upload /tmp/openclaw/uploads/file.pdfopenclaw browser fill --fields '[{"ref":"1","type":"text","value":"Ada"}]'openclaw browser dialog --acceptopenclaw browser wait --text "Done"openclaw browser wait "#main" --url "**/dash" --load networkidle --fn "window.ready===true"openclaw browser evaluate --fn '(el) => el.textContent' --ref 7openclaw browser highlight e12openclaw browser trace startopenclaw browser trace stop
[/code]

State: cookies, storage, offline, headers, geo, device bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url "https://example.com"openclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set theme darkopenclaw browser storage session clearopenclaw browser set offline onopenclaw browser set headers --headers-json '{"X-Debug":"1"}'openclaw browser set credentials user pass            # --clear to removeopenclaw browser set geo 37.7749 -122.4194 --origin "https://example.com"openclaw browser set media darkopenclaw browser set timezone America/New_Yorkopenclaw browser set locale en-USopenclaw browser set device "iPhone 14"
[/code]

Catatan:

  * `upload` dan `dialog` adalah panggilan **arming** ; jalankan sebelum klik/tekan yang memicu pemilih/dialog.
  * `click`/`type`/dll. memerlukan `ref` dari `snapshot` (numerik `12`, ref peran `e12`, atau ref ARIA yang dapat ditindaklanjuti `ax12`). Selector CSS sengaja tidak didukung untuk tindakan. Gunakan `click-coords` saat posisi viewport yang terlihat adalah satu-satunya target yang andal.
  * Jalur unduhan, trace, dan unggahan dibatasi ke root sementara OpenClaw: `/tmp/openclaw{,/downloads,/uploads}` (fallback: `${os.tmpdir()}/openclaw/...`).
  * `upload` juga dapat menetapkan input file secara langsung melalui `--input-ref` atau `--element`.


ID dan label tab stabil bertahan dari penggantian raw-target Chromium saat OpenClaw dapat membuktikan tab penggantinya, seperti URL yang sama atau satu tab lama menjadi satu tab baru setelah pengiriman formulir. ID target mentah tetap volatil; utamakan `suggestedTargetId` dari `tabs` dalam skrip.

Ringkasan flag snapshot:

  * `--format ai` (default dengan Playwright): snapshot AI dengan ref numerik (`aria-ref="<n>"`).
  * `--format aria`: pohon aksesibilitas dengan ref `axN`. Saat Playwright tersedia, OpenClaw mengikat ref dengan ID DOM backend ke halaman langsung agar tindakan lanjutan dapat menggunakannya; jika tidak, perlakukan output sebagai hanya untuk inspeksi.
  * `--efficient` (atau `--mode efficient`): preset snapshot peran ringkas. Tetapkan `browser.snapshotDefaults.mode: "efficient"` untuk menjadikannya default (lihat [Konfigurasi Gateway](</id/gateway/configuration-reference#browser>)).
  * `--interactive`, `--compact`, `--depth`, `--selector` memaksa snapshot peran dengan ref `ref=e12`. `--frame "<iframe>"` membatasi snapshot peran ke iframe.
  * `--labels` menambahkan tangkapan layar khusus viewport dengan label ref yang ditumpangkan (mencetak `MEDIA:<path>`).
  * `--urls` menambahkan tujuan tautan yang ditemukan ke snapshot AI.


## Snapshot dan ref

OpenClaw mendukung dua gaya "snapshot":

  * **Snapshot AI (ref numerik)** : `openclaw browser snapshot` (default; `--format ai`)

    * Output: snapshot teks yang menyertakan ref numerik.
    * Tindakan: `openclaw browser click 12`, `openclaw browser type 23 "hello"`.
    * Secara internal, ref diselesaikan melalui `aria-ref` Playwright.
  * **Snapshot peran (ref peran seperti`e12`)**: `openclaw browser snapshot --interactive` (atau `--compact`, `--depth`, `--selector`, `--frame`)

    * Output: daftar/pohon berbasis peran dengan `[ref=e12]` (dan opsional `[nth=1]`).
    * Tindakan: `openclaw browser click e12`, `openclaw browser highlight e12`.
    * Secara internal, ref diselesaikan melalui `getByRole(...)` (ditambah `nth()` untuk duplikat).
    * Tambahkan `--labels` untuk menyertakan tangkapan layar viewport dengan label `e12` yang ditumpangkan.
    * Tambahkan `--urls` saat teks tautan ambigu dan agen memerlukan target navigasi konkret.
  * **Snapshot ARIA (ref ARIA seperti`ax12`)**: `openclaw browser snapshot --format aria`

    * Output: pohon aksesibilitas sebagai node terstruktur.
    * Tindakan: `openclaw browser click ax12` berfungsi saat path snapshot dapat mengikat ref melalui Playwright dan id DOM backend Chrome.
  * Jika Playwright tidak tersedia, snapshot ARIA masih dapat berguna untuk inspeksi, tetapi ref mungkin tidak dapat ditindaklanjuti. Ambil snapshot ulang dengan `--format ai` atau `--interactive` saat Anda membutuhkan ref tindakan.

  * Bukti Docker untuk path fallback raw-CDP: `pnpm test:docker:browser-cdp-snapshot` memulai Chromium dengan CDP, menjalankan `browser doctor --deep`, dan memverifikasi snapshot role menyertakan URL tautan, elemen yang dapat diklik yang dipromosikan kursor, dan metadata iframe.


Perilaku ref:

  * Ref **tidak stabil antar navigasi** ; jika sesuatu gagal, jalankan ulang `snapshot` dan gunakan ref baru.
  * `/act` mengembalikan `targetId` raw saat ini setelah penggantian yang dipicu tindakan ketika dapat membuktikan tab pengganti. Tetap gunakan id/label tab yang stabil untuk perintah lanjutan.
  * Jika snapshot role diambil dengan `--frame`, ref role dicakup ke iframe tersebut hingga snapshot role berikutnya.
  * Ref `axN` yang tidak dikenal atau sudah usang gagal cepat alih-alih jatuh ke selector `aria-ref` Playwright. Jalankan snapshot baru pada tab yang sama saat hal itu terjadi.


## Peningkatan kemampuan wait

Anda dapat menunggu lebih dari sekadar waktu/teks:

  * Tunggu URL (glob didukung oleh Playwright): 
    * `openclaw browser wait --url "**/dash"`
  * Tunggu status pemuatan: 
    * `openclaw browser wait --load networkidle`
  * Tunggu predicate JS: 
    * `openclaw browser wait --fn "window.ready===true"`
  * Tunggu selector menjadi terlihat: 
    * `openclaw browser wait "#main"`


Ini dapat digabungkan:

bashCopy code
[code]
    openclaw browser wait "#main" \  --url "**/dash" \  --load networkidle \  --fn "window.ready===true" \  --timeout-ms 15000
[/code]

## Alur kerja debug

Saat tindakan gagal (mis. "not visible", "strict mode violation", "covered"):

  1. `openclaw browser snapshot --interactive`
  2. Gunakan `click <ref>` / `type <ref>` (utamakan ref role dalam mode interaktif)
  3. Jika masih gagal: `openclaw browser highlight <ref>` untuk melihat apa yang ditargetkan Playwright
  4. Jika halaman berperilaku aneh: 
     * `openclaw browser errors --clear`
     * `openclaw browser requests --filter api --clear`
  5. Untuk debugging mendalam: rekam trace: 
     * `openclaw browser trace start`
     * reproduksi masalahnya
     * `openclaw browser trace stop` (mencetak `TRACE:<path>`)


## Output JSON

`--json` digunakan untuk scripting dan tooling terstruktur.

Contoh:

bashCopy code
[code]
    openclaw browser status --jsonopenclaw browser snapshot --interactive --jsonopenclaw browser requests --filter api --jsonopenclaw browser cookies --json
[/code]

Snapshot role dalam JSON menyertakan `refs` plus blok `stats` kecil (lines/chars/refs/interactive) sehingga tool dapat menalar ukuran dan kepadatan payload.

## Pengaturan status dan lingkungan

Ini berguna untuk alur kerja "buat situs berperilaku seperti X":

  * Cookie: `cookies`, `cookies set`, `cookies clear`
  * Storage: `storage local|session get|set|clear`
  * Offline: `set offline on|off`
  * Header: `set headers --headers-json '{"X-Debug":"1"}'` (legacy `set headers --json '{"X-Debug":"1"}'` tetap didukung)
  * HTTP basic auth: `set credentials user pass` (atau `--clear`)
  * Geolokasi: `set geo <lat> <lon> --origin "https://example.com"` (atau `--clear`)
  * Media: `set media dark|light|no-preference|none`
  * Zona waktu / locale: `set timezone ...`, `set locale ...`
  * Perangkat / viewport: 
    * `set device "iPhone 14"` (preset perangkat Playwright)
    * `set viewport 1280 720`


## Keamanan dan privasi

  * Profil browser openclaw dapat berisi sesi yang sudah login; perlakukan sebagai sensitif.
  * `browser act kind=evaluate` / `openclaw browser evaluate` dan `wait --fn` menjalankan JavaScript arbitrer dalam konteks halaman. Prompt injection dapat mengarahkan ini. Nonaktifkan dengan `browser.evaluateEnabled=false` jika Anda tidak membutuhkannya.
  * Untuk login dan catatan anti-bot (X/Twitter, dll.), lihat [Login browser + posting X/Twitter](</id/tools/browser-login>).
  * Jaga host Gateway/node tetap privat (loopback atau hanya tailnet).
  * Endpoint CDP jarak jauh sangat kuat; tunnel dan lindungi endpoint tersebut.


Contoh strict-mode (blokir tujuan privat/internal secara default):

json5Copy code
[code]
    {  browser: {    ssrfPolicy: {      dangerouslyAllowPrivateNetwork: false,      hostnameAllowlist: ["*.example.com", "example.com"],      allowedHostnames: ["localhost"], // optional exact allow    },  },}
[/code]

## Terkait

  * [Browser](</id/tools/browser>) \- ikhtisar, konfigurasi, profil, keamanan
  * [Login browser](</id/tools/browser-login>) \- masuk ke situs
  * [Pemecahan masalah Browser Linux](</id/tools/browser-linux-troubleshooting>)
  * [Pemecahan masalah Browser WSL2](</id/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo