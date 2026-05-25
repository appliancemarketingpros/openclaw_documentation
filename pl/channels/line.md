---
title: WIERSZ
source_url: https://docs.openclaw.ai/pl/channels/line
scraped_at: 2026-05-25
---

LINE łączy się z OpenClaw przez LINE Messaging API. Plugin działa jako odbiornik webhooków na Gateway i używa tokenu dostępu kanału oraz sekretu kanału do uwierzytelniania.

Status: Plugin do pobrania. Obsługiwane są wiadomości bezpośrednie, czaty grupowe, multimedia, lokalizacje, wiadomości Flex, wiadomości szablonowe i szybkie odpowiedzi. Reakcje i wątki nie są obsługiwane.

## Instalacja

Zainstaluj LINE przed skonfigurowaniem kanału:

bashCopy code
[code]
    openclaw plugins install @openclaw/line
[/code]

Lokalny checkout (podczas uruchamiania z repozytorium git):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/line-plugin
[/code]

## Konfiguracja

  1. Utwórz konto LINE Developers i otwórz Console: <https://developers.line.biz/console/>
  2. Utwórz (lub wybierz) Provider i dodaj kanał **Messaging API**.
  3. Skopiuj **token dostępu kanału** i **sekret kanału** z ustawień kanału.
  4. Włącz **Użyj webhooka** w ustawieniach Messaging API.
  5. Ustaw URL webhooka na punkt końcowy Gateway (wymagany HTTPS):

CodeCopy code
[code]
    https://gateway-host/line/webhook
[/code]

Gateway odpowiada na weryfikację webhooka LINE (GET) i zdarzenia przychodzące (POST). Jeśli potrzebujesz niestandardowej ścieżki, ustaw `channels.line.webhookPath` lub `channels.line.accounts.<id>.webhookPath` i odpowiednio zaktualizuj URL.

Uwaga dotycząca bezpieczeństwa:

  * Weryfikacja podpisu LINE zależy od treści żądania (HMAC na surowej treści), więc OpenClaw stosuje ścisłe limity treści przed uwierzytelnieniem oraz limit czasu przed weryfikacją.
  * OpenClaw przetwarza zdarzenia webhooka ze zweryfikowanych surowych bajtów żądania. Wartości `req.body` przekształcone przez middleware wyższego poziomu są ignorowane dla bezpieczeństwa integralności podpisu.


## Konfigurowanie

Minimalna konfiguracja:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "pairing",    },  },}
[/code]

Publiczna konfiguracja wiadomości DM:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "open",      allowFrom: ["*"],    },  },}
[/code]

Zmienne środowiskowe (tylko konto domyślne):

  * `LINE_CHANNEL_ACCESS_TOKEN`
  * `LINE_CHANNEL_SECRET`


Pliki tokenu/sekretu:

json5Copy code
[code]
    {  channels: {    line: {      tokenFile: "/path/to/line-token.txt",      secretFile: "/path/to/line-secret.txt",    },  },}
[/code]

`tokenFile` i `secretFile` muszą wskazywać zwykłe pliki. Dowiązania symboliczne są odrzucane.

Wiele kont:

json5Copy code
[code]
    {  channels: {    line: {      accounts: {        marketing: {          channelAccessToken: "...",          channelSecret: "...",          webhookPath: "/line/marketing",        },      },    },  },}
[/code]

## Kontrola dostępu

Wiadomości bezpośrednie domyślnie używają parowania. Nieznani nadawcy otrzymują kod parowania, a ich wiadomości są ignorowane do czasu zatwierdzenia.

bashCopy code
[code]
    openclaw pairing list lineopenclaw pairing approve line &lt;CODE&gt;
[/code]

Listy dozwolonych i zasady:

  * `channels.line.dmPolicy`: `pairing | allowlist | open | disabled`
  * `channels.line.allowFrom`: dozwolone identyfikatory użytkowników LINE dla wiadomości DM; `dmPolicy: "open"` wymaga `["*"]`
  * `channels.line.groupPolicy`: `allowlist | open | disabled`
  * `channels.line.groupAllowFrom`: dozwolone identyfikatory użytkowników LINE dla grup
  * Nadpisania dla grup: `channels.line.groups.<groupId>.allowFrom`
  * Statyczne grupy dostępu nadawców można wskazywać z `allowFrom`, `groupAllowFrom` i grupowego `allowFrom` za pomocą `accessGroup:<name>`.
  * Uwaga dotycząca działania: jeśli `channels.line` całkowicie brakuje, środowisko uruchomieniowe cofa się do `groupPolicy="allowlist"` dla sprawdzeń grup (nawet jeśli ustawiono `channels.defaults.groupPolicy`).


Identyfikatory LINE uwzględniają wielkość liter. Poprawne identyfikatory wyglądają tak:

  * Użytkownik: `U` \+ 32 znaki szesnastkowe
  * Grupa: `C` \+ 32 znaki szesnastkowe
  * Pokój: `R` \+ 32 znaki szesnastkowe


## Zachowanie wiadomości

  * Tekst jest dzielony na fragmenty po 5000 znaków.
  * Formatowanie Markdown jest usuwane; bloki kodu i tabele są konwertowane na karty Flex, gdy to możliwe.
  * Odpowiedzi strumieniowe są buforowane; LINE otrzymuje pełne fragmenty z animacją ładowania, gdy agent pracuje.
  * Pobieranie multimediów jest ograniczone przez `channels.line.mediaMaxMb` (domyślnie 10).
  * Multimedia przychodzące są zapisywane w `~/.openclaw/media/inbound/`, zanim zostaną przekazane do agenta, zgodnie ze wspólnym magazynem multimediów używanym przez inne dołączone pluginy kanałów.


## Dane kanału (wiadomości rozszerzone)

Użyj `channelData.line`, aby wysyłać szybkie odpowiedzi, lokalizacje, karty Flex lub wiadomości szablonowe.

json5Copy code
[code]
    {  text: "Here you go",  channelData: {    line: {      quickReplies: ["Status", "Help"],      location: {        title: "Office",        address: "123 Main St",        latitude: 35.681236,        longitude: 139.767125,      },      flexMessage: {        altText: "Status card",        contents: {          /* Flex payload */        },      },      templateMessage: {        type: "confirm",        text: "Proceed?",        confirmLabel: "Yes",        confirmData: "yes",        cancelLabel: "No",        cancelData: "no",      },    },  },}
[/code]

Plugin LINE zawiera również polecenie `/card` dla presetów wiadomości Flex:

CodeCopy code
[code]
    /card info "Welcome" "Thanks for joining!"
[/code]

## Obsługa ACP

LINE obsługuje powiązania konwersacji ACP (Agent Communication Protocol):

  * `/acp spawn <agent> --bind here` wiąże bieżący czat LINE z sesją ACP bez tworzenia wątku potomnego.
  * Skonfigurowane powiązania ACP i aktywne sesje ACP powiązane z konwersacją działają w LINE tak jak w innych kanałach konwersacji.


Szczegóły znajdziesz w [agentach ACP](</pl/tools/acp-agents>).

## Multimedia wychodzące

Plugin LINE obsługuje wysyłanie obrazów, filmów i plików audio przez narzędzie wiadomości agenta. Multimedia są wysyłane przez ścieżkę dostarczania właściwą dla LINE z odpowiednią obsługą podglądu i śledzenia:

  * **Obrazy** : wysyłane jako wiadomości obrazów LINE z automatycznym generowaniem podglądu.
  * **Filmy** : wysyłane z jawną obsługą podglądu i typu zawartości.
  * **Audio** : wysyłane jako wiadomości audio LINE.


Adresy URL multimediów wychodzących muszą być publicznymi adresami HTTPS. OpenClaw weryfikuje docelową nazwę hosta przed przekazaniem URL do LINE i odrzuca cele local loopback, link-local oraz sieci prywatnych.

Ogólne wysyłanie multimediów cofa się do istniejącej ścieżki tylko dla obrazów, gdy ścieżka właściwa dla LINE nie jest dostępna.

## Rozwiązywanie problemów

  * **Weryfikacja webhooka kończy się niepowodzeniem:** upewnij się, że URL webhooka używa HTTPS, a `channelSecret` odpowiada wartości w konsoli LINE.
  * **Brak zdarzeń przychodzących:** potwierdź, że ścieżka webhooka odpowiada `channels.line.webhookPath` i że Gateway jest osiągalny z LINE.
  * **Błędy pobierania multimediów:** zwiększ `channels.line.mediaMaxMb`, jeśli multimedia przekraczają domyślny limit.


## Powiązane

  * [Przegląd kanałów](</pl/channels>) — wszystkie obsługiwane kanały
  * [Parowanie](</pl/channels/pairing>) — uwierzytelnianie wiadomości DM i przepływ parowania
  * [Grupy](</pl/channels/groups>) — zachowanie czatu grupowego i bramkowanie wzmianek
  * [Routing kanałów](</pl/channels/channel-routing>) — routing sesji dla wiadomości
  * [Bezpieczeństwo](</pl/gateway/security>) — model dostępu i utwardzanie


Was this useful?YesNo