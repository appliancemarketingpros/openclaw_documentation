---
title: Skills yapılandırması
source_url: https://docs.openclaw.ai/tr/tools/skills-config
scraped_at: 2026-05-25
---

Skills yükleyici/kurulum yapılandırmasının çoğu `~/.openclaw/openclaw.json` içindeki `skills` altında bulunur. Aracıya özel skill görünürlüğü `agents.defaults.skills` ve `agents.list[].skills` altında bulunur.

json5Copy code
[code]
    {  skills: {    allowBundled: ["gemini", "peekaboo"],    load: {      extraDirs: ["~/Projects/agent-scripts/skills", "~/Projects/oss/some-skill-pack/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],      watch: true,      watchDebounceMs: 250,    },    install: {      preferBrew: true,      nodeManager: "npm", // npm | pnpm | yarn | bun (Gateway runtime still Node; bun not recommended)      allowUploadedArchives: false,    },    entries: {      "image-lab": {        enabled: true,        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" }, // or plaintext string        env: {          GEMINI_API_KEY: "GEMINI_KEY_HERE",        },      },      peekaboo: { enabled: true },      sag: { enabled: false },    },  },}
[/code]

Yerleşik görüntü oluşturma/düzenleme için `agents.defaults.imageGenerationModel` ile temel `image_generate` aracını tercih edin. `skills.entries.*` yalnızca özel veya üçüncü taraf skill iş akışları içindir.

Belirli bir görüntü sağlayıcısı/modeli seçerseniz, o sağlayıcının kimlik doğrulamasını/API anahtarını da yapılandırın. Tipik örnekler: `google/*` için `GEMINI_API_KEY` veya `GOOGLE_API_KEY`, `openai/*` için `OPENAI_API_KEY` ve `fal/*` için `FAL_KEY`.

Örnekler:

  * Yerel Nano Banana Pro tarzı kurulum: `agents.defaults.imageGenerationModel.primary: "google/gemini-3-pro-image-preview"`
  * Yerel fal kurulumu: `agents.defaults.imageGenerationModel.primary: "fal/fal-ai/flux/dev"`


## Aracı skill izin listeleri

Aynı makine/çalışma alanı skill köklerini, ancak aracı başına farklı bir görünür skill kümesini istediğinizde aracı yapılandırmasını kullanın.

json5Copy code
[code]
    {  agents: {    defaults: {      skills: ["github", "weather"],    },    list: [      { id: "writer" }, // inherits defaults -> github, weather      { id: "docs", skills: ["docs-search"] }, // replaces defaults      { id: "locked-down", skills: [] }, // no skills    ],  },}
[/code]

Kurallar:

  * `agents.defaults.skills`: `agents.list[].skills` değerini atlayan aracılar için paylaşılan temel izin listesi.
  * Skills varsayılan olarak sınırsız kalsın istiyorsanız `agents.defaults.skills` değerini atlayın.
  * `agents.list[].skills`: bu aracı için açık nihai skill kümesi; varsayılanlarla birleştirmez.
  * `agents.list[].skills: []`: bu aracı için hiçbir skill göstermez.


## Alanlar

  * Yerleşik skill kökleri her zaman `~/.openclaw/skills`, `~/.agents/skills`, `<workspace>/.agents/skills` ve `<workspace>/skills` içerir.
  * `allowBundled`: yalnızca **paketlenmiş** skill'ler için isteğe bağlı izin listesi. Ayarlandığında, yalnızca listedeki paketlenmiş skill'ler uygun olur (yönetilen, aracı ve çalışma alanı skill'leri etkilenmez).
  * `load.extraDirs`: taranacak ek skill dizinleri (en düşük öncelik).
  * `load.allowSymlinkTargets`: sembolik bağlantılı skill klasörlerinin, sembolik bağlantı o hedef kökün dışında bulunsa bile çözümlenebileceği güvenilir gerçek hedef dizinler. Bunu `~/.agents/skills/manager -> ~/Projects/manager/skills` gibi kasıtlı kardeş repo düzenleri için kullanın.
  * `load.watch`: skill klasörlerini izleyin ve Skills anlık görüntüsünü yenileyin (varsayılan: true).
  * `load.watchDebounceMs`: skill izleyici olayları için milisaniye cinsinden bekletme (varsayılan: 250).
  * `install.preferBrew`: mevcut olduğunda brew kurucularını tercih edin (varsayılan: true).
  * `install.nodeManager`: node kurucu tercihi (`npm` | `pnpm` | `yarn` | `bun`, varsayılan: npm). Bu yalnızca **skill kurulumlarını** etkiler; Gateway çalışma zamanı hâlâ Node olmalıdır (Bun, WhatsApp/Telegram için önerilmez). 
    * `openclaw setup --node-manager` daha dardır ve şu anda `npm`, `pnpm` veya `bun` kabul eder. Yarn destekli skill kurulumları istiyorsanız `skills.install.nodeManager: "yarn"` değerini elle ayarlayın.
  * `install.allowUploadedArchives`: güvenilir `operator.admin` Gateway istemcilerinin `skills.upload.*` üzerinden hazırlanmış özel zip arşivlerini kurmasına izin verin (varsayılan: false). Bu yalnızca yüklenen arşiv yolunu etkinleştirir; normal ClawHub kurulumları bunu gerektirmez.
  * `entries.<skillKey>`: skill başına geçersiz kılmalar.
  * `agents.defaults.skills`: `agents.list[].skills` değerini atlayan aracılar tarafından devralınan isteğe bağlı varsayılan skill izin listesi.
  * `agents.list[].skills`: isteğe bağlı, aracı başına nihai skill izin listesi; açık listeler devralınan varsayılanları birleştirmek yerine değiştirir.


## Sembolik bağlantılı kardeş repolar

Varsayılan olarak, her skill kökü bir kapsama sınırıdır. `~/.agents/skills` altındaki bir skill klasörü, `~/.agents/skills` dışına çözümlenen bir sembolik bağlantıysa, OpenClaw bunu atlar ve `Skipping escaped skill path outside its configured root` kaydını yazar.

Sembolik bağlantı düzenini koruyun ve yalnızca güvenilir hedef köke izin verin:

json5Copy code
[code]
    {  skills: {    load: {      extraDirs: ["~/Projects/manager/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],    },  },}
[/code]

Bu yapılandırmayla, `~/.agents/skills/manager -> ~/Projects/manager/skills` gibi bir sembolik bağlantı realpath çözümlemesinden sonra kabul edilir. `extraDirs` kardeş repoyu doğrudan da tarar; `allowSymlinkTargets` ise mevcut aracı-skill düzenleri için sembolik bağlantılı yolu korur. Hedef girdileri dar tutun; o kök altındaki her skill ağacına güvenilmediği sürece `~` veya `~/Projects` gibi geniş köklere işaret etmeyin.

Skill başına alanlar:

  * `enabled`: paketlenmiş/kurulu olsa bile bir skill'i devre dışı bırakmak için `false` olarak ayarlayın.
  * `env`: aracı çalıştırması için enjekte edilen ortam değişkenleri (yalnızca zaten ayarlı değilse).
  * `apiKey`: birincil env var bildiren skill'ler için isteğe bağlı kolaylık. Düz metin dizesini veya SecretRef nesnesini (`{ source, provider, id }`) destekler.


## Notlar

  * `entries` altındaki anahtarlar varsayılan olarak skill adına eşlenir. Bir skill `metadata.openclaw.skillKey` tanımlıyorsa bunun yerine o anahtarı kullanın.
  * Yükleme önceliği: `<workspace>/skills` → `<workspace>/.agents/skills` → `~/.agents/skills` → `~/.openclaw/skills` → paketlenmiş skill'ler → `skills.load.extraDirs`.
  * İzleyici etkin olduğunda skill değişiklikleri bir sonraki aracı turunda alınır.


### Korumalı alan skill'leri ve env var'lar

Bir oturum **korumalı alandaysa** , skill süreçleri yapılandırılmış korumalı alan arka ucunun içinde çalışır. Korumalı alan, ana makine `process.env` değerini devralmaz.

Şunlardan birini kullanın:

  * Docker arka ucu için `agents.defaults.sandbox.docker.env` (veya aracı başına `agents.list[].sandbox.docker.env`).
  * Env'i özel korumalı alan imajınıza veya uzak korumalı alan ortamınıza dahil edin.


## İlgili

[**Skills** Skill'lerin ne olduğu ve nasıl yüklendikleri. ](</tr/tools/skills>) [**Creating skills** Özel skill paketleri yazma. ](</tr/tools/creating-skills>) [**Slash commands** Yerel komut kataloğu ve sohbet yönergeleri. ](</tr/tools/slash-commands>) [**Configuration reference** Tam `skills` ve `agents.skills` şeması. ](</tr/gateway/configuration-reference>)

Was this useful?YesNo