---
title: Uzak Gateway kurulumu
source_url: https://docs.openclaw.ai/tr/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> Bu içerik [Uzaktan Erişim](</tr/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>) içine birleştirildi. Güncel kılavuz için o sayfaya bakın.

# OpenClaw.app’i Uzak Gateway ile Çalıştırma

OpenClaw.app, uzak bir Gateway’e bağlanmak için SSH tünelleme kullanır. Bu kılavuz, bunu nasıl kuracağınızı gösterir.

## Genel bakış
[code] 
    flowchart TB
        subgraph Client["Client Machine"]
            direction TB
            A["OpenClaw.app"]
            B["ws://127.0.0.1:18789\n(local port)"]
            T["SSH Tunnel"]
    
            A --> B
            B --> T
        end
        subgraph Remote["Remote Machine"]
            direction TB
            C["Gateway WebSocket"]
            D["ws://127.0.0.1:18789"]
    
            C --> D
        end
        T --> C
[/code]

## Hızlı kurulum

### Adım 1: SSH Yapılandırması Ekleyin

`~/.ssh/config` dosyasını düzenleyin ve şunu ekleyin:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

`&lt;REMOTE_IP&gt;` ve `&lt;REMOTE_USER&gt;` değerlerini kendi değerlerinizle değiştirin.

### Adım 2: SSH Anahtarını Kopyalayın

Açık anahtarınızı uzak makineye kopyalayın (parolayı bir kez girin):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Adım 3: Uzak Gateway Kimlik Doğrulamasını Yapılandırın

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Uzak Gateway’iniz parola kimlik doğrulaması kullanıyorsa bunun yerine `gateway.remote.password` kullanın. `OPENCLAW_GATEWAY_TOKEN`, kabuk düzeyinde geçersiz kılma olarak hâlâ geçerlidir; ancak kalıcı uzak istemci kurulumu `gateway.remote.token` / `gateway.remote.password` şeklindedir.

### Adım 4: SSH Tünelini Başlatın

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Adım 5: OpenClaw.app’i Yeniden Başlatın

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

Uygulama artık SSH tüneli üzerinden uzak Gateway’e bağlanacaktır.

* * *

## Oturum Açıldığında Tüneli Otomatik Başlatma

SSH tünelinin oturum açtığınızda otomatik olarak başlaması için bir başlatma aracısı oluşturun.

### PLIST Dosyasını Oluşturun

Bunu `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist` olarak kaydedin:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### Başlatma Aracısını Yükleyin

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Tünel artık:

  * Oturum açtığınızda otomatik olarak başlar
  * Çökerse yeniden başlatılır
  * Arka planda çalışmaya devam eder


Eski sürüm notu: varsa kalan `com.openclaw.ssh-tunnel` LaunchAgent öğesini kaldırın.

* * *

## Sorun giderme

**Tünelin çalışıp çalışmadığını kontrol edin:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**Tüneli yeniden başlatın:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**Tüneli durdurun:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Nasıl çalışır

Bileşen | Ne Yapar  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Yerel 18789 bağlantı noktasını uzak 18789 bağlantı noktasına iletir  
`ssh -N` | Uzak komut çalıştırmadan SSH kullanır (yalnızca bağlantı noktası iletme)  
`KeepAlive` | Tünel çökerse otomatik olarak yeniden başlatır  
`RunAtLoad` | Aracı yüklendiğinde tüneli başlatır  
  
OpenClaw.app, istemci makinenizde `ws://127.0.0.1:18789` adresine bağlanır. SSH tüneli, bu bağlantıyı Gateway’in çalıştığı uzak makinedeki 18789 bağlantı noktasına iletir.

## İlgili

  * [Uzaktan erişim](</tr/gateway/remote>)
  * [Tailscale](</tr/gateway/tailscale>)


Was this useful?YesNo