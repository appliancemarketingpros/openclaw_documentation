---
title: Raft
source_url: https://docs.openclaw.ai/pt-BR/channels/raft
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

O suporte ao Raft conecta um agente OpenClaw a um Agente Externo do Raft por meio da CLI local do Raft. O Raft envia dicas de ativação autenticadas para o Gateway. Em seguida, o agente usa a CLI do Raft para verificar e enviar mensagens.

## Instalação

O Raft é um Plugin externo oficial. Instale-o no host do Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

Detalhes: [Plugins](</pt-BR/tools/plugin>)

## Pré-requisitos

  * Um workspace do Raft com um Agente Externo.
  * A CLI do Raft instalada no mesmo host que o Gateway do OpenClaw.
  * Um perfil da CLI do Raft que já esteja conectado e associado a esse Agente Externo.


O Plugin não armazena credenciais do Raft. A CLI do Raft mantém essa autenticação em seu próprio perfil.

## Configurar

Defina o perfil na configuração:

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

Para a conta padrão, você também pode definir `RAFT_PROFILE` no ambiente do Gateway:

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

Use uma conta nomeada quando um Gateway se conectar a mais de um Agente Externo do Raft:

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

O fluxo de configuração interativo registra o mesmo perfil:

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## Como Funciona

Quando o Gateway inicia, o Plugin:

  1. Abre um endpoint HTTP de ativação apenas por loopback em uma porta efêmera.
  2. Inicia `raft --profile <profile> agent bridge` com esse endpoint e um token por processo.
  3. Aceita apenas dicas de ativação autenticadas e sem conteúdo, com uma identidade de repetição da ponte local.
  4. Exige um entre `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id` ou `id`.
  5. Desduplica entregas de ativação repetidas recentemente pelo id de evento da ponte, inclusive entre reinicializações do Gateway.
  6. Retorna uma sessão de runtime estável para a ponte atual e um lote vazio de drenagem de atividades para o protocolo da CLI do Raft.
  7. Inicia um turno serializado do agente OpenClaw para cada ativação aceita.


A ponte é responsável pelas novas tentativas de entrega e reconexões do Raft. O turno do OpenClaw recebe apenas um aviso de ativação, não uma cópia do corpo da mensagem do Raft. Ele usa a CLI para ler mensagens pendentes e enviar sua resposta:

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## Verificar

Verifique se o OpenClaw consegue encontrar a CLI e tem um perfil configurado:

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

Em seguida, envie uma mensagem ao Agente Externo do Raft. O log do Gateway deve mostrar a ponte do Raft sendo iniciada, seguida por uma ativação de entrada. O agente deve usar o perfil do Raft configurado para verificar suas mensagens pendentes.

## Solução de Problemas

A CLI do Raft está ausente

Instale a CLI do Raft no host do Gateway e torne `raft` disponível no `PATH` do serviço. Verifique com `raft --help` e reinicie o Gateway.

A ponte encerra imediatamente

Verifique se o perfil configurado está conectado e pertence ao Agente Externo do Raft pretendido. Execute `raft --profile <profile> agent bridge` diretamente para ver o diagnóstico da CLI.

Uma ativação chega, mas nenhuma resposta do Raft é enviada

Isso é esperado quando o agente não invoca a CLI do Raft. A ponte de ativação não transporta corpos de mensagens nem respostas finais automáticas. Verifique a política de ferramentas do agente e garanta que ele possa executar `raft --profile <profile> message check` e `message send`.

## Referências

  * [Raft](<https://raft.build/>)
  * [Documentação do Raft](<https://docs.raft.build/welcome/>)
  * [Integração do Hermes com o Raft](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue