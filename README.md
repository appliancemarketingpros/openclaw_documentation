# Openclaw Documentation

> This repository contains a local Markdown mirror of the official [Openclaw documentation](https://docs.openclaw.ai/).
> It is automatically updated every Monday to reflect any changes in the upstream documentation.

**Last updated:** 2026-06-01

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
- [SMS](channels/sms.md) — [source](https://docs.openclaw.ai/channels/sms)

### Concepts

- [Features](concepts/features.md) — [source](https://docs.openclaw.ai/concepts/features)
- [Gateway architecture](concepts/architecture.md) — [source](https://docs.openclaw.ai/concepts/architecture)

### Tools

- [Goal](tools/goal.md) — [source](https://docs.openclaw.ai/tools/goal)
- [Overview](tools.md) — [source](https://docs.openclaw.ai/tools)
- [Permission modes](tools/permission-modes.md) — [source](https://docs.openclaw.ai/tools/permission-modes)
- [Skill Workshop](tools/skill-workshop.md) — [source](https://docs.openclaw.ai/tools/skill-workshop)

### Providers

- [GMI Cloud](providers/gmi.md) — [source](https://docs.openclaw.ai/providers/gmi)
- [NovitaAI](providers/novita.md) — [source](https://docs.openclaw.ai/providers/novita)
- [Ollama Cloud](providers/ollama-cloud.md) — [source](https://docs.openclaw.ai/providers/ollama-cloud)
- [PixVerse](providers/pixverse.md) — [source](https://docs.openclaw.ai/providers/pixverse)
- [Provider directory](providers.md) — [source](https://docs.openclaw.ai/providers)
- [Qwen OAuth / Portal](providers/qwen-oauth.md) — [source](https://docs.openclaw.ai/providers/qwen-oauth)

### Platforms

- [Platforms](platforms.md) — [source](https://docs.openclaw.ai/platforms)

### Gateway

- [Gateway runbook](gateway.md) — [source](https://docs.openclaw.ai/gateway)
- [npm shrinkwrap](gateway/security/shrinkwrap.md) — [source](https://docs.openclaw.ai/gateway/security/shrinkwrap)

### Cli

- [CLI reference](cli.md) — [source](https://docs.openclaw.ai/cli)
- [Transcripts CLI](cli/transcripts.md) — [source](https://docs.openclaw.ai/cli/transcripts)
- [Workboard CLI](cli/workboard.md) — [source](https://docs.openclaw.ai/cli/workboard)

### Help

- [Help](help.md) — [source](https://docs.openclaw.ai/help)

### Vps

- [Linux server](vps.md) — [source](https://docs.openclaw.ai/vps)

### Plugins

- [Channel inbound API](plugins/sdk-channel-inbound.md) — [source](https://docs.openclaw.ai/plugins/sdk-channel-inbound)
- [Channel outbound API](plugins/sdk-channel-outbound.md) — [source](https://docs.openclaw.ai/plugins/sdk-channel-outbound)
- [Workboard plugin](plugins/workboard.md) — [source](https://docs.openclaw.ai/plugins/workboard)

### Reference

- [Release performance sweep](reference/release-performance-sweep.md) — [source](https://docs.openclaw.ai/reference/release-performance-sweep)

### Agent Runtime Architecture

- [Agent runtime architecture](agent-runtime-architecture.md) — [source](https://docs.openclaw.ai/agent-runtime-architecture)

### Openclaw Agent Runtime

- [OpenClaw agent runtime workflow](openclaw-agent-runtime.md) — [source](https://docs.openclaw.ai/openclaw-agent-runtime)

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
