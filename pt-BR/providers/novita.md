---
title: NovitaAI
source_url: https://docs.openclaw.ai/pt-BR/providers/novita
scraped_at: 2026-06-29
---

ModelsProviders

NovitaAI é um provedor de infraestrutura de IA hospedada com uma API de modelos compatível com OpenAI. No OpenClaw, ele é um provedor de modelos integrado, então o ID do provedor é `novita`, as credenciais passam pelo fluxo normal de autenticação de modelos, e as referências de modelo se parecem com `novita/deepseek/deepseek-v3-0324`.

Use a Novita quando quiser acesso hospedado a rotas de modelos de pesos abertos e de terceiros sem executar seu próprio servidor de inferência. O catálogo integrado se concentra em modelos de chat práticos para turnos de agente, incluindo rotas DeepSeek, Moonshot, MiniMax, GLM e Qwen expostas pela Novita.

Este provedor usa o endpoint compatível com OpenAI da Novita. O OpenClaw cuida do registro do provedor, autenticação, aliases, normalização de referências de modelo e seleção da URL base; a Novita controla a disponibilidade dos modelos em tempo real, permissões da conta, preços e limites de taxa.

## Configuração

Crie uma chave de API em [novita.ai/settings/key-management](<https://novita.ai/settings/key-management>) e execute:

bashCopy code
[code]
    openclaw onboard --auth-choice novita-api-key
[/code]

Ou defina:

bashCopy code
[code]
    export NOVITA_API_KEY="<your-novita-api-key>" # pragma: allowlist secret
[/code]

## Padrões

  * Provedor: `novita`
  * Aliases: `novita-ai`, `novitaai`
  * URL base: `https://api.novita.ai/openai/v1`
  * Variável de ambiente: `NOVITA_API_KEY`
  * Modelo padrão: `novita/deepseek/deepseek-v3-0324`


## Quando escolher a Novita

  * Você quer acesso hospedado a modelos de pesos abertos com uma API compatível com OpenAI.
  * Você quer rotas das famílias DeepSeek, Kimi, MiniMax, GLM ou Qwen por meio de uma única conta de provedor.
  * Você quer outro caminho de fallback hospedado além de OpenRouter, GMI, DeepInfra ou APIs diretas de fornecedores.
  * Você prefere hospedagem de modelos no lado do provedor em vez de manter infraestrutura vLLM, SGLang, LM Studio ou Ollama.


Escolha um provedor direto do fornecedor quando precisar de parâmetros de solicitação nativos do fornecedor ou contratos de suporte. Escolha um provedor local quando o modelo precisar ser executado no seu próprio hardware ou por trás do seu próprio limite de rede.

## Modelos

O catálogo integrado inicializa IDs de rotas NovitaAI comumente disponíveis, incluindo:

  * `novita/moonshotai/kimi-k2.5`
  * `novita/minimax/minimax-m2.7`
  * `novita/zai-org/glm-5`
  * `novita/deepseek/deepseek-v3-0324`
  * `novita/deepseek/deepseek-r1-0528`
  * `novita/qwen/qwen3-235b-a22b-fp8`


O catálogo é um ponto de partida para a seleção de modelos no OpenClaw. Sua conta, região ou o catálogo atual da Novita pode adicionar, remover ou restringir rotas. Verifique o provedor pela CLI antes de definir um padrão de longa duração:

bashCopy code
[code]
    openclaw models list --provider novita
[/code]

## Solução de problemas

  * `401` ou `403`: verifique a chave na página de gerenciamento de chaves da Novita e execute novamente `openclaw onboard --auth-choice novita-api-key` se o perfil armazenado estiver obsoleto.
  * Erros de modelo desconhecido: use o `novita/<route-id>` exato retornado por `openclaw models list --provider novita`.
  * Rotas lentas ou com falha: tente outra rota de modelo da Novita ou defina a Novita como um provedor de fallback para cargas de trabalho que possam tolerar variação específica do provedor.


## Relacionados

  * [Provedores de modelos](</pt-BR/concepts/model-providers>)
  * [Todos os provedores](</pt-BR/providers>)


Was this useful?YesNo

Open issue