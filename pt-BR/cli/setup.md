---
title: Configuração
source_url: https://docs.openclaw.ai/pt-BR/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Inicialize a configuração base e o espaço de trabalho do agente. Com qualquer flag de integração inicial presente, também executa o assistente.

## Opções

Flag | Descrição  
---|---  
`--workspace <dir>` | Diretório do espaço de trabalho do agente (padrão `~/.openclaw/workspace`; armazenado como `agents.defaults.workspace`).  
`--wizard` | Executa a integração inicial interativa.  
`--non-interactive` | Executa a integração inicial sem prompts.  
`--mode <mode>` | Modo de integração inicial: `local` ou `remote`.  
`--import-from <provider>` | Provedor de migração a executar durante a integração inicial.  
`--import-source <path>` | Diretório inicial do agente de origem para `--import-from`.  
`--import-secrets` | Importa segredos compatíveis durante a migração da integração inicial.  
`--remote-url <url>` | URL WebSocket do Gateway remoto.  
`--remote-token <token>` | Token do Gateway remoto (opcional).  
  
### Acionamento automático do assistente

`openclaw setup` executa o assistente quando qualquer uma destas flags está explicitamente presente, mesmo sem `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Exemplos

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Observações

  * `openclaw setup` simples inicializa a configuração e o espaço de trabalho sem executar o fluxo completo de integração inicial.
  * Após o setup simples, execute `openclaw onboard` para a jornada guiada completa, `openclaw configure` para alterações direcionadas ou `openclaw channels add` para adicionar contas de canal.
  * Se o estado do Hermes for detectado, a integração inicial interativa pode oferecer a migração automaticamente. A integração inicial com importação exige um setup novo; use [Migrar](</pt-BR/cli/migrate>) para planos de simulação, backups e modo de sobrescrita fora da integração inicial.


## Relacionados

  * [Referência da CLI](</pt-BR/cli>)
  * [Integração inicial (CLI)](</pt-BR/start/wizard>)
  * [Primeiros passos](</pt-BR/start/getting-started>)
  * [Visão geral da instalação](</pt-BR/install>)


Was this useful?YesNo