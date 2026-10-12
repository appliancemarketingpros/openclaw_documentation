---
title: 1Password gizli bilgiler aracısı
source_url: https://docs.openclaw.ai/tr/plugins/onepassword
scraped_at: 2026-10-12
---

CapabilitiesPlugin guides

# 1Password gizli bilgiler aracısı

Birlikte gelen `onepassword` plugin'i, aracılara özenle seçilmiş bir 1Password alanları kümesini okumak için politika denetimli tek bir araç sağlar. Varsayılan olarak devre dışıdır ve `plugins.entries.onepassword.config` mevcut olana kadar hiçbir işlem yapmaz.

Bu bir aracı aracıdır, SecretRef sağlayıcısı değildir. Ortam değişkenlerini eklemez veya OpenClaw yapılandırma gizli bilgilerini çözümlemez.

## Güvenlik modeli

  * Yalnızca hizmet hesabı kimlik doğrulaması. Token, yerel bir kimlik bilgileri dosyasında kalır ve `openclaw.json` içinde hiçbir zaman kabul edilmez.
  * Yalnızca özenle seçilmiş kayıt defteri. Aracılar yapılandırılmış kısa adları listeleyebilir, ancak plugin hiçbir zaman bir 1Password kasasını numaralandırmaz.
  * Kısa ad başına `auto`, `approve` veya `deny` politikası.
  * Onay izinlerinin süresi dolar. Önbelleğe alınmış bir değer, geçerli politikayı hiçbir zaman atlamaz.
  * Her erişim girişimi OpenClaw'ın paylaşılan SQLite durumuna kaydedilir. Denetim satırları sağlanan gerekçeyi içerir; gerekçelerde hassas bilgi bulundurmayın. Aracı, getirilen bir değeri veya hizmet token'ını hiçbir zaman bir denetim satırına kopyalamaz.
  * Geçerli araç yürütmesinden sonra, OpenClaw'a ait transkript kalıcılığı başarılı bir `get` değerini redakte edilmiş meta verilerle değiştirir.
  * Değer, söz konusu yürütme sırasında model tarafından görülebilir. Model bunu daha sonraki bir araç çağrısına veya yanıta kopyalarsa bu ayrı kayıt, bu plugin'in kalıcılık kancasının kapsamı dışındadır. Politikaları dar tutun ve modelden bir değeri yinelemesini istemeyin.
  * Plugin, her önbellek kaçırmasında `op` öğesini bir kez çağırır. Hız sınırlarında veya diğer hatalarda yeniden deneme yapmaz.
  * Her `op` çağrısı, 1Password masaüstü uygulaması entegrasyonunu devre dışı bırakan en küçük ortamla (`OP_LOAD_DESKTOP_APP_SETTINGS=false`, `OP_BIOMETRIC_UNLOCK_ENABLED=false`) çalışır; böylece Gateway ana makinesinde yüklü bir 1Password uygulaması hiçbir zaman biyometrik veya macOS izin iletişim kutularını tetiklemez.


Hizmet hesabına yalnızca plugin yapılandırmasında kayıtlı kasa ve öğeler için okuma erişimi verin.

## Başlamadan önce

Şunlar gereklidir:

  * Gateway ana makinesinde 1Password CLI'ın (`op`) yüklü olması
  * seçilen öğelere erişimi olan bir 1Password hizmet hesabı
  * hizmet hesabına ayrılmış bir token dosyası


Birlikte gelen plugin'i etkinleştirin:

bashCopy code
[code]
    openclaw plugins enable onepassword
[/code]

OpenClaw durum dizini altında token dizinini ve dosyasını oluşturun:

bashCopy code
[code]
    mkdir -p ~/.openclaw/credentials/onepasswordchmod 700 ~/.openclaw/credentials/onepasswordprintf '%s' "$OP_SERVICE_ACCOUNT_TOKEN" > \  ~/.openclaw/credentials/onepassword/service-account-tokenchmod 600 ~/.openclaw/credentials/onepassword/service-account-tokenunset OP_SERVICE_ACCOUNT_TOKEN
[/code]

`OPENCLAW_STATE_DIR` ayarlandığında `~/.openclaw` değerini bu dizinle değiştirin. Token dosyası grup veya diğer kullanıcılar tarafından okunabilir ya da yazılabilir olduğunda plugin bir kez uyarır.

## Kayıtlı gizli bilgileri yapılandırma

`openclaw.json` dosyasına plugin yapılandırmasını ekleyin:

jsoncCopy code
[code]
    {  "plugins": {    "entries": {      "onepassword": {        "enabled": true,        "config": {          "vault": "Automation",          "defaultPolicy": "approve",          "cacheTtlSeconds": 300,          "grantTtlHours": 720,          "opTimeoutMs": 15000,          "items": {            "repository-token": {              "item": "Repository automation token",              "field": "credential",              "policy": "approve",              "description": "Token for repository automation",            },            "model-key": {              "item": "Model provider key",              "vault": "Agent credentials",              "policy": "auto",            },          },        },      },    },  },}
[/code]

Kısa adlar küçük harf, sayı ve kısa çizgi kullanır; bir harf veya sayıyla başlar ve en fazla 64 karakter içerir. Bir kayıt defteri en fazla 32 kısa ad içerebilir; açıklamalar en fazla 200 karakter olabilir. `field` tek bir alan etiketi veya kimliği kabul eder, virgül içermemelidir ve varsayılan olarak `credential` değerini kullanır. Öğe düzeyindeki bir `vault`, varsayılan kasayı geçersiz kılar. `opBin`, `op` yürütülebilir dosyasının mutlak yolunu ayarlayabilir; aksi hâlde plugin, `op` öğesini `PATH` üzerinden çözümler. Öğe başlıkları kısa çizgiyle başlamamalıdır.

## Aracı aracını kullanma

Aracın adı `onepassword` şeklindedir.

Kayıtlı kısa adları listeleyin:

jsonCopy code
[code]
    { "action": "list" }
[/code]

Sonuç yalnızca kısa adı, açıklamayı, politikayı ve kalıcı bir iznin etkin olup olmadığını içerir. Hiçbir zaman gizli bir değer içermez ve 1Password'ü sorgulamaz.

Bir gizli bilgi isteyin:

jsonCopy code
[code]
    {  "action": "get",  "slug": "repository-token",  "reason": "Authenticate the requested repository operation"}
[/code]

`reason` zorunludur, boş olmamalıdır ve 300 karakterle sınırlıdır. Başarılı bir `get`, değerin yanı sıra yapılandırılmış kısa adı, öğe başlığını ve alan etiketini döndürür.

Araç şeması ayrıca dahili bir `authorizationNonce` parametresi bildirir. Politika katmanı, yetkilendirmeyi yürütülen araç çağrısına aktarmak için isteği değerlendirdikten sonra bunu ekler. Bunu hiçbir zaman elle ayarlamayın: politika kancası sağlanan her değerin üzerine yazar ve bilinmeyen bir değer isteğin başarısız olmasına neden olur.

## Politika kademeleri ve onaylar

  * `auto`: hemen getirir ve isteği denetim kaydına alır.
  * `deny`: isteği engeller ve denetim kaydına alır.
  * `approve`: süresi dolmamış kalıcı bir izin kullanır veya bir kişiden bir kez izin vermesini, her zaman izin vermesini ya da reddetmesini ister.


Bir kez izin verme yalnızca geçerli araç çağrısını yetkilendirir. Her zaman izin verme, söz konusu aracı ve kısa ad için SQLite'a kalıcı bir izin yazar; diğer aracılar kendi onaylarını almalıdır. OpenClaw, her zaman izin verme seçeneğini yalnızca çağıranın somut bir aracı kimliği olduğunda sunar. İzin, varsayılan olarak 720 saat olan `grantTtlHours` sonrasında sona erer. Çözülmemiş veya zaman aşımına uğramış bir onay isteği reddeder; en uzun onay bekleme süresi 600 saniyedir. Plugin en fazla 1.024 kalıcı izin tutar; bu sınıra ulaşıldığında en eski izin kaldırılır ve ilgili aracının bir sonraki erişimi onaylaması gerekir.

Değerlendirilen her yetkilendirme tek kullanımlıktır ve paylaşılan SQLite durumu üzerinden yürütülen araç çağrısına aktarılır; böylece Gateway sürecinde birden fazla plugin örneği etkin olduğunda da aktarım çalışır. Kullanılmayan yetkilendirmelerin süresi 600 saniyelik onay penceresinden sonra dolar.

Bellek içi önbellek varsayılan olarak 300 saniyedir ve yapılandırılmış kısa ad kayıt defteriyle sınırlandırılır. Devre dışı bırakmak için `cacheTtlSeconds` değerini `0` olarak ayarlayın. Politika, her önbellek aramasından önce değerlendirilir ve önbellek isabetleri denetim kaydına alınır. Çalışma zamanı yapılandırmasının yeniden yüklenmesi her politika ve yürütme sınırında geçerli olur; plugin'in devre dışı bırakılması veya bir kısa adın kaldırılması, reddedilmesi ya da başka bir hedefe yönlendirilmesi bekleyen yetkilendirmeleri ve önbelleğe alınmış değerleri geçersiz kılar.

## Durumu ve denetim geçmişini inceleme

Hazır olma durumunu ve kayıt defteri sayılarını gösterin:

bashCopy code
[code]
    openclaw onepassword status
[/code]

Bu komut token dosyasının mevcut olup olmadığını, `op` öğesinin çözümlenip çözümlenmediğini ve yolunu, kayıtlı öğe sayısını ve politika başına sayıları bildirir. Token'ı veya gizli değerleri hiçbir zaman okumaz ya da yazdırmaz.

En son 50 denetim satırını gösterin:

bashCopy code
[code]
    openclaw onepassword auditopenclaw onepassword audit --limit 100
[/code]

Satırlar en yeniden en eskiye sıralanır ve zaman damgasını, aracıyı, kısa adı, sonucu, girişim başarısız olduğunda bir `errorCode` değerini ve kısaltılmış gerekçeyi gösterir. Gerekçe sağlandığı biçimde saklanır; aracı, getirilen değeri hiçbir zaman denetim günlüğüne eklemez.

## 1Password CLI davranışı

Her önbellek kaçırması, yapılandırılmış öğe, kasa ve tam alan seçicisi, JSON çıktısı, sınırlı bir zaman aşımı ve `--cache=false` ile `op item get` öğesini çalıştırır. Alt süreç, öğenin tamamı yerine yalnızca ilgili alanı alır. Alt süreç ortamında yalnızca `OP_SERVICE_ACCOUNT_TOKEN` ve `HOME` bulunur.

Plugin tek bir girişimde bulunur. `RATE_LIMITED` hataları, daha sonraki bir aracı isteğinden önce beklenerek ele alınmalıdır; plugin otomatik bir yeniden deneme döngüsü oluşturmaz.

## Hata kodları

Başarısız girişimler, araç sonucunda ve denetim satırında kapalı bir hata kodu taşır.

1Password erişim hataları:

Kod | Anlamı  
---|---  
`TOKEN_MISSING` | Token dosyası eksik veya boş  
`OP_NOT_FOUND` | `op` ikili dosyası çözümlenemedi  
`ITEM_NOT_FOUND` | Yapılandırılmış öğe kasada değil  
`FIELD_NOT_FOUND` | Yapılandırılmış alan öğede yok; kullanılabilir etiketler listelenir  
`RATE_LIMITED` | 1Password hizmet hesabı hız sınırına ulaşıldı  
`AUTH_FAILED` | Hizmet hesabı kimlik doğrulaması başarısız oldu  
`TIMEOUT` | `op`, `opTimeoutMs` değerini aştı  
`OP_ERROR` | Diğer tüm `op` hataları veya geçersiz çıktı  
  
Politika ve doğrulama hataları:

Kod | Anlamı  
---|---  
`INVALID_ACTION`, `INVALID_REASON`, `INVALID_SLUG` | İstek, girdi doğrulamasında başarısız oldu  
`UNKNOWN_SLUG` | Kısa ad, yapılandırılmış kayıt defterinde değil  
`TOOL_CALL_ID_MISSING` | Çağrı, araç çağrısı kimliği olmadan geldi  
`POLICY_NOT_EVALUATED` | Bu çağrı için eşleşen yetkilendirme yok; istek politika tarafından onaylanmadı  
`POLICY_CHANGED` | Yapılandırma, onay ile yürütme arasında değişti  
`GRANT_EXPIRED` | Kalıcı iznin süresi yürütmeden önce doldu  
`APPROVAL_CANCELLED` | Çalıştırma, onay beklemedeyken iptal edildi  
  
Was this useful?YesNo

Open issue