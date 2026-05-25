---
title: TypeBox
source_url: https://docs.openclaw.ai/pl/concepts/typebox
scraped_at: 2026-05-25
---

TypeBox to biblioteka schematów zorientowana na TypeScript. Używamy jej do definiowania **protokołu WebSocket Gateway** (handshake, żądanie/odpowiedź, zdarzenia serwera). Te schematy napędzają **walidację w czasie działania** , **eksport JSON Schema** i **generowanie kodu Swift** dla aplikacji macOS. Jedno źródło prawdy; cała reszta jest generowana.

Jeśli chcesz poznać kontekst protokołu na wyższym poziomie, zacznij od [architektury Gateway](</pl/concepts/architecture>).

## Model myślowy (30 sekund)

Każda wiadomość Gateway WS jest jedną z trzech ramek:

  * **Żądanie** : `{ type: "req", id, method, params }`
  * **Odpowiedź** : `{ type: "res", id, ok, payload | error }`
  * **Zdarzenie** : `{ type: "event", event, payload, seq?, stateVersion? }`


Pierwsza ramka **musi** być żądaniem `connect`. Następnie klienci mogą wywoływać metody (np. `health`, `send`, `chat.send`) i subskrybować zdarzenia (np. `presence`, `tick`, `agent`).

Przepływ połączenia (minimalny):

CodeCopy code
[code]
    Client                    Gateway  |---- req:connect -------->|  |<---- res:hello-ok --------|  |<---- event:tick ----------|  |---- req:health ---------->|  |<---- res:health ----------|
[/code]

Typowe metody i zdarzenia:

Kategoria | Przykłady | Uwagi  
---|---|---  
Rdzeń | `connect`, `health`, `status` | `connect` musi być pierwsze  
Wiadomości | `send`, `agent`, `agent.wait`, `system-event`, `logs.tail` | skutki uboczne wymagają `idempotencyKey`  
Czat | `chat.history`, `chat.send`, `chat.abort` | WebChat ich używa  
Sesje | `sessions.list`, `sessions.patch`, `sessions.delete` | administracja sesjami  
Automatyzacja | `wake`, `cron.list`, `cron.run`, `cron.runs` | sterowanie wybudzaniem i cronem  
Węzły | `node.list`, `node.invoke`, `node.pair.*` | Gateway WS + działania Node  
Zdarzenia | `tick`, `presence`, `agent`, `chat`, `health`, `shutdown` | wypychanie z serwera  
  
Autorytatywny reklamowany inwentarz **wykrywania** znajduje się w `src/gateway/server-methods-list.ts` (`listGatewayMethods`, `GATEWAY_EVENTS`).

## Gdzie znajdują się schematy

  * Źródło: `src/gateway/protocol/schema.ts`
  * Walidatory w czasie działania (AJV): `src/gateway/protocol/index.ts`
  * Reklamowany rejestr funkcji/wykrywania: `src/gateway/server-methods-list.ts`
  * Handshake serwera + dispatch metod: `src/gateway/server.impl.ts`
  * Klient Node: `src/gateway/client.ts`
  * Wygenerowany JSON Schema: `dist/protocol.schema.json`
  * Wygenerowane modele Swift: `apps/macos/Sources/OpenClawProtocol/GatewayModels.swift`


## Obecny pipeline

  * `pnpm protocol:gen`
    * zapisuje JSON Schema (draft-07) do `dist/protocol.schema.json`
  * `pnpm protocol:gen:swift`
    * generuje modele Gateway w Swift
  * `pnpm protocol:check`
    * uruchamia oba generatory i sprawdza, czy wynik jest skomitowany


## Jak schematy są używane w czasie działania

  * **Po stronie serwera** : każda przychodząca ramka jest walidowana za pomocą AJV. Handshake akceptuje tylko żądanie `connect`, którego parametry pasują do `ConnectParams`.
  * **Po stronie klienta** : klient JS waliduje ramki zdarzeń i odpowiedzi przed ich użyciem.
  * **Wykrywanie funkcji** : Gateway wysyła konserwatywną listę `features.methods` i `features.events` w `hello-ok` z `listGatewayMethods()` oraz `GATEWAY_EVENTS`.
  * Ta lista wykrywania nie jest wygenerowanym zrzutem każdego możliwego do wywołania helpera w `coreGatewayHandlers`; niektóre pomocnicze RPC są zaimplementowane w `src/gateway/server-methods/*.ts`, ale nie są wyliczone na reklamowanej liście funkcji.


## Przykładowe ramki

Connect (pierwsza wiadomość):

jsonCopy code
[code]
    {  "type": "req",  "id": "c1",  "method": "connect",  "params": {    "minProtocol": 3,    "maxProtocol": 4,    "client": {      "id": "openclaw-macos",      "displayName": "macos",      "version": "1.0.0",      "platform": "macos 15.1",      "mode": "ui",      "instanceId": "A1B2"    }  }}
[/code]

Odpowiedź hello-ok:

jsonCopy code
[code]
    {  "type": "res",  "id": "c1",  "ok": true,  "payload": {    "type": "hello-ok",    "protocol": 4,    "server": { "version": "dev", "connId": "ws-1" },    "features": { "methods": ["health"], "events": ["tick"] },    "snapshot": {      "presence": [],      "health": {},      "stateVersion": { "presence": 0, "health": 0 },      "uptimeMs": 0    },    "policy": { "maxPayload": 1048576, "maxBufferedBytes": 1048576, "tickIntervalMs": 30000 }  }}
[/code]

Żądanie + odpowiedź:

jsonCopy code
[code]
    { "type": "req", "id": "r1", "method": "health" }
[/code]

jsonCopy code
[code]
    { "type": "res", "id": "r1", "ok": true, "payload": { "ok": true } }
[/code]

Zdarzenie:

jsonCopy code
[code]
    { "type": "event", "event": "tick", "payload": { "ts": 1730000000 }, "seq": 12 }
[/code]

## Minimalny klient (Node.js)

Najmniejszy użyteczny przepływ: połączenie + health.

tsCopy code
[code]
     const ws = new WebSocket("ws://127.0.0.1:18789"); ws.on("open", () => {  ws.send(    JSON.stringify({      type: "req",      id: "c1",      method: "connect",      params: {        minProtocol: 4,        maxProtocol: 4,        client: {          id: "cli",          displayName: "example",          version: "dev",          platform: "node",          mode: "cli",        },      },    }),  );}); ws.on("message", (data) => {  const msg = JSON.parse(String(data));  if (msg.type === "res" && msg.id === "c1" && msg.ok) {    ws.send(JSON.stringify({ type: "req", id: "h1", method: "health" }));  }  if (msg.type === "res" && msg.id === "h1") {    console.log("health:", msg.payload);    ws.close();  }});
[/code]

## Przykład krok po kroku: dodanie metody od początku do końca

Przykład: dodaj nowe żądanie `system.echo`, które zwraca `{ ok: true, text }`.

  1. **Schemat (źródło prawdy)**


Dodaj do `src/gateway/protocol/schema.ts`:

tsCopy code
[code]
    export const SystemEchoParamsSchema = Type.Object(  { text: NonEmptyString },  { additionalProperties: false },); export const SystemEchoResultSchema = Type.Object(  { ok: Type.Boolean(), text: NonEmptyString },  { additionalProperties: false },);
[/code]

Dodaj oba do `ProtocolSchemas` i wyeksportuj typy:

tsCopy code
[code]
      SystemEchoParams: SystemEchoParamsSchema,  SystemEchoResult: SystemEchoResultSchema,
[/code]

tsCopy code
[code]
    export type SystemEchoParams = Static<typeof SystemEchoParamsSchema>;export type SystemEchoResult = Static<typeof SystemEchoResultSchema>;
[/code]

  2. **Walidacja**


W `src/gateway/protocol/index.ts` wyeksportuj walidator AJV:

tsCopy code
[code]
    export const validateSystemEchoParams = ajv.compile&lt;SystemEchoParams&gt;(SystemEchoParamsSchema);
[/code]

  3. **Zachowanie serwera**


Dodaj handler w `src/gateway/server-methods/system.ts`:

tsCopy code
[code]
    export const systemHandlers: GatewayRequestHandlers = {  "system.echo": ({ params, respond }) => {    const text = String(params.text ?? "");    respond(true, { ok: true, text });  },};
[/code]

Zarejestruj go w `src/gateway/server-methods.ts` (już scala `systemHandlers`), a następnie dodaj `"system.echo"` do wejścia `listGatewayMethods` w `src/gateway/server-methods-list.ts`.

Jeśli metoda może być wywoływana przez klientów operatora lub Node, sklasyfikuj ją także w `src/gateway/method-scopes.ts`, aby egzekwowanie zakresów i reklamowanie funkcji w `hello-ok` pozostały spójne.

  4. **Wygeneruj ponownie**

bashCopy code
[code]
    pnpm protocol:check
[/code]

  5. **Testy + dokumentacja**


Dodaj test serwera w `src/gateway/server.*.test.ts` i opisz metodę w dokumentacji.

## Zachowanie generowania kodu Swift

Generator Swift emituje:

  * enum `GatewayFrame` z przypadkami `req`, `res`, `event` i `unknown`
  * silnie typowane struktury/enumy payloadów
  * wartości `ErrorCode`, `GATEWAY_PROTOCOL_VERSION` i `GATEWAY_MIN_PROTOCOL_VERSION`


Nieznane typy ramek są zachowywane jako surowe payloady dla zgodności w przód.

## Wersjonowanie + zgodność

  * `PROTOCOL_VERSION` znajduje się w `src/gateway/protocol/version.ts`.
  * Klienci wysyłają `minProtocol` \+ `maxProtocol`; serwer odrzuca zakresy, które nie obejmują jego obecnego protokołu.
  * Modele Swift zachowują nieznane typy ramek, aby nie psuć starszych klientów.


## Wzorce i konwencje schematów

  * Większość obiektów używa `additionalProperties: false` dla ścisłych payloadów.
  * `NonEmptyString` jest wartością domyślną dla identyfikatorów oraz nazw metod/zdarzeń.
  * Najwyższego poziomu `GatewayFrame` używa **dyskryminatora** na `type`.
  * Metody ze skutkami ubocznymi zwykle wymagają `idempotencyKey` w parametrach (przykład: `send`, `poll`, `agent`, `chat.send`).
  * `agent` akceptuje opcjonalne `internalEvents` dla generowanego w czasie działania kontekstu orkiestracji (na przykład przekazanie po ukończeniu zadania subagenta/cronu); traktuj to jako wewnętrzną powierzchnię API.


## JSON schematu na żywo

Wygenerowany JSON Schema znajduje się w repozytorium pod `dist/protocol.schema.json`. Opublikowany surowy plik jest zwykle dostępny pod adresem:

  * <https://raw.githubusercontent.com/openclaw/openclaw/main/dist/protocol.schema.json>


## Gdy zmieniasz schematy

  1. Zaktualizuj schematy TypeBox.
  2. Zarejestruj metodę/zdarzenie w `src/gateway/server-methods-list.ts`.
  3. Zaktualizuj `src/gateway/method-scopes.ts`, gdy nowe RPC wymaga klasyfikacji zakresu operatora lub Node.
  4. Uruchom `pnpm protocol:check`.
  5. Skomituj wygenerowany ponownie schemat + modele Swift.


## Powiązane

  * [Protokół bogatego wyjścia](</pl/reference/rich-output-protocol>)
  * [Adaptery RPC](</pl/reference/rpc>)


Was this useful?YesNo