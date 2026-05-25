---
title: Tlon
source_url: https://docs.openclaw.ai/pl/channels/tlon
scraped_at: 2026-05-25
---

Tlon to zdecentralizowany komunikator zbudowany na Urbit. OpenClaw łączy się z Twoim statkiem Urbit i może odpowiadać na wiadomości prywatne oraz wiadomości czatu grupowego. Odpowiedzi w grupach domyślnie wymagają wzmianki @ i można je dodatkowo ograniczyć za pomocą list dozwolonych.

Status: wbudowany Plugin. Obsługiwane są wiadomości prywatne, wzmianki grupowe, odpowiedzi w wątkach, formatowanie tekstu sformatowanego oraz przesyłanie obrazów. Reakcje i ankiety nie są jeszcze obsługiwane.

## Wbudowany Plugin

Tlon jest dostarczany jako wbudowany Plugin w aktualnych wydaniach OpenClaw, więc zwykłe pakietowane kompilacje nie wymagają osobnej instalacji.

Jeśli używasz starszej kompilacji lub niestandardowej instalacji, która wyklucza Tlon, zainstaluj aktualny pakiet npm:

Instalacja przez CLI (rejestr npm):

bashCopy code
[code]
    openclaw plugins install @openclaw/tlon
[/code]

Użyj samego pakietu, aby śledzić aktualny oficjalny znacznik wydania. Przypnij dokładną wersję tylko wtedy, gdy potrzebujesz powtarzalnej instalacji.

Lokalny checkout (podczas uruchamiania z repozytorium git):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/tlon-plugin
[/code]

Szczegóły: [Pluginy](</pl/tools/plugin>)

## Konfiguracja

  1. Upewnij się, że Plugin Tlon jest dostępny. 
     * Aktualne pakietowane wydania OpenClaw już go zawierają.
     * Starsze/niestandardowe instalacje mogą dodać go ręcznie za pomocą powyższych poleceń.
  2. Zbierz adres URL statku i kod logowania.
  3. Skonfiguruj `channels.tlon`.
  4. Uruchom ponownie gateway.
  5. Wyślij wiadomość prywatną do bota albo wspomnij o nim w kanale grupowym.


Minimalna konfiguracja (jedno konto):

json5Copy code
[code]
    {  channels: {    tlon: {      enabled: true,      ship: "~sampel-palnet",      url: "https://your-ship-host",      code: "lidlut-tabwed-pillex-ridrup",      ownerShip: "~your-main-ship", // recommended: your ship, always allowed    },  },}
[/code]

## Prywatne statki/LAN

Domyślnie OpenClaw blokuje prywatne/wewnętrzne nazwy hostów i zakresy adresów IP w celu ochrony przed SSRF. Jeśli Twój statek działa w sieci prywatnej (localhost, adres IP LAN lub wewnętrzna nazwa hosta), musisz jawnie wyrazić na to zgodę:

json5Copy code
[code]
    {  channels: {    tlon: {      url: "http://localhost:8080",      allowPrivateNetwork: true,    },  },}
[/code]

Dotyczy to adresów URL takich jak:

  * `http://localhost:8080`
  * `http://192.168.x.x:8080`
  * `http://my-ship.local:8080`


⚠️ Włącz tę opcję tylko wtedy, gdy ufasz swojej sieci lokalnej. To ustawienie wyłącza zabezpieczenia SSRF dla żądań do adresu URL Twojego statku.

## Kanały grupowe

Automatyczne wykrywanie jest domyślnie włączone. Możesz też ręcznie przypiąć kanały:

json5Copy code
[code]
    {  channels: {    tlon: {      groupChannels: ["chat/~host-ship/general", "chat/~host-ship/support"],    },  },}
[/code]

Wyłącz automatyczne wykrywanie:

json5Copy code
[code]
    {  channels: {    tlon: {      autoDiscoverChannels: false,    },  },}
[/code]

## Kontrola dostępu

Lista dozwolonych wiadomości prywatnych (pusta = brak dozwolonych wiadomości prywatnych, użyj `ownerShip` dla przepływu zatwierdzania):

json5Copy code
[code]
    {  channels: {    tlon: {      dmAllowlist: ["~zod", "~nec"],    },  },}
[/code]

Autoryzacja grup (domyślnie ograniczona):

json5Copy code
[code]
    {  channels: {    tlon: {      defaultAuthorizedShips: ["~zod"],      authorization: {        channelRules: {          "chat/~host-ship/general": {            mode: "restricted",            allowedShips: ["~zod", "~nec"],          },          "chat/~host-ship/announcements": {            mode: "open",          },        },      },    },  },}
[/code]

## Właściciel i system zatwierdzania

Ustaw statek właściciela, aby otrzymywać prośby o zatwierdzenie, gdy nieautoryzowani użytkownicy próbują wejść w interakcję:

json5Copy code
[code]
    {  channels: {    tlon: {      ownerShip: "~your-main-ship",    },  },}
[/code]

Statek właściciela jest **automatycznie autoryzowany wszędzie** — zaproszenia do wiadomości prywatnych są automatycznie akceptowane, a wiadomości na kanałach są zawsze dozwolone. Nie musisz dodawać właściciela do `dmAllowlist` ani `defaultAuthorizedShips`.

Po ustawieniu właściciel otrzymuje powiadomienia w wiadomościach prywatnych dla:

  * Próśb o wiadomość prywatną od statków spoza listy dozwolonych
  * Wzmianek na kanałach bez autoryzacji
  * Próśb o zaproszenie do grupy


## Ustawienia automatycznej akceptacji

Automatycznie akceptuj zaproszenia do wiadomości prywatnych (dla statków w dmAllowlist):

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptDmInvites: true,    },  },}
[/code]

Automatycznie akceptuj zaproszenia do grup od zaufanych statków:

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptGroupInvites: true,      groupInviteAllowlist: ["~zod"],    },  },}
[/code]

`autoAcceptGroupInvites` domyślnie odmawia, gdy `groupInviteAllowlist` jest pusta. Ustaw listę dozwolonych na statki, których zaproszenia do grup mają być akceptowane automatycznie.

## Cele dostarczania (CLI/Cron)

Używaj ich z `openclaw message send` lub dostarczaniem Cron:

  * Wiadomość prywatna: `~sampel-palnet` lub `dm/~sampel-palnet`
  * Grupa: `chat/~host-ship/channel` lub `group:~host-ship/channel`


## Wbudowana umiejętność

Plugin Tlon zawiera wbudowaną umiejętność ([`@tloncorp/tlon-skill`](<https://github.com/tloncorp/tlon-skill>)), która zapewnia dostęp z CLI do operacji Tlon:

  * **Kontakty** : pobieranie/aktualizowanie profili, wyświetlanie listy kontaktów
  * **Kanały** : wyświetlanie listy, tworzenie, publikowanie wiadomości, pobieranie historii
  * **Grupy** : wyświetlanie listy, tworzenie, zarządzanie członkami
  * **Wiadomości prywatne** : wysyłanie wiadomości, reagowanie na wiadomości
  * **Reakcje** : dodawanie/usuwanie reakcji emoji do postów i wiadomości prywatnych
  * **Ustawienia** : zarządzanie uprawnieniami Plugin za pomocą poleceń ukośnikiem


Umiejętność jest automatycznie dostępna po zainstalowaniu Plugin.

## Możliwości

Funkcja | Status  
---|---  
Wiadomości bezpośrednie | ✅ Obsługiwane  
Grupy/kanały | ✅ Obsługiwane (domyślnie wymagają wzmianki)  
Wątki | ✅ Obsługiwane (automatyczne odpowiedzi w wątku)  
Tekst sformatowany | ✅ Markdown konwertowany do formatu Tlon  
Obrazy | ✅ Przesyłane do magazynu Tlon  
Reakcje | ✅ Przez wbudowaną umiejętność  
Ankiety | ❌ Jeszcze nieobsługiwane  
Polecenia natywne | ✅ Obsługiwane (domyślnie tylko dla właściciela)  
  
## Rozwiązywanie problemów

Najpierw uruchom tę sekwencję:

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctor
[/code]

Typowe awarie:

  * **Wiadomości prywatne ignorowane** : nadawca nie znajduje się w `dmAllowlist` i nie skonfigurowano `ownerShip` dla przepływu zatwierdzania.
  * **Wiadomości grupowe ignorowane** : kanał nie został wykryty albo nadawca nie jest autoryzowany.
  * **Błędy połączenia** : sprawdź, czy adres URL statku jest osiągalny; włącz `allowPrivateNetwork` dla lokalnych statków.
  * **Błędy uwierzytelniania** : sprawdź, czy kod logowania jest aktualny (kody rotują).


## Dokumentacja konfiguracji

Pełna konfiguracja: [Konfiguracja](</pl/gateway/configuration>)

Opcje dostawcy:

  * `channels.tlon.enabled`: włącza/wyłącza uruchamianie kanału.
  * `channels.tlon.ship`: nazwa statku Urbit bota (np. `~sampel-palnet`).
  * `channels.tlon.url`: adres URL statku (np. `https://sampel-palnet.tlon.network`).
  * `channels.tlon.code`: kod logowania statku.
  * `channels.tlon.allowPrivateNetwork`: zezwalaj na adresy URL localhost/LAN (obejście SSRF).
  * `channels.tlon.ownerShip`: statek właściciela dla systemu zatwierdzania (zawsze autoryzowany).
  * `channels.tlon.dmAllowlist`: statki, które mogą wysyłać wiadomości prywatne (puste = brak).
  * `channels.tlon.autoAcceptDmInvites`: automatycznie akceptuj wiadomości prywatne od statków z listy dozwolonych.
  * `channels.tlon.autoAcceptGroupInvites`: automatycznie akceptuj zaproszenia do grup od statków z listy dozwolonych.
  * `channels.tlon.groupInviteAllowlist`: statki, których zaproszenia do grup mogą być automatycznie akceptowane.
  * `channels.tlon.autoDiscoverChannels`: automatycznie wykrywaj kanały grupowe (domyślnie: true).
  * `channels.tlon.groupChannels`: ręcznie przypięte gniazda kanałów.
  * `channels.tlon.defaultAuthorizedShips`: statki autoryzowane dla wszystkich kanałów.
  * `channels.tlon.authorization.channelRules`: reguły autoryzacji dla poszczególnych kanałów.
  * `channels.tlon.showModelSignature`: dołącz nazwę modelu do wiadomości.


## Uwagi

  * Odpowiedzi grupowe wymagają wzmianki (np. `~your-bot-ship`), aby odpowiedzieć.
  * Odpowiedzi w wątku: jeśli przychodząca wiadomość jest w wątku, OpenClaw odpowiada w wątku.
  * Tekst sformatowany: formatowanie Markdown (pogrubienie, kursywa, kod, nagłówki, listy) jest konwertowane do natywnego formatu Tlon.
  * Obrazy: adresy URL są przesyłane do magazynu Tlon i osadzane jako bloki obrazów.


## Powiązane

  * [Przegląd kanałów](</pl/channels>) — wszystkie obsługiwane kanały
  * [Parowanie](</pl/channels/pairing>) — uwierzytelnianie wiadomości prywatnych i przepływ parowania
  * [Grupy](</pl/channels/groups>) — zachowanie czatu grupowego i wymaganie wzmianki
  * [Routing kanałów](</pl/channels/channel-routing>) — routing sesji dla wiadomości
  * [Bezpieczeństwo](</pl/gateway/security>) — model dostępu i utwardzanie


Was this useful?YesNo