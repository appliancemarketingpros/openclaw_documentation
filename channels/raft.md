---
title: Raft
source_url: https://docs.openclaw.ai/channels/raft
scraped_at: 2026-06-22
---

ChannelsDeveloper and self-hosted

Raft support connects an OpenClaw agent to a Raft External Agent through the local Raft CLI. Raft sends authenticated wake hints to the Gateway. The agent then uses the Raft CLI to check and send messages.

## Install

Raft is an official external plugin. Install it on the Gateway host:

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

Details: [Plugins](</tools/plugin>)

## Prerequisites

  * A Raft workspace with an External Agent.
  * The Raft CLI installed on the same host as the OpenClaw Gateway.
  * A Raft CLI profile that is already signed in and associated with that External Agent.


The plugin does not store Raft credentials. The Raft CLI keeps that authentication in its own profile.

## Configure

Set the profile in config:

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

For the default account, you can instead set `RAFT_PROFILE` in the Gateway environment:

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

Use a named account when one Gateway connects to more than one Raft External Agent:

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

The interactive setup flow records the same profile:

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## How It Works

When the Gateway starts, the plugin:

  1. Opens a loopback-only HTTP wake endpoint on an ephemeral port.
  2. Starts `raft --profile <profile> agent bridge` with that endpoint and a per-process token.
  3. Accepts only authenticated, content-free wake hints with a replay identity from the local bridge.
  4. Requires one of `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id`, or `id`.
  5. Deduplicates recent retried wake deliveries by bridge event id, including across Gateway restarts.
  6. Returns a stable runtime session for the current bridge and an empty activity-drain batch for the Raft CLI protocol.
  7. Starts one serialized OpenClaw agent turn for each accepted wake.


The bridge owns Raft delivery retries and reconnects. The OpenClaw turn receives only a wake notice, not a copied Raft message body. It uses the CLI to read pending messages and to send its response:

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## Verify

Check that OpenClaw can find the CLI and has a configured profile:

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

Then send a message to the Raft External Agent. The Gateway log should show the Raft bridge starting, followed by an inbound wake. The agent should use the configured Raft profile to check its pending messages.

## Troubleshooting

Raft CLI is missing

Install the Raft CLI on the Gateway host and make `raft` available on the service's `PATH`. Verify it with `raft --help`, then restart the Gateway.

The bridge exits immediately

Verify the configured profile is signed in and belongs to the intended Raft External Agent. Run `raft --profile <profile> agent bridge` directly to see the CLI diagnostic.

A wake arrives but no Raft response is sent

This is expected when the agent does not invoke the Raft CLI. The wake bridge does not carry message bodies or automatic final replies. Check the agent's tool policy and ensure it can run `raft --profile <profile> message check` and `message send`.

## References

  * [Raft](<https://raft.build/>)
  * [Raft documentation](<https://docs.raft.build/welcome/>)
  * [Hermes Raft integration](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue