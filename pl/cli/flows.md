---
title: Przepływy (przekierowanie)
source_url: https://docs.openclaw.ai/pl/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Nie ma polecenia najwyższego poziomu `openclaw flows`. Inspekcja trwałych TaskFlow jest dostępna w `openclaw tasks flow`.

## Podpolecenia

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Podpolecenie | Opis | Argumenty / opcje  
---|---|---  
`list` | Wyświetl śledzone TaskFlow. | Wyjście czytelne maszynowo `--json`; filtr `--status <name>` (zobacz wartości stanu poniżej).  
`show` | Pokaż jeden TaskFlow. | Identyfikator flow `<lookup>` lub klucz właściciela; wyjście czytelne maszynowo `--json`.  
`cancel` | Anuluj uruchomiony TaskFlow. | Identyfikator flow `<lookup>` lub klucz właściciela.  
  
`<lookup>` przyjmuje identyfikator flow (zwracany przez `list` / `show`) albo klucz właściciela flow (stabilny identyfikator używany przez podsystem właścicielski do śledzenia flow).

### Wartości filtra stanu

`--status` w `list` przyjmuje jedną z wartości:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Przykłady

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Pełne omówienie pojęć TaskFlow i tworzenia znajdziesz w [TaskFlow](</pl/automation/taskflow>). Polecenie nadrzędne `tasks` opisano w [dokumentacji CLI tasks](</pl/cli/tasks>).

## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Automatyzacja](</pl/automation>)
  * [TaskFlow](</pl/automation/taskflow>)


Was this useful?YesNo