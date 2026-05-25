---
title: Akışlar (yönlendirme)
source_url: https://docs.openclaw.ai/tr/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Üst düzey bir `openclaw flows` komutu yoktur. Kalıcı TaskFlow incelemesi `openclaw tasks flow` altında yer alır.

## Alt komutlar

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Alt komut | Açıklama | Argümanlar / seçenekler  
---|---|---  
`list` | İzlenen TaskFlow'ları listele. | `--json` makine tarafından okunabilir çıktı; `--status <name>` filtresi (aşağıdaki durum değerlerine bakın).  
`show` | Bir TaskFlow göster. | `<lookup>` akış kimliği veya sahip anahtarı; `--json` makine tarafından okunabilir çıktı.  
`cancel` | Çalışan bir TaskFlow'u iptal et. | `<lookup>` akış kimliği veya sahip anahtarı.  
  
`<lookup>`, bir akış kimliğini (`list` / `show` tarafından döndürülür) veya akışın sahip anahtarını (sahip olan alt sistemin akışı izlemek için kullandığı kararlı tanımlayıcı) kabul eder.

### Durum filtresi değerleri

`list` üzerindeki `--status` şunlardan birini kabul eder:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Örnekler

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Tam TaskFlow kavramları ve yazımı için bkz. [TaskFlow](</tr/automation/taskflow>). Üst `tasks` komutu için bkz. [tasks CLI başvurusu](</tr/cli/tasks>).

## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Otomasyon](</tr/automation>)
  * [TaskFlow](</tr/automation/taskflow>)


Was this useful?YesNo