---
title: SMS
source_url: https://docs.openclaw.ai/tr/channels/sms
scraped_at: 2026-06-29
---

Get started

OpenClaw, bir Twilio telefon numarası veya Messaging Service üzerinden SMS alıp gönderebilir. Gateway, gelen Webhook rotasını kaydeder, varsayılan olarak Twilio istek imzalarını doğrular ve yanıtları Twilio'nun Messages API'si üzerinden geri gönderir.

[**Pairing** SMS için varsayılan DM ilkesi eşleştirmedir. ](</tr/channels/pairing>) [**Gateway security** Webhook erişimini ve gönderici erişim kontrollerini gözden geçirin. ](</tr/gateway/security>) [**Channel troubleshooting** Kanallar arası tanılama ve onarım çalışma kitapları. ](</tr/channels/troubleshooting>)

## Başlamadan önce

Şunlara ihtiyacınız var:

  * Resmi SMS Plugin'i `openclaw plugins install @openclaw/sms` ile yüklenmiş olmalıdır.
  * SMS özellikli telefon numarasına sahip bir Twilio hesabı veya Twilio Messaging Service.
  * Twilio Account SID ve Auth Token.
  * OpenClaw Gateway'inize ulaşan herkese açık bir HTTPS URL'si.
  * Bir gönderici ilkesi seçimi: özel kullanım için `pairing`, önceden onaylanmış telefon numaraları için `allowlist` veya yalnızca kasıtlı olarak herkese açık SMS erişimi için `open`.


Numara her iki yeteneğe de sahipse SMS ve Voice Call için aynı Twilio numarasını kullanın. SMS Webhook'unu ve Voice Webhook'unu Twilio'da ayrı ayrı yapılandırın; bu sayfa yalnızca SMS Webhook'unu kapsar.

## Hızlı Kurulum

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/sms
[/code]

* ### Create or choose a Twilio sender

Twilio'da **Phone Numbers > Manage > Active numbers** bölümünü açın ve SMS özellikli bir numara seçin. Şunları kaydedin:

  * Account SID, örneğin `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
  * Auth Token
  * Gönderici telefon numarası, örneğin `+15551234567`


Sabit bir gönderici numarası yerine Messaging Service kullanıyorsanız Messaging Service SID'yi kaydedin, örneğin `MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

* ### Configure the SMS channel

Bunu `sms.patch.json5` olarak kaydedin ve yer tutucuları değiştirin:

json5Copy code
[code]
    {channels: {sms: {  enabled: true,  accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  authToken: "twilio-auth-token",  fromNumber: "+15551234567",  publicWebhookUrl: "https://gateway.example.com/webhooks/sms",  dmPolicy: "pairing",},},}
[/code]

Uygulayın:

bashCopy code
[code]
    openclaw config patch --file ./sms.patch.json5 --dry-runopenclaw config patch --file ./sms.patch.json5
[/code]

* ### Point Twilio at the Gateway webhook

Twilio telefon numarası ayarlarında **Messaging** bölümünü açın ve **A message comes in** değerini şuna ayarlayın:

textCopy code
[code]
    https://gateway.example.com/webhooks/sms
[/code]

HTTP `POST` kullanın. Varsayılan yerel yol `/webhooks/sms` olur; farklı bir rotaya ihtiyacınız varsa `channels.sms.webhookPath` değerini değiştirin.

* ### Expose the exact SMS webhook path

Herkese açık URL'niz SMS yolunu Gateway sürecine yönlendirmelidir. Yerel test için Tailscale Funnel kullanıyorsanız `/webhooks/sms` yolunu açıkça dışa açın:

bashCopy code
[code]
    tailscale funnel --bg --set-path /webhooks/sms http://127.0.0.1:<gateway-port>/webhooks/smstailscale funnel status
[/code]

Voice Call ve SMS ayrı Webhook yolları kullanır. Aynı Twilio numarası her ikisini de işliyorsa her iki rotayı da Twilio'da ve tünelinizde yapılandırılmış tutun.

* ### Start the Gateway and approve first sender

bashCopy code
[code]
    openclaw gateway
[/code]

Twilio numarasına bir kısa mesaj gönderin. İlk mesaj bir eşleştirme isteği oluşturur. Onaylayın:

bashCopy code
[code]
    openclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;
[/code]

Eşleştirme kodlarının süresi 1 saat sonra dolar.

## Yapılandırma Örnekleri

### Yapılandırma dosyası

Kanal tanımının Gateway yapılandırmasıyla birlikte taşınmasını istediğinizde yapılandırma dosyası kurulumunu kullanın:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

### Ortam değişkenleri

Gizli değerlerin ana makine ortamından geldiği tek hesaplı dağıtımlar için ortam kurulumunu kullanın:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"export TWILIO_AUTH_TOKEN="<twilio-auth-token>"export TWILIO_PHONE_NUMBER="+15551234567"export SMS_PUBLIC_WEBHOOK_URL="https://gateway.example.com/webhooks/sms"
[/code]

Ardından kanalı yapılandırmada etkinleştirin:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

`TWILIO_SMS_FROM`, `TWILIO_PHONE_NUMBER` için bir diğer ad olarak kabul edilir. Twilio'nun göndericiyi Messaging Service'ten seçmesi gerektiğinde telefon numarası göndericisi yerine `TWILIO_MESSAGING_SERVICE_SID` kullanın.

### SecretRef kimlik doğrulama belirteci

`authToken` bir SecretRef olabilir. Gateway'in Twilio Auth Token'ı düz metin yapılandırma olarak depolamak yerine OpenClaw gizli değerler çalışma zamanından çözmesi gerektiğinde bunu kullanın:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: { source: "env", provider: "default", id: "TWILIO_AUTH_TOKEN" },      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Başvurulan ortam değişkeni veya gizli değer sağlayıcısı Gateway çalışma zamanı tarafından görülebilir olmalıdır. Ana makine ortam değişkenlerini değiştirdikten sonra yönetilen Gateway süreçlerini yeniden başlatın.

### Yalnızca izin listesine açık özel numara

Yalnızca bilinen telefon numaralarının ajanla konuşabilmesi gerektiğinde `allowlist` kullanın:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "allowlist",      allowFrom: ["+15557654321"],    },  },}
[/code]

### Messaging Service göndericisi

Twilio'nun göndericiyi Messaging Service üzerinden seçmesi gerektiğinde `fromNumber` yerine `messagingServiceSid` kullanın:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      messagingServiceSid: "MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Yapılandırma ve ortam çözümlemesinden sonra hem `fromNumber` hem de `messagingServiceSid` varsa `fromNumber` kullanılır.

### Varsayılan giden hedef

Otomasyon veya ajan tarafından başlatılan teslimat, gönderim akışı açık bir hedefi atladığında varsayılan bir hedefe sahip olmalıysa `defaultTo` ayarlayın:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      defaultTo: "+15557654321",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",    },  },}
[/code]

## Erişim kontrolü

`channels.sms.dmPolicy` doğrudan SMS erişimini kontrol eder:

  * `pairing` (varsayılan)
  * `allowlist` (`allowFrom` içinde en az bir gönderici gerektirir)
  * `open` (`allowFrom` içinde `"*"` bulunmasını gerektirir)
  * `disabled`


`allowFrom` girdileri `+15551234567` gibi E.164 telefon numaraları olmalıdır. `sms:` önekleri kabul edilir ve normalleştirilir. Özel bir asistan için açık telefon numaralarıyla birlikte `dmPolicy: "allowlist"` tercih edin.

## SMS gönderme

Giden SMS hedefleri, SMS kanalı seçili olarak `sms:` hizmet önekini kullanır:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15551234567 --message "hello"
[/code]

Kanal seçimi örtük olduğunda `twilio-sms:+15551234567`, iMessage tarafından kullanılan mevcut kanal sahipli `sms:` hizmet önekini devralmadan bu kanalı seçer.

bashCopy code
[code]
    openclaw message send --target twilio-sms:+15551234567 --message "hello"
[/code]

CLI açık bir `--target` gerektirir. `defaultTo`, hedefin kanal yapılandırmasından çözülebildiği otomasyon ve ajan tarafından başlatılan teslimat yolları içindir.

Gelen SMS konuşmalarından ajan yanıtları, yapılandırılmış Twilio göndericisi üzerinden otomatik olarak göndericiye geri gider.

SMS çıktısı düz metindir. OpenClaw markdown'ı kaldırır, çitli kod bloklarını düzleştirir, okunabilir bağlantıları korur ve uzun yanıtları Twilio üzerinden göndermeden önce parçalara böler.

## Kurulumu Doğrulama

Gateway başladıktan sonra:

  1. Gateway günlüğünün SMS Webhook rotasını gösterdiğini doğrulayın.
  2. Twilio tarafında bir yoklama çalıştırın:

bashCopy code
[code]
    openclaw channels capabilities --channel smsopenclaw channels status --channel sms --probe --json
[/code]

  3. Telefonunuzdan Twilio numarasına bir SMS gönderin.
  4. `openclaw pairing list sms` çalıştırın.
  5. Eşleştirme kodunu `openclaw pairing approve sms &lt;CODE&gt;` ile onaylayın.
  6. Başka bir SMS gönderin ve ajanın yanıtladığını doğrulayın.


Yalnızca giden test için şunu kullanın:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15557654321 --message "OpenClaw SMS test"
[/code]

### macOS iMessage/SMS'ten uçtan uca test

Messages üzerinden operatör SMS'i gönderebilen bir Mac'te, telefonunuza dokunmadan gönderici tarafını çalıştırmak için `imsg` kullanabilirsiniz:

bashCopy code
[code]
    imsg send --to "+15551234567" --service sms --text "OpenClaw SMS E2E $(date -u +%Y%m%dT%H%M%SZ)" --jsonopenclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;imsg send --to "+15551234567" --service sms --text "reply exactly SMS pong" --json
[/code]

İlk mesaj bir eşleştirme isteği oluşturmalıdır. İkinci mesaj ajan yanıtını Twilio üzerinden almalıdır.

## Webhook güvenliği

Varsayılan olarak OpenClaw, `publicWebhookUrl` ve `authToken` kullanarak `X-Twilio-Signature` doğrular. `publicWebhookUrl` değerini şema, ana makine, yol ve sorgu dizesi dahil olmak üzere Twilio'da yapılandırılan URL ile bayt bayt aynı tutun.

Yalnızca yerel tünel testi için şunu ayarlayabilirsiniz:

json5Copy code
[code]
    {  channels: {    sms: {      dangerouslyDisableSignatureValidation: true,    },  },}
[/code]

Herkese açık bir Gateway'de devre dışı imza doğrulaması kullanmayın.

## Çok hesaplı yapılandırma

Birden fazla Twilio numarası işletiyorsanız `accounts` kullanın:

json5Copy code
[code]
    {  channels: {    sms: {      accounts: {        support: {          enabled: true,          accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",          authToken: "twilio-auth-token",          fromNumber: "+15551234567",          publicWebhookUrl: "https://gateway.example.com/webhooks/sms/support",          webhookPath: "/webhooks/sms/support",          dmPolicy: "allowlist",          allowFrom: ["+15557654321"],        },      },    },  },}
[/code]

Her hesap ayrı bir `webhookPath` kullanmalıdır.

## Sorun giderme

### Twilio 403 döndürüyor veya OpenClaw Webhook'u reddediyor

`publicWebhookUrl` değerinin şema, ana makine, yol ve sorgu dizesi dahil olmak üzere Twilio'da yapılandırılan URL ile tam olarak eşleştiğini kontrol edin. Twilio herkese açık URL dizesini imzalar, bu nedenle proxy yeniden yazmaları ve alternatif ana makine adları imza doğrulamasını bozabilir.

### Eşleştirme isteği görünmüyor

Twilio numarasının **Messaging** Webhook URL'sini ve yöntemini kontrol edin. SMS Webhook URL'sini göstermeli ve `POST` kullanmalıdır. Ayrıca Gateway'in herkese açık internetten veya tüneliniz üzerinden erişilebilir olduğunu doğrulayın.

Twilio mesaj günlüğü `11200` hatasını gösteriyorsa Twilio gelen SMS'i kabul etmiş ancak Webhook'unuza ulaşamamıştır. Şunları kontrol edin:

  * Twilio **Messaging > A message comes in** `publicWebhookUrl` değerini gösteriyor.
  * Yöntem `POST`.
  * Tünel veya ters proxy tam `webhookPath` yolunu dışa açıyor; Tailscale Funnel için `tailscale funnel status` çalıştırın ve `/webhooks/sms` öğesinin listelendiğini doğrulayın.
  * `publicWebhookUrl`, Twilio'nun gönderdiği aynı şema, ana makine, yol ve sorgu dizesini kullanıyor; böylece imza doğrulaması imzalanmış URL'yi yeniden oluşturabilir.


### Giden gönderimler başarısız oluyor

`accountSid`, `authToken` ve `fromNumber` ya da `messagingServiceSid` değerlerinden birinin çözüldüğünü doğrulayın. Deneme Twilio hesabı kullanıyorsanız giden SMS gönderilebilmesi için hedef numaranın Twilio'da doğrulanması gerekebilir.

### Mesajlar geliyor ancak ajan yanıt vermiyor

`dmPolicy` ve `allowFrom` değerlerini kontrol edin. Varsayılan `pairing` ilkesiyle, normal agent turları işlenmeden önce gönderenin onaylanmış olması gerekir.

Was this useful?YesNo

Open issue