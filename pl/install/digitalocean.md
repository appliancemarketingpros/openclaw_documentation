---
title: DigitalOcean
source_url: https://docs.openclaw.ai/pl/install/digitalocean
scraped_at: 2026-05-25
---

Uruchom trwały OpenClaw Gateway na DigitalOcean Droplet (~6 USD/miesiąc za plan Basic 1 GB).

DigitalOcean to najprostsza płatna ścieżka VPS. Jeśli wolisz tańsze lub darmowe opcje:

  * [Hetzner](</pl/install/hetzner>) — 3,79 €/mies., więcej rdzeni/RAM za dolara.
  * [Oracle Cloud](</pl/install/oracle>) — Always Free ARM (do 4 OCPU, 24 GB RAM), ale rejestracja bywa problematyczna i dostępny jest tylko ARM.


## Wymagania wstępne

  * Konto DigitalOcean ([rejestracja](<https://cloud.digitalocean.com/registrations/new>))
  * Para kluczy SSH (albo gotowość do użycia uwierzytelniania hasłem)
  * Około 20 minut


## Konfiguracja

* ### Utwórz Droplet

  1. Zaloguj się do [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Kliknij **Create > Droplets**.
  3. Wybierz: 
     * **Region:** Najbliższy tobie
     * **Image:** Ubuntu 24.04 LTS
     * **Size:** Basic, Regular, 1 vCPU / 1 GB RAM / 25 GB SSD
     * **Authentication:** Klucz SSH (zalecane) albo hasło
  4. Kliknij **Create Droplet** i zanotuj adres IP.


* ### Połącz się i zainstaluj

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Używaj powłoki root tylko do rozruchowej konfiguracji systemu. Uruchamiaj polecenia OpenClaw jako użytkownik `openclaw` bez uprawnień root, aby stan znajdował się w `/home/openclaw/.openclaw/`, a Gateway został zainstalowany jako usługa systemd tego użytkownika.

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Kreator przeprowadzi cię przez uwierzytelnianie modelu, konfigurację kanału, generowanie tokena gateway oraz instalację demona (systemd).

* ### Dodaj swap (zalecane dla Dropletów 1 GB)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Zweryfikuj gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Uzyskaj dostęp do interfejsu Control UI

Gateway domyślnie wiąże się z loopback. Wybierz jedną z tych opcji.

**Opcja A: tunel SSH (najprostsze)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Następnie otwórz `http://localhost:18789`.

**Opcja B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Następnie otwórz `https://<magicdns>/` z dowolnego urządzenia w swoim tailnet.

Tailscale Serve uwierzytelnia ruch Control UI i WebSocket za pomocą nagłówków tożsamości tailnet, co zakłada, że sam host gateway jest zaufany. Punkty końcowe HTTP API używają normalnego trybu uwierzytelniania gateway (token/hasło) niezależnie od tego. Aby wymagać jawnych poświadczeń współdzielonego sekretu przez Serve, ustaw `gateway.auth.allowTailscale: false` i użyj `gateway.auth.mode: "token"` albo `"password"`.

**Opcja C: wiązanie tailnet (bez Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Następnie otwórz `http://<tailscale-ip>:18789` (wymagany token).

## Trwałość i kopie zapasowe

Stan OpenClaw znajduje się w:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` dla poszczególnych agentów, stan kanałów/dostawców oraz dane sesji.
  * `~/.openclaw/workspace/` — przestrzeń robocza agenta ([SOUL.md](<http://SOUL.md>), pamięć, artefakty).


Te dane przetrwają ponowne uruchomienia Dropleta. Aby utworzyć przenośną migawkę:

bashCopy code
[code]
    openclaw backup create
[/code]

Migawki DigitalOcean obejmują cały Droplet; `openclaw backup create` jest przenośne między hostami.

## Wskazówki dla 1 GB RAM

Droplet za 6 USD ma tylko 1 GB RAM. Aby wszystko działało płynnie:

  * Upewnij się, że powyższy krok swap znajduje się w `/etc/fstab`, aby przetrwał ponowne uruchomienia.
  * Preferuj modele oparte na API (Claude, GPT) zamiast lokalnych — lokalne wnioskowanie LLM nie mieści się w 1 GB.
  * Ustaw `agents.defaults.model.primary` na mniejszy model, jeśli przy dużych promptach występują błędy OOM.
  * Monitoruj za pomocą `free -h` i `htop`.


## Rozwiązywanie problemów

**Gateway nie uruchamia się** \-- Uruchom `openclaw doctor --non-interactive` i sprawdź logi za pomocą `journalctl --user -u openclaw-gateway.service -n 50`.

**Port jest już używany** \-- Uruchom `lsof -i :18789`, aby znaleźć proces, a następnie go zatrzymaj.

**Brak pamięci** \-- Sprawdź, czy swap jest aktywny, za pomocą `free -h`. Jeśli nadal występuje OOM, użyj modeli opartych na API (Claude, GPT) zamiast modeli lokalnych albo przejdź na Droplet 2 GB.

## Następne kroki

  * [Kanały](</pl/channels>) \-- połącz Telegram, WhatsApp, Discord i inne
  * [Konfiguracja gateway](</pl/gateway/configuration>) \-- wszystkie opcje konfiguracji
  * [Aktualizowanie](</pl/install/updating>) \-- utrzymuj OpenClaw w aktualnej wersji


## Powiązane

  * [Przegląd instalacji](</pl/install>)
  * [Fly.io](</pl/install/fly>)
  * [Hetzner](</pl/install/hetzner>)
  * [Hosting VPS](</pl/vps>)


Was this useful?YesNo