---
title: Modos de permissão
source_url: https://docs.openclaw.ai/pt-BR/tools/permission-modes
scraped_at: 2026-06-29
---

CapabilitiesTools

Os modos de permissão decidem quanta autoridade um agente tem antes de poder executar comandos no host, gravar arquivos ou pedir acesso extra a um harness de backend. Comece com `tools.exec.mode: "auto"` quando quiser que o OpenClaw use listas de permissões primeiro, depois revisão automática nativa do Codex ou uma rota de aprovação humana para falhas.

## Padrão recomendado

Use `auto` para agentes de codificação que precisam de acesso útil ao host sem transformar cada falha em uma solicitação humana:

bashCopy code
[code]
    openclaw config set tools.exec.mode autoopenclaw approvals getopenclaw gateway restart
[/code]

Depois verifique a política efetiva:

bashCopy code
[code]
    openclaw exec-policy show
[/code]

No modo `auto`, o OpenClaw executa correspondências determinísticas da lista de permissões diretamente. Falhas de aprovação passam primeiro pelo revisor automático nativo do OpenClaw e depois recorrem à rota de aprovação humana configurada quando necessário.

## Modos de exec do host do OpenClaw

`tools.exec.mode` é a superfície de política normalizada para `exec` no host.

Modo | Comportamento | Use quando  
---|---|---  
`deny` | Bloquear exec no host. | Nenhum comando de host é permitido.  
`allowlist` | Executar apenas comandos na lista de permissões. | Você tem um conjunto de comandos sabidamente seguro.  
`ask` | Executar correspondências da lista e perguntar nas falhas. | Um humano deve revisar novos comandos.  
`auto` | Executar correspondências da lista e depois usar revisão automática. | Sessões de codificação precisam de acesso protegido prático.  
`full` | Executar exec no host sem solicitações. | Este host/sessão confiável deve ignorar barreiras de aprovação.  
  
Para a política completa de exec no host, arquivo local de aprovações, esquema da lista de permissões, binários seguros e comportamento de encaminhamento, consulte [Aprovações de exec](</pt-BR/tools/exec-approvals>).

## Mapeamento do Codex Guardian

Para sessões nativas do servidor de aplicativo do Codex, `tools.exec.mode: "auto"` mapeia para aprovações revisadas pelo Codex Guardian quando os requisitos locais do Codex permitem. O OpenClaw normalmente envia:

Campo do Codex | Valor típico  
---|---  
`approvalPolicy` | `on-request`  
`approvalsReviewer` | `auto_review`  
`sandbox` | `workspace-write`  
  
No modo `auto`, o OpenClaw não preserva substituições inseguras legadas do Codex, como `approvalPolicy: "never"` ou `sandbox: "danger-full-access"`. Use `tools.exec.mode: "full"` apenas quando quiser intencionalmente a postura sem aprovação.

Para configuração do servidor de aplicativo, ordem de autenticação e detalhes do runtime nativo do Codex, consulte [harness do Codex](</pt-BR/plugins/codex-harness>).

## Permissões do harness ACPX

Sessões ACPX são não interativas, então não podem clicar em uma solicitação de permissão de TTY. O ACPX usa configurações separadas no nível do harness em `plugins.entries.acpx.config`:

Configuração | Valor comum | Significado  
---|---|---  
`permissionMode` | `approve-reads` | Aprovar automaticamente apenas leituras.  
`permissionMode` | `approve-all` | Aprovar automaticamente gravações e comandos de shell.  
`permissionMode` | `deny-all` | Negar todas as solicitações de permissão.  
`nonInteractivePermissions` | `fail` | Abortar quando uma solicitação seria necessária.  
`nonInteractivePermissions` | `deny` | Negar a solicitação e continuar quando possível.  
  
Configure permissões ACPX separadamente das aprovações de exec do OpenClaw:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions failopenclaw gateway restart
[/code]

Use `approve-all` como o equivalente de emergência do ACPX para uma sessão de harness sem solicitações. Para detalhes de configuração e modos de falha, consulte [configuração de agentes ACP](</pt-BR/tools/acp-agents-setup#permission-configuration>).

## Escolhendo um modo

Objetivo | Configurar  
---|---  
Bloquear comandos do host completamente | `tools.exec.mode: "deny"`  
Permitir apenas comandos sabidamente seguros | `tools.exec.mode: "allowlist"`  
Perguntar a um humano para cada novo formato de comando | `tools.exec.mode: "ask"`  
Usar revisão automática do Codex/OpenClaw antes de humanos | `tools.exec.mode: "auto"`  
Ignorar aprovações de exec no host totalmente | `tools.exec.mode: "full"` mais o arquivo de aprovações do host correspondente  
Fazer sessões ACPX não interativas gravarem/executarem | `plugins.entries.acpx.config.permissionMode: "approve-all"`  
  
Se um comando ainda solicitar aprovação ou falhar depois de alterar o modo, inspecione as duas camadas:

bashCopy code
[code]
    openclaw approvals getopenclaw exec-policy show
[/code]

O exec do host usa o resultado mais restritivo entre a configuração do OpenClaw e o arquivo de aprovações local do host. As permissões do harness ACPX não afrouxam aprovações de exec no host, e aprovações de exec no host não afrouxam solicitações do harness ACPX.

## Relacionados

  * [Aprovações de exec](</pt-BR/tools/exec-approvals>)
  * [Aprovações de exec - avançado](</pt-BR/tools/exec-approvals-advanced>)
  * [harness do Codex](</pt-BR/plugins/codex-harness>)
  * [configuração de agentes ACP](</pt-BR/tools/acp-agents-setup#permission-configuration>)


Was this useful?YesNo

Open issue