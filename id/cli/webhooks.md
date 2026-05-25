---
title: Webhook
source_url: https://docs.openclaw.ai/id/cli/webhooks
scraped_at: 2026-05-25
---

# `openclaw webhooks`

Helper dan integrasi Webhook. Saat ini area ini dibatasi untuk alur Gmail Pub/Sub yang terintegrasi dengan pengawas `gog` bawaan.

## Subperintah

bashCopy code
[code]
    openclaw webhooks gmail setup --account <email> [...]openclaw webhooks gmail run   [--account <email>] [...]
[/code]

Subperintah | Deskripsi  
---|---  
`gmail setup` | Konfigurasikan Gmail watch, topik/langganan Pub/Sub, dan target pengiriman webhook OpenClaw.  
`gmail run` | Jalankan `gog watch serve` plus loop perpanjangan otomatis watch.  
  
## `webhooks gmail setup`

Konfigurasikan Gmail watch, Pub/Sub, dan pengiriman webhook OpenClaw.

bashCopy code
[code]
    openclaw webhooks gmail setup --account you@example.comopenclaw webhooks gmail setup --account you@example.com --project my-gcp-project --jsonopenclaw webhooks gmail setup --account you@example.com --hook-url https://gateway.example.com/hooks/gmail
[/code]

### Wajib

Flag | Deskripsi  
---|---  
`--account <email>` | Akun Gmail yang akan diawasi.  
  
### Opsi Pub/Sub

Flag | Default | Deskripsi  
---|---|---  
`--project <id>` | (tidak ada) | ID proyek GCP (pemilik klien OAuth).  
`--topic <name>` | `gog-gmail-watch` | Nama topik Pub/Sub.  
`--subscription <name>` | `gog-gmail-watch-push` | Nama langganan Pub/Sub.  
`--label <label>` | `INBOX` | Label Gmail yang akan diawasi.  
`--push-endpoint <url>` | (tidak ada) | Endpoint push Pub/Sub eksplisit. Mengganti Tailscale.  
  
### Opsi pengiriman OpenClaw

Flag | Default | Deskripsi  
---|---|---  
`--hook-url <url>` | (tidak ada) | URL webhook OpenClaw.  
`--hook-token <token>` | (tidak ada) | Token webhook OpenClaw.  
`--push-token <token>` | (tidak ada) | Token push yang diteruskan ke `gog watch serve`.  
  
### Opsi `gog watch serve`

Flag | Default | Deskripsi  
---|---|---  
`--bind <host>` | `127.0.0.1` | Host bind `gog watch serve`.  
`--port <port>` | `8788` | Port `gog watch serve`.  
`--path <path>` | `/gmail-pubsub` | Path `gog watch serve`.  
`--include-body` | `true` | Sertakan cuplikan isi email. Berikan `--no-include-body` untuk menonaktifkan.  
`--max-bytes <n>` | `20000` | Byte maksimum per cuplikan isi.  
`--renew-minutes <n>` | `720` (12j) | Perpanjang Gmail watch setiap N menit.  
  
### Eksposur Tailscale

Flag | Default | Deskripsi  
---|---|---  
`--tailscale <mode>` | `funnel` | Ekspos endpoint push melalui tailscale: `funnel`, `serve`, atau `off`.  
`--tailscale-path <path>` | (tidak ada) | Path untuk tailscale serve/funnel.  
`--tailscale-target <t>` | (tidak ada) | Target Tailscale serve/funnel (port, `host:port`, atau URL).  
  
### Keluaran

Flag | Deskripsi  
---|---  
`--json` | Cetak ringkasan yang dapat dibaca mesin, bukan teks.  
  
## `webhooks gmail run`

Jalankan `gog watch serve` plus loop perpanjangan otomatis watch di latar depan.

bashCopy code
[code]
    openclaw webhooks gmail run --account you@example.com
[/code]

`run` menerima flag `gog watch serve`, pengiriman OpenClaw, Pub/Sub, dan Tailscale yang sama seperti `setup`, kecuali:

  * `--account` bersifat **opsional** pada `run` (akan kembali ke akun yang dikonfigurasi).
  * `run` **tidak** menerima `--project`, `--push-endpoint`, atau `--json`.
  * Flag `run` tidak memiliki default bawaan; nilai yang hilang akan kembali ke nilai yang ditulis oleh `setup`.

Kategori | Flag  
---|---  
Pub/Sub | `--account`, `--topic`, `--subscription`, `--label`  
Pengiriman OpenClaw | `--hook-url`, `--hook-token`, `--push-token`  
`gog watch serve` | `--bind`, `--port`, `--path`, `--include-body`, `--max-bytes`, `--renew-minutes`  
Tailscale | `--tailscale`, `--tailscale-path`, `--tailscale-target`  
  
## Alur end-to-end

Lihat [Integrasi Gmail Pub/Sub](</id/automation/cron-jobs#gmail-pubsub-integration>) untuk proyek GCP, OAuth, dan penyiapan sisi gateway yang dipasangkan dengan perintah CLI ini.

## Terkait

  * [Referensi CLI](</id/cli>)
  * [Automasi Webhook](</id/automation/cron-jobs>)
  * [Gmail Pub/Sub](</id/automation/cron-jobs#gmail-pubsub-integration>)


Was this useful?YesNo