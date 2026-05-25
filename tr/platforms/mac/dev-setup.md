---
title: macOS geliştirme kurulumu
source_url: https://docs.openclaw.ai/tr/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# macOS geliştirici kurulumu

OpenClaw macOS uygulamasını kaynaktan derleyip çalıştırın.

## Ön koşullar

Uygulamayı derlemeden önce aşağıdakilerin kurulu olduğundan emin olun:

  1. **Xcode 26.2+** : Swift geliştirme için gereklidir.
  2. **Node.js 24 ve pnpm** : Gateway, CLI ve paketleme betikleri için önerilir. Şu anda `22.16+` olan Node 22 LTS, uyumluluk için desteklenmeye devam eder.


## 1\. Bağımlılıkları yükleyin

Proje genelindeki bağımlılıkları yükleyin:

bashCopy code
[code]
    pnpm install
[/code]

## 2\. Uygulamayı derleyin ve paketleyin

macOS uygulamasını derleyip `dist/OpenClaw.app` içine paketlemek için şunu çalıştırın:

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

Apple Developer ID sertifikanız yoksa betik otomatik olarak **ad-hoc imzalama** (`-`) kullanır.

Geliştirme çalıştırma modları, imzalama bayrakları ve Team ID sorun giderme için macOS uygulaması README dosyasına bakın: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **Not** : Ad-hoc imzalanmış uygulamalar güvenlik istemlerini tetikleyebilir. Uygulama "Abort trap 6" ile hemen çöküyorsa Sorun giderme bölümüne bakın.

## 3\. CLI'ı yükleyin

macOS uygulaması, arka plan görevlerini yönetmek için genel bir `openclaw` CLI kurulumunun olmasını bekler.

**Yüklemek için (önerilir):**

  1. OpenClaw uygulamasını açın.
  2. **General** ayarlar sekmesine gidin.
  3. **"Install CLI"** düğmesine tıklayın.


Alternatif olarak elle yükleyin:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

`pnpm add -g openclaw@<version>` ve `bun add -g openclaw@<version>` de çalışır. Gateway çalışma zamanı için Node önerilen yol olmaya devam eder.

## Sorun giderme

### Derleme başarısız oluyor: araç zinciri veya SDK uyumsuzluğu

macOS uygulama derlemesi en yeni macOS SDK'sını ve Swift 6.2 araç zincirini bekler.

**Sistem bağımlılıkları (gerekli):**

  * **Software Update içinde sunulan en yeni macOS sürümü** (Xcode 26.2 SDK'ları tarafından gereklidir)
  * **Xcode 26.2** (Swift 6.2 araç zinciri)


**Kontroller:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

Sürümler eşleşmiyorsa macOS/Xcode'u güncelleyin ve derlemeyi yeniden çalıştırın.

### İzin verme sırasında uygulama çöküyor

**Speech Recognition** veya **Microphone** erişimine izin vermeye çalıştığınızda uygulama çöküyorsa bunun nedeni bozuk bir TCC önbelleği veya imza uyumsuzluğu olabilir.

**Düzeltme:**

  1. TCC izinlerini sıfırlayın:

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. Bu başarısız olursa macOS'tan "temiz başlangıç" zorlamak için [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) içindeki `BUNDLE_ID` değerini geçici olarak değiştirin.


### Gateway "Starting..." durumunda süresiz kalıyor

Gateway durumu "Starting..." olarak kalıyorsa bağlantı noktasını tutan bir zombi süreç olup olmadığını kontrol edin:

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # LaunchAgent kullanmıyorsanız (geliştirme modu / elle çalıştırmalar), dinleyiciyi bulun:lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

Elle çalıştırılan bir süreç bağlantı noktasını tutuyorsa bu süreci durdurun (Ctrl+C). Son çare olarak yukarıda bulduğunuz PID'yi sonlandırın.

## İlgili

  * [macOS uygulaması](</tr/platforms/macos>)
  * [Kurulum özeti](</tr/install>)


Was this useful?YesNo