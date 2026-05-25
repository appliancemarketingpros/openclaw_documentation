---
title: Geração de música
source_url: https://docs.openclaw.ai/pt-BR/tools/music-generation
scraped_at: 2026-05-25
---

A ferramenta `music_generate` permite que o agente crie música ou áudio por meio do recurso compartilhado de geração de música com provedores configurados: Google, MiniMax e ComfyUI configurado por workflow atualmente.

Para execuções de agente com sessão, o OpenClaw inicia a geração de música como uma tarefa em segundo plano, acompanha-a no ledger de tarefas e então desperta o agente novamente quando a faixa está pronta para que o agente possa avisar o usuário e anexar o áudio finalizado. Em chats de grupo/canal que usam entrega visível somente por ferramenta de mensagem, o agente retransmite o resultado pela ferramenta de mensagem. Se o agente de conclusão escrever apenas uma resposta final privada, o OpenClaw recorre a um envio direto pelo canal com a mídia gerada. O despertar de conclusão avisa explicitamente o agente de que respostas finais normais são privadas nessas rotas.

## Início rápido

### Com provedor compartilhado

* ### Configurar autenticação

Defina uma chave de API para pelo menos um provedor — por exemplo `GEMINI_API_KEY` ou `MINIMAX_API_KEY`.

* ### Escolher um modelo padrão (opcional)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Pedir ao agente

_"Gere uma faixa synthpop animada sobre dirigir à noite por uma cidade de neon."_

O agente chama `music_generate` automaticamente. Não é necessário permitir a ferramenta em uma lista.

Para contextos síncronos diretos sem uma execução de agente com sessão, a ferramenta integrada ainda recorre à geração inline e retorna o caminho final da mídia no resultado da ferramenta.

### Workflow do ComfyUI

* ### Configurar o workflow

Configure `plugins.entries.comfy.config.music` com um workflow JSON e nós de prompt/saída.

* ### Autenticação em nuvem (opcional)

Para o Comfy Cloud, defina `COMFY_API_KEY` ou `COMFY_CLOUD_API_KEY`.

* ### Chamar a ferramenta

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Exemplos de prompts:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## Provedores compatíveis

Provedor | Modelo padrão | Entradas de referência | Controles compatíveis | Autenticação  
---|---|---|---|---  
ComfyUI | `workflow` | Até 1 imagem | Música ou áudio definidos pelo workflow | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | Até 10 imagens | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | Nenhuma | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` ou OAuth da MiniMax  
  
### Matriz de recursos

O contrato de modo explícito usado por `music_generate`, testes de contrato e a varredura live compartilhada:

Provedor | `generate` | `edit` | Limite de edição | Lanes live compartilhadas  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 imagem | Não incluído na varredura compartilhada; coberto por `extensions/comfy/comfy.live.test.ts`  
Google | ✓ | ✓ | 10 imagens | `generate`, `edit`  
MiniMax | ✓ | — | Nenhum | `generate`  
  
Use `action: "list"` para inspecionar provedores e modelos compartilhados disponíveis em runtime:

textCopy code
[code]
    /tool music_generate action=list
[/code]

Use `action: "status"` para inspecionar a tarefa ativa de música com sessão:

textCopy code
[code]
    /tool music_generate action=status
[/code]

Exemplo de geração direta:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## Parâmetros da ferramenta

Prompt de geração de música. Obrigatório para `action: "generate"`.

`"status"` retorna a tarefa atual da sessão; `"list"` inspeciona provedores.

Sobrescrita de provedor/modelo (por exemplo, `google/lyria-3-pro-preview`, `comfy/workflow`).

Letra opcional quando o provedor oferece suporte a entrada explícita de letra.

Solicita saída apenas instrumental quando o provedor oferece suporte.

Caminho ou URL de uma única imagem de referência.

Várias imagens de referência (até 10 em provedores compatíveis).

Duração alvo em segundos quando o provedor oferece suporte a dicas de duração.

Dica de formato de saída quando o provedor oferece suporte.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Timeout opcional da solicitação ao provedor em milissegundos. Quando omitido, o OpenClaw usa `agents.defaults.musicGenerationModel.timeoutMs` se configurado. Valores abaixo de 10000ms são elevados para 10000ms e informados no resultado da ferramenta. OPENCLAW_DOCS_MARKER:paramClose:

## Comportamento assíncrono

A geração de música com sessão é executada como uma tarefa em segundo plano:

  * **Tarefa em segundo plano:** `music_generate` cria uma tarefa em segundo plano, retorna uma resposta de iniciada/tarefa imediatamente e publica a faixa finalizada posteriormente em uma mensagem de acompanhamento do agente.
  * **Prevenção de duplicatas:** enquanto uma tarefa está `queued` ou `running`, chamadas `music_generate` posteriores na mesma sessão retornam o status da tarefa em vez de iniciar outra geração. Use `action: "status"` para verificar explicitamente.
  * **Consulta de status:** `openclaw tasks list` ou `openclaw tasks show <taskId>` inspeciona status em fila, em execução e terminal.
  * **Despertar de conclusão:** o OpenClaw injeta um evento interno de conclusão de volta na mesma sessão para que o modelo possa escrever o acompanhamento voltado ao usuário por conta própria.
  * **Dica de prompt:** turnos posteriores de usuário/manuais na mesma sessão recebem uma pequena dica de runtime quando uma tarefa de música já está em andamento, para que o modelo não chame `music_generate` novamente às cegas.
  * **Fallback sem sessão:** contextos diretos/locais sem uma sessão real de agente são executados inline e retornam o resultado final de áudio no mesmo turno.


### Ciclo de vida da tarefa

Estado | Significado  
---|---  
`queued` | Tarefa criada, aguardando o provedor aceitá-la.  
`running` | O provedor está processando (normalmente de 30 segundos a 3 minutos, dependendo do provedor e da duração).  
`succeeded` | Faixa pronta; o agente desperta e a publica na conversa.  
`failed` | Erro ou timeout do provedor; o agente desperta com detalhes do erro.  
  
Verifique o status pela CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## Configuração

### Seleção de modelo

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### Ordem de seleção de provedores

O OpenClaw tenta os provedores nesta ordem:

  1. Parâmetro `model` da chamada de ferramenta (se o agente especificar um).
  2. `musicGenerationModel.primary` da configuração.
  3. `musicGenerationModel.fallbacks` em ordem.
  4. Detecção automática usando apenas padrões de provedores com autenticação: 
     * provedor padrão atual primeiro;
     * demais provedores de geração de música registrados em ordem de provider-id.


Se um provedor falhar, o próximo candidato é tentado automaticamente. Se todos falharem, o erro inclui detalhes de cada tentativa.

Defina `agents.defaults.mediaGenerationAutoProviderFallback: false` para usar apenas entradas explícitas de `model`, `primary` e `fallbacks`.

## Observações de provedores

ComfyUI

Orientado por workflow e depende do grafo configurado mais o mapeamento de nós para campos de prompt/saída. O Plugin `comfy` incluído se conecta à ferramenta compartilhada `music_generate` por meio do registro de provedores de geração de música.

Google (Lyria 3)

Usa geração em lote do Lyria 3. O fluxo incluído atual oferece suporte a prompt, texto de letra opcional e imagens de referência opcionais.

MiniMax

Usa o endpoint em lote `music_generation`. Oferece suporte a prompt, letras opcionais, modo instrumental, direcionamento de duração e saída mp3 por meio de autenticação por chave de API `minimax` ou OAuth `minimax-portal`.

## Escolhendo o caminho certo

  * **Com provedor compartilhado** quando você quer seleção de modelo, failover de provedor e o fluxo assíncrono integrado de tarefa/status.
  * **Caminho de Plugin (ComfyUI)** quando você precisa de um grafo de workflow personalizado ou de um provedor que não faz parte do recurso compartilhado incluído de música.


Se você estiver depurando comportamento específico do ComfyUI, consulte [ComfyUI](</pt-BR/providers/comfy>). Se você estiver depurando comportamento de provedor compartilhado, comece por [Google (Gemini)](</pt-BR/providers/google>) ou [MiniMax](</pt-BR/providers/minimax>).

## Modos de recurso do provedor

O contrato compartilhado de geração de música oferece suporte a declarações explícitas de modo:

  * `generate` para geração apenas por prompt.
  * `edit` quando a solicitação inclui uma ou mais imagens de referência.


Novas implementações de provedor devem preferir blocos de modo explícitos:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

Campos flat legados como `maxInputImages`, `supportsLyrics` e `supportsFormat` **não** são suficientes para anunciar suporte a edição. Provedores devem declarar `generate` e `edit` explicitamente para que testes live, testes de contrato e a ferramenta compartilhada `music_generate` possam validar o suporte a modos deterministicamente.

## Testes live

Cobertura live opcional para os provedores compartilhados incluídos:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

Wrapper do repositório:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

Este arquivo live carrega variáveis de ambiente de provedor ausentes de `~/.profile`, prefere chaves de API live/env a perfis de autenticação armazenados por padrão e executa tanto a cobertura de `generate` quanto a de `edit` declarada quando o provedor habilita o modo de edição. Cobertura hoje:

  * `google`: `generate` mais `edit`
  * `minimax`: apenas `generate`
  * `comfy`: cobertura live separada do Comfy, não a varredura compartilhada de provedores


Ative a cobertura live para o caminho de música ComfyUI incluído:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

O arquivo live do Comfy também cobre fluxos de trabalho de imagem e vídeo do comfy quando essas seções estão configuradas.

## Relacionado

  * [Tarefas em segundo plano](</pt-BR/automation/tasks>) — acompanhamento de tarefas para execuções desanexadas de `music_generate`
  * [ComfyUI](</pt-BR/providers/comfy>)
  * [Referência de configuração](</pt-BR/gateway/config-agents#agent-defaults>) — configuração de `musicGenerationModel`
  * [Google (Gemini)](</pt-BR/providers/google>)
  * [MiniMax](</pt-BR/providers/minimax>)
  * [Modelos](</pt-BR/concepts/models>) — configuração de modelos e failover
  * [Visão geral das ferramentas](</pt-BR/tools>)


Was this useful?YesNo