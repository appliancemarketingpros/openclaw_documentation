---
title: Autentikasi
source_url: https://docs.openclaw.ai/id/gateway/authentication
scraped_at: 2026-05-25
---

OpenClaw mendukung OAuth dan kunci API untuk penyedia model. Untuk host gateway yang selalu aktif, kunci API biasanya menjadi opsi yang paling mudah diprediksi. Alur berlangganan/OAuth juga didukung saat sesuai dengan model akun penyedia Anda.

Lihat [/concepts/oauth](</id/concepts/oauth>) untuk alur OAuth lengkap dan tata letak penyimpanannya. Untuk autentikasi berbasis SecretRef (penyedia `env`/`file`/`exec`), lihat [Manajemen Rahasia](</id/gateway/secrets>). Untuk aturan kelayakan kredensial/kode alasan yang digunakan oleh `models status --probe`, lihat [Semantik Kredensial Autentikasi](</id/auth-credential-semantics>).

## Penyiapan yang disarankan (kunci API, penyedia apa pun)

Jika Anda menjalankan gateway jangka panjang, mulai dengan kunci API untuk penyedia pilihan Anda. Khusus untuk Anthropic, autentikasi kunci API tetap menjadi penyiapan server yang paling mudah diprediksi, tetapi OpenClaw juga mendukung penggunaan ulang login Claude CLI lokal.

  1. Buat kunci API di konsol penyedia Anda.
  2. Letakkan di **host gateway** (mesin yang menjalankan `openclaw gateway`).

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."openclaw models status
[/code]

  3. Jika Gateway berjalan di bawah systemd/launchd, sebaiknya letakkan kunci di `~/.openclaw/.env` agar daemon dapat membacanya:

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'&lt;PROVIDER&gt;_API_KEY=...EOF
[/code]

Kemudian mulai ulang daemon (atau mulai ulang proses Gateway Anda) dan periksa ulang:

bashCopy code
[code]
    openclaw models statusopenclaw doctor
[/code]

Jika Anda tidak ingin mengelola variabel env sendiri, onboarding dapat menyimpan kunci API untuk digunakan daemon: `openclaw onboard`.

Lihat [Bantuan](</id/help>) untuk detail tentang pewarisan env (`env.shellEnv`, `~/.openclaw/.env`, systemd/launchd).

## Anthropic: kompatibilitas Claude CLI dan token

Autentikasi setup-token Anthropic tetap tersedia di OpenClaw sebagai jalur token yang didukung. Staf Anthropic sejak itu telah memberi tahu kami bahwa penggunaan Claude CLI gaya OpenClaw diizinkan kembali, jadi OpenClaw memperlakukan penggunaan ulang Claude CLI dan penggunaan `claude -p` sebagai disetujui untuk integrasi ini kecuali Anthropic menerbitkan kebijakan baru. Saat penggunaan ulang Claude CLI tersedia di host, itulah jalur yang kini disarankan.

Untuk host gateway jangka panjang, kunci API Anthropic tetap menjadi penyiapan yang paling mudah diprediksi. Jika Anda ingin menggunakan ulang login Claude yang ada di host yang sama, gunakan jalur Anthropic Claude CLI di onboarding/configure.

Penyiapan host yang disarankan untuk penggunaan ulang Claude CLI:

bashCopy code
[code]
    # Run on the gateway hostclaude auth loginclaude auth status --textopenclaw models auth login --provider anthropic --method cli --set-default
[/code]

Ini adalah penyiapan dua langkah:

  1. Masukkan Claude Code sendiri ke Anthropic di host gateway.
  2. Beri tahu OpenClaw untuk mengalihkan pemilihan model Anthropic ke backend `claude-cli` lokal dan menyimpan profil autentikasi OpenClaw yang sesuai.


Jika `claude` tidak ada di `PATH`, instal Claude Code terlebih dahulu atau atur `agents.defaults.cliBackends.claude-cli.command` ke jalur biner sebenarnya.

Entri token manual (penyedia apa pun; menulis `auth-profiles.json` \+ memperbarui konfigurasi):

bashCopy code
[code]
    openclaw models auth paste-token --provider openrouter
[/code]

`auth-profiles.json` hanya menyimpan kredensial. Bentuk kanonisnya adalah:

jsonCopy code
[code]
    {  "version": 1,  "profiles": {    "openrouter:default": {      "type": "api_key",      "provider": "openrouter",      "key": "OPENROUTER_API_KEY"    }  }}
[/code]

OpenClaw mengharapkan bentuk kanonis `version` \+ `profiles` saat runtime. Jika instalasi lama masih memiliki file datar seperti `{ "openrouter": { "apiKey": "..." } }`, jalankan `openclaw doctor --fix` untuk menulis ulangnya sebagai profil kunci API `openrouter:default`; doctor menyimpan salinan `.legacy-flat.*.bak` di samping aslinya. Detail endpoint seperti `baseUrl`, `api`, id model, header, dan timeout berada di bawah `models.providers.<id>` di `openclaw.json` atau `models.json`, bukan di `auth-profiles.json`.

Rute autentikasi eksternal seperti Bedrock `auth: "aws-sdk"` juga bukan kredensial. Jika Anda menginginkan rute Bedrock bernama, letakkan `auth.profiles.<id>.mode: "aws-sdk"` di `openclaw.json`; jangan tulis `type: "aws-sdk"` ke dalam `auth-profiles.json`. `openclaw doctor --fix` memindahkan penanda AWS SDK lama dari penyimpanan kredensial ke metadata konfigurasi.

Referensi profil autentikasi juga didukung untuk kredensial statis:

  * Kredensial `api_key` dapat menggunakan `keyRef: { source, provider, id }`
  * Kredensial `token` dapat menggunakan `tokenRef: { source, provider, id }`
  * Profil mode OAuth tidak mendukung kredensial SecretRef; jika `auth.profiles.<id>.mode` diatur ke `"oauth"`, input `keyRef`/`tokenRef` berbasis SecretRef untuk profil tersebut ditolak.


Pemeriksaan yang ramah otomasi (keluar `1` saat kedaluwarsa/hilang, `2` saat akan kedaluwarsa):

bashCopy code
[code]
    openclaw models status --check
[/code]

Probe autentikasi langsung:

bashCopy code
[code]
    openclaw models status --probe
[/code]

Catatan:

  * Baris probe dapat berasal dari profil autentikasi, kredensial env, atau `models.json`.
  * Jika `auth.order.<provider>` eksplisit menghilangkan profil tersimpan, probe melaporkan `excluded_by_auth_order` untuk profil tersebut alih-alih mencobanya.
  * Jika autentikasi ada tetapi OpenClaw tidak dapat menyelesaikan kandidat model yang dapat diprobe untuk penyedia tersebut, probe melaporkan `status: no_model`.
  * Cooldown rate-limit dapat berlaku per model. Profil yang sedang cooldown untuk satu model masih dapat digunakan untuk model saudaranya pada penyedia yang sama.


Skrip opsional operasi (systemd/Termux) didokumentasikan di sini: [Skrip pemantauan autentikasi](</id/help/scripts#auth-monitoring-scripts>)

## Catatan Anthropic

Backend Anthropic `claude-cli` didukung kembali.

  * Staf Anthropic memberi tahu kami bahwa jalur integrasi OpenClaw ini diizinkan kembali.
  * Karena itu, OpenClaw memperlakukan penggunaan ulang Claude CLI dan penggunaan `claude -p` sebagai disetujui untuk eksekusi berbasis Anthropic kecuali Anthropic menerbitkan kebijakan baru.
  * Kunci API Anthropic tetap menjadi pilihan yang paling mudah diprediksi untuk host gateway jangka panjang dan kontrol penagihan sisi server yang eksplisit.


## Memeriksa status autentikasi model

bashCopy code
[code]
    openclaw models statusopenclaw doctor
[/code]

## Perilaku rotasi kunci API (gateway)

Beberapa penyedia mendukung percobaan ulang permintaan dengan kunci alternatif saat panggilan API mencapai rate limit penyedia.

  * Urutan prioritas: 
    * `OPENCLAW_LIVE_&lt;PROVIDER&gt;_KEY` (override tunggal)
    * `&lt;PROVIDER&gt;_API_KEYS`
    * `&lt;PROVIDER&gt;_API_KEY`
    * `&lt;PROVIDER&gt;_API_KEY_*`
  * Penyedia Google juga menyertakan `GOOGLE_API_KEY` sebagai fallback tambahan.
  * Daftar kunci yang sama dideduplikasi sebelum digunakan.
  * OpenClaw mencoba ulang dengan kunci berikutnya hanya untuk kesalahan rate-limit (misalnya `429`, `rate_limit`, `quota`, `resource exhausted`, `Too many concurrent requests`, `ThrottlingException`, `concurrency limit reached`, atau `workers_ai ... quota limit exceeded`).
  * Kesalahan non-rate-limit tidak dicoba ulang dengan kunci alternatif.
  * Jika semua kunci gagal, kesalahan akhir dari percobaan terakhir dikembalikan.


## Mengontrol kredensial yang digunakan

### Per sesi (perintah chat)

Gunakan `/model <alias-or-id>@<profileId>` untuk menyematkan kredensial penyedia tertentu untuk sesi saat ini (contoh id profil: `anthropic:default`, `anthropic:work`).

Gunakan `/model` (atau `/model list`) untuk picker ringkas; gunakan `/model status` untuk tampilan lengkap (kandidat + profil autentikasi berikutnya, ditambah detail endpoint penyedia jika dikonfigurasi).

### Per agen (override CLI)

Atur override urutan profil autentikasi eksplisit untuk agen (disimpan di `auth-state.json` agen tersebut):

bashCopy code
[code]
    openclaw models auth order get --provider anthropicopenclaw models auth order set --provider anthropic anthropic:defaultopenclaw models auth order clear --provider anthropic
[/code]

Gunakan `--agent <id>` untuk menargetkan agen tertentu; hilangkan untuk menggunakan agen default yang dikonfigurasi. Saat Anda men-debug masalah urutan, `openclaw models status --probe` menampilkan profil tersimpan yang dihilangkan sebagai `excluded_by_auth_order` alih-alih melewatinya diam-diam. Saat Anda men-debug masalah cooldown, ingat bahwa cooldown rate-limit dapat terikat ke satu id model, bukan seluruh profil penyedia.

## Pemecahan masalah

### "Tidak ada kredensial yang ditemukan"

Jika profil Anthropic hilang, konfigurasikan kunci API Anthropic di **host gateway** atau siapkan jalur setup-token Anthropic, lalu periksa ulang:

bashCopy code
[code]
    openclaw models status
[/code]

### Token akan kedaluwarsa/kedaluwarsa

Jalankan `openclaw models status` untuk memastikan profil mana yang akan kedaluwarsa. Jika profil token Anthropic hilang atau kedaluwarsa, segarkan penyiapan tersebut melalui setup-token atau migrasikan ke kunci API Anthropic.

## Terkait

  * [Manajemen rahasia](</id/gateway/secrets>)
  * [Akses jarak jauh](</id/gateway/remote>)
  * [Penyimpanan autentikasi](</id/concepts/oauth>)


Was this useful?YesNo