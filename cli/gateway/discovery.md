---
title: Discover gateways (Bonjour)
source_url: https://docs.openclaw.ai/cli/gateway/discovery
scraped_at: 2026-09-14
---

ReferenceCLI commands

Scanning for Gateway beacons over mDNS and wide-area DNS-SD. Part of the [`openclaw gateway`](</cli/gateway>) reference.

## Discover gateways (Bonjour)

`gateway discover` scans for Gateway beacons (`_openclaw-gw._tcp`).

  * Multicast DNS-SD: `local.`
  * Unicast DNS-SD (wide-area Bonjour): choose a domain (example: `openclaw.internal.`) and set up split DNS + a DNS server; see [Bonjour](</gateway/bonjour>).


Only gateways with Bonjour discovery enabled (default) advertise the beacon.

TXT hints on every beacon: `role` (gateway role hint), `transport` (transport hint, e.g. `gateway`), `gatewayPort` (WebSocket port, usually `18789`), `tailnetDns` (MagicDNS hostname, when available), `gatewayTls` / `gatewayTlsSha256` (TLS enabled + cert fingerprint). `sshPort` and `cliPath` are published only in full discovery mode (`discovery.mdns.mode: "full"`; default is `"minimal"`, which omits them — clients then default SSH targets to port `22`).

### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

Per-command timeout (browse/resolve).

Machine-readable output (also disables styling/spinner).

Examples:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

Was this useful?YesNo

Open issue