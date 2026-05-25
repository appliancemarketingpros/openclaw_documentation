---
title: Diferenças
source_url: https://docs.openclaw.ai/pt-BR/tools/diffs
scraped_at: 2026-05-25
---

`diffs` é uma ferramenta opcional de plugin com orientação de sistema curta integrada e uma Skills complementar que transforma conteúdo de alterações em um artefato de diff somente leitura para agentes.

Ela aceita:

  * texto `before` e `after`
  * um `patch` unificado


Ela pode retornar:

  * uma URL do visualizador do Gateway para apresentação em canvas
  * um caminho de arquivo renderizado (PNG ou PDF) para entrega por mensagem
  * ambas as saídas em uma única chamada


Quando habilitado, o plugin acrescenta uma orientação concisa de uso ao espaço do prompt de sistema e também expõe uma Skills detalhada para casos em que o agente precisa de instruções mais completas.

## Início rápido

* ### Instale o plugin

bashCopy code
[code]
    openclaw plugins install diffs
[/code]

* ### Habilite o plugin

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,      },    },  },}
[/code]

* ### Escolha um modo

### view

Fluxos focados em canvas: os agentes chamam `diffs` com `mode: "view"` e abrem `details.viewerUrl` com `canvas present`.

### file

Entrega de arquivo no chat: os agentes chamam `diffs` com `mode: "file"` e enviam `details.filePath` com `message` usando `path` ou `filePath`.

### both

Combinado: os agentes chamam `diffs` com `mode: "both"` para obter ambos os artefatos em uma única chamada.

## Desabilitar a orientação de sistema integrada

Se quiser manter a ferramenta `diffs` habilitada, mas desabilitar sua orientação integrada de prompt de sistema, defina `plugins.entries.diffs.hooks.allowPromptInjection` como `false`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        hooks: {          allowPromptInjection: false,        },      },    },  },}
[/code]

Isso bloqueia o hook `before_prompt_build` do plugin diffs, mantendo o plugin, a ferramenta e a Skills complementar disponíveis.

Se quiser desabilitar tanto a orientação quanto a ferramenta, desabilite o plugin.

## Fluxo de trabalho típico do agente

* ### Chamar diffs

O agente chama a ferramenta `diffs` com a entrada.

* ### Ler details

O agente lê os campos de `details` na resposta.

* ### Apresentar

O agente abre `details.viewerUrl` com `canvas present`, envia `details.filePath` com `message` usando `path` ou `filePath`, ou faz ambos.

## Exemplos de entrada

### Antes e depois

jsonCopy code
[code]
    {  "before": "# Hello\n\nOne",  "after": "# Hello\n\nTwo",  "path": "docs/example.md",  "mode": "view"}
[/code]

### Patch

jsonCopy code
[code]
    {  "patch": "diff --git a/src/example.ts b/src/example.ts\n--- a/src/example.ts\n+++ b/src/example.ts\n@@ -1 +1 @@\n-const x = 1;\n+const x = 2;\n",  "mode": "both"}
[/code]

## Referência de entrada da ferramenta

Todos os campos são opcionais, salvo indicação em contrário.

Texto original. Obrigatório com `after` quando `patch` é omitido.

Texto atualizado. Obrigatório com `before` quando `patch` é omitido.

Texto de diff unificado. Mutuamente exclusivo com `before` e `after`.

Nome de arquivo exibido para o modo antes e depois.

Dica de substituição de idioma para o modo antes e depois. Valores desconhecidos voltam para texto simples.

Substituição do título do visualizador.

Modo de saída. O padrão é o padrão do plugin `defaults.mode`. Alias obsoleto: `"image"` se comporta como `"file"` e ainda é aceito para compatibilidade retroativa.

Tema do visualizador. O padrão é o padrão do plugin `defaults.theme`.

Layout do diff. O padrão é o padrão do plugin `defaults.layout`.

Expande seções inalteradas quando o contexto completo está disponível. Opção apenas por chamada (não é uma chave padrão do plugin).

Formato do arquivo renderizado. O padrão é o padrão do plugin `defaults.fileFormat`.

Predefinição de qualidade para renderização em PNG ou PDF.

Substituição da escala do dispositivo (`1`-`4`).

Largura máxima de renderização em pixels CSS (`640`-`2400`).

TTL do artefato em segundos para saídas de visualizador e arquivo autônomo. Máximo 21600.

Substituição da origem da URL do visualizador. Substitui `viewerBaseUrl` do plugin. Deve ser `http` ou `https`, sem consulta/hash.

Aliases de entrada legados

Ainda aceitos para compatibilidade retroativa:

  * `format` -> `fileFormat`
  * `imageFormat` -> `fileFormat`
  * `imageQuality` -> `fileQuality`
  * `imageScale` -> `fileScale`
  * `imageMaxWidth` -> `fileMaxWidth`

Validação e limites

  * `before` e `after` têm no máximo 512 KiB cada.
  * `patch` tem no máximo 2 MiB.
  * `path` tem no máximo 2048 bytes.
  * `lang` tem no máximo 128 bytes.
  * `title` tem no máximo 1024 bytes.
  * Limite de complexidade de patch: máximo de 128 arquivos e 120000 linhas no total.
  * `patch` junto com `before` ou `after` é rejeitado.
  * Limites de segurança do arquivo renderizado (aplicam-se a PNG e PDF): 
    * `fileQuality: "standard"`: máximo de 8 MP (8.000.000 pixels renderizados).
    * `fileQuality: "hq"`: máximo de 14 MP (14.000.000 pixels renderizados).
    * `fileQuality: "print"`: máximo de 24 MP (24.000.000 pixels renderizados).
    * PDF também tem um máximo de 50 páginas.


## Contrato de detalhes de saída

A ferramenta retorna metadados estruturados em `details`.

Campos do visualizador

Campos compartilhados para modos que criam um visualizador:

  * `artifactId`
  * `viewerUrl`
  * `viewerPath`
  * `title`
  * `expiresAt`
  * `inputKind`
  * `fileCount`
  * `mode`
  * `context` (`agentId`, `sessionId`, `messageChannel`, `agentAccountId` quando disponível)

Campos de arquivo

Campos de arquivo quando PNG ou PDF é renderizado:

  * `artifactId`
  * `expiresAt`
  * `filePath`
  * `path` (mesmo valor de `filePath`, para compatibilidade com a ferramenta de mensagem)
  * `fileBytes`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`

Aliases de compatibilidade

Também retornados para chamadores existentes:

  * `format` (mesmo valor de `fileFormat`)
  * `imagePath` (mesmo valor de `filePath`)
  * `imageBytes` (mesmo valor de `fileBytes`)
  * `imageQuality` (mesmo valor de `fileQuality`)
  * `imageScale` (mesmo valor de `fileScale`)
  * `imageMaxWidth` (mesmo valor de `fileMaxWidth`)


Resumo do comportamento dos modos:

Modo | O que é retornado  
---|---  
`"view"` | Apenas campos do visualizador.  
`"file"` | Apenas campos de arquivo, sem artefato de visualizador.  
`"both"` | Campos do visualizador mais campos de arquivo. Se a renderização do arquivo falhar, o visualizador ainda retorna com `fileError` e o alias `imageError`.  
  
## Seções inalteradas recolhidas

  * O visualizador pode mostrar linhas como `N unmodified lines`.
  * Controles de expansão nessas linhas são condicionais e não são garantidos para todo tipo de entrada.
  * Controles de expansão aparecem quando o diff renderizado tem dados de contexto expansíveis, o que é típico para entrada antes e depois.
  * Para muitas entradas de patch unificado, os corpos de contexto omitidos não estão disponíveis nos hunks do patch analisado, portanto a linha pode aparecer sem controles de expansão. Esse é o comportamento esperado.
  * `expandUnchanged` se aplica apenas quando há contexto expansível.


## Padrões do plugin

Defina padrões para todo o plugin em `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          defaults: {            fontFamily: "Fira Code",            fontSize: 15,            lineSpacing: 1.6,            layout: "unified",            showLineNumbers: true,            diffIndicators: "bars",            wordWrap: true,            background: true,            theme: "dark",            fileFormat: "png",            fileQuality: "standard",            fileScale: 2,            fileMaxWidth: 960,            mode: "both",            ttlSeconds: 21600,          },        },      },    },  },}
[/code]

Padrões compatíveis:

  * `fontFamily`
  * `fontSize`
  * `lineSpacing`
  * `layout`
  * `showLineNumbers`
  * `diffIndicators`
  * `wordWrap`
  * `background`
  * `theme`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`
  * `mode`
  * `ttlSeconds`


Parâmetros explícitos da ferramenta substituem esses padrões.

### Configuração persistente da URL do visualizador

Fallback pertencente ao plugin para links de visualizador retornados quando uma chamada de ferramenta não passa `baseUrl`. Deve ser `http` ou `https`, sem consulta/hash.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          viewerBaseUrl: "https://gateway.example.com/openclaw",        },      },    },  },}
[/code]

## Configuração de segurança

`false`: solicitações que não são local loopback para rotas do visualizador são negadas. `true`: visualizadores remotos são permitidos se o caminho tokenizado for válido.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          security: {            allowRemoteViewer: false,          },        },      },    },  },}
[/code]

## Ciclo de vida e armazenamento de artefatos

  * Artefatos são armazenados na subpasta temporária: `$TMPDIR/openclaw-diffs`.
  * Os metadados do artefato do visualizador contêm: 
    * ID de artefato aleatório (20 caracteres hexadecimais)
    * token aleatório (48 caracteres hexadecimais)
    * `createdAt` e `expiresAt`
    * caminho `viewer.html` armazenado
  * O TTL padrão do artefato é 30 minutos quando não especificado.
  * O TTL máximo aceito do visualizador é 6 horas.
  * A limpeza é executada de forma oportunista após a criação do artefato.
  * Artefatos expirados são excluídos.
  * A limpeza de fallback remove pastas obsoletas com mais de 24 horas quando os metadados estão ausentes.


## URL do visualizador e comportamento de rede

Rota do visualizador:

  * `/plugins/diffs/view/{artifactId}/{token}`


Ativos do visualizador:

  * `/plugins/diffs/assets/viewer.js`
  * `/plugins/diffs/assets/viewer-runtime.js`


O documento do visualizador resolve esses ativos em relação à URL do visualizador, portanto um prefixo de caminho opcional em `baseUrl` também é preservado para ambas as solicitações de ativos.

Comportamento de construção de URL:

  * Se `baseUrl` da chamada de ferramenta for fornecido, ele será usado após validação rigorosa.
  * Caso contrário, se `viewerBaseUrl` do plugin estiver configurado, ele será usado.
  * Sem nenhuma das substituições, a URL do visualizador usa por padrão o local loopback `127.0.0.1`.
  * Se o modo de bind do gateway for `custom` e `gateway.customBindHost` estiver definido, esse host será usado.


Regras de `baseUrl`:

  * Deve ser `http://` ou `https://`.
  * Consulta e hash são rejeitados.
  * Origem mais caminho base opcional é permitido.


## Modelo de segurança

Reforço de segurança do visualizador

  * Apenas loopback por padrão.
  * Caminhos do visualizador tokenizados com validação rigorosa de ID e token.
  * CSP da resposta do visualizador: 
    * `default-src 'none'`
    * scripts e ativos somente da própria origem
    * sem `connect-src` de saída
  * Limitação de falhas remotas quando o acesso remoto está habilitado: 
    * 40 falhas a cada 60 segundos
    * bloqueio de 60 segundos (`429 Too Many Requests`)

Reforço de segurança da renderização de arquivos

  * O roteamento de solicitações do navegador para captura de tela é negar por padrão.
  * Somente ativos locais do visualizador de `http://127.0.0.1/plugins/diffs/assets/*` são permitidos.
  * Solicitações de rede externas são bloqueadas.


## Requisitos de navegador para o modo de arquivo

`mode: "file"` e `mode: "both"` precisam de um navegador compatível com Chromium.

Ordem de resolução:

* ### Configuração

`browser.executablePath` na configuração do OpenClaw.

* ### Variáveis de ambiente

  * `OPENCLAW_BROWSER_EXECUTABLE_PATH`
  * `BROWSER_EXECUTABLE_PATH`
  * `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`


* ### Fallback da plataforma

Fallback de descoberta de comando/caminho da plataforma.

Texto comum de falha:

  * `Diff PNG/PDF rendering requires a Chromium-compatible browser...`


Corrija instalando Chrome, Chromium, Edge ou Brave, ou definindo uma das opções de caminho de executável acima.

## Solução de problemas

Erros de validação de entrada

  * `Provide patch or both before and after text.` — inclua `before` e `after`, ou forneça `patch`.
  * `Provide either patch or before/after input, not both.` — não misture modos de entrada.
  * `Invalid baseUrl: ...` — use origem `http(s)` com caminho opcional, sem query/hash.
  * `{field} exceeds maximum size (...)` — reduza o tamanho do payload.
  * Rejeição de patch grande — reduza a contagem de arquivos do patch ou o total de linhas.

Acessibilidade do visualizador

  * A URL do visualizador resolve para `127.0.0.1` por padrão.
  * Para cenários de acesso remoto: 
    * defina `viewerBaseUrl` do plugin, ou
    * passe `baseUrl` por chamada de ferramenta, ou
    * use `gateway.bind=custom` e `gateway.customBindHost`
  * Se `gateway.trustedProxies` incluir loopback para um proxy no mesmo host (por exemplo, Tailscale Serve), solicitações brutas de loopback ao visualizador sem cabeçalhos de IP de cliente encaminhados falham fechadas por design.
  * Para essa topologia de proxy: 
    * prefira `mode: "file"` ou `mode: "both"` quando você só precisar de um anexo, ou
    * habilite intencionalmente `security.allowRemoteViewer` e defina `viewerBaseUrl` do plugin ou passe um `baseUrl` de proxy/público quando precisar de uma URL compartilhável do visualizador
  * Habilite `security.allowRemoteViewer` somente quando você pretender acesso externo ao visualizador.

A linha de linhas não modificadas não tem botão de expansão

Isso pode acontecer para entrada de patch quando o patch não carrega contexto expansível. Isso é esperado e não indica falha do visualizador.

Artefato não encontrado

  * O artefato expirou devido ao TTL.
  * O token ou caminho mudou.
  * A limpeza removeu dados obsoletos.


## Orientação operacional

  * Prefira `mode: "view"` para revisões interativas locais no canvas.
  * Prefira `mode: "file"` para canais de chat de saída que precisam de um anexo.
  * Mantenha `allowRemoteViewer` desabilitado, a menos que sua implantação exija URLs remotas do visualizador.
  * Defina `ttlSeconds` curtos e explícitos para diffs sensíveis.
  * Evite enviar segredos na entrada de diff quando não for necessário.
  * Se seu canal comprime imagens agressivamente (por exemplo, Telegram ou WhatsApp), prefira saída em PDF (`fileFormat: "pdf"`).


## Relacionados

  * [Navegador](</pt-BR/tools/browser>)
  * [Plugins](</pt-BR/tools/plugin>)
  * [Visão geral das ferramentas](</pt-BR/tools>)


Was this useful?YesNo