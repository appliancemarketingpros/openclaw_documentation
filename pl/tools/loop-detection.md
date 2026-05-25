---
title: Wykrywanie pętli narzędzi
source_url: https://docs.openclaw.ai/pl/tools/loop-detection
scraped_at: 2026-05-25
---

OpenClaw ma dwa współpracujące mechanizmy zabezpieczające przed powtarzalnymi wzorcami wywołań narzędzi:

  1. **Wykrywanie pętli** (`tools.loopDetection.enabled`) — domyślnie wyłączone. Obserwuje kroczącą historię wywołań narzędzi pod kątem powtarzających się wzorców i ponowień dla nieznanych narzędzi.
  2. **Strażnik po Compaction** (`tools.loopDetection.postCompactionGuard`) — domyślnie włączony, chyba że `tools.loopDetection.enabled` jest jawnie ustawione na `false`. Uzbraja się po każdej próbie ponowienia po Compaction i przerywa uruchomienie, gdy agent wyemituje tę samą trójkę `(tool, args, result)` w ramach okna.


Oba są konfigurowane w tym samym bloku `tools.loopDetection`, ale strażnik po Compaction działa zawsze, gdy przełącznik główny nie jest jawnie wyłączony. Ustaw `tools.loopDetection.enabled: false`, aby wyciszyć oba mechanizmy.

## Dlaczego to istnieje

  * Wykrywanie powtarzalnych sekwencji, które nie robią postępu.
  * Wykrywanie częstych pętli bez wyniku (to samo narzędzie, te same dane wejściowe, powtarzające się błędy).
  * Wykrywanie konkretnych wzorców powtarzanych wywołań dla znanych narzędzi odpytujących.
  * Zapobieganie cyklom przepełnienie kontekstu, następnie Compaction, następnie ta sama pętla, które działałyby bez końca.


## Blok konfiguracji

Globalne wartości domyślne, z pokazanymi wszystkimi udokumentowanymi polami:

json5Copy code
[code]
    {  tools: {    loopDetection: {      enabled: false, // master switch for the rolling-history detectors      historySize: 30,      warningThreshold: 10,      criticalThreshold: 20,      unknownToolThreshold: 10,      globalCircuitBreakerThreshold: 30,      detectors: {        genericRepeat: true,        knownPollNoProgress: true,        pingPong: true,      },      postCompactionGuard: {        windowSize: 3, // armed after compaction-retry; runs unless enabled is explicitly false      },    },  },}
[/code]

Nadpisanie dla agenta (opcjonalne):

json5Copy code
[code]
    {  agents: {    list: [      {        id: "safe-runner",        tools: {          loopDetection: {            enabled: true,            warningThreshold: 8,            criticalThreshold: 16,          },        },      },    ],  },}
[/code]

### Zachowanie pól

Pole | Domyślnie | Efekt  
---|---|---  
`enabled` | `false` | Przełącznik główny dla detektorów kroczącej historii. Ustawienie `false` wyłącza także strażnika po Compaction.  
`historySize` | `30` | Liczba ostatnich wywołań narzędzi przechowywanych do analizy.  
`warningThreshold` | `10` | Próg, po którym wzorzec jest klasyfikowany wyłącznie jako ostrzeżenie.  
`criticalThreshold` | `20` | Próg blokowania powtarzalnych wzorców pętli bez postępu.  
`unknownToolThreshold` | `10` | Blokuje powtarzane wywołania tego samego niedostępnego narzędzia po tylu chybieniach.  
`globalCircuitBreakerThreshold` | `30` | Globalny próg przerywacza braku postępu we wszystkich detektorach.  
`detectors.genericRepeat` | `true` | Ostrzega przy powtarzanych wzorcach to samo narzędzie + te same parametry i blokuje, gdy te same wywołania zwracają także identyczne wyniki.  
`detectors.knownPollNoProgress` | `true` | Wykrywa znane wzorce podobne do odpytywania bez zmiany stanu.  
`detectors.pingPong` | `true` | Wykrywa naprzemienne wzorce ping-pong.  
`postCompactionGuard.windowSize` | `3` | Liczba wywołań narzędzi po Compaction, podczas których strażnik pozostaje uzbrojony, oraz liczba identycznych trójek, która przerywa uruchomienie.  
  
Dla `exec` kontrole braku postępu porównują stabilne wyniki poleceń i ignorują zmienne metadane wykonania, takie jak czas trwania, PID, identyfikator sesji i katalog roboczy. Gdy dostępny jest identyfikator uruchomienia, historia ostatnich wywołań narzędzi jest oceniana tylko w ramach tego uruchomienia, więc zaplanowane cykle Heartbeat i świeże uruchomienia nie dziedziczą przestarzałych liczników pętli z wcześniejszych uruchomień.

## Zalecana konfiguracja

  * Dla mniejszych modeli ustaw `enabled: true` i pozostaw progi z wartościami domyślnymi. Modele flagowe rzadko potrzebują wykrywania na podstawie kroczącej historii i mogą pozostawić przełącznik główny na `false`, nadal korzystając ze strażnika po Compaction.
  * Utrzymuj progi w kolejności `warningThreshold < criticalThreshold < globalCircuitBreakerThreshold`.
  * Jeśli występują fałszywe alarmy: 
    * Zwiększ `warningThreshold` i/lub `criticalThreshold`.
    * Opcjonalnie zwiększ `globalCircuitBreakerThreshold`.
    * Wyłącz tylko konkretny detektor powodujący problemy (`detectors.<name>: false`).
    * Zmniejsz `historySize`, aby kontekst historyczny był mniej rygorystyczny.
  * Aby wyłączyć wszystko (w tym strażnika po Compaction), jawnie ustaw `tools.loopDetection.enabled: false`.


## Strażnik po Compaction

Gdy runner zakończy próbę ponowienia po Compaction po przepełnieniu kontekstu, uzbraja strażnika z krótkim oknem, który obserwuje kilka kolejnych wywołań narzędzi. Jeśli agent wyemituje tę samą trójkę `(toolName, argsHash, resultHash)` wielokrotnie w ramach okna, strażnik uznaje, że Compaction nie przerwało pętli, i przerywa uruchomienie błędem `compaction_loop_persisted`.

Strażnik jest kontrolowany przez główną flagę `tools.loopDetection.enabled` z jednym szczegółem: pozostaje **włączony, gdy flaga jest nieustawiona lub ma wartość`true`**, i dezaktywuje się tylko wtedy, gdy flaga jest jawnie ustawiona na `false`. To zamierzone. Strażnik istnieje po to, aby wychodzić z pętli Compaction, które w przeciwnym razie zużywałyby nieograniczoną liczbę tokenów, więc użytkownik bez konfiguracji nadal otrzymuje ochronę.

json5Copy code
[code]
    {  tools: {    loopDetection: {      // master switch; set false to disable the guard along with the rolling detectors      enabled: true,      postCompactionGuard: {        windowSize: 3, // default      },    },  },}
[/code]

  * Niższe `windowSize` jest bardziej rygorystyczne (mniej prób przed przerwaniem).
  * Wyższe `windowSize` daje agentowi więcej prób odzyskania działania.
  * Strażnik nigdy nie przerywa, gdy wyniki się zmieniają, tylko gdy wyniki są bajtowo identyczne w całym oknie.
  * Jest celowo wąski: uruchamia się tylko bezpośrednio po próbie ponowienia po Compaction.


## Dzienniki i oczekiwane zachowanie

Gdy pętla zostanie wykryta, OpenClaw zgłasza zdarzenie pętli i albo tłumi, albo blokuje następny cykl narzędzi zależnie od wagi. Chroni to użytkowników przed niekontrolowanym zużyciem tokenów i blokadami, zachowując normalny dostęp do narzędzi.

  * Ostrzeżenia pojawiają się najpierw.
  * Tłumienie następuje, gdy wzorce utrzymują się po przekroczeniu progu ostrzeżeń.
  * Progi krytyczne blokują następny cykl narzędzi i ujawniają jasny powód wykrycia pętli w rekordzie uruchomienia.
  * Strażnik po Compaction emituje błędy `compaction_loop_persisted` z nazwą narzędzia powodującego problem i liczbą identycznych wywołań.


## Powiązane

[**Zatwierdzenia exec** Zasady zezwalania/odmawiania wykonywania powłoki. ](</pl/tools/exec-approvals>) [**Poziomy myślenia** Poziomy wysiłku rozumowania i interakcja z zasadami dostawcy. ](</pl/tools/thinking>) [**Podagenci** Uruchamianie izolowanych agentów, aby ograniczać niekontrolowane zachowanie. ](</pl/tools/subagents>) [**Dokumentacja konfiguracji** Pełny schemat `tools.loopDetection` i semantyka scalania. ](</pl/gateway/configuration-reference>)

Was this useful?YesNo