---
title: Nostr
source_url: https://docs.openclaw.ai/tr/channels/nostr
scraped_at: 2026-05-25
---

**Durum:** İsteğe bağlı paketlenmiş Plugin (yapılandırılana kadar varsayılan olarak devre dışıdır).

Nostr, sosyal ağlar için merkeziyetsiz bir protokoldür. Bu kanal, OpenClaw’ın NIP-04 üzerinden şifrelenmiş doğrudan mesajları (DM’ler) almasını ve yanıtlamasını sağlar.

## Paketlenmiş Plugin

Güncel OpenClaw sürümleri Nostr’u paketlenmiş bir Plugin olarak sunar, bu yüzden normal paketlenmiş derlemeler ayrı bir kurulum gerektirmez.

### Eski/özel kurulumlar

  * Onboarding (`openclaw onboard`) ve `openclaw channels add`, Nostr’u paylaşılan kanal kataloğundan göstermeye devam eder.
  * Derlemeniz paketlenmiş Nostr’u hariç tutuyorsa npm paketini doğrudan kurun.

bashCopy code
[code]
    openclaw plugins install @openclaw/nostr
[/code]

Güncel resmi sürüm etiketini takip etmek için yalın paketi kullanın. Tam bir sürümü yalnızca tekrarlanabilir bir kurulum gerektiğinde sabitleyin.

Yerel bir checkout kullanın (geliştirme iş akışları):

bashCopy code
[code]
    openclaw plugins install --link <path-to-local-nostr-plugin>
[/code]

Plugin’leri kurduktan veya etkinleştirdikten sonra Gateway’i yeniden başlatın.

### Etkileşimsiz kurulum

bashCopy code
[code]
    openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY"openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY" --relay-urls "wss://relay.damus.io,wss://relay.primal.net"
[/code]

Anahtarı yapılandırmada depolamak yerine `NOSTR_PRIVATE_KEY` değerini ortamda tutmak için `--use-env` kullanın.

## Hızlı kurulum

  1. Bir Nostr anahtar çifti oluşturun (gerekiyorsa):

bashCopy code
[code]
    # Using naknak key generate
[/code]

  2. Yapılandırmaya ekleyin:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",    },  },}
[/code]

  3. Anahtarı dışa aktarın:

bashCopy code
[code]
    export NOSTR_PRIVATE_KEY="nsec1..."
[/code]

  4. Gateway’i yeniden başlatın.


## Yapılandırma başvurusu

Anahtar | Tür | Varsayılan | Açıklama  
---|---|---|---  
`privateKey` | string | gerekli | `nsec` veya hex biçiminde özel anahtar  
`relays` | string[] | `['wss://relay.damus.io', 'wss://nos.lol']` | Relay URL’leri (WebSocket)  
`dmPolicy` | string | `pairing` | DM erişim ilkesi  
`allowFrom` | string[] | `[]` | İzin verilen gönderen pubkey’leri  
`enabled` | boolean | `true` | Kanalı etkinleştir/devre dışı bırak  
`name` | string | - | Görünen ad  
`profile` | object | - | NIP-01 profil meta verileri  
  
## Profil meta verileri

Profil verileri NIP-01 `kind:0` olayı olarak yayımlanır. Bunu Control UI’dan (Channels -> Nostr -> Profile) yönetebilir veya doğrudan yapılandırmada ayarlayabilirsiniz.

Örnek:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      profile: {        name: "openclaw",        displayName: "OpenClaw",        about: "Personal assistant DM bot",        picture: "https://example.com/avatar.png",        banner: "https://example.com/banner.png",        website: "https://example.com",        nip05: "openclaw@example.com",        lud16: "openclaw@example.com",      },    },  },}
[/code]

Notlar:

  * Profil URL’leri `https://` kullanmalıdır.
  * Relay’lerden içe aktarma alanları birleştirir ve yerel geçersiz kılmaları korur.


## Erişim denetimi

### DM ilkeleri

  * **pairing** (varsayılan): bilinmeyen gönderenler bir eşleştirme kodu alır.
  * **allowlist** : yalnızca `allowFrom` içindeki pubkey’ler DM gönderebilir.
  * **open** : herkese açık gelen DM’ler (`allowFrom: ["*"]` gerektirir).
  * **disabled** : gelen DM’leri yok sayar.


Zorunlu kılma notları:

  * Gelen olay imzaları, gönderen ilkesi ve NIP-04 şifre çözümünden önce doğrulanır; böylece sahte olaylar erken reddedilir.
  * Eşleştirme yanıtları, özgün DM gövdesi işlenmeden gönderilir.
  * Gelen DM’ler hız sınırlamasına tabidir ve aşırı büyük yükler şifre çözmeden önce düşürülür.


### Allowlist örneği

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      dmPolicy: "allowlist",      allowFrom: ["npub1abc...", "npub1xyz..."],    },  },}
[/code]

## Anahtar biçimleri

Kabul edilen biçimler:

  * **Özel anahtar:** `nsec...` veya 64 karakterlik hex
  * **Pubkey’ler (`allowFrom`):** `npub...` veya hex


## Relay’ler

Varsayılanlar: `relay.damus.io` ve `nos.lol`.

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["wss://relay.damus.io", "wss://relay.primal.net", "wss://nostr.wine"],    },  },}
[/code]

İpuçları:

  * Yedeklilik için 2-3 relay kullanın.
  * Çok fazla relay’den kaçının (gecikme, çoğaltma).
  * Ücretli relay’ler güvenilirliği artırabilir.
  * Yerel relay’ler test için uygundur (`ws://localhost:7777`).


## Protokol desteği

NIP | Durum | Açıklama  
---|---|---  
NIP-01 | Desteklenir | Temel olay biçimi + profil meta verileri  
NIP-04 | Desteklenir | Şifrelenmiş DM’ler (`kind:4`)  
NIP-17 | Planlandı | Hediye paketli DM’ler  
NIP-44 | Planlandı | Sürümlü şifreleme  
  
## Test etme

### Yerel relay

bashCopy code
[code]
    # Start strfrydocker run -p 7777:7777 ghcr.io/hoytech/strfry
[/code]

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["ws://localhost:7777"],    },  },}
[/code]

### Manuel test

  1. Günlüklerden bot pubkey’ini (npub) not edin.
  2. Bir Nostr istemcisi açın (Damus, Amethyst vb.).
  3. Bot pubkey’ine DM gönderin.
  4. Yanıtı doğrulayın.


## Sorun giderme

### Mesajlar alınmıyor

  * Özel anahtarın geçerli olduğunu doğrulayın.
  * Relay URL’lerinin erişilebilir olduğundan ve `wss://` (veya yerel için `ws://`) kullandığından emin olun.
  * `enabled` değerinin `false` olmadığını doğrulayın.
  * Relay bağlantı hataları için Gateway günlüklerini kontrol edin.


### Yanıtlar gönderilmiyor

  * Relay’in yazmaları kabul ettiğini kontrol edin.
  * Giden bağlantıyı doğrulayın.
  * Relay hız sınırlarını izleyin.


### Yinelenen yanıtlar

  * Birden fazla relay kullanırken beklenir.
  * Mesajlar olay kimliğine göre tekilleştirilir; yalnızca ilk teslimat bir yanıt tetikler.


## Güvenlik

  * Özel anahtarları asla commit etmeyin.
  * Anahtarlar için ortam değişkenleri kullanın.
  * Üretim botları için `allowlist` kullanmayı değerlendirin.
  * İmzalar gönderen ilkesinden önce doğrulanır ve gönderen ilkesi şifre çözmeden önce uygulanır; böylece sahte olaylar erken reddedilir ve bilinmeyen gönderenler tam kripto çalışmasını zorlayamaz.


## Sınırlamalar (MVP)

  * Yalnızca doğrudan mesajlar (grup sohbeti yok).
  * Medya ekleri yok.
  * Yalnızca NIP-04 (NIP-17 hediye paketleme planlandı).


## İlgili

  * [Kanallara Genel Bakış](</tr/channels>) — desteklenen tüm kanallar
  * [Eşleştirme](</tr/channels/pairing>) — DM kimlik doğrulaması ve eşleştirme akışı
  * [Gruplar](</tr/channels/groups>) — grup sohbeti davranışı ve bahsetme kapısı
  * [Kanal Yönlendirme](</tr/channels/channel-routing>) — mesajlar için oturum yönlendirmesi
  * [Güvenlik](</tr/gateway/security>) — erişim modeli ve sıkılaştırma


Was this useful?YesNo