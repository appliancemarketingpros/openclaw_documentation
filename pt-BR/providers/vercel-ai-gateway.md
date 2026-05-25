---
title: Gateway de IA da Vercel
source_url: https://docs.openclaw.ai/pt-BR/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

O [Vercel AI Gateway](<https://vercel.com/ai-gateway>) fornece uma API unificada para acessar centenas de modelos por meio de um único endpoint.

Propriedade | Valor  
---|---  
Provedor | `vercel-ai-gateway`  
Autenticação | `AI_GATEWAY_API_KEY`  
API | compatível com Anthropic Messages  
Catálogo de modelos | Descoberto automaticamente via `/v1/models`  
  
## Primeiros passos

* ### Defina a chave de API

Execute o onboarding e escolha a opção de autenticação do AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Defina um modelo padrão

Adicione o modelo à sua configuração do OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Verifique se o modelo está disponível

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Exemplo não interativo

Para configurações com scripts ou em CI, passe todos os valores na linha de comando:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Abreviação de ID de modelo

O OpenClaw aceita refs abreviadas de modelos Claude da Vercel e as normaliza em tempo de execução:

Entrada abreviada | Ref de modelo normalizada  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Configuração avançada

Variável de ambiente para processos daemon

Se o OpenClaw Gateway for executado como daemon (launchd/systemd), garanta que `AI_GATEWAY_API_KEY` esteja disponível para esse processo.

Roteamento de provedor

O Vercel AI Gateway roteia solicitações para o provedor upstream com base no prefixo da ref de modelo. Por exemplo, `vercel-ai-gateway/anthropic/claude-opus-4.6` roteia via Anthropic, enquanto `vercel-ai-gateway/openai/gpt-5.5` roteia via OpenAI e `vercel-ai-gateway/moonshotai/kimi-k2.6` roteia via MoonshotAI. Sua única `AI_GATEWAY_API_KEY` lida com a autenticação para todos os provedores upstream.

Níveis de pensamento

As opções de `/think` seguem prefixos de modelos upstream confiáveis quando o OpenClaw conhece o contrato do provedor upstream. `vercel-ai-gateway/anthropic/...` usa o perfil de pensamento do Claude, incluindo padrões adaptativos para modelos Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` e refs no estilo Codex expõem `/think xhigh` assim como os provedores diretos OpenAI/OpenAI Codex. Outras refs com namespace mantêm os níveis normais de raciocínio, a menos que os metadados do catálogo declarem mais.

## Relacionado

[**Seleção de modelos** Escolha de provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Solução de problemas** Solução de problemas geral e FAQ. ](</pt-BR/help/troubleshooting>)

Was this useful?YesNo