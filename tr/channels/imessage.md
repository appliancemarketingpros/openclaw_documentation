---
title: iMessage
source_url: https://docs.openclaw.ai/tr/channels/imessage
scraped_at: 2026-05-25
---

Durum: yerel harici CLI entegrasyonu. Gateway `imsg rpc` sürecini başlatır ve stdio üzerinden JSON-RPC ile iletişim kurar (ayrı daemon/port yoktur). Gelişmiş eylemler `imsg launch` ve başarılı bir özel API yoklaması gerektirir.

**Özel API eylemleri** Yanıtlar, tapback'ler, efektler, ekler ve grup yönetimi. [**Eşleştirme** iMessage DM'leri varsayılan olarak eşleştirme modunu kullanır. ](</tr/channels/pairing>) **Uzak Mac** Gateway Messages Mac üzerinde çalışmıyorsa bir SSH sarmalayıcısı kullanın. [**Yapılandırma başvurusu** Tam iMessage alan başvurusu. ](</tr/gateway/config-channels#imessage>)

## Hızlı kurulum

### Yerel Mac (hızlı yol)

* ### imsg kurun ve doğrulayın

bashCopy code
[code]
    brew install steipete/tap/imsgimsg rpc --helpimsg launchopenclaw channels status --probe
[/code]

* ### OpenClaw'ı yapılandırın

json5Copy code
[code]
    {channels: {imessage: {enabled: true,cliPath: "/usr/local/bin/imsg",dbPath: "/Users/user/Library/Messages/chat.db",},},}
[/code]

* ### Gateway'i başlatın

bashCopy code
[code]
    openclaw gateway
[/code]

* ### İlk DM eşleştirmesini onaylayın (varsayılan dmPolicy)

bashCopy code
[code]
    openclaw pairing list imessageopenclaw pairing approve imessage &lt;CODE&gt;
[/code]

Eşleştirme istekleri 1 saat sonra sona erer.

### SSH üzerinden uzak Mac

OpenClaw yalnızca stdio uyumlu bir `cliPath` gerektirir, bu yüzden `cliPath` değerini uzak bir Mac'e SSH yapan ve `imsg` çalıştıran bir sarmalayıcı betiğine yönlendirebilirsiniz.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T gateway-host imsg "$@"
[/code]

Ekler etkinleştirildiğinde önerilen yapılandırma:

json5Copy code
[code]
    {channels: {imessage: {  enabled: true,  cliPath: "~/.openclaw/scripts/imsg-ssh",  remoteHost: "user@gateway-host", // used for SCP attachment fetches  includeAttachments: true,  // Optional: override allowed attachment roots.  // Defaults include /Users/*/Library/Messages/Attachments  attachmentRoots: ["/Users/*/Library/Messages/Attachments"],  remoteAttachmentRoots: ["/Users/*/Library/Messages/Attachments"],},},}
[/code]

`remoteHost` ayarlanmadıysa, OpenClaw SSH sarmalayıcı betiğini ayrıştırarak bunu otomatik algılamaya çalışır. `remoteHost`, `host` veya `user@host` olmalıdır (boşluk veya SSH seçeneği yok). OpenClaw SCP için katı ana makine anahtarı denetimi kullanır; bu yüzden aktarma ana makinesi anahtarı `~/.ssh/known_hosts` içinde zaten bulunmalıdır. Ek yolları izin verilen köklere göre doğrulanır (`attachmentRoots` / `remoteAttachmentRoots`).

## Gereksinimler ve izinler (macOS)

  * `imsg` çalıştıran Mac üzerinde Messages oturumu açık olmalıdır.
  * OpenClaw/`imsg` çalıştıran süreç bağlamı için Full Disk Access gerekir (Messages DB erişimi).
  * Messages.app üzerinden ileti göndermek için Automation izni gerekir.
  * Gelişmiş eylemler (tepki / düzenleme / göndermeyi geri alma / iş parçacıklı yanıt / efektler / grup işlemleri) için System Integrity Protection devre dışı olmalıdır — aşağıdaki imsg özel API'sini etkinleştirme bölümüne bakın. Temel metin ve medya gönderme/alma onsuz çalışır.


## imsg özel API'sini etkinleştirme

`imsg` iki işletim moduyla gelir:

  * **Temel mod** (varsayılan, SIP değişikliği gerekmez): `send` üzerinden giden metin ve medya, gelen izleme/geçmiş, sohbet listesi. Yeni bir `brew install steipete/tap/imsg` ve yukarıdaki standart macOS izinleriyle kutudan çıktığı gibi elde ettiğiniz budur.
  * **Özel API modu** : `imsg`, dahili `IMCore` işlevlerini çağırmak için `Messages.app` içine bir yardımcı dylib enjekte eder. Bu, `react`, `edit`, `unsend`, `reply` (iş parçacıklı), `sendWithEffect`, `renameGroup`, `setGroupIcon`, `addParticipant`, `removeParticipant`, `leaveGroup` ve ayrıca yazıyor göstergeleri ile okundu bilgilerini açar.


Bu kanal sayfasının belgelediği gelişmiş eylem yüzeyine ulaşmak için Özel API modu gerekir. `imsg` README gereksinim konusunda nettir:

> `read`, `typing`, `launch`, köprü destekli zengin gönderim, ileti mutasyonu ve sohbet yönetimi gibi gelişmiş özellikler isteğe bağlıdır. SIP'nin devre dışı olmasını ve `Messages.app` içine bir yardımcı dylib enjekte edilmesini gerektirirler. SIP etkinken `imsg launch` enjeksiyonu reddeder.

Yardımcı enjeksiyon tekniği, Messages özel API'lerine ulaşmak için `imsg`'nin kendi dylib'ini kullanır. OpenClaw iMessage yolunda üçüncü taraf sunucu veya BlueBubbles runtime yoktur.

### Kurulum

  1. Messages.app çalıştıran Mac üzerinde **`imsg` kurun (veya yükseltin)**:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg status --json
[/code]

`imsg status --json` çıktısı `bridge_version`, `rpc_methods` ve yöntem başına `selectors` bildirir; böylece başlamadan önce geçerli derlemenin neyi desteklediğini görebilirsiniz.

  2. **System Integrity Protection'ı devre dışı bırakın.** Bu macOS sürümüne özeldir, çünkü alttaki Apple gereksinimi işletim sistemine ve donanıma bağlıdır:

     * **macOS 10.13-10.15 (Sierra-Catalina):** Terminal üzerinden Library Validation'ı devre dışı bırakın, Recovery Mode'a yeniden başlatın, `csrutil disable` çalıştırın, yeniden başlatın.
     * **macOS 11+ (Big Sur ve sonrası), Intel:** Recovery Mode (veya Internet Recovery), `csrutil disable`, yeniden başlatın.
     * **macOS 11+, Apple Silicon:** Recovery'ye girmek için güç düğmesi başlangıç dizisi; son macOS sürümlerinde Continue'a tıklarken **Left Shift** tuşunu basılı tutun, ardından `csrutil disable`. Sanal makine kurulumları ayrı bir akış izler — önce bir VM anlık görüntüsü alın.
     * **macOS 26 / Tahoe:** library-validation ilkeleri ve `imagent` özel yetki denetimleri daha da sıkılaştı; `imsg` güncel kalmak için güncellenmiş bir derleme gerektirebilir. Büyük bir macOS yükseltmesinden sonra `imsg launch` enjeksiyonu veya belirli `selectors` false döndürmeye başlarsa, SIP adımının başarılı olduğunu varsaymadan önce `imsg` sürüm notlarını kontrol edin.

`imsg launch` çalıştırmadan önce SIP'yi devre dışı bırakmak için Mac'inize yönelik Apple Recovery-mode akışını izleyin.

  3. **Yardımcıyı enjekte edin.** SIP devre dışıyken ve Messages.app oturumu açıkken:

bashCopy code
[code]imsg launch
[/code]

SIP hâlâ etkinken `imsg launch` enjeksiyonu reddeder; bu yüzden bu, 2. adımın uygulandığına dair bir onay işlevi de görür.

  4. **Köprüyü OpenClaw'dan doğrulayın:**

bashCopy code
[code]openclaw channels status --probe
[/code]

iMessage girdisi `works` bildirmelidir ve `imsg status --json | jq '.selectors'` çıktısı `retractMessagePart: true` ile macOS derlemenizin sunduğu düzenleme / yazıyor / okundu seçicilerini göstermelidir. `actions.ts` içindeki OpenClaw Plugin yöntem başına kapılama yalnızca alttaki seçicisi `true` olan eylemleri duyurur; bu yüzden aracın araç listesinde gördüğünüz eylem yüzeyi, köprünün bu ana makinede gerçekten yapabildiklerini yansıtır.


`openclaw channels status --probe` kanalı `works` olarak bildiriyor ancak belirli eylemler gönderim sırasında "iMessage `<action>` requires the imsg private API bridge" hatası atıyorsa, `imsg launch` komutunu yeniden çalıştırın — yardımcı devreden çıkabilir (Messages.app yeniden başlatma, işletim sistemi güncellemesi vb.) ve önbelleğe alınmış `available: true` durumu, bir sonraki yoklama yenileyene kadar eylemleri duyurmaya devam eder.

### SIP'yi devre dışı bırakamadığınızda

SIP'nin devre dışı olması tehdit modeliniz için kabul edilebilir değilse:

  * `imsg` temel moda geri döner — yalnızca metin + medya + alma.
  * OpenClaw Plugin metin/medya gönderimini ve gelen izlemeyi hâlâ duyurur; yalnızca `react`, `edit`, `unsend`, `reply`, `sendWithEffect` ve grup işlemlerini eylem yüzeyinden gizler (yöntem başına yetenek kapısına göre).
  * Birincil cihazlarınızda SIP'yi etkin tutarken, iMessage iş yükü için SIP kapalı ayrı bir Apple Silicon olmayan Mac (veya ayrılmış bot Mac) çalıştırabilirsiniz. Aşağıdaki Ayrılmış bot macOS kullanıcısı (ayrı iMessage kimliği) bölümüne bakın.


## Erişim denetimi ve yönlendirme

### DM ilkesi

`channels.imessage.dmPolicy` doğrudan iletileri denetler:

  * `pairing` (varsayılan)
  * `allowlist`
  * `open` (`allowFrom` içinde `"*"` bulunmasını gerektirir)
  * `disabled`


İzin listesi alanı: `channels.imessage.allowFrom`.

İzin listesi girdileri gönderenleri tanımlamalıdır: tanıtıcılar veya statik gönderen erişim grupları (`accessGroup:<name>`). `chat_id:*`, `chat_guid:*` veya `chat_identifier:*` gibi sohbet hedefleri için `channels.imessage.groupAllowFrom` kullanın; sayısal `chat_id` kayıt anahtarları için `channels.imessage.groups` kullanın.

### Grup ilkesi + bahsetmeler

`channels.imessage.groupPolicy` grup işlemeyi denetler:

  * `allowlist` (yapılandırıldığında varsayılan)
  * `open`
  * `disabled`


Grup gönderen izin listesi: `channels.imessage.groupAllowFrom`.

`groupAllowFrom` girdileri statik gönderen erişim gruplarına da başvurabilir (`accessGroup:<name>`).

Runtime yedeği: `groupAllowFrom` ayarlanmamışsa, iMessage grup gönderen denetimleri `allowFrom` kullanır; DM ve grup kabulü farklı olmalıysa `groupAllowFrom` ayarlayın. Runtime notu: `channels.imessage` tamamen eksikse, runtime `groupPolicy="allowlist"` değerine geri döner ve bir uyarı günlüğe yazar (`channels.defaults.groupPolicy` ayarlanmış olsa bile).

Gruplar için bahsetme kapılaması:

  * iMessage yerel bahsetme meta verisine sahip değildir
  * bahsetme algılama regex desenlerini kullanır (`agents.list[].groupChat.mentionPatterns`, geri dönüş `messages.groupChat.mentionPatterns`)
  * yapılandırılmış desen yoksa bahsetme kapılaması zorlanamaz


Yetkili göndericilerden gelen denetim komutları gruplarda bahsetme kapılamasını atlayabilir.

Grup başına `systemPrompt`:

`channels.imessage.groups.*` altındaki her girdi isteğe bağlı bir `systemPrompt` dizesi kabul eder. Değer, o gruptaki bir iletiyi işleyen her turda aracının sistem istemine enjekte edilir. Çözümleme, `channels.whatsapp.groups` tarafından kullanılan grup başına istem çözümlemesini yansıtır:

  1. **Gruba özel sistem istemi** (`groups["<chat_id>"].systemPrompt`): belirli grup girdisi eşlemde mevcut olduğunda **ve** `systemPrompt` anahtarı tanımlı olduğunda kullanılır. `systemPrompt` boş bir dizeyse (`""`) joker bastırılır ve o gruba hiçbir sistem istemi uygulanmaz.
  2. **Grup joker sistem istemi** (`groups["*"].systemPrompt`): belirli grup girdisi eşlemde tamamen yoksa veya mevcut olup `systemPrompt` anahtarı tanımlamıyorsa kullanılır.

json5Copy code
[code]
    {  channels: {    imessage: {      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { systemPrompt: "Use British spelling." },        "8421": {          requireMention: true,          systemPrompt: "This is the on-call rotation chat. Keep replies under 3 sentences.",        },        "9907": {          // explicit suppression: the wildcard "Use British spelling." does not apply here          systemPrompt: "",        },      },    },  },}
[/code]

Grup başına istemler yalnızca grup iletilerine uygulanır — bu kanaldaki doğrudan iletiler etkilenmez.

### Oturumlar ve deterministik yanıtlar

  * DM'ler doğrudan yönlendirme kullanır; gruplar grup yönlendirmesi kullanır.
  * Varsayılan `session.dmScope=main` ile iMessage DM'leri aracı ana oturumunda birleştirilir.
  * Grup oturumları yalıtılır (`agent:<agentId>:imessage:group:<chat_id>`).
  * Yanıtlar, kaynak kanal/hedef meta verileri kullanılarak iMessage'a geri yönlendirilir.


Grup benzeri ileti dizisi davranışı:

Bazı çok katılımcılı iMessage ileti dizileri `is_group=false` ile gelebilir. Bu `chat_id`, `channels.imessage.groups` altında açıkça yapılandırılmışsa OpenClaw bunu grup trafiği olarak ele alır (grup kapılaması + grup oturumu yalıtımı).

## ACP konuşma bağlamaları

Eski iMessage sohbetleri ACP oturumlarına da bağlanabilir.

Hızlı operatör akışı:

  * DM veya izin verilen grup sohbetinin içinde `/acp spawn codex --bind here` komutunu çalıştırın.
  * Aynı iMessage konuşmasındaki gelecekteki iletiler, oluşturulan ACP oturumuna yönlendirilir.
  * `/new` ve `/reset`, aynı bağlı ACP oturumunu yerinde sıfırlar.
  * `/acp close`, ACP oturumunu kapatır ve bağlamayı kaldırır.


Yapılandırılmış kalıcı bağlamalar, `type: "acp"` ve `match.channel: "imessage"` içeren üst düzey `bindings[]` girdileri aracılığıyla desteklenir.

`match.peer.id` şunları kullanabilir:

  * `+15555550123` veya `user@example.com` gibi normalize edilmiş DM tanıtıcısı
  * `chat_id:<id>` (kararlı grup bağlamaları için önerilir)
  * `chat_guid:<guid>`
  * `chat_identifier:<identifier>`


Örnek:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "codex",        runtime: {          type: "acp",          acp: { agent: "codex", backend: "acpx", mode: "persistent" },        },      },    ],  },  bindings: [    {      type: "acp",      agentId: "codex",      match: {        channel: "imessage",        accountId: "default",        peer: { kind: "group", id: "chat_id:123" },      },      acp: { label: "codex-group" },    },  ],}
[/code]

Paylaşılan ACP bağlama davranışı için [ACP Aracıları](</tr/tools/acp-agents>) bölümüne bakın.

## Dağıtım desenleri

Ayrılmış bot macOS kullanıcısı (ayrı iMessage kimliği)

Bot trafiğinin kişisel Messages profilinizden yalıtılması için ayrılmış bir Apple ID ve macOS kullanıcısı kullanın.

Tipik akış:

  1. Ayrılmış bir macOS kullanıcısı oluşturun/oturum açın.
  2. Bu kullanıcıda bot Apple ID'siyle Messages'da oturum açın.
  3. Bu kullanıcıya `imsg` kurun.
  4. OpenClaw'ın `imsg` komutunu bu kullanıcı bağlamında çalıştırabilmesi için SSH sarmalayıcısı oluşturun.
  5. `channels.imessage.accounts.<id>.cliPath` ve `.dbPath` değerlerini bu kullanıcı profiline yönlendirin.


İlk çalıştırma, bu bot kullanıcı oturumunda GUI onayları (Automation + Full Disk Access) gerektirebilir.

Tailscale üzerinden uzak Mac (örnek)

Yaygın topoloji:

  * Gateway Linux/VM üzerinde çalışır
  * iMessage + `imsg`, tailnet'inizdeki bir Mac üzerinde çalışır
  * `cliPath` sarmalayıcısı `imsg` çalıştırmak için SSH kullanır
  * `remoteHost`, SCP ek getirmelerini etkinleştirir


Örnek:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "~/.openclaw/scripts/imsg-ssh",      remoteHost: "bot@mac-mini.tailnet-1234.ts.net",      includeAttachments: true,      dbPath: "/Users/bot/Library/Messages/chat.db",    },  },}
[/code]

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T bot@mac-mini.tailnet-1234.ts.net imsg "$@"
[/code]

Hem SSH hem de SCP'nin etkileşimsiz olması için SSH anahtarları kullanın. `known_hosts` doldurulsun diye önce ana makine anahtarının güvenilir olduğundan emin olun (örneğin `ssh bot@mac-mini.tailnet-1234.ts.net`).

Çok hesaplı desen

iMessage, `channels.imessage.accounts` altında hesap başına yapılandırmayı destekler.

Her hesap `cliPath`, `dbPath`, `allowFrom`, `groupPolicy`, `mediaMaxMb`, geçmiş ayarları ve ek kök izin listeleri gibi alanları geçersiz kılabilir.

## Medya, parçalara ayırma ve teslim hedefleri

Ekler ve medya

  * gelen ek alımı **varsayılan olarak kapalıdır** — fotoğrafları, sesli notları, videoyu ve diğer ekleri aracıya iletmek için `channels.imessage.includeAttachments: true` ayarlayın. Bu devre dışıyken, yalnızca ek içeren iMessage iletileri aracıya ulaşmadan önce düşürülür ve hiç `Inbound message` günlük satırı üretmeyebilir.
  * `remoteHost` ayarlandığında uzak ek yolları SCP aracılığıyla getirilebilir
  * ek yolları izin verilen köklerle eşleşmelidir: 
    * `channels.imessage.attachmentRoots` (yerel)
    * `channels.imessage.remoteAttachmentRoots` (uzak SCP modu)
    * varsayılan kök deseni: `/Users/*/Library/Messages/Attachments`
  * SCP sıkı ana makine anahtarı denetimi kullanır (`StrictHostKeyChecking=yes`)
  * giden medya boyutu `channels.imessage.mediaMaxMb` kullanır (varsayılan 16 MB)

Giden parçalara ayırma

  * metin parça sınırı: `channels.imessage.textChunkLimit` (varsayılan 4000)
  * parça modu: `channels.imessage.chunkMode`
    * `length` (varsayılan)
    * `newline` (önce paragraf bölme)

Adresleme biçimleri

Tercih edilen açık hedefler:

  * `chat_id:123` (kararlı yönlendirme için önerilir)
  * `chat_guid:...`
  * `chat_identifier:...`


Tanıtıcı hedefleri de desteklenir:

  * `imessage:+1555...`
  * `sms:+1555...`
  * `user@example.com`

bashCopy code
[code]
    imsg chats --limit 20
[/code]

## Özel API eylemleri

`imsg launch` çalışırken ve `openclaw channels status --probe` `privateApi.available: true` bildirirken, ileti aracı normal metin gönderimlerine ek olarak iMessage yerel eylemlerini kullanabilir.

json5Copy code
[code]
    {  channels: {    imessage: {      actions: {        reactions: true,        edit: true,        unsend: true,        reply: true,        sendWithEffect: true,        sendAttachment: true,        renameGroup: true,        setGroupIcon: true,        addParticipant: true,        removeParticipant: true,        leaveGroup: true,      },    },  },}
[/code]

Kullanılabilir eylemler

  * **react** : iMessage tapback'lerini ekleyin/kaldırın (`messageId`, `emoji`, `remove`). Desteklenen tapback'ler sevgi, beğenme, beğenmeme, gülme, vurgulama ve soru anlamlarına eşlenir.
  * **reply** : Mevcut bir iletiye ileti dizili yanıt gönderin (`messageId`, `text` veya `message`, ayrıca `chatGuid`, `chatId`, `chatIdentifier` veya `to`).
  * **sendWithEffect** : Bir iMessage efektiyle metin gönderin (`text` veya `message`, `effect` veya `effectId`).
  * **edit** : Desteklenen macOS/özel API sürümlerinde gönderilmiş bir iletiyi düzenleyin (`messageId`, `text` veya `newText`).
  * **unsend** : Desteklenen macOS/özel API sürümlerinde gönderilmiş bir iletiyi geri çekin (`messageId`).
  * **upload-file** : Medya/dosya gönderin (`buffer` base64 olarak veya hidrasyon yapılmış `media`/`path`/`filePath`, `filename`, isteğe bağlı `asVoice`). Eski takma ad: `sendAttachment`.
  * **renameGroup** , **setGroupIcon** , **addParticipant** , **removeParticipant** , **leaveGroup** : Geçerli hedef bir grup konuşması olduğunda grup sohbetlerini yönetin.

İleti kimlikleri

Gelen iMessage bağlamı, kullanılabilir olduğunda hem kısa `MessageSid` değerlerini hem de tam ileti GUID'lerini içerir. Kısa kimlikler, son bellek içi yanıt önbelleğiyle sınırlıdır ve kullanılmadan önce geçerli sohbete göre denetlenir. Kısa kimliğin süresi dolmuşsa veya başka bir sohbete aitse tam `MessageSidFull` ile yeniden deneyin.

Yetenek algılama

OpenClaw, özel API eylemlerini yalnızca önbelleğe alınmış yoklama durumu köprünün kullanılamaz olduğunu söylediğinde gizler. Durum bilinmiyorsa eylemler görünür kalır ve gönderim yoklamaları tembel olarak yapar; böylece ilk eylem, ayrı bir manuel durum yenilemesi olmadan `imsg launch` sonrasında başarılı olabilir.

Okundu bilgileri ve yazıyor göstergesi

Özel API köprüsü çalışır durumdayken, kabul edilen gelen sohbetler gönderimden önce okundu olarak işaretlenir ve aracı üretirken göndericiye bir yazıyor balonu gösterilir. Okundu işaretlemeyi şununla devre dışı bırakın:

json5Copy code
[code]
    {  channels: {    imessage: {      sendReadReceipts: false,    },  },}
[/code]

Yöntem başına yetenek listesinden önceki eski `imsg` derlemeleri yazıyor/okundu işlevlerini sessizce kapılayacaktır; OpenClaw eksik okundu bilgisinin nedeni anlaşılabilsin diye yeniden başlatma başına tek seferlik bir uyarı günlüğe yazar.

Gelen tapback'ler

OpenClaw, iMessage tapback'lerine abone olur ve kabul edilen tepkileri normal ileti metni yerine sistem olayları olarak yönlendirir; böylece kullanıcı tapback'i sıradan bir yanıt döngüsünü tetiklemez.

Bildirim modu `channels.imessage.reactionNotifications` tarafından denetlenir:

  * `"own"` (varsayılan): yalnızca kullanıcılar bot tarafından yazılan iletilere tepki verdiğinde bildir.
  * `"all"`: yetkili göndericilerden gelen tüm tapback'ler için bildir.
  * `"off"`: gelen tapback'leri yoksay.


Hesap başına geçersiz kılmalar `channels.imessage.accounts.<id>.reactionNotifications` kullanır.

## Yapılandırma yazımları

iMessage, varsayılan olarak kanal tarafından başlatılan yapılandırma yazımlarına izin verir (`commands.config: true` olduğunda `/config set|unset` için).

Devre dışı bırakma:

json5Copy code
[code]
    {  channels: {    imessage: {      configWrites: false,    },  },}
[/code]

## Bölünmüş gönderilen DM'leri birleştirme (tek kompozisyonda komut + URL)

Bir kullanıcı bir komutu ve URL'yi birlikte yazdığında — örn. `Dump https://example.com/article` — Apple'ın Messages uygulaması gönderimi **iki ayrı`chat.db` satırına** böler:

  1. Bir metin iletisi (`"Dump"`).
  2. Ek olarak OG önizleme görselleri içeren bir URL önizleme balonu (`"https://..."`).


İki satır çoğu kurulumda OpenClaw'a ~0.8-2.0 sn arayla ulaşır. Birleştirme olmadan agent 1. turda komutu tek başına alır, yanıt verir (sık sık "bana URL'yi gönder" der) ve URL'yi ancak 2. turda görür; o noktada komut bağlamı zaten kaybolmuştur. Bu, OpenClaw veya `imsg` tarafından eklenen bir şey değil, Apple'ın gönderme pipeline'ıdır.

`channels.imessage.coalesceSameSenderDms`, bir DM'i aynı gönderenden art arda gelen satırları tek bir agent turunda birleştirecek şekilde etkinleştirir. Grup sohbetleri, çok kullanıcılı tur yapısının korunması için mesaj başına iletilmeye devam eder.

### Ne zaman etkinleştirilmeli

Şu durumlarda etkinleştirin:

  * Tek mesajda `command + payload` bekleyen Skills gönderiyorsanız (dump, paste, save, queue vb.).
  * Kullanıcılarınız komutların yanında URL'ler, görseller veya uzun içerikler yapıştırıyorsa.
  * Eklenen DM tur gecikmesini kabul edebiliyorsanız (aşağıya bakın).


Şu durumlarda devre dışı bırakın:

  * Tek kelimelik DM tetikleyicileri için minimum komut gecikmesine ihtiyacınız varsa.
  * Tüm akışlarınız payload takipleri olmayan tek seferlik komutlarsa.


### Etkinleştirme

json5Copy code
[code]
    {  channels: {    imessage: {      coalesceSameSenderDms: true, // opt in (default: false)    },  },}
[/code]

Bayrak açıkken ve açık bir `messages.inbound.byChannel.imessage` yokken debounce penceresi **2500 ms** 'ye genişler (eski varsayılan 0 ms'dir; debounce yoktur). Daha geniş pencere gereklidir çünkü Apple'ın 0.8-2.0 sn'lik bölünmüş gönderim ritmi daha dar bir varsayılana sığmaz.

Pencereyi kendiniz ayarlamak için:

json5Copy code
[code]
    {  messages: {    inbound: {      byChannel: {        // 2500 ms works for most setups; raise to 4000 ms if your Mac is        // slow or under memory pressure (observed gap can stretch past 2 s        // then).        imessage: 2500,      },    },  },}
[/code]

### Ödünleşimler

  * **DM mesajları için ek gecikme.** Bayrak açıkken her DM (bağımsız denetim komutları ve tek metinli takipler dahil), payload satırı gelme olasılığına karşı gönderilmeden önce debounce penceresine kadar bekler. Grup sohbeti mesajları anında gönderilmeyi korur.
  * **Birleştirilmiş çıktı sınırlıdır.** Birleştirilmiş metin açık bir `…[truncated]` işaretçisiyle 4000 karakterde sınırlandırılır; ekler 20'de; kaynak girdileri 10'da sınırlandırılır (bunun ötesinde ilk artı en son korunur). Her kaynak GUID'i, aşağı akış telemetrisi için `coalescedMessageGuids` içinde izlenir.
  * **Yalnızca DM.** Grup sohbetleri mesaj başına göndermeye düşer, böylece birden fazla kişi yazarken bot yanıt vermeye devam eder.
  * **Etkinleştirmeli, kanal başına.** Diğer kanallar (Telegram, WhatsApp, Slack, …) etkilenmez. `channels.bluebubbles.coalesceSameSenderDms` ayarlayan eski BlueBubbles yapılandırmaları bu değeri `channels.imessage.coalesceSameSenderDms` konumuna taşımalıdır.


### Senaryolar ve agent'ın gördükleri

Kullanıcının oluşturduğu | `chat.db` üretir | Bayrak kapalı (varsayılan) | Bayrak açık + 2500 ms pencere  
---|---|---|---  
`Dump https://example.com` (tek gönderim) | ~1 sn arayla 2 satır | İki agent turu: yalnızca "Dump", sonra URL | Tek tur: birleştirilmiş metin `Dump https://example.com`  
`Save this 📎image.jpg caption` (ek + metin) | 2 satır | İki tur (ek birleştirmede düşer) | Tek tur: metin + görsel korunur  
`/status` (bağımsız komut) | 1 satır | Anında gönderim | **Pencereye kadar bekle, sonra gönder**  
Tek başına yapıştırılmış URL | 1 satır | Anında gönderim | Anında gönderim (kovada yalnızca bir girdi)  
Metin + URL, dakikalar arayla iki kasıtlı ayrı mesaj olarak gönderildi | Pencere dışında 2 satır | İki tur | İki tur (pencere aralarında sona erer)  
Hızlı yoğun akış (pencere içinde >10 küçük DM) | N satır | N tur | Tek tur, sınırlı çıktı (ilk + en son, metin/ek sınırları uygulanır)  
Grup sohbetinde iki kişi yazıyor | M gönderenden N satır | M+ tur (gönderen kovası başına bir) | M+ tur; grup sohbetleri birleştirilmez  
  
## Gateway kapalı kaldıktan sonra arayı kapatma

Gateway çevrimdışıyken (çökme, yeniden başlatma, Mac uykusu, makinenin kapalı olması), Gateway tekrar ayağa kalktığında `imsg watch` mevcut `chat.db` durumundan devam eder; boşluk sırasında gelen her şey varsayılan olarak asla görülmez. Catchup, bu mesajları bir sonraki başlangıçta yeniden oynatır, böylece agent gelen trafiği sessizce kaçırmaz.

Catchup **varsayılan olarak devre dışıdır**. Kanal başına etkinleştirin:

tsCopy code
[code]
    channels: {  imessage: {    catchup: {      enabled: true,             // master switch (default: false)      maxAgeMinutes: 120,        // skip rows older than now - 2h (default: 120, clamp 1..720)      perRunLimit: 50,           // max rows replayed per startup (default: 50, clamp 1..500)      firstRunLookbackMinutes: 30, // first run with no cursor: look back 30 min (default: 30)      maxFailureRetries: 10,     // give up on a wedged guid after 10 dispatch failures (default: 10)    },  },}
[/code]

### Nasıl çalışır

`monitorIMessageProvider` başlangıcı başına bir geçiş, `imsg launch` hazır → `watch.subscribe` → `performIMessageCatchup` → canlı gönderim döngüsü sırasıyla yürütülür. Catchup'ın kendisi, `imsg watch` tarafından kullanılan aynı JSON-RPC istemcisine karşı `chats.list` \+ sohbet başına `messages.history` kullanır. Catchup geçişi sırasında gelen her şey normal şekilde canlı gönderimden akar; mevcut gelen-dedupe önbelleği, yeniden oynatılan satırlarla olan tüm çakışmaları emer.

Yeniden oynatılan her satır canlı gönderim yolundan (`evaluateIMessageInbound` \+ `dispatchInboundMessage`) geçirilir; bu nedenle allowlist'ler, grup ilkesi, debouncer, echo önbelleği ve okundu bilgileri yeniden oynatılan ve canlı mesajlarda aynı davranır.

### İmleç ve yeniden deneme semantiği

Catchup, `<openclawStateDir>/imessage/catchup/<account>__<hash>.json` konumunda hesap başına bir imleç tutar (OpenClaw durum dizini varsayılan olarak `~/.openclaw` olur, `OPENCLAW_STATE_DIR` ile değiştirilebilir):

jsonCopy code
[code]
    {  "lastSeenMs": 1717900800000,  "lastSeenRowid": 482910,  "updatedAt": 1717900801234,  "failureRetries": { "<guid>": 1 }}
[/code]

  * İmleç her başarılı gönderimde ilerler ve bir satırın gönderimi hata fırlattığında tutulur; bir sonraki başlangıç aynı satırı tutulan imleçten yeniden dener.
  * Aynı `guid` için `maxFailureRetries` ardışık hata fırlatmasından sonra catchup bir `warn` kaydeder ve sonraki başlangıçların ilerleyebilmesi için imleci takılmış mesajın ötesine zorla ilerletir.
  * Zaten vazgeçilmiş guid'ler sonraki çalıştırmalarda görüldüğünde atlanır (gönderim denemesi yapılmaz) ve çalışma özetinde `skippedGivenUp` altında sayılır.


### Operatöre görünen sinyaller

CodeCopy code
[code]
    imessage catchup: replayed=N skippedFromMe=… skippedGivenUp=… failed=… givenUp=… fetchedCount=…imessage catchup: giving up on guid=<guid> after &lt;N&gt; failures; advancing cursor past itimessage catchup: fetched &lt;X&gt; rows across chats, capped to perRunLimit=&lt;Y&gt;
[/code]

Bir `WARN ... capped to perRunLimit` satırı, tek bir başlangıcın tüm birikmiş işi boşaltmadığı anlamına gelir. Boşluklarınız düzenli olarak varsayılan 50 satırlık geçişi aşıyorsa `perRunLimit` değerini artırın (maks. 500).

### Ne zaman kapalı bırakılmalı

  * Gateway watchdog otomatik yeniden başlatma ile sürekli çalışıyorsa ve boşluklar her zaman birkaç saniyeden kısaysa; kapalı varsayılanı uygundur.
  * DM hacmi düşükse ve kaçırılan mesajlar agent davranışını değiştirmeyecekse; `firstRunLookbackMinutes` başlangıç penceresi ilk etkinleştirmede beklenmedik eski bağlamı gönderebilir.


Catchup'ı açtığınızda, imleç olmayan ilk başlangıç yalnızca `firstRunLookbackMinutes` kadar geriye bakar (varsayılan 30 dk), tam `maxAgeMinutes` penceresine değil; bu, etkinleştirme öncesi mesajların uzun bir geçmişini yeniden oynatmayı önler.

## Sorun giderme

imsg bulunamadı veya RPC desteklenmiyor

İkili dosyayı ve RPC desteğini doğrulayın:

bashCopy code
[code]
    imsg rpc --helpimsg status --jsonopenclaw channels status --probe
[/code]

Probe RPC'nin desteklenmediğini bildirirse `imsg`'yi güncelleyin. Özel API eylemleri kullanılamıyorsa oturum açmış macOS kullanıcı oturumunda `imsg launch` çalıştırın ve yeniden probe edin. Gateway macOS üzerinde çalışmıyorsa varsayılan yerel `imsg` yolu yerine yukarıdaki SSH üzerinden Uzak Mac kurulumunu kullanın.

Gateway macOS üzerinde çalışmıyor

Varsayılan `cliPath: "imsg"`, Messages'ta oturum açılmış Mac üzerinde çalışmalıdır. Linux veya Windows üzerinde `channels.imessage.cliPath` değerini o Mac'e SSH yapan ve `imsg "$@"` çalıştıran bir sarmalayıcı betiğe ayarlayın.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T messages-mac imsg "$@"
[/code]

Sonra şunu çalıştırın:

bashCopy code
[code]
    openclaw channels status --probe --channel imessage
[/code]

DM'ler yok sayılıyor

Kontrol edin:

  * `channels.imessage.dmPolicy`
  * `channels.imessage.allowFrom`
  * eşleştirme onayları (`openclaw pairing list imessage`)

Grup mesajları yok sayılıyor

Kontrol edin:

  * `channels.imessage.groupPolicy`
  * `channels.imessage.groupAllowFrom`
  * `channels.imessage.groups` allowlist davranışı
  * bahsetme kalıbı yapılandırması (`agents.list[].groupChat.mentionPatterns`)

Uzak ekler başarısız oluyor

Kontrol edin:

  * `channels.imessage.remoteHost`
  * `channels.imessage.remoteAttachmentRoots`
  * Gateway ana makinesinden SSH/SCP anahtar kimlik doğrulaması
  * Gateway ana makinesinde `~/.ssh/known_hosts` içinde host anahtarının bulunması
  * Messages çalıştıran Mac üzerinde uzak yolun okunabilirliği

macOS izin istemleri kaçırıldı

Aynı kullanıcı/oturum bağlamında etkileşimli bir GUI terminalinde yeniden çalıştırın ve istemleri onaylayın:

bashCopy code
[code]
    imsg chats --limit 1imsg send <handle> "test"
[/code]

OpenClaw/`imsg` çalıştıran işlem bağlamı için Full Disk Access + Automation izinlerinin verildiğini doğrulayın.

## Yapılandırma referansı işaretçileri

  * [Yapılandırma referansı - iMessage](</tr/gateway/config-channels#imessage>)
  * [Gateway yapılandırması](</tr/gateway/configuration>)
  * [Eşleştirme](</tr/channels/pairing>)


## İlgili

  * [Kanallara Genel Bakış](</tr/channels>) — desteklenen tüm kanallar
  * [BlueBubbles'ın kaldırılması ve imsg iMessage yolu](</tr/announcements/bluebubbles-imessage>) — duyuru ve geçiş özeti
  * [BlueBubbles'tan geliyorsanız](</tr/channels/imessage-from-bluebubbles>) — yapılandırma çeviri tablosu ve adım adım geçiş
  * [Eşleştirme](</tr/channels/pairing>) — DM kimlik doğrulaması ve eşleştirme akışı
  * [Gruplar](</tr/channels/groups>) — grup sohbeti davranışı ve bahsetme geçidi
  * [Kanal Yönlendirme](</tr/channels/channel-routing>) — mesajlar için oturum yönlendirme
  * [Güvenlik](</tr/gateway/security>) — erişim modeli ve sağlamlaştırma


Was this useful?YesNo