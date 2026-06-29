---
title: ds4
source_url: https://docs.openclaw.ai/tr/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>), DeepSeek V4 Flash'i yerel bir Metal arka ucundan OpenAI uyumlu bir `/v1` API ile sunar. OpenClaw, ds4'e genel `openai-completions` sağlayıcı ailesi üzerinden bağlanır.

ds4, OpenClaw ile birlikte gelen bir sağlayıcı Plugin'i değildir. Bunu `models.providers.ds4` altında yapılandırın, ardından `ds4/deepseek-v4-flash` seçin.

  * Sağlayıcı kimliği: `ds4`
  * Plugin: yok
  * API: OpenAI uyumlu Chat Completions (`openai-completions`)
  * Önerilen temel URL: `http://127.0.0.1:18000/v1`
  * Model kimliği: `deepseek-v4-flash`
  * Araç çağrıları: OpenAI tarzı `tools` ve `tool_calls` üzerinden desteklenir
  * Akıl yürütme: DeepSeek tarzı `thinking` ve `reasoning_effort`


## Gereksinimler

  * Metal desteği olan macOS.
  * `ds4-server` ve DeepSeek V4 Flash GGUF dosyası içeren çalışan bir ds4 checkout'u.
  * Seçtiğiniz bağlam için yeterli bellek. Daha büyük `--ctx` değerleri, sunucu başlatıldığında daha fazla KV belleği ayırır.


## Hızlı başlangıç

* ### ds4-server'ı başlat

`&lt;DS4_DIR&gt;` değerini ds4 checkout yolunuzla değiştirin.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### OpenAI uyumlu endpoint'i doğrula

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

Yanıt `deepseek-v4-flash` içermelidir.

* ### OpenClaw sağlayıcı yapılandırmasını ekle

Tam yapılandırma bölümündeki yapılandırmayı ekleyin, ardından tek seferlik bir model denetimi çalıştırın:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Tam yapılandırma

ds4 zaten `127.0.0.1:18000` üzerinde çalışıyorsa bu yapılandırmayı kullanın.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`contextWindow` değerini `ds4-server --ctx` değeriyle hizalı tutun. OpenClaw'ın sunucu varsayılanından daha az çıktı istemesini özellikle istemiyorsanız `maxTokens` değerini `--tokens` ile hizalı tutun.

## İstek üzerine başlatma

OpenClaw, ds4'ü yalnızca bir `ds4/...` modeli seçildiğinde başlatabilir. Aynı sağlayıcı girdisine `localService` ekleyin:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` mutlak bir çalıştırılabilir dosya yolu olmalıdır. Kabuk araması ve `~` genişletmesi kullanılmaz. Her `localService` alanı için [Yerel model hizmetleri](</tr/gateway/local-model-services>) bölümüne bakın.

## Think Max

ds4, Think Max'i yalnızca iki koşul da doğru olduğunda uygular:

  * `ds4-server`, `--ctx 393216` veya daha yüksek bir değerle başlatılır.
  * İstek `reasoning_effort: "max"` veya eşdeğer ds4 effort alanını kullanır.


Bu büyük bağlamı çalıştırırsanız hem sunucu bayraklarını hem de OpenClaw model meta verilerini güncelleyin:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Test

Doğrudan HTTP denetimiyle başlayın:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Ardından OpenClaw model yönlendirmesini test edin:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Tam bir agent ve araç çağrısı smoke testi için en az 32768 bağlam kullanın:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Beklenen sonuç:

  * `executionTrace.winnerProvider`, `ds4` olur
  * `executionTrace.winnerModel`, `deepseek-v4-flash` olur
  * `toolSummary.calls` en az `1` olur
  * `finalAssistantVisibleText`, `tool-ok` ile başlar


## Sorun giderme

curl /v1/models bağlanamıyor

ds4 çalışmıyor veya `baseUrl` içindeki ana makineye ve porta bağlanmamış. `ds4-server` başlatın, ardından yeniden deneyin:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

Yapılandırılmış `--ctx`, OpenClaw turu için çok küçük. `ds4-server --ctx` değerini artırın, ardından eşleşmesi için `models.providers.ds4.models[].contextWindow` değerini güncelleyin. Araç içeren tam agent turları, doğrudan tek mesajlık curl isteğinden önemli ölçüde daha fazla bağlam gerektirir.

Think Max etkinleşmiyor

ds4, Think Max'i yalnızca `--ctx` en az `393216` olduğunda ve istek `reasoning_effort: "max"` istediğinde kullanır. Daha küçük bağlamlar yüksek akıl yürütmeye geri döner.

İlk istek yavaş

ds4'te soğuk Metal yerleşimi ve model ısınma aşaması vardır. OpenClaw sunucuyu istek üzerine başlattığında `localService.readyTimeoutMs: 300000` kullanın.

## İlgili

[**Yerel model hizmetleri** Model isteklerinden önce yerel model sunucularını istek üzerine başlatın. ](</tr/gateway/local-model-services>) [**Yerel modeller** Yerel model arka uçlarını seçin ve işletin. ](</tr/gateway/local-models>) [**Model sağlayıcıları** Sağlayıcı ref'lerini, kimlik doğrulamayı ve failover'ı yapılandırın. ](</tr/concepts/model-providers>) [**DeepSeek** Yerel DeepSeek sağlayıcı davranışı ve düşünme kontrolleri. ](</tr/providers/deepseek>)

Was this useful?YesNo

Open issue