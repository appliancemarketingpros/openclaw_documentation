---
title: Kasa SecretRef'leri
source_url: https://docs.openclaw.ai/tr/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# Vault SecretRef'leri

Paketle birlikte gelen Vault Plugin'i, OpenClaw'un Gateway başlangıcında ve yeniden yükleme sırasında HashiCorp Vault'taki `exec` SecretRef'lerini çözümlemesini sağlar. OpenClaw, Vault referanslarını yapılandırmada saklar, çözümlenen değerleri bellek içi gizli bilgiler anlık görüntüsünde tutar ve çözümlenen API anahtarlarını `openclaw.json` dosyasına geri yazmaz.

Zaten Vault çalıştırıyorsanız veya model sağlayıcısı anahtarlarının OpenClaw yapılandırma dosyalarının dışında tutulmasını istiyorsanız bunu kullanın. SecretRef çalışma zamanı modeli için [Gizli bilgilerin yönetimi](</tr/gateway/secrets>) bölümüne bakın.

## Başlamadan önce

Gereksinimler:

  * paketle birlikte gelen `vault` Plugin'inin kullanılabilir olduğu OpenClaw
  * erişilebilir bir Vault sunucusu
  * OpenClaw'un çözümlemesi gereken gizli bilgi yollarına okuma erişimi olan bir istemci belirteci üretebilen Vault kimlik doğrulaması
  * Gateway'i başlatan ortamda `VAULT_ADDR` ve ayrıca `VAULT_TOKEN`, `VAULT_TOKEN_FILE` ile birlikte `OPENCLAW_VAULT_AUTH_METHOD=token_file` veya yapılandırılmış bir JWT/Kubernetes oturum açma yöntemi bulunmalıdır


Çözümleyici, Node üzerinden HTTP kullanarak Vault ile iletişim kurar. Gateway'in SecretRef'leri çözümlemek için Vault CLI'ına ihtiyacı yoktur.

`openclaw vault` komutlarını çalıştırmadan önce paketle birlikte gelen Plugin'i etkinleştirin:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Vault'ta bir sağlayıcı anahtarı saklama

OpenClaw varsayılan olarak `secret` konumuna bağlanmış KV v2'yi kullanır; bu, Vault geliştirme sunucusu örnekleriyle uyumludur. Üretim Vault ortamında, SecretRef kimliklerini oluşturmadan önce `OPENCLAW_VAULT_KV_MOUNT` değerini gerçek KV bağlama yolunuza ayarlayın. OpenClaw varsayılanlarıyla şu SecretRef kimliği:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

şu Vault alanını okur:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Bunu Vault CLI ile oluşturmanın bir yolu şudur:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

OpenClaw için kök belirteç değil, kapsamı sınırlandırılmış bir istemci belirteci kullanın. Varsayılan KV v2 düzeninde, model sağlayıcısı anahtarları için asgari bir politika şu şekildedir:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Vault'u Gateway için görünür hâle getirme

Kapsayıcıda çalışmayan yerel bir Gateway için Vault ayarlarını OpenClaw'u başlatan aynı kabukta dışa aktarın. Varsayılan kimlik doğrulama yöntemi, Vault istemci belirtecini `VAULT_TOKEN` değişkeninden okur:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Vault Agent bir belirteç havuzu dosyası yazıyorsa belirteç dosyası kimlik doğrulamasını kullanın:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Özel bir CA tarafından imzalanmış Vault sunucusu için bu CA'yı ana makinenin güven deposuna yükleyip Node sistem güvenini etkinleştirin:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Alternatif olarak doğrudan bir PEM paketi sağlayın:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

OpenClaw başlatıldığında bu değişkenler mevcut olmalıdır. Vault Plugin'i bunları çözümleyici sürecine iletir.

Etkileşimsiz JWT kimlik doğrulaması için bir iş yükü JWT dosyası ve `jwt` türünde bir Vault rolü kullanın:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

JWT dosyası, Vault rolünün kabul ettiği bir hedef kitleye sahip Kubernetes hizmet hesabı belirteci gibi yansıtılmış bir iş yükü belirteci olmalıdır. Etkileşimli OIDC tarayıcı oturumu insanlar için kullanışlıdır, ancak Gateway çalışma zamanı etkileşimsiz JWT oturumu veya bir belirteç dosyası gerektirir.

Vault'un Kubernetes kimlik doğrulama yöntemi için `kubernetes` kullanın. Bu yöntem, Pod olarak çalışan Gateway'ler içindir; varsayılan bağlama noktası `kubernetes`, varsayılan JWT dosyası ise standart hizmet hesabı belirteci yoludur:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

`OPENCLAW_VAULT_AUTH_MOUNT` değişkenini yalnızca Vault, Kubernetes kimlik doğrulamasını `auth/kubernetes` dışında bir konuma bağladıysa ayarlayın. `OPENCLAW_VAULT_JWT_FILE` değişkenini yalnızca hizmet hesabı belirteci özel bir yola yansıtılmışsa ayarlayın.

İsteğe bağlı ayarlar:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Geçerli kabuğun neleri görebildiğini denetleyin:

bashCopy code
[code]
    openclaw vault status
[/code]

Vault destekli birden fazla gizli bilgi sağlayıcısı yapılandırıldığında birini takma adına göre seçin:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status`, `VAULT_TOKEN` değerini hiçbir zaman yazdırmaz; yalnızca belirtecin, belirteç dosyasının ve JWT dosyasının ayarlanıp ayarlanmadığını bildirir.

## SecretRef planı oluşturma ve uygulama

OpenRouter'ın model sağlayıcısı API anahtarını Vault ile eşleyen bir plan oluşturun:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Planı uygulayın ve doğrulayın:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Vault Plugin'i OpenClaw tarafından yönetilen bir exec SecretRef sağlayıcısı üzerinden çözümleme yaptığı için `--allow-exec` kullanın.

Gateway henüz çalışmıyorsa planı uyguladıktan sonra `openclaw secrets reload` komutunu çalıştırmak yerine Gateway'i normal şekilde başlatın.

## Daha fazla sağlayıcı anahtarı yapılandırma

Yerleşik kısayollar:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Tek planda birden fazla sağlayıcı anahtarı:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Kısayolu olmayan paketle birlikte gelen sağlayıcılar veya önceden yapılandırılmış OpenAI uyumlu ve özel model sağlayıcıları için `--provider-key` kullanın:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Her `--provider-key <provider=id>`, `models.providers.<provider>.apiKey` konumuna bir SecretRef yazar. Özel sağlayıcılar için sağlayıcının `baseUrl`, `api` veya `models` ayarlarını oluşturmaz; önce bunları yapılandırın.

Bilinen herhangi bir SecretRef hedef yolu için `--target <path=id>` kullanın:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Çıplak hedef yollar `openclaw.json` dosyasına uygulanır. Mevcut `auth-profiles.json` hedefleri için `auth-profiles:<agentId>:<path>` kullanın. Hedef yol, kayıtlı bir OpenClaw SecretRef hedefi olmalıdır. Kurulum komutu OpenClaw'da rastgele adlandırılmış gizli bilgiler oluşturmaz; gizli bilgi deposu Vault olarak kalır ve OpenClaw, SecretRef'leri yalnızca desteklenen yapılandırma alanlarında saklar.

## SecretRef kimliği biçimi

Vault SecretRef kimlikleri şu kuralı kullanır:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Örnekler:

SecretRef kimliği | Varsayılan KV v2 Vault okuması | Döndürülen alan  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Döndürülen Vault alanı bir dize olmalıdır.

KV v1 için şunu ayarlayın:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

Bu durumda `providers/openrouter/apiKey` şunu okur:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## OpenClaw'un sakladıkları

Bir Vault kurulum planı uygulandığında Plugin tarafından yönetilen bir sağlayıcı saklanır:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Kimlik bilgisi alanları bu sağlayıcıyı gösterir:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

Çözümlenen değer yalnızca etkin çalışma zamanı gizli bilgileri anlık görüntüsünde bulunur.

## Kapsayıcılar ve yönetilen dağıtımlar

Kapsayıcıda çalışan Gateway'ler de aynı Plugin'i ve SecretRef yapılandırmasını kullanır. Kapsayıcıya şunlar aktarılmalıdır:

  * `VAULT_ADDR`
  * bir kimlik doğrulama kaynağı: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` ile birlikte `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` ile birlikte `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` ve `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` ile birlikte `OPENCLAW_VAULT_AUTH_ROLE`; isteğe bağlı olarak `OPENCLAW_VAULT_AUTH_MOUNT` veya `OPENCLAW_VAULT_JWT_FILE` değerini geçersiz kılın
  * isteğe bağlı `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` ve `OPENCLAW_VAULT_KV_VERSION`


Kubernetes kullanırken Vault, küme için Kubernetes kimlik doğrulamasıyla yapılandırılmışsa `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` yöntemini tercih edin. `OPENCLAW_VAULT_AUTH_METHOD=jwt` yöntemini yalnızca Vault, kümeyi genel bir JWT/OIDC düzenleyicisi olarak ele alacak şekilde yapılandırılmışsa kullanın. Her iki seçenek de Kubernetes Secret içinde uzun ömürlü bir Vault belirteci bulundurmaktan daha iyidir. Vault Agent yan kapsayıcısı veya enjektör dağıtımları bunun yerine `token_file` kullanabilir.

Çok kiracılı Vault kurulumlarında kiracı yönlendirmesini Vault politikasında ve dağıtım yapılandırmasında tutun. OpenClaw sabit bir bağlama noktası, rol veya yol gerektirmez: her Gateway ortamı kendi `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` ve SecretRef kimliklerini ayarlayabilir. Paylaşılan tek bir Gateway'in aynı anda farklı Vault kullanıcıları için çözümleme yapması gerekiyorsa farklı kimlik doğrulama ortamlarını sarmalayan, elle yapılandırılmış exec sağlayıcıları kullanın veya kiracıları ayrı Vault ortam değişkenlerine sahip Gateway ortamlarına bölün.

## İlgili

  * [Gizli bilgilerin yönetimi](</tr/gateway/secrets>)
  * [`openclaw secrets`](</tr/cli/secrets>)
  * [Plugin envanteri](</tr/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue