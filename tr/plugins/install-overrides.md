---
title: Plugin kurulum geçersiz kılmaları
source_url: https://docs.openclaw.ai/tr/plugins/install-overrides
scraped_at: 2026-05-25
---

Plugin yükleme geçersiz kılmaları, bakımcıların kurulum zamanı Plugin yüklemelerini belirli bir npm paketi veya yerel npm-pack tarball dosyasına karşı test etmesini sağlar. Bunlar yalnızca E2E ve paket doğrulaması içindir. Normal kullanıcılar Pluginleri [`openclaw plugins install`](</tr/cli/plugins>) ile yüklemelidir.

## Ortam

Her iki değişken de ayarlanmadıkça geçersiz kılmalar devre dışıdır:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

Geçersiz kılma eşlemesi, Plugin kimliğine göre anahtarlanan JSON'dur. Değerler şunları destekler:

  * Kayıt paketleri ve tam sürümler ya da etiketler için `npm:<registry-spec>`
  * `npm pack` tarafından üretilen yerel tarball dosyaları için `npm-pack:<path.tgz>`


Göreli `npm-pack:` yolları geçerli çalışma dizininden çözümlenir.

## Davranış

Kurulum zamanı bir akış, kimliği eşlemede görünen bir Pluginin yüklenmesini istediğinde, OpenClaw katalog, paketle birlikte gelen veya varsayılan npm kaynağı yerine geçersiz kılma kaynağını kullanır. Bu, paylaşılan kurulum zamanı Plugin yükleyicisini kullanan onboarding ve diğer akışlar için geçerlidir.

Geçersiz kılmalar beklenen Plugin kimliğini yine de zorunlu kılar. `codex` ile eşlenen bir tarball, manifest kimliği `codex` olan bir Plugin yüklemelidir.

Geçersiz kılmalar resmi güvenilir kaynak durumunu devralmaz. Katalog girdisi normalde OpenClaw'a ait bir paketi temsil etse bile, geçersiz kılma operatör tarafından sağlanan test girdisi olarak değerlendirilir.

Çalışma alanı `.env` dosyaları yükleme geçersiz kılmalarını etkinleştiremez. Bu değişkenleri, OpenClaw'ı başlatan güvenilir kabukta, CI işinde veya uzak test komutunda ayarlayın.

## Paket E2E

Paket yüklemelerinin ve yükleme kayıtlarının normal OpenClaw durumunuza dokunmaması için yalıtılmış bir durum dizini kullanın:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Yüklü paketi durum dizini altında doğrulayın:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

Canlı sağlayıcı E2E için, test komutunu başlatmadan önce gerçek API anahtarını güvenilir bir kabuktan veya CI sırrından kaynaklayın. Anahtarları yazdırmayın; yalnızca kaynağı ve anahtarın mevcut olup olmadığını raporlayın.

Was this useful?YesNo