# Openclaw Documentation

> This repository contains a local Markdown mirror of the official [Openclaw documentation](https://docs.openclaw.ai/).
> It is automatically updated every Monday to reflect any changes in the upstream documentation.

**Last updated:** 2026-10-19

## Documentation Index

### Overview

- [OpenClaw](index.md) — [source](https://docs.openclaw.ai/)

### Start

- [CLI automation](start/wizard-cli-automation.md) — [source](https://docs.openclaw.ai/start/wizard-cli-automation)
- [CLI setup reference](start/wizard-cli-reference.md) — [source](https://docs.openclaw.ai/start/wizard-cli-reference)
- [Getting started](start/getting-started.md) — [source](https://docs.openclaw.ai/start/getting-started)
- [Onboarding (CLI)](start/wizard.md) — [source](https://docs.openclaw.ai/start/wizard)
- [Onboarding (macOS app)](start/onboarding.md) — [source](https://docs.openclaw.ai/start/onboarding)
- [Onboarding overview](start/onboarding-overview.md) — [source](https://docs.openclaw.ai/start/onboarding-overview)
- [Personal assistant setup](start/openclaw.md) — [source](https://docs.openclaw.ai/start/openclaw)
- [Setup](start/setup.md) — [source](https://docs.openclaw.ai/start/setup)
- [Showcase](start/showcase.md) — [source](https://docs.openclaw.ai/start/showcase)

### Install

- [Install](install.md) — [source](https://docs.openclaw.ai/install)
- [Standalone builds](install/standalone.md) — [source](https://docs.openclaw.ai/install/standalone)

### Channels

- [Chat channels](channels.md) — [source](https://docs.openclaw.ai/channels)

### Concepts

- [Features](concepts/features.md) — [source](https://docs.openclaw.ai/concepts/features)
- [Gateway architecture](concepts/architecture.md) — [source](https://docs.openclaw.ai/concepts/architecture)
- [Session controller](concepts/session-controller.md) — [source](https://docs.openclaw.ai/concepts/session-controller)

### Tools

- [Auto Review](tools/autoreview.md) — [source](https://docs.openclaw.ai/tools/autoreview)
- [Overview](tools.md) — [source](https://docs.openclaw.ai/tools)

### Providers

- [Levanto Sage](providers/levanto.md) — [source](https://docs.openclaw.ai/providers/levanto)
- [Neon AI Gateway](providers/neon.md) — [source](https://docs.openclaw.ai/providers/neon)
- [Poolside (Laguna)](providers/poolside.md) — [source](https://docs.openclaw.ai/providers/poolside)
- [Provider directory](providers.md) — [source](https://docs.openclaw.ai/providers)
- [oMLX](providers/omlx.md) — [source](https://docs.openclaw.ai/providers/omlx)

### Platforms

- [Platforms](platforms.md) — [source](https://docs.openclaw.ai/platforms)

### Gateway

- [Cloud environment file](gateway/cloud-workers/environment-file.md) — [source](https://docs.openclaw.ai/gateway/cloud-workers/environment-file)
- [Gateway runbook](gateway.md) — [source](https://docs.openclaw.ai/gateway)
- [PostgreSQL operator guide](gateway/postgresql.md) — [source](https://docs.openclaw.ai/gateway/postgresql)

### Cli

- [CLI reference](cli.md) — [source](https://docs.openclaw.ai/cli)

### Help

- [Help](help.md) — [source](https://docs.openclaw.ai/help)

### Vps

- [Linux server](vps.md) — [source](https://docs.openclaw.ai/vps)

### Automation

- [MCP Events](automation/mcp-events.md) — [source](https://docs.openclaw.ai/automation/mcp-events)

### Plugins

- [Agent Guidance](plugins/agent-guidance.md) — [source](https://docs.openclaw.ai/plugins/agent-guidance)
- [Awaited transcript and TTS helpers](plugins/sdk-migration/async-transcript-and-tts.md) — [source](https://docs.openclaw.ai/plugins/sdk-migration/async-transcript-and-tts)
- [MCP Relay](plugins/mcp-relay.md) — [source](https://docs.openclaw.ai/plugins/mcp-relay)
- [Migrate synchronous SQLite APIs](plugins/sdk-migration/sqlite-async.md) — [source](https://docs.openclaw.ai/plugins/sdk-migration/sqlite-async)
- [Muse Code agent runtime](plugins/muse.md) — [source](https://docs.openclaw.ai/plugins/muse)
- [Remote Control UI ingress](plugins/sdk-gateway-ingress.md) — [source](https://docs.openclaw.ai/plugins/sdk-gateway-ingress)
- [SubQ](plugins/subq.md) — [source](https://docs.openclaw.ai/plugins/subq)

### Reference

- [Database engines (experimental)](reference/database-engines.md) — [source](https://docs.openclaw.ai/reference/database-engines)

### Releases

- [v2026.10.2](releases/2026.10.2.md) — [source](https://docs.openclaw.ai/releases/2026.10.2)
- [v2026.10.3](releases/2026.10.3.md) — [source](https://docs.openclaw.ai/releases/2026.10.3)
- [v2026.10.4](releases/2026.10.4.md) — [source](https://docs.openclaw.ai/releases/2026.10.4)

### Sv

- [Kom igång](sv/start/getting-started.md) — [source](https://docs.openclaw.ai/sv/start/getting-started)
- [LINE](sv/channels/line.md) — [source](https://docs.openclaw.ai/sv/channels/line)
- [OpenClaw](sv.md) — [source](https://docs.openclaw.ai/sv)

---

## About This Repository

This documentation mirror is maintained automatically via a GitHub Actions workflow
that runs every Monday at 06:00 UTC. The workflow scrapes the official Openclaw
documentation site, detects changed pages using content hashing, and commits only
the modified files.

**Source:** https://docs.openclaw.ai/
**Openclaw GitHub:** https://github.com/openclaw/openclaw

## Usage with AI Tools

This repository is designed to serve as a reference for AI tools managing Openclaw
installations. Each documentation page is stored as a clean Markdown file, organized
by section, making it easy for AI assistants to locate and reference specific
configuration, installation, or troubleshooting information.

### Sections at a Glance

| Section | Description |
|---------|-------------|
| `start/` | Getting started, onboarding, and setup guides |
| `install/` | Installation methods: Docker, Nix, cloud providers, and more |
| `channels/` | Channel setup: WhatsApp, Telegram, Discord, iMessage, etc. |
| `gateway/` | Gateway configuration, security, routing, and API reference |
| `tools/` | Tools and plugins: browser, search, exec, and more |
| `providers/` | AI model provider configuration (Anthropic, OpenAI, Google, etc.) |
| `platforms/` | Platform-specific guides (Windows, macOS, Linux) |
| `concepts/` | Architecture overview and feature reference |
| `cli/` | Full CLI command reference |
| `help/` | Troubleshooting and diagnostics |
| `nodes/` | iOS and Android node setup |
| `security/` | Security, tokens, and access controls |
