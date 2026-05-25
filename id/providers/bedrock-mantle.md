---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/id/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw menyertakan provider **Amazon Bedrock Mantle** bawaan yang terhubung ke endpoint Mantle yang kompatibel dengan OpenAI. Mantle meng-host model sumber terbuka dan pihak ketiga (GPT-OSS, Qwen, Kimi, GLM, dan sejenisnya) melalui permukaan standar `/v1/chat/completions` yang didukung oleh infrastruktur Bedrock.

Properti | Nilai  
---|---  
ID Provider | `amazon-bedrock-mantle`  
API | `openai-completions` (kompatibel dengan OpenAI) atau `anthropic-messages` (rute Anthropic Messages)  
Autentikasi | `AWS_BEARER_TOKEN_BEDROCK` eksplisit atau pembuatan bearer token dari rantai kredensial IAM  
Wilayah default | `us-east-1` (timpa dengan `AWS_REGION` atau `AWS_DEFAULT_REGION`)  
  
## Memulai

Pilih metode autentikasi yang Anda inginkan dan ikuti langkah-langkah penyiapannya.

### Explicit bearer token

**Paling cocok untuk:** lingkungan yang sudah memiliki bearer token Mantle.

* ### Set the bearer token on the gateway host

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

Secara opsional, tetapkan wilayah (default-nya `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

Model yang ditemukan muncul di bawah provider `amazon-bedrock-mantle`. Tidak ada konfigurasi tambahan yang diperlukan kecuali Anda ingin menimpa default.

### IAM credentials

**Paling cocok untuk:** menggunakan kredensial yang kompatibel dengan AWS SDK (konfigurasi bersama, SSO, identitas web, peran instance atau tugas).

* ### Configure AWS credentials on the gateway host

Sumber autentikasi apa pun yang kompatibel dengan AWS SDK dapat digunakan:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw membuat bearer token Mantle dari rantai kredensial secara otomatis.

## Penemuan model otomatis

Ketika `AWS_BEARER_TOKEN_BEDROCK` ditetapkan, OpenClaw menggunakannya secara langsung. Jika tidak, OpenClaw mencoba membuat bearer token Mantle dari rantai kredensial default AWS. Kemudian OpenClaw menemukan model Mantle yang tersedia dengan menanyakan endpoint `/v1/models` wilayah tersebut.

Perilaku | Detail  
---|---  
Cache penemuan | Hasil disimpan dalam cache selama 1 jam  
Penyegaran token IAM | Setiap jam  
  
Untuk mempertahankan Plugin Mantle tetap aktif tetapi menekan penemuan otomatis dan pembuatan bearer token IAM, nonaktifkan toggle penemuan milik Plugin:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Wilayah yang didukung

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Konfigurasi manual

Jika Anda lebih suka konfigurasi eksplisit daripada penemuan otomatis:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Konfigurasi lanjutan

Reasoning support

Dukungan penalaran disimpulkan dari ID model yang memuat pola seperti `thinking`, `reasoner`, atau `gpt-oss-120b`. OpenClaw menetapkan `reasoning: true` secara otomatis untuk model yang cocok selama penemuan.

Endpoint unavailability

Jika endpoint Mantle tidak tersedia atau tidak mengembalikan model, provider dilewati secara diam-diam. OpenClaw tidak menghasilkan error; provider lain yang dikonfigurasi tetap berfungsi normal.

Claude Opus 4.7 via the Anthropic Messages route

Mantle juga mengekspos rute Anthropic Messages yang membawa model Claude melalui jalur streaming yang diautentikasi dengan bearer token yang sama. Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) dapat dipanggil melalui rute ini dengan streaming milik provider, sehingga bearer token AWS tidak diperlakukan seperti kunci API Anthropic.

Ketika Anda menetapkan model Anthropic Messages pada provider Mantle, OpenClaw menggunakan permukaan API `anthropic-messages`, bukan `openai-completions`, untuk model tersebut. Autentikasi tetap berasal dari `AWS_BEARER_TOKEN_BEDROCK` (atau bearer token IAM yang diterbitkan).

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Relationship to Amazon Bedrock provider

Bedrock Mantle adalah provider terpisah dari provider standar [Amazon Bedrock](</id/providers/bedrock>). Mantle menggunakan permukaan `/v1` yang kompatibel dengan OpenAI, sementara provider standar Bedrock menggunakan API Bedrock native.

Kedua provider berbagi kredensial `AWS_BEARER_TOKEN_BEDROCK` yang sama ketika tersedia.

## Terkait

[**Amazon Bedrock** Provider Bedrock native untuk Anthropic Claude, Titan, dan model lainnya. ](</id/providers/bedrock>) [**Model selection** Memilih provider, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**OAuth and auth** Detail autentikasi dan aturan penggunaan ulang kredensial. ](</id/gateway/authentication>) [**Troubleshooting** Masalah umum dan cara mengatasinya. ](</id/help/troubleshooting>)

Was this useful?YesNo