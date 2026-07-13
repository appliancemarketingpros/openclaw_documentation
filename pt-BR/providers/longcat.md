---
title: LongCat
source_url: https://docs.openclaw.ai/pt-BR/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

O [LongCat](<https://longcat.ai>) fornece uma API hospedada para o LongCat-2.0, um modelo de raciocínio desenvolvido para programação e cargas de trabalho agênticas. O OpenClaw fornece o plugin oficial `longcat` para o endpoint compatível com OpenAI do LongCat.

Propriedade | Valor  
---|---  
Provedor | `longcat`  
Autenticação | `LONGCAT_API_KEY`  
API | Chat Completions compatível com OpenAI  
URL base | `https://api.longcat.chat/openai`  
Modelo | `longcat/LongCat-2.0`  
Contexto | 1.048.576 tokens  
Saída máxima | 131.072 tokens  
Entrada | Texto  
  
## Instalar o plugin

Instale o pacote oficial e reinicie o Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Primeiros passos

* ### Criar uma chave de API

Entre na [Plataforma de API do LongCat](<https://longcat.chat/platform/>) e crie uma chave na página [API Keys](<https://longcat.chat/platform/api_keys>).

* ### Executar a integração inicial

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Verificar o modelo

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

A integração inicial adiciona o catálogo hospedado e seleciona `longcat/LongCat-2.0` quando nenhum modelo principal já está configurado.

### Configuração não interativa

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Comportamento do raciocínio

O LongCat oferece controle binário do pensamento. O OpenClaw mapeia os níveis de pensamento ativados para `thinking: { type: "enabled" }` e `/think off` para `thinking: { type: "disabled" }`. Atualmente, o LongCat não documenta `reasoning_effort`, portanto o OpenClaw não o envia.

O LongCat retorna o raciocínio em `reasoning_content`. O OpenClaw preserva esse campo ao reproduzir turnos de chamada de ferramenta do assistente, para que sessões agênticas com vários turnos mantenham o formato de mensagem esperado pelo provedor.

## Preços

O catálogo integrado usa os preços de tabela do LongCat no modelo de pagamento conforme o uso, em USD por milhão de tokens: US$ 0,75 por entrada sem cache, US$ 0,015 por entrada em cache e US$ 2,95 por saída. O LongCat pode oferecer descontos temporários; a [página de preços](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) e seus registros de cobrança são as fontes oficiais.

## LongCat-2.0 auto-hospedado

O provedor `longcat` é destinado à API hospedada do LongCat. Para usar os pesos abertos no [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>), disponibilize o modelo por meio de um runtime compatível com OpenAI e use o provedor [vLLM](</pt-BR/providers/vllm>) ou [SGLang](</pt-BR/providers/sglang>) existente do OpenClaw.

Mantenha o identificador exato do modelo no catálogo do provedor auto-hospedado; não encaminhe uma implantação local por meio de `longcat/LongCat-2.0`.

## Solução de problemas

A chave funciona em um shell, mas não no Gateway

Os processos do Gateway gerenciados por daemon não herdam todas as variáveis do shell interativo. Coloque `LONGCAT_API_KEY` em `~/.openclaw/.env`, configure-a por meio da integração inicial ou use uma referência de segredo aprovada.

As solicitações falham com 402 ou 429

`402` significa que a conta não tem cota de tokens suficiente. `429` significa que a chave de API atingiu um limite de taxa. Verifique o [uso do LongCat](<https://longcat.chat/platform/usage>) e tente novamente as solicitações limitadas por taxa após o período de espera do provedor.

O modelo não aparece

Execute `openclaw plugins list` e confirme se o plugin `longcat` está ativado; depois, execute `openclaw models list --provider longcat`.

## Relacionados

[**Provedores de modelos** Configuração de provedores, referências de modelos e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Documentação da API do LongCat** Endpoints da API hospedada, autenticação, limites e exemplos. ](<https://longcat.chat/platform/docs/>) [**Ficha do modelo LongCat-2.0** Arquitetura, orientações de implantação e detalhes do modelo. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Segredos** Armazene as credenciais do provedor sem incorporar texto simples à configuração. ](</pt-BR/gateway/secrets>)

Was this useful?YesNo

Open issue