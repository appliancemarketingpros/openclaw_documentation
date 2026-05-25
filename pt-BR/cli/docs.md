---
title: Documentação
source_url: https://docs.openclaw.ai/pt-BR/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

Pesquise o índice de documentação ao vivo do OpenClaw pelo terminal. O comando chama o endpoint público de busca MCP da documentação hospedada no Mintlify em `https://docs.openclaw.ai/mcp.SearchOpenClaw` e exibe os resultados no seu terminal.

## Uso

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

Argumentos:

Argumento | Descrição  
---|---  
`[query...]` | Consulta de busca em formato livre. Consultas com várias palavras são unidas com espaços e enviadas como uma só.  
  
## Exemplos

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

Sem consulta, `openclaw docs` imprime a URL do ponto de entrada da documentação mais um exemplo de comando de busca, em vez de executar uma busca.

## Como funciona

`openclaw docs` invoca a CLI `mcporter` para chamar a ferramenta MCP de busca da documentação e, em seguida, analisa os blocos `Title: / Link: / Content:` da saída da ferramenta em uma lista de resultados.

Para resolver `mcporter`, o OpenClaw verifica na ordem:

  1. `mcporter` no `PATH` (usado diretamente se estiver presente).
  2. `pnpm dlx mcporter ...` se `pnpm` estiver instalado.
  3. `npx -y mcporter ...` se `npx` estiver instalado.


Se nenhum estiver disponível, o comando falha com uma dica para instalar `pnpm` (`npm install -g pnpm`).

A chamada de busca usa um tempo limite fixo de 30 segundos. Os trechos dos resultados são truncados para cerca de 220 caracteres por entrada.

## Saída

Em um terminal avançado (TTY), os resultados são exibidos como um título seguido por uma lista com marcadores. Cada marcador mostra o título da página, a URL vinculada da documentação e um trecho curto na linha seguinte. Resultados vazios imprimem "Nenhum resultado.".

Em saída sem recursos avançados (redirecionada por pipe, `--no-color`, scripts), os mesmos dados são exibidos como Markdown:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## Códigos de saída

Código | Significado  
---|---  
`0` | A busca foi bem-sucedida (incluindo respostas sem resultados).  
`1` | A chamada da ferramenta MCP falhou; a saída de erro padrão é impressa em linha.  
  
## Relacionados

  * [Referência da CLI](</pt-BR/cli>)
  * [Documentação ao vivo](<https://docs.openclaw.ai>)


Was this useful?YesNo