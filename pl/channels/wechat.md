---
title: WeChat
source_url: https://docs.openclaw.ai/pl/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw łączy się z WeChat przez zewnętrzny Plugin kanału Tencent `@tencent-weixin/openclaw-weixin`.

Status: zewnętrzny Plugin. Czaty bezpośrednie i multimedia są obsługiwane. Czaty grupowe nie są ogłaszane przez bieżące metadane możliwości Plugin.

## Nazewnictwo

  * **WeChat** to nazwa widoczna dla użytkownika w tej dokumentacji.
  * **Weixin** to nazwa używana przez pakiet Tencent i przez identyfikator Plugin.
  * `openclaw-weixin` to identyfikator kanału OpenClaw.
  * `@tencent-weixin/openclaw-weixin` to pakiet npm.


Używaj `openclaw-weixin` w poleceniach CLI i ścieżkach konfiguracji.

## Jak to działa

Kod WeChat nie znajduje się w głównym repozytorium OpenClaw. OpenClaw udostępnia ogólny kontrakt Plugin kanału, a zewnętrzny Plugin udostępnia środowisko uruchomieniowe specyficzne dla WeChat:

  1. `openclaw plugins install` instaluje `@tencent-weixin/openclaw-weixin`.
  2. Gateway wykrywa manifest Plugin i ładuje punkt wejścia Plugin.
  3. Plugin rejestruje identyfikator kanału `openclaw-weixin`.
  4. `openclaw channels login --channel openclaw-weixin` uruchamia logowanie QR.
  5. Plugin przechowuje poświadczenia konta w katalogu stanu OpenClaw.
  6. Gdy Gateway się uruchamia, Plugin uruchamia monitor Weixin dla każdego skonfigurowanego konta.
  7. Przychodzące wiadomości WeChat są normalizowane przez kontrakt kanału, kierowane do wybranego agenta OpenClaw i odsyłane przez ścieżkę wychodzącą Plugin.


To rozdzielenie ma znaczenie: rdzeń OpenClaw powinien pozostać niezależny od kanałów. Logowanie WeChat, wywołania API Tencent iLink, przesyłanie/pobieranie multimediów, tokeny kontekstu i monitorowanie kont są własnością zewnętrznego Plugin.

## Instalacja

Szybka instalacja:

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

Instalacja ręczna:

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

Po instalacji uruchom ponownie Gateway:

bashCopy code
[code]
    openclaw gateway restart
[/code]

## Logowanie

Uruchom logowanie QR na tej samej maszynie, na której działa Gateway:

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

Zeskanuj kod QR za pomocą WeChat na telefonie i potwierdź logowanie. Po udanym skanowaniu Plugin zapisuje token konta lokalnie.

Aby dodać kolejne konto WeChat, uruchom ponownie to samo polecenie logowania. Dla wielu kont izoluj sesje wiadomości bezpośrednich według konta, kanału i nadawcy:

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## Kontrola dostępu

Wiadomości bezpośrednie używają standardowego modelu parowania i listy dozwolonych OpenClaw dla Plugin kanałów.

Zatwierdź nowych nadawców:

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

Pełny model kontroli dostępu opisuje [Parowanie](</pl/channels/pairing>).

## Zgodność

Plugin sprawdza wersję hosta OpenClaw podczas uruchamiania.

Linia Plugin | Wersja OpenClaw | tag npm  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
Jeśli Plugin zgłasza, że Twoja wersja OpenClaw jest zbyt stara, zaktualizuj OpenClaw albo zainstaluj starszą linię Plugin:

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## Proces sidecar

Plugin WeChat może uruchamiać pracę pomocniczą obok Gateway podczas monitorowania API Tencent iLink. W zgłoszeniu #68451 ta ścieżka pomocnicza ujawniła błąd w ogólnym czyszczeniu nieaktualnych procesów Gateway w OpenClaw: proces podrzędny mógł próbować wyczyścić nadrzędny proces Gateway, powodując pętle ponownego uruchamiania pod menedżerami procesów takimi jak systemd.

Bieżące czyszczenie przy starcie OpenClaw wyklucza bieżący proces i jego przodków, więc pomocnik kanału nie może zabić Gateway, który go uruchomił. Ta poprawka jest ogólna; w rdzeniu nie jest to ścieżka specyficzna dla WeChat.

## Rozwiązywanie problemów

Sprawdź instalację i status:

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

Jeśli kanał jest widoczny jako zainstalowany, ale się nie łączy, potwierdź, że Plugin jest włączony, i uruchom ponownie:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

Jeśli Gateway uruchamia się ponownie wielokrotnie po włączeniu WeChat, zaktualizuj zarówno OpenClaw, jak i Plugin:

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

Jeśli podczas startu pojawia się komunikat, że zainstalowany pakiet Plugin `requires compiled runtime output for TypeScript entry`, pakiet npm został opublikowany bez skompilowanych plików środowiska uruchomieniowego JavaScript wymaganych przez OpenClaw. Zaktualizuj/zainstaluj ponownie po tym, jak wydawca Plugin opublikuje poprawiony pakiet, albo tymczasowo wyłącz/odinstaluj Plugin.

Tymczasowe wyłączenie:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## Powiązana dokumentacja

  * Omówienie kanałów: [Kanały czatu](</pl/channels>)
  * Parowanie: [Parowanie](</pl/channels/pairing>)
  * Routing kanałów: [Routing kanałów](</pl/channels/channel-routing>)
  * Architektura Plugin: [Architektura Plugin](</pl/plugins/architecture>)
  * SDK Plugin kanału: [SDK Plugin kanału](</pl/plugins/sdk-channel-plugins>)
  * Pakiet zewnętrzny: [@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo