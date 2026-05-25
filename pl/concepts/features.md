---
title: Funkcje
source_url: https://docs.openclaw.ai/pl/concepts/features
scraped_at: 2026-05-25
---

## Najważniejsze informacje

[**Kanały** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat i inne za pomocą jednego Gateway. ](</pl/channels>) [**Pluginy** Dołączone pluginy dodają Matrix, Nextcloud Talk, Nostr, Twitch, Zalo i inne bez osobnych instalacji w zwykłych bieżących wydaniach. ](</pl/tools/plugin>) [**Routing** Routing wieloagentowy z izolowanymi sesjami. ](</pl/concepts/multi-agent>) [**Media** Obrazy, audio, wideo, dokumenty oraz generowanie obrazów/wideo. ](</pl/nodes/images>) [**Aplikacje i UI** Web Control UI i aplikacja towarzysząca dla macOS. ](</pl/web/control-ui>) [**Węzły mobilne** Węzły iOS i Android z parowaniem, głosem/czatem oraz rozbudowanymi poleceniami urządzenia. ](</pl/nodes>)

## Pełna lista

**Kanały:**

  * Wbudowane kanały obejmują Discord, Google Chat, iMessage, IRC, Signal, Slack, Telegram, WebChat i WhatsApp
  * Dołączone kanały pluginów obejmują Feishu, LINE, Matrix, Mattermost, Microsoft Teams, Nextcloud Talk, Nostr, QQ Bot, Synology Chat, Tlon, Twitch, Zalo i Zalo Personal
  * Opcjonalne, instalowane osobno pluginy kanałów obejmują Voice Call oraz pakiety firm trzecich, takie jak WeChat
  * Pluginy kanałów firm trzecich mogą dalej rozszerzać Gateway, na przykład WeChat
  * Obsługa czatów grupowych z aktywacją opartą na wzmiankach
  * Bezpieczeństwo wiadomości prywatnych dzięki listom dozwolonych i parowaniu


**Agent:**

  * Wbudowane środowisko uruchomieniowe agenta ze strumieniowaniem narzędzi
  * Routing wieloagentowy z izolowanymi sesjami dla każdego obszaru roboczego lub nadawcy
  * Sesje: czaty bezpośrednie są scalane we współdzielonym `main`; grupy są izolowane
  * Strumieniowanie i dzielenie na fragmenty dla długich odpowiedzi


**Uwierzytelnianie i dostawcy:**

  * Ponad 35 dostawców modeli (Anthropic, OpenAI, Google i inni)
  * Uwierzytelnianie subskrypcji przez OAuth (np. OpenAI Codex)
  * Obsługa dostawców niestandardowych i hostowanych samodzielnie (vLLM, SGLang, Ollama oraz dowolny punkt końcowy zgodny z OpenAI lub Anthropic)


**Media:**

  * Obrazy, audio, wideo i dokumenty na wejściu i wyjściu
  * Wspólne powierzchnie funkcji generowania obrazów i generowania wideo
  * Transkrypcja notatek głosowych
  * Zamiana tekstu na mowę z wieloma dostawcami


**Aplikacje i interfejsy:**

  * WebChat i przeglądarkowy Control UI
  * Aplikacja towarzysząca na pasku menu macOS
  * Węzeł iOS z parowaniem, Canvas, aparatem, nagrywaniem ekranu, lokalizacją i głosem
  * Węzeł Android z parowaniem, czatem, głosem, Canvas, aparatem i poleceniami urządzenia


**Narzędzia i automatyzacja:**

  * Automatyzacja przeglądarki, exec, sandboxing
  * Wyszukiwanie w sieci (Brave, DuckDuckGo, Exa, Firecrawl, Gemini, Grok, Kimi, MiniMax Search, Ollama Web Search, Perplexity, SearXNG, Tavily)
  * Zadania Cron i planowanie Heartbeat
  * Skills, pluginy i potoki przepływu pracy (Lobster)


## Powiązane

[**Funkcje eksperymentalne** Funkcje opcjonalne, które nie zostały jeszcze udostępnione w domyślnej powierzchni. ](</pl/concepts/experimental-features>) [**Środowisko uruchomieniowe agenta** Model środowiska uruchomieniowego agenta i sposób wysyłania uruchomień. ](</pl/concepts/agent>) [**Kanały** Połącz Telegram, WhatsApp, Discord, Slack i inne z jednego Gateway. ](</pl/channels>) [**Pluginy** Dołączone pluginy i pluginy firm trzecich, które rozszerzają OpenClaw. ](</pl/tools/plugin>)

Was this useful?YesNo