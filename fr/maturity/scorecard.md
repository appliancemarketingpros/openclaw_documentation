---
title: Tableau de score de maturité
source_url: https://docs.openclaw.ai/fr/maturity/scorecard
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Tableau de maturité

préparation à la publication - générée à partir de la taxonomie + des preuves QA

Une vue pratique de ce qui est prêt, de ce qui est prouvé et de ce qui nécessite encore du travail.

50 surfaces - 281 domaines de capacité - couverture déterministe, avec qualité et exhaustivité examinées par des humains.

Parcourir les surfaces / Examiner les preuves QA / [Lire la taxonomie](</fr/maturity/taxonomy>)

## À quoi sert cette page

Utilisez cette page pour répondre à une question : quelles surfaces OpenClaw sont des choix crédibles pour une version, et quelles preuves étayent ce jugement ? La couverture provient de preuves QA déterministes ; la qualité et l’exhaustivité sont maintenues sous forme de scores de maturité examinés.

## En un coup d’œil

67% Score de maturité

Alpha Qualité + exhaustivité Couverture Expérimental - 4% Qualité Alpha - 63% Exhaustivité Bêta - 70%

La couverture est délibérément guidée par les preuves : un domaine ne devient pas « prêt » simplement parce que l’implémentation existe. Ce n’est pas une entrée du score de maturité, mais OpenClaw vise à maintenir la couverture de bout en bout au-dessus de 90 % pour les fonctionnalités matures de niveau Stable ou supérieur au fil du temps.

## Plages de score

Expérimental0-50%

Alpha50-70%

Bêta70-80%

Stable80-95%

Clawesome95-100%

## Explorateur de surfaces

Les surfaces sont ordonnées par niveau de maturité, exhaustivité et qualité. La prise en charge LTS est affichée à côté de chaque ligne afin que les options prêtes pour une version soient faciles à comparer.

### Toutes les surfaces

[CLIM4Stable7 domaines](</fr/maturity/taxonomy#cli>)

CouvertureExpérimental4%

QualitéStable83%

ExhaustivitéStable90%

Partiel - 6

[Runtime GatewayM4Stable13 domaines](</fr/maturity/taxonomy#gateway-runtime>)

CouvertureExpérimental6%

QualitéStable81%

ExhaustivitéStable89%

Partiel - 12

[Hôte Gateway LinuxM4Stable5 domaines](</fr/maturity/taxonomy#linux-gateway-host>)

CouvertureExpérimental0%

QualitéBêta75%

ExhaustivitéStable89%

Partiel - 4

[Hôte Gateway macOSM4Stable7 domaines](</fr/maturity/taxonomy#macos-gateway-host>)

CouvertureExpérimental0%

QualitéBêta74%

ExhaustivitéStable88%

Aucun

[DiscordM4Stable6 domaines](</fr/maturity/taxonomy#discord>)

CouvertureExpérimental0%

QualitéBêta73%

ExhaustivitéStable87%

Partiel - 4

[Runtime d’agentM3Bêta9 domaines](</fr/maturity/taxonomy#agent-runtime>)

CouvertureExpérimental33%

QualitéBêta78%

ExhaustivitéBêta79%

Partiel - 6

[Moteur de session, de mémoire et de contexteM3Bêta9 zones](</fr/maturity/taxonomy#session-memory-and-context-engine>)

CouvertureExpérimental30%

QualitéBêta77%

ExhaustivitéBêta79%

Partiel - 6

[Framework de canalM3Bêta8 zones](</fr/maturity/taxonomy#channel-framework>)

CouvertureExpérimental13%

QualitéBêta76%

ExhaustivitéBêta79%

Partiel - 5

[Outils d’automatisation du navigateur, d’exécution et de bac à sableM3Bêta3 zones](</fr/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CouvertureExpérimental21%

QualitéBêta75%

ExhaustivitéBêta79%

Partiel - 2

[ObservabilitéM3Bêta5 zones](</fr/maturity/taxonomy#observability>)

CouvertureExpérimental18%

QualitéBêta75%

ExhaustivitéBêta79%

Partiel - 3

[Chemin de fournisseur OpenAI et CodexM3Bêta5 zones](</fr/maturity/taxonomy#openai-and-codex-provider-path>)

CouvertureExpérimental26%

QualitéBêta74%

ExhaustivitéBêta79%

Partiel - 3

[Application Web GatewayM3Bêta6 zones](</fr/maturity/taxonomy#gateway-web-app>)

CouvertureExpérimental4%

QualitéBêta74%

ExhaustivitéBêta79%

Aucun

[Outils de recherche WebM3Bêta4 zones](</fr/maturity/taxonomy#web-search-tools>)

CouvertureExpérimental9%

QualitéBeta74%

ExhaustivitéBeta79%

Aucun

[PluginsM3Beta9 domaines](</fr/maturity/taxonomy#plugins>)

CouvertureExpérimental12%

QualitéBeta72%

ExhaustivitéBeta79%

Partiel - 7

[Sécurité, authentification, appairage et secretsM3Beta6 domaines](</fr/maturity/taxonomy#security-auth-pairing-and-secrets>)

CouvertureExpérimental16%

QualitéBeta72%

ExhaustivitéBeta79%

Partiel - 5

[Automatisation : Cron, hooks, tâches, interrogation périodiqueM3Beta6 domaines](</fr/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CouvertureExpérimental2%

QualitéBeta72%

ExhaustivitéBeta79%

Aucun

[Hébergement Docker et PodmanM3Beta4 domaines](</fr/maturity/taxonomy#docker-and-podman-hosting>)

CouvertureExpérimental7%

QualitéBeta71%

ExhaustivitéBeta79%

Aucun

[Windows via WSL2M3Beta6 domaines](</fr/maturity/taxonomy#windows-via-wsl2>)

CouvertureExpérimental6%

QualitéAlpha69%

ExhaustivitéBeta79%

Partiel - 5

[Raspberry Pi et petits appareils LinuxM3Beta4 domaines](</fr/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CouvertureExpérimental0%

QualitéAlpha67%

ExhaustivitéBeta79%

Aucun

[Chemin du fournisseur AnthropicM3Beta5 domaines](</fr/maturity/taxonomy#anthropic-provider-path>)

CouvertureExpérimental0%

QualitéBeta71%

ExhaustivitéBeta78%

Aucun

[TelegramM3Beta5 domaines](</fr/maturity/taxonomy#telegram>)

CouvertureExpérimental0%

QualitéAlpha68%

ExhaustivitéBeta78%

Complet - 5

[SlackM3Beta5 domaines](</fr/maturity/taxonomy#slack>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBeta78%

Complet - 5

[Chemin du fournisseur GoogleM3Beta5 domaines](</fr/maturity/taxonomy#google-provider-path>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBeta78%

Aucun

[iMessage et BlueBubblesM3Beta5 domaines](</fr/maturity/taxonomy#imessage-and-bluebubbles>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBeta78%

Aucun

[Application compagnon macOSM3Beta8 domaines](</fr/maturity/taxonomy#macos-companion-app>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBêta78%

Aucun

[Chemin du fournisseur OpenRouterM3Bêta4 domaines](</fr/maturity/taxonomy#openrouter-provider-path>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBêta78%

Aucun

[WhatsAppM3Bêta5 domaines](</fr/maturity/taxonomy#whatsapp>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBêta78%

Aucun

[Compréhension des médias et génération de médiasM2Alpha6 domaines](</fr/maturity/taxonomy#media-understanding-and-media-generation>)

CouvertureExpérimental2%

QualitéAlpha64%

ExhaustivitéAlpha68%

Aucun

[Outils de génération d’images, de vidéos et de musiqueM2Alpha5 domaines](</fr/maturity/taxonomy#image-video-and-music-generation-tools>)

CouvertureExpérimental0%

QualitéAlpha61%

ExhaustivitéAlpha68%

Aucun

[Fournisseurs de modèles locaux : Ollama, vLLM, SGLang, LM StudioM2Alpha5 domaines](</fr/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CouvertureExpérimental0%

QualitéAlpha61%

ExhaustivitéAlpha68%

Aucun

[Fournisseurs hébergés de longue traîneM2Alpha3 domaines](</fr/maturity/taxonomy#long-tail-hosted-providers>)

CouvertureExpérimental0%

QualitéAlpha61%

ExhaustivitéAlpha68%

Aucun

[Voix et conversation en temps réelM2Alpha6 domaines](</fr/maturity/taxonomy#voice-and-realtime-talk>)

CouvertureExpérimental0%

QualitéAlpha61%

ExhaustivitéAlpha68%

Aucun

[MatrixM2Alpha6 domaines](</fr/maturity/taxonomy#matrix>)

CouvertureExpérimental0%

QualitéAlpha60%

ExhaustivitéAlpha67%

Aucun

[Application AndroidM2Alpha7 domaines](</fr/maturity/taxonomy#android-app>)

CouvertureExpérimental0%

QualitéAlpha59%

ExhaustivitéAlpha66%

Aucun

[Google ChatM2Alpha5 domaines](</fr/maturity/taxonomy#google-chat>)

CouvertureExpérimental0%

QualitéAlpha59%

ExhaustivitéAlpha66%

Aucun

[Microsoft TeamsM2Alpha5 domaines](</fr/maturity/taxonomy#microsoft-teams>)

CouvertureExpérimental0%

QualitéAlpha59%

ExhaustivitéAlpha66%

Aucun

[SignalM2Alpha5 domaines](</fr/maturity/taxonomy#signal>)

CouvertureExpérimental0%

QualitéAlpha59%

ExhaustivitéAlpha66%

Aucun

[TUIM2Alpha5 domaines](</fr/maturity/taxonomy#tui>)

CouvertureExpérimental0%

QualitéAlpha59%

ExhaustivitéAlpha66%

Aucun

[Windows natifM2Alpha4 domaines](</fr/maturity/taxonomy#native-windows>)

CouvertureExpérimental0%

QualitéAlpha58%

ExhaustivitéAlpha66%

Partiel - 1

[ClawHubM2Alpha4 domaines](</fr/maturity/taxonomy#clawhub>)

CouvertureExpérimental0%

QualitéAlpha58%

ExhaustivitéAlpha62%

Aucun

[Hébergement KubernetesM2Alpha4 domaines](</fr/maturity/taxonomy#kubernetes-hosting>)

CouvertureExpérimental0%

QualitéAlpha55%

ExhaustivitéAlpha61%

Aucun

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canaux régionauxM2Alpha4 domaines](</fr/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CouvertureExpérimental0%

QualitéAlpha55%

ExhaustivitéAlpha58%

Aucun

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 domaines](</fr/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CouvertureExpérimental0%

QualitéAlpha53%

ExhaustivitéAlpha54%

Aucun

[SDK d’application OpenClawM2Alpha6 domaines](</fr/maturity/taxonomy#openclaw-app-sdk>)

CouvertureExpérimental3%

QualitéAlpha54%

ComplétudeAlpha53%

Aucun

[application iOSM1Expérimental8 domaines](</fr/maturity/taxonomy#ios-app>)

CouvertureExpérimental0%

QualitéExpérimental41%

ComplétudeExpérimental44%

Aucun

[chemin d’installation NixM1Expérimental5 domaines](</fr/maturity/taxonomy#nix-install-path>)

CouvertureExpérimental0%

QualitéExpérimental41%

ComplétudeExpérimental44%

Aucun

[canal d’appel vocalM1Expérimental5 domaines](</fr/maturity/taxonomy#voice-call-channel>)

CouvertureExpérimental0%

QualitéExpérimental41%

ComplétudeExpérimental44%

Aucun

[surfaces compagnes watchOSM1Expérimental5 domaines](</fr/maturity/taxonomy#watchos-companion-surfaces>)

CouvertureExpérimental0%

QualitéExpérimental41%

ComplétudeExpérimental44%

Aucun

[application compagne LinuxM0Planifié5 domaines](</fr/maturity/taxonomy#linux-companion-app>)

CouvertureExpérimental0%

QualitéExpérimental19%

ComplétudeExpérimental21%

Aucun

[application compagne Windows nativeM0Planifié5 domaines](</fr/maturity/taxonomy#native-windows-companion-app>)

CouvertureExpérimental0%

QualitéExpérimental19%

ExhaustivitéExpérimental21%

Aucun

### Cœur

[CLIM4Stable7 domaines](</fr/maturity/taxonomy#cli>)

CouvertureExpérimental4%

QualitéStable83%

ExhaustivitéStable90%

Partiel - 6

[Environnement d’exécution GatewayM4Stable13 domaines](</fr/maturity/taxonomy#gateway-runtime>)

CouvertureExpérimental6%

QualitéStable81%

ExhaustivitéStable89%

Partiel - 12

[Environnement d’exécution des agentsM3Bêta9 domaines](</fr/maturity/taxonomy#agent-runtime>)

CouvertureExpérimental33%

QualitéBêta78%

ExhaustivitéBêta79%

Partiel - 6

[Moteur de session, de mémoire et de contexteM3Bêta9 domaines](</fr/maturity/taxonomy#session-memory-and-context-engine>)

CouvertureExpérimental30%

QualitéBêta77%

ExhaustivitéBêta79%

Partiel - 6

[Infrastructure de canauxM3Bêta8 domaines](</fr/maturity/taxonomy#channel-framework>)

CouvertureExpérimental13%

QualitéBêta76%

ExhaustivitéBêta79%

Partiel - 5

[ObservabilitéM3Bêta5 domaines](</fr/maturity/taxonomy#observability>)

CouvertureExpérimental18%

QualitéBêta75%

ExhaustivitéBêta79%

Partiel - 3

[Application Web GatewayM3Bêta6 domaines](</fr/maturity/taxonomy#gateway-web-app>)

CouvertureExpérimental4%

QualitéBêta74%

ExhaustivitéBêta79%

Aucun

[PluginsM3Bêta9 domaines](</fr/maturity/taxonomy#plugins>)

CouvertureExpérimental12%

QualitéBêta72%

ExhaustivitéBêta79%

Partiel - 7

[Sécurité, authentification, appairage et secretsM3Bêta6 domaines](</fr/maturity/taxonomy#security-auth-pairing-and-secrets>)

CouvertureExpérimental16%

QualitéBêta72%

ExhaustivitéBêta79%

Partiel - 5

[Automatisation : Cron, points d’accroche, tâches, interrogation périodiqueM3Bêta6 domaines](</fr/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CouvertureExpérimental2%

QualitéBêta72%

ExhaustivitéBêta79%

Aucun

[Compréhension des médias et génération de médiasM2Alpha6 domaines](</fr/maturity/taxonomy#media-understanding-and-media-generation>)

CouvertureExpérimental2%

QualitéAlpha64%

ExhaustivitéAlpha68%

Aucun

[Voix et conversation en temps réelM2Alpha6 domaines](</fr/maturity/taxonomy#voice-and-realtime-talk>)

CouvertureExpérimental0%

QualitéAlpha61%

ExhaustivitéAlpha68%

Aucun

[TUIM2Alpha5 domaines](</fr/maturity/taxonomy#tui>)

CouvertureExpérimental0%

QualitéAlpha59%

ComplétudeAlpha66%

Aucun

[ClawHubM2Alpha4 domaines](</fr/maturity/taxonomy#clawhub>)

CouvertureExpérimental0%

QualitéAlpha58%

ComplétudeAlpha62%

Aucun

[OpenClaw App SDKM2Alpha6 domaines](</fr/maturity/taxonomy#openclaw-app-sdk>)

CouvertureExpérimental3%

QualitéAlpha54%

ComplétudeAlpha53%

Aucun

### Plateforme

[Hôte Gateway LinuxM4Stable5 domaines](</fr/maturity/taxonomy#linux-gateway-host>)

CouvertureExpérimental0%

QualitéBêta75%

ComplétudeStable89%

Partiel - 4

[Hôte Gateway macOSM4Stable7 domaines](</fr/maturity/taxonomy#macos-gateway-host>)

CouvertureExpérimental0%

QualitéBêta74%

ComplétudeStable88%

Aucun

[Hébergement Docker et PodmanM3Bêta4 domaines](</fr/maturity/taxonomy#docker-and-podman-hosting>)

CouvertureExpérimental7%

QualitéBêta71%

ComplétudeBêta79%

Aucun

[Windows via WSL2M3Bêta6 domaines](</fr/maturity/taxonomy#windows-via-wsl2>)

CouvertureExpérimental6%

QualitéAlpha69%

ExhaustivitéBêta79%

Partiel - 5

[Raspberry Pi et petits appareils LinuxM3Bêta4 domaines](</fr/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CouvertureExpérimental0%

QualitéAlpha67%

ExhaustivitéBêta79%

Aucun

[Application compagnon macOSM3Bêta8 domaines](</fr/maturity/taxonomy#macos-companion-app>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBêta78%

Aucun

[Application AndroidM2Alpha7 domaines](</fr/maturity/taxonomy#android-app>)

CouvertureExpérimental0%

QualitéAlpha59%

ExhaustivitéAlpha66%

Aucun

[Windows natifM2Alpha4 domaines](</fr/maturity/taxonomy#native-windows>)

CouvertureExpérimental0%

QualitéAlpha58%

ExhaustivitéAlpha66%

Partiel - 1

[Hébergement KubernetesM2Alpha4 domaines](</fr/maturity/taxonomy#kubernetes-hosting>)

CouvertureExpérimental0%

QualitéAlpha55%

ExhaustivitéAlpha61%

Aucun

[Application iOSM1Expérimental8 domaines](</fr/maturity/taxonomy#ios-app>)

CouvertureExpérimental0%

QualitéExpérimental41%

ExhaustivitéExpérimental44%

Aucun

[Chemin d’installation NixM1Expérimental5 domaines](</fr/maturity/taxonomy#nix-install-path>)

CouvertureExpérimental0%

QualitéExpérimental41%

ExhaustivitéExpérimental44%

Aucun

[Surfaces compagnon watchOSM1Expérimental5 domaines](</fr/maturity/taxonomy#watchos-companion-surfaces>)

CouvertureExpérimental0%

QualitéExpérimental41%

ExhaustivitéExpérimental44%

Aucun

[Application compagnon LinuxM0Planifié5 domaines](</fr/maturity/taxonomy#linux-companion-app>)

CouvertureExpérimental0%

QualitéExpérimental19%

ExhaustivitéExpérimental21%

Aucun

[Application compagnon native WindowsM0Planifié5 domaines](</fr/maturity/taxonomy#native-windows-companion-app>)

CouvertureExpérimental0%

QualitéExpérimental19%

ExhaustivitéExpérimental21%

Aucun

### Canal

[DiscordM4Stable6 domaines](</fr/maturity/taxonomy#discord>)

CouvertureExpérimental0%

QualitéBêta73%

ExhaustivitéStable87%

Partiel - 4

[TelegramM3Bêta5 domaines](</fr/maturity/taxonomy#telegram>)

CouvertureExpérimental0%

QualitéAlpha68%

ExhaustivitéBêta78%

Complet - 5

[SlackM3Bêta5 domaines](</fr/maturity/taxonomy#slack>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBêta78%

Complet - 5

[iMessage et BlueBubblesM3Bêta5 domaines](</fr/maturity/taxonomy#imessage-and-bluebubbles>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBêta78%

Aucun

[WhatsAppM3Bêta5 domaines](</fr/maturity/taxonomy#whatsapp>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBêta78%

Aucun

[MatrixM2Alpha6 domaines](</fr/maturity/taxonomy#matrix>)

CouvertureExpérimental0%

QualitéAlpha60%

ExhaustivitéAlpha67%

Aucun

[Google ChatM2Alpha5 domaines](</fr/maturity/taxonomy#google-chat>)

CouvertureExpérimental0%

QualitéAlpha59%

ExhaustivitéAlpha66%

Aucun

[Microsoft TeamsM2Alpha5 domaines](</fr/maturity/taxonomy#microsoft-teams>)

CouvertureExpérimental0%

QualitéAlpha59%

ComplétudeAlpha66%

Aucun

[SignalM2Alpha5 domaines](</fr/maturity/taxonomy#signal>)

CouvertureExpérimental0%

QualitéAlpha59%

ComplétudeAlpha66%

Aucun

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canaux régionauxM2Alpha4 domaines](</fr/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CouvertureExpérimental0%

QualitéAlpha55%

ComplétudeAlpha58%

Aucun

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 domaines](</fr/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CouvertureExpérimental0%

QualitéAlpha53%

ComplétudeAlpha54%

Aucun

[Canal d’appel vocalM1Expérimental5 domaines](</fr/maturity/taxonomy#voice-call-channel>)

CouvertureExpérimental0%

QualitéExpérimental41%

ComplétudeExpérimental44%

Aucun

### Fournisseur et outil

[Automatisation du navigateur, exécution et outils de sandboxM3Beta3 domaines](</fr/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CouvertureExpérimental21%

QualitéBeta75%

ComplétudeBeta79%

Partiel - 2

[Chemin du fournisseur OpenAI et CodexM3Beta5 domaines](</fr/maturity/taxonomy#openai-and-codex-provider-path>)

CouvertureExpérimental26%

QualitéBeta74%

ExhaustivitéBêta79%

Partiel - 3

[Outils de recherche WebM3Bêta4 domaines](</fr/maturity/taxonomy#web-search-tools>)

CouvertureExpérimental9%

QualitéBêta74%

ExhaustivitéBêta79%

Aucun

[Chemin de fournisseur AnthropicM3Bêta5 domaines](</fr/maturity/taxonomy#anthropic-provider-path>)

CouvertureExpérimental0%

QualitéBêta71%

ExhaustivitéBêta78%

Aucun

[Chemin de fournisseur GoogleM3Bêta5 domaines](</fr/maturity/taxonomy#google-provider-path>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBêta78%

Aucun

[Chemin de fournisseur OpenRouterM3Bêta4 domaines](</fr/maturity/taxonomy#openrouter-provider-path>)

CouvertureExpérimental0%

QualitéAlpha66%

ExhaustivitéBêta78%

Aucun

[Outils de génération d’images, de vidéos et de musiqueM2Alpha5 domaines](</fr/maturity/taxonomy#image-video-and-music-generation-tools>)

CouvertureExpérimental0%

QualitéAlpha61%

ExhaustivitéAlpha68%

Aucun

[Fournisseurs de modèles locaux : Ollama, vLLM, SGLang, LM StudioM2Alpha5 domaines](</fr/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CouvertureExpérimental0%

QualitéAlpha61%

ExhaustivitéAlpha68%

Aucun

[Fournisseurs hébergés de longue traîneM2Alpha3 domaines](</fr/maturity/taxonomy#long-tail-hosted-providers>)

CouvertureExpérimental0%

QualitéAlpha61%

ExhaustivitéAlpha68%

Aucun

## Synthèse des preuves QA

Les vérifications ci-dessous indiquent les domaines de la grille d'évaluation qui ont été exercés par les preuves du profil QA.

Validation complète de la taxonomie 2026-06-23T07:24:36.128Z 96 vérifications - 94 réussies, 2 bloquées 0 sur 281 (0 %) domaines - 20 sur 1675 (1,2 %) fonctionnalités - 77 sur 1665 (4,6 %) identifiants de couverture

### État de préparation par domaine

Ouvrez une surface pour inspecter l'état des preuves de chaque catégorie. La liste reste repliée afin que la page demeure utile d'un coup d'œil.

Runtime d'agent - 9 domaines

8 partiellement examinés / 1 à examiner

Exécution des tours d'agent Partiellement examiné - Validation complète de la taxonomie

0 sur 3 (0 %) / 7 sur 24 (29,2 %) 17 lacunes de capacité

Runtimes externes et sous-agents Partiellement examiné - Validation complète de la taxonomie

0 sur 4 (0 %) / 3 sur 10 (30 %) 7 lacunes de capacité

Exécution par fournisseur hébergé Partiellement examiné - Validation complète de la taxonomie

1 sur 5 (20 %) / 1 sur 5 (20 %) 4 lacunes de capacité

Fournisseurs locaux et auto-hébergés À examiner - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Sélection du modèle et du runtime Partiellement examiné - Validation complète de la taxonomie

0 sur 4 (0 %) / 2 sur 8 (25 %) 6 lacunes de capacité

Authentification du fournisseur Partiellement examiné - Validation complète de la taxonomie

0 sur 10 (0 %) / 4 sur 17 (23,5 %) 13 lacunes de capacité

Streaming et progression Partiellement examiné - Validation complète de la taxonomie

0 sur 2 (0 %) / 5 sur 9 (55,6 %) 4 lacunes de capacité

Appels d'outils et traitement des réponses Partiellement examiné - Validation complète de la taxonomie

0 sur 3 (0 %) / 15 sur 23 (65,2 %) 8 lacunes de capacité

Contrôles d'exécution des outils Partiellement examiné - Validation complète de la taxonomie

0 sur 6 (0 %) / 6 sur 12 (50 %) 6 lacunes de capacité

Application Android - 7 domaines

7 à examiner

Configuration de la connexion À examiner - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Runtime de l'appareil À examiner - Validation complète de la taxonomie

0 sur 2 (0 %) / 0 sur 2 (0 %) 2 lacunes de capacité

Distribution À examiner - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacité

Capture de médias À examiner - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Chat mobile À examiner - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Paramètres À examiner - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Voix À examiner - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Chemin du fournisseur Anthropic - 5 domaines

5 à examiner

Entrées multimédias À examiner - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacité

Sélection du modèle et du runtime À examiner - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 12 (0 %) 12 lacunes de capacité

Cache de prompt et contexte À examiner - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Authentification et récupération du fournisseur À examiner - Validation complète de la taxonomie

0 sur 9 (0 %) / 0 sur 9 (0 %) 9 lacunes de capacité

Transport des requêtes et sémantique des tours À examiner - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Automatisation : Cron, hooks, tâches, interrogation - 6 domaines

5 à revoir / 1 partiellement revu

Hooks d’automatisation À revoir - Validation complète de la taxonomie

0 sur 11 (0 %) / 0 sur 11 (0 %) 11 lacunes de capacité

Tâches et flux en arrière-plan À revoir - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Tâches Cron À revoir - Validation complète de la taxonomie

0 sur 15 (0 %) / 0 sur 15 (0 %) 15 lacunes de capacité

Entrée des événements À revoir - Validation complète de la taxonomie

0 sur 15 (0 %) / 0 sur 15 (0 %) 15 lacunes de capacité

Heartbeat Partiellement revu - Validation complète de la taxonomie

0 sur 5 (0 %) / 1 sur 7 (14,3 %) 6 lacunes de capacité

Contrôles d’interrogation À revoir - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Automatisation du navigateur, exécution et outils d’environnement isolé - 3 domaines

2 partiellement revus / 1 à revoir

Automatisation du navigateur Partiellement revu - Validation complète de la taxonomie

1 sur 8 (12,5 %) / 1 sur 8 (12,5 %) 7 lacunes de capacité

Politique d’environnement isolé et d’outils À revoir - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

Invocation et exécution des outils Partiellement revu - Validation complète de la taxonomie

2 sur 6 (33,3 %) / 4 sur 8 (50 %) 4 lacunes de capacité

Application web Gateway - 6 domaines

3 à revoir / 3 partiellement revus

Accès navigateur et confiance À revoir - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Conversation en temps réel dans le navigateur À revoir - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Interface utilisateur du navigateur Partiellement revu - Validation complète de la taxonomie

0 sur 10 (0 %) / 1 sur 12 (8,3 %) 11 lacunes de capacité

Configuration À revoir - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Console opérateur Partiellement revu - Validation complète de la taxonomie

0 sur 10 (0 %) / 1 sur 12 (8,3 %) 11 lacunes de capacité

Conversations WebChat Partiellement revu - Validation complète de la taxonomie

0 sur 15 (0 %) / 2 sur 20 (10 %) 18 lacunes de capacité

Framework de canaux - 8 domaines

4 à revoir / 4 partiellement revus

Actions, commandes et approbations de canal À revoir - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Configuration de canal Partiellement revu - Validation complète de la taxonomie

0 sur 5 (0 %) / 1 sur 7 (14,3 %) 6 lacunes de capacité

Routage et livraison des conversations Partiellement revu - Validation complète de la taxonomie

0 sur 10 (0 %) / 5 sur 27 (18,5 %) 22 lacunes de capacité

Comportement des fils de groupe et des salons ambiants Partiellement revu - Validation complète de la taxonomie

0 sur 5 (0 %) / 4 sur 11 (36,4 %) 7 lacunes de capacité

Accès entrant et contrôles d’identité À revoir - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Pièces jointes multimédias et données de canal enrichies À revoir - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacité

Livraison sortante et pipeline de réponse Partiellement revu - Validation complète de la taxonomie

0 sur 4 (0 %) / 8 sur 21 (38,1 %) 13 lacunes de capacité

État de santé et contrôles opérateur À revoir - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

ClawHub - 4 domaines

4 nécessitent une revue

Découverte du catalogue Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Compatibilité et confiance Nécessite une revue - Validation complète de la taxonomie

0 sur 12 (0 %) / 0 sur 12 (0 %) 12 lacunes de capacité

Cycle de vie et santé du Plugin Nécessite une revue - Validation complète de la taxonomie

0 sur 26 (0 %) / 0 sur 26 (0 %) 26 lacunes de capacité

Publication Nécessite une revue - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

CLI - 7 domaines

5 nécessitent une revue / 2 partiellement revus

Observabilité de la CLI Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Configuration de la CLI Partiellement revu - Validation complète de la taxonomie

1 sur 6 (16,7 %) / 1 sur 6 (16,7 %) 5 lacunes de capacité

Doctor Nécessite une revue - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Gestion du service Gateway Partiellement revu - Validation complète de la taxonomie

0 sur 5 (0 %) / 1 sur 7 (14,3 %) 6 lacunes de capacité

Intégration et configuration de l’authentification Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Configuration des Plugins et des canaux Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Mises à jour et montées de version Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Discord - 6 domaines

6 nécessitent une revue

Accès et identité Nécessite une revue - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

Configuration et opérations des canaux Nécessite une revue - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Routage et livraison des conversations Nécessite une revue - Validation complète de la taxonomie

0 sur 12 (0 %) / 0 sur 12 (0 %) 12 lacunes de capacité

Médias et contenu enrichi Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Contrôles natifs et approbations Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Voix et appels en temps réel Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Hébergement Docker et Podman - 4 domaines

3 nécessitent une revue / 1 partiellement revu

Sandbox et outillage des agents Nécessite une revue - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacité

Opérations de conteneur Nécessite une revue - Validation complète de la taxonomie

0 sur 11 (0 %) / 0 sur 11 (0 %) 11 lacunes de capacité

Configuration de conteneur Nécessite une revue - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

Publication et validation des images Partiellement revu - Validation complète de la taxonomie

1 sur 5 (20 %) / 2 sur 7 (28,6 %) 5 lacunes de capacité

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canaux régionaux - 4 domaines

4 nécessitent une révision

Accès et identité Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Configuration et opérations du canal Nécessite une révision - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

Routage et livraison des conversations Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Médias et contenu enrichi Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Runtime Gateway - 13 domaines

9 nécessitent une révision / 4 partiellement révisés

Approbations et exécution à distance Nécessite une révision - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

Authentification et appairage des appareils Nécessite une révision - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Cycle de vie du Gateway Partiellement révisé - Validation complète de la taxonomie

0 sur 7 (0 %) / 4 sur 12 (33,3 %) 8 lacunes de capacité

API RPC et événements du Gateway Partiellement révisé - Validation complète de la taxonomie

0 sur 20 (0 %) / 2 sur 22 (9,1 %) 20 lacunes de capacité

État, diagnostics et réparation Nécessite une révision - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

Surface Web hébergée Nécessite une révision - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacité

API HTTP Partiellement révisé - Validation complète de la taxonomie

1 sur 4 (25 %) / 1 sur 4 (25 %) 3 lacunes de capacité

Accès réseau et découverte Nécessite une révision - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

Nodes et capacités à distance Nécessite une révision - Validation complète de la taxonomie

0 sur 8 (0 %) / 0 sur 8 (0 %) 8 lacunes de capacité

Compatibilité du protocole Nécessite une révision - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

Rôles et autorisations Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Contrôles de sécurité Nécessite une révision - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

Connexion WebSocket Partiellement révisé - Validation complète de la taxonomie

1 sur 8 (12,5 %) / 1 sur 8 (12,5 %) 7 lacunes de capacité

Google Chat - 5 domaines

5 nécessitent une révision

Accès et identité Nécessite une révision - Validation complète de la taxonomie

0 sur 11 (0 %) / 0 sur 11 (0 %) 11 lacunes de capacité

Configuration et opérations du canal Nécessite une révision - Validation complète de la taxonomie

0 sur 16 (0 %) / 0 sur 16 (0 %) 16 lacunes de capacité

Routage et livraison des conversations Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Médias et contenu enrichi Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Contrôles natifs et approbations Nécessite une révision - Validation complète de la taxonomie

0 sur 16 (0 %) / 0 sur 16 (0 %) 16 lacunes de capacité

Chemin du fournisseur Google - 5 domaines

5 nécessitent une revue

Runtime Gemini direct Nécessite une revue - Validation complète de la taxonomie

0 sur 9 (0 %) / 0 sur 9 (0 %) 9 lacunes de capacités

Médias, recherche et temps réel Nécessite une revue - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacités

Routage des modèles et points de terminaison Nécessite une revue - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacités

Mise en cache des prompts Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacités

Configuration du fournisseur et identifiants Nécessite une revue - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacités

Outils de génération d’images, de vidéos et de musique - 5 domaines

5 nécessitent une revue

Génération d’images Nécessite une revue - Validation complète de la taxonomie

0 sur 9 (0 %) / 0 sur 9 (0 %) 9 lacunes de capacités

Routage et découverte des médias Nécessite une revue - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacités

Génération de musique Nécessite une revue - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacités

Cycle de vie et livraison des tâches Nécessite une revue - Validation complète de la taxonomie

0 sur 12 (0 %) / 0 sur 12 (0 %) 12 lacunes de capacités

Génération de vidéos Nécessite une revue - Validation complète de la taxonomie

0 sur 11 (0 %) / 0 sur 11 (0 %) 11 lacunes de capacités

iMessage et BlueBubbles - 5 domaines

5 nécessitent une revue

Accès et identité Nécessite une revue - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacités

Configuration et opérations du canal Nécessite une revue - Validation complète de la taxonomie

0 sur 11 (0 %) / 0 sur 11 (0 %) 11 lacunes de capacités

Routage et livraison des conversations Nécessite une revue - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacités

Médias et contenu enrichi Nécessite une revue - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacités

Contrôles natifs et approbations Nécessite une revue - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacités

Application iOS - 8 domaines

8 nécessitent une revue

Canvas et écran Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Chat et sessions Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Commandes d’appareil Nécessite une revue - Validation complète de la taxonomie

0 sur 2 (0 %) / 0 sur 2 (0 %) 2 lacunes de capacités

Distribution Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Configuration et diagnostics du Gateway Nécessite une revue - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacités

Médias et partage Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Notifications et arrière-plan Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Voix Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Hébergement Kubernetes - 4 domaines

4 nécessitent une revue

Accès et exposition Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Cycle de vie du cluster Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Configuration et secrets Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Configuration du déploiement Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Application compagnon Linux - 5 domaines

5 nécessitent une revue

Distribution de l'application Nécessite une revue - Validation complète de la taxonomie

0 sur 3 (0%) / 0 sur 3 (0%) 3 lacunes de capacité

Chat et sessions Nécessite une revue - Validation complète de la taxonomie

0 sur 3 (0%) / 0 sur 3 (0%) 3 lacunes de capacité

Fonctionnalités de bureau Nécessite une revue - Validation complète de la taxonomie

0 sur 9 (0%) / 0 sur 9 (0%) 9 lacunes de capacité

Connectivité Gateway Nécessite une revue - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

État et diagnostics Nécessite une revue - Validation complète de la taxonomie

0 sur 7 (0%) / 0 sur 7 (0%) 7 lacunes de capacité

Hôte Gateway Linux - 5 domaines

5 nécessitent une revue

Cibles de déploiement Nécessite une revue - Validation complète de la taxonomie

0 sur 3 (0%) / 0 sur 3 (0%) 3 lacunes de capacité

Diagnostics et réparation Nécessite une revue - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

Runtime Gateway et contrôle du service Nécessite une revue - Validation complète de la taxonomie

0 sur 6 (0%) / 0 sur 6 (0%) 6 lacunes de capacité

Configuration et mises à jour de l'hôte Nécessite une revue - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

Accès à distance et sécurité Nécessite une revue - Validation complète de la taxonomie

0 sur 6 (0%) / 0 sur 6 (0%) 6 lacunes de capacité

Fournisseurs de modèles locaux : Ollama, vLLM, SGLang, LM Studio - 5 domaines

5 nécessitent une revue

Mémoire locale et embeddings Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Plugins de fournisseurs natifs Nécessite une revue - Validation complète de la taxonomie

0 sur 10 (0%) / 0 sur 10 (0%) 10 lacunes de capacité

Sécurité réseau et contrôles des prompts Nécessite une revue - Validation complète de la taxonomie

0 sur 2 (0%) / 0 sur 2 (0%) 2 lacunes de capacité

Compatibilité du runtime compatible avec OpenAI Nécessite une revue - Validation complète de la taxonomie

0 sur 8 (0%) / 0 sur 8 (0%) 8 lacunes de capacité

Configuration, cycle de vie et diagnostics des fournisseurs Nécessite une revue - Validation complète de la taxonomie

0 sur 12 (0%) / 0 sur 12 (0%) 12 lacunes de capacité

Fournisseurs hébergés de longue traîne - 3 domaines

3 nécessitent une revue

Fournisseurs LLM hébergés Nécessite une revue - Validation complète de la taxonomie

0 sur 12 (0%) / 0 sur 12 (0%) 12 lacunes de capacité

Fournisseurs de médias hébergés Nécessite une revue - Validation complète de la taxonomie

0 sur 8 (0%) / 0 sur 8 (0%) 8 lacunes de capacité

Opérations des fournisseurs Nécessite une revue - Validation complète de la taxonomie

0 sur 12 (0%) / 0 sur 12 (0%) 12 lacunes de capacité

Application compagnon macOS - 8 domaines

8 nécessitent une révision

Canvas Nécessite une révision - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacités

Configuration locale Nécessite une révision - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacités

Capacités natives Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacités

Connexions distantes Nécessite une révision - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacités

WebChat distant Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacités

État et paramètres Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacités

Voix et conversation Nécessite une révision - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacités

WebChat Nécessite une révision - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacités

Hôte Gateway macOS - 7 domaines

7 nécessitent une révision

Configuration de la CLI Nécessite une révision - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacités

Diagnostics et observabilité Nécessite une révision - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacités

Cycle de vie du service Gateway Nécessite une révision - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacités

Intégration du Gateway local Nécessite une révision - Validation complète de la taxonomie

0 sur 9 (0 %) / 0 sur 9 (0 %) 9 lacunes de capacités

Autorisations et capacités natives Nécessite une révision - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacités

Profils et isolation Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacités

Mode Gateway distant Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacités

Matrix - 6 domaines

6 nécessitent une révision

Accès et identité Nécessite une révision - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacités

Configuration et opérations du canal Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacités

Routage et livraison des conversations Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Chiffrement et vérification Nécessite une révision - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacités

Médias et contenu enrichi Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Contrôles natifs et approbations Nécessite une révision - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacités

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - 4 domaines

4 nécessitent une révision

Accès et identité Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0%) / 0 sur 1 (0%) 1 lacune de capacité

Configuration et opérations du canal Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0%) / 0 sur 1 (0%) 1 lacune de capacité

Routage et livraison des conversations Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0%) / 0 sur 1 (0%) 1 lacune de capacité

Médias et contenu enrichi Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0%) / 0 sur 1 (0%) 1 lacune de capacité

Compréhension des médias et génération de médias - 6 domaines

4 nécessitent une révision / 2 partiellement révisés

Gestion des médias du canal Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Configuration des médias Nécessite une révision - Validation complète de la taxonomie

0 sur 1 (0%) / 0 sur 1 (0%) 1 lacune de capacité

Génération de médias Partiellement révisé - Validation complète de la taxonomie

1 sur 17 (5.9%) / 1 sur 19 (5.3%) 18 lacunes de capacité

Ingestion et accès aux médias Nécessite une révision - Validation complète de la taxonomie

0 sur 8 (0%) / 0 sur 8 (0%) 8 lacunes de capacité

Compréhension des médias Partiellement révisé - Validation complète de la taxonomie

0 sur 12 (0%) / 1 sur 14 (7.1%) 13 lacunes de capacité

Livraison de la synthèse vocale Nécessite une révision - Validation complète de la taxonomie

0 sur 2 (0%) / 0 sur 2 (0%) 2 lacunes de capacité

Microsoft Teams - 5 domaines

5 nécessitent une révision

Accès et identité Nécessite une révision - Validation complète de la taxonomie

0 sur 9 (0%) / 0 sur 9 (0%) 9 lacunes de capacité

Configuration et opérations du canal Nécessite une révision - Validation complète de la taxonomie

0 sur 9 (0%) / 0 sur 9 (0%) 9 lacunes de capacité

Routage et livraison des conversations Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Médias et contenu enrichi Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Contrôles natifs et approbations Nécessite une révision - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Windows natif - 4 domaines

4 nécessitent une révision

CLI Nécessite une révision - Validation complète de la taxonomie

0 sur 9 (0%) / 0 sur 9 (0%) 9 lacunes de capacité

Gestion du Gateway Nécessite une révision - Validation complète de la taxonomie

0 sur 11 (0%) / 0 sur 11 (0%) 11 lacunes de capacité

Réseau Nécessite une révision - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

Mises à jour Nécessite une révision - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

Native Windows companion app - 5 areas

5 à examiner

Sessions de chat À examiner - Validation complète de la taxonomie

0 sur 2 (0 %) / 0 sur 2 (0 %) 2 lacunes de capacité

Outils de bureau et autorisations À examiner - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Connexion Gateway À examiner - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacité

Installation et mises à jour À examiner - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacité

État et réparation À examiner - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Nix install path - 5 areas

5 à examiner

Activation et UX de l’application À examiner - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

Configuration et état À examiner - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

Transfert d’installation À examiner - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacité

Cycle de vie du Plugin À examiner - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacité

Runtime du service et protections À examiner - Validation complète de la taxonomie

0 sur 8 (0 %) / 0 sur 8 (0 %) 8 lacunes de capacité

OpenAI and Codex provider path - 5 areas

2 à examiner / 3 partiellement examinés

Entrée image et multimodale À examiner - Validation complète de la taxonomie

0 sur 2 (0 %) / 0 sur 2 (0 %) 2 lacunes de capacité

Modèle et authentification Partiellement examiné - Validation complète de la taxonomie

1 sur 6 (16,7 %) / 4 sur 9 (44,4 %) 5 lacunes de capacité

Harnais Codex natif Partiellement examiné - Validation complète de la taxonomie

0 sur 2 (0 %) / 4 sur 9 (44,4 %) 5 lacunes de capacité

Réponses et compatibilité des outils Partiellement examiné - Validation complète de la taxonomie

1 sur 4 (25 %) / 2 sur 5 (40 %) 3 lacunes de capacité

Voix et audio en temps réel À examiner - Validation complète de la taxonomie

0 sur 2 (0 %) / 0 sur 2 (0 %) 2 lacunes de capacité

OpenClaw App SDK - 6 areas

5 à examiner / 1 partiellement examiné

Conversations d’agent À examiner - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

API client À examiner - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacité

Compatibilité À examiner - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Événements et approbations À examiner - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Accès Gateway À examiner - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Assistants de ressources Partiellement examiné - Validation complète de la taxonomie

0 sur 5 (0 %) / 1 sur 6 (16,7 %) 5 lacunes de capacité

Chemin du fournisseur OpenRouter - 4 domaines

4 à examiner

Runtime de chat et normalisation À examiner - Validation complète de la taxonomie

0 sur 15 (0%) / 0 sur 15 (0%) 15 lacunes de capacité

Génération de médias et parole À examiner - Validation complète de la taxonomie

0 sur 7 (0%) / 0 sur 7 (0%) 7 lacunes de capacité

Récupération et diagnostics du fournisseur À examiner - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Configuration et authentification du fournisseur À examiner - Validation complète de la taxonomie

0 sur 14 (0%) / 0 sur 14 (0%) 14 lacunes de capacité

Plugins - 9 domaines

6 à examiner / 3 partiellement examinés

Création et packaging des Plugins À examiner - Validation complète de la taxonomie

0 sur 8 (0%) / 0 sur 8 (0%) 8 lacunes de capacité

Plugins groupés À examiner - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Plugin Canvas À examiner - Validation complète de la taxonomie

0 sur 6 (0%) / 0 sur 6 (0%) 6 lacunes de capacité

Plugins de canaux À examiner - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Installation et exécution des Plugins Partiellement examiné - Validation complète de la taxonomie

0 sur 6 (0%) / 7 sur 20 (35%) 13 lacunes de capacité

Approbations de Plugins À examiner - Validation complète de la taxonomie

0 sur 6 (0%) / 0 sur 6 (0%) 6 lacunes de capacité

Plugins de fournisseurs et d’outils Partiellement examiné - Validation complète de la taxonomie

1 sur 6 (16.7%) / 9 sur 21 (42.9%) 12 lacunes de capacité

Publication de Plugins À examiner - Validation complète de la taxonomie

0 sur 6 (0%) / 0 sur 6 (0%) 6 lacunes de capacité

Test des Plugins Partiellement examiné - Validation complète de la taxonomie

0 sur 6 (0%) / 3 sur 11 (27.3%) 8 lacunes de capacité

Raspberry Pi et petits appareils Linux - 4 domaines

4 à examiner

Runtime du Gateway À examiner - Validation complète de la taxonomie

0 sur 10 (0%) / 0 sur 10 (0%) 10 lacunes de capacité

Performances et diagnostics À examiner - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Accès distant et authentification À examiner - Validation complète de la taxonomie

0 sur 9 (0%) / 0 sur 9 (0%) 9 lacunes de capacité

Configuration et compatibilité À examiner - Validation complète de la taxonomie

0 sur 12 (0%) / 0 sur 12 (0%) 12 lacunes de capacité

Sécurité, authentification, appairage et secrets - 6 domaines

2 partiellement examinés / 4 à examiner

Politique d’approbation et protections des outils Partiellement examiné - Validation complète de la taxonomie

0 sur 2 (0%) / 3 sur 6 (50%) 3 lacunes de capacité

Contrôle d’accès aux canaux À examiner - Validation complète de la taxonomie

0 sur 3 (0%) / 0 sur 3 (0%) 3 lacunes de capacité

Hygiène des identifiants et des secrets Partiellement examiné - Validation complète de la taxonomie

0 sur 5 (0%) / 5 sur 11 (45.5%) 6 lacunes de capacité

Appairage des appareils et des Node À examiner - Validation complète de la taxonomie

0 sur 11 (0%) / 0 sur 11 (0%) 11 lacunes de capacité

Authentification du Gateway et accès distant À examiner - Validation complète de la taxonomie

0 sur 9 (0%) / 0 sur 9 (0%) 9 lacunes de capacité

Confiance des Plugins À examiner - Validation complète de la taxonomie

0 sur 2 (0%) / 0 sur 2 (0%) 2 lacunes de capacité

Session, mémoire et moteur de contexte - 9 domaines

2 nécessitent une revue / 7 partiellement revus

Gestion des sessions CLI et des transcriptions Nécessite une revue - Validation complète de la taxonomie

0 sur 2 (0 %) / 0 sur 2 (0 %) 2 lacunes de capacité

Moteur de contexte Partiellement revu - Validation complète de la taxonomie

0 sur 2 (0 %) / 4 sur 7 (57,1 %) 3 lacunes de capacité

Prompts principaux et contexte Partiellement revu - Validation complète de la taxonomie

0 sur 2 (0 %) / 3 sur 8 (37,5 %) 5 lacunes de capacité

Historique entre clients et parité des sessions Partiellement revu - Validation complète de la taxonomie

0 sur 2 (0 %) / 2 sur 5 (40 %) 3 lacunes de capacité

Diagnostics, maintenance et récupération Partiellement revu - Validation complète de la taxonomie

0 sur 3 (0 %) / 4 sur 10 (40 %) 6 lacunes de capacité

Mémoire Partiellement revu - Validation complète de la taxonomie

0 sur 5 (0 %) / 6 sur 13 (46,2 %) 7 lacunes de capacité

Routage des sessions Partiellement revu - Validation complète de la taxonomie

0 sur 2 (0 %) / 1 sur 4 (25 %) 3 lacunes de capacité

Gestion des tokens Partiellement revu - Validation complète de la taxonomie

0 sur 3 (0 %) / 2 sur 10 (20 %) 8 lacunes de capacité

Persistance des transcriptions Nécessite une revue - Validation complète de la taxonomie

0 sur 2 (0 %) / 0 sur 2 (0 %) 2 lacunes de capacité

Signal - 5 domaines

5 nécessitent une revue

Accès et identité Nécessite une revue - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

Configuration et opérations du canal Nécessite une revue - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

Routage et livraison des conversations Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Médias et contenu enrichi Nécessite une revue - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

Contrôles et approbations natifs Nécessite une revue - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacité

Slack - 5 domaines

5 nécessitent une revue

Accès et identité Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Configuration et opérations du canal Nécessite une revue - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Routage et livraison des conversations Nécessite une revue - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Médias et contenu enrichi Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Contrôles et approbations natifs Nécessite une revue - Validation complète de la taxonomie

0 sur 8 (0 %) / 0 sur 8 (0 %) 8 lacunes de capacité

Telegram - 5 domaines

5 nécessitent une revue

Accès et identité Nécessite une revue - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Configuration et opérations du canal Nécessite une revue - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Routage et livraison des conversations Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Médias et contenu enrichi Nécessite une revue - Validation complète de la taxonomie

0 sur 1 (0 %) / 0 sur 1 (0 %) 1 lacune de capacité

Contrôles et approbations natifs Nécessite une revue - Validation complète de la taxonomie

0 sur 9 (0 %) / 0 sur 9 (0 %) 9 lacunes de capacité

Observabilité - 5 domaines

3 partiellement revus / 2 à examiner

Collecte de diagnostics Partiellement revu - Validation complète de la taxonomie

1 sur 8 (12.5%) / 3 sur 10 (30%) 7 lacunes de capacité

Santé et réparation Partiellement revu - Validation complète de la taxonomie

1 sur 12 (8.3%) / 5 sur 18 (27.8%) 13 lacunes de capacité

Journalisation À examiner - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Diagnostics de session À examiner - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

Exportation de télémétrie Partiellement revu - Validation complète de la taxonomie

1 sur 13 (7.7%) / 7 sur 21 (33.3%) 14 lacunes de capacité

TUI - 5 domaines

5 à examiner

Entrée et commandes À examiner - Validation complète de la taxonomie

0 sur 8 (0%) / 0 sur 8 (0%) 8 lacunes de capacité

Exécution du shell local À examiner - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

Rendu et sécurité de la sortie À examiner - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

Modes d’exécution À examiner - Validation complète de la taxonomie

0 sur 14 (0%) / 0 sur 14 (0%) 14 lacunes de capacité

Gestion de session À examiner - Validation complète de la taxonomie

0 sur 3 (0%) / 0 sur 3 (0%) 3 lacunes de capacité

Voix et conversation en temps réel - 6 domaines

6 à examiner

Conversation dans l’application native À examiner - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

Sessions de conversation en temps réel À examiner - Validation complète de la taxonomie

0 sur 11 (0%) / 0 sur 11 (0%) 11 lacunes de capacité

Parole et transcription À examiner - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Observabilité de la conversation À examiner - Validation complète de la taxonomie

0 sur 5 (0%) / 0 sur 5 (0%) 5 lacunes de capacité

Fournisseurs de conversation À examiner - Validation complète de la taxonomie

0 sur 7 (0%) / 0 sur 7 (0%) 7 lacunes de capacité

Activation vocale et routage À examiner - Validation complète de la taxonomie

0 sur 4 (0%) / 0 sur 4 (0%) 4 lacunes de capacité

Canal d’appels vocaux - 5 domaines

5 à examiner

Accès et identité À examiner - Validation complète de la taxonomie

0 sur 1 (0%) / 0 sur 1 (0%) 1 lacune de capacité

Configuration et opérations du canal À examiner - Validation complète de la taxonomie

0 sur 2 (0%) / 0 sur 2 (0%) 2 lacunes de capacité

Routage et livraison des conversations À examiner - Validation complète de la taxonomie

0 sur 1 (0%) / 0 sur 1 (0%) 1 lacune de capacité

Médias et contenu enrichi À examiner - Validation complète de la taxonomie

0 sur 2 (0%) / 0 sur 2 (0%) 2 lacunes de capacité

Voix et appels en temps réel À examiner - Validation complète de la taxonomie

0 sur 2 (0%) / 0 sur 2 (0%) 2 lacunes de capacité

Surfaces compagnes watchOS - 5 domaines

5 à réviser

Livraison et récupération À réviser - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

Distribution et support À réviser - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

Approbations d’exécution À réviser - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacité

Notifications et réponses À réviser - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

Interface utilisateur de l’application Watch À réviser - Validation complète de la taxonomie

0 sur 3 (0 %) / 0 sur 3 (0 %) 3 lacunes de capacité

Outils de recherche Web - 4 domaines

2 à réviser / 2 partiellement révisés

Sécurité réseau À réviser - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacité

Fournisseurs de recherche Partiellement révisé - Validation complète de la taxonomie

2 sur 19 (10,5 %) / 2 sur 19 (10,5 %) 17 lacunes de capacité

Configuration et diagnostics À réviser - Validation complète de la taxonomie

0 sur 9 (0 %) / 0 sur 9 (0 %) 9 lacunes de capacité

Disponibilité des outils et récupération Partiellement révisé - Validation complète de la taxonomie

2 sur 11 (18,2 %) / 3 sur 12 (25 %) 9 lacunes de capacité

WhatsApp - 5 domaines

5 à réviser

Accès et identité À réviser - Validation complète de la taxonomie

0 sur 7 (0 %) / 0 sur 7 (0 %) 7 lacunes de capacité

Configuration et opérations du canal À réviser - Validation complète de la taxonomie

0 sur 5 (0 %) / 0 sur 5 (0 %) 5 lacunes de capacité

Routage et livraison des conversations À réviser - Validation complète de la taxonomie

0 sur 4 (0 %) / 0 sur 4 (0 %) 4 lacunes de capacité

Médias et contenu enrichi À réviser - Validation complète de la taxonomie

0 sur 2 (0 %) / 0 sur 2 (0 %) 2 lacunes de capacité

Contrôles natifs et approbations À réviser - Validation complète de la taxonomie

0 sur 2 (0 %) / 0 sur 2 (0 %) 2 lacunes de capacité

Windows via WSL2 - 6 domaines

5 à réviser / 1 partiellement révisé

Navigateur et interface utilisateur de contrôle À réviser - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

CLI À réviser - Validation complète de la taxonomie

0 sur 8 (0 %) / 0 sur 8 (0 %) 8 lacunes de capacité

Diagnostics et réparation Partiellement révisé - Validation complète de la taxonomie

1 sur 6 (16,7 %) / 3 sur 8 (37,5 %) 5 lacunes de capacité

Accès et exposition du Gateway À réviser - Validation complète de la taxonomie

0 sur 11 (0 %) / 0 sur 11 (0 %) 11 lacunes de capacité

Cycle de vie du service Gateway À réviser - Validation complète de la taxonomie

0 sur 10 (0 %) / 0 sur 10 (0 %) 10 lacunes de capacité

Configuration de WSL À réviser - Validation complète de la taxonomie

0 sur 6 (0 %) / 0 sur 6 (0 %) 6 lacunes de capacité

> Dernière mise à jour : 2026-06-22

Was this useful?YesNo

Open issue