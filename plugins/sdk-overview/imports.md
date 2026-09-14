---
title: Plugin SDK imports and module layout
source_url: https://docs.openclaw.ai/plugins/sdk-overview/imports
scraped_at: 2026-09-14
---

ReferencePlugin SDK reference

Which `openclaw/plugin-sdk/*` subpath to import from, and how to organize a plugin's own public and internal barrels. Part of the [Plugin SDK overview](</plugins/sdk-overview>).

## Import convention

For features with native Control UI, use [Feature plugins](</plugins/feature-plugins>): `feature-contract` defines shared operations, `feature-plugin` registers their backend implementations, and `control-ui` exposes browser contribution and replacement contracts.

Always import from a specific subpath:

typescriptCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { defineChannelPluginEntry } from "openclaw/plugin-sdk/channel-core";
[/code]

Each subpath is a small, self-contained module. This keeps startup fast and prevents circular dependency issues. For channel-specific entry/build helpers, prefer `openclaw/plugin-sdk/channel-core`; keep `openclaw/plugin-sdk/core` for the broader umbrella surface and shared helpers such as `buildChannelConfigSchema`.

For channel config, publish the channel-owned JSON Schema through `openclaw.plugin.json#channelConfigs`. The `plugin-sdk/channel-config-schema` subpath is for shared schema primitives and the generic builder. OpenClaw's bundled plugins use `plugin-sdk/bundled-channel-config-schema` for retained bundled-channel schemas. That bundled schema subpath is not a pattern for new plugins.

For provider discovery that only needs credential values, use `openclaw/plugin-sdk/secret-input` for `readProviderEnvValue`, `resolveNonEnvSecretRefApiKeyMarker`, and SecretRef coercion/normalization. These helpers do not load profile stores, provider transports, or web-search execution. Use `provider-web-search-config-contract` to read plugin-owned web-search config. Keep full auth and search runtime imports in execution paths.

## Subpath reference

The plugin SDK is exposed as a set of narrow subpaths grouped by area (plugin entry, channel, provider, auth, runtime, capability, memory, and reserved bundled-plugin helpers). For the full catalog — grouped and linked — see [Plugin SDK subpaths](</plugins/sdk-subpaths>).

The compiler entrypoint inventory lives in `scripts/lib/plugin-sdk-entrypoints.json`; typed public exports exclude the internal subpaths listed in `scripts/lib/plugin-sdk-private-local-only-subpaths.json`. Production entries on that list retain JavaScript-only host runtime exports for separately published official plugins, while test-only entries remain unexported. Run `pnpm plugin-sdk:surface` to audit the public export count. Deprecated public subpaths that are old enough and unused by bundled extension production code are tracked in `scripts/lib/plugin-sdk-deprecated-public-subpaths.json`; broad deprecated re-export barrels are tracked in `scripts/lib/plugin-sdk-deprecated-barrel-subpaths.json`.

## Internal module convention

Within your plugin, use local barrel files for internal imports:

textCopy code
[code]
    my-plugin/  api.ts            # Public exports for external consumers  runtime-api.ts    # Internal-only runtime exports  index.ts          # Plugin entry point  setup-entry.ts    # Lightweight setup-only entry (optional)
[/code]

Facade-loaded bundled plugin public surfaces (`api.ts`, `runtime-api.ts`, `index.ts`, `setup-entry.ts`, and similar public entry files) prefer the active runtime config snapshot when OpenClaw is already running. If no runtime snapshot exists yet, they fall back to the resolved config file on disk. Packaged bundled plugin facades should be loaded through OpenClaw's plugin facade loaders; direct imports from `dist/extensions/...` bypass the manifest and runtime sidecar checks that packaged installs use for plugin-owned code.

Provider plugins can expose a narrow plugin-local contract barrel when a helper is intentionally provider-specific and does not belong in a generic SDK subpath yet. Bundled examples:

  * **Anthropic** : public `api.ts` / `contract-api.ts` seam for Claude beta-header and `service_tier` stream helpers.
  * **`@openclaw/openai-provider`** : `api.ts` exports provider builders, default-model helpers, and realtime provider builders.
  * **`@openclaw/openrouter-provider`** : `api.ts` exports the provider builder plus onboarding/config helpers.


Was this useful?YesNo

Open issue