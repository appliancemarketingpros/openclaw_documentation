---
title: Membangun klien Gateway
source_url: https://docs.openclaw.ai/id/gateway/clients
scraped_at: 2026-07-27
---

Gateway & OpsGateway

Gunakan paket Gateway yang dipublikasikan untuk membangun dasbor operator, klien WebChat, dan aplikasi pihak ketiga lainnya. Panduan ini membahas siklus hidup klien seputar kontrak wire: autentikasi, kapabilitas, pemulihan koneksi ulang, riwayat, langganan, dan peningkatan versi.

Untuk bentuk frame, handshake, kesalahan, dan seluruh permukaan metode, baca [spesifikasi protokol Gateway](<https://docs.openclaw.ai/gateway/protocol>).

## Instal paket

bashCopy code
[code]
    npm install @openclaw/gateway-client @openclaw/gateway-protocol
[/code]

  * [`@openclaw/gateway-protocol`](<https://www.npmjs.com/package/@openclaw/gateway-protocol>) menyediakan skema, validator runtime, tipe TypeScript, registri identitas dan kapabilitas klien, pembaca kesalahan terstruktur, serta konstanta versi protokol. Tarball npm-nya juga menyertakan kontrak yang dapat dibaca mesin [`protocol.schema.json`](<https://unpkg.com/@openclaw/gateway-protocol/protocol.schema.json>) yang dihasilkan.
  * [`@openclaw/gateway-client`](<https://www.npmjs.com/package/@openclaw/gateway-client>) adalah implementasi koneksi referensi. Impor akar paket untuk klien Node dan `@openclaw/gateway-client/browser` untuk protokol yang aman bagi peramban, autentikasi perangkat, serta pembantu koneksi ulang.


Entri Node mengelola transport WebSocket-nya sendiri. Host peramban menyediakan adaptor WebSocket beserta penyimpanan persisten dan callback penandatanganan untuk identitas perangkat dan token perangkat.

## Pilih cakupan dan pasangkan perangkat

Klien obrolan interaktif penuh yang juga merender permintaan persetujuan harus meminta `role: "operator"` dengan cakupan berikut:

Cakupan | Kegunaan  
---|---  
`operator.read` | `chat.history`, `sessions.list`, `sessions.subscribe`, status model, dan peristiwa hanya-baca  
`operator.write` | `chat.send` dan mutasi sesi biasa  
`operator.approvals` | Mencantumkan, menampilkan, dan menyelesaikan persetujuan exec atau plugin  
  
Tambahkan `operator.questions` hanya jika klien menangani pertanyaan interaktif, `operator.pairing` hanya jika klien mengelola perangkat atau node yang dipasangkan, dan `operator.admin` hanya untuk operasi administratif seperti `config.patch`. [Referensi cakupan operator](<https://docs.openclaw.ai/gateway/operator-scopes>) mendefinisikan seluruh aturan metode dan waktu persetujuan.

Jangan membuat token bearer per klien dengan mengedit `openclaw.json` secara manual. Konfigurasikan autentikasi bootstrap bersama milik Gateway dengan `openclaw configure --section gateway` atau opsi `openclaw onboard --gateway-auth ...`, lalu biarkan pemasangan perangkat membuat token klien:

  1. Persistensikan identitas perangkat Ed25519 di klien.
  2. Tunggu `connect.challenge`, tandatangani payload perangkat yang terikat dengan tantangan, lalu kirim `connect` dengan peran operator dan cakupan yang diminta, serta token Gateway bersama atau kata sandi untuk autentikasi bootstrap.
  3. Jika Gateway mengembalikan detail `PAIRING_REQUIRED` terstruktur, tampilkan ID permintaan dan jeda atau coba lagi sesuai `error.details.recommendedNextStep`.
  4. Di host Gateway, tinjau permintaan dengan `openclaw devices list`, lalu setujui permintaan terkini yang tepat tersebut dengan `openclaw devices approve <requestId>`.
  5. Hubungkan kembali dan persistensikan `hello-ok.auth.deviceToken` dengan peran serta cakupan yang dinegosiasikan. Gunakan token perangkat tersebut untuk koneksi berikutnya.


Peningkatan cakupan atau peran membuat permintaan pemasangan baru yang tertunda. Rotasi token tidak dapat memperluas kontrak pemasangan yang disetujui. Lihat [CLI Perangkat](<https://docs.openclaw.ai/cli/devices>) untuk perintah persetujuan, rotasi, dan pencabutan.

## Umumkan kapabilitas klien

`connect.params.caps` menjelaskan perilaku opsional yang dapat digunakan klien. Deklarasi ini tidak memberikan otorisasi. Impor nama dari `GATEWAY_CLIENT_CAPS` alih-alih menduplikasi literal string:

tsCopy code
[code]
     const caps = [GATEWAY_CLIENT_CAPS.TOOL_EVENTS];
[/code]

Registri saat ini berisi `approvals`, `exec-approvals`, `inline-widgets`, `run-tool-bindings`, `session-scoped-events`, `plugin-approvals`, `task-suggestions`, `terminal-offset-seq`, `tool-events`, dan `ui-commands`. Umumkan hanya kapabilitas yang benar-benar diimplementasikan klien.

Alat agen yang dikendalikan kapabilitas merupakan penggunaan terpisah dari deklarasi yang sama. Jika suatu alat agen memerlukan kapabilitas klien, Gateway menghilangkan alat tersebut kecuali klien asal telah mengumumkan setiap kapabilitas yang diperlukan.

## Pulihkan status setelah koneksi ulang

Perlakukan setiap koneksi ulang yang berhasil sebagai proyeksi baru atas riwayat persisten dan status proses dalam memori saat ini:

  1. Bangun kembali `sessions.subscribe` dan langganan `sessions.messages.subscribe` milik sesi yang dipilih.
  2. Panggil `chat.history` untuk `sessionKey` yang dipilih dan ganti baris persisten lokal dengan proyeksi `messages` yang dikembalikan.
  3. Jika `inFlightRun` tersedia, adopsi `runId`, `text` yang di-buffer, dan `plan` opsional miliknya. Adopsi proses bahkan ketika `text` kosong.
  4. Baca `sessionInfo.hasActiveRun` dan `sessionInfo.activeRunIds`. Utamakan keanggotaan tepat dalam `activeRunIds` saat menentukan apakah proses yang dipertahankan masih memiliki UI streaming. Nilai `hasActiveRun` yang benar tanpa ID yang tercantum dapat merepresentasikan proyeksi runtime aktif lainnya.
  5. Rekonsiliasikan peristiwa `agent` berikutnya berdasarkan `payload.runId` dan `payload.seq`. Pertahankan urutan tertinggi yang diterima secara independen untuk setiap proses, abaikan urutan yang sudah terlihat atau lebih rendah, dan perlakukan celah maju sebagai alasan untuk memuat ulang riwayat otoritatif.


Frame peristiwa luar juga memiliki `seq` opsional, yang mengurutkan peristiwa pada koneksi WebSocket saat ini. Nilai ini diatur ulang pada koneksi baru. `seq` di dalam payload peristiwa `agent` ditetapkan per proses dan mengurutkan siklus hidup, asisten, rencana, alat, serta peristiwa stream lainnya milik proses tersebut.

## Gunakan metadata riwayat dan anchor stabil

Baris yang dikembalikan oleh `chat.history` dapat membawa envelope metadata `__openclaw`:

  * `id` adalah identitas entri transkrip. Gunakan untuk permintaan riwayat ber-anchor, tetapi bukan sebagai kunci baris tampilan unik.
  * `seq` adalah urutan rekaman transkrip positif. Satu rekaman tersimpan dapat diproyeksikan menjadi lebih dari satu baris tampilan, jadi pertahankan baris-baris saudara dengan `id` dan urutan yang sama secara berkelompok.
  * `kind` mengidentifikasi baris sintetis. Batas Compaction menggunakan `kind: "compaction"` dan dapat menyertakan `tokensBefore` serta `tokensAfter` ketika checkpoint yang cocok mencatat metrik tersebut.


Lakukan penelusuran halaman mundur dengan nilai `hasMore` dan `nextOffset` dari respons. Offset numerik menjelaskan proyeksi transkrip saat ini, jadi jangan persistensikan sebagai bookmark jangka panjang lintas reset atau Compaction. Persistensikan `__openclaw.id` sebagai gantinya. Untuk memulihkan di sekitar baris yang diketahui, panggil `chat.history` dengan `messageId` dan `sessionId` yang mengembalikannya. Gateway dapat menyelesaikan anchor tersebut dari riwayat arsip reset; respons ber-anchor sengaja menghilangkan metadata penelusuran halaman numerik.

## Berlangganan alih-alih melakukan polling penggunaan

Muat katalog awal dengan `sessions.list`, lalu panggil `sessions.subscribe` sekali per koneksi. Gabungkan peristiwa `sessions.changed` berdasarkan `sessionKey`. Payload perubahan sesi dapat membawa `inputTokens`, `outputTokens`, `totalTokens`, `totalTokensFresh`, `contextTokens`, `estimatedCostUsd`, pengaturan penggunaan respons, dan status proses aktif secara langsung.

Beberapa notifikasi perubahan hanya berupa sinyal invalidasi. Jika suatu peristiwa tidak menyertakan bidang baris yang diperlukan tampilan, segarkan `sessions.list`. Jangan melakukan polling `usage.cost` atau `sessions.usage` untuk menjaga daftar sesi langsung tetap mutakhir; cadangkan metode tersebut untuk laporan agregat atau terperinci sesuai permintaan.

## Isi ulang persetujuan exec

Klien dengan `operator.approvals` harus memasang listener peristiwanya segera setelah `hello-ok` selesai, lalu memanggil `exec.approval.list` untuk mengisi ulang permintaan yang mendahului koneksi. Rekonsiliasikan daftar dan peristiwa langsung `exec.approval.requested` / `exec.approval.resolved` berdasarkan ID persetujuan agar transisi yang berpacu dengan permintaan daftar tidak hilang maupun muncul kembali.

## Lacak versi protokol

Versi wire saat ini adalah `4`. Klien operator umum dan WebChat harus menegosiasikan versi terkini yang tepat dengan `minProtocol: 4` dan `maxProtocol: 4`. Hanya klien node terautentikasi dan probe ringan yang memiliki jendela penerimaan N-1, saat ini protokol `3` hingga `4`.

Perubahan protokol bersifat aditif terlebih dahulu. `protocol.schema.json` menyertakan metadata era rilis `since` dan metadata cakupan yang diperlukan untuk metode inti, tetapi peningkatan versi wire tetap merupakan peristiwa perubahan yang merusak bagi klien pihak ketiga. Sematkan versi paket yang Anda uji, tingkatkan klien dan Gateway secara bersamaan ketika versi wire berubah, dan tinjau [changelog OpenClaw](<https://github.com/openclaw/openclaw/blob/main/CHANGELOG.md>) sebelum setiap peningkatan.

## Terkait

  * [Protokol Gateway](<https://docs.openclaw.ai/gateway/protocol>)
  * [Menyematkan OpenClaw](<https://docs.openclaw.ai/gateway/embedding>)
  * [Referensi RPC Gateway](<https://docs.openclaw.ai/reference/rpc>)
  * [Integrasi Gateway untuk aplikasi eksternal](<https://docs.openclaw.ai/gateway/external-apps>)


Was this useful?YesNo

Open issue