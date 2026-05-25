---
title: Twitch
source_url: https://docs.openclaw.ai/pl/channels/twitch
scraped_at: 2026-05-25
---

Obsługa czatu Twitch przez połączenie IRC. OpenClaw łączy się jako użytkownik Twitch (konto bota), aby odbierać i wysyłać wiadomości na kanałach.

## Dołączony Plugin

Jeśli używasz starszej kompilacji albo instalacji niestandardowej, która wyklucza Twitch, zainstaluj pakiet npm bezpośrednio:

### rejestr npm

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### Lokalny checkout

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

Użyj samego pakietu, aby podążać za bieżącym oficjalnym tagiem wydania. Przypnij dokładną wersję tylko wtedy, gdy potrzebujesz odtwarzalnej instalacji.

Szczegóły: [Pluginy](</pl/tools/plugin>)

## Szybka konfiguracja (dla początkujących)

* ### Upewnij się, że Plugin jest dostępny

Bieżące pakietowe wydania OpenClaw już go zawierają. Starsze/niestandardowe instalacje mogą dodać go ręcznie za pomocą powyższych poleceń.

* ### Utwórz konto bota Twitch

Utwórz dedykowane konto Twitch dla bota (albo użyj istniejącego konta).

* ### Wygeneruj dane uwierzytelniające

Użyj [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Wybierz **Bot Token**
  * Sprawdź, czy wybrane są zakresy `chat:read` i `chat:write`
  * Skopiuj **Client ID** i **Access Token**


* ### Znajdź swój identyfikator użytkownika Twitch

Użyj <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/>, aby przekonwertować nazwę użytkownika na identyfikator użytkownika Twitch.

* ### Skonfiguruj token

  * Env: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (tylko konto domyślne)
  * Albo konfiguracja: `channels.twitch.accessToken`


Jeśli ustawiono oba, konfiguracja ma pierwszeństwo (awaryjne użycie env dotyczy tylko konta domyślnego).

* ### Uruchom gateway

Uruchom gateway ze skonfigurowanym kanałem.

Minimalna konfiguracja:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## Czym to jest

  * Kanał Twitch należący do Gateway.
  * Deterministyczne kierowanie: odpowiedzi zawsze wracają do Twitch.
  * Każde konto mapuje się na izolowany klucz sesji `agent:<agentId>:twitch:<accountName>`.
  * `username` to konto bota (to, które się uwierzytelnia), a `channel` to pokój czatu, do którego należy dołączyć.


## Konfiguracja (szczegółowa)

### Wygeneruj dane uwierzytelniające

Użyj [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Wybierz **Bot Token**
  * Sprawdź, czy wybrane są zakresy `chat:read` i `chat:write`
  * Skopiuj **Client ID** i **Access Token**


### Skonfiguruj bota

### Zmienna env (tylko konto domyślne)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Konfiguracja

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

Jeśli ustawiono zarówno env, jak i konfigurację, konfiguracja ma pierwszeństwo.

### Kontrola dostępu (zalecana)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

Preferuj `allowFrom` jako ścisłą listę dozwolonych. Zamiast tego użyj `allowedRoles`, jeśli chcesz kontroli dostępu opartej na rolach.

**Dostępne role:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## Odświeżanie tokenu (opcjonalne)

Tokenów z [Twitch Token Generator](<https://twitchtokengenerator.com/>) nie można odświeżać automatycznie - wygeneruj je ponownie po wygaśnięciu.

Aby automatycznie odświeżać token, utwórz własną aplikację Twitch w [Twitch Developer Console](<https://dev.twitch.tv/console>) i dodaj do konfiguracji:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

Bot automatycznie odświeża tokeny przed wygaśnięciem i zapisuje zdarzenia odświeżania w logach.

## Obsługa wielu kont

Użyj `channels.twitch.accounts` z tokenami dla poszczególnych kont. Wspólny wzorzec opisano w sekcji [Konfiguracja](</pl/gateway/configuration>).

Przykład (jedno konto bota na dwóch kanałach):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## Kontrola dostępu

### Lista dozwolonych identyfikatorów użytkowników (najbezpieczniejsza)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### Oparta na rolach

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` to ścisła lista dozwolonych. Gdy jest ustawiona, dozwolone są tylko te identyfikatory użytkowników. Jeśli chcesz dostępu opartego na rolach, pozostaw `allowFrom` nieustawione i zamiast tego skonfiguruj `allowedRoles`.

### Wyłącz wymaganie @wzmianki

Domyślnie `requireMention` ma wartość `true`. Aby wyłączyć to ustawienie i odpowiadać na wszystkie wiadomości:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## Rozwiązywanie problemów

Najpierw uruchom polecenia diagnostyczne:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

Bot nie odpowiada na wiadomości

  * **Sprawdź kontrolę dostępu:** Upewnij się, że Twój identyfikator użytkownika znajduje się w `allowFrom`, albo tymczasowo usuń `allowFrom` i ustaw `allowedRoles: ["all"]`, aby przetestować.
  * **Sprawdź, czy bot jest na kanale:** Bot musi dołączyć do kanału określonego w `channel`.

Problemy z tokenem

"Nie udało się połączyć" lub błędy uwierzytelniania:

  * Sprawdź, czy `accessToken` jest wartością tokenu dostępu OAuth (zwykle zaczyna się od prefiksu `oauth:`)
  * Sprawdź, czy token ma zakresy `chat:read` i `chat:write`
  * Jeśli używasz odświeżania tokenu, sprawdź, czy ustawiono `clientSecret` i `refreshToken`

Odświeżanie tokenu nie działa

Sprawdź logi pod kątem zdarzeń odświeżania:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

Jeśli widzisz "token refresh disabled (no refresh token)":

  * Upewnij się, że podano `clientSecret`
  * Upewnij się, że podano `refreshToken`


## Konfiguracja

### Konfiguracja konta

Nazwa użytkownika bota.

Token dostępu OAuth z `chat:read` i `chat:write`.

Twitch Client ID (z Token Generator lub Twojej aplikacji).

Kanał, do którego należy dołączyć.

Włącz to konto.

Opcjonalnie: do automatycznego odświeżania tokenu.

Opcjonalnie: do automatycznego odświeżania tokenu.

Wygaśnięcie tokenu w sekundach.

Znacznik czasu uzyskania tokenu.

Lista dozwolonych identyfikatorów użytkowników.

Wymagaj @wzmianki.

### Opcje dostawcy

  * `channels.twitch.enabled` \- Włącz/wyłącz uruchamianie kanału
  * `channels.twitch.username` \- Nazwa użytkownika bota (uproszczona konfiguracja jednego konta)
  * `channels.twitch.accessToken` \- Token dostępu OAuth (uproszczona konfiguracja jednego konta)
  * `channels.twitch.clientId` \- Twitch Client ID (uproszczona konfiguracja jednego konta)
  * `channels.twitch.channel` \- Kanał, do którego należy dołączyć (uproszczona konfiguracja jednego konta)
  * `channels.twitch.accounts.<accountName>` \- Konfiguracja wielu kont (wszystkie pola konta powyżej)


Pełny przykład:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## Akcje narzędzia

Agent może wywołać `twitch` z akcją:

  * `send` \- Wyślij wiadomość do kanału


Przykład:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## Bezpieczeństwo i operacje

  * **Traktuj tokeny jak hasła** — nigdy nie commituj tokenów do git.
  * **Używaj automatycznego odświeżania tokenów** dla długo działających botów.
  * **Używaj list dozwolonych identyfikatorów użytkowników** zamiast nazw użytkowników do kontroli dostępu.
  * **Monitoruj logi** pod kątem zdarzeń odświeżania tokenu i stanu połączenia.
  * **Ogranicz zakres tokenów do minimum** — żądaj tylko `chat:read` i `chat:write`.
  * **Jeśli utkniesz** : uruchom ponownie gateway po potwierdzeniu, że żaden inny proces nie jest właścicielem sesji.


## Limity

  * **500 znaków** na wiadomość (automatycznie dzielone na fragmenty na granicach słów).
  * Markdown jest usuwany przed dzieleniem na fragmenty.
  * Brak ograniczania częstotliwości (używa wbudowanych limitów Twitch).


## Powiązane

  * [Kierowanie kanałów](</pl/channels/channel-routing>) — kierowanie sesji dla wiadomości
  * [Omówienie kanałów](</pl/channels>) — wszystkie obsługiwane kanały
  * [Grupy](</pl/channels/groups>) — zachowanie czatu grupowego i bramkowanie wzmianek
  * [Parowanie](</pl/channels/pairing>) — uwierzytelnianie DM i przepływ parowania
  * [Bezpieczeństwo](</pl/gateway/security>) — model dostępu i utwardzanie


Was this useful?YesNo