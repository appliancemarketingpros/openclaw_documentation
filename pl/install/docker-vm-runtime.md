---
title: Środowisko uruchomieniowe maszyny wirtualnej Docker
source_url: https://docs.openclaw.ai/pl/install/docker-vm-runtime
scraped_at: 2026-05-25
---

Wspólne kroki uruchomieniowe dla instalacji Docker opartych na VM, takich jak GCP, Hetzner i podobni dostawcy VPS.

## Wypiecz wymagane pliki binarne w obrazie

Instalowanie plików binarnych wewnątrz działającego kontenera to pułapka. Wszystko, co zostanie zainstalowane w czasie działania, zostanie utracone po restarcie.

Wszystkie zewnętrzne pliki binarne wymagane przez Skills muszą być zainstalowane podczas budowania obrazu.

Poniższe przykłady pokazują tylko trzy typowe pliki binarne:

  * `gog` (z `gogcli`) do dostępu do Gmaila
  * `goplaces` dla Google Places
  * `wacli` dla WhatsApp


To są przykłady, a nie kompletna lista. Możesz zainstalować tyle plików binarnych, ile potrzeba, używając tego samego wzorca.

Jeśli później dodasz nowe Skills zależne od dodatkowych plików binarnych, musisz:

  1. Zaktualizować Dockerfile
  2. Przebudować obraz
  3. Uruchomić ponownie kontenery


**Przykładowy Dockerfile**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## Zbuduj i uruchom

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

Jeśli budowanie nie powiedzie się z `Killed` lub `exit code 137` podczas `pnpm install --frozen-lockfile`, VM ma za mało pamięci. Przed ponowną próbą użyj większej klasy maszyny.

Zweryfikuj pliki binarne:

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

Oczekiwane wyjście:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Zweryfikuj Gateway:

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

Oczekiwane wyjście:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## Co gdzie jest utrwalane

OpenClaw działa w Docker, ale Docker nie jest źródłem prawdy. Cały długotrwały stan musi przetrwać restarty, przebudowy i ponowne uruchomienia systemu.

Komponent | Lokalizacja | Mechanizm utrwalania | Uwagi  
---|---|---|---  
Konfiguracja Gateway | `/home/node/.openclaw/` | Montowanie woluminu hosta | Obejmuje `openclaw.json`, `.env`  
Profile uwierzytelniania modeli | `/home/node/.openclaw/agents/` | Montowanie woluminu hosta | `agents/<agentId>/agent/auth-profiles.json` (OAuth, klucze API)  
Klucz profilu uwierzytelniania | `/home/node/.config/openclaw/` | Montowanie woluminu hosta | Lokalny klucz szyfrowania dla materiału tokenów profilu uwierzytelniania OAuth  
Konfiguracje Skills | `/home/node/.openclaw/skills/` | Montowanie woluminu hosta | Stan na poziomie Skills  
Obszar roboczy agenta | `/home/node/.openclaw/workspace/` | Montowanie woluminu hosta | Kod i artefakty agenta  
Sesja WhatsApp | `/home/node/.openclaw/` | Montowanie woluminu hosta | Zachowuje logowanie QR  
Baza kluczy Gmaila | `/home/node/.openclaw/` | Wolumin hosta + hasło | Wymaga `GOG_KEYRING_PASSWORD`  
Pakiety Plugin | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | Montowanie woluminu hosta | Korzenie pobieralnych pakietów Plugin  
Zewnętrzne pliki binarne | `/usr/local/bin/` | Obraz Docker | Muszą być wypieczone podczas budowania  
Środowisko uruchomieniowe Node | System plików kontenera | Obraz Docker | Przebudowywane przy każdym budowaniu obrazu  
Pakiety systemu operacyjnego | System plików kontenera | Obraz Docker | Nie instaluj w czasie działania  
Kontener Docker | Efemeryczny | Możliwy do ponownego uruchomienia | Można go bezpiecznie zniszczyć  
  
## Aktualizacje

Aby zaktualizować OpenClaw na VM:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## Powiązane

  * [Docker](</pl/install/docker>)
  * [Podman](</pl/install/podman>)
  * [ClawDock](</pl/install/clawdock>)


Was this useful?YesNo