---
title: Arquitetura de runtime do agente
source_url: https://docs.openclaw.ai/pt-BR/agent-runtime-architecture
scraped_at: 2026-06-29
---

ReferenceTechnical reference

OpenClaw é proprietário direto do runtime de agente integrado. O código do runtime fica em `src/agents/`, os auxiliares de modelo/provedor ficam em `src/llm/`, e os contratos voltados para Plugin são expostos por meio dos barrels `openclaw/plugin-sdk/*`.

## Layout do Runtime

  * `src/agents/embedded-agent-runner/`: loop integrado de tentativa do agente, adaptadores de stream de provedor, Compaction, seleção de modelo e cabeamento de sessão.
  * `src/agents/sessions/`: persistência de sessão, carregamento de extensão, descoberta de recursos, Skills, prompts, temas e renderizadores de ferramenta baseados em TUI.
  * `packages/agent-core/`: núcleo reutilizável de agente, tipos de harness de nível mais baixo, mensagens, auxiliares de Compaction, modelos de prompt e contratos de ferramenta/sessão.
  * `src/agents/runtime/`: fachada OpenClaw para `@openclaw/agent-core`, além de utilitários de proxy local.
  * `src/agents/agent-tools*.ts`: definições de ferramenta, esquemas, política, adaptadores de hooks before/after e suporte a edição no host pertencentes ao OpenClaw.
  * `src/agents/agent-hooks/`: hooks de runtime integrados, como proteções de Compaction e poda de contexto.
  * `src/llm/`: registro de modelo/provedor, auxiliares de transporte e implementações de stream específicas de provedor.


## Limites

O código do core chama o runtime integrado por meio de módulos OpenClaw e barrels do SDK, não por pacotes antigos de agente externo. Plugins usam pontos de entrada documentados de `openclaw/plugin-sdk/*` e não importam componentes internos de `src/**`.

`@earendil-works/pi-tui` continua sendo uma dependência TUI de terceiros. Ela é usada como kit de componentes de terminal pela TUI local e pelos renderizadores de sessão; internalizá-la seria um esforço separado de vendorização.

## Manifestos

Pacotes de recursos declaram recursos OpenClaw nos metadados do pacote:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["extensions/index.ts"],    "skills": ["skills/*.md"],    "prompts": ["prompts/*.md"],    "themes": ["themes/*.json"]  }}
[/code]

O gerenciador de pacotes também descobre diretórios convencionais `extensions/`, `skills/`, `prompts/` e `themes/`.

## Seleção de Runtime

O id padrão do runtime integrado é `openclaw`. Harnesses de Plugin podem registrar ids de runtime adicionais. `auto` seleciona um harness de Plugin compatível quando existe um e, caso contrário, usa o runtime OpenClaw integrado.

## Relacionados

  * [Fluxo de trabalho do runtime de agente OpenClaw](</pt-BR/openclaw-agent-runtime>)
  * [Runtimes de agente](</pt-BR/concepts/agent-runtimes>)


Was this useful?YesNo

Open issue