---
title: Transcripts CLI
source_url: https://docs.openclaw.ai/tr/cli/transcripts
scraped_at: 2026-06-29
---

Get started

# `openclaw transcripts`

OpenClaw'ın çekirdek `transcripts` aracı tarafından yazılan transkriptleri inceleyin. Bu CLI salt okunurdur; yakalama, içe aktarma ve özetleme agent aracı ile yapılandırılmış otomatik başlatma kaynaklarına aittir.

Dünkü notları bulmak, Markdown dosyasını bir düzenleyicide açmak, bir transkripti başka bir araca vermek veya bir oturumun diskte nereye kaydedildiğini ayıklamak istediğinizde CLI'yi kullanın. Yakalamayı başlatmaz veya durdurmaz.

Yapıtlar OpenClaw durum dizini altında bulunur:

textCopy code
[code]
    $OPENCLAW_STATE_DIR/transcripts/YYYY-MM-DD/<session>/  metadata.json  transcript.jsonl  summary.json  summary.md
[/code]

Varsayılan durum dizini `~/.openclaw` dizinidir; farklı bir dizin kullanmak için `OPENCLAW_STATE_DIR` ayarlayın. Tarih dizini oturum başlangıç zamanından gelir ve oturum dizini, oturum kimliğinden türetilmiş güvenli bir dosya sistemi segmentidir.

## Komutlar

bashCopy code
[code]
    openclaw transcripts listopenclaw transcripts show <session>openclaw transcripts show YYYY-MM-DD/<session>openclaw transcripts path <session>openclaw transcripts path YYYY-MM-DD/<session>openclaw transcripts path <session> --diropenclaw transcripts path <session> --metadataopenclaw transcripts path <session> --transcriptopenclaw transcripts list --jsonopenclaw transcripts show <session> --jsonopenclaw transcripts path <session> --json
[/code]

  * `list`: saklanan oturumları, tarih nitelemeli seçiciyi, başlangıç zamanını, başlığı ve `summary.md` yolunu listeler.
  * `show <session>`: saklanan `summary.md` içeriğini yazdırır.
  * `path <session>`: `summary.md` yolunu yazdırır.
  * `path <session> --dir`: oturum dizinini yazdırır.
  * `path <session> --metadata`: `metadata.json` dosyasını yazdırır.
  * `path <session> --transcript`: `transcript.jsonl` dosyasını yazdırır.
  * `--json`: makine tarafından okunabilir çıktı yazdırır.


İnsan tarafından verilen bir oturum kimliği günler arasında tekrarlandığında, `list` çıktısındaki tarih nitelemeli seçiciyi kullanın; örneğin `openclaw transcripts show 2026-05-22/standup`. Varsayılan oturum kimlikleri bir zaman damgası ve rastgele sonek içerir; sabit oturum kimliklerini yalnızca gün içinde benzersiz olduklarında yapılandırın.

## Çıktı

`list`, her satıra bir oturum yazdırır:

textCopy code
[code]
    2026-05-22/standup  2026-05-22T09:00:00.000Z  Weekly standup  /Users/alex/.openclaw/transcripts/2026-05-22/standup/summary.md
[/code]

Çıktı sekmeyle ayrılır. Sütunlar seçici, başlangıç zamanı, başlık ve özet yoludur. Seçici, `show` veya `path` komutuna geri vermek için en güvenli değerdir.

`list --json`, şu alanlara sahip nesneler yazdırır:

  * `sessionId`
  * `selector`
  * `date`
  * `title`
  * `startedAt`
  * `stoppedAt`
  * `source`
  * `path`
  * `summaryPath`
  * `hasSummary`


`show --json`, saklanan oturum meta verilerini, seçiciyi, oturum dizinini, özet yolunu ve özet Markdown metnini döndürür. `path --json`, seçilen yolu ve o dosyanın var olup olmadığını döndürür.

## Günde çok sayıda toplantı

Transkriptler oturumları önce tarihe, sonra oturum kimliğine göre gruplar. Bir gündeki on toplantı, on kardeş klasöre dönüşür:

textCopy code
[code]
    ~/.openclaw/transcripts/2026-05-22/  transcript-2026-05-22T09-00-00-000Z-a1b2c3d4/  transcript-2026-05-22T10-30-00-000Z-b2c3d4e5/  standup/
[/code]

Çoğu otomasyon için varsayılan oluşturulan kimlikleri kullanın. `standup` gibi sabit bir kimliği yalnızca aynı kimlik aynı tarihte iki kez kullanılmayacaksa kullanın.

## Eksik özetler

Canlı oturumlar, oturum durduğunda `summary.md` yazar. İçe aktarılan transkriptler içe aktarmadan hemen sonra `summary.md` yazar. Yakalama etkinken, durdurma sırasında bir sağlayıcı başarısız olduğunda veya herhangi bir ifade gelmeden önce meta veriler yazıldığında bir oturum yine de `list` içinde özet olmadan görünebilir.

Salt eklemeli transkripti incelemek için `path <session> --transcript` kullanın ve Markdown özetini yeniden oluşturmak için `transcripts` araç eylemi `summarize` kullanın.

## Yapılandırma

Transkript yakalama isteğe bağlıdır, çünkü canlı kaynaklar toplantı sesine katılabilir ve onu kaydedebilir. Aracı üst düzey `transcripts.enabled` ile etkinleştirin:

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "maxUtterances": 2000  }}
[/code]

Otomatik başlatma kaynaklarını `openclaw.json` içinde `transcripts.autoStart` ile yapılandırın. Her giriş mevcut olduğunda etkinleştirilir; bir kaynağı devre dışı bırakmak için ilgili girişi atlayın.

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "autoStart": [      {        "providerId": "discord-voice",        "guildId": "1234567890",        "channelId": "2345678901"      },      {        "providerId": "slack-huddle",        "accountId": "workspace",        "channelId": "C123"      }    ]  }}
[/code]

Was this useful?YesNo

Open issue