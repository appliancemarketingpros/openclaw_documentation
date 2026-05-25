---
title: Aracı gönderimi
source_url: https://docs.openclaw.ai/tr/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent`, gelen bir sohbet mesajına gerek olmadan komut satırından tek bir agent turu çalıştırır. Betikli iş akışları, test etme ve programatik teslimat için kullanın.

## Hızlı başlangıç

* ### Run a simple agent turn

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Bu, mesajı Gateway üzerinden gönderir ve yanıtı yazdırır.

* ### Target a specific agent or session

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Deliver the reply to a channel

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Bayraklar

Bayrak | Açıklama  
---|---  
`--message \<text\>` | Gönderilecek mesaj (zorunlu)  
`--to \<dest\>` | Bir hedeften oturum anahtarı türetir (telefon, sohbet kimliği)  
`--agent \<id\>` | Yapılandırılmış bir agent’ı hedefler (`main` oturumunu kullanır)  
`--session-id \<id\>` | Mevcut bir oturumu kimliğine göre yeniden kullanır  
`--local` | Yerel gömülü çalışma zamanını zorlar (Gateway’i atlar)  
`--deliver` | Yanıtı bir sohbet kanalına gönderir  
`--channel \<name\>` | Teslimat kanalı (whatsapp, telegram, discord, slack vb.)  
`--reply-to \<target\>` | Teslimat hedefi geçersiz kılma  
`--reply-channel \<name\>` | Teslimat kanalı geçersiz kılma  
`--reply-account \<id\>` | Teslimat hesabı kimliği geçersiz kılma  
`--thinking \<level\>` | Seçili model profili için düşünme düzeyini ayarlar  
`--verbose \<on|full|off\>` | Ayrıntı düzeyini ayarlar  
`--timeout \<seconds\>` | Agent zaman aşımını geçersiz kılar  
`--json` | Yapılandırılmış JSON çıktısı verir  
  
## Davranış

  * Varsayılan olarak CLI **Gateway üzerinden** gider. Geçerli makinede gömülü çalışma zamanını zorlamak için `--local` ekleyin.
  * Gateway’e ulaşılamazsa CLI yerel gömülü çalıştırmaya **geri döner**.
  * Oturum seçimi: `--to` oturum anahtarını türetir (grup/kanal hedefleri yalıtımı korur; doğrudan sohbetler `main` altında birleşir).
  * Düşünme ve ayrıntı bayrakları oturum deposunda kalıcı olur.
  * Çıktı: varsayılan olarak düz metin ya da yapılandırılmış yük + meta veriler için `--json`.
  * `--json --deliver` ile JSON; gönderilen, bastırılan, kısmi ve başarısız gönderimler için teslimat durumunu içerir. Bkz. [JSON teslimat durumu](</tr/cli/agent#json-delivery-status>).


## Örnekler

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## İlgili

[**Agent CLI reference** Tam `openclaw agent` bayrak ve seçenek başvurusu. ](</tr/cli/agent>) [**Sub-agents** Arka plan alt agent oluşturma. ](</tr/tools/subagents>) [**Sessions** Oturum anahtarlarının nasıl çalıştığı ve `--to`, `--agent` ile `--session-id` değerlerinin bunları nasıl çözdüğü. ](</tr/concepts/session>) [**Slash commands** Agent oturumlarında kullanılan yerel komut kataloğu. ](</tr/tools/slash-commands>)

Was this useful?YesNo