---
title: Wysyłanie przez agenta
source_url: https://docs.openclaw.ai/pl/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` uruchamia pojedynczą turę agenta z wiersza poleceń bez potrzeby przychodzącej wiadomości czatu. Używaj tego do przepływów skryptowych, testowania i programowego dostarczania.

## Szybki start

* ### Run a simple agent turn

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

To wysyła wiadomość przez Gateway i wypisuje odpowiedź.

* ### Target a specific agent or session

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Deliver the reply to a channel

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Flagi

Flaga | Opis  
---|---  
`--message \<text\>` | Wiadomość do wysłania (wymagana)  
`--to \<dest\>` | Wyprowadź klucz sesji z celu (telefon, identyfikator czatu)  
`--agent \<id\>` | Wybierz skonfigurowanego agenta (używa jego sesji `main`)  
`--session-id \<id\>` | Użyj ponownie istniejącej sesji według identyfikatora  
`--local` | Wymuś lokalne osadzone środowisko wykonawcze (pomiń Gateway)  
`--deliver` | Wyślij odpowiedź do kanału czatu  
`--channel \<name\>` | Kanał dostarczania (whatsapp, telegram, discord, slack itd.)  
`--reply-to \<target\>` | Nadpisanie celu dostarczania  
`--reply-channel \<name\>` | Nadpisanie kanału dostarczania  
`--reply-account \<id\>` | Nadpisanie identyfikatora konta dostarczania  
`--thinking \<level\>` | Ustaw poziom myślenia dla wybranego profilu modelu  
`--verbose \<on|full|off\>` | Ustaw poziom szczegółowości  
`--timeout \<seconds\>` | Nadpisz limit czasu agenta  
`--json` | Wypisz ustrukturyzowany JSON  
  
## Zachowanie

  * Domyślnie CLI przechodzi **przez Gateway**. Dodaj `--local`, aby wymusić osadzone środowisko wykonawcze na bieżącej maszynie.
  * Jeśli Gateway jest nieosiągalny, CLI **wraca** do lokalnego osadzonego uruchomienia.
  * Wybór sesji: `--to` wyprowadza klucz sesji (cele grup/kanałów zachowują izolację; czaty bezpośrednie zwijają się do `main`).
  * Flagi myślenia i szczegółowości są utrwalane w magazynie sesji.
  * Wyjście: domyślnie zwykły tekst albo `--json` dla ustrukturyzowanego ładunku + metadanych.
  * Z `--json --deliver` JSON obejmuje status dostarczania dla wysyłek wysłanych, wstrzymanych, częściowych i nieudanych. Zobacz [status dostarczania JSON](</pl/cli/agent#json-delivery-status>).


## Przykłady

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Powiązane

[**Agent CLI reference** Pełna dokumentacja flag i opcji `openclaw agent`. ](</pl/cli/agent>) [**Sub-agents** Uruchamianie podagentów w tle. ](</pl/tools/subagents>) [**Sessions** Jak działają klucze sesji i jak `--to`, `--agent` oraz `--session-id` je rozpoznają. ](</pl/concepts/session>) [**Slash commands** Natywny katalog poleceń używany wewnątrz sesji agenta. ](</pl/tools/slash-commands>)

Was this useful?YesNo