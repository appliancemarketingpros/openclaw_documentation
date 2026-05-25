---
title: Zatwierdzenia
source_url: https://docs.openclaw.ai/pl/cli/approvals
scraped_at: 2026-05-25
---

# `openclaw approvals`

Zarządzaj zatwierdzeniami exec dla **hosta lokalnego** , **hosta gateway** albo **hosta node**. Domyślnie polecenia są kierowane do lokalnego pliku zatwierdzeń na dysku. Użyj `--gateway`, aby kierować je do gateway, albo `--node`, aby kierować je do konkretnego node.

Alias: `openclaw exec-approvals`

Powiązane:

  * Zatwierdzenia exec: [Zatwierdzenia exec](</pl/tools/exec-approvals>)
  * Node: [Node](</pl/nodes>)


## `openclaw exec-policy`

`openclaw exec-policy` to lokalne wygodne polecenie do utrzymywania żądanej konfiguracji `tools.exec.*` i lokalnego pliku zatwierdzeń hosta w synchronizacji w jednym kroku.

Użyj go, gdy chcesz:

  * sprawdzić lokalną żądaną politykę, plik zatwierdzeń hosta i efektywne scalenie
  * zastosować lokalny preset, taki jak YOLO albo deny-all
  * zsynchronizować lokalne `tools.exec.*` i lokalne `~/.openclaw/exec-approvals.json`


Przykłady:

bashCopy code
[code]
    openclaw exec-policy showopenclaw exec-policy show --json openclaw exec-policy preset yoloopenclaw exec-policy preset cautious --json openclaw exec-policy set --host gateway --security full --ask off --ask-fallback full
[/code]

Tryby wyjścia:

  * bez `--json`: wypisuje czytelny dla człowieka widok tabeli
  * `--json`: wypisuje ustrukturyzowane dane czytelne dla maszyn


Bieżący zakres:

  * `exec-policy` jest **tylko lokalne**
  * aktualizuje razem lokalny plik konfiguracji i lokalny plik zatwierdzeń
  * **nie** wypycha polityki do hosta gateway ani hosta node
  * `--host node` jest odrzucane w tym poleceniu, ponieważ zatwierdzenia exec dla node są pobierane z node w czasie działania i muszą być zarządzane przez polecenia zatwierdzeń kierowane do node
  * `openclaw exec-policy show` oznacza zakresy `host=node` jako zarządzane przez node w czasie działania zamiast wyprowadzać efektywną politykę z lokalnego pliku zatwierdzeń


Jeśli musisz bezpośrednio edytować zatwierdzenia hostów zdalnych, nadal używaj `openclaw approvals set --gateway` lub `openclaw approvals set --node <id|name|ip>`.

## Typowe polecenia

bashCopy code
[code]
    openclaw approvals getopenclaw approvals get --node <id|name|ip>openclaw approvals get --gateway
[/code]

`openclaw approvals get` pokazuje teraz efektywną politykę exec dla celów lokalnych, gateway i node:

  * żądaną politykę `tools.exec`
  * politykę pliku zatwierdzeń hosta
  * efektywny wynik po zastosowaniu reguł pierwszeństwa


Pierwszeństwo jest celowe:

  * plik zatwierdzeń hosta jest egzekwowalnym źródłem prawdy
  * żądana polityka `tools.exec` może zawężać lub poszerzać intencję, ale efektywny wynik nadal jest wyprowadzany z reguł hosta
  * `--node` łączy plik zatwierdzeń hosta node z polityką `tools.exec` gateway, ponieważ oba nadal mają zastosowanie w czasie działania
  * jeśli konfiguracja gateway jest niedostępna, CLI wraca do snapshotu zatwierdzeń node i zaznacza, że nie udało się obliczyć końcowej polityki środowiska uruchomieniowego


## Zastępowanie zatwierdzeń z pliku

bashCopy code
[code]
    openclaw approvals set --file ./exec-approvals.jsonopenclaw approvals set --stdin <<'EOF'{ version: 1, defaults: { security: "full", ask: "off" } }EOFopenclaw approvals set --node <id|name|ip> --file ./exec-approvals.jsonopenclaw approvals set --gateway --file ./exec-approvals.json
[/code]

`set` akceptuje JSON5, a nie tylko ścisły JSON. Użyj `--file` albo `--stdin`, nie obu naraz.

## Przykład „nigdy nie pytaj” / YOLO

Dla hosta, który nigdy nie powinien zatrzymywać się na zatwierdzeniach exec, ustaw domyślne wartości pliku zatwierdzeń hosta na `full` \+ `off`:

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Wariant dla node:

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

To zmienia tylko **plik zatwierdzeń hosta**. Aby utrzymać zgodność z żądaną polityką OpenClaw, ustaw również:

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask off
[/code]

Dlaczego `tools.exec.host=gateway` w tym przykładzie:

  * `host=auto` nadal oznacza „sandbox, jeśli dostępny, w przeciwnym razie gateway”.
  * YOLO dotyczy zatwierdzeń, a nie routingu.
  * Jeśli chcesz exec na hoście nawet wtedy, gdy skonfigurowano sandbox, jawnie ustaw wybór hosta przez `gateway` albo `/exec host=gateway`.


To odpowiada obecnemu domyślnemu zachowaniu YOLO dla hosta. Zaostrz je, jeśli chcesz zatwierdzeń.

Lokalny skrót:

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

Ten lokalny skrót aktualizuje jednocześnie żądaną lokalną konfigurację `tools.exec.*` i lokalne wartości domyślne zatwierdzeń. Jest równoważny intencyjnie ręcznej konfiguracji dwuetapowej powyżej, ale tylko dla maszyny lokalnej.

## Pomocniki listy dozwolonych

bashCopy code
[code]
    openclaw approvals allowlist add "~/Projects/**/bin/rg"openclaw approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"openclaw approvals allowlist add --agent "*" "/usr/bin/uname" openclaw approvals allowlist remove "~/Projects/**/bin/rg"
[/code]

## Typowe opcje

`get`, `set` i `allowlist add|remove` obsługują:

  * `--node <id|name|ip>`
  * `--gateway`
  * współdzielone opcje RPC dla node: `--url`, `--token`, `--timeout`, `--json`


Uwagi dotyczące kierowania:

  * brak flag celu oznacza lokalny plik zatwierdzeń na dysku
  * `--gateway` kieruje do pliku zatwierdzeń hosta gateway
  * `--node` kieruje do jednego hosta node po rozwiązaniu identyfikatora, nazwy, IP lub prefiksu identyfikatora


`allowlist add|remove` obsługuje również:

  * `--agent <id>` (domyślnie `*`)


## Uwagi

  * `--node` używa tego samego mechanizmu rozwiązywania co `openclaw nodes` (id, nazwa, ip albo prefiks id).
  * `--agent` domyślnie ma wartość `"*"`, co dotyczy wszystkich agentów.
  * Host node musi deklarować `system.execApprovals.get/set` (aplikacja macOS albo bezgłowy host node).
  * Pliki zatwierdzeń są przechowywane per host w `~/.openclaw/exec-approvals.json`.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Zatwierdzenia exec](</pl/tools/exec-approvals>)


Was this useful?YesNo