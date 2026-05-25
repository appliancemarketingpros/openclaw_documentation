---
title: Yapılandırma
source_url: https://docs.openclaw.ai/tr/cli/config
scraped_at: 2026-05-25
---

`openclaw.json` içinde etkileşimsiz düzenlemeler için config yardımcıları: path üzerinden değerleri get/set/patch/unset/file/schema/validate yapar ve etkin config dosyasını yazdırır. Yapılandırma sihirbazını açmak için alt komut olmadan çalıştırın (`openclaw configure` ile aynı).

## Kök seçenekler

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> `openclaw config` komutunu alt komut olmadan çalıştırdığınızda yinelenebilir kılavuzlu kurulum bölümü filtresi.

Desteklenen kılavuzlu bölümler: `workspace`, `model`, `web`, `gateway`, `daemon`, `channels`, `plugins`, `skills`, `health`.

## Örnekler

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

`openclaw.json` için oluşturulan JSON şemasını JSON olarak stdout’a yazdırır.

What it includes

  * Geçerli kök config şeması ve düzenleyici araçları için kök `$schema` string alanı.
  * Control UI tarafından kullanılan alan `title` ve `description` dokümantasyon metaverisi.
  * İç içe object, wildcard (`*`) ve array-item (`[]`) düğümleri, eşleşen alan dokümantasyonu varsa aynı `title` / `description` metaverisini devralır.
  * `anyOf` / `oneOf` / `allOf` dalları da eşleşen alan dokümantasyonu varsa aynı dokümantasyon metaverisini devralır.
  * Runtime manifestleri yüklenebildiğinde en iyi çaba ile canlı Plugin + kanal şema metaverisi.
  * Geçerli config geçersiz olduğunda bile temiz bir fallback şeması.

Related runtime RPC

`config.schema.lookup`, sığ bir şema düğümü (`title`, `description`, `type`, `enum`, `const`, ortak sınırlar), eşleşen UI ipucu metaverisi ve doğrudan alt özetlerle normalleştirilmiş tek bir config path döndürür. Control UI veya özel istemcilerde path kapsamlı ayrıntı incelemesi için kullanın.

bashCopy code
[code]
    openclaw config schema
[/code]

Başka araçlarla incelemek veya doğrulamak istediğinizde bir dosyaya pipe edin:

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### Path’ler

Path’ler nokta veya köşeli parantez gösterimi kullanır:

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

Belirli bir agent’ı hedeflemek için agent liste indeksini kullanın:

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## Değerler

Değerler mümkün olduğunda JSON5 olarak ayrıştırılır; aksi takdirde string olarak ele alınır. JSON5 ayrıştırmasını zorunlu kılmak için `--strict-json` kullanın. `--json`, eski alias olarak desteklenmeye devam eder.

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json`, ham değeri terminal biçimli metin yerine JSON olarak yazdırır.

Bu map’lere girdi eklerken `--merge` kullanın:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

`--replace` yalnızca verilen değerin eksiksiz hedef değer olmasını bilerek istediğinizde kullanın.

## `config set` modları

`openclaw config set` dört atama stilini destekler:

### Value mode

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### SecretRef builder mode

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Provider builder mode

Provider oluşturucu modu yalnızca `secrets.providers.<alias>` path’lerini hedefler:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### Batch mode

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

Batch ayrıştırma her zaman doğruluk kaynağı olarak batch payload’ını (`--batch-json`/`--batch-file`) kullanır. `--strict-json` / `--json`, batch ayrıştırma davranışını değiştirmez.

## `config patch`

Path tabanlı çok sayıda `config set` komutu çalıştırmak yerine config biçimli bir patch yapıştırmak veya pipe etmek istediğinizde `config patch` kullanın. Girdi bir JSON5 object’tir. Object’ler özyinelemeli olarak merge edilir, array’ler ve skaler değerler hedef değerin yerini alır, `null` hedef path’i siler.

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

Uzak kurulum script’leri için kullanışlı olan stdin üzerinden de patch pipe edebilirsiniz:

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

Örnek patch:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

Bir object veya array özyinelemeli olarak patch edilmek yerine tam olarak verilen değer olmalıysa `--replace-path <path>` kullanın:

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run`, yazmadan şema ve SecretRef çözümlenebilirlik kontrollerini çalıştırır. Exec destekli SecretRef’ler dry-run sırasında varsayılan olarak atlanır; dry-run’ın provider komutlarını yürütmesini bilerek istiyorsanız `--allow-exec` ekleyin.

JSON path/değer modu hem SecretRef’ler hem provider’lar için desteklenmeye devam eder:

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## Provider oluşturucu flag’leri

Provider oluşturucu hedefleri path olarak `secrets.providers.<alias>` kullanmalıdır.

Common flags

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Env provider (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (yinelenebilir)

File provider (--provider-source file)

  * `--provider-path <path>` (zorunlu)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Exec provider (--provider-source exec)

  * `--provider-command <path>` (zorunlu)
  * `--provider-arg <arg>` (yinelenebilir)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (yinelenebilir)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (yinelenebilir)
  * `--provider-trusted-dir <path>` (yinelenebilir)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


Sertleştirilmiş exec provider örneği:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Dry run

`openclaw.json` yazmadan değişiklikleri doğrulamak için `--dry-run` kullanın.

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Dry-run behavior

  * Oluşturucu modu: değişen ref’ler/provider’lar için SecretRef çözümlenebilirlik kontrollerini çalıştırır.
  * JSON modu (`--strict-json`, `--json` veya batch modu): şema doğrulamasını ve SecretRef çözümlenebilirlik kontrollerini çalıştırır.
  * Bilinen desteklenmeyen SecretRef hedef yüzeyleri için ilke doğrulaması da çalışır.
  * İlke kontrolleri değişiklik sonrası config’in tamamını değerlendirir, bu nedenle üst object yazmaları (örneğin `hooks` değerini object olarak ayarlamak) desteklenmeyen yüzey doğrulamasını atlayamaz.
  * Exec SecretRef kontrolleri komut yan etkilerini önlemek için dry-run sırasında varsayılan olarak atlanır.
  * Exec SecretRef kontrollerine dahil olmak için `--dry-run` ile `--allow-exec` kullanın (bu provider komutlarını yürütebilir).
  * `--allow-exec` yalnızca dry-run içindir ve `--dry-run` olmadan kullanılırsa hata verir.

\--dry-run --json fields

`--dry-run --json`, makine tarafından okunabilir bir rapor yazdırır:

  * `ok`: dry-run'ın geçip geçmediği
  * `operations`: değerlendirilen atama sayısı
  * `checks`: şema/çözülebilirlik kontrollerinin çalışıp çalışmadığı
  * `checks.resolvabilityComplete`: çözülebilirlik kontrollerinin tamamlanana kadar çalışıp çalışmadığı (exec referansları atlandığında false)
  * `refsChecked`: dry-run sırasında gerçekten çözümlenen referans sayısı
  * `skippedExecRefs`: `--allow-exec` ayarlanmadığı için atlanan exec referans sayısı
  * `errors`: `ok=false` olduğunda yapılandırılmış şema/çözülebilirlik hataları


### JSON çıktı biçimi

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### Başarı örneği

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### Hata örneği

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

Dry-run başarısız olursa

  * `config schema validation failed`: değişiklik sonrası yapılandırma biçiminiz geçersiz; yolu/değeri veya sağlayıcı/ref nesnesi biçimini düzeltin.
  * `Config policy validation failed: unsupported SecretRef usage`: bu kimlik bilgisini yeniden düz metin/dize girdisine taşıyın ve SecretRef'leri yalnızca desteklenen yüzeylerde tutun.
  * `SecretRef assignment(s) could not be resolved`: başvurulan sağlayıcı/ref şu anda çözülemiyor (eksik env değişkeni, geçersiz dosya işaretçisi, exec sağlayıcısı hatası veya sağlayıcı/kaynak uyumsuzluğu).
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: dry-run exec ref'lerini atladı; exec çözülebilirlik doğrulamasına ihtiyacınız varsa `--allow-exec` ile yeniden çalıştırın.
  * Toplu mod için, başarısız girdileri düzeltin ve yazmadan önce `--dry-run`'ı yeniden çalıştırın.


## Yazma güvenliği

`openclaw config set` ve OpenClaw'a ait diğer yapılandırma yazıcıları, diske kaydetmeden önce değişiklik sonrası tam yapılandırmayı doğrular. Yeni yük şema doğrulamasından geçmezse veya yıkıcı bir üzerine yazma gibi görünürse, aktif yapılandırmaya dokunulmaz ve reddedilen yük yanına `openclaw.json.rejected.*` olarak kaydedilir.

Küçük düzenlemeler için CLI yazmalarını tercih edin:

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

Bir yazma reddedilirse, kaydedilen yükü inceleyin ve tam yapılandırma biçimini düzeltin:

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

Doğrudan düzenleyiciyle yazmalara hâlâ izin verilir, ancak çalışan Gateway bunları doğrulanana kadar güvenilmeyen olarak ele alır. Geçersiz doğrudan düzenlemeler başlangıcı başarısız kılar veya hot reload tarafından atlanır; Gateway `openclaw.json` dosyasını yeniden yazmaz. Öneklenmiş/üzerine yazılmış yapılandırmayı onarmak veya bilinen son iyi kopyayı geri yüklemek için `openclaw doctor --fix` çalıştırın. Bkz. [Gateway sorun giderme](</tr/gateway/troubleshooting#gateway-rejected-invalid-config>).

Tüm dosya kurtarma yalnızca doctor onarımı için ayrılmıştır. Plugin şeması değişiklikleri veya `minHostVersion` uyumsuzluğu, modeller, sağlayıcılar, auth profilleri, kanallar, Gateway açığa çıkarma, araçlar, bellek, tarayıcı veya Cron yapılandırması gibi ilgisiz kullanıcı ayarlarını geri almak yerine görünür kalır.

## Alt komutlar

  * `config file`: Aktif yapılandırma dosyası yolunu yazdırır (`OPENCLAW_CONFIG_PATH` veya varsayılan konumdan çözümlenir). Yol bir sembolik bağlantıyı değil, normal bir dosyayı adlandırmalıdır.


Düzenlemelerden sonra Gateway'i yeniden başlatın.

## Doğrulama

Gateway'i başlatmadan mevcut yapılandırmayı aktif şemaya göre doğrulayın.

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

`openclaw config validate` geçtikten sonra, aynı terminalden her değişikliği doğrularken gömülü bir ajanın aktif yapılandırmayı dokümanlarla karşılaştırması için yerel TUI'yi kullanabilirsiniz:

bashCopy code
[code]
    openclaw chat
[/code]

Ardından TUI içinde:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

Tipik onarım döngüsü:

* ### Dokümanlarla karşılaştır

Ajanın mevcut yapılandırmanızı ilgili doküman sayfasıyla karşılaştırmasını ve en küçük düzeltmeyi önermesini isteyin.

* ### Hedefli düzenlemeleri uygula

Hedefli düzenlemeleri `openclaw config set` veya `openclaw configure` ile uygulayın.

* ### Yeniden doğrula

Her değişiklikten sonra `openclaw config validate` komutunu yeniden çalıştırın.

* ### Çalışma zamanı sorunları için doctor

Doğrulama geçiyor ancak çalışma zamanı hâlâ sağlıksızsa, geçiş ve onarım yardımı için `openclaw doctor` veya `openclaw doctor --fix` çalıştırın.

## İlgili

  * [CLI referansı](</tr/cli>)
  * [Yapılandırma](</tr/gateway/configuration>)


Was this useful?YesNo