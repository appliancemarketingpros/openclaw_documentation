---
title: NovitaAI
source_url: https://docs.openclaw.ai/id/providers/novita
scraped_at: 2026-06-29
---

ModelsProviders

NovitaAI adalah penyedia infrastruktur AI terkelola dengan API model yang kompatibel dengan OpenAI. Di OpenClaw, ini adalah penyedia model bawaan, sehingga id penyedia adalah `novita`, kredensial melewati alur autentikasi model normal, dan ref model tampak seperti `novita/deepseek/deepseek-v3-0324`.

Gunakan Novita saat Anda menginginkan akses terkelola ke rute model open-weight dan pihak ketiga tanpa menjalankan server inferensi sendiri. Katalog bawaan berfokus pada model chat yang praktis untuk giliran agen, termasuk rute DeepSeek, Moonshot, MiniMax, GLM, dan Qwen yang diekspos oleh Novita.

Penyedia ini menggunakan endpoint Novita yang kompatibel dengan OpenAI. OpenClaw menangani pendaftaran penyedia, autentikasi, alias, normalisasi ref model, dan pemilihan URL dasar; Novita mengontrol ketersediaan model live, izin akun, harga, dan batas laju.

## Penyiapan

Buat API key di [novita.ai/settings/key-management](<https://novita.ai/settings/key-management>), lalu jalankan:

bashCopy code
[code]
    openclaw onboard --auth-choice novita-api-key
[/code]

Atau tetapkan:

bashCopy code
[code]
    export NOVITA_API_KEY="<your-novita-api-key>" # pragma: allowlist secret
[/code]

## Default

  * Penyedia: `novita`
  * Alias: `novita-ai`, `novitaai`
  * URL dasar: `https://api.novita.ai/openai/v1`
  * Variabel env: `NOVITA_API_KEY`
  * Model default: `novita/deepseek/deepseek-v3-0324`


## Kapan memilih Novita

  * Anda menginginkan akses model open-weight terkelola dengan API yang kompatibel dengan OpenAI.
  * Anda menginginkan rute keluarga DeepSeek, Kimi, MiniMax, GLM, atau Qwen melalui satu akun penyedia.
  * Anda menginginkan jalur fallback terkelola lain selain OpenRouter, GMI, DeepInfra, atau API vendor langsung.
  * Anda lebih memilih hosting model di sisi penyedia daripada memelihara infrastruktur vLLM, SGLang, LM Studio, atau Ollama.


Pilih penyedia vendor langsung saat Anda memerlukan parameter permintaan native vendor atau kontrak dukungan. Pilih penyedia lokal saat model harus berjalan di perangkat keras Anda sendiri atau di balik batas jaringan Anda sendiri.

## Model

Katalog bawaan menginisialisasi id rute NovitaAI yang umum tersedia, termasuk:

  * `novita/moonshotai/kimi-k2.5`
  * `novita/minimax/minimax-m2.7`
  * `novita/zai-org/glm-5`
  * `novita/deepseek/deepseek-v3-0324`
  * `novita/deepseek/deepseek-r1-0528`
  * `novita/qwen/qwen3-235b-a22b-fp8`


Katalog adalah titik awal untuk pemilihan model OpenClaw. Akun, wilayah, atau katalog Novita saat ini dapat menambahkan, menghapus, atau membatasi rute. Periksa penyedia dari CLI sebelum menetapkan default jangka panjang:

bashCopy code
[code]
    openclaw models list --provider novita
[/code]

## Pemecahan Masalah

  * `401` atau `403`: verifikasi key di halaman manajemen key Novita dan jalankan ulang `openclaw onboard --auth-choice novita-api-key` jika profil yang tersimpan sudah kedaluwarsa.
  * Kesalahan model tidak dikenal: gunakan `novita/<route-id>` persis seperti yang dikembalikan oleh `openclaw models list --provider novita`.
  * Rute lambat atau gagal: coba rute model Novita lain atau tetapkan Novita sebagai penyedia fallback untuk beban kerja yang dapat menoleransi variasi spesifik penyedia.


## Terkait

  * [Penyedia model](</id/concepts/model-providers>)
  * [Semua penyedia](</id/providers>)


Was this useful?YesNo

Open issue