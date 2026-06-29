---
title: Maturity scorecard
source_url: https://docs.openclaw.ai/maturity/scorecard
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Maturity scorecard

release readiness - generated from taxonomy + QA evidence

A practical view of what is ready, what is proven, and what still needs work.

50 surfaces - 281 capability areas - deterministic coverage plus human-reviewed quality and completeness.

Browse surfaces / Inspect QA evidence / [Read the taxonomy](</maturity/taxonomy>)

## What this page is for

Use this page to answer one question: which OpenClaw surfaces are credible choices for a release, and what evidence supports that judgment? Coverage comes from deterministic QA evidence; quality and completeness are maintained as reviewed maturity scores.

## At a glance

67% Maturity score

Alpha Quality + completeness Coverage Experimental - 4% Quality Alpha - 63% Completeness Beta - 70%

Coverage is deliberately evidence-led: an area does not become "ready" just because the implementation exists. It is not an input to the maturity score, but OpenClaw aims to keep end-to-end coverage above 90% for mature Stable-or-better features over time.

## Score bands

Experimental0-50%

Alpha50-70%

Beta70-80%

Stable80-95%

Clawesome95-100%

## Surface explorer

Surfaces are ordered by maturity level, completeness, and quality. LTS support is shown alongside each row so release-ready options are easy to compare.

### All surfaces

[CLIM4Stable7 areas](</maturity/taxonomy#cli>)

CoverageExperimental4%

QualityStable83%

CompletenessStable90%

Partial - 6

[Gateway runtimeM4Stable13 areas](</maturity/taxonomy#gateway-runtime>)

CoverageExperimental6%

QualityStable81%

CompletenessStable89%

Partial - 12

[Linux Gateway hostM4Stable5 areas](</maturity/taxonomy#linux-gateway-host>)

CoverageExperimental0%

QualityBeta75%

CompletenessStable89%

Partial - 4

[macOS Gateway hostM4Stable7 areas](</maturity/taxonomy#macos-gateway-host>)

CoverageExperimental0%

QualityBeta74%

CompletenessStable88%

None

[DiscordM4Stable6 areas](</maturity/taxonomy#discord>)

CoverageExperimental0%

QualityBeta73%

CompletenessStable87%

Partial - 4

[Agent RuntimeM3Beta9 areas](</maturity/taxonomy#agent-runtime>)

CoverageExperimental33%

QualityBeta78%

CompletenessBeta79%

Partial - 6

[Session, memory, and context engineM3Beta9 areas](</maturity/taxonomy#session-memory-and-context-engine>)

CoverageExperimental30%

QualityBeta77%

CompletenessBeta79%

Partial - 6

[Channel frameworkM3Beta8 areas](</maturity/taxonomy#channel-framework>)

CoverageExperimental13%

QualityBeta76%

CompletenessBeta79%

Partial - 5

[Browser automation, exec, and sandbox toolsM3Beta3 areas](</maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CoverageExperimental21%

QualityBeta75%

CompletenessBeta79%

Partial - 2

[ObservabilityM3Beta5 areas](</maturity/taxonomy#observability>)

CoverageExperimental18%

QualityBeta75%

CompletenessBeta79%

Partial - 3

[OpenAI and Codex provider pathM3Beta5 areas](</maturity/taxonomy#openai-and-codex-provider-path>)

CoverageExperimental26%

QualityBeta74%

CompletenessBeta79%

Partial - 3

[Gateway Web AppM3Beta6 areas](</maturity/taxonomy#gateway-web-app>)

CoverageExperimental4%

QualityBeta74%

CompletenessBeta79%

None

[Web search toolsM3Beta4 areas](</maturity/taxonomy#web-search-tools>)

CoverageExperimental9%

QualityBeta74%

CompletenessBeta79%

None

[PluginsM3Beta9 areas](</maturity/taxonomy#plugins>)

CoverageExperimental12%

QualityBeta72%

CompletenessBeta79%

Partial - 7

[Security, auth, pairing, and secretsM3Beta6 areas](</maturity/taxonomy#security-auth-pairing-and-secrets>)

CoverageExperimental16%

QualityBeta72%

CompletenessBeta79%

Partial - 5

[Automation: cron, hooks, tasks, pollingM3Beta6 areas](</maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CoverageExperimental2%

QualityBeta72%

CompletenessBeta79%

None

[Docker and Podman hostingM3Beta4 areas](</maturity/taxonomy#docker-and-podman-hosting>)

CoverageExperimental7%

QualityBeta71%

CompletenessBeta79%

None

[Windows via WSL2M3Beta6 areas](</maturity/taxonomy#windows-via-wsl2>)

CoverageExperimental6%

QualityAlpha69%

CompletenessBeta79%

Partial - 5

[Raspberry Pi and small Linux devicesM3Beta4 areas](</maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CoverageExperimental0%

QualityAlpha67%

CompletenessBeta79%

None

[Anthropic provider pathM3Beta5 areas](</maturity/taxonomy#anthropic-provider-path>)

CoverageExperimental0%

QualityBeta71%

CompletenessBeta78%

None

[TelegramM3Beta5 areas](</maturity/taxonomy#telegram>)

CoverageExperimental0%

QualityAlpha68%

CompletenessBeta78%

Full - 5

[SlackM3Beta5 areas](</maturity/taxonomy#slack>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

Full - 5

[Google provider pathM3Beta5 areas](</maturity/taxonomy#google-provider-path>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[iMessage and BlueBubblesM3Beta5 areas](</maturity/taxonomy#imessage-and-bluebubbles>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[macOS companion appM3Beta8 areas](</maturity/taxonomy#macos-companion-app>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[OpenRouter provider pathM3Beta4 areas](</maturity/taxonomy#openrouter-provider-path>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[WhatsAppM3Beta5 areas](</maturity/taxonomy#whatsapp>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[Media understanding and media generationM2Alpha6 areas](</maturity/taxonomy#media-understanding-and-media-generation>)

CoverageExperimental2%

QualityAlpha64%

CompletenessAlpha68%

None

[Image, video, and music generation toolsM2Alpha5 areas](</maturity/taxonomy#image-video-and-music-generation-tools>)

CoverageExperimental0%

QualityAlpha61%

CompletenessAlpha68%

None

[Local model providers: Ollama, vLLM, SGLang, LM StudioM2Alpha5 areas](</maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CoverageExperimental0%

QualityAlpha61%

CompletenessAlpha68%

None

[Long-tail hosted providersM2Alpha3 areas](</maturity/taxonomy#long-tail-hosted-providers>)

CoverageExperimental0%

QualityAlpha61%

CompletenessAlpha68%

None

[Voice and realtime talkM2Alpha6 areas](</maturity/taxonomy#voice-and-realtime-talk>)

CoverageExperimental0%

QualityAlpha61%

CompletenessAlpha68%

None

[MatrixM2Alpha6 areas](</maturity/taxonomy#matrix>)

CoverageExperimental0%

QualityAlpha60%

CompletenessAlpha67%

None

[Android appM2Alpha7 areas](</maturity/taxonomy#android-app>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[Google ChatM2Alpha5 areas](</maturity/taxonomy#google-chat>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[Microsoft TeamsM2Alpha5 areas](</maturity/taxonomy#microsoft-teams>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[SignalM2Alpha5 areas](</maturity/taxonomy#signal>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[TUIM2Alpha5 areas](</maturity/taxonomy#tui>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[Native WindowsM2Alpha4 areas](</maturity/taxonomy#native-windows>)

CoverageExperimental0%

QualityAlpha58%

CompletenessAlpha66%

Partial - 1

[ClawHubM2Alpha4 areas](</maturity/taxonomy#clawhub>)

CoverageExperimental0%

QualityAlpha58%

CompletenessAlpha62%

None

[Kubernetes hostingM2Alpha4 areas](</maturity/taxonomy#kubernetes-hosting>)

CoverageExperimental0%

QualityAlpha55%

CompletenessAlpha61%

None

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regional channelsM2Alpha4 areas](</maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CoverageExperimental0%

QualityAlpha55%

CompletenessAlpha58%

None

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 areas](</maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CoverageExperimental0%

QualityAlpha53%

CompletenessAlpha54%

None

[OpenClaw App SDKM2Alpha6 areas](</maturity/taxonomy#openclaw-app-sdk>)

CoverageExperimental3%

QualityAlpha54%

CompletenessAlpha53%

None

[iOS appM1Experimental8 areas](</maturity/taxonomy#ios-app>)

CoverageExperimental0%

QualityExperimental41%

CompletenessExperimental44%

None

[Nix install pathM1Experimental5 areas](</maturity/taxonomy#nix-install-path>)

CoverageExperimental0%

QualityExperimental41%

CompletenessExperimental44%

None

[Voice Call channelM1Experimental5 areas](</maturity/taxonomy#voice-call-channel>)

CoverageExperimental0%

QualityExperimental41%

CompletenessExperimental44%

None

[watchOS companion surfacesM1Experimental5 areas](</maturity/taxonomy#watchos-companion-surfaces>)

CoverageExperimental0%

QualityExperimental41%

CompletenessExperimental44%

None

[Linux companion appM0Planned5 areas](</maturity/taxonomy#linux-companion-app>)

CoverageExperimental0%

QualityExperimental19%

CompletenessExperimental21%

None

[Native Windows companion appM0Planned5 areas](</maturity/taxonomy#native-windows-companion-app>)

CoverageExperimental0%

QualityExperimental19%

CompletenessExperimental21%

None

### Core

[CLIM4Stable7 areas](</maturity/taxonomy#cli>)

CoverageExperimental4%

QualityStable83%

CompletenessStable90%

Partial - 6

[Gateway runtimeM4Stable13 areas](</maturity/taxonomy#gateway-runtime>)

CoverageExperimental6%

QualityStable81%

CompletenessStable89%

Partial - 12

[Agent RuntimeM3Beta9 areas](</maturity/taxonomy#agent-runtime>)

CoverageExperimental33%

QualityBeta78%

CompletenessBeta79%

Partial - 6

[Session, memory, and context engineM3Beta9 areas](</maturity/taxonomy#session-memory-and-context-engine>)

CoverageExperimental30%

QualityBeta77%

CompletenessBeta79%

Partial - 6

[Channel frameworkM3Beta8 areas](</maturity/taxonomy#channel-framework>)

CoverageExperimental13%

QualityBeta76%

CompletenessBeta79%

Partial - 5

[ObservabilityM3Beta5 areas](</maturity/taxonomy#observability>)

CoverageExperimental18%

QualityBeta75%

CompletenessBeta79%

Partial - 3

[Gateway Web AppM3Beta6 areas](</maturity/taxonomy#gateway-web-app>)

CoverageExperimental4%

QualityBeta74%

CompletenessBeta79%

None

[PluginsM3Beta9 areas](</maturity/taxonomy#plugins>)

CoverageExperimental12%

QualityBeta72%

CompletenessBeta79%

Partial - 7

[Security, auth, pairing, and secretsM3Beta6 areas](</maturity/taxonomy#security-auth-pairing-and-secrets>)

CoverageExperimental16%

QualityBeta72%

CompletenessBeta79%

Partial - 5

[Automation: cron, hooks, tasks, pollingM3Beta6 areas](</maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CoverageExperimental2%

QualityBeta72%

CompletenessBeta79%

None

[Media understanding and media generationM2Alpha6 areas](</maturity/taxonomy#media-understanding-and-media-generation>)

CoverageExperimental2%

QualityAlpha64%

CompletenessAlpha68%

None

[Voice and realtime talkM2Alpha6 areas](</maturity/taxonomy#voice-and-realtime-talk>)

CoverageExperimental0%

QualityAlpha61%

CompletenessAlpha68%

None

[TUIM2Alpha5 areas](</maturity/taxonomy#tui>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[ClawHubM2Alpha4 areas](</maturity/taxonomy#clawhub>)

CoverageExperimental0%

QualityAlpha58%

CompletenessAlpha62%

None

[OpenClaw App SDKM2Alpha6 areas](</maturity/taxonomy#openclaw-app-sdk>)

CoverageExperimental3%

QualityAlpha54%

CompletenessAlpha53%

None

### Platform

[Linux Gateway hostM4Stable5 areas](</maturity/taxonomy#linux-gateway-host>)

CoverageExperimental0%

QualityBeta75%

CompletenessStable89%

Partial - 4

[macOS Gateway hostM4Stable7 areas](</maturity/taxonomy#macos-gateway-host>)

CoverageExperimental0%

QualityBeta74%

CompletenessStable88%

None

[Docker and Podman hostingM3Beta4 areas](</maturity/taxonomy#docker-and-podman-hosting>)

CoverageExperimental7%

QualityBeta71%

CompletenessBeta79%

None

[Windows via WSL2M3Beta6 areas](</maturity/taxonomy#windows-via-wsl2>)

CoverageExperimental6%

QualityAlpha69%

CompletenessBeta79%

Partial - 5

[Raspberry Pi and small Linux devicesM3Beta4 areas](</maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CoverageExperimental0%

QualityAlpha67%

CompletenessBeta79%

None

[macOS companion appM3Beta8 areas](</maturity/taxonomy#macos-companion-app>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[Android appM2Alpha7 areas](</maturity/taxonomy#android-app>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[Native WindowsM2Alpha4 areas](</maturity/taxonomy#native-windows>)

CoverageExperimental0%

QualityAlpha58%

CompletenessAlpha66%

Partial - 1

[Kubernetes hostingM2Alpha4 areas](</maturity/taxonomy#kubernetes-hosting>)

CoverageExperimental0%

QualityAlpha55%

CompletenessAlpha61%

None

[iOS appM1Experimental8 areas](</maturity/taxonomy#ios-app>)

CoverageExperimental0%

QualityExperimental41%

CompletenessExperimental44%

None

[Nix install pathM1Experimental5 areas](</maturity/taxonomy#nix-install-path>)

CoverageExperimental0%

QualityExperimental41%

CompletenessExperimental44%

None

[watchOS companion surfacesM1Experimental5 areas](</maturity/taxonomy#watchos-companion-surfaces>)

CoverageExperimental0%

QualityExperimental41%

CompletenessExperimental44%

None

[Linux companion appM0Planned5 areas](</maturity/taxonomy#linux-companion-app>)

CoverageExperimental0%

QualityExperimental19%

CompletenessExperimental21%

None

[Native Windows companion appM0Planned5 areas](</maturity/taxonomy#native-windows-companion-app>)

CoverageExperimental0%

QualityExperimental19%

CompletenessExperimental21%

None

### Channel

[DiscordM4Stable6 areas](</maturity/taxonomy#discord>)

CoverageExperimental0%

QualityBeta73%

CompletenessStable87%

Partial - 4

[TelegramM3Beta5 areas](</maturity/taxonomy#telegram>)

CoverageExperimental0%

QualityAlpha68%

CompletenessBeta78%

Full - 5

[SlackM3Beta5 areas](</maturity/taxonomy#slack>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

Full - 5

[iMessage and BlueBubblesM3Beta5 areas](</maturity/taxonomy#imessage-and-bluebubbles>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[WhatsAppM3Beta5 areas](</maturity/taxonomy#whatsapp>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[MatrixM2Alpha6 areas](</maturity/taxonomy#matrix>)

CoverageExperimental0%

QualityAlpha60%

CompletenessAlpha67%

None

[Google ChatM2Alpha5 areas](</maturity/taxonomy#google-chat>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[Microsoft TeamsM2Alpha5 areas](</maturity/taxonomy#microsoft-teams>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[SignalM2Alpha5 areas](</maturity/taxonomy#signal>)

CoverageExperimental0%

QualityAlpha59%

CompletenessAlpha66%

None

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regional channelsM2Alpha4 areas](</maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CoverageExperimental0%

QualityAlpha55%

CompletenessAlpha58%

None

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 areas](</maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CoverageExperimental0%

QualityAlpha53%

CompletenessAlpha54%

None

[Voice Call channelM1Experimental5 areas](</maturity/taxonomy#voice-call-channel>)

CoverageExperimental0%

QualityExperimental41%

CompletenessExperimental44%

None

### Provider and tool

[Browser automation, exec, and sandbox toolsM3Beta3 areas](</maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CoverageExperimental21%

QualityBeta75%

CompletenessBeta79%

Partial - 2

[OpenAI and Codex provider pathM3Beta5 areas](</maturity/taxonomy#openai-and-codex-provider-path>)

CoverageExperimental26%

QualityBeta74%

CompletenessBeta79%

Partial - 3

[Web search toolsM3Beta4 areas](</maturity/taxonomy#web-search-tools>)

CoverageExperimental9%

QualityBeta74%

CompletenessBeta79%

None

[Anthropic provider pathM3Beta5 areas](</maturity/taxonomy#anthropic-provider-path>)

CoverageExperimental0%

QualityBeta71%

CompletenessBeta78%

None

[Google provider pathM3Beta5 areas](</maturity/taxonomy#google-provider-path>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[OpenRouter provider pathM3Beta4 areas](</maturity/taxonomy#openrouter-provider-path>)

CoverageExperimental0%

QualityAlpha66%

CompletenessBeta78%

None

[Image, video, and music generation toolsM2Alpha5 areas](</maturity/taxonomy#image-video-and-music-generation-tools>)

CoverageExperimental0%

QualityAlpha61%

CompletenessAlpha68%

None

[Local model providers: Ollama, vLLM, SGLang, LM StudioM2Alpha5 areas](</maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CoverageExperimental0%

QualityAlpha61%

CompletenessAlpha68%

None

[Long-tail hosted providersM2Alpha3 areas](</maturity/taxonomy#long-tail-hosted-providers>)

CoverageExperimental0%

QualityAlpha61%

CompletenessAlpha68%

None

## QA evidence summary

The checks below show which scorecard areas were exercised by QA profile evidence.

Full taxonomy validation 2026-06-23T07:24:36.128Z 96 checks - 94 passed, 2 blocked 0 of 281 (0%) areas - 20 of 1675 (1.2%) features - 77 of 1665 (4.6%) coverage IDs

### Readiness by area

Open a surface to inspect the evidence state of each category. The list stays collapsed so the page remains useful at a glance.

Agent Runtime - 9 areas

8 partially reviewed / 1 needs review

Agent Turn Execution Partially reviewed - Full taxonomy validation

0 of 3 (0%) / 7 of 24 (29.2%) 17 capability gaps

External Runtimes and Subagents Partially reviewed - Full taxonomy validation

0 of 4 (0%) / 3 of 10 (30%) 7 capability gaps

Hosted Provider Execution Partially reviewed - Full taxonomy validation

1 of 5 (20%) / 1 of 5 (20%) 4 capability gaps

Local and Self-hosted Providers Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Model and Runtime Selection Partially reviewed - Full taxonomy validation

0 of 4 (0%) / 2 of 8 (25%) 6 capability gaps

Provider Auth Partially reviewed - Full taxonomy validation

0 of 10 (0%) / 4 of 17 (23.5%) 13 capability gaps

Streaming and Progress Partially reviewed - Full taxonomy validation

0 of 2 (0%) / 5 of 9 (55.6%) 4 capability gaps

Tool Calls and Response Handling Partially reviewed - Full taxonomy validation

0 of 3 (0%) / 15 of 23 (65.2%) 8 capability gaps

Tool Execution Controls Partially reviewed - Full taxonomy validation

0 of 6 (0%) / 6 of 12 (50%) 6 capability gaps

Android app - 7 areas

7 needs review

Connection Setup Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Device Runtime Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Distribution Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Media Capture Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Mobile Chat Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Settings Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Voice Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Anthropic provider path - 5 areas

5 needs review

Media Inputs Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Model and Runtime Selection Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 12 (0%) 12 capability gaps

Prompt Cache and Context Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Provider Auth and Recovery Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Request Transport and Turn Semantics Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Automation: cron, hooks, tasks, polling - 6 areas

5 needs review / 1 partially reviewed

Automation Hooks Needs review - Full taxonomy validation

0 of 11 (0%) / 0 of 11 (0%) 11 capability gaps

Background Tasks and Flows Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Cron Jobs Needs review - Full taxonomy validation

0 of 15 (0%) / 0 of 15 (0%) 15 capability gaps

Event Ingress Needs review - Full taxonomy validation

0 of 15 (0%) / 0 of 15 (0%) 15 capability gaps

Heartbeat Partially reviewed - Full taxonomy validation

0 of 5 (0%) / 1 of 7 (14.3%) 6 capability gaps

Polling Controls Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Browser automation, exec, and sandbox tools - 3 areas

2 partially reviewed / 1 needs review

Browser Automation Partially reviewed - Full taxonomy validation

1 of 8 (12.5%) / 1 of 8 (12.5%) 7 capability gaps

Sandbox and Tool Policy Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Tool Invocation and Execution Partially reviewed - Full taxonomy validation

2 of 6 (33.3%) / 4 of 8 (50%) 4 capability gaps

Gateway Web App - 6 areas

3 needs review / 3 partially reviewed

Browser Access and Trust Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Browser Realtime Talk Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Browser UI Partially reviewed - Full taxonomy validation

0 of 10 (0%) / 1 of 12 (8.3%) 11 capability gaps

Configuration Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Operator Console Partially reviewed - Full taxonomy validation

0 of 10 (0%) / 1 of 12 (8.3%) 11 capability gaps

WebChat Conversations Partially reviewed - Full taxonomy validation

0 of 15 (0%) / 2 of 20 (10%) 18 capability gaps

Channel framework - 8 areas

4 needs review / 4 partially reviewed

Channel Actions Commands and Approvals Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Channel Setup Partially reviewed - Full taxonomy validation

0 of 5 (0%) / 1 of 7 (14.3%) 6 capability gaps

Conversation Routing and Delivery Partially reviewed - Full taxonomy validation

0 of 10 (0%) / 5 of 27 (18.5%) 22 capability gaps

Group Thread and Ambient Room Behavior Partially reviewed - Full taxonomy validation

0 of 5 (0%) / 4 of 11 (36.4%) 7 capability gaps

Inbound Access and Identity Gates Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Media Attachments and Rich Channel Data Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Outbound Delivery and Reply Pipeline Partially reviewed - Full taxonomy validation

0 of 4 (0%) / 8 of 21 (38.1%) 13 capability gaps

Status Health and Operator Controls Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 6 (0%) 6 capability gaps

ClawHub - 4 areas

4 needs review

Catalog Discovery Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Compatibility and Trust Needs review - Full taxonomy validation

0 of 12 (0%) / 0 of 12 (0%) 12 capability gaps

Plugin Lifecycle and Health Needs review - Full taxonomy validation

0 of 26 (0%) / 0 of 26 (0%) 26 capability gaps

Publishing Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

CLI - 7 areas

5 needs review / 2 partially reviewed

CLI Observability Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

CLI Setup Partially reviewed - Full taxonomy validation

1 of 6 (16.7%) / 1 of 6 (16.7%) 5 capability gaps

Doctor Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Gateway Service Management Partially reviewed - Full taxonomy validation

0 of 5 (0%) / 1 of 7 (14.3%) 6 capability gaps

Onboarding and Auth Setup Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Plugin and Channel Setup Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Updates and Upgrades Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Discord - 6 areas

6 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 12 (0%) / 0 of 12 (0%) 12 capability gaps

Media and Rich Content Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Native Controls and Approvals Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Realtime Voice and Calls Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Docker and Podman hosting - 4 areas

3 needs review / 1 partially reviewed

Agent Sandbox and Tooling Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Container Operations Needs review - Full taxonomy validation

0 of 11 (0%) / 0 of 11 (0%) 11 capability gaps

Container Setup Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Image Release and Validation Partially reviewed - Full taxonomy validation

1 of 5 (20%) / 2 of 7 (28.6%) 5 capability gaps

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regional channels - 4 areas

4 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Media and Rich Content Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Gateway runtime - 13 areas

9 needs review / 4 partially reviewed

Approvals and Remote Execution Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Device Auth and Pairing Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Gateway Lifecycle Partially reviewed - Full taxonomy validation

0 of 7 (0%) / 4 of 12 (33.3%) 8 capability gaps

Gateway RPC APIs and Events Partially reviewed - Full taxonomy validation

0 of 20 (0%) / 2 of 22 (9.1%) 20 capability gaps

Health, Diagnostics, and Repair Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Hosted Web Surface Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

HTTP APIs Partially reviewed - Full taxonomy validation

1 of 4 (25%) / 1 of 4 (25%) 3 capability gaps

Network Access and Discovery Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Nodes and Remote Capabilities Needs review - Full taxonomy validation

0 of 8 (0%) / 0 of 8 (0%) 8 capability gaps

Protocol Compatibility Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Roles and Permissions Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Security Controls Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

WebSocket Connection Partially reviewed - Full taxonomy validation

1 of 8 (12.5%) / 1 of 8 (12.5%) 7 capability gaps

Google Chat - 5 areas

5 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 11 (0%) / 0 of 11 (0%) 11 capability gaps

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 16 (0%) / 0 of 16 (0%) 16 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Media and Rich Content Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Native Controls and Approvals Needs review - Full taxonomy validation

0 of 16 (0%) / 0 of 16 (0%) 16 capability gaps

Google provider path - 5 areas

5 needs review

Direct Gemini Runtime Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Media, Search, and Realtime Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Model Routing and Endpoints Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Prompt Caching Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Provider Setup and Credentials Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Image, video, and music generation tools - 5 areas

5 needs review

Image Generation Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Media Routing and Discovery Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Music Generation Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Task Lifecycle and Delivery Needs review - Full taxonomy validation

0 of 12 (0%) / 0 of 12 (0%) 12 capability gaps

Video Generation Needs review - Full taxonomy validation

0 of 11 (0%) / 0 of 11 (0%) 11 capability gaps

iMessage and BlueBubbles - 5 areas

5 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 11 (0%) / 0 of 11 (0%) 11 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Media and Rich Content Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Native Controls and Approvals Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

iOS app - 8 areas

8 needs review

Canvas and Screen Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Chat and Sessions Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Device Commands Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Distribution Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Gateway Setup and Diagnostics Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Media and Sharing Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Notifications and Background Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Voice Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Kubernetes hosting - 4 areas

4 needs review

Access and Exposure Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Cluster Lifecycle Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Configuration and Secrets Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Deployment Setup Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Linux companion app - 5 areas

5 needs review

App Distribution Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Chat and Sessions Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Desktop Capabilities Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Gateway Connectivity Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Status and Diagnostics Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Linux Gateway host - 5 areas

5 needs review

Deployment Targets Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Diagnostics and Repair Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Gateway Runtime and Service Control Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Host Setup and Updates Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Remote Access and Security Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Local model providers: Ollama, vLLM, SGLang, LM Studio - 5 areas

5 needs review

Local Memory and Embeddings Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Native Provider Plugins Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Network Safety and Prompt Controls Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

OpenAI-Compatible Runtime Compatibility Needs review - Full taxonomy validation

0 of 8 (0%) / 0 of 8 (0%) 8 capability gaps

Provider Setup, Lifecycle, and Diagnostics Needs review - Full taxonomy validation

0 of 12 (0%) / 0 of 12 (0%) 12 capability gaps

Long-tail hosted providers - 3 areas

3 needs review

Hosted LLM Providers Needs review - Full taxonomy validation

0 of 12 (0%) / 0 of 12 (0%) 12 capability gaps

Hosted Media Providers Needs review - Full taxonomy validation

0 of 8 (0%) / 0 of 8 (0%) 8 capability gaps

Provider Operations Needs review - Full taxonomy validation

0 of 12 (0%) / 0 of 12 (0%) 12 capability gaps

macOS companion app - 8 areas

8 needs review

Canvas Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Local Setup Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Native Capabilities Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Remote Connections Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Remote WebChat Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Status and Settings Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Voice and Talk Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

WebChat Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

macOS Gateway host - 7 areas

7 needs review

CLI Setup Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Diagnostics and Observability Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Gateway Service Lifecycle Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Local Gateway Integration Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Permissions and Native Capabilities Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Profiles and Isolation Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Remote Gateway Mode Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Matrix - 6 areas

6 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Encryption and Verification Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Media and Rich Content Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Native Controls and Approvals Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - 4 areas

4 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Media and Rich Content Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Media understanding and media generation - 6 areas

4 needs review / 2 partially reviewed

Channel Media Handling Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Media Configuration Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Media Generation Partially reviewed - Full taxonomy validation

1 of 17 (5.9%) / 1 of 19 (5.3%) 18 capability gaps

Media Intake and Access Needs review - Full taxonomy validation

0 of 8 (0%) / 0 of 8 (0%) 8 capability gaps

Media Understanding Partially reviewed - Full taxonomy validation

0 of 12 (0%) / 1 of 14 (7.1%) 13 capability gaps

Text-to-Speech Delivery Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Microsoft Teams - 5 areas

5 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Media and Rich Content Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Native Controls and Approvals Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Native Windows - 4 areas

4 needs review

CLI Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Gateway Management Needs review - Full taxonomy validation

0 of 11 (0%) / 0 of 11 (0%) 11 capability gaps

Networking Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Updates Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Native Windows companion app - 5 areas

5 needs review

Chat Sessions Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Desktop Tools and Permissions Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Gateway Connection Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Installation and Updates Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Status and Repair Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Nix install path - 5 areas

5 needs review

Activation and App UX Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Config and State Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Install Handoff Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Plugin Lifecycle Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Service Runtime and Guards Needs review - Full taxonomy validation

0 of 8 (0%) / 0 of 8 (0%) 8 capability gaps

OpenAI and Codex provider path - 5 areas

2 needs review / 3 partially reviewed

Image and Multimodal Input Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Model and Auth Partially reviewed - Full taxonomy validation

1 of 6 (16.7%) / 4 of 9 (44.4%) 5 capability gaps

Native Codex Harness Partially reviewed - Full taxonomy validation

0 of 2 (0%) / 4 of 9 (44.4%) 5 capability gaps

Responses and Tool Compatibility Partially reviewed - Full taxonomy validation

1 of 4 (25%) / 2 of 5 (40%) 3 capability gaps

Voice and Realtime Audio Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

OpenClaw App SDK - 6 areas

5 needs review / 1 partially reviewed

Agent Conversations Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Client API Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Compatibility Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Events and Approvals Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Gateway Access Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Resource Helpers Partially reviewed - Full taxonomy validation

0 of 5 (0%) / 1 of 6 (16.7%) 5 capability gaps

OpenRouter provider path - 4 areas

4 needs review

Chat Runtime and Normalization Needs review - Full taxonomy validation

0 of 15 (0%) / 0 of 15 (0%) 15 capability gaps

Media Generation and Speech Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Provider Recovery and Diagnostics Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Provider Setup and Auth Needs review - Full taxonomy validation

0 of 14 (0%) / 0 of 14 (0%) 14 capability gaps

Plugins - 9 areas

6 needs review / 3 partially reviewed

Authoring and Packaging plugins Needs review - Full taxonomy validation

0 of 8 (0%) / 0 of 8 (0%) 8 capability gaps

Bundled plugins Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Canvas plugin Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Channel plugins Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Installing and running plugins Partially reviewed - Full taxonomy validation

0 of 6 (0%) / 7 of 20 (35%) 13 capability gaps

Plugin approvals Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Provider and tool plugins Partially reviewed - Full taxonomy validation

1 of 6 (16.7%) / 9 of 21 (42.9%) 12 capability gaps

Publishing plugins Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Testing plugins Partially reviewed - Full taxonomy validation

0 of 6 (0%) / 3 of 11 (27.3%) 8 capability gaps

Raspberry Pi and small Linux devices - 4 areas

4 needs review

Gateway Runtime Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Performance and Diagnostics Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Remote Access and Auth Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Setup and Compatibility Needs review - Full taxonomy validation

0 of 12 (0%) / 0 of 12 (0%) 12 capability gaps

Security, auth, pairing, and secrets - 6 areas

2 partially reviewed / 4 needs review

Approval Policy and Tool Safeguards Partially reviewed - Full taxonomy validation

0 of 2 (0%) / 3 of 6 (50%) 3 capability gaps

Channel Access Control Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Credential and Secret Hygiene Partially reviewed - Full taxonomy validation

0 of 5 (0%) / 5 of 11 (45.5%) 6 capability gaps

Device and Node Pairing Needs review - Full taxonomy validation

0 of 11 (0%) / 0 of 11 (0%) 11 capability gaps

Gateway Auth and Remote Access Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Plugin Trust Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Session, memory, and context engine - 9 areas

2 needs review / 7 partially reviewed

CLI Session and Transcript Management Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Context Engine Partially reviewed - Full taxonomy validation

0 of 2 (0%) / 4 of 7 (57.1%) 3 capability gaps

Core Prompts and Context Partially reviewed - Full taxonomy validation

0 of 2 (0%) / 3 of 8 (37.5%) 5 capability gaps

Cross-client History and Session Parity Partially reviewed - Full taxonomy validation

0 of 2 (0%) / 2 of 5 (40%) 3 capability gaps

Diagnostics, Maintenance, and Recovery Partially reviewed - Full taxonomy validation

0 of 3 (0%) / 4 of 10 (40%) 6 capability gaps

Memory Partially reviewed - Full taxonomy validation

0 of 5 (0%) / 6 of 13 (46.2%) 7 capability gaps

Session Routing Partially reviewed - Full taxonomy validation

0 of 2 (0%) / 1 of 4 (25%) 3 capability gaps

Token Management Partially reviewed - Full taxonomy validation

0 of 3 (0%) / 2 of 10 (20%) 8 capability gaps

Transcript Persistence Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Signal - 5 areas

5 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Media and Rich Content Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Native Controls and Approvals Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Slack - 5 areas

5 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Media and Rich Content Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Native Controls and Approvals Needs review - Full taxonomy validation

0 of 8 (0%) / 0 of 8 (0%) 8 capability gaps

Telegram - 5 areas

5 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Media and Rich Content Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Native Controls and Approvals Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Observability - 5 areas

3 partially reviewed / 2 needs review

Diagnostic Collection Partially reviewed - Full taxonomy validation

1 of 8 (12.5%) / 3 of 10 (30%) 7 capability gaps

Health and Repair Partially reviewed - Full taxonomy validation

1 of 12 (8.3%) / 5 of 18 (27.8%) 13 capability gaps

Logging Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Session Diagnostics Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Telemetry Export Partially reviewed - Full taxonomy validation

1 of 13 (7.7%) / 7 of 21 (33.3%) 14 capability gaps

TUI - 5 areas

5 needs review

Input and Commands Needs review - Full taxonomy validation

0 of 8 (0%) / 0 of 8 (0%) 8 capability gaps

Local Shell Execution Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Rendering and Output Safety Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Runtime Modes Needs review - Full taxonomy validation

0 of 14 (0%) / 0 of 14 (0%) 14 capability gaps

Session Management Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Voice and realtime talk - 6 areas

6 needs review

Native App Talk Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Realtime Talk Sessions Needs review - Full taxonomy validation

0 of 11 (0%) / 0 of 11 (0%) 11 capability gaps

Speech and Transcription Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Talk Observability Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Talk Providers Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Voice Wake and Routing Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Voice Call channel - 5 areas

5 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 1 (0%) / 0 of 1 (0%) 1 capability gap

Media and Rich Content Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Realtime Voice and Calls Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

watchOS companion surfaces - 5 areas

5 needs review

Delivery and Recovery Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Distribution and Support Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

Exec Approvals Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Notifications and Replies Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Watch App UI Needs review - Full taxonomy validation

0 of 3 (0%) / 0 of 3 (0%) 3 capability gaps

Web search tools - 4 areas

2 needs review / 2 partially reviewed

Network Safety Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Search Providers Partially reviewed - Full taxonomy validation

2 of 19 (10.5%) / 2 of 19 (10.5%) 17 capability gaps

Setup and Diagnostics Needs review - Full taxonomy validation

0 of 9 (0%) / 0 of 9 (0%) 9 capability gaps

Tool Availability and Fetch Partially reviewed - Full taxonomy validation

2 of 11 (18.2%) / 3 of 12 (25%) 9 capability gaps

WhatsApp - 5 areas

5 needs review

Access and Identity Needs review - Full taxonomy validation

0 of 7 (0%) / 0 of 7 (0%) 7 capability gaps

Channel Setup and Operations Needs review - Full taxonomy validation

0 of 5 (0%) / 0 of 5 (0%) 5 capability gaps

Conversation Routing and Delivery Needs review - Full taxonomy validation

0 of 4 (0%) / 0 of 4 (0%) 4 capability gaps

Media and Rich Content Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Native Controls and Approvals Needs review - Full taxonomy validation

0 of 2 (0%) / 0 of 2 (0%) 2 capability gaps

Windows via WSL2 - 6 areas

5 needs review / 1 partially reviewed

Browser and Control UI Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

CLI Needs review - Full taxonomy validation

0 of 8 (0%) / 0 of 8 (0%) 8 capability gaps

Diagnostics and Repair Partially reviewed - Full taxonomy validation

1 of 6 (16.7%) / 3 of 8 (37.5%) 5 capability gaps

Gateway Access and Exposure Needs review - Full taxonomy validation

0 of 11 (0%) / 0 of 11 (0%) 11 capability gaps

Gateway Service Lifecycle Needs review - Full taxonomy validation

0 of 10 (0%) / 0 of 10 (0%) 10 capability gaps

WSL Setup Needs review - Full taxonomy validation

0 of 6 (0%) / 0 of 6 (0%) 6 capability gaps

> Last updated: 2026-06-22

Was this useful?YesNo

Open issue