---
title: Indikator pengetikan
source_url: https://docs.openclaw.ai/id/concepts/typing-indicators
scraped_at: 2026-05-25
---

Indikator pengetikan dikirim ke saluran chat saat sebuah eksekusi aktif. Gunakan `agents.defaults.typingMode` untuk mengontrol **kapan** pengetikan dimulai dan `typingIntervalSeconds` untuk mengontrol **seberapa sering** indikator disegarkan.

## Default

Saat `agents.defaults.typingMode` **tidak disetel** , OpenClaw mempertahankan perilaku lama:

  * **Chat langsung** : pengetikan dimulai segera setelah loop model dimulai.
  * **Chat grup dengan sebutan** : pengetikan dimulai segera.
  * **Chat grup tanpa sebutan** : pengetikan dimulai hanya saat teks pesan mulai streaming.
  * **Eksekusi Heartbeat** : pengetikan dimulai saat eksekusi Heartbeat dimulai jika target Heartbeat yang terselesaikan adalah chat yang mendukung pengetikan dan pengetikan tidak dinonaktifkan.


## Mode

Setel `agents.defaults.typingMode` ke salah satu dari:

  * `never` \- tidak ada indikator pengetikan, sama sekali.
  * `instant` \- mulai mengetik **segera setelah loop model dimulai** , meskipun eksekusi kemudian hanya mengembalikan token balasan senyap.
  * `thinking` \- mulai mengetik pada **delta penalaran pertama** (memerlukan `reasoningLevel: "stream"` untuk eksekusi).
  * `message` \- mulai mengetik pada **delta teks non-senyap pertama** (mengabaikan token senyap `NO_REPLY`).


Urutan "seberapa awal dipicu": `never` → `message` → `thinking` → `instant`

## Konfigurasi

Setel default tingkat agen:

json5Copy code
[code]
    {  agents: {    defaults: {      typingMode: "thinking",      typingIntervalSeconds: 6,    },  },}
[/code]

Timpa mode atau irama per sesi:

json5Copy code
[code]
    {  session: {    typingMode: "message",    typingIntervalSeconds: 4,  },}
[/code]

## Catatan

  * Mode `message` tidak akan menampilkan pengetikan untuk balasan yang hanya senyap ketika seluruh payload adalah token senyap persis (misalnya `NO_REPLY` / `no_reply`, dicocokkan tanpa membedakan huruf besar/kecil).
  * `thinking` hanya dipicu jika eksekusi melakukan streaming penalaran (`reasoningLevel: "stream"`). Jika model tidak memancarkan delta penalaran, pengetikan tidak akan dimulai.
  * Pengetikan Heartbeat adalah sinyal keaktifan untuk target pengiriman yang terselesaikan. Ini dimulai saat eksekusi Heartbeat dimulai, alih-alih mengikuti waktu streaming `message` atau `thinking`. Setel `typingMode: "never"` untuk menonaktifkannya.
  * Heartbeat tidak menampilkan pengetikan saat `target: "none"`, saat target tidak dapat diselesaikan, saat pengiriman chat dinonaktifkan untuk Heartbeat, atau saat saluran tidak mendukung pengetikan.
  * `typingIntervalSeconds` mengontrol **irama penyegaran** , bukan waktu mulai. Defaultnya adalah 6 detik.


## Terkait

[**Kehadiran** Cara Gateway melacak klien yang terhubung dan menampilkannya di tab Instans macOS. ](</id/concepts/presence>) [**Streaming dan pemotongan** Perilaku streaming keluar, batas potongan, dan pengiriman khusus saluran. ](</id/concepts/streaming>)

Was this useful?YesNo