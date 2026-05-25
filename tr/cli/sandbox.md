---
title: Korumalı Alan CLI
source_url: https://docs.openclaw.ai/tr/cli/sandbox
scraped_at: 2026-05-25
---

Yalıtılmış ajan yürütmesi için sandbox çalışma zamanlarını yönetin.

## Genel Bakış

OpenClaw, güvenlik için ajanları yalıtılmış sandbox çalışma zamanlarında çalıştırabilir. `sandbox` komutları, güncellemelerden veya yapılandırma değişikliklerinden sonra bu çalışma zamanlarını incelemenize ve yeniden oluşturmanıza yardımcı olur.

Günümüzde bu genellikle şunlar anlamına gelir:

  * Docker sandbox container'ları
  * `agents.defaults.sandbox.backend = "ssh"` olduğunda SSH sandbox çalışma zamanları
  * `agents.defaults.sandbox.backend = "openshell"` olduğunda OpenShell sandbox çalışma zamanları


`ssh` ve OpenShell `remote` için yeniden oluşturma, Docker'a göre daha önemlidir:

  * uzak çalışma alanı, ilk tohumlamadan sonra kanoniktir
  * `openclaw sandbox recreate`, seçili kapsam için bu kanonik uzak çalışma alanını siler
  * sonraki kullanım, geçerli yerel çalışma alanından yeniden tohumlar


## Komutlar

### `openclaw sandbox explain`

**Etkin** sandbox modunu/kapsamını/çalışma alanı erişimini, sandbox araç politikasını ve yükseltilmiş kapıları (düzeltme yapılandırma anahtarı yollarıyla) inceleyin.

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

Tüm sandbox çalışma zamanlarını durumları ve yapılandırmalarıyla listeleyin.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**Çıktı şunları içerir:**

  * Çalışma zamanı adı ve durumu
  * Backend (`docker`, `openshell` vb.)
  * Yapılandırma etiketi ve geçerli yapılandırmayla eşleşip eşleşmediği
  * Yaş (oluşturulmasından bu yana geçen süre)
  * Boşta kalma süresi (son kullanımdan bu yana geçen süre)
  * İlişkili oturum/ajan


### `openclaw sandbox recreate`

Güncellenmiş yapılandırmayla yeniden oluşturmayı zorlamak için sandbox çalışma zamanlarını kaldırın.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**Seçenekler:**

  * `--all`: Tüm sandbox container'larını yeniden oluştur
  * `--session <key>`: Belirli oturum için container'ı yeniden oluştur
  * `--agent <id>`: Belirli ajan için container'ları yeniden oluştur
  * `--browser`: Yalnızca tarayıcı container'larını yeniden oluştur
  * `--force`: Onay istemini atla


## Kullanım durumları

### Bir Docker imajını güncelledikten sonra

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### Sandbox yapılandırmasını değiştirdikten sonra

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### SSH hedefini veya SSH kimlik doğrulama materyalini değiştirdikten sonra

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

Çekirdek `ssh` backend'i için yeniden oluşturma, SSH hedefindeki kapsam başına uzak çalışma alanı kökünü siler. Sonraki çalıştırma, yerel çalışma alanından yeniden tohumlar.

### OpenShell kaynağını, politikasını veya modunu değiştirdikten sonra

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

OpenShell `remote` modu için yeniden oluşturma, o kapsama ait kanonik uzak çalışma alanını siler. Sonraki çalıştırma, yerel çalışma alanından yeniden tohumlar.

### setupCommand değiştirildikten sonra

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### Yalnızca belirli bir ajan için

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## Bu neden gerekli

Sandbox yapılandırmasını güncellediğinizde:

  * Mevcut çalışma zamanları eski ayarlarla çalışmaya devam eder.
  * Çalışma zamanları yalnızca 24 saat hareketsizlikten sonra budanır.
  * Düzenli kullanılan ajanlar eski çalışma zamanlarını süresiz olarak canlı tutar.


Eski çalışma zamanlarının kaldırılmasını zorlamak için `openclaw sandbox recreate` kullanın. Sonraki ihtiyaçta geçerli ayarlarla otomatik olarak yeniden oluşturulurlar.

## Kayıt defteri geçişi

OpenClaw, sandbox çalışma zamanı meta verilerini sandbox durum dizini altında her container/browser girdisi için bir JSON parçası olarak saklar. Eski kurulumlarda hâlâ monolitik eski dosyalar bulunabilir:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


Normal sandbox çalışma zamanı okumaları bu dosyaları yeniden yazmaz. Geçerli eski girdileri parçalı kayıt defteri dizinlerine geçirmek için `openclaw doctor --fix` çalıştırın. Geçersiz eski dosyalar karantinaya alınır; böylece tek bir bozuk eski kayıt defteri, geçerli çalışma zamanı girdilerini gizleyemez.

## Yapılandırma

Sandbox ayarları `~/.openclaw/openclaw.json` içinde `agents.defaults.sandbox` altında bulunur (ajan başına geçersiz kılmalar `agents.list[].sandbox` içine gider):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Sandboxing](</tr/gateway/sandboxing>)
  * [Ajan çalışma alanı](</tr/concepts/agent-workspace>)
  * [Doctor](</tr/gateway/doctor>): sandbox kurulumunu denetler.


Was this useful?YesNo