# Openclaw Documentation

> This repository contains a local Markdown mirror of the official [Openclaw documentation](https://docs.openclaw.ai/).
> It is automatically updated every Monday to reflect any changes in the upstream documentation.

**Last updated:** 2026-11-09

## Documentation Index

### Overview

- [OpenClaw](index.md) — [source](https://docs.openclaw.ai/)

### Start

- [CLI automation](start/wizard-cli-automation.md) — [source](https://docs.openclaw.ai/start/wizard-cli-automation)
- [CLI setup reference](start/wizard-cli-reference.md) — [source](https://docs.openclaw.ai/start/wizard-cli-reference)
- [Getting started](start/getting-started.md) — [source](https://docs.openclaw.ai/start/getting-started)
- [Multiplayer](start/multiplayer.md) — [source](https://docs.openclaw.ai/start/multiplayer)
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

### Concepts

- [Features](concepts/features.md) — [source](https://docs.openclaw.ai/concepts/features)
- [Gateway architecture](concepts/architecture.md) — [source](https://docs.openclaw.ai/concepts/architecture)

### Tools

- [Deep Research](tools/deep-research.md) — [source](https://docs.openclaw.ai/tools/deep-research)
- [Overview](tools.md) — [source](https://docs.openclaw.ai/tools)

### Providers

- [Provider directory](providers.md) — [source](https://docs.openclaw.ai/providers)
- [Rerank (Decision models)](providers/rerank.md) — [source](https://docs.openclaw.ai/providers/rerank)

### Platforms

- [Platforms](platforms.md) — [source](https://docs.openclaw.ai/platforms)

### Gateway

- [Gateway runbook](gateway.md) — [source](https://docs.openclaw.ai/gateway)

### Cli

- [CLI reference](cli.md) — [source](https://docs.openclaw.ai/cli)

### Help

- [Help](help.md) — [source](https://docs.openclaw.ai/help)

### Vps

- [Linux server](vps.md) — [source](https://docs.openclaw.ai/vps)

### Plugins

- [Research adapters](plugins/research-adapters.md) — [source](https://docs.openclaw.ai/plugins/research-adapters)

### Releases

- [v2026.10.10](releases/2026.10.10.md) — [source](https://docs.openclaw.ai/releases/2026.10.10)
- [v2026.11.1](releases/2026.11.1.md) — [source](https://docs.openclaw.ai/releases/2026.11.1)
- [v2026.11.2](releases/2026.11.2.md) — [source](https://docs.openclaw.ai/releases/2026.11.2)

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
