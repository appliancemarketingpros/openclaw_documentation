---
title: Qwen OAuth / Portal
source_url: https://docs.openclaw.ai/pt-BR/providers/qwen-oauth
scraped_at: 2026-06-29
---

ModelsProviders

`qwen-oauth` é o id do provedor Qwen Portal. Ele direciona para o endpoint do Qwen Portal e mantém configurações antigas do Qwen OAuth / portal endereçáveis por meio de um id de provedor distinto.

Use este provedor quando você tiver especificamente um token atual do Qwen Portal para `https://portal.qwen.ai/v1`, ou quando estiver migrando uma configuração mais antiga do Qwen Portal / Qwen CLI e quiser manter essas credenciais separadas do provedor canônico Qwen Cloud. Ele não é a primeira opção recomendada para novos usuários do Qwen.

Para novas configurações do Qwen Cloud, prefira [Qwen](</pt-BR/providers/qwen>) com o endpoint Standard do ModelStudio, a menos que você tenha especificamente um token atual do Qwen Portal.

## Configuração

Forneça seu token do portal durante o onboarding:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-oauth
[/code]

Ou defina:

bashCopy code
[code]
    export QWEN_API_KEY="<your-qwen-portal-token>" # pragma: allowlist secret
[/code]

## Padrões

  * Provedor: `qwen-oauth`
  * Aliases: `qwen-portal`, `qwen-cli`
  * URL base: `https://portal.qwen.ai/v1`
  * Var. de ambiente: `QWEN_API_KEY`
  * Estilo da API: compatível com OpenAI
  * Modelo padrão: `qwen-oauth/qwen3.5-plus`


## Como isso difere do Qwen

O OpenClaw tem dois ids de provedor voltados ao Qwen:

Provedor | Família de endpoints | Ideal para  
---|---|---  
`qwen` | Endpoints Qwen Cloud / Alibaba DashScope e Coding Plan | Novas configurações com chave de API, Standard pago conforme o uso, Coding Plan, recursos multimodais do DashScope  
`qwen-oauth` | Endpoint Qwen Portal em `portal.qwen.ai/v1` | Tokens existentes do Qwen Portal e configurações legadas do Qwen OAuth / CLI  
  
Ambos os provedores usam formatos de solicitação compatíveis com OpenAI, mas são superfícies de autenticação separadas. Um token armazenado para `qwen-oauth` não deve ser tratado como uma chave DashScope ou ModelStudio, e uma nova chave DashScope deve usar o provedor canônico `qwen` em vez disso.

## Quando escolher Qwen OAuth / Portal

  * Você já tem um token funcional do Qwen Portal.
  * Você está preservando um fluxo de trabalho legado do Qwen OAuth ou Qwen CLI enquanto migra para o modelo de provedores do OpenClaw.
  * Você precisa testar compatibilidade especificamente com o endpoint do Qwen Portal.


Escolha [Qwen](</pt-BR/providers/qwen>) para nova configuração, opções mais amplas de endpoints, Standard ModelStudio, Coding Plan e o catálogo completo de plugins do Qwen.

## Modelos

O catálogo do plugin Qwen define o padrão do Qwen Portal:

  * `qwen-oauth/qwen3.5-plus`


A disponibilidade depende da conta e do token atuais do Qwen Portal. Se sua conta usa chaves de API ModelStudio / DashScope, configure o provedor canônico `qwen`:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-keyopenclaw models set qwen/qwen3-coder-plus
[/code]

## Migração

Perfis legados do Qwen Portal OAuth podem não ser atualizáveis. Se um perfil do portal parar de funcionar, autentique novamente com um token atual ou mude para o provedor Standard do Qwen:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

O ModelStudio global Standard usa:

textCopy code
[code]
    https://dashscope-intl.aliyuncs.com/compatible-mode/v1
[/code]

## Solução de problemas

  * Falhas de atualização do Portal OAuth: perfis legados do Qwen Portal OAuth podem não ser atualizáveis. Execute o onboarding novamente com um token atual.
  * Erros de endpoint incorreto: confirme que a referência do modelo começa com `qwen-oauth/` ao usar um token do portal. Use referências `qwen/` somente para o provedor canônico Qwen.
  * Confusão com `QWEN_API_KEY`: ambas as páginas do Qwen mencionam essa var. de ambiente, mas o onboarding armazena credenciais sob o id do provedor selecionado. Prefira o onboarding quando você mantiver `qwen` e `qwen-oauth` disponíveis na mesma máquina.


## Relacionados

  * [Qwen](</pt-BR/providers/qwen>)
  * [Alibaba Model Studio](</pt-BR/providers/alibaba>)
  * [Provedores de modelo](</pt-BR/concepts/model-providers>)
  * [Todos os provedores](</pt-BR/providers>)


Was this useful?YesNo

Open issue