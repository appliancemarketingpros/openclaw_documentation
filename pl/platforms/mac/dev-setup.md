---
title: Konfiguracja środowiska deweloperskiego na macOS
source_url: https://docs.openclaw.ai/pl/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# Konfiguracja środowiska deweloperskiego macOS

Zbuduj i uruchom aplikację OpenClaw dla macOS ze źródeł.

## Wymagania wstępne

Przed zbudowaniem aplikacji upewnij się, że masz zainstalowane:

  1. **Xcode 26.2+** : wymagane do programowania w Swift.
  2. **Node.js 24 i pnpm** : zalecane dla Gateway, CLI oraz skryptów pakowania. Node 22 LTS, obecnie `22.16+`, pozostaje obsługiwany ze względu na zgodność.


## 1\. Zainstaluj zależności

Zainstaluj zależności dla całego projektu:

bashCopy code
[code]
    pnpm install
[/code]

## 2\. Zbuduj i spakuj aplikację

Aby zbudować aplikację macOS i spakować ją do `dist/OpenClaw.app`, uruchom:

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

Jeśli nie masz certyfikatu Apple Developer ID, skrypt automatycznie użyje **podpisywania ad-hoc** (`-`).

Tryby uruchamiania deweloperskiego, flagi podpisywania i rozwiązywanie problemów z Team ID opisuje README aplikacji macOS: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **Uwaga** : aplikacje podpisane ad-hoc mogą wywoływać monity zabezpieczeń. Jeśli aplikacja natychmiast się zawiesza z komunikatem „Abort trap 6”, zobacz sekcję Rozwiązywanie problemów.

## 3\. Zainstaluj CLI

Aplikacja macOS oczekuje globalnej instalacji CLI `openclaw` do zarządzania zadaniami w tle.

**Aby ją zainstalować (zalecane):**

  1. Otwórz aplikację OpenClaw.
  2. Przejdź do karty ustawień **Ogólne**.
  3. Kliknij **„Zainstaluj CLI”**.


Alternatywnie zainstaluj ją ręcznie:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

`pnpm add -g openclaw@<version>` i `bun add -g openclaw@<version>` również działają. Dla środowiska uruchomieniowego Gateway zalecaną ścieżką pozostaje Node.

## Rozwiązywanie problemów

### Kompilacja nie powiodła się: niezgodność toolchaina lub SDK

Kompilacja aplikacji macOS oczekuje najnowszego SDK macOS oraz toolchaina Swift 6.2.

**Zależności systemowe (wymagane):**

  * **Najnowsza wersja macOS dostępna w Uaktualnieniach oprogramowania** (wymagana przez SDK Xcode 26.2)
  * **Xcode 26.2** (toolchain Swift 6.2)


**Sprawdzenia:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

Jeśli wersje się nie zgadzają, zaktualizuj macOS/Xcode i ponownie uruchom kompilację.

### Aplikacja zawiesza się przy przyznawaniu uprawnienia

Jeśli aplikacja zawiesza się, gdy próbujesz zezwolić na dostęp do **Rozpoznawania mowy** lub **Mikrofonu** , przyczyną może być uszkodzona pamięć podręczna TCC albo niezgodność podpisu.

**Naprawa:**

  1. Zresetuj uprawnienia TCC:

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. Jeśli to się nie powiedzie, tymczasowo zmień `BUNDLE_ID` w [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>), aby wymusić „czysty stan” w macOS.


### Gateway „Uruchamianie...” bez końca

Jeśli status Gateway pozostaje na „Uruchamianie...”, sprawdź, czy proces zombie nie blokuje portu:

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # If you're not using a LaunchAgent (dev mode / manual runs), find the listener:lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

Jeśli ręczne uruchomienie blokuje port, zatrzymaj ten proces (Ctrl+C). W ostateczności zakończ proces o znalezionym wyżej PID.

## Powiązane

  * [Aplikacja macOS](</pl/platforms/macos>)
  * [Omówienie instalacji](</pl/install>)


Was this useful?YesNo