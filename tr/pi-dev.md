---
title: Pi geliştirme iş akışı
source_url: https://docs.openclaw.ai/tr/pi-dev
scraped_at: 2026-05-25
---

OpenClaw içinde Pi entegrasyonu üzerinde çalışmak için sağlıklı bir iş akışı.

## Tür denetimi ve linting

  * Varsayılan yerel doğrulama kapısı: `pnpm check`
  * Derleme kapısı: Değişiklik derleme çıktısını, paketlemeyi veya lazy-loading/modül sınırlarını etkileyebiliyorsa `pnpm build`
  * Pi ağırlıklı değişiklikler için tam landing kapısı: `pnpm check && pnpm test`


## Pi testlerini çalıştırma

Pi odaklı test kümesini doğrudan Vitest ile çalıştırın:

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

Canlı sağlayıcı denemesini dahil etmek için:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

Bu, ana Pi birim test paketlerini kapsar:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## Manuel test

Önerilen akış:

  * Gateway'i geliştirme modunda çalıştırın: 
    * `pnpm gateway:dev`
  * Ajanı doğrudan tetikleyin: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Etkileşimli hata ayıklama için TUI'yi kullanın: 
    * `pnpm tui`


Araç çağrısı davranışı için, araç akışını ve yük işlemeyi görebilmek üzere bir `read` veya `exec` eylemi isteyin.

## Temiz başlangıç sıfırlaması

Durum, OpenClaw durum dizini altında bulunur. Varsayılan değer `~/.openclaw` dizinidir. `OPENCLAW_STATE_DIR` ayarlanmışsa bunun yerine o dizini kullanın.

Her şeyi sıfırlamak için:

  * Yapılandırma için `openclaw.json`
  * Model kimlik doğrulama profilleri (API anahtarları + OAuth) için `agents/<agentId>/agent/auth-profiles.json`
  * Kimlik doğrulama profili deposunun dışında yaşamaya devam eden sağlayıcı/kanal durumu için `credentials/`
  * Ajan oturum geçmişi için `agents/<agentId>/sessions/`
  * Oturum dizini için `agents/<agentId>/sessions/sessions.json`
  * Eski yollar mevcutsa `sessions/`
  * Boş bir çalışma alanı istiyorsanız `workspace/`


Yalnızca oturumları sıfırlamak istiyorsanız, ilgili ajan için `agents/<agentId>/sessions/` dizinini silin. Kimlik doğrulamayı korumak istiyorsanız `agents/<agentId>/agent/auth-profiles.json` dosyasını ve `credentials/` altındaki sağlayıcı durumlarını yerinde bırakın.

## Başvurular

  * [Test Etme](</tr/help/testing>)
  * [Başlarken](</tr/start/getting-started>)


## İlgili

  * [Pi entegrasyonu mimarisi](</tr/pi>)


Was this useful?YesNo