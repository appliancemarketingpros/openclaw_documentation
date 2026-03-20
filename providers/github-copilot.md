---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/providers/github-copilot
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Providers

GitHub Copilot

# 

​

GitHub Copilot

## 

​

What is GitHub Copilot?

GitHub Copilot is GitHub’s AI coding assistant. It provides access to Copilot models for your GitHub account and plan. OpenClaw can use Copilot as a model provider in two different ways.

## 

​

Two ways to use Copilot in OpenClaw

### 

​

1) Built-in GitHub Copilot provider (`github-copilot`)

Use the native device-login flow to obtain a GitHub token, then exchange it for Copilot API tokens when OpenClaw runs. This is the **default** and simplest path because it does not require VS Code.

### 

​

2) Copilot Proxy plugin (`copilot-proxy`)

Use the **Copilot Proxy** VS Code extension as a local bridge. OpenClaw talks to the proxy’s `/v1` endpoint and uses the model list you configure there. Choose this when you already run Copilot Proxy in VS Code or need to route through it. You must enable the plugin and keep the VS Code extension running. Use GitHub Copilot as a model provider (`github-copilot`). The login command runs the GitHub device flow, saves an auth profile, and updates your config to use that profile.

## 

​

CLI setup

Copy
[code]
    openclaw models auth login-github-copilot
    
[/code]

You’ll be prompted to visit a URL and enter a one-time code. Keep the terminal open until it completes.

### 

​

Optional flags

Copy
[code]
    openclaw models auth login-github-copilot --profile-id github-copilot:work
    openclaw models auth login-github-copilot --yes
    
[/code]

## 

​

Set a default model

Copy
[code]
    openclaw models set github-copilot/gpt-4o
    
[/code]

### 

​

Config snippet

Copy
[code]
    {
      agents: { defaults: { model: { primary: "github-copilot/gpt-4o" } } },
    }
    
[/code]

## 

​

Notes

  * Requires an interactive TTY; run it directly in a terminal.
  * Copilot model availability depends on your plan; if a model is rejected, try another ID (for example `github-copilot/gpt-4.1`).
  * The login stores a GitHub token in the auth profile store and exchanges it for a Copilot API token when OpenClaw runs.


[Deepgram](</providers/deepgram>)[Google (Gemini)](</providers/google>)

⌘I