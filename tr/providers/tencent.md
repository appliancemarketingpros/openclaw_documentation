---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/tr/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud, OpenClaw içinde paketlenmiş bir sağlayıcı Plugin olarak gelir. OpenAI uyumlu bir API kullanarak TokenHub uç noktası (`tencent-tokenhub`) üzerinden Tencent Hy3 preview erişimi sağlar.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `tencent-tokenhub`  
Plugin | paketlenmiş, `enabledByDefault: true`  
Kimlik doğrulama env var | `TOKENHUB_API_KEY`  
Onboarding bayrağı | `--auth-choice tokenhub-api-key`  
Doğrudan CLI bayrağı | `--tokenhub-api-key <key>`  
API | OpenAI uyumlu (`openai-completions`)  
Varsayılan temel URL | `https://tokenhub.tencentmaas.com/v1`  
Küresel temel URL | `https://tokenhub-intl.tencentmaas.com/v1` (geçersiz kılma)  
Varsayılan model | `tencent-tokenhub/hy3-preview`  
  
## Hızlı başlangıç

* ### TokenHub API anahtarı oluşturun

Tencent Cloud TokenHub içinde bir API anahtarı oluşturun. Anahtar için sınırlı bir erişim kapsamı seçerseniz izin verilen modellere **Hy3 preview** ekleyin.

* ### Onboarding çalıştırın

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Modeli doğrulayın

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Etkileşimsiz kurulum

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Yerleşik katalog

Model ref | Ad | Girdi | Bağlam | Maksimum çıktı | Notlar  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | text | 256,000 | 64,000 | Varsayılan; akıl yürütme etkin  
  
Hy3 preview, Tencent Hunyuan'ın akıl yürütme, uzun bağlamlı yönerge izleme, kod ve agent iş akışları için büyük MoE dil modelidir. Tencent'in OpenAI uyumlu örnekleri model kimliği olarak `hy3-preview` kullanır ve standart chat-completions araç çağırmanın yanı sıra `reasoning_effort` desteği sağlar.

## Katmanlı fiyatlandırma

Paketlenmiş katalog, girdi penceresi uzunluğuna göre ölçeklenen katmanlı maliyet meta verileriyle gelir; bu nedenle maliyet tahminleri manuel geçersiz kılmalar olmadan doldurulur.

Girdi token aralığı | Girdi ücreti | Çıktı ücreti | Önbellek okuma  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
Ücretler Tencent tarafından duyurulduğu şekilde milyon token başına USD cinsindendir. Fiyatlandırmayı yalnızca farklı bir yüzeye ihtiyaç duyduğunuzda `models.providers.tencent-tokenhub` altında geçersiz kılın.

## Gelişmiş yapılandırma

Uç nokta geçersiz kılma

OpenClaw varsayılan olarak Tencent Cloud'un `https://tokenhub.tencentmaas.com/v1` uç noktasını kullanır. Tencent ayrıca uluslararası bir TokenHub uç noktasını belgeler:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Uç noktayı yalnızca TokenHub hesabınız veya bölgeniz gerektirdiğinde geçersiz kılın.

Daemon için ortam kullanılabilirliği

Gateway yönetilen bir hizmet olarak çalışıyorsa (launchd, systemd, Docker), `TOKENHUB_API_KEY` bu süreç tarafından görülebilir olmalıdır. launchd, systemd veya Docker exec ortamlarının okuyabilmesi için bunu `~/.openclaw/.env` içinde ya da `env.shellEnv` aracılığıyla ayarlayın.

## İlgili

[**Model sağlayıcıları** Sağlayıcıları, model refs değerlerini ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Yapılandırma referansı** Sağlayıcı ayarları dahil tam config şeması. ](</tr/gateway/configuration>) [**Tencent TokenHub** Tencent Cloud'un TokenHub ürün sayfası. ](<https://cloud.tencent.com/product/tokenhub>) [**Hy3 preview model kartı** Tencent Hunyuan Hy3 preview ayrıntıları ve kıyaslamaları. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo