---
title: Ajan çalışma alanı
source_url: https://docs.openclaw.ai/tr/concepts/agent-workspace
scraped_at: 2026-05-25
---

Çalışma alanı, ajanın evidir. Dosya araçları ve çalışma alanı bağlamı için kullanılan tek çalışma dizinidir. Gizli tutun ve bellek olarak ele alın.

Bu, yapılandırma, kimlik bilgileri ve oturumları saklayan `~/.openclaw/` dizininden ayrıdır.

## Varsayılan konum

  * Varsayılan: `~/.openclaw/workspace`
  * `OPENCLAW_PROFILE` ayarlanmışsa ve `"default"` değilse, varsayılan `~/.openclaw/workspace-<profile>` olur.
  * `~/.openclaw/openclaw.json` içinde geçersiz kılın:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure` veya `openclaw setup`, çalışma alanını oluşturur ve eksiklerse önyükleme dosyalarını yerleştirir.

Çalışma alanı dosyalarını zaten kendiniz yönetiyorsanız, önyükleme dosyası oluşturmayı devre dışı bırakabilirsiniz:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Ek çalışma alanı klasörleri

Eski kurulumlar `~/openclaw` oluşturmuş olabilir. Etrafta birden fazla çalışma alanı dizini tutmak, kafa karıştırıcı kimlik doğrulama veya durum kaymasına neden olabilir; çünkü aynı anda yalnızca bir çalışma alanı aktiftir.

## Çalışma alanı dosya haritası

Bunlar, OpenClaw'ın çalışma alanı içinde beklediği standart dosyalardır:

AGENTS.md - işletim talimatları

Ajan için işletim talimatları ve belleği nasıl kullanması gerektiği. Her oturumun başlangıcında yüklenir. Kurallar, öncelikler ve "nasıl davranılacağı" ayrıntıları için iyi bir yerdir.

SOUL.md - kişilik ve ton

Kişilik, ton ve sınırlar. Her oturumda yüklenir. Kılavuz: [SOUL.md kişilik kılavuzu](</tr/concepts/soul>).

USER.md - kullanıcının kim olduğu

Kullanıcının kim olduğu ve ona nasıl hitap edileceği. Her oturumda yüklenir.

IDENTITY.md - ad, hava, emoji

Ajanın adı, havası ve emojisi. Önyükleme ritüeli sırasında oluşturulur/güncellenir.

TOOLS.md - yerel araç kuralları

Yerel araçlarınız ve kurallarınız hakkında notlar. Araç kullanılabilirliğini denetlemez; yalnızca rehberliktir.

HEARTBEAT.md - Heartbeat kontrol listesi

Heartbeat çalıştırmaları için isteğe bağlı küçük kontrol listesi. Token tüketimini önlemek için kısa tutun.

BOOT.md - başlangıç kontrol listesi

Gateway yeniden başlatıldığında otomatik olarak çalıştırılan isteğe bağlı başlangıç kontrol listesi ([dahili hook'lar](</tr/automation/hooks>) etkin olduğunda). Kısa tutun; dışa gönderimler için mesaj aracını kullanın.

BOOTSTRAP.md - ilk çalıştırma ritüeli

Tek seferlik ilk çalıştırma ritüeli. Yalnızca yepyeni bir çalışma alanı için oluşturulur. Ritüel tamamlandıktan sonra silin.

memory/YYYY-MM-DD.md - günlük bellek kaydı

Günlük bellek kaydı (günde bir dosya). Oturum başlangıcında bugün + dün okunması önerilir.

MEMORY.md - düzenlenmiş uzun vadeli bellek (isteğe bağlı)

Düzenlenmiş uzun vadeli bellek: kalıcı gerçekler, tercihler, kararlar ve kısa özetler. Ayrıntılı kayıtları `memory/YYYY-MM-DD.md` içinde tutun; böylece bellek araçları bunları her isteme enjekte etmeden ihtiyaç halinde alabilir. `MEMORY.md` dosyasını yalnızca ana, özel oturumda yükleyin (paylaşılan/grup bağlamlarında değil). İş akışı ve otomatik bellek boşaltma için bkz. [Bellek](</tr/concepts/memory>).

skills/ - çalışma alanı Skills'leri (isteğe bağlı)

Çalışma alanına özel Skills. O çalışma alanı için en yüksek öncelikli Skills konumu. Adlar çakıştığında proje ajan Skills'lerini, kişisel ajan Skills'lerini, yönetilen Skills'leri, paketlenmiş Skills'leri ve `skills.load.extraDirs` değerini geçersiz kılar.

canvas/ - Canvas UI dosyaları (isteğe bağlı)

Düğüm görüntüleri için Canvas UI dosyaları (örneğin `canvas/index.html`).

## Çalışma alanında OLMAYANLAR

Bunlar `~/.openclaw/` altında bulunur ve çalışma alanı reposuna commit EDİLMEMELİDİR:

  * `~/.openclaw/openclaw.json` (yapılandırma)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (model kimlik doğrulama profilleri: OAuth + API anahtarları)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (ajan başına Codex çalışma zamanı hesabı, yapılandırma, Skills, Plugin'ler ve yerel iş parçacığı durumu)
  * `~/.openclaw/credentials/` (kanal/sağlayıcı durumu ve eski OAuth içe aktarma verileri)
  * `~/.openclaw/agents/<agentId>/sessions/` (oturum dökümleri + meta veriler)
  * `~/.openclaw/skills/` (yönetilen Skills)


Oturumları veya yapılandırmayı taşımanız gerekiyorsa, bunları ayrı olarak kopyalayın ve sürüm kontrolünün dışında tutun.

## Git yedeklemesi (önerilir, özel)

Çalışma alanını özel bellek olarak ele alın. Yedeklenebilir ve kurtarılabilir olması için onu **özel** bir git reposuna koyun.

Bu adımları Gateway'in çalıştığı makinede çalıştırın (çalışma alanının bulunduğu yer orasıdır).

* ### Repoyu başlatın

Git kuruluysa, yepyeni çalışma alanları otomatik olarak başlatılır. Bu çalışma alanı zaten bir repo değilse şunu çalıştırın:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Özel bir remote ekleyin

### GitHub web UI

  1. GitHub'da yeni bir **özel** depo oluşturun.
  2. README ile başlatmayın (merge çakışmalarını önler).
  3. HTTPS remote URL'sini kopyalayın.
  4. Remote'u ekleyin ve push edin:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab web UI

  1. GitLab'da yeni bir **özel** depo oluşturun.
  2. README ile başlatmayın (merge çakışmalarını önler).
  3. HTTPS remote URL'sini kopyalayın.
  4. Remote'u ekleyin ve push edin:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Sürekli güncellemeler

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Gizli bilgileri commit etmeyin

Önerilen `.gitignore` başlangıcı:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## Çalışma alanını yeni bir makineye taşıma

* ### Repoyu klonlayın

Repoyu istenen yola klonlayın (varsayılan `~/.openclaw/workspace`).

* ### Yapılandırmayı güncelleyin

`~/.openclaw/openclaw.json` içinde `agents.defaults.workspace` değerini bu yola ayarlayın.

* ### Eksik dosyaları yerleştirin

Eksik dosyaları yerleştirmek için `openclaw setup --workspace <path>` çalıştırın.

* ### Oturumları kopyalayın (isteğe bağlı)

Oturumlara ihtiyacınız varsa, eski makineden `~/.openclaw/agents/<agentId>/sessions/` dizinini ayrı olarak kopyalayın.

## Gelişmiş notlar

  * Çok ajanlı yönlendirme, ajan başına farklı çalışma alanları kullanabilir. Yönlendirme yapılandırması için bkz. [Kanal yönlendirme](</tr/channels/channel-routing>).
  * `agents.defaults.sandbox` etkinleştirilmişse, ana olmayan oturumlar `agents.defaults.sandbox.workspaceRoot` altında oturum başına sandbox çalışma alanları kullanabilir.


## İlgili

  * [Heartbeat](</tr/gateway/heartbeat>) \- [HEARTBEAT.md](<http://HEARTBEAT.md>) çalışma alanı dosyası
  * [Sandboxlama](</tr/gateway/sandboxing>) \- sandboxlanmış ortamlarda çalışma alanı erişimi
  * [Oturum](</tr/concepts/session>) \- oturum depolama yolları
  * [Kalıcı talimatlar](</tr/automation/standing-orders>) \- çalışma alanı dosyalarındaki kalıcı talimatlar


Was this useful?YesNo