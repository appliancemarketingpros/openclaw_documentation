---
title: Nix
source_url: https://docs.openclaw.ai/id/install/nix
scraped_at: 2026-05-25
---

Instal OpenClaw secara deklaratif dengan **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** \- modul Home Manager pihak pertama yang sudah lengkap.

## Yang Anda dapatkan

  * Gateway + aplikasi macOS + alat (whisper, spotify, cameras) -- semuanya dipin
  * Layanan launchd yang tetap berjalan setelah reboot
  * Sistem Plugin dengan config deklaratif
  * Rollback instan: `home-manager switch --rollback`


## Mulai cepat

* ### Instal Determinate Nix

Jika Nix belum terinstal, ikuti instruksi [Determinate Nix installer](<https://github.com/DeterminateSystems/nix-installer>).

* ### Buat flake lokal

Gunakan templat agent-first dari repo nix-openclaw:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### Konfigurasikan rahasia

Siapkan token bot perpesanan dan kunci API penyedia model Anda. File polos di `~/.secrets/` sudah cukup.

* ### Isi placeholder templat dan beralih

bashCopy code
[code]
    home-manager switch
[/code]

* ### Verifikasi

Pastikan layanan launchd berjalan dan bot Anda merespons pesan.

Lihat [README nix-openclaw](<https://github.com/openclaw/nix-openclaw>) untuk opsi modul dan contoh lengkap.

## Perilaku runtime mode Nix

Saat `OPENCLAW_NIX_MODE=1` ditetapkan (otomatis dengan nix-openclaw), OpenClaw masuk ke mode deterministik untuk instalasi yang dikelola Nix. Paket Nix lain dapat menetapkan mode yang sama; nix-openclaw adalah referensi pihak pertama.

Anda juga dapat menetapkannya secara manual:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

Di macOS, aplikasi GUI tidak otomatis mewarisi variabel lingkungan shell. Aktifkan mode Nix melalui defaults sebagai gantinya:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Yang berubah dalam mode Nix

  * Alur auto-install dan mutasi mandiri dinonaktifkan
  * `openclaw.json` diperlakukan sebagai immutable. Default turunan startup tetap hanya runtime, dan penulis config seperti setup, onboarding, `openclaw update` yang memutasi, install/update/uninstall/enable Plugin, `doctor --fix`, `doctor --generate-gateway-token`, dan `openclaw config set` menolak mengedit file tersebut.
  * Agent sebaiknya mengedit sumber Nix sebagai gantinya. Untuk nix-openclaw, gunakan [Mulai Cepat](<https://github.com/openclaw/nix-openclaw#quick-start>) agent-first dan tetapkan config di bawah `programs.openclaw.config` atau `instances.<name>.config`.
  * Dependency yang hilang menampilkan pesan remediasi khusus Nix
  * UI menampilkan banner mode Nix read-only


### Jalur config dan state

OpenClaw membaca config JSON5 dari `OPENCLAW_CONFIG_PATH` dan menyimpan data yang dapat diubah di `OPENCLAW_STATE_DIR`. Saat berjalan di bawah Nix, tetapkan ini secara eksplisit ke lokasi yang dikelola Nix agar state runtime dan config tetap berada di luar store immutable.

Variabel | Default  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### Penemuan PATH layanan

Layanan Gateway launchd/systemd otomatis menemukan biner profil Nix sehingga Plugin dan alat yang melakukan shell out ke executable yang diinstal `nix` berfungsi tanpa penyiapan PATH manual:

  * Saat `NIX_PROFILES` ditetapkan, setiap entri ditambahkan ke PATH layanan dengan prioritas kanan-ke-kiri (sesuai prioritas shell Nix - yang paling kanan menang).
  * Saat `NIX_PROFILES` tidak ditetapkan, `~/.nix-profile/bin` ditambahkan sebagai fallback.


Ini berlaku untuk lingkungan layanan launchd macOS maupun systemd Linux.

## Terkait

[**nix-openclaw** Modul Home Manager sumber kebenaran dan panduan penyiapan lengkap. ](<https://github.com/openclaw/nix-openclaw>) [**Wizard penyiapan** Panduan penyiapan CLI non-Nix. ](</id/start/wizard>) [**Docker** Penyiapan berbasis container sebagai alternatif non-Nix. ](</id/install/docker>) [**Memperbarui** Memperbarui instalasi yang dikelola Home Manager bersama paketnya. ](</id/install/updating>)

Was this useful?YesNo