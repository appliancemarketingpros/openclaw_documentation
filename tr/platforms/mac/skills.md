---
title: Skills (macOS)
source_url: https://docs.openclaw.ai/tr/platforms/mac/skills
scraped_at: 2026-05-25
---

macOS uygulaması OpenClaw Skills'i gateway üzerinden gösterir; Skills'i yerelde ayrıştırmaz.

## Veri kaynağı

  * `skills.status` (gateway), tüm Skills'i uygunluk ve eksik gereksinimlerle birlikte döndürür (paketle gelen Skills için izin listesi engelleri dahil).
  * Gereksinimler, her `SKILL.md` içindeki `metadata.openclaw.requires` alanından türetilir.


## Kurulum eylemleri

  * `metadata.openclaw.install`, kurulum seçeneklerini tanımlar (brew/node/go/uv).
  * Uygulama, kurucuları gateway host üzerinde çalıştırmak için `skills.install` çağırır.
  * Yerleşik tehlikeli kod `critical` bulguları, varsayılan olarak `skills.install` işlemini engeller; şüpheli bulgular ise yalnızca uyarı verir. Tehlikeli geçersiz kılma gateway isteğinde bulunur, ancak varsayılan uygulama akışı kapalı varsayımla kalır.
  * Her kurulum seçeneği `download` ise gateway, tüm indirme seçeneklerini gösterir.
  * Aksi halde gateway, geçerli kurulum tercihleri ve host binary'lerini kullanarak bir tercihli kurucu seçer: `skills.install.preferBrew` etkinse ve `brew` mevcutsa önce Homebrew, sonra `uv`, sonra `skills.install.nodeManager` içindeki yapılandırılmış Node yöneticisi, ardından `go` veya `download` gibi daha sonraki geri dönüşler.
  * Node kurulum etiketleri, `yarn` dahil yapılandırılmış Node yöneticisini yansıtır.


## Env/API anahtarları

  * Uygulama, anahtarları `~/.openclaw/openclaw.json` içinde `skills.entries.<skillKey>` altında saklar.
  * `skills.update`, `enabled`, `apiKey` ve `env` alanlarını yamalar.


## Uzak mod

  * Kurulum + yapılandırma güncellemeleri yerel Mac üzerinde değil, gateway host üzerinde gerçekleşir.


## İlgili

  * [Skills](</tr/tools/skills>)
  * [macOS uygulaması](</tr/platforms/macos>)


Was this useful?YesNo