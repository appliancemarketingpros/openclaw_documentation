---
title: Sessiz önizlemeler için Matrix anlık bildirim kuralları
source_url: https://docs.openclaw.ai/tr/channels/matrix-push-rules
scraped_at: 2026-05-25
---

`channels.matrix.streaming` `"quiet"` olduğunda, OpenClaw tek bir önizleme olayını yerinde düzenler ve sonlandırılmış düzenlemeyi özel bir içerik bayrağıyla işaretler. Matrix istemcileri, son düzenleme için yalnızca kullanıcı başına bir push kuralı bu bayrakla eşleşirse bildirim gösterir. Bu sayfa, Matrix'i kendi barındıran ve bu kuralı her alıcı hesabı için yüklemek isteyen operatörler içindir.

Yalnızca standart Matrix bildirim davranışını istiyorsanız `streaming: "partial"` kullanın veya streaming'i kapalı bırakın. Bkz. [Matrix kanal kurulumu](</tr/channels/matrix#streaming-previews>).

## Önkoşullar

  * alıcı kullanıcı = bildirimi alması gereken kişi
  * bot kullanıcısı = yanıtı gönderen OpenClaw Matrix hesabı
  * aşağıdaki API çağrıları için alıcı kullanıcının erişim token'ını kullanın
  * push kuralındaki `sender` değerini bot kullanıcısının tam MXID'siyle eşleştirin
  * alıcı hesabında çalışan pusher'lar zaten bulunmalıdır — sessiz önizleme kuralları yalnızca normal Matrix push teslimatı sağlıklı olduğunda çalışır


## Adımlar

* ### Sessiz önizlemeleri yapılandırın

json5Copy code
[code]
    {channels: {matrix: {  streaming: "quiet",},},}
[/code]

* ### Alıcının erişim token'ını alın

Mümkünse mevcut bir istemci oturumu token'ını yeniden kullanın. Yeni bir tane oluşturmak için:

bashCopy code
[code]
    curl -sS -X POST \"https://matrix.example.org/_matrix/client/v3/login" \-H "Content-Type: application/json" \--data '{"type": "m.login.password","identifier": { "type": "m.id.user", "user": "@alice:example.org" },"password": "REDACTED"}'
[/code]

* ### Pusher'ların var olduğunu doğrulayın

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushers"
[/code]

Hiç pusher dönmezse, devam etmeden önce bu hesap için normal Matrix push teslimatını düzeltin.

* ### Override push kuralını yükleyin

OpenClaw, sonlandırılmış yalnızca metin önizleme düzenlemelerini `content["com.openclaw.finalized_preview"] = true` ile işaretler. Bu işaretleyiciyle birlikte gönderen olarak bot MXID'siyle eşleşen bir kural yükleyin:

bashCopy code
[code]
    curl -sS -X PUT \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname" \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \-H "Content-Type: application/json" \--data '{"conditions": [  { "kind": "event_match", "key": "type", "pattern": "m.room.message" },  {    "kind": "event_property_is",    "key": "content.m\\.relates_to.rel_type",    "value": "m.replace"  },  {    "kind": "event_property_is",    "key": "content.com\\.openclaw\\.finalized_preview",    "value": true  },  { "kind": "event_match", "key": "sender", "pattern": "@bot:example.org" }],"actions": [  "notify",  { "set_tweak": "sound", "value": "default" },  { "set_tweak": "highlight", "value": false }]}'
[/code]

Çalıştırmadan önce değiştirin:

  * `https://matrix.example.org`: homeserver temel URL'niz
  * `$USER_ACCESS_TOKEN`: alıcı kullanıcının erişim token'ı
  * `openclaw-finalized-preview-botname`: bot başına ve alıcı başına benzersiz bir kural kimliği (kalıp: `openclaw-finalized-preview-<botname>`)
  * `@bot:example.org`: alıcının değil, OpenClaw botunuzun MXID'si


* ### Doğrulayın

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname"
[/code]

Ardından streamed bir yanıtı test edin. Sessiz modda oda sessiz bir taslak önizleme gösterir ve blok ya da tur tamamlandığında bir kez bildirim gönderir.

Kuralı daha sonra kaldırmak için aynı kural URL'sine alıcının token'ıyla `DELETE` gönderin.

## Çoklu bot notları

Push kuralları `ruleId` ile anahtarlanır: aynı kimliğe yeniden `PUT` çalıştırmak tek bir kuralı günceller. Aynı alıcıya bildirim gönderen birden fazla OpenClaw botu için, her bot adına ayrı bir gönderen eşleşmesiyle bir kural oluşturun.

Yeni kullanıcı tanımlı `override` kuralları varsayılan bastırma kurallarının önüne eklenir, bu yüzden ek bir sıralama parametresine gerek yoktur. Kural yalnızca yerinde sonlandırılabilen yalnızca metin önizleme düzenlemelerini etkiler; medya geri dönüşleri ve bayat önizleme geri dönüşleri normal Matrix teslimatını kullanır.

## Homeserver notları

Synapse

Özel bir `homeserver.yaml` değişikliği gerekmez. Normal Matrix bildirimleri bu kullanıcıya zaten ulaşıyorsa, yukarıdaki alıcı token'ı + `pushrules` çağrısı ana kurulum adımıdır.

Synapse'i bir ters proxy veya worker'ların arkasında çalıştırıyorsanız, `/_matrix/client/.../pushrules/` yolunun Synapse'e doğru şekilde ulaştığından emin olun. Push teslimatı ana işlem veya `synapse.app.pusher` / yapılandırılmış pusher worker'ları tarafından işlenir — bunların sağlıklı olduğundan emin olun.

Kural, 2023'te Synapse'e eklenen `event_property_is` push kuralı koşulunu (MSC3758, push kuralı v1.10) kullanır. Daha eski Synapse sürümleri `PUT pushrules/...` çağrısını kabul eder ancak koşulla sessizce hiç eşleşmez — sonlandırılmış bir önizleme düzenlemesinde bildirim gelmezse Synapse'i yükseltin.

Tuwunel

Akış Synapse ile aynıdır; sonlandırılmış önizleme işaretleyicisi için Tuwunel'e özgü yapılandırma gerekmez.

Kullanıcı başka bir cihazda aktifken bildirimler kayboluyorsa, `suppress_push_when_active` seçeneğinin etkin olup olmadığını kontrol edin. Tuwunel bu seçeneği 1.4.2 sürümünde (Eylül 2025) ekledi ve bir cihaz aktifken diğer cihazlara gönderilen push'ları kasıtlı olarak bastırabilir.

## İlgili

  * [Matrix kanal kurulumu](</tr/channels/matrix>)
  * [Streaming kavramları](</tr/concepts/streaming>)


Was this useful?YesNo