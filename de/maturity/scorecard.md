---
title: Reifegrad-Scorecard
source_url: https://docs.openclaw.ai/de/maturity/scorecard
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Reifegrad-Scorecard

Release-Bereitschaft - generiert aus Taxonomie + QA-Nachweisen

Eine praktische Sicht darauf, was bereit ist, was belegt ist und was noch Arbeit benötigt.

50 Oberflächen - 281 Fähigkeitsbereiche - deterministische Abdeckung plus von Menschen geprüfte Qualität und Vollständigkeit.

Oberflächen durchsuchen / QA-Nachweise prüfen / [Taxonomie lesen](</de/maturity/taxonomy>)

## Wofür diese Seite gedacht ist

Verwenden Sie diese Seite, um eine Frage zu beantworten: Welche OpenClaw-Oberflächen sind glaubwürdige Optionen für ein Release, und welche Nachweise stützen diese Beurteilung? Die Abdeckung stammt aus deterministischen QA-Nachweisen; Qualität und Vollständigkeit werden als geprüfte Reifegradbewertungen gepflegt.

## Auf einen Blick

67% Reifegradbewertung

Alpha Qualität + Vollständigkeit Abdeckung Experimental - 4% Qualität Alpha - 63% Vollständigkeit Beta - 70%

Die Abdeckung ist bewusst nachweisgeleitet: Ein Bereich wird nicht allein deshalb „bereit“, weil die Implementierung existiert. Sie fließt nicht in die Reifegradbewertung ein, aber OpenClaw strebt an, die End-to-End-Abdeckung für ausgereifte Stable-oder-bessere Features im Laufe der Zeit über 90% zu halten.

## Bewertungsbereiche

Experimental0-50%

Alpha50-70%

Beta70-80%

Stable80-95%

Clawesome95-100%

## Oberflächen-Explorer

Oberflächen werden nach Reifegrad, Vollständigkeit und Qualität sortiert. LTS-Unterstützung wird neben jeder Zeile angezeigt, damit Release-bereite Optionen leicht vergleichbar sind.

### Alle Oberflächen

[CLIM4Stabil7 Bereiche](</de/maturity/taxonomy#cli>)

AbdeckungExperimentell4%

QualitätStabil83%

VollständigkeitStabil90%

Teilweise - 6

[Gateway-LaufzeitM4Stabil13 Bereiche](</de/maturity/taxonomy#gateway-runtime>)

AbdeckungExperimentell6%

QualitätStabil81%

VollständigkeitStabil89%

Teilweise - 12

[Linux-Gateway-HostM4Stabil5 Bereiche](</de/maturity/taxonomy#linux-gateway-host>)

AbdeckungExperimentell0%

QualitätBeta75%

VollständigkeitStabil89%

Teilweise - 4

[macOS-Gateway-HostM4Stabil7 Bereiche](</de/maturity/taxonomy#macos-gateway-host>)

AbdeckungExperimentell0%

QualitätBeta74%

VollständigkeitStabil88%

Keine

[DiscordM4Stabil6 Bereiche](</de/maturity/taxonomy#discord>)

AbdeckungExperimentell0%

QualitätBeta73%

VollständigkeitStabil87%

Teilweise - 4

[Agent-LaufzeitM3Beta9 Bereiche](</de/maturity/taxonomy#agent-runtime>)

AbdeckungExperimentell33%

QualitätBeta78%

VollständigkeitBeta79%

Teilweise - 6

[Sitzungs-, Speicher- und Kontext-EngineM3Beta9 Bereiche](</de/maturity/taxonomy#session-memory-and-context-engine>)

AbdeckungExperimentell30%

QualitätBeta77%

VollständigkeitBeta79%

Teilweise - 6

[Channel-FrameworkM3Beta8 Bereiche](</de/maturity/taxonomy#channel-framework>)

AbdeckungExperimentell13%

QualitätBeta76%

VollständigkeitBeta79%

Teilweise - 5

[Tools für Browserautomatisierung, Exec und SandboxM3Beta3 Bereiche](</de/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

AbdeckungExperimentell21%

QualitätBeta75%

VollständigkeitBeta79%

Teilweise - 2

[ObservabilityM3Beta5 Bereiche](</de/maturity/taxonomy#observability>)

AbdeckungExperimentell18%

QualitätBeta75%

VollständigkeitBeta79%

Teilweise - 3

[OpenAI- und Codex-Provider-PfadM3Beta5 Bereiche](</de/maturity/taxonomy#openai-and-codex-provider-path>)

AbdeckungExperimentell26%

QualitätBeta74%

VollständigkeitBeta79%

Teilweise - 3

[Gateway-Web-AppM3Beta6 Bereiche](</de/maturity/taxonomy#gateway-web-app>)

AbdeckungExperimentell4%

QualitätBeta74%

VollständigkeitBeta79%

Keine

[Tools für WebsucheM3Beta4 Bereiche](</de/maturity/taxonomy#web-search-tools>)

AbdeckungExperimentell9%

QualitätBeta74%

VollständigkeitBeta79%

Keine

[PluginsM3Beta9 Bereiche](</de/maturity/taxonomy#plugins>)

AbdeckungExperimentell12%

QualitätBeta72%

VollständigkeitBeta79%

Teilweise - 7

[Sicherheit, Authentifizierung, Pairing und SecretsM3Beta6 Bereiche](</de/maturity/taxonomy#security-auth-pairing-and-secrets>)

AbdeckungExperimentell16%

QualitätBeta72%

VollständigkeitBeta79%

Teilweise - 5

[Automatisierung: Cron, Hooks, Aufgaben, PollingM3Beta6 Bereiche](</de/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

AbdeckungExperimentell2%

QualitätBeta72%

VollständigkeitBeta79%

Keine

[Docker- und Podman-HostingM3Beta4 Bereiche](</de/maturity/taxonomy#docker-and-podman-hosting>)

AbdeckungExperimentell7%

QualitätBeta71%

VollständigkeitBeta79%

Keine

[Windows über WSL2M3Beta6 Bereiche](</de/maturity/taxonomy#windows-via-wsl2>)

AbdeckungExperimentell6%

QualitätAlpha69%

VollständigkeitBeta79%

Teilweise - 5

[Raspberry Pi und kleine Linux-GeräteM3Beta4 Bereiche](</de/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

AbdeckungExperimentell0%

QualitätAlpha67%

VollständigkeitBeta79%

Keine

[Anthropic-Provider-PfadM3Beta5 Bereiche](</de/maturity/taxonomy#anthropic-provider-path>)

AbdeckungExperimentell0%

QualitätBeta71%

VollständigkeitBeta78%

Keine

[TelegramM3Beta5 Bereiche](</de/maturity/taxonomy#telegram>)

AbdeckungExperimentell0%

QualitätAlpha68%

VollständigkeitBeta78%

Vollständig - 5

[SlackM3Beta5 Bereiche](</de/maturity/taxonomy#slack>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Vollständig - 5

[Google-Provider-PfadM3Beta5 Bereiche](</de/maturity/taxonomy#google-provider-path>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[iMessage und BlueBubblesM3Beta5 Bereiche](</de/maturity/taxonomy#imessage-and-bluebubbles>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[macOS-Begleit-AppM3Beta8 Bereiche](</de/maturity/taxonomy#macos-companion-app>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[OpenRouter-Provider-PfadM3Beta4 Bereiche](</de/maturity/taxonomy#openrouter-provider-path>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[WhatsAppM3Beta5 Bereiche](</de/maturity/taxonomy#whatsapp>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[Medienverständnis und MediengenerierungM2Alpha6 Bereiche](</de/maturity/taxonomy#media-understanding-and-media-generation>)

AbdeckungExperimentell2%

QualitätAlpha64%

VollständigkeitAlpha68%

Keine

[Werkzeuge zur Bild-, Video- und MusikgenerierungM2Alpha5 Bereiche](</de/maturity/taxonomy#image-video-and-music-generation-tools>)

AbdeckungExperimentell0%

QualitätAlpha61%

VollständigkeitAlpha68%

Keine

[Lokale Modell-Provider: Ollama, vLLM, SGLang, LM StudioM2Alpha5 Bereiche](</de/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

AbdeckungExperimentell0%

QualitätAlpha61%

VollständigkeitAlpha68%

Keine

[Gehostete Long-Tail-ProviderM2Alpha3 Bereiche](</de/maturity/taxonomy#long-tail-hosted-providers>)

AbdeckungExperimentell0%

QualitätAlpha61%

VollständigkeitAlpha68%

Keine

[Sprache und EchtzeitgesprächeM2Alpha6 Bereiche](</de/maturity/taxonomy#voice-and-realtime-talk>)

AbdeckungExperimentell0%

QualitätAlpha61%

VollständigkeitAlpha68%

Keine

[MatrixM2Alpha6 Bereiche](</de/maturity/taxonomy#matrix>)

AbdeckungExperimentell0%

QualitätAlpha60%

VollständigkeitAlpha67%

Keine

[Android-AppM2Alpha7 Bereiche](</de/maturity/taxonomy#android-app>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[Google ChatM2Alpha5 Bereiche](</de/maturity/taxonomy#google-chat>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[Microsoft TeamsM2Alpha5 Bereiche](</de/maturity/taxonomy#microsoft-teams>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[SignalM2Alpha5 Bereiche](</de/maturity/taxonomy#signal>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[TUIM2Alpha5 Bereiche](</de/maturity/taxonomy#tui>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[Natives WindowsM2Alpha4 Bereiche](</de/maturity/taxonomy#native-windows>)

AbdeckungExperimentell0%

QualitätAlpha58%

VollständigkeitAlpha66%

Teilweise - 1

[ClawHubM2Alpha4 Bereiche](</de/maturity/taxonomy#clawhub>)

AbdeckungExperimentell0%

QualitätAlpha58%

VollständigkeitAlpha62%

Keine

[Kubernetes-HostingM2Alpha4 Bereiche](</de/maturity/taxonomy#kubernetes-hosting>)

AbdeckungExperimentell0%

QualitätAlpha55%

VollständigkeitAlpha61%

Keine

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale KanäleM2Alpha4 Bereiche](</de/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

AbdeckungExperimentell0%

QualitätAlpha55%

VollständigkeitAlpha58%

Keine

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 Bereiche](</de/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

AbdeckungExperimentell0%

QualitätAlpha53%

VollständigkeitAlpha54%

Keine

[OpenClaw App SDKM2Alpha6 Bereiche](</de/maturity/taxonomy#openclaw-app-sdk>)

AbdeckungExperimentell3%

QualitätAlpha54%

VollständigkeitAlpha53%

Keine

[iOS-AppM1Experimentell8 Bereiche](</de/maturity/taxonomy#ios-app>)

AbdeckungExperimentell0%

QualitätExperimentell41%

VollständigkeitExperimentell44%

Keine

[Nix-InstallationspfadM1Experimentell5 Bereiche](</de/maturity/taxonomy#nix-install-path>)

AbdeckungExperimentell0%

QualitätExperimentell41%

VollständigkeitExperimentell44%

Keine

[Voice-Call-KanalM1Experimentell5 Bereiche](</de/maturity/taxonomy#voice-call-channel>)

AbdeckungExperimentell0%

QualitätExperimentell41%

VollständigkeitExperimentell44%

Keine

[watchOS-BegleitoberflächenM1Experimentell5 Bereiche](</de/maturity/taxonomy#watchos-companion-surfaces>)

AbdeckungExperimentell0%

QualitätExperimentell41%

VollständigkeitExperimentell44%

Keine

[Linux-Begleit-AppM0Geplant5 Bereiche](</de/maturity/taxonomy#linux-companion-app>)

AbdeckungExperimentell0%

QualitätExperimentell19%

VollständigkeitExperimentell21%

Keine

[Native Windows-Begleit-AppM0Geplant5 Bereiche](</de/maturity/taxonomy#native-windows-companion-app>)

AbdeckungExperimentell0%

QualitätExperimentell19%

VollständigkeitExperimentell21%

Keine

### Kern

[CLIM4Stabil7 Bereiche](</de/maturity/taxonomy#cli>)

AbdeckungExperimentell4%

QualitätStabil83%

VollständigkeitStabil90%

Teilweise - 6

[Gateway-LaufzeitM4Stabil13 Bereiche](</de/maturity/taxonomy#gateway-runtime>)

AbdeckungExperimentell6%

QualitätStabil81%

VollständigkeitStabil89%

Teilweise - 12

[Agent-LaufzeitM3Beta9 Bereiche](</de/maturity/taxonomy#agent-runtime>)

AbdeckungExperimentell33%

QualitätBeta78%

VollständigkeitBeta79%

Teilweise - 6

[Sitzungs-, Speicher- und Kontext-EngineM3Beta9 Bereiche](</de/maturity/taxonomy#session-memory-and-context-engine>)

AbdeckungExperimentell30%

QualitätBeta77%

VollständigkeitBeta79%

Teilweise - 6

[Channel-FrameworkM3Beta8 Bereiche](</de/maturity/taxonomy#channel-framework>)

AbdeckungExperimentell13%

QualitätBeta76%

VollständigkeitBeta79%

Teilweise - 5

[BeobachtbarkeitM3Beta5 Bereiche](</de/maturity/taxonomy#observability>)

AbdeckungExperimentell18%

QualitätBeta75%

VollständigkeitBeta79%

Teilweise - 3

[Gateway-Web-AppM3Beta6 Bereiche](</de/maturity/taxonomy#gateway-web-app>)

AbdeckungExperimentell4%

QualitätBeta74%

VollständigkeitBeta79%

Keine

[PluginsM3Beta9 Bereiche](</de/maturity/taxonomy#plugins>)

AbdeckungExperimentell12%

QualitätBeta72%

VollständigkeitBeta79%

Teilweise - 7

[Sicherheit, Authentifizierung, Pairing und SecretsM3Beta6 Bereiche](</de/maturity/taxonomy#security-auth-pairing-and-secrets>)

AbdeckungExperimentell16%

QualitätBeta72%

VollständigkeitBeta79%

Teilweise - 5

[Automatisierung: Cron, Hooks, Aufgaben, PollingM3Beta6 Bereiche](</de/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

AbdeckungExperimentell2%

QualitätBeta72%

VollständigkeitBeta79%

Keine

[Medienverständnis und MediengenerierungM2Alpha6 Bereiche](</de/maturity/taxonomy#media-understanding-and-media-generation>)

AbdeckungExperimentell2%

QualitätAlpha64%

VollständigkeitAlpha68%

Keine

[Sprache und EchtzeitgesprächeM2Alpha6 Bereiche](</de/maturity/taxonomy#voice-and-realtime-talk>)

AbdeckungExperimentell0%

QualitätAlpha61%

VollständigkeitAlpha68%

Keine

[TUIM2Alpha5 Bereiche](</de/maturity/taxonomy#tui>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[ClawHubM2Alpha4 Bereiche](</de/maturity/taxonomy#clawhub>)

AbdeckungExperimentell0%

QualitätAlpha58%

VollständigkeitAlpha62%

Keine

[OpenClaw App SDKM2Alpha6 Bereiche](</de/maturity/taxonomy#openclaw-app-sdk>)

AbdeckungExperimentell3%

QualitätAlpha54%

VollständigkeitAlpha53%

Keine

### Plattform

[Linux-Gateway-HostM4Stabil5 Bereiche](</de/maturity/taxonomy#linux-gateway-host>)

AbdeckungExperimentell0%

QualitätBeta75%

VollständigkeitStabil89%

Teilweise - 4

[macOS-Gateway-HostM4Stabil7 Bereiche](</de/maturity/taxonomy#macos-gateway-host>)

AbdeckungExperimentell0%

QualitätBeta74%

VollständigkeitStabil88%

Keine

[Docker- und Podman-HostingM3Beta4 Bereiche](</de/maturity/taxonomy#docker-and-podman-hosting>)

AbdeckungExperimentell7%

QualitätBeta71%

VollständigkeitBeta79%

Keine

[Windows über WSL2M3Beta6 Bereiche](</de/maturity/taxonomy#windows-via-wsl2>)

AbdeckungExperimentell6%

QualitätAlpha69%

VollständigkeitBeta79%

Teilweise - 5

[Raspberry Pi und kleine Linux-GeräteM3Beta4 Bereiche](</de/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

AbdeckungExperimentell0%

QualitätAlpha67%

VollständigkeitBeta79%

Keine

[macOS-Begleit-AppM3Beta8 Bereiche](</de/maturity/taxonomy#macos-companion-app>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[Android-AppM2Alpha7 Bereiche](</de/maturity/taxonomy#android-app>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[Natives WindowsM2Alpha4 Bereiche](</de/maturity/taxonomy#native-windows>)

AbdeckungExperimentell0%

QualitätAlpha58%

VollständigkeitAlpha66%

Teilweise - 1

[Kubernetes-HostingM2Alpha4 Bereiche](</de/maturity/taxonomy#kubernetes-hosting>)

AbdeckungExperimentell0%

QualitätAlpha55%

VollständigkeitAlpha61%

Keine

[iOS-AppM1Experimentell8 Bereiche](</de/maturity/taxonomy#ios-app>)

AbdeckungExperimentell0%

QualitätExperimentell41%

VollständigkeitExperimentell44%

Keine

[Nix-InstallationspfadM1Experimentell5 Bereiche](</de/maturity/taxonomy#nix-install-path>)

AbdeckungExperimentell0%

QualitätExperimentell41%

VollständigkeitExperimentell44%

Keine

[watchOS-BegleitoberflächenM1Experimentell5 Bereiche](</de/maturity/taxonomy#watchos-companion-surfaces>)

AbdeckungExperimentell0%

QualitätExperimentell41%

VollständigkeitExperimentell44%

Keine

[Linux-Begleit-AppM0Geplant5 Bereiche](</de/maturity/taxonomy#linux-companion-app>)

AbdeckungExperimentell0%

QualitätExperimentell19%

VollständigkeitExperimentell21%

Keine

[Native Windows-Begleit-AppM0Geplant5 Bereiche](</de/maturity/taxonomy#native-windows-companion-app>)

AbdeckungExperimentell0%

QualitätExperimentell19%

VollständigkeitExperimentell21%

Keine

### Kanal

[DiscordM4Stabil6 Bereiche](</de/maturity/taxonomy#discord>)

AbdeckungExperimentell0%

QualitätBeta73%

VollständigkeitStabil87%

Teilweise - 4

[TelegramM3Beta5 Bereiche](</de/maturity/taxonomy#telegram>)

AbdeckungExperimentell0%

QualitätAlpha68%

VollständigkeitBeta78%

Vollständig - 5

[SlackM3Beta5 Bereiche](</de/maturity/taxonomy#slack>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Vollständig - 5

[iMessage und BlueBubblesM3Beta5 Bereiche](</de/maturity/taxonomy#imessage-and-bluebubbles>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[WhatsAppM3Beta5 Bereiche](</de/maturity/taxonomy#whatsapp>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[MatrixM2Alpha6 Bereiche](</de/maturity/taxonomy#matrix>)

AbdeckungExperimentell0%

QualitätAlpha60%

VollständigkeitAlpha67%

Keine

[Google ChatM2Alpha5 Bereiche](</de/maturity/taxonomy#google-chat>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[Microsoft TeamsM2Alpha5 Bereiche](</de/maturity/taxonomy#microsoft-teams>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[SignalM2Alpha5 Bereiche](</de/maturity/taxonomy#signal>)

AbdeckungExperimentell0%

QualitätAlpha59%

VollständigkeitAlpha66%

Keine

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale KanäleM2Alpha4 Bereiche](</de/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

AbdeckungExperimentell0%

QualitätAlpha55%

VollständigkeitAlpha58%

Keine

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 Bereiche](</de/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

AbdeckungExperimentell0%

QualitätAlpha53%

VollständigkeitAlpha54%

Keine

[Voice-Call-KanalM1Experimentell5 Bereiche](</de/maturity/taxonomy#voice-call-channel>)

AbdeckungExperimentell0%

QualitätExperimentell41%

VollständigkeitExperimentell44%

Keine

### Provider und Tool

[Browser-Automatisierung, exec- und Sandbox-ToolsM3Beta3 Bereiche](</de/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

AbdeckungExperimentell21%

QualitätBeta75%

VollständigkeitBeta79%

Teilweise - 2

[OpenAI- und Codex-Provider-PfadM3Beta5 Bereiche](</de/maturity/taxonomy#openai-and-codex-provider-path>)

AbdeckungExperimentell26%

QualitätBeta74%

VollständigkeitBeta79%

Teilweise - 3

[Websuche-ToolsM3Beta4 Bereiche](</de/maturity/taxonomy#web-search-tools>)

AbdeckungExperimentell9%

QualitätBeta74%

VollständigkeitBeta79%

Keine

[Anthropic-Provider-PfadM3Beta5 Bereiche](</de/maturity/taxonomy#anthropic-provider-path>)

AbdeckungExperimentell0%

QualitätBeta71%

VollständigkeitBeta78%

Keine

[Google-Provider-PfadM3Beta5 Bereiche](</de/maturity/taxonomy#google-provider-path>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[OpenRouter-Provider-PfadM3Beta4 Bereiche](</de/maturity/taxonomy#openrouter-provider-path>)

AbdeckungExperimentell0%

QualitätAlpha66%

VollständigkeitBeta78%

Keine

[Tools zur Bild-, Video- und MusikgenerierungM2Alpha5 Bereiche](</de/maturity/taxonomy#image-video-and-music-generation-tools>)

AbdeckungExperimentell0%

QualitätAlpha61%

VollständigkeitAlpha68%

Keine

[Lokale Modell-Provider: Ollama, vLLM, SGLang, LM StudioM2Alpha5 Bereiche](</de/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

AbdeckungExperimentell0%

QualitätAlpha61%

VollständigkeitAlpha68%

Keine

[Long-Tail-gehostete ProviderM2Alpha3 Bereiche](</de/maturity/taxonomy#long-tail-hosted-providers>)

AbdeckungExperimentell0%

QualitätAlpha61%

VollständigkeitAlpha68%

Keine

## Zusammenfassung der QA-Nachweise

Die folgenden Prüfungen zeigen, welche Scorecard-Bereiche durch Nachweise aus QA-Profilen ausgeübt wurden.

Vollständige Taxonomievalidierung 2026-06-23T07:24:36.128Z 96 Prüfungen - 94 bestanden, 2 blockiert 0 von 281 (0%) Bereichen - 20 von 1675 (1,2%) Funktionen - 77 von 1665 (4,6%) Abdeckungs-IDs

### Bereitschaft nach Bereich

Öffnen Sie eine Oberfläche, um den Nachweisstatus jeder Kategorie zu prüfen. Die Liste bleibt eingeklappt, damit die Seite auf einen Blick nützlich bleibt.

Agent-Laufzeit - 9 Bereiche

8 teilweise geprüft / 1 Prüfung erforderlich

Ausführung von Agentenrunden Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 3 (0%) / 7 von 24 (29,2%) 17 Fähigkeitslücken

Externe Laufzeiten und Subagenten Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 4 (0%) / 3 von 10 (30%) 7 Fähigkeitslücken

Ausführung über gehostete Provider Teilweise geprüft - Vollständige Taxonomievalidierung

1 von 5 (20%) / 1 von 5 (20%) 4 Fähigkeitslücken

Lokale und selbst gehostete Provider Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Modell- und Laufzeitauswahl Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 4 (0%) / 2 von 8 (25%) 6 Fähigkeitslücken

Provider-Authentifizierung Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 10 (0%) / 4 von 17 (23,5%) 13 Fähigkeitslücken

Streaming und Fortschritt Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 2 (0%) / 5 von 9 (55,6%) 4 Fähigkeitslücken

Tool-Aufrufe und Antwortverarbeitung Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 3 (0%) / 15 von 23 (65,2%) 8 Fähigkeitslücken

Steuerung der Tool-Ausführung Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 6 (0%) / 6 von 12 (50%) 6 Fähigkeitslücken

Android-App - 7 Bereiche

7 Prüfung erforderlich

Verbindungseinrichtung Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Gerätelaufzeit Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Fähigkeitslücken

Distribution Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Fähigkeitslücken

Medienerfassung Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Mobiler Chat Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Einstellungen Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Sprache Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Anthropic-Provider-Pfad - 5 Bereiche

5 Prüfung erforderlich

Medieneingaben Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Modell- und Laufzeitauswahl Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 12 (0%) 12 Fähigkeitslücken

Prompt-Cache und Kontext Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Provider-Authentifizierung und Wiederherstellung Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 9 (0%) / 0 von 9 (0%) 9 Fähigkeitslücken

Anfragetransport und Rundensemantik Prüfung erforderlich - Vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Fähigkeitslücken

Automatisierung: Cron, Hooks, Aufgaben, Polling - 6 Bereiche

5 erfordern Überprüfung / 1 teilweise überprüft

Automatisierungs-Hooks Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 11 (0%) / 0 von 11 (0%) 11 Funktionslücken

Hintergrundaufgaben und Abläufe Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Funktionslücken

Cron-Jobs Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 15 (0%) / 0 von 15 (0%) 15 Funktionslücken

Ereignis-Ingress Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 15 (0%) / 0 von 15 (0%) 15 Funktionslücken

Heartbeat Teilweise überprüft - vollständige Taxonomievalidierung

0 von 5 (0%) / 1 von 7 (14.3%) 6 Funktionslücken

Polling-Steuerungen Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Funktionslücken

Browser-Automatisierung, Exec und Sandbox-Tools - 3 Bereiche

2 teilweise überprüft / 1 erfordert Überprüfung

Browser-Automatisierung Teilweise überprüft - vollständige Taxonomievalidierung

1 von 8 (12.5%) / 1 von 8 (12.5%) 7 Funktionslücken

Sandbox- und Tool-Richtlinie Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Funktionslücken

Tool-Aufruf und -Ausführung Teilweise überprüft - vollständige Taxonomievalidierung

2 von 6 (33.3%) / 4 von 8 (50%) 4 Funktionslücken

Gateway-Web-App - 6 Bereiche

3 erfordern Überprüfung / 3 teilweise überprüft

Browser-Zugriff und Vertrauen Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Browser-Echtzeitkommunikation Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Browser-Benutzeroberfläche Teilweise überprüft - vollständige Taxonomievalidierung

0 von 10 (0%) / 1 von 12 (8.3%) 11 Funktionslücken

Konfiguration Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Operator-Konsole Teilweise überprüft - vollständige Taxonomievalidierung

0 von 10 (0%) / 1 von 12 (8.3%) 11 Funktionslücken

WebChat-Unterhaltungen Teilweise überprüft - vollständige Taxonomievalidierung

0 von 15 (0%) / 2 von 20 (10%) 18 Funktionslücken

Kanal-Framework - 8 Bereiche

4 erfordern Überprüfung / 4 teilweise überprüft

Kanalaktionen, Befehle und Genehmigungen Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Kanaleinrichtung Teilweise überprüft - vollständige Taxonomievalidierung

0 von 5 (0%) / 1 von 7 (14.3%) 6 Funktionslücken

Unterhaltungsrouting und Zustellung Teilweise überprüft - vollständige Taxonomievalidierung

0 von 10 (0%) / 5 von 27 (18.5%) 22 Funktionslücken

Gruppenthread- und Ambient-Raum-Verhalten Teilweise überprüft - vollständige Taxonomievalidierung

0 von 5 (0%) / 4 von 11 (36.4%) 7 Funktionslücken

Eingehende Zugriffs- und Identitäts-Gates Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Medienanhänge und umfangreiche Kanaldaten Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Funktionslücken

Ausgehende Zustellung und Antwort-Pipeline Teilweise überprüft - vollständige Taxonomievalidierung

0 von 4 (0%) / 8 von 21 (38.1%) 13 Funktionslücken

Status, Integrität und Operator-Steuerungen Überprüfung erforderlich - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 6 (0%) 6 Funktionslücken

ClawHub - 4 Bereiche

4 müssen geprüft werden

Katalogerkennung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Kompatibilität und Vertrauen Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 12 (0 %) / 0 von 12 (0 %) 12 Funktionslücken

Plugin-Lebenszyklus und Zustand Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 26 (0 %) / 0 von 26 (0 %) 26 Funktionslücken

Veröffentlichung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 7 (0 %) / 0 von 7 (0 %) 7 Funktionslücken

CLI - 7 Bereiche

5 müssen geprüft werden / 2 teilweise geprüft

CLI-Beobachtbarkeit Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

CLI-Einrichtung Teilweise geprüft - Vollständige Taxonomievalidierung

1 von 6 (16,7 %) / 1 von 6 (16,7 %) 5 Funktionslücken

Doctor Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 10 (0 %) / 0 von 10 (0 %) 10 Funktionslücken

Gateway-Dienstverwaltung Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 1 von 7 (14,3 %) 6 Funktionslücken

Onboarding und Auth-Einrichtung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Plugin- und Kanaleinrichtung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Updates und Upgrades Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Discord - 6 Bereiche

6 müssen geprüft werden

Zugriff und Identität Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 6 (0 %) / 0 von 6 (0 %) 6 Funktionslücken

Kanaleinrichtung und Betrieb Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 10 (0 %) / 0 von 10 (0 %) 10 Funktionslücken

Konversationsrouting und Zustellung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 12 (0 %) / 0 von 12 (0 %) 12 Funktionslücken

Medien und Rich Content Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Native Steuerelemente und Genehmigungen Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Echtzeit-Sprache und Anrufe Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Docker- und Podman-Hosting - 4 Bereiche

3 müssen geprüft werden / 1 teilweise geprüft

Agent-Sandbox und Tooling Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 3 (0 %) / 0 von 3 (0 %) 3 Funktionslücken

Containerbetrieb Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 11 (0 %) / 0 von 11 (0 %) 11 Funktionslücken

Containereinrichtung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 6 (0 %) / 0 von 6 (0 %) 6 Funktionslücken

Image-Veröffentlichung und Validierung Teilweise geprüft - Vollständige Taxonomievalidierung

1 von 5 (20 %) / 2 von 7 (28,6 %) 5 Funktionslücken

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale Kanäle - 4 Bereiche

4 müssen geprüft werden

Zugriff und Identität Muss geprüft werden - vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Kanaleinrichtung und Betrieb Muss geprüft werden - vollständige Taxonomievalidierung

0 von 6 (0 %) / 0 von 6 (0 %) 6 Funktionslücken

Konversationsrouting und Zustellung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Medien und Rich Content Muss geprüft werden - vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Gateway-Laufzeit - 13 Bereiche

9 müssen geprüft werden / 4 teilweise geprüft

Genehmigungen und Remote-Ausführung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 6 (0 %) / 0 von 6 (0 %) 6 Funktionslücken

Geräteauthentifizierung und Kopplung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 10 (0 %) / 0 von 10 (0 %) 10 Funktionslücken

Gateway-Lebenszyklus Teilweise geprüft - vollständige Taxonomievalidierung

0 von 7 (0 %) / 4 von 12 (33,3 %) 8 Funktionslücken

Gateway-RPC-APIs und Ereignisse Teilweise geprüft - vollständige Taxonomievalidierung

0 von 20 (0 %) / 2 von 22 (9,1 %) 20 Funktionslücken

Integrität, Diagnose und Reparatur Muss geprüft werden - vollständige Taxonomievalidierung

0 von 7 (0 %) / 0 von 7 (0 %) 7 Funktionslücken

Gehostete Weboberfläche Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0 %) / 0 von 4 (0 %) 4 Funktionslücken

HTTP-APIs Teilweise geprüft - vollständige Taxonomievalidierung

1 von 4 (25 %) / 1 von 4 (25 %) 3 Funktionslücken

Netzwerkzugriff und Erkennung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 6 (0 %) / 0 von 6 (0 %) 6 Funktionslücken

Nodes und Remote-Funktionen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 8 (0 %) / 0 von 8 (0 %) 8 Funktionslücken

Protokollkompatibilität Muss geprüft werden - vollständige Taxonomievalidierung

0 von 7 (0 %) / 0 von 7 (0 %) 7 Funktionslücken

Rollen und Berechtigungen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Sicherheitssteuerungen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 6 (0 %) / 0 von 6 (0 %) 6 Funktionslücken

WebSocket-Verbindung Teilweise geprüft - vollständige Taxonomievalidierung

1 von 8 (12,5 %) / 1 von 8 (12,5 %) 7 Funktionslücken

Google Chat - 5 Bereiche

5 müssen geprüft werden

Zugriff und Identität Muss geprüft werden - vollständige Taxonomievalidierung

0 von 11 (0 %) / 0 von 11 (0 %) 11 Funktionslücken

Kanaleinrichtung und Betrieb Muss geprüft werden - vollständige Taxonomievalidierung

0 von 16 (0 %) / 0 von 16 (0 %) 16 Funktionslücken

Konversationsrouting und Zustellung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Medien und Rich Content Muss geprüft werden - vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Native Steuerelemente und Genehmigungen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 16 (0 %) / 0 von 16 (0 %) 16 Funktionslücken

Google-Provider-Pfad - 5 Bereiche

5 müssen geprüft werden

Direkte Gemini-Runtime Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 9 (0%) / 0 von 9 (0%) 9 Fähigkeitslücken

Medien, Suche und Echtzeit Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Fähigkeitslücken

Modell-Routing und Endpunkte Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Fähigkeitslücken

Prompt-Caching Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Provider-Einrichtung und Zugangsdaten Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Fähigkeitslücken

Tools zur Bild-, Video- und Musikgenerierung - 5 Bereiche

5 müssen geprüft werden

Bildgenerierung Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 9 (0%) / 0 von 9 (0%) 9 Fähigkeitslücken

Medien-Routing und Erkennung Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Musikgenerierung Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Fähigkeitslücken

Aufgabenlebenszyklus und Zustellung Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 12 (0%) / 0 von 12 (0%) 12 Fähigkeitslücken

Videogenerierung Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 11 (0%) / 0 von 11 (0%) 11 Fähigkeitslücken

iMessage und BlueBubbles - 5 Bereiche

5 müssen geprüft werden

Zugriff und Identität Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Fähigkeitslücken

Kanaleinrichtung und Betrieb Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 11 (0%) / 0 von 11 (0%) 11 Fähigkeitslücken

Konversations-Routing und Zustellung Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Medien und Rich Content Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Fähigkeitslücken

Native Steuerelemente und Genehmigungen Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Fähigkeitslücken

iOS-App - 8 Bereiche

8 müssen geprüft werden

Canvas und Bildschirm Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Chat und Sitzungen Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Gerätebefehle Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Fähigkeitslücken

Distribution Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Gateway-Einrichtung und Diagnose Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Fähigkeitslücken

Medien und Teilen Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Benachrichtigungen und Hintergrund Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Sprache Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Kubernetes-Hosting - 4 Bereiche

4 müssen geprüft werden

Zugriff und Exposition Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Cluster-Lebenszyklus Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Konfiguration und Secrets Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Deployment-Einrichtung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Linux-Begleit-App - 5 Bereiche

5 müssen geprüft werden

App-Verteilung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Funktionslücken

Chat und Sitzungen Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Funktionslücken

Desktop-Funktionen Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 9 (0%) / 0 von 9 (0%) 9 Funktionslücken

Gateway-Konnektivität Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Funktionslücken

Status und Diagnose Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Funktionslücken

Linux-Gateway-Host - 5 Bereiche

5 müssen geprüft werden

Deployment-Ziele Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Funktionslücken

Diagnose und Reparatur Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Funktionslücken

Gateway-Laufzeit und Dienststeuerung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Funktionslücken

Host-Einrichtung und Updates Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Funktionslücken

Remote-Zugriff und Sicherheit Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Funktionslücken

Lokale Modell-Provider: Ollama, vLLM, SGLang, LM Studio - 5 Bereiche

5 müssen geprüft werden

Lokaler Speicher und Embeddings Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Native Provider-Plugins Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Funktionslücken

Netzwerksicherheit und Prompt-Steuerungen Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Funktionslücken

OpenAI-kompatible Laufzeitkompatibilität Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 8 (0%) / 0 von 8 (0%) 8 Funktionslücken

Provider-Einrichtung, Lebenszyklus und Diagnose Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 12 (0%) / 0 von 12 (0%) 12 Funktionslücken

Long-Tail-gehostete Provider - 3 Bereiche

3 müssen geprüft werden

Gehostete LLM-Provider Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 12 (0%) / 0 von 12 (0%) 12 Funktionslücken

Gehostete Medien-Provider Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 8 (0%) / 0 von 8 (0%) 8 Funktionslücken

Provider-Betrieb Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 12 (0%) / 0 von 12 (0%) 12 Funktionslücken

macOS-Companion-App - 8 Bereiche

8 müssen geprüft werden

Canvas Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Funktionslücken

Lokale Einrichtung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Funktionslücken

Native Funktionen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Remote-Verbindungen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Funktionslücken

Remote-WebChat Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Status und Einstellungen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Sprache und Sprechen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Funktionslücken

WebChat Muss geprüft werden - vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Funktionslücken

macOS-Gateway-Host - 7 Bereiche

7 müssen geprüft werden

CLI-Einrichtung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Funktionslücken

Diagnose und Beobachtbarkeit Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Funktionslücken

Gateway-Service-Lebenszyklus Muss geprüft werden - vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Funktionslücken

Lokale Gateway-Integration Muss geprüft werden - vollständige Taxonomievalidierung

0 von 9 (0%) / 0 von 9 (0%) 9 Funktionslücken

Berechtigungen und native Funktionen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Funktionslücken

Profile und Isolation Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Remote-Gateway-Modus Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Matrix - 6 Bereiche

6 müssen geprüft werden

Zugriff und Identität Muss geprüft werden - vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Funktionslücken

Kanaleinrichtung und Betrieb Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Konversationsrouting und Zustellung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Funktionslücke

Verschlüsselung und Verifizierung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Funktionslücken

Medien und Rich Content Muss geprüft werden - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Funktionslücke

Native Steuerelemente und Genehmigungen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Funktionslücken

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - 4 Bereiche

4 müssen geprüft werden

Zugriff und Identität Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Kanaleinrichtung und -betrieb Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Konversationsrouting und Zustellung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Medien und Rich Content Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Medienverständnis und Mediengenerierung - 6 Bereiche

4 müssen geprüft werden / 2 teilweise geprüft

Kanal-Medienverarbeitung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Medienkonfiguration Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 1 (0 %) / 0 von 1 (0 %) 1 Funktionslücke

Mediengenerierung Teilweise geprüft - Vollständige Taxonomievalidierung

1 von 17 (5,9 %) / 1 von 19 (5,3 %) 18 Funktionslücken

Medienaufnahme und Zugriff Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 8 (0 %) / 0 von 8 (0 %) 8 Funktionslücken

Medienverständnis Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 12 (0 %) / 1 von 14 (7,1 %) 13 Funktionslücken

Text-to-Speech-Zustellung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 2 (0 %) / 0 von 2 (0 %) 2 Funktionslücken

Microsoft Teams - 5 Bereiche

5 müssen geprüft werden

Zugriff und Identität Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 9 (0 %) / 0 von 9 (0 %) 9 Funktionslücken

Kanaleinrichtung und -betrieb Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 9 (0 %) / 0 von 9 (0 %) 9 Funktionslücken

Konversationsrouting und Zustellung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Medien und Rich Content Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Native Steuerelemente und Genehmigungen Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Natives Windows - 4 Bereiche

4 müssen geprüft werden

CLI Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 9 (0 %) / 0 von 9 (0 %) 9 Funktionslücken

Gateway-Verwaltung Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 11 (0 %) / 0 von 11 (0 %) 11 Funktionslücken

Netzwerk Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 4 (0 %) / 0 von 4 (0 %) 4 Funktionslücken

Updates Muss geprüft werden - Vollständige Taxonomievalidierung

0 von 4 (0 %) / 0 von 4 (0 %) 4 Funktionslücken

Native Windows-Begleit-App - 5 Bereiche

5 benötigen Überprüfung

Chat-Sitzungen Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Fähigkeitslücken

Desktop-Tools und Berechtigungen Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Fähigkeitslücken

Gateway-Verbindung Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Fähigkeitslücken

Installation und Updates Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Status und Reparatur Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Nix-Installationspfad - 5 Bereiche

5 benötigen Überprüfung

Aktivierung und App-UX Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Fähigkeitslücken

Konfiguration und Zustand Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Fähigkeitslücken

Installationsübergabe Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Plugin-Lebenszyklus Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Service-Runtime und Schutzmechanismen Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 8 (0%) / 0 von 8 (0%) 8 Fähigkeitslücken

OpenAI- und Codex-Provider-Pfad - 5 Bereiche

2 benötigen Überprüfung / 3 teilweise überprüft

Bild- und multimodale Eingabe Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Fähigkeitslücken

Modell und Authentifizierung Teilweise überprüft - vollständige Taxonomievalidierung

1 von 6 (16.7%) / 4 von 9 (44.4%) 5 Fähigkeitslücken

Native Codex-Harness Teilweise überprüft - vollständige Taxonomievalidierung

0 von 2 (0%) / 4 von 9 (44.4%) 5 Fähigkeitslücken

Responses und Tool-Kompatibilität Teilweise überprüft - vollständige Taxonomievalidierung

1 von 4 (25%) / 2 von 5 (40%) 3 Fähigkeitslücken

Sprache und Echtzeit-Audio Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Fähigkeitslücken

OpenClaw App SDK - 6 Bereiche

5 benötigen Überprüfung / 1 teilweise überprüft

Agent-Konversationen Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Fähigkeitslücken

Client-API Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Kompatibilität Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Ereignisse und Genehmigungen Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Gateway-Zugriff Benötigt Überprüfung - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Ressourcen-Helfer Teilweise überprüft - vollständige Taxonomievalidierung

0 von 5 (0%) / 1 von 6 (16.7%) 5 Fähigkeitslücken

OpenRouter-Provider-Pfad - 4 Bereiche

4 müssen geprüft werden

Chat-Runtime und Normalisierung Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 15 (0%) / 0 von 15 (0%) 15 Funktionslücken

Mediengenerierung und Sprache Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Funktionslücken

Provider-Wiederherstellung und Diagnose Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Provider-Einrichtung und Authentifizierung Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 14 (0%) / 0 von 14 (0%) 14 Funktionslücken

Plugins - 9 Bereiche

6 müssen geprüft werden / 3 teilweise geprüft

Erstellen und Paketieren von Plugins Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 8 (0%) / 0 von 8 (0%) 8 Funktionslücken

Gebündelte Plugins Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Canvas-Plugin Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Funktionslücken

Channel-Plugins Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Installieren und Ausführen von Plugins Teilweise geprüft - vollständige Taxonomievalidierung

0 von 6 (0%) / 7 von 20 (35%) 13 Funktionslücken

Plugin-Genehmigungen Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Funktionslücken

Provider- und Tool-Plugins Teilweise geprüft - vollständige Taxonomievalidierung

1 von 6 (16.7%) / 9 von 21 (42.9%) 12 Funktionslücken

Veröffentlichen von Plugins Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Funktionslücken

Testen von Plugins Teilweise geprüft - vollständige Taxonomievalidierung

0 von 6 (0%) / 3 von 11 (27.3%) 8 Funktionslücken

Raspberry Pi und kleine Linux-Geräte - 4 Bereiche

4 müssen geprüft werden

Gateway-Runtime Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Funktionslücken

Performance und Diagnose Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Remotezugriff und Authentifizierung Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 9 (0%) / 0 von 9 (0%) 9 Funktionslücken

Einrichtung und Kompatibilität Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 12 (0%) / 0 von 12 (0%) 12 Funktionslücken

Sicherheit, Authentifizierung, Pairing und Secrets - 6 Bereiche

2 teilweise geprüft / 4 müssen geprüft werden

Genehmigungsrichtlinie und Tool-Schutzmaßnahmen Teilweise geprüft - vollständige Taxonomievalidierung

0 von 2 (0%) / 3 von 6 (50%) 3 Funktionslücken

Channel-Zugriffskontrolle Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Funktionslücken

Hygiene für Anmeldedaten und Secrets Teilweise geprüft - vollständige Taxonomievalidierung

0 von 5 (0%) / 5 von 11 (45.5%) 6 Funktionslücken

Geräte- und Node-Pairing Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 11 (0%) / 0 von 11 (0%) 11 Funktionslücken

Gateway-Authentifizierung und Remotezugriff Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 9 (0%) / 0 von 9 (0%) 9 Funktionslücken

Plugin-Vertrauen Prüfung erforderlich - vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Funktionslücken

Sitzung, Memory und Kontext-Engine - 9 Bereiche

2 benötigen Prüfung / 7 teilweise geprüft

CLI-Sitzungs- und Transkriptverwaltung Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Funktionslücken

Kontext-Engine Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 2 (0%) / 4 von 7 (57.1%) 3 Funktionslücken

Core-Prompts und Kontext Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 2 (0%) / 3 von 8 (37.5%) 5 Funktionslücken

Client-übergreifender Verlauf und Sitzungsparität Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 2 (0%) / 2 von 5 (40%) 3 Funktionslücken

Diagnose, Wartung und Wiederherstellung Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 3 (0%) / 4 von 10 (40%) 6 Funktionslücken

Memory Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 5 (0%) / 6 von 13 (46.2%) 7 Funktionslücken

Sitzungsrouting Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 2 (0%) / 1 von 4 (25%) 3 Funktionslücken

Tokenverwaltung Teilweise geprüft - Vollständige Taxonomievalidierung

0 von 3 (0%) / 2 von 10 (20%) 8 Funktionslücken

Transkriptpersistenz Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Funktionslücken

Signal - 5 Bereiche

5 benötigen Prüfung

Zugriff und Identität Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 6 (0%) / 0 von 6 (0%) 6 Funktionslücken

Kanaleinrichtung und Betrieb Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Funktionslücken

Konversationsrouting und Zustellung Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Funktionslücke

Medien und Rich Content Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Funktionslücken

Native Steuerelemente und Genehmigungen Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Funktionslücken

Slack - 5 Bereiche

5 benötigen Prüfung

Zugriff und Identität Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Funktionslücke

Kanaleinrichtung und Betrieb Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Funktionslücken

Konversationsrouting und Zustellung Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Funktionslücken

Medien und Rich Content Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Funktionslücke

Native Steuerelemente und Genehmigungen Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 8 (0%) / 0 von 8 (0%) 8 Funktionslücken

Telegram - 5 Bereiche

5 benötigen Prüfung

Zugriff und Identität Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Funktionslücken

Kanaleinrichtung und Betrieb Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 10 (0%) / 0 von 10 (0%) 10 Funktionslücken

Konversationsrouting und Zustellung Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Funktionslücke

Medien und Rich Content Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Funktionslücke

Native Steuerelemente und Genehmigungen Benötigt Prüfung - Vollständige Taxonomievalidierung

0 von 9 (0%) / 0 von 9 (0%) 9 Funktionslücken

Beobachtbarkeit - 5 Bereiche

3 teilweise geprüft / 2 müssen geprüft werden

Diagnosedatensammlung Teilweise geprüft - vollständige Taxonomievalidierung

1 von 8 (12.5%) / 3 von 10 (30%) 7 Fähigkeitslücken

Zustand und Reparatur Teilweise geprüft - vollständige Taxonomievalidierung

1 von 12 (8.3%) / 5 von 18 (27.8%) 13 Fähigkeitslücken

Protokollierung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Sitzungsdiagnose Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Telemetrieexport Teilweise geprüft - vollständige Taxonomievalidierung

1 von 13 (7.7%) / 7 von 21 (33.3%) 14 Fähigkeitslücken

TUI - 5 Bereiche

5 müssen geprüft werden

Eingabe und Befehle Muss geprüft werden - vollständige Taxonomievalidierung

0 von 8 (0%) / 0 von 8 (0%) 8 Fähigkeitslücken

Lokale Shell-Ausführung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Rendering und Ausgabesicherheit Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Laufzeitmodi Muss geprüft werden - vollständige Taxonomievalidierung

0 von 14 (0%) / 0 von 14 (0%) 14 Fähigkeitslücken

Sitzungsverwaltung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 3 (0%) / 0 von 3 (0%) 3 Fähigkeitslücken

Sprache und Echtzeitgespräche - 6 Bereiche

6 müssen geprüft werden

Gespräche in nativen Apps Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Echtzeit-Gesprächssitzungen Muss geprüft werden - vollständige Taxonomievalidierung

0 von 11 (0%) / 0 von 11 (0%) 11 Fähigkeitslücken

Sprache und Transkription Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Gesprächsbeobachtbarkeit Muss geprüft werden - vollständige Taxonomievalidierung

0 von 5 (0%) / 0 von 5 (0%) 5 Fähigkeitslücken

Gesprächs-Provider Muss geprüft werden - vollständige Taxonomievalidierung

0 von 7 (0%) / 0 von 7 (0%) 7 Fähigkeitslücken

Sprachaktivierung und Routing Muss geprüft werden - vollständige Taxonomievalidierung

0 von 4 (0%) / 0 von 4 (0%) 4 Fähigkeitslücken

Sprachanrufkanal - 5 Bereiche

5 müssen geprüft werden

Zugriff und Identität Muss geprüft werden - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Kanaleinrichtung und Betrieb Muss geprüft werden - vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Fähigkeitslücken

Gesprächsrouting und Zustellung Muss geprüft werden - vollständige Taxonomievalidierung

0 von 1 (0%) / 0 von 1 (0%) 1 Fähigkeitslücke

Medien und Rich Content Muss geprüft werden - vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Fähigkeitslücken

Echtzeit-Sprache und Anrufe Muss geprüft werden - vollständige Taxonomievalidierung

0 von 2 (0%) / 0 von 2 (0%) 2 Fähigkeitslücken

watchOS-Begleitoberflächen - 5 Bereiche

5 müssen überprüft werden

Zustellung und Wiederherstellung Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 7 (0 %) / 0 von 7 (0 %) 7 Funktionslücken

Distribution und Support Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 6 (0 %) / 0 von 6 (0 %) 6 Funktionslücken

Ausführungsgenehmigungen Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 3 (0 %) / 0 von 3 (0 %) 3 Funktionslücken

Benachrichtigungen und Antworten Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 7 (0 %) / 0 von 7 (0 %) 7 Funktionslücken

Watch-App-UI Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 3 (0 %) / 0 von 3 (0 %) 3 Funktionslücken

Websuche-Tools - 4 Bereiche

2 müssen überprüft werden / 2 teilweise überprüft

Netzwerksicherheit Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 4 (0 %) / 0 von 4 (0 %) 4 Funktionslücken

Such-Provider Teilweise überprüft - Vollständige Taxonomievalidierung

2 von 19 (10,5 %) / 2 von 19 (10,5 %) 17 Funktionslücken

Einrichtung und Diagnose Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 9 (0 %) / 0 von 9 (0 %) 9 Funktionslücken

Tool-Verfügbarkeit und Abruf Teilweise überprüft - Vollständige Taxonomievalidierung

2 von 11 (18,2 %) / 3 von 12 (25 %) 9 Funktionslücken

WhatsApp - 5 Bereiche

5 müssen überprüft werden

Zugriff und Identität Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 7 (0 %) / 0 von 7 (0 %) 7 Funktionslücken

Kanaleinrichtung und Betrieb Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 5 (0 %) / 0 von 5 (0 %) 5 Funktionslücken

Konversationsrouting und Zustellung Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 4 (0 %) / 0 von 4 (0 %) 4 Funktionslücken

Medien und Rich Content Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 2 (0 %) / 0 von 2 (0 %) 2 Funktionslücken

Native Steuerelemente und Genehmigungen Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 2 (0 %) / 0 von 2 (0 %) 2 Funktionslücken

Windows über WSL2 - 6 Bereiche

5 müssen überprüft werden / 1 teilweise überprüft

Browser und Control-UI Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 6 (0 %) / 0 von 6 (0 %) 6 Funktionslücken

CLI Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 8 (0 %) / 0 von 8 (0 %) 8 Funktionslücken

Diagnose und Reparatur Teilweise überprüft - Vollständige Taxonomievalidierung

1 von 6 (16,7 %) / 3 von 8 (37,5 %) 5 Funktionslücken

Gateway-Zugriff und Exposition Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 11 (0 %) / 0 von 11 (0 %) 11 Funktionslücken

Gateway-Dienstlebenszyklus Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 10 (0 %) / 0 von 10 (0 %) 10 Funktionslücken

WSL-Einrichtung Muss überprüft werden - Vollständige Taxonomievalidierung

0 von 6 (0 %) / 0 von 6 (0 %) 6 Funktionslücken

> Zuletzt aktualisiert: 2026-06-22

Was this useful?YesNo

Open issue