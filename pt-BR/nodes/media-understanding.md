---
title: Compreensão de mídia
source_url: https://docs.openclaw.ai/pt-BR/nodes/media-understanding
scraped_at: 2026-05-25
---

OpenClaw pode **resumir mídia recebida** (imagem/áudio/vídeo) antes que o pipeline de resposta seja executado. Ele detecta automaticamente quando ferramentas locais ou chaves de provedores estão disponíveis, e pode ser desabilitado ou personalizado. Se a compreensão estiver desativada, os modelos ainda receberão os arquivos/URLs originais como de costume.

O comportamento de mídia específico de cada fornecedor é registrado por Plugins de fornecedor, enquanto o núcleo do OpenClaw é responsável pela configuração compartilhada de `tools.media`, pela ordem de fallback e pela integração com o pipeline de resposta.

## Objetivos

  * Opcional: pré-digerir mídia recebida em texto curto para roteamento mais rápido + melhor análise de comandos.
  * Preservar a entrega da mídia original ao modelo (sempre).
  * Dar suporte a **APIs de provedores** e **fallbacks de CLI**.
  * Permitir vários modelos com fallback ordenado (erro/tamanho/tempo limite).


## Comportamento de alto nível

* ### Coletar anexos

Coletar anexos recebidos (`MediaPaths`, `MediaUrls`, `MediaTypes`).

* ### Selecionar por capacidade

Para cada capacidade habilitada (imagem/áudio/vídeo), selecionar anexos por política (padrão: **primeiro**).

* ### Escolher modelo

Escolher a primeira entrada de modelo elegível (tamanho + capacidade + autenticação).

* ### Fallback em caso de falha

Se um modelo falhar ou a mídia for grande demais, **fazer fallback para a próxima entrada**.

* ### Aplicar bloco de sucesso

Em caso de sucesso:

  * `Body` se torna o bloco `[Image]`, `[Audio]` ou `[Video]`.
  * Áudio define `{{Transcript}}`; a análise de comandos usa o texto da legenda quando presente, caso contrário usa a transcrição.
  * As legendas são preservadas como `User text:` dentro do bloco.


Se a compreensão falhar ou estiver desabilitada, **o fluxo de resposta continua** com o corpo original + anexos.

## Visão geral da configuração

`tools.media` oferece suporte a **modelos compartilhados** mais substituições por capacidade:

Chaves de nível superior

  * `tools.media.models`: lista de modelos compartilhada (use `capabilities` para restringir).
  * `tools.media.image` / `tools.media.audio` / `tools.media.video`: 
    * padrões (`prompt`, `maxChars`, `maxBytes`, `timeoutSeconds`, `language`)
    * substituições de provedor (`baseUrl`, `headers`, `providerOptions`)
    * opções de áudio do Deepgram via `tools.media.audio.providerOptions.deepgram`
    * controles de eco da transcrição de áudio (`echoTranscript`, padrão `false`; `echoFormat`)
    * **lista`models` por capacidade** opcional (preferida antes dos modelos compartilhados)
    * política de `attachments` (`mode`, `maxAttachments`, `prefer`)
    * `scope` (restrição opcional por canal/chatType/chave de sessão)
  * `tools.media.concurrency`: máximo de execuções de capacidade simultâneas (padrão **2**).


json5Copy code
[code]
    {  tools: {    media: {      models: [        /* shared list */      ],      image: {        /* optional overrides */      },      audio: {        /* optional overrides */        echoTranscript: true,        echoFormat: '📝 "{transcript}"',      },      video: {        /* optional overrides */      },    },  },}
[/code]

### Entradas de modelo

Cada entrada de `models[]` pode ser **provedor** ou **CLI** :

### Entrada de provedor

json5Copy code
[code]
    {  type: "provider", // default if omitted  provider: "openai",  model: "gpt-5.5",  prompt: "Describe the image in <= 500 chars.",  maxChars: 500,  maxBytes: 10485760,  timeoutSeconds: 60,  capabilities: ["image"], // optional, used for multi-modal entries  profile: "vision-profile",  preferredProfile: "vision-fallback",}
[/code]

### Entrada de CLI

json5Copy code
[code]
    {  type: "cli",  command: "gemini",  args: [    "-m",    "gemini-3-flash",    "--allowed-tools",    "read_file",    "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",  ],  maxChars: 500,  maxBytes: 52428800,  timeoutSeconds: 120,  capabilities: ["video", "image"],}
[/code]

Modelos de CLI também podem usar:

  * `{{MediaDir}}` (diretório que contém o arquivo de mídia)
  * `{{OutputDir}}` (diretório de rascunho criado para esta execução)
  * `{{OutputBase}}` (caminho base do arquivo de rascunho, sem extensão)


## Padrões e limites

Padrões recomendados:

  * `maxChars`: **500** para imagem/vídeo (curto, amigável para comandos)
  * `maxChars`: **não definido** para áudio (transcrição completa, a menos que você defina um limite)
  * `maxBytes`: 
    * imagem: **10MB**
    * áudio: **20MB**
    * vídeo: **50MB**


Regras

  * Se a mídia exceder `maxBytes`, esse modelo será ignorado e o **próximo modelo será tentado**.
  * Arquivos de áudio menores que **1024 bytes** são tratados como vazios/corrompidos e ignorados antes da transcrição por provedor/CLI; o contexto de resposta recebida recebe uma transcrição de placeholder determinística para que o agente saiba que a nota era pequena demais.
  * Se o modelo retornar mais que `maxChars`, a saída será cortada.
  * `prompt` usa como padrão um simples "Describe the {media}." mais a orientação de `maxChars` (somente imagem/vídeo).
  * Se o modelo de imagem primário ativo já oferecer suporte nativo a visão, o OpenClaw ignora o bloco de resumo `[Image]` e passa a imagem original para o modelo.
  * Se um modelo primário de Gateway/WebChat for somente texto, anexos de imagem são preservados como refs `media://inbound/*` descarregadas para que as ferramentas de imagem/PDF ou o modelo de imagem configurado ainda possam inspecioná-los em vez de perder o anexo.
  * Solicitações explícitas `openclaw infer image describe --model <provider/model>` são diferentes: elas executam esse provedor/modelo com capacidade de imagem diretamente, incluindo refs do Ollama como `ollama/qwen2.5vl:7b`.
  * Se `<capability>.enabled: true` mas nenhum modelo estiver configurado, o OpenClaw tenta o **modelo de resposta ativo** quando o provedor dele oferece suporte à capacidade.


### Detectar automaticamente a compreensão de mídia (padrão)

Se `tools.media.<capability>.enabled` **não** estiver definido como `false` e você não tiver configurado modelos, o OpenClaw detecta automaticamente nesta ordem e **para na primeira opção funcional** :

* ### Modelo de resposta ativo

Modelo de resposta ativo quando o provedor dele oferece suporte à capacidade.

* ### agents.defaults.imageModel

Refs primária/fallback de `agents.defaults.imageModel` (somente imagem). Prefira refs `provider/model`. Refs simples são qualificadas a partir de entradas de modelos de provedores configurados com capacidade de imagem somente quando a correspondência é única.

* ### CLIs locais (somente áudio)

CLIs locais (se instaladas):

  * `sherpa-onnx-offline` (requer `SHERPA_ONNX_MODEL_DIR` com encoder/decoder/joiner/tokens)
  * `whisper-cli` (`whisper-cpp`; usa `WHISPER_CPP_MODEL` ou o modelo tiny incluído)
  * `whisper` (CLI do Python; baixa modelos automaticamente)


* ### CLI do Gemini

`gemini` usando `read_many_files`.

* ### Autenticação do provedor

  * Entradas `models.providers.*` configuradas que oferecem suporte à capacidade são tentadas antes da ordem de fallback incluída.
  * Provedores de configuração somente de imagem com um modelo com capacidade de imagem se registram automaticamente para compreensão de mídia mesmo quando não são um Plugin de fornecedor incluído.
  * A compreensão de imagem do Ollama fica disponível quando selecionada explicitamente, por exemplo por meio de `agents.defaults.imageModel` ou `openclaw infer image describe --model ollama/<vision-model>`.


Ordem de fallback incluída:

  * Áudio: OpenAI → Groq → xAI → Deepgram → OpenRouter → Google → SenseAudio → ElevenLabs → Mistral
  * Imagem: OpenAI → Anthropic → Google → MiniMax → MiniMax Portal → [Z.AI](<http://Z.AI>)
  * Vídeo: Google → Qwen → Moonshot


Para desabilitar a detecção automática, defina:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: false,      },    },  },}
[/code]

### Suporte a ambiente de proxy (modelos de provedor)

Quando a compreensão de mídia por **áudio** e **vídeo** baseada em provedor está habilitada, o OpenClaw respeita variáveis de ambiente padrão de proxy de saída para chamadas HTTP de provedor:

  * `HTTPS_PROXY`
  * `HTTP_PROXY`
  * `ALL_PROXY`
  * `https_proxy`
  * `http_proxy`
  * `all_proxy`


Se nenhuma variável de ambiente de proxy estiver definida, a compreensão de mídia usa saída direta. Se o valor do proxy estiver malformado, o OpenClaw registra um aviso e faz fallback para busca direta.

## Capacidades (opcional)

Se você definir `capabilities`, a entrada só será executada para esses tipos de mídia. Para listas compartilhadas, o OpenClaw pode inferir padrões:

  * `openai`, `anthropic`, `minimax`: **imagem**
  * `minimax-portal`: **imagem**
  * `moonshot`: **imagem + vídeo**
  * `openrouter`: **imagem + áudio**
  * `google` (Gemini API): **imagem + áudio + vídeo**
  * `qwen`: **imagem + vídeo**
  * `mistral`: **áudio**
  * `zai`: **imagem**
  * `groq`: **áudio**
  * `xai`: **áudio**
  * `deepgram`: **áudio**
  * Qualquer catálogo `models.providers.<id>.models[]` com um modelo com capacidade de imagem: **imagem**


Para entradas de CLI, **defina`capabilities` explicitamente** para evitar correspondências surpreendentes. Se você omitir `capabilities`, a entrada será elegível para a lista em que aparece.

## Matriz de suporte de provedores (integrações do OpenClaw)

Capacidade | Integração de provedor | Observações  
---|---|---  
Imagem | OpenAI, OpenAI Codex OAuth, Codex app-server, OpenRouter, Anthropic, Google, MiniMax, Moonshot, Qwen, [Z.AI](<http://Z.AI>), provedores de configuração | Plugins de fornecedor registram suporte a imagem; `openai-codex/*` usa o encanamento do provedor OAuth; `codex/*` usa um turno limitado do Codex app-server; MiniMax e MiniMax OAuth usam `MiniMax-VL-01`; provedores de configuração com capacidade de imagem se registram automaticamente.  
Áudio | OpenAI, Groq, xAI, Deepgram, OpenRouter, Google, SenseAudio, ElevenLabs, Mistral | Transcrição de provedor (Whisper/Groq/xAI/Deepgram/OpenRouter STT/Gemini/SenseAudio/Scribe/Voxtral).  
Vídeo | Google, Qwen, Moonshot | Compreensão de vídeo por provedor via Plugins de fornecedor; a compreensão de vídeo do Qwen usa os endpoints Standard DashScope.  
  
## Orientação para seleção de modelo

  * Prefira o modelo mais forte da geração mais recente disponível para cada capacidade de mídia quando qualidade e segurança forem importantes.
  * Para agentes com ferramentas habilitadas que lidam com entradas não confiáveis, evite modelos de mídia mais antigos/mais fracos.
  * Mantenha pelo menos um fallback por capacidade para disponibilidade (modelo de qualidade + modelo mais rápido/mais barato).
  * Fallbacks de CLI (`whisper-cli`, `whisper`, `gemini`) são úteis quando APIs de provedores estão indisponíveis.
  * Observação sobre `parakeet-mlx`: com `--output-dir`, o OpenClaw lê `<output-dir>/<media-basename>.txt` quando o formato de saída é `txt` (ou não especificado); formatos diferentes de `txt` fazem fallback para stdout.


## Política de anexos

`attachments` por capacidade controla quais anexos são processados:

Se deve processar o primeiro anexo selecionado ou todos eles.

Limita o número processado.

Preferência de seleção entre anexos candidatos.

Quando `mode: "all"`, as saídas são rotuladas como `[Image 1/2]`, `[Audio 2/2]` etc.

Comportamento de extração de anexos de arquivo

  * O texto extraído do arquivo é encapsulado como **conteúdo externo não confiável** antes de ser anexado ao prompt de mídia.
  * O bloco injetado usa marcadores de limite explícitos como `<<&lt;EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` / `<<&lt;END_EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` e inclui uma linha de metadados `Source: External`.
  * Este caminho de extração de anexos omite intencionalmente o banner longo `SECURITY NOTICE:` para evitar inflar o prompt de mídia; os marcadores de limite e os metadados ainda permanecem.
  * Se um arquivo não tiver texto extraível, o OpenClaw injeta `[No extractable text]`.
  * Se um PDF recorrer a imagens renderizadas das páginas nesse caminho, o prompt de mídia mantém o placeholder `[PDF content rendered to images; images not forwarded to model]` porque esta etapa de extração de anexos encaminha blocos de texto, não as imagens renderizadas do PDF.


## Exemplos de configuração

### Modelos compartilhados + substituições

json5Copy code
[code]
    {  tools: {    media: {      models: [        { provider: "openai", model: "gpt-5.5", capabilities: ["image"] },        {          provider: "google",          model: "gemini-3-flash-preview",          capabilities: ["image", "audio", "video"],        },        {          type: "cli",          command: "gemini",          args: [            "-m",            "gemini-3-flash",            "--allowed-tools",            "read_file",            "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",          ],          capabilities: ["image", "video"],        },      ],      audio: {        attachments: { mode: "all", maxAttachments: 2 },      },      video: {        maxChars: 500,      },    },  },}
[/code]

### Apenas áudio + vídeo

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [          { provider: "openai", model: "gpt-4o-mini-transcribe" },          {            type: "cli",            command: "whisper",            args: ["--model", "base", "{{MediaPath}}"],          },        ],      },      video: {        enabled: true,        maxChars: 500,        models: [          { provider: "google", model: "gemini-3-flash-preview" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Somente imagem

json5Copy code
[code]
    {  tools: {    media: {      image: {        enabled: true,        maxBytes: 10485760,        maxChars: 500,        models: [          { provider: "openai", model: "gpt-5.5" },          { provider: "anthropic", model: "claude-opus-4-6" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Entrada multimodal única

json5Copy code
[code]
    {  tools: {    media: {      image: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      audio: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      video: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },    },  },}
[/code]

## Saída de status

Quando o entendimento de mídia é executado, `/status` inclui uma linha curta de resumo:

CodeCopy code
[code]
    📎 Media: image ok (openai/gpt-5.4) · audio skipped (maxBytes)
[/code]

Isso mostra os resultados por capacidade e o provedor/modelo escolhido quando aplicável.

## Observações

  * O entendimento é **best-effort**. Erros não bloqueiam respostas.
  * Os anexos ainda são passados aos modelos mesmo quando o entendimento está desativado.
  * Use `scope` para limitar onde o entendimento é executado (por exemplo, somente DMs).


## Relacionado

  * [Configuração](</pt-BR/gateway/configuration>)
  * [Suporte a imagens e mídia](</pt-BR/nodes/images>)


Was this useful?YesNo