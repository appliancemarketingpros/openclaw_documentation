---
title: Integração (app para macOS)
source_url: https://docs.openclaw.ai/pt-BR/start/onboarding
scraped_at: 2026-05-25
---

Este documento descreve o fluxo de configuração de primeira execução **atual**. O objetivo é uma experiência fluida de "dia 0": escolher onde o Gateway é executado, conectar a autenticação, executar o assistente e permitir que o agente inicialize a si mesmo. Para uma visão geral dos caminhos de onboarding, consulte [Visão geral do onboarding](</pt-BR/start/onboarding-overview>).

* ### Aprovar aviso do macOS

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Aprovar busca por redes locais

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Boas-vindas e aviso de segurança

Leia o aviso de segurança exibido e decida de acordo ![](/assets/macos-onboarding/03-security-notice.png)

Modelo de confiança de segurança:

  * Por padrão, o OpenClaw é um agente pessoal: um limite de operador confiável.
  * Configurações compartilhadas/multiusuário exigem bloqueio (separe os limites de confiança, mantenha o acesso a ferramentas mínimo e siga [Segurança](</pt-BR/gateway/security>)).
  * O onboarding local agora define novas configurações como `tools.profile: "coding"` por padrão, para que novas configurações locais mantenham ferramentas de sistema de arquivos/runtime sem forçar o perfil `full` irrestrito.
  * Se hooks/webhooks ou outros feeds de conteúdo não confiável estiverem habilitados, use uma camada de modelo moderna e forte e mantenha uma política de ferramentas/sandboxing rigorosa.


* ### Local vs Remoto

![](/assets/macos-onboarding/04-choose-gateway.png)

Onde o **Gateway** é executado?

  * **Este Mac (somente local):** o onboarding pode configurar a autenticação e gravar credenciais localmente.
  * **Remoto (via SSH/Tailnet):** o onboarding **não** configura autenticação local; as credenciais devem existir no host do gateway.
  * **Configurar depois:** pule a configuração e deixe o app sem configuração.


* ### Permissões

Escolha quais permissões você quer conceder ao OpenClaw ![](/assets/macos-onboarding/05-permissions.png)

O onboarding solicita as permissões TCC necessárias para:

  * Automação (AppleScript)
  * Notificações
  * Acessibilidade
  * Gravação de Tela
  * Microfone
  * Reconhecimento de Fala
  * Câmera
  * Localização


* ### CLI

* ### Chat de Onboarding (sessão dedicada)

Após a configuração, o app abre uma sessão de chat de onboarding dedicada para que o agente possa se apresentar e orientar os próximos passos. Isso mantém a orientação de primeira execução separada da sua conversa normal. Consulte [Inicialização](</pt-BR/start/bootstrapping>) para saber o que acontece no host do gateway durante a primeira execução do agente.

## Relacionados

  * [Visão geral do onboarding](</pt-BR/start/onboarding-overview>)
  * [Introdução](</pt-BR/start/getting-started>)


Was this useful?YesNo