---
title: Hermes'ten geçiş
source_url: https://docs.openclaw.ai/tr/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw, Hermes durumunu birlikte gelen bir geçiş sağlayıcısı aracılığıyla içe aktarır. Sağlayıcı, durumu değiştirmeden önce her şeyin önizlemesini gösterir, planlarda ve raporlarda gizli bilgileri redakte eder ve uygulamadan önce doğrulanmış bir yedek oluşturur.

## İçe aktarmanın iki yolu

### İlk kurulum sihirbazı

En hızlı yol. Sihirbaz, Hermes'i `~/.hermes` konumunda algılar ve uygulamadan önce bir önizleme gösterir.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Ya da belirli bir kaynağı gösterin:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Betiklenmiş veya tekrarlanabilir çalıştırmalar için `openclaw migrate` kullanın. Tam başvuru için [`openclaw migrate`](</tr/cli/migrate>) bölümüne bakın.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

Hermes `~/.hermes` dışında bulunuyorsa `--from <path>` ekleyin.

## Neler içe aktarılır

Model yapılandırması

  * Hermes `config.yaml` dosyasından varsayılan model seçimi.
  * `providers` ve `custom_providers` üzerinden yapılandırılmış model sağlayıcıları ve özel OpenAI uyumlu uç noktalar.

MCP sunucuları

`mcp_servers` veya `mcp.servers` üzerinden MCP sunucu tanımları.

Çalışma alanı dosyaları

  * `SOUL.md` ve `AGENTS.md`, OpenClaw ajan çalışma alanına kopyalanır.
  * `memories/MEMORY.md` ve `memories/USER.md`, üzerlerine yazılmak yerine eşleşen OpenClaw bellek dosyalarına **eklenir**.

Bellek yapılandırması

OpenClaw dosya belleği için bellek yapılandırma varsayılanları. Honcho gibi harici bellek sağlayıcıları, bilinçli şekilde taşıyabilmeniz için arşiv veya elle inceleme öğeleri olarak kaydedilir.

Skills

`skills/<name>/` altında `SKILL.md` dosyası bulunan Skills, `skills.config` içindeki beceriye özel yapılandırma değerleriyle birlikte kopyalanır.

API anahtarları (isteğe bağlı)

Desteklenen `.env` anahtarlarını içe aktarmak için `--include-secrets` ayarlayın: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Bayrak olmadan gizli bilgiler hiçbir zaman kopyalanmaz.

## Yalnızca arşivde kalanlar

Sağlayıcı, elle inceleme için bunları geçiş raporu dizinine kopyalar, ancak canlı OpenClaw yapılandırmasına veya kimlik bilgilerine **yüklemez** :

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw, biçimler ve güven varsayımları sistemler arasında farklılaşabileceği için bu durumu otomatik olarak yürütmeyi veya ona güvenmeyi reddeder. Arşivi inceledikten sonra ihtiyacınız olanları elle taşıyın.

## Önerilen akış

* ### Planın önizlemesini gösterin

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

Plan; çakışmalar, atlanan öğeler ve tüm hassas öğeler dahil olmak üzere değişecek her şeyi listeler. Plan çıktısı, iç içe geçmiş gizli bilgi gibi görünen anahtarları redakte eder.

* ### Yedekle uygulayın

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw, uygulamadan önce bir yedek oluşturur ve doğrular. API anahtarlarının içe aktarılması gerekiyorsa `--include-secrets` ekleyin.

* ### Doctor çalıştırın

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</tr/gateway/doctor>), bekleyen yapılandırma geçişlerini yeniden uygular ve içe aktarma sırasında ortaya çıkan sorunları denetler.

* ### Yeniden başlatın ve doğrulayın

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Gateway'in sağlıklı olduğunu ve içe aktarılan modelinizin, belleğinizin ve skills'in yüklendiğini doğrulayın.

## Çakışma işleme

Plan çakışma bildirdiğinde uygulama devam etmeyi reddeder (hedefte zaten bir dosya veya yapılandırma değeri vardır).

Yeni bir OpenClaw kurulumunda çakışmalar olağan değildir. Genellikle içe aktarmayı, zaten kullanıcı düzenlemeleri bulunan bir kurulumda yeniden çalıştırdığınızda görünürler.

Uygulama sırasında bir çakışma ortaya çıkarsa (örneğin bir yapılandırma dosyasında beklenmeyen bir yarış), Hermes kalan bağımlı yapılandırma öğelerini kısmen yazmak yerine `blocked by earlier apply conflict` nedeni ile `skipped` olarak işaretler. Geçiş raporu, özgün çakışmayı çözebilmeniz ve içe aktarmayı yeniden çalıştırabilmeniz için engellenen her öğeyi kaydeder.

## Gizli bilgiler

Gizli bilgiler varsayılan olarak hiçbir zaman içe aktarılmaz.

  * Gizli olmayan durumu içe aktarmak için önce `openclaw migrate apply hermes --yes` çalıştırın.
  * Desteklenen `.env` anahtarlarının da kopyalanmasını istiyorsanız `--include-secrets` ile yeniden çalıştırın.
  * SecretRef tarafından yönetilen kimlik bilgileri için, içe aktarma tamamlandıktan sonra SecretRef kaynağını yapılandırın.


## Otomasyon için JSON çıktısı

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

`--json` ile ve `--yes` olmadan, uygulama planı yazdırır ve durumu değiştirmez. Bu, CI ve paylaşılan betikler için en güvenli moddur.

## Sorun giderme

Uygulama çakışmalarla reddediliyor

Plan çıktısını inceleyin. Her çakışma kaynak yolunu ve mevcut hedefi belirtir. Her öğe için atlamaya, hedefi düzenlemeye veya `--overwrite` ile yeniden çalıştırmaya karar verin.

Hermes ~/.hermes dışında bulunuyor

`--from /actual/path` (CLI) veya `--import-source /actual/path` (ilk kurulum) geçirin.

İlk kurulum mevcut bir kurulumda içe aktarmayı reddediyor

İlk kurulum içe aktarmaları yeni bir kurulum gerektirir. Durumu sıfırlayıp yeniden ilk kurulumu yapın ya da `--overwrite` ve açık yedek denetimini destekleyen `openclaw migrate apply hermes` komutunu doğrudan kullanın.

API anahtarları içe aktarılmadı

`--include-secrets` gereklidir ve yalnızca yukarıda listelenen anahtarlar tanınır. `.env` içindeki diğer değişkenler yok sayılır.

## İlgili

  * [`openclaw migrate`](</tr/cli/migrate>): tam CLI başvurusu, Plugin sözleşmesi ve JSON şekilleri.
  * [İlk kurulum](</tr/cli/onboard>): sihirbaz akışı ve etkileşimsiz bayraklar.
  * [Geçiş](</tr/install/migrating>): bir OpenClaw kurulumunu makineler arasında taşıma.
  * [Doctor](</tr/gateway/doctor>): geçiş sonrası sağlık denetimi.
  * [Ajan çalışma alanı](</tr/concepts/agent-workspace>): `SOUL.md`, `AGENTS.md` ve bellek dosyalarının bulunduğu yer.


Was this useful?YesNo