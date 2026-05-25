---
title: Kehadiran
source_url: https://docs.openclaw.ai/id/concepts/presence
scraped_at: 2026-05-25
---

OpenClaw "kehadiran" adalah tampilan ringan dengan upaya terbaik untuk:

  * **Gateway** itu sendiri, dan
  * **klien yang terhubung ke Gateway** (aplikasi mac, WebChat, CLI, dll.)


Kehadiran digunakan terutama untuk merender tab **Instans** aplikasi macOS dan untuk memberikan visibilitas operator secara cepat.

## Bidang kehadiran (yang ditampilkan)

Entri kehadiran adalah objek terstruktur dengan bidang seperti:

  * `instanceId` (opsional tetapi sangat disarankan): identitas klien yang stabil (biasanya `connect.client.instanceId`)
  * `host`: nama host yang mudah dipahami manusia
  * `ip`: alamat IP dengan upaya terbaik
  * `version`: string versi klien
  * `deviceFamily` / `modelIdentifier`: petunjuk perangkat keras
  * `mode`: `ui`, `webchat`, `cli`, `backend`, `probe`, `test`, `node`, ...
  * `lastInputSeconds`: "detik sejak input pengguna terakhir" (jika diketahui)
  * `reason`: `self`, `connect`, `node-connected`, `periodic`, ...
  * `ts`: stempel waktu pembaruan terakhir (md sejak epoch)


## Produsen (asal kehadiran)

Entri kehadiran dihasilkan oleh beberapa sumber dan **digabungkan**.

### 1) Entri mandiri Gateway

Gateway selalu menyiapkan entri "mandiri" saat startup agar UI menampilkan host gateway bahkan sebelum ada klien yang terhubung.

### 2) Koneksi WebSocket

Setiap klien WS dimulai dengan permintaan `connect`. Setelah handshake berhasil, Gateway melakukan upsert entri kehadiran untuk koneksi tersebut.

#### Mengapa perintah CLI sekali jalan tidak muncul

CLI sering terhubung untuk perintah singkat sekali jalan. Untuk menghindari spam pada daftar Instans, `client.mode === "cli"` **tidak** diubah menjadi entri kehadiran.

### 3) Beacon `system-event`

Klien dapat mengirim beacon berkala yang lebih kaya melalui metode `system-event`. Aplikasi mac menggunakan ini untuk melaporkan nama host, IP, dan `lastInputSeconds`.

### 4) Koneksi Node (role: node)

Ketika sebuah node terhubung melalui WebSocket Gateway dengan `role: node`, Gateway melakukan upsert entri kehadiran untuk node tersebut (alur yang sama seperti klien WS lainnya).

## Aturan penggabungan + deduplikasi (mengapa `instanceId` penting)

Entri kehadiran disimpan dalam satu map dalam memori:

  * Entri diberi kunci berdasarkan **kunci kehadiran**.
  * Kunci terbaik adalah `instanceId` yang stabil (dari `connect.client.instanceId`) yang bertahan setelah restart.
  * Kunci tidak peka huruf besar/kecil.


Jika klien terhubung ulang tanpa `instanceId` yang stabil, klien tersebut dapat muncul sebagai baris **duplikat**.

## TTL dan ukuran terbatas

Kehadiran sengaja dibuat sementara:

  * **TTL:** entri yang lebih lama dari 5 menit dipangkas
  * **Entri maksimum:** 200 (yang paling lama dihapus terlebih dahulu)


Ini menjaga daftar tetap segar dan menghindari pertumbuhan memori tanpa batas.

## Catatan remote/tunnel (IP loopback)

Ketika klien terhubung melalui tunnel SSH / penerusan port lokal, Gateway dapat melihat alamat remote sebagai `127.0.0.1`. Untuk menghindari penimpaan IP baik yang dilaporkan klien, alamat remote loopback diabaikan.

## Konsumen

### Tab Instans macOS

Aplikasi macOS merender keluaran `system-presence` dan menerapkan indikator status kecil (Aktif/Menganggur/Kedaluwarsa) berdasarkan usia pembaruan terakhir.

## Tips debugging

  * Untuk melihat daftar mentah, panggil `system-presence` terhadap Gateway.
  * Jika Anda melihat duplikat: 
    * pastikan klien mengirim `client.instanceId` yang stabil dalam handshake
    * pastikan beacon berkala menggunakan `instanceId` yang sama
    * periksa apakah entri yang diturunkan dari koneksi tidak memiliki `instanceId` (duplikat memang diharapkan)


## Terkait

[**Indikator mengetik** Kapan indikator mengetik dikirim dan cara menyesuaikannya. ](</id/concepts/typing-indicators>) [**Streaming dan chunking** Streaming keluar, chunking, dan pemformatan per saluran. ](</id/concepts/streaming>) [**Arsitektur Gateway** Komponen Gateway dan protokol WebSocket yang mendorong pembaruan kehadiran. ](</id/concepts/architecture>) [**Protokol Gateway** Protokol wire untuk `connect`, `system-event`, dan `system-presence`. ](</id/gateway/protocol>)

Was this useful?YesNo