---
title: Pontos de entrada do Plugin
source_url: https://docs.openclaw.ai/pt-BR/plugins/sdk-entrypoints
scraped_at: 2026-05-25
---

Todo plugin exporta um objeto de entrada padrão. O SDK fornece três helpers para criá-los.

Para plugins instalados, `package.json` deve apontar o carregamento em runtime para JavaScript compilado quando disponível:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["./src/index.ts"],    "runtimeExtensions": ["./dist/index.js"],    "setupEntry": "./src/setup-entry.ts",    "runtimeSetupEntry": "./dist/setup-entry.js"  }}
[/code]

`extensions` e `setupEntry` continuam sendo entradas de código-fonte válidas para desenvolvimento em workspace e checkout git. `runtimeExtensions` e `runtimeSetupEntry` são preferidos quando o OpenClaw carrega um pacote instalado e permitem que pacotes npm evitem compilação TypeScript em runtime. Entradas explícitas de runtime são obrigatórias: `runtimeSetupEntry` exige `setupEntry`, e artefatos ausentes de `runtimeExtensions` ou `runtimeSetupEntry` fazem a instalação/descoberta falhar em vez de voltar silenciosamente para o código-fonte. Se um pacote instalado declara apenas uma entrada de código-fonte TypeScript, o OpenClaw usará um par compilado correspondente em `dist/*.js` quando existir e, depois, voltará para o código-fonte TypeScript.

Todos os caminhos de entrada devem permanecer dentro do diretório do pacote do plugin. Entradas de runtime e pares inferidos de JavaScript compilado não tornam válido um caminho de código-fonte `extensions` ou `setupEntry` que escape desse diretório.

## `definePluginEntry`

**Importação:** `openclaw/plugin-sdk/plugin-entry`

Para plugins de provedor, plugins de ferramenta, plugins de hook e qualquer coisa que **não** seja um canal de mensagens.

typescriptCopy code
[code]
     export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Short summary",  register(api) {    api.registerProvider({      /* ... */    });    api.registerTool({      /* ... */    });  },});
[/code]

Campo | Tipo | Obrigatório | Padrão  
---|---|---|---  
`id` | `string` | Sim | -  
`name` | `string` | Sim | -  
`description` | `string` | Sim | -  
`kind` | `string` | Não | -  
`configSchema` | `OpenClawPluginConfigSchema | () => OpenClawPluginConfigSchema` | Não | Schema de objeto vazio  
`register` | `(api: OpenClawPluginApi) => void` | Sim | -  
  
  * `id` deve corresponder ao seu manifesto `openclaw.plugin.json`.
  * `kind` é para slots exclusivos: `"memory"` ou `"context-engine"`.
  * `configSchema` pode ser uma função para avaliação preguiçosa.
  * O OpenClaw resolve e memoriza esse schema no primeiro acesso, então builders de schema caros só são executados uma vez.


## `defineChannelPluginEntry`

**Importação:** `openclaw/plugin-sdk/channel-core`

Envolve `definePluginEntry` com fiação específica de canal. Chama automaticamente `api.registerChannel({ plugin })`, expõe uma seam opcional de metadados da CLI de ajuda raiz e bloqueia `registerFull` com base no modo de registro.

typescriptCopy code
[code]
     export default defineChannelPluginEntry({  id: "my-channel",  name: "My Channel",  description: "Short summary",  plugin: myChannelPlugin,  setRuntime: setMyRuntime,  registerCliMetadata(api) {    api.registerCli(/* ... */);  },  registerFull(api) {    api.registerGatewayMethod(/* ... */);  },});
[/code]

Campo | Tipo | Obrigatório | Padrão  
---|---|---|---  
`id` | `string` | Sim | -  
`name` | `string` | Sim | -  
`description` | `string` | Sim | -  
`plugin` | `ChannelPlugin` | Sim | -  
`configSchema` | `OpenClawPluginConfigSchema | () => OpenClawPluginConfigSchema` | Não | Schema de objeto vazio  
`setRuntime` | `(runtime: PluginRuntime) => void` | Não | -  
`registerCliMetadata` | `(api: OpenClawPluginApi) => void` | Não | -  
`registerFull` | `(api: OpenClawPluginApi) => void` | Não | -  
  
  * `setRuntime` é chamado durante o registro para que você possa armazenar a referência de runtime (normalmente via `createPluginRuntimeStore`). Ele é ignorado durante a captura de metadados da CLI.
  * `registerCliMetadata` é executado durante `api.registrationMode === "cli-metadata"`, `api.registrationMode === "discovery"` e `api.registrationMode === "full"`. Use-o como o local canônico para descritores de CLI pertencentes ao canal, para que a ajuda raiz continue sem ativação, snapshots de descoberta incluam metadados estáticos de comando, e o registro normal de comandos da CLI continue compatível com carregamentos completos de plugins.
  * O registro de descoberta não ativa, mas não é livre de importações. O OpenClaw pode avaliar a entrada confiável do plugin e o módulo do plugin de canal para construir o snapshot, então mantenha importações de topo sem efeitos colaterais e coloque sockets, clientes, workers e serviços atrás de caminhos exclusivos de `"full"`.
  * `registerFull` só é executado quando `api.registrationMode === "full"`. Ele é ignorado durante carregamentos somente de setup.
  * Assim como `definePluginEntry`, `configSchema` pode ser uma factory preguiçosa e o OpenClaw memoriza o schema resolvido no primeiro acesso.
  * Para comandos de CLI raiz pertencentes ao plugin, prefira `api.registerCli(..., { descriptors: [...] })` quando quiser que o comando permaneça carregado de forma preguiçosa sem desaparecer da árvore de parsing da CLI raiz. Para comandos de recurso de nó pareado, prefira `api.registerNodeCliFeature(...)` para que o comando fique sob `openclaw nodes`. Para outros comandos aninhados de plugin, adicione `parentPath` e registre comandos no objeto `program` passado ao registrador; o OpenClaw o resolve para o comando pai antes de chamar o plugin. Para plugins de canal, prefira registrar esses descritores a partir de `registerCliMetadata(...)` e manter `registerFull(...)` focado apenas no trabalho de runtime.
  * Se `registerFull(...)` também registra métodos RPC de gateway, mantenha-os em um prefixo específico do plugin. Namespaces reservados de administração do core (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) são sempre coagidos para `operator.admin`.


## `defineSetupPluginEntry`

**Importação:** `openclaw/plugin-sdk/channel-core`

Para o arquivo leve `setup-entry.ts`. Retorna apenas `{ plugin }`, sem fiação de runtime ou CLI.

typescriptCopy code
[code]
     export default defineSetupPluginEntry(myChannelPlugin);
[/code]

O OpenClaw carrega isto em vez da entrada completa quando um canal está desabilitado, não configurado ou quando o carregamento adiado está habilitado. Consulte [Setup e Configuração](</pt-BR/plugins/sdk-setup#setup-entry>) para saber quando isso importa.

Na prática, combine `defineSetupPluginEntry(...)` com as famílias estreitas de helpers de setup:

  * `openclaw/plugin-sdk/setup-runtime` para helpers de setup seguros para runtime, como adaptadores de patch de setup seguros para importação, saída de nota de lookup, `promptResolvedAllowFrom`, `splitSetupEntries` e proxies de setup delegados
  * `openclaw/plugin-sdk/channel-setup` para superfícies de setup de instalação opcional
  * `openclaw/plugin-sdk/setup-tools` para helpers de setup/instalação de CLI/arquivo/docs


Mantenha SDKs pesados, registro de CLI e serviços de runtime de longa duração na entrada completa.

Canais de workspace incluídos que separam superfícies de setup e runtime podem usar `defineBundledChannelSetupEntry(...)` de `openclaw/plugin-sdk/channel-entry-contract`. Esse contrato permite que a entrada de setup mantenha exportações de plugin/secrets seguras para setup enquanto ainda expõe um setter de runtime:

typescriptCopy code
[code]
     export default defineBundledChannelSetupEntry({  importMetaUrl: import.meta.url,  plugin: {    specifier: "./channel-plugin-api.js",    exportName: "myChannelPlugin",  },  runtime: {    specifier: "./runtime-api.js",    exportName: "setMyChannelRuntime",  },});
[/code]

Use esse contrato incluído apenas quando fluxos de setup realmente precisarem de um setter de runtime leve antes que a entrada completa do canal carregue.

## Modo de registro

`api.registrationMode` informa ao seu plugin como ele foi carregado:

Modo | Quando | O que registrar  
---|---|---  
`"full"` | Inicialização normal do gateway | Tudo  
`"discovery"` | Descoberta de capacidade somente leitura | Registro de canal mais descritores estáticos de CLI; o código de entrada pode carregar, mas ignore sockets, workers, clientes e serviços  
`"setup-only"` | Canal desabilitado/não configurado | Apenas registro de canal  
`"setup-runtime"` | Fluxo de setup com runtime disponível | Registro de canal mais apenas o runtime leve necessário antes que a entrada completa carregue  
`"cli-metadata"` | Ajuda raiz / captura de metadados da CLI | Apenas descritores de CLI  
  
`defineChannelPluginEntry` lida com essa divisão automaticamente. Se você usar `definePluginEntry` diretamente para um canal, verifique o modo por conta própria:

typescriptCopy code
[code]
    register(api) {  if (    api.registrationMode === "cli-metadata" ||    api.registrationMode === "discovery" ||    api.registrationMode === "full"  ) {    api.registerCli(/* ... */);    if (api.registrationMode === "cli-metadata") return;  }   api.registerChannel({ plugin: myPlugin });  if (api.registrationMode !== "full") return;   // Heavy runtime-only registrations  api.registerService(/* ... */);}
[/code]

O modo de descoberta constrói um snapshot de registro que não ativa. Ele ainda pode avaliar a entrada do plugin e o objeto do plugin de canal para que o OpenClaw possa registrar capacidades de canal e descritores estáticos de CLI. Trate a avaliação de módulo em descoberta como confiável, mas leve: sem clientes de rede, subprocessos, listeners, conexões de banco de dados, workers em segundo plano, leituras de credenciais ou outros efeitos colaterais vivos de runtime no nível superior.

Trate `"setup-runtime"` como a janela em que superfícies de inicialização somente de setup devem existir sem reentrar no runtime completo do canal incluído. Bons encaixes são registro de canal, rotas HTTP seguras para setup, métodos de gateway seguros para setup e helpers de setup delegados. Serviços pesados em segundo plano, registradores de CLI e inicializações de SDK de provedor/cliente ainda pertencem a `"full"`.

Para registradores de CLI especificamente:

  * use `descriptors` quando o registrador possui um ou mais comandos raiz e você quer que o OpenClaw carregue sob demanda o módulo real da CLI na primeira invocação
  * garanta que esses descritores cubram toda raiz de comando de nível superior exposta pelo registrador
  * mantenha os nomes de comando dos descritores com letras, números, hífen e sublinhado, começando com uma letra ou número; o OpenClaw rejeita nomes de descritores fora desse formato e remove sequências de controle de terminal das descrições antes de renderizar a ajuda
  * use apenas `commands` somente para caminhos de compatibilidade ansiosa


## Formatos de Plugin

O OpenClaw classifica plugins carregados pelo comportamento de registro deles:

Formato | Descrição  
---|---  
**plain-capability** | Um tipo de capacidade (por exemplo, somente provedor)  
**hybrid-capability** | Vários tipos de capacidade (por exemplo, provedor + fala)  
**hook-only** | Somente hooks, sem capacidades  
**non-capability** | Ferramentas/comandos/serviços, mas sem capacidades  
  
Use `openclaw plugins inspect <id>` para ver o formato de um plugin.

## Relacionados

  * [Visão geral do SDK](</pt-BR/plugins/sdk-overview>) \- API de registro e referência de subcaminhos
  * [Auxiliares de runtime](</pt-BR/plugins/sdk-runtime>) \- `api.runtime` e `createPluginRuntimeStore`
  * [Configuração e setup](</pt-BR/plugins/sdk-setup>) \- manifesto, entrada de setup, carregamento adiado
  * [Plugins de canal](</pt-BR/plugins/sdk-channel-plugins>) \- criação do objeto `ChannelPlugin`
  * [Plugins de provedor](</pt-BR/plugins/sdk-provider-plugins>) \- registro de provedor e hooks


Was this useful?YesNo