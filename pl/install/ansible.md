---
title: Ansible
source_url: https://docs.openclaw.ai/pl/install/ansible
scraped_at: 2026-05-25
---

Wdróż OpenClaw na serwerach produkcyjnych za pomocą **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- zautomatyzowanego instalatora z architekturą stawiającą bezpieczeństwo na pierwszym miejscu.

## Wymagania wstępne

Wymaganie | Szczegóły  
---|---  
**OS** | Debian 11+ lub Ubuntu 20.04+  
**Dostęp** | Uprawnienia root lub sudo  
**Sieć** | Połączenie z internetem do instalacji pakietów  
**Ansible** | 2.14+ (instalowany automatycznie przez skrypt szybkiego startu)  
  
## Co otrzymujesz

  * **Bezpieczeństwo od zapory sieciowej** \-- izolacja UFW + Docker (dostępne tylko SSH + Tailscale)
  * **Tailscale VPN** \-- bezpieczny dostęp zdalny bez publicznego wystawiania usług
  * **Docker** \-- izolowane kontenery piaskownicy, powiązania tylko z localhost
  * **Obrona w głąb** \-- 4-warstwowa architektura bezpieczeństwa
  * **Integracja z systemd** \-- automatyczne uruchamianie przy starcie z utwardzeniem
  * **Konfiguracja jednym poleceniem** \-- pełne wdrożenie w kilka minut


## Szybki start

Instalacja jednym poleceniem:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Co zostanie zainstalowane

Playbook Ansible instaluje i konfiguruje:

  1. **Tailscale** \-- mesh VPN do bezpiecznego dostępu zdalnego
  2. **Zapora UFW** \-- tylko porty SSH + Tailscale
  3. **Docker CE + Compose V2** \-- dla domyślnego backendu piaskownicy agenta
  4. **Node.js 24 + pnpm** \-- zależności środowiska uruchomieniowego (Node 22 LTS, obecnie `22.16+`, pozostaje obsługiwany)
  5. **OpenClaw** \-- uruchamiany na hoście, nie w kontenerze
  6. **Usługa systemd** \-- automatyczny start z utwardzeniem bezpieczeństwa


## Konfiguracja po instalacji

* ### Przełącz się na użytkownika openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Uruchom kreatora wdrażania

Skrypt poinstalacyjny przeprowadzi Cię przez konfigurację ustawień OpenClaw.

* ### Połącz dostawców komunikacji

Zaloguj się do WhatsApp, Telegram, Discord lub Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Zweryfikuj instalację

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Połącz się z Tailscale

Dołącz do swojej siatki VPN, aby uzyskać bezpieczny dostęp zdalny.

### Szybkie polecenia

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## Architektura bezpieczeństwa

Wdrożenie używa 4-warstwowego modelu obrony:

  1. **Zapora sieciowa (UFW)** \-- publicznie wystawione są tylko SSH (22) + Tailscale (41641/udp)
  2. **VPN (Tailscale)** \-- Gateway dostępny tylko przez siatkę VPN
  3. **Izolacja Docker** \-- łańcuch iptables DOCKER-USER zapobiega zewnętrznemu wystawianiu portów
  4. **Utwardzenie systemd** \-- NoNewPrivileges, PrivateTmp, użytkownik nieuprzywilejowany


Aby zweryfikować zewnętrzną powierzchnię ataku:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Otwarty powinien być tylko port 22 (SSH). Wszystkie pozostałe usługi (Gateway, Docker) są zablokowane.

Docker jest instalowany dla piaskownic agentów (izolowane wykonywanie narzędzi), a nie do uruchamiania samego Gateway. Konfigurację piaskownicy znajdziesz w [Piaskownica i narzędzia wielu agentów](</pl/tools/multi-agent-sandbox-tools>).

## Instalacja ręczna

Jeśli wolisz ręcznie kontrolować automatyzację:

* ### Zainstaluj wymagania wstępne

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Sklonuj repozytorium

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Zainstaluj kolekcje Ansible

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Uruchom playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Alternatywnie uruchom bezpośrednio, a następnie ręcznie wykonaj skrypt konfiguracji:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## Aktualizowanie

Instalator Ansible konfiguruje OpenClaw do ręcznych aktualizacji. Standardowy przepływ aktualizacji znajdziesz w [Aktualizowanie](</pl/install/updating>).

Aby ponownie uruchomić playbook Ansible (na przykład w celu zmian konfiguracji):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Jest to idempotentne i można bezpiecznie uruchamiać wielokrotnie.

## Rozwiązywanie problemów

Zapora sieciowa blokuje moje połączenie

  * Najpierw upewnij się, że masz dostęp przez Tailscale VPN
  * Dostęp SSH (port 22) jest zawsze dozwolony
  * Gateway jest zgodnie z projektem dostępny tylko przez Tailscale

Usługa nie uruchamia się bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Problemy z piaskownicą Docker bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Logowanie dostawcy nie działa

Upewnij się, że działasz jako użytkownik `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Konfiguracja zaawansowana

Szczegółową architekturę bezpieczeństwa i rozwiązywanie problemów znajdziesz w repozytorium openclaw-ansible:

  * [Architektura bezpieczeństwa](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Szczegóły techniczne](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Przewodnik rozwiązywania problemów](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Powiązane

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- pełny przewodnik wdrożenia
  * [Docker](</pl/install/docker>) \-- konfiguracja konteneryzowanego Gateway
  * [Piaskownica](</pl/gateway/sandboxing>) \-- konfiguracja piaskownicy agenta
  * [Piaskownica i narzędzia wielu agentów](</pl/tools/multi-agent-sandbox-tools>) \-- izolacja per agent


Was this useful?YesNo