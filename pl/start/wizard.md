---
title: Wprowadzenie (CLI)
source_url: https://docs.openclaw.ai/pl/start/wizard
scraped_at: 2026-05-25
---

CLI onboarding to **zalecany** sposób konfigurowania OpenClaw w systemie macOS, Linux lub Windows (przez WSL2; zdecydowanie zalecane). Konfiguruje lokalny Gateway albo połączenie ze zdalnym Gateway, a także kanały, Skills i domyślne ustawienia obszaru roboczego w jednym prowadzonym procesie.

bashCopy code
[code]
    openclaw onboard
[/code]

Aby później zmienić konfigurację:

bashCopy code
[code]
    openclaw configureopenclaw agents add <name>
[/code]

## QuickStart a Advanced

Onboarding zaczyna się od wyboru **QuickStart** (wartości domyślne) albo **Advanced** (pełna kontrola).

### QuickStart (wartości domyślne)

  * Lokalny Gateway (loopback)
  * Domyślny obszar roboczy (albo istniejący obszar roboczy)
  * Port Gateway **18789**
  * Uwierzytelnianie Gateway **Token** (generowane automatycznie, nawet przy loopback)
  * Domyślna polityka narzędzi dla nowych konfiguracji lokalnych: `tools.profile: "coding"` (istniejący jawny profil zostaje zachowany)
  * Domyślna izolacja DM: lokalny onboarding zapisuje `session.dmScope: "per-channel-peer"`, gdy nie jest ustawione. Szczegóły: [Dokumentacja konfiguracji CLI](</pl/start/wizard-cli-reference#outputs-and-internals>)
  * Ekspozycja Tailscale **Wyłączona**
  * Wiadomości prywatne Telegram + WhatsApp domyślnie używają **listy dozwolonych** (zostaniesz poproszony o numer telefonu)


### Advanced (pełna kontrola)

  * Udostępnia każdy krok (tryb, obszar roboczy, Gateway, kanały, demon, Skills).


## Co konfiguruje onboarding

**Tryb lokalny (domyślny)** prowadzi przez te kroki:

  1. **Model/uwierzytelnianie** — wybierz dowolnego obsługiwanego dostawcę lub przepływ uwierzytelniania (klucz API, OAuth albo ręczne uwierzytelnianie specyficzne dla dostawcy), w tym dostawcę niestandardowego (zgodnego z OpenAI, zgodnego z Anthropic albo automatycznie wykrywanego jako nieznany). Wybierz model domyślny. Uwaga dotycząca bezpieczeństwa: jeśli ten agent będzie uruchamiał narzędzia albo przetwarzał zawartość Webhook/hooks, wybierz najsilniejszy dostępny model najnowszej generacji i utrzymuj restrykcyjną politykę narzędzi. Słabsze/starsze poziomy łatwiej poddać prompt injection. Dla uruchomień nieinteraktywnych `--secret-input-mode ref` zapisuje odwołania oparte na zmiennych środowiskowych w profilach uwierzytelniania zamiast jawnych wartości kluczy API. W nieinteraktywnym trybie `ref` zmienna środowiskowa dostawcy musi być ustawiona; przekazanie flag klucza inline bez tej zmiennej środowiskowej szybko kończy się błędem. W uruchomieniach interaktywnych wybór trybu odwołania do sekretu pozwala wskazać zmienną środowiskową albo skonfigurowane odwołanie dostawcy (`file` lub `exec`), z szybką walidacją wstępną przed zapisaniem. Dla Anthropic interaktywny onboarding/configure oferuje **Anthropic Claude CLI** jako preferowaną ścieżkę lokalną oraz **klucz API Anthropic** jako zalecaną ścieżkę produkcyjną. Anthropic setup-token pozostaje też dostępny jako obsługiwana ścieżka uwierzytelniania tokenem.
  2. **Obszar roboczy** — lokalizacja plików agenta (domyślnie `~/.openclaw/workspace`). Tworzy początkowe pliki bootstrap.
  3. **Gateway** — port, adres powiązania, tryb uwierzytelniania, ekspozycja Tailscale. W interaktywnym trybie tokena wybierz domyślne przechowywanie tokena jako tekst jawny albo włącz SecretRef. Nieinteraktywna ścieżka SecretRef dla tokena: `--gateway-token-ref-env &lt;ENV_VAR&gt;`.
  4. **Kanały** — wbudowane i dołączone kanały czatu, takie jak iMessage, Discord, Feishu, Google Chat, Mattermost, Microsoft Teams, QQ Bot, Signal, Slack, Telegram, WhatsApp i inne.
  5. **Demon** — instaluje LaunchAgent (macOS), jednostkę użytkownika systemd (Linux/WSL2) albo natywne Zaplanowane zadanie Windows z awaryjną opcją folderu autostartu dla użytkownika. Jeśli uwierzytelnianie tokenem wymaga tokena, a `gateway.auth.token` jest zarządzane przez SecretRef, instalacja demona waliduje go, ale nie utrwala rozwiązanego tokena w metadanych środowiska usługi nadzorcy. Jeśli uwierzytelnianie tokenem wymaga tokena, a skonfigurowany token SecretRef nie został rozwiązany, instalacja demona jest blokowana z praktycznymi wskazówkami. Jeśli skonfigurowane są zarówno `gateway.auth.token`, jak i `gateway.auth.password`, a `gateway.auth.mode` nie jest ustawione, instalacja demona jest blokowana, dopóki tryb nie zostanie ustawiony jawnie.
  6. **Kontrola kondycji** — uruchamia Gateway i sprawdza, czy działa.
  7. **Skills** — instaluje zalecane Skills i opcjonalne zależności.


**Tryb zdalny** konfiguruje tylko lokalnego klienta do łączenia się z Gateway w innym miejscu. Nie instaluje ani nie zmienia niczego na zdalnym hoście.

## Dodaj kolejnego agenta

Użyj `openclaw agents add <name>`, aby utworzyć oddzielnego agenta z własnym obszarem roboczym, sesjami i profilami uwierzytelniania. Uruchomienie bez `--workspace` rozpoczyna onboarding.

Co ustawia:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Uwagi:

  * Domyślne obszary robocze używają wzorca `~/.openclaw/workspace-<agentId>`.
  * Dodaj `bindings`, aby kierować przychodzące wiadomości (onboarding może to zrobić).
  * Flagi nieinteraktywne: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Pełna dokumentacja

Szczegółowe omówienie krok po kroku i wyniki konfiguracji znajdziesz w [Dokumentacji konfiguracji CLI](</pl/start/wizard-cli-reference>). Przykłady nieinteraktywne znajdziesz w [Automatyzacji CLI](</pl/start/wizard-cli-automation>). Głębszą dokumentację techniczną, w tym szczegóły RPC, znajdziesz w [Dokumentacji onboardingu](</pl/reference/wizard>).

## Powiązana dokumentacja

  * Dokumentacja poleceń CLI: [`openclaw onboard`](</pl/cli/onboard>)
  * Omówienie onboardingu: [Omówienie onboardingu](</pl/start/onboarding-overview>)
  * Onboarding aplikacji macOS: [Onboarding](</pl/start/onboarding>)
  * Rytuał pierwszego uruchomienia agenta: [Bootstrap agenta](</pl/start/bootstrapping>)


Was this useful?YesNo