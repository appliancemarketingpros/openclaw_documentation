---
title: OpenClaw ajan çalışma zamanı iş akışı
source_url: https://docs.openclaw.ai/tr/openclaw-agent-runtime
scraped_at: 2026-06-29
---

InstallAdvanced setup

OpenClaw içinde OpenClaw ajan çalışma zamanı üzerinde çalışmak için makul bir iş akışı.

## Tür denetimi ve linting

  * Varsayılan yerel gate: `pnpm check`
  * Derleme gate'i: Değişiklik derleme çıktısını, paketlemeyi veya lazy-loading/modül sınırlarını etkileyebildiğinde `pnpm build`
  * Ajan çalışma zamanı değişiklikleri için tam landing gate'i: `pnpm check && pnpm test`


## Ajan Çalışma Zamanı Testlerini Çalıştırma

Ajan çalışma zamanı test kümesini doğrudan Vitest ile çalıştırın:

bashCopy code
[code]
    pnpm test \  "src/agents/agent-*.test.ts" \  "src/agents/embedded-agent-*.test.ts" \  "src/agents/agent-tools*.test.ts" \  "src/agents/agent-settings.test.ts" \  "src/agents/agent-tool-definition-adapter*.test.ts" \  "src/agents/agent-hooks/**/*.test.ts"
[/code]

Canlı sağlayıcı alıştırmasını dahil etmek için:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/embedded-agent-runner-extraparams.live.test.ts
[/code]

Bu, ana ajan çalışma zamanı birim test paketlerini kapsar:

  * `src/agents/agent-*.test.ts`
  * `src/agents/embedded-agent-*.test.ts`
  * `src/agents/agent-tools*.test.ts`
  * `src/agents/agent-settings.test.ts`
  * `src/agents/agent-tool-definition-adapter.test.ts`
  * `src/agents/agent-hooks/*.test.ts`


## Manuel test

Önerilen akış:

  * Gateway'i geliştirme modunda çalıştırın: 
    * `pnpm gateway:dev`
  * Ajanı doğrudan tetikleyin: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Etkileşimli hata ayıklama için TUI'yi kullanın: 
    * `pnpm tui`


Araç çağrısı davranışı için, araç akışını ve yük işleme sürecini görebilmek üzere bir `read` veya `exec` eylemi isteyin.

## Temiz başlangıç sıfırlaması

Durum, OpenClaw durum dizini altında bulunur. Varsayılan değer `~/.openclaw` şeklindedir. `OPENCLAW_STATE_DIR` ayarlanmışsa bunun yerine o dizini kullanın.

Her şeyi sıfırlamak için:

  * Yapılandırma için `openclaw.json`
  * Model kimlik doğrulama profilleri için `agents/<agentId>/agent/auth-profiles.json` (API anahtarları + OAuth)
  * Hâlâ kimlik doğrulama profili deposunun dışında bulunan sağlayıcı/kanal durumu için `credentials/`
  * Ajan oturum geçmişi için `agents/<agentId>/sessions/`
  * Oturum dizini için `agents/<agentId>/sessions/sessions.json`
  * Eski yollar varsa `sessions/`
  * Boş bir çalışma alanı istiyorsanız `workspace/`


Yalnızca oturumları sıfırlamak istiyorsanız, o ajan için `agents/<agentId>/sessions/` dizinini silin. Kimlik doğrulamayı korumak istiyorsanız, `agents/<agentId>/agent/auth-profiles.json` dosyasını ve `credentials/` altındaki tüm sağlayıcı durumunu yerinde bırakın.

## Başvurular

  * [Test Etme](</tr/help/testing>)
  * [Başlarken](</tr/start/getting-started>)


## İlgili

  * [OpenClaw ajan çalışma zamanı mimarisi](</tr/agent-runtime-architecture>)


Was this useful?YesNo

Open issue