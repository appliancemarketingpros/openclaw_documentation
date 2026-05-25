---
title: Navegador
source_url: https://docs.openclaw.ai/pt-BR/cli/browser
scraped_at: 2026-05-25
---

# `openclaw browser`

Gerencie a superfície de controle de navegador do OpenClaw e execute ações de navegador (ciclo de vida, perfis, abas, snapshots, capturas de tela, navegação, entrada, emulação de estado e depuração).

Relacionado:

  * Ferramenta de navegador + API: [Ferramenta de navegador](</pt-BR/tools/browser>)


## Flags comuns

  * `--url <gatewayWsUrl>`: URL WebSocket do Gateway (usa a configuração por padrão).
  * `--token <token>`: token do Gateway (se necessário).
  * `--timeout <ms>`: tempo limite da solicitação (ms).
  * `--expect-final`: aguarda uma resposta final do Gateway.
  * `--browser-profile <name>`: escolhe um perfil de navegador (padrão da configuração).
  * `--json`: saída legível por máquina (quando compatível).


## Início rápido (local)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

Agentes podem executar a mesma verificação de prontidão com `browser({ action: "doctor" })`.

## Solução rápida de problemas

Se `start` falhar com `not reachable after start`, investigue primeiro a prontidão do CDP. Se `start` e `tabs` funcionarem, mas `open` ou `navigate` falhar, o plano de controle do navegador está saudável e a falha geralmente é a política de SSRF de navegação.

Sequência mínima:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

Orientação detalhada: [Solução de problemas do navegador](</pt-BR/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## Ciclo de vida

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

Observações:

  * `doctor --deep` adiciona uma sondagem de snapshot em tempo real. Isso é útil quando a prontidão básica do CDP está verde, mas você quer prova de que a aba atual pode ser inspecionada.
  * Para perfis `attachOnly` e CDP remoto, `openclaw browser stop` fecha a sessão de controle ativa e limpa substituições temporárias de emulação mesmo quando o OpenClaw não iniciou o processo do navegador.
  * Para perfis locais gerenciados, `openclaw browser stop` interrompe o processo do navegador iniciado.
  * `openclaw browser start --headless` se aplica apenas a essa solicitação de inicialização e somente quando o OpenClaw inicia um navegador local gerenciado. Ele não reescreve `browser.headless` nem a configuração do perfil, e não tem efeito para um navegador que já está em execução.
  * Em hosts Linux sem `DISPLAY` ou `WAYLAND_DISPLAY`, perfis locais gerenciados executam automaticamente em modo headless, a menos que `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless=false` ou `browser.profiles.<name>.headless=false` solicite explicitamente um navegador visível.


## Se o comando estiver ausente

Se `openclaw browser` for um comando desconhecido, verifique `plugins.allow` em `~/.openclaw/openclaw.json`.

Quando `plugins.allow` estiver presente, liste explicitamente o Plugin de navegador incluído, a menos que a configuração já tenha um bloco raiz `browser`:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

Um bloco raiz `browser` explícito, por exemplo `browser.enabled=true` ou `browser.profiles.<name>`, também ativa o Plugin de navegador incluído sob uma lista restritiva de Plugins permitidos.

Relacionado: [Ferramenta de navegador](</pt-BR/tools/browser#missing-browser-command-or-tool>)

## Perfis

Perfis são configurações nomeadas de roteamento de navegador. Na prática:

  * `openclaw`: inicia ou anexa a uma instância dedicada do Chrome gerenciada pelo OpenClaw (diretório de dados de usuário isolado).
  * `user`: controla sua sessão existente do Chrome com login por meio do Chrome DevTools MCP.
  * perfis CDP personalizados: apontam para um endpoint CDP local ou remoto.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

Use um perfil específico:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## Abas

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

`tabs` retorna `suggestedTargetId` primeiro, depois o `tabId` estável, como `t1`, o rótulo opcional e o `targetId` bruto. Agentes devem passar `suggestedTargetId` de volta para `focus`, `close`, snapshots e ações. Você pode atribuir um rótulo com `open --label`, `tab new --label` ou `tab label`; rótulos, IDs de aba, IDs de destino brutos e prefixos únicos de ID de destino são todos aceitos. Quando o Chromium substitui o destino bruto subjacente durante uma navegação ou envio de formulário, o OpenClaw mantém o `tabId`/rótulo estável anexado à aba substituta quando consegue comprovar a correspondência. IDs de destino brutos continuam voláteis; prefira `suggestedTargetId`.

## Snapshot / captura de tela / ações

Snapshot:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

Captura de tela:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

Observações:

  * `--full-page` é apenas para capturas de página; não pode ser combinado com `--ref` ou `--element`.
  * Perfis `existing-session` / `user` aceitam capturas de tela de página e capturas `--ref` a partir da saída de snapshot, mas não capturas de tela CSS `--element`.
  * `--labels` sobrepõe as referências atuais do snapshot na captura de tela.
  * `snapshot --urls` acrescenta destinos de links descobertos a snapshots de IA para que agentes possam escolher destinos diretos de navegação em vez de inferir apenas pelo texto do link.


Navegar/clicar/digitar (automação de UI baseada em ref):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
[/code]

Respostas de ação retornam o `targetId` bruto atual após substituição de página acionada por ação quando o OpenClaw consegue comprovar a aba substituta. Scripts ainda devem armazenar e passar `suggestedTargetId`/rótulos para fluxos de trabalho duradouros.

Auxiliares de arquivo + diálogo:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --accept
[/code]

Perfis gerenciados do Chrome salvam downloads comuns acionados por clique no diretório de downloads do OpenClaw (`/tmp/openclaw/downloads` por padrão, ou a raiz temporária configurada). Use `waitfordownload` ou `download` quando o agente precisar aguardar um arquivo específico e retornar seu caminho; esses aguardadores explícitos controlam o próximo download.

## Estado e armazenamento

Viewport + emulação:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

Cookies + armazenamento:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## Depuração

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Chrome existente via MCP

Use o perfil integrado `user`, ou crie seu próprio perfil `existing-session`:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser --browser-profile chrome-live tabs
[/code]

Esse caminho é apenas para host. Para Docker, servidores headless, Browserless ou outras configurações remotas, use um perfil CDP.

Limites atuais de `existing-session`:

  * ações orientadas por snapshot usam refs, não seletores CSS
  * `browser.actionTimeoutMs` define o padrão de solicitações `act` compatíveis para 60000 ms quando chamadores omitem `timeoutMs`; `timeoutMs` por chamada ainda prevalece.
  * `click` é apenas clique esquerdo
  * `type` não oferece suporte a `slowly=true`
  * `press` não oferece suporte a `delayMs`
  * `hover`, `scrollintoview`, `drag`, `select`, `fill` e `evaluate` rejeitam substituições de tempo limite por chamada
  * `select` aceita apenas um valor
  * `wait --load networkidle` não é compatível
  * uploads de arquivos exigem `--ref` / `--input-ref`, não oferecem suporte a CSS `--element` e atualmente aceitam um arquivo por vez
  * hooks de diálogo não oferecem suporte a `--timeout`
  * capturas de tela aceitam capturas de página e `--ref`, mas não CSS `--element`
  * `responsebody`, interceptação de download, exportação de PDF e ações em lote ainda exigem um navegador gerenciado ou perfil CDP bruto


## Controle remoto de navegador (proxy de host Node)

Se o Gateway estiver em execução em uma máquina diferente do navegador, execute um **host Node** na máquina que tem Chrome/Brave/Edge/Chromium. O Gateway encaminhará ações de navegador para esse node (nenhum servidor separado de controle de navegador é necessário).

Use `gateway.nodes.browser.mode` para controlar o roteamento automático e `gateway.nodes.browser.node` para fixar um node específico se vários estiverem conectados.

Segurança + configuração remota: [Ferramenta de navegador](</pt-BR/tools/browser>), [Acesso remoto](</pt-BR/gateway/remote>), [Tailscale](</pt-BR/gateway/tailscale>), [Segurança](</pt-BR/gateway/security>)

## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Navegador](</pt-BR/tools/browser>)


Was this useful?YesNo