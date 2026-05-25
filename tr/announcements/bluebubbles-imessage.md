---
title: BlueBubbles'ın kaldırılması ve imsg iMessage yolu
source_url: https://docs.openclaw.ai/tr/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# BlueBubbles’ın kaldırılması ve imsg iMessage yolu

OpenClaw artık BlueBubbles kanalını birlikte sunmaz. iMessage desteği artık yerel olarak veya bir SSH sarmalayıcısı üzerinden [`imsg`](<https://github.com/steipete/imsg>) başlatan ve stdin/stdout üzerinden JSON-RPC ile iletişim kuran birlikte gelen `imessage` Plugin üzerinden çalışır.

Yapılandırmanız hâlâ `channels.bluebubbles` içeriyorsa bunu `channels.imessage` olarak taşıyın. Eski `/channels/bluebubbles` dokümantasyon URL’si, tam yapılandırma çeviri tablosunu ve geçiş kontrol listesini içeren [BlueBubbles’dan geliyorsanız](</tr/channels/imessage-from-bluebubbles>) sayfasına yönlendirir.

## Ne değişti

  * Desteklenen OpenClaw iMessage yolunda BlueBubbles HTTP sunucusu, webhook rotası, REST parolası veya BlueBubbles Plugin çalışma zamanı yoktur.
  * OpenClaw, Messages.app’in oturum açmış olduğu Mac’te `imsg` üzerinden Mesajlar’ı okur ve izler.
  * Temel gönderme, alma, geçmiş ve medya işlemleri normal `imsg` yüzeylerini ve macOS izinlerini kullanır.
  * İleti dizisi yanıtları, tapback’ler, düzenleme, göndermeyi geri alma, efektler, okundu bilgileri, yazıyor göstergeleri ve grup yönetimi gibi gelişmiş eylemler, özel API köprüsü kullanılabilir durumdayken `imsg launch` gerektirir.
  * Linux ve Windows Gateway’leri, `channels.imessage.cliPath` değerini oturum açılmış Mac’te `imsg` çalıştıran bir SSH sarmalayıcısına ayarlayarak iMessage kullanmaya devam edebilir.


## Ne yapılmalı

  1. Messages Mac’te `imsg` yükleyin ve doğrulayın:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. `imsg` ve OpenClaw çalıştıran süreç bağlamına Tam Disk Erişimi ve Otomasyon izinlerini verin.

  3. Eski yapılandırmayı dönüştürün:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Gateway’i yeniden başlatın ve doğrulayın:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Eski BlueBubbles sunucunuzu silmeden önce DM’leri, grupları, ekleri ve bağımlı olduğunuz tüm özel API eylemlerini test edin.


## Taşıma notları

  * `channels.bluebubbles.serverUrl` ve `channels.bluebubbles.password` için iMessage eşdeğeri yoktur.
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, ek kökleri, medya boyutu sınırları, parçalama ve eylem anahtarlarının iMessage eşdeğerleri vardır.
  * `channels.imessage.includeAttachments` varsayılan olarak hâlâ kapalıdır. Gelen fotoğrafların, sesli notların, videoların veya dosyaların ajana ulaşmasını bekliyorsanız bunu açıkça ayarlayın.
  * `groupPolicy: "allowlist"` ile, varsa `"*"` joker karakter girdisi dahil eski `groups` bloğunu kopyalayın. Grup gönderen izin listeleri ve grup kayıt defteri ayrı kapılardır.
  * `channel: "bluebubbles"` ile eşleşen ACP bağlamaları `channel: "imessage"` olarak değiştirilmelidir.
  * Eski BlueBubbles oturum anahtarları iMessage oturum anahtarlarına dönüşmez. Eşleştirme onayları tanıtıcıya göre taşınır, ancak BlueBubbles oturum anahtarları altındaki konuşma geçmişi taşınmaz.


## Ayrıca bkz.

  * [BlueBubbles’dan geliyorsanız](</tr/channels/imessage-from-bluebubbles>)
  * [iMessage](</tr/channels/imessage>)
  * [Yapılandırma başvurusu - iMessage](</tr/gateway/config-channels#imessage>)


Was this useful?YesNo