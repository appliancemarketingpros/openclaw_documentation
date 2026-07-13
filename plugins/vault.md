---
title: Vault SecretRefs
source_url: https://docs.openclaw.ai/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# Vault SecretRefs

The bundled Vault plugin lets OpenClaw resolve `exec` SecretRefs from HashiCorp Vault at Gateway startup and reload time. OpenClaw stores Vault references in config, keeps resolved values in the in-memory secrets snapshot, and does not write the resolved API keys back to `openclaw.json`.

Use this when you already run Vault or want model provider keys to live outside OpenClaw config files. For the SecretRef runtime model, see [Secrets management](</gateway/secrets>).

## Before you begin

You need:

  * OpenClaw with the bundled `vault` plugin available
  * a reachable Vault server
  * Vault auth that can produce a client token with read access to the secret paths OpenClaw should resolve
  * the environment that starts the Gateway must include `VAULT_ADDR` and either `VAULT_TOKEN`, `OPENCLAW_VAULT_AUTH_METHOD=token_file` with `VAULT_TOKEN_FILE`, or a configured JWT/Kubernetes login


The resolver talks to Vault over HTTP from Node. The Gateway does not need the Vault CLI to resolve SecretRefs.

Enable the bundled plugin before running the `openclaw vault` commands:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Store a provider key in Vault

OpenClaw defaults to KV v2 mounted at `secret`, matching Vault dev-server examples. For production Vault, set `OPENCLAW_VAULT_KV_MOUNT` to your actual KV mount path before creating SecretRef ids. With the OpenClaw defaults, this SecretRef id:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

reads this Vault field:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

One way to create it with the Vault CLI is:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Use a scoped client token for OpenClaw, not a root token. For the default KV v2 layout, a minimal policy for model provider keys looks like:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Make Vault visible to the Gateway

For an uncontainerized local Gateway, export Vault settings in the same shell that starts OpenClaw. The default auth method reads a Vault client token from `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

If Vault Agent writes a token sink file, use token-file auth:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

For a Vault server signed by a private CA, either install that CA in the host trust store and enable Node system trust:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Or provide a PEM bundle directly:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

These variables must be present when OpenClaw starts. The Vault plugin forwards them to its resolver process.

For non-interactive JWT auth, use a workload JWT file and a Vault role of type `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

The JWT file should be a projected workload token, such as a Kubernetes service account token with an audience accepted by the Vault role. Interactive OIDC browser login is useful for humans, but Gateway runtime needs non-interactive JWT login or a token file.

For Vault's Kubernetes auth method, use `kubernetes`. This is intended for Gateways running as Pods; the default mount is `kubernetes`, and the default JWT file is the standard service account token path:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Set `OPENCLAW_VAULT_AUTH_MOUNT` only when Vault mounted Kubernetes auth somewhere other than `auth/kubernetes`. Set `OPENCLAW_VAULT_JWT_FILE` only when the service account token is projected at a custom path.

Optional settings:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Check what the current shell can see:

bashCopy code
[code]
    openclaw vault status
[/code]

When more than one Vault-backed secret provider is configured, select one by alias:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` never prints `VAULT_TOKEN`; it reports only whether the token, token file, and JWT file are set.

## Generate and apply a SecretRef plan

Create a plan that maps OpenRouter's model provider API key to Vault:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Apply and verify the plan:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Use `--allow-exec` because the Vault plugin resolves through an OpenClaw-managed exec SecretRef provider.

If the Gateway is not running yet, start it normally after applying the plan instead of running `openclaw secrets reload`.

## Configure more provider keys

Built-in shortcuts:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Multiple provider keys in one plan:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Bundled providers without shortcuts, or already-configured OpenAI-compatible and custom model providers, use `--provider-key`:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Each `--provider-key <provider=id>` writes a SecretRef to `models.providers.<provider>.apiKey`. For custom providers, it does not create the provider's `baseUrl`, `api`, or `models` settings; configure those first.

Use `--target <path=id>` for any known SecretRef target path:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Bare target paths apply to `openclaw.json`. Use `auth-profiles:<agentId>:<path>` for existing `auth-profiles.json` targets. The target path must be a registered OpenClaw SecretRef target. The setup command does not create arbitrary named secrets in OpenClaw; Vault remains the secret store, and OpenClaw stores SecretRefs only on supported config fields.

## SecretRef id format

Vault SecretRef ids use this convention:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Examples:

SecretRef id | Default KV v2 Vault read | Returned field  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
The returned Vault field must be a string.

For KV v1, set:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

Then `providers/openrouter/apiKey` reads:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## What OpenClaw stores

Applying a Vault setup plan stores a plugin-managed provider:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Credential fields point at that provider:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

The resolved value lives only in the active runtime secrets snapshot.

## Containers and managed deployments

Containerized Gateways still use the same plugin and SecretRef config. The container must receive:

  * `VAULT_ADDR`
  * one auth source: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` plus `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` plus `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE`, and `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` plus `OPENCLAW_VAULT_AUTH_ROLE`; optionally override `OPENCLAW_VAULT_AUTH_MOUNT` or `OPENCLAW_VAULT_JWT_FILE`
  * optional `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT`, and `OPENCLAW_VAULT_KV_VERSION`


When using Kubernetes, prefer `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` when Vault has Kubernetes auth configured for the cluster. Use `OPENCLAW_VAULT_AUTH_METHOD=jwt` only when Vault is configured to treat the cluster as a generic JWT/OIDC issuer. Either option is better than a long-lived Vault token in a Kubernetes Secret. Vault Agent sidecar or injector deployments can use `token_file` instead.

For multi-tenant Vault setups, keep tenant routing in Vault policy and deployment config. OpenClaw does not require a fixed mount, role, or path: each Gateway environment can set its own `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE`, and SecretRef ids. If one shared Gateway must resolve different Vault users at the same time, use manually configured exec providers that wrap distinct auth environments, or split tenants across Gateway environments with separate Vault env.

## Related

  * [Secrets management](</gateway/secrets>)
  * [`openclaw secrets`](</cli/secrets>)
  * [Plugin inventory](</plugins/plugin-inventory>)


Was this useful?YesNo

Open issue