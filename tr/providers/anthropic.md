---
title: Anthropic
source_url: https://docs.openclaw.ai/tr/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic, **Claude** model ailesini geliştirir. OpenClaw iki kimlik doğrulama rotasını destekler:

  * **API anahtarı** — kullanıma dayalı faturalandırmayla doğrudan Anthropic API erişimi (`anthropic/*` modelleri)
  * **Claude CLI** — aynı ana makinede mevcut bir Claude CLI oturum açmasını yeniden kullanma


## Başlarken

### API anahtarı

**En uygun olduğu durum:** standart API erişimi ve kullanıma dayalı faturalandırma.

* ### API anahtarınızı alın

[Anthropic Console](<https://console.anthropic.com/>) içinde bir API anahtarı oluşturun.

* ### Onboarding çalıştırın

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Ya da anahtarı doğrudan iletin:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Yapılandırma örneği

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**En uygun olduğu durum:** ayrı bir API anahtarı olmadan mevcut bir Claude CLI oturum açmasını yeniden kullanma.

* ### Claude CLI'nin kurulu ve oturum açmış olduğundan emin olun

Şununla doğrulayın:

bashCopy code
[code]
    claude --version
[/code]

* ### Onboarding çalıştırın

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw mevcut Claude CLI kimlik bilgilerini algılar ve yeniden kullanır.

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Yapılandırma örneği

Kanonik Anthropic model ref değerini ve bir CLI çalışma zamanı geçersiz kılmasını tercih edin:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Eski `claude-cli/claude-opus-4-7` model ref değerleri uyumluluk için hâlâ çalışır, ancak yeni yapılandırma sağlayıcı/model seçimini `anthropic/*` olarak tutmalı ve yürütme arka ucunu sağlayıcı/model çalışma zamanı politikasına koymalıdır.

## Düşünme varsayılanları (Claude 4.6)

Claude 4.6 modelleri, açık bir düşünme düzeyi ayarlanmadığında OpenClaw içinde varsayılan olarak `adaptive` düşünmeyi kullanır.

İleti başına `/think:<level>` ile veya model parametrelerinde geçersiz kılın:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## İstem önbelleğe alma

OpenClaw, API anahtarıyla kimlik doğrulama için Anthropic'in istem önbelleğe alma özelliğini destekler.

Değer | Önbellek süresi | Açıklama  
---|---|---  
`"short"` (varsayılan) | 5 dakika | API anahtarıyla kimlik doğrulama için otomatik uygulanır  
`"long"` | 1 saat | Genişletilmiş önbellek  
`"none"` | Önbelleğe alma yok | İstem önbelleğe almayı devre dışı bırakır  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Agent başına önbellek geçersiz kılmaları

Temeliniz olarak model düzeyi parametreleri kullanın, ardından belirli agent'ları `agents.list[].params` aracılığıyla geçersiz kılın:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Yapılandırma birleştirme sırası:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (eşleşen `id`, anahtara göre geçersiz kılar)


Bu, aynı modeldeki başka bir agent ani/az yeniden kullanılan trafik için önbelleğe almayı devre dışı bırakırken, bir agent'ın uzun ömürlü bir önbellek tutmasını sağlar.

Bedrock Claude notları

  * Bedrock üzerindeki Anthropic Claude modelleri (`amazon-bedrock/*anthropic.claude*`) yapılandırıldığında `cacheRetention` geçişini kabul eder.
  * Anthropic olmayan Bedrock modelleri çalışma zamanında zorla `cacheRetention: "none"` kullanır.
  * API anahtarı akıllı varsayılanları, açık bir değer ayarlanmadığında Claude-on-Bedrock ref değerleri için de `cacheRetention: "short"` başlangıç değerini verir.


## Gelişmiş yapılandırma

Hızlı mod

OpenClaw'ın paylaşılan `/fast` anahtarı doğrudan Anthropic trafiğini destekler (API anahtarı ve `api.anthropic.com` için OAuth).

Komut | Şuna eşlenir  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Medya anlama (görüntü ve PDF)

Paketlenmiş Anthropic Plugin, görüntü ve PDF anlama özelliğini kaydeder. OpenClaw medya yeteneklerini yapılandırılmış Anthropic kimlik doğrulamasından otomatik çözer — ek yapılandırma gerekmez.

Özellik | Değer  
---|---  
Varsayılan model | `claude-opus-4-7`  
Desteklenen girdi | Görüntüler, PDF belgeleri  
  
Bir konuşmaya görüntü veya PDF eklendiğinde OpenClaw bunu otomatik olarak Anthropic medya anlama sağlayıcısı üzerinden yönlendirir.

1M bağlam penceresi (beta)

Anthropic'in 1M bağlam penceresi beta geçitlidir. Bunu model başına etkinleştirin:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw bunu isteklerde `anthropic-beta: context-1m-2025-08-07` olarak eşler.

`params.context1m: true`, uygun Opus ve Sonnet modelleri için Claude CLI arka ucuna (`claude-cli/*`) da uygulanır ve bu CLI oturumlarının çalışma zamanı bağlam penceresini doğrudan API davranışıyla eşleşecek şekilde genişletir.

Claude Opus 4.7 1M bağlam

`anthropic/claude-opus-4.7` ve onun `claude-cli` varyantı varsayılan olarak 1M bağlam penceresine sahiptir — `params.context1m: true` gerekmez.

## Sorun giderme

401 hataları / token aniden geçersiz

Anthropic token kimlik doğrulamasının süresi dolar ve iptal edilebilir. Yeni kurulumlar için bunun yerine bir Anthropic API anahtarı kullanın.

"anthropic" sağlayıcısı için API anahtarı bulunamadı

Anthropic kimlik doğrulaması **agent başınadır** — yeni agent'lar ana agent'ın anahtarlarını devralmaz. Bu agent için onboarding'i yeniden çalıştırın (veya gateway ana makinesinde bir API anahtarı yapılandırın), ardından `openclaw models status` ile doğrulayın.

"anthropic:default" profili için kimlik bilgisi bulunamadı

Hangi kimlik doğrulama profilinin etkin olduğunu görmek için `openclaw models status` çalıştırın. Onboarding'i yeniden çalıştırın veya bu profil yolu için bir API anahtarı yapılandırın.

Kullanılabilir kimlik doğrulama profili yok (hepsi bekleme süresinde)

`auth.unusableProfiles` için `openclaw models status --json` çıktısını kontrol edin. Anthropic hız sınırı bekleme süreleri model kapsamlı olabilir, bu nedenle kardeş bir Anthropic modeli hâlâ kullanılabilir olabilir. Başka bir Anthropic profili ekleyin veya bekleme süresinin dolmasını bekleyin.

## İlgili

[**Model seçimi** Sağlayıcıları, model ref değerlerini ve failover davranışını seçme. ](</tr/concepts/model-providers>) [**CLI arka uçları** Claude CLI arka ucu kurulumu ve çalışma zamanı ayrıntıları. ](</tr/gateway/cli-backends>) [**İstem önbelleğe alma** İstem önbelleğe almanın sağlayıcılar genelinde nasıl çalıştığı. ](</tr/reference/prompt-caching>) [**OAuth ve kimlik doğrulama** Kimlik doğrulama ayrıntıları ve kimlik bilgisi yeniden kullanım kuralları. ](</tr/gateway/authentication>)

Was this useful?YesNo