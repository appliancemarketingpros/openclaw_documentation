---
title: exe.dev
source_url: https://docs.openclaw.ai/pt-BR/install/exe-dev
scraped_at: 2026-05-25
---

Objetivo: OpenClaw Gateway em execução em uma VM exe.dev, acessível pelo seu laptop via: `https://<vm-name>.exe.xyz`

Esta página pressupõe a imagem **exeuntu** padrão do exe.dev. Se você escolheu uma distribuição diferente, mapeie os pacotes de acordo.

## Caminho rápido para iniciantes

  1. <https://exe.new/openclaw>
  2. Preencha sua chave/token de autenticação conforme necessário
  3. Clique em "Agente" ao lado da sua VM e aguarde Shelley concluir o provisionamento
  4. Abra `https://<vm-name>.exe.xyz/` e autentique-se com o segredo compartilhado configurado (este guia usa autenticação por token por padrão, mas a autenticação por senha também funciona se você alterar `gateway.auth.mode`)
  5. Aprove quaisquer solicitações pendentes de pareamento de dispositivo com `openclaw devices approve <requestId>`


## O que você precisa

  * Conta exe.dev
  * Acesso `ssh exe.dev` a máquinas virtuais [exe.dev](<https://exe.dev>) (opcional)


## Instalação automatizada com Shelley

Shelley, o agente do [exe.dev](<https://exe.dev>), pode instalar o OpenClaw instantaneamente com nosso prompt. O prompt usado é o seguinte:

CodeCopy code
[code]
    Set up OpenClaw (https://docs.openclaw.ai/install) on this VM. Use the non-interactive and accept-risk flags for openclaw onboarding. Add the supplied auth or token as needed. Configure nginx to forward from the default port 18789 to the root location on the default enabled site config, making sure to enable Websocket support. Pairing is done by "openclaw devices list" and "openclaw devices approve <request id>". Make sure the dashboard shows that OpenClaw's health is OK. exe.dev handles forwarding from port 8000 to port 80/443 and HTTPS for us, so the final "reachable" should be <vm-name>.exe.xyz, without port specification.
[/code]

## Instalação manual

## 1) Crie a VM

Do seu dispositivo:

bashCopy code
[code]
    ssh exe.dev new
[/code]

Em seguida, conecte-se:

bashCopy code
[code]
    ssh <vm-name>.exe.xyz
[/code]

## 2) Instale os pré-requisitos (na VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl jq ca-certificates openssl
[/code]

## 3) Instale o OpenClaw

Execute o script de instalação do OpenClaw:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

## 4) Configure o nginx para fazer proxy do OpenClaw para a porta 8000

Edite `/etc/nginx/sites-enabled/default` com

CodeCopy code
[code]
    server {    listen 80 default_server;    listen [::]:80 default_server;    listen 8000;    listen [::]:8000;     server_name _;     location / {        proxy_pass http://127.0.0.1:18789;        proxy_http_version 1.1;         # WebSocket support        proxy_set_header Upgrade $http_upgrade;        proxy_set_header Connection "upgrade";         # Standard proxy headers        proxy_set_header Host $host;        proxy_set_header X-Real-IP $remote_addr;        proxy_set_header X-Forwarded-For $remote_addr;        proxy_set_header X-Forwarded-Proto $scheme;         # Timeout settings for long-lived connections        proxy_read_timeout 86400s;        proxy_send_timeout 86400s;    }}
[/code]

Sobrescreva os cabeçalhos de encaminhamento em vez de preservar cadeias fornecidas pelo cliente. O OpenClaw confia em metadados de IP encaminhados somente de proxies configurados explicitamente, e cadeias `X-Forwarded-For` no estilo de acréscimo são tratadas como um risco de proteção.

## 5) Acesse o OpenClaw e conceda privilégios

Acesse `https://<vm-name>.exe.xyz/` (veja a saída da Control UI do onboarding). Se ele solicitar autenticação, cole o segredo compartilhado configurado da VM. Este guia usa autenticação por token, então obtenha `gateway.auth.token` com `openclaw config get gateway.auth.token` (ou gere um com `openclaw doctor --generate-gateway-token`). Se você alterou o Gateway para autenticação por senha, use `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD`. Aprove dispositivos com `openclaw devices list` e `openclaw devices approve <requestId>`. Em caso de dúvida, use Shelley no seu navegador!

## Configuração de canais remotos

Para hosts remotos, prefira uma chamada `config patch` em vez de muitas chamadas SSH para `config set`. Mantenha tokens reais no ambiente da VM ou em `~/.openclaw/.env`, e coloque somente SecretRefs em `openclaw.json`.

Na VM, faça o ambiente do serviço conter os segredos de que ele precisa:

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'SLACK_BOT_TOKEN=xoxb-...SLACK_APP_TOKEN=xapp-...DISCORD_BOT_TOKEN=...OPENAI_API_KEY=sk-...EOF
[/code]

Na sua máquina local, crie um arquivo de patch e envie-o por pipe para a VM:

json5Copy code
[code]
    // openclaw.remote.patch.json5{  secrets: {    providers: {      default: { source: "env" },    },  },  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --dry-run' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw config patch --stdin' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw gateway restart && openclaw health'
[/code]

Use `--replace-path` quando uma allowlist aninhada deve se tornar exatamente o valor do patch, por exemplo, ao substituir uma allowlist de canal do Discord:

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --replace-path "channels.discord.guilds[\"123\"].channels"' < ./discord.patch.json5
[/code]

## Acesso remoto

O acesso remoto é tratado pela autenticação do [exe.dev](<https://exe.dev>). Por padrão, o tráfego HTTP da porta 8000 é encaminhado para `https://<vm-name>.exe.xyz` com autenticação por email.

## Atualização

bashCopy code
[code]
    npm i -g openclaw@latestopenclaw doctoropenclaw gateway restartopenclaw health
[/code]

Guia: [Atualização](</pt-BR/install/updating>)

## Relacionado

  * [Gateway remoto](</pt-BR/gateway/remote>)
  * [Visão geral da instalação](</pt-BR/install>)


Was this useful?YesNo