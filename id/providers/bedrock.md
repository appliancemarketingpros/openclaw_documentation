---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/id/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw dapat menggunakan model **Amazon Bedrock** melalui penyedia streaming **Bedrock Converse** dari pi-ai. Autentikasi Bedrock menggunakan **rantai kredensial default AWS SDK** , bukan kunci API.

Properti | Nilai  
---|---  
Penyedia | `amazon-bedrock`  
API | `bedrock-converse-stream`  
Autentikasi | Kredensial AWS (env vars, konfigurasi bersama, atau peran instance)  
Wilayah | `AWS_REGION` atau `AWS_DEFAULT_REGION` (default: `us-east-1`)  
  
## Memulai

Pilih metode autentikasi yang Anda inginkan dan ikuti langkah-langkah penyiapannya.

### Access keys / env vars

**Paling cocok untuk:** mesin developer, CI, atau host tempat Anda mengelola kredensial AWS secara langsung.

* ### Set AWS credentials on the gateway host

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### Add a Bedrock provider and model to your config

Tidak diperlukan `apiKey`. Konfigurasikan penyedia dengan `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list
[/code]

### EC2 instance roles (IMDS)

**Paling cocok untuk:** instance EC2 dengan peran IAM terpasang, menggunakan layanan metadata instance untuk autentikasi.

* ### Enable discovery explicitly

Saat menggunakan IMDS, OpenClaw tidak dapat mendeteksi autentikasi AWS hanya dari penanda env, jadi Anda harus ikut serta:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### Optionally add an env marker for auto mode

Jika Anda juga ingin jalur deteksi otomatis penanda env berfungsi (misalnya, untuk permukaan `openclaw status`):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

Anda **tidak** memerlukan kunci API palsu.

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

## Penemuan model otomatis

OpenClaw dapat secara otomatis menemukan model Bedrock yang mendukung **streaming** dan **output teks**. Penemuan menggunakan `bedrock:ListFoundationModels` dan `bedrock:ListInferenceProfiles`, dan hasilnya disimpan dalam cache (default: 1 jam).

Cara penyedia implisit diaktifkan:

  * Jika `plugins.entries.amazon-bedrock.config.discovery.enabled` bernilai `true`, OpenClaw akan mencoba penemuan meskipun tidak ada penanda env AWS.
  * Jika `plugins.entries.amazon-bedrock.config.discovery.enabled` tidak disetel, OpenClaw hanya otomatis menambahkan penyedia Bedrock implisit saat melihat salah satu penanda autentikasi AWS ini: `AWS_BEARER_TOKEN_BEDROCK`, `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, atau `AWS_PROFILE`.
  * Jalur autentikasi runtime Bedrock yang sebenarnya tetap menggunakan rantai default AWS SDK, sehingga konfigurasi bersama, SSO, dan autentikasi peran instance IMDS dapat berfungsi meskipun penemuan memerlukan `enabled: true` untuk ikut serta.


Discovery config options

Opsi konfigurasi berada di bawah `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

Opsi | Default | Deskripsi  
---|---|---  
`enabled` | otomatis | Dalam mode otomatis, OpenClaw hanya mengaktifkan penyedia Bedrock implisit saat melihat penanda env AWS yang didukung. Setel ke `true` untuk memaksa penemuan.  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | Wilayah AWS yang digunakan untuk panggilan API penemuan.  
`providerFilter` | (semua) | Mencocokkan nama penyedia Bedrock (misalnya `anthropic`, `amazon`).  
`refreshInterval` | `3600` | Durasi cache dalam detik. Setel ke `0` untuk menonaktifkan caching.  
`defaultContextWindow` | `32000` | Jendela konteks yang digunakan untuk model yang ditemukan (timpa jika Anda mengetahui batas model Anda).  
`defaultMaxTokens` | `4096` | Token output maksimum yang digunakan untuk model yang ditemukan (timpa jika Anda mengetahui batas model Anda).  
  
## Penyiapan cepat (jalur AWS)

Panduan ini membuat peran IAM, memasang izin Bedrock, mengaitkan profil instance, dan mengaktifkan penemuan OpenClaw pada host EC2.

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## Konfigurasi lanjutan

Inference profiles

OpenClaw menemukan **profil inferensi regional dan global** bersama model foundation. Saat profil dipetakan ke model foundation yang diketahui, profil tersebut mewarisi kemampuan model itu (jendela konteks, token maksimum, penalaran, vision) dan wilayah permintaan Bedrock yang benar disuntikkan secara otomatis. Ini berarti profil Claude lintas wilayah berfungsi tanpa timpa penyedia manual.

ID profil inferensi terlihat seperti `us.anthropic.claude-opus-4-6-v1:0` (regional) atau `anthropic.claude-opus-4-6-v1:0` (global). Jika model pendukung sudah ada dalam hasil penemuan, profil mewarisi set kemampuan penuhnya; jika tidak, default aman diterapkan.

Tidak diperlukan konfigurasi tambahan. Selama penemuan diaktifkan dan prinsipal IAM memiliki `bedrock:ListInferenceProfiles`, profil muncul bersama model foundation di `openclaw models list`.

Service tier

Beberapa model Bedrock mendukung parameter `service_tier` untuk mengoptimalkan biaya atau latensi. Tingkat berikut tersedia:

Tingkat | Deskripsi  
---|---  
`default` | Tingkat Bedrock standar  
`flex` | Pemrosesan berdiskon untuk workload yang dapat menoleransi latensi lebih lama  
`priority` | Pemrosesan diprioritaskan untuk workload sensitif latensi  
`reserved` | Kapasitas terpesan untuk workload kondisi stabil  
  
Setel `serviceTier` (atau `service_tier`) melalui `agents.defaults.params` untuk permintaan model Bedrock, atau per model di `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

Nilai yang valid adalah `default`, `flex`, `priority`, dan `reserved`. Tidak semua model mendukung semua tingkat — jika tingkat yang tidak didukung diminta, Bedrock akan mengembalikan galat validasi. Catatan: pesan galatnya agak menyesatkan; pesan tersebut mungkin mengatakan "The provided model identifier is invalid" alih-alih menunjukkan tingkat layanan yang tidak didukung. Jika Anda melihat galat ini, periksa apakah model mendukung tingkat yang diminta.

Claude Opus 4.7 temperature

Bedrock menolak parameter `temperature` untuk Claude Opus 4.7. OpenClaw menghilangkan `temperature` secara otomatis untuk ref Bedrock Opus 4.7 apa pun, termasuk ID model foundation, profil inferensi bernama, profil inferensi aplikasi yang model dasarnya terselesaikan ke Opus 4.7 melalui `bedrock:GetInferenceProfile`, dan varian bertitik `opus-4.7` dengan awalan wilayah opsional (`us.`, `eu.`, `ap.`, `apac.`, `au.`, `jp.`, `global.`). Tidak diperlukan knob konfigurasi, dan penghilangan ini berlaku untuk objek opsi permintaan maupun bidang payload `inferenceConfig`.

Guardrails

Anda dapat menerapkan [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) ke semua pemanggilan model Bedrock dengan menambahkan objek `guardrail` ke konfigurasi plugin `amazon-bedrock`. Guardrails memungkinkan Anda menerapkan pemfilteran konten, penolakan topik, filter kata, filter informasi sensitif, dan pemeriksaan grounding kontekstual.

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

Opsi | Wajib | Deskripsi  
---|---|---  
`guardrailIdentifier` | Ya | ID guardrail (mis. `abc123`) atau ARN lengkap (mis. `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`).  
`guardrailVersion` | Ya | Nomor versi yang dipublikasikan, atau `"DRAFT"` untuk draf kerja.  
`streamProcessingMode` | Tidak | `"sync"` atau `"async"` untuk evaluasi guardrail selama streaming. Jika dihilangkan, Bedrock menggunakan nilai defaultnya.  
`trace` | Tidak | `"enabled"` atau `"enabled_full"` untuk debugging; hilangkan atau atur ke `"disabled"` untuk produksi.  
Embedding untuk pencarian memori

Bedrock juga dapat berfungsi sebagai penyedia embedding untuk [pencarian memori](</id/concepts/memory-search>). Ini dikonfigurasi terpisah dari penyedia inferensi -- atur `agents.defaults.memorySearch.provider` ke `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Embedding Bedrock menggunakan rantai kredensial AWS SDK yang sama dengan inferensi (peran instance, SSO, kunci akses, konfigurasi bersama, dan identitas web). Tidak diperlukan kunci API. Ketika `provider` adalah `"auto"`, Bedrock terdeteksi otomatis jika rantai kredensial tersebut berhasil di-resolve.

Model embedding yang didukung mencakup Amazon Titan Embed (v1, v2), Amazon Nova Embed, Cohere Embed (v3, v4), dan TwelveLabs Marengo. Lihat [Referensi konfigurasi memori -- Bedrock](</id/reference/memory-config#bedrock-embedding-config>) untuk daftar model lengkap dan opsi dimensi.

Catatan dan peringatan

  * Bedrock memerlukan **akses model** yang diaktifkan di akun/wilayah AWS Anda.
  * Penemuan otomatis memerlukan izin `bedrock:ListFoundationModels` dan `bedrock:ListInferenceProfiles`.
  * Jika Anda mengandalkan mode otomatis, tetapkan salah satu penanda env autentikasi AWS yang didukung pada host gateway. Jika Anda lebih memilih autentikasi IMDS/konfigurasi bersama tanpa penanda env, atur `plugins.entries.amazon-bedrock.config.discovery.enabled: true`.
  * OpenClaw menampilkan sumber kredensial dalam urutan ini: `AWS_BEARER_TOKEN_BEDROCK`, lalu `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, lalu `AWS_PROFILE`, lalu rantai AWS SDK default.
  * Dukungan penalaran bergantung pada model; periksa kartu model Bedrock untuk kemampuan saat ini.
  * Jika Anda lebih memilih alur kunci terkelola, Anda juga dapat menempatkan proxy yang kompatibel dengan OpenAI di depan Bedrock dan mengonfigurasikannya sebagai penyedia OpenAI.


## Terkait

[**Pemilihan model** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Pencarian memori** Embedding Bedrock untuk konfigurasi pencarian memori. ](</id/concepts/memory-search>) [**Referensi konfigurasi memori** Daftar lengkap model embedding Bedrock dan opsi dimensi. ](</id/reference/memory-config#bedrock-embedding-config>) [**Pemecahan masalah** Pemecahan masalah umum dan FAQ. ](</id/help/troubleshooting>)

Was this useful?YesNo