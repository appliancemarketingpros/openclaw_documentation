---
title: Hetzner
source_url: https://docs.openclaw.ai/tr/install/hetzner
scraped_at: 2026-05-25
---

## Hedef

Docker kullanarak Hetzner VPS üzerinde kalıcı durum, görüntüye dahil edilmiş ikili dosyalar ve güvenli yeniden başlatma davranışıyla sürekli çalışan bir OpenClaw Gateway çalıştırın.

"~$5 karşılığında 7/24 OpenClaw" istiyorsanız en basit güvenilir kurulum budur. Hetzner fiyatları değişebilir; en küçük Debian/Ubuntu VPS'i seçin ve OOM sorunlarıyla karşılaşırsanız ölçeği büyütün.

Güvenlik modeli hatırlatması:

  * Şirket içinde paylaşılan agent'lar, herkes aynı güven sınırı içindeyse ve çalışma zamanı yalnızca iş amaçlıysa uygundur.
  * Katı ayrım sağlayın: özel VPS/çalışma zamanı + özel hesaplar; bu ana makinede kişisel Apple/Google/tarayıcı/parola yöneticisi profilleri bulunmamalıdır.
  * Kullanıcılar birbirine karşı saldırgan olabilecekse Gateway/ana makine/OS kullanıcısına göre ayırın.


Bkz. [Güvenlik](</tr/gateway/security>) ve [VPS barındırma](</tr/vps>).

## Ne yapıyoruz (basitçe)?

  * Küçük bir Linux sunucusu kiralayın (Hetzner VPS)
  * Docker'ı kurun (yalıtılmış uygulama çalışma zamanı)
  * OpenClaw Gateway'i Docker içinde başlatın
  * `~/.openclaw` \+ `~/.openclaw/workspace` dizinlerini ana makinede kalıcı hale getirin (yeniden başlatmalarda/yeniden derlemelerde korunur)
  * Dizüstü bilgisayarınızdan bir SSH tüneliyle Control UI'ye erişin


Bağlanan `~/.openclaw` durumu `openclaw.json`, agent başına `agents/<agentId>/agent/auth-profiles.json` ve `.env` dosyasını içerir.

Gateway'e şu yollarla erişilebilir:

  * Dizüstü bilgisayarınızdan SSH bağlantı noktası yönlendirme
  * Güvenlik duvarını ve token'ları kendiniz yönetiyorsanız doğrudan bağlantı noktası açma


Bu kılavuz Hetzner üzerinde Ubuntu veya Debian varsayar.  
Başka bir Linux VPS kullanıyorsanız paketleri buna göre eşleştirin. Genel Docker akışı için bkz. [Docker](</tr/install/docker>).

* * *

## Hızlı yol (deneyimli operatörler)

  1. Hetzner VPS hazırlayın
  2. Docker'ı kurun
  3. OpenClaw deposunu klonlayın
  4. Kalıcı ana makine dizinleri oluşturun
  5. `.env` ve `docker-compose.yml` dosyalarını yapılandırın
  6. Gerekli ikili dosyaları görüntüye dahil edin
  7. `docker compose up -d`
  8. Kalıcılığı ve Gateway erişimini doğrulayın


* * *

## Gerekenler

  * Root erişimi olan Hetzner VPS
  * Dizüstü bilgisayarınızdan SSH erişimi
  * SSH + kopyala/yapıştır konusunda temel rahatlık
  * ~20 dakika
  * Docker ve Docker Compose
  * Model kimlik doğrulama bilgileri
  * İsteğe bağlı sağlayıcı kimlik bilgileri 
    * WhatsApp QR
    * Telegram bot token'ı
    * Gmail OAuth


* * *

* ### Provision the VPS

Hetzner'de bir Ubuntu veya Debian VPS oluşturun.

Root olarak bağlanın:

bashCopy code
[code]
    ssh root@YOUR_VPS_IP
[/code]

Bu kılavuz VPS'in durum bilgisi tutan bir sistem olduğunu varsayar. Bunu atılabilir altyapı gibi ele almayın.

* ### Install Docker (on the VPS)

bashCopy code
[code]
    apt-get updateapt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sh
[/code]

Doğrulayın:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Clone the OpenClaw repository

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Bu kılavuz, ikili dosya kalıcılığını garanti etmek için özel bir görüntü derleyeceğinizi varsayar.

* ### Create persistent host directories

Docker container'ları geçicidir. Uzun ömürlü tüm durum ana makinede bulunmalıdır.

bashCopy code
[code]
    mkdir -p /root/.openclaw/workspace # Set ownership to the container user (uid 1000):chown -R 1000:1000 /root/.openclaw
[/code]

* ### Configure environment variables

Depo kökünde `.env` oluşturun.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/root/.openclawOPENCLAW_WORKSPACE_DIR=/root/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Kararlı Gateway token'ını `.env` üzerinden yönetmek istediğinizde `OPENCLAW_GATEWAY_TOKEN` değerini ayarlayın; aksi halde yeniden başlatmalar arasında istemcilere güvenmeden önce `gateway.auth.token` değerini yapılandırın. Hiçbir kaynak yoksa OpenClaw bu başlangıç için yalnızca çalışma zamanına ait bir token kullanır. Bir anahtarlık parolası oluşturun ve `GOG_KEYRING_PASSWORD` içine yapıştırın:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Bu dosyayı commit'lemeyin.**

Bu `.env` dosyası, `OPENCLAW_GATEWAY_TOKEN` gibi container/çalışma zamanı ortam değişkenleri içindir. Saklanan sağlayıcı OAuth/API anahtarı kimlik doğrulaması, bağlanan `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` içinde yaşar.

* ### Docker Compose configuration

`docker-compose.yml` oluşturun veya güncelleyin.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VPS; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` yalnızca başlangıç kolaylığı içindir; uygun bir Gateway yapılandırmasının yerine geçmez. Dağıtımınız için yine de kimlik doğrulamayı (`gateway.auth.token` veya parola) ayarlayın ve güvenli bind ayarları kullanın.

* ### Shared Docker VM runtime steps

Ortak Docker ana makine akışı için paylaşılan çalışma zamanı kılavuzunu kullanın:

  * [Gerekli ikili dosyaları görüntüye dahil edin](</tr/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Derleyin ve başlatın](</tr/install/docker-vm-runtime#build-and-launch>)
  * [Nerede ne kalıcı olur](</tr/install/docker-vm-runtime#what-persists-where>)
  * [Güncellemeler](</tr/install/docker-vm-runtime#updates>)


* ### Hetzner-specific access

Paylaşılan derleme ve başlatma adımlarından sonra tüneli açmak için aşağıdaki kurulumu tamamlayın:

**Ön koşul:** VPS sshd yapılandırmanızın TCP yönlendirmeye izin verdiğinden emin olun. SSH yapılandırmanızı sertleştirdiyseniz `/etc/ssh/sshd_config` dosyasını kontrol edin ve şunu ayarlayın:

CodeCopy code
[code]
    AllowTcpForwarding local
[/code]

`local`, sunucudan uzak yönlendirmeleri engellerken dizüstü bilgisayarınızdan `ssh -L` yerel yönlendirmelerine izin verir. Bunu `no` olarak ayarlamak tünelin şu hatayla başarısız olmasına neden olur: `channel 3: open failed: administratively prohibited: open failed`

TCP yönlendirmenin etkin olduğunu doğruladıktan sonra SSH hizmetini yeniden başlatın (`systemctl restart ssh`) ve tüneli dizüstü bilgisayarınızdan çalıştırın:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 root@YOUR_VPS_IP
[/code]

Açın:

`http://127.0.0.1:18789/`

Yapılandırılmış paylaşılan sırrı yapıştırın. Bu kılavuz varsayılan olarak Gateway token'ını kullanır; parola kimlik doğrulamasına geçtiyseniz bunun yerine o parolayı kullanın.

Paylaşılan kalıcılık haritası [Docker VM Runtime](</tr/install/docker-vm-runtime#what-persists-where>) içinde bulunur.

## Kod Olarak Altyapı (Terraform)

Kod olarak altyapı iş akışlarını tercih eden ekipler için topluluk tarafından sürdürülen bir Terraform kurulumu şunları sağlar:

  * Uzak durum yönetimiyle modüler Terraform yapılandırması
  * cloud-init aracılığıyla otomatik hazırlama
  * Dağıtım betikleri (bootstrap, deploy, backup/restore)
  * Güvenlik sertleştirmesi (güvenlik duvarı, UFW, yalnızca SSH erişimi)
  * Gateway erişimi için SSH tüneli yapılandırması


**Depolar:**

  * Altyapı: [openclaw-terraform-hetzner](<https://github.com/andreesg/openclaw-terraform-hetzner>)
  * Docker yapılandırması: [openclaw-docker-config](<https://github.com/andreesg/openclaw-docker-config>)


Bu yaklaşım, yukarıdaki Docker kurulumunu tekrarlanabilir dağıtımlar, sürüm kontrollü altyapı ve otomatik felaket kurtarma ile tamamlar.

## Sonraki adımlar

  * Mesajlaşma kanallarını kurun: [Kanallar](</tr/channels>)
  * Gateway'i yapılandırın: [Gateway yapılandırması](</tr/gateway/configuration>)
  * OpenClaw'ı güncel tutun: [Güncelleme](</tr/install/updating>)


## İlgili

  * [Kurulum genel bakışı](</tr/install>)
  * [Fly.io](</tr/install/fly>)
  * [Docker](</tr/install/docker>)
  * [VPS barındırma](</tr/vps>)


Was this useful?YesNo