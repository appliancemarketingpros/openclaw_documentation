---
title: Upstash Box
source_url: https://docs.openclaw.ai/pl/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Uruchom trwały OpenClaw Gateway w Upstash Box, zarządzanym środowisku Linux z obsługą cyklu życia keep-alive.

Użyj tunelu SSH do dostępu do panelu. Nie wystawiaj portu Gateway bezpośrednio do publicznego internetu.

## Wymagania wstępne

  * Konto Upstash
  * Upstash Box z keep-alive
  * Klient SSH na komputerze lokalnym


## Utwórz Box

Utwórz Box z keep-alive w konsoli Upstash. Zanotuj identyfikator Box, taki jak `right-flamingo-14486`, oraz klucz API Box.

Upstash utrzymuje aktualny przewodnik OpenClaw Box pod adresem [Konfiguracja OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Połącz się za pomocą tunelu SSH

Przekieruj port panelu OpenClaw na komputer lokalny. Gdy pojawi się monit, użyj klucza API Box jako hasła SSH:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Opcje keepalive ograniczają zrywanie bezczynnego tunelu podczas wdrażania.

## Zainstaluj OpenClaw

Wewnątrz Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Uruchom wdrażanie

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Postępuj zgodnie z monitami. Skopiuj URL panelu i token po zakończeniu wdrażania.

## Uruchom Gateway

Skonfiguruj Gateway dla sieci Box i uruchom go w tle:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

Przy aktywnym tunelu SSH otwórz lokalnie URL panelu:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Automatyczne ponowne uruchamianie

Ustaw to polecenie jako skrypt inicjalizacyjny Box, aby Gateway uruchamiał się ponownie przy starcie Box:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Rozwiązywanie problemów

Jeśli SSH zawiesza się podczas wdrażania, połącz się ponownie z czystą konfiguracją SSH i opcjami keepalive:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

To pomija nieaktualne lokalne ustawienia `~/.ssh/config` i utrzymuje tunel aktywny podczas okresów bezczynności sieci.

## Powiązane

  * [Zdalny dostęp](</pl/gateway/remote>)
  * [Bezpieczeństwo Gateway](</pl/gateway/security>)
  * [Aktualizowanie OpenClaw](</pl/install/updating>)


Was this useful?YesNo

Open issue