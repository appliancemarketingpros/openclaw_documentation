---
title: Together AI
source_url: https://docs.openclaw.ai/pt-BR/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) fornece acesso a modelos open-source líderes, incluindo Llama, DeepSeek, Kimi e outros, por meio de uma API unificada.

Propriedade | Valor  
---|---  
Provedor | `together`  
Autenticação | `TOGETHER_API_KEY`  
API | compatível com OpenAI  
URL base | `https://api.together.xyz/v1`  
  
## Introdução

* ### Obtenha uma chave de API

Crie uma chave de API em [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Defina um modelo padrão

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Exemplo não interativo

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Catálogo integrado

O OpenClaw inclui este catálogo Together integrado:

Ref. do modelo | Nome | Entrada | Contexto | Observações  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | texto, imagem | 262,144 | Modelo padrão; raciocínio habilitado  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | texto | 202,752 | Modelo de texto de uso geral  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | texto | 131,072 | Modelo rápido para instruções  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | texto, imagem | 10,000,000 | Multimodal  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | texto, imagem | 20,000,000 | Multimodal  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | texto | 131,072 | Modelo de texto geral  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | texto | 131,072 | Modelo de raciocínio  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | texto | 262,144 | Modelo de texto Kimi secundário  
  
## Geração de vídeo

O Plugin `together` integrado também registra geração de vídeo por meio da ferramenta compartilhada `video_generate`.

Propriedade | Valor  
---|---  
Modelo de vídeo padrão | `together/Wan-AI/Wan2.2-T2V-A14B`  
Modos | texto para vídeo, referência de imagem única  
Parâmetros compatíveis | `aspectRatio`, `resolution`  
  
Para usar o Together como provedor de vídeo padrão:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Observação sobre o ambiente

Se o Gateway for executado como um daemon (launchd/systemd), garanta que `TOGETHER_API_KEY` esteja disponível para esse processo (por exemplo, em `~/.openclaw/.env` ou via `env.shellEnv`).

Solução de problemas

  * Verifique se sua chave funciona: `openclaw models list --provider together`
  * Se os modelos não aparecerem, confirme que a chave de API está definida no ambiente correto para o processo do seu Gateway.
  * Refs. de modelo usam o formato `together/<model-id>`.


## Relacionados

[**Seleção de modelo** Regras de provedor, refs. de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Geração de vídeo** Parâmetros da ferramenta compartilhada de geração de vídeo e seleção de provedor. ](</pt-BR/tools/video-generation>) [**Referência de configuração** Esquema de configuração completo, incluindo configurações de provedor. ](</pt-BR/gateway/configuration-reference>) [**Together AI** Painel do Together AI, documentação da API e preços. ](<https://together.ai>)

Was this useful?YesNo