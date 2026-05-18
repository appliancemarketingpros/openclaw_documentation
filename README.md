# Openclaw Documentation

> This repository contains a local Markdown mirror of the official [Openclaw documentation](https://docs.openclaw.ai/).
> It is automatically updated every Monday to reflect any changes in the upstream documentation.

**Last updated:** 2026-05-18

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

### Channels

- [Ambient room events](channels/ambient-room-events.md) — [source](https://docs.openclaw.ai/channels/ambient-room-events)
- [Bot loop protection](channels/bot-loop-protection.md) — [source](https://docs.openclaw.ai/channels/bot-loop-protection)
- [Chat channels](channels.md) — [source](https://docs.openclaw.ai/channels)

### Concepts

- [Features](concepts/features.md) — [source](https://docs.openclaw.ai/concepts/features)
- [Gateway architecture](concepts/architecture.md) — [source](https://docs.openclaw.ai/concepts/architecture)
- [Personal agent benchmark pack](concepts/personal-agent-benchmark-pack.md) — [source](https://docs.openclaw.ai/concepts/personal-agent-benchmark-pack)

### Tools

- [Overview](tools.md) — [source](https://docs.openclaw.ai/tools)

### Providers

- [Provider directory](providers.md) — [source](https://docs.openclaw.ai/providers)
- [ds4](providers/ds4.md) — [source](https://docs.openclaw.ai/providers/ds4)

### Platforms

- [Platforms](platforms.md) — [source](https://docs.openclaw.ai/platforms)

### Gateway

- [Gateway runbook](gateway.md) — [source](https://docs.openclaw.ai/gateway)
- [Local model services](gateway/local-model-services.md) — [source](https://docs.openclaw.ai/gateway/local-model-services)
- [Operator scopes](gateway/operator-scopes.md) — [source](https://docs.openclaw.ai/gateway/operator-scopes)
- [Secure file operations](gateway/security/secure-file-operations.md) — [source](https://docs.openclaw.ai/gateway/security/secure-file-operations)
- [Security audit checks](gateway/security/audit-checks.md) — [source](https://docs.openclaw.ai/gateway/security/audit-checks)

### Cli

- [CLI reference](cli.md) — [source](https://docs.openclaw.ai/cli)

### Help

- [Help](help.md) — [source](https://docs.openclaw.ai/help)

### Vps

- [Linux server](vps.md) — [source](https://docs.openclaw.ai/vps)

### Plugins

- [Admin HTTP RPC plugin](plugins/admin-http-rpc.md) — [source](https://docs.openclaw.ai/plugins/admin-http-rpc)
- [Channel ingress API](plugins/sdk-channel-ingress.md) — [source](https://docs.openclaw.ai/plugins/sdk-channel-ingress)

### Reference

- [Code mode](reference/code-mode.md) — [source](https://docs.openclaw.ai/reference/code-mode)

### Announcements

- [BlueBubbles removal and the imsg iMessage path](announcements/bluebubbles-imessage.md) — [source](https://docs.openclaw.ai/announcements/bluebubbles-imessage)

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
