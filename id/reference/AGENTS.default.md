---
title: AGENTS.md Bawaan
source_url: https://docs.openclaw.ai/id/reference/AGENTS.default
scraped_at: 2026-05-25
---

## Jalankan pertama kali (direkomendasikan)

OpenClaw menggunakan direktori workspace khusus untuk agen. Default: `~/.openclaw/workspace` (dapat dikonfigurasi melalui `agents.defaults.workspace`).

  1. Buat workspace (jika belum ada):

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace
[/code]

  2. Salin templat workspace default ke dalam workspace:

bashCopy code
[code]
    cp docs/reference/templates/AGENTS.md ~/.openclaw/workspace/AGENTS.mdcp docs/reference/templates/SOUL.md ~/.openclaw/workspace/SOUL.mdcp docs/reference/templates/TOOLS.md ~/.openclaw/workspace/TOOLS.md
[/code]

  3. Opsional: jika Anda menginginkan daftar skill asisten pribadi, ganti [AGENTS.md](<http://AGENTS.md>) dengan file ini:

bashCopy code
[code]
    cp docs/reference/AGENTS.default.md ~/.openclaw/workspace/AGENTS.md
[/code]

  4. Opsional: pilih workspace lain dengan mengatur `agents.defaults.workspace` (mendukung `~`):

json5Copy code
[code]
    {  agents: { defaults: { workspace: "~/.openclaw/workspace" } },}
[/code]

## Default keamanan

  * Jangan membuang direktori atau rahasia ke chat.
  * Jangan jalankan perintah destruktif kecuali diminta secara eksplisit.
  * Jangan kirim balasan parsial/streaming ke permukaan perpesanan eksternal (hanya balasan final).


## Awal sesi (wajib)

  * Baca `SOUL.md`, `USER.md`, dan hari ini+kemarin di `memory/`.
  * Baca `MEMORY.md` jika ada.
  * Lakukan sebelum merespons.


## Soul (wajib)

  * `SOUL.md` mendefinisikan identitas, nada, dan batasan. Jaga agar tetap terbaru.
  * Jika Anda mengubah `SOUL.md`, beri tahu pengguna.
  * Anda adalah instance baru di setiap sesi; kontinuitas berada di file-file ini.


## Ruang bersama (direkomendasikan)

  * Anda bukan suara pengguna; berhati-hatilah di chat grup atau kanal publik.
  * Jangan bagikan data pribadi, informasi kontak, atau catatan internal.


## Sistem memori (direkomendasikan)

  * Log harian: `memory/YYYY-MM-DD.md` (buat `memory/` jika perlu).
  * Memori jangka panjang: `MEMORY.md` untuk fakta, preferensi, dan keputusan yang tahan lama.
  * `memory.md` huruf kecil adalah input perbaikan lama saja; jangan sengaja menyimpan kedua file root.
  * Saat awal sesi, baca hari ini + kemarin + `MEMORY.md` jika ada.
  * Tangkap: keputusan, preferensi, batasan, loop terbuka.
  * Hindari rahasia kecuali diminta secara eksplisit.


## Alat dan skill

  * Alat berada di dalam skill; ikuti `SKILL.md` masing-masing skill saat Anda membutuhkannya.
  * Simpan catatan khusus lingkungan di `TOOLS.md` (Catatan untuk Skills).


## Tips pencadangan (direkomendasikan)

Jika Anda memperlakukan workspace ini sebagai "memori" Clawd, jadikan ini repo git (idealnya privat) agar `AGENTS.md` dan file memori Anda dicadangkan.

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.mdgit commit -m "Add Clawd workspace"# Optional: add a private remote + push
[/code]

## Apa yang dilakukan OpenClaw

  * Menjalankan Gateway WhatsApp + agen pengodean Pi sehingga asisten dapat membaca/menulis chat, mengambil konteks, dan menjalankan skill melalui host Mac.
  * Aplikasi macOS mengelola izin (perekaman layar, notifikasi, mikrofon) dan mengekspos CLI `openclaw` melalui biner bawaannya.
  * Chat langsung secara default digabungkan ke sesi `main` milik agen; grup tetap terisolasi sebagai `agent:<agentId>:<channel>:group:<id>` (ruangan/kanal: `agent:<agentId>:<channel>:channel:<id>`); heartbeat menjaga tugas latar belakang tetap hidup.


## Skill inti (aktifkan di Pengaturan → Skills)

  * **mcporter** \- Runtime/CLI server alat untuk mengelola backend skill eksternal.
  * **Peekaboo** \- Screenshot macOS cepat dengan analisis visi AI opsional.
  * **camsnap** \- Tangkap frame, klip, atau peringatan gerakan dari kamera keamanan RTSP/ONVIF.
  * **oracle** \- CLI agen siap OpenAI dengan pemutaran ulang sesi dan kontrol browser.
  * **eightctl** \- Kendalikan tidur Anda, dari terminal.
  * **imsg** \- Kirim, baca, stream iMessage & SMS.
  * **wacli** \- CLI WhatsApp: sinkronkan, cari, kirim.
  * **discord** \- Aksi Discord: reaksi, stiker, polling. Gunakan target `user:<id>` atau `channel:<id>` (id numerik polos bersifat ambigu).
  * **gog** \- CLI Google Suite: Gmail, Calendar, Drive, Contacts.
  * **spotify-player** \- Klien Spotify terminal untuk mencari/mengantrikan/mengontrol pemutaran.
  * **sag** \- Ucapan ElevenLabs dengan UX say bergaya Mac; secara default stream ke speaker.
  * **Sonos CLI** \- Kontrol speaker Sonos (temukan/status/pemutaran/volume/pengelompokan) dari skrip.
  * **blucli** \- Putar, kelompokkan, dan otomatisasi pemutar BluOS dari skrip.
  * **OpenHue CLI** \- Kontrol pencahayaan Philips Hue untuk scene dan otomatisasi.
  * **OpenAI Whisper** \- Speech-to-text lokal untuk dikte cepat dan transkrip pesan suara.
  * **Gemini CLI** \- Model Google Gemini dari terminal untuk tanya jawab cepat.
  * **agent-tools** \- Toolkit utilitas untuk otomatisasi dan skrip pembantu.


## Catatan penggunaan

  * Utamakan CLI `openclaw` untuk scripting; aplikasi Mac menangani izin.
  * Jalankan instalasi dari tab Skills; tab ini menyembunyikan tombol jika biner sudah ada.
  * Biarkan heartbeat tetap aktif agar asisten dapat menjadwalkan pengingat, memantau inbox, dan memicu tangkapan kamera.
  * UI Canvas berjalan layar penuh dengan overlay native. Hindari menempatkan kontrol penting di tepi kiri atas/kanan atas/bawah; tambahkan gutter eksplisit di layout dan jangan mengandalkan inset safe-area.
  * Untuk verifikasi berbasis browser, gunakan `openclaw browser` (tab/status/screenshot) dengan profil Chrome yang dikelola OpenClaw.
  * Untuk inspeksi DOM, gunakan `openclaw browser eval|query|dom|snapshot` (dan `--json`/`--out` saat Anda membutuhkan output mesin).
  * Untuk interaksi, gunakan `openclaw browser click|type|hover|drag|select|upload|press|wait|navigate|back|evaluate|run` (click/type memerlukan referensi snapshot; gunakan `evaluate` untuk selector CSS).


## Terkait

  * [Workspace agen](</id/concepts/agent-workspace>)
  * [Runtime agen](</id/concepts/agent>)


Was this useful?YesNo