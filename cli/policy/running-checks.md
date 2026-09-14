---
title: Run and configure policy checks
source_url: https://docs.openclaw.ai/cli/policy/running-checks
scraped_at: 2026-09-14
---

ReferenceCLI commands

Running checks during authoring, and the plugin settings behind them. Part of the [`openclaw policy`](</cli/policy>) reference.

## Run checks

Run policy-only checks during authoring:

bashCopy code
[code]
    openclaw policy checkopenclaw policy check --agent opsopenclaw policy check --jsonopenclaw policy check --severity-min error
[/code]

`policy check` runs only the policy check set and emits evidence, findings, and attestation hashes. The same findings also appear in `openclaw doctor --lint` when the Policy plugin is enabled. In a multi-agent fleet with explicit ownership, pass `--agent <id>` so the command reads governed declarations and `policy.jsonc` from that agent's workspace. A sole-agent or retained legacy-owner configuration still resolves without the flag; OpenClaw never selects an arbitrary first agent.

Compare an operator policy file against an authored baseline:

bashCopy code
[code]
    openclaw policy compare --baseline official.policy.jsoncopenclaw policy compare --baseline official.policy.jsonc --agent opsopenclaw policy compare --baseline official.policy.jsonc --policy policy.jsonc --json
[/code]

`policy compare` checks policy-file syntax against policy-file syntax; it does not inspect runtime state, evidence, credentials, or secrets. It uses the same rule metadata that governs scoped overlays: allowlists must stay equal or narrower, denylists must stay equal or broader, required booleans must keep their value, ordered strings may only move toward the stricter end of the configured order, and exact lists must match. The baseline can be an organization-authored policy; the checked policy may add stricter values or extra rules. A top-level checked rule can satisfy a scoped baseline rule when it is equally or more restrictive. Scope names do not need to match between files; comparison is keyed by selector (`agentIds`/`channelIds`) and field. For routing probes, every baseline probe id must remain with the same route and expected agent. A checked policy may add probes or narrow `matchedBy`, but removing a probe, changing its route or agent, or widening its accepted match kinds is weaker. When the checked policy path comes from the plugin configuration and is relative, `--agent <id>` selects the workspace used to resolve it. Absolute policy paths do not depend on an agent workspace.

Clean compare (`--json`):

jsonCopy code
[code]
    {  "ok": true,  "baselinePath": "official.policy.jsonc",  "policyPath": "policy.jsonc",  "rulesChecked": 3,  "findings": []}
[/code]

Clean `policy check --json` output includes stable hashes an operator or supervisor can record:

jsonCopy code
[code]
    {  "ok": true,  "attestation": {    "policy": {      "path": "policy.jsonc",      "hash": "sha256:..."    },    "workspace": {      "scope": "policy",      "hash": "sha256:..."    },    "findingsHash": "sha256:...",    "attestationHash": "sha256:..."  },  "checksRun": 5,  "checksSkipped": 0,  "findings": []}
[/code]

## Configure policy

Policy config lives under `plugins.entries.policy.config`.

jsoncCopy code
[code]
    {  "plugins": {    "entries": {      "policy": {        "enabled": true,        "config": {          "enabled": true,          "path": "policy.jsonc",          "workspaceRepairs": false,          "expectedHash": "sha256:...",          "expectedAttestationHash": "sha256:...",        },      },    },  },}
[/code]

Setting | Purpose  
---|---  
`enabled` | Enable policy checks even before `policy.jsonc` exists.  
`workspaceRepairs` | Allow `doctor --fix` to edit policy-managed workspace settings.  
`expectedHash` | Optional hash-lock for the approved policy artifact.  
`expectedAttestationHash` | Optional hash-lock for the last accepted clean policy check.  
`path` | Workspace-relative location of the policy artifact.  
  
Set `plugins.entries.policy.config.enabled` to `false` to disable policy checks for a workspace while leaving the plugin installed.

Was this useful?YesNo

Open issue