---
title: Penyiapan
source_url: https://docs.openclaw.ai/id/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Inisialisasi konfigurasi dasar dan ruang kerja agen. Jika ada flag orientasi awal, juga menjalankan wizard.

## Opsi

Flag | Deskripsi  
---|---  
`--workspace <dir>` | Direktori ruang kerja agen (default `~/.openclaw/workspace`; disimpan sebagai `agents.defaults.workspace`).  
`--wizard` | Jalankan orientasi awal interaktif.  
`--non-interactive` | Jalankan orientasi awal tanpa prompt.  
`--mode <mode>` | Mode orientasi awal: `local` atau `remote`.  
`--import-from <provider>` | Penyedia migrasi yang akan dijalankan selama orientasi awal.  
`--import-source <path>` | Home agen sumber untuk `--import-from`.  
`--import-secrets` | Impor rahasia yang didukung selama migrasi orientasi awal.  
`--remote-url <url>` | URL WebSocket Gateway jarak jauh.  
`--remote-token <token>` | Token Gateway jarak jauh (opsional).  
  
### Pemicu otomatis wizard

`openclaw setup` menjalankan wizard ketika salah satu flag ini secara eksplisit ada, bahkan tanpa `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Contoh

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Catatan

  * `openclaw setup` biasa menginisialisasi konfigurasi dan ruang kerja tanpa menjalankan alur orientasi awal penuh.
  * Setelah setup biasa, jalankan `openclaw onboard` untuk perjalanan terpandu penuh, `openclaw configure` untuk perubahan tertarget, atau `openclaw channels add` untuk menambahkan akun saluran.
  * Jika status Hermes terdeteksi, orientasi awal interaktif dapat menawarkan migrasi secara otomatis. Orientasi awal impor memerlukan setup baru; gunakan [Migrasi](</id/cli/migrate>) untuk rencana dry-run, cadangan, dan mode timpa di luar orientasi awal.


## Terkait

  * [Referensi CLI](</id/cli>)
  * [Orientasi awal (CLI)](</id/start/wizard>)
  * [Memulai](</id/start/getting-started>)
  * [Ikhtisar instalasi](</id/install>)


Was this useful?YesNo