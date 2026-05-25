---
title: Secrets apply 计划契约
source_url: https://docs.openclaw.ai/zh-CN/gateway/secrets-plan-contract
scraped_at: 2026-05-25
---

本页定义了 `openclaw secrets apply` 强制执行的严格契约。

如果某个目标不符合这些规则，apply 会在修改配置之前失败。

## 计划文件结构

`openclaw secrets apply --from <plan.json>` 期望接收一个包含计划目标的 `targets` 数组：

json5Copy code
[code]
    {  version: 1,  protocolVersion: 1,  targets: [    {      type: "models.providers.apiKey",      path: "models.providers.openai.apiKey",      pathSegments: ["models", "providers", "openai", "apiKey"],      providerId: "openai",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },    {      type: "auth-profiles.api_key.key",      path: "profiles.openai:default.key",      pathSegments: ["profiles", "openai:default", "key"],      agentId: "main",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },  ],}
[/code]

## 支持的目标范围

在以下位置中的受支持凭证路径，接受计划目标：

  * [SecretRef Credential Surface](</zh-CN/reference/secretref-credential-surface>)


## 目标类型行为

通用规则：

  * `target.type` 必须是已识别类型，并且必须匹配规范化后的 `target.path` 结构。


出于兼容性考虑，现有计划仍接受以下别名：

  * `models.providers.apiKey`
  * `skills.entries.apiKey`
  * `channels.googlechat.serviceAccount`


## 路径验证规则

每个目标都会按以下所有规则进行验证：

  * `type` 必须是已识别的目标类型。
  * `path` 必须是非空的点路径。
  * `pathSegments` 可以省略。如果提供，它在规范化后必须与 `path` 完全一致。
  * 以下禁止的段会被拒绝：`__proto__`、`prototype`、`constructor`。
  * 规范化后的路径必须匹配该目标类型已注册的路径结构。
  * 如果设置了 `providerId` 或 `accountId`，它必须与路径中编码的 id 匹配。
  * `auth-profiles.json` 目标需要 `agentId`。
  * 创建新的 `auth-profiles.json` 映射时，请包含 `authProfileProvider`。


## 失败行为

如果目标验证失败，apply 会退出并报错，例如：

textCopy code
[code]
    Invalid plan target path for models.providers.apiKey: models.providers.openai.baseUrl
[/code]

无效计划不会提交任何写入。

## 执行提供商同意行为

  * `--dry-run` 默认跳过执行 SecretRef 检查。
  * 包含执行 SecretRefs / 提供商的计划，在写入模式下如果未设置 `--allow-exec` 会被拒绝。
  * 验证 / 应用包含执行内容的计划时，请在 dry-run 和写入命令中都传入 `--allow-exec`。


## 运行时与审计范围说明

  * 仅引用形式的 `auth-profiles.json` 条目（`keyRef` / `tokenRef`）会纳入运行时解析和审计覆盖范围。
  * `secrets apply` 会写入受支持的 `openclaw.json` 目标、受支持的 `auth-profiles.json` 目标，以及可选的清理目标。


## 操作员检查

bashCopy code
[code]
    # 验证计划但不写入openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run # 然后正式应用openclaw secrets apply --from /tmp/openclaw-secrets-plan.json # 对于包含执行内容的计划，在两种模式下都要显式选择启用openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-exec
[/code]

如果 apply 因目标路径无效消息而失败，请使用 `openclaw secrets configure` 重新生成计划，或将目标路径修正为上述支持的结构。

## 相关文档

  * [Secrets Management](</zh-CN/gateway/secrets>)
  * [CLI `secrets`](</zh-CN/cli/secrets>)
  * [SecretRef Credential Surface](</zh-CN/reference/secretref-credential-surface>)
  * [Configuration Reference](</zh-CN/gateway/configuration-reference>)


Was this useful?YesNo