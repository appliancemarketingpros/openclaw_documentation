---
title: Pengiriman agen
source_url: https://docs.openclaw.ai/id/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` menjalankan satu giliran agen dari baris perintah tanpa memerlukan pesan chat masuk. Gunakan untuk alur kerja berskrip, pengujian, dan pengiriman terprogram.

## Mulai cepat

* ### Jalankan giliran agen sederhana

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Ini mengirim pesan melalui Gateway dan mencetak balasannya.

* ### Targetkan agen atau sesi tertentu

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Kirim balasan ke kanal

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Opsi

Opsi | Deskripsi  
---|---  
`--message \<text\>` | Pesan yang akan dikirim (wajib)  
`--to \<dest\>` | Turunkan kunci sesi dari target (telepon, id chat)  
`--agent \<id\>` | Targetkan agen yang dikonfigurasi (menggunakan sesi `main`)  
`--session-id \<id\>` | Gunakan kembali sesi yang sudah ada berdasarkan id  
`--local` | Paksa runtime tertanam lokal (lewati Gateway)  
`--deliver` | Kirim balasan ke kanal chat  
`--channel \<name\>` | Kanal pengiriman (whatsapp, telegram, discord, slack, dll.)  
`--reply-to \<target\>` | Override target pengiriman  
`--reply-channel \<name\>` | Override kanal pengiriman  
`--reply-account \<id\>` | Override id akun pengiriman  
`--thinking \<level\>` | Atur level berpikir untuk profil model yang dipilih  
`--verbose \<on|full|off\>` | Atur level verbose  
`--timeout \<seconds\>` | Override batas waktu agen  
`--json` | Keluarkan JSON terstruktur  
  
## Perilaku

  * Secara default, CLI berjalan **melalui Gateway**. Tambahkan `--local` untuk memaksa runtime tertanam pada mesin saat ini.
  * Jika Gateway tidak dapat dijangkau, CLI **fallback** ke eksekusi tertanam lokal.
  * Pemilihan sesi: `--to` menurunkan kunci sesi (target grup/kanal mempertahankan isolasi; chat langsung digabungkan ke `main`).
  * Flag thinking dan verbose dipertahankan ke dalam penyimpanan sesi.
  * Output: teks biasa secara default, atau `--json` untuk payload + metadata terstruktur.
  * Dengan `--json --deliver`, JSON menyertakan status pengiriman untuk pengiriman terkirim, disupresi, parsial, dan gagal. Lihat [Status pengiriman JSON](</id/cli/agent#json-delivery-status>).


## Contoh

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Terkait

[**Referensi CLI agen** Referensi lengkap flag dan opsi `openclaw agent`. ](</id/cli/agent>) [**Sub-agen** Pembuatan sub-agen latar belakang. ](</id/tools/subagents>) [**Sesi** Cara kerja kunci sesi dan cara `--to`, `--agent`, dan `--session-id` menyelesaikannya. ](</id/concepts/session>) [**Perintah slash** Katalog perintah native yang digunakan di dalam sesi agen. ](</id/tools/slash-commands>)

Was this useful?YesNo