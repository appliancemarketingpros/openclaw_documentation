---
title: Claude'dan geçiş
source_url: https://docs.openclaw.ai/tr/install/migrating-claude
scraped_at: 2026-05-25
---

OpenClaw, yerel Claude durumunu paketle birlikte gelen Claude migration sağlayıcısı aracılığıyla içe aktarır. Sağlayıcı, durumu değiştirmeden önce her öğeyi önizler, planlarda ve raporlarda gizli bilgileri redakte eder ve uygulamadan önce doğrulanmış bir yedek oluşturur.

## İçe aktarmanın iki yolu

### Onboarding wizard

Sihirbaz, yerel Claude durumunu algıladığında Claude seçeneğini sunar.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Ya da belirli bir kaynağı gösterin:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Betikli veya tekrarlanabilir çalıştırmalar için `openclaw migrate` kullanın. Tam başvuru için [`openclaw migrate`](</tr/cli/migrate>) sayfasına bakın.

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Belirli bir Claude Code ana dizinini veya proje kökünü içe aktarmak için `--from <path>` ekleyin.

## Neler içe aktarılır

Instructions and memory

  * Proje `CLAUDE.md` ve `.claude/CLAUDE.md` içeriği OpenClaw ajan çalışma alanındaki `AGENTS.md` dosyasına kopyalanır veya eklenir.
  * Kullanıcı `~/.claude/CLAUDE.md` içeriği çalışma alanındaki `USER.md` dosyasına eklenir.

MCP servers

MCP sunucu tanımları, mevcut olduğunda proje `.mcp.json`, Claude Code `~/.claude.json` ve Claude Desktop `claude_desktop_config.json` dosyalarından içe aktarılır.

Skills and commands

  * `SKILL.md` dosyası olan Claude skills, OpenClaw çalışma alanı skills dizinine kopyalanır.
  * `.claude/commands/` veya `~/.claude/commands/` altındaki Claude komut Markdown dosyaları, `disable-model-invocation: true` ile OpenClaw skills öğelerine dönüştürülür.


## Neler yalnızca arşiv olarak kalır

Sağlayıcı bunları elle gözden geçirmek üzere migration raporuna kopyalar, ancak canlı OpenClaw yapılandırmasına **yüklemez** :

  * Claude hook'ları
  * Claude izinleri ve geniş araç izin listeleri
  * Claude ortam varsayılanları
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * `.claude/agents/` veya `~/.claude/agents/` altındaki Claude alt ajanları
  * Claude Code önbellekleri, planları ve proje geçmişi dizinleri
  * Claude Desktop uzantıları ve işletim sisteminde saklanan kimlik bilgileri


OpenClaw hook'ları yürütmeyi, izin listelerine güvenmeyi veya opak OAuth ve Desktop kimlik bilgisi durumunu otomatik olarak çözmeyi reddeder. İhtiyacınız olanları arşivi gözden geçirdikten sonra elle taşıyın.

## Kaynak seçimi

`--from` olmadan OpenClaw, `~/.claude` konumundaki varsayılan Claude Code ana dizinini, örneklenen Claude Code `~/.claude.json` durum dosyasını ve macOS üzerindeki Claude Desktop MCP yapılandırmasını inceler.

`--from` bir proje kökünü gösterdiğinde OpenClaw yalnızca o projenin `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/` ve `.mcp.json` gibi Claude dosyalarını içe aktarır. Proje kökü içe aktarımı sırasında global Claude ana dizininizi okumaz.

## Önerilen akış

* ### Preview the plan

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

Plan; çakışmalar, atlanan öğeler ve iç içe MCP `env` veya `headers` alanlarından redakte edilen hassas değerler dahil olmak üzere değişecek her şeyi listeler.

* ### Apply with backup

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw, uygulamadan önce bir yedek oluşturur ve doğrular.

* ### Run doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</tr/gateway/doctor>), içe aktarımdan sonra yapılandırma veya durum sorunlarını denetler.

* ### Restart and verify

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Gateway'in sağlıklı olduğunu ve içe aktarılan talimatlarınızın, MCP sunucularınızın ve skills öğelerinizin yüklendiğini doğrulayın.

## Çakışma yönetimi

Plan çakışmalar bildirdiğinde uygulama devam etmeyi reddeder (hedefte zaten bir dosya veya yapılandırma değeri vardır).

Yeni bir OpenClaw kurulumu için çakışmalar olağan değildir. Genellikle içe aktarımı, zaten kullanıcı düzenlemeleri olan bir kurulumda yeniden çalıştırdığınızda ortaya çıkarlar.

## Otomasyon için JSON çıktısı

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

`--json` ile ve `--yes` olmadan, uygulama planı yazdırır ve durumu değiştirmez. Bu, CI ve paylaşılan betikler için en güvenli moddur.

## Sorun giderme

Claude state lives outside ~/.claude

`--from /actual/path` (CLI) veya `--import-source /actual/path` (onboarding) iletin.

Onboarding refuses to import on an existing setup

Onboarding içe aktarımları yeni bir kurulum gerektirir. Ya durumu sıfırlayıp onboarding'i yeniden çalıştırın ya da doğrudan `openclaw migrate apply claude` kullanın; bu komut `--overwrite` ve açık yedekleme denetimini destekler.

MCP servers from Claude Desktop did not import

Claude Desktop, `claude_desktop_config.json` dosyasını platforma özgü bir yoldan okur. OpenClaw bunu otomatik algılamadıysa `--from` değerini o dosyanın dizinine yönlendirin.

Claude commands became skills with model invocation disabled

Tasarım gereği böyledir. Claude komutları kullanıcı tarafından tetiklenir, bu nedenle OpenClaw bunları `disable-model-invocation: true` ile skills olarak içe aktarır. Ajanın bunları otomatik çağırmasını istiyorsanız her skill'in frontmatter bölümünü düzenleyin.

## İlgili

  * [`openclaw migrate`](</tr/cli/migrate>): tam CLI başvurusu, plugin sözleşmesi ve JSON şekilleri.
  * [Migration kılavuzu](</tr/install/migrating>): tüm migration yolları.
  * [Hermes'ten migration](</tr/install/migrating-hermes>): diğer sistemler arası içe aktarma yolu.
  * [Onboarding](</tr/cli/onboard>): sihirbaz akışı ve etkileşimsiz bayraklar.
  * [Doctor](</tr/gateway/doctor>): migration sonrası sağlık denetimi.
  * [Ajan çalışma alanı](</tr/concepts/agent-workspace>): `AGENTS.md`, `USER.md` ve skills öğelerinin bulunduğu yer.


Was this useful?YesNo