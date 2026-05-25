---
title: Eksekusi kode
source_url: https://docs.openclaw.ai/id/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` menjalankan analisis Python jarak jauh yang di-sandbox pada Responses API milik xAI. Fitur ini didaftarkan oleh Plugin `xai` bawaan (di bawah kontrak `tools`) dan diarahkan ke endpoint `https://api.x.ai/v1/responses` yang sama dengan yang digunakan oleh `x_search`.

Properti | Nilai  
---|---  
Nama alat | `code_execution`  
Plugin penyedia | `xai` (bawaan, `enabledByDefault: true`)  
Autentikasi | profil autentikasi xAI, `XAI_API_KEY`, atau `plugins.entries.xai.config.webSearch.apiKey`  
Model default | `grok-4-1-fast`  
Batas waktu default | 30 detik  
`maxTurns` default | belum diatur (xAI menerapkan batas internalnya sendiri)  
  
Ini berbeda dari [`exec`](</id/tools/exec>) lokal:

  * `exec` menjalankan perintah shell di mesin Anda atau node yang dipasangkan.
  * `code_execution` menjalankan Python di sandbox jarak jauh milik xAI.


Gunakan `code_execution` untuk:

  * Perhitungan.
  * Tabulasi.
  * Statistik cepat.
  * Analisis bergaya bagan.
  * Menganalisis data yang dikembalikan oleh `x_search` atau `web_search`.


Jangan gunakan ini saat Anda memerlukan file lokal, shell Anda, repo Anda, atau perangkat yang dipasangkan. Gunakan [`exec`](</id/tools/exec>) untuk itu.

## Penyiapan

* ### Provide an xAI API key

Jalankan `openclaw onboard --auth-choice xai-api-key` untuk `code_execution` dan `x_search`, atau tetapkan `XAI_API_KEY` / konfigurasikan kunci di bawah Plugin xAI saat Anda juga ingin pencarian web Grok menggunakan kredensial yang sama:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

Atau melalui config:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Enable and tune code_execution

Alat ini dibatasi oleh `plugins.entries.xai.config.codeExecution.enabled`. Default-nya mati.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Restart the Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` muncul di daftar alat agen setelah Plugin xAI mendaftar ulang dengan `enabled: true`.

## Cara menggunakannya

Ajukan permintaan secara alami dan buat maksud analisisnya eksplisit:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

Alat ini mengambil satu parameter `task` secara internal, jadi agen harus mengirim permintaan analisis lengkap dan data inline apa pun dalam satu prompt.

## Kesalahan

Saat alat berjalan tanpa autentikasi, alat ini mengembalikan kesalahan `missing_xai_api_key` terstruktur yang menunjuk ke opsi profil autentikasi, env var, dan config. Kesalahan ini berupa JSON, bukan exception yang dilempar, sehingga agen dapat memperbaiki sendiri:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Batasan

  * Ini adalah eksekusi xAI jarak jauh, bukan eksekusi proses lokal.
  * Perlakukan hasil sebagai analisis sementara, bukan sesi notebook persisten.
  * Jangan mengasumsikan akses ke file lokal atau workspace Anda.
  * Untuk data X terbaru, gunakan [`x_search`](</id/tools/web#x_search>) terlebih dahulu dan teruskan hasilnya ke `code_execution`.


## Terkait

[**Exec tool** Eksekusi shell lokal di mesin Anda atau node yang dipasangkan. ](</id/tools/exec>) [**Exec approvals** Kebijakan izinkan/tolak untuk eksekusi shell. ](</id/tools/exec-approvals>) [**Web tools** `web_search`, `x_search`, dan `web_fetch`. ](</id/tools/web>) [**xAI provider** Model Grok, pencarian web/x, dan config eksekusi kode. ](</id/providers/xai>)

Was this useful?YesNo