---
title: Grupy rozgłoszeniowe
source_url: https://docs.openclaw.ai/pl/channels/broadcast-groups
scraped_at: 2026-05-25
---

## Omówienie

Grupy broadcast umożliwiają wielu agentom jednoczesne przetwarzanie tej samej wiadomości i odpowiadanie na nią. Pozwala to tworzyć wyspecjalizowane zespoły agentów, które współpracują w jednej grupie WhatsApp lub DM — wszystko przy użyciu jednego numeru telefonu.

Obecny zakres: **tylko WhatsApp** (kanał web).

Grupy broadcast są oceniane po listach dozwolonych kanałów i regułach aktywacji grup. W grupach WhatsApp oznacza to, że broadcast następuje wtedy, gdy OpenClaw normalnie by odpowiedział (na przykład: po wzmiance, zależnie od ustawień grupy).

## Przypadki użycia

1\. Wyspecjalizowane zespoły agentów

Wdrażaj wielu agentów z atomowymi, skoncentrowanymi odpowiedzialnościami:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

Każdy agent przetwarza tę samą wiadomość i przedstawia swoją wyspecjalizowaną perspektywę.

2\. Obsługa wielu języków CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. Przepływy pracy zapewniania jakości CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. Automatyzacja zadań CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## Konfiguracja

### Podstawowa konfiguracja

Dodaj sekcję najwyższego poziomu `broadcast` (obok `bindings`). Klucze to identyfikatory peer WhatsApp:

  * czaty grupowe: JID grupy (np. `120363403215116621@g.us`)
  * DM: numer telefonu E.164 (np. `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**Wynik:** Gdy OpenClaw miałby odpowiedzieć w tym czacie, uruchomi wszystkich trzech agentów.

### Strategia przetwarzania

Kontroluj, jak agenci przetwarzają wiadomości:

### parallel (domyślnie)

Wszyscy agenci przetwarzają jednocześnie:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

Agenci przetwarzają w kolejności (jeden czeka, aż poprzedni skończy):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### Pełny przykład

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## Jak to działa

### Przepływ wiadomości

* ### Przychodzi wiadomość przychodząca

Przychodzi wiadomość z grupy WhatsApp lub DM.

* ### Sprawdzenie broadcast

System sprawdza, czy identyfikator peer znajduje się w `broadcast`.

* ### Jeśli znajduje się na liście broadcast

  * Wszyscy wymienieni agenci przetwarzają wiadomość.
  * Każdy agent ma własny klucz sesji i izolowany kontekst.
  * Agenci przetwarzają równolegle (domyślnie) lub sekwencyjnie.


* ### Jeśli nie znajduje się na liście broadcast

Stosowany jest normalny routing (pierwsze pasujące powiązanie).

### Izolacja sesji

Każdy agent w grupie broadcast utrzymuje całkowicie osobne:

  * **Klucze sesji** (`agent:alfred:whatsapp:group:120363...` vs `agent:baerbel:whatsapp:group:120363...`)
  * **Historia rozmowy** (agent nie widzi wiadomości innych agentów)
  * **Workspace** (osobne sandboxy, jeśli skonfigurowano)
  * **Dostęp do narzędzi** (różne listy allow/deny)
  * **Pamięć/kontekst** (osobne [IDENTITY.md](<http://IDENTITY.md>), [SOUL.md](<http://SOUL.md>), itp.)
  * **Bufor kontekstu grupy** (ostatnie wiadomości grupowe używane jako kontekst) jest współdzielony per peer, więc wszyscy agenci broadcast widzą ten sam kontekst po wyzwoleniu


Pozwala to każdemu agentowi mieć:

  * Różne osobowości
  * Różny dostęp do narzędzi (np. tylko do odczytu vs. odczyt i zapis)
  * Różne modele (np. opus vs. sonnet)
  * Różne zainstalowane Skills


### Przykład: izolowane sesje

W grupie `120363403215116621@g.us` z agentami `["alfred", "baerbel"]`:

### Kontekst Alfreda

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Kontekst Bärbel

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## Najlepsze praktyki

1\. Utrzymuj agentów skoncentrowanych

Projektuj każdego agenta z jedną, jasną odpowiedzialnością:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **Dobrze:** Każdy agent ma jedno zadanie. ❌ **Źle:** Jeden ogólny agent "dev-helper".

2\. Używaj opisowych nazw

Jasno pokaż, co robi każdy agent:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. Skonfiguruj różny dostęp do narzędzi

Daj agentom tylko te narzędzia, których potrzebują:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` ma dostęp tylko do odczytu. `fixer` może czytać i zapisywać.

4\. Monitoruj wydajność

Przy wielu agentach rozważ:

  * Użycie `"strategy": "parallel"` (domyślnie) dla szybkości
  * Ograniczenie grup broadcast do 5-10 agentów
  * Użycie szybszych modeli dla prostszych agentów

5\. Obsługuj awarie z gracją

Agenci zawodzą niezależnie. Błąd jednego agenta nie blokuje pozostałych:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## Zgodność

### Dostawcy

Grupy broadcast obecnie działają z:

  * ✅ WhatsApp (zaimplementowane)
  * 🚧 Telegram (planowane)
  * 🚧 Discord (planowane)
  * 🚧 Slack (planowane)


### Routing

Grupy broadcast działają obok istniejącego routingu:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: Odpowiada tylko alfred (normalny routing).
  * `GROUP_B`: Odpowiadają agent1 ORAZ agent2 (broadcast).


## Rozwiązywanie problemów

Agenci nie odpowiadają

**Sprawdź:**

  1. Identyfikatory agentów istnieją w `agents.list`.
  2. Format identyfikatora peer jest poprawny (np. `120363403215116621@g.us`).
  3. Agenci nie znajdują się na listach deny.


**Debugowanie:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

Odpowiada tylko jeden agent

**Przyczyna:** Identyfikator peer może znajdować się w `bindings`, ale nie w `broadcast`.

**Rozwiązanie:** Dodaj go do konfiguracji broadcast albo usuń z bindings.

Problemy z wydajnością

Jeśli przy wielu agentach działa wolno:

  * Zmniejsz liczbę agentów na grupę.
  * Użyj lżejszych modeli (sonnet zamiast opus).
  * Sprawdź czas uruchamiania sandboxa.


## Przykłady

Przykład 1: Zespół przeglądu kodu jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**Użytkownik wysyła:** Fragment kodu.

**Odpowiedzi:**

  * code-formatter: "Naprawiono wcięcia i dodano podpowiedzi typów"
  * security-scanner: "⚠️ Luka SQL injection w linii 12"
  * test-coverage: "Pokrycie wynosi 45%, brakuje testów dla przypadków błędów"
  * docs-checker: "Brak docstringa dla funkcji `process_data`"

Przykład 2: Obsługa wielu języków jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## Dokumentacja API

### Schemat konfiguracji

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### Pola

Jak przetwarzać agentów. `parallel` uruchamia wszystkich agentów jednocześnie; `sequential` uruchamia ich w kolejności tablicy.

JID grupy WhatsApp, numer E.164 lub inny identyfikator peer. Wartością jest tablica identyfikatorów agentów, którzy powinni przetwarzać wiadomości.

## Ograniczenia

  1. **Maksymalna liczba agentów:** Brak twardego limitu, ale 10+ agentów może działać wolno.
  2. **Współdzielony kontekst:** Agenci nie widzą odpowiedzi innych agentów (celowo).
  3. **Kolejność wiadomości:** Odpowiedzi równoległe mogą nadejść w dowolnej kolejności.
  4. **Limity szybkości:** Wszyscy agenci wliczają się do limitów szybkości WhatsApp.


## Przyszłe ulepszenia

Planowane funkcje:

  * [ ] Tryb współdzielonego kontekstu (agenci widzą odpowiedzi innych agentów)
  * [ ] Koordynacja agentów (agenci mogą sygnalizować sobie nawzajem)
  * [ ] Dynamiczny wybór agentów (wybór agentów na podstawie treści wiadomości)
  * [ ] Priorytety agentów (niektórzy agenci odpowiadają przed innymi)


## Powiązane

  * [Routing kanałów](</pl/channels/channel-routing>)
  * [Grupy](</pl/channels/groups>)
  * [Narzędzia piaskownicy wieloagentowej](</pl/tools/multi-agent-sandbox-tools>)
  * [Parowanie](</pl/channels/pairing>)
  * [Zarządzanie sesją](</pl/concepts/session>)


Was this useful?YesNo