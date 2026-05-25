---
title: API wejścia kanału
source_url: https://docs.openclaw.ai/pl/plugins/sdk-channel-ingress
scraped_at: 2026-05-25
---

# API ingressu kanałów

Ingress kanałów to eksperymentalna granica kontroli dostępu dla przychodzących zdarzeń kanałów. Używaj `openclaw/plugin-sdk/channel-ingress-runtime` dla ścieżek odbioru. Starsza ścieżka podrzędna `openclaw/plugin-sdk/channel-ingress` pozostaje eksportowana jako przestarzała fasada zgodności dla Pluginów zewnętrznych.

Pluginy są właścicielami faktów platformowych i skutków ubocznych. Rdzeń jest właścicielem ogólnej polityki: list dozwolonych DM/grup, wpisów DM w magazynie parowania, bramek tras, bramek poleceń, autoryzacji zdarzeń, aktywacji przez wzmiankę, zredagowanej diagnostyki i dopuszczenia.

## Resolver środowiska uruchomieniowego

tsCopy code
[code]
       defineStableChannelIngressIdentity,  resolveChannelMessageIngress,} from "openclaw/plugin-sdk/channel-ingress-runtime"; const identity = defineStableChannelIngressIdentity({  key: "platform-user-id",  normalize: normalizePlatformUserId,  sensitivity: "pii",}); const result = await resolveChannelMessageIngress({  channelId: "my-channel",  accountId,  identity,  subject: { stableId: platformUserId },  conversation: { kind: isGroup ? "group" : "direct", id: conversationId },  event: { kind: "message", authMode: "inbound", mayPair: !isGroup },  policy: {    dmPolicy: config.dmPolicy,    groupPolicy: config.groupPolicy,    groupAllowFromFallbackToAllowFrom: true,  },  allowFrom: config.allowFrom,  groupAllowFrom: config.groupAllowFrom,  accessGroups: cfg.accessGroups,  route,  readStoreAllowFrom,  command: hasControlCommand ? { allowTextCommands: true, hasControlCommand } : undefined,});
[/code]

Nie obliczaj z góry efektywnych list dozwolonych, właścicieli poleceń ani grup poleceń. Resolver wyprowadza je z surowych list dozwolonych, wywołań zwrotnych magazynu, deskryptorów tras, grup dostępu, polityki i rodzaju rozmowy.

## Wynik

Dołączone Pluginy powinny używać nowoczesnych projekcji bezpośrednio:

  * `ingress`: uporządkowana decyzja bramki i dopuszczenie
  * `senderAccess`: tylko autoryzacja nadawcy/rozmowy
  * `routeAccess`: projekcja trasy i nadawcy trasy
  * `commandAccess`: autoryzacja polecenia; false, gdy nie uruchomiono bramki polecenia
  * `activationAccess`: wynik wzmianki/aktywacji


Autoryzacja zdarzeń pozostaje dostępna w uporządkowanym `ingress.graph` oraz decydującym `ingress.reasonCode`; nie jest emitowana żadna osobna projekcja zdarzenia.

Przestarzałe pomocniki SDK dla zewnętrznych Pluginów mogą wewnętrznie odtwarzać starsze kształty. Nowe dołączone ścieżki odbioru nie powinny tłumaczyć nowoczesnych wyników z powrotem na lokalne DTO.

## Grupy dostępu

Wpisy `accessGroup:<name>` pozostają zredagowane. Rdzeń sam rozwiązuje statyczne grupy `message.senders` i wywołuje `resolveAccessGroupMembership` tylko dla grup dynamicznych, które wymagają wyszukiwania na platformie. Brakujące, nieobsługiwane i nieudane grupy kończą się odmową.

## Tryby zdarzeń

`authMode` | Znaczenie  
---|---  
`inbound` | zwykłe bramki nadawcy przychodzącego  
`command` | bramki poleceń dla wywołań zwrotnych lub przycisków zakresowych  
`origin-subject` | aktor musi pasować do podmiotu oryginalnej wiadomości  
`route-only` | tylko bramki tras dla zaufanych zdarzeń zakresowych trasy  
`none` | wewnętrzne zdarzenia zarządzane przez Plugin omijają wspólną autoryzację  
  
Używaj `mayPair: false` dla reakcji, przycisków, wywołań zwrotnych i natywnych poleceń.

## Trasy i aktywacja

Używaj deskryptorów tras dla pokoju, tematu, gildii, wątku lub zagnieżdżonej polityki tras:

tsCopy code
[code]
    route: {  id: "room",  allowed: roomAllowed,  enabled: roomEnabled,  senderPolicy: "replace",  senderAllowFrom: roomAllowFrom,  blockReason: "room_sender_not_allowlisted",}
[/code]

Używaj `channelIngressRoutes(...)`, gdy Plugin ma kilka opcjonalnych deskryptorów tras; filtruje on wyłączone gałęzie, zachowując fakty tras jako ogólne i uporządkowane według `precedence` każdego deskryptora.

Bramkowanie wzmianki jest bramką aktywacji. Brak trafienia wzmianki zwraca `admission: "skip"`, więc jądro tury nie przetwarza tury wyłącznie obserwacyjnej. Większość kanałów powinna pozostawić aktywację po bramkach nadawcy i poleceń. Publiczne powierzchnie czatu, które muszą wyciszyć ruch bez wzmianki przed szumem z listy dozwolonych nadawców, mogą włączyć `activation.order: "before-sender"`, gdy obejście poleceń tekstowych jest wyłączone. Kanały z niejawną aktywacją, takie jak odpowiedzi w wątkach bota, mogą przekazać `activation.allowedImplicitMentionKinds`; projektowane `activationAccess.shouldBypassMention` zgłasza wtedy, kiedy polecenie lub niejawna aktywacja ominęła jawną wzmiankę.

## Redakcja

Surowe wartości nadawców i surowe wpisy list dozwolonych są wyłącznie wejściem resolvera. Nie mogą pojawiać się w rozwiązanym stanie, decyzjach, diagnostyce, migawkach ani faktach zgodności. Używaj nieprzezroczystych identyfikatorów podmiotów, identyfikatorów wpisów, identyfikatorów tras i identyfikatorów diagnostycznych.

## Weryfikacja

bashCopy code
[code]
    pnpm test src/channels/message-access/message-access.test.ts src/plugin-sdk/channel-ingress-runtime.test.tspnpm plugin-sdk:api:check
[/code]

Was this useful?YesNo