---
title: Autenticação por proxy confiável
source_url: https://docs.openclaw.ai/pt-BR/gateway/trusted-proxy-auth
scraped_at: 2026-05-25
---

## Quando usar

Use o modo de autenticação `trusted-proxy` quando:

  * Você executa o OpenClaw atrás de um **proxy ciente de identidade** (Pomerium, Caddy + OAuth, nginx + oauth2-proxy, Traefik + forward auth).
  * Seu proxy lida com toda a autenticação e passa a identidade do usuário por meio de cabeçalhos.
  * Você está em um ambiente Kubernetes ou de contêiner em que o proxy é o único caminho até o Gateway.
  * Você está encontrando erros WebSocket `1008 unauthorized` porque navegadores não conseguem passar tokens em payloads WS.


## Quando NÃO usar

  * Se seu proxy não autentica usuários (apenas um terminador TLS ou balanceador de carga).
  * Se houver qualquer caminho até o Gateway que contorne o proxy (brechas no firewall, acesso pela rede interna).
  * Se você não tiver certeza de que seu proxy remove/substitui corretamente os cabeçalhos encaminhados.
  * Se você só precisa de acesso pessoal de usuário único (considere Tailscale Serve + loopback para uma configuração mais simples).


## Como funciona

* ### Proxy authenticates the user

Seu proxy reverso autentica usuários (OAuth, OIDC, SAML etc.).

* ### Proxy adds an identity header

O proxy adiciona um cabeçalho com a identidade do usuário autenticado (por exemplo, `x-forwarded-user: nick@example.com`).

* ### Gateway verifies trusted source

O OpenClaw verifica se a solicitação veio de um **IP de proxy confiável** (configurado em `gateway.trustedProxies`).

* ### Gateway extracts identity

O OpenClaw extrai a identidade do usuário do cabeçalho configurado.

* ### Authorize

Se tudo estiver correto, a solicitação é autorizada.

## Comportamento de pareamento da Control UI

Quando `gateway.auth.mode = "trusted-proxy"` está ativo e a solicitação passa nas verificações de trusted-proxy, as sessões WebSocket da Control UI podem se conectar sem identidade de pareamento de dispositivo.

Implicações:

  * O pareamento deixa de ser a barreira principal para acesso à Control UI neste modo.
  * A política de autenticação do seu proxy reverso e `allowUsers` se tornam o controle de acesso efetivo.
  * Mantenha a entrada do gateway bloqueada apenas para IPs de proxy confiáveis (`gateway.trustedProxies` \+ firewall).


## Configuração

json5Copy code
[code]
    {  gateway: {    // Trusted-proxy auth expects requests from a non-loopback trusted proxy source by default    bind: "lan",     // CRITICAL: Only add your proxy's IP(s) here    trustedProxies: ["10.0.0.1", "172.17.0.1"],     auth: {      mode: "trusted-proxy",      trustedProxy: {        // Header containing authenticated user identity (required)        userHeader: "x-forwarded-user",         // Optional: headers that MUST be present (proxy verification)        requiredHeaders: ["x-forwarded-proto", "x-forwarded-host"],         // Optional: restrict to specific users (empty = allow all)        allowUsers: ["nick@example.com", "admin@company.org"],         // Optional: allow a same-host loopback proxy after explicit opt-in        allowLoopback: false,      },    },  },}
[/code]

### Referência de configuração

Array de endereços IP de proxy nos quais confiar. Solicitações de outros IPs são rejeitadas.

Deve ser `"trusted-proxy"`.

Nome do cabeçalho que contém a identidade do usuário autenticado.

Cabeçalhos adicionais que devem estar presentes para que a solicitação seja confiável.

Lista de permissão de identidades de usuário. Vazio significa permitir todos os usuários autenticados.

Suporte opcional para proxies reversos de loopback no mesmo host. O padrão é `false`.

## Terminação TLS e HSTS

Use um ponto de terminação TLS e aplique HSTS nele.

### Proxy TLS termination (recommended)

Quando seu proxy reverso lida com HTTPS para `https://control.example.com`, defina `Strict-Transport-Security` no proxy para esse domínio.

  * Boa opção para implantações expostas à internet.
  * Mantém a política de certificados e endurecimento HTTP em um só lugar.
  * O OpenClaw pode permanecer em HTTP de loopback atrás do proxy.


Valor de cabeçalho de exemplo:

textCopy code
[code]
    Strict-Transport-Security: max-age=31536000; includeSubDomains
[/code]

### Gateway TLS termination

Se o próprio OpenClaw servir HTTPS diretamente (sem proxy com terminação TLS), defina:

json5Copy code
[code]
    {  gateway: {    tls: { enabled: true },    http: {      securityHeaders: {        strictTransportSecurity: "max-age=31536000; includeSubDomains",      },    },  },}
[/code]

`strictTransportSecurity` aceita um valor de cabeçalho em string ou `false` para desabilitar explicitamente.

### Orientação de implantação gradual

  * Comece primeiro com uma duração máxima curta (por exemplo, `max-age=300`) enquanto valida o tráfego.
  * Aumente para valores de longa duração (por exemplo, `max-age=31536000`) somente depois de ter alta confiança.
  * Adicione `includeSubDomains` somente se todos os subdomínios estiverem prontos para HTTPS.
  * Use preload somente se você atender intencionalmente aos requisitos de preload para todo o conjunto de domínios.
  * O desenvolvimento local apenas em loopback não se beneficia de HSTS.


## Exemplos de configuração de proxy

Pomerium

O Pomerium passa a identidade em `x-pomerium-claim-email` (ou outros cabeçalhos de declaração) e um JWT em `x-pomerium-jwt-assertion`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Pomerium's IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-pomerium-claim-email",        requiredHeaders: ["x-pomerium-jwt-assertion"],      },    },  },}
[/code]

Trecho de configuração do Pomerium:

yamlCopy code
[code]
    routes:  - from: https://openclaw.example.com    to: http://openclaw-gateway:18789    policy:      - allow:          or:            - email:                is: nick@example.com    pass_identity_headers: true
[/code]

Caddy with OAuth

O Caddy com o Plugin `caddy-security` pode autenticar usuários e passar cabeçalhos de identidade.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Caddy/sidecar proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

Trecho de Caddyfile:

CodeCopy code
[code]
    openclaw.example.com {    authenticate with oauth2_provider    authorize with policy1     reverse_proxy openclaw:18789 {        header_up X-Forwarded-User {http.auth.user.email}    }}
[/code]

nginx + oauth2-proxy

O oauth2-proxy autentica usuários e passa a identidade em `x-auth-request-email`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // nginx/oauth2-proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-auth-request-email",      },    },  },}
[/code]

Trecho de configuração do nginx:

nginxCopy code
[code]
    location / {    auth_request /oauth2/auth;    auth_request_set $user $upstream_http_x_auth_request_email;     proxy_pass http://openclaw:18789;    proxy_set_header X-Auth-Request-Email $user;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "upgrade";}
[/code]

Traefik with forward auth json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["172.17.0.1"], // Traefik container IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

## Configuração mista de token

O OpenClaw rejeita configurações ambíguas em que tanto um `gateway.auth.token` (ou `OPENCLAW_GATEWAY_TOKEN`) quanto o modo `trusted-proxy` estão ativos ao mesmo tempo. Configurações mistas de token podem fazer com que solicitações de loopback sejam autenticadas silenciosamente pelo caminho de autenticação errado.

Se você vir um erro `mixed_trusted_proxy_token` na inicialização:

  * Remova o token compartilhado ao usar o modo trusted-proxy, ou
  * Altere `gateway.auth.mode` para `"token"` se você pretende usar autenticação baseada em token.


Cabeçalhos de identidade trusted-proxy em loopback ainda falham de forma fechada: chamadores no mesmo host não são autenticados silenciosamente como usuários de proxy. Chamadores internos do OpenClaw que contornam o proxy podem se autenticar com `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD` em vez disso. O fallback por token continua intencionalmente sem suporte no modo trusted-proxy.

## Cabeçalho de escopos de operador

A autenticação trusted-proxy é um modo HTTP **portador de identidade** , então os chamadores podem declarar opcionalmente escopos de operador com `x-openclaw-scopes`.

Exemplos:

  * `x-openclaw-scopes: operator.read`
  * `x-openclaw-scopes: operator.read,operator.write`
  * `x-openclaw-scopes: operator.admin,operator.write`


Comportamento:

  * Quando o cabeçalho está presente, o OpenClaw respeita o conjunto de escopos declarado.
  * Quando o cabeçalho está presente, mas vazio, a solicitação declara **nenhum** escopo de operador.
  * Quando o cabeçalho está ausente, APIs HTTP portadoras de identidade normais recorrem ao conjunto padrão de escopos de operador.
  * As **rotas HTTP de Plugin** com autenticação de Gateway são mais restritas por padrão: quando `x-openclaw-scopes` está ausente, o escopo de runtime delas recorre a `operator.write`.
  * Solicitações HTTP de origem em navegador ainda precisam passar por `gateway.controlUi.allowedOrigins` (ou modo deliberado de fallback por cabeçalho Host) mesmo depois que a autenticação trusted-proxy é bem-sucedida.


Regra prática: envie `x-openclaw-scopes` explicitamente quando quiser que uma solicitação trusted-proxy seja mais restrita do que os padrões, ou quando uma rota de Plugin com autenticação de gateway precisar de algo mais forte do que escopo de escrita.

## Lista de verificação de segurança

Antes de habilitar a autenticação trusted-proxy, verifique:

  * [ ] **O proxy é o único caminho** : A porta do Gateway está protegida por firewall de tudo, exceto seu proxy.
  * [ ] **trustedProxies é mínimo** : Somente os IPs reais do seu proxy, não sub-redes inteiras.
  * [ ] **A origem de proxy em loopback é deliberada** : A autenticação trusted-proxy falha de forma fechada para solicitações com origem em loopback, a menos que `gateway.auth.trustedProxy.allowLoopback` esteja explicitamente habilitado para um proxy no mesmo host.
  * [ ] **O proxy remove cabeçalhos** : Seu proxy sobrescreve (não acrescenta) cabeçalhos `x-forwarded-*` dos clientes.
  * [ ] **Terminação TLS** : Seu proxy lida com TLS; usuários se conectam via HTTPS.
  * [ ] **allowedOrigins é explícito** : A UI de Controle não loopback usa `gateway.controlUi.allowedOrigins` explícito.
  * [ ] **allowUsers está definido** (recomendado): Restrinja a usuários conhecidos em vez de permitir qualquer pessoa autenticada.
  * [ ] **Nenhuma configuração mista de token** : Não defina `gateway.auth.token` e `gateway.auth.mode: "trusted-proxy"` ao mesmo tempo.
  * [ ] **O fallback de senha local é privado** : Se você configurar `gateway.auth.password` para chamadores diretos internos, mantenha a porta do Gateway protegida por firewall para que clientes remotos que não passam pelo proxy não possam acessá-la diretamente.


## Auditoria de segurança

`openclaw security audit` sinalizará a autenticação trusted-proxy com uma descoberta de severidade **crítica**. Isso é intencional — é um lembrete de que você está delegando a segurança à configuração do seu proxy.

A auditoria verifica:

  * Aviso/lembrete crítico base `gateway.trusted_proxy_auth`
  * Configuração `trustedProxies` ausente
  * Configuração `userHeader` ausente
  * `allowUsers` vazio (permite qualquer usuário autenticado)
  * `allowLoopback` habilitado para origens de proxy no mesmo host
  * Política de origem do navegador curinga ou ausente em superfícies expostas da UI de Controle


## Solução de problemas

trusted_proxy_untrusted_source

A solicitação não veio de um IP em `gateway.trustedProxies`. Verifique:

  * O IP do proxy está correto? (IPs de contêineres Docker podem mudar.)
  * Há um balanceador de carga na frente do seu proxy?
  * Use `docker inspect` ou `kubectl get pods -o wide` para encontrar os IPs reais.

trusted_proxy_loopback_source

O OpenClaw rejeitou uma solicitação trusted-proxy com origem em loopback.

Verifique:

  * O proxy está se conectando de `127.0.0.1` / `::1`?
  * Você está tentando usar autenticação trusted-proxy com um proxy reverso local no mesmo host?


Correção:

  * Prefira autenticação por token/senha para clientes internos no mesmo host que não passam pelo proxy, ou
  * Encaminhe por um endereço de proxy confiável que não seja loopback e mantenha esse IP em `gateway.trustedProxies`, ou
  * Para um proxy reverso deliberado no mesmo host, defina `gateway.auth.trustedProxy.allowLoopback = true`, mantenha o endereço de loopback em `gateway.trustedProxies` e garanta que o proxy remova ou sobrescreva cabeçalhos de identidade.

trusted_proxy_user_missing

O cabeçalho de usuário estava vazio ou ausente. Verifique:

  * Seu proxy está configurado para passar cabeçalhos de identidade?
  * O nome do cabeçalho está correto? (não diferencia maiúsculas de minúsculas, mas a grafia importa)
  * O usuário está realmente autenticado no proxy?

trusted_proxy_missing_header_*

Um cabeçalho obrigatório não estava presente. Verifique:

  * Sua configuração de proxy para esses cabeçalhos específicos.
  * Se cabeçalhos estão sendo removidos em algum ponto da cadeia.

trusted_proxy_user_not_allowed

O usuário está autenticado, mas não está em `allowUsers`. Adicione-o ou remova a lista de permissão.

trusted_proxy_origin_not_allowed

A autenticação trusted-proxy foi bem-sucedida, mas o cabeçalho `Origin` do navegador não passou nas verificações de origem da UI de Controle.

Verifique:

  * `gateway.controlUi.allowedOrigins` inclui a origem exata do navegador.
  * Você não está dependendo de origens curinga, a menos que queira intencionalmente o comportamento de permitir tudo.
  * Se você usa intencionalmente o modo de fallback de cabeçalho Host, `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` está definido deliberadamente.

WebSocket still failing

Garanta que seu proxy:

  * Ofereça suporte a upgrades WebSocket (`Upgrade: websocket`, `Connection: upgrade`).
  * Passe os cabeçalhos de identidade em solicitações de upgrade WebSocket (não apenas HTTP).
  * Não tenha um caminho de autenticação separado para conexões WebSocket.


## Migração da autenticação por token

Se você está migrando da autenticação por token para trusted-proxy:

* ### Configure the proxy

Configure seu proxy para autenticar usuários e passar cabeçalhos.

* ### Test the proxy independently

Teste a configuração do proxy de forma independente (curl com cabeçalhos).

* ### Update OpenClaw config

Atualize a configuração do OpenClaw com autenticação trusted-proxy.

* ### Restart the Gateway

Reinicie o Gateway.

* ### Test WebSocket

Teste conexões WebSocket a partir da UI de Controle.

* ### Audit

Execute `openclaw security audit` e revise as descobertas.

## Relacionados

  * [Configuração](</pt-BR/gateway/configuration>) — referência de configuração
  * [Acesso remoto](</pt-BR/gateway/remote>) — outros padrões de acesso remoto
  * [Segurança](</pt-BR/gateway/security>) — guia completo de segurança
  * [Tailscale](</pt-BR/gateway/tailscale>) — alternativa mais simples para acesso somente por tailnet


Was this useful?YesNo