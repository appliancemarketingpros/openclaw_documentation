---
title: Qianfan
source_url: https://docs.openclaw.ai/id/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan adalah platform MaaS Baidu, yang menyediakan **API terpadu** yang merutekan permintaan ke banyak model di balik satu endpoint dan kunci API. Platform ini kompatibel dengan OpenAI, sehingga sebagian besar SDK OpenAI dapat bekerja dengan mengganti URL dasar.

Properti | Nilai  
---|---  
Penyedia | `qianfan`  
Autentikasi | `QIANFAN_API_KEY`  
API | Kompatibel dengan OpenAI  
URL Dasar | `https://qianfan.baidubce.com/v2`  
  
## Memulai

* ### Buat akun Baidu Cloud

Daftar atau masuk di [Konsol Qianfan](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) dan pastikan Anda telah mengaktifkan akses API Qianfan.

* ### Buat kunci API

Buat aplikasi baru atau pilih yang sudah ada, lalu buat kunci API. Format kuncinya adalah `bce-v3/ALTAK-...`.

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Katalog bawaan

Ref model | Input | Konteks | Output maks | Penalaran | Catatan  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | teks | 98,304 | 32,768 | Ya | Model default  
`qianfan/ernie-5.0-thinking-preview` | teks, gambar | 119,000 | 64,000 | Ya | Multimodal  
  
## Contoh konfigurasi

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport dan kompatibilitas

Qianfan berjalan melalui jalur transport yang kompatibel dengan OpenAI, bukan pembentukan permintaan OpenAI native. Artinya fitur SDK OpenAI standar berfungsi, tetapi parameter khusus penyedia mungkin tidak diteruskan.

Katalog dan penimpaan

Katalog bawaan saat ini mencakup `deepseek-v3.2` dan `ernie-5.0-thinking-preview`. Tambahkan atau timpa `models.providers.qianfan` hanya saat Anda membutuhkan URL dasar kustom atau metadata model.

Pemecahan masalah

  * Pastikan kunci API Anda dimulai dengan `bce-v3/ALTAK-` dan akses API Qianfan telah diaktifkan di konsol Baidu Cloud.
  * Jika model tidak tercantum, pastikan akun Anda telah mengaktifkan layanan Qianfan.
  * URL dasar default adalah `https://qianfan.baidubce.com/v2`. Ubah hanya jika Anda menggunakan endpoint kustom atau proksi.


## Terkait

[**Pemilihan model** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Referensi konfigurasi** Referensi konfigurasi lengkap OpenClaw. ](</id/gateway/configuration-reference>) [**Penyiapan agen** Mengonfigurasi default agen dan penetapan model. ](</id/concepts/agent>) [**Dokumentasi API Qianfan** Dokumentasi API Qianfan resmi. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo