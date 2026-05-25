---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/tr/providers/github-copilot
scraped_at: 2026-05-25
---

GitHub Copilot, GitHub'ın AI kodlama asistanıdır. GitHub hesabınız ve planınız için Copilot modellerine erişim sağlar. OpenClaw, Copilot'u iki farklı şekilde model sağlayıcısı olarak kullanabilir.

## OpenClaw'da Copilot'u kullanmanın iki yolu

### Yerleşik sağlayıcı (github-copilot)

GitHub belirteci almak için yerel cihazla oturum açma akışını kullanın, ardından OpenClaw çalıştığında bunu Copilot API belirteçleriyle değiştirin. Bu, VS Code gerektirmediği için **varsayılan** ve en basit yoldur.

* ### Oturum açma komutunu çalıştırın

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Bir URL'yi ziyaret etmeniz ve tek kullanımlık bir kod girmeniz istenir. İşlem tamamlanana kadar terminali açık tutun.

* ### Varsayılan model belirleyin

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

Veya yapılandırmada:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Copilot Proxy Plugin'i (copilot-proxy)

Yerel köprü olarak **Copilot Proxy** VS Code uzantısını kullanın. OpenClaw, proxy'nin `/v1` uç noktasıyla iletişim kurar ve orada yapılandırdığınız model listesini kullanır.

## İsteğe bağlı bayraklar

Bayrak | Açıklama  
---|---  
`--yes` | Onay istemini atla  
`--set-default` | Sağlayıcının önerilen varsayılan modelini de uygula  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Etkileşimsiz ilk kurulum

Copilot için zaten bir GitHub OAuth erişim belirteciniz varsa, başsız kurulum sırasında `openclaw onboard --non-interactive` ile içe aktarın:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

`--auth-choice` seçeneğini atlayabilirsiniz; `--github-copilot-token` iletildiğinde GitHub Copilot sağlayıcı kimlik doğrulama seçimi çıkarımsanır. Bayrak atlanırsa, ilk kurulum sırasıyla `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, ardından `GITHUB_TOKEN` değerlerine geri döner. Düz metin yerine `auth-profiles.json` içinde env destekli bir `tokenRef` depolamak için `COPILOT_GITHUB_TOKEN` ayarlanmışken `--secret-input-mode ref` kullanın.

Etkileşimli TTY gerekli

Cihazla oturum açma akışı etkileşimli bir TTY gerektirir. Bunu etkileşimsiz bir betik veya CI işlem hattında değil, doğrudan terminalde çalıştırın.

Model kullanılabilirliği planınıza bağlıdır

Copilot model kullanılabilirliği GitHub planınıza bağlıdır. Bir model reddedilirse başka bir ID deneyin (örneğin `github-copilot/gpt-4.1`).

Copilot API'den canlı katalog yenileme

Cihazla oturum açma (veya env-var) kimlik doğrulama yolu bir GitHub belirtecini çözdükten sonra, OpenClaw model kataloğunu talep üzerine `${baseUrl}/models` üzerinden yeniler (VS Code Copilot'un kullandığı aynı uç nokta); böylece çalışma zamanı manifesto değişimi olmadan hesap başına yetkilendirmeyi ve doğru bağlam pencerelerini izler. Yeni yayımlanan Copilot modelleri OpenClaw yükseltmesi olmadan görünür hale gelir ve bağlam pencereleri gerçek model başına sınırları yansıtır (ör. gpt-5.x serisi için 400k, dahili `claude-opus-*-1m` varyantları için 1M).

Keşif devre dışıysa, kullanıcının GitHub kimlik doğrulama profili yoksa, belirteç değişimi başarısız olursa veya `/models` HTTPS çağrısı hata verirse paketlenen statik katalog görünür yedek olarak kalır. Tamamen statik manifesto kataloğuna güvenmek ve bundan çıkmak için (çevrimdışı / air-gapped senaryolar):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Aktarım seçimi

Claude model ID'leri Anthropic Messages aktarımını otomatik olarak kullanır. GPT, o-series ve Gemini modelleri OpenAI Responses aktarımını korur. OpenClaw doğru aktarımı model ref'e göre seçer.

İstek uyumluluğu

OpenClaw, yerleşik Compaction, araç sonucu ve görüntü takip turları dahil olmak üzere Copilot aktarımlarında Copilot IDE tarzı istek üst bilgileri gönderir. Bu davranış Copilot API'sine karşı doğrulanmadıkça, Copilot için sağlayıcı düzeyinde Responses devamını etkinleştirmez.

Ortam değişkeni çözümleme sırası

OpenClaw, Copilot kimlik doğrulamasını ortam değişkenlerinden aşağıdaki öncelik sırasıyla çözer:

Öncelik | Değişken | Notlar  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | En yüksek öncelik, Copilot'a özgü  
2 | `GH_TOKEN` | GitHub CLI belirteci (yedek)  
3 | `GITHUB_TOKEN` | Standart GitHub belirteci (en düşük)  
  
Birden fazla değişken ayarlandığında OpenClaw en yüksek öncelikli olanı kullanır. Cihazla oturum açma akışı (`openclaw models auth login-github-copilot`) belirtecini kimlik doğrulama profili deposunda saklar ve tüm ortam değişkenlerine göre önceliklidir.

Belirteç depolama

Oturum açma, kimlik doğrulama profili deposunda bir GitHub belirteci saklar ve OpenClaw çalıştığında bunu bir Copilot API belirteciyle değiştirir. Belirteci elle yönetmeniz gerekmez.

## Bellek araması embedding'leri

GitHub Copilot, [bellek araması](</tr/concepts/memory-search>) için embedding sağlayıcısı olarak da hizmet verebilir. Bir Copilot aboneliğiniz varsa ve oturum açtıysanız, OpenClaw bunu ayrı bir API anahtarı olmadan embedding'ler için kullanabilir.

### Otomatik algılama

`memorySearch.provider` `"auto"` olduğunda (varsayılan), GitHub Copilot öncelik 15'te denenir -- yerel embedding'lerden sonra, ancak OpenAI ve diğer ücretli sağlayıcılardan önce. Bir GitHub belirteci kullanılabiliyorsa, OpenClaw kullanılabilir embedding modellerini Copilot API'den keşfeder ve en iyisini otomatik olarak seçer.

### Açık yapılandırma

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Nasıl çalışır

  1. OpenClaw GitHub belirtecinizi çözer (env vars veya kimlik doğrulama profilinden).
  2. Bunu kısa ömürlü bir Copilot API belirteciyle değiştirir.
  3. Kullanılabilir embedding modellerini keşfetmek için Copilot `/models` uç noktasını sorgular.
  4. En iyi modeli seçer (`text-embedding-3-small` tercih edilir).
  5. Embedding isteklerini Copilot `/embeddings` uç noktasına gönderir.


Model kullanılabilirliği GitHub planınıza bağlıdır. Kullanılabilir embedding modeli yoksa, OpenClaw Copilot'u atlar ve sonraki sağlayıcıyı dener.

## İlgili

[**Model seçimi** Sağlayıcıları, model ref'lerini ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**OAuth ve kimlik doğrulama** Kimlik doğrulama ayrıntıları ve kimlik bilgisi yeniden kullanım kuralları. ](</tr/gateway/authentication>)

Was this useful?YesNo