---
title: iMessage troubleshooting
source_url: https://docs.openclaw.ai/channels/imessage/troubleshooting
scraped_at: 2026-09-14
---

ChannelsMainstream messaging

Symptom-first fixes for the iMessage channel, plus the configuration reference links.

## Troubleshooting

imsg not found or RPC unsupported

Validate the binary and RPC support:

bashCopy code
[code]
    imsg rpc --helpimsg status --jsonopenclaw channels status --probe
[/code]

If the probe reports RPC unsupported, update `imsg`. If private API actions are unavailable, run `imsg launch` in the logged-in macOS user session and probe again. If the Gateway is not running on macOS, use the [Remote Mac over SSH](</channels/imessage/setup#remote-mac-over-ssh>) setup instead of the default local `imsg` path.

Messages send but inbound iMessages do not arrive

First prove whether the message reached the local Mac. If `chat.db` does not change, OpenClaw cannot receive the message even when `imsg status --json` reports a healthy bridge.

bashCopy code
[code]
    imsg chats --limit 10 --jsonimsg watch --chat-id <chat-id> --jsonsqlite3 ~/Library/Messages/chat.db \"select datetime(max(date)/1000000000 + 978307200, 'unixepoch', 'localtime'), max(ROWID) from message;"
[/code]

If phone-sent messages create no new rows, repair the macOS Messages and Apple Push layer before changing OpenClaw config. A one-shot service refresh is often enough:

bashCopy code
[code]
    launchctl kickstart -k system/com.apple.apsdlaunchctl kickstart -k gui/$(id -u)/com.apple.CommCenterlaunchctl kickstart -k gui/$(id -u)/com.apple.identityservicesdlaunchctl kickstart -k gui/$(id -u)/com.apple.imagentimsg launchopenclaw gateway restart
[/code]

Send a fresh iMessage from the phone and confirm a new `chat.db` row or `imsg watch` event before debugging OpenClaw sessions. Do not run this as a periodic bridge-relaunch loop; repeated `imsg launch` plus gateway restarts during active work can interrupt deliveries and strand in-flight channel runs.

Gateway is not running on macOS

The default `cliPath: "imsg"` must run on the Mac signed into Messages. On Linux or Windows, set `channels.imessage.cliPath` to a wrapper script that SSHes to that Mac and runs `imsg "$@"`.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T messages-mac imsg "$@"
[/code]

Then run:

bashCopy code
[code]
    openclaw channels status --probe --channel imessage
[/code]

DMs are ignored

Check:

  * `channels.imessage.dmPolicy`
  * `channels.imessage.allowFrom`
  * pairing approvals (`openclaw pairing list imessage`)

Group messages are ignored

Check:

  * `channels.imessage.groupPolicy`
  * `channels.imessage.groupAllowFrom`
  * `channels.imessage.groups` allowlist behavior
  * mention gating: explicit patterns or the routed agent's identity name/emoji; set `requireMention: false` for the chat in the effective root or account `groups` map to process all messages from allowed senders

Remote attachments fail

Check:

  * `channels.imessage.remoteHost`
  * `channels.imessage.remoteAttachmentRoots`
  * SSH/SCP key auth from the gateway host
  * host key exists in `~/.ssh/known_hosts` on the gateway host
  * remote path readability on the Mac running Messages

macOS permission prompts were missed

Re-run in an interactive GUI terminal in the same user/session context and approve prompts:

bashCopy code
[code]
    imsg chats --limit 1imsg send <handle> "test"
[/code]

Confirm Full Disk Access + Automation are granted for the process context that runs OpenClaw/`imsg`.

## Configuration reference pointers

  * [Configuration reference - iMessage](</gateway/config-channels#imessage>)
  * [Gateway configuration](</gateway/configuration>)
  * [Pairing](</channels/pairing>)


## Related

  * [Channels Overview](</channels>) — all supported channels
  * [BlueBubbles removal and the imsg iMessage path](</announcements/bluebubbles-imessage>) — announcement and migration summary
  * [Coming from BlueBubbles](</channels/imessage-from-bluebubbles>) — config translation table and step-by-step cutover
  * [Pairing](</channels/pairing>) — DM authentication and pairing flow
  * [Groups](</channels/groups>) — group chat behavior and mention gating
  * [Channel routing](</channels/channel-routing>) — session routing for messages
  * [Security](</gateway/security>) — access model and hardening


Was this useful?YesNo

Open issue