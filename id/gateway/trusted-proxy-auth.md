---
title: Autentikasi proksi tepercaya
source_url: https://docs.openclaw.ai/id/gateway/trusted-proxy-auth
scraped_at: 2026-05-25
---

## Kapan menggunakan

Gunakan mode auth `trusted-proxy` ketika:

  * Anda menjalankan OpenClaw di belakang **proxy sadar-identitas** (Pomerium, Caddy + OAuth, nginx + oauth2-proxy, Traefik + forward auth).
  * Proxy Anda menangani semua autentikasi dan meneruskan identitas pengguna melalui header.
  * Anda berada di lingkungan Kubernetes atau container tempat proxy menjadi satu-satunya jalur ke Gateway.
  * Anda mengalami error WebSocket `1008 unauthorized` karena browser tidak dapat meneruskan token dalam payload WS.


## Kapan TIDAK menggunakan

  * Jika proxy Anda tidak mengautentikasi pengguna (hanya terminator TLS atau load balancer).
  * Jika ada jalur apa pun ke Gateway yang melewati proxy (celah firewall, akses jaringan internal).
  * Jika Anda tidak yakin apakah proxy Anda menghapus/menimpa header yang diteruskan dengan benar.
  * Jika Anda hanya memerlukan akses pribadi untuk satu pengguna (pertimbangkan Tailscale Serve + loopback untuk penyiapan yang lebih sederhana).


## Cara kerjanya

* ### Proxy mengautentikasi pengguna

Proxy balik Anda mengautentikasi pengguna (OAuth, OIDC, SAML, dan sebagainya).

* ### Proxy menambahkan header identitas

Proxy menambahkan header dengan identitas pengguna yang diautentikasi (misalnya, `x-forwarded-user: nick@example.com`).

* ### Gateway memverifikasi sumber tepercaya

OpenClaw memeriksa bahwa permintaan berasal dari **IP proxy tepercaya** (dikonfigurasi di `gateway.trustedProxies`).

* ### Gateway mengekstrak identitas

OpenClaw mengekstrak identitas pengguna dari header yang dikonfigurasi.

* ### Otorisasi

Jika semuanya lolos pemeriksaan, permintaan diotorisasi.

## Perilaku penyandingan Control UI

Saat `gateway.auth.mode = "trusted-proxy"` aktif dan permintaan lolos pemeriksaan trusted-proxy, sesi WebSocket Control UI dapat terhubung tanpa identitas penyandingan perangkat.

Implikasi:

  * Penyandingan tidak lagi menjadi gerbang utama untuk akses Control UI dalam mode ini.
  * Kebijakan auth proxy balik Anda dan `allowUsers` menjadi kontrol akses efektif.
  * Kunci ingress gateway hanya ke IP proxy tepercaya (`gateway.trustedProxies` \+ firewall).


## Konfigurasi

json5Copy code
[code]
    {  gateway: {    // Trusted-proxy auth expects requests from a non-loopback trusted proxy source by default    bind: "lan",     // CRITICAL: Only add your proxy's IP(s) here    trustedProxies: ["10.0.0.1", "172.17.0.1"],     auth: {      mode: "trusted-proxy",      trustedProxy: {        // Header containing authenticated user identity (required)        userHeader: "x-forwarded-user",         // Optional: headers that MUST be present (proxy verification)        requiredHeaders: ["x-forwarded-proto", "x-forwarded-host"],         // Optional: restrict to specific users (empty = allow all)        allowUsers: ["nick@example.com", "admin@company.org"],         // Optional: allow a same-host loopback proxy after explicit opt-in        allowLoopback: false,      },    },  },}
[/code]

### Referensi konfigurasi

Array alamat IP proxy yang akan dipercaya. Permintaan dari IP lain ditolak.

Harus berupa `"trusted-proxy"`.

Nama header yang berisi identitas pengguna yang diautentikasi.

Header tambahan yang harus ada agar permintaan dipercaya.

Allowlist identitas pengguna. Kosong berarti mengizinkan semua pengguna yang diautentikasi.

Dukungan opt-in untuk proxy balik loopback pada host yang sama. Default ke `false`.

## Terminasi TLS dan HSTS

Gunakan satu titik terminasi TLS dan terapkan HSTS di sana.

### Terminasi TLS proxy (direkomendasikan)

Saat proxy balik Anda menangani HTTPS untuk `https://control.example.com`, tetapkan `Strict-Transport-Security` pada proxy untuk domain tersebut.

  * Cocok untuk deployment yang menghadap internet.
  * Menjaga kebijakan sertifikat + pengerasan HTTP di satu tempat.
  * OpenClaw dapat tetap menggunakan HTTP loopback di belakang proxy.


Contoh nilai header:

textCopy code
[code]
    Strict-Transport-Security: max-age=31536000; includeSubDomains
[/code]

### Terminasi TLS Gateway

Jika OpenClaw sendiri melayani HTTPS secara langsung (tanpa proxy terminasi TLS), tetapkan:

json5Copy code
[code]
    {  gateway: {    tls: { enabled: true },    http: {      securityHeaders: {        strictTransportSecurity: "max-age=31536000; includeSubDomains",      },    },  },}
[/code]

`strictTransportSecurity` menerima nilai header string, atau `false` untuk menonaktifkan secara eksplisit.

### Panduan rollout

  * Mulai dengan usia maksimum pendek terlebih dahulu (misalnya `max-age=300`) saat memvalidasi traffic.
  * Tingkatkan ke nilai berumur panjang (misalnya `max-age=31536000`) hanya setelah keyakinan tinggi.
  * Tambahkan `includeSubDomains` hanya jika setiap subdomain siap HTTPS.
  * Gunakan preload hanya jika Anda sengaja memenuhi persyaratan preload untuk seluruh kumpulan domain Anda.
  * Pengembangan lokal khusus loopback tidak mendapat manfaat dari HSTS.


## Contoh penyiapan proxy

Pomerium

Pomerium meneruskan identitas dalam `x-pomerium-claim-email` (atau header klaim lain) dan JWT dalam `x-pomerium-jwt-assertion`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Pomerium's IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-pomerium-claim-email",        requiredHeaders: ["x-pomerium-jwt-assertion"],      },    },  },}
[/code]

Cuplikan konfigurasi Pomerium:

yamlCopy code
[code]
    routes:  - from: https://openclaw.example.com    to: http://openclaw-gateway:18789    policy:      - allow:          or:            - email:                is: nick@example.com    pass_identity_headers: true
[/code]

Caddy dengan OAuth

Caddy dengan Plugin `caddy-security` dapat mengautentikasi pengguna dan meneruskan header identitas.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Caddy/sidecar proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

Cuplikan Caddyfile:

CodeCopy code
[code]
    openclaw.example.com {    authenticate with oauth2_provider    authorize with policy1     reverse_proxy openclaw:18789 {        header_up X-Forwarded-User {http.auth.user.email}    }}
[/code]

nginx + oauth2-proxy

oauth2-proxy mengautentikasi pengguna dan meneruskan identitas dalam `x-auth-request-email`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // nginx/oauth2-proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-auth-request-email",      },    },  },}
[/code]

Cuplikan konfigurasi nginx:

nginxCopy code
[code]
    location / {    auth_request /oauth2/auth;    auth_request_set $user $upstream_http_x_auth_request_email;     proxy_pass http://openclaw:18789;    proxy_set_header X-Auth-Request-Email $user;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "upgrade";}
[/code]

Traefik dengan forward auth json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["172.17.0.1"], // Traefik container IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

## Konfigurasi token campuran

OpenClaw menolak konfigurasi ambigu ketika `gateway.auth.token` (atau `OPENCLAW_GATEWAY_TOKEN`) dan mode `trusted-proxy` aktif secara bersamaan. Konfigurasi token campuran dapat menyebabkan permintaan loopback diam-diam diautentikasi pada jalur auth yang salah.

Jika Anda melihat error `mixed_trusted_proxy_token` saat startup:

  * Hapus token bersama saat menggunakan mode trusted-proxy, atau
  * Alihkan `gateway.auth.mode` ke `"token"` jika Anda bermaksud menggunakan auth berbasis token.


Header identitas trusted-proxy loopback tetap gagal tertutup: pemanggil pada host yang sama tidak diautentikasi diam-diam sebagai pengguna proxy. Pemanggil OpenClaw internal yang melewati proxy dapat mengautentikasi dengan `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD` sebagai gantinya. Fallback token tetap sengaja tidak didukung dalam mode trusted-proxy.

## Header cakupan operator

Auth trusted-proxy adalah mode HTTP **pembawa identitas** , sehingga pemanggil dapat secara opsional mendeklarasikan cakupan operator dengan `x-openclaw-scopes`.

Contoh:

  * `x-openclaw-scopes: operator.read`
  * `x-openclaw-scopes: operator.read,operator.write`
  * `x-openclaw-scopes: operator.admin,operator.write`


Perilaku:

  * Saat header ada, OpenClaw menghormati kumpulan cakupan yang dideklarasikan.
  * Saat header ada tetapi kosong, permintaan mendeklarasikan **tanpa** cakupan operator.
  * Saat header tidak ada, API HTTP pembawa identitas normal fallback ke kumpulan cakupan default operator standar.
  * **Route HTTP Plugin** gateway-auth lebih sempit secara default: saat `x-openclaw-scopes` tidak ada, cakupan runtime-nya fallback ke `operator.write`.
  * Permintaan HTTP asal browser masih harus lolos `gateway.controlUi.allowedOrigins` (atau mode fallback Host-header yang disengaja) bahkan setelah auth trusted-proxy berhasil.


Aturan praktis: kirim `x-openclaw-scopes` secara eksplisit saat Anda ingin permintaan trusted-proxy lebih sempit daripada default, atau saat route Plugin gateway-auth memerlukan sesuatu yang lebih kuat daripada cakupan tulis.

## Checklist keamanan

Sebelum mengaktifkan autentikasi trusted-proxy, verifikasi:

  * [ ] **Proxy adalah satu-satunya jalur** : Port Gateway dibatasi firewall dari semuanya kecuali proxy Anda.
  * [ ] **trustedProxies minimal** : Hanya IP proxy aktual Anda, bukan seluruh subnet.
  * [ ] **Sumber proxy loopback disengaja** : Autentikasi trusted-proxy gagal tertutup untuk permintaan bersumber loopback kecuali `gateway.auth.trustedProxy.allowLoopback` diaktifkan secara eksplisit untuk proxy pada host yang sama.
  * [ ] **Proxy menghapus header** : Proxy Anda menimpa (bukan menambahkan) header `x-forwarded-*` dari klien.
  * [ ] **Terminasi TLS** : Proxy Anda menangani TLS; pengguna terhubung melalui HTTPS.
  * [ ] **allowedOrigins eksplisit** : Control UI non-loopback menggunakan `gateway.controlUi.allowedOrigins` yang eksplisit.
  * [ ] **allowUsers disetel** (direkomendasikan): Batasi ke pengguna yang diketahui, bukan mengizinkan siapa pun yang terautentikasi.
  * [ ] **Tidak ada konfigurasi token campuran** : Jangan setel `gateway.auth.token` dan `gateway.auth.mode: "trusted-proxy"` sekaligus.
  * [ ] **Fallback kata sandi lokal bersifat privat** : Jika Anda mengonfigurasi `gateway.auth.password` untuk pemanggil langsung internal, tetap batasi port Gateway dengan firewall agar klien jarak jauh non-proxy tidak dapat mencapainya secara langsung.


## Audit keamanan

`openclaw security audit` akan menandai autentikasi trusted-proxy dengan temuan tingkat keparahan **critical**. Ini disengaja — ini adalah pengingat bahwa Anda mendelegasikan keamanan ke pengaturan proxy Anda.

Audit memeriksa:

  * Peringatan/pengingat kritis dasar `gateway.trusted_proxy_auth`
  * Konfigurasi `trustedProxies` yang hilang
  * Konfigurasi `userHeader` yang hilang
  * `allowUsers` kosong (mengizinkan pengguna terautentikasi mana pun)
  * `allowLoopback` yang diaktifkan untuk sumber proxy pada host yang sama
  * Kebijakan origin browser wildcard atau hilang pada permukaan Control UI yang terekspos


## Pemecahan masalah

trusted_proxy_untrusted_source

Permintaan tidak berasal dari IP di `gateway.trustedProxies`. Periksa:

  * Apakah IP proxy sudah benar? (IP container Docker dapat berubah.)
  * Apakah ada load balancer di depan proxy Anda?
  * Gunakan `docker inspect` atau `kubectl get pods -o wide` untuk menemukan IP aktual.

trusted_proxy_loopback_source

OpenClaw menolak permintaan trusted-proxy bersumber loopback.

Periksa:

  * Apakah proxy terhubung dari `127.0.0.1` / `::1`?
  * Apakah Anda mencoba menggunakan autentikasi trusted-proxy dengan reverse proxy loopback pada host yang sama?


Perbaikan:

  * Lebih baik gunakan autentikasi token/kata sandi untuk klien internal pada host yang sama yang tidak melalui proxy, atau
  * Rute melalui alamat proxy tepercaya non-loopback dan simpan IP tersebut di `gateway.trustedProxies`, atau
  * Untuk reverse proxy pada host yang sama yang disengaja, setel `gateway.auth.trustedProxy.allowLoopback = true`, simpan alamat loopback di `gateway.trustedProxies`, dan pastikan proxy menghapus atau menimpa header identitas.

trusted_proxy_user_missing

Header pengguna kosong atau hilang. Periksa:

  * Apakah proxy Anda dikonfigurasi untuk meneruskan header identitas?
  * Apakah nama header sudah benar? (tidak peka huruf besar-kecil, tetapi ejaan penting)
  * Apakah pengguna benar-benar terautentikasi di proxy?

trusted_proxy_missing_header_*

Header wajib tidak ada. Periksa:

  * Konfigurasi proxy Anda untuk header spesifik tersebut.
  * Apakah header dihapus di suatu tempat dalam rantai.

trusted_proxy_user_not_allowed

Pengguna terautentikasi tetapi tidak ada di `allowUsers`. Tambahkan mereka atau hapus allowlist.

trusted_proxy_origin_not_allowed

Autentikasi trusted-proxy berhasil, tetapi header browser `Origin` tidak lolos pemeriksaan origin Control UI.

Periksa:

  * `gateway.controlUi.allowedOrigins` menyertakan origin browser yang tepat.
  * Anda tidak mengandalkan origin wildcard kecuali Anda memang menginginkan perilaku izinkan-semua.
  * Jika Anda sengaja menggunakan mode fallback header Host, `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` disetel secara sengaja.

WebSocket still failing

Pastikan proxy Anda:

  * Mendukung upgrade WebSocket (`Upgrade: websocket`, `Connection: upgrade`).
  * Meneruskan header identitas pada permintaan upgrade WebSocket (bukan hanya HTTP).
  * Tidak memiliki jalur autentikasi terpisah untuk koneksi WebSocket.


## Migrasi dari autentikasi token

Jika Anda berpindah dari autentikasi token ke trusted-proxy:

* ### Konfigurasikan proxy

Konfigurasikan proxy Anda untuk mengautentikasi pengguna dan meneruskan header.

* ### Uji proxy secara independen

Uji pengaturan proxy secara independen (curl dengan header).

* ### Perbarui konfigurasi OpenClaw

Perbarui konfigurasi OpenClaw dengan autentikasi trusted-proxy.

* ### Mulai ulang Gateway

Mulai ulang Gateway.

* ### Uji WebSocket

Uji koneksi WebSocket dari Control UI.

* ### Audit

Jalankan `openclaw security audit` dan tinjau temuan.

## Terkait

  * [Konfigurasi](</id/gateway/configuration>) — referensi konfigurasi
  * [Akses jarak jauh](</id/gateway/remote>) — pola akses jarak jauh lainnya
  * [Keamanan](</id/gateway/security>) — panduan keamanan lengkap
  * [Tailscale](</id/gateway/tailscale>) — alternatif yang lebih sederhana untuk akses khusus tailnet


Was this useful?YesNo