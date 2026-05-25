---
title: Fluxo de trabalho de desenvolvimento do Pi
source_url: https://docs.openclaw.ai/pt-BR/pi-dev
scraped_at: 2026-05-25
---

Um fluxo de trabalho sensato para trabalhar na integração com Pi no OpenClaw.

## Verificação de tipos e lint

  * Verificação local padrão: `pnpm check`
  * Verificação de compilação: `pnpm build` quando a alteração puder afetar a saída de compilação, o empacotamento ou os limites de carregamento tardio/módulo
  * Verificação completa antes da integração para alterações com foco pesado em Pi: `pnpm check && pnpm test`


## Executando testes de Pi

Execute o conjunto de testes focado em Pi diretamente com Vitest:

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

Para incluir o exercício do provedor ao vivo:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

Isso cobre os principais conjuntos de testes unitários de Pi:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## Testes manuais

Fluxo recomendado:

  * Execute o gateway em modo de desenvolvimento: 
    * `pnpm gateway:dev`
  * Acione o agente diretamente: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Use a TUI para depuração interativa: 
    * `pnpm tui`


Para comportamento de chamadas de ferramenta, solicite uma ação `read` ou `exec` para que você possa ver o streaming de ferramentas e o tratamento de payloads.

## Redefinição completa do estado inicial

O estado fica no diretório de estado do OpenClaw. O padrão é `~/.openclaw`. Se `OPENCLAW_STATE_DIR` estiver definido, use esse diretório.

Para redefinir tudo:

  * `openclaw.json` para configuração
  * `agents/<agentId>/agent/auth-profiles.json` para perfis de autenticação de modelo (chaves de API + OAuth)
  * `credentials/` para estado de provedor/canal que ainda fica fora do armazenamento de perfis de autenticação
  * `agents/<agentId>/sessions/` para histórico de sessões do agente
  * `agents/<agentId>/sessions/sessions.json` para o índice de sessões
  * `sessions/` se existirem caminhos legados
  * `workspace/` se você quiser um workspace em branco


Se você quiser apenas redefinir sessões, exclua `agents/<agentId>/sessions/` desse agente. Se quiser manter a autenticação, deixe `agents/<agentId>/agent/auth-profiles.json` e qualquer estado de provedor em `credentials/` no lugar.

## Referências

  * [Testes](</pt-BR/help/testing>)
  * [Introdução](</pt-BR/start/getting-started>)


## Relacionado

  * [Arquitetura da integração com Pi](</pt-BR/pi>)


Was this useful?YesNo