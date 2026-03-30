# Openclaw Documentation

> This repository contains a local Markdown mirror of the official [Openclaw documentation](https://docs.openclaw.ai/).
> It is automatically updated every Monday to reflect any changes in the upstream documentation.

**Last updated:** 2026-03-30

## Documentation Index

### Overview

- [OpenClaw](index.md) — [source](https://docs.openclaw.ai/)

### Start

- [CLI Automation](start/wizard-cli-automation.md) — [source](https://docs.openclaw.ai/start/wizard-cli-automation)
- [CLI Setup Reference](start/wizard-cli-reference.md) — [source](https://docs.openclaw.ai/start/wizard-cli-reference)
- [Getting Started](start/getting-started.md) — [source](https://docs.openclaw.ai/start/getting-started)
- [Onboarding (CLI)](start/wizard.md) — [source](https://docs.openclaw.ai/start/wizard)
- [Onboarding (macOS App)](start/onboarding.md) — [source](https://docs.openclaw.ai/start/onboarding)
- [Onboarding Overview](start/onboarding-overview.md) — [source](https://docs.openclaw.ai/start/onboarding-overview)
- [Personal Assistant Setup](start/openclaw.md) — [source](https://docs.openclaw.ai/start/openclaw)
- [Setup](start/setup.md) — [source](https://docs.openclaw.ai/start/setup)
- [Showcase](start/showcase.md) — [source](https://docs.openclaw.ai/start/showcase)

### Install

- [ClawDock](install/clawdock.md) — [source](https://docs.openclaw.ai/install/clawdock)
- [Install](install.md) — [source](https://docs.openclaw.ai/install)

### Channels

- [Chat Channels](channels.md) — [source](https://docs.openclaw.ai/channels)

### Concepts

- [Features](concepts/features.md) — [source](https://docs.openclaw.ai/concepts/features)
- [Gateway Architecture](concepts/architecture.md) — [source](https://docs.openclaw.ai/concepts/architecture)

### Tools

- [Image Generation](tools/image-generation.md) — [source](https://docs.openclaw.ai/tools/image-generation)
- [Tools and Plugins](tools.md) — [source](https://docs.openclaw.ai/tools)

### Providers

- [Provider Directory](providers.md) — [source](https://docs.openclaw.ai/providers)

### Platforms

- [Platforms](platforms.md) — [source](https://docs.openclaw.ai/platforms)

### Gateway

- [Gateway Runbook](gateway.md) — [source](https://docs.openclaw.ai/gateway)

### Cli

- [CLI Reference](cli.md) — [source](https://docs.openclaw.ai/cli)
- [CLI Reference](cli/index.md) — [source](https://docs.openclaw.ai/cli/index)

### Help

- [Help](help.md) — [source](https://docs.openclaw.ai/help)

### Vps

- [Linux Server](vps.md) — [source](https://docs.openclaw.ai/vps)

### Automation

- [Automation Overview](automation.md) — [source](https://docs.openclaw.ai/automation)
- [Background Tasks](automation/tasks.md) — [source](https://docs.openclaw.ai/automation/tasks)

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
