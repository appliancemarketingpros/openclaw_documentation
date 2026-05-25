---
title: Alur (pengalihan)
source_url: https://docs.openclaw.ai/id/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Tidak ada perintah `openclaw flows` tingkat atas. Inspeksi TaskFlow yang tahan lama berada di bawah `openclaw tasks flow`.

## Subperintah

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Subperintah | Deskripsi | Argumen / opsi  
---|---|---  
`list` | Mencantumkan TaskFlow yang dilacak. | `--json` keluaran yang dapat dibaca mesin; filter `--status <name>` (lihat nilai status di bawah).  
`show` | Menampilkan satu TaskFlow. | `<lookup>` ID alur atau kunci pemilik; `--json` keluaran yang dapat dibaca mesin.  
`cancel` | Membatalkan TaskFlow yang sedang berjalan. | `<lookup>` ID alur atau kunci pemilik.  
  
`<lookup>` menerima ID alur (yang dikembalikan oleh `list` / `show`) atau kunci pemilik alur (pengidentifikasi stabil yang digunakan subsistem pemilik untuk melacak alur).

### Nilai filter status

`--status` pada `list` menerima salah satu dari:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Contoh

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Untuk konsep TaskFlow lengkap dan penulisan, lihat [TaskFlow](</id/automation/taskflow>). Untuk perintah induk `tasks`, lihat [referensi CLI tasks](</id/cli/tasks>).

## Terkait

  * [Referensi CLI](</id/cli>)
  * [Automasi](</id/automation>)
  * [TaskFlow](</id/automation/taskflow>)


Was this useful?YesNo