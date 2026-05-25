---
title: Protocolo de saída rica
source_url: https://docs.openclaw.ai/pt-BR/reference/rich-output-protocol
scraped_at: 2026-05-25
---

A saída do assistente pode carregar um pequeno conjunto de diretivas de entrega/renderização:

  * `MEDIA:` para entrega de anexos
  * `[[audio_as_voice]]` para dicas de apresentação de áudio
  * `[[reply_to_current]]` / `[[reply_to:<id>]]` para metadados de resposta
  * `[embed ...]` para renderização rica da UI de controle


Anexos `MEDIA:` remotos devem ser URLs `https:` públicas. `http:` puro, loopback, link-local, nomes de host privados e internos são ignorados como diretivas de anexo; buscadores de mídia do lado do servidor ainda aplicam suas próprias proteções de rede.

Anexos `MEDIA:` locais podem usar caminhos absolutos, caminhos relativos ao workspace ou caminhos relativos à home `~/`. Eles ainda passam pela política de leitura de arquivos do agente e por verificações de tipo de mídia antes da entrega.

A sintaxe Markdown simples de imagem permanece como texto por padrão. Canais que intencionalmente mapeiam respostas de imagem Markdown para anexos de mídia aderem a isso em seu adaptador de saída; o Telegram faz isso para que `![alt](url)` ainda possa se tornar uma resposta de mídia.

Essas diretivas são separadas. `MEDIA:` e tags de resposta/voz permanecem como metadados de entrega; `[embed ...]` é o caminho de renderização rica exclusivo da web. Mídia confiável de resultado de ferramenta usa o mesmo parser `MEDIA:` / `[[audio_as_voice]]` antes da entrega, então saídas de texto de ferramentas ainda podem marcar um anexo de áudio como nota de voz.

Quando streaming em blocos está habilitado, `MEDIA:` permanece como metadado de entrega única para um turno. Se a mesma URL de mídia for enviada em um bloco transmitido em streaming e repetida no payload final do assistente, o OpenClaw entrega o anexo uma vez e remove a duplicata do payload final.

## `[embed ...]`

`[embed ...]` é a única sintaxe de renderização rica voltada para agentes para a UI de controle.

Exemplo autofechado:

textCopy code
[code]
    [embed ref="cv_123" title="Status" /]
[/code]

Regras:

  * `[view ...]` não é mais válido para novas saídas.
  * Shortcodes de embed são renderizados apenas na superfície de mensagem do assistente.
  * Apenas embeds baseados em URL são renderizados. Use `ref="..."` ou `url="..."`.
  * Shortcodes de embed HTML inline em forma de bloco não são renderizados.
  * A UI web remove o shortcode do texto visível e renderiza o embed inline.
  * `MEDIA:` não é um alias de embed e não deve ser usado para renderização rica de embed.


## Formato de renderização armazenado

O bloco normalizado/armazenado de conteúdo do assistente é um item estruturado `canvas`:

jsonCopy code
[code]
    {  "type": "canvas",  "preview": {    "kind": "canvas",    "surface": "assistant_message",    "render": "url",    "viewId": "cv_123",    "url": "/__openclaw__/canvas/documents/cv_123/index.html",    "title": "Status",    "preferredHeight": 320  }}
[/code]

Blocos ricos armazenados/renderizados usam esse formato `canvas` diretamente. `present_view` não é reconhecido.

## Relacionado

  * [Adaptadores RPC](</pt-BR/reference/rpc>)
  * [Typebox](</pt-BR/concepts/typebox>)


Was this useful?YesNo