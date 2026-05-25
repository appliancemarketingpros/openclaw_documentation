---
title: Docker VM çalışma zamanı
source_url: https://docs.openclaw.ai/tr/install/docker-vm-runtime
scraped_at: 2026-05-25
---

GCP, Hetzner ve benzeri VPS sağlayıcıları gibi VM tabanlı Docker kurulumları için paylaşılan çalışma zamanı adımları.

## Gerekli ikili dosyaları imaja dahil edin

Çalışan bir konteynerin içine ikili dosya kurmak tuzaktır. Çalışma zamanında kurulan her şey yeniden başlatmada kaybolur.

Skills tarafından gereken tüm harici ikili dosyalar imaj derleme zamanında kurulmalıdır.

Aşağıdaki örnekler yalnızca üç yaygın ikili dosyayı gösterir:

  * Gmail erişimi için `gog` (`gogcli` kaynağından)
  * Google Places için `goplaces`
  * WhatsApp için `wacli`


Bunlar örnektir, eksiksiz bir liste değildir. Aynı deseni kullanarak gerektiği kadar çok ikili dosya kurabilirsiniz.

Daha sonra ek ikili dosyalara bağımlı yeni Skills eklerseniz şunları yapmanız gerekir:

  1. Dockerfile'ı güncelleyin
  2. İmajı yeniden derleyin
  3. Konteynerleri yeniden başlatın


**Örnek Dockerfile**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## Derleyin ve başlatın

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

Derleme `pnpm install --frozen-lockfile` sırasında `Killed` veya `exit code 137` ile başarısız olursa VM'nin belleği yetersizdir. Yeniden denemeden önce daha büyük bir makine sınıfı kullanın.

İkili dosyaları doğrulayın:

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

Beklenen çıktı:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Gateway'i doğrulayın:

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

Beklenen çıktı:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## Ne nerede kalıcı olur

OpenClaw Docker içinde çalışır, ancak Docker doğruluk kaynağı değildir. Tüm uzun ömürlü durum yeniden başlatmalardan, yeniden derlemelerden ve yeniden başlatılan makinelerden sonra korunmalıdır.

Bileşen | Konum | Kalıcılık mekanizması | Notlar  
---|---|---|---  
Gateway yapılandırması | `/home/node/.openclaw/` | Ana makine volume mount | `openclaw.json`, `.env` içerir  
Model kimlik doğrulama profilleri | `/home/node/.openclaw/agents/` | Ana makine volume mount | `agents/<agentId>/agent/auth-profiles.json` (OAuth, API anahtarları)  
Kimlik doğrulama profili anahtarı | `/home/node/.config/openclaw/` | Ana makine volume mount | OAuth kimlik doğrulama profili token materyali için yerel şifreleme anahtarı  
Skill yapılandırmaları | `/home/node/.openclaw/skills/` | Ana makine volume mount | Skill düzeyinde durum  
Agent çalışma alanı | `/home/node/.openclaw/workspace/` | Ana makine volume mount | Kod ve agent yapıtları  
WhatsApp oturumu | `/home/node/.openclaw/` | Ana makine volume mount | QR oturum açmayı korur  
Gmail anahtarlığı | `/home/node/.openclaw/` | Ana makine volume + parola | `GOG_KEYRING_PASSWORD` gerektirir  
Plugin paketleri | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | Ana makine volume mount | İndirilebilir plugin paketi kökleri  
Harici ikili dosyalar | `/usr/local/bin/` | Docker imajı | Derleme zamanında imaja dahil edilmelidir  
Node çalışma zamanı | Konteyner dosya sistemi | Docker imajı | Her imaj derlemesinde yeniden derlenir  
OS paketleri | Konteyner dosya sistemi | Docker imajı | Çalışma zamanında kurmayın  
Docker konteyneri | Geçici | Yeniden başlatılabilir | Yok etmek güvenlidir  
  
## Güncellemeler

VM üzerindeki OpenClaw'ı güncellemek için:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## İlgili

  * [Docker](</tr/install/docker>)
  * [Podman](</tr/install/podman>)
  * [ClawDock](</tr/install/clawdock>)


Was this useful?YesNo