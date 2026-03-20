---
title: Railway
source_url: https://docs.openclaw.ai/install/railway
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Hosting

Railway

Deploy OpenClaw on Railway with a one-click template and finish setup in your browser. This is the easiest “no terminal on the server” path: Railway runs the Gateway for you, and you configure everything via the `/setup` web wizard.

## 

​

Quick checklist (new users)

  1. Click **Deploy on Railway** (below).
  2. Add a **Volume** mounted at `/data`.
  3. Set the required **Variables** (at least `SETUP_PASSWORD`).
  4. Enable **HTTP Proxy** on port `8080`.
  5. Open `https://<your-railway-domain>/setup` and finish the wizard.


## 

​

One-click deploy

[Deploy on Railway](<https://railway.com/deploy/clawdbot-railway-template>) After deploy, find your public URL in **Railway → your service → Settings → Domains**. Railway will either:

  * give you a generated domain (often `https://<something>.up.railway.app`), or
  * use your custom domain if you attached one.

Then open:

  * `https://<your-railway-domain>/setup` — web setup (password protected)
  * `https://<your-railway-domain>/openclaw` — Control UI


## 

​

What you get

  * Hosted OpenClaw Gateway + Control UI
  * Web setup at `/setup` (no terminal commands)
  * Persistent storage via Railway Volume (`/data`) so config/credentials/workspace survive redeploys
  * Backup export at `/setup/export` to migrate off Railway later


## 

​

Required Railway settings

### 

​

Public Networking

Enable **HTTP Proxy** for the service.

  * Port: `8080`


### 

​

Volume (required)

Attach a volume mounted at:

  * `/data`


### 

​

Variables

Set these variables on the service:

  * `SETUP_PASSWORD` (required)
  * `PORT=8080` (required — must match the port in Public Networking)
  * `OPENCLAW_STATE_DIR=/data/.openclaw` (recommended)
  * `OPENCLAW_WORKSPACE_DIR=/data/workspace` (recommended)
  * `OPENCLAW_GATEWAY_TOKEN` (recommended; treat as an admin secret)


## 

​

Setup flow

  1. Visit `https://<your-railway-domain>/setup` and enter your `SETUP_PASSWORD`.
  2. Choose a model/auth provider and paste your key.
  3. (Optional) Add Telegram/Discord/Slack tokens.
  4. Click **Run setup**.

If Telegram DMs are set to pairing, web setup can approve the pairing code.

## 

​

Connect a channel

Paste your Telegram or Discord token into the `/setup` wizard. For setup instructions, see the channel docs:

  * [Telegram](</channels/telegram>) (fastest — just a bot token)
  * [Discord](</channels/discord>)
  * [All channels](</channels>)


## 

​

Backups & migration

Download a backup at:

  * `https://<your-railway-domain>/setup/export`

This exports your OpenClaw state + workspace so you can migrate to another host without losing config or memory.

## 

​

Next steps

  * Set up messaging channels: [Channels](</channels>)
  * Configure the Gateway: [Gateway configuration](</gateway/configuration>)
  * Keep OpenClaw up to date: [Updating](</install/updating>)


[Oracle Cloud](</install/oracle>)[Raspberry Pi](</install/raspberry-pi>)

⌘I