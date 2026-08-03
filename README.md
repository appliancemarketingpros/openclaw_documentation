# Openclaw Documentation

> This repository contains a local Markdown mirror of the official [Openclaw documentation](https://docs.openclaw.ai/).
> It is automatically updated every Monday to reflect any changes in the upstream documentation.

**Last updated:** 2026-08-03

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

- [Daytona](install/daytona.md) — [source](https://docs.openclaw.ai/install/daytona)
- [Install](install.md) — [source](https://docs.openclaw.ai/install)

### Channels

- [Buzz](channels/buzz.md) — [source](https://docs.openclaw.ai/channels/buzz)
- [Chat channels](channels.md) — [source](https://docs.openclaw.ai/channels)

### Concepts

- [Agent bindings](concepts/agent-bindings.md) — [source](https://docs.openclaw.ai/concepts/agent-bindings)
- [Features](concepts/features.md) — [source](https://docs.openclaw.ai/concepts/features)
- [Gateway architecture](concepts/architecture.md) — [source](https://docs.openclaw.ai/concepts/architecture)
- [Memory architecture](concepts/memory-architecture.md) — [source](https://docs.openclaw.ai/concepts/memory-architecture)
- [Standing intents](concepts/standing-intents.md) — [source](https://docs.openclaw.ai/concepts/standing-intents)
- [User model](concepts/user-model.md) — [source](https://docs.openclaw.ai/concepts/user-model)

### Tools

- [Connect MCP servers](tools/mcp.md) — [source](https://docs.openclaw.ai/tools/mcp)
- [Overview](tools.md) — [source](https://docs.openclaw.ai/tools)

### Providers

- [Fish Audio](providers/fish-audio.md) — [source](https://docs.openclaw.ai/providers/fish-audio)
- [Provider directory](providers.md) — [source](https://docs.openclaw.ai/providers)

### Platforms

- [Platforms](platforms.md) — [source](https://docs.openclaw.ai/platforms)

### Gateway

- [Dependency locking](gateway/security/dependency-locking.md) — [source](https://docs.openclaw.ai/gateway/security/dependency-locking)
- [Gateway runbook](gateway.md) — [source](https://docs.openclaw.ai/gateway)
- [Give your Gateway a stable HTTPS URL](gateway/stable-https-url.md) — [source](https://docs.openclaw.ai/gateway/stable-https-url)

### Cli

- [CLI reference](cli.md) — [source](https://docs.openclaw.ai/cli)

### Help

- [Help](help.md) — [source](https://docs.openclaw.ai/help)

### Vps

- [Linux server](vps.md) — [source](https://docs.openclaw.ai/vps)

### Nodes

- [Media playback](nodes/media-playback.md) — [source](https://docs.openclaw.ai/nodes/media-playback)

### Plugins

- [Beam plugin](plugins/beam.md) — [source](https://docs.openclaw.ai/plugins/beam)

### Web

- [Control UI URLs](web/urls.md) — [source](https://docs.openclaw.ai/web/urls)
- [Notifications](web/notifications.md) — [source](https://docs.openclaw.ai/web/notifications)

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
