---
title: iMessage setup
source_url: https://docs.openclaw.ai/channels/imessage/setup
scraped_at: 2026-09-14
---

ChannelsMainstream messaging

Install the plugin, install and verify `imsg` on the signed-in Messages Mac, configure the channel, and grant the macOS permissions it needs.

## Install the plugin

Install the official iMessage plugin on the Gateway host:

bashCopy code
[code]
    openclaw plugins install @openclaw/imessage
[/code]

Check the [application result](</plugins/manage-plugins#apply-changes-and-inspect>) before continuing.

[**Private API actions** Replies, tapbacks, effects, polls, attachments, and group management. ](</channels/imessage/rich-messages#private-api-actions>) [**Pairing** iMessage DMs default to pairing mode. ](</channels/pairing>) **Remote Mac** Use an SSH wrapper when the Gateway is not running on the Messages Mac. [**Configuration reference** Full iMessage field reference. ](</gateway/config-channels#imessage>)

## Quick setup

### Local Mac (fast path)

* ### Install and verify imsg

bashCopy code
[code]
    brew install steipete/tap/imsgbrew update && brew upgrade imsgimsg rpc --helpimsg launchopenclaw channels status --probe
[/code]

When the local setup wizard detects a missing default `imsg` command, it can prompt to install `steipete/tap/imsg` through Homebrew. If it detects a Homebrew-managed `imsg`, it can prompt to reinstall or update it. Custom `cliPath` wrappers are not modified.

* ### Configure OpenClaw

json5Copy code
[code]
    {channels: {imessage: {enabled: true,cliPath: "/usr/local/bin/imsg",dbPath: "/Users/user/Library/Messages/chat.db",},},}
[/code]

* ### Start gateway

bashCopy code
[code]
    openclaw gateway
[/code]

* ### Approve first DM pairing (default dmPolicy)

bashCopy code
[code]
    openclaw pairing list imessageopenclaw pairing approve imessage <CODE>
[/code]

Pairing requests expire after 1 hour.

### Remote Mac over SSH

Most setups do not need SSH. Use this topology only when the Gateway cannot run on the signed-in Messages Mac. Point `cliPath` at a stdio-compatible wrapper on the **Gateway host** that SSHes to the Messages Mac and runs `imsg`. Use the wrapper's absolute path so service launches do not depend on shell home expansion. Install and update `imsg` on that remote Mac, not on the Gateway host:

bashCopy code
[code]
    ssh messages-mac 'brew install steipete/tap/imsg && brew update && brew upgrade imsg'
[/code]

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T messages-mac imsg "$@"
[/code]

Recommended config when attachments are enabled:

json5Copy code
[code]
    {channels: {imessage: {  enabled: true,  cliPath: "/home/openclaw/.openclaw/scripts/imsg-ssh",  remoteHost: "user@messages-mac", // Mac that runs Messages.app and imsg  // This path is interpreted on the Messages Mac, not on the Gateway host.  dbPath: "/Users/user/Library/Messages/chat.db",  includeAttachments: true,  // Optional: extra allowed attachment roots (merged with the default  // /Users/*/Library/Messages/Attachments).  attachmentRoots: ["/Users/*/Library/Messages/Attachments"],  remoteAttachmentRoots: ["/Users/*/Library/Messages/Attachments"],},},}
[/code]

`remoteHost` identifies the Messages Mac. OpenClaw uses it for both inbound attachment fetches and outbound attachment staging. For outbound files, OpenClaw creates an owner-only temporary path on that Mac, copies the file over the existing strict SSH/SCP transport, passes only the remote path to `imsg`, and attempts removal after success, failure, or timeout. A failed cleanup SSH call emits a warning and can leave the owner-only temporary directory behind.

An explicit `remoteHost` is recommended and wins when set. For compatibility, OpenClaw auto-detects the existing transparent `exec ssh ... imsg "$@"` wrapper shape once per process and reuses that host across monitoring, probes, sends, and private actions. Auto-detection covers only the simple documented transparent wrapper; option-rich wrappers such as ProxyJump/ProxyCommand must configure `remoteHost`. `remoteHost` must be `host` or `user@host` (no spaces or SSH options); unsafe values are ignored. OpenClaw uses strict host-key checking for SSH/SCP, so the Messages Mac host key must already exist in `~/.ssh/known_hosts` on the Gateway host. Attachment paths are validated against allowed roots (`attachmentRoots` / `remoteAttachmentRoots`).

## Requirements and permissions (macOS)

  * Messages must be signed in on the Mac running `imsg`.
  * Full Disk Access is required for the process context running OpenClaw/`imsg` (Messages DB access).
  * Automation permission is required to send messages through Messages.app.
  * For advanced actions (react / edit / unsend / threaded reply / effects / polls / group ops), System Integrity Protection must be disabled — see [Enabling the imsg private API](</channels/imessage/private-api#enabling-the-imsg-private-api>). Basic text and media send/receive work without it.

SSH wrapper sends fail with AppleEvents -1743

A remote-SSH setup can read chats, pass `channels status --probe`, and process inbound messages while outbound sends still fail with an AppleEvents authorization error:

textCopy code
[code]
    Not authorized to send Apple events to Messages. (-1743)
[/code]

Check the signed-in Mac user's TCC database or System Settings > Privacy & Security > Automation. If the Automation entry is recorded for `/usr/libexec/sshd-keygen-wrapper` instead of the `imsg` or local shell process, macOS may not expose a usable Messages toggle for that SSH server-side client:

textCopy code
[code]
    kTCCServiceAppleEvents | /usr/libexec/sshd-keygen-wrapper | auth_value=0 | com.apple.MobileSMS
[/code]

In that state, repeating `tccutil reset AppleEvents` or rerunning `imsg send` through the same SSH wrapper may keep failing because the process context that needs Messages Automation is the SSH wrapper, not an app the UI can grant.

Use one of the supported `imsg` process contexts instead:

  * Run the Gateway, or at least the `imsg` bridge, in the logged-in Messages user's local session.
  * Start the Gateway with a LaunchAgent for that user after granting Full Disk Access and Automation from the same session.
  * If you keep the two-user SSH topology, verify that a real outbound `imsg send` succeeds through the exact wrapper before enabling the channel. If it cannot be granted Automation, reconfigure to a single-user `imsg` setup instead of relying on the SSH wrapper for sends.


Was this useful?YesNo

Open issue