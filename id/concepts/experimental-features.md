---
title: Fitur eksperimental
source_url: https://docs.openclaw.ai/id/concepts/experimental-features
scraped_at: 2026-05-25
---

Fitur eksperimental di OpenClaw adalah **permukaan pratinjau yang harus diaktifkan secara eksplisit**. Fitur ini berada di balik flag eksplisit karena masih memerlukan penggunaan nyata sebelum layak menjadi default stabil atau kontrak publik jangka panjang.

Perlakukan fitur ini berbeda dari config normal:

  * Biarkan **nonaktif secara default** kecuali doc terkait meminta Anda mencobanya.
  * Perkirakan **bentuk dan perilaku berubah** lebih cepat daripada config stabil.
  * Utamakan jalur stabil terlebih dahulu jika sudah ada.
  * Jika Anda menerapkan OpenClaw secara luas, uji flag eksperimental di lingkungan yang lebih kecil sebelum memasukkannya ke baseline bersama.


## Flag yang saat ini didokumentasikan

Permukaan | Kunci | Gunakan saat | Selengkapnya  
---|---|---|---  
Runtime model lokal | `agents.defaults.experimental.localModelLean` | Backend lokal yang lebih kecil atau lebih ketat kewalahan dengan permukaan alat default penuh OpenClaw | [Model Lokal](</id/gateway/local-models>)  
Pencarian memori | `agents.defaults.memorySearch.experimental.sessionMemory` | Anda ingin `memory_search` mengindeks transkrip sesi sebelumnya dan menerima biaya storage/pengindeksan ekstra | [Referensi konfigurasi memori](</id/reference/memory-config#session-memory-search-experimental>)  
Alat perencanaan terstruktur | `tools.experimental.planTool` | Anda ingin alat `update_plan` terstruktur diekspos untuk pelacakan kerja multi-langkah di runtime dan UI yang kompatibel | [Referensi konfigurasi Gateway](</id/gateway/config-tools#toolsexperimental>)  
  
## Mode ramping model lokal

`agents.defaults.experimental.localModelLean: true` adalah katup pelepas tekanan untuk setup model lokal yang lebih lemah. Saat aktif, OpenClaw menghapus tiga alat default — `browser`, `cron`, dan `message` — dari permukaan alat agen untuk setiap giliran. Tidak ada hal lain yang berubah.

### Mengapa tiga alat ini

Tiga alat ini memiliki deskripsi terbesar dan bentuk parameter terbanyak dalam runtime default OpenClaw. Pada backend kompatibel OpenAI dengan konteks kecil atau lebih ketat, inilah perbedaan antara:

  * Skema alat masuk dengan rapi ke prompt vs. mendesak keluar riwayat percakapan.
  * Model memilih alat yang tepat vs. menghasilkan panggilan alat yang tidak valid karena terlalu banyak skema yang terlihat mirip.
  * Adaptor Chat Completions tetap berada dalam batas output terstruktur server vs. memicu 400 pada ukuran payload panggilan alat.


Menghapusnya tidak diam-diam mengubah kabel OpenClaw — ini hanya membuat daftar alat lebih pendek. Model tetap memiliki `read`, `write`, `edit`, `exec`, `apply_patch`, pencarian/pengambilan web (jika dikonfigurasi), memori, dan alat sesi/agen yang tersedia.

### Kapan mengaktifkannya

Aktifkan mode ramping saat Anda sudah membuktikan bahwa model dapat berbicara dengan Gateway tetapi giliran agen penuh bermasalah. Rangkaian sinyal yang umum adalah:

  1. `openclaw infer model run --gateway --model <ref> --prompt "Reply with exactly: pong"` berhasil.
  2. Giliran agen normal gagal dengan panggilan alat yang tidak valid, prompt terlalu besar, atau model mengabaikan alatnya.
  3. Mengubah `localModelLean: true` mengatasi kegagalan tersebut.


### Kapan membiarkannya nonaktif

Jika backend Anda menangani runtime default penuh dengan bersih, biarkan ini nonaktif. Mode ramping adalah solusi sementara, bukan default. Mode ini ada karena sebagian stack lokal memerlukan permukaan alat yang lebih kecil agar berperilaku baik; model hosted dan rig lokal dengan resource memadai tidak memerlukannya.

Mode ramping juga tidak menggantikan `tools.profile`, `tools.allow`/`tools.deny`, atau pintasan model `compat.supportsTools: false`. Jika Anda memerlukan permukaan alat yang lebih sempit secara permanen untuk agen tertentu, gunakan knob stabil tersebut daripada flag eksperimental.

### Aktifkan

json5Copy code
[code]
    {  agents: {    defaults: {      experimental: {        localModelLean: true,      },    },  },}
[/code]

Mulai ulang Gateway setelah mengubah flag, lalu konfirmasi daftar alat yang dipangkas dengan:

bashCopy code
[code]
    openclaw status --deep
[/code]

Output status mendalam mencantumkan alat agen yang aktif; `browser`, `cron`, dan `message` seharusnya tidak ada saat mode ramping aktif.

## Eksperimental bukan berarti tersembunyi

Jika suatu fitur bersifat eksperimental, OpenClaw harus menyatakannya dengan jelas di doc dan di jalur config itu sendiri. Yang **tidak** boleh dilakukan adalah menyelundupkan perilaku pratinjau ke dalam knob default yang terlihat stabil lalu berpura-pura itu normal. Begitulah permukaan config menjadi berantakan.

## Terkait

  * [Fitur](</id/concepts/features>)
  * [Kanal rilis](</id/install/development-channels>)


Was this useful?YesNo