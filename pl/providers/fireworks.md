---
title: Fajerwerki
source_url: https://docs.openclaw.ai/pl/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) udostępnia modele o otwartych wagach i routowane modele przez API zgodne z OpenAI. OpenClaw zawiera dołączony Plugin dostawcy Fireworks, który jest dostarczany z dwoma wstępnie skatalogowanymi modelami Kimi i akceptuje dowolny model Fireworks lub identyfikator routera w czasie działania.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `fireworks` (alias: `fireworks-ai`)  
Plugin | dołączony, `enabledByDefault: true`  
Zmienna env uwierzytelniania | `FIREWORKS_API_KEY`  
Flaga onboardingu | `--auth-choice fireworks-api-key`  
Bezpośrednia flaga CLI | `--fireworks-api-key <key>`  
API | zgodne z OpenAI (`openai-completions`)  
Bazowy URL | `https://api.fireworks.ai/inference/v1`  
Model domyślny | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
Alias domyślny | `Kimi K2.5 Turbo`  
  
## Pierwsze kroki

* ### Ustaw klucz API Fireworks

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Onboarding zapisuje klucz dla dostawcy `fireworks` w Twoich profilach uwierzytelniania i ustawia router **Fire Pass** Kimi K2.5 Turbo jako model domyślny.

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

Lista powinna zawierać `Kimi K2.6` oraz `Kimi K2.5 Turbo (Fire Pass)`. Jeśli `FIREWORKS_API_KEY` nie zostanie rozwiązany, `openclaw models status --json` zgłosi brakujące dane uwierzytelniające w `auth.unusableProfiles`.

## Konfiguracja nieinteraktywna

W przypadku instalacji skryptowych lub CI przekaż wszystko w wierszu poleceń:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Wbudowany katalog

Odwołanie do modelu | Nazwa | Wejście | Kontekst | Maks. wyjście | Myślenie  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | tekst + obraz | 262,144 | 262,144 | Wymuszone wyłączenie  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | tekst + obraz | 256,000 | 256,000 | Wymuszone wyłączenie (domyślnie)  
  
## Niestandardowe identyfikatory modeli Fireworks

OpenClaw akceptuje dowolny model Fireworks lub identyfikator routera w czasie działania. Użyj dokładnego identyfikatora pokazanego przez Fireworks i poprzedź go prefiksem `fireworks/`. Dynamiczne rozwiązywanie klonuje szablon Fire Pass (wejście tekst + obraz, API zgodne z OpenAI, domyślny koszt zero) i automatycznie wyłącza myślenie, gdy identyfikator pasuje do wzorca Kimi.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

Jak działa prefiksowanie identyfikatorów modeli

Każde odwołanie do modelu Fireworks w OpenClaw zaczyna się od `fireworks/`, po którym następuje dokładny identyfikator lub ścieżka routera z platformy Fireworks. Na przykład:

  * Model routera: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Model bezpośredni: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw usuwa prefiks `fireworks/` podczas konstruowania żądania API i wysyła pozostałą ścieżkę do punktu końcowego Fireworks jako pole `model` zgodne z OpenAI.

Dlaczego myślenie jest wymuszanie wyłączane dla Kimi

Fireworks K2.6 zwraca 400, jeśli żądanie zawiera parametry `reasoning_*`, mimo że Kimi obsługuje myślenie przez własne API Moonshot. Dołączona polityka (`extensions/fireworks/thinking-policy.ts`) ogłasza tylko poziom myślenia `off` dla identyfikatorów modeli Kimi, dzięki czemu ręczne przełączniki `/think` i powierzchnie polityk dostawcy pozostają zgodne z kontraktem czasu działania.

Aby używać rozumowania Kimi od początku do końca, skonfiguruj [dostawcę Moonshot](</pl/providers/moonshot>) i kieruj ten sam model przez niego.

Dostępność środowiska dla demona

Jeśli Gateway działa jako zarządzana usługa (launchd, systemd, Docker), klucz Fireworks musi być widoczny dla tego procesu — nie tylko dla Twojej interaktywnej powłoki.

W systemie macOS `openclaw gateway install` już podłącza `~/.openclaw/.env` do pliku środowiska LaunchAgent. Uruchom instalację ponownie (lub `openclaw doctor --fix`) po rotacji klucza.

## Powiązane

[**Dostawcy modeli** Wybieranie dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Tryby myślenia** Poziomy `/think`, polityki dostawców i routowanie modeli zdolnych do rozumowania. ](</pl/tools/thinking>) [**Moonshot** Uruchamiaj Kimi z natywnym wynikiem myślenia przez własne API Moonshot. ](</pl/providers/moonshot>) [**Rozwiązywanie problemów** Ogólne rozwiązywanie problemów i FAQ. ](</pl/help/troubleshooting>)

Was this useful?YesNo