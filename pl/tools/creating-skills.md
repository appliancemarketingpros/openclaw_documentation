---
title: Tworzenie Skills
source_url: https://docs.openclaw.ai/pl/tools/creating-skills
scraped_at: 2026-05-25
---

Skills uczą agenta, jak i kiedy używać narzędzi. Każda umiejętność jest katalogiem zawierającym plik `SKILL.md` z frontmatter YAML i instrukcjami w markdown.

Informacje o tym, jak Skills są ładowane i priorytetyzowane, znajdziesz w [Skills](</pl/tools/skills>).

## Utwórz swoją pierwszą umiejętność

* ### Utwórz katalog umiejętności

Skills znajdują się w Twoim obszarze roboczym. Utwórz nowy folder:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Napisz SKILL.md

Utwórz `SKILL.md` w tym katalogu. Frontmatter definiuje metadane, a treść markdown zawiera instrukcje dla agenta.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

Używaj zapisu z łącznikami, małymi literami, cyframi i łącznikami dla `name` umiejętności. Utrzymuj nazwę folderu i `name` we frontmatter spójne.

* ### Dodaj narzędzia (opcjonalnie)

Możesz definiować niestandardowe schematy narzędzi we frontmatter albo poinstruować agenta, aby używał istniejących narzędzi systemowych (takich jak `exec` lub `browser`). Skills mogą także być dostarczane w pluginach razem z narzędziami, które dokumentują.

* ### Załaduj umiejętność

Uruchom nową sesję, aby OpenClaw wykrył umiejętność:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

Sprawdź, czy umiejętność została załadowana:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Przetestuj ją

Wyślij wiadomość, która powinna wyzwolić umiejętność:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

Możesz też po prostu porozmawiać z agentem i poprosić o powitanie.

## Dokumentacja metadanych umiejętności

Frontmatter YAML obsługuje te pola:

Pole | Wymagane | Opis  
---|---|---  
`name` | Tak | Unikalny identyfikator używający małych liter, cyfr i łączników  
`description` | Tak | Jednowierszowy opis pokazywany agentowi  
`metadata.openclaw.os` | Nie | Filtr systemu operacyjnego (`["darwin"]`, `["linux"]` itd.)  
`metadata.openclaw.requires.bins` | Nie | Wymagane pliki binarne w PATH  
`metadata.openclaw.requires.config` | Nie | Wymagane klucze konfiguracji  
  
## Najlepsze praktyki

  * **Pisz zwięźle** — instruuj model, _co_ ma zrobić, a nie jak być AI
  * **Bezpieczeństwo przede wszystkim** — jeśli Twoja umiejętność używa `exec`, upewnij się, że prompty nie pozwalają na dowolne wstrzykiwanie poleceń z niezaufanych danych wejściowych
  * **Testuj lokalnie** — użyj `openclaw agent --message "..."`, aby przetestować przed udostępnieniem
  * **Używaj ClawHub** — przeglądaj i współtwórz umiejętności w [ClawHub](<https://clawhub.ai>)


## Gdzie znajdują się Skills

Lokalizacja | Priorytet | Zakres  
---|---|---  
`\<workspace\>/skills/` | Najwyższy | Dla agenta  
`\<workspace\>/.agents/skills/` | Wysoki | Dla agenta w obszarze roboczym  
`~/.agents/skills/` | Średni | Współdzielony profil agenta  
`~/.openclaw/skills/` | Średni | Współdzielone (wszyscy agenci)  
Wbudowane (dostarczane z OpenClaw) | Niski | Globalny  
`skills.load.extraDirs` | Najniższy | Niestandardowe foldery współdzielone  
  
## Powiązane

  * [Dokumentacja Skills](</pl/tools/skills>) — reguły ładowania, priorytetu i bramkowania
  * [Konfiguracja Skills](</pl/tools/skills-config>) — schemat konfiguracji `skills.*`
  * [ClawHub](</pl/clawhub>) — publiczny rejestr umiejętności
  * [Tworzenie Pluginów](</pl/plugins/building-plugins>) — pluginy mogą dostarczać Skills


Was this useful?YesNo