---
title: Manage plugins
source_url: https://docs.openclaw.ai/plugins/manage-plugins
scraped_at: 2026-05-04
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Plugins

Manage plugins

> ## Documentation Index
> 
> Fetch the complete documentation index at: <https://docs.openclaw.ai/llms.txt>
> 
> Use this file to discover all available pages before exploring further.

Most plugin workflows are a few commands: search, install, restart the Gateway, verify, and uninstall when you no longer need the plugin.

## 

​

List plugins
[code] 
    openclaw plugins list
    openclaw plugins list --enabled
    openclaw plugins list --verbose
    openclaw plugins list --json
    
[/code]

Use `--json` for scripts. It includes registry diagnostics and each plugin’s static `dependencyStatus` when the plugin package declares `dependencies` or `optionalDependencies`.
[code] 
    openclaw plugins list --json \
      | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
    
[/code]

`plugins list` is a cold inventory check. It shows what OpenClaw can discover from config, manifests, and the plugin registry; it does not prove that an already-running Gateway process imported the plugin runtime.

## 

​

Install plugins
[code] 
    # Search ClawHub for plugin packages.
    openclaw plugins search "calendar"
    
    # Bare package specs try ClawHub first, then npm fallback.
    openclaw plugins install <package>
    
    # Force one source.
    openclaw plugins install clawhub:<package>
    openclaw plugins install npm:<package>
    
    # Install a specific version or dist-tag.
    openclaw plugins install clawhub:<package>@1.2.3
    openclaw plugins install clawhub:<package>@beta
    openclaw plugins install npm:@scope/openclaw-plugin@1.2.3
    openclaw plugins install npm:@openclaw/codex
    
    # Install from git or a local development checkout.
    openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0
    openclaw plugins install ./my-plugin
    openclaw plugins install --link ./my-plugin
    
[/code]

After installing plugin code, restart the Gateway that serves your channels:
[code] 
    openclaw gateway restart
    openclaw plugins inspect <plugin-id> --runtime --json
    
[/code]

Use `inspect --runtime` when you need proof that the plugin registered runtime surfaces such as tools, hooks, services, Gateway methods, or plugin-owned CLI commands.

## 

​

Update plugins
[code] 
    openclaw plugins update <plugin-id>
    openclaw plugins update <npm-package-or-spec>
    openclaw plugins update --all
    
[/code]

If a plugin was installed from an npm dist-tag such as `@beta`, later `update <plugin-id>` calls reuse that recorded tag. Passing an explicit npm spec switches the tracked install to that spec for future updates.
[code] 
    openclaw plugins update @scope/openclaw-plugin@beta
    openclaw plugins update @scope/openclaw-plugin
    
[/code]

The second command moves a plugin back to the registry’s default release line when it was previously pinned to an exact version or tag. When `openclaw update` runs on the beta channel, default-line npm and ClawHub plugin records try the matching plugin `@beta` release first. If that beta release does not exist, OpenClaw falls back to the recorded default/latest spec. Exact versions and explicit tags such as `@rc` or `@beta` are preserved.

## 

​

Uninstall plugins
[code] 
    openclaw plugins uninstall <plugin-id> --dry-run
    openclaw plugins uninstall <plugin-id>
    openclaw plugins uninstall <plugin-id> --keep-files
    openclaw gateway restart
    
[/code]

Uninstall removes the plugin’s config entry, plugin index record, allow/deny list entries, and linked load paths when applicable. Managed install directories are removed unless you pass `--keep-files`.

## 

​

Publish plugins

You can publish external plugins to [ClawHub](<https://clawhub.ai>), npmjs.com, or both.

### 

​

Publish to ClawHub

ClawHub is the primary public discovery surface for OpenClaw plugins. It gives users searchable metadata, version history, and registry scan results before install.
[code] 
    npm i -g clawhub
    clawhub login
    clawhub package publish your-org/your-plugin --dry-run
    clawhub package publish your-org/your-plugin
    clawhub package publish your-org/your-plugin@v1.0.0
    
[/code]

Users install from ClawHub with:
[code] 
    openclaw plugins install clawhub:<package>
    openclaw plugins install <package>
    
[/code]

The bare form still checks ClawHub first.

### 

​

Publish to npmjs.com

Native npm plugins must include a plugin manifest and `package.json` OpenClaw entrypoint metadata.

package.json
[code]
    {
      "name": "@acme/openclaw-plugin",
      "version": "1.0.0",
      "type": "module",
      "openclaw": {
        "extensions": ["./dist/index.js"]
      }
    }
    
[/code]
[code] 
    npm publish --access public
    
[/code]

Users install npm-only with:
[code] 
    openclaw plugins install npm:@acme/openclaw-plugin
    openclaw plugins install npm:@acme/openclaw-plugin@beta
    openclaw plugins install npm:@acme/openclaw-plugin@1.0.0
    
[/code]

If the same package is also available on ClawHub, `npm:` skips ClawHub lookup and forces npm resolution.

## 

​

Source choice

  * **ClawHub** : use when you want OpenClaw-native discovery, scan summaries, versions, and install hints.
  * **npmjs.com** : use when you already ship JavaScript packages or need npm dist-tags/private registry workflows.
  * **Git** : use when you want to install directly from a branch, tag, or commit.
  * **Local path** : use when you are developing or testing a plugin on the same machine.


## 

​

Related

  * [Plugins](</tools/plugin>) \- overview and troubleshooting
  * [`openclaw plugins`](</cli/plugins>) \- full CLI reference
  * [ClawHub](</tools/clawhub>) \- publish and registry operations
  * [Building plugins](</plugins/building-plugins>) \- create a plugin package
  * [Plugin manifest](</plugins/manifest>) \- manifest and package metadata


[Install and Configure](</tools/plugin>)[Community plugins](</plugins/community>)

⌘I