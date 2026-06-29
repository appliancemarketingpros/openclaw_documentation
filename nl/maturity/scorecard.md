---
title: Volwassenheidsscorekaart
source_url: https://docs.openclaw.ai/nl/maturity/scorecard
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Maturiteitsscorekaart

releasegereedheid - gegenereerd uit taxonomie + QA-bewijs

Een praktisch overzicht van wat gereed is, wat bewezen is en wat nog werk vereist.

50 oppervlakken - 281 functiegebieden - deterministische dekking plus door mensen beoordeelde kwaliteit en volledigheid.

Door oppervlakken bladeren / QA-bewijs inspecteren / [De taxonomie lezen](</nl/maturity/taxonomy>)

## Waarvoor deze pagina bedoeld is

Gebruik deze pagina om één vraag te beantwoorden: welke OpenClaw-oppervlakken zijn geloofwaardige keuzes voor een release, en welk bewijs ondersteunt dat oordeel? Dekking komt uit deterministisch QA-bewijs; kwaliteit en volledigheid worden onderhouden als beoordeelde maturiteitsscores.

## In één oogopslag

67% Maturiteitsscore

Alpha Kwaliteit + volledigheid Dekking Experimenteel - 4% Kwaliteit Alpha - 63% Volledigheid Beta - 70%

Dekking wordt bewust door bewijs gestuurd: een gebied wordt niet "gereed" alleen omdat de implementatie bestaat. Het is geen invoer voor de maturiteitsscore, maar OpenClaw streeft ernaar de end-to-end-dekking na verloop van tijd boven 90% te houden voor mature Stabiel-of-betere functies.

## Scorebanden

Experimenteel0-50%

Alpha50-70%

Beta70-80%

Stabiel80-95%

Clawesome95-100%

## Oppervlakteverkenner

Oppervlakken zijn geordend op maturiteitsniveau, volledigheid en kwaliteit. LTS-ondersteuning wordt naast elke rij weergegeven, zodat releaseklare opties eenvoudig te vergelijken zijn.

### All surfaces

[CLIM4Stabiel7 gebieden](</nl/maturity/taxonomy#cli>)

DekkingExperimenteel4%

KwaliteitStabiel83%

VolledigheidStabiel90%

Gedeeltelijk - 6

[Gateway-runtimeM4Stabiel13 gebieden](</nl/maturity/taxonomy#gateway-runtime>)

DekkingExperimenteel6%

KwaliteitStabiel81%

VolledigheidStabiel89%

Gedeeltelijk - 12

[Linux Gateway-hostM4Stabiel5 gebieden](</nl/maturity/taxonomy#linux-gateway-host>)

DekkingExperimenteel0%

KwaliteitBeta75%

VolledigheidStabiel89%

Gedeeltelijk - 4

[macOS Gateway-hostM4Stabiel7 gebieden](</nl/maturity/taxonomy#macos-gateway-host>)

DekkingExperimenteel0%

KwaliteitBeta74%

VolledigheidStabiel88%

Geen

[DiscordM4Stabiel6 gebieden](</nl/maturity/taxonomy#discord>)

DekkingExperimenteel0%

KwaliteitBeta73%

VolledigheidStabiel87%

Gedeeltelijk - 4

[Agent-runtimeM3Beta9 gebieden](</nl/maturity/taxonomy#agent-runtime>)

DekkingExperimenteel33%

KwaliteitBeta78%

VolledigheidBeta79%

Gedeeltelijk - 6

[Sessie-, geheugen- en context-engineM3Beta9 gebieden](</nl/maturity/taxonomy#session-memory-and-context-engine>)

DekkingExperimenteel30%

KwaliteitBeta77%

VolledigheidBeta79%

Gedeeltelijk - 6

[KanaalframeworkM3Beta8 gebieden](</nl/maturity/taxonomy#channel-framework>)

DekkingExperimenteel13%

KwaliteitBeta76%

VolledigheidBeta79%

Gedeeltelijk - 5

[Browserautomatisering, exec- en sandboxtoolsM3Beta3 gebieden](</nl/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

DekkingExperimenteel21%

KwaliteitBeta75%

VolledigheidBeta79%

Gedeeltelijk - 2

[ObserveerbaarheidM3Beta5 gebieden](</nl/maturity/taxonomy#observability>)

DekkingExperimenteel18%

KwaliteitBeta75%

VolledigheidBeta79%

Gedeeltelijk - 3

[Providerpad voor OpenAI en CodexM3Beta5 gebieden](</nl/maturity/taxonomy#openai-and-codex-provider-path>)

DekkingExperimenteel26%

KwaliteitBeta74%

VolledigheidBeta79%

Gedeeltelijk - 3

[Gateway Web AppM3Beta6 gebieden](</nl/maturity/taxonomy#gateway-web-app>)

DekkingExperimenteel4%

KwaliteitBeta74%

VolledigheidBeta79%

Geen

[WebzoektoolsM3Beta4 gebieden](</nl/maturity/taxonomy#web-search-tools>)

DekkingExperimenteel9%

KwaliteitBeta74%

VolledigheidBeta79%

Geen

[PluginsM3Beta9 gebieden](</nl/maturity/taxonomy#plugins>)

DekkingExperimenteel12%

KwaliteitBeta72%

VolledigheidBeta79%

Gedeeltelijk - 7

[Beveiliging, authenticatie, koppeling en geheimenM3Beta6 gebieden](</nl/maturity/taxonomy#security-auth-pairing-and-secrets>)

DekkingExperimenteel16%

KwaliteitBeta72%

VolledigheidBeta79%

Gedeeltelijk - 5

[Automatisering: cron, hooks, taken, pollingM3Beta6 gebieden](</nl/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

DekkingExperimenteel2%

KwaliteitBeta72%

VolledigheidBeta79%

Geen

[Docker- en Podman-hostingM3Beta4 gebieden](</nl/maturity/taxonomy#docker-and-podman-hosting>)

DekkingExperimenteel7%

KwaliteitBeta71%

VolledigheidBeta79%

Geen

[Windows via WSL2M3Beta6 gebieden](</nl/maturity/taxonomy#windows-via-wsl2>)

DekkingExperimenteel6%

KwaliteitAlpha69%

VolledigheidBeta79%

Gedeeltelijk - 5

[Raspberry Pi en kleine Linux-apparatenM3Beta4 gebieden](</nl/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

DekkingExperimenteel0%

KwaliteitAlpha67%

VolledigheidBeta79%

Geen

[Anthropic-providerpadM3Beta5 gebieden](</nl/maturity/taxonomy#anthropic-provider-path>)

DekkingExperimenteel0%

KwaliteitBeta71%

VolledigheidBeta78%

Geen

[TelegramM3Beta5 gebieden](</nl/maturity/taxonomy#telegram>)

DekkingExperimenteel0%

KwaliteitAlpha68%

VolledigheidBeta78%

Volledig - 5

[SlackM3Beta5 gebieden](</nl/maturity/taxonomy#slack>)

DekkingExperimenteel0%

KwaliteitAlpha66%

VolledigheidBeta78%

Volledig - 5

[Google-providerpadM3Beta5 gebieden](</nl/maturity/taxonomy#google-provider-path>)

DekkingExperimenteel0%

KwaliteitAlpha66%

VolledigheidBeta78%

Geen

[iMessage en BlueBubblesM3Beta5 gebieden](</nl/maturity/taxonomy#imessage-and-bluebubbles>)

DekkingExperimenteel0%

KwaliteitAlpha66%

VolledigheidBeta78%

Geen

[macOS-begeleidende appM3Beta8 gebieden](</nl/maturity/taxonomy#macos-companion-app>)

DekkingExperimenteel0%

KwaliteitAlpha66%

VolledigheidBèta78%

Geen

[OpenRouter-providerpadM3Bèta4 gebieden](</nl/maturity/taxonomy#openrouter-provider-path>)

DekkingExperimenteel0%

KwaliteitAlfa66%

VolledigheidBèta78%

Geen

[WhatsAppM3Bèta5 gebieden](</nl/maturity/taxonomy#whatsapp>)

DekkingExperimenteel0%

KwaliteitAlfa66%

VolledigheidBèta78%

Geen

[Mediabegrip en mediageneratieM2Alfa6 gebieden](</nl/maturity/taxonomy#media-understanding-and-media-generation>)

DekkingExperimenteel2%

KwaliteitAlfa64%

VolledigheidAlfa68%

Geen

[Tools voor het genereren van afbeeldingen, video en muziekM2Alfa5 gebieden](</nl/maturity/taxonomy#image-video-and-music-generation-tools>)

DekkingExperimenteel0%

KwaliteitAlfa61%

VolledigheidAlfa68%

Geen

[Lokale modelproviders: Ollama, vLLM, SGLang, LM StudioM2Alfa5 gebieden](</nl/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

DekkingExperimenteel0%

KwaliteitAlfa61%

VolledigheidAlfa68%

Geen

[Gehoste long-tail-providersM2Alfa3 gebieden](</nl/maturity/taxonomy#long-tail-hosted-providers>)

DekkingExperimenteel0%

KwaliteitAlfa61%

VolledigheidAlfa68%

Geen

[Spraak en realtime gesprekM2Alfa6 gebieden](</nl/maturity/taxonomy#voice-and-realtime-talk>)

DekkingExperimenteel0%

KwaliteitAlfa61%

VolledigheidAlfa68%

Geen

[MatrixM2Alfa6 gebieden](</nl/maturity/taxonomy#matrix>)

DekkingExperimenteel0%

KwaliteitAlfa60%

VolledigheidAlfa67%

Geen

[Android-appM2Alfa7 gebieden](</nl/maturity/taxonomy#android-app>)

DekkingExperimenteel0%

KwaliteitAlfa59%

VolledigheidAlfa66%

Geen

[Google ChatM2Alfa5 gebieden](</nl/maturity/taxonomy#google-chat>)

DekkingExperimenteel0%

KwaliteitAlfa59%

VolledigheidAlfa66%

Geen

[Microsoft TeamsM2Alfa5 gebieden](</nl/maturity/taxonomy#microsoft-teams>)

DekkingExperimenteel0%

KwaliteitAlfa59%

VolledigheidAlfa66%

Geen

[SignalM2Alfa5 gebieden](</nl/maturity/taxonomy#signal>)

DekkingExperimenteel0%

KwaliteitAlfa59%

VolledigheidAlfa66%

Geen

[TUIM2Alfa5 gebieden](</nl/maturity/taxonomy#tui>)

DekkingExperimenteel0%

KwaliteitAlpha59%

VolledigheidAlpha66%

Geen

[Native WindowsM2Alpha4 gebieden](</nl/maturity/taxonomy#native-windows>)

DekkingExperimenteel0%

KwaliteitAlpha58%

VolledigheidAlpha66%

Gedeeltelijk - 1

[ClawHubM2Alpha4 gebieden](</nl/maturity/taxonomy#clawhub>)

DekkingExperimenteel0%

KwaliteitAlpha58%

VolledigheidAlpha62%

Geen

[Kubernetes-hostingM2Alpha4 gebieden](</nl/maturity/taxonomy#kubernetes-hosting>)

DekkingExperimenteel0%

KwaliteitAlpha55%

VolledigheidAlpha61%

Geen

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale kanalenM2Alpha4 gebieden](</nl/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

DekkingExperimenteel0%

KwaliteitAlpha55%

VolledigheidAlpha58%

Geen

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 gebieden](</nl/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

DekkingExperimenteel0%

KwaliteitAlpha53%

VolledigheidAlpha54%

Geen

[OpenClaw App SDKM2Alpha6 gebieden](</nl/maturity/taxonomy#openclaw-app-sdk>)

DekkingExperimenteel3%

KwaliteitAlfa54%

VolledigheidAlfa53%

Geen

[iOS-appM1Experimenteel8 gebieden](</nl/maturity/taxonomy#ios-app>)

DekkingExperimenteel0%

KwaliteitExperimenteel41%

VolledigheidExperimenteel44%

Geen

[Nix-installatiepadM1Experimenteel5 gebieden](</nl/maturity/taxonomy#nix-install-path>)

DekkingExperimenteel0%

KwaliteitExperimenteel41%

VolledigheidExperimenteel44%

Geen

[SpraakoproepkanaalM1Experimenteel5 gebieden](</nl/maturity/taxonomy#voice-call-channel>)

DekkingExperimenteel0%

KwaliteitExperimenteel41%

VolledigheidExperimenteel44%

Geen

[watchOS-begeleidende oppervlakkenM1Experimenteel5 gebieden](</nl/maturity/taxonomy#watchos-companion-surfaces>)

DekkingExperimenteel0%

KwaliteitExperimenteel41%

VolledigheidExperimenteel44%

Geen

[Linux-begeleidende appM0Gepland5 gebieden](</nl/maturity/taxonomy#linux-companion-app>)

DekkingExperimenteel0%

KwaliteitExperimenteel19%

VolledigheidExperimenteel21%

Geen

[Native Windows-begeleidende appM0Gepland5 gebieden](</nl/maturity/taxonomy#native-windows-companion-app>)

DekkingExperimenteel0%

KwaliteitExperimenteel19%

VolledigheidExperimenteel21%

Geen

### Kern

[CLIM4Stabiel7 gebieden](</nl/maturity/taxonomy#cli>)

DekkingExperimenteel4%

KwaliteitStabiel83%

VolledigheidStabiel90%

Gedeeltelijk - 6

[Gateway-runtimeM4Stabiel13 gebieden](</nl/maturity/taxonomy#gateway-runtime>)

DekkingExperimenteel6%

KwaliteitStabiel81%

VolledigheidStabiel89%

Gedeeltelijk - 12

[Agent-runtimeM3Bèta9 gebieden](</nl/maturity/taxonomy#agent-runtime>)

DekkingExperimenteel33%

KwaliteitBèta78%

VolledigheidBèta79%

Gedeeltelijk - 6

[Sessie-, geheugen- en contextengineM3Bèta9 gebieden](</nl/maturity/taxonomy#session-memory-and-context-engine>)

DekkingExperimenteel30%

KwaliteitBèta77%

VolledigheidBèta79%

Gedeeltelijk - 6

[KanaalframeworkM3Bèta8 gebieden](</nl/maturity/taxonomy#channel-framework>)

DekkingExperimenteel13%

KwaliteitBèta76%

VolledigheidBèta79%

Gedeeltelijk - 5

[ObserveerbaarheidM3Bèta5 gebieden](</nl/maturity/taxonomy#observability>)

DekkingExperimenteel18%

KwaliteitBèta75%

VolledigheidBèta79%

Gedeeltelijk - 3

[Gateway-webappM3Bèta6 gebieden](</nl/maturity/taxonomy#gateway-web-app>)

DekkingExperimenteel4%

KwaliteitBèta74%

VolledigheidBèta79%

Geen

[PluginsM3Bèta9 gebieden](</nl/maturity/taxonomy#plugins>)

DekkingExperimenteel12%

KwaliteitBèta72%

VolledigheidBèta79%

Gedeeltelijk - 7

[Beveiliging, authenticatie, koppeling en geheimenM3Bèta6 gebieden](</nl/maturity/taxonomy#security-auth-pairing-and-secrets>)

DekkingExperimenteel16%

KwaliteitBèta72%

VolledigheidBèta79%

Gedeeltelijk - 5

[Automatisering: Cron, hooks, taken, pollingM3Bèta6 gebieden](</nl/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

DekkingExperimenteel2%

KwaliteitBèta72%

VolledigheidBèta79%

Geen

[Mediabegrip en mediageneratieM2Alfa6 gebieden](</nl/maturity/taxonomy#media-understanding-and-media-generation>)

DekkingExperimenteel2%

KwaliteitAlfa64%

VolledigheidAlfa68%

Geen

[Spraak en realtimegesprekkenM2Alfa6 gebieden](</nl/maturity/taxonomy#voice-and-realtime-talk>)

DekkingExperimenteel0%

KwaliteitAlfa61%

VolledigheidAlfa68%

Geen

[TUIM2Alpha5 gebieden](</nl/maturity/taxonomy#tui>)

DekkingExperimenteel0%

KwaliteitAlpha59%

VolledigheidAlpha66%

Geen

[ClawHubM2Alpha4 gebieden](</nl/maturity/taxonomy#clawhub>)

DekkingExperimenteel0%

KwaliteitAlpha58%

VolledigheidAlpha62%

Geen

[OpenClaw App SDKM2Alpha6 gebieden](</nl/maturity/taxonomy#openclaw-app-sdk>)

DekkingExperimenteel3%

KwaliteitAlpha54%

VolledigheidAlpha53%

Geen

### Platform

[Linux Gateway-hostM4Stabiel5 gebieden](</nl/maturity/taxonomy#linux-gateway-host>)

DekkingExperimenteel0%

KwaliteitBeta75%

VolledigheidStabiel89%

Gedeeltelijk - 4

[macOS Gateway-hostM4Stabiel7 gebieden](</nl/maturity/taxonomy#macos-gateway-host>)

DekkingExperimenteel0%

KwaliteitBeta74%

VolledigheidStabiel88%

Geen

[Docker- en Podman-hostingM3Beta4 gebieden](</nl/maturity/taxonomy#docker-and-podman-hosting>)

DekkingExperimenteel7%

KwaliteitBeta71%

VolledigheidBeta79%

Geen

[Windows via WSL2M3Beta6 gebieden](</nl/maturity/taxonomy#windows-via-wsl2>)

DekkingExperimenteel6%

KwaliteitAlpha69%

VolledigheidBeta79%

Gedeeltelijk - 5

[Raspberry Pi en kleine Linux-apparatenM3Beta4 gebieden](</nl/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

DekkingExperimenteel0%

KwaliteitAlpha67%

VolledigheidBeta79%

Geen

[macOS-begeleidende appM3Beta8 gebieden](</nl/maturity/taxonomy#macos-companion-app>)

DekkingExperimenteel0%

KwaliteitAlpha66%

VolledigheidBeta78%

Geen

[Android-appM2Alpha7 gebieden](</nl/maturity/taxonomy#android-app>)

DekkingExperimenteel0%

KwaliteitAlpha59%

VolledigheidAlpha66%

Geen

[Native WindowsM2Alpha4 gebieden](</nl/maturity/taxonomy#native-windows>)

DekkingExperimenteel0%

KwaliteitAlpha58%

VolledigheidAlpha66%

Gedeeltelijk - 1

[Kubernetes-hostingM2Alpha4 gebieden](</nl/maturity/taxonomy#kubernetes-hosting>)

DekkingExperimenteel0%

KwaliteitAlpha55%

VolledigheidAlpha61%

Geen

[iOS-appM1Experimenteel8 gebieden](</nl/maturity/taxonomy#ios-app>)

DekkingExperimenteel0%

KwaliteitExperimenteel41%

VolledigheidExperimenteel44%

Geen

[Nix-installatiepadM1Experimenteel5 gebieden](</nl/maturity/taxonomy#nix-install-path>)

DekkingExperimenteel0%

KwaliteitExperimenteel41%

VolledigheidExperimenteel44%

Geen

[watchOS-begeleidende oppervlakkenM1Experimenteel5 gebieden](</nl/maturity/taxonomy#watchos-companion-surfaces>)

DekkingExperimenteel0%

KwaliteitExperimenteel41%

VolledigheidExperimenteel44%

Geen

[Linux-begeleidende appM0Gepland5 gebieden](</nl/maturity/taxonomy#linux-companion-app>)

DekkingExperimenteel0%

KwaliteitExperimenteel19%

VolledigheidExperimenteel21%

Geen

[Native Windows-begeleidende appM0Gepland5 gebieden](</nl/maturity/taxonomy#native-windows-companion-app>)

DekkingExperimenteel0%

KwaliteitExperimenteel19%

VolledigheidExperimenteel21%

Geen

### Kanaal

[DiscordM4Stabiel6 gebieden](</nl/maturity/taxonomy#discord>)

DekkingExperimenteel0%

KwaliteitBeta73%

VolledigheidStabiel87%

Gedeeltelijk - 4

[TelegramM3Beta5 gebieden](</nl/maturity/taxonomy#telegram>)

DekkingExperimenteel0%

KwaliteitAlpha68%

VolledigheidBeta78%

Volledig - 5

[SlackM3Beta5 gebieden](</nl/maturity/taxonomy#slack>)

DekkingExperimenteel0%

KwaliteitAlpha66%

VolledigheidBeta78%

Volledig - 5

[iMessage en BlueBubblesM3Beta5 gebieden](</nl/maturity/taxonomy#imessage-and-bluebubbles>)

DekkingExperimenteel0%

KwaliteitAlpha66%

VolledigheidBeta78%

Geen

[WhatsAppM3Beta5 gebieden](</nl/maturity/taxonomy#whatsapp>)

DekkingExperimenteel0%

KwaliteitAlpha66%

VolledigheidBeta78%

Geen

[MatrixM2Alpha6 gebieden](</nl/maturity/taxonomy#matrix>)

DekkingExperimenteel0%

KwaliteitAlpha60%

VolledigheidAlpha67%

Geen

[Google ChatM2Alpha5 gebieden](</nl/maturity/taxonomy#google-chat>)

DekkingExperimenteel0%

KwaliteitAlpha59%

VolledigheidAlpha66%

Geen

[Microsoft TeamsM2Alpha5 gebieden](</nl/maturity/taxonomy#microsoft-teams>)

DekkingExperimenteel0%

KwaliteitAlpha59%

VolledigheidAlfa66%

Geen

[SignalM2Alfa5 gebieden](</nl/maturity/taxonomy#signal>)

DekkingExperimenteel0%

KwaliteitAlfa59%

VolledigheidAlfa66%

Geen

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale kanalenM2Alfa4 gebieden](</nl/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

DekkingExperimenteel0%

KwaliteitAlfa55%

VolledigheidAlfa58%

Geen

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alfa4 gebieden](</nl/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

DekkingExperimenteel0%

KwaliteitAlfa53%

VolledigheidAlfa54%

Geen

[SpraakoproepkanaalM1Experimenteel5 gebieden](</nl/maturity/taxonomy#voice-call-channel>)

DekkingExperimenteel0%

KwaliteitExperimenteel41%

VolledigheidExperimenteel44%

Geen

### Provider en tool

[Browserautomatisering, exec en sandboxtoolsM3Bèta3 gebieden](</nl/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

DekkingExperimenteel21%

KwaliteitBèta75%

VolledigheidBèta79%

Gedeeltelijk - 2

[OpenAI- en Codex-providerpadM3Bèta5 gebieden](</nl/maturity/taxonomy#openai-and-codex-provider-path>)

DekkingExperimenteel26%

KwaliteitBèta74%

VolledigheidBèta79%

Gedeeltelijk - 3

[WebzoektoolsM3Bèta4 gebieden](</nl/maturity/taxonomy#web-search-tools>)

DekkingExperimenteel9%

KwaliteitBèta74%

VolledigheidBèta79%

Geen

[Anthropic-providerpadM3Bèta5 gebieden](</nl/maturity/taxonomy#anthropic-provider-path>)

DekkingExperimenteel0%

KwaliteitBèta71%

VolledigheidBèta78%

Geen

[Google-providerpadM3Bèta5 gebieden](</nl/maturity/taxonomy#google-provider-path>)

DekkingExperimenteel0%

KwaliteitAlfa66%

VolledigheidBèta78%

Geen

[OpenRouter-providerpadM3Bèta4 gebieden](</nl/maturity/taxonomy#openrouter-provider-path>)

DekkingExperimenteel0%

KwaliteitAlfa66%

VolledigheidBèta78%

Geen

[Tools voor beeld-, video- en muziekgeneratieM2Alfa5 gebieden](</nl/maturity/taxonomy#image-video-and-music-generation-tools>)

DekkingExperimenteel0%

KwaliteitAlfa61%

VolledigheidAlfa68%

Geen

[Lokale modelproviders: Ollama, vLLM, SGLang, LM StudioM2Alfa5 gebieden](</nl/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

DekkingExperimenteel0%

KwaliteitAlfa61%

VolledigheidAlfa68%

Geen

[Gehoste longtail-providersM2Alfa3 gebieden](</nl/maturity/taxonomy#long-tail-hosted-providers>)

DekkingExperimenteel0%

KwaliteitAlfa61%

VolledigheidAlfa68%

Geen

## Samenvatting van QA-bewijs

De onderstaande controles tonen welke scorecardgebieden zijn uitgevoerd met bewijs uit QA-profielen.

Volledige taxonomievalidatie 2026-06-23T07:24:36.128Z 96 controles - 94 geslaagd, 2 geblokkeerd 0 van 281 (0%) gebieden - 20 van 1675 (1.2%) functies - 77 van 1665 (4.6%) dekkings-ID's

### Gereedheid per gebied

Open een oppervlak om de bewijsstatus van elke categorie te bekijken. De lijst blijft samengevouwen zodat de pagina in één oogopslag bruikbaar blijft.

Agentruntime - 9 gebieden

8 gedeeltelijk beoordeeld / 1 moet worden beoordeeld

Uitvoering van agentbeurt Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 3 (0%) / 7 van 24 (29.2%) 17 lacunes in mogelijkheden

Externe runtimes en subagenten Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 3 van 10 (30%) 7 lacunes in mogelijkheden

Uitvoering bij gehoste providers Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 5 (20%) / 1 van 5 (20%) 4 lacunes in mogelijkheden

Lokale en zelfgehoste providers Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 lacunes in mogelijkheden

Model- en runtimeselectie Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 2 van 8 (25%) 6 lacunes in mogelijkheden

Provider-authenticatie Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 4 van 17 (23.5%) 13 lacunes in mogelijkheden

Streaming en voortgang Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 2 (0%) / 5 van 9 (55.6%) 4 lacunes in mogelijkheden

Toolaanroepen en responsafhandeling Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 3 (0%) / 15 van 23 (65.2%) 8 lacunes in mogelijkheden

Uitvoeringscontroles voor tools Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 6 van 12 (50%) 6 lacunes in mogelijkheden

Android-app - 7 gebieden

7 moeten worden beoordeeld

Verbindingsconfiguratie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 lacune in mogelijkheden

Apparaatruntime Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 lacunes in mogelijkheden

Distributie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 lacunes in mogelijkheden

Media vastleggen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 lacune in mogelijkheden

Mobiele chat Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 lacune in mogelijkheden

Instellingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 lacune in mogelijkheden

Spraak Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 lacune in mogelijkheden

Anthropic-providerpad - 5 gebieden

5 moeten worden beoordeeld

Media-invoer Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 lacunes in mogelijkheden

Model- en runtimeselectie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 12 (0%) 12 lacunes in mogelijkheden

Promptcache en context Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 lacunes in mogelijkheden

Provider-authenticatie en herstel Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 lacunes in mogelijkheden

Aanvraagtransport en beurtsemantiek Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 lacunes in mogelijkheden

Automatisering: Cron, hooks, taken, polling - 6 gebieden

5 hebben beoordeling nodig / 1 gedeeltelijk beoordeeld

Automatiseringshooks Beoordeling nodig - volledige taxonomievalidatie

0 van 11 (0%) / 0 van 11 (0%) 11 mogelijkheidslacunes

Achtergrondtaken en flows Beoordeling nodig - volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 mogelijkheidslacunes

Cron-taken Beoordeling nodig - volledige taxonomievalidatie

0 van 15 (0%) / 0 van 15 (0%) 15 mogelijkheidslacunes

Gebeurtenisinkomend verkeer Beoordeling nodig - volledige taxonomievalidatie

0 van 15 (0%) / 0 van 15 (0%) 15 mogelijkheidslacunes

Heartbeat Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 1 van 7 (14,3%) 6 mogelijkheidslacunes

Pollingbesturing Beoordeling nodig - volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 mogelijkheidslacunes

Browserautomatisering, exec en sandbox-tools - 3 gebieden

2 gedeeltelijk beoordeeld / 1 heeft beoordeling nodig

Browserautomatisering Gedeeltelijk beoordeeld - volledige taxonomievalidatie

1 van 8 (12,5%) / 1 van 8 (12,5%) 7 mogelijkheidslacunes

Sandbox- en toolbeleid Beoordeling nodig - volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 mogelijkheidslacunes

Toolaanroep en uitvoering Gedeeltelijk beoordeeld - volledige taxonomievalidatie

2 van 6 (33,3%) / 4 van 8 (50%) 4 mogelijkheidslacunes

Gateway-webapp - 6 gebieden

3 hebben beoordeling nodig / 3 gedeeltelijk beoordeeld

Browsertoegang en vertrouwen Beoordeling nodig - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 mogelijkheidslacunes

Realtime browsergesprek Beoordeling nodig - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 mogelijkheidslacunes

Browser-UI Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 10 (0%) / 1 van 12 (8,3%) 11 mogelijkheidslacunes

Configuratie Beoordeling nodig - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 mogelijkheidslacunes

Operatorconsole Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 10 (0%) / 1 van 12 (8,3%) 11 mogelijkheidslacunes

WebChat-gesprekken Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 15 (0%) / 2 van 20 (10%) 18 mogelijkheidslacunes

Kanaalframework - 8 gebieden

4 hebben beoordeling nodig / 4 gedeeltelijk beoordeeld

Kanaalacties, opdrachten en goedkeuringen Beoordeling nodig - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 mogelijkheidslacunes

Kanaalinstelling Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 1 van 7 (14,3%) 6 mogelijkheidslacunes

Gespreksroutering en levering Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 10 (0%) / 5 van 27 (18,5%) 22 mogelijkheidslacunes

Gedrag van groepsthreads en omgevingsruimten Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 4 van 11 (36,4%) 7 mogelijkheidslacunes

Inkomende toegang en identiteitspoorten Beoordeling nodig - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 mogelijkheidslacunes

Mediabijlagen en rijke kanaalgegevens Beoordeling nodig - volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 mogelijkheidslacunes

Uitgaande levering en antwoordpipeline Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 4 (0%) / 8 van 21 (38,1%) 13 mogelijkheidslacunes

Statusgezondheid en operatorbesturing Beoordeling nodig - volledige taxonomievalidatie

0 van 4 (0%) / 0 van 6 (0%) 6 mogelijkheidslacunes

ClawHub - 4 gebieden

4 moeten worden beoordeeld

Catalogusdetectie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 lacunes in mogelijkheden

Compatibiliteit en vertrouwen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 12 (0%) / 0 van 12 (0%) 12 lacunes in mogelijkheden

Plugin-levenscyclus en gezondheid Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 26 (0%) / 0 van 26 (0%) 26 lacunes in mogelijkheden

Publicatie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 lacunes in mogelijkheden

CLI - 7 gebieden

5 moeten worden beoordeeld / 2 gedeeltelijk beoordeeld

CLI-observeerbaarheid Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 lacunes in mogelijkheden

CLI-inrichting Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 6 (16.7%) / 1 van 6 (16.7%) 5 lacunes in mogelijkheden

Doctor Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 lacunes in mogelijkheden

Gateway-servicebeheer Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 1 van 7 (14.3%) 6 lacunes in mogelijkheden

Onboarding en auth-inrichting Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 lacunes in mogelijkheden

Plugin- en kanaalinrichting Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 lacunes in mogelijkheden

Updates en upgrades Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 lacunes in mogelijkheden

Discord - 6 gebieden

6 moeten worden beoordeeld

Toegang en identiteit Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 lacunes in mogelijkheden

Kanaalinrichting en -bewerkingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 lacunes in mogelijkheden

Gespreksroutering en aflevering Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 12 (0%) / 0 van 12 (0%) 12 lacunes in mogelijkheden

Media en rijke content Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 lacune in mogelijkheden

Native bedieningselementen en goedkeuringen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 lacunes in mogelijkheden

Realtime spraak en oproepen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 lacunes in mogelijkheden

Docker- en Podman-hosting - 4 gebieden

3 moeten worden beoordeeld / 1 gedeeltelijk beoordeeld

Agent-sandbox en tooling Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 lacunes in mogelijkheden

Containerbewerkingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 11 (0%) / 0 van 11 (0%) 11 lacunes in mogelijkheden

Containerinrichting Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 lacunes in mogelijkheden

Image-release en validatie Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 5 (20%) / 2 van 7 (28.6%) 5 lacunes in mogelijkheden

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale kanalen - 4 gebieden

4 moeten worden beoordeeld

Toegang en identiteit Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Kanaalconfiguratie en bewerkingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 functionaliteitslacunes

Gespreksroutering en aflevering Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Media en rijke content Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Gateway-runtime - 13 gebieden

9 moeten worden beoordeeld / 4 gedeeltelijk beoordeeld

Goedkeuringen en externe uitvoering Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 functionaliteitslacunes

Apparaatauthenticatie en koppeling Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 functionaliteitslacunes

Gateway-levenscyclus Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 4 van 12 (33.3%) 8 functionaliteitslacunes

Gateway-RPC-API's en gebeurtenissen Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 20 (0%) / 2 van 22 (9.1%) 20 functionaliteitslacunes

Status, diagnostiek en reparatie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 functionaliteitslacunes

Gehoste webinterface Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

HTTP-API's Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 4 (25%) / 1 van 4 (25%) 3 functionaliteitslacunes

Netwerktoegang en detectie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 functionaliteitslacunes

Nodes en externe mogelijkheden Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 8 (0%) / 0 van 8 (0%) 8 functionaliteitslacunes

Protocolcompatibiliteit Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 functionaliteitslacunes

Rollen en machtigingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Beveiligingscontroles Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 functionaliteitslacunes

WebSocket-verbinding Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 8 (12.5%) / 1 van 8 (12.5%) 7 functionaliteitslacunes

Google Chat - 5 gebieden

5 moeten worden beoordeeld

Toegang en identiteit Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 11 (0%) / 0 van 11 (0%) 11 functionaliteitslacunes

Kanaalconfiguratie en bewerkingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 16 (0%) / 0 van 16 (0%) 16 functionaliteitslacunes

Gespreksroutering en aflevering Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Media en rijke content Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Systeemeigen bedieningselementen en goedkeuringen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 16 (0%) / 0 van 16 (0%) 16 functionaliteitslacunes

Google-providerpad - 5 gebieden

5 moeten worden beoordeeld

Directe Gemini-runtime Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 functionaliteitslacunes

Media, zoeken en realtime Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 functionaliteitslacunes

Modelroutering en endpoints Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 functionaliteitslacunes

Promptcaching Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Providerinstallatie en aanmeldgegevens Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 functionaliteitslacunes

Tools voor beeld-, video- en muziekgeneratie - 5 gebieden

5 moeten worden beoordeeld

Beeldgeneratie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 functionaliteitslacunes

Mediaroutering en ontdekking Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

Muziekgeneratie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 functionaliteitslacunes

Taaklevenscyclus en levering Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 12 (0%) / 0 van 12 (0%) 12 functionaliteitslacunes

Videogeneratie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 11 (0%) / 0 van 11 (0%) 11 functionaliteitslacunes

iMessage en BlueBubbles - 5 gebieden

5 moeten worden beoordeeld

Toegang en identiteit Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 functionaliteitslacunes

Kanaalinstallatie en bewerkingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 11 (0%) / 0 van 11 (0%) 11 functionaliteitslacunes

Gespreksroutering en levering Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

Media en rijke content Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 functionaliteitslacunes

Native bedieningselementen en goedkeuringen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 functionaliteitslacunes

iOS-app - 8 gebieden

8 moeten worden beoordeeld

Canvas en scherm Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Chat en sessies Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Apparaatopdrachten Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 functionaliteitslacunes

Distributie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Gateway-installatie en diagnostiek Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 functionaliteitslacunes

Media en delen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Meldingen en achtergrond Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Spraak Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 functionaliteitslacune

Kubernetes-hosting - 4 gebieden

4 moeten worden beoordeeld

Toegang en blootstelling Beoordeling nodig - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Clusterlevenscyclus Beoordeling nodig - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Configuratie en geheimen Beoordeling nodig - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Implementatie-instelling Beoordeling nodig - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Linux-companion-app - 5 gebieden

5 moeten worden beoordeeld

App-distributie Beoordeling nodig - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 functionaliteitslacunes

Chat en sessies Beoordeling nodig - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 functionaliteitslacunes

Desktopmogelijkheden Beoordeling nodig - Volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 functionaliteitslacunes

Gateway-connectiviteit Beoordeling nodig - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

Status en diagnostiek Beoordeling nodig - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 functionaliteitslacunes

Linux Gateway-host - 5 gebieden

5 moeten worden beoordeeld

Implementatiedoelen Beoordeling nodig - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 functionaliteitslacunes

Diagnostiek en herstel Beoordeling nodig - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

Gateway-runtime en servicebeheer Beoordeling nodig - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 functionaliteitslacunes

Hostinstelling en updates Beoordeling nodig - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

Externe toegang en beveiliging Beoordeling nodig - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 functionaliteitslacunes

Lokale modelproviders: Ollama, vLLM, SGLang, LM Studio - 5 gebieden

5 moeten worden beoordeeld

Lokaal geheugen en embeddings Beoordeling nodig - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Native provider-Plugins Beoordeling nodig - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 functionaliteitslacunes

Netwerkveiligheid en promptbesturing Beoordeling nodig - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 functionaliteitslacunes

Compatibiliteit met OpenAI-compatibele runtime Beoordeling nodig - Volledige taxonomievalidatie

0 van 8 (0%) / 0 van 8 (0%) 8 functionaliteitslacunes

Providerinstelling, levenscyclus en diagnostiek Beoordeling nodig - Volledige taxonomievalidatie

0 van 12 (0%) / 0 van 12 (0%) 12 functionaliteitslacunes

Long-tail gehoste providers - 3 gebieden

3 moeten worden beoordeeld

Gehoste LLM-providers Beoordeling nodig - Volledige taxonomievalidatie

0 van 12 (0%) / 0 van 12 (0%) 12 functionaliteitslacunes

Gehoste mediaproviders Beoordeling nodig - Volledige taxonomievalidatie

0 van 8 (0%) / 0 van 8 (0%) 8 functionaliteitslacunes

Provideractiviteiten Beoordeling nodig - Volledige taxonomievalidatie

0 van 12 (0%) / 0 van 12 (0%) 12 functionaliteitslacunes

macOS-begeleidende app - 8 gebieden

8 moeten worden beoordeeld

Canvas Moet worden beoordeeld - volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Lokale configuratie Moet worden beoordeeld - volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 capaciteitslacunes

Systeemeigen mogelijkheden Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Externe verbindingen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 capaciteitslacunes

Externe WebChat Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Status en instellingen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Spraak en praten Moet worden beoordeeld - volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 capaciteitslacunes

WebChat Moet worden beoordeeld - volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 capaciteitslacunes

macOS Gateway-host - 7 gebieden

7 moeten worden beoordeeld

CLI-configuratie Moet worden beoordeeld - volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Diagnostiek en observeerbaarheid Moet worden beoordeeld - volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Gateway-servicelevenscyclus Moet worden beoordeeld - volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 capaciteitslacunes

Lokale Gateway-integratie Moet worden beoordeeld - volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 capaciteitslacunes

Machtigingen en systeemeigen mogelijkheden Moet worden beoordeeld - volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Profielen en isolatie Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Externe Gateway-modus Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Matrix - 6 gebieden

6 moeten worden beoordeeld

Toegang en identiteit Moet worden beoordeeld - volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 capaciteitslacunes

Kanaalconfiguratie en bewerkingen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Gespreksroutering en bezorging Moet worden beoordeeld - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitslacune

Versleuteling en verificatie Moet worden beoordeeld - volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 capaciteitslacunes

Media en uitgebreide inhoud Moet worden beoordeeld - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitslacune

Systeemeigen bedieningselementen en goedkeuringen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 capaciteitslacunes

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - 4 gebieden

4 moeten worden beoordeeld

Toegang en identiteit Beoordeling nodig - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitslacune

Kanaalconfiguratie en -beheer Beoordeling nodig - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitslacune

Gespreksroutering en aflevering Beoordeling nodig - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitslacune

Media en rijke inhoud Beoordeling nodig - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitslacune

Mediabegrip en mediageneratie - 6 gebieden

4 moeten worden beoordeeld / 2 gedeeltelijk beoordeeld

Kanaalmedia-afhandeling Beoordeling nodig - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Mediaconfiguratie Beoordeling nodig - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitslacune

Mediageneratie Gedeeltelijk beoordeeld - volledige taxonomievalidatie

1 van 17 (5.9%) / 1 van 19 (5.3%) 18 capaciteitslacunes

Media-inname en toegang Beoordeling nodig - volledige taxonomievalidatie

0 van 8 (0%) / 0 van 8 (0%) 8 capaciteitslacunes

Mediabegrip Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 12 (0%) / 1 van 14 (7.1%) 13 capaciteitslacunes

Tekst-naar-spraak-aflevering Beoordeling nodig - volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 capaciteitslacunes

Microsoft Teams - 5 gebieden

5 moeten worden beoordeeld

Toegang en identiteit Beoordeling nodig - volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 capaciteitslacunes

Kanaalconfiguratie en -beheer Beoordeling nodig - volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 capaciteitslacunes

Gespreksroutering en aflevering Beoordeling nodig - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Media en rijke inhoud Beoordeling nodig - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Native bedieningselementen en goedkeuringen Beoordeling nodig - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Native Windows - 4 gebieden

4 moeten worden beoordeeld

CLI Beoordeling nodig - volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 capaciteitslacunes

Gateway-beheer Beoordeling nodig - volledige taxonomievalidatie

0 van 11 (0%) / 0 van 11 (0%) 11 capaciteitslacunes

Netwerken Beoordeling nodig - volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Updates Beoordeling nodig - volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Native Windows-companion-app - 5 gebieden

5 moeten worden beoordeeld

Chatsessies Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 functionaliteitslacunes

Desktoptools en machtigingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 functionaliteitslacunes

Gateway-verbinding Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 functionaliteitslacunes

Installatie en updates Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

Status en reparatie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Nix-installatiepad - 5 gebieden

5 moeten worden beoordeeld

Activering en app-UX Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 functionaliteitslacunes

Configuratie en status Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 functionaliteitslacunes

Installatie-overdracht Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

Plugin-levenscyclus Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

Service-runtime en beveiligingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 8 (0%) / 0 van 8 (0%) 8 functionaliteitslacunes

OpenAI- en Codex-providerpad - 5 gebieden

2 moeten worden beoordeeld / 3 gedeeltelijk beoordeeld

Afbeeldingen en multimodale invoer Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 functionaliteitslacunes

Model en authenticatie Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 6 (16.7%) / 4 van 9 (44.4%) 5 functionaliteitslacunes

Native Codex-harnas Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 2 (0%) / 4 van 9 (44.4%) 5 functionaliteitslacunes

Responses en toolcompatibiliteit Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 4 (25%) / 2 van 5 (40%) 3 functionaliteitslacunes

Spraak en realtime audio Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 functionaliteitslacunes

OpenClaw App SDK - 6 gebieden

5 moeten worden beoordeeld / 1 gedeeltelijk beoordeeld

Agentgesprekken Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 functionaliteitslacunes

Client-API Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 functionaliteitslacunes

Compatibiliteit Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Gebeurtenissen en goedkeuringen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Gateway-toegang Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 functionaliteitslacunes

Resource-helpers Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 1 van 6 (16.7%) 5 functionaliteitslacunes

OpenRouter-providerpad - 4 gebieden

4 moeten worden beoordeeld

Chatruntime en normalisatie Moet worden beoordeeld - volledige taxonomievalidatie

0 van 15 (0%) / 0 van 15 (0%) 15 capaciteitslacunes

Mediageneratie en spraak Moet worden beoordeeld - volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 capaciteitslacunes

Providerherstel en diagnostiek Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Providerinstallatie en Auth Moet worden beoordeeld - volledige taxonomievalidatie

0 van 14 (0%) / 0 van 14 (0%) 14 capaciteitslacunes

Plugins - 9 gebieden

6 moeten worden beoordeeld / 3 gedeeltelijk beoordeeld

Plugins maken en verpakken Moet worden beoordeeld - volledige taxonomievalidatie

0 van 8 (0%) / 0 van 8 (0%) 8 capaciteitslacunes

Meegeleverde plugins Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Canvas-plugin Moet worden beoordeeld - volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 capaciteitslacunes

Kanaalplugins Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Plugins installeren en uitvoeren Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 6 (0%) / 7 van 20 (35%) 13 capaciteitslacunes

Plugin-goedkeuringen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 capaciteitslacunes

Provider- en toolplugins Gedeeltelijk beoordeeld - volledige taxonomievalidatie

1 van 6 (16.7%) / 9 van 21 (42.9%) 12 capaciteitslacunes

Plugins publiceren Moet worden beoordeeld - volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 capaciteitslacunes

Plugins testen Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 6 (0%) / 3 van 11 (27.3%) 8 capaciteitslacunes

Raspberry Pi en kleine Linux-apparaten - 4 gebieden

4 moeten worden beoordeeld

Gateway Runtime Moet worden beoordeeld - volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 capaciteitslacunes

Prestaties en diagnostiek Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Externe toegang en Auth Moet worden beoordeeld - volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 capaciteitslacunes

Installatie en compatibiliteit Moet worden beoordeeld - volledige taxonomievalidatie

0 van 12 (0%) / 0 van 12 (0%) 12 capaciteitslacunes

Beveiliging, Auth, koppeling en geheimen - 6 gebieden

2 gedeeltelijk beoordeeld / 4 moeten worden beoordeeld

Goedkeuringsbeleid en toolbeveiligingen Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 2 (0%) / 3 van 6 (50%) 3 capaciteitslacunes

Toegangscontrole voor kanalen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 capaciteitslacunes

Referentie- en geheimhygiëne Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 5 van 11 (45.5%) 6 capaciteitslacunes

Apparaat- en Node-koppeling Moet worden beoordeeld - volledige taxonomievalidatie

0 van 11 (0%) / 0 van 11 (0%) 11 capaciteitslacunes

Gateway Auth en externe toegang Moet worden beoordeeld - volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 capaciteitslacunes

Plugin-vertrouwen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 capaciteitslacunes

Sessie-, geheugen- en contextengine - 9 gebieden

2 moeten worden beoordeeld / 7 gedeeltelijk beoordeeld

CLI-sessie- en transcriptbeheer Moet worden beoordeeld - volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 capaciteitshiaten

Contextengine Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 2 (0%) / 4 van 7 (57.1%) 3 capaciteitshiaten

Kernprompts en context Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 2 (0%) / 3 van 8 (37.5%) 5 capaciteitshiaten

Geschiedenis en sessiepariteit tussen clients Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 2 (0%) / 2 van 5 (40%) 3 capaciteitshiaten

Diagnostiek, onderhoud en herstel Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 3 (0%) / 4 van 10 (40%) 6 capaciteitshiaten

Geheugen Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 6 van 13 (46.2%) 7 capaciteitshiaten

Sessierouting Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 2 (0%) / 1 van 4 (25%) 3 capaciteitshiaten

Tokenbeheer Gedeeltelijk beoordeeld - volledige taxonomievalidatie

0 van 3 (0%) / 2 van 10 (20%) 8 capaciteitshiaten

Transcriptpersistentie Moet worden beoordeeld - volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 capaciteitshiaten

Signal - 5 gebieden

5 moeten worden beoordeeld

Toegang en identiteit Moet worden beoordeeld - volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 capaciteitshiaten

Kanaalconfiguratie en bewerkingen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 capaciteitshiaten

Gespreksroutering en aflevering Moet worden beoordeeld - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitshiaat

Media en rijke content Moet worden beoordeeld - volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 capaciteitshiaten

Native bedieningselementen en goedkeuringen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 capaciteitshiaten

Slack - 5 gebieden

5 moeten worden beoordeeld

Toegang en identiteit Moet worden beoordeeld - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitshiaat

Kanaalconfiguratie en bewerkingen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 capaciteitshiaten

Gespreksroutering en aflevering Moet worden beoordeeld - volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitshiaten

Media en rijke content Moet worden beoordeeld - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitshiaat

Native bedieningselementen en goedkeuringen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 8 (0%) / 0 van 8 (0%) 8 capaciteitshiaten

Telegram - 5 gebieden

5 moeten worden beoordeeld

Toegang en identiteit Moet worden beoordeeld - volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 capaciteitshiaten

Kanaalconfiguratie en bewerkingen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 capaciteitshiaten

Gespreksroutering en aflevering Moet worden beoordeeld - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitshiaat

Media en rijke content Moet worden beoordeeld - volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitshiaat

Native bedieningselementen en goedkeuringen Moet worden beoordeeld - volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 capaciteitshiaten

Observeerbaarheid - 5 gebieden

3 gedeeltelijk beoordeeld / 2 beoordeling nodig

Diagnostische verzameling Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 8 (12.5%) / 3 van 10 (30%) 7 capaciteitslacunes

Status en herstel Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 12 (8.3%) / 5 van 18 (27.8%) 13 capaciteitslacunes

Logging Beoordeling nodig - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Sessiediagnostiek Beoordeling nodig - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Telemetry-export Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 13 (7.7%) / 7 van 21 (33.3%) 14 capaciteitslacunes

TUI - 5 gebieden

5 beoordeling nodig

Invoer en opdrachten Beoordeling nodig - Volledige taxonomievalidatie

0 van 8 (0%) / 0 van 8 (0%) 8 capaciteitslacunes

Lokale shelluitvoering Beoordeling nodig - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Veiligheid van weergave en uitvoer Beoordeling nodig - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Runtime-modi Beoordeling nodig - Volledige taxonomievalidatie

0 van 14 (0%) / 0 van 14 (0%) 14 capaciteitslacunes

Sessiebeheer Beoordeling nodig - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 capaciteitslacunes

Spraak en realtime gesprekken - 6 gebieden

6 beoordeling nodig

Gesprekken in native app Beoordeling nodig - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Realtime gesprekssessies Beoordeling nodig - Volledige taxonomievalidatie

0 van 11 (0%) / 0 van 11 (0%) 11 capaciteitslacunes

Spraak en transcriptie Beoordeling nodig - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Observeerbaarheid van gesprekken Beoordeling nodig - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 capaciteitslacunes

Gespreksproviders Beoordeling nodig - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 capaciteitslacunes

Spraakactivering en routering Beoordeling nodig - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 capaciteitslacunes

Spraakoproepkanaal - 5 gebieden

5 beoordeling nodig

Toegang en identiteit Beoordeling nodig - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitslacune

Kanaalconfiguratie en bewerkingen Beoordeling nodig - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 capaciteitslacunes

Gespreksroutering en aflevering Beoordeling nodig - Volledige taxonomievalidatie

0 van 1 (0%) / 0 van 1 (0%) 1 capaciteitslacune

Media en rich content Beoordeling nodig - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 capaciteitslacunes

Realtime spraak en oproepen Beoordeling nodig - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 capaciteitslacunes

watchOS-begeleidende interfaces - 5 gebieden

5 moeten worden beoordeeld

Levering en herstel Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 hiaten in mogelijkheden

Distributie en ondersteuning Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 hiaten in mogelijkheden

Uitvoeringsgoedkeuringen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 hiaten in mogelijkheden

Meldingen en antwoorden Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 hiaten in mogelijkheden

Watch-app-UI Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 3 (0%) / 0 van 3 (0%) 3 hiaten in mogelijkheden

Webzoektools - 4 gebieden

2 moeten worden beoordeeld / 2 gedeeltelijk beoordeeld

Netwerkveiligheid Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 hiaten in mogelijkheden

Zoekproviders Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

2 van 19 (10.5%) / 2 van 19 (10.5%) 17 hiaten in mogelijkheden

Installatie en diagnostiek Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 9 (0%) / 0 van 9 (0%) 9 hiaten in mogelijkheden

Toolbeschikbaarheid en ophalen Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

2 van 11 (18.2%) / 3 van 12 (25%) 9 hiaten in mogelijkheden

WhatsApp - 5 gebieden

5 moeten worden beoordeeld

Toegang en identiteit Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 7 (0%) / 0 van 7 (0%) 7 hiaten in mogelijkheden

Kanaalinstallatie en bewerkingen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 5 (0%) / 0 van 5 (0%) 5 hiaten in mogelijkheden

Gespreksroutering en levering Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 4 (0%) / 0 van 4 (0%) 4 hiaten in mogelijkheden

Media en rich content Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 hiaten in mogelijkheden

Systeemeigen bedieningselementen en goedkeuringen Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 2 (0%) / 0 van 2 (0%) 2 hiaten in mogelijkheden

Windows via WSL2 - 6 gebieden

5 moeten worden beoordeeld / 1 gedeeltelijk beoordeeld

Browser en Control UI Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 hiaten in mogelijkheden

CLI Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 8 (0%) / 0 van 8 (0%) 8 hiaten in mogelijkheden

Diagnostiek en reparatie Gedeeltelijk beoordeeld - Volledige taxonomievalidatie

1 van 6 (16.7%) / 3 van 8 (37.5%) 5 hiaten in mogelijkheden

Gateway-toegang en blootstelling Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 11 (0%) / 0 van 11 (0%) 11 hiaten in mogelijkheden

Levenscyclus van de Gateway-service Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 10 (0%) / 0 van 10 (0%) 10 hiaten in mogelijkheden

WSL-installatie Moet worden beoordeeld - Volledige taxonomievalidatie

0 van 6 (0%) / 0 van 6 (0%) 6 hiaten in mogelijkheden

> Laatst bijgewerkt: 2026-06-22

Was this useful?YesNo

Open issue