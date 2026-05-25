---
title: Microsoft Teams
source_url: https://docs.openclaw.ai/id/channels/msteams
scraped_at: 2026-05-25
---

Status: teks + lampiran DM didukung; pengiriman file channel/grup memerlukan `sharePointSiteId` \+ izin Graph (lihat Mengirim file dalam obrolan grup). Poll dikirim melalui Adaptive Cards. Tindakan pesan mengekspos `upload-file` eksplisit untuk pengiriman yang mengutamakan file.

## Plugin bawaan

Microsoft Teams dikirim sebagai Plugin bawaan dalam rilis OpenClaw saat ini, jadi tidak diperlukan instalasi terpisah dalam build paket normal.

Jika Anda menggunakan build lama atau instalasi kustom yang mengecualikan Teams bawaan, instal paket npm secara langsung:

bashCopy code
[code]
    openclaw plugins install @openclaw/msteams
[/code]

Gunakan paket polos untuk mengikuti tag rilis resmi saat ini. Sematkan versi persis hanya saat Anda memerlukan instalasi yang dapat direproduksi.

Checkout lokal (saat berjalan dari repo git):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/msteams-plugin
[/code]

Detail: [Plugin](</id/tools/plugin>)

## Penyiapan cepat

[`@microsoft/teams.cli`](<https://www.npmjs.com/package/@microsoft/teams.cli>) menangani pendaftaran bot, pembuatan manifest, dan pembuatan kredensial dalam satu perintah.

**1\. Instal dan masuk**

bashCopy code
[code]
    npm install -g @microsoft/teams.cli@previewteams loginteams status   # verify you're logged in and see your tenant info
[/code]

**2\. Mulai tunnel** (Teams tidak dapat menjangkau localhost)

Instal dan autentikasi devtunnel CLI jika Anda belum melakukannya ([panduan memulai](<https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/get-started>)).

bashCopy code
[code]
    # One-time setup (persistent URL across sessions):devtunnel create my-openclaw-bot --allow-anonymousdevtunnel port create my-openclaw-bot -p 3978 --protocol auto # Each dev session:devtunnel host my-openclaw-bot# Your endpoint: https://<tunnel-id>.devtunnels.ms/api/messages
[/code]

Alternatif: `ngrok http 3978` atau `tailscale funnel 3978` (tetapi ini dapat mengubah URL setiap sesi).

**3\. Buat aplikasi**

bashCopy code
[code]
    teams app create \  --name "OpenClaw" \  --endpoint "https://<your-tunnel-url>/api/messages"
[/code]

Perintah tunggal ini:

  * Membuat aplikasi Entra ID (Azure AD)
  * Menghasilkan client secret
  * Membangun dan mengunggah manifest aplikasi Teams (dengan ikon)
  * Mendaftarkan bot (dikelola Teams secara default - tidak perlu langganan Azure)


Output akan menampilkan `CLIENT_ID`, `CLIENT_SECRET`, `TENANT_ID`, dan **Teams App ID** \- catat ini untuk langkah berikutnya. Output juga menawarkan untuk menginstal aplikasi di Teams secara langsung.

**4\. Konfigurasikan OpenClaw** menggunakan kredensial dari output:

json5Copy code
[code]
    {  channels: {    msteams: {      enabled: true,      appId: "&lt;CLIENT_ID&gt;",      appPassword: "&lt;CLIENT_SECRET&gt;",      tenantId: "&lt;TENANT_ID&gt;",      webhook: { port: 3978, path: "/api/messages" },    },  },}
[/code]

Atau gunakan variabel lingkungan secara langsung: `MSTEAMS_APP_ID`, `MSTEAMS_APP_PASSWORD`, `MSTEAMS_TENANT_ID`.

**5\. Instal aplikasi di Teams**

`teams app create` akan meminta Anda menginstal aplikasi - pilih "Install in Teams". Jika Anda melewatkannya, Anda dapat memperoleh tautannya nanti:

bashCopy code
[code]
    teams app get <teamsAppId> --install-link
[/code]

**6\. Verifikasi semuanya berfungsi**

bashCopy code
[code]
    teams app doctor <teamsAppId>
[/code]

Ini menjalankan diagnostik di seluruh pendaftaran bot, konfigurasi aplikasi AAD, validitas manifest, dan penyiapan SSO.

Untuk deployment produksi, pertimbangkan menggunakan [autentikasi terfederasi](</id/channels/msteams#federated-authentication-certificate-plus-managed-identity>) (sertifikat atau managed identity) alih-alih client secret.

## Tujuan

  * Berbicara dengan OpenClaw melalui DM Teams, obrolan grup, atau channel.
  * Menjaga routing tetap deterministik: balasan selalu kembali ke channel tempat balasan diterima.
  * Secara default menggunakan perilaku channel yang aman (mention diperlukan kecuali dikonfigurasi lain).


## Penulisan konfigurasi

Secara default, Microsoft Teams diizinkan menulis pembaruan konfigurasi yang dipicu oleh `/config set|unset` (memerlukan `commands.config: true`).

Nonaktifkan dengan:

json5Copy code
[code]
    {  channels: { msteams: { configWrites: false } },}
[/code]

## Kontrol akses (DM + grup)

**Akses DM**

  * Default: `channels.msteams.dmPolicy = "pairing"`. Pengirim tidak dikenal diabaikan hingga disetujui.
  * `channels.msteams.allowFrom` harus menggunakan ID objek AAD yang stabil atau grup akses pengirim statis seperti `accessGroup:core-team`.
  * Jangan mengandalkan pencocokan UPN/nama tampilan untuk allowlist - keduanya dapat berubah. OpenClaw menonaktifkan pencocokan nama langsung secara default; ikut serta secara eksplisit dengan `channels.msteams.dangerouslyAllowNameMatching: true`.
  * Wizard dapat menyelesaikan nama menjadi ID melalui Microsoft Graph saat kredensial mengizinkan.


**Akses grup**

  * Default: `channels.msteams.groupPolicy = "allowlist"` (diblokir kecuali Anda menambahkan `groupAllowFrom`). Gunakan `channels.defaults.groupPolicy` untuk menimpa default saat belum ditetapkan.
  * `channels.msteams.groupAllowFrom` mengontrol pengirim atau grup akses pengirim statis mana yang dapat memicu dalam obrolan grup/channel (fallback ke `channels.msteams.allowFrom`).
  * Tetapkan `groupPolicy: "open"` untuk mengizinkan anggota mana pun (tetap dibatasi mention secara default).
  * Untuk tidak mengizinkan **channel apa pun** , tetapkan `channels.msteams.groupPolicy: "disabled"`.


Contoh:

json5Copy code
[code]
    {  channels: {    msteams: {      groupPolicy: "allowlist",      groupAllowFrom: ["00000000-0000-0000-0000-000000000000", "accessGroup:core-team"],    },  },}
[/code]

**Teams + allowlist channel**

  * Batasi cakupan balasan grup/channel dengan mencantumkan teams dan channel di bawah `channels.msteams.teams`.
  * Key harus menggunakan ID percakapan Teams yang stabil dari tautan Teams, bukan nama tampilan yang dapat berubah.
  * Saat `groupPolicy="allowlist"` dan allowlist teams ada, hanya teams/channel yang tercantum yang diterima (dibatasi mention).
  * Wizard konfigurasi menerima entri `Team/Channel` dan menyimpannya untuk Anda.
  * Saat startup, OpenClaw menyelesaikan nama allowlist team/channel dan pengguna menjadi ID (saat izin Graph mengizinkan) dan mencatat pemetaan; nama team/channel yang tidak terselesaikan disimpan sebagaimana diketik tetapi diabaikan untuk routing secara default kecuali `channels.msteams.dangerouslyAllowNameMatching: true` diaktifkan.


Contoh:

json5Copy code
[code]
    {  channels: {    msteams: {      groupPolicy: "allowlist",      teams: {        "My Team": {          channels: {            General: { requireMention: true },          },        },      },    },  },}
[/code]

**Penyiapan manual (tanpa Teams CLI)**

Jika Anda tidak dapat menggunakan Teams CLI, Anda dapat menyiapkan bot secara manual melalui Azure Portal.

### Cara kerjanya

  1. Pastikan Plugin Microsoft Teams tersedia (dibundel dalam rilis saat ini).
  2. Buat **Azure Bot** (App ID + secret + tenant ID).
  3. Bangun **paket aplikasi Teams** yang mereferensikan bot dan menyertakan izin RSC di bawah.
  4. Unggah/instal aplikasi Teams ke dalam team (atau cakupan personal untuk DM).
  5. Konfigurasikan `msteams` di `~/.openclaw/openclaw.json` (atau variabel lingkungan) dan mulai Gateway.
  6. Gateway mendengarkan traffic Webhook Bot Framework di `/api/messages` secara default.


### Langkah 1: Buat Azure Bot

  1. Buka [Buat Azure Bot](<https://portal.azure.com/#create/Microsoft.AzureBot>)

  2. Isi tab **Basics** :

Bidang | Nilai  
---|---  
**Bot handle** | Nama bot Anda, misalnya, `openclaw-msteams` (harus unik)  
**Subscription** | Pilih langganan Azure Anda  
**Resource group** | Buat baru atau gunakan yang ada  
**Pricing tier** | **Free** untuk dev/pengujian  
**Type of App** | **Single Tenant** (direkomendasikan - lihat catatan di bawah)  
**Creation type** | **Create new Microsoft App ID**  


  3. Klik **Review + create** → **Create** (tunggu ~1-2 menit)


### Langkah 2: Dapatkan kredensial

  1. Buka sumber daya Azure Bot Anda → **Configuration**
  2. Salin **Microsoft App ID** → ini adalah `appId` Anda
  3. Klik **Manage Password** → buka App Registration
  4. Di bawah **Certificates & secrets** → **New client secret** → salin **Value** → ini adalah `appPassword` Anda
  5. Buka **Overview** → salin **Directory (tenant) ID** → ini adalah `tenantId` Anda


### Langkah 3: Konfigurasikan endpoint Messaging

  1. Di Azure Bot → **Configuration**
  2. Tetapkan **Messaging endpoint** ke URL Webhook Anda: 
     * Produksi: `https://your-domain.com/api/messages`
     * Dev lokal: Gunakan tunnel (lihat Pengembangan Lokal di bawah)


### Langkah 4: Aktifkan channel Teams

  1. Di Azure Bot → **Channels**
  2. Klik **Microsoft Teams** → Configure → Save
  3. Terima Terms of Service


### Langkah 5: Bangun manifest aplikasi Teams

  * Sertakan entri `bot` dengan `botId = &lt;App ID&gt;`.
  * Cakupan: `personal`, `team`, `groupChat`.
  * `supportsFiles: true` (diperlukan untuk penanganan file cakupan personal).
  * Tambahkan izin RSC (lihat Izin RSC).
  * Buat ikon: `outline.png` (32x32) dan `color.png` (192x192).
  * Zip ketiga file bersama-sama: `manifest.json`, `outline.png`, `color.png`.


### Langkah 6: Konfigurasikan OpenClaw

json5Copy code
[code]
    {  channels: {    msteams: {      enabled: true,      appId: "&lt;APP_ID&gt;",      appPassword: "&lt;APP_PASSWORD&gt;",      tenantId: "&lt;TENANT_ID&gt;",      webhook: { port: 3978, path: "/api/messages" },    },  },}
[/code]

Variabel lingkungan: `MSTEAMS_APP_ID`, `MSTEAMS_APP_PASSWORD`, `MSTEAMS_TENANT_ID`.

### Langkah 7: Jalankan Gateway

Channel Teams dimulai secara otomatis saat Plugin tersedia dan konfigurasi `msteams` ada dengan kredensial.

## Autentikasi terfederasi (sertifikat plus managed identity)

> Ditambahkan pada 2026.4.11

Untuk deployment produksi, OpenClaw mendukung **autentikasi terfederasi** sebagai alternatif yang lebih aman untuk client secret. Tersedia dua metode:

### Opsi A: Autentikasi berbasis sertifikat

Gunakan sertifikat PEM yang terdaftar dengan pendaftaran aplikasi Entra ID Anda.

**Penyiapan:**

  1. Buat atau dapatkan sertifikat (format PEM dengan private key).
  2. Di Entra ID → App Registration → **Certificates & secrets** → **Certificates** → Unggah sertifikat publik.


**Konfigurasi:**

json5Copy code
[code]
    {  channels: {    msteams: {      enabled: true,      appId: "&lt;APP_ID&gt;",      tenantId: "&lt;TENANT_ID&gt;",      authType: "federated",      certificatePath: "/path/to/cert.pem",      webhook: { port: 3978, path: "/api/messages" },    },  },}
[/code]

**Variabel lingkungan:**

  * `MSTEAMS_AUTH_TYPE=federated`
  * `MSTEAMS_CERTIFICATE_PATH=/path/to/cert.pem`


### Opsi B: Azure Managed Identity

Gunakan Azure Managed Identity untuk autentikasi tanpa kata sandi. Ini ideal untuk deployment pada infrastruktur Azure (AKS, App Service, Azure VM) tempat managed identity tersedia.

**Cara kerjanya:**

  1. Pod/VM bot memiliki managed identity (ditetapkan sistem atau ditetapkan pengguna).
  2. **Kredensial identitas terfederasi** menautkan managed identity ke pendaftaran aplikasi Entra ID.
  3. Saat runtime, OpenClaw menggunakan `@azure/identity` untuk memperoleh token dari endpoint Azure IMDS (`169.254.169.254`).
  4. Token diteruskan ke Teams SDK untuk autentikasi bot.


**Prasyarat:**

  * Infrastruktur Azure dengan managed identity diaktifkan (identitas workload AKS, App Service, VM)
  * Kredensial identitas terfederasi dibuat pada pendaftaran aplikasi Entra ID
  * Akses jaringan ke IMDS (`169.254.169.254:80`) dari pod/VM


**Konfigurasi (managed identity yang ditetapkan sistem):**

json5Copy code
[code]
    {  channels: {    msteams: {      enabled: true,      appId: "&lt;APP_ID&gt;",      tenantId: "&lt;TENANT_ID&gt;",      authType: "federated",      useManagedIdentity: true,      webhook: { port: 3978, path: "/api/messages" },    },  },}
[/code]

**Konfigurasi (managed identity yang ditetapkan pengguna):**

json5Copy code
[code]
    {  channels: {    msteams: {      enabled: true,      appId: "&lt;APP_ID&gt;",      tenantId: "&lt;TENANT_ID&gt;",      authType: "federated",      useManagedIdentity: true,      managedIdentityClientId: "&lt;MI_CLIENT_ID&gt;",      webhook: { port: 3978, path: "/api/messages" },    },  },}
[/code]

**Variabel lingkungan:**

  * `MSTEAMS_AUTH_TYPE=federated`
  * `MSTEAMS_USE_MANAGED_IDENTITY=true`
  * `MSTEAMS_MANAGED_IDENTITY_CLIENT_ID=<client-id>` (hanya untuk yang ditetapkan pengguna)


### Penyiapan AKS Workload Identity

Untuk deployment AKS yang menggunakan workload identity:

  1. **Aktifkan workload identity** pada kluster AKS Anda.

  2. **Buat kredensial identitas federasi** pada pendaftaran aplikasi Entra ID:

bashCopy code
[code]az ad app federated-credential create --id &lt;APP_OBJECT_ID&gt; --parameters '{  "name": "my-bot-workload-identity",  "issuer": "&lt;AKS_OIDC_ISSUER_URL&gt;",  "subject": "system:serviceaccount:&lt;NAMESPACE&gt;:&lt;SERVICE_ACCOUNT&gt;",  "audiences": ["api://AzureADTokenExchange"]}'
[/code]

  3. **Anotasikan akun layanan Kubernetes** dengan ID klien aplikasi:

yamlCopy code
[code]apiVersion: v1kind: ServiceAccountmetadata:  name: my-bot-sa  annotations:    azure.workload.identity/client-id: "&lt;APP_CLIENT_ID&gt;"
[/code]

  4. **Beri label pada pod** untuk injeksi workload identity:

yamlCopy code
[code]metadata:  labels:    azure.workload.identity/use: "true"
[/code]

  5. **Pastikan akses jaringan** ke IMDS (`169.254.169.254`) - jika menggunakan NetworkPolicy, tambahkan aturan egress yang mengizinkan lalu lintas ke `169.254.169.254/32` pada port 80.


### Perbandingan jenis autentikasi

Metode | Konfigurasi | Kelebihan | Kekurangan  
---|---|---|---  
**Rahasia klien** | `appPassword` | Penyiapan sederhana | Rotasi rahasia diperlukan, kurang aman  
**Sertifikat** | `authType: "federated"` \+ `certificatePath` | Tidak ada rahasia bersama melalui jaringan | Beban pengelolaan sertifikat  
**Managed Identity** | `authType: "federated"` \+ `useManagedIdentity` | Tanpa kata sandi, tidak ada rahasia untuk dikelola | Infrastruktur Azure diperlukan  
  
**Perilaku default:** Saat `authType` tidak diatur, OpenClaw menggunakan autentikasi rahasia klien secara default. Konfigurasi yang sudah ada tetap berfungsi tanpa perubahan.

## Pengembangan lokal (tunneling)

Teams tidak dapat menjangkau `localhost`. Gunakan tunnel pengembangan persisten agar URL Anda tetap sama di seluruh sesi:

bashCopy code
[code]
    # One-time setup:devtunnel create my-openclaw-bot --allow-anonymousdevtunnel port create my-openclaw-bot -p 3978 --protocol auto # Each dev session:devtunnel host my-openclaw-bot
[/code]

Alternatif: `ngrok http 3978` atau `tailscale funnel 3978` (URL dapat berubah pada setiap sesi).

Jika URL tunnel Anda berubah, perbarui endpoint:

bashCopy code
[code]
    teams app update <teamsAppId> --endpoint "https://<new-url>/api/messages"
[/code]

## Menguji Bot

**Jalankan diagnostik:**

bashCopy code
[code]
    teams app doctor <teamsAppId>
[/code]

Memeriksa pendaftaran bot, aplikasi AAD, manifes, dan konfigurasi SSO dalam satu lintasan.

**Kirim pesan uji:**

  1. Instal aplikasi Teams (gunakan tautan instal dari `teams app get <id> --install-link`)
  2. Temukan bot di Teams dan kirim DM
  3. Periksa log Gateway untuk aktivitas masuk


## Variabel lingkungan

Semua kunci konfigurasi dapat diatur melalui variabel lingkungan sebagai gantinya:

  * `MSTEAMS_APP_ID`
  * `MSTEAMS_APP_PASSWORD`
  * `MSTEAMS_TENANT_ID`
  * `MSTEAMS_AUTH_TYPE` (opsional: `"secret"` atau `"federated"`)
  * `MSTEAMS_CERTIFICATE_PATH` (federated + sertifikat)
  * `MSTEAMS_CERTIFICATE_THUMBPRINT` (opsional, tidak diperlukan untuk autentikasi)
  * `MSTEAMS_USE_MANAGED_IDENTITY` (federated + managed identity)
  * `MSTEAMS_MANAGED_IDENTITY_CLIENT_ID` (hanya MI yang ditetapkan pengguna)


## Tindakan info anggota

OpenClaw mengekspos tindakan `member-info` yang didukung Graph untuk Microsoft Teams agar agent dan automasi dapat me-resolve detail anggota channel (nama tampilan, email, peran) langsung dari Microsoft Graph.

Persyaratan:

  * Izin RSC `Member.Read.Group` (sudah ada dalam manifes yang direkomendasikan)
  * Untuk lookup lintas tim: izin Graph Application `User.Read.All` dengan persetujuan admin


Tindakan ini dikendalikan oleh `channels.msteams.actions.memberInfo` (default: aktif saat kredensial Graph tersedia).

## Konteks riwayat

  * `channels.msteams.historyLimit` mengontrol berapa banyak pesan channel/grup terbaru yang dibungkus ke dalam prompt.
  * Fallback ke `messages.groupChat.historyLimit`. Atur `0` untuk menonaktifkan (default 50).
  * Riwayat thread yang diambil difilter berdasarkan daftar izin pengirim (`allowFrom` / `groupAllowFrom`), sehingga penyemaian konteks thread hanya menyertakan pesan dari pengirim yang diizinkan.
  * Konteks lampiran yang dikutip (`ReplyTo*` yang diturunkan dari HTML balasan Teams) saat ini diteruskan sebagaimana diterima.
  * Dengan kata lain, daftar izin mengatur siapa yang dapat memicu agent; hanya jalur konteks tambahan tertentu yang difilter saat ini.
  * Riwayat DM dapat dibatasi dengan `channels.msteams.dmHistoryLimit` (giliran pengguna). Override per pengguna: `channels.msteams.dms["<user_id>"].historyLimit`.


## Izin RSC Teams saat ini (manifes)

Berikut adalah **izin resourceSpecific yang ada** dalam manifes aplikasi Teams kami. Izin ini hanya berlaku di dalam tim/chat tempat aplikasi diinstal.

**Untuk channel (cakupan tim):**

  * `ChannelMessage.Read.Group` (Application) - menerima semua pesan channel tanpa @mention
  * `ChannelMessage.Send.Group` (Application)
  * `Member.Read.Group` (Application)
  * `Owner.Read.Group` (Application)
  * `ChannelSettings.Read.Group` (Application)
  * `TeamMember.Read.Group` (Application)
  * `TeamSettings.Read.Group` (Application)


**Untuk chat grup:**

  * `ChatMessage.Read.Chat` (Application) - menerima semua pesan chat grup tanpa @mention


Untuk menambahkan izin RSC melalui Teams CLI:

bashCopy code
[code]
    teams app rsc add <teamsAppId> ChannelMessage.Read.Group --type Application
[/code]

## Contoh manifes Teams (disunting)

Contoh minimal dan valid dengan kolom yang diperlukan. Ganti ID dan URL.

json5Copy code
[code]
    {  $schema: "https://developer.microsoft.com/en-us/json-schemas/teams/v1.23/MicrosoftTeams.schema.json",  manifestVersion: "1.23",  version: "1.0.0",  id: "00000000-0000-0000-0000-000000000000",  name: { short: "OpenClaw" },  developer: {    name: "Your Org",    websiteUrl: "https://example.com",    privacyUrl: "https://example.com/privacy",    termsOfUseUrl: "https://example.com/terms",  },  description: { short: "OpenClaw in Teams", full: "OpenClaw in Teams" },  icons: { outline: "outline.png", color: "color.png" },  accentColor: "#5B6DEF",  bots: [    {      botId: "11111111-1111-1111-1111-111111111111",      scopes: ["personal", "team", "groupChat"],      isNotificationOnly: false,      supportsCalling: false,      supportsVideo: false,      supportsFiles: true,    },  ],  webApplicationInfo: {    id: "11111111-1111-1111-1111-111111111111",  },  authorization: {    permissions: {      resourceSpecific: [        { name: "ChannelMessage.Read.Group", type: "Application" },        { name: "ChannelMessage.Send.Group", type: "Application" },        { name: "Member.Read.Group", type: "Application" },        { name: "Owner.Read.Group", type: "Application" },        { name: "ChannelSettings.Read.Group", type: "Application" },        { name: "TeamMember.Read.Group", type: "Application" },        { name: "TeamSettings.Read.Group", type: "Application" },        { name: "ChatMessage.Read.Chat", type: "Application" },      ],    },  },}
[/code]

### Catatan manifes (kolom wajib)

  * `bots[].botId` **harus** cocok dengan ID Aplikasi Azure Bot.
  * `webApplicationInfo.id` **harus** cocok dengan ID Aplikasi Azure Bot.
  * `bots[].scopes` harus menyertakan permukaan yang Anda rencanakan untuk digunakan (`personal`, `team`, `groupChat`).
  * `bots[].supportsFiles: true` diperlukan untuk penanganan file dalam cakupan personal.
  * `authorization.permissions.resourceSpecific` harus menyertakan baca/kirim channel jika Anda menginginkan lalu lintas channel.


### Memperbarui aplikasi yang ada

Untuk memperbarui aplikasi Teams yang sudah terinstal (misalnya, untuk menambahkan izin RSC):

bashCopy code
[code]
    # Download, edit, and re-upload the manifestteams app manifest download <teamsAppId> manifest.json# Edit manifest.json locally...teams app manifest upload manifest.json <teamsAppId># Version is auto-bumped if content changed
[/code]

Setelah memperbarui, instal ulang aplikasi di setiap tim agar izin baru berlaku, dan **keluar sepenuhnya lalu luncurkan ulang Teams** (bukan hanya menutup jendela) untuk menghapus metadata aplikasi yang di-cache.

Pembaruan manifes manual (tanpa CLI)

  1. Perbarui `manifest.json` Anda dengan pengaturan baru
  2. **Naikkan kolom`version`** (misalnya, `1.0.0` → `1.1.0`)
  3. **Zip ulang** manifes dengan ikon (`manifest.json`, `outline.png`, `color.png`)
  4. Unggah zip baru: 
     * **Teams Admin Center:** Aplikasi Teams → Kelola aplikasi → temukan aplikasi Anda → Unggah versi baru
     * **Sideload:** Di Teams → Aplikasi → Kelola aplikasi Anda → Unggah aplikasi kustom


## Kemampuan: hanya RSC vs Graph

### Dengan **hanya Teams RSC** (aplikasi terinstal, tanpa izin Graph API)

Berfungsi:

  * Membaca konten **teks** pesan channel.
  * Mengirim konten **teks** pesan channel.
  * Menerima lampiran file **personal (DM)**.


TIDAK berfungsi:

  * **Isi gambar atau file** channel/grup (payload hanya menyertakan stub HTML).
  * Mengunduh lampiran yang disimpan di SharePoint/OneDrive.
  * Membaca riwayat pesan (di luar event Webhook langsung).


### Dengan **Teams RSC + izin Microsoft Graph Application**

Menambahkan:

  * Mengunduh konten yang di-host (gambar yang ditempelkan ke pesan).
  * Mengunduh lampiran file yang disimpan di SharePoint/OneDrive.
  * Membaca riwayat pesan channel/chat melalui Graph.


### RSC vs Graph API

Kemampuan | Izin RSC | Graph API  
---|---|---  
**Pesan real-time** | Ya (melalui Webhook) | Tidak (hanya polling)  
**Pesan historis** | Tidak | Ya (dapat mengueri riwayat)  
**Kompleksitas penyiapan** | Hanya manifes aplikasi | Memerlukan persetujuan admin + alur token  
**Berfungsi offline** | Tidak (harus berjalan) | Ya (kueri kapan saja)  
  
**Intinya:** RSC untuk mendengarkan secara real-time; Graph API untuk akses historis. Untuk mengejar pesan yang terlewat saat offline, Anda memerlukan Graph API dengan `ChannelMessage.Read.All` (memerlukan persetujuan admin).

## Media + riwayat yang diaktifkan Graph (diperlukan untuk channel)

Jika Anda memerlukan gambar/file di **channel** atau ingin mengambil **riwayat pesan** , Anda harus mengaktifkan izin Microsoft Graph dan memberikan persetujuan admin.

  1. Di Entra ID (Azure AD) **App Registration** , tambahkan **izin Application** Microsoft Graph: 
     * `ChannelMessage.Read.All` (lampiran channel + riwayat)
     * `Chat.Read.All` atau `ChatMessage.Read.All` (chat grup)
  2. **Berikan persetujuan admin** untuk tenant.
  3. Naikkan **versi manifes** aplikasi Teams, unggah ulang, dan **instal ulang aplikasi di Teams**.
  4. **Keluar sepenuhnya lalu luncurkan ulang Teams** untuk menghapus metadata aplikasi yang di-cache.


**Izin tambahan untuk mention pengguna:** @mention pengguna berfungsi langsung untuk pengguna dalam percakapan. Namun, jika Anda ingin mencari dan me-mention pengguna secara dinamis yang **tidak berada dalam percakapan saat ini** , tambahkan izin `User.Read.All` (Application) dan berikan persetujuan admin.

## Batasan yang diketahui

### Timeout Webhook

Teams mengirimkan pesan melalui Webhook HTTP. Jika pemrosesan terlalu lama (misalnya, respons LLM yang lambat), Anda mungkin melihat:

  * Timeout Gateway
  * Teams mencoba ulang pesan (menyebabkan duplikasi)
  * Balasan yang terlewat


OpenClaw menangani ini dengan kembali secara cepat dan mengirim balasan secara proaktif, tetapi respons yang sangat lambat masih dapat menyebabkan masalah.

### Pemformatan

Markdown Teams lebih terbatas daripada Slack atau Discord:

  * Pemformatan dasar berfungsi: **tebal** , _miring_ , `code`, tautan
  * Markdown kompleks (tabel, daftar bertingkat) mungkin tidak dirender dengan benar
  * Adaptive Cards didukung untuk jajak pendapat dan pengiriman presentasi semantik (lihat di bawah)


## Konfigurasi

Pengaturan utama (lihat `/gateway/configuration` untuk pola channel bersama):

  * `channels.msteams.enabled`: aktifkan/nonaktifkan channel.
  * `channels.msteams.appId`, `channels.msteams.appPassword`, `channels.msteams.tenantId`: kredensial bot.
  * `channels.msteams.webhook.port` (default `3978`)
  * `channels.msteams.webhook.path` (default `/api/messages`)
  * `channels.msteams.dmPolicy`: `pairing | allowlist | open | disabled` (default: pairing)
  * `channels.msteams.allowFrom`: daftar yang diizinkan untuk DM (ID objek AAD direkomendasikan). Wizard menyelesaikan nama menjadi ID saat penyiapan ketika akses Graph tersedia.
  * `channels.msteams.dangerouslyAllowNameMatching`: toggle darurat untuk mengaktifkan kembali pencocokan UPN/nama tampilan yang dapat berubah dan perutean nama tim/channel langsung.
  * `channels.msteams.textChunkLimit`: ukuran potongan teks keluar.
  * `channels.msteams.chunkMode`: `length` (default) atau `newline` untuk memisahkan pada baris kosong (batas paragraf) sebelum pemotongan berdasarkan panjang.
  * `channels.msteams.mediaAllowHosts`: daftar host yang diizinkan untuk lampiran masuk (default ke domain Microsoft/Teams).
  * `channels.msteams.mediaAuthAllowHosts`: daftar host yang diizinkan untuk melampirkan header Authorization pada percobaan ulang media (default ke host Graph + Bot Framework).
  * `channels.msteams.requireMention`: wajibkan @mention di channel/grup (default true).
  * `channels.msteams.replyStyle`: `thread | top-level` (lihat Gaya Balasan).
  * `channels.msteams.teams.<teamId>.replyStyle`: override per tim.
  * `channels.msteams.teams.<teamId>.requireMention`: override per tim.
  * `channels.msteams.teams.<teamId>.tools`: override kebijakan tool default per tim (`allow`/`deny`/`alsoAllow`) yang digunakan saat override channel tidak ada.
  * `channels.msteams.teams.<teamId>.toolsBySender`: override kebijakan tool default per tim per pengirim (`"*"` wildcard didukung).
  * `channels.msteams.teams.<teamId>.channels.<conversationId>.replyStyle`: override per channel.
  * `channels.msteams.teams.<teamId>.channels.<conversationId>.requireMention`: override per channel.
  * `channels.msteams.teams.<teamId>.channels.<conversationId>.tools`: override kebijakan tool per channel (`allow`/`deny`/`alsoAllow`).
  * `channels.msteams.teams.<teamId>.channels.<conversationId>.toolsBySender`: override kebijakan tool per channel per pengirim (`"*"` wildcard didukung).
  * Kunci `toolsBySender` sebaiknya menggunakan prefiks eksplisit: `channel:`, `id:`, `e164:`, `username:`, `name:` (kunci lama tanpa prefiks masih hanya dipetakan ke `id:`).
  * `channels.msteams.actions.memberInfo`: aktifkan atau nonaktifkan aksi info anggota yang didukung Graph (default: diaktifkan ketika kredensial Graph tersedia).
  * `channels.msteams.authType`: jenis autentikasi - `"secret"` (default) atau `"federated"`.
  * `channels.msteams.certificatePath`: path ke file sertifikat PEM (federated + autentikasi sertifikat).
  * `channels.msteams.certificateThumbprint`: thumbprint sertifikat (opsional, tidak diperlukan untuk autentikasi).
  * `channels.msteams.useManagedIdentity`: aktifkan autentikasi managed identity (mode federated).
  * `channels.msteams.managedIdentityClientId`: ID klien untuk managed identity yang ditetapkan pengguna.
  * `channels.msteams.sharePointSiteId`: ID situs SharePoint untuk unggahan file dalam obrolan grup/channel (lihat Mengirim file dalam obrolan grup).


## Perutean dan sesi

  * Kunci sesi mengikuti format agen standar (lihat [/concepts/session](</id/concepts/session>)): 
    * Pesan langsung berbagi sesi utama (`agent:<agentId>:<mainKey>`).
    * Pesan channel/grup menggunakan ID percakapan: 
      * `agent:<agentId>:msteams:channel:<conversationId>`
      * `agent:<agentId>:msteams:group:<conversationId>`


## Gaya balasan: thread vs postingan

Teams baru-baru ini memperkenalkan dua gaya UI channel di atas model data dasar yang sama:

Gaya | Deskripsi | `replyStyle` yang direkomendasikan  
---|---|---  
**Postingan** (klasik) | Pesan muncul sebagai kartu dengan balasan ber-thread di bawahnya | `thread` (default)  
**Thread** (mirip Slack) | Pesan mengalir secara linear, lebih mirip Slack | `top-level`  
  
**Masalahnya:** API Teams tidak mengekspos gaya UI mana yang digunakan channel. Jika Anda menggunakan `replyStyle` yang salah:

  * `thread` di channel bergaya Thread → balasan muncul bertingkat dengan canggung
  * `top-level` di channel bergaya Postingan → balasan muncul sebagai postingan tingkat atas terpisah, bukan di dalam thread


**Solusi:** Konfigurasikan `replyStyle` per channel berdasarkan bagaimana channel disiapkan:

json5Copy code
[code]
    {  channels: {    msteams: {      replyStyle: "thread",      teams: {        "19:abc...@thread.tacv2": {          channels: {            "19:xyz...@thread.tacv2": {              replyStyle: "top-level",            },          },        },      },    },  },}
[/code]

### Prioritas resolusi

Ketika bot mengirim balasan ke channel, `replyStyle` diselesaikan dari override yang paling spesifik hingga default. Nilai pertama yang bukan `undefined` yang menang:

  1. **Per channel** — `channels.msteams.teams.<teamId>.channels.<conversationId>.replyStyle`
  2. **Per tim** — `channels.msteams.teams.<teamId>.replyStyle`
  3. **Global** — `channels.msteams.replyStyle`
  4. **Default implisit** — diturunkan dari `requireMention`: 
     * `requireMention: true` → `thread`
     * `requireMention: false` → `top-level`


Jika Anda menetapkan `requireMention: false` secara global tanpa `replyStyle` eksplisit, mention di channel bergaya Postingan akan muncul sebagai postingan tingkat atas meskipun pesan masuknya adalah balasan thread. Pin `replyStyle: "thread"` pada tingkat global, tim, atau channel untuk menghindari kejutan.

### Pelestarian konteks thread

Ketika `replyStyle: "thread"` berlaku dan bot di-@mention dari dalam thread channel, OpenClaw melampirkan kembali root thread asli ke referensi percakapan keluar (`19:…@thread.tacv2;messageid=<root>`) agar balasan masuk ke thread yang sama. Ini berlaku untuk pengiriman live (dalam turn) maupun pengiriman proaktif yang dibuat setelah konteks turn Bot Framework kedaluwarsa (misalnya, agen yang berjalan lama, balasan tool-call antrean melalui `mcp__openclaw__message`).

Root thread diambil dari `threadId` yang disimpan pada referensi percakapan. Referensi tersimpan lama yang dibuat sebelum `threadId` kembali menggunakan `activityId` (aktivitas masuk apa pun yang terakhir menanam percakapan), sehingga deployment yang ada tetap berfungsi tanpa seeding ulang.

Ketika `replyStyle: "top-level"` berlaku, pesan masuk thread channel sengaja dijawab sebagai postingan tingkat atas baru — tidak ada sufiks thread yang dilampirkan. Ini adalah perilaku yang benar untuk channel bergaya Thread; jika Anda melihat postingan tingkat atas ketika mengharapkan balasan ber-thread, `replyStyle` Anda diatur secara keliru untuk channel tersebut.

## Lampiran dan gambar

**Batasan saat ini:**

  * **DM:** Gambar dan lampiran file berfungsi melalui API file bot Teams.
  * **Channel/grup:** Lampiran berada di penyimpanan M365 (SharePoint/OneDrive). Payload Webhook hanya menyertakan stub HTML, bukan byte file aktual. **Izin Graph API diperlukan** untuk mengunduh lampiran channel.
  * Untuk pengiriman eksplisit yang mendahulukan file, gunakan `action=upload-file` dengan `media` / `filePath` / `path`; `message` opsional menjadi teks/komentar pendamping, dan `filename` mengganti nama unggahan.


Tanpa izin Graph, pesan channel dengan gambar akan diterima sebagai teks saja (konten gambar tidak dapat diakses oleh bot). Secara default, OpenClaw hanya mengunduh media dari hostname Microsoft/Teams. Override dengan `channels.msteams.mediaAllowHosts` (gunakan `["*"]` untuk mengizinkan host apa pun). Header Authorization hanya dilampirkan untuk host dalam `channels.msteams.mediaAuthAllowHosts` (default ke host Graph + Bot Framework). Jaga daftar ini tetap ketat (hindari sufiks multi-tenant).

## Mengirim file dalam obrolan grup

Bot dapat mengirim file dalam DM menggunakan alur FileConsentCard (bawaan). Namun, **mengirim file dalam obrolan grup/channel** memerlukan penyiapan tambahan:

Konteks | Cara file dikirim | Penyiapan yang diperlukan  
---|---|---  
**DM** | FileConsentCard → pengguna menerima → bot mengunggah | Berfungsi langsung tanpa konfigurasi tambahan  
**Obrolan grup/channel** | Unggah ke SharePoint → bagikan tautan | Memerlukan `sharePointSiteId` \+ izin Graph  
**Gambar (konteks apa pun)** | Inline berenkode Base64 | Berfungsi langsung tanpa konfigurasi tambahan  
  
### Mengapa obrolan grup memerlukan SharePoint

Bot tidak memiliki drive OneDrive pribadi (endpoint Graph API `/me/drive` tidak berfungsi untuk identitas aplikasi). Untuk mengirim file dalam obrolan grup/channel, bot mengunggah ke **situs SharePoint** dan membuat tautan berbagi.

### Penyiapan

  1. **Tambahkan izin Graph API** di Entra ID (Azure AD) → App Registration:

     * `Sites.ReadWrite.All` (Application) - mengunggah file ke SharePoint
     * `Chat.Read.All` (Application) - opsional, mengaktifkan tautan berbagi per pengguna
  2. **Berikan persetujuan admin** untuk tenant.

  3. **Dapatkan ID situs SharePoint Anda:**

bashCopy code
[code]# Via Graph Explorer or curl with a valid token:curl -H "Authorization: Bearer $TOKEN" \  "https://graph.microsoft.com/v1.0/sites/{hostname}:/{site-path}" # Example: for a site at "contoso.sharepoint.com/sites/BotFiles"curl -H "Authorization: Bearer $TOKEN" \  "https://graph.microsoft.com/v1.0/sites/contoso.sharepoint.com:/sites/BotFiles" # Response includes: "id": "contoso.sharepoint.com,guid1,guid2"
[/code]

  4. **Konfigurasikan OpenClaw:**

json5Copy code
[code]{  channels: {    msteams: {      // ... other config ...      sharePointSiteId: "contoso.sharepoint.com,guid1,guid2",    },  },}
[/code]


### Perilaku berbagi

Izin | Perilaku berbagi  
---|---  
`Sites.ReadWrite.All` saja | Tautan berbagi seluruh organisasi (siapa pun di org dapat mengakses)  
`Sites.ReadWrite.All` \+ `Chat.Read.All` | Tautan berbagi per pengguna (hanya anggota chat yang dapat mengakses)  
  
Berbagi per pengguna lebih aman karena hanya peserta chat yang dapat mengakses file. Jika izin `Chat.Read.All` tidak ada, bot kembali menggunakan berbagi seluruh organisasi.

### Perilaku fallback

Skenario | Hasil  
---|---  
Obrolan grup + file + `sharePointSiteId` dikonfigurasi | Unggah ke SharePoint, kirim tautan berbagi  
Obrolan grup + file + tanpa `sharePointSiteId` | Coba unggah OneDrive (mungkin gagal), kirim teks saja  
Chat pribadi + file | Alur FileConsentCard (berfungsi tanpa SharePoint)  
Konteks apa pun + gambar | Inline berenkode Base64 (berfungsi tanpa SharePoint)  
  
### Lokasi file tersimpan

File yang diunggah disimpan dalam folder `/OpenClawShared/` di pustaka dokumen default situs SharePoint yang dikonfigurasi.

## Jajak pendapat (Adaptive Cards)

OpenClaw mengirim jajak pendapat Teams sebagai Adaptive Cards (tidak ada API jajak pendapat Teams native).

  * CLI: `openclaw message poll --channel msteams --target conversation:<id> ...`
  * Suara dicatat oleh Gateway di `~/.openclaw/msteams-polls.json`.
  * Gateway harus tetap online untuk mencatat suara.
  * Polling belum memposting ringkasan hasil secara otomatis (periksa file store jika diperlukan).


## Kartu presentasi

Kirim payload presentasi semantik ke pengguna atau percakapan Teams menggunakan alat `message` atau CLI. OpenClaw merendernya sebagai Teams Adaptive Cards dari kontrak presentasi generik.

Parameter `presentation` menerima blok semantik. Ketika `presentation` disediakan, teks pesan bersifat opsional.

**Alat agen:**

json5Copy code
[code]
    {  action: "send",  channel: "msteams",  target: "user:<id>",  presentation: {    title: "Hello",    blocks: [{ type: "text", text: "Hello!" }],  },}
[/code]

**CLI:**

bashCopy code
[code]
    openclaw message send --channel msteams \  --target "conversation:19:abc...@thread.tacv2" \  --presentation '{"title":"Hello","blocks":[{"type":"text","text":"Hello!"}]}'
[/code]

Untuk detail format target, lihat Format target di bawah.

## Format target

Target MSTeams menggunakan prefiks untuk membedakan pengguna dan percakapan:

Jenis target | Format | Contoh  
---|---|---  
Pengguna (berdasarkan ID) | `user:<aad-object-id>` | `user:40a1a0ed-4ff2-4164-a219-55518990c197`  
Pengguna (berdasarkan nama) | `user:<display-name>` | `user:John Smith` (memerlukan Graph API)  
Grup/channel | `conversation:<conversation-id>` | `conversation:19:abc123...@thread.tacv2`  
Grup/channel (mentah) | `<conversation-id>` | `19:abc123...@thread.tacv2` (jika berisi `@thread`)  
  
**Contoh CLI:**

bashCopy code
[code]
    # Send to a user by IDopenclaw message send --channel msteams --target "user:40a1a0ed-..." --message "Hello" # Send to a user by display name (triggers Graph API lookup)openclaw message send --channel msteams --target "user:John Smith" --message "Hello" # Send to a group chat or channelopenclaw message send --channel msteams --target "conversation:19:abc...@thread.tacv2" --message "Hello" # Send a presentation card to a conversationopenclaw message send --channel msteams --target "conversation:19:abc...@thread.tacv2" \  --presentation '{"title":"Hello","blocks":[{"type":"text","text":"Hello"}]}'
[/code]

**Contoh alat agen:**

json5Copy code
[code]
    {  action: "send",  channel: "msteams",  target: "user:John Smith",  message: "Hello!",}
[/code]

json5Copy code
[code]
    {  action: "send",  channel: "msteams",  target: "conversation:19:abc...@thread.tacv2",  presentation: {    title: "Hello",    blocks: [{ type: "text", text: "Hello" }],  },}
[/code]

## Pesan proaktif

  * Pesan proaktif hanya mungkin **setelah** pengguna berinteraksi, karena kami menyimpan referensi percakapan pada titik tersebut.
  * Lihat `/gateway/configuration` untuk `dmPolicy` dan gating allowlist.


## ID Tim dan Channel (Jebakan Umum)

Parameter kueri `groupId` dalam URL Teams **BUKAN** ID tim yang digunakan untuk konfigurasi. Ekstrak ID dari path URL sebagai gantinya:

**URL Tim:**

CodeCopy code
[code]
    https://teams.microsoft.com/l/team/19%3ABk4j...%40thread.tacv2/conversations?groupId=...                                    └────────────────────────────┘                                    Team conversation ID (URL-decode this)
[/code]

**URL Channel:**

CodeCopy code
[code]
    https://teams.microsoft.com/l/channel/19%3A15bc...%40thread.tacv2/ChannelName?groupId=...                                      └─────────────────────────┘                                      Channel ID (URL-decode this)
[/code]

**Untuk konfigurasi:**

  * Kunci tim = segmen path setelah `/team/` (di-URL-decode, misalnya, `19:Bk4j...@thread.tacv2`; tenant lama mungkin menampilkan `@thread.skype`, yang juga valid)
  * Kunci channel = segmen path setelah `/channel/` (di-URL-decode)
  * **Abaikan** parameter kueri `groupId` untuk routing OpenClaw. Itu adalah ID grup Microsoft Entra, bukan ID percakapan Bot Framework yang digunakan dalam aktivitas Teams yang masuk.


## Channel privat

Bot memiliki dukungan terbatas di channel privat:

Fitur | Channel Standar | Channel Privat  
---|---|---  
Instalasi bot | Ya | Terbatas  
Pesan real-time (webhook) | Ya | Mungkin tidak berfungsi  
Izin RSC | Ya | Mungkin berperilaku berbeda  
@mention | Ya | Jika bot dapat diakses  
Riwayat Graph API | Ya | Ya (dengan izin)  
  
**Solusi sementara jika channel privat tidak berfungsi:**

  1. Gunakan channel standar untuk interaksi bot
  2. Gunakan DM - pengguna selalu dapat mengirim pesan langsung ke bot
  3. Gunakan Graph API untuk akses historis (memerlukan `ChannelMessage.Read.All`)


## Pemecahan masalah

### Masalah umum

  * **Gambar tidak muncul di channel:** Izin Graph atau persetujuan admin hilang. Instal ulang aplikasi Teams dan tutup sepenuhnya/buka kembali Teams.
  * **Tidak ada respons di channel:** mention diperlukan secara default; atur `channels.msteams.requireMention=false` atau konfigurasikan per tim/channel.
  * **Ketidakcocokan versi (Teams masih menampilkan manifes lama):** hapus + tambahkan ulang aplikasi dan tutup Teams sepenuhnya untuk menyegarkan.
  * **401 Unauthorized dari webhook:** Diharapkan saat menguji secara manual tanpa Azure JWT - berarti endpoint dapat dijangkau tetapi autentikasi gagal. Gunakan Azure Web Chat untuk menguji dengan benar.


### Kesalahan unggah manifes

  * **"Icon file cannot be empty":** Manifes merujuk file ikon yang berukuran 0 byte. Buat ikon PNG yang valid (32x32 untuk `outline.png`, 192x192 untuk `color.png`).
  * **"[webApplicationInfo.Id](<http://webApplicationInfo.Id>) already in use":** Aplikasi masih terpasang di tim/chat lain. Temukan dan copot pemasangannya terlebih dahulu, atau tunggu 5-10 menit untuk propagasi.
  * **"Something went wrong" saat mengunggah:** Unggah melalui <https://admin.teams.microsoft.com> sebagai gantinya, buka DevTools browser (F12) → tab Network, dan periksa body respons untuk kesalahan sebenarnya.
  * **Sideload gagal:** Coba "Upload an app to your org's app catalog" alih-alih "Upload a custom app" - ini sering melewati pembatasan sideload.


### Izin RSC tidak berfungsi

  1. Verifikasi `webApplicationInfo.id` sama persis dengan App ID bot Anda
  2. Unggah ulang aplikasi dan instal ulang di tim/chat
  3. Periksa apakah admin organisasi Anda telah memblokir izin RSC
  4. Konfirmasi Anda menggunakan scope yang tepat: `ChannelMessage.Read.Group` untuk tim, `ChatMessage.Read.Chat` untuk chat grup


## Referensi

  * [Buat Azure Bot](<https://learn.microsoft.com/en-us/azure/bot-service/bot-service-quickstart-registration>) \- panduan penyiapan Azure Bot
  * [Teams Developer Portal](<https://dev.teams.microsoft.com/apps>) \- buat/kelola aplikasi Teams
  * [Skema manifes aplikasi Teams](<https://learn.microsoft.com/en-us/microsoftteams/platform/resources/schema/manifest-schema>)
  * [Terima pesan channel dengan RSC](<https://learn.microsoft.com/en-us/microsoftteams/platform/bots/how-to/conversations/channel-messages-with-rsc>)
  * [Referensi izin RSC](<https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/rsc/resource-specific-consent>)
  * [Penanganan file bot Teams](<https://learn.microsoft.com/en-us/microsoftteams/platform/bots/how-to/bots-filesv4>) (channel/grup memerlukan Graph)
  * [Pesan proaktif](<https://learn.microsoft.com/en-us/microsoftteams/platform/bots/how-to/conversations/send-proactive-messages>)
  * [@microsoft/teams.cli](<https://www.npmjs.com/package/@microsoft/teams.cli>) \- Teams CLI untuk manajemen bot


## Terkait

  * [Ikhtisar Channel](</id/channels>) \- semua channel yang didukung
  * [Pairing](</id/channels/pairing>) \- autentikasi DM dan alur pairing
  * [Grup](</id/channels/groups>) \- perilaku chat grup dan gating mention
  * [Routing Channel](</id/channels/channel-routing>) \- routing sesi untuk pesan
  * [Keamanan](</id/gateway/security>) \- model akses dan hardening


Was this useful?YesNo