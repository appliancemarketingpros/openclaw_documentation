---
title: Showcase
source_url: https://docs.openclaw.ai/start/showcase
scraped_at: 2026-06-08
---

Get startedOverview

OpenClaw projects are not toy demos. People are shipping PR review loops, mobile apps, home automation, voice systems, devtools, and memory-heavy workflows from the channels they already use — chat-native builds on Telegram, WhatsApp, Discord, and terminals; real automation for booking, shopping, and support without waiting for an API; and physical-world integrations with printers, vacuums, cameras, and home systems.

## Fresh from Discord

Recent standouts across coding, devtools, mobile, and chat-native product building.

[**PR Review to Telegram Feedback** **@bangnokia** • `review` `github` `telegram` OpenCode finishes the change, opens a PR, OpenClaw reviews the diff and replies in Telegram with suggestions plus a clear merge verdict. ![OpenClaw PR review feedback delivered in Telegram](/assets/showcase/pr-review-telegram.jpg) ](<https://x.com/i/status/2010878524543131691>) [**Wine Cellar Skill in Minutes** **@prades_maxime** • `skills` `local` `csv` Asked "Robby" (@openclaw) for a local wine cellar skill. It requests a sample CSV export and a store path, then builds and tests the skill (962 bottles in the example). ![OpenClaw building a local wine cellar skill from CSV](/assets/showcase/wine-cellar-skill.jpg) ](<https://x.com/i/status/2010916352454791216>) [**Tesco Shop Autopilot** **@marchattonhere** • `automation` `browser` `shopping` Weekly meal plan, regulars, book delivery slot, confirm order. No APIs, just browser control. ![Tesco shop automation via chat](/assets/showcase/tesco-shop.jpg) ](<https://x.com/i/status/2009724862470689131>) [**SNAG screenshot-to-Markdown** **@am-will** • `devtools` `screenshots` `markdown` Hotkey a screen region, Gemini vision, instant Markdown in your clipboard. ![SNAG screenshot-to-markdown tool](/assets/showcase/snag.png) ](<https://github.com/am-will/snag>) [**Agents UI** **@kitze** • `ui` `skills` `sync` Desktop app to manage skills and commands across Agents, Claude, Codex, and OpenClaw. ![Agents UI app](/assets/showcase/agents-ui.jpg) ](<https://releaseflow.net/kitze/agents-ui>) [**Telegram voice notes (papla.media)** **Community** • `voice` `tts` `telegram` Wraps papla.media TTS and sends results as Telegram voice notes (no annoying autoplay). ![Telegram voice note output from TTS](/assets/showcase/papla-tts.jpg) ](<https://papla.media/docs>) [**CodexMonitor** **@odrobnik** • `devtools` `codex` `brew` Homebrew-installed helper to list, inspect, and watch local OpenAI Codex sessions (CLI + VS Code). ![CodexMonitor on ClawHub](/assets/showcase/codexmonitor.png) ](<https://clawhub.ai/odrobnik/codexmonitor>) [**Bambu 3D Printer Control** **@tobiasbischoff** • `hardware` `3d-printing` `skill` Control and troubleshoot BambuLab printers: status, jobs, camera, AMS, calibration, and more. ![Bambu CLI skill on ClawHub](/assets/showcase/bambu-cli.png) ](<https://clawhub.ai/tobiasbischoff/bambu-cli>) [**Vienna transport (Wiener Linien)** **@hjanuschka** • `travel` `transport` `skill` Real-time departures, disruptions, elevator status, and routing for Vienna's public transport. ![Wiener Linien skill on ClawHub](/assets/showcase/wienerlinien.png) ](<https://clawhub.ai/hjanuschka/wienerlinien>) **ParentPay school meals** **@George5562** • `automation` `browser` `parenting` Automated UK school meal booking via ParentPay. Uses mouse coordinates for reliable table cell clicking. [**R2 upload (Send Me My Files)** **@julianengel** • `files` `r2` `presigned-urls` Upload to Cloudflare R2/S3 and generate secure presigned download links. Useful for remote OpenClaw instances. ![R2 upload skill on ClawHub](/assets/showcase/r2-upload.png) ](<https://clawhub.ai/skills/r2-upload>) **iOS app via Telegram** **@coard** • `ios` `xcode` `testflight` Built a complete iOS app with maps and voice recording, deployed to TestFlight entirely via Telegram chat. ![iOS app on TestFlight](/assets/showcase/ios-testflight.jpg) **Oura Ring health assistant** **@AS** • `health` `oura` `calendar` Personal AI health assistant integrating Oura ring data with calendar, appointments, and gym schedule. ![Oura ring health assistant](/assets/showcase/oura-health.png) [**Kev's Dream Team (14+ agents)** **@adam91holt** • `multi-agent` `orchestration` 14+ agents under one gateway with an Opus 4.5 orchestrator delegating to Codex workers. See the [technical write-up](<https://github.com/adam91holt/orchestrated-ai-articles>) and [Clawdspace](<https://github.com/adam91holt/clawdspace>) for agent sandboxing. ](<https://github.com/adam91holt/orchestrated-ai-articles>) [**Linear CLI** **@NessZerra** • `devtools` `linear` `cli` CLI for Linear that integrates with agentic workflows (Claude Code, OpenClaw). Manage issues, projects, and workflows from the terminal. ](<https://github.com/Finesssee/linear-cli>) [**Beeper CLI** **@jules** • `messaging` `beeper` `cli` Read, send, and archive messages via Beeper Desktop. Uses Beeper local MCP API so agents can manage all your chats (iMessage, WhatsApp, and more) in one place. ](<https://github.com/blqke/beepcli>)

## Automation and workflows

Scheduling, browser control, support loops, and the "just do the task for me" side of the product.

[**Winix air purifier control** **@antonplex** • `automation` `hardware` `air-quality` Claude Code discovered and confirmed the purifier controls, then OpenClaw takes over to manage room air quality. ![Winix air purifier control via OpenClaw](/assets/showcase/winix-air-purifier.jpg) ](<https://x.com/antonplex/status/2010518442471006253>) [**Pretty sky camera shots** **@signalgaining** • `automation` `camera` `skill` Triggered by a roof camera: ask OpenClaw to snap a sky photo whenever it looks pretty. It designed a skill and took the shot. ![Roof camera sky snapshot captured by OpenClaw](/assets/showcase/roof-camera-sky.jpg) ](<https://x.com/signalgaining/status/2010523120604746151>) [**Visual morning briefing scene** **@buddyhadry** • `automation` `briefing` `telegram` A scheduled prompt generates one scene image each morning (weather, tasks, date, favorite post or quote) via an OpenClaw persona. ](<https://x.com/buddyhadry/status/2010005331925954739>) [**Padel court booking** **@joshp123** • `automation` `booking` `cli` Playtomic availability checker plus booking CLI. Never miss an open court again. ![padel-cli screenshot](/assets/showcase/padel-screenshot.jpg) ](<https://github.com/joshp123/padel-cli>) **Accounting intake** **Community** • `automation` `email` `pdf` Collects PDFs from email, preps documents for a tax consultant. Monthly accounting on autopilot. [**Couch potato dev mode** **@davekiss** • `telegram` `migration` `astro` Rebuilt an entire personal site via Telegram while watching Netflix — Notion to Astro, 18 posts migrated, DNS to Cloudflare. Never opened a laptop. ](<https://davekiss.com>) **Job search agent** **@attol8** • `automation` `api` `skill` Searches job listings, matches against CV keywords, and returns relevant opportunities with links. Built in 30 minutes using the JSearch API. [**Jira skill builder** **@jdrhyne** • `jira` `skill` `devtools` OpenClaw connected to Jira, then generated a new skill on the fly (before it existed on ClawHub). ](<https://x.com/jdrhyne/status/2008336434827002232>) [**Todoist skill via Telegram** **@iamsubhrajyoti** • `todoist` `skill` `telegram` Automated Todoist tasks and had OpenClaw generate the skill directly in Telegram chat. ](<https://x.com/iamsubhrajyoti/status/2009949389884920153>) **TradingView analysis** **@bheem1798** • `finance` `browser` `automation` Logs into TradingView via browser automation, screenshots charts, and performs technical analysis on demand. No API needed — just browser control. **Slack auto-support** **@henrymascot** • `slack` `automation` `support` Watches a company Slack channel, responds helpfully, and forwards notifications to Telegram. Autonomously fixed a production bug in a deployed app without being asked.

## Knowledge and memory

Systems that index, search, remember, and reason over personal or team knowledge.

[**xuezh Chinese learning** **@joshp123** • `learning` `voice` `skill` Chinese learning engine with pronunciation feedback and study flows via OpenClaw. ![xuezh pronunciation feedback](/assets/showcase/xuezh-pronunciation.jpeg) ](<https://github.com/joshp123/xuezh>) **WhatsApp memory vault** **Community** • `memory` `transcription` `indexing` Ingests full WhatsApp exports, transcribes 1k+ voice notes, cross-checks with git logs, outputs linked markdown reports. [**Karakeep semantic search** **@jamesbrooksco** • `search` `vector` `bookmarks` Adds vector search to Karakeep bookmarks using Qdrant plus OpenAI or Ollama embeddings. ](<https://github.com/jamesbrooksco/karakeep-semantic-search>) **Inside-Out-2 memory** **Community** • `memory` `beliefs` `self-model` Separate memory manager that turns session files into memories, then beliefs, then an evolving self model.

## Voice and phone

Speech-first entry points, phone bridges, and transcription-heavy workflows.

[**Clawdia phone bridge** **@alejandroOPI** • `voice` `vapi` `bridge` Vapi voice assistant to OpenClaw HTTP bridge. Near real-time phone calls with your agent. ](<https://github.com/alejandroOPI/clawdia-bridge>) [**OpenRouter transcription** **@obviyus** • `transcription` `multilingual` `skill` Multi-lingual audio transcription via OpenRouter (Gemini, and more). Available on ClawHub. ![OpenRouter transcription skill on ClawHub](/assets/showcase/openrouter-transcribe.png) ](<https://clawhub.ai/obviyus/openrouter-transcribe>)

## Infrastructure and deployment

Packaging, deployment, and integrations that make OpenClaw easier to run and extend.

[**Home Assistant add-on** **@ngutman** • `homeassistant` `docker` `raspberry-pi` OpenClaw gateway running on Home Assistant OS with SSH tunnel support and persistent state. ](<https://github.com/ngutman/openclaw-ha-addon>) [**Home Assistant skill** **ClawHub** • `homeassistant` `skill` `automation` Control and automate Home Assistant devices via natural language. ![Home Assistant skill on ClawHub](/assets/showcase/homeassistant.png) ](<https://clawhub.ai/skills/homeassistant>) [**Nix packaging** **@openclaw** • `nix` `packaging` `deployment` Batteries-included nixified OpenClaw configuration for reproducible deployments. ](<https://github.com/openclaw/nix-openclaw>) [**CalDAV calendar** **ClawHub** • `calendar` `caldav` `skill` Calendar skill using khal and vdirsyncer. Self-hosted calendar integration. ![CalDAV calendar skill on ClawHub](/assets/showcase/caldav-calendar.png) ](<https://clawhub.ai/skills/caldav-calendar>)

## Home and hardware

The physical-world side of OpenClaw: homes, sensors, cameras, vacuums, and other devices.

[**GoHome automation** **@joshp123** • `home` `nix` `grafana` Nix-native home automation with OpenClaw as the interface, plus Grafana dashboards. ![GoHome Grafana dashboard](/assets/showcase/gohome-grafana.png) ](<https://github.com/joshp123/gohome>) [**Roborock vacuum** **@joshp123** • `vacuum` `iot` `plugin` Control your Roborock robot vacuum through natural conversation. ![Roborock status](/assets/showcase/roborock-screenshot.jpg) ](<https://github.com/joshp123/gohome/tree/main/plugins/roborock>)

## Community projects

Things that grew beyond a single workflow into broader products or ecosystems.

[**StarSwap marketplace** **Community** • `marketplace` `astronomy` `webapp` Full astronomy gear marketplace. Built with and around the OpenClaw ecosystem. ](<https://star-swap.com/>)

## Submit your project

* ### Share it

Post in [#self-promotion on Discord](<https://discord.gg/clawd>) or [tweet @openclaw](<https://x.com/openclaw>).

* ### Include details

Tell us what it does, link to the repo or demo, and share a screenshot if you have one.

* ### Get featured

We'll add standout projects to this page.

## Related

  * [Getting started](</start/getting-started>)
  * [OpenClaw](</start/openclaw>)


Was this useful?YesNo

Open issue