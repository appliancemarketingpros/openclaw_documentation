---
title: Pas startowy
source_url: https://docs.openclaw.ai/pl/providers/runway
scraped_at: 2026-05-25
---

OpenClaw dostarcza dołączonego dostawcę `runway` do hostowanego generowania wideo. Plugin jest domyślnie włączony i rejestruje dostawcę `runway` względem kontraktu `videoGenerationProviders`.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `runway`  
Plugin | dołączony, `enabledByDefault: true`  
Zmienne env auth | `RUNWAYML_API_SECRET` (kanoniczna) lub `RUNWAY_API_KEY`  
Flaga onboardingu | `--auth-choice runway-api-key`  
Bezpośrednia flaga CLI | `--runway-api-key <key>`  
API | Generowanie wideo Runway oparte na zadaniach (sondowanie `GET /v1/tasks/{id}`)  
Model domyślny | `runway/gen4.5`  
  
## Pierwsze kroki

* ### Ustaw klucz API

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Ustaw Runway jako domyślnego dostawcę wideo

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Wygeneruj wideo

Poproś agenta o wygenerowanie wideo. Runway zostanie użyty automatycznie.

## Obsługiwane tryby i modele

Dostawca udostępnia siedem modeli Runway podzielonych na trzy tryby. Ten sam identyfikator modelu może obsługiwać więcej niż jeden tryb (na przykład `gen4.5` działa zarówno dla tekstu na wideo, jak i obrazu na wideo).

Tryb | Modele | Wejście referencyjne  
---|---|---  
Tekst na wideo | `gen4.5` (domyślny), `veo3.1`, `veo3.1_fast`, `veo3` | Brak  
Obraz na wideo | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 obraz lokalny lub zdalny  
Wideo na wideo | `gen4_aleph` | 1 wideo lokalne lub zdalne  
  
Lokalne referencje obrazów i wideo są obsługiwane przez identyfikatory URI danych.

Proporcje obrazu | Dozwolone wartości  
---|---  
Tekst na wideo | `16:9`, `9:16`  
Edycje obrazu i wideo | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Konfiguracja

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Konfiguracja zaawansowana

Aliasy zmiennych środowiskowych

OpenClaw rozpoznaje zarówno `RUNWAYML_API_SECRET` (kanoniczną), jak i `RUNWAY_API_KEY`. Każda z tych zmiennych uwierzytelni dostawcę Runway.

Sondowanie zadań

Runway używa API opartego na zadaniach. Po przesłaniu żądania generowania OpenClaw sonduje `GET /v1/tasks/{id}`, aż wideo będzie gotowe. Zachowanie sondowania nie wymaga dodatkowej konfiguracji.

## Powiązane

[**Generowanie wideo** Wspólne parametry narzędzia, wybór dostawcy i zachowanie asynchroniczne. ](</pl/tools/video-generation>) [**Dokumentacja konfiguracji** Domyślne ustawienia agenta, w tym model generowania wideo. ](</pl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo