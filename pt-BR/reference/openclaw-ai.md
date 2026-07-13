---
title: pacote @openclaw/ai
source_url: https://docs.openclaw.ai/pt-BR/reference/openclaw-ai
scraped_at: 2026-07-13
---

ReferenceTechnical reference

`@openclaw/ai` é a forma publicável como biblioteca da camada de execução de modelos do OpenClaw: contratos de mensagens/ferramentas/streams independentes de provedor, validação, diagnósticos, streams de eventos, um registro de runtime isolado e adaptadores carregados sob demanda para as oito famílias de APIs integradas (Anthropic Messages, OpenAI Completions, OpenAI Responses, Azure OpenAI Responses, ChatGPT/Codex Responses, Google Generative AI, Google Vertex, Mistral Conversations).

Ela é publicada junto com o pacote raiz `openclaw` em cada versão, fixada na mesma versão, com seu próprio `npm-shrinkwrap.json`, para que sua árvore de dependências transitivas fique bloqueada no momento da instalação. A instalação de `openclaw` instala automaticamente a versão correspondente de `@openclaw/ai`; consumidores da biblioteca podem depender dela diretamente, sem nenhum código da aplicação OpenClaw.

## Início rápido

jsCopy code
[code]
      const runtime = createLlmRuntime();registerBuiltInApiProviders(runtime.registry); const stream = runtime.streamSimple(model, { messages }, { apiKey });for await (const event of stream) {  if (event.type === "text_delta") process.stdout.write(event.delta);}const result = await stream.result();
[/code]

Uma versão executável está disponível no repositório em `examples/ai-chat`.

## Contrato de design

  * **Com escopo de instância por padrão.** Importar o pacote não registra nada globalmente. `createApiRegistry()` / `createLlmRuntime()` retornam instâncias isoladas; `registerBuiltInApiProviders(registry)` habilita os transportes integrados em um registro. Os módulos de SDK dos provedores são carregados sob demanda no primeiro uso.
  * **A política do host é injetada, não incluída.** A proteção das solicitações de busca (por exemplo, a política contra SSRF), a ocultação de segredos no texto de reprodução dos resultados de ferramentas, os padrões de ferramentas estritas do OpenAI e o registro de diagnósticos são portas `AiTransportHost` configuradas com `configureAiTransportHost`. Os padrões da biblioteca são inertes; o OpenClaw instala suas implementações reais em sua fachada de stream.
  * **Uma única identidade de stream de eventos.** `@openclaw/ai/event-stream` é o construtor canônico de `EventStream`, compartilhado pelo núcleo do OpenClaw, pelo agent-core e por consumidores externos.
  * **Os subcaminhos`internal/*` não são uma API.** Eles existem para a própria aplicação OpenClaw e não oferecem nenhuma garantia de semver.
  * IDs de provedores, credenciais, catálogos de modelos, novas tentativas e failover continuam sendo responsabilidades da aplicação. O OpenClaw adiciona essas camadas ao redor deste pacote; o consumidor da biblioteca fornece diretamente um objeto `Model` e as opções.


## Exportações de subcaminhos

Subcaminho | Conteúdo  
---|---  
`.` | Contratos, `createApiRegistry`, `createLlmRuntime`, `configureAiTransportHost`  
`./providers` | `registerBuiltInApiProviders`, `resetApiProviders`  
`./types` | Tipos de modelo/mensagem/ferramenta/stream  
`./validation` | Validação de argumentos de ferramentas  
`./diagnostics` | Contratos de diagnóstico  
`./event-stream` | Implementação compartilhada de `EventStream`  
`./internal/*` | Interno ao OpenClaw, sem garantia de semver  
  
Was this useful?YesNo

Open issue