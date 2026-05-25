---
title: Grupy dostępu
source_url: https://docs.openclaw.ai/pl/channels/access-groups
scraped_at: 2026-05-25
---

Grupy dostępu to nazwane listy nadawców, które definiujesz raz i do których odwołujesz się z list dozwolonych kanałów za pomocą `accessGroup:<name>`.

Używaj ich, gdy te same osoby powinny mieć dostęp w kilku kanałach wiadomości albo gdy jeden zaufany zestaw ma obowiązywać zarówno dla autoryzacji nadawców w DM, jak i w grupach.

Grupy dostępu same z siebie nie przyznają dostępu. Grupa ma znaczenie tylko wtedy, gdy odwołuje się do niej pole listy dozwolonych.

## Statyczne grupy nadawców wiadomości

Statyczne grupy nadawców używają `type: "message.senders"`.

json5Copy code
[code]
    {  accessGroups: {    operators: {      type: "message.senders",      members: {        "*": ["global-owner-id"],        discord: ["discord:123456789012345678"],        telegram: ["987654321"],        whatsapp: ["+15551234567"],      },    },  },}
[/code]

Listy członków są indeksowane według identyfikatora kanału wiadomości:

Klucz | Znaczenie  
---|---  
`"*"` | Wspólne wpisy sprawdzane dla każdego kanału wiadomości, który odwołuje się do grupy.  
`discord` | Wpisy sprawdzane tylko przy dopasowywaniu listy dozwolonych Discord.  
`telegram` | Wpisy sprawdzane tylko przy dopasowywaniu listy dozwolonych Telegram.  
`whatsapp` | Wpisy sprawdzane tylko przy dopasowywaniu listy dozwolonych WhatsApp.  
  
Wpisy są dopasowywane zgodnie ze zwykłymi regułami `allowFrom` kanału docelowego. OpenClaw nie tłumaczy identyfikatorów nadawców między kanałami. Jeśli Alice ma identyfikator Telegram i identyfikator Discord, podaj oba identyfikatory pod odpowiednimi kluczami.

## Odwoływanie się do grup z list dozwolonych

Odwołaj się do grupy za pomocą `accessGroup:<name>` wszędzie tam, gdzie ścieżka kanału wiadomości obsługuje listy dozwolonych nadawców.

Przykład listy dozwolonych dla DM:

json5Copy code
[code]
    {  accessGroups: {    operators: {      type: "message.senders",      members: {        discord: ["discord:123456789012345678"],        telegram: ["987654321"],      },    },  },  channels: {    discord: {      dmPolicy: "allowlist",      allowFrom: ["accessGroup:operators"],    },    telegram: {      dmPolicy: "allowlist",      allowFrom: ["accessGroup:operators"],    },  },}
[/code]

Przykład listy dozwolonych nadawców w grupie:

json5Copy code
[code]
    {  accessGroups: {    oncall: {      type: "message.senders",      members: {        whatsapp: ["+15551234567"],        googlechat: ["users/1234567890"],      },    },  },  channels: {    whatsapp: {      groupPolicy: "allowlist",      groupAllowFrom: ["accessGroup:oncall"],    },    googlechat: {      spaces: {        "spaces/AAA": {          users: ["accessGroup:oncall"],        },      },    },  },}
[/code]

Możesz łączyć grupy i wpisy bezpośrednie:

json5Copy code
[code]
    {  channels: {    discord: {      dmPolicy: "allowlist",      allowFrom: ["accessGroup:operators", "discord:123456789012345678"],    },  },}
[/code]

## Obsługiwane ścieżki kanałów wiadomości

Grupy dostępu są dostępne we współdzielonych ścieżkach autoryzacji kanałów wiadomości, w tym:

  * listach dozwolonych nadawców DM, takich jak `channels.<channel>.allowFrom`
  * listach dozwolonych nadawców w grupach, takich jak `channels.<channel>.groupAllowFrom`
  * specyficznych dla kanału listach dozwolonych nadawców dla poszczególnych pokoi, które używają tych samych reguł dopasowywania nadawców
  * ścieżkach autoryzacji poleceń, które ponownie używają list dozwolonych nadawców kanału wiadomości


Obsługa kanałów zależy od tego, czy dany kanał jest podłączony przez współdzielone pomocniki autoryzacji nadawców OpenClaw. Aktualna obsługa wbudowana obejmuje Discord, Feishu, Google Chat, iMessage, LINE, Mattermost, Microsoft Teams, Nextcloud Talk, Nostr, QQBot, Signal, WhatsApp, Zalo i Zalo Personal. Statyczne grupy `message.senders` są zaprojektowane jako niezależne od kanału, więc nowe kanały wiadomości powinny je obsługiwać, używając współdzielonych pomocników SDK Plugin zamiast niestandardowego rozwijania list dozwolonych.

## Diagnostyka Plugin

Autorzy Plugin mogą sprawdzać ustrukturyzowany stan grup dostępu bez rozwijania go z powrotem do płaskiej listy dozwolonych:

typescriptCopy code
[code]
     const state = await resolveAccessGroupAllowFromState({  accessGroups: cfg.accessGroups,  allowFrom: channelConfig.allowFrom,  channel: "my-channel",  accountId: "default",  senderId,  isSenderAllowed,});
[/code]

Wynik raportuje grupy, do których się odwołano, dopasowane, brakujące, nieobsługiwane i zakończone niepowodzeniem. Użyj tego, gdy potrzebujesz diagnostyki lub testów zgodności. Używaj `expandAllowFromWithAccessGroups(...)` tylko dla ścieżek kompatybilności, które nadal oczekują płaskiej tablicy `allowFrom`.

## Odbiorcy kanału Discord

Discord obsługuje także dynamiczny typ grupy dostępu:

json5Copy code
[code]
    {  accessGroups: {    maintainers: {      type: "discord.channelAudience",      guildId: "1456350064065904867",      channelId: "1456744319972282449",      membership: "canViewChannel",    },  },  channels: {    discord: {      dmPolicy: "allowlist",      allowFrom: ["accessGroup:maintainers"],    },  },}
[/code]

`discord.channelAudience` oznacza „zezwól nadawcom DM Discord, którzy obecnie mogą wyświetlać ten kanał gildii”. OpenClaw rozpoznaje nadawcę przez Discord w czasie autoryzacji i stosuje reguły uprawnień Discord `ViewChannel`.

Użyj tego, gdy kanał Discord jest już źródłem prawdy dla zespołu, takim jak `#maintainers` lub `#on-call`.

Wymagania i zachowanie w razie niepowodzenia:

  * Bot potrzebuje dostępu do gildii i kanału.
  * Bot potrzebuje **Server Members Intent** w Discord Developer Portal.
  * Grupa dostępu odmawia dostępu w razie niepowodzenia, gdy Discord zwraca `Missing Access`, nadawcy nie można rozpoznać jako członka gildii albo kanał należy do innej gildii.


Więcej przykładów specyficznych dla Discord: [Kontrola dostępu Discord](</pl/channels/discord#access-control-and-routing>)

## Uwagi dotyczące bezpieczeństwa

  * Grupy dostępu są aliasami list dozwolonych, nie rolami. Same z siebie nie tworzą właścicieli, nie zatwierdzają próśb o parowanie ani nie przyznają uprawnień do narzędzi.
  * `dmPolicy: "open"` nadal wymaga `"*"` w efektywnej liście dozwolonych DM. Odwołanie do grupy dostępu nie jest tym samym co dostęp publiczny.
  * Brakujące nazwy grup odmawiają dostępu w razie niepowodzenia. Jeśli `allowFrom` zawiera `accessGroup:operators`, a `accessGroups.operators` nie istnieje, ten wpis nie autoryzuje nikogo.
  * Utrzymuj stabilne identyfikatory kanałów. Preferuj identyfikatory numeryczne/użytkowników zamiast nazw wyświetlanych, gdy kanał obsługuje oba warianty.


## Rozwiązywanie problemów

Jeśli nadawca powinien pasować, ale jest blokowany:

  1. Potwierdź, że pole listy dozwolonych zawiera dokładne odwołanie `accessGroup:<name>`.
  2. Potwierdź, że `accessGroups.<name>.type` jest poprawne.
  3. Potwierdź, że identyfikator nadawcy jest wymieniony pod pasującym kluczem kanału albo pod `"*"`.
  4. Potwierdź, że wpis używa zwykłej składni listy dozwolonych dla tego kanału.
  5. W przypadku odbiorców kanału Discord potwierdź, że bot widzi kanał gildii i ma włączone Server Members Intent.


Uruchom `openclaw doctor` po edycji konfiguracji kontroli dostępu. Wykrywa wiele nieprawidłowych kombinacji list dozwolonych i zasad przed uruchomieniem.

Was this useful?YesNo