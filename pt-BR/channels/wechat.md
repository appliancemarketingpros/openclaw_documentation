---
title: WeChat
source_url: https://docs.openclaw.ai/pt-BR/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw se conecta ao WeChat por meio do plugin de canal externo `@tencent-weixin/openclaw-weixin` da Tencent.

Status: plugin externo. Chats diretos e mídia são compatíveis. Chats em grupo não são anunciados pelos metadados de capacidade atuais do plugin.

## Nomenclatura

  * **WeChat** é o nome voltado ao usuário nestes docs.
  * **Weixin** é o nome usado pelo pacote da Tencent e pelo id do plugin.
  * `openclaw-weixin` é o id do canal do OpenClaw.
  * `@tencent-weixin/openclaw-weixin` é o pacote npm.


Use `openclaw-weixin` em comandos de CLI e caminhos de configuração.

## Como funciona

O código do WeChat não fica no repo principal do OpenClaw. O OpenClaw fornece o contrato genérico de plugin de canal, e o plugin externo fornece o runtime específico do WeChat:

  1. `openclaw plugins install` instala `@tencent-weixin/openclaw-weixin`.
  2. O Gateway descobre o manifesto do plugin e carrega o ponto de entrada do plugin.
  3. O plugin registra o id de canal `openclaw-weixin`.
  4. `openclaw channels login --channel openclaw-weixin` inicia o login por QR.
  5. O plugin armazena as credenciais da conta no diretório de estado do OpenClaw.
  6. Quando o Gateway inicia, o plugin inicia seu monitor do Weixin para cada conta configurada.
  7. Mensagens recebidas do WeChat são normalizadas pelo contrato de canal, roteadas para o agente OpenClaw selecionado e enviadas de volta pelo caminho de saída do plugin.


Essa separação é importante: o núcleo do OpenClaw deve permanecer agnóstico a canais. Login do WeChat, chamadas da API Tencent iLink, upload/download de mídia, tokens de contexto e monitoramento de contas pertencem ao plugin externo.

## Instalação

Instalação rápida:

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

Instalação manual:

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

Reinicie o Gateway após a instalação:

bashCopy code
[code]
    openclaw gateway restart
[/code]

## Login

Execute o login por QR na mesma máquina que executa o Gateway:

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

Escaneie o código QR com o WeChat no seu telefone e confirme o login. O plugin salva o token da conta localmente após uma leitura bem-sucedida.

Para adicionar outra conta do WeChat, execute o mesmo comando de login novamente. Para múltiplas contas, isole sessões de mensagem direta por conta, canal e remetente:

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## Controle de acesso

Mensagens diretas usam o modelo normal de pareamento e allowlist do OpenClaw para plugins de canal.

Aprove novos remetentes:

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

Para o modelo completo de controle de acesso, consulte [Pareamento](</pt-BR/channels/pairing>).

## Compatibilidade

O plugin verifica a versão do host OpenClaw na inicialização.

Linha do plugin | Versão do OpenClaw | tag npm  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
Se o plugin informar que sua versão do OpenClaw é antiga demais, atualize o OpenClaw ou instale a linha legada do plugin:

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## Processo sidecar

O plugin do WeChat pode executar trabalho auxiliar ao lado do Gateway enquanto monitora a API Tencent iLink. Na issue #68451, esse caminho auxiliar expôs um bug na limpeza genérica de Gateways obsoletos do OpenClaw: um processo filho podia tentar limpar o processo Gateway pai, causando loops de reinício sob gerenciadores de processo como systemd.

A limpeza atual de inicialização do OpenClaw exclui o processo atual e seus ancestrais, portanto um auxiliar de canal não deve encerrar o Gateway que o iniciou. Essa correção é genérica; não é um caminho específico do WeChat no núcleo.

## Solução de problemas

Verifique instalação e status:

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

Se o canal aparecer como instalado, mas não se conectar, confirme que o plugin está habilitado e reinicie:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

Se o Gateway reiniciar repetidamente após habilitar o WeChat, atualize tanto o OpenClaw quanto o plugin:

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

Se a inicialização informar que o pacote de plugin instalado `requires compiled runtime output for TypeScript entry`, o pacote npm foi publicado sem os arquivos compilados de runtime JavaScript necessários para o OpenClaw. Atualize/reinstale depois que o publicador do plugin lançar um pacote corrigido, ou desabilite/desinstale o plugin temporariamente.

Desabilitação temporária:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## Docs relacionados

  * Visão geral de canais: [Canais de chat](</pt-BR/channels>)
  * Pareamento: [Pareamento](</pt-BR/channels/pairing>)
  * Roteamento de canal: [Roteamento de canal](</pt-BR/channels/channel-routing>)
  * Arquitetura de plugin: [Arquitetura de Plugin](</pt-BR/plugins/architecture>)
  * SDK de plugin de canal: [SDK de Plugin de canal](</pt-BR/plugins/sdk-channel-plugins>)
  * Pacote externo: [@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo