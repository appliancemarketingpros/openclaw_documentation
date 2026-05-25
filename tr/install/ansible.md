---
title: Ansible
source_url: https://docs.openclaw.ai/tr/install/ansible
scraped_at: 2026-05-25
---

OpenClaw'ı **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** ile üretim sunucularına dağıtın -- güvenlik öncelikli mimariye sahip otomatik bir kurulum aracı.

## Önkoşullar

Gereksinim | Ayrıntılar  
---|---  
**İS** | Debian 11+ veya Ubuntu 20.04+  
**Erişim** | Root veya sudo ayrıcalıkları  
**Ağ** | Paket kurulumu için internet bağlantısı  
**Ansible** | 2.14+ (hızlı başlangıç betiği tarafından otomatik kurulur)  
  
## Ne elde edersiniz

  * **Önce güvenlik duvarı güvenliği** \-- UFW + Docker izolasyonu (yalnızca SSH + Tailscale erişilebilir)
  * **Tailscale VPN** \-- hizmetleri herkese açık şekilde dışa açmadan güvenli uzaktan erişim
  * **Docker** \-- izole sandbox kapsayıcıları, yalnızca localhost bağlamaları
  * **Derinlemesine savunma** \-- 4 katmanlı güvenlik mimarisi
  * **Systemd entegrasyonu** \-- güçlendirme ile açılışta otomatik başlatma
  * **Tek komutla kurulum** \-- dakikalar içinde eksiksiz dağıtım


## Hızlı başlangıç

Tek komutla kurulum:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Neler kurulur

Ansible playbook şunları kurar ve yapılandırır:

  1. **Tailscale** \-- güvenli uzaktan erişim için mesh VPN
  2. **UFW güvenlik duvarı** \-- yalnızca SSH + Tailscale bağlantı noktaları
  3. **Docker CE + Compose V2** \-- varsayılan ajan sandbox arka ucu için
  4. **Node.js 24 + pnpm** \-- çalışma zamanı bağımlılıkları (Node 22 LTS, şu anda `22.16+`, desteklenmeye devam eder)
  5. **OpenClaw** \-- ana makine tabanlı, kapsayıcılaştırılmamış
  6. **Systemd hizmeti** \-- güvenlik güçlendirmesiyle otomatik başlatma


## Kurulum Sonrası Ayarlar

* ### openclaw kullanıcısına geçin

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Onboarding sihirbazını çalıştırın

Kurulum sonrası betiği, OpenClaw ayarlarını yapılandırmanız için size rehberlik eder.

* ### Mesajlaşma sağlayıcılarını bağlayın

WhatsApp, Telegram, Discord veya Signal ile oturum açın:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Kurulumu doğrulayın

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Tailscale'e bağlanın

Güvenli uzaktan erişim için VPN mesh ağınıza katılın.

### Hızlı komutlar

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## Güvenlik mimarisi

Dağıtım 4 katmanlı bir savunma modeli kullanır:

  1. **Güvenlik duvarı (UFW)** \-- yalnızca SSH (22) + Tailscale (41641/udp) herkese açık şekilde dışa açıktır
  2. **VPN (Tailscale)** \-- Gateway yalnızca VPN mesh üzerinden erişilebilir
  3. **Docker izolasyonu** \-- DOCKER-USER iptables zinciri harici bağlantı noktası açılmasını önler
  4. **Systemd güçlendirmesi** \-- NoNewPrivileges, PrivateTmp, ayrıcalıksız kullanıcı


Harici saldırı yüzeyinizi doğrulamak için:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Yalnızca 22 numaralı bağlantı noktası (SSH) açık olmalıdır. Diğer tüm hizmetler (Gateway, Docker) kilitlenmiştir.

Docker, Gateway'in kendisini çalıştırmak için değil, ajan sandbox'ları (izole araç yürütme) için kurulur. Sandbox yapılandırması için [Multi-Agent Sandbox and Tools](</tr/tools/multi-agent-sandbox-tools>) sayfasına bakın.

## Manuel kurulum

Otomasyon üzerinde manuel denetimi tercih ediyorsanız:

* ### Önkoşulları kurun

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Depoyu klonlayın

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Ansible koleksiyonlarını kurun

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Playbook'u çalıştırın

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Alternatif olarak, doğrudan çalıştırıp ardından kurulum betiğini daha sonra manuel olarak yürütün:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## Güncelleme

Ansible kurulum aracı, OpenClaw'ı manuel güncellemeler için ayarlar. Standart güncelleme akışı için [Güncelleme](</tr/install/updating>) sayfasına bakın.

Ansible playbook'u yeniden çalıştırmak için (örneğin yapılandırma değişiklikleri için):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Bu işlem idempotenttir ve birden çok kez güvenle çalıştırılabilir.

## Sorun giderme

Güvenlik duvarı bağlantımı engelliyor

  * Önce Tailscale VPN üzerinden erişebildiğinizden emin olun
  * SSH erişimine (22 numaralı bağlantı noktası) her zaman izin verilir
  * Gateway tasarım gereği yalnızca Tailscale üzerinden erişilebilir

Hizmet başlamıyor bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Docker sandbox sorunları bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Sağlayıcı oturumu açılamıyor

`openclaw` kullanıcısı olarak çalıştığınızdan emin olun:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Gelişmiş yapılandırma

Ayrıntılı güvenlik mimarisi ve sorun giderme için openclaw-ansible deposuna bakın:

  * [Güvenlik Mimarisi](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Teknik Ayrıntılar](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Sorun Giderme Kılavuzu](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## İlgili

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- tam dağıtım kılavuzu
  * [Docker](</tr/install/docker>) \-- kapsayıcılaştırılmış Gateway kurulumu
  * [Sandboxing](</tr/gateway/sandboxing>) \-- ajan sandbox yapılandırması
  * [Multi-Agent Sandbox and Tools](</tr/tools/multi-agent-sandbox-tools>) \-- ajan başına izolasyon


Was this useful?YesNo