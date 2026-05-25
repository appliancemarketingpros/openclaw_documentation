---
title: Linux sunucusu
source_url: https://docs.openclaw.ai/tr/vps
scraped_at: 2026-05-25
---

OpenClaw Gateway'i herhangi bir Linux sunucusunda veya bulut VPS üzerinde çalıştırın. Bu sayfa bir sağlayıcı seçmenize yardımcı olur, bulut dağıtımlarının nasıl çalıştığını açıklar ve her yerde geçerli olan genel Linux ayarlamalarını kapsar.

## Bir sağlayıcı seçin

[**Railway** [**Northflank** [**DigitalOcean** [**Oracle Cloud** [**Fly.io** [**Hetzner** [**Hostinger** [**GCP** [**Azure** [**exe.dev** [**Raspberry Pi** **AWS (EC2 / Lightsail / ücretsiz katman)** da iyi çalışır. Topluluk tarafından hazırlanmış bir video anlatımı [x.com/techfrenAJ/status/2014934471095812547](<https://x.com/techfrenAJ/status/2014934471095812547>) adresinde mevcuttur (topluluk kaynağı -- kullanılamaz hale gelebilir). Bulut kurulumları nasıl çalışır

  * **Gateway VPS üzerinde çalışır** ve durum + çalışma alanına sahip olur.
  * Dizüstü bilgisayarınızdan veya telefonunuzdan **Kontrol Arayüzü** ya da **Tailscale/SSH** üzerinden bağlanırsınız.
  * VPS'yi doğruluk kaynağı olarak kabul edin ve durum + çalışma alanını düzenli olarak **yedekleyin**.
  * Güvenli varsayılan: Gateway'i loopback üzerinde tutun ve ona SSH tüneli veya Tailscale Serve üzerinden erişin. `lan` veya `tailnet` adresine bağlarsanız `gateway.auth.token` ya da `gateway.auth.password` zorunlu olsun.

İlgili sayfalar: [Gateway uzaktan erişim](</tr/gateway/remote>), [Platformlar merkezi](</tr/platforms>). Önce yönetici erişimini sağlamlaştırın OpenClaw'u herkese açık bir VPS üzerine kurmadan önce, makinenin kendisini nasıl yönetmek istediğinize karar verin.

  * Yalnızca Tailnet üzerinden yönetici erişimi istiyorsanız önce Tailscale'i kurun, VPS'yi tailnet'inize katın, Tailscale IP'si veya MagicDNS adı üzerinden ikinci bir SSH oturumunu doğrulayın, ardından herkese açık SSH erişimini kısıtlayın.
  * Tailscale kullanmıyorsanız, daha fazla hizmeti dışa açmadan önce SSH yolunuz için eşdeğer sağlamlaştırmayı uygulayın.
  * Bu, Gateway erişiminden ayrıdır. OpenClaw'u yine loopback'e bağlı tutabilir ve pano için SSH tüneli veya Tailscale Serve kullanabilirsiniz.

Tailscale'e özgü Gateway seçenekleri [Tailscale](</tr/gateway/tailscale>) bölümünde yer alır. VPS üzerinde paylaşılan şirket ajanı Tek bir ajanı bir ekip için çalıştırmak, her kullanıcı aynı güven sınırı içindeyse ve ajan yalnızca iş amaçlıysa geçerli bir kurulumdur.

  * Onu ayrılmış bir çalışma ortamında tutun (VPS/VM/kapsayıcı + ayrılmış OS kullanıcısı/hesapları).
  * Bu çalışma ortamında kişisel Apple/Google hesaplarına veya kişisel tarayıcı/parola yöneticisi profillerine giriş yapmayın.
  * Kullanıcılar birbirine karşı hasmane davranabilecekse gateway/ana makine/OS kullanıcısına göre ayırın.

Güvenlik modeli ayrıntıları: [Güvenlik](</tr/gateway/security>). VPS ile düğümleri kullanma Gateway'i bulutta tutabilir ve yerel cihazlarınızdaki **düğümleri** eşleyebilirsiniz (Mac/iOS/Android/headless). Düğümler, Gateway bulutta kalırken yerel ekran/kamera/canvas ve `system.run` yetenekleri sağlar. Belgeler: [Düğümler](</tr/nodes>), [Düğümler CLI](</tr/cli/nodes>). Küçük VM'ler ve ARM ana makineleri için başlangıç ayarlaması Düşük güçlü VM'lerde (veya ARM ana makinelerinde) CLI komutları yavaş geliyorsa Node'un modül derleme önbelleğini etkinleştirin: bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF'export NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

  * `NODE_COMPILE_CACHE` tekrarlanan komut başlangıç sürelerini iyileştirir.
  * `OPENCLAW_NO_RESPAWN=1`, kendini yeniden başlatma yolundan gelen ek başlangıç yükünü önler.
  * İlk komut çalıştırması önbelleği ısıtır; sonraki çalıştırmalar daha hızlıdır.
  * Raspberry Pi'ye özgü ayrıntılar için [Raspberry Pi](</tr/install/raspberry-pi>) bölümüne bakın.

systemd ayarlama kontrol listesi (isteğe bağlı) `systemd` kullanan VM ana makineleri için şunları değerlendirin:

  * Kararlı bir başlangıç yolu için hizmet ortam değişkenleri ekleyin: 
    * `OPENCLAW_NO_RESPAWN=1`
    * `NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache`
  * Yeniden başlatma davranışını açık tutun: 
    * `Restart=always`
    * `RestartSec=2`
    * `TimeoutStartSec=90`
  * Rastgele G/Ç soğuk başlangıç cezalarını azaltmak için durum/önbellek yollarında SSD destekli diskleri tercih edin.

Standart `openclaw onboard --install-daemon` yolu için kullanıcı birimini düzenleyin: bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Bunun yerine bilerek bir sistem birimi kurduysanız, `openclaw-gateway.service` dosyasını `sudo systemctl edit openclaw-gateway.service` ile düzenleyin. `Restart=` ilkelerinin otomatik kurtarmaya nasıl yardımcı olduğu: [systemd hizmet kurtarmayı otomatikleştirebilir](<https://www.redhat.com/en/blog/systemd-automate-recovery>). Linux OOM davranışı, alt süreç kurban seçimi ve `exit 137` tanıları için [Linux bellek baskısı ve OOM sonlandırmaları](</tr/platforms/linux#memory-pressure-and-oom-kills>) bölümüne bakın. İlgili

  * [Kurulum genel bakışı](</tr/install>)
  * [DigitalOcean](</tr/install/digitalocean>)
  * [Fly.io](</tr/install/fly>)
  * [Hetzner](</tr/install/hetzner>)

](</tr/install/raspberry-pi>) Was this useful?YesNo ](</tr/install/exe-dev>)](</tr/install/azure>)](</tr/install/gcp>)](</tr/install/hostinger>)](</tr/install/hetzner>)](</tr/install/fly>)](</tr/install/oracle>)](</tr/install/digitalocean>)](</tr/install/northflank>)](</tr/install/railway>)