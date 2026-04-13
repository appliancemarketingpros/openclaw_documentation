---
title: Plugin Testing
source_url: https://docs.openclaw.ai/plugins/sdk-testing
scraped_at: 2026-04-13
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

SDK Reference

Plugin Testing

# 

​

Plugin Testing

Reference for test utilities, patterns, and lint enforcement for OpenClaw plugins.

**Looking for test examples?** The how-to guides include worked test examples: [Channel plugin tests](</plugins/sdk-channel-plugins#step-6-test>) and [Provider plugin tests](</plugins/sdk-provider-plugins#step-6-test>).

## 

​

Test utilities

**Import:** `openclaw/plugin-sdk/testing` The testing subpath exports a narrow set of helpers for plugin authors:
[code] 
    import {
      installCommonResolveTargetErrorCases,
      shouldAckReaction,
      removeAckReactionAfterReply,
    } from "openclaw/plugin-sdk/testing";
    
[/code]

### 

​

Available exports

Export| Purpose  
---|---  
`installCommonResolveTargetErrorCases`| Shared test cases for target resolution error handling  
`shouldAckReaction`| Check whether a channel should add an ack reaction  
`removeAckReactionAfterReply`| Remove ack reaction after reply delivery  
  
### 

​

Types

The testing subpath also re-exports types useful in test files:
[code] 
    import type {
      ChannelAccountSnapshot,
      ChannelGatewayContext,
      OpenClawConfig,
      PluginRuntime,
      RuntimeEnv,
      MockFn,
    } from "openclaw/plugin-sdk/testing";
    
[/code]

## 

​

Testing target resolution

Use `installCommonResolveTargetErrorCases` to add standard error cases for channel target resolution:
[code] 
    import { describe } from "vitest";
    import { installCommonResolveTargetErrorCases } from "openclaw/plugin-sdk/testing";
    
    describe("my-channel target resolution", () => {
      installCommonResolveTargetErrorCases({
        resolveTarget: ({ to, mode, allowFrom }) => {
          // Your channel's target resolution logic
          return myChannelResolveTarget({ to, mode, allowFrom });
        },
        implicitAllowFrom: ["user1", "user2"],
      });
    
      // Add channel-specific test cases
      it("should resolve @username targets", () => {
        // ...
      });
    });
    
[/code]

## 

​

Testing patterns

### 

​

Unit testing a channel plugin
[code] 
    import { describe, it, expect, vi } from "vitest";
    
    describe("my-channel plugin", () => {
      it("should resolve account from config", () => {
        const cfg = {
          channels: {
            "my-channel": {
              token: "test-token",
              allowFrom: ["user1"],
            },
          },
        };
    
        const account = myPlugin.setup.resolveAccount(cfg, undefined);
        expect(account.token).toBe("test-token");
      });
    
      it("should inspect account without materializing secrets", () => {
        const cfg = {
          channels: {
            "my-channel": { token: "test-token" },
          },
        };
    
        const inspection = myPlugin.setup.inspectAccount(cfg, undefined);
        expect(inspection.configured).toBe(true);
        expect(inspection.tokenStatus).toBe("available");
        // No token value exposed
        expect(inspection).not.toHaveProperty("token");
      });
    });
    
[/code]

### 

​

Unit testing a provider plugin
[code] 
    import { describe, it, expect } from "vitest";
    
    describe("my-provider plugin", () => {
      it("should resolve dynamic models", () => {
        const model = myProvider.resolveDynamicModel({
          modelId: "custom-model-v2",
          // ... context
        });
    
        expect(model.id).toBe("custom-model-v2");
        expect(model.provider).toBe("my-provider");
        expect(model.api).toBe("openai-completions");
      });
    
      it("should return catalog when API key is available", async () => {
        const result = await myProvider.catalog.run({
          resolveProviderApiKey: () => ({ apiKey: "test-key" }),
          // ... context
        });
    
        expect(result?.provider?.models).toHaveLength(2);
      });
    });
    
[/code]

### 

​

Mocking the plugin runtime

For code that uses `createPluginRuntimeStore`, mock the runtime in tests:
[code] 
    import { createPluginRuntimeStore } from "openclaw/plugin-sdk/runtime-store";
    import type { PluginRuntime } from "openclaw/plugin-sdk/runtime-store";
    
    const store = createPluginRuntimeStore<PluginRuntime>("test runtime not set");
    
    // In test setup
    const mockRuntime = {
      agent: {
        resolveAgentDir: vi.fn().mockReturnValue("/tmp/agent"),
        // ... other mocks
      },
      config: {
        loadConfig: vi.fn(),
        writeConfigFile: vi.fn(),
      },
      // ... other namespaces
    } as unknown as PluginRuntime;
    
    store.setRuntime(mockRuntime);
    
    // After tests
    store.clearRuntime();
    
[/code]

### 

​

Testing with per-instance stubs

Prefer per-instance stubs over prototype mutation:
[code] 
    // Preferred: per-instance stub
    const client = new MyChannelClient();
    client.sendMessage = vi.fn().mockResolvedValue({ id: "msg-1" });
    
    // Avoid: prototype mutation
    // MyChannelClient.prototype.sendMessage = vi.fn();
    
[/code]

## 

​

Contract tests (in-repo plugins)

Bundled plugins have contract tests that verify registration ownership:
[code] 
    pnpm test -- src/plugins/contracts/
    
[/code]

These tests assert:

  * Which plugins register which providers
  * Which plugins register which speech providers
  * Registration shape correctness
  * Runtime contract compliance


### 

​

Running scoped tests

For a specific plugin:
[code] 
    pnpm test -- <bundled-plugin-root>/my-channel/
    
[/code]

For contract tests only:
[code] 
    pnpm test -- src/plugins/contracts/shape.contract.test.ts
    pnpm test -- src/plugins/contracts/auth.contract.test.ts
    pnpm test -- src/plugins/contracts/runtime.contract.test.ts
    
[/code]

## 

​

Lint enforcement (in-repo plugins)

Three rules are enforced by `pnpm check` for in-repo plugins:

  1. **No monolithic root imports** — `openclaw/plugin-sdk` root barrel is rejected
  2. **No direct`src/` imports** — plugins cannot import `../../src/` directly
  3. **No self-imports** — plugins cannot import their own `plugin-sdk/<name>` subpath

External plugins are not subject to these lint rules, but following the same patterns is recommended.

## 

​

Test configuration

OpenClaw uses Vitest with V8 coverage thresholds. For plugin tests:
[code] 
    # Run all tests
    pnpm test
    
    # Run specific plugin tests
    pnpm test -- <bundled-plugin-root>/my-channel/src/channel.test.ts
    
    # Run with a specific test name filter
    pnpm test -- <bundled-plugin-root>/my-channel/ -t "resolves account"
    
    # Run with coverage
    pnpm test:coverage
    
[/code]

If local runs cause memory pressure:
[code] 
    OPENCLAW_VITEST_MAX_WORKERS=1 pnpm test
    
[/code]

## 

​

Related

  * [SDK Overview](</plugins/sdk-overview>) — import conventions
  * [SDK Channel Plugins](</plugins/sdk-channel-plugins>) — channel plugin interface
  * [SDK Provider Plugins](</plugins/sdk-provider-plugins>) — provider plugin hooks
  * [Building Plugins](</plugins/building-plugins>) — getting started guide


[Setup and Config](</plugins/sdk-setup>)[Plugin Manifest](</plugins/manifest>)

⌘I