---
title: Havai fişekler
source_url: https://docs.openclaw.ai/tr/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>), açık ağırlıklı ve yönlendirilmiş modelleri OpenAI uyumlu bir API üzerinden sunar. OpenClaw, önceden kataloglanmış iki Kimi modeliyle gelen ve çalışma zamanında herhangi bir Fireworks modelini veya yönlendirici kimliğini kabul eden yerleşik bir Fireworks sağlayıcı Plugin içerir.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `fireworks` (alias: `fireworks-ai`)  
Plugin | yerleşik, `enabledByDefault: true`  
Kimlik doğrulama env var | `FIREWORKS_API_KEY`  
Onboarding bayrağı | `--auth-choice fireworks-api-key`  
Doğrudan CLI bayrağı | `--fireworks-api-key <key>`  
API | OpenAI uyumlu (`openai-completions`)  
Temel URL | `https://api.fireworks.ai/inference/v1`  
Varsayılan model | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
Varsayılan alias | `Kimi K2.5 Turbo`  
  
## Başlarken

* ### Fireworks API anahtarını ayarlayın

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Doğrudan bayrakCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Yalnızca envCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Onboarding, anahtarı kimlik doğrulama profillerinizde `fireworks` sağlayıcısına kaydeder ve **Fire Pass** Kimi K2.5 Turbo yönlendiricisini varsayılan model olarak ayarlar.

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

Liste `Kimi K2.6` ve `Kimi K2.5 Turbo (Fire Pass)` öğelerini içermelidir. `FIREWORKS_API_KEY` çözümlenmemişse, `openclaw models status --json` eksik kimlik bilgisini `auth.unusableProfiles` altında bildirir.

## Etkileşimsiz kurulum

Betikli veya CI kurulumları için her şeyi komut satırında iletin:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Yerleşik katalog

Model ref | Ad | Girdi | Bağlam | Maksimum çıktı | Thinking  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | metin + görsel | 262,144 | 262,144 | Zorunlu kapalı  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | metin + görsel | 256,000 | 256,000 | Zorunlu kapalı (varsayılan)  
  
## Özel Fireworks model kimlikleri

OpenClaw, çalışma zamanında herhangi bir Fireworks modelini veya yönlendirici kimliğini kabul eder. Fireworks tarafından gösterilen tam kimliği kullanın ve başına `fireworks/` ekleyin. Dinamik çözümleme, Fire Pass şablonunu (metin + görsel girdisi, OpenAI uyumlu API, varsayılan maliyet sıfır) klonlar ve kimlik Kimi kalıbıyla eşleştiğinde thinking özelliğini otomatik olarak devre dışı bırakır.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

Model kimliği önekleme nasıl çalışır

OpenClaw'daki her Fireworks model ref değeri, `fireworks/` ile başlar ve ardından Fireworks platformundaki tam kimlik veya yönlendirici yolu gelir. Örneğin:

  * Yönlendirici modeli: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Doğrudan model: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw, API isteğini oluştururken `fireworks/` önekini çıkarır ve kalan yolu OpenAI uyumlu `model` alanı olarak Fireworks uç noktasına gönderir.

Kimi için thinking neden zorunlu olarak kapalıdır

Fireworks K2.6, istek `reasoning_*` parametreleri taşıyorsa 400 döndürür; Kimi, Moonshot'ın kendi API'si üzerinden thinking destekliyor olsa bile. Yerleşik ilke (`extensions/fireworks/thinking-policy.ts`), Kimi model kimlikleri için yalnızca `off` thinking düzeyini duyurur; böylece manuel `/think` geçişleri ve sağlayıcı ilkesi yüzeyleri çalışma zamanı sözleşmesiyle hizalı kalır.

Kimi akıl yürütmesini uçtan uca kullanmak için [Moonshot sağlayıcısını](</tr/providers/moonshot>) yapılandırın ve aynı modeli onun üzerinden yönlendirin.

Daemon için ortam kullanılabilirliği

Gateway yönetilen bir hizmet olarak çalışıyorsa (launchd, systemd, Docker), Fireworks anahtarı yalnızca etkileşimli shell'iniz tarafından değil, o süreç tarafından da görülebilir olmalıdır.

macOS'te `openclaw gateway install`, `~/.openclaw/.env` dosyasını LaunchAgent ortam dosyasına zaten bağlar. Anahtarı döndürdükten sonra kurulumu yeniden çalıştırın (veya `openclaw doctor --fix` çalıştırın).

## İlgili

[**Model sağlayıcıları** Sağlayıcıları, model ref değerlerini ve failover davranışını seçme. ](</tr/concepts/model-providers>) [**Thinking modları** `/think` düzeyleri, sağlayıcı ilkeleri ve akıl yürütme yetenekli modelleri yönlendirme. ](</tr/tools/thinking>) [**Moonshot** Moonshot'ın kendi API'si üzerinden Kimi'yi yerel thinking çıktısıyla çalıştırın. ](</tr/providers/moonshot>) [**Sorun giderme** Genel sorun giderme ve SSS. ](</tr/help/troubleshooting>)

Was this useful?YesNo