---
title: Windows
source_url: https://docs.openclaw.ai/tr/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw hem **yerel Windows** hem de **WSL2** destekler. WSL2 daha kararlı yoldur ve tam deneyim için önerilir; CLI, Gateway ve araçlar Linux içinde tam uyumlulukla çalışır. Yerel Windows, aşağıda belirtilen bazı sınırlamalarla temel CLI ve Gateway kullanımı için çalışır.

Yerel Windows eşlikçi uygulamaları planlanmaktadır.

## WSL2 (önerilir)

  * [Başlarken](</tr/start/getting-started>) (WSL içinde kullanın)
  * [Kurulum ve güncellemeler](</tr/install/updating>)
  * Resmi WSL2 kılavuzu (Microsoft): <https://learn.microsoft.com/windows/wsl/install>


## Yerel Windows durumu

Yerel Windows CLI akışları gelişiyor, ancak WSL2 hâlâ önerilen yoldur.

Bugün yerel Windows üzerinde iyi çalışanlar:

  * `install.ps1` üzerinden web sitesi yükleyicisi
  * `openclaw --version`, `openclaw doctor` ve `openclaw plugins list --json` gibi yerel CLI kullanımı
  * aşağıdaki gibi gömülü local-agent/provider duman testi:

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

Mevcut sınırlamalar:

  * `openclaw onboard --non-interactive`, `--skip-health` geçmediğiniz sürece hâlâ erişilebilir bir yerel gateway bekler
  * `openclaw onboard --non-interactive --install-daemon` ve `openclaw gateway install` önce Windows Zamanlanmış Görevleri dener
  * Zamanlanmış Görev oluşturma reddedilirse, OpenClaw kullanıcı başına Başlangıç klasöründe bir oturum açma öğesine geri döner ve gateway’i hemen başlatır
  * `schtasks` kendisi takılır veya yanıt vermeyi bırakırsa, OpenClaw artık bu yolu hızlıca iptal eder ve sonsuza kadar takılı kalmak yerine geri dönüş yolunu kullanır
  * Zamanlanmış Görevler, daha iyi gözetici durumu sağladıkları için mevcut olduklarında hâlâ tercih edilir


Gateway hizmeti kurulumu olmadan yalnızca yerel CLI istiyorsanız şunlardan birini kullanın:

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

Yerel Windows üzerinde yönetilen başlangıç istiyorsanız:

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

Zamanlanmış Görev oluşturma engellenirse, geri dönüş hizmet modu yine de mevcut kullanıcının Başlangıç klasörü aracılığıyla oturum açıldıktan sonra otomatik başlar.

## Gateway

  * [Gateway çalıştırma kılavuzu](</tr/gateway>)
  * [Yapılandırma](</tr/gateway/configuration>)


## Gateway hizmeti kurulumu (CLI)

WSL2 içinde:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Veya:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Veya:

CodeCopy code
[code]
    openclaw configure
[/code]

İstendiğinde **Gateway hizmeti** seçeneğini belirleyin.

Onar/taşı:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Windows oturum açmadan önce Gateway otomatik başlatma

Ekransız kurulumlarda, Windows’ta kimse oturum açmasa bile tam önyükleme zincirinin çalıştığından emin olun.

### 1) Kullanıcı hizmetlerini oturum açmadan çalışır tutun

WSL içinde:

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) OpenClaw gateway kullanıcı hizmetini kurun

WSL içinde:

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) Windows önyüklemesinde WSL’yi otomatik başlatın

Yönetici olarak PowerShell’de:

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

`Ubuntu` değerini şuradan aldığınız dağıtım adınızla değiştirin:

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### Başlangıç zincirini doğrulayın

Yeniden başlatmadan sonra (Windows oturum açmadan önce), WSL’den kontrol edin:

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## Gelişmiş: WSL hizmetlerini LAN üzerinden açığa çıkarma (portproxy)

WSL’nin kendi sanal ağı vardır. Başka bir makinenin **WSL içinde** çalışan bir hizmete (SSH, yerel bir TTS sunucusu veya Gateway) erişmesi gerekiyorsa, bir Windows portunu mevcut WSL IP’sine yönlendirmeniz gerekir. WSL IP’si yeniden başlatmalardan sonra değişir, bu yüzden yönlendirme kuralını yenilemeniz gerekebilir.

Örnek (PowerShell’de **Yönetici olarak**):

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

Porta Windows Güvenlik Duvarı üzerinden izin verin (bir kez):

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

WSL yeniden başladıktan sonra portproxy’yi yenileyin:

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

Notlar:

  * Başka bir makineden SSH, **Windows ana makine IP’sini** hedefler (örnek: `ssh user@windows-host -p 2222`).
  * Uzak düğümler **erişilebilir** bir Gateway URL’sini işaret etmelidir (`127.0.0.1` değil); doğrulamak için `openclaw status --all` kullanın.
  * LAN erişimi için `listenaddress=0.0.0.0` kullanın; `127.0.0.1` yalnızca yerel tutar.
  * Bunun otomatik olmasını istiyorsanız, yenileme adımını oturum açıldığında çalıştıracak bir Zamanlanmış Görev kaydedin.


## Adım adım WSL2 kurulumu

### 1) WSL2 + Ubuntu kurun

PowerShell’i açın (Yönetici):

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

Windows isterse yeniden başlatın.

### 2) systemd’yi etkinleştirin (gateway kurulumu için gereklidir)

WSL terminalinizde:

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

Ardından PowerShell’den:

powershellCopy code
[code]
    wsl --shutdown
[/code]

Ubuntu’yu yeniden açın, ardından doğrulayın:

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) OpenClaw’u kurun (WSL içinde)

WSL içinde normal bir ilk kurulum için Linux Başlarken akışını izleyin:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

İlk katılım yerine kaynaktan geliştirme yapıyorsanız, [Kurulum](</tr/start/setup>) bölümündeki kaynak geliştirme döngüsünü kullanın:

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

Tam kılavuz: [Başlarken](</tr/start/getting-started>)

## Windows eşlikçi uygulaması

Henüz bir Windows eşlikçi uygulamamız yok. Bunun gerçekleşmesine yardımcı olmak isterseniz katkılar memnuniyetle karşılanır.

## Git ve GitHub bağlantısı (katkıda bulunanlar)

Bazı ağlar GitHub’a HTTPS erişimini engeller veya kısıtlar. `git clone` zaman aşımı veya bağlantı sıfırlamalarıyla başarısız olursa, başka bir ağ, VPN veya kuruluşunuzun sağladığı bir HTTP/HTTPS proxy deneyin.

`gh auth login`, tarayıcı cihaz akışı sırasında başarısız olursa (örneğin `github.com:443` erişiminde zaman aşımı), bunun yerine kişisel erişim belirteciyle kimlik doğrulayın:

  1. En az `repo` kapsamına (klasik PAT) veya eşdeğer ayrıntılı erişime sahip bir belirteç oluşturun.
  2. Geçerli oturum için PowerShell’de:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. `gh auth status` eksik `read:org` hakkında uyarı verirse, bu kapsamı içeren bir belirteç oluşturun ve değişkeni yeniden atayın:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` yalnızca `gh auth login` ile kimlik doğruladıysanız ve yenilenecek saklanmış kimlik bilgileriniz varsa geçerlidir (`GH_TOKEN` kullanırken değil).

Belirteçleri asla commit etmeyin veya issue’lara ya da pull request’lere yapıştırmayın.

## İlgili

  * [Kurulum özeti](</tr/install>)
  * [Platformlar](</tr/platforms>)


Was this useful?YesNo