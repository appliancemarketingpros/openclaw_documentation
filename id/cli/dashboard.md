---
title: Dasbor
source_url: https://docs.openclaw.ai/id/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

Buka UI Kontrol menggunakan autentikasi Anda saat ini.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Catatan:

  * `dashboard` menyelesaikan SecretRef `gateway.auth.token` yang dikonfigurasi jika memungkinkan.
  * `dashboard` mengikuti `gateway.tls.enabled`: gateway dengan TLS diaktifkan mencetak/membuka URL UI Kontrol `https://` dan terhubung melalui `wss://`.
  * Jika pengiriman melalui clipboard/browser gagal untuk URL dashboard yang diautentikasi token, `dashboard` mencatat petunjuk autentikasi manual yang aman dengan menyebut `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token`, dan kunci fragmen `token` tanpa mencetak nilai token.
  * Untuk token yang dikelola SecretRef (terselesaikan atau belum terselesaikan), `dashboard` mencetak/menyalin/membuka URL tanpa token untuk menghindari pemaparan secret eksternal dalam output terminal, riwayat clipboard, atau argumen peluncuran browser.
  * Jika `gateway.auth.token` dikelola SecretRef tetapi tidak terselesaikan di jalur perintah ini, perintah mencetak URL tanpa token dan panduan remediasi eksplisit alih-alih menyematkan placeholder token yang tidak valid.


## Terkait

  * [Referensi CLI](</id/cli>)
  * [Dashboard](</id/web/dashboard>)


Was this useful?YesNo