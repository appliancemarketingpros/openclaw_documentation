---
title: Node + tsx çökmesi
source_url: https://docs.openclaw.ai/tr/debug/node-issue
scraped_at: 2026-05-25
---

# Node + tsx "__name is not a function" çökmesi

## Özet

OpenClaw’ı Node üzerinden `tsx` ile çalıştırmak başlangıçta şu hatayla başarısız oluyor:

CodeCopy code
[code]
    [openclaw] Failed to start CLI: TypeError: __name is not a function    at createSubsystemLogger (.../src/logging/subsystem.ts:203:25)    at .../src/agents/auth-profiles/constants.ts:25:20
[/code]

Bu, geliştirme betikleri Bun’dan `tsx`’e geçirildikten sonra başladı (commit `2871657e`, 2026-01-06). Aynı çalışma zamanı yolu Bun ile çalışıyordu.

## Ortam

  * Node: v25.x (v25.3.0 üzerinde gözlendi)
  * tsx: 4.21.0
  * OS: macOS (yeniden üretim Node 25 çalıştıran diğer platformlarda da olası)


## Yeniden üretim (yalnızca Node)

bashCopy code
[code]
    # in repo rootnode --versionpnpm installnode --import tsx src/entry.ts status
[/code]

## Repoda minimal yeniden üretim

bashCopy code
[code]
    node --import tsx scripts/repro/tsx-name-repro.ts
[/code]

## Node sürümü kontrolü

  * Node 25.3.0: başarısız
  * Node 22.22.0 (Homebrew `node@22`): başarısız
  * Node 24: burada henüz yüklü değil; doğrulama gerekiyor


## Notlar / hipotez

  * `tsx`, TS/ESM dönüştürmek için esbuild kullanır. esbuild’in `keepNames` seçeneği bir `__name` yardımcısı üretir ve işlev tanımlarını `__name(...)` ile sarar.
  * Çökme, `__name` değerinin var olduğunu ancak çalışma zamanında bir işlev olmadığını gösteriyor; bu da yardımcının Node 25 yükleyici yolunda bu modül için eksik olduğu veya üzerine yazıldığı anlamına gelir.
  * Benzer `__name` yardımcısı sorunları, yardımcının eksik olduğu veya yeniden yazıldığı durumlarda diğer esbuild tüketicilerinde bildirilmiştir.


## Regresyon geçmişi

  * `2871657e` (2026-01-06): Bun’ı isteğe bağlı hale getirmek için betikler Bun’dan tsx’e geçirildi.
  * Bundan önce (Bun yolu), `openclaw status` ve `gateway:watch` çalışıyordu.


## Geçici çözümler

  * Geliştirme betikleri için Bun kullanın (mevcut geçici geri alma).

  * Repo tür denetimi için `tsgo` kullanın, ardından oluşturulan çıktıyı çalıştırın:

bashCopy code
[code]pnpm tsgonode openclaw.mjs status
[/code]

  * Tarihsel not: Bu Node/tsx sorunu hata ayıklanırken burada `tsc` kullanılmıştı, ancak repo tür denetimi hatları artık `tsgo` kullanıyor.

  * Mümkünse TS yükleyicisinde esbuild keepNames seçeneğini devre dışı bırakın (`__name` yardımcısının eklenmesini önler); tsx şu anda bunu dışa açmıyor.

  * Sorunun Node 25’e özgü olup olmadığını görmek için Node LTS (22/24) sürümlerini `tsx` ile test edin.


## Referanslar

  * <https://opennext.js.org/cloudflare/howtos/keep_names>
  * <https://esbuild.github.io/api/#keep-names>
  * <https://github.com/evanw/esbuild/issues/1031>


## Sonraki adımlar

  * Node 25 regresyonunu doğrulamak için Node 22/24 üzerinde yeniden üretin.
  * Bilinen bir regresyon varsa `tsx` nightly sürümünü test edin veya daha eski bir sürüme sabitleyin.
  * Node LTS üzerinde yeniden üretilirse, `__name` yığın izlemesiyle birlikte üst projeye minimal bir yeniden üretim bildirin.


## İlgili

  * [Node.js kurulumu](</tr/install/node>)
  * [Gateway sorun giderme](</tr/gateway/troubleshooting>)


Was this useful?YesNo