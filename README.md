# Openclaw Documentation

> This repository contains a local Markdown mirror of the official [Openclaw documentation](https://docs.openclaw.ai/).
> It is automatically updated every Monday to reflect any changes in the upstream documentation.

**Last updated:** 2026-10-05

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

- [Chat channels](channels.md) — [source](https://docs.openclaw.ai/channels)
- [X / Twitter](channels/x.md) — [source](https://docs.openclaw.ai/channels/x)

### Concepts

- [Features](concepts/features.md) — [source](https://docs.openclaw.ai/concepts/features)
- [Gateway architecture](concepts/architecture.md) — [source](https://docs.openclaw.ai/concepts/architecture)
- [Storage locations](concepts/storage-locations.md) — [source](https://docs.openclaw.ai/concepts/storage-locations)

### Tools

- [Overview](tools.md) — [source](https://docs.openclaw.ai/tools)

### Providers

- [Kie AI](providers/kie.md) — [source](https://docs.openclaw.ai/providers/kie)
- [Provider directory](providers.md) — [source](https://docs.openclaw.ai/providers)

### Platforms

- [Platforms](platforms.md) — [source](https://docs.openclaw.ai/platforms)

### Gateway

- [Gateway runbook](gateway.md) — [source](https://docs.openclaw.ai/gateway)

### Cli

- [CLI reference](cli.md) — [source](https://docs.openclaw.ai/cli)
- [Users](cli/users.md) — [source](https://docs.openclaw.ai/cli/users)
- [storage](cli/storage.md) — [source](https://docs.openclaw.ai/cli/storage)

### Help

- [Help](help.md) — [source](https://docs.openclaw.ai/help)

### Vps

- [Linux server](vps.md) — [source](https://docs.openclaw.ai/vps)

### Plugins

- [Agents API](plugins/agentsapi.md) — [source](https://docs.openclaw.ai/plugins/agentsapi)
- [Cloudflare](plugins/cloudflare.md) — [source](https://docs.openclaw.ai/plugins/cloudflare)
- [Slack huddles plugin](plugins/slack-huddles.md) — [source](https://docs.openclaw.ai/plugins/slack-huddles)

### Reference

- [Database access in workers](reference/database-schemas/worker-access.md) — [source](https://docs.openclaw.ai/reference/database-schemas/worker-access)
- [Database worker migration inventory](reference/database-schemas/worker-access-inventory.md) — [source](https://docs.openclaw.ai/reference/database-schemas/worker-access-inventory)
- [Session transcript working sets](reference/session-management-compaction/resident-history.md) — [source](https://docs.openclaw.ai/reference/session-management-compaction/resident-history)

### Releases

- [v2026.9.7](releases/2026.9.7.md) — [source](https://docs.openclaw.ai/releases/2026.9.7)
- [v2026.9.8](releases/2026.9.8.md) — [source](https://docs.openclaw.ai/releases/2026.9.8)

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
