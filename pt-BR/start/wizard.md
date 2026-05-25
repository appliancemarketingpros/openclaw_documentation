---
title: Configuração inicial (CLI)
source_url: https://docs.openclaw.ai/pt-BR/start/wizard
scraped_at: 2026-05-25
---

A integração via CLI é a forma **recomendada** de configurar o OpenClaw no macOS, Linux ou Windows (via WSL2; altamente recomendado). Ela configura um Gateway local ou uma conexão com Gateway remoto, além de canais, skills e padrões de workspace em um único fluxo guiado.

bashCopy code
[code]
    openclaw onboard
[/code]

Para reconfigurar depois:

bashCopy code
[code]
    openclaw configureopenclaw agents add <name>
[/code]

## QuickStart vs Avançado

A integração começa com **QuickStart** (padrões) vs **Avançado** (controle total).

### QuickStart (padrões)

  * Gateway local (loopback)
  * Padrão de workspace (ou workspace existente)
  * Porta do Gateway **18789**
  * Autenticação do Gateway **Token** (gerado automaticamente, mesmo em loopback)
  * Política de ferramentas padrão para novas configurações locais: `tools.profile: "coding"` (perfil explícito existente é preservado)
  * Padrão de isolamento de DMs: a integração local grava `session.dmScope: "per-channel-peer"` quando não definido. Detalhes: [Referência de configuração da CLI](</pt-BR/start/wizard-cli-reference#outputs-and-internals>)
  * Exposição do Tailscale **Desativada**
  * DMs do Telegram + WhatsApp usam **lista de permissões** por padrão (você receberá uma solicitação para informar seu número de telefone)


### Avançado (controle total)

  * Expõe todas as etapas (modo, workspace, Gateway, canais, daemon, skills).


## O que a integração configura

O **modo local (padrão)** orienta você por estas etapas:

  1. **Modelo/Auth** — escolha qualquer provedor/fluxo de autenticação compatível (chave de API, OAuth ou autenticação manual específica do provedor), incluindo Custom Provider (compatível com OpenAI, compatível com Anthropic ou detecção automática Unknown). Escolha um modelo padrão. Nota de segurança: se este agente executará ferramentas ou processará conteúdo de webhook/hooks, prefira o modelo mais forte de última geração disponível e mantenha a política de ferramentas rígida. Camadas mais fracas/antigas são mais fáceis de sofrer prompt injection. Para execuções não interativas, `--secret-input-mode ref` armazena refs apoiadas por env em perfis de autenticação em vez de valores de chave de API em texto simples. No modo `ref` não interativo, a variável de ambiente do provedor deve estar definida; passar flags de chave inline sem essa variável de ambiente falha rapidamente. Em execuções interativas, escolher o modo de referência de segredo permite apontar para uma variável de ambiente ou uma ref de provedor configurada (`file` ou `exec`), com uma validação rápida de pré-verificação antes de salvar. Para Anthropic, a integração/configuração interativa oferece **Anthropic Claude CLI** como o caminho local preferido e **chave de API da Anthropic** como o caminho recomendado para produção. O setup-token da Anthropic também continua disponível como um caminho de autenticação por token compatível.
  2. **Workspace** — Local para arquivos do agente (padrão `~/.openclaw/workspace`). Inicializa arquivos de bootstrap.
  3. **Gateway** — Porta, endereço de bind, modo de autenticação, exposição do Tailscale. No modo de token interativo, escolha o armazenamento padrão de token em texto simples ou opte por SecretRef. Caminho SecretRef de token não interativo: `--gateway-token-ref-env &lt;ENV_VAR&gt;`.
  4. **Canais** — canais de chat integrados e empacotados, como iMessage, Discord, Feishu, Google Chat, Mattermost, Microsoft Teams, QQ Bot, Signal, Slack, Telegram, WhatsApp e outros.
  5. **Daemon** — Instala um LaunchAgent (macOS), unidade de usuário systemd (Linux/WSL2) ou Tarefa Agendada nativa do Windows com fallback por usuário na pasta Inicializar. Se a autenticação por token exigir um token e `gateway.auth.token` for gerenciado por SecretRef, a instalação do daemon o valida, mas não persiste o token resolvido nos metadados de ambiente do serviço supervisor. Se a autenticação por token exigir um token e o SecretRef de token configurado não for resolvido, a instalação do daemon será bloqueada com orientações acionáveis. Se `gateway.auth.token` e `gateway.auth.password` estiverem configurados e `gateway.auth.mode` não estiver definido, a instalação do daemon será bloqueada até que o modo seja definido explicitamente.
  6. **Verificação de integridade** — Inicia o Gateway e verifica se ele está em execução.
  7. **Skills** — Instala skills recomendadas e dependências opcionais.


O **modo remoto** configura apenas o cliente local para se conectar a um Gateway em outro lugar. Ele **não** instala nem altera nada no host remoto.

## Adicionar outro agente

Use `openclaw agents add <name>` para criar um agente separado com seu próprio workspace, sessões e perfis de autenticação. Executar sem `--workspace` inicia a integração.

O que ele define:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Notas:

  * Workspaces padrão seguem `~/.openclaw/workspace-<agentId>`.
  * Adicione `bindings` para rotear mensagens de entrada (a integração pode fazer isso).
  * Flags não interativas: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Referência completa

Para detalhamentos passo a passo e saídas de configuração, consulte [Referência de configuração da CLI](</pt-BR/start/wizard-cli-reference>). Para exemplos não interativos, consulte [Automação da CLI](</pt-BR/start/wizard-cli-automation>). Para a referência técnica mais aprofundada, incluindo detalhes de RPC, consulte [Referência de integração](</pt-BR/reference/wizard>).

## Documentação relacionada

  * Referência de comandos da CLI: [`openclaw onboard`](</pt-BR/cli/onboard>)
  * Visão geral da integração: [Visão geral da integração](</pt-BR/start/onboarding-overview>)
  * Integração do app macOS: [Integração](</pt-BR/start/onboarding>)
  * Ritual de primeira execução do agente: [Bootstrap do agente](</pt-BR/start/bootstrapping>)


Was this useful?YesNo