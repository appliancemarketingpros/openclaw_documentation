---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/id/providers/github-copilot
scraped_at: 2026-05-25
---

GitHub Copilot adalah asisten pengodean AI dari GitHub. Ini menyediakan akses ke model Copilot untuk akun dan paket GitHub Anda. OpenClaw dapat menggunakan Copilot sebagai penyedia model dengan dua cara berbeda.

## Dua cara menggunakan Copilot di OpenClaw

### Penyedia bawaan (github-copilot)

Gunakan alur login perangkat native untuk mendapatkan token GitHub, lalu tukarkan token tersebut dengan token API Copilot saat OpenClaw berjalan. Ini adalah jalur **default** dan paling sederhana karena tidak memerlukan VS Code.

* ### Jalankan perintah login

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Anda akan diminta mengunjungi URL dan memasukkan kode sekali pakai. Biarkan terminal tetap terbuka hingga selesai.

* ### Tetapkan model default

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

Atau dalam konfigurasi:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Plugin Copilot Proxy (copilot-proxy)

Gunakan ekstensi VS Code **Copilot Proxy** sebagai jembatan lokal. OpenClaw berbicara dengan endpoint `/v1` milik proxy dan menggunakan daftar model yang Anda konfigurasi di sana.

## Flag opsional

Flag | Deskripsi  
---|---  
`--yes` | Lewati prompt konfirmasi  
`--set-default` | Juga terapkan model default yang direkomendasikan penyedia  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Onboarding non-interaktif

Jika Anda sudah memiliki token akses GitHub OAuth untuk Copilot, impor token tersebut saat penyiapan headless dengan `openclaw onboard --non-interactive`:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

Anda juga dapat menghilangkan `--auth-choice`; meneruskan `--github-copilot-token` akan menyimpulkan pilihan autentikasi penyedia GitHub Copilot. Jika flag dihilangkan, onboarding akan fallback ke `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, lalu `GITHUB_TOKEN`. Gunakan `--secret-input-mode ref` dengan `COPILOT_GITHUB_TOKEN` yang disetel untuk menyimpan `tokenRef` berbasis env alih-alih teks biasa di `auth-profiles.json`.

TTY interaktif diperlukan

Alur login perangkat memerlukan TTY interaktif. Jalankan langsung di terminal, bukan dalam skrip non-interaktif atau pipeline CI.

Ketersediaan model bergantung pada paket Anda

Ketersediaan model Copilot bergantung pada paket GitHub Anda. Jika sebuah model ditolak, coba ID lain (misalnya `github-copilot/gpt-4.1`).

Penyegaran katalog langsung dari API Copilot

Setelah jalur autentikasi login perangkat (atau env-var) menyelesaikan token GitHub, OpenClaw menyegarkan katalog model sesuai permintaan dari `${baseUrl}/models` (endpoint yang sama yang digunakan VS Code Copilot) sehingga runtime melacak hak akses per akun dan jendela konteks yang akurat tanpa churn manifest. Model Copilot yang baru dipublikasikan menjadi terlihat tanpa upgrade OpenClaw, dan jendela konteks mencerminkan batas per model yang sebenarnya (mis. 400k untuk seri gpt-5.x, 1M untuk varian internal `claude-opus-*-1m`).

Katalog statis bawaan tetap menjadi fallback yang terlihat saat discovery dinonaktifkan, pengguna tidak memiliki profil autentikasi GitHub, pertukaran token gagal, atau panggilan HTTPS `/models` mengalami error. Untuk opt out dan sepenuhnya mengandalkan katalog manifest statis (skenario offline / air-gapped):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Pemilihan transport

ID model Claude menggunakan transport Anthropic Messages secara otomatis. Model GPT, o-series, dan Gemini tetap menggunakan transport OpenAI Responses. OpenClaw memilih transport yang benar berdasarkan ref model.

Kompatibilitas permintaan

OpenClaw mengirim header permintaan bergaya IDE Copilot pada transport Copilot, termasuk giliran bawaan untuk Compaction, hasil alat, dan tindak lanjut gambar. Ini tidak mengaktifkan kelanjutan Responses tingkat penyedia untuk Copilot kecuali perilaku tersebut telah diverifikasi terhadap API Copilot.

Urutan resolusi variabel lingkungan

OpenClaw menyelesaikan autentikasi Copilot dari variabel lingkungan dalam urutan prioritas berikut:

Prioritas | Variabel | Catatan  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | Prioritas tertinggi, khusus Copilot  
2 | `GH_TOKEN` | Token GitHub CLI (fallback)  
3 | `GITHUB_TOKEN` | Token GitHub standar (terendah)  
  
Ketika beberapa variabel disetel, OpenClaw menggunakan variabel dengan prioritas tertinggi. Alur login perangkat (`openclaw models auth login-github-copilot`) menyimpan tokennya di penyimpanan profil autentikasi dan lebih diprioritaskan daripada semua variabel lingkungan.

Penyimpanan token

Login menyimpan token GitHub di penyimpanan profil autentikasi dan menukarnya dengan token API Copilot saat OpenClaw berjalan. Anda tidak perlu mengelola token secara manual.

## Embedding pencarian memori

GitHub Copilot juga dapat berfungsi sebagai penyedia embedding untuk [pencarian memori](</id/concepts/memory-search>). Jika Anda memiliki langganan Copilot dan telah login, OpenClaw dapat menggunakannya untuk embedding tanpa kunci API terpisah.

### Deteksi otomatis

Saat `memorySearch.provider` adalah `"auto"` (default), GitHub Copilot dicoba pada prioritas 15 -- setelah embedding lokal tetapi sebelum OpenAI dan penyedia berbayar lainnya. Jika token GitHub tersedia, OpenClaw menemukan model embedding yang tersedia dari API Copilot dan memilih yang terbaik secara otomatis.

### Konfigurasi eksplisit

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Cara kerjanya

  1. OpenClaw menyelesaikan token GitHub Anda (dari env vars atau profil autentikasi).
  2. Menukarnya dengan token API Copilot berumur pendek.
  3. Mengkueri endpoint Copilot `/models` untuk menemukan model embedding yang tersedia.
  4. Memilih model terbaik (lebih memilih `text-embedding-3-small`).
  5. Mengirim permintaan embedding ke endpoint Copilot `/embeddings`.


Ketersediaan model bergantung pada paket GitHub Anda. Jika tidak ada model embedding yang tersedia, OpenClaw melewati Copilot dan mencoba penyedia berikutnya.

## Terkait

[**Pemilihan model** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**OAuth dan autentikasi** Detail autentikasi dan aturan penggunaan ulang kredensial. ](</id/gateway/authentication>)

Was this useful?YesNo