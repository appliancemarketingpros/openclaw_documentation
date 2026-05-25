---
title: OAuth
source_url: https://docs.openclaw.ai/id/concepts/oauth
scraped_at: 2026-05-25
---

OpenClaw mendukung "auth langganan" melalui OAuth untuk penyedia yang menawarkannya (terutama **OpenAI Codex (ChatGPT OAuth)**). Untuk Anthropic, pemisahan praktisnya sekarang adalah:

  * **Kunci API Anthropic** : penagihan API Anthropic normal
  * **Anthropic Claude CLI / auth langganan di dalam OpenClaw** : staf Anthropic memberi tahu kami bahwa penggunaan ini diizinkan lagi


OpenAI Codex OAuth secara eksplisit didukung untuk digunakan di alat eksternal seperti OpenClaw. Halaman ini menjelaskan:

Untuk Anthropic di produksi, auth kunci API adalah jalur yang lebih aman dan direkomendasikan.

  * cara kerja **pertukaran token** OAuth (PKCE)
  * tempat token **disimpan** (dan alasannya)
  * cara menangani **beberapa akun** (profil + penggantian per sesi)


OpenClaw juga mendukung **Plugin penyedia** yang membawa alur OAuth atau kunci API mereka sendiri. Jalankan melalui:

bashCopy code
[code]
    openclaw models auth login --provider <id>
[/code]

## Penampung token (mengapa ini ada)

Penyedia OAuth umumnya menerbitkan **token penyegaran baru** selama alur login/penyegaran. Beberapa penyedia (atau klien OAuth) dapat membatalkan token penyegaran lama saat token baru diterbitkan untuk pengguna/aplikasi yang sama.

Gejala praktis:

  * Anda login melalui OpenClaw _dan_ melalui Claude Code / Codex CLI → salah satunya secara acak akan "logout" nanti


Untuk mengurangi hal itu, OpenClaw memperlakukan `auth-profiles.json` sebagai **penampung token** :

  * runtime membaca kredensial dari **satu tempat**
  * kami dapat menyimpan beberapa profil dan merutekannya secara deterministik
  * penggunaan ulang CLI eksternal bersifat spesifik penyedia: Codex CLI dapat melakukan bootstrap profil `openai-codex:default` yang kosong, tetapi setelah OpenClaw memiliki profil OAuth lokal, token penyegaran lokal menjadi kanonis; integrasi lain dapat tetap dikelola secara eksternal dan membaca ulang penyimpanan auth CLI mereka
  * jalur status dan startup yang sudah mengetahui cakupan set penyedia yang dikonfigurasi membatasi penemuan CLI eksternal ke set tersebut, sehingga penyimpanan login CLI yang tidak terkait tidak diperiksa untuk penyiapan satu penyedia


## Penyimpanan (tempat token berada)

Secret disimpan di penyimpanan auth agen:

  * Profil auth (OAuth + kunci API + ref tingkat nilai opsional): `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
  * File kompatibilitas lama: `~/.openclaw/agents/<agentId>/agent/auth.json` (entri `api_key` statis dibersihkan saat ditemukan)


File lama khusus impor (masih didukung, tetapi bukan penyimpanan utama):

  * `~/.openclaw/credentials/oauth.json` (diimpor ke `auth-profiles.json` pada penggunaan pertama)


Semua di atas juga menghormati `$OPENCLAW_STATE_DIR` (penggantian direktori state). Referensi lengkap: [/gateway/configuration](</id/gateway/configuration-reference#auth-storage>)

Untuk ref secret statis dan perilaku aktivasi snapshot runtime, lihat [Manajemen Secret](</id/gateway/secrets>).

Saat agen sekunder tidak memiliki profil auth lokal, OpenClaw menggunakan pewarisan baca-lanjut dari penyimpanan agen default/utama. Ini tidak mengkloning `auth-profiles.json` milik agen utama saat membaca. Token penyegaran OAuth sangat sensitif: alur penyalinan normal melewatinya secara default karena beberapa penyedia memutar atau membatalkan token penyegaran setelah digunakan. Konfigurasikan login OAuth terpisah untuk agen saat agen tersebut membutuhkan akun independen.

## Kompatibilitas token lama Anthropic

OpenClaw juga mengekspos setup-token Anthropic sebagai jalur auth token yang didukung, tetapi sekarang lebih memilih penggunaan ulang Claude CLI dan `claude -p` saat tersedia.

## Migrasi Anthropic Claude CLI

OpenClaw mendukung kembali penggunaan ulang Anthropic Claude CLI. Jika Anda sudah memiliki login Claude lokal di host, onboarding/konfigurasi dapat menggunakannya ulang secara langsung.

## Pertukaran OAuth (cara kerja login)

Alur login interaktif OpenClaw diimplementasikan di `@earendil-works/pi-ai` dan dihubungkan ke wizard/perintah.

### Setup-token Anthropic

Bentuk alur:

  1. mulai setup-token Anthropic atau paste-token dari OpenClaw
  2. OpenClaw menyimpan kredensial Anthropic yang dihasilkan dalam profil auth
  3. pemilihan model tetap pada `anthropic/...`
  4. profil auth Anthropic yang ada tetap tersedia untuk rollback/kontrol urutan


### OpenAI Codex (ChatGPT OAuth)

OpenAI Codex OAuth secara eksplisit didukung untuk digunakan di luar Codex CLI, termasuk alur kerja OpenClaw.

Bentuk alur (PKCE):

  1. hasilkan verifier/challenge PKCE + `state` acak
  2. buka `https://auth.openai.com/oauth/authorize?...`
  3. coba tangkap callback di `http://127.0.0.1:1455/auth/callback`
  4. jika callback tidak dapat bind (atau Anda berada di lingkungan remote/headless), tempel URL/kode redirect
  5. lakukan pertukaran di `https://auth.openai.com/oauth/token`
  6. ekstrak `accountId` dari token akses dan simpan `{ access, refresh, expires, accountId }`


Jalur wizard adalah `openclaw onboard` → pilihan auth `openai-codex`.

## Penyegaran + kedaluwarsa

Profil menyimpan timestamp `expires`.

Saat runtime:

  * jika `expires` berada di masa depan → gunakan token akses yang tersimpan
  * jika kedaluwarsa → segarkan (di bawah file lock) dan timpa kredensial yang tersimpan
  * jika agen sekunder membaca profil OAuth agen utama yang diwarisi, penyegaran menulis kembali ke penyimpanan agen utama alih-alih menyalin token penyegaran ke penyimpanan agen sekunder
  * pengecualian: beberapa kredensial CLI eksternal tetap dikelola secara eksternal; OpenClaw membaca ulang penyimpanan auth CLI tersebut alih-alih menggunakan token penyegaran yang disalin. Bootstrap Codex CLI sengaja lebih sempit: ia menyemai profil `openai-codex:default` yang kosong, lalu penyegaran milik OpenClaw menjaga profil lokal tetap kanonis.


Alur penyegaran bersifat otomatis; Anda umumnya tidak perlu mengelola token secara manual.

## Beberapa akun (profil) + perutean

Dua pola:

### 1) Disarankan: agen terpisah

Jika Anda ingin "pribadi" dan "kerja" tidak pernah berinteraksi, gunakan agen terisolasi (sesi + kredensial + workspace terpisah):

bashCopy code
[code]
    openclaw agents add workopenclaw agents add personal
[/code]

Lalu konfigurasikan auth per agen (wizard) dan rutekan chat ke agen yang tepat.

### 2) Lanjutan: beberapa profil dalam satu agen

`auth-profiles.json` mendukung beberapa ID profil untuk penyedia yang sama.

Pilih profil mana yang digunakan:

  * secara global melalui urutan konfigurasi (`auth.order`)
  * per sesi melalui `/model ...@<profileId>`


Contoh (penggantian sesi):

  * `/model Opus@anthropic:work`


Cara melihat ID profil yang tersedia:

  * `openclaw channels list --json` (menampilkan `auth[]`)


Dokumentasi terkait:

  * [Failover model](</id/concepts/model-failover>) (aturan rotasi + cooldown)
  * [Perintah slash](</id/tools/slash-commands>) (permukaan perintah)


## Terkait

  * [Autentikasi](</id/gateway/authentication>) \- ringkasan auth penyedia model
  * [Secret](</id/gateway/secrets>) \- penyimpanan kredensial dan SecretRef
  * [Referensi Konfigurasi](</id/gateway/configuration-reference#auth-storage>) \- kunci konfigurasi auth


Was this useful?YesNo