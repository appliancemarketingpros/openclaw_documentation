---
title: Crestodian
source_url: https://docs.openclaw.ai/tr/cli/crestodian
scraped_at: 2026-05-25
---

# `openclaw crestodian`

Crestodian, OpenClaw'ın yerel kurulum, onarım ve yapılandırma yardımcısıdır. Normal aracı yolu bozulduğunda erişilebilir kalacak şekilde tasarlanmıştır.

Komutsuz `openclaw` çalıştırmak, Crestodian'ı etkileşimli terminalde başlatır. `openclaw crestodian` çalıştırmak aynı yardımcıyı açıkça başlatır.

## Crestodian'ın gösterdikleri

Başlangıçta etkileşimli Crestodian, `openclaw tui` tarafından kullanılan aynı TUI kabuğunu bir Crestodian sohbet arka ucu ile açar. Sohbet günlüğü kısa bir karşılama ile başlar:

  * Crestodian'ın ne zaman başlatılacağı
  * Crestodian'ın gerçekten kullandığı model veya belirleyici planlayıcı yolu
  * yapılandırma geçerliliği ve varsayılan aracı
  * ilk başlangıç yoklamasından Gateway erişilebilirliği
  * Crestodian'ın yapabileceği sonraki hata ayıklama eylemi


Başlamak için gizli bilgileri dökmez veya Plugin CLI komutlarını yüklemez. TUI normal üst bilgi, sohbet günlüğü, durum satırı, alt bilgi, otomatik tamamlama ve düzenleyici denetimlerini sağlamaya devam eder.

Yapılandırma yolu, doküman/kaynak yolları, yerel CLI yoklamaları, API anahtarı varlığı, aracılar, model ve Gateway ayrıntılarını içeren ayrıntılı envanter için `status` kullanın.

Crestodian, normal aracılarla aynı OpenClaw referans keşfini kullanır. Bir Git checkout içinde kendisini yerel `docs/` ve yerel kaynak ağacına yönlendirir. Bir npm paket kurulumunda paketle birlikte gelen dokümanları kullanır ve dokümanlar yeterli olmadığında kaynağı incelemeye yönelik açık yönlendirmeyle <https://github.com/openclaw/openclaw> bağlantısını verir.

## Örnekler

bashCopy code
[code]
    openclawopenclaw crestodianopenclaw crestodian --jsonopenclaw crestodian --message "models"openclaw crestodian --message "validate config"openclaw crestodian --message "setup workspace ~/Projects/work model openai/gpt-5.5" --yesopenclaw crestodian --message "set default model openai/gpt-5.5" --yesopenclaw onboard --modern
[/code]

Crestodian TUI içinde:

textCopy code
[code]
    statushealthdoctordoctor fixvalidate configsetupsetup workspace ~/Projects/work model openai/gpt-5.5config set gateway.port 19001config set-ref gateway.auth.token env OPENCLAW_GATEWAY_TOKENgateway statusrestart gatewayagentscreate agent work workspace ~/Projects/workmodelsset default model openai/gpt-5.5plugins listplugins search slackplugin install clawhub:openclaw-codex-app-serverplugin uninstall openclaw-codex-app-servertalk to work agenttalk to agent for ~/Projects/workauditquit
[/code]

## Güvenli başlangıç

Crestodian'ın başlangıç yolu kasıtlı olarak küçüktür. Şu durumlarda çalışabilir:

  * `openclaw.json` eksikken
  * `openclaw.json` geçersizken
  * Gateway kapalıyken
  * Plugin komut kaydı kullanılamıyorken
  * henüz hiçbir aracı yapılandırılmamışken


`openclaw --help` ve `openclaw --version` yine normal hızlı yolları kullanır. Etkileşimsiz `openclaw`, kök yardımı yazdırmak yerine kısa bir mesajla çıkar; çünkü komutsuz ürün Crestodian'dır.

## İşlemler ve onay

Crestodian, yapılandırmayı plansız şekilde düzenlemek yerine tipli işlemler kullanır.

Salt okunur işlemler hemen çalıştırılabilir:

  * genel bakışı göster
  * aracıları listele
  * yüklü Plugin'leri listele
  * ClawHub Plugin'lerinde ara
  * model/arka uç durumunu göster
  * durum veya sağlık kontrollerini çalıştır
  * Gateway erişilebilirliğini denetle
  * doctor'ı etkileşimli düzeltmeler olmadan çalıştır
  * yapılandırmayı doğrula
  * denetim günlüğü yolunu göster


Doğrudan komut için `--yes` geçmediğiniz sürece, kalıcı işlemler etkileşimli modda konuşma onayı gerektirir:

  * yapılandırma yaz
  * `config set` çalıştır
  * desteklenen SecretRef değerlerini `config set-ref` aracılığıyla ayarla
  * kurulum/onboarding bootstrap çalıştır
  * varsayılan modeli değiştir
  * Gateway'i başlat, durdur veya yeniden başlat
  * aracılar oluştur
  * ClawHub veya npm'den Plugin'ler yükle
  * Plugin'leri kaldır
  * yapılandırmayı veya durumu yeniden yazan doctor onarımlarını çalıştır


Uygulanan yazmalar şuraya kaydedilir:

textCopy code
[code]
    ~/.openclaw/audit/crestodian.jsonl
[/code]

Keşif denetlenmez. Yalnızca uygulanan işlemler ve yazmalar günlüğe kaydedilir.

`openclaw onboard --modern`, Crestodian'ı modern onboarding önizlemesi olarak başlatır. Düz `openclaw onboard` hâlâ klasik onboarding çalıştırır.

## Kurulum bootstrap'i

`setup`, sohbet öncelikli onboarding bootstrap'idir. Yalnızca tipli yapılandırma işlemleri üzerinden yazar ve önce onay ister.

textCopy code
[code]
    setupsetup workspace ~/Projects/worksetup workspace ~/Projects/work model openai/gpt-5.5
[/code]

Hiçbir model yapılandırılmadığında, setup ilk kullanılabilir arka ucu şu sırayla seçer ve neyi seçtiğini size söyler:

  * zaten yapılandırılmışsa mevcut açık model
  * `OPENAI_API_KEY` -> `openai/gpt-5.5`
  * `ANTHROPIC_API_KEY` -> `anthropic/claude-opus-4-7`
  * Claude Code CLI -> `claude-cli/claude-opus-4-7`
  * Codex CLI -> `codex-cli/gpt-5.5`


Hiçbiri kullanılamıyorsa setup yine de varsayılan çalışma alanını yazar ve modeli ayarsız bırakır. Codex/Claude Code'u yükleyin veya oturum açın ya da `OPENAI_API_KEY`/`ANTHROPIC_API_KEY` değerlerini kullanıma açın, ardından setup'ı yeniden çalıştırın.

## Model Destekli Planlayıcı

Crestodian her zaman belirleyici modda başlar. Belirleyici ayrıştırıcının anlamadığı belirsiz komutlar için yerel Crestodian, OpenClaw'ın normal çalışma zamanı yolları üzerinden tek bir sınırlı planlayıcı turu yapabilir. Önce yapılandırılmış OpenClaw modelini kullanır. Henüz kullanılabilir yapılandırılmış model yoksa, makinede zaten bulunan yerel çalışma zamanlarına geri dönebilir:

  * Claude Code CLI: `claude-cli/claude-opus-4-7`
  * Codex app-server harness: `openai/gpt-5.5`
  * Codex CLI: `codex-cli/gpt-5.5`


Model destekli planlayıcı yapılandırmayı doğrudan değiştiremez. İsteği Crestodian'ın tipli komutlarından birine çevirmelidir; ardından normal onay ve denetim kuralları uygulanır. Crestodian bir şey çalıştırmadan önce kullandığı modeli ve yorumlanan komutu yazdırır. Yapılandırmasız geri dönüş planlayıcı turları geçicidir, çalışma zamanı desteklediğinde araçları devre dışıdır ve geçici bir çalışma alanı/oturum kullanır.

Mesaj kanalı kurtarma modu, model destekli planlayıcıyı kullanmaz. Uzak kurtarma belirleyici kalır; böylece bozuk veya ele geçirilmiş normal bir aracı yolu yapılandırma düzenleyicisi olarak kullanılamaz.

## Bir aracıya geçme

Crestodian'dan çıkıp normal TUI'yi açmak için doğal dil seçici kullanın:

textCopy code
[code]
    talk to agenttalk to work agentswitch to main agent
[/code]

`openclaw tui`, `openclaw chat` ve `openclaw terminal` hâlâ normal aracı TUI'sini doğrudan açar. Crestodian'ı başlatmazlar.

Normal TUI'ye geçtikten sonra Crestodian'a dönmek için `/crestodian` kullanın. Bir takip isteği ekleyebilirsiniz:

textCopy code
[code]
    /crestodian/crestodian restart gateway
[/code]

TUI içindeki aracı geçişleri, `/crestodian` komutunun kullanılabilir olduğuna dair bir iz bırakır.

## Mesaj kurtarma modu

Mesaj kurtarma modu, Crestodian için mesaj kanalı giriş noktasıdır. Normal aracınızın ölü olduğu, ancak WhatsApp gibi güvenilir bir kanalın hâlâ komut aldığı durum içindir.

Desteklenen metin komutu:

  * `/crestodian <request>`


Operatör akışı:

textCopy code
[code]
    You, in a trusted owner DM: /crestodian statusOpenClaw: Crestodian rescue mode. Gateway reachable: no. Config valid: no.You: /crestodian restart gatewayOpenClaw: Plan: restart the Gateway. Reply /crestodian yes to apply.You: /crestodian yesOpenClaw: Applied. Audit entry written.
[/code]

Aracı oluşturma, yerel istemden veya kurtarma modundan da kuyruğa alınabilir:

textCopy code
[code]
    create agent work workspace ~/Projects/work model openai/gpt-5.5/crestodian create agent work workspace ~/Projects/work
[/code]

Uzak kurtarma modu bir yönetici yüzeyidir. Normal sohbet gibi değil, uzak yapılandırma onarımı gibi ele alınmalıdır.

Uzak kurtarma için güvenlik sözleşmesi:

  * Sandbox etkin olduğunda devre dışıdır. Bir aracı/oturum sandbox içindeyse Crestodian uzak kurtarmayı reddetmeli ve yerel CLI onarımının gerekli olduğunu açıklamalıdır.
  * Varsayılan etkin durum `auto` değeridir: uzak kurtarmaya yalnızca çalışma zamanının zaten sandbox'sız yerel yetkiye sahip olduğu güvenilir YOLO işleminde izin ver.
  * Açık bir sahip kimliği gerektir. Kurtarma joker gönderici kurallarını, açık grup politikasını, kimliği doğrulanmamış webhook'ları veya anonim kanalları kabul etmemelidir.
  * Varsayılan olarak yalnızca sahip DM'leri. Grup/kanal kurtarma açık opt-in gerektirir.
  * Plugin arama ve listeleme salt okunurdur. Çalıştırılabilir kod indirdiği için Plugin yükleme varsayılan olarak yalnızca yereldir. Plugin kaldırma, kurtarma politikası kalıcı yazmalara izin verdiğinde onaylanmış bir onarım işlemi olarak izin verilebilir.
  * Uzak kurtarma yerel TUI'yi açamaz veya etkileşimli aracı oturumuna geçemez. Aracı devri için yerel `openclaw` kullanın.
  * Kalıcı yazmalar, kurtarma modunda bile onay gerektirir.
  * Uygulanan her kurtarma işlemini denetle. Mesaj kanalı kurtarma; kanal, hesap, gönderen ve kaynak adresi meta verilerini kaydeder. Yapılandırmayı değiştiren işlemler ayrıca önceki ve sonraki yapılandırma hash'lerini kaydeder.
  * Gizli bilgileri asla yankılama. SecretRef incelemesi değerleri değil, kullanılabilirliği bildirmelidir.
  * Gateway canlıysa Gateway tipli işlemlerini tercih et. Gateway ölü ise yalnızca normal aracı döngüsüne bağlı olmayan en küçük yerel onarım yüzeyini kullan.


Yapılandırma şekli:

jsoncCopy code
[code]
    {  "crestodian": {    "rescue": {      "enabled": "auto",      "ownerDmOnly": true,    },  },}
[/code]

`enabled` şunları kabul etmelidir:

  * `"auto"`: varsayılan. Yalnızca etkin çalışma zamanı YOLO olduğunda ve sandbox kapalı olduğunda izin ver.
  * `false`: mesaj kanalı kurtarmaya hiçbir zaman izin verme.
  * `true`: sahip/kanal kontrolleri geçtiğinde kurtarmaya açıkça izin ver. Bu yine de sandbox reddini atlamamalıdır.


Varsayılan `"auto"` YOLO duruşu:

  * sandbox modu `off` değerine çözümlenir
  * `tools.exec.security` `full` değerine çözümlenir
  * `tools.exec.ask` `off` değerine çözümlenir


Uzak kurtarma Docker hattı tarafından kapsanır:

bashCopy code
[code]
    pnpm test:docker:crestodian-rescue
[/code]

Yapılandırmasız yerel planlayıcı geri dönüşü şununla kapsanır:

bashCopy code
[code]
    pnpm test:docker:crestodian-planner
[/code]

Opt-in canlı kanal komut yüzeyi smoke, `/crestodian status` ile birlikte kurtarma işleyicisi üzerinden kalıcı bir onay gidiş dönüşünü denetler:

bashCopy code
[code]
    pnpm test:live:crestodian-rescue-channel
[/code]

Crestodian üzerinden yeni yapılandırmasız kurulum şununla kapsanır:

bashCopy code
[code]
    pnpm test:docker:crestodian-first-run
[/code]

Bu hat boş bir durum diziniyle başlar, çıplak `openclaw` komutunu Crestodian'a yönlendirir, varsayılan modeli ayarlar, ek bir aracı oluşturur, Plugin etkinleştirmesi ve token SecretRef aracılığıyla Discord'u yapılandırır, yapılandırmayı doğrular ve denetim günlüğünü denetler. QA Lab ayrıca aynı Ring 0 akışı için repo destekli bir senaryoya sahiptir:

bashCopy code
[code]
    pnpm openclaw qa suite --scenario crestodian-ring-zero-setup
[/code]

## İlgili

  * [CLI referansı](</tr/cli>)
  * [Doctor](</tr/cli/doctor>)
  * [TUI](</tr/cli/tui>)
  * [Sandbox](</tr/cli/sandbox>)
  * [Güvenlik](</tr/cli/security>)


Was this useful?YesNo