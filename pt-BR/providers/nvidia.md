---
title: NVIDIA
source_url: https://docs.openclaw.ai/pt-BR/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA fornece uma API compatível com OpenAI em `https://integrate.api.nvidia.com/v1` para modelos abertos gratuitamente. Autentique-se com uma chave de API de [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Primeiros passos

* ### Obtenha sua chave de API

Crie uma chave de API em [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Exporte a chave e execute o onboarding

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Defina um modelo NVIDIA

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Para configuração não interativa, você também pode passar a chave diretamente:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Exemplo de configuração

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Catálogo integrado

Ref do modelo | Nome | Contexto | Saída máxima  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Configuração avançada

Comportamento de ativação automática

O provedor é ativado automaticamente quando a variável de ambiente `NVIDIA_API_KEY` está definida. Nenhuma configuração explícita de provedor é necessária além da chave.

Catálogo e preços

O catálogo incluído é estático. Os custos têm valor padrão `0` no código-fonte, pois a NVIDIA atualmente oferece acesso gratuito à API para os modelos listados.

Endpoint compatível com OpenAI

A NVIDIA usa o endpoint de completions padrão `/v1`. Qualquer ferramenta compatível com OpenAI deve funcionar imediatamente com a URL base da NVIDIA.

Respostas lentas de provedores personalizados

Alguns modelos personalizados hospedados pela NVIDIA podem demorar mais que o watchdog de ociosidade padrão do modelo antes de emitirem o primeiro bloco de resposta. Para entradas personalizadas de provedor NVIDIA, aumente o tempo limite do provedor em vez de aumentar o tempo limite de runtime de todo o agente:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Relacionados

[**Seleção de modelos** Escolha de provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Referência completa de configuração para agentes, modelos e provedores. ](</pt-BR/gateway/configuration-reference>)

Was this useful?YesNo