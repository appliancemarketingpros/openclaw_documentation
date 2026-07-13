---
title: LongCat
source_url: https://docs.openclaw.ai/id/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) menyediakan API terkelola untuk LongCat-2.0, sebuah model penalaran yang dibuat untuk pemrograman dan beban kerja berbasis agen. OpenClaw menyediakan plugin resmi `longcat` untuk endpoint LongCat yang kompatibel dengan OpenAI.

Properti | Nilai  
---|---  
Penyedia | `longcat`  
Autentikasi | `LONGCAT_API_KEY`  
API | Chat Completions kompatibel OpenAI  
URL dasar | `https://api.longcat.chat/openai`  
Model | `longcat/LongCat-2.0`  
Konteks | 1.048.576 token  
Keluaran maks. | 131.072 token  
Masukan | Teks  
  
## Instal Plugin

Instal paket resmi, lalu mulai ulang Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Memulai

* ### Buat kunci API

Masuk ke [Platform API LongCat](<https://longcat.chat/platform/>) dan buat kunci di halaman [Kunci API](<https://longcat.chat/platform/api_keys>).

* ### Jalankan orientasi awal

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Verifikasi model

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

Orientasi awal menambahkan katalog terkelola dan memilih `longcat/LongCat-2.0` jika belum ada model utama yang dikonfigurasi.

### Penyiapan noninteraktif

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Perilaku penalaran

LongCat menyediakan kontrol berpikir biner. OpenClaw memetakan tingkat berpikir yang diaktifkan ke `thinking: { type: "enabled" }` dan `/think off` ke `thinking: { type: "disabled" }`. Saat ini LongCat tidak mendokumentasikan `reasoning_effort`, sehingga OpenClaw tidak mengirimkannya.

LongCat mengembalikan penalaran dalam `reasoning_content`. OpenClaw mempertahankan kolom tersebut ketika memutar ulang giliran pemanggilan alat oleh asisten agar sesi agen multigiliran mempertahankan bentuk pesan yang diharapkan penyedia.

## Harga

Katalog bawaan menggunakan harga bayar sesuai pemakaian LongCat dalam USD per satu juta token: $0,75 untuk masukan tanpa cache, $0,015 untuk masukan dengan cache, dan $2,95 untuk keluaran. LongCat mungkin menawarkan diskon sementara; [halaman harga](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) dan catatan penagihan Anda merupakan sumber yang berlaku.

## LongCat-2.0 yang dihosting sendiri

Penyedia `longcat` ditujukan untuk API terkelola LongCat. Untuk bobot terbuka di [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>), sajikan model melalui runtime yang kompatibel dengan OpenAI dan gunakan penyedia [vLLM](</id/providers/vllm>) atau [SGLang](</id/providers/sglang>) OpenClaw yang sudah ada.

Pertahankan pengidentifikasi model runtime yang tepat dalam katalog penyedia yang dihosting sendiri; jangan arahkan penerapan lokal melalui `longcat/LongCat-2.0`.

## Pemecahan masalah

Kunci berfungsi di shell tetapi tidak di Gateway

Proses Gateway yang dikelola daemon tidak mewarisi setiap variabel shell interaktif. Letakkan `LONGCAT_API_KEY` di `~/.openclaw/.env`, konfigurasikan melalui orientasi awal, atau gunakan referensi rahasia yang disetujui.

Permintaan gagal dengan 402 atau 429

`402` berarti akun tidak memiliki kuota token yang memadai. `429` berarti kunci API mencapai batas laju. Periksa [penggunaan LongCat](<https://longcat.chat/platform/usage>) dan coba lagi permintaan yang dibatasi lajunya setelah periode tunggu penyedia.

Model tidak muncul

Jalankan `openclaw plugins list` dan pastikan plugin `longcat` diaktifkan, lalu jalankan `openclaw models list --provider longcat`.

## Terkait

[**Penyedia model** Konfigurasi penyedia, referensi model, dan perilaku pengalihan saat gagal. ](</id/concepts/model-providers>) [**Dokumentasi API LongCat** Endpoint API terkelola, autentikasi, batas, dan contoh. ](<https://longcat.chat/platform/docs/>) [**Kartu model LongCat-2.0** Arsitektur, panduan penerapan, dan detail model. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Rahasia** Simpan kredensial penyedia tanpa menyematkan teks biasa dalam konfigurasi. ](</id/gateway/secrets>)

Was this useful?YesNo

Open issue