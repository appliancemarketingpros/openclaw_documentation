---
title: Verify a cloud worker profile
source_url: https://docs.openclaw.ai/gateway/cloud-workers/verify-the-profile
scraped_at: 2026-09-14
---

Gateway & OpsGateway

The checks to run before and after restarting the Gateway, and the end-to-end flow that read-only readiness checks do not substitute for.

## Verify the profile

Validate before restarting the Gateway:

bashCopy code
[code]
    openclaw config validate --jsonopenclaw plugins inspect crabbox --runtime --json
[/code]

Changes under `cloudWorkers.profiles` require a Gateway restart. The default `gateway.reload.mode: "hybrid"` watches the config and performs that restart automatically; with reload watching disabled, run `openclaw gateway restart`.

To use the same profile with Codex, enable a trusted Codex plugin installation on the Gateway and explicitly add `codex.exec-server.stdio.v1` to `gateway.nodes.commands.allow`. Bootstrap includes and enables the required plugin in the cloud node's isolated state automatically. Installing the runtime does not grant execution authority: persistent command enablement does not replace the critical launch approval. **Allow once** covers one exec-server launch; **Allow always** covers later launches only while the exact placement, node pairing, environment owner, command approval scope, and workspace stay current.

After the Gateway is back, prove the profile is advertised and compare it with Crabbox's read-only lease inventory:

bashCopy code
[code]
    openclaw gateway call environments.list --params '{}'crabbox list --provider aws --json
[/code]

The `environments.list` response must include the configured id under `profiles`. `crabbox list` is non-mutating. By contrast, `crabbox warmup` provisions a lease, and `crabbox stop` or `crabbox release` tears one down; use those mutating commands only when you intend to create or destroy cloud resources.

Before relying on a new profile, authorize provider spend and test allocation, setup, node enrollment, a turn in the selected runtime, and a workspace edit reconciled back to the Gateway. Test cancellation and interrupted-dispatch replay against the same lease, then stop the session and verify teardown using Crabbox's provider-specific cleanup contract. Read-only readiness checks and mocked tests are not substitutes for this end-to-end verification.

Was this useful?YesNo

Open issue