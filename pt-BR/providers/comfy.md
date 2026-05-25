---
title: ComfyUI
source_url: https://docs.openclaw.ai/pt-BR/providers/comfy
scraped_at: 2026-05-25
---

O OpenClaw inclui um plugin `comfy` no pacote para execuções do ComfyUI orientadas por fluxo de trabalho. O plugin é totalmente orientado por fluxo de trabalho, então o OpenClaw não tenta mapear controles genéricos de `size`, `aspectRatio`, `resolution`, `durationSeconds` ou no estilo de TTS para o seu grafo.

Propriedade | Detalhe  
---|---  
Provider | `comfy`  
Models | `comfy/workflow`  
Superfícies compartilhadas | `image_generate`, `video_generate`, `music_generate`  
Auth | Nenhuma para ComfyUI local; `COMFY_API_KEY` ou `COMFY_CLOUD_API_KEY` para Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` e Comfy Cloud `/api/*`  
  
## O que ele oferece

  * Geração de imagem a partir de um JSON de fluxo de trabalho
  * Edição de imagem com 1 imagem de referência enviada
  * Geração de vídeo a partir de um JSON de fluxo de trabalho
  * Geração de vídeo com 1 imagem de referência enviada
  * Geração de música ou áudio por meio da ferramenta compartilhada `music_generate`
  * Download da saída de um nó configurado ou de todos os nós de saída correspondentes


## Primeiros passos

Escolha entre executar o ComfyUI na sua própria máquina ou usar o Comfy Cloud.

### Local

**Ideal para:** executar sua própria instância do ComfyUI na sua máquina ou LAN.

* ### Inicie o ComfyUI localmente

Certifique-se de que sua instância local do ComfyUI esteja em execução (o padrão é `http://127.0.0.1:8188`).

* ### Prepare o JSON do seu fluxo de trabalho

Exporte ou crie um arquivo JSON de fluxo de trabalho do ComfyUI. Anote os IDs dos nós para o nó de entrada do prompt e o nó de saída do qual você quer que o OpenClaw leia.

* ### Configure o provider

Defina `mode: "local"` e aponte para seu arquivo de fluxo de trabalho. Aqui está um exemplo mínimo de imagem:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Defina o modelo padrão

Aponte o OpenClaw para o modelo `comfy/workflow` para a capacidade que você configurou:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifique

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Ideal para:** executar fluxos de trabalho no Comfy Cloud sem gerenciar recursos locais de GPU.

* ### Obtenha uma chave de API

Cadastre-se em [comfy.org](<https://comfy.org>) e gere uma chave de API no painel da sua conta.

* ### Defina a chave de API

Forneça sua chave por um destes métodos:

bashCopy code
[code]
    # Variável de ambiente (preferencial)export COMFY_API_KEY="your-key" # Variável de ambiente alternativaexport COMFY_CLOUD_API_KEY="your-key" # Ou inline na configuraçãoopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Prepare o JSON do seu fluxo de trabalho

Exporte ou crie um arquivo JSON de fluxo de trabalho do ComfyUI. Anote os IDs dos nós para o nó de entrada do prompt e o nó de saída.

* ### Configure o provider

Defina `mode: "cloud"` e aponte para seu arquivo de fluxo de trabalho:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Defina o modelo padrão

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifique

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Configuração

O Comfy oferece suporte a configurações compartilhadas de conexão no nível superior, além de seções de fluxo de trabalho por capacidade (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Chaves compartilhadas

Chave | Tipo | Descrição  
---|---|---  
`mode` | `"local"` or `"cloud"` | Modo de conexão.  
`baseUrl` | string | O padrão é `http://127.0.0.1:8188` para local ou `https://cloud.comfy.org` para cloud.  
`apiKey` | string | Chave inline opcional, alternativa às variáveis de ambiente `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Permite um `baseUrl` privado/LAN no modo cloud.  
  
### Chaves por capacidade

Estas chaves se aplicam dentro das seções `image`, `video` ou `music`:

Chave | Obrigatória | Padrão | Descrição  
---|---|---|---  
`workflow` ou `workflowPath` | Sim | \-- | Caminho para o arquivo JSON do fluxo de trabalho do ComfyUI.  
`promptNodeId` | Sim | \-- | ID do nó que recebe o prompt de texto.  
`promptInputName` | Não | `"text"` | Nome da entrada no nó do prompt.  
`outputNodeId` | Não | \-- | ID do nó para ler a saída. Se omitido, todos os nós de saída correspondentes serão usados.  
`pollIntervalMs` | Não | \-- | Intervalo de polling em milissegundos para a conclusão do trabalho.  
`timeoutMs` | Não | \-- | Tempo limite em milissegundos para a execução do fluxo de trabalho.  
  
As seções `image` e `video` também oferecem suporte a:

Chave | Obrigatória | Padrão | Descrição  
---|---|---|---  
`inputImageNodeId` | Sim (ao passar uma imagem de referência) | \-- | ID do nó que recebe a imagem de referência enviada.  
`inputImageInputName` | Não | `"image"` | Nome da entrada no nó da imagem.  
  
## Detalhes do fluxo de trabalho

Fluxos de trabalho de imagem

Defina o modelo de imagem padrão como `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Exemplo de edição com imagem de referência:**

Para ativar a edição de imagem com uma imagem de referência enviada, adicione `inputImageNodeId` à sua configuração de imagem:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Fluxos de trabalho de vídeo

Defina o modelo de vídeo padrão como `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Os fluxos de trabalho de vídeo do Comfy oferecem suporte a texto para vídeo e imagem para vídeo por meio do grafo configurado.

Fluxos de trabalho de música

O plugin incluído no pacote registra um provider de geração de música para saídas de áudio ou música definidas por fluxo de trabalho, expostas por meio da ferramenta compartilhada `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Use a seção de configuração `music` para apontar para o JSON do seu fluxo de trabalho de áudio e para o nó de saída.

Compatibilidade com versões anteriores

A configuração de imagem existente no nível superior (sem a seção `image` aninhada) ainda funciona:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

O OpenClaw trata esse formato legado como a configuração do fluxo de trabalho de imagem. Você não precisa migrar imediatamente, mas as seções aninhadas `image` / `video` / `music` são recomendadas para novas configurações.

Testes ao vivo

Existe cobertura ao vivo opcional para o plugin incluído no pacote:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

O teste ao vivo ignora casos individuais de imagem, vídeo ou música, a menos que a seção correspondente do fluxo de trabalho do Comfy esteja configurada.

## Relacionado

[**Geração de imagem** Configuração e uso da ferramenta de geração de imagem. ](</pt-BR/tools/image-generation>) [**Geração de vídeo** Configuração e uso da ferramenta de geração de vídeo. ](</pt-BR/tools/video-generation>) [**Geração de música** Configuração da ferramenta de geração de música e áudio. ](</pt-BR/tools/music-generation>) [**Diretório de providers** Visão geral de todos os providers e referências de modelos. ](</pt-BR/providers>) [**Referência de configuração** Referência completa de configuração, incluindo os padrões do agente. ](</pt-BR/gateway/config-agents#agent-defaults>)

Was this useful?YesNo