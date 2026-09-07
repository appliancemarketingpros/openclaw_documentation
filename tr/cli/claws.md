---
title: Pençeler
source_url: https://docs.openclaw.ai/tr/cli/claws
scraped_at: 2026-09-07
---

ReferenceCLI commands

# `openclaw claws`

Claw, yeni bir OpenClaw agent'ı için sürümlendirilmiş bir kurulumdur. Agent'ın taşınabilir kimliğini, çalışma alanı dosyalarını, Skills'lerini, Plugin'lerini, MCP sunucularını ve Cron işlerini tanımlayabilir. Çalıştırma ortamına özgü agent ayarları, başvurulan bir paket profilinde taşınabilir. Claw, mevcut bir agent'ın yerini almaz veya onu değiştirmez.

Claw'lar deneyseldir. Şemaları, komut çıktıları ve yaşam döngüleri değişebilir. Komut yüzeyini açıkça etkinleştirin:

bashCopy code
[code]
    export OPENCLAW_EXPERIMENTAL_CLAWS=1
[/code]

Mevcut CLI, yerel bir paket dizinini, `CLAW.md` veya gruplandırılmış JSON manifestini okur. Claw'ların tamamını ClawHub üzerinden yayımlamak, aramak ve kurmak ayrı bir kayıt sistemi hattıdır ve henüz bu komut yüzeyinin parçası değildir.

## Claw paketi oluşturma

Bir paket; `package.json`, bir `CLAW.md` manifesti ve bu manifestin başvurduğu tüm profilleri veya çalışma alanı yan dosyalarını içerir:

jsonCopy code
[code]
    {  "name": "@acme/incident-triage-claw",  "version": "1.0.0",  "type": "module",  "openclaw": { "claw": "CLAW.md" }}
[/code]

`CLAW.md`, YAML ön bilgisiyle başlar. Markdown gövdesi, Claw'ı insanlar için açıklar ve agent yapılandırmasının parçası değildir:

mdCopy code
[code]
    ---schemaVersion: 1agent:  id: incident-triage  name: Olay triyajımetadata:  openclaw.config: profiles/openclaw.ymlworkspace:  bootstrapFiles: {}packages: []mcpServers: {}cronJobs: []--- # Olay triyajı Olayları incelemek ve yönlendirmek için tek bir agent oluşturur.
[/code]

`metadata`, taşınabilir tüketici ipuçları için dizeden dizeye bir eşlemedir. OpenClaw'ın `openclaw.config` anahtarı, isteğe bağlı ve pakete göreli bir YAML profiline işaret eder. Dışa aktarılan varsayılan değer `profiles/openclaw.yml` şeklindedir; işaretçi belirleyici olduğundan bir paket başka bir güvenli göreli `.yml` veya `.yaml` yolu seçebilir.

yamlCopy code
[code]
    schemaVersion: 1agent:  tools:    profile: coding    alsoAllow: [cron]    deny: [exec]    fs:      workspaceOnly: true  memory:    search:      enabled: true      rememberAcrossConversations: true      sources: [memory, sessions]
[/code]

Bu profil yalnızca Claw paketinin içinde bulunur. OpenClaw, söz konusu Claw'ı incelerken, eklerken, güncellerken ve dışa aktarırken profili doğrular ve kullanır; profil, kullanıcının normal OpenClaw yapılandırma yoluna kopyalanmaz. Diğer çalıştırma ortamları, ad alanlı meta veri anahtarını yok sayıp taşınabilir manifest alanlarını kullanabilir.

Aynı katı sürüm 1 şeması, gruplandırılmış JSON manifestlerini kabul etmeye devam eder. Gruplandırılmış JSON, OpenClaw profilinin ikinci bir kopyasını gömmek yerine aynı `metadata.openclaw.config` işaretçisini kullanır. Bu sayfadaki diğer şema parçaları JSON kullanır; eşdeğer anahtarlar `CLAW.md` ön bilgisinde de mevcuttur.

OpenClaw paket profili, çalışan OpenClaw sürümünde kayıtlı herhangi bir yerleşik araç profilini seçip ardından bunu `alsoAllow`, `deny` ve `tools.fs.workspaceOnly: true` ile daraltabilir. Bir Claw, bu alanı `false` olarak ayarlayıp ana makine dosya sistemi sınırlandırmasını zayıflatamaz. `tools.allow`, açık bir izin listesi olarak kullanılmaya devam eder ancak `alsoAllow` ile birleştirilemez. Bir Claw ayrıca `memory.search.enabled` değerini ayarlayabilir, taşınabilir `memory` ve `sessions` kaynaklarını seçebilir ve `rememberAcrossConversations` ile konuşmalar arası belleği etkinleştirebilir. `sessions` kaynağını bildirmek, bu etkinleştirmenin yapılmasını gerektirir. Ana makine politikası bu ayarları yine de sınırlar ve Claw'lar özel profil tanımları, sağlayıcılar, kimlik bilgileri, bağlamalar veya yerel bellek yolları taşımaz. Başvurulan profil 256 KiB ile sınırlıdır, JSON uyumlu YAML olmalıdır; takma adlar, sabitleyiciler, etiketler veya birleştirme anahtarları kullanamaz ve paket içinde bulunan, sembolik bağlantı veya sabit bağlantı olmayan normal bir dosya olmalıdır.

Paket ve çalışma alanı yolları paket kökü içinde kalmalıdır. Manifestler 1 MiB, paket meta verileri 256 KiB ile sınırlıdır; çalışma alanı kaynakları ise dosya başına ve toplam için ayrı sınırlar uygular. Çalışma alanı kaynakları, sembolik bağlantılı üst dizinleri de reddeder.

Çalışma alanı dosyaları yol ile bildirilir ve paket yan dosyalarından okunur. `SOUL.md` gibi başlangıç dosyaları adlandırılmış girdiler kullanır; ek dosyalar pakete göreli kaynakları ve çalışma alanına göreli hedefleri kullanır:

jsonCopy code
[code]
    {  "workspace": {    "bootstrapFiles": {      "SOUL.md": { "source": "workspace/SOUL.md" }    },    "files": [      {        "source": "workspace/reference/policy.md",        "path": "reference/policy.md"      }    ]  }}
[/code]

Skills ve Plugin'ler tam ClawHub sürümlerini kullanır:

jsonCopy code
[code]
    {  "packages": [    {      "kind": "skill",      "source": "clawhub",      "ref": "incident-triage",      "version": "1.0.0"    },    {      "kind": "plugin",      "source": "clawhub",      "ref": "@acme/audit-plugin",      "version": "2.0.0"    }  ]}
[/code]

Deneme çalıştırması, onaydan önce tam yapıtı, bütünlüğü ve tüm ClawHub güven uyarılarını çözümlemek için mevcut Skill ve Plugin ön kontrol yollarını kullanır. Uyarı, bütünlüğe bağlı planda görünür kalır. Uygulama, eksik yapıtları kurar veya eşleşenleri yeniden kullanır ve Claw'ın her kaynağı oluşturduğunu mu yoksa ona başvurduğunu mu kaydeder. Plugin'ler agent başına kurulumlar yerine süreç genelindeki OpenClaw yetenekleri olarak kalır.

Cron işleri, yeni agent için zamanlanmış çalışmaları bildirir:

jsonCopy code
[code]
    {  "cronJobs": [    {      "id": "daily-summary",      "name": "Günlük olay özeti",      "schedule": { "cron": "0 9 * * *", "timezone": "UTC" },      "session": "isolated",      "message": "Etkin olayları özetle."    }  ]}
[/code]

Claw'lar mevcut Gateway zamanlayıcısını kullanır ve oluşturulan işleri yeni agent'a bağlar. Önizleme, kaynak bilgisi, durum ve kaldırma, sıradan Cron komutlarının davranışını değiştirmeden bu işleri kapsar. Kaldırma işlemi, canlı işi Gateway üzerinden yeniden okur ve sahip olunan tanımı planlamadan sonra değişmişse işi korur.

MCP bildirimleri mevcut `mcp.servers` yapılandırma modelini kullanır:

jsonCopy code
[code]
    {  "mcpServers": {    "statuspage": {      "command": "npx",      "args": ["--yes", "@acme/statuspage-mcp@1.0.0"],      "env": { "STATUSPAGE_TOKEN": "${STATUSPAGE_TOKEN}" }    }  }}
[/code]

Ortam başvuruları başvuru olarak kalır; Claw'lar çözümlenmiş gizli değerleri gömmez. Çakışmasız bir bildirim yönetilen duruma gelirken, tamamen aynı olan mevcut veya paylaşılan bir bildirime başvurulur. Önizleme, kaynak bilgisi, durum, dışa aktarma ve kaldırma, diğer Claw kaynaklarıyla aynı sahiplik politikasını izler.

## İnceleme ve önizleme

Yerel değişiklikleri planlamadan kaynağı doğrulayın:

bashCopy code
[code]
    openclaw claws inspect ./incident-triage.claw.json
[/code]

Önerilen tüm yaşam döngüsü eylemlerini önizleyin:

bashCopy code
[code]
    openclaw claws add ./incident-triage.claw.json --dry-run --json
[/code]

Plan; türetilen agent ve çalışma alanını, önerilen her eylemi, ön koşulları, engelleyicileri, farklı yetenek yükseltmelerini ve bir `planIntegrity` özetini bildirir. Yetenek kayıtları tam paket, MCP, zamanlanmış çalışma, korumalı alan, araç veya Heartbeat etkisini gösterir. Agent'ı oluşturmadan önce planı inceleyin:

bashCopy code
[code]
    openclaw claws add ./incident-triage.claw.json \  --yes \  --plan-integrity <SHA256_FROM_DRY_RUN>
[/code]

`--yes` tek başına yeterli değildir. OpenClaw planı yeniden oluşturur ve önizlemeden sonra kaynak, hedef veya canlı yapılandırma değişmişse onayı reddeder. Paket varsayılanları yerel durumla çakıştığında hem önizleme hem uygulama sırasında `--agent-id` veya `--workspace` kullanın. Geçici profiller ve paralel doğrulama için açık bir `--workspace` iletin; `OPENCLAW_STATE_DIR` çalışma zamanı durumunu başka konuma taşır ancak varsayılan çalışma alanı konumunu değiştirmez.

Claw eklemek; yeni agent'ı ve çalışma alanı yapılandırmasını oluşturur, bildirilen çalışma alanı dosyalarını yazar, bildirilen Skill ve Plugin yapıtlarını kurar veya yeniden kullanır ve paket, MCP ve Cron kaynak bilgisini kaydeder. Mevcut dosyaların üzerine yazılmaz ve sahip olunan içerik değiştiğinde yeniden denemeler güvenli biçimde başarısız olur.

## Kurulu durumu inceleme

bashCopy code
[code]
    openclaw claws statusopenclaw claws status incident-triage --jsonopenclaw doctor
[/code]

`status`, kurulu agent'ı ve kayıtlı çalışma alanı, paket, MCP ve Cron kaynak bilgisini mevcut durumla karşılaştırır. Yerel durumu değiştirmeden tamamlanmamış kurulumları, eksik kaynakları ve sapmaları bildirir. `openclaw doctor`, tamamlanmamış sahiplik kayıtları, güvenli olmayan yönetilen dosyalar ve canlı Gateway envanteriyle doğrulanamayan Cron işleri için Claw'a özgü tanılamalar ekler.

Claw kaynak bilgisi iki ilişkiyi birbirinden ayırır:

  * **Yönetilen:** Claw, kaynağı oluşturmuştur ve şu anda yönetmektedir. Kaynak değişmemişse ve çakışan başka bir sahip kalmamışsa temizleme adayıdır.
  * **Başvurulan:** Kaynak bağımsız olarak zaten vardı veya paylaşılmaktadır. Kaldırma işlemi, bu Claw'ın başvurusunu serbest bırakır ve varsayılan olarak kaynağı korur.


Bu bir başvuru sayacı değildir. Sıradan Plugin, Skill ve agent komutları mevcut davranışlarını korur; Claw'lar bunların üzerine kaynak bilgisi ve korumalı yaşam döngüsü işlemleri ekler.

## Kurulu bir Claw'ı güncelleme

Güncelleme, varsayılan olarak Claw eklenirken kaydedilen kaynağı kullanır. Kaynak taşındığında veya başka bir paket dizini test edilirken `--from` kullanın:

bashCopy code
[code]
    openclaw claws update incident-triage --dry-run --jsonopenclaw claws update incident-triage \  --from ./incident-triage-next \  --dry-run --json
[/code]

Plan, mevcut kaynak bilgisini ve canlı durumu hedef manifestle karşılaştırır. Yetenek yükseltmeleri ve engelleyiciler dâhil olmak üzere agent, çalışma alanı, paket, MCP, Cron ve sahiplik değişikliklerini bildirir. Yetenek yükseltmelerinin ayrı, makine tarafından okunabilir kayıtları ve insan tarafından okunabilir çıktıda sansürlenmiş tam etkileri içeren `!` satırları vardır. Çözümlenen paket bütünlüğü, kurulum kimliği ve tüm güven uyarıları dâhil edilir. Bir paket bildirimini kaldırmak, güncelleme sırasında yapıtı kaldırmadan bu Claw'ın bağlantısını serbest bırakır. Nihai tam `planIntegrity` onayı, sıradan içerik değişikliklerinin yanı sıra açıklanan bu kümeyi de bağlar. Ana makineler aynı kayıtları ayrı bir iletişim kutusu veya toplu birden çok agent incelemesi için kullanabilir. Tam olarak incelenen planı açık onayla uygulayın:

bashCopy code
[code]
    openclaw claws update incident-triage \  --yes \  --plan-integrity <SHA256_FROM_DRY_RUN>
[/code]

OpenClaw, her değişiklikten önce planı yeniden oluşturur ve sahip olunan duruma karşılaştırmalı değiş tokuş uygular. Kaldırılan paket bildirimleri, yapıtları kaldırmadan bağımlılık bağlantılarını serbest bırakır. Cron değişiklikleri canlı zamanlayıcı tanımını yeniden okur ve operatör kaynaklı sapmada durur. Paket kurucuları, kaynak yapılandırma yazıcıları ve Gateway zamanlayıcısı tek bir işlem değildir. Harici bir değişiklikten sonra telafinin başarısı kanıtlanamazsa OpenClaw, yapılandırılmış `status: partial` ile birlikte `update_partial` hata kodunu bildirir, belirsiz kaynak bilgisini korur ve durur. `claws status`, etkilenen kaynak ve `openclaw doctor` öğelerini inceleyin; ardından yeniden denemeden veya herhangi bir şeyi kaldırmadan önce tekrar önizleme yapın.

## Kurulu bir Claw'ı kaldırma

Temizleme seçeneklerini belirlemeden önce kaldırma işlemini önizleyin:

bashCopy code
[code]
    openclaw claws remove incident-triage --dry-run --jsonopenclaw claws remove incident-triage \  --yes \  --plan-integrity <SHA256_FROM_DRY_RUN>
[/code]

Varsayılan işlem, uygun yönetilen durumu kaldırır ve başvurulan durumu serbest bırakır. Değiştirilmiş dosyalar ve başka bir güncel sahibi bulunan kaynaklar korunur veya engellenir. Temizleme seçenekleri plan özetinin parçasıdır; `--yes` bunları hiçbir zaman genişletmez. Genel olarak kurulu Plugin'ler, bu Claw'ın başvurusu serbest bırakılırken korunur; süreç genelindeki bir Plugin'i kaldırmak istediğinizde sıradan Plugin yaşam döngüsünü ayrıca kullanın.

Başka güncel sahibi olmayan, Claw tarafından oluşturulmuş ve değişmemiş başvuruları kaldırmak için hem önizleme hem uygulamaya `--remove-unused` ekleyin. Bunun yerine tam başvurulan kaynakları seçmek için `--remove-referenced` seçeneğini tekrarlayın:

bashCopy code
[code]
    openclaw claws remove incident-triage \  --dry-run \  --remove-referenced 'plugin:@acme/audit-plugin@2.0.0'
[/code]

`--force-referenced` seçeneğini yalnızca görüntülenen bağımlıları, bağımsız sahipleri ve önceden var olan kaynağı inceledikten sonra kullanın. Bu seçenek, söz konusu çakışmalara rağmen seçilen temizliğe izin verir; plan bütünlüğü onayını atlamaz.

## Kurulu bir agent'ı dışa aktarma

Dışa aktarma, yeni bir paket dizini oluşturur ve hedef zaten mevcutsa veya yönetilen durumda sapma oluşmuşsa başarısız olur:

bashCopy code
[code]
    openclaw claws export incident-triage --out ./incident-triage-export --json
[/code]

Sonuç; `package.json`, kurallı `CLAW.md` ve yönetilen çalışma alanı yardımcı dosyalarını içerir. Bu, taşınabilir bir Claw paketidir, tüm örneğin yedeği değildir: ilgisiz aracılar, kimlik bilgileri, oturumlar ve sahiplenilmemiş yerel durum hariç tutulur.

## Komut başvurusu

Komut | Amaç  
---|---  
`claws inspect <source>` | Bir paket dizinini veya gruplandırılmış manifesti doğrular.  
`claws add <source>` | Yeni bir aracıyı ve çalışma alanını önizler veya oluşturur.  
`claws status [claw-or-agent]` | Kurulu durumu, sahipliği ve sapmayı bildirir.  
`claws update <claw-or-agent>` | Seçilen kaynaktaki değişiklikleri önizler veya uygular.  
`claws remove <claw-or-agent>` | Aracıyı ve uygun kaynakları önizler veya kaldırır.  
`claws export <agent> --out <path>` | Kurulu bir aracıdan taşınabilir bir paket oluşturur.  
  
Deneysel, makinece okunabilir çıktı için `--json` kullanın.

## Ayrıca bkz.

  * [Aracılar](</tr/cli/agents>)
  * [Skills](</tr/tools/skills>)
  * [Pluginler](</tr/tools/plugin>)
  * [Cron işleri](</tr/automation/cron-jobs>)
  * [MCP yapılandırması](</tr/gateway/configuration-reference#mcp>)


Was this useful?YesNo

Open issue