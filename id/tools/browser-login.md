---
title: Masuk melalui peramban
source_url: https://docs.openclaw.ai/id/tools/browser-login
scraped_at: 2026-05-25
---

## Login manual (direkomendasikan)

Ketika sebuah situs memerlukan login, **masuk secara manual** di profil browser **host** (browser openclaw).

Jangan **pernah** memberikan kredensial Anda kepada model. Login otomatis sering memicu pertahanan anti-bot dan dapat mengunci akun.

Kembali ke dokumentasi browser utama: [Browser](</id/tools/browser>).

## Profil Chrome mana yang digunakan?

OpenClaw mengendalikan **profil Chrome khusus** (bernama `openclaw`, UI berwarna jingga). Ini terpisah dari profil browser harian Anda.

Untuk panggilan tool browser agen:

  * Pilihan default: agen harus menggunakan browser `openclaw` terisolasinya.
  * Gunakan `profile="user"` hanya ketika sesi login yang sudah ada penting dan pengguna berada di depan komputer untuk mengklik/menyetujui prompt lampiran apa pun.
  * Jika Anda memiliki beberapa profil browser pengguna, tentukan profil secara eksplisit alih-alih menebak.


Dua cara mudah untuk mengaksesnya:

  1. **Minta agen membuka browser** lalu login sendiri.
  2. **Buka melalui CLI** :

bashCopy code
[code]
    openclaw browser startopenclaw browser open https://x.com
[/code]

Jika Anda memiliki beberapa profil, berikan `--browser-profile <name>` (default-nya adalah `openclaw`).

## X/Twitter: alur yang direkomendasikan

  * **Baca/cari/thread:** gunakan browser **host** (login manual).
  * **Posting pembaruan:** gunakan browser **host** (login manual).


## Sandboxing + akses browser host

Sesi browser tersandbox **lebih mungkin** memicu deteksi bot. Untuk X/Twitter (dan situs ketat lainnya), pilih browser **host**.

Jika agen tersandbox, tool browser default ke sandbox. Untuk mengizinkan kontrol host:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        browser: {          allowHostControl: true,        },      },    },  },}
[/code]

Lalu buka browser host sendiri (pemanggilan CLI selalu berjalan terhadap browser host):

bashCopy code
[code]
    openclaw browser open https://x.com --browser-profile openclaw
[/code]

Panggilan tool `browser` agen kemudian dapat menargetkan host setelah `sandbox.browser.allowHostControl: true` ditetapkan. Sebagai alternatif, nonaktifkan sandboxing untuk agen yang memposting pembaruan.

## Terkait

  * [Browser](</id/tools/browser>)
  * [Pemecahan masalah Browser Linux](</id/tools/browser-linux-troubleshooting>)
  * [Pemecahan masalah Browser WSL2](</id/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo