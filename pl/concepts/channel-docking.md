---
title: Dokowanie kanału
source_url: https://docs.openclaw.ai/pl/concepts/channel-docking
scraped_at: 2026-05-25
---

Dokowanie kanału to przekazywanie połączeń dla jednej sesji OpenClaw.

Zachowuje ten sam kontekst rozmowy, ale zmienia miejsce, do którego będą dostarczane przyszłe odpowiedzi dla tej sesji.

## Przykład

Alice może pisać do OpenClaw na Telegram i Discord:

json5Copy code
[code]
    {  session: {    identityLinks: {      alice: ["telegram:123", "discord:456"],    },  },}
[/code]

Jeśli Alice wyśle to z Telegram:

textCopy code
[code]
    /dock_discord
[/code]

OpenClaw zachowuje bieżący kontekst sesji i zmienia trasę odpowiedzi:

Przed dokowaniem | Po `/dock_discord`  
---|---  
Odpowiedzi trafiają do Telegram `123` | Odpowiedzi trafiają do Discord `456`  
  
Sesja nie jest tworzona ponownie. Historia transkryptu pozostaje przypisana do tej samej sesji.

## Dlaczego tego używać

Użyj dokowania, gdy zadanie zaczyna się w jednej aplikacji czatu, ale kolejne odpowiedzi powinny trafiać gdzie indziej.

Typowy przepływ:

  1. Uruchom zadanie agenta z Telegram.
  2. Przenieś się do Discord, gdzie koordynujesz pracę.
  3. Wyślij `/dock_discord` z sesji Telegram.
  4. Zachowaj tę samą sesję OpenClaw, ale odbieraj przyszłe odpowiedzi w Discord.


## Wymagana konfiguracja

Dokowanie wymaga `session.identityLinks`. Nadawca źródłowy i docelowy peer muszą znajdować się w tej samej grupie tożsamości:

json5Copy code
[code]
    {  session: {    identityLinks: {      alice: ["telegram:123", "discord:456", "slack:U123"],    },  },}
[/code]

Wartości to identyfikatory peerów z prefiksem kanału:

Wartość | Znaczenie  
---|---  
`telegram:123` | identyfikator nadawcy Telegram `123`  
`discord:456` | identyfikator bezpośredniego peera Discord `456`  
`slack:U123` | identyfikator użytkownika Slack `U123`  
  
Klucz kanoniczny (`alice` powyżej) jest tylko wspólną nazwą grupy tożsamości. Polecenia dokowania używają wartości z prefiksem kanału, aby potwierdzić, że nadawca źródłowy i docelowy peer to ta sama osoba.

## Polecenia

Polecenia dokowania są generowane z załadowanych pluginów kanałów, które obsługują polecenia natywne. Obecne polecenia w pakiecie:

Kanał docelowy | Polecenie | Alias  
---|---|---  
Discord | `/dock-discord` | `/dock_discord`  
Mattermost | `/dock-mattermost` | `/dock_mattermost`  
Slack | `/dock-slack` | `/dock_slack`  
Telegram | `/dock-telegram` | `/dock_telegram`  
  
Aliasy z podkreśleniem są przydatne w natywnych powierzchniach poleceń, takich jak Telegram.

## Co się zmienia

Dokowanie aktualizuje pola dostarczania aktywnej sesji:

Pole sesji | Przykład po `/dock_discord`  
---|---  
`lastChannel` | `discord`  
`lastTo` | `456`  
`lastAccountId` | konto kanału docelowego albo `default`  
  
Te pola są utrwalane w magazynie sesji i używane przez późniejsze dostarczanie odpowiedzi dla tej sesji.

## Co się nie zmienia

Dokowanie nie:

  * tworzy kont kanałów
  * łączy nowego bota Discord, Telegram, Slack ani Mattermost
  * nadaje użytkownikowi dostępu
  * omija list dozwolonych kanałów ani zasad DM
  * przenosi historii transkryptu do innej sesji
  * sprawia, że niepowiązani użytkownicy współdzielą sesję


Zmienia tylko trasę dostarczania dla bieżącej sesji.

## Rozwiązywanie problemów

**Polecenie informuje, że nadawca nie jest powiązany.**

Dodaj zarówno bieżącego nadawcę, jak i docelowego peera do tej samej grupy `session.identityLinks`. Na przykład, jeśli nadawca Telegram `123` ma zostać zadokowany do peera Discord `456`, uwzględnij zarówno `telegram:123`, jak i `discord:456`.

**Polecenie informuje, że nie istnieje aktywna sesja.**

Dokuj z istniejącej sesji czatu bezpośredniego. Polecenie wymaga aktywnego wpisu sesji, aby mogło utrwalić nową trasę.

**Odpowiedzi nadal trafiają do starego kanału.**

Sprawdź, czy polecenie zwróciło komunikat powodzenia, i potwierdź, że identyfikator docelowego peera odpowiada identyfikatorowi używanemu przez ten kanał. Dokowanie zmienia tylko trasę aktywnej sesji; inna sesja może nadal kierować odpowiedzi gdzie indziej.

**Muszę przełączyć z powrotem.**

Wyślij pasujące polecenie dla pierwotnego kanału, takie jak `/dock_telegram` lub `/dock-telegram`, od powiązanego nadawcy.

Was this useful?YesNo