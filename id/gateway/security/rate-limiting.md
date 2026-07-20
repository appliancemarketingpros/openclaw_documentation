---
title: Pembatasan laju
source_url: https://docs.openclaw.ai/id/gateway/security/rate-limiting
scraped_at: 2026-07-20
---

Gateway & OpsGateway

Gateway menerapkan beberapa batas laju yang independen. Batas-batas tersebut melindungi batas sistem yang berbeda, menggunakan identitas yang berbeda sebagai kunci, dan menghasilkan bentuk kesalahan yang berbeda. Halaman ini adalah referensi untuk semuanya.

Sekilas:

Permukaan | Batas (bawaan) | Dikunci berdasarkan | Dapat dikonfigurasi  
---|---|---|---  
Autentikasi gagal (token/kata sandi/perangkat) | 10 kegagalan / 60 dtk, penguncian 5 mnt | IP + cakupan kredensial | `gateway.auth.rateLimit`  
Kegagalan autentikasi WS dari browser | sama, loopback **tidak** dikecualikan | IP, atau origin halaman dari loopback | `gateway.auth.rateLimit`  
Kegagalan autentikasi Webhook (`/hooks`) | 20 kegagalan / 60 dtk, penguncian 60 dtk | IP | tidak  
RPC penulisan bidang kontrol | 30 permintaan / 60 dtk per metode | metode + perangkat + IP | tidak  
Pembuatan sesi ACP | 120 sesi / 10 dtk | instans penerjemah | internal  
Siklus mulai ulang Gateway | jeda 30 dtk antar mulai ulang | proses | tidak  
  
## Percobaan autentikasi (praautentikasi)

Percobaan autentikasi yang gagal dibatasi lajunya per IP klien, sebelum penanganan permintaan apa pun. Ini adalah perlindungan terhadap serangan brute force untuk Gateway yang terekspos.

  * Hanya kredensial yang _salah_ yang dihitung. Kredensial yang tidak ada (klien yang tidak pernah mengirim token) dan autentikasi yang berhasil tidak menghabiskan kuota; autentikasi yang berhasil mengatur ulang penghitung untuk IP tersebut.
  * Bawaan: 10 kegagalan per 60 detik, lalu penguncian selama 5 menit untuk IP tersebut.
  * Loopback (`127.0.0.1` / `::1`) dikecualikan secara bawaan agar sesi CLI lokal tidak dapat terkunci.
  * Penghitung dicakup per kelas kredensial, sehingga banjir serangan terhadap satu permukaan tidak menggeser permukaan lain. Cakupan mencakup token/kata sandi Gateway bersama, token perangkat, pemasangan Node, persetujuan ulang Node yang telah dipasangkan, token bootstrap perangkat, dan penerbitan tantangan watchOS.


Selama terkunci, percobaan koneksi gagal dengan:

jsonCopy code
[code]
    {  "code": "INVALID_REQUEST",  "message": "unauthorized: too many failed authentication attempts (retry later)",  "retryable": true,  "retryAfterMs": 297000,  "details": {    "code": "AUTH_RATE_LIMITED",    "authReason": "rate_limited",    "recommendedNextStep": "wait_then_retry"  }}
[/code]

Percobaan dari IP lain (termasuk loopback) tidak terpengaruh selama penguncian.

Sesuaikan di bawah `gateway.auth.rateLimit` dalam `openclaw.json`:

jsonCopy code
[code]
    {  "gateway": {    "auth": {      "rateLimit": {        "maxAttempts": 10,        "windowMs": 60000,        "lockoutMs": 300000,        "exemptLoopback": true      }    }  }}
[/code]

Entri `AUTH_RATE_LIMITED` yang berulang dalam log Gateway berarti seseorang sedang menebak kredensial; lihat [panduan paparan](</id/gateway/security/exposure-runbook>).

### Koneksi dari browser

Koneksi WebSocket yang membawa header `Origin` browser menggunakan batas yang sama, tetapi pengecualian loopback **selalu dinonaktifkan** — halaman berbahaya dalam browser lokal tetap merupakan klien yang tidak tepercaya, sehingga localhost tidak mendapatkan pengecualian pada jalur tersebut. Ketika koneksi seperti itu tiba _dari_ alamat loopback, kegagalannya dikunci berdasarkan origin halaman yang dinormalisasi (misalnya `browser-origin:https://evil.example`), bukan IP loopback bersama, sehingga setiap origin memiliki bucket sendiri; dari alamat non-loopback, kuncinya tetap berupa IP klien. Hal ini tidak dapat dikonfigurasi.

### Webhook

Ingress HTTP `/hooks` memiliki pembatas kegagalannya sendiri: 20 autentikasi gagal per 60 detik per IP klien, lalu penguncian selama 60 detik. Loopback tidak dikecualikan. Autentikasi hook yang berhasil mengatur ulang penghitung. Permintaan yang dibatasi menerima HTTP `429 Too Many Requests` biasa dengan header `Retry-After` (detik). Batasnya tetap; jika integrasi yang sah memicu batas ini, perbaiki kredensialnya alih-alih mencoba ulang dengan lebih agresif.

## Penulisan bidang kontrol (perlindungan pascaautentikasi)

RPC admin sisi penulisan (`config.apply`, `config.patch`, `plugins.install`, `plugins.setEnabled`, `plugins.uninstall`, `update.run`, `worktrees.*`, `gateway.restart.request`, ...) juga dibatasi lajunya **setelah** otorisasi: 30 permintaan per 60 detik, per metode, per `deviceId+clientIp`.

Ini bukan batas keamanan — pemanggil sudah memiliki `operator.admin` — melainkan perlindungan yang membatasi loop klien atau agen tak terkendali yang membebani operasi mahal. Penggunaan interaktif tidak pernah mencapai batas ini; setiap metode memiliki bucket sendiri, sehingga mengaktifkan atau menonaktifkan Plugin tidak menghabiskan kuota penulisan konfigurasi.

Ketika batas terlampaui, permintaan gagal dengan kesalahan yang dapat dicoba ulang:

jsonCopy code
[code]
    {  "code": "UNAVAILABLE",  "message": "rate limit exceeded for config.patch; retry after 35s",  "retryable": true,  "retryAfterMs": 34539,  "details": { "method": "config.patch", "limit": "30 per 60s" }}
[/code]

Klien harus mematuhi `retryAfterMs`. Batas ini tetap (tidak dapat dikonfigurasi); bucket kedaluwarsa dengan sendirinya dan dibersihkan oleh pemeliharaan Gateway.

## Pembuatan sesi ACP

Penerjemah ACP membatasi pembuatan sesi hingga 120 sesi baru per jendela 10 detik per instans penerjemah. Melebihinya menyebabkan permintaan gagal dengan kesalahan yang pesannya memuat waktu tunggu (tidak ada bidang `retryAfterMs` terstruktur pada jalur ini):

CodeCopy code
[code]
    Batas laju pembuatan sesi ACP terlampaui untuk <method>; coba lagi setelah <n> dtk.
[/code]

Hal ini membatasi klien tak terkendali yang membuat sesi dalam sebuah loop; penggunaan IDE dan agen normal tetap jauh di bawah batas tersebut.

## Jeda mulai ulang

Permintaan mulai ulang Gateway digabungkan, lalu menerapkan jeda 30 detik di antara siklus mulai ulang. Mulai ulang yang diminta selama masa jeda dijadwalkan setelah masa tersebut berakhir, bukan ditolak. Ini terpisah dari pembatas bidang kontrol di atas: `gateway.restart.request` menggunakan satu slot kuota bidang kontrol _dan_ mulai ulang yang dihasilkan mematuhi jeda tersebut.

## Catatan operasional

  * Semua pembatas berada dalam memori dan berlaku per proses, serta beberapa Gateway tidak berbagi status. Mengganti proses Gateway menghapus penghitung yang dimiliki Gateway (penguncian autentikasi, pembatasan Webhook, bucket bidang kontrol). Jeda mulai ulang sengaja bertahan selama siklus mulai ulang dalam proses — hal itulah yang dibatasinya — dan hanya diatur ulang bersama proses. Batas sesi ACP dimiliki oleh instans penerjemahnya dan diatur ulang ketika instans tersebut dibuat ulang, bukan saat Gateway dimulai ulang.
  * Peta bucket dibatasi (batas maksimum entri tetap ditambah pembersihan berkala), sehingga banjir kunci unik tidak dapat meningkatkan penggunaan memori tanpa batas.
  * Ketika klien berada di belakang proksi terbalik, IP efektifnya adalah IP klien yang telah ditentukan; lihat [autentikasi proksi tepercaya](</id/gateway/trusted-proxy-auth>) untuk mengetahui cara header proksi divalidasi sebelum dapat memengaruhinya.
  * Pensinyalan percobaan ulang berbeda menurut permukaan: pembatas RPC Gateway mengembalikan `retryable: true` beserta `retryAfterMs`, ingress Webhook menggunakan HTTP 429 dengan header `Retry-After`, dan ACP menyematkan waktu tunggu dalam pesan kesalahan. Dalam setiap kasus, tunggu selama durasi yang ditunjukkan alih-alih langsung mencoba lagi.


Was this useful?YesNo

Open issue