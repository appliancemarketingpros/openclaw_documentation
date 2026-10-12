---
title: Ringkasan HealthKit
source_url: https://docs.openclaw.ai/id/platforms/ios-healthkit
scraped_at: 2026-10-12
---

PlatformsPlatforms overview

# Ringkasan HealthKit

OpenClaw dapat meminta ringkasan hanya-baca untuk hari kalender saat ini dari node iPhone atau iPad yang terhubung. Perangkat menghitung agregat di perangkat dan hanya mengembalikan jumlah langkah, durasi tidur, rata-rata detak jantung saat istirahat, serta jumlah/durasi latihan. Sampel, sumber, metadata, catatan klinis HealthKit individual, penyerapan latar belakang, dan penulisan tidak didukung.

Fitur ini dinonaktifkan secara default. Fitur ini memerlukan persetujuan terpisah pada perangkat iOS dan otorisasi pada Gateway.

## Persyaratan

  * iPhone atau iPad yang menjalankan aplikasi iOS OpenClaw tempat HealthKit melaporkan data kesehatan sebagai tersedia.
  * Node iOS yang terhubung dan disetujui. Lihat [penyiapan aplikasi iOS](</id/platforms/ios>).
  * Gateway terkini yang dapat menjangkau node iOS.
  * Data Health yang dapat dibaca untuk setiap metrik yang ingin Anda lihat. Apple Watch dapat menyumbangkan data ke penyimpanan Apple Health, tetapi aplikasi watchOS OpenClaw tidak diperlukan untuk ringkasan HealthKit.


## Aktifkan akses

### 1\. Otorisasi perintah Gateway

Tambahkan `health.summary` ke array `gateway.nodes.allowCommands` yang sudah ada di `openclaw.json`. Pertahankan semua perintah yang sudah ada:

json5Copy code
[code]
    {  gateway: {    nodes: {      allowCommands: ["health.summary"],    },  },}
[/code]

`health.summary` diklasifikasikan sebagai sangat sensitif terhadap privasi dan tidak pernah diizinkan oleh default platform iOS. Entri dalam `gateway.nodes.denyCommands` mengesampingkan entri izin. Lihat [Kebijakan perintah Node](</id/nodes#command-policy>).

### 2\. Aktifkan berbagi pada perangkat iOS

Di aplikasi iOS:

  1. Buka **Settings - > Permissions** dan temukan **Apple Health Summaries** di bagian **Apple Health** yang selalu terlihat.
  2. Ketuk **Enable Apple Health Summaries**.
  3. Baca pengungkapan, lalu pilih kategori Health yang boleh dibaca OpenClaw pada lembar izin Apple.


Sakelar tersebut mencatat pilihan eksplisit Anda untuk berbagi dengan OpenClaw. Sakelar tersebut tidak menyatakan bahwa Apple memberikan izin untuk setiap kategori yang diminta.

Mengaktifkan ringkasan Health menambahkan `health.summary` ke permukaan perintah yang dideklarasikan node. Setujui pembaruan pemasangan node yang dihasilkan:

bashCopy code
[code]
    openclaw nodes pendingopenclaw nodes approve <requestId>
[/code]

Kemudian verifikasi bahwa perangkat iOS yang terhubung mengekspos perintah `health.summary` yang efektif:

bashCopy code
[code]
    openclaw nodes describe --node "<iOS device name>"
[/code]

## Minta ringkasan hari ini

Hanya `today` yang didukung. Ringkasan ini mencakup waktu dari tengah malam setempat hingga waktu permintaan, menggunakan kalender dan zona waktu perangkat iOS saat ini.

bashCopy code
[code]
    openclaw nodes invoke \  --node "<iOS device name>" \  --command health.summary \  --params '{"period":"today"}' \  --json
[/code]

Agen dapat memanggil perintah yang sama dengan alat `nodes`:

jsonCopy code
[code]
    {  "action": "invoke",  "node": "<iOS device name>",  "invokeCommand": "health.summary",  "invokeParamsJson": "{\"period\":\"today\"}"}
[/code]

Payload ringkasan berisi:

Bidang | Arti  
---|---  
`period` | Selalu `today`  
`startISO` | Awal hari setempat, dikodekan sebagai instan ISO  
`endISO` | Waktu permintaan, dikodekan sebagai instan ISO  
`timeZoneIdentifier` | Pengidentifikasi zona waktu perangkat iOS  
`stepCount` | Jumlah langkah kumulatif yang dibulatkan  
`sleepDurationMinutes` | Waktu tidur yang dideduplikasi, dibatasi untuk hari ini  
`restingHeartRateBpm` | Rata-rata detak jantung saat istirahat  
`workoutCount` | Latihan yang dimulai hari ini  
`workoutDurationMinutes` | Durasi total latihan tersebut  
  
Bidang metrik bersifat opsional dan dihilangkan ketika HealthKit tidak mengembalikan nilai yang dapat dibaca. Tahap tidur dan sumber yang tumpang tindih digabungkan sebelum durasi dihitung, sehingga menit yang sama tidak dihitung dua kali.

## Perilaku privasi

  * Agregasi berlangsung pada perangkat iOS. Sampel mentah tidak meninggalkan perangkat.
  * Agregat yang diminta meninggalkan perangkat melalui Gateway Anda. Saat agen memintanya, agregat tersebut mencapai penyedia AI yang dikonfigurasi dan mungkin tetap berada dalam riwayat obrolan. Pemanggilan CLI langsung mengembalikannya kepada operator CLI.
  * OpenClaw hanya meminta akses baca. OpenClaw tidak dapat menambahkan atau mengubah data Health.
  * OpenClaw hanya membaca HealthKit saat `health.summary` dipanggil. Tidak ada penyerapan data kesehatan di latar belakang.
  * HealthKit sengaja tidak mengungkapkan apakah akses baca ditolak. Metrik yang tidak tersedia dapat berarti akses ditolak, tidak ada sampel yang cocok, atau jenis data tidak tersedia. OpenClaw tidak dapat membedakan kasus-kasus tersebut.
  * Ringkasan ini ditujukan untuk konteks kesehatan dan kebugaran pribadi, bukan diagnosis atau nasihat medis.


Untuk berhenti berbagi, kembali ke **Apple Health Summaries** dan ketuk **Turn Off Summaries**. Perangkat iOS kemudian menghapus kemampuan Health dan perintah `health.summary` dari permukaan nodenya. Anda juga dapat menghapus `health.summary` dari `gateway.nodes.allowCommands` untuk menutup gerbang di sisi Gateway.

## Pemecahan masalah

### Perintah tidak dideklarasikan oleh node

Pastikan ringkasan Apple Health diaktifkan di aplikasi iOS dan perangkat terhubung. Jalankan `openclaw nodes pending` dan setujui setiap pembaruan kemampuan, lalu periksa kembali `openclaw nodes describe --node "<iOS device name>"`.

### Perintah memerlukan persetujuan eksplisit

Tambahkan `health.summary` ke `gateway.nodes.allowCommands`. Periksa juga bahwa `gateway.nodes.denyCommands` tidak memuatnya; daftar penolakan diprioritaskan.

### `HEALTH_ACCESS_DISABLED`

Sakelar berbagi di sisi aplikasi dinonaktifkan. Aktifkan **Apple Health Summaries** di bawah **Settings - > Permissions -> Apple Health** pada perangkat iOS.

### Ringkasan berhasil tetapi metrik tidak tersedia

Buka aplikasi Health Apple dan pastikan data untuk hari ini tersedia. Tinjau akses OpenClaw di pengaturan Health Apple, tetapi jangan menganggap hasil kosong sebagai bukti bahwa akses ditolak: HealthKit sengaja menyembunyikan perbedaan tersebut.

### Rentang waktu lama gagal

Perintah hanya menerima `{"period":"today"}`. Ringkasan beberapa hari dan historis tidak didukung.

## Terkait

  * [Aplikasi iOS](</id/platforms/ios>)
  * [Node](</id/nodes>)
  * [Referensi konfigurasi Gateway](</id/gateway/configuration-reference#gateway>)
  * [Audit keamanan](</id/gateway/security>)


Was this useful?YesNo

Open issue