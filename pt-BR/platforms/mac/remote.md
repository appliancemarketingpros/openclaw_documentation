---
title: Controle remoto
source_url: https://docs.openclaw.ai/pt-BR/platforms/mac/remote
scraped_at: 2026-05-25
---

Este fluxo permite que o app macOS atue como um controle remoto completo para um Gateway OpenClaw em execução em outro host (desktop/servidor). É o recurso **Remoto via SSH** (execução remota) do app. Todos os recursos, verificações de integridade, encaminhamento de Voice Wake e Chat Web reutilizam a mesma configuração SSH remota em _Ajustes → Geral_.

## Modos

  * **Local (este Mac)** : Tudo roda no laptop. Sem SSH envolvido.
  * **Remoto via SSH (padrão)** : Os comandos do OpenClaw são executados no host remoto. O app para Mac abre uma conexão SSH com `-o BatchMode`, além da identidade/chave escolhida e um encaminhamento de porta local.
  * **Remoto direto (ws/wss)** : Sem túnel SSH. O app para Mac se conecta diretamente à URL do Gateway (por exemplo, via Tailscale Serve ou um proxy reverso HTTPS público).


## Transportes remotos

O modo remoto oferece suporte a dois transportes:

  * **Túnel SSH** (padrão): Usa `ssh -N -L ...` para encaminhar a porta do Gateway para localhost. O Gateway verá o IP do Node como `127.0.0.1` porque o túnel usa loopback.
  * **Direto (ws/wss)** : Conecta diretamente à URL do Gateway. O Gateway vê o IP real do cliente.


No modo de túnel SSH, nomes de host LAN/tailnet descobertos são salvos como `gateway.remote.sshTarget`. O app mantém `gateway.remote.url` no endpoint de túnel local, por exemplo `ws://127.0.0.1:18789`, para que a CLI, o Chat Web e o serviço de host Node local usem todos o mesmo transporte seguro por loopback.

A automação de navegador no modo remoto pertence ao host Node da CLI, não ao Node nativo do app macOS. O app inicia o serviço de host Node instalado quando possível; se você precisar de controle de navegador a partir desse Mac, instale/inicie-o com `openclaw node install ...` e `openclaw node start` (ou execute `openclaw node run ...` em primeiro plano) e, em seguida, aponte para esse Node com capacidade de navegador.

## Pré-requisitos no host remoto

  1. Instale Node + pnpm e compile/instale a CLI do OpenClaw (`pnpm install && pnpm build && pnpm link --global`).
  2. Garanta que `openclaw` esteja no PATH para shells não interativos (crie um symlink em `/usr/local/bin` ou `/opt/homebrew/bin`, se necessário).
  3. Abra SSH com autenticação por chave. Recomendamos IPs do **Tailscale** para alcance estável fora da LAN.


## Configuração do app macOS

  1. Abra _Ajustes → Geral_.
  2. Em **OpenClaw executa** , escolha **Remoto via SSH** e defina: 
     * **Transporte** : **Túnel SSH** ou **Direto (ws/wss)**.
     * **Destino SSH** : `user@host` (`:port` opcional). 
       * Se o Gateway estiver na mesma LAN e anunciar Bonjour, escolha-o na lista descoberta para preencher este campo automaticamente.
     * **URL do Gateway** (somente Direto): `wss://gateway.example.ts.net` (ou `ws://...` para local/LAN).
     * **Arquivo de identidade** (avançado): caminho para sua chave.
     * **Raiz do projeto** (avançado): caminho do checkout remoto usado para comandos.
     * **Caminho da CLI** (avançado): caminho opcional para um ponto de entrada/binário `openclaw` executável (preenchido automaticamente quando anunciado).
  3. Clique em **Testar remoto**. Sucesso indica que o `openclaw status --json` remoto roda corretamente. Falhas geralmente significam problemas de PATH/CLI; o código de saída 127 significa que a CLI não foi encontrada remotamente.
  4. As verificações de integridade e o Chat Web agora serão executados automaticamente por meio desse túnel SSH.


## Chat Web

  * **Túnel SSH** : O Chat Web se conecta ao Gateway pela porta de controle WebSocket encaminhada (padrão 18789).
  * **Direto (ws/wss)** : O Chat Web se conecta diretamente à URL do Gateway configurada.
  * Não há mais um servidor HTTP separado do WebChat.


## Permissões

  * O host remoto precisa das mesmas aprovações TCC que o local (Automação, Acessibilidade, Gravação de Tela, Microfone, Reconhecimento de Fala, Notificações). Execute o onboarding nessa máquina para concedê-las uma vez.
  * Nodes anunciam seu estado de permissão via `node.list` / `node.describe` para que os agentes saibam o que está disponível.


## Observações de segurança

  * Prefira binds de loopback no host remoto e conecte via SSH ou Tailscale.
  * O tunelamento SSH usa verificação estrita de chave de host; confie primeiro na chave do host para que ela exista em `~/.ssh/known_hosts`.
  * Se você vincular o Gateway a uma interface que não seja loopback, exija autenticação válida do Gateway: token, senha ou um proxy reverso ciente de identidade com `gateway.auth.mode: "trusted-proxy"`.
  * Consulte [Segurança](</pt-BR/gateway/security>) e [Tailscale](</pt-BR/gateway/tailscale>).


## Fluxo de login do WhatsApp (remoto)

  * Execute `openclaw channels login --verbose` **no host remoto**. Escaneie o QR com o WhatsApp no seu telefone.
  * Execute o login novamente nesse host se a autenticação expirar. A verificação de integridade exibirá problemas de vínculo.


## Solução de problemas

  * **código de saída 127 / não encontrado** : `openclaw` não está no PATH para shells sem login. Adicione-o a `/etc/paths`, ao rc do seu shell, ou crie um symlink em `/usr/local/bin`/`/opt/homebrew/bin`.
  * **Sondagem de integridade falhou** : verifique o alcance SSH, o PATH e se o Baileys está conectado (`openclaw status --json`).
  * **Chat Web travado** : confirme que o Gateway está em execução no host remoto e que a porta encaminhada corresponde à porta WS do Gateway; a UI exige uma conexão WS íntegra.
  * **IP do Node mostra 127.0.0.1** : esperado com o túnel SSH. Altere **Transporte** para **Direto (ws/wss)** se quiser que o Gateway veja o IP real do cliente.
  * **Dashboard funciona, mas as capacidades do Mac estão offline** : isso significa que a conexão de operador/controle do app está íntegra, mas a conexão do Node complementar não está conectada ou está sem sua superfície de comandos. Abra a seção de dispositivo na barra de menus e verifique se o Mac está `paired · disconnected`. Para endpoints Tailscale Serve `wss://*.ts.net`, o app detecta pins legados obsoletos de folha TLS após a rotação de certificado, limpa o pin obsoleto quando o macOS confia no novo certificado e tenta novamente automaticamente. Se o certificado não for confiável pelo sistema ou o host não for um nome do Tailscale Serve, revise o certificado ou mude para **Remoto via SSH**.
  * **Voice Wake** : frases de acionamento são encaminhadas automaticamente no modo remoto; nenhum encaminhador separado é necessário.


## Sons de notificação

Escolha sons por notificação a partir de scripts com `openclaw` e `node.invoke`, por exemplo:

bashCopy code
[code]
    openclaw nodes notify --node <id> --title "Ping" --body "Remote gateway ready" --sound Glass
[/code]

Não há mais uma alternância global de "som padrão" no app; os chamadores escolhem um som (ou nenhum) por solicitação.

## Relacionado

  * [app macOS](</pt-BR/platforms/macos>)
  * [Acesso remoto](</pt-BR/gateway/remote>)


Was this useful?YesNo