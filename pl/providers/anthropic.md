---
title: Anthropic
source_url: https://docs.openclaw.ai/pl/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic tworzy rodzinę modeli **Claude**. OpenClaw obsługuje dwie ścieżki uwierzytelniania:

  * **klucz API** — bezpośredni dostęp do API Anthropic z rozliczaniem według użycia (modele `anthropic/*`)
  * **Claude CLI** — ponowne użycie istniejącego logowania Claude CLI na tym samym hoście


## Pierwsze kroki

### API key

**Najlepsze do:** standardowego dostępu API i rozliczania według użycia.

* ### Get your API key

Utwórz klucz API w [konsoli Anthropic](<https://console.anthropic.com/>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Albo przekaż klucz bezpośrednio:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Przykład konfiguracji

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**Najlepsze do:** ponownego użycia istniejącego logowania Claude CLI bez osobnego klucza API.

* ### Ensure Claude CLI is installed and logged in

Zweryfikuj za pomocą:

bashCopy code
[code]
    claude --version
[/code]

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw wykrywa i ponownie używa istniejących poświadczeń Claude CLI.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Przykład konfiguracji

Preferuj kanoniczne odwołanie do modelu Anthropic oraz nadpisanie środowiska wykonawczego CLI:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Starsze odwołania do modeli `claude-cli/claude-opus-4-7` nadal działają ze względu na zgodność, ale nowa konfiguracja powinna zachowywać wybór dostawcy/modelu jako `anthropic/*`, a backend wykonawczy umieszczać w polityce środowiska wykonawczego dostawcy/modelu.

## Domyślne myślenie (Claude 4.6)

Modele Claude 4.6 domyślnie używają w OpenClaw myślenia `adaptive`, gdy nie ustawiono jawnego poziomu myślenia.

Nadpisz dla pojedynczej wiadomości za pomocą `/think:<level>` albo w parametrach modelu:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## Buforowanie promptów

OpenClaw obsługuje funkcję buforowania promptów Anthropic dla uwierzytelniania kluczem API.

Wartość | Czas trwania bufora | Opis  
---|---|---  
`"short"` (domyślnie) | 5 minut | Stosowane automatycznie dla uwierzytelniania kluczem API  
`"long"` | 1 godzina | Rozszerzony bufor  
`"none"` | Bez buforowania | Wyłącz buforowanie promptów  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Per-agent cache overrides

Użyj parametrów na poziomie modelu jako wartości bazowej, a następnie nadpisz konkretne agenty przez `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Kolejność scalania konfiguracji:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (pasujące `id`, nadpisuje według klucza)


Dzięki temu jeden agent może utrzymywać długotrwały bufor, podczas gdy inny agent na tym samym modelu wyłącza buforowanie dla ruchu skokowego lub o niskim ponownym użyciu.

Bedrock Claude notes

  * Modele Anthropic Claude w Bedrock (`amazon-bedrock/*anthropic.claude*`) akceptują przekazanie `cacheRetention`, gdy jest skonfigurowane.
  * Modele Bedrock inne niż Anthropic są w czasie działania wymuszane na `cacheRetention: "none"`.
  * Inteligentne wartości domyślne dla klucza API ustawiają też `cacheRetention: "short"` dla odwołań Claude-on-Bedrock, gdy nie ustawiono jawnej wartości.


## Zaawansowana konfiguracja

Fast mode

Wspólny przełącznik `/fast` w OpenClaw obsługuje bezpośredni ruch Anthropic (klucz API i OAuth do `api.anthropic.com`).

Polecenie | Mapuje na  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Media understanding (image and PDF)

Dołączony Plugin Anthropic rejestruje rozumienie obrazów i PDF. OpenClaw automatycznie rozstrzyga możliwości multimediów na podstawie skonfigurowanego uwierzytelniania Anthropic — nie jest potrzebna żadna dodatkowa konfiguracja.

Właściwość | Wartość  
---|---  
Model domyślny | `claude-opus-4-7`  
Obsługiwane wejście | Obrazy, dokumenty PDF  
  
Gdy obraz lub PDF zostanie dołączony do rozmowy, OpenClaw automatycznie kieruje go przez dostawcę rozumienia multimediów Anthropic.

1M context window (beta)

Okno kontekstu 1M Anthropic jest objęte dostępem beta. Włącz je dla modelu:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw mapuje to w żądaniach na `anthropic-beta: context-1m-2025-08-07`.

`params.context1m: true` ma też zastosowanie do backendu Claude CLI (`claude-cli/*`) dla kwalifikujących się modeli Opus i Sonnet, rozszerzając okno kontekstu środowiska wykonawczego dla tych sesji CLI tak, aby odpowiadało zachowaniu bezpośredniego API.

Claude Opus 4.7 1M context

`anthropic/claude-opus-4.7` oraz jego wariant `claude-cli` mają domyślnie okno kontekstu 1M — `params.context1m: true` nie jest potrzebne.

## Rozwiązywanie problemów

401 errors / token suddenly invalid

Uwierzytelnianie tokenem Anthropic wygasa i może zostać unieważnione. W przypadku nowych konfiguracji użyj zamiast tego klucza API Anthropic.

No API key found for provider "anthropic"

Uwierzytelnianie Anthropic jest **per agent** — nowe agenty nie dziedziczą kluczy głównego agenta. Uruchom ponownie onboarding dla tego agenta (albo skonfiguruj klucz API na hoście gateway), a następnie zweryfikuj za pomocą `openclaw models status`.

No credentials found for profile "anthropic:default"

Uruchom `openclaw models status`, aby sprawdzić, który profil uwierzytelniania jest aktywny. Uruchom ponownie onboarding albo skonfiguruj klucz API dla ścieżki tego profilu.

No available auth profile (all in cooldown)

Sprawdź `openclaw models status --json` pod kątem `auth.unusableProfiles`. Okresy cooldown limitów szybkości Anthropic mogą być ograniczone do modelu, więc pokrewny model Anthropic może nadal być używalny. Dodaj kolejny profil Anthropic albo poczekaj na zakończenie cooldown.

## Powiązane

[**Model selection** Wybór dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**CLI backends** Szczegóły konfiguracji i działania backendu Claude CLI. ](</pl/gateway/cli-backends>) [**Prompt caching** Jak buforowanie promptów działa u różnych dostawców. ](</pl/reference/prompt-caching>) [**OAuth and auth** Szczegóły uwierzytelniania i reguły ponownego użycia poświadczeń. ](</pl/gateway/authentication>)

Was this useful?YesNo