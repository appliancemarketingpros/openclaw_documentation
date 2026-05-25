---
title: Formatação Markdown
source_url: https://docs.openclaw.ai/pt-BR/concepts/markdown-formatting
scraped_at: 2026-05-25
---

OpenClaw formata Markdown de saída convertendo-o em uma representação intermediária compartilhada (IR) antes de renderizar a saída específica de cada canal. A IR mantém o texto de origem intacto enquanto carrega intervalos de estilo/link para que a divisão em partes e a renderização possam permanecer consistentes entre canais.

## Objetivos

  * **Consistência:** uma etapa de análise, vários renderizadores.
  * **Divisão segura em partes:** dividir o texto antes da renderização para que a formatação inline nunca quebre entre partes.
  * **Adequação ao canal:** mapear a mesma IR para mrkdwn do Slack, HTML do Telegram e intervalos de estilo do Signal sem reanalisar o Markdown.


## Pipeline

  1. **Analisar Markdown - > IR**
     * A IR é texto simples mais intervalos de estilo (negrito/itálico/tachado/código/spoiler) e intervalos de link.
     * Os deslocamentos são unidades de código UTF-16 para que os intervalos de estilo do Signal se alinhem com sua API.
     * Tabelas são analisadas somente quando um canal opta pela conversão de tabelas.
  2. **Dividir IR em partes (formatação primeiro)**
     * A divisão em partes acontece no texto da IR antes da renderização.
     * A formatação inline não é dividida entre partes; os intervalos são fatiados por parte.
  3. **Renderizar por canal**
     * **Slack:** tokens mrkdwn (negrito/itálico/tachado/código), links como `<url|label>`.
     * **Telegram:** tags HTML (`<b>`, `<i>`, `<s>`, `<code>`, `<pre><code>`, `<a href>`).
     * **Signal:** texto simples + intervalos `text-style`; links viram `label (url)` quando o rótulo é diferente.


## Exemplo de IR

Markdown de entrada:

markdownCopy code
[code]
    Hello **world** - see [docs](https://docs.openclaw.ai).
[/code]

IR (esquemática):

jsonCopy code
[code]
    {  "text": "Hello world - see docs.",  "styles": [{ "start": 6, "end": 11, "style": "bold" }],  "links": [{ "start": 19, "end": 23, "href": "https://docs.openclaw.ai" }]}
[/code]

## Onde é usada

  * Adaptadores de saída do Slack, Telegram e Signal renderizam a partir da IR.
  * Outros canais (WhatsApp, iMessage, Microsoft Teams, Discord) ainda usam texto simples ou suas próprias regras de formatação, com conversão de tabelas Markdown aplicada antes da divisão em partes quando habilitada.


## Tratamento de tabelas

Tabelas Markdown não têm suporte consistente entre clientes de chat. Use `markdown.tables` para controlar a conversão por canal (e por conta).

  * `code`: renderiza tabelas como blocos de código (padrão para a maioria dos canais).
  * `bullets`: converte cada linha em pontos de lista (padrão para Matrix, Signal e WhatsApp).
  * `off`: desabilita a análise e a conversão de tabelas; o texto bruto da tabela passa adiante.


Chaves de configuração:

yamlCopy code
[code]
    channels:  discord:    markdown:      tables: code    accounts:      work:        markdown:          tables: off
[/code]

## Regras de divisão em partes

  * Os limites de partes vêm dos adaptadores/configuração de canal e são aplicados ao texto da IR.
  * Cercas de código são preservadas como um único bloco com uma nova linha final para que os canais as renderizem corretamente.
  * Prefixos de lista e prefixos de citação em bloco fazem parte do texto da IR, então a divisão em partes não ocorre no meio do prefixo.
  * Estilos inline (negrito/itálico/tachado/código-inline/spoiler) nunca são divididos entre partes; o renderizador reabre estilos dentro de cada parte.


Se precisar de mais informações sobre o comportamento de divisão em partes entre canais, consulte [Streaming + divisão em partes](</pt-BR/concepts/streaming>).

## Política de links

  * **Slack:** `[label](url)` -> `<url|label>`; URLs sem formatação permanecem sem formatação. Autolink é desabilitado durante a análise para evitar links duplicados.
  * **Telegram:** `[label](url)` -> `<a href="url">label</a>` (modo de análise HTML).
  * **Signal:** `[label](url)` -> `label (url)`, a menos que o rótulo corresponda à URL.


## Spoilers

Marcadores de spoiler (`||spoiler||`) são analisados somente para o Signal, onde são mapeados para intervalos de estilo SPOILER. Outros canais os tratam como texto simples.

## Como adicionar ou atualizar um formatador de canal

  1. **Analisar uma vez:** use o helper compartilhado `markdownToIR(...)` com opções apropriadas ao canal (autolink, estilo de cabeçalho, prefixo de citação em bloco).
  2. **Renderizar:** implemente um renderizador com `renderMarkdownWithMarkers(...)` e um mapa de marcadores de estilo (ou intervalos de estilo do Signal).
  3. **Dividir em partes:** chame `chunkMarkdownIR(...)` antes de renderizar; renderize cada parte.
  4. **Conectar o adaptador:** atualize o adaptador de saída do canal para usar o novo divisor em partes e renderizador.
  5. **Testar:** adicione ou atualize testes de formatação e um teste de entrega de saída se o canal usar divisão em partes.


## Problemas comuns

  * Tokens entre sinais de menor/maior do Slack (`<@U123>`, `<#C123>`, `<https://...>`) devem ser preservados; escape HTML bruto com segurança.
  * HTML do Telegram exige escape de texto fora das tags para evitar marcação quebrada.
  * Intervalos de estilo do Signal dependem de deslocamentos UTF-16; não use deslocamentos de pontos de código.
  * Preserve novas linhas finais para blocos de código cercados para que os marcadores de fechamento fiquem em sua própria linha.


## Relacionados

[**Streaming e divisão em partes** Comportamento de streaming de saída, limites de partes e entrega específica por canal. ](</pt-BR/concepts/streaming>) [**Prompt do sistema** O que o modelo vê antes da conversa, incluindo arquivos de workspace injetados. ](</pt-BR/concepts/system-prompt>)

Was this useful?YesNo