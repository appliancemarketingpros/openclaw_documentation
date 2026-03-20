---
title: Plugins
source_url: https://docs.openclaw.ai/tools/plugin
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Plugins

Plugins

# 

​

Plugins

Plugins extend OpenClaw with new capabilities: channels, model providers, tools, skills, speech, image generation, and more. Some plugins are **core** (shipped with OpenClaw), others are **external** (published on npm by the community).

## 

​

Quick start

1

See what is loaded

Copy
[code]
    openclaw plugins list
    
[/code]

2

Install a plugin

Copy
[code]
    # From npm
    openclaw plugins install @openclaw/voice-call
    
    # From a local directory or archive
    openclaw plugins install ./my-plugin
    openclaw plugins install ./my-plugin.tgz
    
[/code]

3

Restart the Gateway

Copy
[code]
    openclaw gateway restart
    
[/code]

Then configure under `plugins.entries.\<id\>.config` in your config file.

## 

​

Plugin types

OpenClaw recognizes two plugin formats:

Format| How it works| Examples  
---|---|---  
**Native**| `openclaw.plugin.json` \+ runtime module; executes in-process| Official plugins, community npm packages  
**Bundle**|  Codex/Claude/Cursor-compatible layout; mapped to OpenClaw features| `.codex-plugin/`, `.claude-plugin/`, `.cursor-plugin/`  
  
Both show up under `openclaw plugins list`. See [Plugin Bundles](</plugins/bundles>) for bundle details.

## 

​

Official plugins

### 

​

Installable (npm)

Plugin| Package| Docs  
---|---|---  
Matrix| `@openclaw/matrix`| [Matrix](</channels/matrix>)  
Microsoft Teams| `@openclaw/msteams`| [Microsoft Teams](</channels/msteams>)  
Nostr| `@openclaw/nostr`| [Nostr](</channels/nostr>)  
Voice Call| `@openclaw/voice-call`| [Voice Call](</plugins/voice-call>)  
Zalo| `@openclaw/zalo`| [Zalo](</channels/zalo>)  
Zalo Personal| `@openclaw/zalouser`| [Zalo Personal](</plugins/zalouser>)  
  
### 

​

Core (shipped with OpenClaw)

Model providers (enabled by default)

`anthropic`, `byteplus`, `cloudflare-ai-gateway`, `github-copilot`, `google`, `huggingface`, `kilocode`, `kimi-coding`, `minimax`, `mistral`, `modelstudio`, `moonshot`, `nvidia`, `openai`, `opencode`, `opencode-go`, `openrouter`, `qianfan`, `qwen-portal-auth`, `synthetic`, `together`, `venice`, `vercel-ai-gateway`, `volcengine`, `xiaomi`, `zai`

Memory plugins

  * `memory-core` — bundled memory search (default via `plugins.slots.memory`)
  * `memory-lancedb` — install-on-demand long-term memory with auto-recall/capture (set `plugins.slots.memory = "memory-lancedb"`)


Speech providers (enabled by default)

`elevenlabs`, `microsoft`

Other

  * `copilot-proxy` — VS Code Copilot Proxy bridge (disabled by default)


Looking for third-party plugins? See [Community Plugins](</plugins/community>).

## 

​

Configuration

Copy
[code]
    {
      plugins: {
        enabled: true,
        allow: ["voice-call"],
        deny: ["untrusted-plugin"],
        load: { paths: ["~/Projects/oss/voice-call-extension"] },
        entries: {
          "voice-call": { enabled: true, config: { provider: "twilio" } },
        },
      },
    }
    
[/code]

Field| Description  
---|---  
`enabled`| Master toggle (default: `true`)  
`allow`| Plugin allowlist (optional)  
`deny`| Plugin denylist (optional; deny wins)  
`load.paths`| Extra plugin files/directories  
`slots`| Exclusive slot selectors (e.g. `memory`, `contextEngine`)  
`entries.\<id\>`| Per-plugin toggles + config  
  
Config changes **require a gateway restart**.

Plugin states: disabled vs missing vs invalid

  * **Disabled** : plugin exists but enablement rules turned it off. Config is preserved.
  * **Missing** : config references a plugin id that discovery did not find.
  * **Invalid** : plugin exists but its config does not match the declared schema.


## 

​

Discovery and precedence

OpenClaw scans for plugins in this order (first match wins):

1

Config paths

`plugins.load.paths` — explicit file or directory paths.

2

Workspace extensions

`\<workspace\>/.openclaw/extensions/*.ts` and `\<workspace\>/.openclaw/extensions/*/index.ts`.

3

Global extensions

`~/.openclaw/extensions/*.ts` and `~/.openclaw/extensions/*/index.ts`.

4

Bundled plugins

Shipped with OpenClaw. Many are enabled by default (model providers, speech). Others require explicit enablement.

### 

​

Enablement rules

  * `plugins.enabled: false` disables all plugins
  * `plugins.deny` always wins over allow
  * `plugins.entries.\<id\>.enabled: false` disables that plugin
  * Workspace-origin plugins are **disabled by default** (must be explicitly enabled)
  * Bundled plugins follow the built-in default-on set unless overridden
  * Exclusive slots can force-enable the selected plugin for that slot


## 

​

Plugin slots (exclusive categories)

Some categories are exclusive (only one active at a time):

Copy
[code]
    {
      plugins: {
        slots: {
          memory: "memory-core", // or "none" to disable
          contextEngine: "legacy", // or a plugin id
        },
      },
    }
    
[/code]

Slot| What it controls| Default  
---|---|---  
`memory`| Active memory plugin| `memory-core`  
`contextEngine`| Active context engine| `legacy` (built-in)  
  
## 

​

CLI reference

Copy
[code]
    openclaw plugins list                    # compact inventory
    openclaw plugins inspect <id>            # deep detail
    openclaw plugins inspect <id> --json     # machine-readable
    openclaw plugins status                  # operational summary
    openclaw plugins doctor                  # diagnostics
    
    openclaw plugins install <npm-spec>      # install from npm
    openclaw plugins install <path>          # install from local path
    openclaw plugins install -l <path>       # link (no copy) for dev
    openclaw plugins update <id>             # update one plugin
    openclaw plugins update --all            # update all
    
    openclaw plugins enable <id>
    openclaw plugins disable <id>
    
[/code]

See [`openclaw plugins` CLI reference](</cli/plugins>) for full details.

## 

​

Plugin API overview

Plugins export either a function or an object with `register(api)`:

Copy
[code]
    export default definePluginEntry({
      id: "my-plugin",
      name: "My Plugin",
      register(api) {
        api.registerProvider({
          /* ... */
        });
        api.registerTool({
          /* ... */
        });
        api.registerChannel({
          /* ... */
        });
      },
    });
    
[/code]

Common registration methods:

Method| What it registers  
---|---  
`registerProvider`| Model provider (LLM)  
`registerChannel`| Chat channel  
`registerTool`| Agent tool  
`registerHook` / `on(...)`| Lifecycle hooks  
`registerSpeechProvider`| Text-to-speech / STT  
`registerMediaUnderstandingProvider`| Image/audio analysis  
`registerImageGenerationProvider`| Image generation  
`registerWebSearchProvider`| Web search  
`registerHttpRoute`| HTTP endpoint  
`registerCommand` / `registerCli`| CLI commands  
`registerContextEngine`| Context engine  
`registerService`| Background service  
  
## 

​

Related

  * [Building Plugins](</plugins/building-plugins>) — create your own plugin
  * [Plugin Bundles](</plugins/bundles>) — Codex/Claude/Cursor bundle compatibility
  * [Plugin Manifest](</plugins/manifest>) — manifest schema
  * [Registering Tools](</plugins/agent-tools>) — add agent tools in a plugin
  * [Plugin Internals](</plugins/architecture>) — capability model and load pipeline
  * [Community Plugins](</plugins/community>) — third-party listings


[Tools and Plugins](</tools>)[Building Plugins](</plugins/building-plugins>)

⌘I