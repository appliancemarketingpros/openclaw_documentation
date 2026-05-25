---
title: Wprowadzenie (aplikacja macOS)
source_url: https://docs.openclaw.ai/pl/start/onboarding
scraped_at: 2026-05-25
---

Ten dokument opisuje **bieżący** przepływ konfiguracji przy pierwszym uruchomieniu. Celem jest płynne doświadczenie „dnia 0”: wybierz, gdzie działa Gateway, podłącz uwierzytelnianie, uruchom kreator i pozwól agentowi samodzielnie się zainicjować. Ogólny przegląd ścieżek wdrożenia znajdziesz w [Przeglądzie wdrożenia](</pl/start/onboarding-overview>).

* ### Zatwierdź ostrzeżenie macOS

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Zatwierdź wyszukiwanie sieci lokalnych

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Powitanie i informacja o bezpieczeństwie

Przeczytaj wyświetloną informację o bezpieczeństwie i podejmij odpowiednią decyzję ![](/assets/macos-onboarding/03-security-notice.png)

Model zaufania bezpieczeństwa:

  * Domyślnie OpenClaw jest agentem osobistym: jedna zaufana granica operatora.
  * Konfiguracje współdzielone/wieloużytkownikowe wymagają ograniczeń (oddziel granice zaufania, utrzymuj dostęp narzędzi na minimalnym poziomie i postępuj zgodnie z sekcją [Bezpieczeństwo](</pl/gateway/security>)).
  * Lokalne wdrożenie ustawia teraz domyślnie dla nowych konfiguracji `tools.profile: "coding"`, dzięki czemu świeże lokalne konfiguracje zachowują narzędzia systemu plików/środowiska uruchomieniowego bez wymuszania nieograniczonego profilu `full`.
  * Jeśli włączone są hooki/webhooki lub inne kanały niezaufanych treści, użyj mocnego, nowoczesnego poziomu modelu i utrzymuj rygorystyczne zasady narzędzi/sandboxingu.


* ### Lokalnie a zdalnie

![](/assets/macos-onboarding/04-choose-gateway.png)

Gdzie działa **Gateway**?

  * **Ten Mac (tylko lokalnie):** wdrożenie może skonfigurować uwierzytelnianie i zapisać poświadczenia lokalnie.
  * **Zdalnie (przez SSH/Tailnet):** wdrożenie **nie** konfiguruje lokalnego uwierzytelniania; poświadczenia muszą istnieć na hoście gateway.
  * **Skonfiguruj później:** pomiń konfigurację i pozostaw aplikację nieskonfigurowaną.


* ### Uprawnienia

Wybierz, jakie uprawnienia chcesz nadać OpenClaw ![](/assets/macos-onboarding/05-permissions.png)

Wdrożenie prosi o uprawnienia TCC potrzebne do:

  * Automatyzacji (AppleScript)
  * Powiadomień
  * Dostępności
  * Nagrywania ekranu
  * Mikrofonu
  * Rozpoznawania mowy
  * Kamery
  * Lokalizacji


* ### CLI

* ### Czat wdrożeniowy (dedykowana sesja)

Po konfiguracji aplikacja otwiera dedykowaną sesję czatu wdrożeniowego, aby agent mógł się przedstawić i poprowadzić przez kolejne kroki. Oddziela to wskazówki pierwszego uruchomienia od normalnej rozmowy. Zobacz [Bootstrapping](</pl/start/bootstrapping>), aby dowiedzieć się, co dzieje się na hoście gateway podczas pierwszego uruchomienia agenta.

## Powiązane

  * [Przegląd wdrożenia](</pl/start/onboarding-overview>)
  * [Pierwsze kroki](</pl/start/getting-started>)


Was this useful?YesNo