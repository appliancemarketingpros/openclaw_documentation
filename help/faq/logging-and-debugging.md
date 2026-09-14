---
title: Logging and debugging
source_url: https://docs.openclaw.ai/help/faq/logging-and-debugging
scraped_at: 2026-09-14
---

HelpFAQ

## Logging and debugging

Where are logs?

File logs (structured): `/tmp/openclaw/openclaw-YYYY-MM-DD.log` for the default profile, or `/tmp/openclaw/openclaw-<profile>-YYYY-MM-DD.log` for a named profile. Set a stable path via `logging.file`; file log level via `logging.level`; console verbosity via `--verbose` and `logging.consoleLevel`.

Fastest tail:

bashCopy code
[code]
    openclaw logs --follow
[/code]

Service/supervisor logs (when the gateway runs via launchd/systemd):

  * macOS launchd stdout and stderr: `~/Library/Logs/openclaw/gateway.log` (profiles use `gateway-<profile>.log`; both streams share this file, so startup failures that happen before the logger starts are recorded here too).
  * Linux: `journalctl --user -u openclaw-gateway[-<profile>].service -n 200 --no-pager`.
  * Windows: `schtasks /Query /TN "OpenClaw Gateway (<profile>)" /V /FO LIST`.


See [Troubleshooting](</gateway/troubleshooting>) for more.

How do I start/stop/restart the Gateway service? bashCopy code
[code]
    openclaw gateway statusopenclaw gateway restart
[/code]

If you run the gateway manually, `openclaw gateway --force` can reclaim the port. See [Gateway](</gateway>).

I closed my terminal on Windows - how do I restart OpenClaw?

Three Windows install modes:

**1) Windows Hub local setup** : the native app manages a local app-owned WSL Gateway. Open **OpenClaw Companion** from the Start menu or tray, then use **Gateway Setup** or the Connections tab.

**2) Manual WSL2 Gateway** : the Gateway runs inside Linux.

powershellCopy code
[code]
    wslopenclaw gateway statusopenclaw gateway restart
[/code]

If you never installed the service, start it in the foreground: `openclaw gateway run`.

**3) Native Windows CLI/Gateway** : runs directly in Windows.

powershellCopy code
[code]
    openclaw gateway statusopenclaw gateway restart
[/code]

If you run it manually (no service): `openclaw gateway run`.

Docs: [Windows](</platforms/windows>), [Gateway service runbook](</gateway>).

The Gateway is up but replies never arrive. What should I check?

Quick health sweep:

bashCopy code
[code]
    openclaw statusopenclaw models statusopenclaw channels statusopenclaw logs --follow
[/code]

Common causes: model auth not loaded on the **gateway host** (check `models status`), channel pairing/allowlist blocking replies (check channel config and logs), or WebChat/Dashboard open without the right token. If remote, confirm the tunnel/Tailscale connection is up and the Gateway WebSocket is reachable.

Docs: [Channels](</channels>), [Troubleshooting](</gateway/troubleshooting>), [Remote access](</gateway/remote>).

"Disconnected from gateway: no reason" - what now?

Usually means the UI lost the WebSocket connection. Check: is the Gateway running (`openclaw gateway status`)? Is it healthy (`openclaw status`)? Does the UI have the right token (`openclaw dashboard`)? If remote, is the tunnel/Tailscale link up?

Then tail logs:

bashCopy code
[code]
    openclaw logs --follow
[/code]

Docs: [Dashboard](</web/dashboard>), [Remote access](</gateway/remote>), [Troubleshooting](</gateway/troubleshooting>).

Telegram setMyCommands fails. What should I check? bashCopy code
[code]
    openclaw channels statusopenclaw channels logs --channel telegram
[/code]

Then match the error:

  * `BOT_COMMANDS_TOO_MUCH`: the Telegram menu has too many entries. OpenClaw already trims to the Telegram limit and retries with fewer commands, but some menu entries may still be dropped. Reduce plugin/skill/custom commands, or disable `channels.telegram.commands.native` if you do not need the menu.
  * `TypeError: fetch failed`, `Network request for 'setMyCommands' failed!`, or similar network errors: on a VPS or behind a proxy, confirm outbound HTTPS is allowed and DNS works for `api.telegram.org`.


If the Gateway is remote, check logs on the Gateway host.

Docs: [Telegram](</channels/telegram>), [Channel troubleshooting](</channels/troubleshooting>).

TUI shows no output. What should I check? bashCopy code
[code]
    openclaw statusopenclaw models statusopenclaw logs --follow
[/code]

In the TUI, use `/status` to see the current state. If you expect replies in a chat channel, confirm delivery is enabled (`/deliver on`).

Docs: [TUI](</web/tui>), [Slash commands](</tools/slash-commands>).

How do I completely stop then start the Gateway?

If you installed the service (launchd on macOS, systemd on Linux):

bashCopy code
[code]
    openclaw gateway stopopenclaw gateway start
[/code]

In the foreground, stop with Ctrl-C, then `openclaw gateway run`.

Docs: [Gateway service runbook](</gateway>).

ELI5: openclaw gateway restart vs openclaw gateway

`openclaw gateway restart` restarts the **background service** (launchd/systemd). `openclaw gateway` runs the gateway **in the foreground** for this terminal session. Use the gateway subcommands if you installed the service; use the bare foreground run for a one-off.

Fastest way to get more details when something fails

Start the Gateway with `--verbose` for more console detail, then inspect the log file for channel auth, model routing, and RPC errors.

Was this useful?YesNo

Open issue