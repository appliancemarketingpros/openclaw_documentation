---
title: Inicialização do agente
source_url: https://docs.openclaw.ai/pt-BR/start/bootstrapping
scraped_at: 2026-05-25
---

A inicialização é o ritual de **primeira execução** que prepara um espaço de trabalho do agente e coleta detalhes de identidade. Ela acontece após a integração, quando o agente é iniciado pela primeira vez.

## O que a inicialização faz

Na primeira execução do agente, o OpenClaw inicializa o espaço de trabalho (padrão `~/.openclaw/workspace`):

  * Cria `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.
  * Executa um breve ritual de perguntas e respostas (uma pergunta por vez).
  * Grava identidade + preferências em `IDENTITY.md`, `USER.md`, `SOUL.md`.
  * Remove `BOOTSTRAP.md` ao terminar, para que ele seja executado apenas uma vez.


Para execuções com modelos incorporados/locais, o OpenClaw mantém `BOOTSTRAP.md` fora do contexto de sistema privilegiado. Na primeira execução interativa principal, ele ainda passa o conteúdo do arquivo no prompt do usuário para que modelos que não chamam a ferramenta `read` de forma confiável possam concluir o ritual. Se a execução atual não puder acessar o espaço de trabalho com segurança, o agente recebe uma nota de inicialização limitada em vez de uma saudação genérica.

## Como pular a inicialização

Para pular isso em um espaço de trabalho pré-preenchido, execute `openclaw onboard --skip-bootstrap`.

## Onde ela é executada

A inicialização sempre é executada no **host do Gateway**. Se o app para macOS se conectar a um Gateway remoto, o espaço de trabalho e os arquivos de inicialização ficarão nessa máquina remota.

## Documentação relacionada

  * Integração do app para macOS: [Integração](</pt-BR/start/onboarding>)
  * Layout do espaço de trabalho: [Espaço de trabalho do agente](</pt-BR/concepts/agent-workspace>)


Was this useful?YesNo