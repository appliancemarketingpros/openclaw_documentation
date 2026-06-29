---
title: Architektura środowiska uruchomieniowego agentów
source_url: https://docs.openclaw.ai/pl/agent-runtime-architecture
scraped_at: 2026-06-29
---

ReferenceTechnical reference

OpenClaw bezpośrednio posiada wbudowane środowisko uruchomieniowe agenta. Kod środowiska uruchomieniowego znajduje się w `src/agents/`, pomocnicze elementy modelu/dostawcy znajdują się w `src/llm/`, a kontrakty przeznaczone dla Pluginów są udostępniane przez beczki `openclaw/plugin-sdk/*`.

## Układ Środowiska Uruchomieniowego

  * `src/agents/embedded-agent-runner/`: wbudowana pętla prób agenta, adaptery strumieni dostawców, Compaction, wybór modelu i okablowanie sesji.
  * `src/agents/sessions/`: utrwalanie sesji, ładowanie rozszerzeń, odkrywanie zasobów, Skills, prompty, motywy i renderery narzędzi oparte na TUI.
  * `packages/agent-core/`: wielokrotnego użytku rdzeń agenta, niższopoziomowe typy uprzęży, wiadomości, pomocniki Compaction, szablony promptów oraz kontrakty narzędzi/sesji.
  * `src/agents/runtime/`: fasada OpenClaw dla `@openclaw/agent-core` oraz lokalne narzędzia proxy.
  * `src/agents/agent-tools*.ts`: definicje narzędzi, schematy, polityka, adaptery haków przed/po oraz obsługa edycji hosta należące do OpenClaw.
  * `src/agents/agent-hooks/`: wbudowane haki środowiska uruchomieniowego, takie jak zabezpieczenia Compaction i przycinanie kontekstu.
  * `src/llm/`: rejestr modeli/dostawców, pomocniki transportu oraz implementacje strumieni specyficzne dla dostawców.


## Granice

Kod rdzenia wywołuje wbudowane środowisko uruchomieniowe przez moduły OpenClaw i beczki SDK, a nie przez stare zewnętrzne pakiety agentów. Pluginy używają udokumentowanych punktów wejścia `openclaw/plugin-sdk/*` i nie importują wewnętrznych elementów `src/**`.

`@earendil-works/pi-tui` pozostaje zewnętrzną zależnością TUI. Jest używany jako zestaw komponentów terminalowych przez lokalne TUI i renderery sesji; jego internalizacja byłaby osobnym wysiłkiem vendoringu.

## Manifesty

Pakiety zasobów deklarują zasoby OpenClaw w metadanych pakietu:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["extensions/index.ts"],    "skills": ["skills/*.md"],    "prompts": ["prompts/*.md"],    "themes": ["themes/*.json"]  }}
[/code]

Menedżer pakietów odkrywa również konwencjonalne katalogi `extensions/`, `skills/`, `prompts/` i `themes/`.

## Wybór Środowiska Uruchomieniowego

Domyślny identyfikator wbudowanego środowiska uruchomieniowego to `openclaw`. Uprzęże Pluginów mogą rejestrować dodatkowe identyfikatory środowisk uruchomieniowych. `auto` wybiera obsługującą uprząż Pluginu, gdy taka istnieje, a w przeciwnym razie używa wbudowanego środowiska uruchomieniowego OpenClaw.

## Powiązane

  * [Przepływ pracy środowiska uruchomieniowego agenta OpenClaw](</pl/openclaw-agent-runtime>)
  * [Środowiska uruchomieniowe agentów](</pl/concepts/agent-runtimes>)


Was this useful?YesNo

Open issue