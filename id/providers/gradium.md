---
title: Gradium
source_url: https://docs.openclaw.ai/id/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>) adalah penyedia teks-ke-ucapan bawaan untuk OpenClaw. Plugin dapat merender balasan audio normal (WAV), output Opus yang kompatibel dengan catatan suara, dan audio u-law 8 kHz untuk permukaan telepon.

Properti | Nilai  
---|---  
ID penyedia | `gradium`  
Autentikasi | `GRADIUM_API_KEY` atau config `apiKey`  
URL dasar | `https://api.gradium.ai` (default)  
Suara default | `Emma` (`YTpq7expH9539ERJ`)  
  
## Penyiapan

Buat kunci API Gradium, lalu ekspos ke OpenClaw dengan env var atau kunci config.

### Env var

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### Kunci config

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

Plugin memeriksa `apiKey` yang telah di-resolve terlebih dahulu dan melakukan fallback ke variabel lingkungan `GRADIUM_API_KEY`.

## Config

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

Kunci | Tipe | Deskripsi  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | Kunci API yang telah di-resolve. Mendukung `${ENV}` dan referensi rahasia.  
`messages.tts.providers.gradium.baseUrl` | string | Mengganti origin API. Garis miring penutup dihapus. Default ke `https://api.gradium.ai`.  
`messages.tts.providers.gradium.voiceId` | string | ID suara default yang digunakan saat tidak ada penggantian direktif.  
  
Format audio output dipilih secara otomatis oleh runtime berdasarkan permukaan target dan tidak dapat dikonfigurasi dari `openclaw.json`. Lihat Output di bawah.

## Suara

Nama | ID Suara  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
Suara default: Emma.

### Penggantian suara per pesan

Saat kebijakan ucapan aktif mengizinkan penggantian suara, Anda dapat mengganti suara secara inline menggunakan token direktif. Semua ini di-resolve ke penggantian `voiceId` yang sama:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

Jika kebijakan ucapan menonaktifkan penggantian suara, direktif akan dikonsumsi tetapi diabaikan.

## Output

Runtime memilih format output dari permukaan target. Penyedia tidak mensintesis format lain saat ini.

Target | Format | Ekstensi file | Laju sampel | Flag kompatibel suara  
---|---|---|---|---  
Audio standar | `wav` | `.wav` | penyedia | tidak  
Catatan suara | `opus` | `.opus` | penyedia | ya  
Telepon | `ulaw_8000` | n/a | 8 kHz | n/a  
  
## Urutan pemilihan otomatis

Di antara penyedia TTS yang dikonfigurasi, urutan pemilihan otomatis Gradium adalah `30`. Lihat [Teks-ke-Ucapan](</id/tools/tts>) untuk mengetahui cara OpenClaw memilih penyedia aktif saat `messages.tts.provider` tidak dipin.

## Terkait

  * [Teks-ke-Ucapan](</id/tools/tts>)
  * [Ikhtisar Media](</id/tools/media-overview>)


Was this useful?YesNo