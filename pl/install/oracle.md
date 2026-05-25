---
title: Oracle Cloud
source_url: https://docs.openclaw.ai/pl/install/oracle
scraped_at: 2026-05-25
---

Uruchom trwały OpenClaw Gateway w warstwie ARM **Always Free** Oracle Cloud (do 4 OCPU, 24 GB RAM, 200 GB przestrzeni dyskowej) bez kosztów.

## Wymagania wstępne

  * Konto Oracle Cloud ([rejestracja](<https://www.oracle.com/cloud/free/>)) -- jeśli napotkasz problemy, zobacz [społecznościowy przewodnik rejestracji](<https://gist.github.com/rssnyder/51e3cfedd730e7dd5f4a816143b25dbd>)
  * Konto Tailscale (bezpłatne na [tailscale.com](<https://tailscale.com>))
  * Para kluczy SSH
  * Około 30 minut


## Konfiguracja

* ### Utwórz instancję OCI

  1. Zaloguj się do [Oracle Cloud Console](<https://cloud.oracle.com/>).
  2. Przejdź do **Compute > Instances > Create Instance**.
  3. Skonfiguruj: 
     * **Nazwa:** `openclaw`
     * **Obraz:** Ubuntu 24.04 (aarch64)
     * **Kształt:** `VM.Standard.A1.Flex` (Ampere ARM)
     * **OCPU:** 2 (lub do 4)
     * **Pamięć:** 12 GB (lub do 24 GB)
     * **Wolumin rozruchowy:** 50 GB (do 200 GB bezpłatnie)
     * **Klucz SSH:** Dodaj swój klucz publiczny
  4. Kliknij **Create** i zanotuj publiczny adres IP.


* ### Połącz się i zaktualizuj system

bashCopy code
[code]
    ssh ubuntu@YOUR_PUBLIC_IP sudo apt update && sudo apt upgrade -ysudo apt install -y build-essential
[/code]

`build-essential` jest wymagany do kompilacji ARM niektórych zależności.

* ### Skonfiguruj użytkownika i nazwę hosta

bashCopy code
[code]
    sudo hostnamectl set-hostname openclawsudo passwd ubuntusudo loginctl enable-linger ubuntu
[/code]

Włączenie linger utrzymuje usługi użytkownika po wylogowaniu.

* ### Zainstaluj Tailscale

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | shsudo tailscale up --ssh --hostname=openclaw
[/code]

Od teraz łącz się przez Tailscale: `ssh ubuntu@openclaw`.

* ### Zainstaluj OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bashsource ~/.bashrc
[/code]

Po wyświetleniu pytania „How do you want to hatch your bot?” wybierz **Do this later**.

* ### Skonfiguruj Gateway

Użyj uwierzytelniania tokenem z Tailscale Serve, aby zapewnić bezpieczny dostęp zdalny.

bashCopy code
[code]
    openclaw config set gateway.bind loopbackopenclaw config set gateway.auth.mode tokenopenclaw doctor --generate-gateway-tokenopenclaw config set gateway.tailscale.mode serveopenclaw config set gateway.trustedProxies '["127.0.0.1"]' systemctl --user restart openclaw-gateway.service
[/code]

`gateway.trustedProxies=["127.0.0.1"]` tutaj służy tylko do obsługi przekazywanego adresu IP/klienta lokalnego przez lokalne proxy Tailscale Serve. To **nie** jest `gateway.auth.mode: "trusted-proxy"`. Trasy podglądu różnic zachowują w tej konfiguracji tryb bezpiecznego zamknięcia: surowe żądania podglądu z `127.0.0.1` bez przekazywanych nagłówków proxy mogą zwrócić `Diff not found`. Użyj `mode=file` / `mode=both` dla załączników albo świadomie włącz zdalne podglądy i ustaw `plugins.entries.diffs.config.viewerBaseUrl` (lub przekaż proxy `baseUrl`), jeśli potrzebujesz udostępnialnych linków do podglądu.

* ### Zablokuj zabezpieczenia VCN

Zablokuj cały ruch z wyjątkiem Tailscale na brzegu sieci:

  1. Przejdź do **Networking > Virtual Cloud Networks** w konsoli OCI.
  2. Kliknij swoją VCN, a następnie **Security Lists > Default Security List**.
  3. **Usuń** wszystkie reguły ruchu przychodzącego poza `0.0.0.0/0 UDP 41641` (Tailscale).
  4. Zachowaj domyślne reguły ruchu wychodzącego (zezwól na cały ruch wychodzący).


Blokuje to SSH na porcie 22, HTTP, HTTPS i wszystko inne na brzegu sieci. Od tego momentu możesz łączyć się tylko przez Tailscale.

* ### Zweryfikuj

bashCopy code
[code]
    openclaw --versionsystemctl --user status openclaw-gateway.servicetailscale serve statuscurl http://localhost:18789
[/code]

Uzyskaj dostęp do interfejsu sterowania z dowolnego urządzenia w swojej sieci tailnet:

CodeCopy code
[code]
    https://openclaw.<tailnet-name>.ts.net/
[/code]

Zastąp `<tailnet-name>` nazwą swojej sieci tailnet (widoczną w `tailscale status`).

## Zweryfikuj stan zabezpieczeń

Przy zablokowanej VCN (otwarty tylko UDP 41641) i Gateway powiązanym z loopback, ruch publiczny jest blokowany na brzegu sieci, a dostęp administracyjny jest dostępny tylko w sieci tailnet. Eliminuje to potrzebę kilku tradycyjnych kroków utwardzania VPS:

Tradycyjny krok | Potrzebny? | Dlaczego  
---|---|---  
Zapora UFW | Nie | VCN blokuje ruch, zanim dotrze on do instancji.  
fail2ban | Nie | Port 22 jest zablokowany w VCN; brak powierzchni do ataków brute-force.  
Utwardzanie sshd | Nie | Tailscale SSH nie używa sshd.  
Wyłączenie logowania root | Nie | Tailscale uwierzytelnia przez tożsamość tailnet, nie użytkowników systemu.  
Uwierzytelnianie tylko kluczem SSH | Nie | To samo — tożsamość tailnet zastępuje systemowe klucze SSH.  
Utwardzanie IPv6 | Zwykle nie | Zależy od ustawień VCN/podsieci; sprawdź, co faktycznie jest przypisane/eksponowane.  
  
Nadal zalecane:

  * `chmod 700 ~/.openclaw`, aby ograniczyć uprawnienia plików poświadczeń.
  * `openclaw security audit` do sprawdzenia stanu zabezpieczeń specyficznego dla OpenClaw.
  * Regularne `sudo apt update && sudo apt upgrade` dla poprawek systemu operacyjnego.
  * Okresowo przeglądaj urządzenia w [konsoli administracyjnej Tailscale](<https://login.tailscale.com/admin>).


Szybkie polecenia weryfikacyjne:

bashCopy code
[code]
    # Confirm no public ports are listeningsudo ss -tlnp | grep -v '127.0.0.1\|::1' # Verify Tailscale SSH is activetailscale status | grep -q 'offers: ssh' && echo "Tailscale SSH active" # Optional: disable sshd entirely once Tailscale SSH is confirmed workingsudo systemctl disable --now ssh
[/code]

## Uwagi dotyczące ARM

Warstwa Always Free używa ARM (`aarch64`). Większość funkcji OpenClaw działa poprawnie; niewielka liczba natywnych plików binarnych wymaga kompilacji ARM:

  * Node.js, Telegram, WhatsApp (Baileys): czysty JavaScript, bez problemów.
  * Większość pakietów npm z kodem natywnym: dostępne są wstępnie zbudowane artefakty `linux-arm64`.
  * Opcjonalne pomocniki CLI (np. pliki binarne Go/Rust dostarczane przez Skills): przed instalacją sprawdź, czy istnieje wydanie `aarch64` / `linux-arm64`.


Zweryfikuj architekturę za pomocą `uname -m` (powinno wypisać `aarch64`). W przypadku plików binarnych bez kompilacji ARM zainstaluj je ze źródeł albo je pomiń.

## Trwałość i kopie zapasowe

Stan OpenClaw znajduje się w:

  * `~/.openclaw/` — `openclaw.json`, per-agent `auth-profiles.json`, stan kanałów/dostawców i dane sesji.
  * `~/.openclaw/workspace/` — przestrzeń robocza agenta ([SOUL.md](<http://SOUL.md>), pamięć, artefakty).


Przetrwają one ponowne uruchomienia. Aby utworzyć przenośną migawkę:

bashCopy code
[code]
    openclaw backup create
[/code]

## Rozwiązanie awaryjne: tunel SSH

Jeśli Tailscale Serve nie działa, użyj tunelu SSH z komputera lokalnego:

bashCopy code
[code]
    ssh -L 18789:127.0.0.1:18789 ubuntu@openclaw
[/code]

Następnie otwórz `http://localhost:18789`.

## Rozwiązywanie problemów

**Utworzenie instancji kończy się błędem („Out of capacity”)** \-- Instancje ARM w warstwie bezpłatnej są popularne. Spróbuj użyć innej domeny dostępności albo ponów próbę poza godzinami szczytu.

**Tailscale nie łączy się** \-- Uruchom `sudo tailscale up --ssh --hostname=openclaw --reset`, aby ponownie się uwierzytelnić.

**Gateway nie uruchamia się** \-- Uruchom `openclaw doctor --non-interactive` i sprawdź dzienniki za pomocą `journalctl --user -u openclaw-gateway.service -n 50`.

**Problemy z plikami binarnymi ARM** \-- Większość pakietów npm działa na ARM64. W przypadku natywnych plików binarnych szukaj wydań `linux-arm64` lub `aarch64`. Zweryfikuj architekturę za pomocą `uname -m`.

## Następne kroki

  * [Kanały](</pl/channels>) \-- połącz Telegram, WhatsApp, Discord i więcej
  * [Konfiguracja Gateway](</pl/gateway/configuration>) \-- wszystkie opcje konfiguracji
  * [Aktualizowanie](</pl/install/updating>) \-- utrzymuj OpenClaw w aktualnej wersji


## Powiązane

  * [Omówienie instalacji](</pl/install>)
  * [GCP](</pl/install/gcp>)
  * [Hosting VPS](</pl/vps>)


Was this useful?YesNo