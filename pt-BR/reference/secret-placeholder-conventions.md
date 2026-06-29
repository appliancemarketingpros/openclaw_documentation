---
title: Convenções de espaços reservados de segredos
source_url: https://docs.openclaw.ai/pt-BR/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Convenções de placeholders de segredos

Use placeholders que sejam legíveis por humanos, mas que não pareçam segredos reais.

## Estilo recomendado

  * Prefira valores descritivos como `example-openai-key-not-real` ou `example-discord-bot-token`.
  * Para trechos de shell, prefira `${OPENAI_API_KEY}` em vez de strings inline que pareçam tokens.
  * Mantenha os exemplos obviamente falsos e restritos ao propósito (provedor, canal, tipo de autenticação).


## Evite estes padrões na documentação

  * Texto literal de cabeçalho ou rodapé de chave privada PEM.
  * Prefixos que pareçam credenciais ativas, por exemplo `sk-...`, `xoxb-...`, `AKIA...`.
  * Tokens bearer com aparência realista copiados de logs de runtime.


## Exemplo

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue