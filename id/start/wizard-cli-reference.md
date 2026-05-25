---
title: Referensi penyiapan CLI
source_url: https://docs.openclaw.ai/id/start/wizard-cli-reference
scraped_at: 2026-05-25
---

Halaman ini adalah referensi lengkap untuk `openclaw onboard`. Untuk panduan singkat, lihat [Onboarding (CLI)](</id/start/wizard>).

## Yang dilakukan wizard

Mode lokal (default) memandu Anda melalui:

  * Penyiapan model dan autentikasi (OAuth langganan OpenAI Code, Anthropic Claude CLI atau kunci API, serta opsi MiniMax, GLM, Ollama, Moonshot, StepFun, dan AI Gateway)
  * Lokasi workspace dan file bootstrap
  * Pengaturan Gateway (port, bind, autentikasi, tailscale)
  * Kanal dan penyedia (Telegram, WhatsApp, Discord, Google Chat, Mattermost, Signal, iMessage, dan Plugin kanal bawaan lainnya)
  * Instalasi daemon (LaunchAgent, unit pengguna systemd, atau Windows Scheduled Task native dengan fallback folder Startup)
  * Pemeriksaan kesehatan
  * Penyiapan Skills


Mode jarak jauh mengonfigurasi mesin ini untuk terhubung ke gateway di tempat lain. Mode ini tidak menginstal atau mengubah apa pun pada host jarak jauh.

## Detail alur lokal

* ### Deteksi konfigurasi yang ada

  * Jika `~/.openclaw/openclaw.json` ada, pilih Keep, Modify, atau Reset.
  * Menjalankan ulang wizard tidak menghapus apa pun kecuali Anda secara eksplisit memilih Reset (atau meneruskan `--reset`).
  * CLI `--reset` default ke `config+creds+sessions`; gunakan `--reset-scope full` untuk juga menghapus workspace.
  * Jika konfigurasi tidak valid atau berisi kunci lama, wizard berhenti dan meminta Anda menjalankan `openclaw doctor` sebelum melanjutkan.
  * Reset menggunakan `trash` dan menawarkan cakupan: 
    * Hanya konfigurasi
    * Konfigurasi + kredensial + sesi
    * Reset penuh (juga menghapus workspace)


* ### Model dan autentikasi

  * Matriks opsi lengkap ada di Opsi autentikasi dan model.


* ### Workspace

  * Default `~/.openclaw/workspace` (dapat dikonfigurasi).
  * Menyemai file workspace yang diperlukan untuk ritual bootstrap saat pertama dijalankan.
  * Tata letak workspace: [Workspace agen](</id/concepts/agent-workspace>).


* ### Gateway

  * Meminta port, bind, mode autentikasi, dan eksposur tailscale.
  * Direkomendasikan: tetap aktifkan autentikasi token bahkan untuk loopback agar klien WS lokal harus melakukan autentikasi.
  * Dalam mode token, penyiapan interaktif menawarkan: 
    * **Buat/simpan token teks biasa** (default)
    * **Gunakan SecretRef** (opt-in)
  * Dalam mode kata sandi, penyiapan interaktif juga mendukung penyimpanan teks biasa atau SecretRef.
  * Jalur SecretRef token non-interaktif: `--gateway-token-ref-env &lt;ENV_VAR&gt;`. 
    * Memerlukan variabel env yang tidak kosong di lingkungan proses onboarding.
    * Tidak dapat digabungkan dengan `--gateway-token`.
  * Nonaktifkan autentikasi hanya jika Anda sepenuhnya memercayai setiap proses lokal.
  * Bind non-loopback tetap memerlukan autentikasi.


* ### Kanal

  * [WhatsApp](</id/channels/whatsapp>): login QR opsional
  * [Telegram](</id/channels/telegram>): token bot
  * [Discord](</id/channels/discord>): token bot
  * [Google Chat](</id/channels/googlechat>): JSON akun layanan + audiens webhook
  * [Mattermost](</id/channels/mattermost>): token bot + URL dasar
  * [Signal](</id/channels/signal>): instalasi `signal-cli` opsional + konfigurasi akun
  * [iMessage](</id/channels/imessage>): jalur CLI `imsg` \+ akses DB Messages; gunakan pembungkus SSH saat Gateway berjalan di luar Mac
  * Keamanan DM: default adalah pairing. DM pertama mengirim kode; setujui melalui `openclaw pairing approve <channel> <code>` atau gunakan allowlist.


* ### Instalasi daemon

  * macOS: LaunchAgent 
    * Memerlukan sesi pengguna yang sudah login; untuk headless, gunakan LaunchDaemon kustom (tidak disertakan).
  * Linux dan Windows melalui WSL2: unit pengguna systemd 
    * Wizard mencoba `loginctl enable-linger <user>` agar gateway tetap berjalan setelah logout.
    * Mungkin meminta sudo (menulis `/var/lib/systemd/linger`); wizard mencoba tanpa sudo terlebih dahulu.
  * Windows native: Scheduled Task terlebih dahulu 
    * Jika pembuatan tugas ditolak, OpenClaw fallback ke item login folder Startup per pengguna dan segera memulai gateway.
    * Scheduled Task tetap direkomendasikan karena menyediakan status supervisor yang lebih baik.
  * Pemilihan runtime: Node (direkomendasikan; wajib untuk WhatsApp dan Telegram). Bun tidak direkomendasikan.


* ### Pemeriksaan kesehatan

  * Memulai gateway (jika diperlukan) dan menjalankan `openclaw health`.
  * `openclaw status --deep` menambahkan probe kesehatan gateway langsung ke keluaran status, termasuk probe kanal jika didukung.


* ### Skills

  * Membaca Skills yang tersedia dan memeriksa persyaratan.
  * Memungkinkan Anda memilih manajer node: npm, pnpm, atau bun.
  * Menginstal dependensi opsional (sebagian menggunakan Homebrew di macOS).


* ### Selesai

  * Ringkasan dan langkah berikutnya, termasuk opsi aplikasi iOS, Android, dan macOS.


## Detail mode jarak jauh

Mode jarak jauh mengonfigurasi mesin ini untuk terhubung ke gateway di tempat lain.

Yang Anda tetapkan:

  * URL gateway jarak jauh (`ws://...`)
  * Token jika autentikasi gateway jarak jauh diperlukan (direkomendasikan)


## Opsi autentikasi dan model

Kunci API Anthropic

Menggunakan `ANTHROPIC_API_KEY` jika ada atau meminta kunci, lalu menyimpannya untuk penggunaan daemon.

Langganan OpenAI Code (OAuth)

Alur browser; tempel `code#state`.

Mengatur `agents.defaults.model` ke `openai/gpt-5.5` melalui runtime Codex saat model belum diatur atau sudah merupakan keluarga OpenAI.

Langganan OpenAI Code (pairing perangkat)

Alur pairing browser dengan kode perangkat berumur pendek.

Mengatur `agents.defaults.model` ke `openai/gpt-5.5` melalui runtime Codex saat model belum diatur atau sudah merupakan keluarga OpenAI.

Kunci API OpenAI

Menggunakan `OPENAI_API_KEY` jika ada atau meminta kunci, lalu menyimpan kredensial di profil autentikasi.

Mengatur `agents.defaults.model` ke `openai/gpt-5.5` saat model belum diatur, `openai/*`, atau `openai-codex/*`.

Kunci API xAI (Grok)

Meminta `XAI_API_KEY` dan mengonfigurasi xAI sebagai penyedia model.

OpenCode

Meminta `OPENCODE_API_KEY` (atau `OPENCODE_ZEN_API_KEY`) dan memungkinkan Anda memilih katalog Zen atau Go. URL penyiapan: [opencode.ai/auth](<https://opencode.ai/auth>).

Kunci API (generik)

Menyimpan kunci untuk Anda.

Vercel AI Gateway

Meminta `AI_GATEWAY_API_KEY`. Detail lebih lanjut: [Vercel AI Gateway](</id/providers/vercel-ai-gateway>).

Cloudflare AI Gateway

Meminta ID akun, ID gateway, dan `CLOUDFLARE_AI_GATEWAY_API_KEY`. Detail lebih lanjut: [Cloudflare AI Gateway](</id/providers/cloudflare-ai-gateway>).

MiniMax

Konfigurasi ditulis otomatis. Default hosted adalah `MiniMax-M2.7`; penyiapan kunci API menggunakan `minimax/...`, dan penyiapan OAuth menggunakan `minimax-portal/...`. Detail lebih lanjut: [MiniMax](</id/providers/minimax>).

StepFun

Konfigurasi ditulis otomatis untuk StepFun standar atau Step Plan pada endpoint China atau global. Standar saat ini mencakup `step-3.5-flash`, dan Step Plan juga mencakup `step-3.5-flash-2603`. Detail lebih lanjut: [StepFun](</id/providers/stepfun>).

Synthetic (kompatibel dengan Anthropic)

Meminta `SYNTHETIC_API_KEY`. Detail lebih lanjut: [Synthetic](</id/providers/synthetic>).

Ollama (model terbuka cloud dan lokal)

Meminta `Cloud + Local`, `Cloud only`, atau `Local only` terlebih dahulu. `Cloud only` menggunakan `OLLAMA_API_KEY` dengan `https://ollama.com`. Mode berbasis host meminta URL dasar (default `http://127.0.0.1:11434`), menemukan model yang tersedia, dan menyarankan default. `Cloud + Local` juga memeriksa apakah host Ollama tersebut sudah masuk untuk akses cloud. Detail lebih lanjut: [Ollama](</id/providers/ollama>).

Moonshot dan Kimi Coding

Konfigurasi Moonshot (Kimi K2) dan Kimi Coding ditulis otomatis. Detail lebih lanjut: [Moonshot AI (Kimi + Kimi Coding)](</id/providers/moonshot>).

Penyedia kustom

Berfungsi dengan endpoint yang kompatibel dengan OpenAI dan kompatibel dengan Anthropic.

Onboarding interaktif mendukung pilihan penyimpanan kunci API yang sama seperti alur kunci API penyedia lainnya:

  * **Tempel kunci API sekarang** (teks biasa)
  * **Gunakan referensi rahasia** (ref env atau ref penyedia yang dikonfigurasi, dengan validasi preflight)


Flag non-interaktif:

  * `--auth-choice custom-api-key`
  * `--custom-base-url`
  * `--custom-model-id`
  * `--custom-api-key` (opsional; fallback ke `CUSTOM_API_KEY`)
  * `--custom-provider-id` (opsional)
  * `--custom-compatibility <openai|anthropic>` (opsional; default `openai`)
  * `--custom-image-input` / `--custom-text-input` (opsional; menimpa kapabilitas input model yang disimpulkan)

Lewati

Membiarkan autentikasi belum dikonfigurasi.

Perilaku model:

  * Pilih model default dari opsi yang terdeteksi, atau masukkan penyedia dan model secara manual.
  * Onboarding penyedia kustom menyimpulkan dukungan gambar untuk ID model umum dan hanya bertanya saat nama model tidak dikenal.
  * Saat onboarding dimulai dari pilihan autentikasi penyedia, pemilih model lebih mengutamakan penyedia tersebut secara otomatis. Untuk Volcengine dan BytePlus, preferensi yang sama juga cocok dengan varian coding-plan mereka (`volcengine-plan/*`, `byteplus-plan/*`).
  * Jika filter penyedia pilihan tersebut akan kosong, pemilih fallback ke katalog lengkap alih-alih tidak menampilkan model.
  * Wizard menjalankan pemeriksaan model dan memperingatkan jika model yang dikonfigurasi tidak dikenal atau autentikasinya hilang.


Jalur kredensial dan profil:

  * Profil autentikasi (kunci API + OAuth): `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
  * Impor OAuth lama: `~/.openclaw/credentials/oauth.json`


Mode penyimpanan kredensial:

  * Perilaku onboarding default mempertahankan kunci API sebagai nilai teks biasa di profil autentikasi.
  * `--secret-input-mode ref` mengaktifkan mode referensi alih-alih penyimpanan kunci teks biasa. Dalam penyiapan interaktif, Anda dapat memilih salah satu: 
    * ref variabel lingkungan (misalnya `keyRef: { source: "env", provider: "default", id: "OPENAI_API_KEY" }`)
    * ref penyedia yang dikonfigurasi (`file` atau `exec`) dengan alias penyedia + id
  * Mode referensi interaktif menjalankan validasi preflight cepat sebelum menyimpan. 
    * Ref env: memvalidasi nama variabel + nilai tidak kosong di lingkungan onboarding saat ini.
    * Ref penyedia: memvalidasi konfigurasi penyedia dan me-resolve id yang diminta.
    * Jika preflight gagal, onboarding menampilkan kesalahan dan memungkinkan Anda mencoba lagi.
  * Dalam mode non-interaktif, `--secret-input-mode ref` hanya berbasis env. 
    * Tetapkan variabel env penyedia di lingkungan proses onboarding.
    * Flag kunci inline (misalnya `--openai-api-key`) mengharuskan variabel env tersebut diatur; jika tidak, onboarding gagal cepat.
    * Untuk penyedia kustom, mode non-interaktif `ref` menyimpan `models.providers.<id>.apiKey` sebagai `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.
    * Dalam kasus penyedia kustom tersebut, `--custom-api-key` mengharuskan `CUSTOM_API_KEY` diatur; jika tidak, onboarding gagal cepat.
  * Kredensial autentikasi Gateway mendukung pilihan teks biasa dan SecretRef dalam penyiapan interaktif: 
    * Mode token: **Buat/simpan token teks biasa** (default) atau **Gunakan SecretRef**.
    * Mode kata sandi: teks biasa atau SecretRef.
  * Jalur SecretRef token non-interaktif: `--gateway-token-ref-env &lt;ENV_VAR&gt;`.
  * Penyiapan teks biasa yang ada tetap berfungsi tanpa perubahan.


## Output dan internal

Bidang umum di `~/.openclaw/openclaw.json`:

  * `agents.defaults.workspace`
  * `agents.defaults.skipBootstrap` ketika `--skip-bootstrap` diteruskan
  * `agents.defaults.model` / `models.providers` (jika Minimax dipilih)
  * `tools.profile` (onboarding lokal default ke `"coding"` ketika belum diatur; nilai eksplisit yang sudah ada dipertahankan)
  * `gateway.*` (mode, bind, auth, tailscale)
  * `session.dmScope` (onboarding lokal default ke `per-channel-peer` ketika belum diatur; nilai eksplisit yang sudah ada dipertahankan)
  * `channels.telegram.botToken`, `channels.discord.token`, `channels.matrix.*`, `channels.signal.*`, `channels.imessage.*`
  * Allowlist saluran (Slack, Discord, Matrix, Microsoft Teams) ketika Anda ikut serta selama prompt (nama diresolusikan ke ID jika memungkinkan)
  * `skills.install.nodeManager`
    * Flag `setup --node-manager` menerima `npm`, `pnpm`, atau `bun`.
    * Konfigurasi manual masih dapat mengatur `skills.install.nodeManager: "yarn"` nanti.
  * `wizard.lastRunAt`
  * `wizard.lastRunVersion`
  * `wizard.lastRunCommit`
  * `wizard.lastRunCommand`
  * `wizard.lastRunMode`


`openclaw agents add` menulis `agents.list[]` dan `bindings` opsional.

Kredensial WhatsApp ditempatkan di bawah `~/.openclaw/credentials/whatsapp/<accountId>/`. Sesi disimpan di bawah `~/.openclaw/agents/<agentId>/sessions/`.

RPC wizard Gateway:

  * `wizard.start`
  * `wizard.next`
  * `wizard.cancel`
  * `wizard.status`


Klien (aplikasi macOS dan Control UI) dapat merender langkah tanpa mengimplementasikan ulang logika onboarding.

Perilaku penyiapan Signal:

  * Mengunduh aset rilis yang sesuai
  * Menyimpannya di bawah `~/.openclaw/tools/signal-cli/<version>/`
  * Menulis `channels.signal.cliPath` dalam konfigurasi
  * Build JVM memerlukan Java 21
  * Build native digunakan ketika tersedia
  * Windows menggunakan WSL2 dan mengikuti alur signal-cli Linux di dalam WSL


## Dokumen Terkait

  * Hub onboarding: [Onboarding (CLI)](</id/start/wizard>)
  * Otomasi dan skrip: [Otomasi CLI](</id/start/wizard-cli-automation>)
  * Referensi perintah: [`openclaw onboard`](</id/cli/onboard>)


Was this useful?YesNo