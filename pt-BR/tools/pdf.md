---
title: Ferramenta de PDF
source_url: https://docs.openclaw.ai/pt-BR/tools/pdf
scraped_at: 2026-05-25
---

`pdf` analisa um ou mais documentos PDF e retorna texto.

Comportamento rápido:

  * Modo de provedor nativo para provedores de modelo Anthropic e Google.
  * Modo de fallback de extração para outros provedores (extrai texto primeiro e, depois, imagens das páginas quando necessário).
  * Compatível com entrada única (`pdf`) ou múltipla (`pdfs`), com máximo de 10 PDFs por chamada.


## Disponibilidade

A ferramenta só é registrada quando o OpenClaw consegue resolver uma configuração de modelo compatível com PDF para o agente:

  1. `agents.defaults.pdfModel`
  2. fallback para `agents.defaults.imageModel`
  3. fallback para o modelo resolvido de sessão/padrão do agente
  4. se provedores com PDF nativo forem baseados em autenticação, preferi-los antes de candidatos genéricos de fallback de imagem


Se nenhum modelo utilizável puder ser resolvido, a ferramenta `pdf` não é exposta.

Observações de disponibilidade:

  * A cadeia de fallback considera autenticação. Um `provider/model` configurado só conta se o OpenClaw realmente conseguir autenticar esse provedor para o agente.
  * Provedores de PDF nativo atualmente são **Anthropic** e **Google**.
  * Se o provedor resolvido de sessão/padrão já tiver um modelo de visão/PDF configurado, a ferramenta PDF o reutiliza antes de recorrer a outros provedores baseados em autenticação.


## Referência de entrada

Um caminho ou URL de PDF.

Vários caminhos ou URLs de PDF, até 10 no total.

Prompt de análise.

Filtro de páginas como `1-5` ou `1,3,7-9`.

Substituição opcional de modelo no formato `provider/model`.

Limite de tamanho por PDF em MB. O padrão é `agents.defaults.pdfMaxBytesMb` ou `10`.

Observações de entrada:

  * `pdf` e `pdfs` são mesclados e deduplicados antes do carregamento.
  * Se nenhuma entrada de PDF for fornecida, a ferramenta retorna erro.
  * `pages` é interpretado como números de página começando em 1, deduplicado, ordenado e limitado ao máximo de páginas configurado.
  * `maxBytesMb` usa como padrão `agents.defaults.pdfMaxBytesMb` ou `10`.


## Referências de PDF compatíveis

  * caminho de arquivo local (incluindo expansão de `~`)
  * URL `file://`
  * URL `http://` e `https://`
  * refs de entrada gerenciadas pelo OpenClaw, como `media://inbound/<id>`


Observações sobre referências:

  * Outros esquemas de URI (por exemplo, `ftp://`) são rejeitados com `unsupported_pdf_reference`.
  * No modo sandbox, URLs remotos `http(s)` são rejeitados.
  * Com a política de arquivos somente no workspace ativada, caminhos de arquivos locais fora das raízes permitidas são rejeitados.
  * Refs de entrada gerenciadas e caminhos reproduzidos no armazenamento de mídia de entrada do OpenClaw são permitidos com a política de arquivos somente no workspace.


## Modos de execução

### Modo de provedor nativo

O modo nativo é usado para os provedores `anthropic` e `google`. A ferramenta envia bytes brutos de PDF diretamente para as APIs do provedor.

Limites do modo nativo:

  * `pages` não é compatível. Se definido, a ferramenta retorna um erro.
  * Entrada com múltiplos PDFs é compatível; cada PDF é enviado como um bloco de documento nativo / parte de PDF inline antes do prompt.


### Modo de fallback de extração

O modo de fallback é usado para provedores não nativos.

Fluxo:

  1. Extrair texto das páginas selecionadas (até `agents.defaults.pdfMaxPages`, padrão `20`).
  2. Se o comprimento do texto extraído for inferior a `200` caracteres, renderizar as páginas selecionadas como imagens PNG e incluí-las.
  3. Enviar o conteúdo extraído mais o prompt para o modelo selecionado.


Detalhes do fallback:

  * A extração de imagem de página usa um orçamento de pixels de `4,000,000`.
  * Se o modelo de destino não oferecer suporte a entrada de imagem e não houver texto extraível, a ferramenta retorna erro.
  * Se a extração de texto tiver sucesso, mas a extração de imagem exigiria visão em um modelo somente texto, o OpenClaw descarta as imagens renderizadas e continua com o texto extraído.
  * O fallback de extração usa o Plugin `document-extract` incluído. O Plugin é responsável por `pdfjs-dist`; `@napi-rs/canvas` é usado somente quando o fallback de renderização de imagem está disponível.


## Configuração

json5Copy code
[code]
    {  agents: {    defaults: {      pdfModel: {        primary: "anthropic/claude-opus-4-6",        fallbacks: ["openai/gpt-5.4-mini"],      },      pdfMaxBytesMb: 10,      pdfMaxPages: 20,    },  },}
[/code]

Consulte a [Referência de configuração](</pt-BR/gateway/configuration-reference>) para detalhes completos dos campos.

## Detalhes da saída

A ferramenta retorna texto em `content[0].text` e metadados estruturados em `details`.

Campos comuns de `details`:

  * `model`: ref de modelo resolvida (`provider/model`)
  * `native`: `true` para modo de provedor nativo, `false` para fallback
  * `attempts`: tentativas de fallback que falharam antes do sucesso


Campos de caminho:

  * entrada de PDF único: `details.pdf`
  * entradas de múltiplos PDFs: `details.pdfs[]` com entradas `pdf`
  * metadados de reescrita de caminho no sandbox (quando aplicável): `rewrittenFrom`


## Comportamento de erro

  * Entrada de PDF ausente: lança `pdf required: provide a path or URL to a PDF document`
  * PDFs em excesso: retorna erro estruturado em `details.error = "too_many_pdfs"`
  * Esquema de referência incompatível: retorna `details.error = "unsupported_pdf_reference"`
  * Modo nativo com `pages`: lança erro claro `pages is not supported with native PDF providers`


## Exemplos

PDF único:

jsonCopy code
[code]
    {  "pdf": "/tmp/report.pdf",  "prompt": "Summarize this report in 5 bullets"}
[/code]

Múltiplos PDFs:

jsonCopy code
[code]
    {  "pdfs": ["/tmp/q1.pdf", "/tmp/q2.pdf"],  "prompt": "Compare risks and timeline changes across both documents"}
[/code]

Modelo de fallback com filtro de páginas:

jsonCopy code
[code]
    {  "pdf": "https://example.com/report.pdf",  "pages": "1-3,7",  "model": "openai/gpt-5.4-mini",  "prompt": "Extract only customer-impacting incidents"}
[/code]

## Relacionado

  * [Visão geral das ferramentas](</pt-BR/tools>) \- todas as ferramentas de agente disponíveis
  * [Referência de configuração](</pt-BR/gateway/config-agents#agent-defaults>) \- configuração de pdfMaxBytesMb e pdfMaxPages


Was this useful?YesNo