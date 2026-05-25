---
title: Taslakları ilerlet
source_url: https://docs.openclaw.ai/tr/concepts/progress-drafts
scraped_at: 2026-05-25
---

İlerleme taslakları, uzun süren ajan turlarının sohbet içinde canlı hissettirmesini sağlar ve konuşmayı geçici durum yanıtları yığınına dönüştürmez.

İlerleme taslakları etkinleştirildiğinde OpenClaw, yalnızca turun gerçek iş yaptığını kanıtlamasından sonra görünür bir devam eden çalışma mesajı oluşturur, ajan okurken, plan yaparken, araçları çağırırken veya onay beklerken bunu günceller ve ardından kanal bunu güvenli biçimde yapabiliyorsa bu taslağı nihai yanıta dönüştürür.

textCopy code
[code]
    Shelling...📖 from docs/concepts/progress-drafts.md🔎 Web Search: for "discord edit message"🛠️ Bash: run tests
[/code]

Araç ağırlıklı çalışma sırasında tek bir düzenli durum mesajı ve tur bittiğinde nihai yanıt istediğinizde ilerleme taslaklarını kullanın.

## Hızlı başlangıç

İlerleme taslaklarını kanal başına `streaming.mode: "progress"` ile etkinleştirin:

json5Copy code
[code]
    {  channels: {    discord: {      streaming: {        mode: "progress",      },    },  },}
[/code]

Bu genellikle yeterlidir. OpenClaw otomatik tek kelimelik bir etiket seçer, iş en az beş saniye sürdüğünde veya ikinci bir iş olayı yayımladığında beklemeyi bırakır, yararlı iş gerçekleşirken kompakt ilerleme satırları ekler ve o tur için yinelenen bağımsız ilerleme sohbetini bastırır.

## Kullanıcıların gördüğü

Bir ilerleme taslağının iki parçası vardır:

Bölüm | Amaç  
---|---  
Etiket | `Thinking...` veya `Shelling...` gibi kısa bir başlangıç/durum satırı.  
İlerleme satırları | Ayrıntılı çıktıyla aynı araç simgelerini ve ayrıntı biçimleyicisini kullanan kompakt çalışma güncellemeleri.  
  
Etiket, ajan anlamlı işe başladıktan ve beş saniye boyunca meşgul kaldıktan ya da ikinci bir iş olayı yayımladıktan sonra görünür. Dönen ilerleme satırı listesinin bir parçasıdır; bu nedenle yeterince somut iş göründüğünde başlangıç durumu yukarı kayar. Yalnızca düz metin yanıtları ilerleme taslağı göstermez. İlerleme satırları yalnızca ajan yararlı iş güncellemeleri yayımladığında eklenir; örneğin `🛠️ Bash: run tests`, `🔎 Web Search: for "discord edit message"` veya `✍️ Write: to /tmp/file`. Varsayılan olarak `/verbose` ile aynı kompakt açıklama modunu kullanırlar; hata ayıklarken ham komutların/ayrıntıların da eklenmesini istiyorsanız `agents.defaults.toolProgressDetail: "raw"` ayarını yapın. Mümkün olduğunda nihai yanıt taslağın yerini alır; aksi halde OpenClaw nihai yanıtı normal şekilde gönderir ve kanalın taşıma mekanizmasına göre taslağı temizler veya güncellemeyi durdurur.

## Bir mod seçin

`channels.<channel>.streaming.mode` görünür devam eden çalışma davranışını denetler:

Mod | En uygun kullanım | Sohbette görünenler  
---|---|---  
`off` | Sessiz kanallar | Yalnızca nihai yanıt.  
`partial` | Yanıt metninin görünmesini izleme | En son yanıt metniyle düzenlenen tek taslak.  
`block` | Daha büyük yanıt önizleme parçaları | Daha büyük parçalar halinde güncellenen veya eklenen tek önizleme.  
`progress` | Araç ağırlıklı veya uzun süren turlar | Tek durum taslağı, ardından nihai yanıt.  
  
Kullanıcılar yanıt metninin token token akmasını izlemekten çok "ne oluyor" sorusunu önemsediğinde `progress` seçin.

Yanıtın kendisi ilerleme sinyali olduğunda `partial` seçin.

Daha büyük metin parçalarında taslak önizleme güncellemeleri istediğinizde `block` seçin. Discord ve Telegram üzerinde `streaming.mode: "block"` hâlâ önizleme akışıdır, normal blok teslimi değildir. Normal blok yanıtları istediğinizde `streaming.block.enabled` veya eski `blockStreaming` kullanın.

## Etiketleri yapılandırın

İlerleme etiketleri `channels.<channel>.streaming.progress` altında bulunur.

Varsayılan etiket `auto` değeridir; bu, OpenClaw'ın yerleşik üç noktalı tek kelimelik etiket havuzundan seçim yapar:

textCopy code
[code]
    Thinking...Shelling...Scuttling...Clawing...Pinching...Molting...Bubbling...Tiding...Reefing...Cracking...Sifting...Brining...Nautiling...Krilling...Barnacling...Lobstering...Tidepooling...Pearling...Snapping...Surfacing...
[/code]

Sabit bir etiket kullanın:

json5Copy code
[code]
    {  channels: {    discord: {      streaming: {        mode: "progress",        progress: {          label: "Investigating",        },      },    },  },}
[/code]

Kendi otomatik etiket havuzunuzu kullanın:

json5Copy code
[code]
    {  channels: {    discord: {      streaming: {        mode: "progress",        progress: {          label: "auto",          labels: ["Checking", "Reading", "Testing", "Finishing"],        },      },    },  },}
[/code]

Etiketi gizleyip yalnızca ilerleme satırlarını gösterin:

json5Copy code
[code]
    {  channels: {    discord: {      streaming: {        mode: "progress",        progress: {          label: false,        },      },    },  },}
[/code]

## İlerleme satırlarını denetleyin

İlerleme modunda ilerleme satırları varsayılan olarak etkindir. Bunlar gerçek çalışma olaylarından gelir: araç başlangıçları, öğe güncellemeleri, görev planları, onaylar, komut çıktısı, yama özetleri ve benzer ajan etkinlikleri.

OpenClaw, ilerleme taslakları ve `/verbose` için aynı biçimleyiciyi kullanır:

json5Copy code
[code]
    {  agents: {    defaults: {      toolProgressDetail: "explain", // explain | raw    },  },}
[/code]

`"explain"` varsayılandır ve taslakları `🛠️ check JS syntax for /tmp/app.js` gibi kısa etiketlerle kararlı tutar. `"raw"` mevcut olduğunda alttaki komutu/ayrıntıyı ekler; bu hata ayıklarken yararlıdır ancak sohbette daha gürültülüdür.

Örneğin aynı komut, ayrıntı moduna bağlı olarak farklı görünür:

Mod | İlerleme satırı  
---|---  
`explain` | `🛠️ check JS syntax for /tmp/app.js`  
`raw` | `🛠️ check JS syntax for /tmp/app.js, node --check /tmp/app.js`  
  
Kaç satırın görünür kalacağını sınırlayın:

json5Copy code
[code]
    {  channels: {    discord: {      streaming: {        mode: "progress",        progress: {          maxLines: 4,        },      },    },  },}
[/code]

Taslak düzenlenirken sohbet balonu yeniden akışını azaltmak için ilerleme satırları otomatik olarak sıkıştırılır.

OpenClaw, yinelenen taslak düzenlemelerinin her güncellemede farklı biçimde satır kaydırmaması için uzun ilerleme satırlarını varsayılan olarak kısaltır. Ön ek okunabilir kalır ve yollar veya ham komutlar gibi uzun ayrıntılar üç noktayla kısaltılır.

Slack, ilerleme satırlarını tek bir metin gövdesi yerine yapılandırılmış Block Kit alanları olarak işleyebilir:

json5Copy code
[code]
    {  channels: {    slack: {      streaming: {        mode: "progress",        progress: {          render: "rich",        },      },    },  },}
[/code]

Zengin işleme aynı düz metin geri dönüşünü korur; böylece daha zengin yapıyı desteklemeyen kanallar ve istemciler yine de kompakt ilerleme metnini gösterebilir.

Tek ilerleme taslağını koruyup araç ve görev satırlarını gizleyin:

json5Copy code
[code]
    {  channels: {    discord: {      streaming: {        mode: "progress",        progress: {          toolProgress: false,        },      },    },  },}
[/code]

`toolProgress: false` ile OpenClaw, o tur için eski bağımsız araç ilerleme mesajlarını yine de bastırır. Yapılandırılmışsa etiket hariç, kanal nihai yanıta kadar görsel olarak sessiz kalır.

## Kanal davranışı

Her kanal desteklediği en temiz taşıma mekanizmasını kullanır:

Kanal | İlerleme taşıması | Notlar  
---|---|---  
Discord | Tek mesaj gönder, sonra düzenle. | Sığdığı zaman nihai metin tek güvenli önizleme mesajında yerinde düzenlenir.  
Matrix | Tek olay gönder, sonra düzenle. | Hesap düzeyi akış yapılandırması hesap düzeyi taslakları denetler.  
Microsoft Teams | Kişisel sohbetlerde yerel Teams akışı. | `streaming.mode: "block"` Teams blok teslimine eşlenir.  
Slack | Yerel akış veya düzenlenebilir taslak gönderisi. | İş parçacığı kullanılabilirliği, yerel akışın kullanılıp kullanılamayacağını etkiler.  
Telegram | Tek mesaj gönder, sonra düzenle. | Eski görünür taslaklar, nihai zaman damgalarının yararlı kalması için değiştirilebilir.  
Mattermost | Düzenlenebilir taslak gönderisi. | Araç etkinliği aynı taslak tarzı gönderiye katlanır.  
  
Güvenli düzenleme desteği olmayan kanallar genellikle yazıyor göstergelerine veya yalnızca nihai teslimata geri döner.

## Sonlandırma

Nihai yanıt hazır olduğunda OpenClaw sohbeti temiz tutmaya çalışır:

  * Taslak güvenli biçimde nihai yanıta dönüşebiliyorsa OpenClaw onu yerinde düzenler.
  * Kanal yerel ilerleme akışı kullanıyorsa OpenClaw, yerel taşıma nihai metni kabul ettiğinde bu akışı sonlandırır.
  * Nihai yanıtta medya, onay istemi, açık bir yanıt hedefi, çok fazla parça veya başarısız düzenleme/gönderme varsa OpenClaw nihai yanıtı normal kanal teslim yolundan gönderir.


Geri dönüş yolu bilinçli bir tercihtir. Metni kaybetmekten, yanıtı yanlış iş parçacığına yerleştirmekten veya taslağı kanalın güvenli biçimde temsil edemeyeceği bir yükle ezmektense yeni bir nihai yanıt göndermek daha iyidir.

## Sorun giderme

**Yalnızca nihai yanıtı görüyorum.**

Mesajı işleyen hesap veya kanal için `channels.<channel>.streaming.mode` değerinin `progress` olarak ayarlandığını kontrol edin. Bazı grup veya alıntı-yanıt yolları, kanal doğru mesajı güvenli biçimde düzenleyemediğinde bir tur için taslak önizlemelerini devre dışı bırakabilir.

**Etiketi görüyorum ama araç satırlarını görmüyorum.**

`streaming.progress.toolProgress` ayarını kontrol edin. `false` ise OpenClaw tek taslak davranışını korur ancak araç ve görev ilerleme satırlarını gizler.

**Düzenlenmiş taslak yerine yeni bir nihai mesaj görüyorum.**

Bu bir güvenlik geri dönüşüdür. Medya yanıtları, uzun yanıtlar, açık yanıt hedefleri, eski Telegram taslakları, eksik Slack iş parçacığı hedefleri, silinmiş önizleme mesajları veya başarısız yerel akış sonlandırması için gerçekleşebilir.

**Hâlâ bağımsız ilerleme mesajları görüyorum.**

İlerleme modu, bir taslak etkin olduğunda varsayılan bağımsız araç ilerleme mesajlarını bastırır. Bağımsız mesajlar hâlâ görünüyorsa turun gerçekten ilerleme modunu kullandığını ve `streaming.mode: "off"` ya da o mesaj için taslak oluşturamayan bir kanal yolu kullanmadığını doğrulayın.

**Teams, Discord veya Telegram'dan farklı davranıyor.**

Microsoft Teams, kişisel sohbetlerde genel gönder-ve-düzenle önizleme taşıması yerine yerel akış kullanır. Teams ayrıca `streaming.mode: "block"` değerini Teams blok teslimi olarak ele alır; çünkü Discord ve Telegram tarafından kullanılan aynı taslak önizleme blok moduna sahip değildir.

## İlgili

  * [Akış ve parçalara ayırma](</tr/concepts/streaming>)
  * [Mesajlar](</tr/concepts/messages>)
  * [Kanal yapılandırması](</tr/gateway/config-channels>)
  * [Discord](</tr/channels/discord>)
  * [Matrix](</tr/channels/matrix>)
  * [Microsoft Teams](</tr/channels/msteams>)
  * [Slack](</tr/channels/slack>)
  * [Telegram](</tr/channels/telegram>)


Was this useful?YesNo