---
title: Tanılama bayrakları
source_url: https://docs.openclaw.ai/tr/diagnostics/flags
scraped_at: 2026-05-25
---

Tanılama bayrakları, her yerde ayrıntılı günlük kaydını açmadan hedeflenmiş hata ayıklama günlüklerini etkinleştirmenizi sağlar. Bayraklar isteğe bağlıdır ve bir alt sistem bunları denetlemediği sürece etkili olmaz.

## Nasıl çalışır?

  * Bayraklar dizelerdir (büyük/küçük harfe duyarsız).
  * Bayrakları yapılandırmada veya bir ortam değişkeni geçersiz kılmasıyla etkinleştirebilirsiniz.
  * Joker karakterler desteklenir: 
    * `telegram.*`, `telegram.http` ile eşleşir
    * `*` tüm bayrakları etkinleştirir


## Yapılandırma ile etkinleştirme

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Birden çok bayrak:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Bayrakları değiştirdikten sonra Gateway'i yeniden başlatın.

## Ortam değişkeni geçersiz kılması (tek seferlik)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Tüm bayrakları devre dışı bırakma:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## Zaman çizelgesi artefaktları

`timeline` bayrağı, harici QA donanımları için yapılandırılmış başlangıç ve çalışma zamanı zamanlama olayları yazar:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Bunu yapılandırmada da etkinleştirebilirsiniz:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

Zaman çizelgesi dosya yolu yine `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH` değerinden gelir. `timeline` yalnızca yapılandırmadan etkinleştirildiğinde, OpenClaw yapılandırmayı henüz okumamış olduğundan en erken yapılandırma yükleme aralıkları yayımlanmaz; sonraki başlangıç aralıkları yapılandırma bayrağını kullanır.

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` ve `OPENCLAW_DIAGNOSTICS=*` de her tanılama bayrağını etkinleştirdikleri için zaman çizelgesini etkinleştirir. Yalnızca JSONL zamanlama artefaktını istiyorsanız `timeline` tercih edin.

Zaman çizelgesi kayıtları `openclaw.diagnostics.v1` zarfını kullanır. Olaylar işlem kimlikleri, aşama adları, aralık adları, süreler, Plugin kimlikleri, bağımlılık sayıları, olay döngüsü gecikme örnekleri, sağlayıcı işlem adları, alt işlem çıkış durumu ve başlangıç hatası adları/iletileri içerebilir. Zaman çizelgesi dosyalarını yerel tanılama artefaktları olarak ele alın; makinenizin dışında paylaşmadan önce gözden geçirin.

## Günlükler nereye gider?

Bayraklar, günlükleri standart tanılama günlük dosyasına yazar. Varsayılan olarak:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

`logging.file` ayarlarsanız bunun yerine o yolu kullanın. Günlükler JSONL biçimindedir (satır başına bir JSON nesnesi). Sansürleme yine `logging.redactSensitive` değerine göre uygulanır.

## Günlükleri çıkarma

En son günlük dosyasını seçin:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Telegram HTTP tanılaması için filtreleyin:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Brave Search HTTP tanılaması için filtreleyin:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Veya yeniden üretirken takip edin:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

Uzak Gateway'ler için `openclaw logs --follow` da kullanabilirsiniz (bkz. [/cli/logs](</tr/cli/logs>)).

## Notlar

  * `logging.level`, `warn` değerinden daha yüksek ayarlanmışsa bu günlükler bastırılabilir. Varsayılan `info` uygundur.
  * `brave.http`, Brave Search istek URL'lerini/sorgu parametrelerini, yanıt durumunu/zamanlamasını ve önbellek isabet/kaçırma/yazma olaylarını günlüğe kaydeder. API anahtarlarını veya yanıt gövdelerini günlüğe kaydetmez, ancak arama sorguları hassas olabilir.
  * Bayrakları etkin bırakmak güvenlidir; yalnızca ilgili alt sistemin günlük hacmini etkilerler.
  * Günlük hedeflerini, düzeylerini ve sansürlemeyi değiştirmek için [/logging](</tr/logging>) kullanın.


## İlgili

  * [Gateway tanılaması](</tr/gateway/diagnostics>)
  * [Gateway sorun giderme](</tr/gateway/troubleshooting>)


Was this useful?YesNo