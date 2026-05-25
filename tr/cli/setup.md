---
title: Kurulum
source_url: https://docs.openclaw.ai/tr/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Temel yapılandırmayı ve ajan çalışma alanını başlatın. Herhangi bir başlangıç bayrağı mevcutsa sihirbazı da çalıştırır.

## Seçenekler

Bayrak | Açıklama  
---|---  
`--workspace <dir>` | Ajan çalışma alanı dizini (varsayılan `~/.openclaw/workspace`; `agents.defaults.workspace` olarak saklanır).  
`--wizard` | Etkileşimli başlangıcı çalıştır.  
`--non-interactive` | Başlangıcı istemler olmadan çalıştır.  
`--mode <mode>` | Başlangıç modu: `local` veya `remote`.  
`--import-from <provider>` | Başlangıç sırasında çalıştırılacak geçiş sağlayıcısı.  
`--import-source <path>` | `--import-from` için kaynak ajan ana dizini.  
`--import-secrets` | Başlangıç geçişi sırasında desteklenen gizli bilgileri içe aktar.  
`--remote-url <url>` | Uzak Gateway WebSocket URL'si.  
`--remote-token <token>` | Uzak Gateway token'ı (isteğe bağlı).  
  
### Sihirbaz otomatik tetikleyicisi

`openclaw setup`, `--wizard` olmadan bile bu bayraklardan herhangi biri açıkça mevcut olduğunda sihirbazı çalıştırır:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Örnekler

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Notlar

  * Düz `openclaw setup`, tam başlangıç akışını çalıştırmadan yapılandırmayı ve çalışma alanını başlatır.
  * Düz kurulumdan sonra, tam kılavuzlu yolculuk için `openclaw onboard`, hedefli değişiklikler için `openclaw configure` veya kanal hesapları eklemek için `openclaw channels add` çalıştırın.
  * Hermes durumu algılanırsa etkileşimli başlangıç otomatik olarak geçiş önerebilir. İçe aktarmalı başlangıç yeni bir kurulum gerektirir; başlangıç dışında kuru çalıştırma planları, yedekler ve üzerine yazma modu için [Geçiş](</tr/cli/migrate>) kullanın.


## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Başlangıç (CLI)](</tr/start/wizard>)
  * [Başlarken](</tr/start/getting-started>)
  * [Kuruluma genel bakış](</tr/install>)


Was this useful?YesNo