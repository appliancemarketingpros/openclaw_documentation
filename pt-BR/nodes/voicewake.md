---
title: Ativação por voz
source_url: https://docs.openclaw.ai/pt-BR/nodes/voicewake
scraped_at: 2026-05-25
---

OpenClaw trata **palavras de ativação como uma única lista global** pertencente ao **Gateway**.

  * Não há **palavras de ativação personalizadas por Node**.
  * **Qualquer UI de Node/app pode editar** a lista; as alterações são persistidas pelo Gateway e transmitidas para todos.
  * macOS e iOS mantêm alternâncias locais de **Ativação por voz habilitada/desabilitada** (a UX local e as permissões diferem).
  * Atualmente, o Android mantém a Ativação por voz desativada e usa um fluxo manual de microfone na aba Voz.


## Armazenamento (host do Gateway)

As palavras de ativação são armazenadas na máquina do Gateway em:

  * `~/.openclaw/settings/voicewake.json`


Formato:

jsonCopy code
[code]
    { "triggers": ["openclaw", "claude", "computer"], "updatedAtMs": 1730000000000 }
[/code]

## Protocolo

### Métodos

  * `voicewake.get` → `{ triggers: string[] }`
  * `voicewake.set` com parâmetros `{ triggers: string[] }` → `{ triggers: string[] }`


Observações:

  * Os gatilhos são normalizados (espaços aparados, vazios removidos). Listas vazias retornam aos padrões.
  * Limites são aplicados por segurança (limites de quantidade/tamanho).


### Métodos de roteamento (gatilho → destino)

  * `voicewake.routing.get` → `{ config: VoiceWakeRoutingConfig }`
  * `voicewake.routing.set` com parâmetros `{ config: VoiceWakeRoutingConfig }` → `{ config: VoiceWakeRoutingConfig }`


Formato de `VoiceWakeRoutingConfig`:

jsonCopy code
[code]
    {  "version": 1,  "defaultTarget": { "mode": "current" },  "routes": [{ "trigger": "robot wake", "target": { "sessionKey": "agent:main:main" } }],  "updatedAtMs": 1730000000000}
[/code]

Os destinos de rota oferecem suporte a exatamente um de:

  * `{ "mode": "current" }`
  * `{ "agentId": "main" }`
  * `{ "sessionKey": "agent:main:main" }`


### Eventos

  * carga útil de `voicewake.changed` `{ triggers: string[] }`
  * carga útil de `voicewake.routing.changed` `{ config: VoiceWakeRoutingConfig }`


Quem recebe:

  * Todos os clientes WebSocket (app macOS, WebChat etc.)
  * Todos os Nodes conectados (iOS/Android), e também no momento em que um Node se conecta, como envio inicial do "estado atual".


## Comportamento do cliente

### App macOS

  * Usa a lista global para controlar os gatilhos de `VoiceWakeRuntime`.
  * Editar "Palavras de gatilho" nas configurações de Ativação por voz chama `voicewake.set` e então depende da transmissão para manter outros clientes sincronizados.


### Node iOS

  * Usa a lista global para detecção de gatilhos de `VoiceWakeManager`.
  * Editar Palavras de ativação em Configurações chama `voicewake.set` (pelo WS do Gateway) e também mantém a detecção local de palavras de ativação responsiva.


### Node Android

  * Atualmente, a Ativação por voz está desabilitada no runtime/configurações do Android.
  * A voz no Android usa captura manual de microfone na aba Voz em vez de gatilhos por palavras de ativação.


## Relacionado

  * [Modo de conversa](</pt-BR/nodes/talk>)
  * [Áudio e notas de voz](</pt-BR/nodes/audio>)
  * [Compreensão de mídia](</pt-BR/nodes/media-understanding>)


Was this useful?YesNo