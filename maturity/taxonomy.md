---
title: Maturity taxonomy
source_url: https://docs.openclaw.ai/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Maturity taxonomy

the model behind the scorecard

Surfaces > categories > capabilities > evidence.

50 surfaces grouped into 4 families, with every category tied back to canonical docs and QA coverage IDs.

Browse product areas / Open detailed taxonomy / [View scores](</maturity/scorecard>)

## How to read this page

A surface is a product area such as Gateway runtime, Discord, or the macOS app. Each surface contains categories, and each category contains the capability-level checks that QA scenarios cover. Use the scorecard for release-level judgment; use this page to inspect the model underneath it.

## Maturity levels

M0PlannedDirection is known, but no supported user path exists.Promotion: Design issue, owner, and target surface exist.

M1ExperimentalImplemented behind caveats, flags, source builds, or maintainer-only flows.Promotion: Maintainer can run the scenario from current main.

M2AlphaReal users can try it, but breaking changes and incomplete UX are expected.Promotion: Documented setup, basic tests, known caveats, and at least one real-environment proof.

M3BetaPublic path exists and the main workflow is usable with bounded caveats.Promotion: Install/update docs, regression tests, support runbook, and successful scenario proof across the expected environment.

M4StableRecommended path for normal users. Failures are treated as regressions.Promotion: Release gate, doctor/troubleshooting path, broad docs, and repeated real-world proof.

M5ClawesomePolished, delightful, well-instrumented, and competitive with the best comparable workflow.Promotion: Stable plus user scorecard pass across representative users.

## Product areas

### Core

CLI M4Stable7 areas - 90% complete Gateway runtime M4Stable13 areas - 89% complete Agent Runtime M3Beta9 areas - 79% complete Session, memory, and context engine M3Beta9 areas - 79% complete Channel framework M3Beta8 areas - 79% complete Observability M3Beta5 areas - 79% complete Gateway Web App M3Beta6 areas - 79% complete Plugins M3Beta9 areas - 79% complete Security, auth, pairing, and secrets M3Beta6 areas - 79% complete Automation: cron, hooks, tasks, polling M3Beta6 areas - 79% complete Media understanding and media generation M2Alpha6 areas - 68% complete Voice and realtime talk M2Alpha6 areas - 68% complete TUI M2Alpha5 areas - 66% complete ClawHub M2Alpha4 areas - 62% complete OpenClaw App SDK M2Alpha6 areas - 53% complete

### Platform

Linux Gateway host M4Stable5 areas - 89% complete macOS Gateway host M4Stable7 areas - 88% complete Docker and Podman hosting M3Beta4 areas - 79% complete Windows via WSL2 M3Beta6 areas - 79% complete Raspberry Pi and small Linux devices M3Beta4 areas - 79% complete macOS companion app M3Beta8 areas - 78% complete Android app M2Alpha7 areas - 66% complete Native Windows M2Alpha4 areas - 66% complete Kubernetes hosting M2Alpha4 areas - 61% complete iOS app M1Experimental8 areas - 44% complete Nix install path M1Experimental5 areas - 44% complete watchOS companion surfaces M1Experimental5 areas - 44% complete Linux companion app M0Planned5 areas - 21% complete Native Windows companion app M0Planned5 areas - 21% complete

### Channel

Discord M4Stable6 areas - 87% complete Telegram M3Beta5 areas - 78% complete Slack M3Beta5 areas - 78% complete iMessage and BlueBubbles M3Beta5 areas - 78% complete WhatsApp M3Beta5 areas - 78% complete Matrix M2Alpha6 areas - 67% complete Google Chat M2Alpha5 areas - 66% complete Microsoft Teams M2Alpha5 areas - 66% complete Signal M2Alpha5 areas - 66% complete Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regional channels M2Alpha4 areas - 58% complete Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alpha4 areas - 54% complete Voice Call channel M1Experimental5 areas - 44% complete

### Provider and tool

Browser automation, exec, and sandbox tools M3Beta3 areas - 79% complete OpenAI and Codex provider path M3Beta5 areas - 79% complete Web search tools M3Beta4 areas - 79% complete Anthropic provider path M3Beta5 areas - 78% complete Google provider path M3Beta5 areas - 78% complete OpenRouter provider path M3Beta4 areas - 78% complete Image, video, and music generation tools M2Alpha5 areas - 68% complete Local model providers: Ollama, vLLM, SGLang, LM Studio M2Alpha5 areas - 68% complete Long-tail hosted providers M2Alpha3 areas - 68% complete

## Details

### Core

CLI - M4 Stable - 7 areas

Normal setup and repair paths are documented across install, CLI, and gateway docs. Platform-specific Windows paths are tracked in the Windows via WSL2 and Native Windows rows.

Coverage Experimental - 4%Quality Stable - 83%Completeness Stable - 90%Partial - 6

CLI Setup 6 capabilities / LTS-supported

Experimental17%

Stable89%

Stable90%

[Index](</install>), [Installer](</install/installer>), [Node](</install/node>), [Updating](</install/updating>)

Onboarding and Auth Setup 5 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Onboard](</cli/onboard>), [Configure](</cli/configure>), [Onboarding Overview](</start/onboarding-overview>)

Plugin and Channel Setup 5 capabilities

Experimental0%

Beta75%

Stable89%

[Onboard](</cli/onboard>), [Plugins](</cli/plugins>), [Channels](</cli/channels>)

Gateway Service Management 5 capabilities / LTS-supported

Experimental14%

Stable87%

Stable90%

[Gateway](</cli/gateway>), [Updating](</install/updating>), [Troubleshooting](</gateway/troubleshooting>)

CLI Observability 5 capabilities / LTS-supported

Experimental0%

Stable89%

Stable90%

[Status](</cli/status>), [Health](</cli/health>), [Logs](</cli/logs>), [Diagnostics](</gateway/diagnostics>)

Doctor 10 capabilities / LTS-supported

Experimental0%

Stable89%

Stable90%

[Doctor](</cli/doctor>), [Doctor](</gateway/doctor>), [Secrets](</gateway/secrets>), [Troubleshooting](</gateway/troubleshooting>)

Updates and Upgrades 5 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Updating](</install/updating>), [Update](</cli/update>), [Troubleshooting](</gateway/troubleshooting>)

Gateway runtime - M4 Stable - 13 areas

Core architecture, auth, pairing, protocol docs, daemon docs, and CLI runbooks are broad and current.

Coverage Experimental - 6%Quality Stable - 81%Completeness Stable - 89%Partial - 12

Approvals and Remote Execution 6 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Protocol](</gateway/protocol>), [Index](</gateway/security>)

HTTP APIs 4 capabilities / LTS-supported

Experimental25%

Stable90%

Stable90%

[Index](</gateway>), [Openai Http Api](</gateway/openai-http-api>), [Openresponses Http Api](</gateway/openresponses-http-api>), [Tools Invoke Http Api](</gateway/tools-invoke-http-api>), [Hooks](</automation/hooks>), [Index](</web>)

Hosted Web Surface 4 capabilities / LTS-supported

Experimental0%

Stable89%

Stable90%

[Index](</gateway>), [Architecture](</concepts/architecture>), [Control Ui](</web/control-ui>), [Webchat](</web/webchat>), [Canvas](</refactor/canvas>)

Gateway RPC APIs and Events 20 capabilities / LTS-supported

Experimental9%

Stable90%

Stable90%

[Protocol](</gateway/protocol>), [Index](</gateway>), [Architecture](</concepts/architecture>)

Device Auth and Pairing 10 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Protocol](</gateway/protocol>), [Pairing](</gateway/pairing>), [Index](</gateway/security>)

Network Access and Discovery 6 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Index](</gateway>), [Discovery](</gateway/discovery>), [Protocol](</gateway/protocol>)

Nodes and Remote Capabilities 8 capabilities

Experimental0%

Beta75%

Stable89%

[Protocol](</gateway/protocol>), [Architecture](</concepts/architecture>), [Index](</nodes>)

Health, Diagnostics, and Repair 7 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Index](</gateway>), [Diagnostics](</gateway/diagnostics>), [Doctor](</gateway/doctor>)

Protocol Compatibility 7 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Protocol](</gateway/protocol>), [Architecture](</concepts/architecture>), [Typebox](</concepts/typebox>), [Bridge Protocol](</gateway/bridge-protocol>)

Roles and Permissions 5 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Protocol](</gateway/protocol>), [Index](</gateway/security>)

Gateway Lifecycle 7 capabilities / LTS-supported

Experimental33%

Stable90%

Stable90%

[Index](</gateway>), [Architecture](</concepts/architecture>)

Security Controls 6 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Index](</gateway/security>), [Protocol](</gateway/protocol>), [Discovery](</gateway/discovery>)

WebSocket Connection 8 capabilities / LTS-supported

Experimental13%

Stable90%

Stable90%

[Protocol](</gateway/protocol>), [Architecture](</concepts/architecture>)

Agent Runtime - M3 Beta - 9 areas

Main loop, models, provider routing, and tool streaming are first-class, but provider behavior shifts weekly and needs scenario proof per release.

Coverage Experimental - 33%Quality Beta - 78%Completeness Beta - 79%Partial - 6

Agent Turn Execution 3 capabilities / LTS-supported

Experimental29%

Beta79%

Beta79%

[Agent Loop](</concepts/agent-loop>), [Agent](</cli/agent>), [Agent Runtimes](</concepts/agent-runtimes>)

External Runtimes and Subagents 4 capabilities

Experimental30%

Beta79%

Beta79%

[Agent Runtimes](</concepts/agent-runtimes>), [Anthropic](</providers/anthropic>), [Google](</providers/google>), [Subagents](</tools/subagents>)

Hosted Provider Execution 5 capabilities / LTS-supported

Experimental20%

Beta79%

Beta79%

[Openai](</providers/openai>), [Anthropic](</providers/anthropic>), [Google](</providers/google>), [Models](</concepts/models>)

Local and Self-hosted Providers 5 capabilities

Experimental0%

Alpha68%

Beta79%

[Ollama](</providers/ollama>), [Models](</concepts/models>), [Agent](</cli/agent>)

Model and Runtime Selection 4 capabilities / LTS-supported

Experimental25%

Beta79%

Beta79%

[Models](</concepts/models>), [Models](</cli/models>), [Openai](</providers/openai>), [Agent Runtimes](</concepts/agent-runtimes>)

Provider Auth 10 capabilities / LTS-supported

Experimental24%

Beta79%

Beta79%

[Models](</concepts/models>), [Agent](</cli/agent>), [Models](</cli/models>), [Openai](</providers/openai>), [Anthropic](</providers/anthropic>), [Google](</providers/google>), [Subagents](</tools/subagents>)

Streaming and Progress 2 capabilities

Alpha56%

Beta79%

Beta79%

[Streaming](</concepts/streaming>), [Agent Loop](</concepts/agent-loop>)

Tool Calls and Response Handling 3 capabilities / LTS-supported

Alpha65%

Beta79%

Beta79%

[Agent Loop](</concepts/agent-loop>), [Ollama](</providers/ollama>)

Tool Execution Controls 6 capabilities / LTS-supported

Alpha50%

Beta79%

Beta79%

[Sandbox Vs Tool Policy Vs Elevated](</gateway/sandbox-vs-tool-policy-vs-elevated>), [Agent Loop](</concepts/agent-loop>), [Subagents](</tools/subagents>)

Session, memory, and context engine - M3 Beta - 9 areas

Strong docs and active implementation. Maturity depends on transcript durability, compaction quality, and cross-client parity.

Coverage Experimental - 30%Quality Beta - 77%Completeness Beta - 79%Partial - 6

CLI Session and Transcript Management 2 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Session](</concepts/session>), [Session Management Compaction](</reference/session-management-compaction>), [Sessions](</cli/sessions>)

Token Management 3 capabilities / LTS-supported

Experimental20%

Beta79%

Beta79%

[Compaction](</concepts/compaction>), [Context](</concepts/context>), [Session Management Compaction](</reference/session-management-compaction>)

Context Engine 2 capabilities / LTS-supported

Alpha57%

Beta79%

Beta79%

[Context](</concepts/context>), [Context Engine](</concepts/context-engine>), [Codex Context Engine Harness](</plan/codex-context-engine-harness>)

Cross-client History and Session Parity 2 capabilities

Experimental40%

Beta79%

Beta79%

[Webchat](</web/webchat>), [Android](</platforms/android>), [Channel Routing](</channels/channel-routing>)

Diagnostics, Maintenance, and Recovery 3 capabilities

Experimental40%

Beta79%

Beta79%

[Diagnostics](</gateway/diagnostics>), [Session Management Compaction](</reference/session-management-compaction>), [Flags](</diagnostics/flags>)

Core Prompts and Context 2 capabilities / LTS-supported

Experimental38%

Beta79%

Beta79%

[Context](</concepts/context>), [Transcript Hygiene](</reference/transcript-hygiene>), [Discord](</channels/discord>)

Memory 5 capabilities

Experimental46%

Beta79%

Beta79%

[Memory Config](</reference/memory-config>), [Memory Qmd](</concepts/memory-qmd>), [Memory](</concepts/memory>), [Discord](</channels/discord>)

Session Routing 2 capabilities / LTS-supported

Experimental25%

Beta79%

Beta79%

[Session](</concepts/session>), [Channel Routing](</channels/channel-routing>), [Discord](</channels/discord>)

Transcript Persistence 2 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Session Management Compaction](</reference/session-management-compaction>), [Transcript Hygiene](</reference/transcript-hygiene>)

Channel framework - M3 Beta - 8 areas

Many channels share Gateway delivery and routing contracts, but channel behavior varies by upstream API and account-policy constraints.

Coverage Experimental - 13%Quality Beta - 76%Completeness Beta - 79%Partial - 5

Channel Actions Commands and Approvals 5 capabilities

Experimental0%

Beta79%

Beta79%

[Groups](</channels/groups>), [Discord](</channels/discord>), [Googlechat](</channels/googlechat>), [Signal](</channels/signal>), [Matrix](</channels/matrix>)

Channel Setup 5 capabilities / LTS-supported

Experimental14%

Beta79%

Beta79%

[Index](</channels>), [Pairing](</channels/pairing>), [Troubleshooting](</channels/troubleshooting>), [Sdk Channel Plugins](</plugins/sdk-channel-plugins>)

Group Thread and Ambient Room Behavior 5 capabilities

Experimental36%

Beta79%

Beta79%

[Groups](</channels/groups>), [Group Messages](</channels/group-messages>), [Ambient Room Events](</channels/ambient-room-events>), [Broadcast Groups](</channels/broadcast-groups>), [Discord](</channels/discord>)

Inbound Access and Identity Gates 5 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Access Groups](</channels/access-groups>), [Groups](</channels/groups>), [Discord](</channels/discord>), [Line](</channels/line>)

Media Attachments and Rich Channel Data 4 capabilities

Experimental0%

Alpha68%

Beta79%

[Line](</channels/line>), [Signal](</channels/signal>), [Googlechat](</channels/googlechat>), [Matrix](</channels/matrix>), [Discord](</channels/discord>)

Outbound Delivery and Reply Pipeline 4 capabilities / LTS-supported

Experimental38%

Beta79%

Beta79%

[Groups](</channels/groups>), [Ambient Room Events](</channels/ambient-room-events>), [Discord](</channels/discord>), [Matrix](</channels/matrix>), [Config Channels](</gateway/config-channels>)

Conversation Routing and Delivery 10 capabilities / LTS-supported

Experimental19%

Beta79%

Beta79%

[Channel Routing](</channels/channel-routing>), [Groups](</channels/groups>), [Discord](</channels/discord>), [Matrix](</channels/matrix>), [Troubleshooting](</channels/troubleshooting>), [Configuration Reference](</gateway/configuration-reference>)

Status Health and Operator Controls 4 capabilities / LTS-supported

Experimental0%

Beta79%

Beta79%

[Health](</gateway/health>), [Configuration Reference](</gateway/configuration-reference>), [Troubleshooting](</channels/troubleshooting>), [Discord](</channels/discord>)

Observability - M3 Beta - 5 areas

OTel, Prometheus, logging, and diagnostics docs exist. Needs a public "what operators should look at first" maturity pass.

Coverage Experimental - 18%Quality Beta - 75%Completeness Beta - 79%Partial - 3

Health and Repair 12 capabilities / LTS-supported

Experimental28%

Beta79%

Beta79%

[Health](</gateway/health>), [Telegram](</channels/telegram>), [Doctor](</cli/doctor>), [Doctor](</gateway/doctor>), [Sdk Subpaths](</plugins/sdk-subpaths>), [Health](</cli/health>), [Protocol](</gateway/protocol>)

Logging 5 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Logging](</logging>), [Logging](</gateway/logging>), [Logs](</cli/logs>)

Diagnostic Collection 8 capabilities

Experimental30%

Beta79%

Beta79%

[Diagnostics](</gateway/diagnostics>), [Health](</gateway/health>), [Codex Harness](</plugins/codex-harness>), [Protocol](</gateway/protocol>)

Telemetry Export 13 capabilities

Experimental33%

Beta79%

Beta79%

[Hooks](</plugins/hooks>), [Opentelemetry](</gateway/opentelemetry>), [Logging](</logging>), [Sdk Subpaths](</plugins/sdk-subpaths>), [Diagnostics Otel](</plugins/reference/diagnostics-otel>), [Prometheus](</gateway/prometheus>), [Diagnostics Prometheus](</plugins/reference/diagnostics-prometheus>)

Session Diagnostics 4 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Opentelemetry](</gateway/opentelemetry>), [Prometheus](</gateway/prometheus>), [Diagnostics](</gateway/diagnostics>), [Protocol](</gateway/protocol>)

Gateway Web App - M3 Beta - 6 areas

Web UI is documented with pairing, chat, PWA, Talk, push, and remote Gateway flows. Promote after cross-browser and mobile-PWA scorecards.

Coverage Experimental - 4%Quality Beta - 74%Completeness Beta - 79%None

Browser Realtime Talk 5 capabilities

Experimental0%

Alpha68%

Beta79%

[Control Ui](</web/control-ui>), [Protocol](</gateway/protocol>), [Talk](</nodes/talk>)

Browser Access and Trust 5 capabilities

Experimental0%

Alpha68%

Beta79%

[Control Ui](</web/control-ui>), [Dashboard](</web/dashboard>), [Tailscale](</gateway/tailscale>), [Remote](</gateway/remote>)

Configuration 5 capabilities

Experimental0%

Alpha68%

Beta79%

[Control Ui](</web/control-ui>), [Configuration](</gateway/configuration>)

Browser UI 10 capabilities

Experimental8%

Beta79%

Beta79%

[Control Ui](</web/control-ui>), [Index](</web>), [Dashboard](</web/dashboard>), [Protocol](</gateway/protocol>)

WebChat Conversations 15 capabilities

Experimental10%

Beta79%

Beta79%

[Control Ui](</web/control-ui>), [Webchat](</web/webchat>), [Getting Started](</start/getting-started>), [Channel Routing](</channels/channel-routing>), [Secure File Operations](</gateway/security/secure-file-operations>)

Operator Console 10 capabilities

Experimental8%

Beta79%

Beta79%

[Control Ui](</web/control-ui>), [Health](</gateway/health>), [Protocol](</gateway/protocol>), [Dashboard](</web/dashboard>)

Plugins - M3 Beta - 9 areas

Broad docs and strong internal runtime evidence exist across manifests, discovery, loading, provider/tool architecture, and approval boundaries. Keep the row at beta until public SDK API/subpaths and external distribution proof are stronger.

Coverage Experimental - 12%Quality Beta - 72%Completeness Beta - 79%Partial - 7

Authoring and Packaging plugins 8 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Building Plugins](</plugins/building-plugins>), [Sdk Overview](</plugins/sdk-overview>), [Sdk Entrypoints](</plugins/sdk-entrypoints>), [Sdk Subpaths](</plugins/sdk-subpaths>), [Manifest](</plugins/manifest>), [Reference](</plugins/reference>)

Bundled plugins 5 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Plugin Inventory](</plugins/plugin-inventory>), [Plugins](</cli/plugins>), [Architecture Internals](</plugins/architecture-internals>)

Canvas plugin 6 capabilities

Experimental0%

Alpha68%

Beta79%

[Canvas](</plugins/reference/canvas>), [Canvas](</refactor/canvas>), [Configuration Reference](</gateway/configuration-reference>)

Installing and running plugins 6 capabilities / LTS-supported

Experimental35%

Beta79%

Beta79%

[Architecture](</plugins/architecture>), [Architecture Internals](</plugins/architecture-internals>), [Plugins](</cli/plugins>)

Channel plugins 5 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Sdk Channel Plugins](</plugins/sdk-channel-plugins>), [Sdk Channel Inbound](</plugins/sdk-channel-inbound>), [Sdk Channel Outbound](</plugins/sdk-channel-outbound>)

Provider and tool plugins 6 capabilities / LTS-supported

Experimental43%

Beta79%

Beta79%

[Sdk Provider Plugins](</plugins/sdk-provider-plugins>), [Tool Plugins](</plugins/tool-plugins>), [Adding Capabilities](</plugins/adding-capabilities>)

Plugin approvals 6 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Plugin Permission Requests](</plugins/plugin-permission-requests>), [Exec Approvals](</tools/exec-approvals>), [Sdk Channel Plugins](</plugins/sdk-channel-plugins>)

Publishing plugins 6 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Plugins](</cli/plugins>), [Compatibility](</plugins/compatibility>), [Publishing](</clawhub/publishing>)

Testing plugins 6 capabilities

Experimental27%

Beta79%

Beta79%

[Sdk Testing](</plugins/sdk-testing>), [Sdk Setup](</plugins/sdk-setup>), [Codex Harness](</plugins/codex-harness>)

Security, auth, pairing, and secrets - M3 Beta - 6 areas

Good docs and hardening surfaces exist. Promote after regular upgrade/security scenario runs prove no setup regressions.

Coverage Experimental - 16%Quality Beta - 72%Completeness Beta - 79%Partial - 5

Approval Policy and Tool Safeguards 2 capabilities / LTS-supported

Alpha50%

Beta79%

Beta79%

[Exec Approvals](</tools/exec-approvals>), [Approvals](</cli/approvals>), [Plugin Permission Requests](</plugins/plugin-permission-requests>), [Audit Checks](</gateway/security/audit-checks>)

Gateway Auth and Remote Access 9 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Index](</gateway/security>), [Exposure Runbook](</gateway/security/exposure-runbook>), [Trusted Proxy Auth](</gateway/trusted-proxy-auth>), [Tailscale](</gateway/tailscale>), [Remote](</gateway/remote>), [Configuration Reference](</gateway/configuration-reference>), [Gateway](</cli/gateway>), [Doctor](</cli/doctor>), [Control Ui](</web/control-ui>), [Browser Control](</tools/browser-control>), [Audit Checks](</gateway/security/audit-checks>)

Channel Access Control 3 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Pairing](</channels/pairing>), [Telegram](</channels/telegram>), [Access Groups](</channels/access-groups>), [Audit Checks](</gateway/security/audit-checks>)

Device and Node Pairing 11 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Protocol](</gateway/protocol>), [Devices](</cli/devices>), [Pairing](</channels/pairing>), [Pairing](</gateway/pairing>), [Operator Scopes](</gateway/operator-scopes>), [Control Ui](</web/control-ui>), [Webchat](</web/webchat>), [Approvals](</cli/approvals>)

Plugin Trust 2 capabilities

Experimental0%

Alpha68%

Beta79%

[Manifest](</plugins/manifest>), [Plugin Permission Requests](</plugins/plugin-permission-requests>), [Manage Plugins](</plugins/manage-plugins>), [Audit Checks](</gateway/security/audit-checks>)

Credential and Secret Hygiene 5 capabilities / LTS-supported

Experimental46%

Beta79%

Beta79%

[Authentication](</gateway/authentication>), [Models](</cli/models>), [Openai](</providers/openai>), [Oauth](</concepts/oauth>), [Secrets](</gateway/secrets>), [Secrets](</cli/secrets>), [Secretref Credential Surface](</reference/secretref-credential-surface>), [Audit Checks](</gateway/security/audit-checks>)

Automation: cron, hooks, tasks, polling - M3 Beta - 6 areas

Documented and usable, but scenario proof should cover unattended delivery, retries, and failure visibility.

Coverage Experimental - 2%Quality Beta - 72%Completeness Beta - 79%None

Cron Jobs 15 capabilities

Experimental0%

Beta79%

Beta79%

[Cron Jobs](</automation/cron-jobs>), [Cron](</cli/cron>), [Protocol](</gateway/protocol>), [Tasks](</automation/tasks>), [Discord](</channels/discord>)

Event Ingress 15 capabilities

Experimental0%

Alpha68%

Beta79%

[Telegram](</channels/telegram>), [Zalo](</channels/zalo>), [Troubleshooting](</channels/troubleshooting>), [Imessage From Bluebubbles](</channels/imessage-from-bluebubbles>), [Gmail Pubsub Integration](</automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</automation/gmail-pubsub>), [Webhooks](</cli/webhooks>), [Webhooks](</automation/cron-jobs#webhooks>), [Webhook](</automation/webhook>)

Automation Hooks 11 capabilities

Experimental0%

Alpha68%

Beta79%

[Hooks](</automation/hooks>), [Hooks](</cli/hooks>), [Hooks](</plugins/hooks>), [Plugin Permission Requests](</plugins/plugin-permission-requests>), [Sdk Subpaths](</plugins/sdk-subpaths>)

Background Tasks and Flows 10 capabilities

Experimental0%

Alpha68%

Beta79%

[Tasks](</automation/tasks>), [Index](</automation>), [Tasks](</cli/tasks>), [Taskflow](</automation/taskflow>), [Sdk Runtime](</plugins/sdk-runtime>)

Heartbeat 5 capabilities

Experimental14%

Beta79%

Beta79%

[Index](</automation>), [Heartbeat](</gateway/heartbeat>), [Commitments](</concepts/commitments>)

Polling Controls 10 capabilities

Experimental0%

Alpha68%

Beta79%

[Poll](</automation/poll>), [Message](</cli/message>), [Telegram](</channels/telegram>), [Msteams](</channels/msteams>), [Background Process](</gateway/background-process>)

Media understanding and media generation - M2 Alpha - 6 areas

Broad capability surface exists, but provider variance, file limits, and node/app parity make this not stable yet.

Coverage Experimental - 2%Quality Alpha - 64%Completeness Alpha - 68%None

Media Intake and Access 8 capabilities

Experimental0%

Alpha61%

Alpha68%

[Media Overview](</tools/media-overview>), [Media Understanding](</nodes/media-understanding>), [Secure File Operations](</gateway/security/secure-file-operations>), [Pdf](</tools/pdf>), [Image Generation](</tools/image-generation>), [Qr](</cli/qr>), [Line](</channels/line>), [Whatsapp](</channels/whatsapp>)

Channel Media Handling 5 capabilities

Experimental0%

Alpha61%

Alpha68%

[Images](</nodes/images>), [Media Overview](</tools/media-overview>), [Discord](</channels/discord>)

Media Configuration 1 capabilities

Experimental0%

Alpha61%

Alpha68%

[Media Overview](</tools/media-overview>), [Image Generation](</tools/image-generation>), [Manifest](</plugins/manifest>), [Codex Harness](</plugins/codex-harness>)

Text-to-Speech Delivery 2 capabilities

Experimental0%

Alpha61%

Alpha68%

[Tts](</tools/tts>), [Media Overview](</tools/media-overview>), [Discord](</channels/discord>)

Media Understanding 12 capabilities

Experimental7%

Alpha69%

Alpha69%

[Audio](</nodes/audio>), [Media Understanding](</nodes/media-understanding>), [Media Overview](</tools/media-overview>), [Whatsapp](</channels/whatsapp>), [Images](</nodes/images>), [Infer](</cli/infer>), [Pdf](</tools/pdf>)

Media Generation 17 capabilities

Experimental5%

Alpha69%

Alpha69%

[Image Generation](</tools/image-generation>), [Media Overview](</tools/media-overview>), [Skills](</tools/skills>), [Music Generation](</tools/music-generation>), [Video Generation](</tools/video-generation>)

Voice and realtime talk - M2 Alpha - 6 areas

Multiple implementations exist across Control UI, apps, and providers. Needs latency, failure-mode, and setup scorecards before beta.

Coverage Experimental - 0%Quality Alpha - 61%Completeness Alpha - 68%None

Talk Providers 7 capabilities

Experimental0%

Alpha61%

Alpha68%

[Openai](</providers/openai>), [Google](</providers/google>), [Sdk Provider Plugins](</plugins/sdk-provider-plugins>), [Talk](</nodes/talk>), [Control Ui](</web/control-ui>)

Realtime Talk Sessions 11 capabilities

Experimental0%

Alpha61%

Alpha68%

[Talk](</nodes/talk>), [Control Ui](</web/control-ui>)

Speech and Transcription 5 capabilities

Experimental0%

Alpha61%

Alpha68%

[Talk](</nodes/talk>), [Openai](</providers/openai>), [Google](</providers/google>)

Native App Talk 4 capabilities

Experimental0%

Alpha61%

Alpha68%

[Talk](</nodes/talk>), [Voicewake](</platforms/mac/voicewake>)

Voice Wake and Routing 4 capabilities

Experimental0%

Alpha61%

Alpha68%

[Voicewake](</nodes/voicewake>), [Voicewake](</platforms/mac/voicewake>), [Voice Overlay](</platforms/mac/voice-overlay>)

Talk Observability 5 capabilities

Experimental0%

Alpha61%

Alpha68%

[Control Ui](</web/control-ui>), [Voice Overlay](</platforms/mac/voice-overlay>), [Talk](</nodes/talk>)

TUI - M2 Alpha - 5 areas

Present in docs and source, but less visible as a primary user workflow. Needs explicit scenario definition.

Coverage Experimental - 0%Quality Alpha - 59%Completeness Alpha - 66%None

Runtime Modes 14 capabilities

Experimental0%

Alpha59%

Alpha66%

[Tui](</cli/tui>), [Tui](</web/tui>), [Index](</cli>)

Input and Commands 8 capabilities

Experimental0%

Alpha59%

Alpha66%

[Tui](</web/tui>)

Session Management 3 capabilities

Experimental0%

Alpha59%

Alpha66%

[Tui](</web/tui>), [Sessions](</cli/sessions>)

Local Shell Execution 4 capabilities

Experimental0%

Alpha59%

Alpha66%

[Tui](</web/tui>), [Tui](</cli/tui>)

Rendering and Output Safety 4 capabilities

Experimental0%

Alpha59%

Alpha66%

[Tui](</web/tui>), [Qr](</cli/qr>), [Logs](</cli/logs>), [Completion](</cli/completion>)

ClawHub - M2 Alpha - 4 areas

Public docs and ecosystem concept exist. Needs install, trust, update, rollback, and compatibility scorecards.

Coverage Experimental - 0%Quality Alpha - 58%Completeness Alpha - 62%None

Publishing 7 capabilities

Experimental0%

Alpha54%

Alpha55%

[Publishing](</clawhub/publishing>), [Creating Skills](</tools/creating-skills>), [Community](</plugins/community>)

Catalog Discovery 5 capabilities

Experimental0%

Alpha61%

Alpha68%

[Plugin](</tools/plugin>), [Plugins](</cli/plugins>), [Skills](</cli/skills>), [Skills](</tools/skills>), [Community](</plugins/community>)

Compatibility and Trust 12 capabilities

Experimental0%

Alpha55%

Alpha56%

[Plugin](</tools/plugin>), [Plugins](</cli/plugins>), [Compatibility](</plugins/compatibility>), [Plugin Inventory](</plugins/plugin-inventory>), [Publishing](</clawhub/publishing>), [Skills](</tools/skills>), [Skills Config](</tools/skills-config>)

Plugin Lifecycle and Health 26 capabilities

Experimental0%

Alpha61%

Alpha68%

[Plugin](</tools/plugin>), [Plugins](</cli/plugins>), [Skills](</cli/skills>), [Skills](</tools/skills>), [Protocol](</gateway/protocol>), [Bundles](</plugins/bundles>), [Dependency Resolution](</plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 areas

OpenClaw App SDK is a distinct external app contract separate from Gateway runtime and Plugin SDK. Current scoring shows a real `@openclaw/sdk` path with gaps around public packaging, auto-discovery, approvals, helpers, and compatibility.

Coverage Experimental - 3%Quality Alpha - 54%Completeness Alpha - 53%None

Client API 4 capabilities

Experimental0%

Alpha51%

Alpha50%

[Openclaw Sdk](</gateway/external-apps>), [Openclaw Sdk Api Design](</gateway/external-apps>)

Gateway Access 5 capabilities

Experimental0%

Alpha53%

Alpha54%

[Openclaw Sdk](</gateway/external-apps>), [Openclaw Sdk Api Design](</gateway/external-apps>), [Protocol](</gateway/protocol>), [Index](</gateway/security>)

Agent Conversations 6 capabilities

Experimental0%

Alpha52%

Alpha52%

[Openclaw Sdk](</gateway/external-apps>), [Openclaw Sdk Api Design](</gateway/external-apps>), [Protocol](</gateway/protocol>)

Events and Approvals 5 capabilities

Experimental0%

Alpha52%

Alpha52%

[Openclaw Sdk](</gateway/external-apps>), [Openclaw Sdk Api Design](</gateway/external-apps>), [Protocol](</gateway/protocol>)

Resource Helpers 5 capabilities

Experimental17%

Alpha62%

Alpha53%

[Openclaw Sdk](</gateway/external-apps>), [Openclaw Sdk Api Design](</gateway/external-apps>)

Compatibility 5 capabilities

Experimental0%

Alpha54%

Alpha55%

[Openclaw Sdk Api Design](</gateway/external-apps>), [Typebox](</concepts/typebox>), [Protocol](</gateway/protocol>)

### Platform

Linux Gateway host - M4 Stable - 5 areas

Node runtime is recommended, systemd user service is documented, and VPS/container guidance is broad.

Coverage Experimental - 0%Quality Beta - 75%Completeness Stable - 89%Partial - 4

Host Setup and Updates 4 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Index](</install>), [Updating](</install/updating>), [Linux](</platforms/linux>), [Index](</platforms>)

Gateway Runtime and Service Control 6 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Index](</gateway>), [Gateway](</cli/gateway>), [Linux](</platforms/linux>), [Vps](</vps>)

Remote Access and Security 6 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Remote](</gateway/remote>), [Tailscale](</gateway/tailscale>), [Exposure Runbook](</gateway/security/exposure-runbook>), [Authentication](</gateway/authentication>), [Secrets](</gateway/secrets>)

Diagnostics and Repair 4 capabilities / LTS-supported

Experimental0%

Beta75%

Stable89%

[Status](</cli/status>), [Logs](</cli/logs>), [Doctor](</cli/doctor>), [Diagnostics](</gateway/diagnostics>), [Index](</gateway>)

Deployment Targets 3 capabilities

Experimental0%

Beta75%

Stable89%

[Vps](</vps>), [Docker](</install/docker>), [Hetzner](</install/hetzner>), [Digitalocean](</install/digitalocean>), [Kubernetes](</install/kubernetes>), [Podman](</install/podman>)

macOS Gateway host - M4 Stable - 7 areas

LaunchAgent service path, local/remote Gateway modes, CLI install, and app integration are documented.

Coverage Experimental - 0%Quality Beta - 74%Completeness Stable - 88%None

CLI Setup 4 capabilities

Experimental0%

Beta74%

Stable88%

[Macos](</platforms/macos>), [Bundled Gateway](</platforms/mac/bundled-gateway>), [Installer](</install/installer>), [Node](</install/node>)

Local Gateway Integration 9 capabilities

Experimental0%

Beta74%

Stable88%

[Macos](</platforms/macos>), [Bundled Gateway](</platforms/mac/bundled-gateway>), [Remote](</platforms/mac/remote>), [Index](</gateway>), [Gateway](</cli/gateway>), [Bonjour](</gateway/bonjour>)

Remote Gateway Mode 5 capabilities

Experimental0%

Beta74%

Stable88%

[Remote](</platforms/mac/remote>), [Remote](</gateway/remote>), [Tailscale](</gateway/tailscale>)

Gateway Service Lifecycle 10 capabilities

Experimental0%

Beta74%

Stable88%

[Macos](</platforms/macos>), [Bundled Gateway](</platforms/mac/bundled-gateway>), [Gateway](</cli/gateway>), [Index](</gateway>), [Update](</cli/update>), [Updating](</install/updating>), [Uninstall](</install/uninstall>), [Troubleshooting](</gateway/troubleshooting>)

Diagnostics and Observability 4 capabilities

Experimental0%

Beta74%

Stable88%

[Bundled Gateway](</platforms/mac/bundled-gateway>), [Macos](</platforms/macos>), [Gateway](</cli/gateway>), [Doctor](</gateway/doctor>), [Troubleshooting](</gateway/troubleshooting>)

Permissions and Native Capabilities 4 capabilities

Experimental0%

Beta74%

Stable88%

[Macos](</platforms/macos>), [Remote](</platforms/mac/remote>)

Profiles and Isolation 5 capabilities

Experimental0%

Beta74%

Stable88%

[Multiple Gateways](</gateway/multiple-gateways>), [Index](</gateway>), [Gateway](</cli/gateway>)

Docker and Podman hosting - M3 Beta - 4 areas

Install docs exist and are common deployment paths. Promote after recurring release smoke captures upgrade and volume behavior.

Coverage Experimental - 7%Quality Beta - 71%Completeness Beta - 79%None

Container Setup 6 capabilities

Experimental0%

Alpha68%

Beta79%

[Docker](</install/docker>), [Podman](</install/podman>)

Container Operations 11 capabilities

Experimental0%

Alpha68%

Beta79%

[Podman](</install/podman>), [Docker Vm Runtime](</install/docker-vm-runtime>), [Docker](</install/docker>), [Hetzner](</install/hetzner>), [Hostinger](</install/hostinger>)

Image Release and Validation 5 capabilities

Experimental29%

Beta79%

Beta79%

[Docker](</install/docker>), [Docker Vm Runtime](</install/docker-vm-runtime>), [Full Release Validation](</reference/full-release-validation>)

Agent Sandbox and Tooling 3 capabilities

Experimental0%

Alpha68%

Beta79%

[Docker](</install/docker>), [Docker Vm Runtime](</install/docker-vm-runtime>)

Windows via WSL2 - M3 Beta - 6 areas

Recommended Windows path with systemd/user-service guidance and boot-chain docs. Promote after repeated install/update scorecards.

Coverage Experimental - 6%Quality Alpha - 69%Completeness Beta - 79%Partial - 5

WSL Setup 6 capabilities / LTS-supported

Experimental0%

Alpha67%

Beta79%

[Windows](</platforms/windows>), [Getting Started](</start/getting-started>)

CLI 8 capabilities / LTS-supported

Experimental0%

Alpha67%

Beta79%

[Windows](</platforms/windows>), [Getting Started](</start/getting-started>), [Updating](</install/updating>), [Onboard](</cli/onboard>), [Doctor](</cli/doctor>), [Status](</cli/status>), [Logs](</cli/logs>)

Gateway Service Lifecycle 10 capabilities / LTS-supported

Experimental0%

Alpha67%

Beta79%

[Windows](</platforms/windows>), [Index](</gateway>), [Doctor](</gateway/doctor>)

Gateway Access and Exposure 11 capabilities / LTS-supported

Experimental0%

Alpha67%

Beta79%

[Authentication](</gateway/authentication>), [Secrets](</gateway/secrets>), [Remote](</gateway/remote>), [Exposure Runbook](</gateway/security/exposure-runbook>), [Windows](</platforms/windows>)

Diagnostics and Repair 6 capabilities / LTS-supported

Experimental38%

Beta79%

Beta79%

[Windows](</platforms/windows>), [Status](</cli/status>), [Logs](</cli/logs>), [Doctor](</cli/doctor>), [Doctor](</gateway/doctor>)

Browser and Control UI 6 capabilities

Experimental0%

Alpha67%

Beta79%

[Browser Wsl2 Windows Remote Cdp Troubleshooting](</tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Browser](</tools/browser>), [Control Ui](</web/control-ui>)

Raspberry Pi and small Linux devices - M3 Beta - 4 areas

Platform docs exist and Gateway path is Linux-based. Needs hardware-specific release smoke proof to move higher.

Coverage Experimental - 0%Quality Alpha - 67%Completeness Beta - 79%None

Setup and Compatibility 12 capabilities

Experimental0%

Alpha67%

Beta79%

[Raspberry Pi](</install/raspberry-pi>), [Index](</install>), [Faq First Run](</help/faq-first-run>), [Faq](</help/faq>), [Linux](</platforms/linux>), [Installer](</install/installer>)

Remote Access and Auth 9 capabilities

Experimental0%

Alpha67%

Beta79%

[Raspberry Pi](</install/raspberry-pi>), [Authentication](</gateway/authentication>), [Secrets](</gateway/secrets>), [Pairing](</gateway/pairing>), [Devices](</cli/devices>), [Remote](</gateway/remote>), [Tailscale](</gateway/tailscale>)

Gateway Runtime 10 capabilities

Experimental0%

Alpha67%

Beta79%

[Index](</gateway>), [Gateway](</cli/gateway>), [Raspberry Pi](</install/raspberry-pi>), [Linux](</platforms/linux>), [Vps](</vps>)

Performance and Diagnostics 5 capabilities

Experimental0%

Alpha67%

Beta79%

[Raspberry Pi](</install/raspberry-pi>), [Linux](</platforms/linux>), [Health](</gateway/health>), [Diagnostics](</gateway/diagnostics>)

macOS companion app - M3 Beta - 8 areas

Rich menu bar app, permissions, node mode, Canvas, voice wake, WebChat, and remote mode exist. Still fast-moving enough to avoid Stable.

Coverage Experimental - 0%Quality Alpha - 66%Completeness Beta - 78%None

Canvas 4 capabilities

Experimental0%

Alpha66%

Beta78%

[Canvas](</platforms/mac/canvas>), [Macos](</platforms/macos>), [Webchat](</web/webchat>)

Local Setup 7 capabilities

Experimental0%

Alpha66%

Beta78%

[Bundled Gateway](</platforms/mac/bundled-gateway>), [Macos](</platforms/macos>), [Child Process](</platforms/mac/child-process>), [Dev Setup](</platforms/mac/dev-setup>)

Status and Settings 5 capabilities

Experimental0%

Alpha66%

Beta78%

[Menu Bar](</platforms/mac/menu-bar>), [Icon](</platforms/mac/icon>), [Macos](</platforms/macos>), [Health](</platforms/mac/health>), [Logging](</platforms/mac/logging>), [Remote](</platforms/mac/remote>)

Native Capabilities 5 capabilities

Experimental0%

Alpha66%

Beta78%

[Macos](</platforms/macos>), [Xpc](</platforms/mac/xpc>), [Permissions](</platforms/mac/permissions>), [Signing](</platforms/mac/signing>), [Peekaboo](</platforms/mac/peekaboo>)

Remote Connections 3 capabilities

Experimental0%

Alpha66%

Beta78%

[Remote](</platforms/mac/remote>), [Macos](</platforms/macos>), [Remote](</gateway/remote>)

Voice and Talk 3 capabilities

Experimental0%

Alpha66%

Beta78%

[Voicewake](</platforms/mac/voicewake>), [Voice Overlay](</platforms/mac/voice-overlay>), [Talk](</nodes/talk>), [Macos](</platforms/macos>)

WebChat 3 capabilities

Experimental0%

Alpha66%

Beta78%

[Webchat](</platforms/mac/webchat>), [Macos](</platforms/macos>), [Webchat](</web/webchat>)

Remote WebChat 5 capabilities

Experimental0%

Alpha66%

Beta78%

[Webchat](</platforms/mac/webchat>), [Remote](</gateway/remote>), [Remote](</platforms/mac/remote>)

Android app - M2 Alpha - 7 areas

Public Google Play path exists, but app docs still describe the rebuild as extremely alpha and call out release hardening work.

Coverage Experimental - 0%Quality Alpha - 59%Completeness Alpha - 66%None

Media Capture 1 capabilities

Experimental0%

Alpha59%

Alpha66%

[Android](</platforms/android>), [Camera](</nodes/camera>)

Mobile Chat 1 capabilities

Experimental0%

Alpha59%

Alpha66%

[Android](</platforms/android>)

Connection Setup 1 capabilities

Experimental0%

Alpha59%

Alpha66%

[Android](</platforms/android>), [Bonjour](</gateway/bonjour>), [Pairing](</gateway/pairing>)

Distribution 3 capabilities

Experimental0%

Alpha59%

Alpha66%

[Android](</platforms/android>)

Settings 1 capabilities

Experimental0%

Alpha59%

Alpha66%

[Android](</platforms/android>)

Voice 1 capabilities

Experimental0%

Alpha59%

Alpha66%

[Android](</platforms/android>), [Talk](</nodes/talk>)

Device Runtime 2 capabilities

Experimental0%

Alpha59%

Alpha66%

[Android](</platforms/android>), [Troubleshooting](</nodes/troubleshooting>), [Protocol](</gateway/protocol>)

Native Windows - M2 Alpha - 4 areas

Core CLI/Gateway flows work, but docs still recommend WSL2 for the full experience and list native caveats.

Coverage Experimental - 0%Quality Alpha - 58%Completeness Alpha - 66%Partial - 1

CLI 9 capabilities / LTS-supported

Experimental0%

Alpha54%

Alpha64%

[Index](</install>), [Installer](</install/installer>), [Windows](</platforms/windows>), [Getting Started](</start/getting-started>), [Onboard](</cli/onboard>)

Gateway Management 11 capabilities

Experimental0%

Alpha59%

Alpha66%

[Windows](</platforms/windows>), [Index](</gateway>), [Gateway](</cli/gateway>), [Doctor](</cli/doctor>)

Networking 4 capabilities

Experimental0%

Alpha59%

Alpha66%

[Windows](</platforms/windows>), [Index](</gateway>), [Gateway](</cli/gateway>)

Updates 4 capabilities

Experimental0%

Alpha59%

Alpha66%

[Updating](</install/updating>), [Ci](</ci>)

Kubernetes hosting - M2 Alpha - 4 areas

Kubernetes hosting is a distinct Kustomize-based cluster deployment path. Current scoring shows a real minimal deployment path with gaps around Kubernetes-specific CI, ingress/TLS/NetworkPolicy packaging, backup/restore, and production exposure hardening.

Coverage Experimental - 0%Quality Alpha - 55%Completeness Alpha - 61%None

Deployment Setup 5 capabilities

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</install/kubernetes>), [Index](</install>)

Configuration and Secrets 5 capabilities

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</install/kubernetes>), [Secrets](</gateway/secrets>), [Environment](</help/environment>)

Access and Exposure 5 capabilities

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</install/kubernetes>), [Authentication](</gateway/authentication>), [Remote](</gateway/remote>), [Exposure Runbook](</gateway/security/exposure-runbook>)

Cluster Lifecycle 5 capabilities

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</install/kubernetes>), [Index](</gateway>)

iOS app - M1 Experimental - 8 areas

Internal preview / super-alpha. TestFlight and relay-backed push flows exist, but no public distribution yet.

Coverage Experimental - 0%Quality Experimental - 41%Completeness Experimental - 44%None

Media and Sharing 1 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>), [Camera](</nodes/camera>)

Canvas and Screen 1 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>), [Canvas](</plugins/reference/canvas>)

Chat and Sessions 1 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>), [Webchat](</web/webchat>), [Protocol](</gateway/protocol>)

Gateway Setup and Diagnostics 7 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>), [Pairing](</channels/pairing>)

Distribution 1 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>)

Device Commands 2 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>), [Protocol](</gateway/protocol>)

Notifications and Background 1 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>), [Configuration](</gateway/configuration>)

Voice 1 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>), [Talk](</nodes/talk>)

Nix install path - M1 Experimental - 5 areas

Optional install flow. Needs clearer support promise before alpha/beta promotion.

Coverage Experimental - 0%Quality Experimental - 41%Completeness Experimental - 44%None

Install Handoff 4 capabilities

Experimental0%

Experimental41%

Experimental44%

[Nix](</install/nix>), [Index](</install>), [Docs Directory](</start/docs-directory>)

Plugin Lifecycle 4 capabilities

Experimental0%

Experimental41%

Experimental44%

[Manage Plugins](</plugins/manage-plugins>), [Plugin](</tools/plugin>), [Nix](</install/nix>)

Activation and App UX 7 capabilities

Experimental0%

Experimental41%

Experimental44%

[Nix](</install/nix>)

Config and State 7 capabilities

Experimental0%

Experimental41%

Experimental44%

[Nix](</install/nix>), [Setup](</cli/setup>), [Environment](</help/environment>)

Service Runtime and Guards 8 capabilities

Experimental0%

Experimental41%

Experimental44%

[Nix](</install/nix>), [Setup](</cli/setup>), [Doctor](</cli/doctor>), [Update](</cli/update>)

watchOS companion surfaces - M1 Experimental - 5 areas

Source has Watch app/extension surfaces; public docs do not yet present this as a user feature.

Coverage Experimental - 0%Quality Experimental - 41%Completeness Experimental - 44%None

Delivery and Recovery 7 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>)

Exec Approvals 3 capabilities

Experimental0%

Experimental41%

Experimental44%

[Exec Approvals](</tools/exec-approvals>), [Ios](</platforms/ios>)

Distribution and Support 6 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>)

Notifications and Replies 7 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>)

Watch App UI 3 capabilities

Experimental0%

Experimental41%

Experimental44%

[Ios](</platforms/ios>)

Linux companion app - M0 Planned - 5 areas

Docs say native Linux companion apps are planned; Gateway is the supported Linux path today.

Coverage Experimental - 0%Quality Experimental - 19%Completeness Experimental - 21%None

App Distribution 3 capabilities

Experimental0%

Experimental19%

Experimental21%

[Linux](</platforms/linux>), [Index](</platforms>), [Index](</install>)

Gateway Connectivity 4 capabilities

Experimental0%

Experimental19%

Experimental21%

[Linux](</platforms/linux>), [Index](</gateway>), [Pairing](</gateway/pairing>), [Remote](</gateway/remote>)

Chat and Sessions 3 capabilities

Experimental0%

Experimental19%

Experimental21%

[Linux](</platforms/linux>), [Protocol](</gateway/protocol>), [Webchat](</web/webchat>)

Desktop Capabilities 9 capabilities

Experimental0%

Experimental19%

Experimental21%

[Linux](</platforms/linux>), [Exec Approvals](</tools/exec-approvals>), [Secrets](</gateway/secrets>), [Index](</nodes>), [Exec](</tools/exec>), [Talk](</nodes/talk>), [Camera](</nodes/camera>)

Status and Diagnostics 7 capabilities

Experimental0%

Experimental19%

Experimental21%

[Linux](</platforms/linux>), [Openclaw](</start/openclaw>), [Doctor](</gateway/doctor>)

Native Windows companion app - M0 Planned - 5 areas

Planned only.

Coverage Experimental - 0%Quality Experimental - 19%Completeness Experimental - 21%None

Installation and Updates 4 capabilities

Experimental0%

Experimental19%

Experimental21%

[Windows](</platforms/windows>), [Index](</install>)

Gateway Connection 3 capabilities

Experimental0%

Experimental19%

Experimental21%

[Windows](</platforms/windows>), [Index](</gateway>), [Pairing](</gateway/pairing>), [Remote](</gateway/remote>)

Chat Sessions 2 capabilities

Experimental0%

Experimental19%

Experimental21%

[Windows](</platforms/windows>), [Protocol](</gateway/protocol>)

Status and Repair 5 capabilities

Experimental0%

Experimental19%

Experimental21%

[Windows](</platforms/windows>), [Doctor](</gateway/doctor>), [Index](</gateway>)

Desktop Tools and Permissions 10 capabilities

Experimental0%

Experimental19%

Experimental21%

[Windows](</platforms/windows>), [Index](</nodes>), [Exec](</tools/exec>), [Exec Approvals](</tools/exec-approvals>), [Index](</gateway/security>)

### Channel

Discord - M4 Stable - 6 areas

Deep docs and broad feature coverage. Voice/delegation paths should stay separately scored as beta/alpha.

Coverage Experimental - 0%Quality Beta - 73%Completeness Stable - 87%Partial - 4

Channel Setup and Operations 10 capabilities / LTS-supported

Experimental0%

Beta73%

Stable87%

[Discord](</channels/discord>), [Discord](</plugins/reference/discord>), [Fly](</install/fly>), [Slash Commands](</tools/slash-commands>), [Health](</gateway/health>), [Channels](</cli/channels>), [Config Channels](</gateway/config-channels>)

Access and Identity 6 capabilities / LTS-supported

Experimental0%

Beta73%

Stable87%

[Discord](</channels/discord>), [Pairing](</channels/pairing>), [Access Groups](</channels/access-groups>), [Groups](</channels/groups>)

Conversation Routing and Delivery 12 capabilities / LTS-supported

Experimental0%

Beta73%

Stable87%

[Discord](</channels/discord>), [Channel Routing](</channels/channel-routing>), [Groups](</channels/groups>), [Access Groups](</channels/access-groups>), [Acp Agents](</tools/acp-agents>), [Subagents](</tools/subagents>)

Media and Rich Content 1 capabilities / LTS-supported

Experimental0%

Beta73%

Stable87%

[Discord](</channels/discord>)

Native Controls and Approvals 5 capabilities

Experimental0%

Beta73%

Stable87%

[Discord](</channels/discord>), [Slash Commands](</tools/slash-commands>)

Realtime Voice and Calls 5 capabilities

Experimental0%

Beta73%

Stable87%

[Discord](</channels/discord>), [Openai](</providers/openai>), [Elevenlabs](</providers/elevenlabs>), [Qa E2e Automation](</concepts/qa-e2e-automation>), [Config Channels](</gateway/config-channels>)

Telegram - M3 Beta - 5 areas

Core channel is mature enough for regular use, but high-variance UX and media edge cases need recurring scenario proof.

Coverage Experimental - 0%Quality Alpha - 68%Completeness Beta - 78%Full - 5

Channel Setup and Operations 10 capabilities / LTS-supported

Experimental0%

Alpha66%

Beta78%

[Telegram](</channels/telegram>), [Config Channels](</gateway/config-channels>), [Channels](</cli/channels>)

Access and Identity 10 capabilities / LTS-supported

Experimental0%

Alpha66%

Beta78%

[Telegram](</channels/telegram>), [Pairing](</channels/pairing>), [Access Groups](</channels/access-groups>), [Groups](</channels/groups>), [Multi Agent](</concepts/multi-agent>)

Conversation Routing and Delivery 1 capabilities / LTS-supported

Experimental0%

Alpha66%

Beta78%

[Telegram](</channels/telegram>), [Groups](</channels/groups>), [Multi Agent](</concepts/multi-agent>)

Media and Rich Content 1 capabilities / LTS-supported

Experimental0%

Alpha66%

Beta78%

[Telegram](</channels/telegram>), [Location](</channels/location>)

Native Controls and Approvals 9 capabilities / LTS-supported

Experimental0%

Beta77%

Beta79%

[Telegram](</channels/telegram>), [Exec Approvals](</tools/exec-approvals>), [Reactions](</tools/reactions>)

Slack - M3 Beta - 5 areas

First-class channel docs and routing surface. Needs workspace install/admin scenario scorecards.

Coverage Experimental - 0%Quality Alpha - 66%Completeness Beta - 78%Full - 5

Channel Setup and Operations 10 capabilities / LTS-supported

Experimental0%

Alpha66%

Beta78%

[Slack](</channels/slack>), [Slack](</plugins/reference/slack>), [Secrets](</gateway/secrets>), [Qa E2e Automation](</concepts/qa-e2e-automation>), [Troubleshooting](</channels/troubleshooting>)

Access and Identity 1 capabilities / LTS-supported

Experimental0%

Alpha66%

Beta78%

[Slack](</channels/slack>), [Pairing](</channels/pairing>)

Conversation Routing and Delivery 5 capabilities / LTS-supported

Experimental0%

Alpha66%

Beta78%

[Slack](</channels/slack>), [Bot Loop Protection](</channels/bot-loop-protection>), [Pairing](</channels/pairing>)

Media and Rich Content 1 capabilities / LTS-supported

Experimental0%

Alpha66%

Beta78%

[Slack](</channels/slack>), [Qa E2e Automation](</concepts/qa-e2e-automation>)

Native Controls and Approvals 8 capabilities / LTS-supported

Experimental0%

Alpha66%

Beta78%

[Slack](</channels/slack>), [Slash Commands](</tools/slash-commands>), [Exec Approvals](</tools/exec-approvals>)

iMessage and BlueBubbles - M3 Beta - 5 areas

Supported iMessage runs through imsg on a signed-in macOS Messages host; legacy BlueBubbles configs require migration. Keep macOS permissions, SSH wrapper, SIP/private API, and migration caveats visible.

Coverage Experimental - 0%Quality Alpha - 66%Completeness Beta - 78%None

Channel Setup and Operations 11 capabilities

Experimental0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</announcements/bluebubbles-imessage>), [Imessage From Bluebubbles](</channels/imessage-from-bluebubbles>), [Config Channels](</gateway/config-channels>), [Imessage](</channels/imessage>)

Access and Identity 6 capabilities

Experimental0%

Alpha66%

Beta78%

[Imessage](</channels/imessage>), [Imessage From Bluebubbles](</channels/imessage-from-bluebubbles>), [Config Channels](</gateway/config-channels>)

Conversation Routing and Delivery 4 capabilities

Experimental0%

Alpha66%

Beta78%

[Imessage](</channels/imessage>)

Media and Rich Content 7 capabilities

Experimental0%

Alpha66%

Beta78%

[Imessage](</channels/imessage>), [Imessage From Bluebubbles](</channels/imessage-from-bluebubbles>), [Config Channels](</gateway/config-channels>)

Native Controls and Approvals 3 capabilities

Experimental0%

Alpha66%

Beta78%

[Imessage](</channels/imessage>)

WhatsApp - M3 Beta - 5 areas

Core path is important and documented; upstream Baileys/session volatility keeps it below Stable.

Coverage Experimental - 0%Quality Alpha - 66%Completeness Beta - 78%None

Channel Setup and Operations 5 capabilities

Experimental0%

Alpha66%

Beta78%

[Whatsapp](</channels/whatsapp>), [Config Channels](</gateway/config-channels>), [Whatsapp](</plugins/reference/whatsapp>), [Qa E2e Automation](</concepts/qa-e2e-automation>), [Doctor](</gateway/doctor>)

Access and Identity 7 capabilities

Experimental0%

Alpha66%

Beta78%

[Whatsapp](</channels/whatsapp>), [Config Channels](</gateway/config-channels>), [Qa E2e Automation](</concepts/qa-e2e-automation>), [Pairing](</channels/pairing>)

Conversation Routing and Delivery 4 capabilities

Experimental0%

Alpha66%

Beta78%

[Whatsapp](</channels/whatsapp>), [Group Messages](</channels/group-messages>)

Media and Rich Content 2 capabilities

Experimental0%

Alpha66%

Beta78%

[Whatsapp](</channels/whatsapp>)

Native Controls and Approvals 2 capabilities

Experimental0%

Alpha66%

Beta78%

[Whatsapp](</channels/whatsapp>)

Matrix - M2 Alpha - 6 areas

Supported via bundled plugin. Needs bridge, auth, and room lifecycle scorecards.

Coverage Experimental - 0%Quality Alpha - 60%Completeness Alpha - 67%None

Channel Setup and Operations 5 capabilities

Experimental0%

Alpha60%

Alpha67%

[Matrix](</channels/matrix>), [Matrix Migration](</channels/matrix-migration>)

Access and Identity 7 capabilities

Experimental0%

Alpha60%

Alpha67%

[Matrix](</channels/matrix>), [Groups](</channels/groups>), [Bot Loop Protection](</channels/bot-loop-protection>)

Conversation Routing and Delivery 1 capabilities

Experimental0%

Alpha60%

Alpha67%

[Matrix](</channels/matrix>)

Media and Rich Content 1 capabilities

Experimental0%

Alpha60%

Alpha67%

[Matrix](</channels/matrix>)

Native Controls and Approvals 6 capabilities

Experimental0%

Alpha60%

Alpha67%

[Matrix](</channels/matrix>)

Encryption and Verification 3 capabilities

Experimental0%

Alpha60%

Alpha67%

[Matrix](</channels/matrix>), [Matrix Migration](</channels/matrix-migration>)

Google Chat - M2 Alpha - 5 areas

Documented channel, but enterprise/admin setup raises maturity risk.

Coverage Experimental - 0%Quality Alpha - 59%Completeness Alpha - 66%None

Channel Setup and Operations 16 capabilities

Experimental0%

Alpha59%

Alpha66%

[Googlechat](</channels/googlechat>), [Googlechat](</plugins/reference/googlechat>), [Config Channels](</gateway/config-channels>), [Wizard Cli Reference](</start/wizard-cli-reference>), [Secrets](</gateway/secrets>), [Secretref Credential Surface](</reference/secretref-credential-surface>), [Health](</gateway/health>), [Plugin Inventory](</plugins/plugin-inventory>), [Index](</channels>)

Access and Identity 11 capabilities

Experimental0%

Alpha59%

Alpha66%

[Googlechat](</channels/googlechat>), [Pairing](</channels/pairing>), [Access Groups](</channels/access-groups>), [Config Channels](</gateway/config-channels>), [Bot Loop Protection](</channels/bot-loop-protection>), [Channel Routing](</channels/channel-routing>)

Conversation Routing and Delivery 1 capabilities

Experimental0%

Alpha59%

Alpha66%

[Googlechat](</channels/googlechat>), [Bot Loop Protection](</channels/bot-loop-protection>), [Access Groups](</channels/access-groups>), [Channel Routing](</channels/channel-routing>)

Media and Rich Content 1 capabilities

Experimental0%

Alpha59%

Alpha66%

[Googlechat](</channels/googlechat>), [Message](</cli/message>), [Media Understanding](</nodes/media-understanding>), [Secretref Credential Surface](</reference/secretref-credential-surface>)

Native Controls and Approvals 16 capabilities

Experimental0%

Alpha59%

Alpha66%

[Googlechat](</channels/googlechat>), [Message](</cli/message>), [Media Understanding](</nodes/media-understanding>), [Secretref Credential Surface](</reference/secretref-credential-surface>), [Reactions](</tools/reactions>), [Slash Commands](</tools/slash-commands>), [Config Agents](</gateway/config-agents>), [Message Lifecycle Refactor](</concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 areas

Enterprise auth/admin flows need explicit scenario proof.

Coverage Experimental - 0%Quality Alpha - 59%Completeness Alpha - 66%None

Channel Setup and Operations 9 capabilities

Experimental0%

Alpha59%

Alpha66%

[Msteams](</channels/msteams>), [Msteams](</plugins/reference/msteams>), [Config Channels](</gateway/config-channels>), [Health](</gateway/health>)

Access and Identity 9 capabilities

Experimental0%

Alpha59%

Alpha66%

[Msteams](</channels/msteams>), [Pairing](</channels/pairing>), [Access Groups](</channels/access-groups>)

Conversation Routing and Delivery 5 capabilities

Experimental0%

Alpha59%

Alpha66%

[Msteams](</channels/msteams>), [Groups](</channels/groups>), [Channel Routing](</channels/channel-routing>)

Media and Rich Content 5 capabilities

Experimental0%

Alpha59%

Alpha66%

[Msteams](</channels/msteams>)

Native Controls and Approvals 5 capabilities

Experimental0%

Alpha59%

Alpha66%

[Msteams](</channels/msteams>), [Exec Approvals Advanced](</tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 areas

Supported channel docs exist; needs stronger install and reconnect proof.

Coverage Experimental - 0%Quality Alpha - 59%Completeness Alpha - 66%None

Channel Setup and Operations 7 capabilities

Experimental0%

Alpha59%

Alpha66%

[Signal](</channels/signal>), [Signal](</plugins/reference/signal>)

Access and Identity 6 capabilities

Experimental0%

Alpha59%

Alpha66%

[Signal](</channels/signal>)

Conversation Routing and Delivery 1 capabilities

Experimental0%

Alpha59%

Alpha66%

[Signal](</channels/signal>)

Media and Rich Content 7 capabilities

Experimental0%

Alpha59%

Alpha66%

[Signal](</channels/signal>)

Native Controls and Approvals 3 capabilities

Experimental0%

Alpha59%

Alpha66%

[Signal](</channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regional channels - M2 Alpha - 4 areas

Important regional coverage, but public support level should be calibrated per account type, upstream approval, and maintainer proof.

Coverage Experimental - 0%Quality Alpha - 55%Completeness Alpha - 58%None

Channel Setup and Operations 6 capabilities

Experimental0%

Alpha61%

Alpha68%

[Index](</channels>), [Pairing](</channels/pairing>), [Feishu](</plugins/reference/feishu>), [Architecture Internals](</plugins/architecture-internals>)

Access and Identity 1 capabilities

Experimental0%

Alpha53%

Alpha54%

No linked docs

Conversation Routing and Delivery 1 capabilities

Experimental0%

Alpha53%

Alpha54%

No linked docs

Media and Rich Content 1 capabilities

Experimental0%

Alpha53%

Alpha54%

No linked docs

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 areas

Supported surfaces exist, but maturity likely varies by upstream and maintainer coverage. Score individually later.

Coverage Experimental - 0%Quality Alpha - 53%Completeness Alpha - 54%None

Channel Setup and Operations 1 capabilities

Experimental0%

Alpha53%

Alpha54%

No linked docs

Access and Identity 1 capabilities

Experimental0%

Alpha53%

Alpha54%

No linked docs

Conversation Routing and Delivery 1 capabilities

Experimental0%

Alpha53%

Alpha54%

No linked docs

Media and Rich Content 1 capabilities

Experimental0%

Alpha53%

Alpha54%

No linked docs

Voice Call channel - M1 Experimental - 5 areas

Optional/plugin path with complex realtime behavior. Needs scenario scorecard before public beta.

Coverage Experimental - 0%Quality Experimental - 41%Completeness Experimental - 44%None

Channel Setup and Operations 2 capabilities

Experimental0%

Experimental41%

Experimental44%

[Voicecall](</cli/voicecall>), [Voice Call](</plugins/voice-call>), [Protocol](</gateway/protocol>)

Access and Identity 1 capabilities

Experimental0%

Experimental41%

Experimental44%

[Voice Call](</plugins/voice-call>), [Voicecall](</cli/voicecall>)

Conversation Routing and Delivery 1 capabilities

Experimental0%

Experimental41%

Experimental44%

[Voice Call](</plugins/voice-call>)

Media and Rich Content 2 capabilities

Experimental0%

Experimental41%

Experimental44%

[Voice Call](</plugins/voice-call>), [Plugin Inventory](</plugins/plugin-inventory>)

Realtime Voice and Calls 2 capabilities

Experimental0%

Experimental41%

Experimental44%

[Voice Call](</plugins/voice-call>)

### Provider and tool

Browser automation, exec, and sandbox tools - M3 Beta - 3 areas

Core tools are documented, but host security and permission UX should stay under active scorecard review.

Coverage Experimental - 21%Quality Beta - 75%Completeness Beta - 79%Partial - 2

Browser Automation 8 capabilities

Experimental13%

Beta79%

Beta79%

[Browser Control](</tools/browser-control>), [Testing](</help/testing>), [Browser](</tools/browser>), [Index](</gateway/security>), [Audit Checks](</gateway/security/audit-checks>)

Tool Invocation and Execution 6 capabilities / LTS-supported

Alpha50%

Beta79%

Beta79%

[Exec](</tools/exec>), [Background Process](</gateway/background-process>), [Tools Invoke Http Api](</gateway/tools-invoke-http-api>), [Operator Scopes](</gateway/operator-scopes>), [Protocol](</gateway/protocol>), [Exec Approvals](</tools/exec-approvals>), [Exec Approvals Advanced](</tools/exec-approvals-advanced>), [Elevated](</tools/elevated>)

Sandbox and Tool Policy 6 capabilities / LTS-supported

Experimental0%

Alpha68%

Beta79%

[Sandboxing](</gateway/sandboxing>), [Sandbox Vs Tool Policy Vs Elevated](</gateway/sandbox-vs-tool-policy-vs-elevated>), [Multi Agent Sandbox Tools](</tools/multi-agent-sandbox-tools>), [Codex Harness Reference](</plugins/codex-harness-reference>), [Config Tools](</gateway/config-tools>)

OpenAI and Codex provider path - M3 Beta - 5 areas

Deep docs, OAuth/subscription path, realtime voice, image, and compatibility behavior. Provider churn keeps this from Stable without release-scorecard proof.

Coverage Experimental - 26%Quality Beta - 74%Completeness Beta - 79%Partial - 3

Model and Auth 6 capabilities / LTS-supported

Experimental44%

Beta79%

Beta79%

[Openai](</providers/openai>), [Codex Harness](</plugins/codex-harness>), [Models](</concepts/models>), [Oauth](</concepts/oauth>), [Codex Harness Reference](</plugins/codex-harness-reference>), [Auth Monitoring](</automation/auth-monitoring>)

Responses and Tool Compatibility 4 capabilities / LTS-supported

Experimental40%

Beta79%

Beta79%

[Openai](</providers/openai>), [Openresponses Http Api](</gateway/openresponses-http-api>), [Openai Http Api](</gateway/openai-http-api>), [Codex Native Plugins](</plugins/codex-native-plugins>)

Native Codex Harness 2 capabilities / LTS-supported

Experimental44%

Beta79%

Beta79%

[Codex Harness](</plugins/codex-harness>), [Codex Harness Runtime](</plugins/codex-harness-runtime>), [Codex Harness Reference](</plugins/codex-harness-reference>), [Codex Native Plugins](</plugins/codex-native-plugins>)

Image and Multimodal Input 2 capabilities

Experimental0%

Alpha67%

Beta79%

[Openai](</providers/openai>), [Image Generation](</tools/image-generation>), [Images](</nodes/images>)

Voice and Realtime Audio 2 capabilities

Experimental0%

Alpha67%

Beta79%

[Openai](</providers/openai>), [Discord](</channels/discord>), [Voice Call](</plugins/voice-call>)

Web search tools - M3 Beta - 4 areas

Multiple providers and docs exist. Needs quota/error/SSRF proof per provider family.

Coverage Experimental - 9%Quality Beta - 74%Completeness Beta - 79%None

Search Providers 19 capabilities

Experimental11%

Beta79%

Beta79%

[Web](</tools/web>), [Brave Search](</tools/brave-search>), [Tavily](</tools/tavily>), [Exa Search](</tools/exa-search>), [Firecrawl](</tools/firecrawl>), [Perplexity Search](</tools/perplexity-search>), [Duckduckgo Search](</tools/duckduckgo-search>), [Searxng Search](</tools/searxng-search>), [Gemini Search](</tools/gemini-search>), [Grok Search](</tools/grok-search>), [Kimi Search](</tools/kimi-search>), [Minimax Search](</tools/minimax-search>), [Ollama Search](</tools/ollama-search>), [Sdk Subpaths](</plugins/sdk-subpaths>), [Sdk Overview](</plugins/sdk-overview>), [Manifest](</plugins/manifest>)

Setup and Diagnostics 9 capabilities

Experimental0%

Alpha68%

Beta79%

[Web](</tools/web>), [Web Fetch](</tools/web-fetch>), [Faq](</help/faq>), [Api Usage Costs](</reference/api-usage-costs>), [Brave Search](</tools/brave-search>), [Perplexity Search](</tools/perplexity-search>), [Tavily](</tools/tavily>), [Firecrawl](</tools/firecrawl>)

Network Safety 4 capabilities

Experimental0%

Alpha68%

Beta79%

[Web](</tools/web>), [Web Fetch](</tools/web-fetch>), [Firecrawl](</tools/firecrawl>), [Searxng Search](</tools/searxng-search>)

Tool Availability and Fetch 11 capabilities

Experimental25%

Beta79%

Beta79%

[Config Tools](</gateway/config-tools>), [Web Fetch](</tools/web-fetch>), [Web](</tools/web>), [Faq](</help/faq>)

Anthropic provider path - M3 Beta - 5 areas

First-class model provider. Needs recurring auth/catalog/tool-call scenario proof.

Coverage Experimental - 0%Quality Beta - 71%Completeness Beta - 78%None

Provider Auth and Recovery 9 capabilities

Experimental0%

Alpha66%

Beta78%

[Anthropic](</providers/anthropic>), [Doctor](</gateway/doctor>), [Configuration Examples](</gateway/configuration-examples>), [Troubleshooting](</gateway/troubleshooting>), [Prompt Caching](</reference/prompt-caching>)

Model and Runtime Selection 10 capabilities

Experimental0%

Beta78%

Beta79%

[Anthropic](</providers/anthropic>), [Config Agents](</gateway/config-agents>), [Models](</concepts/models>), [Cli Backends](</gateway/cli-backends>)

Request Transport and Turn Semantics 10 capabilities

Experimental0%

Beta77%

Beta79%

[Anthropic](</providers/anthropic>), [Prompt Caching](</reference/prompt-caching>), [Troubleshooting](</gateway/troubleshooting>), [Cli Backends](</gateway/cli-backends>), [Model Providers](</concepts/model-providers>)

Prompt Cache and Context 5 capabilities

Experimental0%

Alpha66%

Beta78%

[Anthropic](</providers/anthropic>), [Prompt Caching](</reference/prompt-caching>), [Troubleshooting](</gateway/troubleshooting>), [Heartbeat](</gateway/heartbeat>)

Media Inputs 4 capabilities

Experimental0%

Alpha66%

Beta78%

[Anthropic](</providers/anthropic>), [Config Agents](</gateway/config-agents>)

Google provider path - M3 Beta - 5 areas

First-class provider with model and realtime surfaces. Needs separate Live/Talk scoring.

Coverage Experimental - 0%Quality Alpha - 66%Completeness Beta - 78%None

Provider Setup and Credentials 10 capabilities

Experimental0%

Alpha66%

Beta78%

[Google](</providers/google>), [Model Providers](</concepts/model-providers>)

Model Routing and Endpoints 10 capabilities

Experimental0%

Alpha66%

Beta78%

[Google](</providers/google>), [Model Providers](</concepts/model-providers>), [Google](</plugins/reference/google>), [Gemini Search](</tools/gemini-search>)

Direct Gemini Runtime 9 capabilities

Experimental0%

Alpha66%

Beta78%

[Google](</providers/google>), [Model Providers](</concepts/model-providers>), [Faq Models](</help/faq-models>), [Testing Live](</help/testing-live>)

Media, Search, and Realtime 10 capabilities

Experimental0%

Alpha66%

Beta78%

[Google](</plugins/reference/google>), [Google](</providers/google>)

Prompt Caching 5 capabilities

Experimental0%

Alpha66%

Beta78%

[Prompt Caching](</reference/prompt-caching>), [Google](</providers/google>), [Model Providers](</concepts/model-providers>), [Token Use](</reference/token-use>)

OpenRouter provider path - M3 Beta - 4 areas

Unified provider path is documented and valuable, but model-specific behavior varies.

Coverage Experimental - 0%Quality Alpha - 66%Completeness Beta - 78%None

Provider Setup and Auth 14 capabilities

Experimental0%

Alpha66%

Beta78%

[Openrouter](</providers/openrouter>), [Model Providers](</concepts/model-providers>), [Configure](</cli/configure>), [Authentication](</gateway/authentication>), [Environment](</help/environment>), [Models](</cli/models>), [Models](</concepts/models>)

Chat Runtime and Normalization 15 capabilities

Experimental0%

Alpha66%

Beta78%

[Openrouter](</providers/openrouter>), [Model Providers](</concepts/model-providers>), [Prompt Caching](</reference/prompt-caching>)

Provider Recovery and Diagnostics 5 capabilities

Experimental0%

Alpha66%

Beta78%

[Model Failover](</concepts/model-failover>), [Openrouter](</providers/openrouter>), [Models](</cli/models>)

Media Generation and Speech 7 capabilities

Experimental0%

Alpha66%

Beta78%

[Openrouter](</providers/openrouter>), [Image Generation](</tools/image-generation>), [Music Generation](</tools/music-generation>), [Media Overview](</tools/media-overview>), [Video Generation](</tools/video-generation>), [Tts](</tools/tts>)

Image, video, and music generation tools - M2 Alpha - 5 areas

Capability exists across providers, but quality, latency, and parameter compatibility vary too much for beta without per-provider proof.

Coverage Experimental - 0%Quality Alpha - 61%Completeness Alpha - 68%None

Media Routing and Discovery 4 capabilities

Experimental0%

Alpha61%

Alpha68%

[Config Agents](</gateway/config-agents>), [Image Generation](</tools/image-generation>), [Video Generation](</tools/video-generation>), [Music Generation](</tools/music-generation>)

Task Lifecycle and Delivery 12 capabilities

Experimental0%

Alpha61%

Alpha68%

[Media Overview](</tools/media-overview>), [Image Generation](</tools/image-generation>), [Video Generation](</tools/video-generation>), [Music Generation](</tools/music-generation>)

Image Generation 9 capabilities

Experimental0%

Alpha61%

Alpha68%

[Image Generation](</tools/image-generation>), [Infer](</cli/infer>), [Media Overview](</tools/media-overview>)

Video Generation 11 capabilities

Experimental0%

Alpha61%

Alpha68%

[Video Generation](</tools/video-generation>), [Runway](</providers/runway>), [Pixverse](</providers/pixverse>), [Fal](</providers/fal>), [Openrouter](</providers/openrouter>)

Music Generation 6 capabilities

Experimental0%

Alpha61%

Alpha68%

[Music Generation](</tools/music-generation>)

Local model providers: Ollama, vLLM, SGLang, LM Studio - M2 Alpha - 5 areas

Useful and documented, but environment variance is high.

Coverage Experimental - 0%Quality Alpha - 61%Completeness Alpha - 68%None

Provider Setup, Lifecycle, and Diagnostics 12 capabilities

Experimental0%

Alpha61%

Alpha68%

[Local Models](</gateway/local-models>), [Lmstudio](</providers/lmstudio>), [Ollama](</providers/ollama>), [Vllm](</providers/vllm>), [Local Model Services](</gateway/local-model-services>), [Config Agents](</gateway/config-agents>), [Troubleshooting](</gateway/troubleshooting>), [Doctor](</gateway/doctor>)

Native Provider Plugins 10 capabilities

Experimental0%

Alpha61%

Alpha68%

[Ollama](</providers/ollama>), [Lmstudio](</providers/lmstudio>)

OpenAI-Compatible Runtime Compatibility 8 capabilities

Experimental0%

Alpha61%

Alpha68%

[Vllm](</providers/vllm>), [Sglang](</providers/sglang>), [Local Models](</gateway/local-models>), [Lmstudio](</providers/lmstudio>)

Local Memory and Embeddings 5 capabilities

Experimental0%

Alpha61%

Alpha68%

[Memory](</concepts/memory>), [Doctor](</gateway/doctor>)

Network Safety and Prompt Controls 2 capabilities

Experimental0%

Alpha61%

Alpha68%

[Index](</gateway/security>), [Config Tools](</gateway/config-tools>), [Local Models](</gateway/local-models>)

Long-tail hosted providers - M2 Alpha - 3 areas

Many docs/reference pages exist; score should be generated from provider metadata plus live smoke coverage.

Coverage Experimental - 0%Quality Alpha - 61%Completeness Alpha - 68%None

Hosted LLM Providers 12 capabilities

Experimental0%

Alpha61%

Alpha68%

[Index](</providers>), [Model Providers](</concepts/model-providers>), [Testing Live](</help/testing-live>), [Onboard](</cli/onboard>)

Hosted Media Providers 8 capabilities

Experimental0%

Alpha61%

Alpha68%

[Manifest](</plugins/manifest>), [Testing Live](</help/testing-live>), [Index](</providers>)

Provider Operations 12 capabilities

Experimental0%

Alpha61%

Alpha68%

[Index](</providers>), [Model Providers](</concepts/model-providers>), [Manifest](</plugins/manifest>), [Testing Live](</help/testing-live>), [Models](</cli/models>)

Was this useful?YesNo

Open issue