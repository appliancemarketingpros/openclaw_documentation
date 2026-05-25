---
title: Saluran QA
source_url: https://docs.openclaw.ai/id/channels/qa-channel
scraped_at: 2026-05-25
---

`qa-channel` adalah transport pesan sintetis bawaan untuk QA OpenClaw otomatis. Ini bukan saluran produksi - ini ada untuk menguji batas Plugin saluran yang sama dengan yang digunakan oleh transport nyata sambil menjaga state tetap deterministik dan sepenuhnya dapat diperiksa.

## Apa yang dilakukan

  * Tata bahasa target kelas Slack: 
    * `dm:<user>`
    * `channel:<room>`
    * `group:<room>`
    * `thread:<room>/<thread>`
  * Percakapan `channel:` dan `group:` bersama ditampilkan kepada agen sebagai giliran ruang grup/saluran, sehingga percakapan tersebut menguji kebijakan balasan-terlihat dan perutean alat-pesan yang sama dengan yang digunakan oleh Discord, Slack, Telegram, dan transport serupa.
  * Bus sintetis berbasis HTTP untuk injeksi pesan masuk, penangkapan transkrip keluar, pembuatan thread, reaksi, edit, hapus, dan tindakan pencarian/baca.
  * Runner pemeriksaan mandiri sisi host yang menulis laporan Markdown ke `.artifacts/qa-e2e/`.


## Konfigurasi

jsonCopy code
[code]
    {  "channels": {    "qa-channel": {      "baseUrl": "http://127.0.0.1:43123",      "botUserId": "openclaw",      "botDisplayName": "OpenClaw QA",      "allowFrom": ["*"],      "pollTimeoutMs": 1000    }  }}
[/code]

Kunci akun:

  * `enabled` \- toggle utama untuk akun ini.
  * `name` \- label tampilan opsional.
  * `baseUrl` \- URL bus sintetis.
  * `botUserId` \- id pengguna bot bergaya Matrix yang digunakan dalam tata bahasa target.
  * `botDisplayName` \- nama tampilan untuk pesan keluar.
  * `pollTimeoutMs` \- jendela tunggu long-poll. Bilangan bulat antara 100 dan 30000.
  * `allowFrom` \- daftar izinkan pengirim (id pengguna atau `"*"`). Pesan langsung dan kebijakan grup yang diizinkan sama-sama menggunakan id pengirim sintetis ini.
  * `groupPolicy` \- kebijakan ruang bersama: `"open"` (default), `"allowlist"`, atau `"disabled"`.
  * `groupAllowFrom` \- daftar izinkan pengirim ruang bersama opsional. Jika dihilangkan di bawah `"allowlist"`, QA Channel kembali menggunakan `allowFrom`.
  * `groups.<room>.requireMention` \- wajibkan mention bot sebelum membalas di ruang grup/saluran tertentu. `groups."*"` menetapkan default.
  * `defaultTo` \- target fallback saat tidak ada yang diberikan.
  * `actions.messages` / `actions.reactions` / `actions.search` / `actions.threads` \- pembatasan alat per tindakan.


Kunci multi-akun di tingkat teratas:

  * `accounts` \- record override per akun bernama yang dikunci berdasarkan id akun.
  * `defaultAccount` \- id akun pilihan saat beberapa akun dikonfigurasi.


## Runner

Pemeriksaan mandiri sisi host (menulis laporan Markdown di bawah `.artifacts/qa-e2e/`):

bashCopy code
[code]
    pnpm qa:e2e
[/code]

Ini merutekan melalui `qa-lab`, memulai bus QA dalam repo, mem-boot slice runtime `qa-channel` bawaan, dan menjalankan pemeriksaan mandiri deterministik.

Suite skenario lengkap berbasis repo:

bashCopy code
[code]
    pnpm openclaw qa suite
[/code]

Menjalankan skenario secara paralel terhadap lane Gateway QA. Lihat [ikhtisar QA](</id/concepts/qa-e2e-automation>) untuk skenario, profil, dan mode penyedia.

Situs QA berbasis Docker (Gateway + UI debugger QA Lab dalam satu stack):

bashCopy code
[code]
    pnpm qa:lab:up
[/code]

Membangun situs QA, memulai stack Gateway + QA Lab berbasis Docker, dan mencetak URL QA Lab. Dari sana Anda dapat memilih skenario, memilih lane model, meluncurkan run individual, dan melihat hasil secara langsung. Debugger QA Lab terpisah dari bundel Control UI yang dikirimkan.

## Terkait

  * [Ikhtisar QA](</id/concepts/qa-e2e-automation>) \- stack keseluruhan, adaptor transport, penulisan skenario
  * [QA Matrix](</id/concepts/qa-matrix>) \- contoh runner transport langsung yang menggerakkan saluran nyata
  * [Pairing](</id/channels/pairing>)
  * [Grup](</id/channels/groups>)
  * [Ikhtisar saluran](</id/channels>)


Was this useful?YesNo