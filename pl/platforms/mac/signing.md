---
title: Podpisywanie macOS
source_url: https://docs.openclaw.ai/pl/platforms/mac/signing
scraped_at: 2026-05-25
---

# podpisywanie mac (kompilacje debug)

Ta aplikacja jest zwykle budowana z użyciem [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>), który teraz:

  * ustawia stabilny identyfikator pakietu debug: `ai.openclaw.mac.debug`
  * zapisuje Info.plist z tym identyfikatorem pakietu (nadpisanie przez `BUNDLE_ID=...`)
  * wywołuje [`scripts/codesign-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/codesign-mac-app.sh>), aby podpisać główny plik binarny i pakiet aplikacji, dzięki czemu macOS traktuje każdą przebudowę jako ten sam podpisany pakiet i zachowuje uprawnienia TCC (powiadomienia, dostępność, nagrywanie ekranu, mikrofon, mowa). Aby uprawnienia były stabilne, użyj prawdziwej tożsamości podpisującej; ad-hoc wymaga jawnego włączenia i jest kruche (zobacz [uprawnienia macOS](</pl/platforms/mac/permissions>)).
  * domyślnie używa `CODESIGN_TIMESTAMP=auto`; włącza to zaufane znaczniki czasu dla podpisów Developer ID. Ustaw `CODESIGN_TIMESTAMP=off`, aby pominąć znakowanie czasem (offline kompilacje debug).
  * wstrzykuje metadane kompilacji do Info.plist: `OpenClawBuildTimestamp` (UTC) i `OpenClawGitCommit` (krótki hash), aby panel Informacje mógł pokazać kompilację, git oraz kanał debug/release.
  * **Pakowanie domyślnie używa Node 24** : skrypt uruchamia kompilacje TS i kompilację Control UI. Node 22 LTS, obecnie `22.16+`, pozostaje obsługiwany ze względu na kompatybilność.
  * odczytuje `SIGN_IDENTITY` ze środowiska. Dodaj `export SIGN_IDENTITY="Apple Development: Your Name (TEAMID)"` (albo swój certyfikat Developer ID Application) do konfiguracji powłoki, aby zawsze podpisywać swoim certyfikatem. Podpisywanie ad-hoc wymaga jawnego włączenia przez `ALLOW_ADHOC_SIGNING=1` lub `SIGN_IDENTITY="-"` (niezalecane do testowania uprawnień).
  * po podpisaniu uruchamia audyt Team ID i kończy się błędem, jeśli jakikolwiek Mach-O w pakiecie aplikacji jest podpisany innym Team ID. Ustaw `SKIP_TEAM_ID_CHECK=1`, aby pominąć.


## Użycie

bashCopy code
[code]
    # from repo rootscripts/package-mac-app.sh               # auto-selects identity; errors if none foundSIGN_IDENTITY="Developer ID Application: Your Name" scripts/package-mac-app.sh   # real certALLOW_ADHOC_SIGNING=1 scripts/package-mac-app.sh    # ad-hoc (permissions will not stick)SIGN_IDENTITY="-" scripts/package-mac-app.sh        # explicit ad-hoc (same caveat)DISABLE_LIBRARY_VALIDATION=1 scripts/package-mac-app.sh   # dev-only Sparkle Team ID mismatch workaround
[/code]

### Uwaga dotycząca podpisywania ad-hoc

Podczas podpisywania z `SIGN_IDENTITY="-"` (ad-hoc) skrypt automatycznie wyłącza **Hardened Runtime** (`--options runtime`). Jest to konieczne, aby zapobiec awariom, gdy aplikacja próbuje załadować osadzone frameworki (takie jak Sparkle), które nie mają tego samego Team ID. Podpisy ad-hoc psują też trwałość uprawnień TCC; kroki naprawcze znajdziesz w [uprawnieniach macOS](</pl/platforms/mac/permissions>).

## Metadane kompilacji dla Informacji

`package-mac-app.sh` oznacza pakiet następującymi danymi:

  * `OpenClawBuildTimestamp`: ISO8601 UTC w momencie pakowania
  * `OpenClawGitCommit`: krótki hash git (albo `unknown`, jeśli niedostępny)


Karta Informacje odczytuje te klucze, aby pokazać wersję, datę kompilacji, commit git oraz to, czy jest to kompilacja debug (przez `#if DEBUG`). Uruchom pakietowanie po zmianach w kodzie, aby odświeżyć te wartości.

## Dlaczego

Uprawnienia TCC są powiązane z identyfikatorem pakietu _oraz_ podpisem kodu. Niepodpisane kompilacje debug ze zmieniającymi się UUID powodowały, że macOS zapominał przyznane uprawnienia po każdej przebudowie. Podpisanie plików binarnych (domyślnie ad-hoc) i zachowanie stałego identyfikatora/ścieżki pakietu (`dist/OpenClaw.app`) zachowuje uprawnienia między kompilacjami, zgodnie z podejściem VibeTunnel.

## Powiązane

  * [aplikacja macOS](</pl/platforms/macos>)
  * [uprawnienia macOS](</pl/platforms/mac/permissions>)


Was this useful?YesNo