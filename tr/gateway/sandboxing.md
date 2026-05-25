---
title: Korumalı Alan
source_url: https://docs.openclaw.ai/tr/gateway/sandboxing
scraped_at: 2026-05-25
---

OpenClaw, etki alanını daraltmak için **araçları sandbox backend'leri içinde** çalıştırabilir. Bu **isteğe bağlıdır** ve yapılandırmayla (`agents.defaults.sandbox` veya `agents.list[].sandbox`) kontrol edilir. Sandbox kapalıysa araçlar host üzerinde çalışır. Gateway host üzerinde kalır; araç yürütme etkinleştirildiğinde yalıtılmış bir sandbox içinde çalışır.

## Sandbox'a alınanlar

  * Araç yürütme (`exec`, `read`, `write`, `edit`, `apply_patch`, `process` vb.).
  * İsteğe bağlı sandbox tarayıcısı (`agents.defaults.sandbox.browser`).


Sandbox tarayıcısı ayrıntıları

  * Varsayılan olarak sandbox tarayıcısı, tarayıcı aracı ihtiyaç duyduğunda otomatik başlatılır (CDP'nin erişilebilir olmasını sağlar). `agents.defaults.sandbox.browser.autoStart` ve `agents.defaults.sandbox.browser.autoStartTimeoutMs` ile yapılandırın.
  * Varsayılan olarak sandbox tarayıcısı container'ları, global `bridge` ağı yerine özel bir Docker ağı (`openclaw-sandbox-browser`) kullanır. `agents.defaults.sandbox.browser.network` ile yapılandırın.
  * İsteğe bağlı `agents.defaults.sandbox.browser.cdpSourceRange`, container kenarındaki CDP girişini bir CIDR izin listesiyle sınırlar (örneğin `172.21.0.1/32`).
  * noVNC gözlemci erişimi varsayılan olarak parolayla korunur; OpenClaw, yerel bir bootstrap sayfası sunan ve noVNC'yi parolayla URL parçasında (sorgu/header günlüklerinde değil) açan kısa ömürlü bir token URL'si üretir.
  * `agents.defaults.sandbox.browser.allowHostControl`, sandbox'a alınmış oturumların host tarayıcısını açıkça hedeflemesine izin verir.
  * İsteğe bağlı izin listeleri `target: "custom"` için geçit görevi görür: `allowedControlUrls`, `allowedControlHosts`, `allowedControlPorts`.


Sandbox'a alınmayanlar:

  * Gateway sürecinin kendisi.
  * Sandbox dışında çalışmasına açıkça izin verilen herhangi bir araç (örn. `tools.elevated`). 
    * **Yükseltilmiş exec, sandbox'ı atlar ve yapılandırılmış kaçış yolunu kullanır (varsayılan olarak`gateway` veya exec hedefi `node` olduğunda `node`).**
    * Sandbox kapalıysa `tools.elevated` yürütmeyi değiştirmez (zaten host üzerindedir). Bkz. [Yükseltilmiş Mod](</tr/tools/elevated>).


## Modlar

`agents.defaults.sandbox.mode`, sandbox'ın **ne zaman** kullanılacağını kontrol eder:

### off

Sandbox yok.

### non-main

Yalnızca **ana olmayan** oturumları sandbox'a alır (normal sohbetlerin host üzerinde olmasını istiyorsanız varsayılan).

`"non-main"`, agent id'ye değil `session.mainKey` değerine (varsayılan `"main"`) dayanır. Grup/kanal oturumları kendi anahtarlarını kullanır, bu yüzden ana olmayan sayılırlar ve sandbox'a alınırlar.

### all

Her oturum bir sandbox içinde çalışır.

## Kapsam

`agents.defaults.sandbox.scope`, **kaç container** oluşturulacağını kontrol eder:

  * `"agent"` (varsayılan): agent başına bir container.
  * `"session"`: oturum başına bir container.
  * `"shared"`: sandbox'a alınmış tüm oturumlar tarafından paylaşılan bir container.


## Backend

`agents.defaults.sandbox.backend`, sandbox'ı **hangi runtime'ın** sağlayacağını kontrol eder:

  * `"docker"` (sandbox etkinleştirildiğinde varsayılan): yerel Docker destekli sandbox runtime'ı.
  * `"ssh"`: genel SSH destekli uzak sandbox runtime'ı.
  * `"openshell"`: OpenShell destekli sandbox runtime'ı.


SSH'ye özgü yapılandırma `agents.defaults.sandbox.ssh` altında bulunur. OpenShell'e özgü yapılandırma `plugins.entries.openshell.config` altında bulunur.

### Backend seçme

| Docker | SSH | OpenShell  
---|---|---|---  
**Nerede çalışır** | Yerel container | SSH ile erişilebilir herhangi bir host | OpenShell tarafından yönetilen sandbox  
**Kurulum** | `scripts/sandbox-setup.sh` | SSH anahtarı + hedef host | OpenShell Plugin etkin  
**Çalışma alanı modeli** | Bind-mount veya kopya | Uzak-kanonik (bir kez tohumla) | `mirror` veya `remote`  
**Ağ kontrolü** | `docker.network` (varsayılan: yok) | Uzak host'a bağlı | OpenShell'e bağlı  
**Tarayıcı sandbox'ı** | Desteklenir | Desteklenmez | Henüz desteklenmiyor  
**Bind mount'lar** | `docker.binds` | N/A | N/A  
**En uygun olduğu yer** | Yerel geliştirme, tam yalıtım | Uzak bir makineye aktarma | İsteğe bağlı iki yönlü senkronizasyonla yönetilen uzak sandbox'lar  
  
### Docker backend'i

Sandbox varsayılan olarak kapalıdır. Sandbox'ı etkinleştirir ve bir backend seçmezseniz OpenClaw Docker backend'ini kullanır. Araçları ve sandbox tarayıcılarını Docker daemon socket'i (`/var/run/docker.sock`) üzerinden yerel olarak yürütür. Sandbox container yalıtımı Docker namespace'leri tarafından belirlenir.

Host GPU'larını Docker sandbox'larına göstermek için `agents.defaults.sandbox.docker.gpus` değerini veya agent başına `agents.list[].sandbox.docker.gpus` geçersiz kılmasını ayarlayın. Değer, Docker'ın `--gpus` bayrağına ayrı bir argüman olarak geçirilir; örneğin `"all"` veya `"device=GPU-uuid"` ve NVIDIA Container Toolkit gibi uyumlu bir host runtime'ı gerektirir.

### SSH backend'i

OpenClaw'ın `exec`, dosya araçları ve medya okumalarını rastgele bir SSH erişilebilir makinede sandbox'a almasını istediğinizde `backend: "ssh"` kullanın.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "ssh",        scope: "session",        workspaceAccess: "rw",        ssh: {          target: "user@gateway-host:22",          workspaceRoot: "/tmp/openclaw-sandboxes",          strictHostKeyChecking: true,          updateHostKeys: true,          identityFile: "~/.ssh/id_ed25519",          certificateFile: "~/.ssh/id_ed25519-cert.pub",          knownHostsFile: "~/.ssh/known_hosts",          // Or use SecretRefs / inline contents instead of local files:          // identityData: { source: "env", provider: "default", id: "SSH_IDENTITY" },          // certificateData: { source: "env", provider: "default", id: "SSH_CERTIFICATE" },          // knownHostsData: { source: "env", provider: "default", id: "SSH_KNOWN_HOSTS" },        },      },    },  },}
[/code]

Nasıl çalışır

  * OpenClaw, `sandbox.ssh.workspaceRoot` altında kapsam başına bir uzak kök oluşturur.
  * Oluşturma veya yeniden oluşturma sonrasındaki ilk kullanımda OpenClaw, bu uzak çalışma alanını yerel çalışma alanından bir kez tohumlar.
  * Bundan sonra `exec`, `read`, `write`, `edit`, `apply_patch`, prompt medya okumaları ve gelen medya hazırlama doğrudan SSH üzerinden uzak çalışma alanına karşı çalışır.
  * OpenClaw uzak değişiklikleri yerel çalışma alanına otomatik olarak geri senkronize etmez.

Kimlik doğrulama materyali

  * `identityFile`, `certificateFile`, `knownHostsFile`: mevcut yerel dosyaları kullanır ve bunları OpenSSH yapılandırması üzerinden geçirir.
  * `identityData`, `certificateData`, `knownHostsData`: inline string'ler veya SecretRefs kullanır. OpenClaw bunları normal secrets runtime snapshot'ı üzerinden çözer, `0600` ile geçici dosyalara yazar ve SSH oturumu sona erdiğinde siler.
  * Aynı öğe için hem `*File` hem de `*Data` ayarlanmışsa, o SSH oturumu için `*Data` kazanır.

Uzak-kanonik sonuçlar

Bu bir **uzak-kanonik** modeldir. İlk tohumlamadan sonra uzak SSH çalışma alanı gerçek sandbox durumu olur.

  * Tohum adımından sonra OpenClaw dışında yapılan host-yerel düzenlemeler, sandbox'ı yeniden oluşturana kadar uzaktan görünmez.
  * `openclaw sandbox recreate`, kapsam başına uzak kökü siler ve sonraki kullanımda yeniden yerelden tohumlar.
  * Tarayıcı sandbox'ı SSH backend'inde desteklenmez.
  * `sandbox.docker.*` ayarları SSH backend'i için geçerli değildir.


### OpenShell backend'i

OpenClaw'ın araçları OpenShell tarafından yönetilen uzak bir ortamda sandbox'a almasını istediğinizde `backend: "openshell"` kullanın. Tam kurulum rehberi, yapılandırma referansı ve çalışma alanı modu karşılaştırması için özel [OpenShell sayfasına](</tr/gateway/openshell>) bakın.

OpenShell, genel SSH backend'iyle aynı çekirdek SSH aktarımını ve uzak dosya sistemi köprüsünü yeniden kullanır ve OpenShell'e özgü lifecycle (`sandbox create/get/delete`, `sandbox ssh-config`) ile isteğe bağlı `mirror` çalışma alanı modunu ekler.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "openshell",        scope: "session",        workspaceAccess: "rw",      },    },  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "remote", // mirror | remote          remoteWorkspaceDir: "/sandbox",          remoteAgentWorkspaceDir: "/agent",        },      },    },  },}
[/code]

OpenShell modları:

  * `mirror` (varsayılan): yerel çalışma alanı kanonik kalır. OpenClaw, exec öncesinde yerel dosyaları OpenShell'e senkronize eder ve exec sonrasında uzak çalışma alanını geri senkronize eder.
  * `remote`: sandbox oluşturulduktan sonra OpenShell çalışma alanı kanoniktir. OpenClaw uzak çalışma alanını yerel çalışma alanından bir kez tohumlar, ardından dosya araçları ve exec, değişiklikleri geri senkronize etmeden doğrudan uzak sandbox'a karşı çalışır.


Uzak aktarım ayrıntıları

  * OpenClaw, `openshell sandbox ssh-config <name>` üzerinden OpenShell'den sandbox'a özgü SSH yapılandırması ister.
  * Core bu SSH yapılandırmasını geçici bir dosyaya yazar, SSH oturumunu açar ve `backend: "ssh"` tarafından kullanılan aynı uzak dosya sistemi köprüsünü yeniden kullanır.
  * Yalnızca `mirror` modunda lifecycle farklıdır: exec öncesinde yerelden uzağa senkronize et, ardından exec sonrasında geri senkronize et.

Mevcut OpenShell sınırlamaları

  * sandbox tarayıcısı henüz desteklenmiyor
  * `sandbox.docker.binds`, OpenShell backend'inde desteklenmiyor
  * `sandbox.docker.*` altındaki Docker'a özgü runtime ayarları yalnızca Docker backend'i için geçerli olmaya devam eder


#### Çalışma alanı modları

OpenShell'in iki çalışma alanı modeli vardır. Pratikte en önemli kısım budur.

### mirror (yerel kanonik)

**Yerel çalışma alanının kanonik kalmasını** istediğinizde `plugins.entries.openshell.config.mode: "mirror"` kullanın.

Davranış:

  * `exec` öncesinde OpenClaw yerel çalışma alanını OpenShell korumalı alanına senkronize eder.
  * `exec` sonrasında OpenClaw uzak çalışma alanını yerel çalışma alanına geri senkronize eder.
  * Dosya araçları yine korumalı alan köprüsü üzerinden çalışır, ancak yerel çalışma alanı turlar arasında doğruluk kaynağı olarak kalır.


Bunu şu durumlarda kullanın:

  * dosyaları OpenClaw dışında yerel olarak düzenlediğinizde ve bu değişikliklerin korumalı alanda otomatik olarak görünmesini istediğinizde
  * OpenShell korumalı alanının mümkün olduğunca Docker arka ucu gibi davranmasını istediğinizde
  * ana makine çalışma alanının her exec turundan sonra korumalı alan yazmalarını yansıtmasını istediğinizde


Dezavantaj: exec öncesi ve sonrasında ek senkronizasyon maliyeti.

### remote (OpenShell canonical)

**OpenShell çalışma alanının kanonik hale gelmesini** istediğinizde `plugins.entries.openshell.config.mode: "remote"` kullanın.

Davranış:

  * Korumalı alan ilk kez oluşturulduğunda, OpenClaw uzak çalışma alanını yerel çalışma alanından bir kez tohumlar.
  * Bundan sonra `exec`, `read`, `write`, `edit` ve `apply_patch` doğrudan uzak OpenShell çalışma alanına karşı çalışır.
  * OpenClaw, exec sonrasında uzak değişiklikleri yerel çalışma alanına geri senkronize **etmez**.
  * İstem zamanındaki medya okumaları yine çalışır; çünkü dosya ve medya araçları yerel bir ana makine yolu varsaymak yerine korumalı alan köprüsü üzerinden okur.
  * Aktarım, `openshell sandbox ssh-config` tarafından döndürülen OpenShell korumalı alanına SSH üzerinden yapılır.


Önemli sonuçlar:

  * Tohumlama adımından sonra ana makinede OpenClaw dışında dosyaları düzenlerseniz, uzak korumalı alan bu değişiklikleri otomatik olarak **görmez**.
  * Korumalı alan yeniden oluşturulursa, uzak çalışma alanı yerel çalışma alanından tekrar tohumlanır.
  * `scope: "agent"` veya `scope: "shared"` ile bu uzak çalışma alanı aynı kapsamda paylaşılır.


Bunu şu durumlarda kullanın:

  * korumalı alan öncelikle uzak OpenShell tarafında yaşamalıysa
  * tur başına senkronizasyon ek yükünü azaltmak istiyorsanız
  * ana makineye yerel düzenlemelerin uzak korumalı alan durumunun sessizce üzerine yazmasını istemiyorsanız


Korumalı alanı geçici bir yürütme ortamı olarak düşünüyorsanız `mirror` seçin. Korumalı alanı gerçek çalışma alanı olarak düşünüyorsanız `remote` seçin.

#### OpenShell yaşam döngüsü

OpenShell korumalı alanları yine normal korumalı alan yaşam döngüsü üzerinden yönetilir:

  * `openclaw sandbox list`, Docker çalışma zamanlarının yanı sıra OpenShell çalışma zamanlarını da gösterir
  * `openclaw sandbox recreate` geçerli çalışma zamanını siler ve OpenClaw'ın sonraki kullanımda bunu yeniden oluşturmasına izin verir
  * temizleme mantığı da arka uç farkındadır


`remote` modu için yeniden oluşturma özellikle önemlidir:

  * yeniden oluşturma, o kapsam için kanonik uzak çalışma alanını siler
  * sonraki kullanım, yerel çalışma alanından yeni bir uzak çalışma alanı tohumlar


`mirror` modu için yeniden oluşturma, yerel çalışma alanı zaten kanonik kaldığından esas olarak uzak yürütme ortamını sıfırlar.

## Çalışma alanı erişimi

`agents.defaults.sandbox.workspaceAccess`, **korumalı alanın neyi görebileceğini** denetler:

### none (default)

Araçlar `~/.openclaw/sandboxes` altında bir korumalı alan çalışma alanı görür.

### ro

Ajan çalışma alanını `/agent` konumuna salt okunur olarak bağlar (`write`/`edit`/`apply_patch` devre dışı kalır).

### rw

Ajan çalışma alanını `/workspace` konumuna okuma/yazma olarak bağlar.

OpenShell arka ucu ile:

  * `mirror` modu, exec turları arasında yerel çalışma alanını yine kanonik kaynak olarak kullanır
  * `remote` modu, ilk tohumlamadan sonra uzak OpenShell çalışma alanını kanonik kaynak olarak kullanır
  * `workspaceAccess: "ro"` ve `"none"` yazma davranışını aynı şekilde kısıtlamaya devam eder


Gelen medya etkin korumalı alan çalışma alanına (`media/inbound/*`) kopyalanır.

## Özel bağlama noktaları

`agents.defaults.sandbox.docker.binds`, ek ana makine dizinlerini konteynere bağlar. Biçim: `host:container:mode` (ör. `"/home/user/source:/source:rw"`).

Global ve ajan başına bağlamalar **birleştirilir** (değiştirilmez). `scope: "shared"` altında, ajan başına bağlamalar yok sayılır.

`agents.defaults.sandbox.browser.binds`, ek ana makine dizinlerini yalnızca **korumalı alan tarayıcı** konteynerine bağlar.

  * Ayarlandığında (`[]` dahil), tarayıcı konteyneri için `agents.defaults.sandbox.docker.binds` değerinin yerine geçer.
  * Atlandığında, tarayıcı konteyneri `agents.defaults.sandbox.docker.binds` değerine geri döner (geriye dönük uyumlu).


Örnek (salt okunur kaynak + ek bir veri dizini):

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        docker: {          binds: ["/home/user/source:/source:ro", "/var/data/myapp:/data:ro"],        },      },    },    list: [      {        id: "build",        sandbox: {          docker: {            binds: ["/mnt/cache:/cache:rw"],          },        },      },    ],  },}
[/code]

## İmajlar ve kurulum

Varsayılan Docker imajı: `openclaw-sandbox:bookworm-slim`

* ### Varsayılan imajı oluştur

Bir kaynak checkout üzerinden:

bashCopy code
[code]
    scripts/sandbox-setup.sh
[/code]

Bir npm kurulumundan (kaynak checkout gerekmez):

bashCopy code
[code]
    docker build -t openclaw-sandbox:bookworm-slim - <<'DOCKERFILE'FROM debian:bookworm-slimENV DEBIAN_FRONTEND=noninteractiveRUN apt-get update && apt-get install -y --no-install-recommends \  bash ca-certificates curl git jq python3 ripgrep \  && rm -rf /var/lib/apt/lists/*RUN useradd --create-home --shell /bin/bash sandboxUSER sandboxWORKDIR /home/sandboxCMD ["sleep", "infinity"]DOCKERFILE
[/code]

Varsayılan imaj Node içermez. Bir skill Node (veya diğer çalışma zamanları) gerektiriyorsa, özel bir imaja gömün ya da `sandbox.docker.setupCommand` üzerinden kurun (ağ çıkışı + yazılabilir kök + root kullanıcı gerektirir).

`openclaw-sandbox:bookworm-slim` eksik olduğunda OpenClaw sessizce düz `debian:bookworm-slim` ile değiştirmez. Varsayılan imajı hedefleyen korumalı alan çalıştırmaları, siz imajı oluşturana kadar bir oluşturma talimatıyla hızlıca başarısız olur; çünkü paketli imaj, korumalı alan yazma/düzenleme yardımcıları için `python3` taşır.

* ### İsteğe bağlı: ortak imajı oluştur

Yaygın araçlarla daha işlevsel bir korumalı alan imajı için (örneğin `curl`, `jq`, `nodejs`, `python3`, `git`):

Bir kaynak checkout üzerinden:

bashCopy code
[code]
    scripts/sandbox-common-setup.sh
[/code]

Bir npm kurulumundan, önce varsayılan imajı oluşturun (yukarıya bakın), ardından depodaki [`scripts/docker/sandbox/Dockerfile.common`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.common>) dosyasını kullanarak ortak imajı bunun üzerinde oluşturun.

Ardından `agents.defaults.sandbox.docker.image` değerini `openclaw-sandbox-common:bookworm-slim` olarak ayarlayın.

* ### İsteğe bağlı: korumalı alan tarayıcı imajını oluştur

Bir kaynak checkout üzerinden:

bashCopy code
[code]
    scripts/sandbox-browser-setup.sh
[/code]

Bir npm kurulumundan, depodaki [`scripts/docker/sandbox/Dockerfile.browser`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.browser>) dosyasını kullanarak oluşturun.

Varsayılan olarak, Docker korumalı alan konteynerleri **ağ olmadan** çalışır. `agents.defaults.sandbox.docker.network` ile geçersiz kılın.

Korumalı alan tarayıcı Chromium varsayılanları

Paketli korumalı alan tarayıcı imajı, konteynerleştirilmiş iş yükleri için muhafazakar Chromium başlatma varsayılanları da uygular. Geçerli konteyner varsayılanları şunları içerir:

  * `--remote-debugging-address=127.0.0.1`
  * `--remote-debugging-port=<derived from OPENCLAW_BROWSER_CDP_PORT>`
  * `--user-data-dir=${HOME}/.chrome`
  * `--no-first-run`
  * `--no-default-browser-check`
  * `--disable-3d-apis`
  * `--disable-gpu`
  * `--disable-dev-shm-usage`
  * `--disable-background-networking`
  * `--disable-extensions`
  * `--disable-features=TranslateUI`
  * `--disable-breakpad`
  * `--disable-crash-reporter`
  * `--disable-software-rasterizer`
  * `--no-zygote`
  * `--metrics-recording-only`
  * `--renderer-process-limit=2`
  * `noSandbox` etkinleştirildiğinde `--no-sandbox`.
  * Üç grafik sertleştirme bayrağı (`--disable-3d-apis`, `--disable-software-rasterizer`, `--disable-gpu`) isteğe bağlıdır ve konteynerlerde GPU desteği olmadığında kullanışlıdır. İş yükünüz WebGL veya diğer 3B/tarayıcı özellikleri gerektiriyorsa `OPENCLAW_BROWSER_DISABLE_GRAPHICS_FLAGS=0` ayarlayın.
  * `--disable-extensions` varsayılan olarak etkindir ve eklentiye bağımlı akışlar için `OPENCLAW_BROWSER_DISABLE_EXTENSIONS=0` ile devre dışı bırakılabilir.
  * `--renderer-process-limit=2`, `OPENCLAW_BROWSER_RENDERER_PROCESS_LIMIT=&lt;N&gt;` tarafından denetlenir; burada `0`, Chromium varsayılanını korur.


Farklı bir çalışma zamanı profiline ihtiyacınız varsa, özel bir tarayıcı imajı kullanın ve kendi entrypoint değerinizi sağlayın. Yerel (konteyner olmayan) Chromium profilleri için ek başlatma bayrakları eklemek üzere `browser.extraArgs` kullanın.

Ağ güvenliği varsayılanları

  * `network: "host"` engellenir.
  * `network: "container:<id>"` varsayılan olarak engellenir (namespace katılma atlatma riski).
  * Acil durum geçersiz kılması: `agents.defaults.sandbox.docker.dangerouslyAllowContainerNamespaceJoin: true`.


Docker kurulumları ve konteynerleştirilmiş Gateway burada bulunur: [Docker](</tr/install/docker>)

Docker Gateway dağıtımları için `scripts/docker/setup.sh` korumalı alan yapılandırmasını başlatabilir. Bu yolu etkinleştirmek için `OPENCLAW_SANDBOX=1` (veya `true`/`yes`/`on`) ayarlayın. Soket konumunu `OPENCLAW_DOCKER_SOCKET` ile geçersiz kılabilirsiniz. Tam kurulum ve ortam referansı: [Docker](</tr/install/docker#agent-sandbox>).

## setupCommand (tek seferlik konteyner kurulumu)

`setupCommand`, korumalı alan konteyneri oluşturulduktan sonra **bir kez** çalışır (her çalıştırmada değil). Konteyner içinde `sh -lc` üzerinden yürütülür.

Yollar:

  * Global: `agents.defaults.sandbox.docker.setupCommand`
  * Ajan başına: `agents.list[].sandbox.docker.setupCommand`


Common pitfalls

  * Varsayılan `docker.network` `"none"` değeridir (dışa erişim yoktur), bu yüzden paket kurulumları başarısız olur.
  * `docker.network: "container:<id>"`, `dangerouslyAllowContainerNamespaceJoin: true` gerektirir ve yalnızca acil durumlarda kullanılmalıdır.
  * `readOnlyRoot: true` yazmaları engeller; `readOnlyRoot: false` ayarlayın veya özel bir imaj hazırlayın.
  * Paket kurulumları için `user` root olmalıdır (`user` değerini atlayın veya `user: "0:0"` ayarlayın).
  * Korumalı alan `exec`, ana makinenin `process.env` değerini **devralmaz**. Skill API anahtarları için `agents.defaults.sandbox.docker.env` (veya özel bir imaj) kullanın.


## Araç ilkesi ve kaçış mekanizmaları

Araç izin/verme ilkeleri, korumalı alan kurallarından önce uygulanmaya devam eder. Bir araç genel olarak veya ajan bazında reddedilmişse, korumalı alan onu geri getirmez.

`tools.elevated`, `exec` komutunu korumalı alanın dışında çalıştıran açık bir kaçış mekanizmasıdır (varsayılan olarak `gateway`, exec hedefi `node` olduğunda ise `node`). `/exec` yönergeleri yalnızca yetkili gönderenler için geçerlidir ve oturum bazında kalıcıdır; `exec` komutunu kesin olarak devre dışı bırakmak için araç ilkesi reddini kullanın (bkz. [Korumalı alan vs Araç İlkesi vs Yükseltilmiş](</tr/gateway/sandbox-vs-tool-policy-vs-elevated>)).

Hata ayıklama:

  * Etkin korumalı alan modunu, araç ilkesini ve düzeltme yapılandırma anahtarlarını incelemek için `openclaw sandbox explain` kullanın.
  * "Bu neden engellendi?" zihinsel modeli için bkz. [Korumalı alan vs Araç İlkesi vs Yükseltilmiş](</tr/gateway/sandbox-vs-tool-policy-vs-elevated>).


Kilit altında tutun.

## Çok ajanlı geçersiz kılmalar

Her ajan korumalı alanı ve araçları geçersiz kılabilir: `agents.list[].sandbox` ve `agents.list[].tools` (ayrıca korumalı alan araç ilkesi için `agents.list[].tools.sandbox.tools`). Öncelik sırası için bkz. [Çok Ajanlı Korumalı Alan ve Araçlar](</tr/tools/multi-agent-sandbox-tools>).

## En küçük etkinleştirme örneği

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        scope: "session",        workspaceAccess: "none",      },    },  },}
[/code]

## İlgili

  * [Çok Ajanlı Korumalı Alan ve Araçlar](</tr/tools/multi-agent-sandbox-tools>) — ajan bazlı geçersiz kılmalar ve öncelik sırası
  * [OpenShell](</tr/gateway/openshell>) — yönetilen korumalı alan arka uç kurulumu, çalışma alanı modları ve yapılandırma başvurusu
  * [Korumalı alan yapılandırması](</tr/gateway/config-agents#agentsdefaultssandbox>)
  * [Korumalı alan vs Araç İlkesi vs Yükseltilmiş](</tr/gateway/sandbox-vs-tool-policy-vs-elevated>) — "bu neden engellendi?" hata ayıklaması
  * [Güvenlik](</tr/gateway/security>)


Was this useful?YesNo