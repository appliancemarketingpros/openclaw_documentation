---
title: SecretRefs do cofre
source_url: https://docs.openclaw.ai/pt-BR/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# SecretRefs do Vault

O plugin Vault incluído permite que o OpenClaw resolva SecretRefs de `exec` do HashiCorp Vault na inicialização e no recarregamento do Gateway. O OpenClaw armazena referências do Vault na configuração, mantém os valores resolvidos no snapshot de segredos em memória e não grava as chaves de API resolvidas de volta no `openclaw.json`.

Use isso quando você já utiliza o Vault ou deseja manter as chaves dos provedores de modelos fora dos arquivos de configuração do OpenClaw. Para conhecer o modelo de runtime do SecretRef, consulte [Gerenciamento de segredos](</pt-BR/gateway/secrets>).

## Antes de começar

Você precisa de:

  * OpenClaw com o plugin `vault` incluído disponível
  * um servidor Vault acessível
  * autenticação do Vault capaz de gerar um token de cliente com acesso de leitura aos caminhos de segredos que o OpenClaw deve resolver
  * o ambiente que inicia o Gateway deve incluir `VAULT_ADDR` e uma destas opções: `VAULT_TOKEN`, `OPENCLAW_VAULT_AUTH_METHOD=token_file` com `VAULT_TOKEN_FILE` ou um login JWT/Kubernetes configurado


O resolvedor se comunica com o Vault por HTTP a partir do Node. O Gateway não precisa da CLI do Vault para resolver SecretRefs.

Ative o plugin incluído antes de executar os comandos `openclaw vault`:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Armazene uma chave de provedor no Vault

Por padrão, o OpenClaw usa KV v2 montado em `secret`, de acordo com os exemplos do servidor de desenvolvimento do Vault. Para um Vault de produção, defina `OPENCLAW_VAULT_KV_MOUNT` como o caminho de montagem KV real antes de criar IDs de SecretRef. Com os padrões do OpenClaw, este ID de SecretRef:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

lê este campo do Vault:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Uma forma de criá-lo com a CLI do Vault é:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Use um token de cliente com escopo definido para o OpenClaw, não um token raiz. Para o layout KV v2 padrão, uma política mínima para chaves de provedores de modelos tem esta aparência:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Torne o Vault visível para o Gateway

Para um Gateway local sem contêiner, exporte as configurações do Vault no mesmo shell que inicia o OpenClaw. O método de autenticação padrão lê um token de cliente do Vault de `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Se o Vault Agent gravar um arquivo de destino do token, use a autenticação por arquivo de token:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Para um servidor Vault assinado por uma AC privada, instale essa AC no repositório de confiança do host e ative a confiança do sistema no Node:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Ou forneça diretamente um pacote PEM:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

Essas variáveis devem estar presentes quando o OpenClaw for iniciado. O plugin Vault as encaminha para o processo resolvedor.

Para autenticação JWT não interativa, use um arquivo JWT da carga de trabalho e uma função do Vault do tipo `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

O arquivo JWT deve ser um token projetado da carga de trabalho, como um token de conta de serviço do Kubernetes com um público aceito pela função do Vault. O login interativo OIDC pelo navegador é útil para pessoas, mas o runtime do Gateway precisa de login JWT não interativo ou de um arquivo de token.

Para o método de autenticação Kubernetes do Vault, use `kubernetes`. Isso se destina a Gateways executados como Pods; a montagem padrão é `kubernetes`, e o arquivo JWT padrão é o caminho padrão do token da conta de serviço:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Defina `OPENCLAW_VAULT_AUTH_MOUNT` somente quando o Vault tiver montado a autenticação Kubernetes em outro local que não seja `auth/kubernetes`. Defina `OPENCLAW_VAULT_JWT_FILE` somente quando o token da conta de serviço for projetado em um caminho personalizado.

Configurações opcionais:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Verifique o que o shell atual consegue acessar:

bashCopy code
[code]
    openclaw vault status
[/code]

Quando mais de um provedor de segredos baseado no Vault estiver configurado, selecione um pelo alias:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` nunca exibe `VAULT_TOKEN`; ele informa apenas se o token, o arquivo de token e o arquivo JWT estão definidos.

## Gere e aplique um plano de SecretRef

Crie um plano que mapeie a chave de API do provedor de modelos OpenRouter para o Vault:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Aplique e verifique o plano:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Use `--allow-exec` porque o plugin Vault faz a resolução por meio de um provedor SecretRef de exec gerenciado pelo OpenClaw.

Se o Gateway ainda não estiver em execução, inicie-o normalmente após aplicar o plano, em vez de executar `openclaw secrets reload`.

## Configure mais chaves de provedores

Atalhos integrados:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Várias chaves de provedores em um único plano:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Provedores incluídos sem atalhos, ou provedores de modelos personalizados e compatíveis com a OpenAI já configurados, usam `--provider-key`:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Cada `--provider-key <provider=id>` grava um SecretRef em `models.providers.<provider>.apiKey`. Para provedores personalizados, isso não cria as configurações `baseUrl`, `api` ou `models` do provedor; configure-as primeiro.

Use `--target <path=id>` para qualquer caminho de destino SecretRef conhecido:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Caminhos de destino simples se aplicam ao `openclaw.json`. Use `auth-profiles:<agentId>:<path>` para destinos existentes no `auth-profiles.json`. O caminho de destino deve ser um destino SecretRef registrado no OpenClaw. O comando de configuração não cria segredos nomeados arbitrários no OpenClaw; o Vault continua sendo o armazenamento de segredos, e o OpenClaw armazena SecretRefs apenas em campos de configuração compatíveis.

## Formato do ID de SecretRef

Os IDs de SecretRef do Vault usam esta convenção:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Exemplos:

ID de SecretRef | Leitura padrão do Vault KV v2 | Campo retornado  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
O campo retornado pelo Vault deve ser uma string.

Para KV v1, defina:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

Em seguida, `providers/openrouter/apiKey` lê:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## O que o OpenClaw armazena

A aplicação de um plano de configuração do Vault armazena um provedor gerenciado pelo plugin:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Os campos de credenciais apontam para esse provedor:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

O valor resolvido permanece apenas no snapshot de segredos do runtime ativo.

## Contêineres e implantações gerenciadas

Gateways em contêineres ainda usam o mesmo plugin e a mesma configuração de SecretRef. O contêiner deve receber:

  * `VAULT_ADDR`
  * uma fonte de autenticação: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` mais `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` mais `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` e `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` mais `OPENCLAW_VAULT_AUTH_ROLE`; opcionalmente, substitua `OPENCLAW_VAULT_AUTH_MOUNT` ou `OPENCLAW_VAULT_JWT_FILE`
  * opcionalmente, `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` e `OPENCLAW_VAULT_KV_VERSION`


Ao usar o Kubernetes, prefira `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` quando o Vault tiver a autenticação Kubernetes configurada para o cluster. Use `OPENCLAW_VAULT_AUTH_METHOD=jwt` somente quando o Vault estiver configurado para tratar o cluster como um emissor JWT/OIDC genérico. Qualquer uma das opções é melhor do que um token do Vault de longa duração em um Secret do Kubernetes. Implantações com contêiner auxiliar ou injetor do Vault Agent podem usar `token_file` em vez disso.

Para configurações do Vault com vários locatários, mantenha o roteamento de locatários na política do Vault e na configuração da implantação. O OpenClaw não exige uma montagem, função ou caminho fixos: cada ambiente do Gateway pode definir seus próprios `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` e IDs de SecretRef. Se um único Gateway compartilhado precisar resolver diferentes usuários do Vault ao mesmo tempo, use provedores de exec configurados manualmente que encapsulem ambientes de autenticação distintos ou distribua os locatários entre ambientes do Gateway com variáveis de ambiente do Vault separadas.

## Relacionado

  * [Gerenciamento de segredos](</pt-BR/gateway/secrets>)
  * [`openclaw secrets`](</pt-BR/cli/secrets>)
  * [Inventário de plugins](</pt-BR/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue