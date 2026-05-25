---
title: Tryb podwyższonych uprawnień
source_url: https://docs.openclaw.ai/pl/tools/elevated
scraped_at: 2026-05-25
---

Gdy agent działa w piaskownicy, jego polecenia `exec` są ograniczone do środowiska piaskownicy. **Tryb podwyższonych uprawnień** pozwala agentowi wyjść poza nią i zamiast tego uruchamiać polecenia poza piaskownicą, z konfigurowalnymi bramkami zatwierdzania.

## Dyrektywy

Kontroluj tryb podwyższonych uprawnień dla sesji za pomocą poleceń slash:

Dyrektywa | Co robi  
---|---  
`/elevated on` | Uruchamia poza piaskownicą na skonfigurowanej ścieżce hosta, zachowuje zatwierdzenia  
`/elevated ask` | To samo co `on` (alias)  
`/elevated full` | Uruchamia poza piaskownicą na skonfigurowanej ścieżce hosta i pomija zatwierdzenia  
`/elevated off` | Wraca do wykonywania ograniczonego do piaskownicy  
  
Dostępne także jako `/elev on|off|ask|full`.

Wyślij `/elevated` bez argumentu, aby zobaczyć bieżący poziom.

## Jak to działa

* ### Sprawdź dostępność

Tryb podwyższonych uprawnień musi być włączony w konfiguracji, a nadawca musi znajdować się na liście dozwolonych:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Ustaw poziom

Wyślij wiadomość zawierającą tylko dyrektywę, aby ustawić domyślną wartość sesji:

CodeCopy code
[code]
    /elevated full
[/code]

Albo użyj jej w treści wiadomości (dotyczy tylko tej wiadomości):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Polecenia działają poza piaskownicą

Przy aktywnych podwyższonych uprawnieniach wywołania `exec` opuszczają piaskownicę. Efektywnym hostem jest domyślnie `gateway` albo `node`, gdy skonfigurowanym/sesyjnym celem exec jest `node`. W trybie `full` zatwierdzenia exec są pomijane. W trybie `on`/`ask` skonfigurowane reguły zatwierdzania nadal obowiązują.

## Kolejność rozstrzygania

  1. **Dyrektywa w treści wiadomości** (dotyczy tylko tej wiadomości)
  2. **Nadpisanie sesji** (ustawione przez wysłanie wiadomości zawierającej tylko dyrektywę)
  3. **Globalna wartość domyślna** (`agents.defaults.elevatedDefault` w konfiguracji)


## Dostępność i listy dozwolonych

  * **Globalna bramka** : `tools.elevated.enabled` (musi być `true`)
  * **Lista dozwolonych nadawców** : `tools.elevated.allowFrom` z listami dla poszczególnych kanałów
  * **Bramka dla agenta** : `agents.list[].tools.elevated.enabled` (może tylko dodatkowo ograniczać)
  * **Lista dozwolonych dla agenta** : `agents.list[].tools.elevated.allowFrom` (nadawca musi pasować zarówno do globalnej, jak i tej dla agenta)
  * **Awaryjne ustawienie Discord** : jeśli `tools.elevated.allowFrom.discord` jest pominięte, jako wartość awaryjna używane jest `channels.discord.allowFrom`
  * **Wszystkie bramki muszą przejść pomyślnie** ; w przeciwnym razie tryb podwyższonych uprawnień jest traktowany jako niedostępny


Formaty wpisów listy dozwolonych:

Prefiks | Dopasowuje  
---|---  
(brak) | Identyfikator nadawcy, E.164 lub pole From  
`name:` | Wyświetlana nazwa nadawcy  
`username:` | Nazwa użytkownika nadawcy  
`tag:` | Tag nadawcy  
`id:`, `from:`, `e164:` | Jawne wskazanie tożsamości  
  
## Czego nie kontroluje tryb podwyższonych uprawnień

  * **Polityka narzędzi** : jeśli `exec` jest zabroniony przez politykę narzędzi, tryb podwyższonych uprawnień nie może tego nadpisać.
  * **Polityka wyboru hosta** : tryb podwyższonych uprawnień nie zmienia `auto` w swobodne nadpisanie między hostami. Używa skonfigurowanych/sesyjnych reguł celu exec, wybierając `node` tylko wtedy, gdy celem już jest `node`.
  * **Niezależne od`/exec`**: dyrektywa `/exec` dostosowuje domyślne ustawienia exec dla sesji dla autoryzowanych nadawców i nie wymaga trybu podwyższonych uprawnień.


## Powiązane

[**Narzędzie exec** Wykonywanie poleceń powłoki przez agenta. ](</pl/tools/exec>) [**Zatwierdzenia exec** System zatwierdzania i list dozwolonych dla `exec`. ](</pl/tools/exec-approvals>) [**Piaskownica** Konfiguracja piaskownicy na poziomie Gateway. ](</pl/gateway/sandboxing>) [**Piaskownica a polityka narzędzi a tryb podwyższonych uprawnień** Jak trzy bramki składają się podczas wywołania narzędzia. ](</pl/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo