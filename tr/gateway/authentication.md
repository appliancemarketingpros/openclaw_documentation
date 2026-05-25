---
title: Kimlik doğrulama
source_url: https://docs.openclaw.ai/tr/gateway/authentication
scraped_at: 2026-05-25
---

OpenClaw, model sağlayıcıları için OAuth ve API anahtarlarını destekler. Sürekli açık Gateway ana makineleri için API anahtarları genellikle en öngörülebilir seçenektir. Abonelik/OAuth akışları, sağlayıcı hesap modelinizle eşleştiğinde ayrıca desteklenir.

Tam OAuth akışı ve depolama düzeni için [/concepts/oauth](</tr/concepts/oauth>) bölümüne bakın. SecretRef tabanlı kimlik doğrulama (`env`/`file`/`exec` sağlayıcıları) için [Gizli Bilgi Yönetimi](</tr/gateway/secrets>) bölümüne bakın. `models status --probe` tarafından kullanılan kimlik bilgisi uygunluğu/neden kodu kuralları için [Kimlik Doğrulama Kimlik Bilgisi Semantiği](</tr/auth-credential-semantics>) bölümüne bakın.

## Önerilen kurulum (API anahtarı, herhangi bir sağlayıcı)

Uzun süre çalışan bir Gateway çalıştırıyorsanız seçtiğiniz sağlayıcı için bir API anahtarıyla başlayın. Özellikle Anthropic için API anahtarı kimlik doğrulaması hâlâ en öngörülebilir sunucu kurulumudur, ancak OpenClaw yerel bir Claude CLI oturum açma bilgisinin yeniden kullanılmasını da destekler.

  1. Sağlayıcı konsolunuzda bir API anahtarı oluşturun.
  2. Bunu **Gateway ana makinesine** (`openclaw gateway` çalıştıran makine) koyun.

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."openclaw models status
[/code]

  3. Gateway systemd/launchd altında çalışıyorsa daemon'ın okuyabilmesi için anahtarı `~/.openclaw/.env` içine koymayı tercih edin:

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'&lt;PROVIDER&gt;_API_KEY=...EOF
[/code]

Ardından daemon'ı yeniden başlatın (veya Gateway sürecinizi yeniden başlatın) ve yeniden kontrol edin:

bashCopy code
[code]
    openclaw models statusopenclaw doctor
[/code]

Ortam değişkenlerini kendiniz yönetmek istemiyorsanız, onboarding daemon kullanımı için API anahtarlarını saklayabilir: `openclaw onboard`.

Ortam devralma (`env.shellEnv`, `~/.openclaw/.env`, systemd/launchd) ayrıntıları için [Yardım](</tr/help>) bölümüne bakın.

## Anthropic: Claude CLI ve belirteç uyumluluğu

Anthropic kurulum belirteci kimlik doğrulaması, desteklenen bir belirteç yolu olarak OpenClaw içinde hâlâ kullanılabilir. Anthropic personeli o zamandan beri OpenClaw tarzı Claude CLI kullanımına yeniden izin verildiğini bize bildirdiği için OpenClaw, Anthropic yeni bir ilke yayımlamadığı sürece Claude CLI yeniden kullanımını ve `claude -p` kullanımını bu entegrasyon için onaylanmış kabul eder. Claude CLI yeniden kullanımı ana makinede kullanılabiliyorsa, artık tercih edilen yol budur.

Uzun süre çalışan Gateway ana makineleri için Anthropic API anahtarı hâlâ en öngörülebilir kurulumdur. Aynı ana makinede mevcut bir Claude oturum açma bilgisini yeniden kullanmak istiyorsanız onboarding/configure içinde Anthropic Claude CLI yolunu kullanın.

Claude CLI yeniden kullanımı için önerilen ana makine kurulumu:

bashCopy code
[code]
    # Run on the gateway hostclaude auth loginclaude auth status --textopenclaw models auth login --provider anthropic --method cli --set-default
[/code]

Bu iki adımlı bir kurulumdur:

  1. Claude Code'un kendisini Gateway ana makinesinde Anthropic'e oturtum açtırın.
  2. OpenClaw'a Anthropic model seçimini yerel `claude-cli` backend'ine geçirmesini ve eşleşen OpenClaw kimlik doğrulama profilini saklamasını söyleyin.


`claude`, `PATH` üzerinde değilse önce Claude Code'u yükleyin veya `agents.defaults.cliBackends.claude-cli.command` değerini gerçek ikili dosya yoluna ayarlayın.

El ile belirteç girişi (herhangi bir sağlayıcı; `auth-profiles.json` yazar ve yapılandırmayı günceller):

bashCopy code
[code]
    openclaw models auth paste-token --provider openrouter
[/code]

`auth-profiles.json` yalnızca kimlik bilgilerini saklar. Kanonik biçim şöyledir:

jsonCopy code
[code]
    {  "version": 1,  "profiles": {    "openrouter:default": {      "type": "api_key",      "provider": "openrouter",      "key": "OPENROUTER_API_KEY"    }  }}
[/code]

OpenClaw çalışma zamanında kanonik `version` \+ `profiles` biçimini bekler. Daha eski bir kurulumda hâlâ `{ "openrouter": { "apiKey": "..." } }` gibi düz bir dosya varsa, bunu bir `openrouter:default` API anahtarı profili olarak yeniden yazmak için `openclaw doctor --fix` çalıştırın; doctor özgünün yanında bir `.legacy-flat.*.bak` kopyası tutar. `baseUrl`, `api`, model kimlikleri, başlıklar ve zaman aşımları gibi uç nokta ayrıntıları `auth-profiles.json` içinde değil, `openclaw.json` veya `models.json` içindeki `models.providers.<id>` altında yer almalıdır.

Bedrock `auth: "aws-sdk"` gibi harici kimlik doğrulama rotaları da kimlik bilgisi değildir. Adlandırılmış bir Bedrock rotası istiyorsanız `openclaw.json` içine `auth.profiles.<id>.mode: "aws-sdk"` koyun; `auth-profiles.json` içine `type: "aws-sdk"` yazmayın. `openclaw doctor --fix`, eski AWS SDK işaretçilerini kimlik bilgisi deposundan yapılandırma metadata'sına taşır.

Kimlik doğrulama profili referansları statik kimlik bilgileri için de desteklenir:

  * `api_key` kimlik bilgileri `keyRef: { source, provider, id }` kullanabilir
  * `token` kimlik bilgileri `tokenRef: { source, provider, id }` kullanabilir
  * OAuth modundaki profiller SecretRef kimlik bilgilerini desteklemez; `auth.profiles.<id>.mode` `"oauth"` olarak ayarlanmışsa, bu profil için SecretRef destekli `keyRef`/`tokenRef` girdisi reddedilir.


Otomasyon dostu kontrol (süresi dolmuş/eksik olduğunda çıkış `1`, süresi dolmak üzere olduğunda `2`):

bashCopy code
[code]
    openclaw models status --check
[/code]

Canlı kimlik doğrulama probları:

bashCopy code
[code]
    openclaw models status --probe
[/code]

Notlar:

  * Prob satırları kimlik doğrulama profillerinden, ortam kimlik bilgilerinden veya `models.json` dosyasından gelebilir.
  * Açık `auth.order.<provider>` saklanan bir profili atlarsa prob, o profili denemek yerine `excluded_by_auth_order` bildirir.
  * Kimlik doğrulama varsa ancak OpenClaw bu sağlayıcı için problanabilir bir model adayı çözemiyorsa prob `status: no_model` bildirir.
  * Hız sınırı soğuma süreleri model kapsamlı olabilir. Bir model için soğumada olan bir profil, aynı sağlayıcıdaki kardeş bir model için hâlâ kullanılabilir olabilir.


İsteğe bağlı operasyon betikleri (systemd/Termux) burada belgelenmiştir: [Kimlik doğrulama izleme betikleri](</tr/help/scripts#auth-monitoring-scripts>)

## Anthropic notu

Anthropic `claude-cli` backend'i yeniden desteklenmektedir.

  * Anthropic personeli bu OpenClaw entegrasyon yoluna yeniden izin verildiğini bize bildirdi.
  * Bu nedenle OpenClaw, Anthropic yeni bir ilke yayımlamadığı sürece Claude CLI yeniden kullanımını ve `claude -p` kullanımını Anthropic destekli çalıştırmalar için onaylanmış kabul eder.
  * Anthropic API anahtarları, uzun süre çalışan Gateway ana makineleri ve açık sunucu tarafı faturalandırma denetimi için en öngörülebilir seçenek olmaya devam eder.


## Model kimlik doğrulama durumunu denetleme

bashCopy code
[code]
    openclaw models statusopenclaw doctor
[/code]

## API anahtarı döndürme davranışı (Gateway)

Bazı sağlayıcılar, bir API çağrısı sağlayıcı hız sınırına takıldığında isteğin alternatif anahtarlarla yeniden denenmesini destekler.

  * Öncelik sırası: 
    * `OPENCLAW_LIVE_&lt;PROVIDER&gt;_KEY` (tekil geçersiz kılma)
    * `&lt;PROVIDER&gt;_API_KEYS`
    * `&lt;PROVIDER&gt;_API_KEY`
    * `&lt;PROVIDER&gt;_API_KEY_*`
  * Google sağlayıcıları ayrıca ek bir yedek olarak `GOOGLE_API_KEY` içerir.
  * Aynı anahtar listesi kullanımdan önce tekilleştirilir.
  * OpenClaw yalnızca hız sınırı hataları için bir sonraki anahtarla yeniden dener (örneğin `429`, `rate_limit`, `quota`, `resource exhausted`, `Too many concurrent requests`, `ThrottlingException`, `concurrency limit reached` veya `workers_ai ... quota limit exceeded`).
  * Hız sınırı dışındaki hatalar alternatif anahtarlarla yeniden denenmez.
  * Tüm anahtarlar başarısız olursa son denemeden gelen nihai hata döndürülür.


## Hangi kimlik bilgisinin kullanılacağını denetleme

### Oturum başına (sohbet komutu)

Geçerli oturum için belirli bir sağlayıcı kimlik bilgisini sabitlemek üzere `/model <alias-or-id>@<profileId>` kullanın (örnek profil kimlikleri: `anthropic:default`, `anthropic:work`).

Kompakt bir seçici için `/model` (veya `/model list`) kullanın; tam görünüm için (adaylar + sonraki kimlik doğrulama profili, ayrıca yapılandırılmışsa sağlayıcı uç nokta ayrıntıları) `/model status` kullanın.

### Aracı başına (CLI geçersiz kılması)

Bir aracı için açık bir kimlik doğrulama profili sırası geçersiz kılması ayarlayın (o aracının `auth-state.json` dosyasında saklanır):

bashCopy code
[code]
    openclaw models auth order get --provider anthropicopenclaw models auth order set --provider anthropic anthropic:defaultopenclaw models auth order clear --provider anthropic
[/code]

Belirli bir aracıyı hedeflemek için `--agent <id>` kullanın; yapılandırılmış varsayılan aracıyı kullanmak için bunu atlayın. Sıra sorunlarında hata ayıklarken `openclaw models status --probe`, atlanan saklanmış profilleri sessizce geçmek yerine `excluded_by_auth_order` olarak gösterir. Soğuma sorunlarında hata ayıklarken hız sınırı soğumalarının tüm sağlayıcı profiline değil, tek bir model kimliğine bağlı olabileceğini unutmayın.

## Sorun giderme

### "Kimlik bilgisi bulunamadı"

Anthropic profili eksikse **Gateway ana makinesinde** bir Anthropic API anahtarı yapılandırın veya Anthropic kurulum belirteci yolunu ayarlayın, ardından yeniden kontrol edin:

bashCopy code
[code]
    openclaw models status
[/code]

### Belirtecin süresi doluyor/dolmuş

Hangi profilin süresinin dolmakta olduğunu doğrulamak için `openclaw models status` çalıştırın. Bir Anthropic belirteç profili eksikse veya süresi dolmuşsa bu kurulumu kurulum belirteciyle yenileyin ya da Anthropic API anahtarına geçin.

## İlgili

  * [Gizli bilgi yönetimi](</tr/gateway/secrets>)
  * [Uzaktan erişim](</tr/gateway/remote>)
  * [Kimlik doğrulama depolaması](</tr/concepts/oauth>)


Was this useful?YesNo