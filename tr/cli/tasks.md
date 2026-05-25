---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/tr/cli/tasks
scraped_at: 2026-05-25
---

Dayanıklı arka plan görevlerini ve Task Flow durumunu inceleyin. Alt komut olmadan, `openclaw tasks`, `openclaw tasks list` ile eşdeğerdir.

Yaşam döngüsü ve teslim modeli için [Arka Plan Görevleri](</tr/automation/tasks>) bölümüne bakın.

## Kullanım

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Kök Seçenekler

  * `--json`: JSON çıktısı üretir.
  * `--runtime <name>`: türe göre filtreler: `subagent`, `acp`, `cron` veya `cli`.
  * `--status <name>`: duruma göre filtreler: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` veya `lost`.


## Alt Komutlar

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

İzlenen arka plan görevlerini en yeniden en eskiye doğru listeler.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Görev kimliği, çalıştırma kimliği veya oturum anahtarıyla tek bir görevi gösterir.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Çalışan bir görevin bildirim politikasını değiştirir.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Çalışan bir arka plan görevini iptal eder.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Bayat, kayıp, teslimi başarısız olmuş veya başka şekilde tutarsız görev ve Task Flow kayıtlarını ortaya çıkarır. `cleanupAfter` zamanına kadar tutulan kayıp görevler uyarıdır; süresi dolmuş veya damgalanmamış kayıp görevler hatadır.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Görev ve Task Flow mutabakatını, temizleme damgalamasını, budamayı ve bayat cron çalıştırma oturumu kayıt defteri temizliğini önizler veya uygular. Cron görevleri için mutabakat, eski bir etkin görevi `lost` olarak işaretlemeden önce kalıcı çalıştırma günlüklerini/iş durumunu kullanır; böylece tamamlanmış cron çalıştırmaları, yalnızca bellek içi Gateway çalışma zamanı durumu kaybolduğu için yanlış denetim hatalarına dönüşmez. Çevrimdışı CLI denetimi, Gateway'in süreç yerel cron etkin iş kümesi için yetkili kaynak değildir. Çalıştırma kimliği/kaynak kimliği olan CLI görevleri, eski bir alt oturum satırı kalsa bile canlı Gateway çalıştırma bağlamları kaybolduğunda `lost` olarak işaretlenir. Uygulandığında bakım, şu anda çalışan cron işlerini korurken ve cron olmayan oturum satırlarına dokunmadan 7 günden eski `cron:<jobId>:run:<uuid>` oturum kayıt defteri satırlarını da budar.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Görev defteri altındaki dayanıklı Task Flow durumunu inceler veya iptal eder.

## İlgili

  * [CLI referansı](</tr/cli>)
  * [Arka plan görevleri](</tr/automation/tasks>)


Was this useful?YesNo