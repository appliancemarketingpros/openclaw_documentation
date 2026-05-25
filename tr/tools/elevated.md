---
title: Yükseltilmiş mod
source_url: https://docs.openclaw.ai/tr/tools/elevated
scraped_at: 2026-05-25
---

Bir ajan sandbox içinde çalıştığında, `exec` komutları sandbox ortamıyla sınırlanır. **Yükseltilmiş mod** , ajanın bunun yerine sandbox dışına çıkıp komutları sandbox dışında çalıştırmasına olanak tanır; yapılandırılabilir onay kapılarıyla birlikte.

## Yönergeler

Yükseltilmiş modu oturum başına eğik çizgi komutlarıyla denetleyin:

Yönerge | Ne yapar  
---|---  
`/elevated on` | Yapılandırılmış ana makine yolunda sandbox dışında çalıştırır, onayları korur  
`/elevated ask` | `on` ile aynı (takma ad)  
`/elevated full` | Yapılandırılmış ana makine yolunda sandbox dışında çalıştırır ve onayları atlar  
`/elevated off` | Sandbox ile sınırlı yürütmeye geri döner  
  
Ayrıca `/elev on|off|ask|full` olarak da kullanılabilir.

Geçerli düzeyi görmek için argümansız `/elevated` gönderin.

## Nasıl çalışır?

* ### Kullanılabilirliği denetle

Elevated yapılandırmada etkinleştirilmiş olmalı ve gönderen izin listesinde olmalıdır:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Düzeyi ayarla

Oturum varsayılanını ayarlamak için yalnızca yönerge içeren bir mesaj gönderin:

CodeCopy code
[code]
    /elevated full
[/code]

Veya satır içinde kullanın (yalnızca o mesaja uygulanır):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Komutlar sandbox dışında çalışır

Elevated etkinken, `exec` çağrıları sandbox dışına çıkar. Etkin ana makine varsayılan olarak `gateway` olur; yapılandırılmış/oturum exec hedefi `node` olduğunda ise `node` olur. `full` modunda exec onayları atlanır. `on`/`ask` modunda yapılandırılmış onay kuralları uygulanmaya devam eder.

## Çözümleme sırası

  1. Mesajdaki **satır içi yönerge** (yalnızca o mesaja uygulanır)
  2. **Oturum geçersiz kılması** (yalnızca yönerge içeren bir mesaj gönderilerek ayarlanır)
  3. **Genel varsayılan** (yapılandırmada `agents.defaults.elevatedDefault`)


## Kullanılabilirlik ve izin listeleri

  * **Genel kapı** : `tools.elevated.enabled` (`true` olmalıdır)
  * **Gönderen izin listesi** : kanal başına listelerle `tools.elevated.allowFrom`
  * **Ajan başına kapı** : `agents.list[].tools.elevated.enabled` (yalnızca daha fazla kısıtlayabilir)
  * **Ajan başına izin listesi** : `agents.list[].tools.elevated.allowFrom` (gönderen hem genel hem ajan başına kuralla eşleşmelidir)
  * **Discord geri dönüşü** : `tools.elevated.allowFrom.discord` atlanırsa, geri dönüş olarak `channels.discord.allowFrom` kullanılır
  * **Tüm kapılar geçmelidir** ; aksi takdirde elevated kullanılamaz kabul edilir


İzin listesi girdi biçimleri:

Önek | Eşleştiği değer  
---|---  
(yok) | Gönderen kimliği, E.164 veya From alanı  
`name:` | Gönderen görünen adı  
`username:` | Gönderen kullanıcı adı  
`tag:` | Gönderen etiketi  
`id:`, `from:`, `e164:` | Açık kimlik hedefleme  
  
## Elevated neyi denetlemez?

  * **Araç ilkesi** : `exec` araç ilkesi tarafından reddedilirse, elevated bunu geçersiz kılamaz.
  * **Ana makine seçimi ilkesi** : elevated, `auto` değerini serbest bir ana makineler arası geçersiz kılmaya dönüştürmez. Yapılandırılmış/oturum exec hedef kurallarını kullanır ve yalnızca hedef zaten `node` olduğunda `node` seçer.
  * **`/exec` öğesinden ayrıdır**: `/exec` yönergesi, yetkili gönderenler için oturum başına exec varsayılanlarını ayarlar ve yükseltilmiş mod gerektirmez.


## İlgili

[**Exec aracı** Ajandan kabuk komutu yürütme. ](</tr/tools/exec>) [**Exec onayları** `exec` için onay ve izin listesi sistemi. ](</tr/tools/exec-approvals>) [**Sandboxing** Gateway düzeyinde sandbox yapılandırması. ](</tr/gateway/sandboxing>) [**Sandbox ve Araç İlkesi ve Elevated** Bir araç çağrısı sırasında üç kapının nasıl birleştiği. ](</tr/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo