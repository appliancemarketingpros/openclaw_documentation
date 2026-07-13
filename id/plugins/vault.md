---
title: SecretRefs Vault
source_url: https://docs.openclaw.ai/id/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# SecretRef Vault

Plugin Vault bawaan memungkinkan OpenClaw me-resolve SecretRef `exec` dari HashiCorp Vault saat Gateway dimulai dan dimuat ulang. OpenClaw menyimpan referensi Vault dalam konfigurasi, mempertahankan nilai yang telah di-resolve dalam snapshot rahasia di memori, dan tidak menulis kembali kunci API yang telah di-resolve ke `openclaw.json`.

Gunakan ini jika Anda sudah menjalankan Vault atau ingin menyimpan kunci penyedia model di luar file konfigurasi OpenClaw. Untuk model runtime SecretRef, lihat [Pengelolaan rahasia](</id/gateway/secrets>).

## Sebelum memulai

Anda memerlukan:

  * OpenClaw dengan plugin `vault` bawaan yang tersedia
  * server Vault yang dapat dijangkau
  * autentikasi Vault yang dapat menghasilkan token klien dengan akses baca ke jalur rahasia yang perlu di-resolve oleh OpenClaw
  * lingkungan yang memulai Gateway harus menyertakan `VAULT_ADDR` dan salah satu dari `VAULT_TOKEN`, `OPENCLAW_VAULT_AUTH_METHOD=token_file` dengan `VAULT_TOKEN_FILE`, atau login JWT/Kubernetes yang telah dikonfigurasi


Resolver berkomunikasi dengan Vault melalui HTTP dari Node. Gateway tidak memerlukan CLI Vault untuk me-resolve SecretRef.

Aktifkan plugin bawaan sebelum menjalankan perintah `openclaw vault`:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Menyimpan kunci penyedia di Vault

OpenClaw secara default menggunakan KV v2 yang dipasang di `secret`, sesuai dengan contoh server pengembangan Vault. Untuk Vault produksi, atur `OPENCLAW_VAULT_KV_MOUNT` ke jalur pemasangan KV yang sebenarnya sebelum membuat ID SecretRef. Dengan pengaturan default OpenClaw, ID SecretRef ini:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

membaca bidang Vault berikut:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Salah satu cara untuk membuatnya dengan CLI Vault adalah:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Gunakan token klien dengan cakupan terbatas untuk OpenClaw, bukan token root. Untuk tata letak KV v2 default, kebijakan minimal bagi kunci penyedia model terlihat seperti:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Membuat Vault terlihat oleh Gateway

Untuk Gateway lokal tanpa kontainer, ekspor pengaturan Vault di shell yang sama yang memulai OpenClaw. Metode autentikasi default membaca token klien Vault dari `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Jika Vault Agent menulis file sink token, gunakan autentikasi file token:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Untuk server Vault yang ditandatangani oleh CA privat, instal CA tersebut di penyimpanan kepercayaan host dan aktifkan kepercayaan sistem Node:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Atau berikan bundel PEM secara langsung:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

Variabel-variabel ini harus tersedia saat OpenClaw dimulai. Plugin Vault meneruskannya ke proses resolver-nya.

Untuk autentikasi JWT noninteraktif, gunakan file JWT beban kerja dan peran Vault bertipe `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

File JWT harus berupa token beban kerja yang diproyeksikan, seperti token akun layanan Kubernetes dengan audiens yang diterima oleh peran Vault. Login peramban OIDC interaktif berguna bagi manusia, tetapi runtime Gateway memerlukan login JWT noninteraktif atau file token.

Untuk metode autentikasi Kubernetes milik Vault, gunakan `kubernetes`. Ini ditujukan bagi Gateway yang berjalan sebagai Pod; pemasangan default adalah `kubernetes`, dan file JWT default adalah jalur token akun layanan standar:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Atur `OPENCLAW_VAULT_AUTH_MOUNT` hanya jika Vault memasang autentikasi Kubernetes di lokasi selain `auth/kubernetes`. Atur `OPENCLAW_VAULT_JWT_FILE` hanya jika token akun layanan diproyeksikan ke jalur khusus.

Pengaturan opsional:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Periksa apa yang dapat dilihat oleh shell saat ini:

bashCopy code
[code]
    openclaw vault status
[/code]

Jika lebih dari satu penyedia rahasia berbasis Vault dikonfigurasi, pilih salah satunya berdasarkan alias:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` tidak pernah mencetak `VAULT_TOKEN`; perintah ini hanya melaporkan apakah token, file token, dan file JWT telah diatur.

## Membuat dan menerapkan rencana SecretRef

Buat rencana yang memetakan kunci API penyedia model OpenRouter ke Vault:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Terapkan dan verifikasi rencana:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Gunakan `--allow-exec` karena plugin Vault melakukan resolusi melalui penyedia SecretRef exec yang dikelola OpenClaw.

Jika Gateway belum berjalan, mulai seperti biasa setelah menerapkan rencana alih-alih menjalankan `openclaw secrets reload`.

## Mengonfigurasi lebih banyak kunci penyedia

Pintasan bawaan:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Beberapa kunci penyedia dalam satu rencana:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Penyedia bawaan tanpa pintasan, atau penyedia model kompatibel OpenAI dan khusus yang sudah dikonfigurasi, menggunakan `--provider-key`:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Setiap `--provider-key <provider=id>` menulis SecretRef ke `models.providers.<provider>.apiKey`. Untuk penyedia khusus, perintah ini tidak membuat pengaturan `baseUrl`, `api`, atau `models` milik penyedia; konfigurasikan pengaturan tersebut terlebih dahulu.

Gunakan `--target <path=id>` untuk setiap jalur target SecretRef yang diketahui:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Jalur target polos diterapkan ke `openclaw.json`. Gunakan `auth-profiles:<agentId>:<path>` untuk target `auth-profiles.json` yang sudah ada. Jalur target harus merupakan target SecretRef OpenClaw yang terdaftar. Perintah penyiapan tidak membuat rahasia bernama secara sembarang di OpenClaw; Vault tetap menjadi penyimpanan rahasia, dan OpenClaw hanya menyimpan SecretRef pada bidang konfigurasi yang didukung.

## Format ID SecretRef

ID SecretRef Vault menggunakan konvensi berikut:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Contoh:

ID SecretRef | Pembacaan Vault KV v2 default | Bidang yang dikembalikan  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Bidang Vault yang dikembalikan harus berupa string.

Untuk KV v1, atur:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

Kemudian `providers/openrouter/apiKey` membaca:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## Yang disimpan OpenClaw

Menerapkan rencana penyiapan Vault akan menyimpan penyedia yang dikelola plugin:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Bidang kredensial mengarah ke penyedia tersebut:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

Nilai yang di-resolve hanya berada dalam snapshot rahasia runtime yang aktif.

## Kontainer dan penerapan terkelola

Gateway dalam kontainer tetap menggunakan plugin dan konfigurasi SecretRef yang sama. Kontainer harus menerima:

  * `VAULT_ADDR`
  * satu sumber autentikasi: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` ditambah `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` ditambah `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE`, dan `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` ditambah `OPENCLAW_VAULT_AUTH_ROLE`; secara opsional timpa `OPENCLAW_VAULT_AUTH_MOUNT` atau `OPENCLAW_VAULT_JWT_FILE`
  * `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT`, dan `OPENCLAW_VAULT_KV_VERSION` yang bersifat opsional


Saat menggunakan Kubernetes, utamakan `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` jika Vault telah mengonfigurasi autentikasi Kubernetes untuk klaster. Gunakan `OPENCLAW_VAULT_AUTH_METHOD=jwt` hanya jika Vault dikonfigurasi untuk memperlakukan klaster sebagai penerbit JWT/OIDC generik. Kedua opsi tersebut lebih baik daripada token Vault berumur panjang dalam Secret Kubernetes. Penerapan sidecar atau injektor Vault Agent dapat menggunakan `token_file` sebagai gantinya.

Untuk penyiapan Vault multipenyewa, pertahankan perutean penyewa dalam kebijakan Vault dan konfigurasi penerapan. OpenClaw tidak memerlukan pemasangan, peran, atau jalur tetap: setiap lingkungan Gateway dapat mengatur `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE`, dan ID SecretRef-nya sendiri. Jika satu Gateway bersama harus me-resolve pengguna Vault yang berbeda secara bersamaan, gunakan penyedia exec yang dikonfigurasi secara manual dan membungkus lingkungan autentikasi yang berbeda, atau pisahkan penyewa ke beberapa lingkungan Gateway dengan lingkungan Vault terpisah.

## Terkait

  * [Pengelolaan rahasia](</id/gateway/secrets>)
  * [`openclaw secrets`](</id/cli/secrets>)
  * [Inventaris Plugin](</id/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue