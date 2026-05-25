---
title: Ollama
source_url: https://docs.openclaw.ai/id/providers/ollama
scraped_at: 2026-05-25
---

OpenClaw terintegrasi dengan API asli Ollama (`/api/chat`) untuk model cloud terhosting dan server Ollama lokal/di-host sendiri. Anda dapat menggunakan Ollama dalam tiga mode: `Cloud + Local` melalui host Ollama yang dapat dijangkau, `Cloud only` terhadap `https://ollama.com`, atau `Local only` terhadap host Ollama yang dapat dijangkau.

Konfigurasi penyedia Ollama menggunakan `baseUrl` sebagai kunci kanonis. OpenClaw juga menerima `baseURL` untuk kompatibilitas dengan contoh bergaya OpenAI SDK, tetapi konfigurasi baru sebaiknya mengutamakan `baseUrl`.

## Aturan autentikasi

Local and LAN hosts

Host Ollama lokal dan LAN tidak memerlukan token bearer nyata. OpenClaw menggunakan penanda lokal `ollama-local` hanya untuk URL dasar Ollama loopback, jaringan privat, `.local`, dan bare-hostname.

Remote and Ollama Cloud hosts

Host publik jarak jauh dan Ollama Cloud (`https://ollama.com`) memerlukan kredensial nyata melalui `OLLAMA_API_KEY`, profil autentikasi, atau `apiKey` milik penyedia.

Custom provider ids

ID penyedia kustom yang menetapkan `api: "ollama"` mengikuti aturan yang sama. Misalnya, penyedia `ollama-remote` yang mengarah ke host Ollama LAN privat dapat menggunakan `apiKey: "ollama-local"` dan sub-agen akan menyelesaikan penanda tersebut melalui hook penyedia Ollama alih-alih memperlakukannya sebagai kredensial yang hilang. Pencarian memori juga dapat menetapkan `agents.defaults.memorySearch.provider` ke ID penyedia kustom tersebut agar embedding menggunakan endpoint Ollama yang sesuai.

Auth profiles

`auth-profiles.json` menyimpan kredensial untuk ID penyedia. Letakkan pengaturan endpoint (`baseUrl`, `api`, ID model, header, timeout) di `models.providers.<id>`. Berkas profil autentikasi datar lama seperti `{ "ollama-windows": { "apiKey": "ollama-local" } }` bukan format runtime; jalankan `openclaw doctor --fix` untuk menulis ulangnya menjadi profil kunci API kanonis `ollama-windows:default` dengan cadangan. `baseUrl` dalam berkas itu adalah derau kompatibilitas dan sebaiknya dipindahkan ke konfigurasi penyedia.

Memory embedding scope

Saat Ollama digunakan untuk embedding memori, autentikasi bearer dibatasi pada host tempat ia dideklarasikan:

  * Kunci tingkat penyedia hanya dikirim ke host Ollama milik penyedia tersebut.
  * `agents.*.memorySearch.remote.apiKey` hanya dikirim ke host embedding jarak jauhnya.
  * Nilai env `OLLAMA_API_KEY` murni diperlakukan sebagai konvensi Ollama Cloud, tidak dikirim ke host lokal atau di-host sendiri secara default.


## Memulai

Pilih metode dan mode penyiapan yang Anda inginkan.

### Onboarding (recommended)

**Paling cocok untuk:** jalur tercepat menuju penyiapan cloud atau lokal Ollama yang berfungsi.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard
[/code]

Pilih **Ollama** dari daftar penyedia.

* ### Choose your mode

  * **Cloud + Local** — host Ollama lokal plus model cloud yang dirutekan melalui host tersebut
  * **Cloud only** — model Ollama terhosting melalui `https://ollama.com`
  * **Local only** — hanya model lokal


* ### Select a model

`Cloud only` meminta `OLLAMA_API_KEY` dan menyarankan default cloud terhosting. `Cloud + Local` dan `Local only` meminta URL dasar Ollama, menemukan model yang tersedia, dan otomatis menarik model lokal yang dipilih jika belum tersedia. Saat Ollama melaporkan tag `:latest` terinstal seperti `gemma4:latest`, penyiapan menampilkan model terinstal itu sekali, bukan menampilkan `gemma4` dan `gemma4:latest` sekaligus atau menarik alias polos lagi. `Cloud + Local` juga memeriksa apakah host Ollama tersebut sudah masuk untuk akses cloud.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider ollama
[/code]

### Mode non-interaktif

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --accept-risk
[/code]

Secara opsional tentukan URL dasar atau model kustom:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

### Manual setup

**Paling cocok untuk:** kontrol penuh atas penyiapan cloud atau lokal.

* ### Choose cloud or local

  * **Cloud + Local** : pasang Ollama, masuk dengan `ollama signin`, dan rutekan permintaan cloud melalui host tersebut
  * **Cloud only** : gunakan `https://ollama.com` dengan `OLLAMA_API_KEY`
  * **Local only** : pasang Ollama dari [ollama.com/download](<https://ollama.com/download>)


* ### Pull a local model (local only)

bashCopy code
[code]
    ollama pull gemma4# orollama pull gpt-oss:20b# orollama pull llama3.3
[/code]

* ### Enable Ollama for OpenClaw

Untuk `Cloud only`, gunakan `OLLAMA_API_KEY` nyata Anda. Untuk penyiapan yang didukung host, nilai placeholder apa pun dapat digunakan:

bashCopy code
[code]
    # Cloudexport OLLAMA_API_KEY="your-ollama-api-key" # Local-onlyexport OLLAMA_API_KEY="ollama-local" # Or configure in your config fileopenclaw config set models.providers.ollama.apiKey "OLLAMA_API_KEY"
[/code]

* ### Inspect and set your model

bashCopy code
[code]
    openclaw models listopenclaw models set ollama/gemma4
[/code]

Atau tetapkan default dalam konfigurasi:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ollama/gemma4" },    },  },}
[/code]

## Model cloud

### Cloud + Local

`Cloud + Local` menggunakan host Ollama yang dapat dijangkau sebagai titik kontrol untuk model lokal dan cloud. Ini adalah alur hibrida pilihan Ollama.

Gunakan **Cloud + Local** selama penyiapan. OpenClaw meminta URL dasar Ollama, menemukan model lokal dari host tersebut, dan memeriksa apakah host sudah masuk untuk akses cloud dengan `ollama signin`. Saat host sudah masuk, OpenClaw juga menyarankan default cloud terhosting seperti `kimi-k2.5:cloud`, `minimax-m2.7:cloud`, dan `glm-5.1:cloud`.

Jika host belum masuk, OpenClaw mempertahankan penyiapan hanya lokal hingga Anda menjalankan `ollama signin`.

### Cloud only

`Cloud only` berjalan terhadap API terhosting Ollama di `https://ollama.com`.

Gunakan **Cloud only** selama penyiapan. OpenClaw meminta `OLLAMA_API_KEY`, menetapkan `baseUrl: "https://ollama.com"`, dan mengisi daftar model cloud terhosting. Jalur ini **tidak** memerlukan server Ollama lokal atau `ollama signin`.

Daftar model cloud yang ditampilkan selama `openclaw onboard` diisi langsung dari `https://ollama.com/api/tags`, dibatasi hingga 500 entri, sehingga pemilih mencerminkan katalog terhosting saat ini, bukan seed statis. Jika `ollama.com` tidak dapat dijangkau atau tidak mengembalikan model pada waktu penyiapan, OpenClaw kembali ke saran hardcode sebelumnya agar onboarding tetap selesai.

### Local only

Dalam mode hanya lokal, OpenClaw menemukan model dari instans Ollama yang dikonfigurasi. Jalur ini ditujukan untuk server Ollama lokal atau di-host sendiri.

OpenClaw saat ini menyarankan `gemma4` sebagai default lokal.

## Penemuan model (penyedia implisit)

Saat Anda menetapkan `OLLAMA_API_KEY` (atau profil autentikasi) dan **tidak** mendefinisikan `models.providers.ollama` atau penyedia jarak jauh kustom lain dengan `api: "ollama"`, OpenClaw menemukan model dari instans Ollama lokal di `http://127.0.0.1:11434`.

Perilaku | Detail  
---|---  
Kueri katalog | Mengueri `/api/tags`  
Deteksi kapabilitas | Menggunakan lookup `/api/show` best-effort untuk membaca `contextWindow`, parameter Modelfile `num_ctx` yang diperluas, dan kapabilitas termasuk vision/tools  
Model vision | Model dengan kapabilitas `vision` yang dilaporkan oleh `/api/show` ditandai sebagai mampu gambar (`input: ["text", "image"]`), sehingga OpenClaw otomatis menyisipkan gambar ke prompt  
Deteksi reasoning | Menggunakan kapabilitas `/api/show` jika tersedia, termasuk `thinking`; fallback ke heuristik nama model (`r1`, `reasoning`, `think`) saat Ollama menghilangkan kapabilitas  
Batas token | Menetapkan `maxTokens` ke batas token maksimum default Ollama yang digunakan OpenClaw  
Biaya | Menetapkan semua biaya ke `0`  
  
Ini menghindari entri model manual sambil menjaga katalog tetap selaras dengan instans Ollama lokal. Anda dapat menggunakan ref lengkap seperti `ollama/<pulled-model>:latest` dalam `infer model run` lokal; OpenClaw menyelesaikan model terinstal itu dari katalog langsung Ollama tanpa memerlukan entri `models.json` yang ditulis manual.

Untuk host Ollama yang sudah masuk, beberapa model `:cloud` mungkin dapat digunakan melalui `/api/chat` dan `/api/show` sebelum muncul di `/api/tags`. Saat Anda secara eksplisit memilih ref lengkap `ollama/<model>:cloud`, OpenClaw memvalidasi model hilang yang persis itu dengan `/api/show` dan menambahkannya ke katalog runtime hanya jika Ollama mengonfirmasi metadata model. Salah ketik tetap gagal sebagai model tidak dikenal, bukan dibuat otomatis.

bashCopy code
[code]
    # See what models are availableollama listopenclaw models list
[/code]

Untuk uji smoke pembuatan teks sempit yang menghindari seluruh permukaan alat agen, gunakan `infer model run` lokal dengan ref model Ollama lengkap:

bashCopy code
[code]
    OLLAMA_API_KEY=ollama-local \  openclaw infer model run \    --local \    --model ollama/llama3.2:latest \    --prompt "Reply with exactly: pong" \    --json
[/code]

Jalur itu tetap menggunakan penyedia, autentikasi, dan transport Ollama asli yang dikonfigurasi OpenClaw, tetapi tidak memulai giliran agen chat atau memuat konteks MCP/alat. Jika ini berhasil sementara balasan agen normal gagal, selidiki kapasitas prompt/alat agen model berikutnya.

Untuk uji smoke model vision sempit pada jalur ramping yang sama, tambahkan satu atau beberapa berkas gambar ke `infer model run`. Ini mengirim prompt dan gambar langsung ke model vision Ollama yang dipilih tanpa memuat alat chat, memori, atau konteks sesi sebelumnya:

bashCopy code
[code]
    OLLAMA_API_KEY=ollama-local \  openclaw infer model run \    --local \    --model ollama/qwen2.5vl:7b \    --prompt "Describe this image in one sentence." \    --file ./photo.jpg \    --json
[/code]

`model run --file` menerima berkas yang terdeteksi sebagai `image/*`, termasuk input PNG, JPEG, dan WebP umum. Berkas non-gambar ditolak sebelum Ollama dipanggil. Untuk pengenalan ucapan, gunakan `openclaw infer audio transcribe` sebagai gantinya.

Saat Anda mengganti percakapan dengan `/model ollama/<model>`, OpenClaw memperlakukan itu sebagai pilihan pengguna yang persis. Jika `baseUrl` Ollama yang dikonfigurasi tidak dapat dijangkau, balasan berikutnya gagal dengan kesalahan penyedia alih-alih diam-diam menjawab dari model fallback lain yang dikonfigurasi.

Pekerjaan Cron terisolasi melakukan satu pemeriksaan keamanan lokal tambahan sebelum memulai giliran agen. Jika model yang dipilih terselesaikan ke penyedia Ollama lokal, jaringan privat, atau `.local` dan `/api/tags` tidak dapat dijangkau, OpenClaw mencatat eksekusi Cron tersebut sebagai `skipped` dengan `ollama/<model>` yang dipilih di teks galat. Praflight endpoint disimpan dalam cache selama 5 menit, sehingga beberapa pekerjaan Cron yang diarahkan ke daemon Ollama yang sama dan sedang berhenti tidak semuanya meluncurkan permintaan model yang gagal.

Verifikasi langsung jalur teks lokal, jalur stream native, dan embeddings terhadap Ollama lokal dengan:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_OLLAMA=1 OPENCLAW_LIVE_OLLAMA_WEB_SEARCH=0 \  pnpm test:live -- extensions/ollama/ollama.live.test.ts
[/code]

Untuk menambahkan model baru, cukup tarik dengan Ollama:

bashCopy code
[code]
    ollama pull mistral
[/code]

Model baru akan ditemukan secara otomatis dan tersedia untuk digunakan.

## Vision dan deskripsi gambar

Plugin Ollama bawaan mendaftarkan Ollama sebagai penyedia pemahaman media yang mendukung gambar. Ini memungkinkan OpenClaw merutekan permintaan deskripsi gambar eksplisit dan default model gambar yang dikonfigurasi melalui model vision Ollama lokal atau ter-host.

Untuk vision lokal, tarik model yang mendukung gambar:

bashCopy code
[code]
    ollama pull qwen2.5vl:7bexport OLLAMA_API_KEY="ollama-local"
[/code]

Lalu verifikasi dengan CLI infer:

bashCopy code
[code]
    openclaw infer image describe \  --file ./photo.jpg \  --model ollama/qwen2.5vl:7b \  --json
[/code]

`--model` harus berupa ref `<provider/model>` lengkap. Saat ditetapkan, `openclaw infer image describe` menjalankan model tersebut secara langsung, alih-alih melewati deskripsi karena model mendukung vision native.

Gunakan `infer image describe` saat Anda menginginkan alur penyedia pemahaman gambar OpenClaw, `agents.defaults.imageModel` yang dikonfigurasi, dan bentuk keluaran deskripsi gambar. Gunakan `infer model run --file` saat Anda menginginkan probe model multimodal mentah dengan prompt khusus dan satu atau beberapa gambar.

Untuk menjadikan Ollama model pemahaman gambar default untuk media masuk, konfigurasikan `agents.defaults.imageModel`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageModel: {        primary: "ollama/qwen2.5vl:7b",      },    },  },}
[/code]

Utamakan ref `ollama/<model>` lengkap. Jika model yang sama terdaftar di bawah `models.providers.ollama.models` dengan `input: ["text", "image"]` dan tidak ada penyedia gambar lain yang dikonfigurasi yang mengekspos ID model polos tersebut, OpenClaw juga menormalkan ref `imageModel` polos seperti `qwen2.5vl:7b` menjadi `ollama/qwen2.5vl:7b`. Jika lebih dari satu penyedia gambar yang dikonfigurasi memiliki ID polos yang sama, gunakan prefiks penyedia secara eksplisit.

Model vision lokal yang lambat dapat memerlukan timeout pemahaman gambar yang lebih panjang daripada model cloud. Model tersebut juga dapat crash atau berhenti saat Ollama mencoba mengalokasikan konteks vision penuh yang diiklankan pada perangkat keras terbatas. Tetapkan timeout kapabilitas, dan batasi `num_ctx` pada entri model saat Anda hanya memerlukan giliran deskripsi gambar normal:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        models: [          {            id: "qwen2.5vl:7b",            name: "qwen2.5vl:7b",            input: ["text", "image"],            params: { num_ctx: 2048, keep_alive: "1m" },          },        ],      },    },  },  tools: {    media: {      image: {        timeoutSeconds: 180,        models: [{ provider: "ollama", model: "qwen2.5vl:7b", timeoutSeconds: 300 }],      },    },  },}
[/code]

Timeout ini berlaku untuk pemahaman gambar masuk dan untuk tool `image` eksplisit yang dapat dipanggil agen selama giliran. `models.providers.ollama.timeoutSeconds` tingkat penyedia tetap mengontrol penjaga permintaan HTTP Ollama yang mendasarinya untuk panggilan model normal.

Verifikasi langsung tool gambar eksplisit terhadap Ollama lokal dengan:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_OLLAMA_IMAGE=1 \  pnpm test:live -- src/agents/tools/image-tool.ollama.live.test.ts
[/code]

Jika Anda mendefinisikan `models.providers.ollama.models` secara manual, tandai model vision dengan dukungan input gambar:

json5Copy code
[code]
    {  id: "qwen2.5vl:7b",  name: "qwen2.5vl:7b",  input: ["text", "image"],  contextWindow: 128000,  maxTokens: 8192,}
[/code]

OpenClaw menolak permintaan deskripsi gambar untuk model yang tidak ditandai mampu gambar. Dengan penemuan implisit, OpenClaw membaca ini dari Ollama saat `/api/show` melaporkan kapabilitas vision.

## Konfigurasi

### Basic (implicit discovery)

Jalur pengaktifan lokal-saja paling sederhana adalah melalui variabel lingkungan:

bashCopy code
[code]
    export OLLAMA_API_KEY="ollama-local"
[/code]

### Explicit (manual models)

Gunakan konfigurasi eksplisit saat Anda menginginkan penyiapan cloud ter-host, Ollama berjalan di host/port lain, Anda ingin memaksa window konteks atau daftar model tertentu, atau Anda menginginkan definisi model yang sepenuhnya manual.

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [          {            id: "kimi-k2.5:cloud",            name: "kimi-k2.5:cloud",            reasoning: false,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192          }        ]      }    }  }}
[/code]

### Custom base URL

Jika Ollama berjalan di host atau port berbeda (konfigurasi eksplisit menonaktifkan penemuan otomatis, jadi definisikan model secara manual):

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        apiKey: "ollama-local",        baseUrl: "http://ollama-host:11434", // No /v1 - use native Ollama API URL        api: "ollama", // Set explicitly to guarantee native tool-calling behavior        timeoutSeconds: 300, // Optional: give cold local models longer to connect and stream        models: [          {            id: "qwen3:32b",            name: "qwen3:32b",            params: {              keep_alive: "15m", // Optional: keep the model loaded between turns            },          },        ],      },    },  },}
[/code]

## Resep umum

Gunakan ini sebagai titik awal dan ganti ID model dengan nama persis dari `ollama list` atau `openclaw models list --provider ollama`.

Local model with auto-discovery

Gunakan ini saat Ollama berjalan di mesin yang sama dengan Gateway dan Anda ingin OpenClaw menemukan model yang terpasang secara otomatis.

bashCopy code
[code]
    ollama serveollama pull gemma4export OLLAMA_API_KEY="ollama-local"openclaw models list --provider ollamaopenclaw models set ollama/gemma4
[/code]

Jalur ini menjaga konfigurasi tetap minimal. Jangan tambahkan blok `models.providers.ollama` kecuali Anda ingin mendefinisikan model secara manual.

LAN Ollama host with manual models

Gunakan URL Ollama native untuk host LAN. Jangan tambahkan `/v1`.

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://gpu-box.local:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 300,        contextWindow: 32768,        maxTokens: 8192,        models: [          {            id: "qwen3.5:9b",            name: "qwen3.5:9b",            reasoning: true,            input: ["text"],            params: {              num_ctx: 32768,              thinking: false,              keep_alive: "15m",            },          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "ollama/qwen3.5:9b" },    },  },}
[/code]

`contextWindow` adalah anggaran konteks sisi OpenClaw. `params.num_ctx` dikirim ke Ollama untuk permintaan. Jaga keduanya tetap selaras saat perangkat keras Anda tidak dapat menjalankan konteks penuh yang diiklankan oleh model.

Ollama Cloud only

Gunakan ini saat Anda tidak menjalankan daemon lokal dan ingin model Ollama ter-host secara langsung.

bashCopy code
[code]
    export OLLAMA_API_KEY="your-ollama-api-key"
[/code]

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [          {            id: "kimi-k2.5:cloud",            name: "kimi-k2.5:cloud",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "ollama/kimi-k2.5:cloud" },    },  },}
[/code]

Cloud plus local through a signed-in daemon

Gunakan ini saat daemon Ollama lokal atau LAN sudah masuk dengan `ollama signin` dan harus melayani model lokal serta model `:cloud`.

bashCopy code
[code]
    ollama signinollama pull gemma4
[/code]

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://127.0.0.1:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 300,        models: [          { id: "gemma4", name: "gemma4", input: ["text"] },          { id: "kimi-k2.5:cloud", name: "kimi-k2.5:cloud", input: ["text", "image"] },        ],      },    },  },  agents: {    defaults: {      model: {        primary: "ollama/gemma4",        fallbacks: ["ollama/kimi-k2.5:cloud"],      },    },  },}
[/code]

Multiple Ollama hosts

Gunakan ID penyedia khusus saat Anda memiliki lebih dari satu server Ollama. Setiap penyedia mendapatkan host, model, auth, timeout, dan ref modelnya sendiri.

json5Copy code
[code]
    {  models: {    providers: {      "ollama-fast": {        baseUrl: "http://mini.local:11434",        apiKey: "ollama-local",        api: "ollama",        contextWindow: 32768,        models: [{ id: "gemma4", name: "gemma4", input: ["text"] }],      },      "ollama-large": {        baseUrl: "http://gpu-box.local:11434",        apiKey: "ollama-local",        api: "ollama",        timeoutSeconds: 420,        contextWindow: 131072,        maxTokens: 16384,        models: [{ id: "qwen3.5:27b", name: "qwen3.5:27b", input: ["text"] }],      },    },  },  agents: {    defaults: {      model: {        primary: "ollama-fast/gemma4",        fallbacks: ["ollama-large/qwen3.5:27b"],      },    },  },}
[/code]

Saat OpenClaw mengirim permintaan, prefiks penyedia aktif dihapus sehingga `ollama-large/qwen3.5:27b` mencapai Ollama sebagai `qwen3.5:27b`.

Lean local model profile

Beberapa model lokal dapat menjawab prompt sederhana tetapi kesulitan dengan seluruh permukaan tool agen. Mulailah dengan membatasi tool dan konteks sebelum mengubah pengaturan runtime global.

json5Copy code
[code]
    {  agents: {    defaults: {      experimental: {        localModelLean: true,      },      model: { primary: "ollama/gemma4" },    },  },  models: {    providers: {      ollama: {        baseUrl: "http://127.0.0.1:11434",        apiKey: "ollama-local",        api: "ollama",        contextWindow: 32768,        models: [          {            id: "gemma4",            name: "gemma4",            input: ["text"],            params: { num_ctx: 32768 },            compat: { supportsTools: false },          },        ],      },    },  },}
[/code]

Gunakan `compat.supportsTools: false` hanya ketika model atau server secara andal gagal pada skema alat. Ini menukar kapabilitas agen dengan stabilitas. `localModelLean` menghapus alat peramban, cron, dan pesan dari permukaan agen, tetapi tidak mengubah konteks runtime atau mode berpikir Ollama. Pasangkan dengan `params.num_ctx` eksplisit dan `params.thinking: false` untuk model berpikir kecil bergaya Qwen yang berulang atau menghabiskan anggaran responsnya untuk penalaran tersembunyi.

### Pemilihan model

Setelah dikonfigurasi, semua model Ollama Anda tersedia:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "ollama/gpt-oss:20b",        fallbacks: ["ollama/llama3.3", "ollama/qwen2.5-coder:32b"],      },    },  },}
[/code]

ID penyedia Ollama kustom juga didukung. Ketika sebuah referensi model menggunakan prefiks penyedia aktif, seperti `ollama-spark/qwen3:32b`, OpenClaw hanya menghapus prefiks tersebut sebelum memanggil Ollama sehingga server menerima `qwen3:32b`.

Untuk model lokal yang lambat, utamakan penyetelan permintaan dalam cakupan penyedia sebelum menaikkan timeout runtime seluruh agen:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        timeoutSeconds: 300,        models: [          {            id: "gemma4:26b",            name: "gemma4:26b",            params: { keep_alive: "15m" },          },        ],      },    },  },}
[/code]

`timeoutSeconds` berlaku untuk permintaan HTTP model, termasuk penyiapan koneksi, header, streaming isi, dan total pembatalan guarded-fetch. `params.keep_alive` diteruskan ke Ollama sebagai `keep_alive` tingkat atas pada permintaan native `/api/chat`; atur per model ketika waktu muat giliran pertama menjadi hambatan.

### Verifikasi cepat

bashCopy code
[code]
    # Ollama daemon visible to this machinecurl http://127.0.0.1:11434/api/tags # OpenClaw catalog and selected modelopenclaw models list --provider ollamaopenclaw models status # Direct model smokeopenclaw infer model run \  --model ollama/gemma4 \  --prompt "Reply with exactly: ok"
[/code]

Untuk host jarak jauh, ganti `127.0.0.1` dengan host yang digunakan dalam `baseUrl`. Jika `curl` berfungsi tetapi OpenClaw tidak, periksa apakah Gateway berjalan di mesin, container, atau akun layanan yang berbeda.

## Ollama Web Search

OpenClaw mendukung **Ollama Web Search** sebagai penyedia `web_search` bawaan.

Properti | Detail  
---|---  
Host | Menggunakan host Ollama yang Anda konfigurasi (`models.providers.ollama.baseUrl` jika diatur, jika tidak `http://127.0.0.1:11434`); `https://ollama.com` menggunakan API hosted secara langsung  
Auth | Tanpa kunci untuk host Ollama lokal yang sudah masuk; `OLLAMA_API_KEY` atau auth penyedia yang dikonfigurasi untuk pencarian langsung `https://ollama.com` atau host yang dilindungi auth  
Persyaratan | Host lokal/self-hosted harus berjalan dan masuk dengan `ollama signin`; pencarian hosted langsung memerlukan `baseUrl: "https://ollama.com"` plus kunci API Ollama asli  
  
Pilih **Ollama Web Search** selama `openclaw onboard` atau `openclaw configure --section web`, atau atur:

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

Untuk pencarian hosted langsung melalui Ollama Cloud:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [{ id: "kimi-k2.5:cloud", name: "kimi-k2.5:cloud", input: ["text"] }],      },    },  },  tools: {    web: {      search: { provider: "ollama" },    },  },}
[/code]

Untuk daemon lokal yang sudah masuk, OpenClaw menggunakan proxy `/api/experimental/web_search` milik daemon. Untuk `https://ollama.com`, OpenClaw memanggil endpoint hosted `/api/web_search` secara langsung.

## Konfigurasi lanjutan

Legacy OpenAI-compatible mode

Jika Anda perlu menggunakan endpoint kompatibel OpenAI sebagai gantinya (misalnya, di balik proxy yang hanya mendukung format OpenAI), atur `api: "openai-completions"` secara eksplisit:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434/v1",        api: "openai-completions",        injectNumCtxForOpenAICompat: true, // default: true        apiKey: "ollama-local",        models: [...]      }    }  }}
[/code]

Mode ini mungkin tidak mendukung streaming dan pemanggilan alat secara bersamaan. Anda mungkin perlu menonaktifkan streaming dengan `params: { streaming: false }` dalam konfigurasi model.

Ketika `api: "openai-completions"` digunakan dengan Ollama, OpenClaw menyuntikkan `options.num_ctx` secara default sehingga Ollama tidak diam-diam kembali ke jendela konteks 4096. Jika proxy/upstream Anda menolak kolom `options` yang tidak dikenal, nonaktifkan perilaku ini:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434/v1",        api: "openai-completions",        injectNumCtxForOpenAICompat: false,        apiKey: "ollama-local",        models: [...]      }    }  }}
[/code]

Context windows

Untuk model yang ditemukan otomatis, OpenClaw menggunakan jendela konteks yang dilaporkan oleh Ollama jika tersedia, termasuk nilai `PARAMETER num_ctx` yang lebih besar dari Modelfile kustom. Jika tidak, OpenClaw kembali ke jendela konteks default Ollama yang digunakan oleh OpenClaw.

Anda dapat mengatur default `contextWindow`, `contextTokens`, dan `maxTokens` tingkat penyedia untuk setiap model di bawah penyedia Ollama tersebut, lalu menimpanya per model saat diperlukan. `contextWindow` adalah anggaran prompt dan Compaction OpenClaw. Permintaan native Ollama membiarkan `options.num_ctx` tidak diatur kecuali Anda secara eksplisit mengonfigurasi `params.num_ctx`, sehingga Ollama dapat menerapkan default berdasarkan modelnya sendiri, `OLLAMA_CONTEXT_LENGTH`, atau VRAM. Untuk membatasi atau memaksa konteks runtime per permintaan Ollama tanpa membangun ulang Modelfile, atur `params.num_ctx`; nilai tidak valid, nol, negatif, dan non-finite diabaikan. Adapter Ollama kompatibel OpenAI tetap menyuntikkan `options.num_ctx` secara default dari `params.num_ctx` atau `contextWindow` yang dikonfigurasi; nonaktifkan dengan `injectNumCtxForOpenAICompat: false` jika upstream Anda menolak `options`.

Entri model native Ollama juga menerima opsi runtime umum Ollama di bawah `params`, termasuk `temperature`, `top_p`, `top_k`, `min_p`, `num_predict`, `stop`, `repeat_penalty`, `num_batch`, `num_thread`, dan `use_mmap`. OpenClaw hanya meneruskan kunci permintaan Ollama, sehingga parameter runtime OpenClaw seperti `streaming` tidak bocor ke Ollama. Gunakan `params.think` atau `params.thinking` untuk mengirim `think` Ollama tingkat atas; `false` menonaktifkan berpikir tingkat API untuk model berpikir bergaya Qwen.

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        contextWindow: 32768,        models: [          {            id: "llama3.3",            contextWindow: 131072,            maxTokens: 65536,            params: {              num_ctx: 32768,              temperature: 0.7,              top_p: 0.9,              thinking: false,            },          }        ]      }    }  }}
[/code]

`agents.defaults.models["ollama/<model>"].params.num_ctx` per model juga berfungsi. Jika keduanya dikonfigurasi, entri model penyedia eksplisit menang atas default agen.

Thinking control

Untuk model native Ollama, OpenClaw meneruskan kontrol berpikir sesuai yang diharapkan Ollama: `think` tingkat atas, bukan `options.think`. Model yang ditemukan otomatis dengan respons `/api/show` yang menyertakan kapabilitas `thinking` mengekspos `/think low`, `/think medium`, `/think high`, dan `/think max`; model non-berpikir hanya mengekspos `/think off`.

bashCopy code
[code]
    openclaw agent --model ollama/gemma4 --thinking offopenclaw agent --model ollama/gemma4 --thinking low
[/code]

Anda juga dapat mengatur default model:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "ollama/gemma4": {          thinking: "low",        },      },    },  },}
[/code]

`params.think` atau `params.thinking` per model dapat menonaktifkan atau memaksa berpikir API Ollama untuk model tertentu yang dikonfigurasi. OpenClaw mempertahankan parameter model eksplisit tersebut ketika proses aktif hanya memiliki default implisit `off`; perintah runtime non-off seperti `/think medium` tetap menimpa proses aktif.

Reasoning models

OpenClaw memperlakukan model dengan nama seperti `deepseek-r1`, `reasoning`, atau `think` sebagai berkemampuan penalaran secara default.

bashCopy code
[code]
    ollama pull deepseek-r1:32b
[/code]

Tidak diperlukan konfigurasi tambahan. OpenClaw menandainya secara otomatis.

Model costs

Ollama gratis dan berjalan secara lokal, sehingga semua biaya model diatur ke $0. Ini berlaku untuk model yang ditemukan otomatis maupun yang didefinisikan manual.

Memory embeddings

Plugin Ollama bawaan mendaftarkan penyedia embedding memori untuk [pencarian memori](</id/concepts/memory>). Ini menggunakan URL dasar Ollama dan kunci API yang dikonfigurasi, memanggil endpoint `/api/embed` Ollama saat ini, dan membatch beberapa potongan memori ke dalam satu permintaan `input` jika memungkinkan.

Properti | Nilai  
---|---  
Model default | `nomic-embed-text`  
Auto-pull | Ya — model embedding ditarik secara otomatis jika belum ada secara lokal  
  
Embedding waktu kueri menggunakan prefiks retrieval untuk model yang memerlukan atau merekomendasikannya, termasuk `nomic-embed-text`, `qwen3-embedding`, dan `mxbai-embed-large`. Batch dokumen memori tetap mentah sehingga indeks yang ada tidak memerlukan migrasi format.

Untuk memilih Ollama sebagai penyedia embedding pencarian memori:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "ollama",        remote: {          // Default for Ollama. Raise on larger hosts if reindexing is too slow.          nonBatchConcurrency: 1,        },      },    },  },}
[/code]

Untuk host embedding jarak jauh, pertahankan auth dalam cakupan host tersebut:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "ollama",        model: "nomic-embed-text",        remote: {          baseUrl: "http://gpu-box.local:11434",          apiKey: "ollama-local",          nonBatchConcurrency: 2,        },      },    },  },}
[/code]

Konfigurasi streaming

Integrasi Ollama OpenClaw menggunakan **API Ollama native** (`/api/chat`) secara default, yang sepenuhnya mendukung streaming dan pemanggilan alat secara bersamaan. Tidak diperlukan konfigurasi khusus.

Untuk permintaan `/api/chat` native, OpenClaw juga meneruskan kontrol penalaran langsung ke Ollama: `/think off` dan `openclaw agent --thinking off` mengirim `think: false` tingkat atas kecuali nilai model eksplisit `params.think`/`params.thinking` dikonfigurasi, sementara `/think low|medium|high` mengirim string upaya `think` tingkat atas yang sesuai. `/think max` dipetakan ke upaya native tertinggi Ollama, `think: "high"`.

## Pemecahan Masalah

Loop crash WSL2 (reboot berulang)

Pada WSL2 dengan NVIDIA/CUDA, installer Linux resmi Ollama membuat unit systemd `ollama.service` dengan `Restart=always`. Jika layanan tersebut dimulai otomatis dan memuat model berbasis GPU saat boot WSL2, Ollama dapat menahan memori host saat model dimuat. Reklaim memori Hyper-V tidak selalu dapat mereklamasi halaman yang tertahan tersebut, sehingga Windows dapat menghentikan VM WSL2, systemd memulai Ollama lagi, dan loop berulang.

Bukti umum:

  * reboot atau penghentian WSL2 berulang dari sisi Windows
  * CPU tinggi di `app.slice` atau `ollama.service` sesaat setelah WSL2 dimulai
  * SIGTERM dari systemd, bukan peristiwa OOM-killer Linux


OpenClaw mencatat peringatan startup ketika mendeteksi WSL2, `ollama.service` diaktifkan dengan `Restart=always`, dan marker CUDA terlihat.

Mitigasi:

bashCopy code
[code]
    sudo systemctl disable ollama
[/code]

Tambahkan ini ke `%USERPROFILE%\.wslconfig` di sisi Windows, lalu jalankan `wsl --shutdown`:

iniCopy code
[code]
    [experimental]autoMemoryReclaim=disabled
[/code]

Tetapkan keep-alive yang lebih pendek di lingkungan layanan Ollama, atau mulai Ollama secara manual hanya saat Anda membutuhkannya:

bashCopy code
[code]
    export OLLAMA_KEEP_ALIVE=5mollama serve
[/code]

Lihat [ollama/ollama#11317](<https://github.com/ollama/ollama/issues/11317>).

Ollama tidak terdeteksi

Pastikan Ollama berjalan dan Anda telah menetapkan `OLLAMA_API_KEY` (atau profil auth), serta Anda **tidak** mendefinisikan entri `models.providers.ollama` eksplisit:

bashCopy code
[code]
    ollama serve
[/code]

Verifikasi bahwa API dapat diakses:

bashCopy code
[code]
    curl http://localhost:11434/api/tags
[/code]

Tidak ada model yang tersedia

Jika model Anda tidak tercantum, tarik model secara lokal atau definisikan secara eksplisit di `models.providers.ollama`.

bashCopy code
[code]
    ollama list  # See what's installedollama pull gemma4ollama pull gpt-oss:20bollama pull llama3.3     # Or another model
[/code]

Koneksi ditolak

Periksa bahwa Ollama berjalan pada port yang benar:

bashCopy code
[code]
    # Check if Ollama is runningps aux | grep ollama # Or restart Ollamaollama serve
[/code]

Host jarak jauh berfungsi dengan curl tetapi tidak dengan OpenClaw

Verifikasi dari mesin dan runtime yang sama dengan yang menjalankan Gateway:

bashCopy code
[code]
    openclaw gateway status --deepcurl http://ollama-host:11434/api/tags
[/code]

Penyebab umum:

  * `baseUrl` mengarah ke `localhost`, tetapi Gateway berjalan di Docker atau pada host lain.
  * URL menggunakan `/v1`, yang memilih perilaku kompatibel OpenAI alih-alih Ollama native.
  * Host jarak jauh memerlukan perubahan firewall atau binding LAN di sisi Ollama.
  * Model tersedia di daemon laptop Anda tetapi tidak di daemon jarak jauh.

Model menghasilkan JSON alat sebagai teks

Ini biasanya berarti provider menggunakan mode kompatibel OpenAI atau model tidak dapat menangani skema alat.

Utamakan mode Ollama native:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",        api: "ollama",      },    },  },}
[/code]

Jika model lokal kecil masih gagal pada skema alat, tetapkan `compat.supportsTools: false` pada entri model tersebut dan uji ulang.

Kimi atau GLM mengembalikan simbol kacau

Respons Kimi/GLM yang di-hosting yang panjang dan berupa rangkaian simbol nonlinguistik diperlakukan sebagai output provider yang gagal, bukan sebagai jawaban asisten yang berhasil. Ini memungkinkan retry, fallback, atau penanganan kesalahan normal mengambil alih tanpa menyimpan teks rusak tersebut ke dalam sesi.

Jika ini terjadi berulang kali, ambil nama model mentah, file sesi saat ini, dan apakah proses menggunakan `Cloud + Local` atau `Cloud only`, lalu coba sesi baru dan model fallback:

bashCopy code
[code]
    openclaw infer model run --model ollama/kimi-k2.5:cloud --prompt "Reply with exactly: ok" --jsonopenclaw models set ollama/gemma4
[/code]

Model lokal cold timeout

Model lokal besar dapat memerlukan pemuatan pertama yang lama sebelum streaming dimulai. Batasi timeout hanya pada provider Ollama, dan secara opsional minta Ollama menjaga model tetap dimuat antar giliran:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        timeoutSeconds: 300,        models: [          {            id: "gemma4:26b",            name: "gemma4:26b",            params: { keep_alive: "15m" },          },        ],      },    },  },}
[/code]

Jika host itu sendiri lambat menerima koneksi, `timeoutSeconds` juga memperpanjang timeout koneksi Undici yang dijaga untuk provider ini.

Model konteks besar terlalu lambat atau kehabisan memori

Banyak model Ollama mengiklankan konteks yang lebih besar daripada yang dapat dijalankan perangkat keras Anda dengan nyaman. Ollama native menggunakan default konteks runtime Ollama sendiri kecuali Anda menetapkan `params.num_ctx`. Batasi anggaran OpenClaw dan konteks permintaan Ollama ketika Anda menginginkan latensi token pertama yang dapat diprediksi:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        contextWindow: 32768,        maxTokens: 8192,        models: [          {            id: "qwen3.5:9b",            name: "qwen3.5:9b",            params: { num_ctx: 32768, thinking: false },          },        ],      },    },  },}
[/code]

Turunkan `contextWindow` terlebih dahulu jika OpenClaw mengirim terlalu banyak prompt. Turunkan `params.num_ctx` jika Ollama memuat konteks runtime yang terlalu besar untuk mesin. Turunkan `maxTokens` jika generasi berjalan terlalu lama.

## Terkait

[**Provider model** Ikhtisar semua provider, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Pemilihan model** Cara memilih dan mengonfigurasi model. ](</id/concepts/models>) [**Pencarian Web Ollama** Detail lengkap penyiapan dan perilaku untuk pencarian web berbasis Ollama. ](</id/tools/ollama-search>) [**Konfigurasi** Referensi konfigurasi lengkap. ](</id/gateway/configuration>)

Was this useful?YesNo