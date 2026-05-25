---
title: Skonfiguruj
source_url: https://docs.openclaw.ai/pl/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

Interaktywny monit do ukierunkowanych zmian w istniejącej konfiguracji: poświadczeń, urządzeń, domyślnych ustawień agenta, Gateway, kanałów, pluginów, Skills i kontroli kondycji.

Użyj `openclaw onboard` dla pełnego, prowadzonego procesu pierwszego uruchomienia, `openclaw setup` tylko dla bazowej konfiguracji/przestrzeni roboczej oraz `openclaw channels add`, gdy potrzebujesz wyłącznie skonfigurować konto kanału.

Gdy konfiguracja zaczyna się od wyboru uwierzytelniania dostawcy, selektory modelu domyślnego i listy dozwolonych automatycznie preferują tego dostawcę. W przypadku sparowanych dostawców, takich jak Volcengine i BytePlus, ta sama preferencja obejmuje także ich warianty planu kodowania (`volcengine-plan/*`, `byteplus-plan/*`). Jeśli filtr preferowanego dostawcy dałby pustą listę, konfiguracja wraca do niefiltrowanego katalogu zamiast pokazywać pusty selektor.

Dla wyszukiwania w sieci `openclaw configure --section web` pozwala wybrać dostawcę i skonfigurować jego poświadczenia. Niektórzy dostawcy pokazują także specyficzne dla dostawcy dodatkowe monity:

  * **Grok** może zaoferować opcjonalną konfigurację `x_search` z tym samym `XAI_API_KEY` i pozwolić wybrać model `x_search`.
  * **Kimi** może zapytać o region API Moonshot (`api.moonshot.ai` kontra `api.moonshot.cn`) oraz domyślny model wyszukiwania w sieci Kimi.


Powiązane:

  * Odniesienie konfiguracji Gateway: [Konfiguracja](</pl/gateway/configuration>)
  * CLI konfiguracji: [Konfiguracja](</pl/cli/config>)


## Opcje

  * `--section <section>`: powtarzalny filtr sekcji


Dostępne sekcje:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


Uwagi:

  * Wybór miejsca działania Gateway zawsze aktualizuje `gateway.mode`. Możesz wybrać „Kontynuuj” bez innych sekcji, jeśli tylko tego potrzebujesz.
  * Po zapisach lokalnej konfiguracji narzędzie konfiguracyjne instaluje wybrane pluginy do pobrania, gdy wymaga ich wybrana ścieżka konfiguracji. Zdalna konfiguracja Gateway nie instaluje lokalnych pakietów pluginów.
  * Usługi zorientowane na kanały (Slack/Discord/Matrix/Microsoft Teams) podczas konfiguracji proszą o listy dozwolonych kanałów/pokojów. Możesz wprowadzić nazwy lub identyfikatory; kreator rozwiązuje nazwy na identyfikatory, gdy to możliwe.
  * Jeśli uruchomisz krok instalacji demona, uwierzytelnianie tokenem wymaga tokenu, a `gateway.auth.token` jest zarządzane przez SecretRef, konfiguracja weryfikuje SecretRef, ale nie zapisuje rozwiązanych wartości tokenu w postaci zwykłego tekstu do metadanych środowiska usługi nadzorcy.
  * Jeśli uwierzytelnianie tokenem wymaga tokenu, a skonfigurowany SecretRef tokenu nie został rozwiązany, konfiguracja blokuje instalację demona z praktycznymi wskazówkami naprawczymi.
  * Jeśli skonfigurowane są zarówno `gateway.auth.token`, jak i `gateway.auth.password`, a `gateway.auth.mode` nie jest ustawione, konfiguracja blokuje instalację demona do czasu jawnego ustawienia trybu.


## Przykłady

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## Powiązane

  * [Odnośnik CLI](</pl/cli>)
  * [Konfiguracja](</pl/gateway/configuration>)


Was this useful?YesNo