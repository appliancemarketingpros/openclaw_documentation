---
title: Gateway de IA da Cloudflare
source_url: https://docs.openclaw.ai/pt-BR/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway fica na frente das APIs dos provedores e permite adicionar análises, cache e controles. Para a Anthropic, o OpenClaw usa a API Anthropic Messages por meio do endpoint do seu Gateway.

Propriedade | Valor  
---|---  
Provedor | `cloudflare-ai-gateway`  
URL base | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Modelo padrão | `cloudflare-ai-gateway/claude-sonnet-4-6`  
Chave de API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (sua chave de API do provedor para solicitações pelo Gateway)  
  
Quando o raciocínio está ativado para modelos Anthropic Messages, o OpenClaw remove turnos finais de pré-preenchimento do assistente antes de enviar a carga útil pelo Cloudflare AI Gateway. A Anthropic rejeita o pré-preenchimento de respostas com raciocínio estendido, enquanto o pré-preenchimento comum sem raciocínio permanece disponível.

## Primeiros passos

* ### Defina a chave de API do provedor e os detalhes do Gateway

Execute a integração inicial e escolha a opção de autenticação do Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Isso solicita seu ID da conta, ID do Gateway e chave de API.

* ### Defina um modelo padrão

Adicione o modelo à configuração do OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Verifique se o modelo está disponível

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Exemplo não interativo

Para configurações com script ou CI, passe todos os valores na linha de comando:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Configuração avançada

Gateways autenticados

Se você habilitou a autenticação do Gateway no Cloudflare, adicione o cabeçalho `cf-aig-authorization`. Isso é **além da** sua chave de API do provedor.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Observação sobre o ambiente

Se o Gateway for executado como um daemon (launchd/systemd), garanta que `CLOUDFLARE_AI_GATEWAY_API_KEY` esteja disponível para esse processo.

## Relacionado

[**Seleção de modelo** Escolha de provedores, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Solução de problemas** Solução de problemas geral e perguntas frequentes. ](</pt-BR/help/troubleshooting>)

Was this useful?YesNo