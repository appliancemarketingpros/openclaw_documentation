---
title: Volwassenheidstaxonomie
source_url: https://docs.openclaw.ai/nl/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Volwassenheidstaxonomie

het model achter de scorecard

Oppervlakken > categorieën > mogelijkheden > bewijs.

50 oppervlakken gegroepeerd in 4 families, waarbij elke categorie is gekoppeld aan canonieke docs en QA-dekkings-ID's.

Productgebieden bekijken / Gedetailleerde taxonomie openen / [Scores bekijken](</nl/maturity/scorecard>)

## Hoe je deze pagina leest

Een oppervlak is een productgebied zoals Gateway-runtime, Discord of de macOS-app. Elk oppervlak bevat categorieën, en elke categorie bevat controles op mogelijkheidsniveau die QA-scenario's afdekken. Gebruik de scorecard voor oordeel op releaseniveau; gebruik deze pagina om het onderliggende model te inspecteren.

## Volwassenheidsniveaus

M0GeplandDe richting is bekend, maar er bestaat geen ondersteund gebruikerspad.Promotie: ontwerpissue, eigenaar en doeloppervlak bestaan.

M1ExperimenteelGeïmplementeerd met kanttekeningen, vlaggen, bronbuilds of flows alleen voor maintainers.Promotie: maintainer kan het scenario uitvoeren vanaf de huidige main.

M2AlphaEchte gebruikers kunnen het proberen, maar brekende wijzigingen en onvolledige UX zijn te verwachten.Promotie: gedocumenteerde installatie, basistests, bekende kanttekeningen en ten minste één bewijs uit een echte omgeving.

M3BetaEr bestaat een publiek pad en de hoofdworkflow is bruikbaar met beperkte kanttekeningen.Promotie: installatie-/updatedocs, regressietests, support-runbook en succesvol scenariobewijs in de verwachte omgeving.

M4StabielAanbevolen pad voor normale gebruikers. Fouten worden behandeld als regressies.Promotie: releasegate, doctor-/probleemoplossingspad, brede docs en herhaald bewijs uit de praktijk.

M5ClawesomeGepolijst, prettig, goed geïnstrumenteerd en concurrerend met de beste vergelijkbare workflow.Promotie: Stabiel plus geslaagde gebruikersscorecard voor representatieve gebruikers.

## Productgebieden

### Kern

CLI M4Stabiel7 gebieden - 90% voltooid Gateway-runtime M4Stabiel13 gebieden - 89% voltooid Agent-runtime M3Beta9 gebieden - 79% voltooid Sessie-, geheugen- en context-engine M3Beta9 gebieden - 79% voltooid Kanaalframework M3Beta8 gebieden - 79% voltooid Observeerbaarheid M3Beta5 gebieden - 79% voltooid Gateway-web-app M3Beta6 gebieden - 79% voltooid Plugins M3Beta9 gebieden - 79% voltooid Beveiliging, auth, koppeling en geheimen M3Beta6 gebieden - 79% voltooid Automatisering: Cron, hooks, taken, polling M3Beta6 gebieden - 79% voltooid Mediabegrip en mediageneratie M2Alpha6 gebieden - 68% voltooid Spraak en realtime-gesprek M2Alpha6 gebieden - 68% voltooid TUI M2Alpha5 gebieden - 66% voltooid ClawHub M2Alpha4 gebieden - 62% voltooid OpenClaw App SDK M2Alpha6 gebieden - 53% voltooid

### Platform

Linux Gateway-host M4Stabiel5 gebieden - 89% voltooid macOS Gateway-host M4Stabiel7 gebieden - 88% voltooid Docker- en Podman-hosting M3Beta4 gebieden - 79% voltooid Windows via WSL2 M3Beta6 gebieden - 79% voltooid Raspberry Pi en kleine Linux-apparaten M3Beta4 gebieden - 79% voltooid macOS-begeleidende app M3Beta8 gebieden - 78% voltooid Android-app M2Alpha7 gebieden - 66% voltooid Native Windows M2Alpha4 gebieden - 66% voltooid Kubernetes-hosting M2Alpha4 gebieden - 61% voltooid iOS-app M1Experimenteel8 gebieden - 44% voltooid Nix-installatiepad M1Experimenteel5 gebieden - 44% voltooid watchOS-begeleidende oppervlakken M1Experimenteel5 gebieden - 44% voltooid Linux-begeleidende app M0Gepland5 gebieden - 21% voltooid Native Windows-begeleidende app M0Gepland5 gebieden - 21% voltooid

### Kanaal

Discord M4Stabiel6 gebieden - 87% voltooid Telegram M3Beta5 gebieden - 78% voltooid Slack M3Beta5 gebieden - 78% voltooid iMessage en BlueBubbles M3Beta5 gebieden - 78% voltooid WhatsApp M3Beta5 gebieden - 78% voltooid Matrix M2Alpha6 gebieden - 67% voltooid Google Chat M2Alpha5 gebieden - 66% voltooid Microsoft Teams M2Alpha5 gebieden - 66% voltooid Signal M2Alpha5 gebieden - 66% voltooid Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale kanalen M2Alpha4 gebieden - 58% voltooid Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alpha4 gebieden - 54% voltooid Spraakoproepkanaal M1Experimenteel5 gebieden - 44% voltooid

### Provider en tool

Browserautomatisering, exec en sandbox-tools M3Beta3 gebieden - 79% voltooid OpenAI- en Codex-providerpad M3Beta5 gebieden - 79% voltooid Webzoektools M3Beta4 gebieden - 79% voltooid Anthropic-providerpad M3Beta5 gebieden - 78% voltooid Google-providerpad M3Beta5 gebieden - 78% voltooid OpenRouter-providerpad M3Beta4 gebieden - 78% voltooid Tools voor het genereren van afbeeldingen, video en muziek M2Alpha5 gebieden - 68% voltooid Lokale modelproviders: Ollama, vLLM, SGLang, LM Studio M2Alpha5 gebieden - 68% voltooid Gehoste longtail-providers M2Alpha3 gebieden - 68% voltooid

## Details

### Kern

CLI - M4 Stabiel - 7 gebieden

Normale installatie- en reparatiepaden zijn gedocumenteerd in de installatie-, CLI- en gatewaydocumentatie. Platformspecifieke Windows-paden worden bijgehouden in de rijen Windows via WSL2 en Native Windows.

Dekking experimenteel - 4%Kwaliteit stabiel - 83%Volledigheid stabiel - 90%Gedeeltelijk - 6

CLI-installatie 6 mogelijkheden / met LTS-ondersteuning

Experimenteel17%

Stabiel89%

Stabiel90%

[Index](</nl/install>), [Installatieprogramma](</nl/install/installer>), [Node](</nl/install/node>), [Bijwerken](</nl/install/updating>)

Onboarding- en auth-installatie 5 mogelijkheden / met LTS-ondersteuning

Experimenteel0%

Beta75%

Stabiel89%

[Onboard](</nl/cli/onboard>), [Configureren](</nl/cli/configure>), [Onboarding-overzicht](</nl/start/onboarding-overview>)

Plugin- en kanaalinstallatie 5 mogelijkheden

Experimenteel0%

Beta75%

Stabiel89%

[Onboard](</nl/cli/onboard>), [Plugins](</nl/cli/plugins>), [Kanalen](</nl/cli/channels>)

Beheer van Gateway-service 5 mogelijkheden / met LTS-ondersteuning

Experimenteel14%

Stabiel87%

Stabiel90%

[Gateway](</nl/cli/gateway>), [Bijwerken](</nl/install/updating>), [Probleemoplossing](</nl/gateway/troubleshooting>)

CLI-observeerbaarheid 5 mogelijkheden / met LTS-ondersteuning

Experimenteel0%

Stabiel89%

Stabiel90%

[Status](</nl/cli/status>), [Gezondheid](</nl/cli/health>), [Logs](</nl/cli/logs>), [Diagnostiek](</nl/gateway/diagnostics>)

Doctor 10 mogelijkheden / met LTS-ondersteuning

Experimenteel0%

Stabiel89%

Stabiel90%

[Doctor](</nl/cli/doctor>), [Doctor](</nl/gateway/doctor>), [Geheimen](</nl/gateway/secrets>), [Probleemoplossing](</nl/gateway/troubleshooting>)

Updates en upgrades 5 mogelijkheden / met LTS-ondersteuning

Experimenteel0%

Beta75%

Stabiel89%

[Bijwerken](</nl/install/updating>), [Update](</nl/cli/update>), [Probleemoplossing](</nl/gateway/troubleshooting>)

Gateway-runtime - M4 Stabiel - 13 gebieden

Kernarchitectuur, auth, koppeling, protocol-documentatie, daemon-documentatie en CLI-runbooks zijn breed en actueel.

Dekking experimenteel - 6%Kwaliteit stabiel - 81%Volledigheid stabiel - 89%Gedeeltelijk - 12

Goedkeuringen en uitvoering op afstand 6 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Protocol](</nl/gateway/protocol>), [Index](</nl/gateway/security>)

HTTP-API's 4 mogelijkheden / LTS-ondersteund

Experimenteel25%

Stabiel90%

Stabiel90%

[Index](</nl/gateway>), [Openai HTTP-API](</nl/gateway/openai-http-api>), [Openresponses HTTP-API](</nl/gateway/openresponses-http-api>), [Tools Invoke HTTP-API](</nl/gateway/tools-invoke-http-api>), [Hooks](</nl/automation/hooks>), [Index](</nl/web>)

Gehost weboppervlak 4 mogelijkheden / LTS-ondersteund

Experimenteel0%

Stabiel89%

Stabiel90%

[Index](</nl/gateway>), [Architectuur](</nl/concepts/architecture>), [Control-UI](</nl/web/control-ui>), [Webchat](</nl/web/webchat>), [Canvas](</nl/refactor/canvas>)

Gateway RPC-API's en gebeurtenissen 20 mogelijkheden / LTS-ondersteund

Experimenteel9%

Stabiel90%

Stabiel90%

[Protocol](</nl/gateway/protocol>), [Index](</nl/gateway>), [Architectuur](</nl/concepts/architecture>)

Apparaatauthenticatie en koppeling 10 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Protocol](</nl/gateway/protocol>), [Koppeling](</nl/gateway/pairing>), [Index](</nl/gateway/security>)

Netwerktoegang en detectie 6 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Index](</nl/gateway>), [Detectie](</nl/gateway/discovery>), [Protocol](</nl/gateway/protocol>)

Nodes en mogelijkheden op afstand 8 mogelijkheden

Experimenteel0%

Beta75%

Stabiel89%

[Protocol](</nl/gateway/protocol>), [Architectuur](</nl/concepts/architecture>), [Index](</nl/nodes>)

Status, diagnostiek en herstel 7 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Index](</nl/gateway>), [Diagnostiek](</nl/gateway/diagnostics>), [Doctor](</nl/gateway/doctor>)

Protocolcompatibiliteit 7 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Protocol](</nl/gateway/protocol>), [Architectuur](</nl/concepts/architecture>), [Typebox](</nl/concepts/typebox>), [Bridge-protocol](</nl/gateway/bridge-protocol>)

Rollen en machtigingen 5 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Protocol](</nl/gateway/protocol>), [Index](</nl/gateway/security>)

Gateway-levenscyclus 7 mogelijkheden / LTS-ondersteund

Experimenteel33%

Stabiel90%

Stabiel90%

[Index](</nl/gateway>), [Architectuur](</nl/concepts/architecture>)

Beveiligingsmaatregelen 6 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Index](</nl/gateway/security>), [Protocol](</nl/gateway/protocol>), [Ontdekking](</nl/gateway/discovery>)

WebSocket-verbinding 8 mogelijkheden / LTS-ondersteund

Experimenteel13%

Stabiel90%

Stabiel90%

[Protocol](</nl/gateway/protocol>), [Architectuur](</nl/concepts/architecture>)

Agentruntime - M3 Beta - 9 gebieden

Hoofdlus, modellen, provider-routering en toolstreaming zijn volwaardige onderdelen, maar providergedrag verandert wekelijks en vereist scenariobewijs per release.

Dekking Experimenteel - 33%Kwaliteit Beta - 78%Volledigheid Beta - 79%Gedeeltelijk - 6

Uitvoering van agentbeurten 3 mogelijkheden / LTS-ondersteund

Experimenteel29%

Bèta79%

Bèta79%

[Agentlus](</nl/concepts/agent-loop>), [Agent](</nl/cli/agent>), [Agent-runtimes](</nl/concepts/agent-runtimes>)

Externe runtimes en subagents 4 mogelijkheden

Experimenteel30%

Bèta79%

Bèta79%

[Agent-runtimes](</nl/concepts/agent-runtimes>), [Anthropic](</nl/providers/anthropic>), [Google](</nl/providers/google>), [Subagents](</nl/tools/subagents>)

Uitvoering door gehoste providers 5 mogelijkheden / LTS-ondersteund

Experimenteel20%

Bèta79%

Bèta79%

[Openai](</nl/providers/openai>), [Anthropic](</nl/providers/anthropic>), [Google](</nl/providers/google>), [Modellen](</nl/concepts/models>)

Lokale en zelfgehoste providers 5 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Ollama](</nl/providers/ollama>), [Modellen](</nl/concepts/models>), [Agent](</nl/cli/agent>)

Model- en runtimeselectie 4 mogelijkheden / LTS-ondersteund

Experimenteel25%

Bèta79%

Bèta79%

[Modellen](</nl/concepts/models>), [Modellen](</nl/cli/models>), [Openai](</nl/providers/openai>), [Agent-runtimes](</nl/concepts/agent-runtimes>)

Provider-authenticatie 10 mogelijkheden / LTS-ondersteund

Experimenteel24%

Bèta79%

Bèta79%

[Modellen](</nl/concepts/models>), [Agent](</nl/cli/agent>), [Modellen](</nl/cli/models>), [Openai](</nl/providers/openai>), [Anthropic](</nl/providers/anthropic>), [Google](</nl/providers/google>), [Subagents](</nl/tools/subagents>)

Streaming en voortgang 2 mogelijkheden

Alfa56%

Bèta79%

Bèta79%

[Streaming](</nl/concepts/streaming>), [Agentlus](</nl/concepts/agent-loop>)

Tool-aanroepen en responsverwerking 3 mogelijkheden / LTS-ondersteund

Alfa65%

Bèta79%

Bèta79%

[Agentlus](</nl/concepts/agent-loop>), [Ollama](</nl/providers/ollama>)

Controls voor tooluitvoering 6 mogelijkheden / door LTS ondersteund

Alfa50%

Bèta79%

Bèta79%

[Sandbox versus toolbeleid versus verhoogd](</nl/gateway/sandbox-vs-tool-policy-vs-elevated>), [Agentlus](</nl/concepts/agent-loop>), [Subagenten](</nl/tools/subagents>)

Sessie, geheugen en context-engine - M3 Beta - 9 gebieden

Sterke documentatie en actieve implementatie. Volwassenheid hangt af van transcriptieduurzaamheid, Compaction-kwaliteit en pariteit tussen clients.

Dekking Experimenteel - 30%Kwaliteit Beta - 77%Volledigheid Beta - 79%Gedeeltelijk - 6

CLI-sessie- en transcriptbeheer 2 mogelijkheden / met LTS-ondersteuning

Experimenteel0%

Alfa68%

Bèta79%

[Sessie](</nl/concepts/session>), [Sessiebeheer Compaction](</nl/reference/session-management-compaction>), [Sessies](</nl/cli/sessions>)

Tokenbeheer 3 mogelijkheden / met LTS-ondersteuning

Experimenteel20%

Bèta79%

Bèta79%

[Compaction](</nl/concepts/compaction>), [Context](</nl/concepts/context>), [Sessiebeheer Compaction](</nl/reference/session-management-compaction>)

Context Engine 2 mogelijkheden / met LTS-ondersteuning

Alfa57%

Bèta79%

Bèta79%

[Context](</nl/concepts/context>), [Context Engine](</nl/concepts/context-engine>), [Codex Context Engine-harnas](</nl/plan/codex-context-engine-harness>)

Cross-client geschiedenis en sessiepariteit 2 mogelijkheden

Experimenteel40%

Bèta79%

Bèta79%

[Webchat](</nl/web/webchat>), [Android](</nl/platforms/android>), [Kanaalroutering](</nl/channels/channel-routing>)

Diagnostiek, onderhoud en herstel 3 mogelijkheden

Experimenteel40%

Bèta79%

Bèta79%

[Diagnostiek](</nl/gateway/diagnostics>), [Sessiebeheer Compaction](</nl/reference/session-management-compaction>), [Vlaggen](</nl/diagnostics/flags>)

Kernprompts en context 2 mogelijkheden / met LTS-ondersteuning

Experimenteel38%

Bèta79%

Bèta79%

[Context](</nl/concepts/context>), [Transcripthygiëne](</nl/reference/transcript-hygiene>), [Discord](</nl/channels/discord>)

Geheugen 5 mogelijkheden

Experimenteel46%

Bèta79%

Bèta79%

[Geheugenconfiguratie](</nl/reference/memory-config>), [Geheugen-Qmd](</nl/concepts/memory-qmd>), [Geheugen](</nl/concepts/memory>), [Discord](</nl/channels/discord>)

Sessieroutering 2 mogelijkheden / met LTS-ondersteuning

Experimenteel25%

Bèta79%

Bèta79%

[Sessie](</nl/concepts/session>), [Kanaalroutering](</nl/channels/channel-routing>), [Discord](</nl/channels/discord>)

Transcriptpersistentie 2 mogelijkheden / door LTS ondersteund

Experimenteel0%

Alfa68%

Bèta79%

[Sessiebeheer Compaction](</nl/reference/session-management-compaction>), [Transcripthygiëne](</nl/reference/transcript-hygiene>)

Kanaalframework - M3-bèta - 8 gebieden

Veel kanalen delen Gateway-bezorgings- en routeringscontracten, maar kanaalgedrag verschilt per upstream-API en beperkingen van accountbeleid.

Dekking experimenteel - 13%Kwaliteit bèta - 76%Volledigheid bèta - 79%Gedeeltelijk - 5

Kanaalactieopdrachten en goedkeuringen 5 mogelijkheden

Experimenteel0%

Bèta79%

Bèta79%

[Groepen](</nl/channels/groups>), [Discord](</nl/channels/discord>), [Google Chat](</nl/channels/googlechat>), [Signal](</nl/channels/signal>), [Matrix](</nl/channels/matrix>)

Kanaalconfiguratie 5 mogelijkheden / LTS-ondersteund

Experimenteel14%

Bèta79%

Bèta79%

[Index](</nl/channels>), [Koppelen](</nl/channels/pairing>), [Probleemoplossing](</nl/channels/troubleshooting>), [SDK-kanaalplugins](</nl/plugins/sdk-channel-plugins>)

Groepsthread- en ambient-ruimtegedrag 5 mogelijkheden

Experimenteel36%

Bèta79%

Bèta79%

[Groepen](</nl/channels/groups>), [Groepsberichten](</nl/channels/group-messages>), [Ambient-ruimtegebeurtenissen](</nl/channels/ambient-room-events>), [Uitzendgroepen](</nl/channels/broadcast-groups>), [Discord](</nl/channels/discord>)

Inkomende toegang en identiteitspoorten 5 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa68%

Bèta79%

[Toegangsgroepen](</nl/channels/access-groups>), [Groepen](</nl/channels/groups>), [Discord](</nl/channels/discord>), [LINE](</nl/channels/line>)

Mediabijlagen en rijke kanaalgegevens 4 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[LINE](</nl/channels/line>), [Signal](</nl/channels/signal>), [Google Chat](</nl/channels/googlechat>), [Matrix](</nl/channels/matrix>), [Discord](</nl/channels/discord>)

Uitgaande aflevering en antwoordpipeline 4 mogelijkheden / LTS-ondersteund

Experimenteel38%

Bèta79%

Bèta79%

[Groepen](</nl/channels/groups>), [Ambient-ruimtegebeurtenissen](</nl/channels/ambient-room-events>), [Discord](</nl/channels/discord>), [Matrix](</nl/channels/matrix>), [Configuratiekanalen](</nl/gateway/config-channels>)

Gespreksroutering en aflevering 10 mogelijkheden / LTS-ondersteund

Experimenteel19%

Bèta79%

Bèta79%

[Kanaalroutering](</nl/channels/channel-routing>), [Groepen](</nl/channels/groups>), [Discord](</nl/channels/discord>), [Matrix](</nl/channels/matrix>), [Probleemoplossing](</nl/channels/troubleshooting>), [Configuratiereferentie](</nl/gateway/configuration-reference>)

Statusgezondheid en operatorbediening 4 mogelijkheden / LTS-ondersteund

Experimenteel0%

Bèta79%

Beta79%

[Status](</nl/gateway/health>), [Configuratiereferentie](</nl/gateway/configuration-reference>), [Probleemoplossing](</nl/channels/troubleshooting>), [Discord](</nl/channels/discord>)

Observability - M3 Beta - 5 areas

OTel-, Prometheus-, logging- en diagnostiekdocumentatie bestaat. Heeft een openbare volwassenheidsronde nodig voor "waar operators als eerste naar moeten kijken".

Dekking Experimenteel - 18%Kwaliteit Beta - 75%Volledigheid Beta - 79%Gedeeltelijk - 3

Status en reparatie 12 mogelijkheden / LTS-ondersteund

Experimenteel28%

Beta79%

Beta79%

[Status](</nl/gateway/health>), [Telegram](</nl/channels/telegram>), [Doctor](</nl/cli/doctor>), [Doctor](</nl/gateway/doctor>), [SDK-subpaden](</nl/plugins/sdk-subpaths>), [Status](</nl/cli/health>), [Protocol](</nl/gateway/protocol>)

Logging 5 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa68%

Beta79%

[Logging](</nl/logging>), [Logging](</nl/gateway/logging>), [Logs](</nl/cli/logs>)

Diagnostische verzameling 8 mogelijkheden

Experimenteel30%

Beta79%

Beta79%

[Diagnostiek](</nl/gateway/diagnostics>), [Status](</nl/gateway/health>), [Codex-harnas](</nl/plugins/codex-harness>), [Protocol](</nl/gateway/protocol>)

Telemetry-export 13 mogelijkheden

Experimenteel33%

Beta79%

Beta79%

[Hooks](</nl/plugins/hooks>), [Opentelemetry](</nl/gateway/opentelemetry>), [Logging](</nl/logging>), [SDK-subpaden](</nl/plugins/sdk-subpaths>), [Diagnostiek Otel](</nl/plugins/reference/diagnostics-otel>), [Prometheus](</nl/gateway/prometheus>), [Diagnostiek Prometheus](</nl/plugins/reference/diagnostics-prometheus>)

Sessiediagnostiek 4 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa68%

Beta79%

[Opentelemetry](</nl/gateway/opentelemetry>), [Prometheus](</nl/gateway/prometheus>), [Diagnostiek](</nl/gateway/diagnostics>), [Protocol](</nl/gateway/protocol>)

Gateway-webapp - M3 Beta - 6 gebieden

Web-UI is gedocumenteerd met koppeling, chat, PWA, Talk, push en externe Gateway-flows. Promoveer na scorecards voor cross-browser en mobiele PWA.

Dekking Experimenteel - 4%Kwaliteit Beta - 74%Volledigheid Beta - 79%Geen

Realtime browsergesprek 5 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Control Ui](</nl/web/control-ui>), [Protocol](</nl/gateway/protocol>), [Gesprek](</nl/nodes/talk>)

Browsertoegang en vertrouwen 5 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Control Ui](</nl/web/control-ui>), [Dashboard](</nl/web/dashboard>), [Tailscale](</nl/gateway/tailscale>), [Extern](</nl/gateway/remote>)

Configuratie 5 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Control Ui](</nl/web/control-ui>), [Configuratie](</nl/gateway/configuration>)

Browser-UI 10 mogelijkheden

Experimenteel8%

Bèta79%

Bèta79%

[Control Ui](</nl/web/control-ui>), [Index](</nl/web>), [Dashboard](</nl/web/dashboard>), [Protocol](</nl/gateway/protocol>)

WebChat-gesprekken 15 mogelijkheden

Experimenteel10%

Bèta79%

Bèta79%

[Control Ui](</nl/web/control-ui>), [Webchat](</nl/web/webchat>), [Aan de slag](</nl/start/getting-started>), [Kanaalroutering](</nl/channels/channel-routing>), [Veilige bestandsbewerkingen](</nl/gateway/security/secure-file-operations>)

Operatorconsole 10 mogelijkheden

Experimenteel8%

Bèta79%

Bèta79%

[Control Ui](</nl/web/control-ui>), [Gezondheid](</nl/gateway/health>), [Protocol](</nl/gateway/protocol>), [Dashboard](</nl/web/dashboard>)

Plugins - M3 Bèta - 9 gebieden

Er bestaan brede documentatie en sterk intern runtime-bewijs voor manifests, discovery, laden, provider-/toolarchitectuur en goedkeuringsgrenzen. Houd de rij op bèta totdat publiek SDK API-/subpadbewijs en extern distributiebewijs sterker zijn.

Dekking Experimenteel - 12%Kwaliteit Bèta - 72%Volledigheid Bèta - 79%Gedeeltelijk - 7

Plugins maken en verpakken 8 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alpha68%

Beta79%

[Plugins bouwen](</nl/plugins/building-plugins>), [Sdk-overzicht](</nl/plugins/sdk-overview>), [Sdk-entrypoints](</nl/plugins/sdk-entrypoints>), [Sdk-subpaden](</nl/plugins/sdk-subpaths>), [Manifest](</nl/plugins/manifest>), [Referentie](</nl/plugins/reference>)

Meegeleverde plugins 5 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alpha68%

Beta79%

[Plugin-inventaris](</nl/plugins/plugin-inventory>), [Plugins](</nl/cli/plugins>), [Interne architectuur](</nl/plugins/architecture-internals>)

Canvas-plugin 6 mogelijkheden

Experimenteel0%

Alpha68%

Beta79%

[Canvas](</nl/plugins/reference/canvas>), [Canvas](</nl/refactor/canvas>), [Configuratiereferentie](</nl/gateway/configuration-reference>)

Plugins installeren en uitvoeren 6 mogelijkheden / LTS-ondersteund

Experimenteel35%

Beta79%

Beta79%

[Architectuur](</nl/plugins/architecture>), [Interne architectuur](</nl/plugins/architecture-internals>), [Plugins](</nl/cli/plugins>)

Kanaalplugins 5 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alpha68%

Beta79%

[Sdk-kanaalplugins](</nl/plugins/sdk-channel-plugins>), [Sdk-kanaal inkomend](</nl/plugins/sdk-channel-inbound>), [Sdk-kanaal uitgaand](</nl/plugins/sdk-channel-outbound>)

Provider- en toolplugins 6 mogelijkheden / LTS-ondersteund

Experimenteel43%

Beta79%

Beta79%

[Sdk-providerplugins](</nl/plugins/sdk-provider-plugins>), [Toolplugins](</nl/plugins/tool-plugins>), [Mogelijkheden toevoegen](</nl/plugins/adding-capabilities>)

Plugin-goedkeuringen 6 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alpha68%

Beta79%

[Plugin-machtigingsverzoeken](</nl/plugins/plugin-permission-requests>), [Exec-goedkeuringen](</nl/tools/exec-approvals>), [Sdk-kanaalplugins](</nl/plugins/sdk-channel-plugins>)

Plugins publiceren 6 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alpha68%

Beta79%

[Plugins](</nl/cli/plugins>), [Compatibiliteit](</nl/plugins/compatibility>), [Publiceren](</nl/clawhub/publishing>)

Plugins testen 6 mogelijkheden

Experimenteel27%

Beta79%

Beta79%

[Sdk testen](</nl/plugins/sdk-testing>), [Sdk instellen](</nl/plugins/sdk-setup>), [Codex-harnas](</nl/plugins/codex-harness>)

Security, auth, pairing, and secrets - M3 Beta - 6 areas

Goede documentatie en hardingsoppervlakken bestaan. Promoveer nadat regelmatige upgrade- en beveiligingsscenarioruns bewijzen dat er geen setup-regressies zijn.

Dekking Experimenteel - 16%Kwaliteit Beta - 72%Volledigheid Beta - 79%Gedeeltelijk - 5

Goedkeuringsbeleid en toolbeveiligingen 2 mogelijkheden / LTS-ondersteund

Alpha50%

Beta79%

Beta79%

[Exec-goedkeuringen](</nl/tools/exec-approvals>), [Goedkeuringen](</nl/cli/approvals>), [Plugin-machtigingsverzoeken](</nl/plugins/plugin-permission-requests>), [Auditcontroles](</nl/gateway/security/audit-checks>)

Gateway-authenticatie en externe toegang 9 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alpha68%

Beta79%

[Index](</nl/gateway/security>), [Runbook voor blootstelling](</nl/gateway/security/exposure-runbook>), [Vertrouwde-proxy-authenticatie](</nl/gateway/trusted-proxy-auth>), [Tailscale](</nl/gateway/tailscale>), [Extern](</nl/gateway/remote>), [Configuratiereferentie](</nl/gateway/configuration-reference>), [Gateway](</nl/cli/gateway>), [Doctor](</nl/cli/doctor>), [Control-UI](</nl/web/control-ui>), [Browserbesturing](</nl/tools/browser-control>), [Auditcontroles](</nl/gateway/security/audit-checks>)

Toegangscontrole voor kanalen 3 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alpha68%

Beta79%

[Koppelen](</nl/channels/pairing>), [Telegram](</nl/channels/telegram>), [Toegangsgroepen](</nl/channels/access-groups>), [Auditcontroles](</nl/gateway/security/audit-checks>)

Apparaat- en Node-koppeling 11 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alpha68%

Beta79%

[Protocol](</nl/gateway/protocol>), [Apparaten](</nl/cli/devices>), [Koppelen](</nl/channels/pairing>), [Koppelen](</nl/gateway/pairing>), [Operatorbereiken](</nl/gateway/operator-scopes>), [Control-UI](</nl/web/control-ui>), [Webchat](</nl/web/webchat>), [Goedkeuringen](</nl/cli/approvals>)

Plugin-vertrouwen 2 mogelijkheden

Experimenteel0%

Alpha68%

Beta79%

[Manifest](</nl/plugins/manifest>), [Plugin-machtigingsverzoeken](</nl/plugins/plugin-permission-requests>), [Plugins beheren](</nl/plugins/manage-plugins>), [Auditcontroles](</nl/gateway/security/audit-checks>)

Hygiëne voor referenties en geheimen 5 mogelijkheden / LTS-ondersteund

Experimenteel46%

Beta79%

Beta79%

[Authenticatie](</nl/gateway/authentication>), [Modellen](</nl/cli/models>), [Openai](</nl/providers/openai>), [Oauth](</nl/concepts/oauth>), [Geheimen](</nl/gateway/secrets>), [Geheimen](</nl/cli/secrets>), [Secretref-referentieoppervlak](</nl/reference/secretref-credential-surface>), [Auditcontroles](</nl/gateway/security/audit-checks>)

Automation: cron, hooks, tasks, polling - M3 Beta - 6 areas

Gedocumenteerd en bruikbaar, maar scenariobewijs moet onbeheerde levering, nieuwe pogingen en zichtbaarheid van fouten dekken.

Dekking Experimenteel - 2%Kwaliteit Beta - 72%Volledigheid Beta - 79%Geen

Cron-taken 15 mogelijkheden

Experimenteel0%

Bèta79%

Bèta79%

[Cron-taken](</nl/automation/cron-jobs>), [Cron](</nl/cli/cron>), [Protocol](</nl/gateway/protocol>), [Taken](</nl/automation/tasks>), [Discord](</nl/channels/discord>)

Gebeurtenisinvoer 15 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Telegram](</nl/channels/telegram>), [Zalo](</nl/channels/zalo>), [Probleemoplossing](</nl/channels/troubleshooting>), [iMessage vanuit Bluebubbles](</nl/channels/imessage-from-bluebubbles>), [Gmail Pubsub-integratie](</nl/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</nl/automation/cron-jobs>), [Webhooks](</nl/cli/webhooks>), [Webhooks](</nl/automation/cron-jobs#webhooks>), [Webhook](</nl/automation/cron-jobs>)

Automatiseringshooks 11 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Hooks](</nl/automation/hooks>), [Hooks](</nl/cli/hooks>), [Hooks](</nl/plugins/hooks>), [Plugin-machtigingsverzoeken](</nl/plugins/plugin-permission-requests>), [SDK-subpaden](</nl/plugins/sdk-subpaths>)

Achtergrondtaken en flows 10 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Taken](</nl/automation/tasks>), [Index](</nl/automation>), [Taken](</nl/cli/tasks>), [Taskflow](</nl/automation/taskflow>), [SDK-runtime](</nl/plugins/sdk-runtime>)

Heartbeat 5 mogelijkheden

Experimenteel14%

Bèta79%

Bèta79%

[Index](</nl/automation>), [Heartbeat](</nl/gateway/heartbeat>), [Verplichtingen](</nl/concepts/commitments>)

Pollingbesturing 10 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Pollen](</nl/cli/message>), [Bericht](</nl/cli/message>), [Telegram](</nl/channels/telegram>), [Msteams](</nl/channels/msteams>), [Achtergrondproces](</nl/gateway/background-process>)

Mediabegrip en mediageneratie - M2 Alfa - 6 gebieden

Er bestaat een breed mogelijkhedenoppervlak, maar providervariatie, bestandslimieten en pariteit tussen Node en app maken dit nog niet stabiel.

Dekking Experimenteel - 2%Kwaliteit Alfa - 64%Volledigheid Alfa - 68%Geen

Media-invoer en toegang 8 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Mediaoverzicht](</nl/tools/media-overview>), [Mediabegrip](</nl/nodes/media-understanding>), [Veilige bestandsbewerkingen](</nl/gateway/security/secure-file-operations>), [Pdf](</nl/tools/pdf>), [Afbeeldingsgeneratie](</nl/tools/image-generation>), [Qr](</nl/cli/qr>), [LINE](</nl/channels/line>), [WhatsApp](</nl/channels/whatsapp>)

Afhandeling van kanaalmedia 5 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Afbeeldingen](</nl/nodes/images>), [Mediaoverzicht](</nl/tools/media-overview>), [Discord](</nl/channels/discord>)

Mediaconfiguratie 1 mogelijkheid

Experimenteel0%

Alpha61%

Alpha68%

[Mediaoverzicht](</nl/tools/media-overview>), [Afbeeldingsgeneratie](</nl/tools/image-generation>), [Manifest](</nl/plugins/manifest>), [Codex-harnas](</nl/plugins/codex-harness>)

Tekst-naar-spraaklevering 2 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Tts](</nl/tools/tts>), [Mediaoverzicht](</nl/tools/media-overview>), [Discord](</nl/channels/discord>)

Mediabegrip 12 mogelijkheden

Experimenteel7%

Alpha69%

Alpha69%

[Audio](</nl/nodes/audio>), [Mediabegrip](</nl/nodes/media-understanding>), [Mediaoverzicht](</nl/tools/media-overview>), [WhatsApp](</nl/channels/whatsapp>), [Afbeeldingen](</nl/nodes/images>), [Afleiden](</nl/cli/infer>), [Pdf](</nl/tools/pdf>)

Mediageneratie 17 mogelijkheden

Experimenteel5%

Alpha69%

Alpha69%

[Afbeeldingsgeneratie](</nl/tools/image-generation>), [Mediaoverzicht](</nl/tools/media-overview>), [Skills](</nl/tools/skills>), [Muziekgeneratie](</nl/tools/music-generation>), [Videogeneratie](</nl/tools/video-generation>)

Spraak en realtime gesprek - M2 Alpha - 6 gebieden

Er bestaan meerdere implementaties in Control UI, apps en providers. Hiervoor zijn scorecards voor latentie, foutmodi en installatie nodig vóór beta.

Dekking experimenteel - 0%Kwaliteit Alpha - 61%Volledigheid Alpha - 68%Geen

Gespreksproviders 7 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Openai](</nl/providers/openai>), [Google](</nl/providers/google>), [SDK-providerplugins](</nl/plugins/sdk-provider-plugins>), [Gesprek](</nl/nodes/talk>), [Besturings-UI](</nl/web/control-ui>)

Realtime gesprekssessies 11 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Gesprek](</nl/nodes/talk>), [Besturings-UI](</nl/web/control-ui>)

Spraak en transcriptie 5 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Gesprek](</nl/nodes/talk>), [Openai](</nl/providers/openai>), [Google](</nl/providers/google>)

Gesprekken in native apps 4 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Gesprek](</nl/nodes/talk>), [Voicewake](</nl/platforms/mac/voicewake>)

Spraakactivering en routering 4 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Voicewake](</nl/nodes/voicewake>), [Voicewake](</nl/platforms/mac/voicewake>), [Spraakoverlay](</nl/platforms/mac/voice-overlay>)

Observeerbaarheid van gesprekken 5 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Besturings-UI](</nl/web/control-ui>), [Spraakoverlay](</nl/platforms/mac/voice-overlay>), [Gesprek](</nl/nodes/talk>)

TUI - M2 Alpha - 5 domeinen

Aanwezig in documentatie en broncode, maar minder zichtbaar als primaire gebruikersworkflow. Heeft een expliciete scenariodefinitie nodig.

Dekking Experimenteel - 0%Kwaliteit Alpha - 59%Volledigheid Alpha - 66%Geen

Runtime-modi 14 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[TUI](</nl/cli/tui>), [TUI](</nl/web/tui>), [Index](</nl/cli>)

Invoer en opdrachten 8 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[TUI](</nl/web/tui>)

Sessiebeheer 3 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[TUI](</nl/web/tui>), [Sessies](</nl/cli/sessions>)

Lokale shell-uitvoering 4 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[TUI](</nl/web/tui>), [TUI](</nl/cli/tui>)

Rendering en uitvoerveiligheid 4 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[TUI](</nl/web/tui>), [QR](</nl/cli/qr>), [Logs](</nl/cli/logs>), [Voltooiing](</nl/cli/completion>)

ClawHub - M2 Alpha - 4 gebieden

Openbare docs en ecosysteemconcept bestaan. Vereist installatie-, vertrouwens-, update-, rollback- en compatibiliteitsscorekaarten.

Dekking Experimenteel - 0%Kwaliteit Alpha - 58%Volledigheid Alpha - 62%Geen

Publicatie 7 capaciteiten

Experimenteel0%

Alpha54%

Alpha55%

[Publicatie](</nl/clawhub/publishing>), [Skills maken](</nl/tools/creating-skills>), [Community](</nl/plugins/community>)

Catalogusdetectie 5 capaciteiten

Experimenteel0%

Alpha61%

Alpha68%

[Plugin](</nl/tools/plugin>), [Plugins](</nl/cli/plugins>), [Skills](</nl/cli/skills>), [Skills](</nl/tools/skills>), [Community](</nl/plugins/community>)

Compatibiliteit en vertrouwen 12 capaciteiten

Experimenteel0%

Alpha55%

Alpha56%

[Plugin](</nl/tools/plugin>), [Plugins](</nl/cli/plugins>), [Compatibiliteit](</nl/plugins/compatibility>), [Plugin-inventaris](</nl/plugins/plugin-inventory>), [Publicatie](</nl/clawhub/publishing>), [Skills](</nl/tools/skills>), [Skills-configuratie](</nl/tools/skills-config>)

Plugin-levenscyclus en -status 26 capaciteiten

Experimenteel0%

Alpha61%

Alpha68%

[Plugin](</nl/tools/plugin>), [Plugins](</nl/cli/plugins>), [Skills](</nl/cli/skills>), [Skills](</nl/tools/skills>), [Protocol](</nl/gateway/protocol>), [Bundels](</nl/plugins/bundles>), [Afhankelijkheidsresolutie](</nl/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 gebieden

OpenClaw App SDK is een afzonderlijk extern appcontract, los van Gateway-runtime en Plugin SDK. De huidige score toont een echt `@openclaw/sdk`-pad met hiaten rond openbare packaging, automatische detectie, goedkeuringen, hulpfuncties en compatibiliteit.

Dekking experimenteel - 3%Kwaliteit Alpha - 54%Volledigheid Alpha - 53%Geen

Client-API 4 mogelijkheden

Experimenteel0%

Alpha51%

Alpha50%

[Openclaw Sdk](</nl/gateway/external-apps>), [Openclaw Sdk-API-ontwerp](</nl/gateway/external-apps>)

Gateway-toegang 5 mogelijkheden

Experimenteel0%

Alpha53%

Alpha54%

[Openclaw Sdk](</nl/gateway/external-apps>), [Openclaw Sdk-API-ontwerp](</nl/gateway/external-apps>), [Protocol](</nl/gateway/protocol>), [Index](</nl/gateway/security>)

Agentgesprekken 6 mogelijkheden

Experimenteel0%

Alpha52%

Alpha52%

[Openclaw Sdk](</nl/gateway/external-apps>), [Openclaw Sdk-API-ontwerp](</nl/gateway/external-apps>), [Protocol](</nl/gateway/protocol>)

Gebeurtenissen en goedkeuringen 5 mogelijkheden

Experimenteel0%

Alpha52%

Alpha52%

[Openclaw Sdk](</nl/gateway/external-apps>), [Openclaw Sdk-API-ontwerp](</nl/gateway/external-apps>), [Protocol](</nl/gateway/protocol>)

Resource-helpers 5 mogelijkheden

Experimenteel17%

Alpha62%

Alpha53%

[Openclaw Sdk](</nl/gateway/external-apps>), [Openclaw Sdk-API-ontwerp](</nl/gateway/external-apps>)

Compatibiliteit 5 mogelijkheden

Experimenteel0%

Alpha54%

Alpha55%

[Openclaw Sdk-API-ontwerp](</nl/gateway/external-apps>), [Typebox](</nl/concepts/typebox>), [Protocol](</nl/gateway/protocol>)

### Platform

Linux Gateway-host - M4 Stabiel - 5 gebieden

Node-runtime wordt aanbevolen, systemd-gebruikersservice is gedocumenteerd en VPS/container-richtlijnen zijn breed.

Dekking Experimenteel - 0%Kwaliteit Beta - 75%Volledigheid Stabiel - 89%Gedeeltelijk - 4

Hostconfiguratie en updates 4 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Index](</nl/install>), [Bijwerken](</nl/install/updating>), [Linux](</nl/platforms/linux>), [Index](</nl/platforms>)

Gateway-runtime en servicebeheer 6 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Index](</nl/gateway>), [Gateway](</nl/cli/gateway>), [Linux](</nl/platforms/linux>), [VPS](</nl/vps>)

Externe toegang en beveiliging 6 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Extern](</nl/gateway/remote>), [Tailscale](</nl/gateway/tailscale>), [Runbook voor blootstelling](</nl/gateway/security/exposure-runbook>), [Authenticatie](</nl/gateway/authentication>), [Geheimen](</nl/gateway/secrets>)

Diagnostiek en herstel 4 mogelijkheden / LTS-ondersteund

Experimenteel0%

Beta75%

Stabiel89%

[Status](</nl/cli/status>), [Logboeken](</nl/cli/logs>), [Doctor](</nl/cli/doctor>), [Diagnostiek](</nl/gateway/diagnostics>), [Index](</nl/gateway>)

Implementatiedoelen 3 mogelijkheden

Experimenteel0%

Beta75%

Stabiel89%

[VPS](</nl/vps>), [Docker](</nl/install/docker>), [Hetzner](</nl/install/hetzner>), [Digitalocean](</nl/install/digitalocean>), [Kubernetes](</nl/install/kubernetes>), [Podman](</nl/install/podman>)

macOS Gateway-host - M4 Stabiel - 7 gebieden

LaunchAgent-servicepad, lokale/externe Gateway-modi, CLI-installatie en app-integratie zijn gedocumenteerd.

Dekking Experimenteel - 0%Kwaliteit Beta - 74%Volledigheid Stabiel - 88%Geen

CLI-installatie 4 mogelijkheden

Experimenteel0%

Beta74%

Stabiel88%

[Macos](</nl/platforms/macos>), [Meegeleverde Gateway](</nl/platforms/mac/bundled-gateway>), [Installatieprogramma](</nl/install/installer>), [Node](</nl/install/node>)

Lokale Gateway-integratie 9 mogelijkheden

Experimenteel0%

Beta74%

Stabiel88%

[Macos](</nl/platforms/macos>), [Meegeleverde Gateway](</nl/platforms/mac/bundled-gateway>), [Extern](</nl/platforms/mac/remote>), [Index](</nl/gateway>), [Gateway](</nl/cli/gateway>), [Bonjour](</nl/gateway/bonjour>)

Externe Gateway-modus 5 mogelijkheden

Experimenteel0%

Beta74%

Stabiel88%

[Extern](</nl/platforms/mac/remote>), [Extern](</nl/gateway/remote>), [Tailscale](</nl/gateway/tailscale>)

Levenscyclus van de Gateway-service 10 mogelijkheden

Experimenteel0%

Beta74%

Stabiel88%

[Macos](</nl/platforms/macos>), [Meegeleverde Gateway](</nl/platforms/mac/bundled-gateway>), [Gateway](</nl/cli/gateway>), [Index](</nl/gateway>), [Bijwerken](</nl/cli/update>), [Bijwerken](</nl/install/updating>), [Verwijderen](</nl/install/uninstall>), [Probleemoplossing](</nl/gateway/troubleshooting>)

Diagnostiek en observeerbaarheid 4 mogelijkheden

Experimenteel0%

Beta74%

Stabiel88%

[Meegeleverde Gateway](</nl/platforms/mac/bundled-gateway>), [Macos](</nl/platforms/macos>), [Gateway](</nl/cli/gateway>), [Doctor](</nl/gateway/doctor>), [Probleemoplossing](</nl/gateway/troubleshooting>)

Machtigingen en native mogelijkheden 4 mogelijkheden

Experimenteel0%

Beta74%

Stabiel88%

[Macos](</nl/platforms/macos>), [Extern](</nl/platforms/mac/remote>)

Profielen en isolatie 5 mogelijkheden

Experimenteel0%

Beta74%

Stabiel88%

[Meerdere Gateways](</nl/gateway/multiple-gateways>), [Index](</nl/gateway>), [Gateway](</nl/cli/gateway>)

Docker- en Podman-hosting - M3 Beta - 4 gebieden

Installatiedocumentatie bestaat en omvat gangbare implementatiepaden. Promoveer nadat terugkerende release-smokecontroles upgrade- en volumegedrag vastleggen.

Dekking Experimenteel - 7%Kwaliteit Beta - 71%Volledigheid Beta - 79%Geen

Containerconfiguratie 6 mogelijkheden

Experimenteel0%

Alpha68%

Beta79%

[Docker](</nl/install/docker>), [Podman](</nl/install/podman>)

Containerbewerkingen 11 mogelijkheden

Experimenteel0%

Alpha68%

Beta79%

[Podman](</nl/install/podman>), [Docker Vm Runtime](</nl/install/docker-vm-runtime>), [Docker](</nl/install/docker>), [Hetzner](</nl/install/hetzner>), [Hostinger](</nl/install/hostinger>)

Imagerelease en validatie 5 mogelijkheden

Experimenteel29%

Beta79%

Beta79%

[Docker](</nl/install/docker>), [Docker Vm Runtime](</nl/install/docker-vm-runtime>), [Volledige releasevalidatie](</nl/reference/full-release-validation>)

Agentsandbox en tooling 3 mogelijkheden

Experimenteel0%

Alpha68%

Beta79%

[Docker](</nl/install/docker>), [Docker Vm Runtime](</nl/install/docker-vm-runtime>)

Windows via WSL2 - M3 Beta - 6 gebieden

Aanbevolen Windows-pad met begeleiding voor systemd/gebruikersservice en documentatie over de boot-keten. Promoveer na herhaalde install/update-scorecards.

Dekking Experimenteel - 6%Kwaliteit Alpha - 69%Volledigheid Beta - 79%Gedeeltelijk - 5

WSL-installatie 6 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa67%

Bèta79%

[Windows](</nl/platforms/windows>), [Aan de slag](</nl/start/getting-started>)

CLI 8 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa67%

Bèta79%

[Windows](</nl/platforms/windows>), [Aan de slag](</nl/start/getting-started>), [Bijwerken](</nl/install/updating>), [Onboard](</nl/cli/onboard>), [Doctor](</nl/cli/doctor>), [Status](</nl/cli/status>), [Logs](</nl/cli/logs>)

Levenscyclus van Gateway-service 10 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa67%

Bèta79%

[Windows](</nl/platforms/windows>), [Index](</nl/gateway>), [Doctor](</nl/gateway/doctor>)

Gateway-toegang en blootstelling 11 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa67%

Bèta79%

[Authenticatie](</nl/gateway/authentication>), [Geheimen](</nl/gateway/secrets>), [Extern](</nl/gateway/remote>), [Runbook voor blootstelling](</nl/gateway/security/exposure-runbook>), [Windows](</nl/platforms/windows>)

Diagnostiek en herstel 6 mogelijkheden / LTS-ondersteund

Experimenteel38%

Bèta79%

Bèta79%

[Windows](</nl/platforms/windows>), [Status](</nl/cli/status>), [Logs](</nl/cli/logs>), [Doctor](</nl/cli/doctor>), [Doctor](</nl/gateway/doctor>)

Browser en Control UI 6 mogelijkheden

Experimenteel0%

Alfa67%

Bèta79%

[Probleemoplossing voor Browser Wsl2 Windows Remote Cdp](</nl/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Browser](</nl/tools/browser>), [Control Ui](</nl/web/control-ui>)

Raspberry Pi en kleine Linux-apparaten - M3 Bèta - 4 gebieden

Platformdocs bestaan en het Gateway-pad is gebaseerd op Linux. Vereist hardwarespecifiek bewijs met release-smoketest om hoger te komen.

Dekking Experimenteel - 0%Kwaliteit Alfa - 67%Volledigheid Bèta - 79%Geen

Installatie en compatibiliteit 12 mogelijkheden

Experimenteel0%

Alpha67%

Beta79%

[Raspberry Pi](</nl/install/raspberry-pi>), [Index](</nl/install>), [Veelgestelde vragen eerste keer uitvoeren](</nl/help/faq-first-run>), [Veelgestelde vragen](</nl/help/faq>), [Linux](</nl/platforms/linux>), [Installatieprogramma](</nl/install/installer>)

Externe toegang en verificatie 9 mogelijkheden

Experimenteel0%

Alpha67%

Beta79%

[Raspberry Pi](</nl/install/raspberry-pi>), [Verificatie](</nl/gateway/authentication>), [Geheimen](</nl/gateway/secrets>), [Koppelen](</nl/gateway/pairing>), [Apparaten](</nl/cli/devices>), [Extern](</nl/gateway/remote>), [Tailscale](</nl/gateway/tailscale>)

Gateway-runtime 10 mogelijkheden

Experimenteel0%

Alpha67%

Beta79%

[Index](</nl/gateway>), [Gateway](</nl/cli/gateway>), [Raspberry Pi](</nl/install/raspberry-pi>), [Linux](</nl/platforms/linux>), [VPS](</nl/vps>)

Prestaties en diagnostiek 5 mogelijkheden

Experimenteel0%

Alpha67%

Beta79%

[Raspberry Pi](</nl/install/raspberry-pi>), [Linux](</nl/platforms/linux>), [Status](</nl/gateway/health>), [Diagnostiek](</nl/gateway/diagnostics>)

macOS-begeleidende app - M3 Beta - 8 gebieden

Uitgebreide menubalk-app, machtigingen, Node-modus, Canvas, spraakactivering, WebChat en externe modus bestaan. Nog steeds snel genoeg in ontwikkeling om Stable te vermijden.

Dekking Experimenteel - 0%Kwaliteit Alpha - 66%Volledigheid Beta - 78%Geen

Canvas 4 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Canvas](</nl/platforms/mac/canvas>), [Macos](</nl/platforms/macos>), [Webchat](</nl/web/webchat>)

Lokale installatie 7 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Meegeleverde Gateway](</nl/platforms/mac/bundled-gateway>), [Macos](</nl/platforms/macos>), [Kindproces](</nl/platforms/mac/child-process>), [Ontwikkelinstallatie](</nl/platforms/mac/dev-setup>)

Status en instellingen 5 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Menubalk](</nl/platforms/mac/menu-bar>), [Pictogram](</nl/platforms/mac/icon>), [Macos](</nl/platforms/macos>), [Status](</nl/platforms/mac/health>), [Logging](</nl/platforms/mac/logging>), [Extern](</nl/platforms/mac/remote>)

Native mogelijkheden 5 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Macos](</nl/platforms/macos>), [Xpc](</nl/platforms/mac/xpc>), [Machtigingen](</nl/platforms/mac/permissions>), [Ondertekening](</nl/platforms/mac/signing>), [Peekaboo](</nl/platforms/mac/peekaboo>)

Externe verbindingen 3 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Extern](</nl/platforms/mac/remote>), [Macos](</nl/platforms/macos>), [Extern](</nl/gateway/remote>)

Spraak en Talk 3 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Voicewake](</nl/platforms/mac/voicewake>), [Spraakoverlay](</nl/platforms/mac/voice-overlay>), [Talk](</nl/nodes/talk>), [Macos](</nl/platforms/macos>)

WebChat 3 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Webchat](</nl/platforms/mac/webchat>), [Macos](</nl/platforms/macos>), [Webchat](</nl/web/webchat>)

Externe WebChat 5 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Webchat](</nl/platforms/mac/webchat>), [Extern](</nl/gateway/remote>), [Extern](</nl/platforms/mac/remote>)

Android-app - M2 Alpha - 7 gebieden

Er bestaat een openbaar Google Play-pad, maar de app-documentatie beschrijft de herbouw nog steeds als uiterst alpha en wijst op werk voor release-hardening.

Dekking Experimenteel - 0%Kwaliteit Alpha - 59%Volledigheid Alpha - 66%Geen

Media vastleggen 1 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Android](</nl/platforms/android>), [Camera](</nl/nodes/camera>)

Mobiele chat 1 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Android](</nl/platforms/android>)

Verbinding instellen 1 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Android](</nl/platforms/android>), [Bonjour](</nl/gateway/bonjour>), [Pairing](</nl/gateway/pairing>)

Distributie 3 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Android](</nl/platforms/android>)

Instellingen 1 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Android](</nl/platforms/android>)

Spraak 1 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Android](</nl/platforms/android>), [Talk](</nl/nodes/talk>)

Apparaatruntime 2 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Android](</nl/platforms/android>), [Probleemoplossing](</nl/nodes/troubleshooting>), [Protocol](</nl/gateway/protocol>)

Native Windows - M2 Alpha - 4 gebieden

Kernflows voor CLI/Gateway werken, maar de docs raden nog steeds WSL2 aan voor de volledige ervaring en vermelden native aandachtspunten.

Dekking Experimenteel - 0%Kwaliteit Alpha - 58%Volledigheid Alpha - 66%Gedeeltelijk - 1

CLI 9 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa54%

Alfa64%

[Index](</nl/install>), [Installatieprogramma](</nl/install/installer>), [Windows](</nl/platforms/windows>), [Aan de slag](</nl/start/getting-started>), [Onboarden](</nl/cli/onboard>)

Gateway-beheer 11 mogelijkheden

Experimenteel0%

Alfa59%

Alfa66%

[Windows](</nl/platforms/windows>), [Index](</nl/gateway>), [Gateway](</nl/cli/gateway>), [Doctor](</nl/cli/doctor>)

Netwerken 4 mogelijkheden

Experimenteel0%

Alfa59%

Alfa66%

[Windows](</nl/platforms/windows>), [Index](</nl/gateway>), [Gateway](</nl/cli/gateway>)

Updates 4 mogelijkheden

Experimenteel0%

Alfa59%

Alfa66%

[Bijwerken](</nl/install/updating>), [CI](</nl/ci>)

Kubernetes-hosting - M2 Alfa - 4 gebieden

Kubernetes-hosting is een afzonderlijk, op Kustomize gebaseerd implementatiepad voor clusters. De huidige score laat een echt minimaal implementatiepad zien, met hiaten rond Kubernetes-specifieke CI, verpakking van ingress/TLS/NetworkPolicy, back-up/herstel en hardening van blootstelling in productie.

Dekking Experimental - 0%Kwaliteit Alpha - 55%Volledigheid Alpha - 61%Geen

Implementatie-instelling 5 mogelijkheden

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</nl/install/kubernetes>), [Index](</nl/install>)

Configuratie en geheimen 5 mogelijkheden

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</nl/install/kubernetes>), [Geheimen](</nl/gateway/secrets>), [Omgeving](</nl/help/environment>)

Toegang en blootstelling 5 mogelijkheden

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</nl/install/kubernetes>), [Authenticatie](</nl/gateway/authentication>), [Extern](</nl/gateway/remote>), [Runbook voor blootstelling](</nl/gateway/security/exposure-runbook>)

Clusterlevenscyclus 5 mogelijkheden

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</nl/install/kubernetes>), [Index](</nl/gateway>)

iOS-app - M1 Experimental - 8 gebieden

Interne preview / super-alpha. TestFlight- en relay-ondersteunde pushflows bestaan, maar er is nog geen openbare distributie.

Dekking experimenteel - 0%Kwaliteit experimenteel - 41%Volledigheid experimenteel - 44%Geen

Media en delen 1 mogelijkheid

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>), [Camera](</nl/nodes/camera>)

Canvas en scherm 1 mogelijkheid

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>), [Canvas](</nl/plugins/reference/canvas>)

Chat en sessies 1 mogelijkheid

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>), [Webchat](</nl/web/webchat>), [Protocol](</nl/gateway/protocol>)

Gateway-installatie en diagnostiek 7 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>), [Koppelen](</nl/channels/pairing>)

Distributie 1 mogelijkheid

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>)

Apparaatopdrachten 2 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>), [Protocol](</nl/gateway/protocol>)

Meldingen en achtergrond 1 mogelijkheid

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>), [Configuratie](</nl/gateway/configuration>)

Spraak 1 mogelijkheid

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>), [Praten](</nl/nodes/talk>)

Nix-installatiepad - M1 experimenteel - 5 gebieden

Optionele installatiestroom. Heeft een duidelijkere ondersteuningstoezegging nodig vóór promotie naar alfa/bèta.

Dekking Experimenteel - 0%Kwaliteit Experimenteel - 41%Volledigheid Experimenteel - 44%Geen

Installatie-overdracht 4 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Nix](</nl/install/nix>), [Index](</nl/install>), [Documentatiemap](</nl/start/docs-directory>)

Plugin-levenscyclus 4 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Plugins beheren](</nl/plugins/manage-plugins>), [Plugin](</nl/tools/plugin>), [Nix](</nl/install/nix>)

Activering en app-UX 7 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Nix](</nl/install/nix>)

Configuratie en status 7 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Nix](</nl/install/nix>), [Instellen](</nl/cli/setup>), [Omgeving](</nl/help/environment>)

Serviceruntime en beveiligingen 8 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Nix](</nl/install/nix>), [Instellen](</nl/cli/setup>), [Doctor](</nl/cli/doctor>), [Bijwerken](</nl/cli/update>)

watchOS-begeleidende oppervlakken - M1 Experimenteel - 5 gebieden

Broncode bevat Watch-app-/extensieoppervlakken; openbare documentatie presenteert dit nog niet als gebruikersfunctie.

Dekking Experimenteel - 0%Kwaliteit Experimenteel - 41%Volledigheid Experimenteel - 44%Geen

Levering en herstel 7 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>)

Uitvoeringsgoedkeuringen 3 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Uitvoeringsgoedkeuringen](</nl/tools/exec-approvals>), [Ios](</nl/platforms/ios>)

Distributie en ondersteuning 6 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>)

Meldingen en antwoorden 7 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>)

Gebruikersinterface van de Watch-app 3 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Ios](</nl/platforms/ios>)

Linux-begeleidende app - M0 Gepland - 5 gebieden

Documentatie vermeldt dat native Linux-begeleidende apps gepland zijn; Gateway is vandaag het ondersteunde Linux-pad.

Dekking Experimenteel - 0%Kwaliteit Experimenteel - 19%Volledigheid Experimenteel - 21%Geen

App-distributie 3 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Linux](</nl/platforms/linux>), [Index](</nl/platforms>), [Index](</nl/install>)

Gateway-connectiviteit 4 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Linux](</nl/platforms/linux>), [Index](</nl/gateway>), [Koppelen](</nl/gateway/pairing>), [Op afstand](</nl/gateway/remote>)

Chat en sessies 3 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Linux](</nl/platforms/linux>), [Protocol](</nl/gateway/protocol>), [Webchat](</nl/web/webchat>)

Desktopmogelijkheden 9 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Linux](</nl/platforms/linux>), [Exec-goedkeuringen](</nl/tools/exec-approvals>), [Geheimen](</nl/gateway/secrets>), [Index](</nl/nodes>), [Exec](</nl/tools/exec>), [Praten](</nl/nodes/talk>), [Camera](</nl/nodes/camera>)

Status en diagnostiek 7 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Linux](</nl/platforms/linux>), [Openclaw](</nl/start/openclaw>), [Doctor](</nl/gateway/doctor>)

Native Windows-begeleidende app - M0 Gepland - 5 gebieden

Alleen gepland.

Dekking Experimenteel - 0%Kwaliteit Experimenteel - 19%Volledigheid Experimenteel - 21%Geen

Installatie en updates 4 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Windows](</nl/platforms/windows>), [Index](</nl/install>)

Gateway-verbinding 3 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Windows](</nl/platforms/windows>), [Index](</nl/gateway>), [Koppelen](</nl/gateway/pairing>), [Extern](</nl/gateway/remote>)

Chatsessies 2 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Windows](</nl/platforms/windows>), [Protocol](</nl/gateway/protocol>)

Status en herstel 5 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Windows](</nl/platforms/windows>), [Doctor](</nl/gateway/doctor>), [Index](</nl/gateway>)

Desktoptools en machtigingen 10 mogelijkheden

Experimenteel0%

Experimenteel19%

Experimenteel21%

[Windows](</nl/platforms/windows>), [Index](</nl/nodes>), [Exec](</nl/tools/exec>), [Exec-goedkeuringen](</nl/tools/exec-approvals>), [Index](</nl/gateway/security>)

### Kanaal

Discord - M4 Stabiel - 6 gebieden

Diepgaande docs en brede functiedekking. Spraak-/delegatiepaden moeten afzonderlijk beoordeeld blijven als bèta/alfa.

Dekking Experimenteel - 0%Kwaliteit Bèta - 73%Volledigheid Stabiel - 87%Gedeeltelijk - 4

Kanaalconfiguratie en -beheer 10 capabilities / LTS-ondersteund

Experimenteel0%

Bèta73%

Stabiel87%

[Discord](</nl/channels/discord>), [Discord](</nl/plugins/reference/discord>), [Fly](</nl/install/fly>), [Slash Commands](</nl/tools/slash-commands>), [Health](</nl/gateway/health>), [Kanalen](</nl/cli/channels>), [Configuratiekanalen](</nl/gateway/config-channels>)

Toegang en identiteit 6 capabilities / LTS-ondersteund

Experimenteel0%

Bèta73%

Stabiel87%

[Discord](</nl/channels/discord>), [Koppelen](</nl/channels/pairing>), [Toegangsgroepen](</nl/channels/access-groups>), [Groepen](</nl/channels/groups>)

Gespreksroutering en aflevering 12 capabilities / LTS-ondersteund

Experimenteel0%

Bèta73%

Stabiel87%

[Discord](</nl/channels/discord>), [Kanaalroutering](</nl/channels/channel-routing>), [Groepen](</nl/channels/groups>), [Toegangsgroepen](</nl/channels/access-groups>), [ACP-agenten](</nl/tools/acp-agents>), [Subagenten](</nl/tools/subagents>)

Media en rich content 1 capability / LTS-ondersteund

Experimenteel0%

Bèta73%

Stabiel87%

[Discord](</nl/channels/discord>)

Native bedieningselementen en goedkeuringen 5 capabilities

Experimenteel0%

Bèta73%

Stabiel87%

[Discord](</nl/channels/discord>), [Slash Commands](</nl/tools/slash-commands>)

Realtime spraak en gesprekken 5 capabilities

Experimenteel0%

Bèta73%

Stabiel87%

[Discord](</nl/channels/discord>), [Openai](</nl/providers/openai>), [Elevenlabs](</nl/providers/elevenlabs>), [QA-E2E-automatisering](</nl/concepts/qa-e2e-automation>), [Configuratiekanalen](</nl/gateway/config-channels>)

Telegram - M3 Bèta - 5 gebieden

Het kernkanaal is volwassen genoeg voor regelmatig gebruik, maar UX met hoge variatie en randgevallen rond media vereisen terugkerend scenariobewijs.

Dekking Experimenteel - 0%Kwaliteit Alfa - 68%Volledigheid Bèta - 78%Volledig - 5

Kanaalinstelling en -beheer 10 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa66%

Bèta78%

[Telegram](</nl/channels/telegram>), [Configuratiekanalen](</nl/gateway/config-channels>), [Kanalen](</nl/cli/channels>)

Toegang en identiteit 10 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa66%

Bèta78%

[Telegram](</nl/channels/telegram>), [Koppelen](</nl/channels/pairing>), [Toegangsgroepen](</nl/channels/access-groups>), [Groepen](</nl/channels/groups>), [Multi Agent](</nl/concepts/multi-agent>)

Gespreksroutering en levering 1 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa66%

Bèta78%

[Telegram](</nl/channels/telegram>), [Groepen](</nl/channels/groups>), [Multi Agent](</nl/concepts/multi-agent>)

Media en rijke content 1 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa66%

Bèta78%

[Telegram](</nl/channels/telegram>), [Locatie](</nl/channels/location>)

Native bedieningselementen en goedkeuringen 9 mogelijkheden / LTS-ondersteund

Experimenteel0%

Bèta77%

Bèta79%

[Telegram](</nl/channels/telegram>), [Exec-goedkeuringen](</nl/tools/exec-approvals>), [Reacties](</nl/tools/reactions>)

Slack - M3 Bèta - 5 gebieden

Volwaardige kanaaldocumentatie en routeringsoppervlak. Heeft scorekaarten nodig voor scenario's voor workspace-installatie/beheer.

Dekking Experimenteel - 0%Kwaliteit Alfa - 66%Volledigheid Bèta - 78%Volledig - 5

Kanaalinstellingen en -activiteiten 10 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa66%

Beta78%

[Slack](</nl/channels/slack>), [Geheimen](</nl/gateway/secrets>), [QA E2E-automatisering](</nl/concepts/qa-e2e-automation>), [Probleemoplossing](</nl/channels/troubleshooting>)

Toegang en identiteit 1 mogelijkheid / LTS-ondersteund

Experimenteel0%

Alfa66%

Beta78%

[Slack](</nl/channels/slack>), [Koppelen](</nl/channels/pairing>)

Gespreksroutering en aflevering 5 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa66%

Beta78%

[Slack](</nl/channels/slack>), [Bescherming tegen botlussen](</nl/channels/bot-loop-protection>), [Koppelen](</nl/channels/pairing>)

Media en rijke content 1 mogelijkheid / LTS-ondersteund

Experimenteel0%

Alfa66%

Beta78%

[Slack](</nl/channels/slack>), [QA E2E-automatisering](</nl/concepts/qa-e2e-automation>)

Native bedieningselementen en goedkeuringen 8 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa66%

Beta78%

[Slack](</nl/channels/slack>), [Slash-opdrachten](</nl/tools/slash-commands>), [Exec-goedkeuringen](</nl/tools/exec-approvals>)

iMessage en BlueBubbles - M3 Beta - 5 gebieden

Ondersteunde iMessage draait via imsg op een macOS Messages-host waarop is ingelogd; oudere BlueBubbles-configuraties vereisen migratie. Houd macOS-machtigingen, SSH-wrapper, SIP/private API en migratiekanttekeningen zichtbaar.

Dekking Experimenteel - 0%Kwaliteit Alfa - 66%Volledigheid Beta - 78%Geen

Kanaalconfiguratie en -beheer 11 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</nl/announcements/bluebubbles-imessage>), [Imessage From Bluebubbles](</nl/channels/imessage-from-bluebubbles>), [Kanalen configureren](</nl/gateway/config-channels>), [Imessage](</nl/channels/imessage>)

Toegang en identiteit 6 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Imessage](</nl/channels/imessage>), [Imessage From Bluebubbles](</nl/channels/imessage-from-bluebubbles>), [Kanalen configureren](</nl/gateway/config-channels>)

Gespreksroutering en bezorging 4 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Imessage](</nl/channels/imessage>)

Media en rijke content 7 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Imessage](</nl/channels/imessage>), [Imessage From Bluebubbles](</nl/channels/imessage-from-bluebubbles>), [Kanalen configureren](</nl/gateway/config-channels>)

Native bedieningselementen en goedkeuringen 3 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Imessage](</nl/channels/imessage>)

WhatsApp - M3 Beta - 5 areas

Het kernpad is belangrijk en gedocumenteerd; volatiliteit in upstream Baileys/sessies houdt het onder Stable.

Dekking Experimenteel - 0%Kwaliteit Alpha - 66%Volledigheid Beta - 78%Geen

Kanaalconfiguratie en -beheer 5 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[WhatsApp](</nl/channels/whatsapp>), [Kanalen configureren](</nl/gateway/config-channels>), [WhatsApp](</nl/plugins/reference/whatsapp>), [QA E2E-automatisering](</nl/concepts/qa-e2e-automation>), [Doctor](</nl/gateway/doctor>)

Toegang en identiteit 7 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[WhatsApp](</nl/channels/whatsapp>), [Kanalen configureren](</nl/gateway/config-channels>), [QA E2E-automatisering](</nl/concepts/qa-e2e-automation>), [Koppeling](</nl/channels/pairing>)

Gespreksroutering en bezorging 4 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[WhatsApp](</nl/channels/whatsapp>), [Groepsberichten](</nl/channels/group-messages>)

Media en rijke content 2 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[WhatsApp](</nl/channels/whatsapp>)

Native besturingselementen en goedkeuringen 2 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[WhatsApp](</nl/channels/whatsapp>)

Matrix - M2 Alpha - 6 gebieden

Ondersteund via gebundelde Plugin. Vereist scorecards voor bridge, auth en room-levenscyclus.

Dekking experimenteel - 0%Kwaliteit Alpha - 60%Volledigheid Alpha - 67%Geen

Kanaalconfiguratie en bewerkingen 5 mogelijkheden

Experimenteel0%

Alfa60%

Alfa67%

[Matrix](</nl/channels/matrix>), [Matrix-migratie](</nl/channels/matrix-migration>)

Toegang en identiteit 7 mogelijkheden

Experimenteel0%

Alfa60%

Alfa67%

[Matrix](</nl/channels/matrix>), [Groepen](</nl/channels/groups>), [Bescherming tegen botloops](</nl/channels/bot-loop-protection>)

Gespreksroutering en bezorging 1 mogelijkheid

Experimenteel0%

Alfa60%

Alfa67%

[Matrix](</nl/channels/matrix>)

Media en rijke content 1 mogelijkheid

Experimenteel0%

Alfa60%

Alfa67%

[Matrix](</nl/channels/matrix>)

Native bedieningselementen en goedkeuringen 6 mogelijkheden

Experimenteel0%

Alfa60%

Alfa67%

[Matrix](</nl/channels/matrix>)

Versleuteling en verificatie 3 mogelijkheden

Experimenteel0%

Alfa60%

Alfa67%

[Matrix](</nl/channels/matrix>), [Matrix-migratie](</nl/channels/matrix-migration>)

Google Chat - M2 Alfa - 5 gebieden

Gedocumenteerd kanaal, maar enterprise-/beheerdersconfiguratie verhoogt het maturiteitsrisico.

Dekking Experimenteel - 0%Kwaliteit Alfa - 59%Volledigheid Alfa - 66%Geen

Kanaalconfiguratie en -beheer 16 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Google Chat](</nl/channels/googlechat>), [Google Chat](</nl/plugins/reference/googlechat>), [Config-kanalen](</nl/gateway/config-channels>), [Wizard-CLI-referentie](</nl/start/wizard-cli-reference>), [Geheimen](</nl/gateway/secrets>), [Secretref-referentiegegevensoppervlak](</nl/reference/secretref-credential-surface>), [Gezondheid](</nl/gateway/health>), [Plugin-inventaris](</nl/plugins/plugin-inventory>), [Index](</nl/channels>)

Toegang en identiteit 11 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Google Chat](</nl/channels/googlechat>), [Koppelen](</nl/channels/pairing>), [Toegangsgroepen](</nl/channels/access-groups>), [Config-kanalen](</nl/gateway/config-channels>), [Botlusbescherming](</nl/channels/bot-loop-protection>), [Kanaalroutering](</nl/channels/channel-routing>)

Gespreksroutering en bezorging 1 mogelijkheid

Experimenteel0%

Alpha59%

Alpha66%

[Google Chat](</nl/channels/googlechat>), [Botlusbescherming](</nl/channels/bot-loop-protection>), [Toegangsgroepen](</nl/channels/access-groups>), [Kanaalroutering](</nl/channels/channel-routing>)

Media en rijke content 1 mogelijkheid

Experimenteel0%

Alpha59%

Alpha66%

[Google Chat](</nl/channels/googlechat>), [Bericht](</nl/cli/message>), [Mediabegrip](</nl/nodes/media-understanding>), [Secretref-referentiegegevensoppervlak](</nl/reference/secretref-credential-surface>)

Systeemeigen bedieningselementen en goedkeuringen 16 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Google Chat](</nl/channels/googlechat>), [Bericht](</nl/cli/message>), [Mediabegrip](</nl/nodes/media-understanding>), [Secretref-referentiegegevensoppervlak](</nl/reference/secretref-credential-surface>), [Reacties](</nl/tools/reactions>), [Slash-opdrachten](</nl/tools/slash-commands>), [Config-agenten](</nl/gateway/config-agents>), [Berichtlevenscyclus-refactor](</nl/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 gebieden

Enterprise-auth-/beheerflows hebben expliciet scenariobewijs nodig.

Dekking Experimenteel - 0%Kwaliteit Alpha - 59%Volledigheid Alpha - 66%Geen

Kanaalinstelling en -beheer 9 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Msteams](</nl/channels/msteams>), [Msteams](</nl/plugins/reference/msteams>), [Configuratiekanalen](</nl/gateway/config-channels>), [Status](</nl/gateway/health>)

Toegang en identiteit 9 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Msteams](</nl/channels/msteams>), [Koppelen](</nl/channels/pairing>), [Toegangsgroepen](</nl/channels/access-groups>)

Gespreksroutering en levering 5 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Msteams](</nl/channels/msteams>), [Groepen](</nl/channels/groups>), [Kanaalroutering](</nl/channels/channel-routing>)

Media en rijke content 5 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Msteams](</nl/channels/msteams>)

Systeemeigen bediening en goedkeuringen 5 mogelijkheden

Experimenteel0%

Alpha59%

Alpha66%

[Msteams](</nl/channels/msteams>), [Geavanceerde uitvoeringsgoedkeuringen](</nl/tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 gebieden

Ondersteunde kanaaldocumentatie bestaat; sterkere installatie- en herverbindingsbewijzen zijn nodig.

Dekking Experimenteel - 0%Kwaliteit Alpha - 59%Volledigheid Alpha - 66%Geen

Kanaalinstelling en -beheer 7 mogelijkheden

Experimenteel0%

Alfa59%

Alfa66%

[Signal](</nl/channels/signal>), [Signal](</nl/plugins/reference/signal>)

Toegang en identiteit 6 mogelijkheden

Experimenteel0%

Alfa59%

Alfa66%

[Signal](</nl/channels/signal>)

Gespreksroutering en aflevering 1 mogelijkheid

Experimenteel0%

Alfa59%

Alfa66%

[Signal](</nl/channels/signal>)

Media en rijke inhoud 7 mogelijkheden

Experimenteel0%

Alfa59%

Alfa66%

[Signal](</nl/channels/signal>)

Native bedieningselementen en goedkeuringen 3 mogelijkheden

Experimenteel0%

Alfa59%

Alfa66%

[Signal](</nl/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, regionale kanalen - M2 Alfa - 4 gebieden

Belangrijke regionale dekking, maar het niveau van publieke ondersteuning moet per accounttype, upstream-goedkeuring en maintainer-bewijs worden afgestemd.

Dekking experimenteel - 0%Kwaliteit Alfa - 55%Volledigheid Alfa - 58%Geen

Kanaalinstelling en -beheer 6 mogelijkheden

Experimenteel0%

Alpha61%

Alpha68%

[Index](</nl/channels>), [Koppelen](</nl/channels/pairing>), [Feishu](</nl/plugins/reference/feishu>), [Interne architectuurdetails](</nl/plugins/architecture-internals>)

Toegang en identiteit 1 mogelijkheid

Experimenteel0%

Alpha53%

Alpha54%

Geen gekoppelde documentatie

Gespreksroutering en levering 1 mogelijkheid

Experimenteel0%

Alpha53%

Alpha54%

Geen gekoppelde documentatie

Media en rijke content 1 mogelijkheid

Experimenteel0%

Alpha53%

Alpha54%

Geen gekoppelde documentatie

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 gebieden

Ondersteunde oppervlakken bestaan, maar de volwassenheid varieert waarschijnlijk per upstream en maintainerdekking. Later afzonderlijk scoren.

Dekking Experimenteel - 0%Kwaliteit Alpha - 53%Volledigheid Alpha - 54%Geen

Kanaalinstelling en -operaties 1 mogelijkheden

Experimenteel0%

Alfa53%

Alfa54%

Geen gekoppelde docs

Toegang en identiteit 1 mogelijkheden

Experimenteel0%

Alfa53%

Alfa54%

Geen gekoppelde docs

Gespreksroutering en bezorging 1 mogelijkheden

Experimenteel0%

Alfa53%

Alfa54%

Geen gekoppelde docs

Media en rijke content 1 mogelijkheden

Experimenteel0%

Alfa53%

Alfa54%

Geen gekoppelde docs

Spraakoproepkanaal - M1 Experimenteel - 5 gebieden

Optioneel/Plugin-pad met complex realtimegedrag. Heeft een scenarioscorekaart nodig vóór publieke bèta.

Dekking Experimenteel - 0%Kwaliteit Experimenteel - 41%Volledigheid Experimenteel - 44%Geen

Kanaalinstelling en bewerkingen 2 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Voicecall](</nl/cli/voicecall>), [Spraakoproep](</nl/plugins/voice-call>), [Protocol](</nl/gateway/protocol>)

Toegang en identiteit 1 mogelijkheid

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Spraakoproep](</nl/plugins/voice-call>), [Voicecall](</nl/cli/voicecall>)

Gespreksroutering en levering 1 mogelijkheid

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Spraakoproep](</nl/plugins/voice-call>)

Media en rijke content 2 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Spraakoproep](</nl/plugins/voice-call>), [Plugin-inventaris](</nl/plugins/plugin-inventory>)

Realtime spraak en oproepen 2 mogelijkheden

Experimenteel0%

Experimenteel41%

Experimenteel44%

[Spraakoproep](</nl/plugins/voice-call>)

### Provider en tool

Browserautomatisering, exec- en sandboxtools - M3 Beta - 3 gebieden

Kerntools zijn gedocumenteerd, maar hostbeveiliging en de gebruikservaring voor machtigingen moeten actief in de scorecardbeoordeling blijven.

Dekking Experimenteel - 21%Kwaliteit Beta - 75%Volledigheid Beta - 79%Gedeeltelijk - 2

Browserautomatisering 8 mogelijkheden

Experimenteel13%

Bèta79%

Bèta79%

[Browserbediening](</nl/tools/browser-control>), [Testen](</nl/help/testing>), [Browser](</nl/tools/browser>), [Index](</nl/gateway/security>), [Auditcontroles](</nl/gateway/security/audit-checks>)

Toolaanroep en uitvoering 6 mogelijkheden / LTS-ondersteund

Alfa50%

Bèta79%

Bèta79%

[Exec](</nl/tools/exec>), [Achtergrondproces](</nl/gateway/background-process>), [Tools HTTP-API aanroepen](</nl/gateway/tools-invoke-http-api>), [Operatorbereiken](</nl/gateway/operator-scopes>), [Protocol](</nl/gateway/protocol>), [Exec-goedkeuringen](</nl/tools/exec-approvals>), [Geavanceerde Exec-goedkeuringen](</nl/tools/exec-approvals-advanced>), [Verhoogd](</nl/tools/elevated>)

Sandbox en toolbeleid 6 mogelijkheden / LTS-ondersteund

Experimenteel0%

Alfa68%

Bèta79%

[Sandboxing](</nl/gateway/sandboxing>), [Sandbox versus toolbeleid versus verhoogd](</nl/gateway/sandbox-vs-tool-policy-vs-elevated>), [Sandboxtools voor meerdere agents](</nl/tools/multi-agent-sandbox-tools>), [Codex-harnessreferentie](</nl/plugins/codex-harness-reference>), [Configuratietools](</nl/gateway/config-tools>)

OpenAI- en Codex-providerpad - M3 Bèta - 5 gebieden

Uitgebreide documentatie, OAuth-/abonnementspad, realtime spraak, afbeeldingen en compatibiliteitsgedrag. Providerwijzigingen houden dit uit Stabiel zonder bewijs uit de release-scorecard.

Dekking Experimenteel - 26%Kwaliteit Bèta - 74%Volledigheid Bèta - 79%Gedeeltelijk - 3

Model en Auth 6 mogelijkheden / LTS-ondersteund

Experimenteel44%

Beta79%

Beta79%

[Openai](</nl/providers/openai>), [Codex Harness](</nl/plugins/codex-harness>), [Modellen](</nl/concepts/models>), [Oauth](</nl/concepts/oauth>), [Codex Harness-referentie](</nl/plugins/codex-harness-reference>), [Auth-monitoring](</nl/gateway/authentication>)

Responses- en toolcompatibiliteit 4 mogelijkheden / LTS-ondersteund

Experimenteel40%

Beta79%

Beta79%

[Openai](</nl/providers/openai>), [Openresponses HTTP-API](</nl/gateway/openresponses-http-api>), [Openai HTTP-API](</nl/gateway/openai-http-api>), [Codex Native Plugins](</nl/plugins/codex-native-plugins>)

Native Codex Harness 2 mogelijkheden / LTS-ondersteund

Experimenteel44%

Beta79%

Beta79%

[Codex Harness](</nl/plugins/codex-harness>), [Codex Harness-runtime](</nl/plugins/codex-harness-runtime>), [Codex Harness-referentie](</nl/plugins/codex-harness-reference>), [Codex Native Plugins](</nl/plugins/codex-native-plugins>)

Afbeeldings- en multimodale invoer 2 mogelijkheden

Experimenteel0%

Alpha67%

Beta79%

[Openai](</nl/providers/openai>), [Afbeeldingen genereren](</nl/tools/image-generation>), [Afbeeldingen](</nl/nodes/images>)

Spraak en realtime-audio 2 mogelijkheden

Experimenteel0%

Alpha67%

Beta79%

[Openai](</nl/providers/openai>), [Discord](</nl/channels/discord>), [Spraakoproep](</nl/plugins/voice-call>)

Webzoektools - M3 Beta - 4 gebieden

Er bestaan meerdere providers en docs. Vereist quota-/fout-/SSRF-bewijs per providerfamilie.

Dekking Experimenteel - 9%Kwaliteit Beta - 74%Volledigheid Beta - 79%Geen

Zoekproviders 19 mogelijkheden

Experimenteel11%

Bèta79%

Bèta79%

[Web](</nl/tools/web>), [Brave Search](</nl/tools/brave-search>), [Tavily](</nl/tools/tavily>), [Exa Search](</nl/tools/exa-search>), [Firecrawl](</nl/tools/firecrawl>), [Perplexity Search](</nl/tools/perplexity-search>), [Duckduckgo Search](</nl/tools/duckduckgo-search>), [Searxng Search](</nl/tools/searxng-search>), [Gemini Search](</nl/tools/gemini-search>), [Grok Search](</nl/tools/grok-search>), [Kimi Search](</nl/tools/kimi-search>), [Minimax Search](</nl/tools/minimax-search>), [Ollama Search](</nl/tools/ollama-search>), [Sdk-subpaden](</nl/plugins/sdk-subpaths>), [Sdk-overzicht](</nl/plugins/sdk-overview>), [Manifest](</nl/plugins/manifest>)

Configuratie en diagnostiek 9 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Web](</nl/tools/web>), [Web Fetch](</nl/tools/web-fetch>), [Veelgestelde vragen](</nl/help/faq>), [API-gebruikskosten](</nl/reference/api-usage-costs>), [Brave Search](</nl/tools/brave-search>), [Perplexity Search](</nl/tools/perplexity-search>), [Tavily](</nl/tools/tavily>), [Firecrawl](</nl/tools/firecrawl>)

Netwerkveiligheid 4 mogelijkheden

Experimenteel0%

Alfa68%

Bèta79%

[Web](</nl/tools/web>), [Web Fetch](</nl/tools/web-fetch>), [Firecrawl](</nl/tools/firecrawl>), [Searxng Search](</nl/tools/searxng-search>)

Beschikbaarheid van tools en ophalen 11 mogelijkheden

Experimenteel25%

Bèta79%

Bèta79%

[Configuratietools](</nl/gateway/config-tools>), [Web Fetch](</nl/tools/web-fetch>), [Web](</nl/tools/web>), [Veelgestelde vragen](</nl/help/faq>)

Anthropic-providerpad - M3 Bèta - 5 gebieden

Eersteklas modelprovider. Vereist terugkerend scenariobewijs voor authenticatie, catalogus en tool-calls.

Dekking Experimenteel - 0%Kwaliteit Bèta - 71%Volledigheid Bèta - 78%Geen

Providerauthenticatie en herstel 9 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Anthropic](</nl/providers/anthropic>), [Doctor](</nl/gateway/doctor>), [Configuratievoorbeelden](</nl/gateway/configuration-examples>), [Probleemoplossing](</nl/gateway/troubleshooting>), [Promptcaching](</nl/reference/prompt-caching>)

Model- en runtime-selectie 10 mogelijkheden

Experimenteel0%

Beta78%

Beta79%

[Anthropic](</nl/providers/anthropic>), [Agents configureren](</nl/gateway/config-agents>), [Modellen](</nl/concepts/models>), [CLI-backends](</nl/gateway/cli-backends>)

Aanvraagtransport en beurtsemantiek 10 mogelijkheden

Experimenteel0%

Beta77%

Beta79%

[Anthropic](</nl/providers/anthropic>), [Promptcaching](</nl/reference/prompt-caching>), [Probleemoplossing](</nl/gateway/troubleshooting>), [CLI-backends](</nl/gateway/cli-backends>), [Modelproviders](</nl/concepts/model-providers>)

Promptcache en context 5 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Anthropic](</nl/providers/anthropic>), [Promptcaching](</nl/reference/prompt-caching>), [Probleemoplossing](</nl/gateway/troubleshooting>), [Heartbeat](</nl/gateway/heartbeat>)

Media-invoer 4 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Anthropic](</nl/providers/anthropic>), [Agents configureren](</nl/gateway/config-agents>)

Google-providerpad - M3 Beta - 5 gebieden

Eersteklas provider met model- en realtime-oppervlakken. Heeft aparte Live/Talk-score nodig.

Dekking Experimenteel - 0%Kwaliteit Alpha - 66%Volledigheid Beta - 78%Geen

Providerinstellingen en referenties 10 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Google](</nl/providers/google>), [Modelproviders](</nl/concepts/model-providers>)

Modelroutering en eindpunten 10 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Google](</nl/providers/google>), [Modelproviders](</nl/concepts/model-providers>), [Google](</nl/plugins/reference/google>), [Gemini Search](</nl/tools/gemini-search>)

Directe Gemini-runtime 9 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Google](</nl/providers/google>), [Modelproviders](</nl/concepts/model-providers>), [Veelgestelde vragen over modellen](</nl/help/faq-models>), [Live testen](</nl/help/testing-live>)

Media, zoeken en realtime 10 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Google](</nl/plugins/reference/google>), [Google](</nl/providers/google>)

Promptcaching 5 mogelijkheden

Experimenteel0%

Alfa66%

Bèta78%

[Promptcaching](</nl/reference/prompt-caching>), [Google](</nl/providers/google>), [Modelproviders](</nl/concepts/model-providers>), [Tokengebruik](</nl/reference/token-use>)

OpenRouter-providerpad - M3 Bèta - 4 gebieden

Het uniforme providerpad is gedocumenteerd en waardevol, maar modelspecifiek gedrag varieert.

Dekking Experimenteel - 0%Kwaliteit Alfa - 66%Volledigheid Bèta - 78%Geen

Providerconfiguratie en authenticatie 14 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Openrouter](</nl/providers/openrouter>), [Modelproviders](</nl/concepts/model-providers>), [Configureren](</nl/cli/configure>), [Authenticatie](</nl/gateway/authentication>), [Omgeving](</nl/help/environment>), [Modellen](</nl/cli/models>), [Modellen](</nl/concepts/models>)

Chatruntime en normalisatie 15 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Openrouter](</nl/providers/openrouter>), [Modelproviders](</nl/concepts/model-providers>), [Promptcaching](</nl/reference/prompt-caching>)

Providerherstel en diagnostiek 5 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Modelfailover](</nl/concepts/model-failover>), [Openrouter](</nl/providers/openrouter>), [Modellen](</nl/cli/models>)

Mediageneratie en spraak 7 mogelijkheden

Experimenteel0%

Alpha66%

Beta78%

[Openrouter](</nl/providers/openrouter>), [Afbeeldingsgeneratie](</nl/tools/image-generation>), [Muziekgeneratie](</nl/tools/music-generation>), [Mediaoverzicht](</nl/tools/media-overview>), [Videogeneratie](</nl/tools/video-generation>), [Tts](</nl/tools/tts>)

Tools voor afbeeldings-, video- en muziekgeneratie - M2 Alpha - 5 gebieden

Mogelijkheid bestaat bij meerdere providers, maar kwaliteit, latentie en parametercompatibiliteit verschillen te veel voor beta zonder bewijs per provider.

Dekking Experimenteel - 0%Kwaliteit Alpha - 61%Volledigheid Alpha - 68%Geen

Mediaroutering en -ontdekking 4 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Configuratie-agents](</nl/gateway/config-agents>), [Afbeeldingsgeneratie](</nl/tools/image-generation>), [Videogeneratie](</nl/tools/video-generation>), [Muziekgeneratie](</nl/tools/music-generation>)

Taaklevenscyclus en levering 12 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Mediaoverzicht](</nl/tools/media-overview>), [Afbeeldingsgeneratie](</nl/tools/image-generation>), [Videogeneratie](</nl/tools/video-generation>), [Muziekgeneratie](</nl/tools/music-generation>)

Afbeeldingsgeneratie 9 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Afbeeldingsgeneratie](</nl/tools/image-generation>), [Infer](</nl/cli/infer>), [Mediaoverzicht](</nl/tools/media-overview>)

Videogeneratie 11 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Videogeneratie](</nl/tools/video-generation>), [Runway](</nl/providers/runway>), [Pixverse](</nl/providers/pixverse>), [Fal](</nl/providers/fal>), [Openrouter](</nl/providers/openrouter>)

Muziekgeneratie 6 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Muziekgeneratie](</nl/tools/music-generation>)

Lokale modelproviders: Ollama, vLLM, SGLang, LM Studio - M2 Alfa - 5 gebieden

Bruikbaar en gedocumenteerd, maar de variatie tussen omgevingen is groot.

Dekking Experimenteel - 0%Kwaliteit Alfa - 61%Volledigheid Alfa - 68%Geen

Providerconfiguratie, levenscyclus en diagnostiek 12 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Lokale modellen](</nl/gateway/local-models>), [Lmstudio](</nl/providers/lmstudio>), [Ollama](</nl/providers/ollama>), [Vllm](</nl/providers/vllm>), [Lokale modelservices](</nl/gateway/local-model-services>), [Configuratie van agents](</nl/gateway/config-agents>), [Probleemoplossing](</nl/gateway/troubleshooting>), [Diagnose](</nl/gateway/doctor>)

Native providerplugins 10 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Ollama](</nl/providers/ollama>), [Lmstudio](</nl/providers/lmstudio>)

Compatibiliteit met OpenAI-compatibele runtime 8 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Vllm](</nl/providers/vllm>), [Sglang](</nl/providers/sglang>), [Lokale modellen](</nl/gateway/local-models>), [Lmstudio](</nl/providers/lmstudio>)

Lokaal geheugen en embeddings 5 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Geheugen](</nl/concepts/memory>), [Diagnose](</nl/gateway/doctor>)

Netwerkveiligheid en promptbesturing 2 mogelijkheden

Experimenteel0%

Alfa61%

Alfa68%

[Index](</nl/gateway/security>), [Configuratietools](</nl/gateway/config-tools>), [Lokale modellen](</nl/gateway/local-models>)

Long-tail gehoste providers - M2 Alfa - 3 gebieden

Er bestaan veel docs-/referentiepagina's; de score moet worden gegenereerd op basis van providermetadata plus dekking door live smoke-tests.

Dekking Experimenteel - 0%Kwaliteit Alfa - 61%Volledigheid Alfa - 68%Geen

Gehoste LLM-providers 12 capaciteiten

Experimenteel0%

Alfa61%

Alfa68%

[Index](</nl/providers>), [Modelproviders](</nl/concepts/model-providers>), [Live testen](</nl/help/testing-live>), [Onboarden](</nl/cli/onboard>)

Gehoste mediaproviders 8 capaciteiten

Experimenteel0%

Alfa61%

Alfa68%

[Manifest](</nl/plugins/manifest>), [Live testen](</nl/help/testing-live>), [Index](</nl/providers>)

Provideroperaties 12 capaciteiten

Experimenteel0%

Alfa61%

Alfa68%

[Index](</nl/providers>), [Modelproviders](</nl/concepts/model-providers>), [Manifest](</nl/plugins/manifest>), [Live testen](</nl/help/testing-live>), [Modellen](</nl/cli/models>)

Was this useful?YesNo

Open issue