---
title: Gizli bilgi yönetimi
source_url: https://docs.openclaw.ai/tr/gateway/secrets
scraped_at: 2026-05-25
---

OpenClaw, desteklenen kimlik bilgilerinin yapılandırmada düz metin olarak saklanmasına gerek kalmaması için eklemeli SecretRef'leri destekler.

## Hedefler ve çalışma zamanı modeli

Gizler, bellek içi bir çalışma zamanı anlık görüntüsüne çözümlenir.

  * Çözümleme, istek yollarında tembel değil, aktivasyon sırasında isteklidir.
  * Etkin olarak aktif bir SecretRef çözümlenemediğinde başlangıç hızlıca başarısız olur.
  * Yeniden yükleme atomik değiştirme kullanır: tam başarı ya da bilinen son iyi anlık görüntüyü koru.
  * SecretRef ilke ihlalleri (örneğin SecretRef girdisiyle birleştirilmiş OAuth-modu kimlik doğrulama profilleri), çalışma zamanı değişiminden önce aktivasyonu başarısız kılar.
  * Çalışma zamanı istekleri yalnızca aktif bellek içi anlık görüntüden okur.
  * İlk başarılı yapılandırma aktivasyonundan/yüklemesinden sonra, çalışma zamanı kod yolları başarılı bir yeniden yükleme onu değiştirene kadar bu aktif bellek içi anlık görüntüyü okumayı sürdürür.
  * Giden teslim yolları da bu aktif anlık görüntüden okur (örneğin Discord yanıt/iş parçacığı teslimi ve Telegram eylem gönderimleri); her gönderimde SecretRef'leri yeniden çözümlemezler.


Bu, giz sağlayıcı kesintilerini sıcak istek yollarından uzak tutar.

## Aktif yüzey filtreleme

SecretRef'ler yalnızca etkin olarak aktif yüzeylerde doğrulanır.

  * Etkin yüzeyler: çözümlenmemiş referanslar başlangıcı/yeniden yüklemeyi engeller.
  * İnaktif yüzeyler: çözümlenmemiş referanslar başlangıcı/yeniden yüklemeyi engellemez.
  * İnaktif referanslar `SECRETS_REF_IGNORED_INACTIVE_SURFACE` koduyla ölümcül olmayan tanılar üretir.


İnaktif yüzey örnekleri

  * Devre dışı kanal/hesap girdileri.
  * Hiçbir etkin hesabın devralmadığı üst düzey kanal kimlik bilgileri.
  * Devre dışı araç/özellik yüzeyleri.
  * `tools.web.search.provider` tarafından seçilmeyen web arama sağlayıcısına özgü anahtarlar. Otomatik modda (sağlayıcı ayarlanmamışsa), anahtarlar biri çözümlenene kadar sağlayıcı otomatik algılaması için öncelik sırasına göre yoklanır. Seçimden sonra, seçilmeyen sağlayıcı anahtarları seçilene kadar inaktif kabul edilir.
  * Sandbox SSH kimlik doğrulama malzemesi (`agents.defaults.sandbox.ssh.identityData`, `certificateData`, `knownHostsData` ve aracı başına geçersiz kılmalar), yalnızca varsayılan aracı veya etkin bir aracı için etkin sandbox arka ucu `ssh` olduğunda aktiftir.
  * `gateway.remote.token` / `gateway.remote.password` SecretRef'leri şu durumlardan biri doğruysa aktiftir: 
    * `gateway.mode=remote`
    * `gateway.remote.url` yapılandırılmıştır
    * `gateway.tailscale.mode`, `serve` veya `funnel` değerindedir
    * Bu uzak yüzeyler olmadan yerel modda: 
      * `gateway.remote.token`, belirteç kimlik doğrulaması kazanabildiğinde ve hiçbir env/auth belirteci yapılandırılmadığında aktiftir.
      * `gateway.remote.password`, yalnızca parola kimlik doğrulaması kazanabildiğinde ve hiçbir env/auth parolası yapılandırılmadığında aktiftir.
  * `OPENCLAW_GATEWAY_TOKEN` ayarlandığında, `gateway.auth.token` SecretRef'i başlangıç kimlik doğrulama çözümlemesi için inaktiftir, çünkü env belirteç girdisi o çalışma zamanı için kazanır.


## Gateway kimlik doğrulama yüzeyi tanıları

`gateway.auth.token`, `gateway.auth.password`, `gateway.remote.token` veya `gateway.remote.password` üzerinde bir SecretRef yapılandırıldığında, gateway başlangıcı/yeniden yüklemesi yüzey durumunu açıkça günlükler:

  * `active`: SecretRef etkin kimlik doğrulama yüzeyinin parçasıdır ve çözümlenmelidir.
  * `inactive`: SecretRef bu çalışma zamanı için yok sayılır, çünkü başka bir kimlik doğrulama yüzeyi kazanır ya da uzak kimlik doğrulama devre dışıdır/aktif değildir.


Bu girdiler `SECRETS_GATEWAY_AUTH_SURFACE` ile günlüğe yazılır ve aktif yüzey ilkesinin kullandığı nedeni içerir; böylece bir kimlik bilgisinin neden aktif veya inaktif kabul edildiğini görebilirsiniz.

## Onboarding referans ön denetimi

Onboarding etkileşimli modda çalıştığında ve SecretRef depolamasını seçtiğinizde, OpenClaw kaydetmeden önce ön denetim doğrulaması çalıştırır:

  * Env referansları: env var adını doğrular ve kurulum sırasında boş olmayan bir değerin görünür olduğunu onaylar.
  * Sağlayıcı referansları (`file` veya `exec`): sağlayıcı seçimini doğrular, `id` değerini çözümler ve çözümlenen değer türünü denetler.
  * Quickstart yeniden kullanım yolu: `gateway.auth.token` zaten bir SecretRef olduğunda, onboarding aynı hızlı başarısız olma kapısını kullanarak probe/dashboard bootstrap'ten önce onu çözümler (`env`, `file` ve `exec` referansları için).


Doğrulama başarısız olursa onboarding hatayı gösterir ve yeniden denemenize izin verir.

## SecretRef sözleşmesi

Her yerde tek bir nesne şekli kullanın:

json5Copy code
[code]
    { source: "env" | "file" | "exec", provider: "default", id: "..." }
[/code]

### env

json5Copy code
[code]
    { source: "env", provider: "default", id: "OPENAI_API_KEY" }
[/code]

Doğrulama:

  * `provider`, `^[a-z][a-z0-9_-]{0,63}$` ile eşleşmelidir
  * `id`, `^[A-Z][A-Z0-9_]{0,127}$` ile eşleşmelidir


### file

json5Copy code
[code]
    { source: "file", provider: "filemain", id: "/providers/openai/apiKey" }
[/code]

Doğrulama:

  * `provider`, `^[a-z][a-z0-9_-]{0,63}$` ile eşleşmelidir
  * `id` mutlak bir JSON pointer (`/...`) olmalıdır
  * Segmentlerde RFC6901 kaçışları: `~` => `~0`, `/` => `~1`


### exec

json5Copy code
[code]
    { source: "exec", provider: "vault", id: "providers/openai/apiKey" }
[/code]

Doğrulama:

  * `provider`, `^[a-z][a-z0-9_-]{0,63}$` ile eşleşmelidir
  * `id`, `^[A-Za-z0-9][A-Za-z0-9._:/-]{0,255}$` ile eşleşmelidir
  * `id`, eğik çizgiyle ayrılmış yol segmentleri olarak `.` veya `..` içermemelidir (örneğin `a/../b` reddedilir)


## Sağlayıcı yapılandırması

Sağlayıcıları `secrets.providers` altında tanımlayın:

json5Copy code
[code]
    {  secrets: {    providers: {      default: { source: "env" },      filemain: {        source: "file",        path: "~/.openclaw/secrets.json",        mode: "json", // or "singleValue"      },      vault: {        source: "exec",        command: "/usr/local/bin/openclaw-vault-resolver",        args: ["--profile", "prod"],        passEnv: ["PATH", "VAULT_ADDR"],        jsonOnly: true,      },    },    defaults: {      env: "default",      file: "filemain",      exec: "vault",    },    resolution: {      maxProviderConcurrency: 4,      maxRefsPerProvider: 512,      maxBatchBytes: 262144,    },  },}
[/code]

Env sağlayıcısı

  * `allowlist` aracılığıyla isteğe bağlı izin listesi.
  * Eksik/boş env değerleri çözümlemeyi başarısız kılar.

Dosya sağlayıcısı

  * Yerel dosyayı `path` konumundan okur.
  * `mode: "json"`, JSON nesnesi yükü bekler ve `id` değerini pointer olarak çözümler.
  * `mode: "singleValue"`, ref id `"value"` bekler ve dosya içeriğini döndürür.
  * Yol, sahiplik/izin denetimlerinden geçmelidir.
  * Windows fail-closed notu: Bir yol için ACL doğrulaması kullanılamıyorsa çözümleme başarısız olur. Yalnızca güvenilen yollar için yol güvenliği denetimlerini atlamak üzere bu sağlayıcıda `allowInsecurePath: true` ayarlayın.

Exec sağlayıcısı

  * Yapılandırılmış mutlak ikili yolunu çalıştırır, kabuk kullanmaz.
  * Varsayılan olarak `command`, normal bir dosyayı göstermelidir (symlink değil).
  * Symlink komut yollarına izin vermek için `allowSymlinkCommand: true` ayarlayın (örneğin Homebrew shim'leri). OpenClaw çözümlenen hedef yolu doğrular.
  * Paket yöneticisi yolları için `allowSymlinkCommand` ile `trustedDirs` değerini eşleyin (örneğin `["/opt/homebrew"]`).
  * Zaman aşımı, çıktı yok zaman aşımı, çıktı bayt sınırları, env izin listesi ve güvenilen dizinleri destekler.
  * Windows fail-closed notu: Komut yolu için ACL doğrulaması kullanılamıyorsa çözümleme başarısız olur. Yalnızca güvenilen yollar için yol güvenliği denetimlerini atlamak üzere bu sağlayıcıda `allowInsecurePath: true` ayarlayın.


İstek yükü (stdin):

jsonCopy code
[code]
    { "protocolVersion": 1, "provider": "vault", "ids": ["providers/openai/apiKey"] }
[/code]

Yanıt yükü (stdout):

jsoncCopy code
[code]
    { "protocolVersion": 1, "values": { "providers/openai/apiKey": "<openai-api-key>" } } // pragma: allowlist secret
[/code]

İsteğe bağlı id başına hatalar:

jsonCopy code
[code]
    {  "protocolVersion": 1,  "values": {},  "errors": { "providers/openai/apiKey": { "message": "not found" } }}
[/code]

## Exec entegrasyon örnekleri

1Password CLI json5Copy code
[code]
    {  secrets: {    providers: {      onepassword_openai: {        source: "exec",        command: "/opt/homebrew/bin/op",        allowSymlinkCommand: true, // required for Homebrew symlinked binaries        trustedDirs: ["/opt/homebrew"],        args: ["read", "op://Personal/OpenClaw QA API Key/password"],        passEnv: ["HOME"],        jsonOnly: false,      },    },  },  models: {    providers: {      openai: {        baseUrl: "https://api.openai.com/v1",        models: [{ id: "gpt-5", name: "gpt-5" }],        apiKey: { source: "exec", provider: "onepassword_openai", id: "value" },      },    },  },}
[/code]

HashiCorp Vault CLI json5Copy code
[code]
    {  secrets: {    providers: {      vault_openai: {        source: "exec",        command: "/opt/homebrew/bin/vault",        allowSymlinkCommand: true, // required for Homebrew symlinked binaries        trustedDirs: ["/opt/homebrew"],        args: ["kv", "get", "-field=OPENAI_API_KEY", "secret/openclaw"],        passEnv: ["VAULT_ADDR", "VAULT_TOKEN"],        jsonOnly: false,      },    },  },  models: {    providers: {      openai: {        baseUrl: "https://api.openai.com/v1",        models: [{ id: "gpt-5", name: "gpt-5" }],        apiKey: { source: "exec", provider: "vault_openai", id: "value" },      },    },  },}
[/code]

sops json5Copy code
[code]
    {  secrets: {    providers: {      sops_openai: {        source: "exec",        command: "/opt/homebrew/bin/sops",        allowSymlinkCommand: true, // required for Homebrew symlinked binaries        trustedDirs: ["/opt/homebrew"],        args: ["-d", "--extract", '["providers"]["openai"]["apiKey"]', "/path/to/secrets.enc.json"],        passEnv: ["SOPS_AGE_KEY_FILE"],        jsonOnly: false,      },    },  },  models: {    providers: {      openai: {        baseUrl: "https://api.openai.com/v1",        models: [{ id: "gpt-5", name: "gpt-5" }],        apiKey: { source: "exec", provider: "sops_openai", id: "value" },      },    },  },}
[/code]

## MCP sunucu ortam değişkenleri

`plugins.entries.acpx.config.mcpServers` aracılığıyla yapılandırılan MCP sunucu env var'ları SecretInput destekler. Bu, API anahtarlarını ve belirteçleri düz metin yapılandırmanın dışında tutar:

json5Copy code
[code]
    {  plugins: {    entries: {      acpx: {        enabled: true,        config: {          mcpServers: {            github: {              command: "npx",              args: ["-y", "@modelcontextprotocol/server-github"],              env: {                GITHUB_PERSONAL_ACCESS_TOKEN: {                  source: "env",                  provider: "default",                  id: "MCP_GITHUB_PAT",                },              },            },          },        },      },    },  },}
[/code]

Düz metin string değerleri hala çalışır. `${MCP_SERVER_API_KEY}` gibi env-template referansları ve SecretRef nesneleri, MCP sunucu süreci başlatılmadan önce gateway aktivasyonu sırasında çözümlenir. Diğer SecretRef yüzeylerinde olduğu gibi, çözümlenmemiş referanslar yalnızca `acpx` plugin'i etkin olarak aktif olduğunda aktivasyonu engeller.

## Sandbox SSH kimlik doğrulama malzemesi

Çekirdek `ssh` sandbox arka ucu, SSH kimlik doğrulama malzemesi için SecretRef'leri de destekler:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "ssh",        ssh: {          target: "user@gateway-host:22",          identityData: { source: "env", provider: "default", id: "SSH_IDENTITY" },          certificateData: { source: "env", provider: "default", id: "SSH_CERTIFICATE" },          knownHostsData: { source: "env", provider: "default", id: "SSH_KNOWN_HOSTS" },        },      },    },  },}
[/code]

Çalışma zamanı davranışı:

  * OpenClaw bu başvuruları her SSH çağrısı sırasında tembel olarak değil, sandbox etkinleştirmesi sırasında çözümler.
  * Çözümlenen değerler kısıtlayıcı izinlere sahip geçici dosyalara yazılır ve oluşturulan SSH yapılandırmasında kullanılır.
  * Etkili sandbox arka ucu `ssh` değilse, bu başvurular devre dışı kalır ve başlatmayı engellemez.


## Desteklenen kimlik bilgisi yüzeyi

Standart desteklenen ve desteklenmeyen kimlik bilgileri şurada listelenir:

  * [SecretRef Kimlik Bilgisi Yüzeyi](</tr/reference/secretref-credential-surface>)


## Gerekli davranış ve öncelik

  * Başvurusu olmayan alan: değişmez.
  * Başvurusu olan alan: etkinleştirme sırasında etkin yüzeylerde gereklidir.
  * Hem düz metin hem de başvuru varsa, desteklenen öncelik yollarında başvuru öncelikli olur.
  * Redaksiyon işareti `__OPENCLAW_REDACTED__`, dahili yapılandırma redaksiyonu/geri yüklemesi için ayrılmıştır ve değişmez gönderilmiş yapılandırma verisi olarak reddedilir.


Uyarı ve denetim sinyalleri:

  * `SECRETS_REF_OVERRIDES_PLAINTEXT` (çalışma zamanı uyarısı)
  * `REF_SHADOWED` (`auth-profiles.json` kimlik bilgileri `openclaw.json` başvurularına göre öncelikli olduğunda denetim bulgusu)


Google Chat uyumluluk davranışı:

  * `serviceAccountRef`, düz metin `serviceAccount` değerine göre önceliklidir.
  * Kardeş başvuru ayarlandığında düz metin değer yok sayılır.


## Etkinleştirme tetikleyicileri

Gizli etkinleştirme şu durumlarda çalışır:

  * Başlatma (ön kontrol artı son etkinleştirme)
  * Yapılandırma yeniden yükleme sıcak uygulama yolu
  * Yapılandırma yeniden yükleme yeniden başlatma denetimi yolu
  * `secrets.reload` ile manuel yeniden yükleme
  * Düzenlemeleri kalıcı hale getirmeden önce gönderilen yapılandırma yükü içinde etkin yüzey SecretRef çözülebilirliği için Gateway yapılandırma yazma RPC ön kontrolü (`config.set` / `config.apply` / `config.patch`)


Etkinleştirme sözleşmesi:

  * Başarı, anlık görüntüyü atomik olarak değiştirir.
  * Başlatma hatası Gateway başlatmasını iptal eder.
  * Çalışma zamanı yeniden yükleme hatası, bilinen son iyi anlık görüntüyü korur.
  * Yazma-RPC ön kontrol hatası, gönderilen yapılandırmayı reddeder ve hem disk yapılandırmasını hem de etkin çalışma zamanı anlık görüntüsünü değiştirmeden bırakır.
  * Giden bir yardımcı/araç çağrısına çağrıya özel açık bir kanal tokeni sağlamak SecretRef etkinleştirmesini tetiklemez; etkinleştirme noktaları başlatma, yeniden yükleme ve açık `secrets.reload` olarak kalır.


## Bozulmuş ve kurtarılmış sinyaller

Sağlıklı bir durumdan sonra yeniden yükleme zamanı etkinleştirmesi başarısız olduğunda OpenClaw bozulmuş sırlar durumuna girer.

Tek seferlik sistem olayı ve günlük kodları:

  * `SECRETS_RELOADER_DEGRADED`
  * `SECRETS_RELOADER_RECOVERED`


Davranış:

  * Bozulmuş: çalışma zamanı bilinen son iyi anlık görüntüyü korur.
  * Kurtarılmış: bir sonraki başarılı etkinleştirmeden sonra bir kez yayınlanır.
  * Zaten bozulmuş durumdayken tekrarlanan hatalar uyarıları günlüğe yazar, ancak olayları gereksiz yere çoğaltmaz.
  * Başlatmada hızlı başarısız olma bozulmuş olayları yayınlamaz, çünkü çalışma zamanı hiç etkin olmamıştır.


## Komut yolu çözümlemesi

Komut yolları, Gateway anlık görüntü RPC aracılığıyla desteklenen SecretRef çözümlemesine katılmayı seçebilir.

İki geniş davranış vardır:

### Katı komut yolları

Örneğin `openclaw memory` uzak bellek yolları ve uzak paylaşılan gizli başvurularına ihtiyaç duyduğunda `openclaw qr --remote`. Etkin anlık görüntüden okurlar ve gerekli bir SecretRef kullanılamadığında hızlı başarısız olurlar.

### Salt okunur komut yolları

Örneğin `openclaw status`, `openclaw status --all`, `openclaw channels status`, `openclaw channels resolve`, `openclaw security audit` ve salt okunur doctor/yapılandırma onarım akışları. Bunlar da etkin anlık görüntüyü tercih eder, ancak hedeflenen bir SecretRef bu komut yolunda kullanılamadığında iptal etmek yerine bozulmuş moda düşer.

Salt okunur davranış:

  * Gateway çalışırken, bu komutlar önce etkin anlık görüntüden okur.
  * Gateway çözümlemesi eksikse veya Gateway kullanılamıyorsa, belirli komut yüzeyi için hedefli yerel geri dönüş denerler.
  * Hedeflenen bir SecretRef hâlâ kullanılamıyorsa, komut bozulmuş salt okunur çıktı ve "bu komut yolunda yapılandırılmış ancak kullanılamıyor" gibi açık tanılamalarla devam eder.
  * Bu bozulmuş davranış yalnızca komuta yereldir. Çalışma zamanı başlatma, yeniden yükleme veya gönderme/kimlik doğrulama yollarını zayıflatmaz.


Diğer notlar:

  * Arka uç sır döndürmesinden sonra anlık görüntü yenilemesi `openclaw secrets reload` tarafından ele alınır.
  * Bu komut yollarının kullandığı Gateway RPC yöntemi: `secrets.resolve`.


## Denetim ve yapılandırma iş akışı

Varsayılan operatör akışı:

* ### Geçerli durumu denetle

bashCopy code
[code]
    openclaw secrets audit --check
[/code]

* ### SecretRef'leri yapılandır

bashCopy code
[code]
    openclaw secrets configure
[/code]

* ### Yeniden denetle

bashCopy code
[code]
    openclaw secrets audit --check
[/code]

secrets audit

Bulgular şunları içerir:

  * bekleyen düz metin değerler (`openclaw.json`, `auth-profiles.json`, `.env` ve oluşturulan `agents/*/agent/models.json`)
  * oluşturulan `models.json` girdilerinde düz metin hassas sağlayıcı başlığı kalıntıları
  * çözümlenmemiş başvurular
  * öncelik gölgelemesi (`auth-profiles.json` dosyasının `openclaw.json` başvurularına göre öncelik alması)
  * eski kalıntılar (`auth.json`, OAuth hatırlatmaları)


Çalıştırma notu:

  * Varsayılan olarak denetim, komut yan etkilerinden kaçınmak için exec SecretRef çözülebilirlik denetimlerini atlar.
  * Denetim sırasında exec sağlayıcılarını yürütmek için `openclaw secrets audit --allow-exec` kullanın.


Başlık kalıntısı notu:

  * Hassas sağlayıcı başlığı algılama ada dayalı sezgiseldir (yaygın kimlik doğrulama/kimlik bilgisi başlığı adları ve `authorization`, `x-api-key`, `token`, `secret`, `password` ve `credential` gibi parçalar).

secrets configure

Etkileşimli yardımcı şunları yapar:

  * önce `secrets.providers` yapılandırır (`env`/`file`/`exec`, ekle/düzenle/kaldır)
  * bir agent kapsamı için `openclaw.json` içindeki desteklenen sır taşıyan alanları ve ayrıca `auth-profiles.json` alanlarını seçmenize izin verir
  * hedef seçicide doğrudan yeni bir `auth-profiles.json` eşlemesi oluşturabilir
  * SecretRef ayrıntılarını yakalar (`source`, `provider`, `id`)
  * ön kontrol çözümlemesi çalıştırır
  * hemen uygulayabilir


Çalıştırma notu:

  * Ön kontrol, `--allow-exec` ayarlanmadıkça exec SecretRef denetimlerini atlar.
  * Doğrudan `configure --apply` üzerinden uyguluyorsanız ve plan exec başvuruları/sağlayıcıları içeriyorsa, uygulama adımı için de `--allow-exec` ayarlı kalsın.


Yararlı modlar:

  * `openclaw secrets configure --providers-only`
  * `openclaw secrets configure --skip-provider-setup`
  * `openclaw secrets configure --agent <id>`


`configure` uygulama varsayılanları:

  * hedeflenen sağlayıcılar için `auth-profiles.json` dosyasından eşleşen statik kimlik bilgilerini temizler
  * `auth.json` dosyasından eski statik `api_key` girdilerini temizler
  * `<config-dir>/.env` dosyasından eşleşen bilinen sır satırlarını temizler

secrets apply

Kaydedilmiş bir planı uygula:

bashCopy code
[code]
    openclaw secrets apply --from /tmp/openclaw-secrets-plan.jsonopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-runopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-exec
[/code]

Çalıştırma notu:

  * kuru çalışma, `--allow-exec` ayarlanmadıkça exec denetimlerini atlar.
  * yazma modu, `--allow-exec` ayarlanmadıkça exec SecretRef'leri/sağlayıcıları içeren planları reddeder.


Katı hedef/yol sözleşmesi ayrıntıları ve kesin ret kuralları için bkz. [Secrets Apply Plan Sözleşmesi](</tr/gateway/secrets-plan-contract>).

## Tek yönlü güvenlik ilkesi

Güvenlik modeli:

  * ön kontrol yazma modundan önce başarılı olmalıdır
  * çalışma zamanı etkinleştirmesi commit öncesinde doğrulanır
  * apply, dosyaları atomik dosya değiştirme ve hata durumunda en iyi çabayla geri yükleme kullanarak günceller


## Eski kimlik doğrulama uyumluluk notları

Statik kimlik bilgileri için çalışma zamanı artık düz metin eski kimlik doğrulama depolamasına bağlı değildir.

  * Çalışma zamanı kimlik bilgisi kaynağı, çözümlenmiş bellek içi anlık görüntüdür.
  * Eski statik `api_key` girdileri keşfedildiğinde temizlenir.
  * OAuth ile ilgili uyumluluk davranışı ayrı kalır.


## Web UI notu

Bazı SecretInput birliklerini form moduna göre ham düzenleyici modunda yapılandırmak daha kolaydır.

## İlgili

  * [Kimlik Doğrulama](</tr/gateway/authentication>) — kimlik doğrulama kurulumu
  * [CLI: secrets](</tr/cli/secrets>) — CLI komutları
  * [Ortam Değişkenleri](</tr/help/environment>) — ortam önceliği
  * [SecretRef Kimlik Bilgisi Yüzeyi](</tr/reference/secretref-credential-surface>) — kimlik bilgisi yüzeyi
  * [Secrets Apply Plan Sözleşmesi](</tr/gateway/secrets-plan-contract>) — plan sözleşmesi ayrıntıları
  * [Güvenlik](</tr/gateway/security>) — güvenlik duruşu


Was this useful?YesNo