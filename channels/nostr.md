---
title: Nostr
source_url: https://docs.openclaw.ai/channels/nostr
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Messaging platforms

Nostr

# 

​

Nostr

**Status:** Optional plugin (disabled by default). Nostr is a decentralized protocol for social networking. This channel enables OpenClaw to receive and respond to encrypted direct messages (DMs) via NIP-04.

## 

​

Install (on demand)

### 

​

Onboarding (recommended)

  * Onboarding (`openclaw onboard`) and `openclaw channels add` list optional channel plugins.
  * Selecting Nostr prompts you to install the plugin on demand.

Install defaults:

  * **Dev channel + git checkout available:** uses the local plugin path.
  * **Stable/Beta:** downloads from npm.

You can always override the choice in the prompt.

### 

​

Manual install

Copy
[code]
    openclaw plugins install @openclaw/nostr
    
[/code]

Use a local checkout (dev workflows):

Copy
[code]
    openclaw plugins install --link <path-to-openclaw>/extensions/nostr
    
[/code]

Restart the Gateway after installing or enabling plugins.

### 

​

Non-interactive setup

Copy
[code]
    openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY"
    openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY" --relay-urls "wss://relay.damus.io,wss://relay.primal.net"
    
[/code]

Use `--use-env` to keep `NOSTR_PRIVATE_KEY` in the environment instead of storing the key in config.

## 

​

Quick setup

  1. Generate a Nostr keypair (if needed):


Copy
[code]
    # Using nak
    nak key generate
    
[/code]

  2. Add to config:


Copy
[code]
    {
      channels: {
        nostr: {
          privateKey: "${NOSTR_PRIVATE_KEY}",
        },
      },
    }
    
[/code]

  3. Export the key:


Copy
[code]
    export NOSTR_PRIVATE_KEY="nsec1..."
    
[/code]

  4. Restart the Gateway.


## 

​

Configuration reference

Key| Type| Default| Description  
---|---|---|---  
`privateKey`| string| required| Private key in `nsec` or hex format  
`relays`| string[]| `['wss://relay.damus.io', 'wss://nos.lol']`| Relay URLs (WebSocket)  
`dmPolicy`| string| `pairing`| DM access policy  
`allowFrom`| string[]| `[]`| Allowed sender pubkeys  
`enabled`| boolean| `true`| Enable/disable channel  
`name`| string| -| Display name  
`profile`| object| -| NIP-01 profile metadata  
  
## 

​

Profile metadata

Profile data is published as a NIP-01 `kind:0` event. You can manage it from the Control UI (Channels -> Nostr -> Profile) or set it directly in config. Example:

Copy
[code]
    {
      channels: {
        nostr: {
          privateKey: "${NOSTR_PRIVATE_KEY}",
          profile: {
            name: "openclaw",
            displayName: "OpenClaw",
            about: "Personal assistant DM bot",
            picture: "https://example.com/avatar.png",
            banner: "https://example.com/banner.png",
            website: "https://example.com",
            nip05: "openclaw@example.com",
            lud16: "openclaw@example.com",
          },
        },
      },
    }
    
[/code]

Notes:

  * Profile URLs must use `https://`.
  * Importing from relays merges fields and preserves local overrides.


## 

​

Access control

### 

​

DM policies

  * **pairing** (default): unknown senders get a pairing code.
  * **allowlist** : only pubkeys in `allowFrom` can DM.
  * **open** : public inbound DMs (requires `allowFrom: ["*"]`).
  * **disabled** : ignore inbound DMs.


### 

​

Allowlist example

Copy
[code]
    {
      channels: {
        nostr: {
          privateKey: "${NOSTR_PRIVATE_KEY}",
          dmPolicy: "allowlist",
          allowFrom: ["npub1abc...", "npub1xyz..."],
        },
      },
    }
    
[/code]

## 

​

Key formats

Accepted formats:

  * **Private key:** `nsec...` or 64-char hex
  * **Pubkeys (`allowFrom`):** `npub...` or hex


## 

​

Relays

Defaults: `relay.damus.io` and `nos.lol`.

Copy
[code]
    {
      channels: {
        nostr: {
          privateKey: "${NOSTR_PRIVATE_KEY}",
          relays: ["wss://relay.damus.io", "wss://relay.primal.net", "wss://nostr.wine"],
        },
      },
    }
    
[/code]

Tips:

  * Use 2-3 relays for redundancy.
  * Avoid too many relays (latency, duplication).
  * Paid relays can improve reliability.
  * Local relays are fine for testing (`ws://localhost:7777`).


## 

​

Protocol support

NIP| Status| Description  
---|---|---  
NIP-01| Supported| Basic event format + profile metadata  
NIP-04| Supported| Encrypted DMs (`kind:4`)  
NIP-17| Planned| Gift-wrapped DMs  
NIP-44| Planned| Versioned encryption  
  
## 

​

Testing

### 

​

Local relay

Copy
[code]
    # Start strfry
    docker run -p 7777:7777 ghcr.io/hoytech/strfry
    
[/code]

Copy
[code]
    {
      channels: {
        nostr: {
          privateKey: "${NOSTR_PRIVATE_KEY}",
          relays: ["ws://localhost:7777"],
        },
      },
    }
    
[/code]

### 

​

Manual test

  1. Note the bot pubkey (npub) from logs.
  2. Open a Nostr client (Damus, Amethyst, etc.).
  3. DM the bot pubkey.
  4. Verify the response.


## 

​

Troubleshooting

### 

​

Not receiving messages

  * Verify the private key is valid.
  * Ensure relay URLs are reachable and use `wss://` (or `ws://` for local).
  * Confirm `enabled` is not `false`.
  * Check Gateway logs for relay connection errors.


### 

​

Not sending responses

  * Check relay accepts writes.
  * Verify outbound connectivity.
  * Watch for relay rate limits.


### 

​

Duplicate responses

  * Expected when using multiple relays.
  * Messages are deduplicated by event ID; only the first delivery triggers a response.


## 

​

Security

  * Never commit private keys.
  * Use environment variables for keys.
  * Consider `allowlist` for production bots.


## 

​

Limitations (MVP)

  * Direct messages only (no group chats).
  * No media attachments.
  * NIP-04 only (NIP-17 gift-wrap planned).


[Nextcloud Talk](</channels/nextcloud-talk>)[Signal](</channels/signal>)

⌘I