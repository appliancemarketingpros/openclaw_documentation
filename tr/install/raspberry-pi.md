---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/tr/install/raspberry-pi
scraped_at: 2026-05-25
---

Kalıcı, her zaman açık bir OpenClaw Gateway'i Raspberry Pi üzerinde çalıştırın. Pi yalnızca gateway olduğu için (modeller API üzerinden bulutta çalışır), mütevazı bir Pi bile iş yükünü rahatça karşılar; tipik donanım maliyeti **tek seferlik $35–80** aralığındadır, aylık ücret yoktur.

## Donanım uyumluluğu

Pi modeli | RAM | Çalışır mı? | Notlar  
---|---|---|---  
Pi 5 | 4/8 GB | En iyi | En hızlı, önerilir.  
Pi 4 | 4 GB | İyi | Çoğu kullanıcı için en uygun nokta.  
Pi 4 | 2 GB | Uygun | Swap ekleyin.  
Pi 4 | 1 GB | Sınırlı | Swap ve minimal yapılandırmayla mümkün.  
Pi 3B+ | 1 GB | Yavaş | Çalışır ama ağırdır.  
Pi Zero 2 W | 512 MB | Hayır | Önerilmez.  
  
**Minimum:** 1 GB RAM, 1 çekirdek, 500 MB boş disk, 64 bit işletim sistemi. **Önerilen:** 2 GB+ RAM, 16 GB+ SD kart (veya USB SSD), Ethernet.

## Ön koşullar

  * 2 GB+ RAM'e sahip Raspberry Pi 4 veya 5 (4 GB önerilir)
  * MicroSD kart (16 GB+) veya USB SSD (daha iyi performans)
  * Resmi Pi güç kaynağı
  * Ağ bağlantısı (Ethernet veya WiFi)
  * 64 bit Raspberry Pi OS (gerekli -- 32 bit kullanmayın)
  * Yaklaşık 30 dakika


## Kurulum

* ### İşletim sistemini yazdırın

Masaüstü gerekmeyen başsız bir sunucu için **Raspberry Pi OS Lite (64-bit)** kullanın.

  1. [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>) uygulamasını indirin.
  2. İşletim sistemi seçin: **Raspberry Pi OS Lite (64-bit)**.
  3. Ayarlar iletişim kutusunda önceden yapılandırın: 
     * Ana makine adı: `gateway-host`
     * SSH'yi etkinleştirin
     * Kullanıcı adı ve parola belirleyin
     * WiFi'yi yapılandırın (Ethernet kullanmıyorsanız)
  4. SD kartınıza veya USB sürücünüze yazdırın, takın ve Pi'yi başlatın.


* ### SSH ile bağlanın

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### Sistemi güncelleyin

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### Node.js 24'ü kurun

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### Swap ekleyin (2 GB veya daha az için önemli)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### OpenClaw'u kurun

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### İlk kurulumu çalıştırın

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Sihirbazı izleyin. Başsız cihazlar için OAuth yerine API anahtarları önerilir. Başlamak için en kolay kanal Telegram'dır.

* ### Doğrulayın

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Control UI'ye erişin

Bilgisayarınızda, Pi'den bir pano URL'si alın:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

Ardından başka bir terminalde SSH tüneli oluşturun:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

Yazdırılan URL'yi yerel tarayıcınızda açın. Her zaman açık uzaktan erişim için [Tailscale entegrasyonu](</tr/gateway/tailscale>) bölümüne bakın.

## Performans ipuçları

**USB SSD kullanın** \-- SD kartlar yavaştır ve yıpranır. USB SSD performansı ciddi biçimde artırır. [Pi USB önyükleme kılavuzuna](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>) bakın.

**Modül derleme önbelleğini etkinleştirin** \-- Daha düşük güçlü Pi ana makinelerinde tekrarlanan CLI çağrılarını hızlandırır:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**Bellek kullanımını azaltın** \-- Başsız kurulumlar için GPU belleğini serbest bırakın ve kullanılmayan hizmetleri devre dışı bırakın:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**Kararlı yeniden başlatmalar için systemd drop-in** \-- Bu Pi çoğunlukla OpenClaw çalıştırıyorsa bir hizmet drop-in'i ekleyin:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Ardından `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service` çalıştırın. Başsız bir Pi'de, kullanıcı hizmetinin oturum kapatıldıktan sonra da çalışmayı sürdürmesi için lingering'i bir kez etkinleştirin: `sudo loginctl enable-linger "$(whoami)"`.

## Önerilen model kurulumu

Pi yalnızca gateway çalıştırdığı için bulutta barındırılan API modellerini kullanın:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

Yerel LLM'leri Pi üzerinde çalıştırmayın; küçük modeller bile kullanışlı olamayacak kadar yavaştır. Model işini Claude veya GPT'ye bırakın.

## ARM ikili dosya notları

Çoğu OpenClaw özelliği ARM64 üzerinde değişiklik gerektirmeden çalışır (Node.js, Telegram, WhatsApp/Baileys, Chromium). Zaman zaman ARM derlemeleri olmayan ikili dosyalar genellikle Skills tarafından gönderilen isteğe bağlı Go/Rust CLI araçlarıdır. Kaynaktan derlemeye geçmeden önce eksik bir ikili dosyanın yayın sayfasında `linux-arm64` / `aarch64` yapıtlarını doğrulayın.

## Kalıcılık ve yedeklemeler

OpenClaw durumu şunların altında bulunur:

  * `~/.openclaw/` — `openclaw.json`, ajan başına `auth-profiles.json`, kanal/sağlayıcı durumu, oturumlar.
  * `~/.openclaw/workspace/` — ajan çalışma alanı ([SOUL.md](<http://SOUL.md>), bellek, yapıtlar).


Bunlar yeniden başlatmalardan etkilenmez. Taşınabilir bir anlık görüntü almak için:

bashCopy code
[code]
    openclaw backup create
[/code]

Bunları SSD üzerinde tutarsanız, SD karta kıyasla hem performans hem de ömür iyileşir.

## Sorun giderme

**Bellek yetersiz** \-- Swap'ın etkin olduğunu `free -h` ile doğrulayın. Kullanılmayan hizmetleri devre dışı bırakın (`sudo systemctl disable cups bluetooth avahi-daemon`). Yalnızca API tabanlı modeller kullanın.

**Yavaş performans** \-- SD kart yerine USB SSD kullanın. CPU kısıtlamasını `vcgencmd get_throttled` ile kontrol edin (`0x0` döndürmelidir).

**Hizmet başlamıyor** \-- Günlükleri `journalctl --user -u openclaw-gateway.service --no-pager -n 100` ile kontrol edin ve `openclaw doctor --non-interactive` çalıştırın. Bu başsız bir Pi ise lingering'in etkin olduğunu da doğrulayın: `sudo loginctl enable-linger "$(whoami)"`.

**ARM ikili dosya sorunları** \-- Bir skill "exec format error" ile başarısız olursa ikili dosyanın ARM64 derlemesi olup olmadığını kontrol edin. Mimarileri `uname -m` ile doğrulayın (`aarch64` göstermelidir).

**WiFi kopuyor** \-- WiFi güç yönetimini devre dışı bırakın: `sudo iwconfig wlan0 power off`.

## Sonraki adımlar

  * [Kanallar](</tr/channels>) \-- Telegram, WhatsApp, Discord ve daha fazlasını bağlayın
  * [Gateway yapılandırması](</tr/gateway/configuration>) \-- tüm yapılandırma seçenekleri
  * [Güncelleme](</tr/install/updating>) \-- OpenClaw'u güncel tutun


## İlgili

  * [Kurulum genel bakışı](</tr/install>)
  * [Linux sunucusu](</tr/vps>)
  * [Platformlar](</tr/platforms>)


Was this useful?YesNo