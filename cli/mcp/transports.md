---
title: Transports and OAuth
source_url: https://docs.openclaw.ai/cli/mcp/transports
scraped_at: 2026-09-14
---

ReferenceCLI commands

These are the transport shapes a saved MCP server definition can use, and the OAuth workflow that HTTP transports can authenticate with.

## Stdio transport

Launches a local child process and communicates over stdin/stdout.

Field | Description  
---|---  
`command` | Executable to spawn (required)  
`args` | Array of command-line arguments  
`env` | Extra environment variables  
`cwd` / `workingDirectory` | Working directory for the process  
  
## SSE / HTTP transport

Connects to a remote MCP server over HTTP Server-Sent Events.

Field | Description  
---|---  
`url` | HTTP or HTTPS URL of the remote server (required)  
`headers` | Optional key-value map of HTTP headers (for example auth tokens)  
`connectionTimeoutMs` | Per-server connection timeout in ms (optional)  
`requestTimeoutMs` | Per-server MCP request timeout in milliseconds  
`auth: "oauth"` | Use MCP OAuth credentials saved by `openclaw mcp login`  
`sslVerify` | Set false only for explicitly trusted private HTTPS endpoints  
`clientCert` / `clientKey` | mTLS client certificate and key paths  
`supportsParallelToolCalls` | Hint that concurrent calls are safe for this server  
  
Example:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "remote-tools": {        "url": "https://mcp.example.com",        "auth": "oauth",        "requestTimeoutMs": 20000,        "headers": {          "Authorization": "Bearer <token>"        }      }    }  }}
[/code]

Sensitive values in `url` (userinfo) and `headers` are redacted in logs and status output. `openclaw mcp doctor` warns when sensitive-looking `headers` or `env` entries contain literal values, so operators can move those values out of committed config.

## OAuth workflow

OAuth is for HTTP MCP servers that advertise the MCP OAuth flow. Static `Authorization` headers are ignored for a server while `auth: "oauth"` is enabled. By default, OAuth credentials are shared and operator-managed. Credentials saved by `openclaw mcp login` work with embedded MCP, CLI runners, and the local Codex app-server.

Native MCP OAuth sessions live in the owner-only shared SQLite database at `<state-dir>/state/openclaw.sqlite` (`mcp_oauth_stores`). The row can contain access and refresh tokens, dynamic client registration secrets, discovery metadata, and the temporary PKCE verifier. Refresh, login, and logout use the same SQLite lease, so parallel OpenClaw processes cannot consume one refresh token or resurrect a logged-out session.

Upgrades from the retired `<state-dir>/mcp-oauth/*.json` store are handled only by `openclaw doctor --fix`. Runtime code never reads, writes, or falls back to those files.

Until shared credentials are available, OpenClaw omits only that MCP server from the agent runtime instead of failing the agent turn. The operator, or an agent with shell access, can then run `openclaw mcp login <name>` and use the server on a later turn.

If a server rejects a token with `insufficient_scope`, OpenClaw preserves the requested scope and asks for `openclaw mcp login <name>` instead of repeating a refresh that cannot grant new scope. That login starts a new authorization request while keeping the previous token until replacement credentials are saved.

When a remote MCP service is already backed by a separate OpenClaw refresh-capable auth profile, you can optionally set `oauth.authProfileId`. OpenClaw refreshes either credential source before runtime projection and passes only the current access token to the downstream MCP client.

Set `oauth.identity: "per-requester"` when every authenticated sender should connect a separate account. Per-requester OAuth requires an HTTP server URL and cannot use `oauth.authProfileId`. Configure `gateway.publicOrigin` as the externally reachable HTTPS origin of the Gateway; HTTP is accepted only for literal loopback hosts (`localhost`, `127.0.0.1`, or `[::1]`) during local development. The provider redirects to `<gateway.publicOrigin>/oauth/mcp/callback` after authorization.

json5Copy code
[code]
    {  gateway: {    publicOrigin: "https://gateway.example.com",  },  mcp: {    servers: {      docs: {        url: "https://mcp.example.com/mcp",        transport: "streamable-http",        auth: "oauth",        oauth: {          identity: "per-requester",          scope: "docs.read",        },      },    },  },}
[/code]

The per-requester flow is sender-driven:

  1. The sender calls a tool from the server before connecting an account.
  2. OpenClaw returns a sign-in link for that sender instead of exposing another sender's credentials.
  3. The provider redirects through the Gateway callback. After the callback succeeds, the sender retries the tool call with their connected account.


If `gateway.publicOrigin` is missing, the sign-in result names that setting and `openclaw doctor` reports the same operator fix. `openclaw mcp login` and `openclaw mcp logout` remain operator-only commands for shared credentials; they do not manage per-requester accounts.

Sign-in links are single-use bearer links: any chat participant who opens one connects their own account to the sender the link was issued for. Use per-requester OAuth in channels where every trusted sender is mutually trusted; a requester-private sign-in handoff is tracked as follow-up work.

The shared operator flow uses the following commands:

* ### Save the server

Add or update the server with `auth: "oauth"` and any optional OAuth metadata.

bashCopy code
[code]
    openclaw mcp set docs '{"url":"https://mcp.example.com/mcp","transport":"streamable-http","auth":"oauth","oauth":{"scope":"docs.read"}}'
[/code]

For an auth-profile-backed bearer, save the profile binding:

bashCopy code
[code]
    openclaw mcp set docs '{"url":"https://mcp.example.com/mcp","transport":"streamable-http","auth":"oauth","oauth":{"authProfileId":"docs:mcp"}}'
[/code]

* ### Start login

Run login to create the authorization request.

bashCopy code
[code]
    openclaw mcp login docs
[/code]

OpenClaw starts the registered loopback callback, prints the authorization URL, and stores temporary OAuth verifier state in shared SQLite. Approve the request in the browser and return to the terminal; token exchange completes automatically after the callback arrives.

* ### Use the manual fallback when needed

If the browser runs on another machine or cannot reach the printed loopback address, copy the returned code and pass it back to OpenClaw.

bashCopy code
[code]
    openclaw mcp login docs --code abc123
[/code]

* ### Check authorization

Use status or doctor to confirm that tokens are present and do not require additional authorization. If status reports `authorization-required` or doctor asks for additional authorization, run `openclaw mcp login <name>` again.

bashCopy code
[code]
    openclaw mcp status --verboseopenclaw mcp doctor docs --probe
[/code]

* ### Clear credentials

Logout removes stored OAuth credentials but keeps the saved server definition.

bashCopy code
[code]
    openclaw mcp logout docs
[/code]

If the provider rotates tokens or the authorization state gets stuck, run `openclaw mcp logout <name>`, then repeat `login`. `logout` can clear credentials for a saved HTTP server even after `auth: "oauth"` has been removed from config, as long as the server name and URL still identify the credential store entry.

## Streamable HTTP transport

`streamable-http` is an additional transport option alongside `sse` and `stdio`. It uses HTTP streaming for bidirectional communication with remote MCP servers.

Field | Description  
---|---  
`url` | HTTP or HTTPS URL of the remote server (required)  
`transport` | Set to `"streamable-http"` to select this transport; when omitted, OpenClaw uses `sse`  
`headers` | Optional key-value map of HTTP headers (for example auth tokens)  
`connectionTimeoutMs` | Per-server connection timeout in ms (optional)  
`requestTimeoutMs` | Per-server MCP request timeout in milliseconds  
`auth: "oauth"` | Use MCP OAuth credentials saved by `openclaw mcp login`  
`sslVerify` | Set false only for explicitly trusted private HTTPS endpoints  
`clientCert` / `clientKey` | mTLS client certificate and key paths  
`supportsParallelToolCalls` | Hint that concurrent calls are safe for this server  
  
OpenClaw config uses `transport: "streamable-http"` as the canonical spelling. CLI-native MCP `type: "http"` values are accepted when saved through `openclaw mcp set` and repaired by `openclaw doctor --fix` in existing config, but `transport` is what embedded OpenClaw consumes directly.

Example:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "streaming-tools": {        "url": "https://mcp.example.com/stream",        "transport": "streamable-http",        "connectionTimeoutMs": 10000,        "requestTimeoutMs": 30000,        "headers": {          "Authorization": "Bearer <token>"        }      }    }  }}
[/code]

Was this useful?YesNo

Open issue