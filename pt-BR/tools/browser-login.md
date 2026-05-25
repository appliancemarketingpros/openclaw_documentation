---
title: Login pelo navegador
source_url: https://docs.openclaw.ai/pt-BR/tools/browser-login
scraped_at: 2026-05-25
---

## Login manual (recomendado)

Quando um site exigir login, **entre manualmente** no perfil do navegador do **host** (o navegador do openclaw).

**Não** forneça suas credenciais ao modelo. Logins automatizados costumam acionar defesas antibot e podem bloquear a conta.

Voltar para a documentação principal do navegador: [Navegador](</pt-BR/tools/browser>).

## Qual perfil do Chrome é usado?

O OpenClaw controla um **perfil dedicado do Chrome** (chamado `openclaw`, com interface em tom alaranjado). Ele é separado do seu perfil de navegador do dia a dia.

Para chamadas da ferramenta de navegador do agente:

  * Escolha padrão: o agente deve usar seu navegador `openclaw` isolado.
  * Use `profile="user"` somente quando sessões já autenticadas existentes forem importantes e o usuário estiver no computador para clicar/aprovar qualquer prompt de anexação.
  * Se você tiver vários perfis de navegador de usuário, especifique o perfil explicitamente em vez de adivinhar.


Duas formas simples de acessá-lo:

  1. **Peça ao agente para abrir o navegador** e depois faça login você mesmo.
  2. **Abra-o via CLI** :

bashCopy code
[code]
    openclaw browser startopenclaw browser open https://x.com
[/code]

Se você tiver vários perfis, passe `--browser-profile <name>` (o padrão é `openclaw`).

## X/Twitter: fluxo recomendado

  * **Ler/pesquisar/threads:** use o navegador do **host** (login manual).
  * **Publicar atualizações:** use o navegador do **host** (login manual).


## Sandboxing + acesso ao navegador do host

Sessões de navegador em sandbox têm **maior probabilidade** de acionar detecção de bots. Para X/Twitter (e outros sites rigorosos), prefira o navegador do **host**.

Se o agente estiver em sandbox, a ferramenta de navegador usa a sandbox por padrão. Para permitir controle do host:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        browser: {          allowHostControl: true,        },      },    },  },}
[/code]

Depois, abra você mesmo o navegador do host (invocações pela CLI sempre rodam contra o navegador do host):

bashCopy code
[code]
    openclaw browser open https://x.com --browser-profile openclaw
[/code]

As chamadas da ferramenta `browser` do agente podem então mirar o host assim que `sandbox.browser.allowHostControl: true` estiver definido. Como alternativa, desative a sandbox para o agente que publica atualizações.

## Relacionados

  * [Navegador](</pt-BR/tools/browser>)
  * [Solução de problemas do navegador no Linux](</pt-BR/tools/browser-linux-troubleshooting>)
  * [Solução de problemas do navegador no WSL2](</pt-BR/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo