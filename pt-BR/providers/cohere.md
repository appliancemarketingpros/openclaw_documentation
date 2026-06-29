---
title: Cohere
source_url: https://docs.openclaw.ai/pt-BR/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) fornece inferência compatível com OpenAI por meio de sua API de compatibilidade. O OpenClaw distribui o provedor Cohere durante sua transição de externalização e também o publica como um Plugin externo oficial com o catálogo de modelos Command A.

Propriedade | Valor  
---|---  
ID do provedor | `cohere`  
Plugin | incluído durante a transição; pacote externo oficial  
Variável de ambiente de autenticação | `COHERE_API_KEY`  
Flag de onboarding | `--auth-choice cohere-api-key`  
Flag direta da CLI | `--cohere-api-key <key>`  
API | compatível com OpenAI (`openai-completions`)  
URL base | `https://api.cohere.ai/compatibility/v1`  
Modelo padrão | `cohere/command-a-03-2025`  
  
## Comece

  1. O Cohere está incluído nos pacotes atuais do OpenClaw. Se ele não estiver disponível, instale o pacote externo e reinicie o Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Crie uma chave de API da Cohere.
  3. Execute o onboarding:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Confirme que o catálogo está disponível:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

O modelo padrão é definido somente quando nenhum modelo primário já está configurado.

## Configuração somente por ambiente

Disponibilize `COHERE_API_KEY` para o processo do Gateway e então selecione o modelo Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Relacionado

  * [Provedores de modelos](</pt-BR/concepts/model-providers>)
  * [CLI de modelos](</pt-BR/cli/models>)
  * [Diretório de provedores](</pt-BR/providers>)


Was this useful?YesNo

Open issue