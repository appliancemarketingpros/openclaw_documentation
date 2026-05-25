---
title: Yuanbao
source_url: https://docs.openclaw.ai/pl/channels/yuanbao
scraped_at: 2026-05-25
---

Tencent Yuanbao to platforma asystenta AI firmy Tencent. Plugin kanału OpenClaw łączy boty Yuanbao z OpenClaw przez WebSocket, aby mogły komunikować się z użytkownikami przez wiadomości bezpośrednie i czaty grupowe.

**Status:** gotowe do użycia produkcyjnego dla DM botów + czatów grupowych. WebSocket jest jedynym obsługiwanym trybem połączenia.

* * *

## Szybki start

> **Wymaga OpenClaw 2026.4.10 lub nowszej wersji.** Uruchom `openclaw --version`, aby sprawdzić wersję. Zaktualizuj za pomocą `openclaw update`.

* ### Dodaj kanał Yuanbao ze swoimi poświadczeniami

bashCopy code
[code]
    openclaw channels add --channel yuanbao --token "appKey:appSecret"
[/code]

Wartość `--token` używa formatu `appKey:appSecret` rozdzielonego dwukropkiem. Możesz uzyskać te dane z aplikacji Yuanbao, tworząc robota w ustawieniach swojej aplikacji.

* ### Po zakończeniu konfiguracji uruchom ponownie Gateway, aby zastosować zmiany

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Konfiguracja interaktywna (alternatywa)

Możesz też użyć interaktywnego kreatora:

bashCopy code
[code]
    openclaw channels login --channel yuanbao
[/code]

Postępuj zgodnie z monitami, aby wprowadzić App ID i App Secret.

* * *

## Kontrola dostępu

### Wiadomości bezpośrednie

Skonfiguruj `dmPolicy`, aby kontrolować, kto może wysyłać DM do bota:

  * `"pairing"` \- nieznani użytkownicy otrzymują kod parowania; zatwierdź przez CLI
  * `"allowlist"` \- czatować mogą tylko użytkownicy wymienieni w `allowFrom`
  * `"open"` \- zezwól wszystkim użytkownikom (domyślnie)
  * `"disabled"` \- wyłącz wszystkie DM


**Zatwierdzanie prośby o parowanie:**

bashCopy code
[code]
    openclaw pairing list yuanbaoopenclaw pairing approve yuanbao &lt;CODE&gt;
[/code]

### Czaty grupowe

**Wymaganie wzmianki** (`channels.yuanbao.requireMention`):

  * `true` \- wymagaj @wzmianki (domyślnie)
  * `false` \- odpowiadaj bez @wzmianki


Odpowiedź na wiadomość bota w czacie grupowym jest traktowana jako niejawna wzmianka.

* * *

## Przykłady konfiguracji

### Podstawowa konfiguracja z otwartą zasadą DM

json5Copy code
[code]
    {  channels: {    yuanbao: {      appKey: "your_app_key",      appSecret: "your_app_secret",      dm: {        policy: "open",      },    },  },}
[/code]

### Ogranicz DM do konkretnych użytkowników

json5Copy code
[code]
    {  channels: {    yuanbao: {      appKey: "your_app_key",      appSecret: "your_app_secret",      dm: {        policy: "allowlist",        allowFrom: ["user_id_1", "user_id_2"],      },    },  },}
[/code]

### Wyłącz wymaganie @wzmianki w grupach

json5Copy code
[code]
    {  channels: {    yuanbao: {      requireMention: false,    },  },}
[/code]

### Optymalizuj dostarczanie wiadomości wychodzących

json5Copy code
[code]
    {  channels: {    yuanbao: {      // Send each chunk immediately without buffering      outboundQueueStrategy: "immediate",    },  },}
[/code]

### Dostrój strategię merge-text

json5Copy code
[code]
    {  channels: {    yuanbao: {      outboundQueueStrategy: "merge-text",      minChars: 2800, // buffer until this many chars      maxChars: 3000, // force split above this limit      idleMs: 5000, // auto-flush after idle timeout (ms)    },  },}
[/code]

* * *

## Typowe polecenia

Polecenie | Opis  
---|---  
`/help` | Pokaż dostępne polecenia  
`/status` | Pokaż status bota  
`/new` | Rozpocznij nową sesję  
`/stop` | Zatrzymaj bieżące uruchomienie  
`/restart` | Uruchom ponownie OpenClaw  
`/compact` | Skompaktuj kontekst sesji  
  
> Yuanbao obsługuje natywne menu poleceń ukośnikowych. Polecenia są automatycznie synchronizowane z platformą po uruchomieniu Gateway.

* * *

## Rozwiązywanie problemów

### Bot nie odpowiada w czatach grupowych

  1. Upewnij się, że bot został dodany do grupy
  2. Upewnij się, że używasz @wzmianki o bocie (domyślnie wymagane)
  3. Sprawdź logi: `openclaw logs --follow`


### Bot nie odbiera wiadomości

  1. Upewnij się, że bot został utworzony i zatwierdzony w aplikacji Yuanbao
  2. Upewnij się, że `appKey` i `appSecret` są poprawnie skonfigurowane
  3. Upewnij się, że Gateway działa: `openclaw gateway status`
  4. Sprawdź logi: `openclaw logs --follow`


### Bot wysyła puste lub zastępcze odpowiedzi

  1. Sprawdź, czy model AI zwraca poprawną treść
  2. Domyślna odpowiedź zastępcza to: "暂时无法解答，你可以换个问题问问我哦"
  3. Dostosuj ją przez `channels.yuanbao.fallbackReply`


### Wyciekł App Secret

  1. Zresetuj App Secret w YuanBao APP
  2. Zaktualizuj wartość w swojej konfiguracji
  3. Uruchom ponownie Gateway: `openclaw gateway restart`


* * *

## Konfiguracja zaawansowana

### Wiele kont

json5Copy code
[code]
    {  channels: {    yuanbao: {      defaultAccount: "main",      accounts: {        main: {          appKey: "key_xxx",          appSecret: "secret_xxx",          name: "Primary bot",        },        backup: {          appKey: "key_yyy",          appSecret: "secret_yyy",          name: "Backup bot",          enabled: false,        },      },    },  },}
[/code]

`defaultAccount` kontroluje, które konto jest używane, gdy wychodzące API nie określają `accountId`.

### Limity wiadomości

  * `maxChars` \- maksymalna liczba znaków w pojedynczej wiadomości (domyślnie: `3000` znaków)
  * `mediaMaxMb` \- limit przesyłania/pobierania multimediów (domyślnie: `20` MB)
  * `overflowPolicy` \- zachowanie, gdy wiadomość przekracza limit: `"split"` (domyślnie) lub `"stop"`


### Streaming

Yuanbao obsługuje wyjście przesyłane strumieniowo na poziomie bloków. Po włączeniu bot wysyła tekst we fragmentach w miarę jego generowania.

json5Copy code
[code]
    {  channels: {    yuanbao: {      disableBlockStreaming: false, // block streaming enabled (default)    },  },}
[/code]

Ustaw `disableBlockStreaming: true`, aby wysłać pełną odpowiedź w jednej wiadomości.

### Kontekst historii czatu grupowego

Kontroluj, ile historycznych wiadomości jest uwzględnianych w kontekście AI dla czatów grupowych:

json5Copy code
[code]
    {  channels: {    yuanbao: {      historyLimit: 100, // default: 100, set 0 to disable    },  },}
[/code]

### Tryb odpowiedzi do wiadomości

Kontroluj, jak bot cytuje wiadomości podczas odpowiadania w czatach grupowych:

json5Copy code
[code]
    {  channels: {    yuanbao: {      replyToMode: "first", // "off" | "first" | "all" (default: "first")    },  },}
[/code]

Wartość | Zachowanie  
---|---  
`"off"` | Bez odpowiedzi z cytatem  
`"first"` | Cytuj tylko pierwszą odpowiedź na wiadomość przychodzącą (domyślnie)  
`"all"` | Cytuj każdą odpowiedź  
  
### Wstrzykiwanie podpowiedzi Markdown

Domyślnie bot wstrzykuje instrukcje do promptu systemowego, aby zapobiec opakowywaniu całej odpowiedzi przez model AI w bloki kodu markdown.

json5Copy code
[code]
    {  channels: {    yuanbao: {      markdownHintEnabled: true, // default: true    },  },}
[/code]

### Tryb debugowania

Włącz niezredagowane wyjście logów dla konkretnych identyfikatorów botów:

json5Copy code
[code]
    {  channels: {    yuanbao: {      debugBotIds: ["bot_user_id_1", "bot_user_id_2"],    },  },}
[/code]

### Routing wielu agentów

Użyj `bindings`, aby kierować DM lub grupy Yuanbao do różnych agentów.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main" },      { id: "agent-a", workspace: "/home/user/agent-a" },      { id: "agent-b", workspace: "/home/user/agent-b" },    ],  },  bindings: [    {      agentId: "agent-a",      match: {        channel: "yuanbao",        peer: { kind: "direct", id: "user_xxx" },      },    },    {      agentId: "agent-b",      match: {        channel: "yuanbao",        peer: { kind: "group", id: "group_zzz" },      },    },  ],}
[/code]

Pola routingu:

  * `match.channel`: `"yuanbao"`
  * `match.peer.kind`: `"direct"` (DM) lub `"group"` (czat grupowy)
  * `match.peer.id`: identyfikator użytkownika lub kod grupy


* * *

## Dokumentacja konfiguracji

Pełna konfiguracja: [Konfiguracja Gateway](</pl/gateway/configuration>)

Ustawienie | Opis | Domyślnie  
---|---|---  
`channels.yuanbao.enabled` | Włącz/wyłącz kanał | `true`  
`channels.yuanbao.defaultAccount` | Domyślne konto dla routingu wychodzącego | `default`  
`channels.yuanbao.accounts.<id>.appKey` | App Key (używany do podpisywania i generowania biletu) | -  
`channels.yuanbao.accounts.<id>.appSecret` | App Secret (używany do podpisywania) | -  
`channels.yuanbao.accounts.<id>.token` | Wstępnie podpisany token (pomija automatyczne podpisywanie biletu) | -  
`channels.yuanbao.accounts.<id>.name` | Nazwa wyświetlana konta | -  
`channels.yuanbao.accounts.<id>.enabled` | Włącz/wyłącz konkretne konto | `true`  
`channels.yuanbao.dm.policy` | Zasada DM | `open`  
`channels.yuanbao.dm.allowFrom` | Lista dozwolonych DM (lista identyfikatorów użytkowników) | -  
`channels.yuanbao.requireMention` | Wymagaj @wzmianki w grupach | `true`  
`channels.yuanbao.overflowPolicy` | Obsługa długich wiadomości (`split` lub `stop`) | `split`  
`channels.yuanbao.replyToMode` | Strategia odpowiedzi do wiadomości w grupach (`off`, `first`, `all`) | `first`  
`channels.yuanbao.outboundQueueStrategy` | Strategia wychodząca (`merge-text` lub `immediate`) | `merge-text`  
`channels.yuanbao.minChars` | Merge-text: minimalna liczba znaków wyzwalająca wysłanie | `2800`  
`channels.yuanbao.maxChars` | Merge-text: maksymalna liczba znaków na wiadomość | `3000`  
`channels.yuanbao.idleMs` | Merge-text: limit bezczynności przed automatycznym opróżnieniem (ms) | `5000`  
`channels.yuanbao.mediaMaxMb` | Limit rozmiaru multimediów (MB) | `20`  
`channels.yuanbao.historyLimit` | Wpisy kontekstu historii czatu grupowego | `100`  
`channels.yuanbao.disableBlockStreaming` | Wyłącz wyjście strumieniowe na poziomie bloków | `false`  
`channels.yuanbao.fallbackReply` | Odpowiedź zastępcza, gdy AI nie zwraca treści | `暂时无法解答，你可以换个问题问问我哦`  
`channels.yuanbao.markdownHintEnabled` | Wstrzykuj instrukcje zapobiegające opakowywaniu markdown | `true`  
`channels.yuanbao.debugBotIds` | Lista dozwolonych identyfikatorów botów do debugowania (niezredagowane logi) | `[]`  
  
* * *

## Obsługiwane typy wiadomości

### Odbieranie

  * ✅ Tekst
  * ✅ Obrazy
  * ✅ Pliki
  * ✅ Audio / głos
  * ✅ Wideo
  * ✅ Naklejki / niestandardowe emoji
  * ✅ Elementy niestandardowe (karty linków itp.)


### Wysyłanie

  * ✅ Tekst (z obsługą markdown)
  * ✅ Obrazy
  * ✅ Pliki
  * ✅ Audio
  * ✅ Wideo
  * ✅ Naklejki


### Wątki i odpowiedzi

  * ✅ Odpowiedzi z cytatem (konfigurowalne przez `replyToMode`)
  * ❌ Odpowiedzi w wątkach (nieobsługiwane przez platformę)


* * *

## Powiązane

  * [Przegląd kanałów](</pl/channels>) \- wszystkie obsługiwane kanały
  * [Parowanie](</pl/channels/pairing>) \- uwierzytelnianie DM i przepływ parowania
  * [Grupy](</pl/channels/groups>) \- zachowanie czatu grupowego i bramkowanie wzmianek
  * [Routing kanałów](</pl/channels/channel-routing>) \- routing sesji dla wiadomości
  * [Bezpieczeństwo](</pl/gateway/security>) \- model dostępu i wzmacnianie zabezpieczeń


Was this useful?YesNo