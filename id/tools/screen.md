---
title: Layar
source_url: https://docs.openclaw.ai/id/tools/screen
scraped_at: 2026-07-20
---

CapabilitiesTools

Alat `screen` memungkinkan agen mengatur Control UI berbasis peramban. Alat ini merupakan permukaan tata letak dan navigasi bertipe, bukan alat pengambilan tangkapan layar atau otomatisasi peramban.

Alat ini hanya tersedia ketika klien asal mengiklankan kapabilitas `ui-commands`. Setidaknya satu Control UI yang mendukung harus tetap terhubung saat alat dijalankan; jika tidak, Gateway akan mengembalikan `UNAVAILABLE`.

## Tindakan

Tindakan | Efek | Masukan opsional  
---|---|---  
`split_right` | Membagi panel sesi target ke kanan | `sessionKey` (secara default menggunakan sesi saat ini)  
`split_down` | Membagi panel sesi target ke bawah | `sessionKey` (secara default menggunakan sesi saat ini)  
`close_pane` | Menutup panel sesi target | `sessionKey` (secara default menggunakan sesi saat ini)  
`focus` | Memfokuskan panel sesi target | `sessionKey` (secara default menggunakan sesi saat ini)  
`navigate` | Membuka sesi target | `sessionKey` (secara default menggunakan sesi saat ini)  
`sidebar_show` / `sidebar_hide` | Menampilkan atau menyembunyikan bilah sisi utama | -  
`terminal_show` / `terminal_hide` | Menampilkan atau menyembunyikan panel terminal operator | `dock` (`bottom` atau `right`) saat ditampilkan  
`browser_show` / `browser_hide` | Menampilkan atau menyembunyikan panel peramban | `dock` (`bottom` atau `right`) saat ditampilkan  
  
Perintah yang berhasil akan mengembalikan `{ "ok": true }` setelah Gateway menyiarkan peristiwa bertipe `ui.command`.

## Perutean dan keamanan

Protokol v1 secara sengaja mengirimkan perintah ke setiap Control UI terhubung yang mengiklankan `ui-commands`; perintah tersebut tidak menargetkan satu tab peramban. Hal ini penting ketika operator yang sama membuka beberapa dasbor.

RPC Gateway memerlukan `operator.write`. Alat ini hanya dapat mengubah status tampilan: alat ini tidak dapat membaca piksel, mengambil tangkapan layar, mengeklik konten halaman secara arbitrer, atau melewati izin panel sesi dan operator yang dipilih.

## Terkait

  * [Control UI](</id/web/control-ui>)
  * [Protokol Gateway](</id/gateway/protocol#method-families>)
  * [Alat peramban](</id/tools/browser>)


Was this useful?YesNo

Open issue