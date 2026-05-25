---
title: macOS imzalama
source_url: https://docs.openclaw.ai/tr/platforms/mac/signing
scraped_at: 2026-05-25
---

# mac imzalama (hata ayıklama derlemeleri)

Bu uygulama genellikle [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) üzerinden derlenir; bu betik artık:

  * kararlı bir hata ayıklama paket tanımlayıcısı ayarlar: `ai.openclaw.mac.debug`
  * Info.plist dosyasını bu paket kimliğiyle yazar (`BUNDLE_ID=...` ile geçersiz kılın)
  * macOS’in her yeniden derlemeyi aynı imzalı paket olarak ele alması ve TCC izinlerini (bildirimler, erişilebilirlik, ekran kaydı, mikrofon, konuşma) koruması için ana ikiliyi ve uygulama paketini imzalamak üzere [`scripts/codesign-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/codesign-mac-app.sh>) dosyasını çağırır. Kararlı izinler için gerçek bir imzalama kimliği kullanın; ad-hoc isteğe bağlıdır ve kırılgandır (bkz. [macOS izinleri](</tr/platforms/mac/permissions>)).
  * varsayılan olarak `CODESIGN_TIMESTAMP=auto` kullanır; Developer ID imzaları için güvenilir zaman damgalarını etkinleştirir. Zaman damgalamayı atlamak için `CODESIGN_TIMESTAMP=off` ayarlayın (çevrimdışı hata ayıklama derlemeleri).
  * derleme üst verilerini Info.plist içine enjekte eder: `OpenClawBuildTimestamp` (UTC) ve `OpenClawGitCommit` (kısa hash); böylece Hakkında bölmesi derlemeyi, git’i ve hata ayıklama/sürüm kanalını gösterebilir.
  * **Paketleme varsayılan olarak Node 24 kullanır** : betik TS derlemelerini ve Control UI derlemesini çalıştırır. Şu anda `22.16+` olan Node 22 LTS, uyumluluk için desteklenmeye devam eder.
  * ortamdan `SIGN_IDENTITY` değerini okur. Her zaman sertifikanızla imzalamak için kabuk rc dosyanıza `export SIGN_IDENTITY="Apple Development: Your Name (TEAMID)"` (veya Developer ID Application sertifikanızı) ekleyin. Ad-hoc imzalama, `ALLOW_ADHOC_SIGNING=1` veya `SIGN_IDENTITY="-"` üzerinden açıkça etkinleştirme gerektirir (izin testi için önerilmez).
  * imzalamadan sonra bir Team ID denetimi çalıştırır ve uygulama paketinin içindeki herhangi bir Mach-O farklı bir Team ID ile imzalanmışsa başarısız olur. Atlamak için `SKIP_TEAM_ID_CHECK=1` ayarlayın.


## Kullanım

bashCopy code
[code]
    # from repo rootscripts/package-mac-app.sh               # auto-selects identity; errors if none foundSIGN_IDENTITY="Developer ID Application: Your Name" scripts/package-mac-app.sh   # real certALLOW_ADHOC_SIGNING=1 scripts/package-mac-app.sh    # ad-hoc (permissions will not stick)SIGN_IDENTITY="-" scripts/package-mac-app.sh        # explicit ad-hoc (same caveat)DISABLE_LIBRARY_VALIDATION=1 scripts/package-mac-app.sh   # dev-only Sparkle Team ID mismatch workaround
[/code]

### Ad-hoc İmzalama Notu

`SIGN_IDENTITY="-"` (ad-hoc) ile imzalama yapıldığında, betik **Hardened Runtime** (`--options runtime`) özelliğini otomatik olarak devre dışı bırakır. Bu, uygulama aynı Team ID’yi paylaşmayan gömülü framework’leri (Sparkle gibi) yüklemeye çalıştığında çökmeleri önlemek için gereklidir. Ad-hoc imzalar ayrıca TCC izin kalıcılığını bozar; kurtarma adımları için [macOS izinleri](</tr/platforms/mac/permissions>) sayfasına bakın.

## Hakkında için derleme üst verileri

`package-mac-app.sh` paketi şunlarla damgalar:

  * `OpenClawBuildTimestamp`: paketleme anında ISO8601 UTC
  * `OpenClawGitCommit`: kısa git hash’i (veya kullanılamıyorsa `unknown`)


Hakkında sekmesi bu anahtarları okuyarak sürümü, derleme tarihini, git commit’ini ve bunun bir hata ayıklama derlemesi olup olmadığını (`#if DEBUG` aracılığıyla) gösterir. Kod değişikliklerinden sonra bu değerleri yenilemek için paketleyiciyi çalıştırın.

## Neden

TCC izinleri paket tanımlayıcısına _ve_ kod imzasına bağlıdır. Değişen UUID’lere sahip imzasız hata ayıklama derlemeleri, macOS’in her yeniden derlemeden sonra verilen izinleri unutmasına neden oluyordu. İkilileri (varsayılan olarak ad-hoc) imzalamak ve sabit bir paket kimliği/yolu (`dist/OpenClaw.app`) korumak, VibeTunnel yaklaşımıyla uyumlu şekilde derlemeler arasında izinleri korur.

## İlgili

  * [macOS uygulaması](</tr/platforms/macos>)
  * [macOS izinleri](</tr/platforms/mac/permissions>)


Was this useful?YesNo