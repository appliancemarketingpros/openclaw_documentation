---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/pl/providers/github-copilot
scraped_at: 2026-05-25
---

GitHub Copilot to asystent kodowania AI od GitHub. Zapewnia dostęp do modeli Copilot dla Twojego konta i planu GitHub. OpenClaw może używać Copilot jako dostawcy modeli na dwa różne sposoby.

## Dwa sposoby używania Copilot w OpenClaw

### Wbudowany dostawca (github-copilot)

Użyj natywnego przepływu logowania urządzenia, aby uzyskać token GitHub, a następnie wymieniaj go na tokeny API Copilot podczas działania OpenClaw. To jest **domyślna** i najprostsza ścieżka, ponieważ nie wymaga VS Code.

* ### Uruchom polecenie logowania

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Zostaniesz poproszony o odwiedzenie URL i wpisanie jednorazowego kodu. Pozostaw terminal otwarty do czasu zakończenia.

* ### Ustaw domyślny model

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

Albo w konfiguracji:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Plugin Copilot Proxy (copilot-proxy)

Użyj rozszerzenia **Copilot Proxy** dla VS Code jako lokalnego mostu. OpenClaw komunikuje się z punktem końcowym `/v1` proxy i używa listy modeli skonfigurowanej w tym miejscu.

## Opcjonalne flagi

Flaga | Opis  
---|---  
`--yes` | Pomiń monit o potwierdzenie  
`--set-default` | Zastosuj także zalecany domyślny model dostawcy  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Wdrażanie nieinteraktywne

Jeśli masz już token dostępu GitHub OAuth dla Copilot, zaimportuj go podczas konfiguracji bezinterfejsowej za pomocą `openclaw onboard --non-interactive`:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

Możesz też pominąć `--auth-choice`; przekazanie `--github-copilot-token` wywnioskuje wybór uwierzytelniania dostawcy GitHub Copilot. Jeśli flaga zostanie pominięta, wdrażanie wróci kolejno do `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, a następnie `GITHUB_TOKEN`. Użyj `--secret-input-mode ref` z ustawionym `COPILOT_GITHUB_TOKEN`, aby przechowywać wspierany zmienną środowiskową `tokenRef` zamiast tekstu jawnego w `auth-profiles.json`.

Wymagany interaktywny TTY

Przepływ logowania urządzenia wymaga interaktywnego TTY. Uruchom go bezpośrednio w terminalu, nie w nieinteraktywnym skrypcie ani potoku CI.

Dostępność modeli zależy od Twojego planu

Dostępność modeli Copilot zależy od Twojego planu GitHub. Jeśli model zostanie odrzucony, spróbuj innego ID (na przykład `github-copilot/gpt-4.1`).

Odświeżanie katalogu na żywo z API Copilot

Gdy ścieżka uwierzytelniania logowania urządzenia (lub zmiennej środowiskowej) rozwiąże token GitHub, OpenClaw odświeża katalog modeli na żądanie z `${baseUrl}/models` (tego samego punktu końcowego, którego używa VS Code Copilot), więc środowisko wykonawcze śledzi uprawnienia konta i dokładne okna kontekstu bez zmian manifestu. Nowo opublikowane modele Copilot stają się widoczne bez aktualizacji OpenClaw, a okna kontekstu odzwierciedlają rzeczywiste limity poszczególnych modeli (np. 400k dla serii gpt-5.x, 1M dla wewnętrznych wariantów `claude-opus-*-1m`).

Dołączony katalog statyczny pozostaje widocznym rozwiązaniem awaryjnym, gdy wykrywanie jest wyłączone, użytkownik nie ma profilu uwierzytelniania GitHub, wymiana tokenu kończy się niepowodzeniem albo wywołanie HTTPS `/models` zwraca błąd. Aby zrezygnować i polegać wyłącznie na statycznym katalogu manifestu (scenariusze offline / odizolowane):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Wybór transportu

ID modeli Claude automatycznie używają transportu Anthropic Messages. Modele GPT, z serii o oraz Gemini zachowują transport OpenAI Responses. OpenClaw wybiera właściwy transport na podstawie referencji modelu.

Zgodność żądań

OpenClaw wysyła nagłówki żądań w stylu IDE Copilot w transportach Copilot, w tym wbudowane Compaction, wyniki narzędzi i kolejne tury po obrazach. Nie włącza kontynuacji Responses na poziomie dostawcy dla Copilot, chyba że takie zachowanie zostało zweryfikowane względem API Copilot.

Kolejność rozwiązywania zmiennych środowiskowych

OpenClaw rozwiązuje uwierzytelnianie Copilot ze zmiennych środowiskowych w następującej kolejności priorytetów:

Priorytet | Zmienna | Uwagi  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | Najwyższy priorytet, specyficzna dla Copilot  
2 | `GH_TOKEN` | Token GitHub CLI (awaryjnie)  
3 | `GITHUB_TOKEN` | Standardowy token GitHub (najniżej)  
  
Gdy ustawionych jest wiele zmiennych, OpenClaw używa tej o najwyższym priorytecie. Przepływ logowania urządzenia (`openclaw models auth login-github-copilot`) zapisuje swój token w magazynie profili uwierzytelniania i ma pierwszeństwo przed wszystkimi zmiennymi środowiskowymi.

Przechowywanie tokenów

Logowanie zapisuje token GitHub w magazynie profili uwierzytelniania i wymienia go na token API Copilot podczas działania OpenClaw. Nie musisz zarządzać tokenem ręcznie.

## Osadzenia wyszukiwania w pamięci

GitHub Copilot może też działać jako dostawca osadzeń dla [wyszukiwania w pamięci](</pl/concepts/memory-search>). Jeśli masz subskrypcję Copilot i jesteś zalogowany, OpenClaw może używać go do osadzeń bez osobnego klucza API.

### Automatyczne wykrywanie

Gdy `memorySearch.provider` ma wartość `"auto"` (domyślnie), GitHub Copilot jest próbowany z priorytetem 15 -- po lokalnych osadzeniach, ale przed OpenAI i innymi płatnymi dostawcami. Jeśli token GitHub jest dostępny, OpenClaw wykrywa dostępne modele osadzeń z API Copilot i automatycznie wybiera najlepszy.

### Jawna konfiguracja

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Jak to działa

  1. OpenClaw rozwiązuje Twój token GitHub (ze zmiennych środowiskowych lub profilu uwierzytelniania).
  2. Wymienia go na krótkotrwały token API Copilot.
  3. Odpytuje punkt końcowy Copilot `/models`, aby wykryć dostępne modele osadzeń.
  4. Wybiera najlepszy model (preferuje `text-embedding-3-small`).
  5. Wysyła żądania osadzeń do punktu końcowego Copilot `/embeddings`.


Dostępność modeli zależy od Twojego planu GitHub. Jeśli żadne modele osadzeń nie są dostępne, OpenClaw pomija Copilot i próbuje następnego dostawcy.

## Powiązane

[**Wybór modelu** Wybieranie dostawców, referencji modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**OAuth i uwierzytelnianie** Szczegóły uwierzytelniania i reguły ponownego użycia poświadczeń. ](</pl/gateway/authentication>)

Was this useful?YesNo