---
title: Sandbox CLI
source_url: https://docs.openclaw.ai/cli/sandbox
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Tools and execution

Sandbox CLI

# 

​

Sandbox CLI

Manage sandbox runtimes for isolated agent execution.

## 

​

Overview

OpenClaw can run agents in isolated sandbox runtimes for security. The `sandbox` commands help you inspect and recreate those runtimes after updates or configuration changes. Today that usually means:

  * Docker sandbox containers
  * SSH sandbox runtimes when `agents.defaults.sandbox.backend = "ssh"`
  * OpenShell sandbox runtimes when `agents.defaults.sandbox.backend = "openshell"`

For `ssh` and OpenShell `remote`, recreate matters more than with Docker:

  * the remote workspace is canonical after the initial seed
  * `openclaw sandbox recreate` deletes that canonical remote workspace for the selected scope
  * next use seeds it again from the current local workspace


## 

​

Commands

### 

​

`openclaw sandbox explain`

Inspect the **effective** sandbox mode/scope/workspace access, sandbox tool policy, and elevated gates (with fix-it config key paths).

Copy
[code]
    openclaw sandbox explain
    openclaw sandbox explain --session agent:main:main
    openclaw sandbox explain --agent work
    openclaw sandbox explain --json
    
[/code]

### 

​

`openclaw sandbox list`

List all sandbox runtimes with their status and configuration.

Copy
[code]
    openclaw sandbox list
    openclaw sandbox list --browser  # List only browser containers
    openclaw sandbox list --json     # JSON output
    
[/code]

**Output includes:**

  * Runtime name and status
  * Backend (`docker`, `openshell`, etc.)
  * Config label and whether it matches current config
  * Age (time since creation)
  * Idle time (time since last use)
  * Associated session/agent


### 

​

`openclaw sandbox recreate`

Remove sandbox runtimes to force recreation with updated config.

Copy
[code]
    openclaw sandbox recreate --all                # Recreate all containers
    openclaw sandbox recreate --session main       # Specific session
    openclaw sandbox recreate --agent mybot        # Specific agent
    openclaw sandbox recreate --browser            # Only browser containers
    openclaw sandbox recreate --all --force        # Skip confirmation
    
[/code]

**Options:**

  * `--all`: Recreate all sandbox containers
  * `--session <key>`: Recreate container for specific session
  * `--agent <id>`: Recreate containers for specific agent
  * `--browser`: Only recreate browser containers
  * `--force`: Skip confirmation prompt

**Important:** Runtimes are automatically recreated when the agent is next used.

## 

​

Use Cases

### 

​

After updating a Docker image

Copy
[code]
    # Pull new image
    docker pull openclaw-sandbox:latest
    docker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim
    
    # Update config to use new image
    # Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image)
    
    # Recreate containers
    openclaw sandbox recreate --all
    
[/code]

### 

​

After changing sandbox configuration

Copy
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*)
    
    # Recreate to apply new config
    openclaw sandbox recreate --all
    
[/code]

### 

​

After changing SSH target or SSH auth material

Copy
[code]
    # Edit config:
    # - agents.defaults.sandbox.backend
    # - agents.defaults.sandbox.ssh.target
    # - agents.defaults.sandbox.ssh.workspaceRoot
    # - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile
    # - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData
    
    openclaw sandbox recreate --all
    
[/code]

For the core `ssh` backend, recreate deletes the per-scope remote workspace root on the SSH target. The next run seeds it again from the local workspace.

### 

​

After changing OpenShell source, policy, or mode

Copy
[code]
    # Edit config:
    # - agents.defaults.sandbox.backend
    # - plugins.entries.openshell.config.from
    # - plugins.entries.openshell.config.mode
    # - plugins.entries.openshell.config.policy
    
    openclaw sandbox recreate --all
    
[/code]

For OpenShell `remote` mode, recreate deletes the canonical remote workspace for that scope. The next run seeds it again from the local workspace.

### 

​

After changing setupCommand

Copy
[code]
    openclaw sandbox recreate --all
    # or just one agent:
    openclaw sandbox recreate --agent family
    
[/code]

### 

​

For a specific agent only

Copy
[code]
    # Update only one agent's containers
    openclaw sandbox recreate --agent alfred
    
[/code]

## 

​

Why is this needed?

**Problem:** When you update sandbox configuration:

  * Existing runtimes continue running with old settings
  * Runtimes are only pruned after 24h of inactivity
  * Regularly-used agents keep old runtimes alive indefinitely

**Solution:** Use `openclaw sandbox recreate` to force removal of old runtimes. They’ll be recreated automatically with current settings when next needed. Tip: prefer `openclaw sandbox recreate` over manual backend-specific cleanup. It uses the Gateway’s runtime registry and avoids mismatches when scope/session keys change.

## 

​

Configuration

Sandbox settings live in `~/.openclaw/openclaw.json` under `agents.defaults.sandbox` (per-agent overrides go in `agents.list[].sandbox`):

Copy
[code]
    {
      "agents": {
        "defaults": {
          "sandbox": {
            "mode": "all", // off, non-main, all
            "backend": "docker", // docker, ssh, openshell
            "scope": "agent", // session, agent, shared
            "docker": {
              "image": "openclaw-sandbox:bookworm-slim",
              "containerPrefix": "openclaw-sbx-",
              // ... more Docker options
            },
            "prune": {
              "idleHours": 24, // Auto-prune after 24h idle
              "maxAgeDays": 7, // Auto-prune after 7 days
            },
          },
        },
      },
    }
    
[/code]

## 

​

See Also

  * [Sandbox Documentation](</gateway/sandboxing>)
  * [Agent Configuration](</concepts/agent-workspace>)
  * [Doctor Command](</gateway/doctor>) \- Check sandbox setup


[nodes](</cli/nodes>)[config](</cli/config>)

⌘I