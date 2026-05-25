---
title: Konfigurasi
source_url: https://docs.openclaw.ai/id/cli/config
scraped_at: 2026-05-25
---

Pembantu konfigurasi untuk edit non-interaktif di `openclaw.json`: get/set/patch/unset/file/schema/validate nilai berdasarkan path dan mencetak file konfigurasi aktif. Jalankan tanpa subperintah untuk membuka wizard konfigurasi (sama seperti `openclaw configure`).

## Opsi root

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> Filter bagian penyiapan terpandu yang dapat diulang saat Anda menjalankan `openclaw config` tanpa subperintah.

Bagian terpandu yang didukung: `workspace`, `model`, `web`, `gateway`, `daemon`, `channels`, `plugins`, `skills`, `health`.

## Contoh

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

Cetak skema JSON yang dihasilkan untuk `openclaw.json` ke stdout sebagai JSON.

Yang disertakan

  * Skema konfigurasi root saat ini, ditambah field string `$schema` root untuk tooling editor.
  * Metadata dokumentasi field `title` dan `description` yang digunakan oleh Control UI.
  * Node objek bersarang, wildcard (`*`), dan item array (`[]`) mewarisi metadata `title` / `description` yang sama saat dokumentasi field yang cocok ada.
  * Cabang `anyOf` / `oneOf` / `allOf` juga mewarisi metadata dokumentasi yang sama saat dokumentasi field yang cocok ada.
  * Metadata skema Plugin + channel live secara best-effort saat manifes runtime dapat dimuat.
  * Skema fallback yang bersih bahkan saat konfigurasi saat ini tidak valid.

RPC runtime terkait

`config.schema.lookup` mengembalikan satu path konfigurasi ternormalisasi dengan node skema dangkal (`title`, `description`, `type`, `enum`, `const`, batas umum), metadata petunjuk UI yang cocok, dan ringkasan child langsung. Gunakan ini untuk penelusuran mendalam berbasis path di Control UI atau klien khusus.

bashCopy code
[code]
    openclaw config schema
[/code]

Pipe ke file saat Anda ingin memeriksa atau memvalidasinya dengan alat lain:

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### Path

Path menggunakan notasi titik atau kurung siku:

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

Gunakan indeks daftar agent untuk menargetkan agent tertentu:

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## Nilai

Nilai diparse sebagai JSON5 jika memungkinkan; jika tidak, nilai diperlakukan sebagai string. Gunakan `--strict-json` untuk mewajibkan parsing JSON5. `--json` tetap didukung sebagai alias lama.

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json` mencetak nilai mentah sebagai JSON, bukan teks berformat terminal.

Gunakan `--merge` saat menambahkan entri ke map tersebut:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

Gunakan `--replace` hanya saat Anda sengaja ingin nilai yang diberikan menjadi nilai target lengkap.

## Mode `config set`

`openclaw config set` mendukung empat gaya penetapan:

### Mode nilai

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### Mode pembuat SecretRef

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Mode pembuat provider

Mode pembuat provider hanya menargetkan path `secrets.providers.<alias>`:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### Mode batch

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

Parsing batch selalu menggunakan payload batch (`--batch-json`/`--batch-file`) sebagai sumber kebenaran. `--strict-json` / `--json` tidak mengubah perilaku parsing batch.

## `config patch`

Gunakan `config patch` saat Anda ingin menempelkan atau melakukan pipe patch berbentuk konfigurasi, bukan menjalankan banyak perintah `config set` berbasis path. Input berupa objek JSON5. Objek digabungkan secara rekursif, array dan nilai skalar menggantikan nilai target, dan `null` menghapus path target.

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

Anda juga dapat melakukan pipe patch melalui stdin, yang berguna untuk skrip penyiapan jarak jauh:

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

Contoh patch:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

Gunakan `--replace-path <path>` saat satu objek atau array harus menjadi persis nilai yang diberikan, bukan dipatch secara rekursif:

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run` menjalankan pemeriksaan skema dan keterpecahan SecretRef tanpa menulis. SecretRef berbasis exec dilewati secara default selama dry-run; tambahkan `--allow-exec` saat Anda sengaja ingin dry-run menjalankan perintah provider.

Mode path/nilai JSON tetap didukung untuk SecretRef dan provider:

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## Flag pembuat provider

Target pembuat provider harus menggunakan `secrets.providers.<alias>` sebagai path.

Flag umum

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Provider env (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (dapat diulang)

Provider file (--provider-source file)

  * `--provider-path <path>` (wajib)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Provider exec (--provider-source exec)

  * `--provider-command <path>` (wajib)
  * `--provider-arg <arg>` (dapat diulang)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (dapat diulang)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (dapat diulang)
  * `--provider-trusted-dir <path>` (dapat diulang)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


Contoh provider exec yang diperkeras:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Dry run

Gunakan `--dry-run` untuk memvalidasi perubahan tanpa menulis `openclaw.json`.

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Perilaku dry-run

  * Mode pembuat: menjalankan pemeriksaan keterpecahan SecretRef untuk ref/provider yang berubah.
  * Mode JSON (`--strict-json`, `--json`, atau mode batch): menjalankan validasi skema plus pemeriksaan keterpecahan SecretRef.
  * Validasi kebijakan juga berjalan untuk surface target SecretRef yang diketahui tidak didukung.
  * Pemeriksaan kebijakan mengevaluasi konfigurasi penuh setelah perubahan, sehingga penulisan objek induk (misalnya menetapkan `hooks` sebagai objek) tidak dapat melewati validasi surface yang tidak didukung.
  * Pemeriksaan SecretRef exec dilewati secara default selama dry-run untuk menghindari efek samping perintah.
  * Gunakan `--allow-exec` dengan `--dry-run` untuk memilih ikut pemeriksaan SecretRef exec (ini dapat mengeksekusi perintah provider).
  * `--allow-exec` hanya untuk dry-run dan error jika digunakan tanpa `--dry-run`.

Field --dry-run --json

`--dry-run --json` mencetak laporan yang dapat dibaca mesin:

  * `ok`: apakah dry-run berhasil
  * `operations`: jumlah penetapan yang dievaluasi
  * `checks`: apakah pemeriksaan skema/resolvability dijalankan
  * `checks.resolvabilityComplete`: apakah pemeriksaan resolvability berjalan sampai selesai (false ketika ref exec dilewati)
  * `refsChecked`: jumlah ref yang benar-benar diselesaikan selama dry-run
  * `skippedExecRefs`: jumlah ref exec yang dilewati karena `--allow-exec` tidak ditetapkan
  * `errors`: kegagalan skema/resolvability terstruktur ketika `ok=false`


### Bentuk keluaran JSON

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### Contoh berhasil

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### Contoh gagal

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

Jika dry-run gagal

  * `config schema validation failed`: bentuk config setelah perubahan tidak valid; perbaiki jalur/nilai atau bentuk objek provider/ref.
  * `Config policy validation failed: unsupported SecretRef usage`: pindahkan kredensial itu kembali ke input teks biasa/string dan pertahankan SecretRef hanya pada permukaan yang didukung.
  * `SecretRef assignment(s) could not be resolved`: provider/ref yang direferensikan saat ini tidak dapat diselesaikan (env var hilang, pointer file tidak valid, kegagalan provider exec, atau ketidakcocokan provider/sumber).
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: dry-run melewati ref exec; jalankan ulang dengan `--allow-exec` jika Anda memerlukan validasi resolvability exec.
  * Untuk mode batch, perbaiki entri yang gagal dan jalankan ulang `--dry-run` sebelum menulis.


## Keamanan tulis

`openclaw config set` dan penulis config milik OpenClaw lainnya memvalidasi seluruh config setelah perubahan sebelum mengirimkannya ke disk. Jika payload baru gagal validasi skema atau terlihat seperti penimpaan yang destruktif, config aktif dibiarkan tetap ada dan payload yang ditolak disimpan di sampingnya sebagai `openclaw.json.rejected.*`.

Utamakan penulisan CLI untuk edit kecil:

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

Jika penulisan ditolak, periksa payload yang disimpan dan perbaiki bentuk config lengkapnya:

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

Penulisan langsung dengan editor tetap diizinkan, tetapi Gateway yang berjalan memperlakukannya sebagai tidak tepercaya sampai tervalidasi. Edit langsung yang tidak valid menggagalkan startup atau dilewati oleh hot reload; Gateway tidak menulis ulang `openclaw.json`. Jalankan `openclaw doctor --fix` untuk memperbaiki config yang berprefiks/tertimpah atau memulihkan salinan terakhir yang diketahui baik. Lihat [Pemecahan masalah Gateway](</id/gateway/troubleshooting#gateway-rejected-invalid-config>).

Pemulihan seluruh file dikhususkan untuk perbaikan doctor. Perubahan skema Plugin atau ketidaksesuaian `minHostVersion` tetap ditampilkan jelas alih-alih mengembalikan pengaturan pengguna yang tidak terkait seperti model, provider, profil auth, channel, paparan gateway, tool, memory, browser, atau config cron.

## Subperintah

  * `config file`: Cetak jalur file config aktif (diselesaikan dari `OPENCLAW_CONFIG_PATH` atau lokasi default). Jalur tersebut harus menunjuk ke file reguler, bukan symlink.


Mulai ulang gateway setelah pengeditan.

## Validasi

Validasi config saat ini terhadap skema aktif tanpa memulai gateway.

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

Setelah `openclaw config validate` berhasil, Anda dapat menggunakan TUI lokal agar agen tertanam membandingkan config aktif dengan dokumen saat Anda memvalidasi setiap perubahan dari terminal yang sama:

bashCopy code
[code]
    openclaw chat
[/code]

Lalu di dalam TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

Loop perbaikan umum:

* ### Bandingkan dengan dokumen

Minta agen membandingkan config Anda saat ini dengan halaman dokumen yang relevan dan menyarankan perbaikan terkecil.

* ### Terapkan edit tertarget

Terapkan edit tertarget dengan `openclaw config set` atau `openclaw configure`.

* ### Validasi ulang

Jalankan ulang `openclaw config validate` setelah setiap perubahan.

* ### Doctor untuk masalah runtime

Jika validasi berhasil tetapi runtime masih tidak sehat, jalankan `openclaw doctor` atau `openclaw doctor --fix` untuk bantuan migrasi dan perbaikan.

## Terkait

  * [Referensi CLI](</id/cli>)
  * [Konfigurasi](</id/gateway/configuration>)


Was this useful?YesNo