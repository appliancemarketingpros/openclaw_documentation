---
title: Moonshot AI
source_url: https://docs.openclaw.ai/tr/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot, OpenAI uyumlu uç noktalarla Kimi API sağlar. Sağlayıcıyı yapılandırın ve varsayılan modeli `moonshot/kimi-k2.6` olarak ayarlayın ya da `kimi/kimi-for-coding` ile Kimi Coding kullanın.

## Yerleşik model kataloğu

Model referansı | Ad | Akıl yürütme | Girdi | Bağlam | Maks çıkış  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | Hayır | metin, görsel | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | Hayır | metin, görsel | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | Evet | metin | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | Evet | metin | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | Hayır | metin | 256,000 | 16,384  
  
Güncel Moonshot barındırmalı K2 modelleri için paketlenmiş maliyet tahminleri, Moonshot'ın yayımlanmış kullandıkça öde ücretlerini kullanır: Kimi K2.6 için $0.16/MTok önbellek isabeti, $0.95/MTok girdi ve $4.00/MTok çıktı; Kimi K2.5 için $0.10/MTok önbellek isabeti, $0.60/MTok girdi ve $3.00/MTok çıktı. Diğer eski katalog girdileri, yapılandırmada geçersiz kılmadığınız sürece sıfır maliyet yer tutucularını korur.

## Başlarken

Sağlayıcınızı seçin ve kurulum adımlarını izleyin.

### Moonshot API

**En uygun olduğu kullanım:** Moonshot Open Platform üzerinden Kimi K2 modelleri.

* ### Choose your endpoint region

Kimlik doğrulama seçimi | Uç nokta | Bölge  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | Uluslararası  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | Çin  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

Ya da Çin uç noktası için:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Run a live smoke test

Normal oturumlarınıza dokunmadan model erişimini ve maliyet takibini doğrulamak istediğinizde yalıtılmış bir durum dizini kullanın:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

JSON yanıtı `provider: "moonshot"` ve `model: "kimi-k2.6"` bildirmelidir. Asistan döküm girdisi, Moonshot kullanım metaverisi döndürdüğünde normalleştirilmiş token kullanımını ve tahmini maliyeti `usage.cost` altında saklar.

### Yapılandırma örneği

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**En uygun olduğu kullanım:** Kimi Coding uç noktası üzerinden kod odaklı görevler.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### Yapılandırma örneği

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Kimi web araması

OpenClaw ayrıca Moonshot web araması tarafından desteklenen bir `web_search` sağlayıcısı olarak **Kimi** ile birlikte gelir.

* ### Etkileşimli web araması kurulumunu çalıştır

bashCopy code
[code]
    openclaw configure --section web
[/code]

`plugins.entries.moonshot.config.webSearch.*` değerlerini saklamak için web araması bölümünde **Kimi** seçeneğini seçin.

* ### Web araması bölgesini ve modelini yapılandır

Etkileşimli kurulum şunları sorar:

Ayar | Seçenekler  
---|---  
API bölgesi | `https://api.moonshot.ai/v1` (uluslararası) veya `https://api.moonshot.cn/v1` (Çin)  
Web araması modeli | Varsayılan olarak `kimi-k2.6` kullanılır  
  
Yapılandırma `plugins.entries.moonshot.config.webSearch` altında bulunur:

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## Gelişmiş yapılandırma

Yerel düşünme modu

Moonshot Kimi ikili yerel düşünmeyi destekler:

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


Bunu model başına `agents.defaults.models.<provider/model>.params` aracılığıyla yapılandırın:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw ayrıca Moonshot için çalışma zamanı `/think` düzeylerini eşler:

`/think` düzeyi | Moonshot davranışı  
---|---  
`/think off` | `thinking.type=disabled`  
Off olmayan herhangi bir düzey | `thinking.type=enabled`  
  
Kimi K2.6 ayrıca `reasoning_content` için çok turlu saklamayı denetleyen isteğe bağlı bir `thinking.keep` alanını kabul eder. Turlar arasında tam akıl yürütmeyi korumak için bunu `"all"` olarak ayarlayın; sunucu varsayılan stratejisini kullanmak için bunu atlayın (veya `null` bırakın). OpenClaw, `thinking.keep` alanını yalnızca `moonshot/kimi-k2.6` için iletir ve diğer modellerden çıkarır.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

Araç çağrısı kimliği temizleme

Moonshot Kimi, `functions.<name>:<index>` biçimindeki tool_call kimlikleri sunar. OpenClaw bunları değiştirmeden korur, böylece çok turlu araç çağrıları çalışmaya devam eder.

Özel bir OpenAI uyumlu sağlayıcıda katı temizlemeyi zorlamak için `sanitizeToolCallIds: true` ayarlayın:

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

Akış kullanım uyumluluğu

Yerel Moonshot uç noktaları (`https://api.moonshot.ai/v1` ve `https://api.moonshot.cn/v1`), paylaşılan `openai-completions` taşımasında akış kullanım uyumluluğunu duyurur. OpenClaw bunu uç nokta yeteneklerine göre belirler, bu yüzden aynı yerel Moonshot ana bilgisayarlarını hedefleyen uyumlu özel sağlayıcı kimlikleri aynı akış kullanım davranışını devralır.

Paketle gelen K2.6 fiyatlandırmasıyla, giriş, çıkış ve önbellek okuma tokenlarını içeren akış kullanımı ayrıca `/status`, `/usage full`, `/usage cost` ve döküm destekli oturum muhasebesi için yerel tahmini USD maliyetine dönüştürülür.

Uç nokta ve model ref başvurusu Sağlayıcı | Model ref öneki | Uç nokta | Kimlik doğrulama env var  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Kimi Coding uç noktası | `KIMI_API_KEY`  
Web arama | N/A | Moonshot API bölgesiyle aynı | `KIMI_API_KEY` veya `MOONSHOT_API_KEY`  
  
  * Kimi web araması `KIMI_API_KEY` veya `MOONSHOT_API_KEY` kullanır ve varsayılan olarak `kimi-k2.6` modeliyle `https://api.moonshot.ai/v1` adresini kullanır.
  * Gerekirse fiyatlandırmayı ve bağlam meta verilerini `models.providers` içinde geçersiz kılın.
  * Moonshot bir model için farklı bağlam limitleri yayımlarsa, `contextWindow` değerini buna göre ayarlayın.


## İlgili

[**Model seçimi** Sağlayıcıları, model ref'lerini ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Web arama** Kimi dahil web arama sağlayıcılarını yapılandırma. ](</tr/tools/web>) [**Yapılandırma başvurusu** Sağlayıcılar, modeller ve plugin'ler için tam config şeması. ](</tr/gateway/configuration-reference>) [**Moonshot Open Platform** Moonshot API anahtarı yönetimi ve dokümantasyonu. ](<https://platform.moonshot.ai>)

Was this useful?YesNo