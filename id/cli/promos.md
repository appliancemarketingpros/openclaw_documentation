---
title: Promosi
source_url: https://docs.openclaw.ai/id/cli/promos
scraped_at: 2026-07-13
---

ReferenceCLI commands

# `openclaw promos`

Temukan dan klaim penawaran model promosi yang dipublikasikan di ClawHub. Mengklaim promosi akan mengonfigurasi penyedia (autentikasi dan plugin, bila diperlukan) serta mendaftarkan model promosi tersebut — tanpa menjalankan ulang orientasi awal dan tanpa mengubah model default Anda kecuali Anda memintanya.

Terkait:

  * Model default dan fallback: [Model](</id/cli/models>)
  * Penyiapan autentikasi penyedia: [Memulai](</id/start/getting-started>)


## Perintah

bashCopy code
[code]
    openclaw promos listopenclaw promos claim <slug>openclaw promos claim <slug> --api-key <key> --set-default
[/code]

## `openclaw promos list`

Mencantumkan promosi yang sedang aktif, beserta modelnya, default yang disarankan, sisa waktu, dan perintah klaim yang tepat. `--json` mencetak payload mentah.

## `openclaw promos claim <slug>`

Mengklaim promosi yang sedang aktif:

  1. Mengambil promosi dari ClawHub dan memverifikasi bahwa promosi tersebut masih dalam periode berlakunya.
  2. Memvalidasi penyedia promosi, pilihan autentikasi, dan paket plugin yang dideklarasikan terhadap versi OpenClaw yang terinstal. ID yang tidak dikenal atau ketidakcocokan paket akan ditolak — promosi tidak akan pernah membuat CLI menjalankan sesuatu yang belum diketahui cara menjalankannya.
  3. Menggunakan kembali kredensial penyedia yang sudah ada jika tersedia. Jika tidak, proses akan memandu Anda melalui alur autentikasi normal penyedia (dengan terlebih dahulu mencetak URL pendaftaran promosi untuk mendapatkan kunci gratis). `--api-key <key>` menyelesaikan autentikasi kunci API tanpa prompt, sesuai dengan flag noninteraktif `openclaw onboard`; agar kunci tidak tercantum pada baris perintah, ekspor variabel lingkungan penyedia sebagai gantinya (misalnya `OPENROUTER_API_KEY`) — kredensial lingkungan yang sudah ada akan terdeteksi secara otomatis dan tidak memerlukan flag.
  4. Mendaftarkan model promosi beserta aliasnya. Alias yang sudah ada tidak pernah ditimpa.
  5. Menawarkan untuk menetapkan model yang disarankan oleh promosi sebagai default Anda — `--set-default` melewati pertanyaan tersebut; jika tidak, tidak ada yang berubah pada pengaturan default Anda.


Saat periode promosi berakhir, penyedia berhenti menyediakan model gratis; konfigurasi dan kredensial Anda tidak berubah. Beralih kembali kapan saja dengan `openclaw models set <model>`.

## Penemuan pasif di `models list`

`openclaw models list` juga menampilkan promosi tanpa mengharuskan Anda meminta langsung ke ClawHub:

  * Penawaran aktif dengan model yang belum Anda konfigurasi muncul dalam grup "Tersedia melalui promosi" di bawah tabel, masing-masing disertai perintah klaimnya.
  * Model yang Anda daftarkan melalui `promos claim` memiliki tag `promo`, yang berubah menjadi `promo ended` setelah periode penawaran berakhir.
  * Saat penawaran baru pertama kali terlihat, pemberitahuan satu kali akan mengarahkan ke `openclaw promos list`. Penawaran yang sudah Anda cantumkan atau klaim tidak akan pernah diumumkan lagi.


Fitur ini membaca salinan cache lokal dari umpan promosi yang dihosting oleh ClawHub (biasanya diperbarui sekali sehari melalui permintaan bersyarat, atau lebih awal saat snapshot cache kedaluwarsa; kegagalan pembaruan dilewati tanpa pemberitahuan). Pembaruan data usang menunggu paling lama 2,5 detik dan tidak pernah mengganggu pencantuman. Output `--json` dan `--plain` tetap bersih untuk pemrosesan mesin: tanpa bagian atau pemberitahuan promosi. Proses klaim selalu memvalidasi ulang terhadap API ClawHub yang aktif, sehingga penawaran yang ditarik lebih awal akan ditolak meskipun salinan cache masih menampilkannya.

Was this useful?YesNo

Open issue