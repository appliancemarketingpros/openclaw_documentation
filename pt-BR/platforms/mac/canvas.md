---
title: Tela
source_url: https://docs.openclaw.ai/pt-BR/platforms/mac/canvas
scraped_at: 2026-05-25
---

O app macOS incorpora um **painel Canvas** controlado por agente usando `WKWebView`. Ele é um workspace visual leve para HTML/CSS/JS, A2UI e pequenas superfícies de UI interativas.

## Onde o Canvas fica

O estado do Canvas é armazenado em Application Support:

  * `~/Library/Application Support/OpenClaw/canvas/<session>/...`


O painel Canvas serve esses arquivos por meio de um **esquema de URL personalizado** :

  * `openclaw-canvas://<session>/<path>`


Exemplos:

  * `openclaw-canvas://main/` → `<canvasRoot>/main/index.html`
  * `openclaw-canvas://main/assets/app.css` → `<canvasRoot>/main/assets/app.css`
  * `openclaw-canvas://main/widgets/todo/` → `<canvasRoot>/main/widgets/todo/index.html`


Se não houver `index.html` na raiz, o app mostra uma **página scaffold integrada**.

## Comportamento do painel

  * Painel sem borda, redimensionável, ancorado perto da barra de menus (ou do cursor do mouse).
  * Lembra tamanho/posição por sessão.
  * Recarrega automaticamente quando arquivos locais do canvas mudam.
  * Apenas um painel Canvas fica visível por vez (a sessão é alternada conforme necessário).


O Canvas pode ser desativado em Configurações → **Permitir Canvas**. Quando desativado, os comandos Node de canvas retornam `CANVAS_DISABLED`.

## Superfície da API do agente

O Canvas é exposto via **Gateway WebSocket** , para que o agente possa:

  * mostrar/ocultar o painel
  * navegar para um caminho ou URL
  * avaliar JavaScript
  * capturar uma imagem de snapshot


Exemplos de CLI:

bashCopy code
[code]
    openclaw nodes canvas present --node <id>openclaw nodes canvas navigate --node <id> --url "/"openclaw nodes canvas eval --node <id> --js "document.title"openclaw nodes canvas snapshot --node <id>
[/code]

Observações:

  * `canvas.navigate` aceita **caminhos locais do canvas** , URLs `http(s)` e URLs `file://`.
  * Se você passar `"/"`, o Canvas mostra o scaffold local ou `index.html`.


## A2UI no Canvas

A2UI é hospedado pelo host de canvas do Gateway e renderizado dentro do painel Canvas. Quando o Gateway anuncia um host de Canvas, o app macOS navega automaticamente para a página host do A2UI na primeira abertura.

URL padrão do host A2UI:

CodeCopy code
[code]
    http://<gateway-host>:18789/__openclaw__/a2ui/
[/code]

### Comandos A2UI (v0.8)

Atualmente, o Canvas aceita mensagens servidor→cliente **A2UI v0.8** :

  * `beginRendering`
  * `surfaceUpdate`
  * `dataModelUpdate`
  * `deleteSurface`


`createSurface` (v0.9) não é compatível.

Exemplo de CLI:

bashCopy code
[code]
    cat > /tmp/a2ui-v0.8.jsonl <<'EOFA2'{"surfaceUpdate":{"surfaceId":"main","components":[{"id":"root","component":{"Column":{"children":{"explicitList":["title","content"]}}}},{"id":"title","component":{"Text":{"text":{"literalString":"Canvas (A2UI v0.8)"},"usageHint":"h1"}}},{"id":"content","component":{"Text":{"text":{"literalString":"If you can read this, A2UI push works."},"usageHint":"body"}}}]}}{"beginRendering":{"surfaceId":"main","root":"root"}}EOFA2 openclaw nodes canvas a2ui push --jsonl /tmp/a2ui-v0.8.jsonl --node <id>
[/code]

Smoke rápido:

bashCopy code
[code]
    openclaw nodes canvas a2ui push --node <id> --text "Hello from A2UI"
[/code]

## Acionando execuções do agente pelo Canvas

O Canvas pode acionar novas execuções do agente por meio de links profundos:

  * `openclaw://agent?...`


Exemplo (em JS):

jsCopy code
[code]
    window.location.href = "openclaw://agent?message=Review%20this%20design";
[/code]

O app solicita confirmação, a menos que uma chave válida seja fornecida.

## Observações de segurança

  * O esquema do Canvas bloqueia travessia de diretórios; os arquivos devem ficar sob a raiz da sessão.
  * O conteúdo local do Canvas usa um esquema personalizado (nenhum servidor de loopback necessário).
  * URLs externas `http(s)` são permitidas apenas quando navegadas explicitamente.


## Relacionados

  * [app macOS](</pt-BR/platforms/macos>)
  * [WebChat](</pt-BR/web/webchat>)


Was this useful?YesNo