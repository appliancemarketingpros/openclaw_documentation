---
title: Kancalar
source_url: https://docs.openclaw.ai/tr/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Ajan kancalarını yönetin (`/new`, `/reset` ve Gateway başlangıcı gibi komutlar için olay güdümlü otomasyonlar).

`openclaw hooks` komutunu alt komut olmadan çalıştırmak, `openclaw hooks list` ile eşdeğerdir.

İlgili:

  * Kancalar: [Kancalar](</tr/automation/hooks>)
  * Plugin kancaları: [Plugin kancaları](</tr/plugins/hooks>)


## Tüm kancaları listeleme

bashCopy code
[code]
    openclaw hooks list
[/code]

Çalışma alanı, yönetilen, ek ve paketle gelen dizinlerden keşfedilen tüm kancaları listeler. Gateway başlangıcı, en az bir dahili kanca yapılandırılana kadar dahili kanca işleyicilerini yüklemez.

**Seçenekler:**

  * `--eligible`: Yalnızca uygun kancaları gösterir (gereksinimler karşılanmış)
  * `--json`: JSON olarak çıktı verir
  * `-v, --verbose`: Eksik gereksinimler dahil ayrıntılı bilgileri gösterir


**Örnek çıktı:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Örnek (ayrıntılı):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Uygun olmayan kancalar için eksik gereksinimleri gösterir.

**Örnek (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Programlı kullanım için yapılandırılmış JSON döndürür.

## Kanca bilgilerini alma

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Belirli bir kanca hakkında ayrıntılı bilgi gösterir.

**Argümanlar:**

  * `<name>`: Kanca adı veya kanca anahtarı (ör. `session-memory`)


**Seçenekler:**

  * `--json`: JSON olarak çıktı verir


**Örnek:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Çıktı:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Kancaların uygunluğunu denetleme

bashCopy code
[code]
    openclaw hooks check
[/code]

Kanca uygunluk durumunun özetini gösterir (kaç tanesi hazır, kaç tanesi hazır değil).

**Seçenekler:**

  * `--json`: JSON olarak çıktı verir


**Örnek çıktı:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Bir kancayı etkinleştirme

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Yapılandırmanıza ekleyerek belirli bir kancayı etkinleştirir (varsayılan olarak `~/.openclaw/openclaw.json`).

**Not:** Çalışma alanı kancaları, burada veya yapılandırmada etkinleştirilene kadar varsayılan olarak devre dışıdır. Plugin tarafından yönetilen kancalar `openclaw hooks list` içinde `plugin:<id>` gösterir ve buradan etkinleştirilemez/devre dışı bırakılamaz. Bunun yerine Plugin'i etkinleştirin/devre dışı bırakın.

**Argümanlar:**

  * `<name>`: Kanca adı (ör. `session-memory`)


**Örnek:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Çıktı:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Ne yapar:**

  * Kancanın var olup olmadığını ve uygun olup olmadığını denetler
  * Yapılandırmanızda `hooks.internal.entries.<name>.enabled = true` değerini günceller
  * Yapılandırmayı diske kaydeder


Kanca `<workspace>/hooks/` içinden geldiyse, Gateway'in bunu yüklemesinden önce bu katılım adımı gerekir.

**Etkinleştirdikten sonra:**

  * Kancaların yeniden yüklenmesi için gateway'i yeniden başlatın (macOS'ta menü çubuğu uygulamasını yeniden başlatın veya geliştirmede gateway sürecinizi yeniden başlatın).


## Bir kancayı devre dışı bırakma

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Yapılandırmanızı güncelleyerek belirli bir kancayı devre dışı bırakır.

**Argümanlar:**

  * `<name>`: Kanca adı (ör. `command-logger`)


**Örnek:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Çıktı:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Devre dışı bıraktıktan sonra:**

  * Kancaların yeniden yüklenmesi için gateway'i yeniden başlatın


## Notlar

  * `openclaw hooks list --json`, `info --json` ve `check --json`, yapılandırılmış JSON'u doğrudan stdout'a yazar.
  * Plugin tarafından yönetilen kancalar burada etkinleştirilemez veya devre dışı bırakılamaz; bunun yerine sahibi olan Plugin'i etkinleştirin veya devre dışı bırakın.


## Kanca paketlerini yükleme

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Kanca paketlerini birleşik plugins yükleyicisi üzerinden yükleyin.

`openclaw hooks install` uyumluluk takma adı olarak çalışmaya devam eder, ancak bir kullanımdan kaldırma uyarısı yazdırır ve `openclaw plugins install` komutuna yönlendirir.

Npm tanımları **yalnızca registry** kapsamındadır (paket adı + isteğe bağlı **tam sürüm** veya **dist-tag**). Git/URL/file tanımları ve semver aralıkları reddedilir. Bağımlılık yüklemeleri, kabuğunuzda global npm yükleme ayarları olsa bile güvenlik için `--ignore-scripts` ile proje yerelinde çalışır.

Çıplak tanımlar ve `@latest` kararlı kanalda kalır. npm bunlardan herhangi birini ön sürüme çözümlerse OpenClaw durur ve `@beta`/`@rc` gibi bir ön sürüm etiketiyle veya tam bir ön sürüm numarasıyla açıkça katılmanızı ister.

**Ne yapar:**

  * Kanca paketini `~/.openclaw/hooks/<id>` içine kopyalar
  * Yüklü kancaları `hooks.internal.entries.*` içinde etkinleştirir
  * Yüklemeyi `hooks.internal.installs` altında kaydeder


**Seçenekler:**

  * `-l, --link`: Yerel bir dizini kopyalamak yerine bağlar (`hooks.internal.load.extraDirs` içine ekler)
  * `--pin`: npm yüklemelerini `hooks.internal.installs` içinde tam çözümlenmiş `name@version` olarak kaydeder


**Desteklenen arşivler:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Örnekler:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Bağlanan kanca paketleri, çalışma alanı kancaları olarak değil, operatör tarafından yapılandırılmış bir dizinden gelen yönetilen kancalar olarak değerlendirilir.

## Kanca paketlerini güncelleme

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

İzlenen npm tabanlı kanca paketlerini birleşik plugins güncelleyicisi üzerinden güncelleyin.

`openclaw hooks update` uyumluluk takma adı olarak çalışmaya devam eder, ancak bir kullanımdan kaldırma uyarısı yazdırır ve `openclaw plugins update` komutuna yönlendirir.

**Seçenekler:**

  * `--all`: İzlenen tüm kanca paketlerini günceller
  * `--dry-run`: Yazmadan neyin değişeceğini gösterir


Saklanan bir bütünlük hash'i varsa ve getirilen yapıt hash'i değişirse, OpenClaw bir uyarı yazdırır ve devam etmeden önce onay ister. CI/etkileşimsiz çalıştırmalarda istemleri atlamak için global `--yes` kullanın.

## Paketle gelen kancalar

### session-memory

`/new` veya `/reset` verdiğinizde oturum bağlamını belleğe kaydeder.

**Etkinleştir:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Çıktı:** Varsayılan olarak `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md`. Model tarafından oluşturulan dosya adı slug'ları için `hooks.internal.entries.session-memory.llmSlug: true` ayarlayın.

**Ayrıca bakın:** [session-memory belgeleri](</tr/automation/hooks#session-memory>)

### bootstrap-extra-files

`agent:bootstrap` sırasında ek bootstrap dosyaları (örneğin monorepo yerelinde `AGENTS.md` / `TOOLS.md`) enjekte eder.

**Etkinleştir:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Ayrıca bakın:** [bootstrap-extra-files belgeleri](</tr/automation/hooks#bootstrap-extra-files>)

### command-logger

Tüm komut olaylarını merkezi bir denetim dosyasına kaydeder.

**Etkinleştir:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Çıktı:** `~/.openclaw/logs/commands.log`

**Günlükleri görüntüle:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Ayrıca bakın:** [command-logger belgeleri](</tr/automation/hooks#command-logger>)

### boot-md

Gateway başladığında (kanallar başladıktan sonra) `BOOT.md` çalıştırır.

**Olaylar** : `gateway:startup`

**Etkinleştir** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Ayrıca bakın:** [boot-md belgeleri](</tr/automation/hooks#boot-md>)

## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Otomasyon kancaları](</tr/automation/hooks>)


Was this useful?YesNo