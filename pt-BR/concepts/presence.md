---
title: Presença
source_url: https://docs.openclaw.ai/pt-BR/concepts/presence
scraped_at: 2026-05-25
---

A "presença" do OpenClaw é uma visão leve e de melhor esforço de:

  * o próprio **Gateway** , e
  * **clientes conectados ao Gateway** (app para Mac, WebChat, CLI etc.)


A presença é usada principalmente para renderizar a aba **Instâncias** do app para macOS e fornecer visibilidade rápida ao operador.

## Campos de presença (o que aparece)

As entradas de presença são objetos estruturados com campos como:

  * `instanceId` (opcional, mas fortemente recomendado): identidade estável do cliente (geralmente `connect.client.instanceId`)
  * `host`: nome de host legível para humanos
  * `ip`: endereço IP de melhor esforço
  * `version`: string da versão do cliente
  * `deviceFamily` / `modelIdentifier`: dicas de hardware
  * `mode`: `ui`, `webchat`, `cli`, `backend`, `probe`, `test`, `node`, ...
  * `lastInputSeconds`: "segundos desde a última entrada do usuário" (se conhecido)
  * `reason`: `self`, `connect`, `node-connected`, `periodic`, ...
  * `ts`: carimbo de data/hora da última atualização (ms desde a época Unix)


## Produtores (de onde vem a presença)

As entradas de presença são produzidas por várias fontes e **mescladas**.

### 1) Entrada própria do Gateway

O Gateway sempre inicializa uma entrada "própria" na inicialização para que as UIs mostrem o host do gateway mesmo antes de qualquer cliente se conectar.

### 2) Conexão WebSocket

Todo cliente WS começa com uma solicitação `connect`. Após um handshake bem-sucedido, o Gateway faz upsert de uma entrada de presença para essa conexão.

#### Por que comandos CLI pontuais não aparecem

A CLI costuma se conectar para comandos curtos e pontuais. Para evitar poluir a lista de Instâncias, `client.mode === "cli"` **não** é transformado em uma entrada de presença.

### 3) Beacons `system-event`

Os clientes podem enviar beacons periódicos mais ricos por meio do método `system-event`. O app para Mac usa isso para informar nome de host, IP e `lastInputSeconds`.

### 4) Conexões de Node (role: node)

Quando um node se conecta pelo WebSocket do Gateway com `role: node`, o Gateway faz upsert de uma entrada de presença para esse node (o mesmo fluxo de outros clientes WS).

## Regras de mesclagem + desduplicação (por que `instanceId` importa)

As entradas de presença são armazenadas em um único mapa em memória:

  * As entradas são indexadas por uma **chave de presença**.
  * A melhor chave é um `instanceId` estável (de `connect.client.instanceId`) que sobrevive a reinicializações.
  * As chaves não diferenciam maiúsculas de minúsculas.


Se um cliente se reconectar sem um `instanceId` estável, ele poderá aparecer como uma linha **duplicada**.

## TTL e tamanho limitado

A presença é intencionalmente efêmera:

  * **TTL:** entradas com mais de 5 minutos são removidas
  * **Máximo de entradas:** 200 (as mais antigas são descartadas primeiro)


Isso mantém a lista atualizada e evita crescimento ilimitado de memória.

## Observação sobre remoto/túnel (IPs de loopback)

Quando um cliente se conecta por um túnel SSH / encaminhamento de porta local, o Gateway pode ver o endereço remoto como `127.0.0.1`. Para evitar sobrescrever um bom IP informado pelo cliente, endereços remotos de loopback são ignorados.

## Consumidores

### Aba Instâncias do macOS

O app para macOS renderiza a saída de `system-presence` e aplica um pequeno indicador de status (Ativo/Ocioso/Obsoleto) com base na idade da última atualização.

## Dicas de depuração

  * Para ver a lista bruta, chame `system-presence` no Gateway.
  * Se você vir duplicatas: 
    * confirme se os clientes enviam um `client.instanceId` estável no handshake
    * confirme se os beacons periódicos usam o mesmo `instanceId`
    * verifique se a entrada derivada da conexão está sem `instanceId` (duplicatas são esperadas)


## Relacionados

[**Indicadores de digitação** Quando indicadores de digitação são enviados e como ajustá-los. ](</pt-BR/concepts/typing-indicators>) [**Streaming e divisão em partes** Streaming de saída, divisão em partes e formatação por canal. ](</pt-BR/concepts/streaming>) [**Arquitetura do Gateway** Componentes do Gateway e o protocolo WebSocket que aciona atualizações de presença. ](</pt-BR/concepts/architecture>) [**Protocolo do Gateway** O protocolo de transmissão para `connect`, `system-event` e `system-presence`. ](</pt-BR/gateway/protocol>)

Was this useful?YesNo