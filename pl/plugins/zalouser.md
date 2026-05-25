---
title: Osobisty Plugin Zalo
source_url: https://docs.openclaw.ai/pl/plugins/zalouser
scraped_at: 2026-05-25
---

Obsługa Zalo Personal dla OpenClaw przez Plugin, z użyciem natywnego `zca-js` do automatyzacji zwykłego konta użytkownika Zalo.

## Nazewnictwo

Identyfikator kanału to `zalouser`, aby jednoznacznie wskazać, że automatyzuje on **osobiste konto użytkownika Zalo** (nieoficjalnie). Zachowujemy `zalo` dla potencjalnej przyszłej oficjalnej integracji z API Zalo.

## Gdzie działa

Ten Plugin działa **wewnątrz procesu Gateway**.

Jeśli używasz zdalnego Gateway, zainstaluj/skonfiguruj go na **maszynie uruchamiającej Gateway** , a następnie zrestartuj Gateway.

Nie jest wymagany zewnętrzny binarny CLI `zca`/`openzca`.

## Instalacja

### Opcja A: instalacja z npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Użyj samego pakietu, aby śledzić bieżący oficjalny tag wydania. Przypnij dokładną wersję tylko wtedy, gdy potrzebujesz powtarzalnej instalacji.

Następnie zrestartuj Gateway.

### Opcja B: instalacja z folderu lokalnego (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Następnie zrestartuj Gateway.

## Konfiguracja

Konfiguracja kanału znajduje się w `channels.zalouser` (nie w `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Narzędzie agenta

Nazwa narzędzia: `zalouser`

Akcje: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Akcje wiadomości kanału obsługują także `react` dla reakcji na wiadomości.

## Powiązane

  * [Tworzenie Pluginów](</pl/plugins/building-plugins>)
  * [ClawHub](</pl/clawhub>)


Was this useful?YesNo