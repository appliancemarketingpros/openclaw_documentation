---
title: Fly.io
source_url: https://docs.openclaw.ai/pt-BR/install/fly
scraped_at: 2026-05-25
---

**Objetivo:** Gateway do OpenClaw em execução em uma máquina da [Fly.io](<https://fly.io>) com armazenamento persistente, HTTPS automático e acesso ao Discord/canal.

## O que você precisa

  * [CLI flyctl](<https://fly.io/docs/hands-on/install-flyctl/>) instalada
  * Conta [Fly.io](<http://Fly.io>) (o plano gratuito funciona)
  * Autenticação do modelo: chave de API para o provedor de modelo escolhido
  * Credenciais do canal: token de bot do Discord, token do Telegram etc.


## Caminho rápido para iniciantes

  1. Clone o repositório → personalize `fly.toml`
  2. Crie o app + volume → defina os segredos
  3. Implante com `fly deploy`
  4. Acesse via SSH para criar a configuração ou use a UI de Controle


* ### Criar o app Fly

bashCopy code
[code]
    # Clone the repogit clone https://github.com/openclaw/openclaw.gitcd openclaw # Create a new Fly app (pick your own name)fly apps create my-openclaw # Create a persistent volume (1GB is usually enough)fly volumes create openclaw_data --size 1 --region iad
[/code]

**Dica:** Escolha uma região próxima de você. Opções comuns: `lhr` (Londres), `iad` (Virgínia), `sjc` (San Jose).

* ### Configurar fly.toml

Edite `fly.toml` para corresponder ao nome e aos requisitos do seu app.

**Observação de segurança:** A configuração padrão expõe uma URL pública. Para uma implantação reforçada sem IP público, consulte Implantação privada ou use `deploy/fly.private.toml`.

tomlCopy code
[code]
    app = "my-openclaw"  # Your app nameprimary_region = "iad" [build]  dockerfile = "Dockerfile" [env]  NODE_ENV = "production"  OPENCLAW_PREFER_PNPM = "1"  OPENCLAW_STATE_DIR = "/data"  NODE_OPTIONS = "--max-old-space-size=1536" [processes]  app = "node dist/index.js gateway --allow-unconfigured --port 3000 --bind lan" [http_service]  internal_port = 3000  force_https = true  auto_stop_machines = false  auto_start_machines = true  min_machines_running = 1  processes = ["app"] [[vm]]  size = "shared-cpu-2x"  memory = "2048mb" [mounts]  source = "openclaw_data"  destination = "/data"
[/code]

A imagem Docker do OpenClaw usa `tini` como entrypoint. Os comandos de processo da Fly substituem o `CMD` do Docker sem substituir o `ENTRYPOINT`, então o processo ainda é executado sob o `tini`.

**Configurações principais:**

Configuração | Motivo  
---|---  
`--bind lan` | Vincula a `0.0.0.0` para que o proxy da Fly consiga acessar o gateway  
`--allow-unconfigured` | Inicia sem um arquivo de configuração (você criará um depois)  
`internal_port = 3000` | Deve corresponder a `--port 3000` (ou `OPENCLAW_GATEWAY_PORT`) para as verificações de integridade da Fly  
`memory = "2048mb"` | 512 MB é pouco demais; 2 GB é recomendado  
`OPENCLAW_STATE_DIR = "/data"` | Persiste o estado no volume  
* ### Definir segredos

bashCopy code
[code]
    # Required: Gateway token (for non-loopback binding)fly secrets set OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32) # Model provider API keysfly secrets set ANTHROPIC_API_KEY=sk-ant-... # Optional: Other providersfly secrets set OPENAI_API_KEY=sk-...fly secrets set GOOGLE_API_KEY=... # Channel tokensfly secrets set DISCORD_BOT_TOKEN=MTQ...
[/code]

**Observações:**

  * Vínculos não loopback (`--bind lan`) exigem um caminho válido de autenticação do gateway. Este exemplo da [Fly.io](<http://Fly.io>) usa `OPENCLAW_GATEWAY_TOKEN`, mas `gateway.auth.password` ou uma implantação `trusted-proxy` não loopback configurada corretamente também satisfazem o requisito.
  * Trate esses tokens como senhas.
  * **Prefira variáveis de ambiente em vez de arquivo de configuração** para todas as chaves de API e tokens. Isso mantém os segredos fora de `openclaw.json`, onde poderiam ser expostos ou registrados acidentalmente.


* ### Implantar

bashCopy code
[code]
    fly deploy
[/code]

A primeira implantação compila a imagem Docker (~2 a 3 minutos). Implantações posteriores são mais rápidas.

Após a implantação, verifique:

bashCopy code
[code]
    fly statusfly logs
[/code]

Você deve ver:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:3000 (PID xxx)[discord] logged in to discord as xxx
[/code]

* ### Criar arquivo de configuração

Acesse a máquina via SSH para criar uma configuração adequada:

bashCopy code
[code]
    fly ssh console
[/code]

Crie o diretório e o arquivo de configuração:

bashCopy code
[code]
    mkdir -p /datacat > /data/openclaw.json << 'EOF'{  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-opus-4-6",        "fallbacks": ["anthropic/claude-sonnet-4-6", "openai/gpt-5.4"]      },      "maxConcurrent": 4    },    "list": [      {        "id": "main",        "default": true      }    ]  },  "auth": {    "profiles": {      "anthropic:default": { "mode": "token", "provider": "anthropic" },      "openai:default": { "mode": "token", "provider": "openai" }    }  },  "bindings": [    {      "agentId": "main",      "match": { "channel": "discord" }    }  ],  "channels": {    "discord": {      "enabled": true,      "groupPolicy": "allowlist",      "guilds": {        "YOUR_GUILD_ID": {          "channels": { "general": { "allow": true } },          "requireMention": false        }      }    }  },  "gateway": {    "mode": "local",    "bind": "auto",    "controlUi": {      "allowedOrigins": [        "https://my-openclaw.fly.dev",        "http://localhost:3000",        "http://127.0.0.1:3000"      ]    }  },  "meta": {}}EOF
[/code]

**Observação:** Com `OPENCLAW_STATE_DIR=/data`, o caminho da configuração é `/data/openclaw.json`.

**Observação:** Substitua `https://my-openclaw.fly.dev` pela origem real do seu app Fly. A inicialização do Gateway semeia origens locais da UI de Controle a partir dos valores de runtime `--bind` e `--port`, para que a primeira inicialização possa prosseguir antes que a configuração exista, mas o acesso pelo navegador via Fly ainda precisa da origem HTTPS exata listada em `gateway.controlUi.allowedOrigins`.

**Observação:** O token do Discord pode vir de:

  * Variável de ambiente: `DISCORD_BOT_TOKEN` (recomendado para segredos)
  * Arquivo de configuração: `channels.discord.token`


Se usar variável de ambiente, não é necessário adicionar o token à configuração. O gateway lê `DISCORD_BOT_TOKEN` automaticamente.

Reinicie para aplicar:

bashCopy code
[code]
    exitfly machine restart <machine-id>
[/code]

* ### Acessar o Gateway

### UI de Controle

Abra no navegador:

bashCopy code
[code]
    fly open
[/code]

Ou acesse `https://my-openclaw.fly.dev/`

Autentique-se com o segredo compartilhado configurado. Este guia usa o token do gateway de `OPENCLAW_GATEWAY_TOKEN`; se você mudou para autenticação por senha, use essa senha.

### Logs

bashCopy code
[code]
    fly logs              # Live logsfly logs --no-tail    # Recent logs
[/code]

### Console SSH

bashCopy code
[code]
    fly ssh console
[/code]

## Solução de problemas

### "App is not listening on expected address"

O gateway está vinculando a `127.0.0.1` em vez de `0.0.0.0`.

**Correção:** Adicione `--bind lan` ao comando de processo em `fly.toml`.

### Verificações de integridade falhando / conexão recusada

A Fly não consegue acessar o gateway na porta configurada.

**Correção:** Garanta que `internal_port` corresponda à porta do gateway (defina `--port 3000` ou `OPENCLAW_GATEWAY_PORT=3000`).

### OOM / Problemas de memória

O contêiner continua reiniciando ou sendo encerrado. Sinais: `SIGABRT`, `v8::internal::Runtime_AllocateInYoungGeneration` ou reinicializações silenciosas.

**Correção:** Aumente a memória em `fly.toml`:

tomlCopy code
[code]
    [[vm]]  memory = "2048mb"
[/code]

Ou atualize uma máquina existente:

bashCopy code
[code]
    fly machine update <machine-id> --vm-memory 2048 -y
[/code]

**Observação:** 512 MB é pouco demais. 1 GB pode funcionar, mas pode gerar OOM sob carga ou com logs verbosos. **2 GB é recomendado.**

### Problemas de bloqueio do Gateway

O Gateway se recusa a iniciar com erros de "already running".

Isso acontece quando o contêiner reinicia, mas o arquivo de bloqueio de PID persiste no volume.

**Correção:** Exclua o arquivo de bloqueio:

bashCopy code
[code]
    fly ssh console --command "rm -f /data/gateway.*.lock"fly machine restart <machine-id>
[/code]

O arquivo de bloqueio fica em `/data/gateway.*.lock` (não em um subdiretório).

### Configuração não está sendo lida

`--allow-unconfigured` apenas ignora a proteção de inicialização. Ele não cria nem repara `/data/openclaw.json`, então verifique se sua configuração real existe e inclui `gateway.mode="local"` quando você quiser uma inicialização normal do gateway local.

Verifique se a configuração existe:

bashCopy code
[code]
    fly ssh console --command "cat /data/openclaw.json"
[/code]

### Gravar configuração via SSH

O comando `fly ssh console -C` não oferece suporte a redirecionamento de shell. Para gravar um arquivo de configuração:

bashCopy code
[code]
    # Use echo + tee (pipe from local to remote)echo '{"your":"config"}' | fly ssh console -C "tee /data/openclaw.json" # Or use sftpfly sftp shell> put /local/path/config.json /data/openclaw.json
[/code]

**Observação:** `fly sftp` pode falhar se o arquivo já existir. Exclua primeiro:

bashCopy code
[code]
    fly ssh console --command "rm /data/openclaw.json"
[/code]

### Estado não está persistindo

Se você perder perfis de autenticação, estado de canal/provedor ou sessões após uma reinicialização, o diretório de estado está gravando no sistema de arquivos do contêiner.

**Correção:** Garanta que `OPENCLAW_STATE_DIR=/data` esteja definido em `fly.toml` e reimplante.

## Atualizações

bashCopy code
[code]
    # Pull latest changesgit pull # Redeployfly deploy # Check healthfly statusfly logs
[/code]

### Atualizar comando da máquina

Se você precisar alterar o comando de inicialização sem uma reimplantação completa:

bashCopy code
[code]
    # Get machine IDfly machines list # Update commandfly machine update <machine-id> --command "node dist/index.js gateway --port 3000 --bind lan" -y # Or with memory increasefly machine update <machine-id> --vm-memory 2048 --command "node dist/index.js gateway --port 3000 --bind lan" -y
[/code]

**Observação:** Após `fly deploy`, o comando da máquina pode voltar ao que está em `fly.toml`. Se você fez alterações manuais, reaplique-as após a implantação.

## Implantação privada (reforçada)

Por padrão, a Fly aloca IPs públicos, tornando seu gateway acessível em `https://your-app.fly.dev`. Isso é conveniente, mas significa que sua implantação pode ser descoberta por scanners da internet (Shodan, Censys etc.).

Para uma implantação reforçada **sem exposição pública** , use o modelo privado.

### Quando usar implantação privada

  * Você faz apenas chamadas/mensagens **de saída** (sem webhooks de entrada)
  * Você usa túneis **ngrok ou Tailscale** para quaisquer callbacks de Webhook
  * Você acessa o gateway via **SSH, proxy ou WireGuard** em vez do navegador
  * Você quer que a implantação fique **oculta de scanners da internet**


### Configuração

Use `deploy/fly.private.toml` em vez da configuração padrão:

bashCopy code
[code]
    # Deploy with private configfly deploy -c deploy/fly.private.toml
[/code]

Ou converta uma implantação existente:

bashCopy code
[code]
    # List current IPsfly ips list -a my-openclaw # Release public IPsfly ips release <public-ipv4> -a my-openclawfly ips release <public-ipv6> -a my-openclaw # Switch to private config so future deploys don't re-allocate public IPs# (remove [http_service] or deploy with the private template)fly deploy -c deploy/fly.private.toml # Allocate private-only IPv6fly ips allocate-v6 --private -a my-openclaw
[/code]

Depois disso, `fly ips list` deve mostrar apenas um IP do tipo `private`:

CodeCopy code
[code]
    VERSION  IP                   TYPE             REGIONv6       fdaa:x:x:x:x::x      private          global
[/code]

### Acessar uma implantação privada

Como não há URL pública, use um destes métodos:

**Opção 1: Proxy local (mais simples)**

bashCopy code
[code]
    # Forward local port 3000 to the appfly proxy 3000:3000 -a my-openclaw # Then open http://localhost:3000 in browser
[/code]

**Opção 2: VPN WireGuard**

bashCopy code
[code]
    # Create WireGuard config (one-time)fly wireguard create # Import to WireGuard client, then access via internal IPv6# Example: http://[fdaa:x:x:x:x::x]:3000
[/code]

**Opção 3: somente SSH**

bashCopy code
[code]
    fly ssh console -a my-openclaw
[/code]

### Webhooks com implantação privada

Se você precisar de callbacks de webhook (Twilio, Telnyx etc.) sem exposição pública:

  1. **Túnel ngrok** \- Execute o ngrok dentro do contêiner ou como sidecar
  2. **Tailscale Funnel** \- Exponha caminhos específicos via Tailscale
  3. **Somente saída** \- Alguns provedores (Twilio) funcionam bem para chamadas de saída sem webhooks


Exemplo de configuração de chamada de voz com ngrok:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          tunnel: { provider: "ngrok" },          webhookSecurity: {            allowedHosts: ["example.ngrok.app"],          },        },      },    },  },}
[/code]

O túnel ngrok é executado dentro do contêiner e fornece uma URL pública de webhook sem expor o próprio app Fly. Defina `webhookSecurity.allowedHosts` como o hostname público do túnel para que os cabeçalhos de host encaminhados sejam aceitos.

### Benefícios de segurança

Aspecto | Público | Privado  
---|---|---  
Scanners da internet | Detectável | Oculto  
Ataques diretos | Possíveis | Bloqueados  
Acesso à interface de controle | Navegador | Proxy/VPN  
Entrega de webhook | Direta | Via túnel  
  
## Observações

  * A [Fly.io](<http://Fly.io>) usa **arquitetura x86** (não ARM)
  * O Dockerfile é compatível com ambas as arquiteturas
  * Para onboarding do WhatsApp/Telegram, use `fly ssh console`
  * Dados persistentes ficam no volume em `/data`
  * Signal requer Java + signal-cli; use uma imagem personalizada e mantenha a memória em 2 GB ou mais.


## Custo

Com a configuração recomendada (`shared-cpu-2x`, 2 GB de RAM):

  * Cerca de US$ 10-15/mês, dependendo do uso
  * O plano gratuito inclui uma cota


Consulte [preços da Fly.io](<https://fly.io/docs/about/pricing/>) para obter detalhes.

## Próximos passos

  * Configure canais de mensagens: [Canais](</pt-BR/channels>)
  * Configure o Gateway: [Configuração do Gateway](</pt-BR/gateway/configuration>)
  * Mantenha o OpenClaw atualizado: [Atualização](</pt-BR/install/updating>)


## Relacionado

  * [Visão geral da instalação](</pt-BR/install>)
  * [Hetzner](</pt-BR/install/hetzner>)
  * [Docker](</pt-BR/install/docker>)
  * [Hospedagem VPS](</pt-BR/vps>)


Was this useful?YesNo