---
title: Skills (macOS)
source_url: https://docs.openclaw.ai/pl/platforms/mac/skills
scraped_at: 2026-05-25
---

Aplikacja macOS udostępnia Skills OpenClaw przez gateway; nie parsuje Skills lokalnie.

## Źródło danych

  * `skills.status` (gateway) zwraca wszystkie Skills wraz z kwalifikowalnością i brakującymi wymaganiami (w tym blokadami allowlisty dla dołączonych Skills).
  * Wymagania są wyprowadzane z `metadata.openclaw.requires` w każdym `SKILL.md`.


## Akcje instalacji

  * `metadata.openclaw.install` definiuje opcje instalacji (`brew`/`node`/`go`/`uv`).
  * Aplikacja wywołuje `skills.install`, aby uruchamiać instalatory na hoście gateway.
  * Wbudowane znaleziska `critical` z wykrywania niebezpiecznego kodu domyślnie blokują `skills.install`; podejrzane znaleziska nadal tylko ostrzegają. Nadpisanie niebezpieczeństwa istnieje w żądaniu gateway, ale domyślny przepływ aplikacji pozostaje fail-closed.
  * Jeśli każda opcja instalacji ma wartość `download`, gateway udostępnia wszystkie możliwości pobrania.
  * W przeciwnym razie gateway wybiera jeden preferowany instalator zgodnie z bieżącymi preferencjami instalacji i binariami hosta: najpierw Homebrew, gdy `skills.install.preferBrew` jest włączone i istnieje `brew`, potem `uv`, następnie skonfigurowany menedżer node z `skills.install.nodeManager`, a potem dalsze fallbacki, takie jak `go` lub `download`.
  * Etykiety instalacji Node odzwierciedlają skonfigurowany menedżer node, w tym `yarn`.


## Env/klucze API

  * Aplikacja przechowuje klucze w `~/.openclaw/openclaw.json` pod `skills.entries.<skillKey>`.
  * `skills.update` aktualizuje `enabled`, `apiKey` i `env`.


## Tryb zdalny

  * Aktualizacje instalacji i konfiguracji odbywają się na hoście gateway (a nie na lokalnym Macu).


## Powiązane

  * [Skills](</pl/tools/skills>)
  * [Aplikacja macOS](</pl/platforms/macos>)


Was this useful?YesNo