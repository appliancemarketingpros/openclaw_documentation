---
title: Northflank
source_url: https://docs.openclaw.ai/pl/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Wdróż OpenClaw na Northflank za pomocą szablonu one-click i uzyskaj dostęp przez webowe Control UI. To najprostsza ścieżka „bez terminala na serwerze”: Northflank uruchamia Gateway za Ciebie.

## Jak zacząć

  1. Kliknij [Deploy OpenClaw](<https://northflank.com/stacks/deploy-openclaw>), aby otworzyć szablon.
  2. Utwórz [konto w Northflank](<https://app.northflank.com/signup>), jeśli jeszcze go nie masz.
  3. Kliknij **Deploy OpenClaw now**.
  4. Ustaw wymaganą zmienną środowiskową: `OPENCLAW_GATEWAY_TOKEN` (użyj silnej losowej wartości).
  5. Kliknij **Deploy stack** , aby zbudować i uruchomić szablon OpenClaw.
  6. Poczekaj na zakończenie wdrożenia, a następnie kliknij **View resources**.
  7. Otwórz usługę OpenClaw.
  8. Otwórz publiczny adres URL OpenClaw pod `/openclaw` i połącz się przy użyciu skonfigurowanego współdzielonego sekretu. Ten szablon domyślnie używa `OPENCLAW_GATEWAY_TOKEN`; jeśli zastąpisz go uwierzytelnianiem hasłem, użyj zamiast tego tego hasła.


## Co otrzymujesz

  * Hostowany Gateway OpenClaw + Control UI
  * Trwałą pamięć przez Northflank Volume (`/data`), dzięki czemu `openclaw.json`, `auth-profiles.json` dla poszczególnych agentów, stan kanałów/dostawców, sesje i workspace przetrwają ponowne wdrożenia


## Połącz kanał

Użyj Control UI pod `/openclaw` albo uruchom `openclaw onboard` przez SSH, aby uzyskać instrukcje konfiguracji kanałów:

  * [Telegram](</pl/channels/telegram>) (najszybciej — wystarczy token bota)
  * [Discord](</pl/channels/discord>)
  * [Wszystkie kanały](</pl/channels>)


## Następne kroki

  * Skonfiguruj kanały wiadomości: [Kanały](</pl/channels>)
  * Skonfiguruj Gateway: [Konfiguracja Gateway](</pl/gateway/configuration>)
  * Aktualizuj OpenClaw na bieżąco: [Aktualizowanie](</pl/install/updating>)


Was this useful?YesNo