---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/pt-BR/providers/tencent
scraped_at: 2026-05-25
---

O Tencent Cloud é distribuído como um Plugin de provedor incluído no OpenClaw. Ele fornece acesso ao Tencent Hy3 preview pelo endpoint TokenHub (`tencent-tokenhub`) usando uma API compatível com OpenAI.

Propriedade | Valor  
---|---  
ID do provedor | `tencent-tokenhub`  
Plugin | incluído, `enabledByDefault: true`  
Var. env. de auth | `TOKENHUB_API_KEY`  
Flag de onboarding | `--auth-choice tokenhub-api-key`  
Flag direta da CLI | `--tokenhub-api-key <key>`  
API | compatível com OpenAI (`openai-completions`)  
URL base padrão | `https://tokenhub.tencentmaas.com/v1`  
URL base global | `https://tokenhub-intl.tencentmaas.com/v1` (substituição)  
Modelo padrão | `tencent-tokenhub/hy3-preview`  
  
## Início rápido

* ### Crie uma chave de API do TokenHub

Crie uma chave de API no Tencent Cloud TokenHub. Se escolher um escopo de acesso limitado para a chave, inclua **Hy3 preview** nos modelos permitidos.

* ### Execute o onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Flag diretaCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Somente envCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Verifique o modelo

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Configuração não interativa

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catálogo integrado

Ref do modelo | Nome | Entrada | Contexto | Saída máxima | Observações  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | texto | 256.000 | 64.000 | Padrão; com raciocínio habilitado  
  
Hy3 preview é o grande modelo de linguagem MoE Tencent Hunyuan para raciocínio, acompanhamento de instruções com contexto longo, código e fluxos de trabalho de agente. Os exemplos compatíveis com OpenAI da Tencent usam `hy3-preview` como ID do modelo e oferecem suporte a chamadas de ferramentas padrão de chat-completions, além de `reasoning_effort`.

## Preços em camadas

O catálogo incluído traz metadados de custo em camadas que escalam com o tamanho da janela de entrada, para que as estimativas de custo sejam preenchidas sem substituições manuais.

Intervalo de tokens de entrada | Taxa de entrada | Taxa de saída | Leitura do cache  
---|---|---|---  
0 - 16.000 | 0,176 | 0,587 | 0,059  
16.000 - 32.000 | 0,235 | 0,939 | 0,088  
32.000+ | 0,293 | 1,173 | 0,117  
  
As taxas são por milhão de tokens em USD, conforme anunciado pela Tencent. Substitua os preços em `models.providers.tencent-tokenhub` somente quando precisar de uma superfície diferente.

## Configuração avançada

Substituição do endpoint

O OpenClaw usa por padrão o endpoint `https://tokenhub.tencentmaas.com/v1` do Tencent Cloud. A Tencent também documenta um endpoint internacional do TokenHub:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Substitua o endpoint somente quando sua conta ou região do TokenHub exigir.

Disponibilidade do ambiente para o daemon

Se o Gateway for executado como um serviço gerenciado (launchd, systemd, Docker), `TOKENHUB_API_KEY` deve estar visível para esse processo. Defina-o em `~/.openclaw/.env` ou via `env.shellEnv` para que ambientes launchd, systemd ou Docker exec possam lê-lo.

## Relacionados

[**Provedores de modelos** Escolha de provedores, refs de modelos e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Esquema de configuração completo, incluindo configurações de provedor. ](</pt-BR/gateway/configuration>) [**Tencent TokenHub** Página do produto TokenHub do Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**Card do modelo Hy3 preview** Detalhes e benchmarks do Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo