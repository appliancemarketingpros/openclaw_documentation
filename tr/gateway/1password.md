---
title: 1Password
source_url: https://docs.openclaw.ai/tr/gateway/1password
scraped_at: 2026-07-20
---

Gateway & OpsGateway

OpenClaw, **1Password** ile iki bağımsız şekilde eşleşir:

  * **Yapılandırma gizli bilgileri:** `openclaw.json` içindeki herhangi bir [SecretRef](</tr/gateway/secrets>) alanı, çalışma zamanında `op` CLI aracılığıyla çözümlenebilir; böylece API anahtarları hiçbir zaman yapılandırma dosyasında bulunmaz.
  * **Ajan iş akışları:** paketle birlikte gelen `1password` skill'i, ajanlara kendi görevleri için `op` ile oturum açmayı ve gizli bilgileri okumayı veya enjekte etmeyi öğretir.


## Gereksinimler

  * [1Password CLI](<https://developer.1password.com/docs/cli/get-started/>) (`op`), Gateway ana makinesine yüklenmiş olmalıdır (macOS'ta `brew install 1password-cli`).
  * `op` için bir kimlik doğrulama modu: 
    * **Hizmet hesabı** (ekransız Gateway'ler için önerilir): Gateway hizmet ortamında `OP_SERVICE_ACCOUNT_TOKEN` değişkenini dışa aktarın. Masaüstü uygulaması ve etkileşimli oturum açma gerekmez.
    * **Masaüstü uygulaması entegrasyonu** : 1Password uygulaması, CLI entegrasyonu etkinleştirilmiş olarak aynı makinede çalışır. İlk çağrılar Touch ID'yi veya sistem kimlik doğrulamasını tetikleyebilir.
    * **Bağımsız oturum açma** : `op signin`, her oturumda istem gösterir. Skill aracılığıyla ajanlar için kullanılabilir, ancak ekransız bir Gateway'de yapılandırma gizli bilgilerinin çözümlenmesi için uygun değildir.


## Yapılandırma gizli bilgilerini op ile çözümleme

Bir `op://vault/item/field` başvurusuyla `op read` çalıştıran bir exec gizli bilgi sağlayıcısı tanımlayın, ardından SecretRef destekleyen herhangi bir alanı buna yönlendirin:

json5Copy code
[code]
    {  secrets: {    providers: {      onepassword_openai: {        source: "exec",        command: "/opt/homebrew/bin/op",        allowSymlinkCommand: true, // Homebrew sembolik bağlantılı ikili dosyaları için gereklidir        trustedDirs: ["/opt/homebrew"],        args: ["read", "op://Personal/OpenClaw QA API Key/password"],        passEnv: ["HOME"],        jsonOnly: false,      },    },  },  models: {    providers: {      openai: {        baseUrl: "https://api.openai.com/v1",        models: [{ id: "gpt-5", name: "gpt-5" }],        apiKey: { source: "exec", provider: "onepassword_openai", id: "value" },      },    },  },}
[/code]

Parçaların birlikte çalışma şekli:

  * `command` mutlak bir yol olmalıdır; `trustedDirs` bu dizini güvenilir olarak işaretler ve Homebrew, `op` dosyasını sembolik bağlantı olarak yüklediği için `allowSymlinkCommand` gereklidir.
  * `args`, `op://vault/item/field` başvurusunu olduğu gibi taşır. OpenClaw, `op://` şemasını kendisi ayrıştırmaz; bunu `op` ikili dosyası çözümler.
  * `passEnv`, listelenen değişkenleri Gateway ortamından iletir. Masaüstü uygulaması entegrasyonu `HOME` gerektirir; hizmet hesapları ayrıca Gateway hizmet ortamında `OP_SERVICE_ACCOUNT_TOKEN` bulunmasını gerektirir (bunu `passEnv` içine ekleyin veya yalnızca token'ın yapılandırma dosyasında okunabilir olmasını kabul ediyorsanız `env` aracılığıyla ayarlayın).
  * Tek değerli çıktı için `id: "value"` ayarını koruyun. `jsonOnly: true` ve bir JSON yükü kullanıldığında, bunun yerine alanları bir JSON işaretçisi kimliğiyle adresleyin.
  * Her gizli bilgi için bir sağlayıcı girdisi kullanmak, başvuruların denetlenebilir kalmasını sağlar; sağlayıcıları tüketicilerine göre adlandırın (`onepassword_openai`, `onepassword_telegram`).


Çözümleme sırası, önbelleğe alma ve hata semantiği için [Gateway gizli bilgileri](</tr/gateway/secrets>) sayfasına; SecretRef kabul eden tüm alanlar için [SecretRef Kimlik Bilgisi Yüzeyi](</tr/reference/secretref-credential-surface>) sayfasına bakın.

## Ekransız Gateway'ler için hizmet hesabı kurulumu

  1. 1Password hesabınızda bir hizmet hesabı oluşturun ve yalnızca Gateway'in ihtiyaç duyduğu kasa öğelerine okuma erişimi verin.
  2. `OP_SERVICE_ACCOUNT_TOKEN` değerini Gateway hizmetine sağlayın (launchd plist'i, systemd birimi veya kapsayıcı ortamı).
  3. `"OP_SERVICE_ACCOUNT_TOKEN"` değerini sağlayıcının `passEnv` listesine ekleyin.
  4. Gateway ana makine ortamından doğrulayın: `op whoami`, istem göstermeden hizmet hesabını yazdırmalıdır.


Hizmet hesabıyla okuma işlemleri, kasanın `op://` başvurusunda açıkça adlandırılmasını gerektirir. Hesabın kapsamını sıkı tutun; bu, hamiline ait bir kimlik bilgisidir.

## Ajanlar için 1password skill'i

OpenClaw, ajanları yetkin `op` operatörlerine dönüştüren bir `1password` skill'i paketle sunar: kullanılabilir kimlik doğrulama modunu (hizmet hesabı, masaüstü uygulaması entegrasyonu veya bağımsız oturum açma) algılar, herhangi bir şeyi okumadan önce `op whoami` ile erişimi doğrular ve gizli bilgi değerlerini diske yazmak yerine `op run` / `op inject` kullanımını tercih eder. Skill, `op` ikili dosyasını gerektirir ve eksik olduğunda Homebrew ile yükleme seçeneği sunar.

Ajanlar bunu kendi iş akışlarında, örneğin görevin ortasında bir dağıtım token'ı okumak veya ortam değişkenlerini bir komuta enjekte etmek için kullanır. Yapılandırma gizli bilgilerinin çözümlenmesinden bağımsızdır; Gateway, herhangi bir skill devreye girmeden SecretRef'leri çözümler.

## Güvenlik notları

  * Exec sağlayıcıları aracılığıyla çözümlenen gizli bilgi değerleri Gateway belleğinde kalır; yapılandırma anlık görüntüleri ve `config.get` yanıtları SecretRef alanlarını sansürler.
  * Gizli bilgi değerlerini asla `openclaw.json`, günlüklere veya sohbete koymayın. Öğe adlarını yapılandırmada, değerleri 1Password'da tutun.
  * 1Password denetim izi, her hizmet hesabı okumasını göstererek anahtar döndürme ve olay incelemesini uygulanabilir kılar.


## Sorun giderme

  * `command not found` veya işlem başlatma hataları: mutlak `op` yolunu kullanın ve dizinini `trustedDirs` içine ekleyin.
  * `op` çözümleniyor ancak okuma işlemleri sembolik bağlantı hatalarıyla başarısız oluyor: Homebrew yüklemeleri için `allowSymlinkCommand: true` ayarını yapın.
  * `account is not signed in`: hizmet hesapları için `OP_SERVICE_ACCOUNT_TOKEN` değerinin Gateway hizmetine ulaştığını ve `passEnv` içinde listelendiğini doğrulayın; masaüstü entegrasyonu için uygulamanın çalıştığını ve kilidinin açık olduğunu doğrulayın.
  * İlk okumalar yavaşsa: sağlayıcıdaki `timeoutMs` değerini artırın; `op` soğuk başlatmaları, yoğun ana makinelerde katı zaman aşımlarını aşabilir.


Was this useful?YesNo

Open issue