---
title: Bun (deneysel)
source_url: https://docs.openclaw.ai/tr/install/bun
scraped_at: 2026-05-25
---

Bun, TypeScript'i doğrudan çalıştırmak için isteğe bağlı bir yerel çalışma zamanıdır (`bun run ...`, `bun --watch ...`). Varsayılan paket yöneticisi, tamamen desteklenen ve belge araçları tarafından kullanılan `pnpm` olarak kalır. Bun, `pnpm-lock.yaml` dosyasını kullanamaz ve onu yok sayar.

## Kurulum

* ### Install dependencies

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` git tarafından yok sayılır, bu yüzden depoda değişiklik gürültüsü oluşmaz. Kilit dosyası yazımlarını tamamen atlamak için:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Build and test

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Yaşam döngüsü betikleri

Bun, açıkça güvenilmediği sürece bağımlılık yaşam döngüsü betiklerini engeller. Bu depo için yaygın olarak engellenen betikler gerekli değildir:

  * `baileys` `preinstall` \-- Node ana sürümünün >= 20 olduğunu denetler (OpenClaw varsayılan olarak Node 24 kullanır ve şu anda `22.16+` olan Node 22 LTS'yi hâlâ destekler)
  * `protobufjs` `postinstall` \-- uyumsuz sürüm şemaları hakkında uyarılar üretir (derleme yapıtı yok)


Bu betikleri gerektiren bir çalışma zamanı sorunuyla karşılaşırsanız, onlara açıkça güvenin:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Uyarılar

Bazı betikler hâlâ pnpm'i sabit olarak kullanır (örneğin `docs:build`, `ui:*`, `protocol:check`). Şimdilik bunları pnpm üzerinden çalıştırın.

## İlgili

  * [Kurulum genel bakışı](</tr/install>)
  * [Node.js](</tr/install/node>)
  * [Güncelleme](</tr/install/updating>)


Was this useful?YesNo