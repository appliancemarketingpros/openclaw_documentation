---
title: 保管库 SecretRefs
source_url: https://docs.openclaw.ai/zh-CN/plugins/vault
scraped_at: 2026-07-13
---

快速开始

# Vault SecretRefs

内置的 Vault 插件让 OpenClaw 能够在 Gateway 网关启动和重新加载时，从 HashiCorp Vault 解析 `exec` SecretRefs。OpenClaw 将 Vault 引用存储在配置中，把解析后的值保存在内存中的密钥快照里，并且不会将解析后的 API 密钥写回 `openclaw.json`。

如果你已经在运行 Vault，或者希望将模型提供商密钥存放在 OpenClaw 配置文件之外，请使用此功能。有关 SecretRef 运行时模型，请参阅[密钥管理](</zh-CN/gateway/secrets>)。

## 开始之前

你需要：

  * 提供内置 `vault` 插件的 OpenClaw
  * 可访问的 Vault 服务器
  * 能够生成客户端令牌的 Vault 身份验证方式，该令牌对 OpenClaw 应解析的密钥路径具有读取权限
  * 启动 Gateway 网关的环境必须包含 `VAULT_ADDR`，并包含以下任一身份验证配置：`VAULT_TOKEN`；`OPENCLAW_VAULT_AUTH_METHOD=token_file` 和 `VAULT_TOKEN_FILE`；或已配置的 JWT/Kubernetes 登录


解析器通过 Node 使用 HTTP 与 Vault 通信。Gateway 网关无需安装 Vault CLI 即可解析 SecretRefs。

运行 `openclaw vault` 命令前，请启用内置插件：

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## 在 Vault 中存储提供商密钥

OpenClaw 默认使用挂载在 `secret` 的 KV v2，这与 Vault 开发服务器示例一致。对于生产环境中的 Vault，请在创建 SecretRef ID 前，将 `OPENCLAW_VAULT_KV_MOUNT` 设置为实际的 KV 挂载路径。使用 OpenClaw 默认值时，以下 SecretRef ID：

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

会读取以下 Vault 字段：

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

一种使用 Vault CLI 创建它的方法是：

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

请为 OpenClaw 使用权限受限的客户端令牌，而不是根令牌。对于默认的 KV v2 布局，模型提供商密钥的最小策略如下：

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## 让 Gateway 网关能够访问 Vault

对于未容器化的本地 Gateway 网关，请在启动 OpenClaw 的同一 shell 中导出 Vault 设置。默认身份验证方式从 `VAULT_TOKEN` 读取 Vault 客户端令牌：

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

如果 Vault Agent 将令牌写入接收文件，请使用令牌文件身份验证：

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

对于由私有 CA 签名的 Vault 服务器，可以将该 CA 安装到主机信任存储中，并启用 Node 系统信任：

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

也可以直接提供 PEM 证书包：

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

OpenClaw 启动时必须存在这些变量。Vault 插件会将它们转发给其解析器进程。

对于非交互式 JWT 身份验证，请使用工作负载 JWT 文件和类型为 `jwt` 的 Vault 角色：

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

JWT 文件应是投射的工作负载令牌，例如受众被 Vault 角色接受的 Kubernetes 服务账号令牌。交互式 OIDC 浏览器登录适合人工操作，但 Gateway 网关运行时需要非交互式 JWT 登录或令牌文件。

对于 Vault 的 Kubernetes 身份验证方式，请使用 `kubernetes`。此方式适用于以 Pod 形式运行的 Gateway 网关；默认挂载点为 `kubernetes`，默认 JWT 文件为标准服务账号令牌路径：

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

仅当 Vault 将 Kubernetes 身份验证挂载在 `auth/kubernetes` 之外的位置时，才设置 `OPENCLAW_VAULT_AUTH_MOUNT`。仅当服务账号令牌被投射到自定义路径时，才设置 `OPENCLAW_VAULT_JWT_FILE`。

可选设置：

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

检查当前 shell 可以访问的内容：

bashCopy code
[code]
    openclaw vault status
[/code]

配置了多个由 Vault 支持的密钥提供商时，请通过别名选择一个：

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` 绝不会输出 `VAULT_TOKEN`；它只报告令牌、令牌文件和 JWT 文件是否已设置。

## 生成并应用 SecretRef 计划

创建一个将 OpenRouter 模型提供商 API 密钥映射到 Vault 的计划：

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

应用并验证该计划：

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

由于 Vault 插件通过 OpenClaw 管理的 exec SecretRef 提供商进行解析，因此需要使用 `--allow-exec`。

如果 Gateway 网关尚未运行，请在应用计划后正常启动它，而不是运行 `openclaw secrets reload`。

## 配置更多提供商密钥

内置快捷方式：

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

在一个计划中配置多个提供商密钥：

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

对于没有快捷方式的内置提供商，或者已配置的 OpenAI 兼容提供商和自定义模型提供商，请使用 `--provider-key`：

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

每个 `--provider-key <provider=id>` 都会将 SecretRef 写入 `models.providers.<provider>.apiKey`。对于自定义提供商，此命令不会创建该提供商的 `baseUrl`、`api` 或 `models` 设置；请先配置这些设置。

对于任何已知的 SecretRef 目标路径，请使用 `--target <path=id>`：

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

不带前缀的目标路径应用于 `openclaw.json`。对于现有的 `auth-profiles.json` 目标，请使用 `auth-profiles:<agentId>:<path>`。目标路径必须是已注册的 OpenClaw SecretRef 目标。设置命令不会在 OpenClaw 中创建任意命名的密钥；Vault 仍是密钥存储，而 OpenClaw 仅在受支持的配置字段中存储 SecretRefs。

## SecretRef ID 格式

Vault SecretRef ID 使用以下约定：

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

示例：

SecretRef ID | 默认的 KV v2 Vault 读取路径 | 返回的字段  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Vault 返回的字段必须是字符串。

对于 KV v1，请设置：

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

此时，`providers/openrouter/apiKey` 会读取：

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## OpenClaw 存储的内容

应用 Vault 设置计划会存储一个由插件管理的提供商：

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

凭证字段指向该提供商：

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

解析后的值仅存在于当前运行时密钥快照中。

## 容器和托管式部署

容器化的 Gateway 网关仍使用相同的插件和 SecretRef 配置。容器必须接收：

  * `VAULT_ADDR`
  * 一种身份验证来源： 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` 加上 `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` 加上 `OPENCLAW_VAULT_AUTH_MOUNT`、`OPENCLAW_VAULT_AUTH_ROLE` 和 `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` 加上 `OPENCLAW_VAULT_AUTH_ROLE`；可以选择覆盖 `OPENCLAW_VAULT_AUTH_MOUNT` 或 `OPENCLAW_VAULT_JWT_FILE`
  * 可选的 `VAULT_NAMESPACE`、`OPENCLAW_VAULT_KV_MOUNT` 和 `OPENCLAW_VAULT_KV_VERSION`


使用 Kubernetes 时，如果 Vault 已为集群配置 Kubernetes 身份验证，请优先使用 `OPENCLAW_VAULT_AUTH_METHOD=kubernetes`。仅当 Vault 被配置为将集群视为通用 JWT/OIDC 颁发者时，才使用 `OPENCLAW_VAULT_AUTH_METHOD=jwt`。这两种选项都优于将长期有效的 Vault 令牌存储在 Kubernetes Secret 中。使用 Vault Agent 边车或注入器的部署可以改用 `token_file`。

对于多租户 Vault 设置，请将租户路由保留在 Vault 策略和部署配置中。OpenClaw 不要求固定的挂载点、角色或路径：每个 Gateway 网关环境都可以设置自己的 `OPENCLAW_VAULT_KV_MOUNT`、`OPENCLAW_VAULT_AUTH_ROLE` 和 SecretRef ID。如果一个共享 Gateway 网关必须同时解析不同 Vault 用户的密钥，请使用手动配置的 exec 提供商来封装不同的身份验证环境，或者将租户拆分到具有独立 Vault 环境变量的不同 Gateway 网关环境中。

## 相关内容

  * [密钥管理](</zh-CN/gateway/secrets>)
  * [`openclaw secrets`](</zh-CN/cli/secrets>)
  * [插件清单](</zh-CN/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue