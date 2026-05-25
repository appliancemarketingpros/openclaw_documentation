---
title: OpenClaw
source_url: https://docs.openclaw.ai/pl
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"ZŁUSZCZAĆ! ZŁUSZCZAĆ!"_ — Kosmiczny homar, prawdopodobnie

**Gateway dla agentów AI na dowolny system operacyjny, obsługujący Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo i więcej.**

Wyślij wiadomość i otrzymaj odpowiedź agenta z kieszeni. Uruchom jeden Gateway dla wbudowanych kanałów, dołączonych pluginów kanałów, WebChat i węzłów mobilnych.

[**Rozpocznij** Zainstaluj OpenClaw i uruchom Gateway w kilka minut. ](</pl/start/getting-started>) [**Uruchom onboarding** Konfiguracja z przewodnikiem za pomocą `openclaw onboard` i przepływów parowania. ](</pl/start/wizard>) [**Otwórz Control UI** Uruchom panel przeglądarkowy do czatu, konfiguracji i sesji. ](</pl/web/control-ui>)

## Czym jest OpenClaw?

OpenClaw to **samodzielnie hostowany gateway** , który łączy Twoje ulubione aplikacje czatu i powierzchnie kanałów — wbudowane kanały oraz dołączone lub zewnętrzne pluginy kanałów, takie jak Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo i inne — z agentami AI do programowania, takimi jak Pi. Uruchamiasz jeden proces Gateway na własnym komputerze (lub serwerze), a on staje się mostem między Twoimi aplikacjami do wiadomości i zawsze dostępnym asystentem AI.

**Dla kogo to jest?** Dla programistów i zaawansowanych użytkowników, którzy chcą osobistego asystenta AI, do którego mogą pisać z dowolnego miejsca — bez rezygnowania z kontroli nad swoimi danymi ani polegania na usłudze hostowanej.

**Co go wyróżnia?**

  * **Samodzielne hostowanie** : działa na Twoim sprzęcie, według Twoich zasad
  * **Wielokanałowość** : jeden Gateway obsługuje jednocześnie wbudowane kanały oraz dołączone lub zewnętrzne pluginy kanałów
  * **Natywność dla agentów** : zaprojektowany dla agentów programistycznych z użyciem narzędzi, sesjami, pamięcią i routingiem wielu agentów
  * **Open source** : licencja MIT, projekt rozwijany przez społeczność


**Czego potrzebujesz?** Node 24 (zalecane) lub Node 22 LTS (`22.16+`) dla zgodności, klucza API od wybranego dostawcy oraz 5 minut. Aby uzyskać najlepszą jakość i bezpieczeństwo, użyj najmocniejszego dostępnego modelu najnowszej generacji.

## Jak to działa
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway jest pojedynczym źródłem prawdy dla sesji, routingu i połączeń kanałów.

## Kluczowe możliwości

[**Wielokanałowy gateway** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat i więcej w jednym procesie Gateway. ](</pl/channels>) [**Kanały Plugin** Dołączone pluginy dodają Matrix, Nostr, Twitch, Zalo i więcej w zwykłych bieżących wydaniach. ](</pl/tools/plugin>) [**Routing wielu agentów** Izolowane sesje dla każdego agenta, obszaru roboczego lub nadawcy. ](</pl/concepts/multi-agent>) [**Obsługa multimediów** Wysyłaj i odbieraj obrazy, audio i dokumenty. ](</pl/nodes/images>) [**Web Control UI** Panel przeglądarkowy do czatu, konfiguracji, sesji i węzłów. ](</pl/web/control-ui>) [**Węzły mobilne** Sparuj węzły iOS i Android dla przepływów pracy z Canvas, kamerą i głosem. ](</pl/nodes>)

## Szybki start

* ### Zainstaluj OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Przeprowadź onboarding i zainstaluj usługę

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Czat

Otwórz Control UI w przeglądarce i wyślij wiadomość:

bashCopy code
[code]
    openclaw dashboard
[/code]

Albo połącz kanał ([Telegram](</pl/channels/telegram>) jest najszybszy) i rozmawiaj z telefonu.

Potrzebujesz pełnej instalacji i konfiguracji deweloperskiej? Zobacz [Pierwsze kroki](</pl/start/getting-started>).

## Panel

Otwórz przeglądarkowy Control UI po uruchomieniu Gateway.

  * Domyślnie lokalnie: <http://127.0.0.1:18789/>
  * Dostęp zdalny: [Powierzchnie webowe](</pl/web>) i [Tailscale](</pl/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Konfiguracja (opcjonalnie)

Konfiguracja znajduje się w `~/.openclaw/openclaw.json`.

  * Jeśli **nic nie zrobisz** , OpenClaw użyje dołączonego pliku binarnego Pi w trybie RPC z sesjami dla każdego nadawcy.
  * Jeśli chcesz go ograniczyć, zacznij od `channels.whatsapp.allowFrom` oraz (dla grup) reguł wzmianek.


Przykład:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Zacznij tutaj

[**Centra dokumentacji** Cała dokumentacja i przewodniki, uporządkowane według przypadków użycia. ](</pl/start/hubs>) [**Konfiguracja** Podstawowe ustawienia Gateway, tokeny i konfiguracja dostawcy. ](</pl/gateway/configuration>) [**Dostęp zdalny** Wzorce dostępu przez SSH i tailnet. ](</pl/gateway/remote>) [**Kanały** Konfiguracja specyficzna dla kanału dla Feishu, Microsoft Teams, WhatsApp, Telegram, Discord i innych. ](</pl/channels/telegram>) [**Węzły** Węzły iOS i Android z parowaniem, Canvas, kamerą i akcjami urządzenia. ](</pl/nodes>) [**Pomoc** Punkt wejścia do typowych poprawek i rozwiązywania problemów. ](</pl/help>)

## Dowiedz się więcej

[**Pełna lista funkcji** Pełne możliwości kanałów, routingu i multimediów. ](</pl/concepts/features>) [**Routing wielu agentów** Izolacja obszaru roboczego i sesje dla każdego agenta. ](</pl/concepts/multi-agent>) [**Bezpieczeństwo** Tokeny, listy dozwolonych i kontrolki bezpieczeństwa. ](</pl/gateway/security>) [**Rozwiązywanie problemów** Diagnostyka Gateway i typowe błędy. ](</pl/gateway/troubleshooting>) [**O projekcie i autorzy** Początki projektu, współtwórcy i licencja. ](</pl/reference/credits>)

Was this useful?YesNo