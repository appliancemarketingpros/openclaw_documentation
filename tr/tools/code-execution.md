---
title: Kod yürütme
source_url: https://docs.openclaw.ai/tr/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution`, xAI'ın Responses API'sinde korumalı alana alınmış uzak Python analizi çalıştırır. Paketle birlikte gelen `xai` Plugin'i tarafından (`tools` sözleşmesi kapsamında) kaydedilir ve `x_search` tarafından kullanılan aynı `https://api.x.ai/v1/responses` uç noktasına gönderilir.

Özellik | Değer  
---|---  
Araç adı | `code_execution`  
Sağlayıcı Plugin'i | `xai` (paketle birlikte gelir, `enabledByDefault: true`)  
Kimlik doğrulama | xAI auth profili, `XAI_API_KEY` veya `plugins.entries.xai.config.webSearch.apiKey`  
Varsayılan model | `grok-4-1-fast`  
Varsayılan zaman aşımı | 30 saniye  
Varsayılan `maxTurns` | ayarlanmamış (xAI kendi iç sınırını uygular)  
  
Bu, yerel [`exec`](</tr/tools/exec>) aracından farklıdır:

  * `exec`, makinenizde veya eşleştirilmiş node üzerinde shell komutları çalıştırır.
  * `code_execution`, Python'ı xAI'ın uzak korumalı alanında çalıştırır.


`code_execution` şunlar için kullanılır:

  * Hesaplamalar.
  * Tablo oluşturma.
  * Hızlı istatistikler.
  * Grafik tarzı analiz.
  * `x_search` veya `web_search` tarafından döndürülen verileri analiz etme.


Yerel dosyalara, shell'inize, reponuza veya eşleştirilmiş cihazlara ihtiyacınız olduğunda bunu **kullanmayın**. Bunun için [`exec`](</tr/tools/exec>) kullanın.

## Kurulum

* ### Bir xAI API anahtarı sağlayın

`code_execution` ve `x_search` için `openclaw onboard --auth-choice xai-api-key` çalıştırın veya Grok web aramasının aynı kimlik bilgisini kullanmasını da istiyorsanız `XAI_API_KEY` ayarlayın / anahtarı xAI Plugin'i altında yapılandırın:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

Ya da config üzerinden:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### code_execution aracını etkinleştirin ve ayarlayın

Araç, `plugins.entries.xai.config.codeExecution.enabled` ile denetlenir. Varsayılan olarak kapalıdır.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // varsayılan xAI kod yürütme modelini geçersiz kılar            maxTurns: 2,            // dahili araç turları için isteğe bağlı üst sınır            timeoutSeconds: 30,     // istek zaman aşımı (varsayılan: 30)          },        },      },    },  },}
[/code]

* ### Gateway'i yeniden başlatın

bashCopy code
[code]
    openclaw gateway restart
[/code]

xAI Plugin'i `enabled: true` ile yeniden kaydolduktan sonra `code_execution`, ajanın araç listesinde görünür.

## Nasıl kullanılır

Doğal şekilde sorun ve analiz amacını açık belirtin:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

Araç dahili olarak tek bir `task` parametresi alır, bu nedenle ajan tam analiz isteğini ve varsa satır içi verileri tek bir prompt içinde göndermelidir.

## Hatalar

Araç kimlik doğrulama olmadan çalıştığında, auth profili, env var ve config seçeneklerini işaret eden yapılandırılmış bir `missing_xai_api_key` hatası döndürür. Hata, fırlatılan bir exception değil JSON'dır; bu nedenle ajan kendi kendini düzeltebilir:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Sınırlar

  * Bu, yerel süreç yürütmesi değil, uzak xAI yürütmesidir.
  * Sonuçları kalıcı bir notebook oturumu değil, geçici analiz olarak ele alın.
  * Yerel dosyalara veya çalışma alanınıza erişim olduğunu varsaymayın.
  * Güncel X verileri için önce [`x_search`](</tr/tools/web#x_search>) kullanın ve sonucu `code_execution` içine aktarın.


## İlgili

[**Exec aracı** Makinenizde veya eşleştirilmiş node üzerinde yerel shell yürütmesi. ](</tr/tools/exec>) [**Exec onayları** Shell yürütmesi için izin verme/reddetme ilkesi. ](</tr/tools/exec-approvals>) [**Web araçları** `web_search`, `x_search` ve `web_fetch`. ](</tr/tools/web>) [**xAI sağlayıcısı** Grok modelleri, web/x araması ve kod yürütme config'i. ](</tr/providers/xai>)

Was this useful?YesNo