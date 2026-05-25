---
title: TypeBox
source_url: https://docs.openclaw.ai/pt-BR/concepts/typebox
scraped_at: 2026-05-25
---

TypeBox é uma biblioteca de esquemas com TypeScript em primeiro lugar. Nós a usamos para definir o **protocolo WebSocket do Gateway** (handshake, solicitação/resposta, eventos do servidor). Esses esquemas impulsionam a **validação em runtime** , a **exportação de JSON Schema** e a **geração de código Swift** para o app macOS. Uma única fonte da verdade; todo o resto é gerado.

Se você quiser o contexto de protocolo de nível mais alto, comece por [Arquitetura do Gateway](</pt-BR/concepts/architecture>).

## Modelo mental (30 segundos)

Toda mensagem WS do Gateway é um dos três frames:

  * **Solicitação** : `{ type: "req", id, method, params }`
  * **Resposta** : `{ type: "res", id, ok, payload | error }`
  * **Evento** : `{ type: "event", event, payload, seq?, stateVersion? }`


O primeiro frame **deve** ser uma solicitação `connect`. Depois disso, clientes podem chamar métodos (por exemplo, `health`, `send`, `chat.send`) e assinar eventos (por exemplo, `presence`, `tick`, `agent`).

Fluxo de conexão (mínimo):

CodeCopy code
[code]
    Client                    Gateway  |---- req:connect -------->|  |<---- res:hello-ok --------|  |<---- event:tick ----------|  |---- req:health ---------->|  |<---- res:health ----------|
[/code]

Métodos + eventos comuns:

Categoria | Exemplos | Observações  
---|---|---  
Núcleo | `connect`, `health`, `status` | `connect` deve ser o primeiro  
Mensagens | `send`, `agent`, `agent.wait`, `system-event`, `logs.tail` | efeitos colaterais precisam de `idempotencyKey`  
Chat | `chat.history`, `chat.send`, `chat.abort` | WebChat usa estes  
Sessões | `sessions.list`, `sessions.patch`, `sessions.delete` | administração de sessão  
Automação | `wake`, `cron.list`, `cron.run`, `cron.runs` | controle de wake + cron  
Nós | `node.list`, `node.invoke`, `node.pair.*` | WS do Gateway + ações de nó  
Eventos | `tick`, `presence`, `agent`, `chat`, `health`, `shutdown` | push do servidor  
  
O inventário autoritativo de **descoberta** anunciado fica em `src/gateway/server-methods-list.ts` (`listGatewayMethods`, `GATEWAY_EVENTS`).

## Onde os esquemas ficam

  * Fonte: `src/gateway/protocol/schema.ts`
  * Validadores de runtime (AJV): `src/gateway/protocol/index.ts`
  * Registro de recursos/descoberta anunciados: `src/gateway/server-methods-list.ts`
  * Handshake do servidor + despacho de métodos: `src/gateway/server.impl.ts`
  * Cliente Node: `src/gateway/client.ts`
  * JSON Schema gerado: `dist/protocol.schema.json`
  * Modelos Swift gerados: `apps/macos/Sources/OpenClawProtocol/GatewayModels.swift`


## Pipeline atual

  * `pnpm protocol:gen`
    * grava JSON Schema (draft-07) em `dist/protocol.schema.json`
  * `pnpm protocol:gen:swift`
    * gera modelos Swift do gateway
  * `pnpm protocol:check`
    * executa ambos os geradores e verifica se a saída está comitada


## Como os esquemas são usados em runtime

  * **Lado do servidor** : todo frame de entrada é validado com AJV. O handshake só aceita uma solicitação `connect` cujos params correspondam a `ConnectParams`.
  * **Lado do cliente** : o cliente JS valida frames de evento e resposta antes de usá-los.
  * **Descoberta de recursos** : o Gateway envia uma lista conservadora de `features.methods` e `features.events` em `hello-ok` a partir de `listGatewayMethods()` e `GATEWAY_EVENTS`.
  * Essa lista de descoberta não é um despejo gerado de todo helper chamável em `coreGatewayHandlers`; alguns RPCs auxiliares são implementados em `src/gateway/server-methods/*.ts` sem serem enumerados na lista de recursos anunciada.


## Frames de exemplo

Connect (primeira mensagem):

jsonCopy code
[code]
    {  "type": "req",  "id": "c1",  "method": "connect",  "params": {    "minProtocol": 3,    "maxProtocol": 4,    "client": {      "id": "openclaw-macos",      "displayName": "macos",      "version": "1.0.0",      "platform": "macos 15.1",      "mode": "ui",      "instanceId": "A1B2"    }  }}
[/code]

Resposta hello-ok:

jsonCopy code
[code]
    {  "type": "res",  "id": "c1",  "ok": true,  "payload": {    "type": "hello-ok",    "protocol": 4,    "server": { "version": "dev", "connId": "ws-1" },    "features": { "methods": ["health"], "events": ["tick"] },    "snapshot": {      "presence": [],      "health": {},      "stateVersion": { "presence": 0, "health": 0 },      "uptimeMs": 0    },    "policy": { "maxPayload": 1048576, "maxBufferedBytes": 1048576, "tickIntervalMs": 30000 }  }}
[/code]

Solicitação + resposta:

jsonCopy code
[code]
    { "type": "req", "id": "r1", "method": "health" }
[/code]

jsonCopy code
[code]
    { "type": "res", "id": "r1", "ok": true, "payload": { "ok": true } }
[/code]

Evento:

jsonCopy code
[code]
    { "type": "event", "event": "tick", "payload": { "ts": 1730000000 }, "seq": 12 }
[/code]

## Cliente mínimo (Node.js)

Menor fluxo útil: connect + health.

tsCopy code
[code]
     const ws = new WebSocket("ws://127.0.0.1:18789"); ws.on("open", () => {  ws.send(    JSON.stringify({      type: "req",      id: "c1",      method: "connect",      params: {        minProtocol: 4,        maxProtocol: 4,        client: {          id: "cli",          displayName: "example",          version: "dev",          platform: "node",          mode: "cli",        },      },    }),  );}); ws.on("message", (data) => {  const msg = JSON.parse(String(data));  if (msg.type === "res" && msg.id === "c1" && msg.ok) {    ws.send(JSON.stringify({ type: "req", id: "h1", method: "health" }));  }  if (msg.type === "res" && msg.id === "h1") {    console.log("health:", msg.payload);    ws.close();  }});
[/code]

## Exemplo trabalhado: adicionar um método de ponta a ponta

Exemplo: adicionar uma nova solicitação `system.echo` que retorna `{ ok: true, text }`.

  1. **Esquema (fonte da verdade)**


Adicione a `src/gateway/protocol/schema.ts`:

tsCopy code
[code]
    export const SystemEchoParamsSchema = Type.Object(  { text: NonEmptyString },  { additionalProperties: false },); export const SystemEchoResultSchema = Type.Object(  { ok: Type.Boolean(), text: NonEmptyString },  { additionalProperties: false },);
[/code]

Adicione ambos a `ProtocolSchemas` e exporte os tipos:

tsCopy code
[code]
      SystemEchoParams: SystemEchoParamsSchema,  SystemEchoResult: SystemEchoResultSchema,
[/code]

tsCopy code
[code]
    export type SystemEchoParams = Static<typeof SystemEchoParamsSchema>;export type SystemEchoResult = Static<typeof SystemEchoResultSchema>;
[/code]

  2. **Validação**


Em `src/gateway/protocol/index.ts`, exporte um validador AJV:

tsCopy code
[code]
    export const validateSystemEchoParams = ajv.compile&lt;SystemEchoParams&gt;(SystemEchoParamsSchema);
[/code]

  3. **Comportamento do servidor**


Adicione um handler em `src/gateway/server-methods/system.ts`:

tsCopy code
[code]
    export const systemHandlers: GatewayRequestHandlers = {  "system.echo": ({ params, respond }) => {    const text = String(params.text ?? "");    respond(true, { ok: true, text });  },};
[/code]

Registre-o em `src/gateway/server-methods.ts` (já mescla `systemHandlers`), depois adicione `"system.echo"` à entrada de `listGatewayMethods` em `src/gateway/server-methods-list.ts`.

Se o método for chamável por clientes operador ou nó, classifique-o também em `src/gateway/method-scopes.ts` para que a aplicação de escopo e a publicidade de recursos de `hello-ok` permaneçam alinhadas.

  4. **Regenerar**

bashCopy code
[code]
    pnpm protocol:check
[/code]

  5. **Testes + docs**


Adicione um teste de servidor em `src/gateway/server.*.test.ts` e observe o método nos docs.

## Comportamento da geração de código Swift

O gerador Swift emite:

  * enum `GatewayFrame` com casos `req`, `res`, `event` e `unknown`
  * Structs/enums de payload fortemente tipados
  * Valores `ErrorCode`, `GATEWAY_PROTOCOL_VERSION` e `GATEWAY_MIN_PROTOCOL_VERSION`


Tipos de frame desconhecidos são preservados como payloads brutos para compatibilidade futura.

## Versionamento + compatibilidade

  * `PROTOCOL_VERSION` fica em `src/gateway/protocol/version.ts`.
  * Clientes enviam `minProtocol` \+ `maxProtocol`; o servidor rejeita intervalos que não incluem seu protocolo atual.
  * Os modelos Swift mantêm tipos de frame desconhecidos para evitar quebrar clientes mais antigos.


## Padrões e convenções de esquema

  * A maioria dos objetos usa `additionalProperties: false` para payloads estritos.
  * `NonEmptyString` é o padrão para IDs e nomes de métodos/eventos.
  * O `GatewayFrame` de nível superior usa um **discriminador** em `type`.
  * Métodos com efeitos colaterais normalmente exigem um `idempotencyKey` em params (exemplo: `send`, `poll`, `agent`, `chat.send`).
  * `agent` aceita `internalEvents` opcionais para contexto de orquestração gerado em runtime (por exemplo, repasse de conclusão de subagente/tarefa cron); trate isso como superfície de API interna.


## JSON de esquema ativo

O JSON Schema gerado está no repo em `dist/protocol.schema.json`. O arquivo bruto publicado normalmente está disponível em:

  * <https://raw.githubusercontent.com/openclaw/openclaw/main/dist/protocol.schema.json>


## Quando você alterar esquemas

  1. Atualize os esquemas TypeBox.
  2. Registre o método/evento em `src/gateway/server-methods-list.ts`.
  3. Atualize `src/gateway/method-scopes.ts` quando o novo RPC precisar de classificação de escopo de operador ou nó.
  4. Execute `pnpm protocol:check`.
  5. Comite o esquema regenerado + os modelos Swift.


## Relacionado

  * [Protocolo de saída rica](</pt-BR/reference/rich-output-protocol>)
  * [Adaptadores RPC](</pt-BR/reference/rpc>)


Was this useful?YesNo