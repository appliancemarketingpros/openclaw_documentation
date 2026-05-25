---
title: Nostr
source_url: https://docs.openclaw.ai/pl/channels/nostr
scraped_at: 2026-05-25
---

**Status:** Opcjonalny dołączony Plugin (domyślnie wyłączony do czasu skonfigurowania).

Nostr to zdecentralizowany protokół sieci społecznościowych. Ten kanał umożliwia OpenClaw odbieranie zaszyfrowanych wiadomości bezpośrednich (DM) i odpowiadanie na nie przez NIP-04.

## Dołączony Plugin

Bieżące wydania OpenClaw dostarczają Nostr jako dołączony Plugin, więc zwykłe spakowane kompilacje nie wymagają osobnej instalacji.

### Starsze/niestandardowe instalacje

  * Onboarding (`openclaw onboard`) oraz `openclaw channels add` nadal pokazują Nostr ze współdzielonego katalogu kanałów.
  * Jeśli Twoja kompilacja wyklucza dołączony Nostr, zainstaluj pakiet npm bezpośrednio.

bashCopy code
[code]
    openclaw plugins install @openclaw/nostr
[/code]

Użyj samego pakietu, aby śledzić bieżący oficjalny tag wydania. Przypnij dokładną wersję tylko wtedy, gdy potrzebujesz powtarzalnej instalacji.

Użyj lokalnej kopii roboczej (przepływy deweloperskie):

bashCopy code
[code]
    openclaw plugins install --link <path-to-local-nostr-plugin>
[/code]

Uruchom ponownie Gateway po zainstalowaniu lub włączeniu pluginów.

### Konfiguracja nieinteraktywna

bashCopy code
[code]
    openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY"openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY" --relay-urls "wss://relay.damus.io,wss://relay.primal.net"
[/code]

Użyj `--use-env`, aby zachować `NOSTR_PRIVATE_KEY` w środowisku zamiast przechowywać klucz w konfiguracji.

## Szybka konfiguracja

  1. Wygeneruj parę kluczy Nostr (jeśli potrzebna):

bashCopy code
[code]
    # Using naknak key generate
[/code]

  2. Dodaj do konfiguracji:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",    },  },}
[/code]

  3. Wyeksportuj klucz:

bashCopy code
[code]
    export NOSTR_PRIVATE_KEY="nsec1..."
[/code]

  4. Uruchom ponownie Gateway.


## Dokumentacja konfiguracji

Klucz | Typ | Domyślnie | Opis  
---|---|---|---  
`privateKey` | string | wymagane | Klucz prywatny w formacie `nsec` lub hex  
`relays` | string[] | `['wss://relay.damus.io', 'wss://nos.lol']` | Adresy URL przekaźników (WebSocket)  
`dmPolicy` | string | `pairing` | Zasady dostępu do DM  
`allowFrom` | string[] | `[]` | Dozwolone klucze publiczne nadawców  
`enabled` | boolean | `true` | Włącz/wyłącz kanał  
`name` | string | - | Nazwa wyświetlana  
`profile` | object | - | Metadane profilu NIP-01  
  
## Metadane profilu

Dane profilu są publikowane jako zdarzenie NIP-01 `kind:0`. Możesz zarządzać nimi z Control UI (Channels -> Nostr -> Profile) albo ustawić je bezpośrednio w konfiguracji.

Przykład:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      profile: {        name: "openclaw",        displayName: "OpenClaw",        about: "Personal assistant DM bot",        picture: "https://example.com/avatar.png",        banner: "https://example.com/banner.png",        website: "https://example.com",        nip05: "openclaw@example.com",        lud16: "openclaw@example.com",      },    },  },}
[/code]

Uwagi:

  * Adresy URL profilu muszą używać `https://`.
  * Importowanie z przekaźników scala pola i zachowuje lokalne nadpisania.


## Kontrola dostępu

### Zasady DM

  * **pairing** (domyślnie): nieznani nadawcy otrzymują kod parowania.
  * **allowlist** : DM mogą wysyłać tylko klucze publiczne z `allowFrom`.
  * **open** : publiczne przychodzące DM (wymaga `allowFrom: ["*"]`).
  * **disabled** : ignoruj przychodzące DM.


Uwagi dotyczące wymuszania:

  * Podpisy zdarzeń przychodzących są weryfikowane przed zasadami nadawcy i odszyfrowaniem NIP-04, więc sfałszowane zdarzenia są odrzucane wcześnie.
  * Odpowiedzi parowania są wysyłane bez przetwarzania pierwotnej treści DM.
  * Przychodzące DM są ograniczane limitem szybkości, a zbyt duże ładunki są odrzucane przed odszyfrowaniem.


### Przykład allowlist

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      dmPolicy: "allowlist",      allowFrom: ["npub1abc...", "npub1xyz..."],    },  },}
[/code]

## Formaty kluczy

Akceptowane formaty:

  * **Klucz prywatny:** `nsec...` lub 64-znakowy hex
  * **Klucze publiczne (`allowFrom`):** `npub...` lub hex


## Przekaźniki

Domyślnie: `relay.damus.io` i `nos.lol`.

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["wss://relay.damus.io", "wss://relay.primal.net", "wss://nostr.wine"],    },  },}
[/code]

Wskazówki:

  * Używaj 2-3 przekaźników dla redundancji.
  * Unikaj zbyt wielu przekaźników (opóźnienia, duplikacja).
  * Płatne przekaźniki mogą poprawić niezawodność.
  * Lokalne przekaźniki dobrze sprawdzają się w testach (`ws://localhost:7777`).


## Obsługa protokołu

NIP | Status | Opis  
---|---|---  
NIP-01 | Obsługiwane | Podstawowy format zdarzeń + metadane profilu  
NIP-04 | Obsługiwane | Szyfrowane DM (`kind:4`)  
NIP-17 | Planowane | DM w opakowaniu prezentowym  
NIP-44 | Planowane | Szyfrowanie wersjonowane  
  
## Testowanie

### Lokalny przekaźnik

bashCopy code
[code]
    # Start strfrydocker run -p 7777:7777 ghcr.io/hoytech/strfry
[/code]

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["ws://localhost:7777"],    },  },}
[/code]

### Test ręczny

  1. Zanotuj klucz publiczny bota (npub) z logów.
  2. Otwórz klienta Nostr (Damus, Amethyst itd.).
  3. Wyślij DM na klucz publiczny bota.
  4. Zweryfikuj odpowiedź.


## Rozwiązywanie problemów

### Wiadomości nie są odbierane

  * Zweryfikuj, czy klucz prywatny jest prawidłowy.
  * Upewnij się, że adresy URL przekaźników są osiągalne i używają `wss://` (lub `ws://` lokalnie).
  * Potwierdź, że `enabled` nie ma wartości `false`.
  * Sprawdź logi Gateway pod kątem błędów połączeń z przekaźnikami.


### Odpowiedzi nie są wysyłane

  * Sprawdź, czy przekaźnik akceptuje zapisy.
  * Zweryfikuj łączność wychodzącą.
  * Uważaj na limity szybkości przekaźników.


### Zduplikowane odpowiedzi

  * Oczekiwane przy używaniu wielu przekaźników.
  * Wiadomości są deduplikowane według identyfikatora zdarzenia; tylko pierwsze dostarczenie wywołuje odpowiedź.


## Bezpieczeństwo

  * Nigdy nie commituj kluczy prywatnych.
  * Używaj zmiennych środowiskowych dla kluczy.
  * Rozważ `allowlist` dla botów produkcyjnych.
  * Podpisy są weryfikowane przed zasadami nadawcy, a zasady nadawcy są wymuszane przed odszyfrowaniem, więc sfałszowane zdarzenia są odrzucane wcześnie, a nieznani nadawcy nie mogą wymusić pełnej pracy kryptograficznej.


## Ograniczenia (MVP)

  * Tylko wiadomości bezpośrednie (bez czatów grupowych).
  * Brak załączników multimedialnych.
  * Tylko NIP-04 (planowany gift-wrap NIP-17).


## Powiązane

  * [Przegląd kanałów](</pl/channels>) — wszystkie obsługiwane kanały
  * [Parowanie](</pl/channels/pairing>) — uwierzytelnianie DM i przepływ parowania
  * [Grupy](</pl/channels/groups>) — zachowanie czatu grupowego i kontrola wzmianek
  * [Routing kanałów](</pl/channels/channel-routing>) — routing sesji dla wiadomości
  * [Bezpieczeństwo](</pl/gateway/security>) — model dostępu i utwardzanie


Was this useful?YesNo