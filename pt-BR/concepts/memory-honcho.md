---
title: Memória Honcho
source_url: https://docs.openclaw.ai/pt-BR/concepts/memory-honcho
scraped_at: 2026-05-25
---

[Honcho](<https://honcho.dev>) adiciona memória nativa de IA ao OpenClaw. Ele persiste conversas em um serviço dedicado e constrói modelos de usuário e de agente ao longo do tempo, dando ao seu agente contexto entre sessões que vai além de arquivos Markdown do workspace.

## O que ele oferece

  * **Memória entre sessões** \-- as conversas são persistidas após cada turno, então o contexto é mantido entre redefinições de sessão, Compaction e trocas de canal.
  * **Modelagem de usuário** \-- o Honcho mantém um perfil para cada usuário (preferências, fatos, estilo de comunicação) e para o agente (personalidade, comportamentos aprendidos).
  * **Busca semântica** \-- busca em observações de conversas passadas, não apenas na sessão atual.
  * **Consciência de vários agentes** \-- agentes pais acompanham automaticamente subagentes gerados, com os pais adicionados como observadores em sessões filhas.


## Ferramentas disponíveis

O Honcho registra ferramentas que o agente pode usar durante a conversa:

**Recuperação de dados (rápida, sem chamada ao LLM):**

Ferramenta | O que faz  
---|---  
`honcho_context` | Representação completa do usuário entre sessões  
`honcho_search_conclusions` | Busca semântica em conclusões armazenadas  
`honcho_search_messages` | Localiza mensagens entre sessões (filtra por remetente, data)  
`honcho_session` | Histórico e resumo da sessão atual  
  
**Perguntas e respostas (powered by LLM):**

Ferramenta | O que faz  
---|---  
`honcho_ask` | Faz perguntas sobre o usuário. `depth='quick'` para fatos, `'thorough'` para síntese  
  
## Primeiros passos

Instale o plugin e execute a configuração:

bashCopy code
[code]
    openclaw plugins install @honcho-ai/openclaw-honchoopenclaw honcho setupopenclaw gateway --force
[/code]

O comando de configuração solicita suas credenciais de API, grava a configuração e opcionalmente migra arquivos de memória existentes do workspace.

## Configuração

As configurações ficam em `plugins.entries["openclaw-honcho"].config`:

json5Copy code
[code]
    {  plugins: {    entries: {      "openclaw-honcho": {        config: {          apiKey: "your-api-key", // omita para auto-hospedado          workspaceId: "openclaw", // isolamento de memória          baseUrl: "https://api.honcho.dev",        },      },    },  },}
[/code]

Para instâncias auto-hospedadas, aponte `baseUrl` para seu servidor local (por exemplo `http://localhost:8000`) e omita a chave de API.

## Migrando memória existente

Se você já tiver arquivos de memória existentes no workspace (`USER.md`, `MEMORY.md`, `IDENTITY.md`, `memory/`, `canvas/`), `openclaw honcho setup` detecta e oferece a migração deles.

## Como funciona

Após cada turno da IA, a conversa é persistida no Honcho. Tanto mensagens do usuário quanto do agente são observadas, permitindo que o Honcho construa e refine seus modelos ao longo do tempo.

Durante a conversa, as ferramentas do Honcho consultam o serviço na fase `before_prompt_build`, injetando contexto relevante antes que o modelo veja o prompt. Isso garante limites de turno precisos e recordação relevante.

## Honcho vs memória integrada

| Integrada / QMD | Honcho  
---|---|---  
**Armazenamento** | Arquivos Markdown do workspace | Serviço dedicado (local ou hospedado)  
**Entre sessões** | Via arquivos de memória | Automático, integrado  
**Modelagem de usuário** | Manual (gravar em [MEMORY.md](<http://MEMORY.md>)) | Perfis automáticos  
**Busca** | Vetorial + palavra-chave (híbrida) | Semântica sobre observações  
**Vários agentes** | Não rastreado | Consciência de pai/filho  
**Dependências** | Nenhuma (integrada) ou binário QMD | Instalação de plugin  
  
O Honcho e o sistema de memória integrado podem funcionar juntos. Quando o QMD está configurado, ferramentas adicionais ficam disponíveis para buscar em arquivos Markdown locais junto com a memória entre sessões do Honcho.

## Comandos da CLI

bashCopy code
[code]
    openclaw honcho setup                        # Configura a chave de API e migra arquivosopenclaw honcho status                       # Verifica o status da conexãoopenclaw honcho ask <question>               # Consulta o Honcho sobre o usuárioopenclaw honcho search <query> [-k N] [-d D] # Busca semântica na memória
[/code]

## Leitura adicional

  * [Código-fonte do plugin](<https://github.com/plastic-labs/openclaw-honcho>)
  * [Documentação do Honcho](<https://docs.honcho.dev>)
  * [Guia de integração do Honcho com OpenClaw](<https://docs.honcho.dev/v3/guides/integrations/openclaw>)
  * [Memória](</pt-BR/concepts/memory>) \-- visão geral da memória do OpenClaw
  * [Motores de contexto](</pt-BR/concepts/context-engine>) \-- como funcionam os motores de contexto de plugin


## Relacionado

  * [Visão geral da memória](</pt-BR/concepts/memory>)
  * [Motor de memória integrado](</pt-BR/concepts/memory-builtin>)
  * [Motor de memória QMD](</pt-BR/concepts/memory-qmd>)


Was this useful?YesNo