---
title: Configuração do Gateway remoto
source_url: https://docs.openclaw.ai/pt-BR/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> Este conteúdo foi incorporado a [Acesso remoto](</pt-BR/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>). Consulte essa página para o guia atual.

# Executando o OpenClaw.app com um Gateway remoto

O OpenClaw.app usa tunelamento SSH para se conectar a um Gateway remoto. Este guia mostra como configurá-lo.

## Visão geral
[code] 
    flowchart TB
        subgraph Client["Client Machine"]
            direction TB
            A["OpenClaw.app"]
            B["ws://127.0.0.1:18789\n(local port)"]
            T["SSH Tunnel"]
    
            A --> B
            B --> T
        end
        subgraph Remote["Remote Machine"]
            direction TB
            C["Gateway WebSocket"]
            D["ws://127.0.0.1:18789"]
    
            C --> D
        end
        T --> C
[/code]

## Configuração rápida

### Etapa 1: Adicionar configuração SSH

Edite `~/.ssh/config` e adicione:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Substitua `&lt;REMOTE_IP&gt;` e `&lt;REMOTE_USER&gt;` pelos seus valores.

### Etapa 2: Copiar a chave SSH

Copie sua chave pública para a máquina remota (digite a senha uma vez):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Etapa 3: Configurar a autenticação do Gateway remoto

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Use `gateway.remote.password` como alternativa se o seu Gateway remoto usar autenticação por senha. `OPENCLAW_GATEWAY_TOKEN` ainda é válido como uma substituição no nível do shell, mas a configuração durável do cliente remoto é `gateway.remote.token` / `gateway.remote.password`.

### Etapa 4: Iniciar o túnel SSH

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Etapa 5: Reiniciar o OpenClaw.app

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

O aplicativo agora se conectará ao Gateway remoto por meio do túnel SSH.

* * *

## Iniciar o túnel automaticamente ao fazer login

Para que o túnel SSH seja iniciado automaticamente quando você fizer login, crie um Launch Agent.

### Criar o arquivo PLIST

Salve isto como `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### Carregar o Launch Agent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

O túnel agora irá:

  * Iniciar automaticamente quando você fizer login
  * Reiniciar se falhar
  * Continuar em execução em segundo plano


Observação legada: remova qualquer LaunchAgent `com.openclaw.ssh-tunnel` remanescente, se presente.

* * *

## Solução de problemas

**Verifique se o túnel está em execução:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**Reinicie o túnel:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**Pare o túnel:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Como funciona

Componente | O que ele faz  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Encaminha a porta local 18789 para a porta remota 18789  
`ssh -N` | SSH sem executar comandos remotos (apenas encaminhamento de porta)  
`KeepAlive` | Reinicia automaticamente o túnel se ele falhar  
`RunAtLoad` | Inicia o túnel quando o agente é carregado  
  
O OpenClaw.app se conecta a `ws://127.0.0.1:18789` na sua máquina cliente. O túnel SSH encaminha essa conexão para a porta 18789 na máquina remota onde o Gateway está em execução.

## Relacionado

  * [Acesso remoto](</pt-BR/gateway/remote>)
  * [Tailscale](</pt-BR/gateway/tailscale>)


Was this useful?YesNo