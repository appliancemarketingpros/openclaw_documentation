---
title: Peramban
source_url: https://docs.openclaw.ai/id/cli/browser
scraped_at: 2026-05-25
---

# `openclaw browser`

Kelola permukaan kontrol peramban OpenClaw dan jalankan aksi peramban (siklus hidup, profil, tab, snapshot, tangkapan layar, navigasi, input, emulasi status, dan debugging).

Terkait:

  * Alat peramban + API: [Alat peramban](</id/tools/browser>)


## Flag umum

  * `--url <gatewayWsUrl>`: URL WebSocket Gateway (default dari konfigurasi).
  * `--token <token>`: token Gateway (jika diperlukan).
  * `--timeout <ms>`: batas waktu permintaan (ms).
  * `--expect-final`: tunggu respons final Gateway.
  * `--browser-profile <name>`: pilih profil peramban (default dari konfigurasi).
  * `--json`: output yang dapat dibaca mesin (jika didukung).


## Mulai cepat (lokal)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

Agent dapat menjalankan pemeriksaan kesiapan yang sama dengan `browser({ action: "doctor" })`.

## Pemecahan masalah cepat

Jika `start` gagal dengan `not reachable after start`, pecahkan masalah kesiapan CDP terlebih dahulu. Jika `start` dan `tabs` berhasil tetapi `open` atau `navigate` gagal, control plane peramban sehat dan kegagalan biasanya berasal dari kebijakan SSRF navigasi.

Urutan minimal:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

Panduan terperinci: [Pemecahan masalah peramban](</id/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## Siklus hidup

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

Catatan:

  * `doctor --deep` menambahkan probe snapshot langsung. Ini berguna saat kesiapan CDP dasar sudah hijau tetapi Anda ingin bukti bahwa tab saat ini dapat diperiksa.
  * Untuk profil `attachOnly` dan CDP jarak jauh, `openclaw browser stop` menutup sesi kontrol aktif dan menghapus override emulasi sementara meskipun OpenClaw tidak meluncurkan proses peramban itu sendiri.
  * Untuk profil lokal terkelola, `openclaw browser stop` menghentikan proses peramban yang dibuat.
  * `openclaw browser start --headless` hanya berlaku untuk permintaan start tersebut dan hanya saat OpenClaw meluncurkan peramban lokal terkelola. Ini tidak menulis ulang `browser.headless` atau konfigurasi profil, dan tidak berdampak untuk peramban yang sudah berjalan.
  * Pada host Linux tanpa `DISPLAY` atau `WAYLAND_DISPLAY`, profil lokal terkelola berjalan headless secara otomatis kecuali `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless=false`, atau `browser.profiles.<name>.headless=false` secara eksplisit meminta peramban yang terlihat.


## Jika perintah tidak ada

Jika `openclaw browser` adalah perintah yang tidak dikenal, periksa `plugins.allow` di `~/.openclaw/openclaw.json`.

Saat `plugins.allow` ada, cantumkan Plugin peramban bawaan secara eksplisit kecuali konfigurasi sudah memiliki blok akar `browser`:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

Blok akar `browser` eksplisit, misalnya `browser.enabled=true` atau `browser.profiles.<name>`, juga mengaktifkan Plugin peramban bawaan di bawah allowlist Plugin yang restriktif.

Terkait: [Alat peramban](</id/tools/browser#missing-browser-command-or-tool>)

## Profil

Profil adalah konfigurasi perutean peramban bernama. Dalam praktiknya:

  * `openclaw`: meluncurkan atau melampirkan ke instance Chrome khusus yang dikelola OpenClaw (direktori data pengguna terisolasi).
  * `user`: mengontrol sesi Chrome Anda yang sudah masuk melalui Chrome DevTools MCP.
  * profil CDP khusus: mengarah ke endpoint CDP lokal atau jarak jauh.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

Gunakan profil tertentu:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## Tab

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

`tabs` mengembalikan `suggestedTargetId` terlebih dahulu, lalu `tabId` stabil seperti `t1`, label opsional, dan `targetId` mentah. Agent harus meneruskan `suggestedTargetId` kembali ke `focus`, `close`, snapshot, dan aksi. Anda dapat menetapkan label dengan `open --label`, `tab new --label`, atau `tab label`; label, id tab, id target mentah, dan prefiks id target unik semuanya diterima. Saat Chromium mengganti target mentah yang mendasari selama navigasi atau pengiriman formulir, OpenClaw mempertahankan `tabId`/label stabil yang terpasang pada tab pengganti saat dapat membuktikan kecocokannya. Id target mentah tetap volatil; utamakan `suggestedTargetId`.

## Snapshot / tangkapan layar / aksi

Snapshot:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

Tangkapan layar:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

Catatan:

  * `--full-page` hanya untuk tangkapan halaman; tidak dapat digabungkan dengan `--ref` atau `--element`.
  * Profil `existing-session` / `user` mendukung tangkapan layar halaman dan tangkapan layar `--ref` dari output snapshot, tetapi tidak mendukung tangkapan layar CSS `--element`.
  * `--labels` menimpa ref snapshot saat ini pada tangkapan layar.
  * `snapshot --urls` menambahkan tujuan tautan yang ditemukan ke snapshot AI sehingga agent dapat memilih target navigasi langsung tanpa menebak hanya dari teks tautan.


Navigasi/klik/ketik (otomasi UI berbasis ref):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
[/code]

Respons aksi mengembalikan `targetId` mentah saat ini setelah penggantian halaman yang dipicu aksi ketika OpenClaw dapat membuktikan tab pengganti. Skrip tetap harus menyimpan dan meneruskan `suggestedTargetId`/label untuk alur kerja jangka panjang.

Pembantu file + dialog:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --accept
[/code]

Profil Chrome terkelola menyimpan unduhan biasa yang dipicu klik ke direktori unduhan OpenClaw (`/tmp/openclaw/downloads` secara default, atau root sementara yang dikonfigurasi). Gunakan `waitfordownload` atau `download` saat agent perlu menunggu file tertentu dan mengembalikan jalurnya; penunggu eksplisit tersebut memiliki unduhan berikutnya.

## Status dan penyimpanan

Viewport + emulasi:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

Cookie + penyimpanan:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## Debugging

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Chrome yang ada melalui MCP

Gunakan profil `user` bawaan, atau buat profil `existing-session` Anda sendiri:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser --browser-profile chrome-live tabs
[/code]

Jalur ini hanya untuk host. Untuk Docker, server headless, Browserless, atau penyiapan jarak jauh lainnya, gunakan profil CDP sebagai gantinya.

Batasan `existing-session` saat ini:

  * aksi berbasis snapshot menggunakan ref, bukan selector CSS
  * `browser.actionTimeoutMs` menetapkan default permintaan `act` yang didukung ke 60000 ms saat pemanggil menghilangkan `timeoutMs`; `timeoutMs` per panggilan tetap menang.
  * `click` hanya klik kiri
  * `type` tidak mendukung `slowly=true`
  * `press` tidak mendukung `delayMs`
  * `hover`, `scrollintoview`, `drag`, `select`, `fill`, dan `evaluate` menolak override batas waktu per panggilan
  * `select` hanya mendukung satu nilai
  * `wait --load networkidle` tidak didukung
  * unggahan file memerlukan `--ref` / `--input-ref`, tidak mendukung CSS `--element`, dan saat ini mendukung satu file pada satu waktu
  * hook dialog tidak mendukung `--timeout`
  * tangkapan layar mendukung tangkapan halaman dan `--ref`, tetapi tidak mendukung CSS `--element`
  * `responsebody`, intersepsi unduhan, ekspor PDF, dan aksi batch tetap memerlukan peramban terkelola atau profil CDP mentah


## Kontrol peramban jarak jauh (proksi host node)

Jika Gateway berjalan pada mesin yang berbeda dari peramban, jalankan **host node** pada mesin yang memiliki Chrome/Brave/Edge/Chromium. Gateway akan memproksikan aksi peramban ke node tersebut (tidak perlu server kontrol peramban terpisah).

Gunakan `gateway.nodes.browser.mode` untuk mengontrol perutean otomatis dan `gateway.nodes.browser.node` untuk menetapkan node tertentu jika beberapa node terhubung.

Keamanan + penyiapan jarak jauh: [Alat peramban](</id/tools/browser>), [Akses jarak jauh](</id/gateway/remote>), [Tailscale](</id/gateway/tailscale>), [Keamanan](</id/gateway/security>)

## Terkait

  * [Referensi CLI](</id/cli>)
  * [Peramban](</id/tools/browser>)


Was this useful?YesNo