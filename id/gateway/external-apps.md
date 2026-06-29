---
title: Integrasi Gateway untuk aplikasi eksternal
source_url: https://docs.openclaw.ai/id/gateway/external-apps
scraped_at: 2026-06-29
---

ReferenceRPC and API

Aplikasi eksternal sebaiknya berkomunikasi dengan OpenClaw melalui protokol Gateway saat ini. Gunakan WebSocket Gateway dan metode RPC saat skrip, dasbor, pekerjaan CI, ekstensi IDE, atau proses lain ingin memulai eksekusi agen, mengalirkan peristiwa, menunggu hasil, membatalkan pekerjaan, atau memeriksa sumber daya Gateway.

## Yang tersedia saat ini

Permukaan | Status | Gunakan untuk  
---|---|---  
[Protokol Gateway](</id/gateway/protocol>) | Siap | Transport WebSocket, handshake koneksi, cakupan auth, versioning protokol, dan peristiwa.  
[Referensi RPC Gateway](</id/reference/rpc>) | Siap | Metode Gateway saat ini untuk agen, sesi, tugas, model, alat, artefak, dan persetujuan.  
[`openclaw agent`](</id/cli/agent>) | Siap | Integrasi skrip sekali jalan saat menjalankan CLI dari shell sudah cukup.  
[`openclaw message`](</id/cli/message>) | Siap | Mengirim pesan atau tindakan kanal dari skrip.  
  
Pohon sumber berisi pekerjaan paket internal untuk pustaka klien mendatang, tetapi itu bukan permukaan instalasi publik. Perlakukan sebagai detail implementasi pratinjau sampai paket tersebut dipublikasikan dan diberi versi.

## Jalur yang direkomendasikan

  1. Jalankan atau temukan Gateway.
  2. Hubungkan melalui [protokol Gateway](</id/gateway/protocol>).
  3. Panggil metode RPC terdokumentasi dari [referensi RPC Gateway](</id/reference/rpc>).
  4. Sematkan versi OpenClaw yang Anda uji.
  5. Periksa ulang referensi RPC saat memutakhirkan OpenClaw.


Untuk eksekusi agen, mulai dengan RPC `agent` dan pasangkan dengan `agent.wait` saat Anda memerlukan hasil terminal. Untuk status percakapan yang tahan lama, gunakan metode `sessions.*`. Untuk integrasi UI, berlangganan peristiwa Gateway dan render hanya keluarga peristiwa yang dipahami aplikasi Anda.

## Kode aplikasi vs kode Plugin

Gunakan RPC Gateway saat kode berada di luar OpenClaw:

  * skrip Node yang memulai atau mengamati eksekusi agen
  * pekerjaan CI yang memanggil Gateway
  * dasbor dan panel admin
  * ekstensi IDE
  * bridge eksternal yang tidak perlu menjadi Plugin kanal
  * pengujian integrasi dengan transport Gateway palsu atau nyata


Gunakan SDK Plugin saat kode berjalan di dalam OpenClaw:

  * Plugin penyedia
  * Plugin kanal
  * hook alat atau siklus hidup
  * Plugin harness agen
  * helper runtime tepercaya


Aplikasi eksternal sebaiknya tidak mengimpor `openclaw/plugin-sdk/*`; subpath tersebut ditujukan untuk Plugin yang dimuat oleh OpenClaw.

## Terkait

  * [Protokol Gateway](</id/gateway/protocol>)
  * [Referensi RPC Gateway](</id/reference/rpc>)
  * [Perintah CLI agent](</id/cli/agent>)
  * [Perintah CLI message](</id/cli/message>)
  * [Loop agen](</id/concepts/agent-loop>)
  * [Runtime agen](</id/concepts/agent-runtimes>)
  * [Sesi](</id/concepts/session>)
  * [Tugas latar belakang](</id/automation/tasks>)
  * [Agen ACP](</id/tools/acp-agents>)
  * [Ikhtisar SDK Plugin](</id/plugins/sdk-overview>)


Was this useful?YesNo

Open issue