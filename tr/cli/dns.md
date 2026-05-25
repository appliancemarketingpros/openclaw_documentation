---
title: DNS
source_url: https://docs.openclaw.ai/tr/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

Geniş alan keşfi için DNS yardımcıları (Tailscale + CoreDNS). Şu anda macOS + Homebrew CoreDNS odaklıdır.

İlgili:

  * Gateway keşfi: [Keşif](</tr/gateway/discovery>)
  * Geniş alan keşfi yapılandırması: [Yapılandırma](</tr/gateway/configuration>)


## Kurulum

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Unicast DNS-SD keşfi için CoreDNS kurulumunu planlayın veya uygulayın.

Seçenekler:

  * `--domain <domain>`: geniş alan keşfi alan adı (örneğin `openclaw.internal`)
  * `--apply`: CoreDNS yapılandırmasını yükle veya güncelle ve hizmeti yeniden başlat (sudo gerektirir; yalnızca macOS)


Gösterdikleri:

  * çözümlenen keşif alan adı
  * bölge dosyası yolu
  * mevcut tailnet IP’leri
  * önerilen `openclaw.json` keşif yapılandırması
  * ayarlanacak Tailscale Split DNS ad sunucusu/alan adı değerleri


Notlar:

  * `--apply` olmadan komut yalnızca bir planlama yardımcısıdır ve önerilen kurulumu yazdırır.
  * `--domain` atlanırsa OpenClaw yapılandırmadaki `discovery.wideArea.domain` değerini kullanır.
  * `--apply` şu anda yalnızca macOS destekler ve Homebrew CoreDNS bekler.
  * `--apply`, gerekirse bölge dosyasını önyükler, CoreDNS içe aktarma bendinin mevcut olmasını sağlar ve `coredns` brew hizmetini yeniden başlatır.


## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Keşif](</tr/gateway/discovery>)


Was this useful?YesNo