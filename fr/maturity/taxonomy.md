---
title: Taxonomie de maturité
source_url: https://docs.openclaw.ai/fr/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Taxonomie de maturité

le modèle derrière le tableau de score

Surfaces > catégories > capacités > preuves.

50 surfaces regroupées en 4 familles, chaque catégorie étant reliée aux docs canoniques et aux ID de couverture QA.

Parcourir les domaines produit / Ouvrir la taxonomie détaillée / [Voir les scores](</fr/maturity/scorecard>)

## Comment lire cette page

Une surface est un domaine produit tel que le runtime Gateway, Discord ou l’application macOS. Chaque surface contient des catégories, et chaque catégorie contient les vérifications au niveau des capacités couvertes par les scénarios QA. Utilisez le tableau de score pour le jugement au niveau d’une release ; utilisez cette page pour examiner le modèle sous-jacent.

## Niveaux de maturité

M0PlanifiéLa direction est connue, mais aucun parcours utilisateur pris en charge n’existe.Promotion : un ticket de conception, un propriétaire et une surface cible existent.

M1ExpérimentalImplémenté avec des réserves, des flags, des builds depuis les sources ou des flux réservés aux mainteneurs.Promotion : un mainteneur peut exécuter le scénario depuis la branche main actuelle.

M2AlphaDe vrais utilisateurs peuvent l’essayer, mais des changements cassants et une UX incomplète sont attendus.Promotion : configuration documentée, tests de base, réserves connues et au moins une preuve en environnement réel.

M3BetaUn parcours public existe et le workflow principal est utilisable avec des réserves limitées.Promotion : docs d’installation/mise à jour, tests de régression, runbook de support et preuve de scénario réussie dans l’environnement attendu.

M4StableParcours recommandé pour les utilisateurs normaux. Les échecs sont traités comme des régressions.Promotion : garde de release, parcours doctor/dépannage, docs étendues et preuves répétées en conditions réelles.

M5ClawesomeSoigné, agréable, bien instrumenté et compétitif face au meilleur workflow comparable.Promotion : Stable plus réussite au tableau de score utilisateur sur des utilisateurs représentatifs.

## Domaines produit

### Cœur

CLI M4Stable7 domaines - 90 % terminé Runtime Gateway M4Stable13 domaines - 89 % terminé Runtime d’agent M3Beta9 domaines - 79 % terminé Session, mémoire et moteur de contexte M3Beta9 domaines - 79 % terminé Framework de canal M3Beta8 domaines - 79 % terminé Observabilité M3Beta5 domaines - 79 % terminé Application Web Gateway M3Beta6 domaines - 79 % terminé Plugins M3Bêta9 domaines - 79 % terminé Sécurité, authentification, appairage et secrets M3Bêta6 domaines - 79 % terminé Automatisation : Cron, hooks, tâches, interrogation M3Bêta6 domaines - 79 % terminé Compréhension des médias et génération de médias M2Alpha6 domaines - 68 % terminé Voix et conversation en temps réel M2Alpha6 domaines - 68 % terminé TUI M2Alpha5 domaines - 66 % terminé ClawHub M2Alpha4 domaines - 62 % terminé SDK d’application OpenClaw M2Alpha6 domaines - 53 % terminé

### Platform

Hôte Gateway Linux M4Stable5 domaines - 89 % terminé Hôte Gateway macOS M4Stable7 domaines - 88 % terminé Hébergement Docker et Podman M3Bêta4 domaines - 79 % terminé Windows via WSL2 M3Bêta6 domaines - 79 % terminé Raspberry Pi et petits appareils Linux M3Bêta4 domaines - 79 % terminé Application compagnon macOS M3Bêta8 domaines - 78 % terminé Application Android M2Alpha7 domaines - 66 % terminé Windows natif M2Alpha4 domaines - 66 % terminé Hébergement Kubernetes M2Alpha4 domaines - 61 % terminé Application iOS M1Expérimental8 domaines - 44 % terminé Chemin d’installation Nix M1Expérimental5 domaines - 44 % terminé Surfaces compagnes watchOS M1Expérimental5 domaines - 44 % terminé Application compagne Linux M0Planifié5 domaines - 21 % terminé Application compagne Windows native M0Planifié5 domaines - 21 % terminé

### Canal

Discord M4Stable6 domaines - 87 % terminé Telegram M3Bêta5 domaines - 78 % terminé Slack M3Bêta5 domaines - 78 % terminé iMessage et BlueBubbles M3Bêta5 domaines - 78 % terminé WhatsApp M3Bêta5 domaines - 78 % terminé Matrix M2Alpha6 domaines - 67 % terminé Google Chat M2Alpha5 domaines - 66 % terminé Microsoft Teams M2Alpha5 domaines - 66 % terminé Signal M2Alpha5 domaines - 66 % terminé Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canaux régionaux M2Alpha4 domaines - 58 % terminé Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alpha4 domaines - 54 % terminé Canal d’appel vocal M1Expérimental5 domaines - 44 % terminé

### Fournisseur et outil

Outils d’automatisation du navigateur, d’exécution et de bac à sable M3Bêta3 domaines - 79 % terminé Chemin de fournisseur OpenAI et Codex M3Bêta5 domaines - 79 % terminé Outils de recherche Web M3Bêta4 domaines - 79 % terminé Chemin de fournisseur Anthropic M3Bêta5 domaines - 78 % terminé Chemin de fournisseur Google M3Bêta5 domaines - 78 % terminé Chemin de fournisseur OpenRouter M3Bêta4 domaines - 78 % terminé Outils de génération d’images, de vidéos et de musique M2Alpha5 domaines - 68 % terminé Fournisseurs de modèles locaux : Ollama, vLLM, SGLang, LM Studio M2Alpha5 domaines - 68 % terminé Fournisseurs hébergés de longue traîne M2Alpha3 domaines - 68 % terminé

## Détails

### Cœur

CLI - M4 Stable - 7 domaines

Les chemins de configuration et de réparation normaux sont documentés dans les docs d’installation, de CLI et de Gateway. Les chemins Windows propres à chaque plateforme sont suivis dans les lignes Windows via WSL2 et Windows natif.

Couverture expérimentale - 4 %Qualité stable - 83 %Exhaustivité stable - 90 %Partiel - 6

Configuration du CLI 6 capacités / pris en charge par LTS

Expérimental17%

Stable89%

Stable90%

[Index](</fr/install>), [Programme d’installation](</fr/install/installer>), [Node](</fr/install/node>), [Mise à jour](</fr/install/updating>)

Configuration de l’onboarding et de l’authentification 5 capacités / pris en charge par LTS

Expérimental0%

Bêta75%

Stable89%

[Onboarding](</fr/cli/onboard>), [Configuration](</fr/cli/configure>), [Vue d’ensemble de l’onboarding](</fr/start/onboarding-overview>)

Configuration des Plugins et des canaux 5 capacités

Expérimental0%

Bêta75%

Stable89%

[Onboarding](</fr/cli/onboard>), [Plugins](</fr/cli/plugins>), [Canaux](</fr/cli/channels>)

Gestion du service Gateway 5 capacités / pris en charge par LTS

Expérimental14%

Stable87%

Stable90%

[Gateway](</fr/cli/gateway>), [Mise à jour](</fr/install/updating>), [Dépannage](</fr/gateway/troubleshooting>)

Observabilité du CLI 5 capacités / pris en charge par LTS

Expérimental0%

Stable89%

Stable90%

[État](</fr/cli/status>), [Santé](</fr/cli/health>), [Journaux](</fr/cli/logs>), [Diagnostics](</fr/gateway/diagnostics>)

Doctor 10 capacités / pris en charge par LTS

Expérimental0%

Stable89%

Stable90%

[Doctor](</fr/cli/doctor>), [Doctor](</fr/gateway/doctor>), [Secrets](</fr/gateway/secrets>), [Dépannage](</fr/gateway/troubleshooting>)

Mises à jour et montées de version 5 capacités / pris en charge par LTS

Expérimental0%

Bêta75%

Stable89%

[Mise à jour](</fr/install/updating>), [Mettre à jour](</fr/cli/update>), [Dépannage](</fr/gateway/troubleshooting>)

Runtime Gateway - M4 Stable - 13 domaines

L’architecture de base, l’authentification, l’appairage, la documentation du protocole, la documentation du daemon et les runbooks CLI sont étendus et à jour.

Couverture Expérimental - 6%Qualité Stable - 81%Exhaustivité Stable - 89%Partiel - 12

Approbations et exécution à distance 6 capacités / pris en charge par LTS

Expérimental0%

Bêta75%

Stable89%

[Protocole](</fr/gateway/protocol>), [Index](</fr/gateway/security>)

API HTTP 4 capacités / pris en charge par LTS

Expérimental25%

Stable90%

Stable90%

[Index](</fr/gateway>), [API HTTP Openai](</fr/gateway/openai-http-api>), [API HTTP Openresponses](</fr/gateway/openresponses-http-api>), [API HTTP Tools Invoke](</fr/gateway/tools-invoke-http-api>), [Hooks](</fr/automation/hooks>), [Index](</fr/web>)

Surface Web hébergée 4 capacités / pris en charge par LTS

Expérimental0%

Stable89%

Stable90%

[Index](</fr/gateway>), [Architecture](</fr/concepts/architecture>), [IU de contrôle](</fr/web/control-ui>), [Webchat](</fr/web/webchat>), [Canvas](</fr/refactor/canvas>)

API RPC et événements du Gateway 20 capacités / pris en charge par LTS

Expérimental9%

Stable90%

Stable90%

[Protocole](</fr/gateway/protocol>), [Index](</fr/gateway>), [Architecture](</fr/concepts/architecture>)

Authentification des appareils et appairage 10 capacités / pris en charge par LTS

Expérimental0%

Bêta75%

Stable89%

[Protocole](</fr/gateway/protocol>), [Appairage](</fr/gateway/pairing>), [Index](</fr/gateway/security>)

Accès réseau et découverte 6 capacités / pris en charge par LTS

Expérimental0%

Bêta75%

Stable89%

[Index](</fr/gateway>), [Découverte](</fr/gateway/discovery>), [Protocole](</fr/gateway/protocol>)

Nœuds et capacités à distance 8 capacités

Expérimental0%

Bêta75%

Stable89%

[Protocole](</fr/gateway/protocol>), [Architecture](</fr/concepts/architecture>), [Index](</fr/nodes>)

Santé, diagnostics et réparation 7 capacités / pris en charge par LTS

Expérimental0%

Bêta75%

Stable89%

[Index](</fr/gateway>), [Diagnostics](</fr/gateway/diagnostics>), [Doctor](</fr/gateway/doctor>)

Compatibilité du protocole 7 capacités / pris en charge en LTS

Expérimental0%

Bêta75%

Stable89%

[Protocole](</fr/gateway/protocol>), [Architecture](</fr/concepts/architecture>), [Typebox](</fr/concepts/typebox>), [Protocole Bridge](</fr/gateway/bridge-protocol>)

Rôles et autorisations 5 capacités / pris en charge en LTS

Expérimental0%

Bêta75%

Stable89%

[Protocole](</fr/gateway/protocol>), [Index](</fr/gateway/security>)

Cycle de vie du Gateway 7 capacités / pris en charge en LTS

Expérimental33%

Stable90%

Stable90%

[Index](</fr/gateway>), [Architecture](</fr/concepts/architecture>)

Contrôles de sécurité 6 capacités / pris en charge en LTS

Expérimental0%

Bêta75%

Stable89%

[Index](</fr/gateway/security>), [Protocole](</fr/gateway/protocol>), [Découverte](</fr/gateway/discovery>)

Connexion WebSocket 8 capacités / pris en charge en LTS

Expérimental13%

Stable90%

Stable90%

[Protocole](</fr/gateway/protocol>), [Architecture](</fr/concepts/architecture>)

Exécution de l’agent - M3 Beta - 9 domaines

La boucle principale, les modèles, le routage des fournisseurs et le streaming d’outils sont des éléments de premier ordre, mais le comportement des fournisseurs change chaque semaine et nécessite une preuve par scénario pour chaque version.

Couverture expérimentale - 33%Qualité Beta - 78%Complétude Beta - 79%Partiel - 6

Exécution d’un tour d’agent 3 capacités / pris en charge par LTS

Expérimental29%

Bêta79%

Bêta79%

[Boucle d’agent](</fr/concepts/agent-loop>), [Agent](</fr/cli/agent>), [Environnements d’exécution d’agent](</fr/concepts/agent-runtimes>)

Environnements d’exécution externes et sous-agents 4 capacités

Expérimental30%

Bêta79%

Bêta79%

[Environnements d’exécution d’agent](</fr/concepts/agent-runtimes>), [Anthropic](</fr/providers/anthropic>), [Google](</fr/providers/google>), [Sous-agents](</fr/tools/subagents>)

Exécution via fournisseurs hébergés 5 capacités / pris en charge par LTS

Expérimental20%

Bêta79%

Bêta79%

[Openai](</fr/providers/openai>), [Anthropic](</fr/providers/anthropic>), [Google](</fr/providers/google>), [Modèles](</fr/concepts/models>)

Fournisseurs locaux et auto-hébergés 5 capacités

Expérimental0%

Alpha68%

Bêta79%

[Ollama](</fr/providers/ollama>), [Modèles](</fr/concepts/models>), [Agent](</fr/cli/agent>)

Sélection du modèle et de l’environnement d’exécution 4 capacités / pris en charge par LTS

Expérimental25%

Bêta79%

Bêta79%

[Modèles](</fr/concepts/models>), [Modèles](</fr/cli/models>), [Openai](</fr/providers/openai>), [Environnements d’exécution d’agent](</fr/concepts/agent-runtimes>)

Authentification du fournisseur 10 capacités / pris en charge par LTS

Expérimental24%

Bêta79%

Bêta79%

[Modèles](</fr/concepts/models>), [Agent](</fr/cli/agent>), [Modèles](</fr/cli/models>), [Openai](</fr/providers/openai>), [Anthropic](</fr/providers/anthropic>), [Google](</fr/providers/google>), [Sous-agents](</fr/tools/subagents>)

Diffusion en continu et progression 2 capacités

Alpha56%

Bêta79%

Bêta79%

[Diffusion en continu](</fr/concepts/streaming>), [Boucle d’agent](</fr/concepts/agent-loop>)

Appels d’outils et traitement des réponses 3 capacités / pris en charge par LTS

Alpha65%

Bêta79%

Bêta79%

[Boucle d’agent](</fr/concepts/agent-loop>), [Ollama](</fr/providers/ollama>)

Contrôles d’exécution des outils 6 capacités / pris en charge par LTS

Alpha50%

Bêta79%

Bêta79%

[Bac à sable vs politique des outils vs mode élevé](</fr/gateway/sandbox-vs-tool-policy-vs-elevated>), [Boucle de l’agent](</fr/concepts/agent-loop>), [Sous-agents](</fr/tools/subagents>)

Session, memory, and context engine - M3 Beta - 9 areas

Documentation solide et implémentation active. La maturité dépend de la durabilité des transcriptions, de la qualité de la compaction et de la parité entre clients.

Couverture expérimentale - 30%Qualité bêta - 77%Complétude bêta - 79%Partiel - 6

Gestion des sessions CLI et des transcriptions 2 capacités / compatible LTS

Expérimental0%

Alpha68%

Bêta79%

[Session](</fr/concepts/session>), [Compaction de gestion des sessions](</fr/reference/session-management-compaction>), [Sessions](</fr/cli/sessions>)

Gestion des jetons 3 capacités / compatible LTS

Expérimental20%

Bêta79%

Bêta79%

[Compaction](</fr/concepts/compaction>), [Contexte](</fr/concepts/context>), [Compaction de gestion des sessions](</fr/reference/session-management-compaction>)

Moteur de contexte 2 capacités / compatible LTS

Alpha57%

Bêta79%

Bêta79%

[Contexte](</fr/concepts/context>), [Moteur de contexte](</fr/concepts/context-engine>), [Harnais du moteur de contexte Codex](</fr/plan/codex-context-engine-harness>)

Historique interclients et parité des sessions 2 capacités

Expérimental40%

Bêta79%

Bêta79%

[Chat web](</fr/web/webchat>), [Android](</fr/platforms/android>), [Routage des canaux](</fr/channels/channel-routing>)

Diagnostics, maintenance et récupération 3 capacités

Expérimental40%

Bêta79%

Bêta79%

[Diagnostics](</fr/gateway/diagnostics>), [Compaction de gestion des sessions](</fr/reference/session-management-compaction>), [Indicateurs](</fr/diagnostics/flags>)

Prompts et contexte principaux 2 capacités / compatible LTS

Expérimental38%

Bêta79%

Bêta79%

[Contexte](</fr/concepts/context>), [Hygiène des transcriptions](</fr/reference/transcript-hygiene>), [Discord](</fr/channels/discord>)

Mémoire 5 capacités

Expérimental46%

Bêta79%

Bêta79%

[Configuration de la mémoire](</fr/reference/memory-config>), [Qmd de mémoire](</fr/concepts/memory-qmd>), [Mémoire](</fr/concepts/memory>), [Discord](</fr/channels/discord>)

Routage des sessions 2 capacités / compatible LTS

Expérimental25%

Bêta79%

Bêta79%

[Session](</fr/concepts/session>), [Routage des canaux](</fr/channels/channel-routing>), [Discord](</fr/channels/discord>)

Persistance des transcriptions 2 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Bêta79%

[Compaction de la gestion des sessions](</fr/reference/session-management-compaction>), [Hygiène des transcriptions](</fr/reference/transcript-hygiene>)

Cadre de canaux - Bêta M3 - 8 domaines

De nombreux canaux partagent les contrats de livraison et de routage du Gateway, mais le comportement des canaux varie selon les contraintes de l’API amont et de la politique de compte.

Couverture expérimentale - 13 %Qualité bêta - 76 %Complétude bêta - 79 %Partiel - 5

Commandes d’actions de canal et approbations 5 capacités

Expérimental0%

Bêta79%

Bêta79%

[Groupes](</fr/channels/groups>), [Discord](</fr/channels/discord>), [Googlechat](</fr/channels/googlechat>), [Signal](</fr/channels/signal>), [Matrix](</fr/channels/matrix>)

Configuration des canaux 5 capacités / pris en charge par LTS

Expérimental14%

Bêta79%

Bêta79%

[Index](</fr/channels>), [Appairage](</fr/channels/pairing>), [Dépannage](</fr/channels/troubleshooting>), [Plugins de canal SDK](</fr/plugins/sdk-channel-plugins>)

Comportement des fils de groupe et des salons ambiants 5 capacités

Expérimental36%

Bêta79%

Bêta79%

[Groupes](</fr/channels/groups>), [Messages de groupe](</fr/channels/group-messages>), [Événements de salon ambiant](</fr/channels/ambient-room-events>), [Groupes de diffusion](</fr/channels/broadcast-groups>), [Discord](</fr/channels/discord>)

Accès entrant et contrôles d’identité 5 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Bêta79%

[Groupes d’accès](</fr/channels/access-groups>), [Groupes](</fr/channels/groups>), [Discord](</fr/channels/discord>), [LINE](</fr/channels/line>)

Pièces jointes multimédias et données de canal enrichies 4 capacités

Expérimental0%

Alpha68%

Bêta79%

[LINE](</fr/channels/line>), [Signal](</fr/channels/signal>), [Googlechat](</fr/channels/googlechat>), [Matrix](</fr/channels/matrix>), [Discord](</fr/channels/discord>)

Distribution sortante et pipeline de réponse 4 capacités / pris en charge par LTS

Expérimental38%

Bêta79%

Bêta79%

[Groupes](</fr/channels/groups>), [Événements de salon ambiant](</fr/channels/ambient-room-events>), [Discord](</fr/channels/discord>), [Matrix](</fr/channels/matrix>), [Canaux de configuration](</fr/gateway/config-channels>)

Routage et distribution des conversations 10 capacités / pris en charge par LTS

Expérimental19%

Bêta79%

Bêta79%

[Routage des canaux](</fr/channels/channel-routing>), [Groupes](</fr/channels/groups>), [Discord](</fr/channels/discord>), [Matrix](</fr/channels/matrix>), [Dépannage](</fr/channels/troubleshooting>), [Référence de configuration](</fr/gateway/configuration-reference>)

État de santé et contrôles opérateur 4 capacités / pris en charge par LTS

Expérimental0%

Bêta79%

Bêta79%

[Santé](</fr/gateway/health>), [Référence de configuration](</fr/gateway/configuration-reference>), [Dépannage](</fr/channels/troubleshooting>), [Discord](</fr/channels/discord>)

Observability - M3 Beta - 5 areas

La documentation sur OTel, Prometheus, la journalisation et les diagnostics existe. Nécessite une revue publique de maturité « ce que les opérateurs doivent examiner en premier ».

Couverture Expérimental - 18%Qualité Bêta - 75%Complétude Bêta - 79%Partiel - 3

Santé et réparation 12 capacités / pris en charge par LTS

Expérimental28%

Bêta79%

Bêta79%

[Santé](</fr/gateway/health>), [Telegram](</fr/channels/telegram>), [Doctor](</fr/cli/doctor>), [Doctor](</fr/gateway/doctor>), [Sous-chemins du SDK](</fr/plugins/sdk-subpaths>), [Santé](</fr/cli/health>), [Protocole](</fr/gateway/protocol>)

Journalisation 5 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Bêta79%

[Journalisation](</fr/logging>), [Journalisation](</fr/gateway/logging>), [Journaux](</fr/cli/logs>)

Collecte de diagnostics 8 capacités

Expérimental30%

Bêta79%

Bêta79%

[Diagnostics](</fr/gateway/diagnostics>), [Santé](</fr/gateway/health>), [Harnais Codex](</fr/plugins/codex-harness>), [Protocole](</fr/gateway/protocol>)

Export de télémétrie 13 capacités

Expérimental33%

Bêta79%

Bêta79%

[Hooks](</fr/plugins/hooks>), [Opentelemetry](</fr/gateway/opentelemetry>), [Journalisation](</fr/logging>), [Sous-chemins du SDK](</fr/plugins/sdk-subpaths>), [Diagnostics Otel](</fr/plugins/reference/diagnostics-otel>), [Prometheus](</fr/gateway/prometheus>), [Diagnostics Prometheus](</fr/plugins/reference/diagnostics-prometheus>)

Diagnostics de session 4 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Bêta79%

[Opentelemetry](</fr/gateway/opentelemetry>), [Prometheus](</fr/gateway/prometheus>), [Diagnostics](</fr/gateway/diagnostics>), [Protocole](</fr/gateway/protocol>)

Application Web Gateway - M3 Bêta - 6 domaines

L’interface Web est documentée avec les flux d’association, de chat, de PWA, de Talk, de notifications push et de Gateway distant. Promouvoir après les tableaux de bord inter-navigateurs et mobile-PWA.

Couverture Expérimental - 4%Qualité Bêta - 74%Complétude Bêta - 79%Aucun

Conversation en temps réel dans le navigateur 5 capacités

Expérimental0%

Alpha68%

Bêta79%

[UI de contrôle](</fr/web/control-ui>), [Protocole](</fr/gateway/protocol>), [Talk](</fr/nodes/talk>)

Accès au navigateur et confiance 5 capacités

Expérimental0%

Alpha68%

Bêta79%

[UI de contrôle](</fr/web/control-ui>), [Tableau de bord](</fr/web/dashboard>), [Tailscale](</fr/gateway/tailscale>), [Accès à distance](</fr/gateway/remote>)

Configuration 5 capacités

Expérimental0%

Alpha68%

Bêta79%

[UI de contrôle](</fr/web/control-ui>), [Configuration](</fr/gateway/configuration>)

UI du navigateur 10 capacités

Expérimental8%

Bêta79%

Bêta79%

[UI de contrôle](</fr/web/control-ui>), [Index](</fr/web>), [Tableau de bord](</fr/web/dashboard>), [Protocole](</fr/gateway/protocol>)

Conversations WebChat 15 capacités

Expérimental10%

Bêta79%

Bêta79%

[UI de contrôle](</fr/web/control-ui>), [Webchat](</fr/web/webchat>), [Bien démarrer](</fr/start/getting-started>), [Routage des canaux](</fr/channels/channel-routing>), [Opérations sécurisées sur les fichiers](</fr/gateway/security/secure-file-operations>)

Console opérateur 10 capacités

Expérimental8%

Bêta79%

Bêta79%

[UI de contrôle](</fr/web/control-ui>), [Santé](</fr/gateway/health>), [Protocole](</fr/gateway/protocol>), [Tableau de bord](</fr/web/dashboard>)

Plugins - M3 Bêta - 9 domaines

Une documentation étendue et de solides preuves d’exécution internes existent pour les manifestes, la découverte, le chargement, l’architecture des fournisseurs/outils et les limites d’approbation. Gardez la ligne en bêta jusqu’à ce que les preuves concernant l’API SDK publique, les sous-chemins et la distribution externe soient plus solides.

Couverture Expérimental - 12%Qualité Bêta - 72%Exhaustivité Bêta - 79%Partiel - 7

Création et empaquetage de plugins 8 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Beta79%

[Créer des plugins](</fr/plugins/building-plugins>), [Vue d’ensemble du SDK](</fr/plugins/sdk-overview>), [Points d’entrée du SDK](</fr/plugins/sdk-entrypoints>), [Sous-chemins du SDK](</fr/plugins/sdk-subpaths>), [Manifeste](</fr/plugins/manifest>), [Référence](</fr/plugins/reference>)

Plugins groupés 5 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Beta79%

[Inventaire des plugins](</fr/plugins/plugin-inventory>), [Plugins](</fr/cli/plugins>), [Architecture interne](</fr/plugins/architecture-internals>)

Plugin Canvas 6 capacités

Expérimental0%

Alpha68%

Beta79%

[Canvas](</fr/plugins/reference/canvas>), [Canvas](</fr/refactor/canvas>), [Référence de configuration](</fr/gateway/configuration-reference>)

Installation et exécution des plugins 6 capacités / pris en charge par LTS

Expérimental35%

Beta79%

Beta79%

[Architecture](</fr/plugins/architecture>), [Architecture interne](</fr/plugins/architecture-internals>), [Plugins](</fr/cli/plugins>)

Plugins de canal 5 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Beta79%

[Plugins de canal du SDK](</fr/plugins/sdk-channel-plugins>), [Entrant de canal du SDK](</fr/plugins/sdk-channel-inbound>), [Sortant de canal du SDK](</fr/plugins/sdk-channel-outbound>)

Plugins de fournisseurs et d’outils 6 capacités / pris en charge par LTS

Expérimental43%

Beta79%

Beta79%

[Plugins de fournisseurs du SDK](</fr/plugins/sdk-provider-plugins>), [Plugins d’outils](</fr/plugins/tool-plugins>), [Ajout de capacités](</fr/plugins/adding-capabilities>)

Approbations de plugins 6 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Beta79%

[Demandes d’autorisation des plugins](</fr/plugins/plugin-permission-requests>), [Approbations d’exécution](</fr/tools/exec-approvals>), [Plugins de canal du SDK](</fr/plugins/sdk-channel-plugins>)

Publication de plugins 6 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Bêta79%

[Plugins](</fr/cli/plugins>), [Compatibilité](</fr/plugins/compatibility>), [Publication](</fr/clawhub/publishing>)

Test des plugins 6 capacités

Expérimental27%

Bêta79%

Bêta79%

[Tests du SDK](</fr/plugins/sdk-testing>), [Configuration du SDK](</fr/plugins/sdk-setup>), [Harnais Codex](</fr/plugins/codex-harness>)

Sécurité, authentification, appairage et secrets - M3 Bêta - 6 domaines

Une bonne documentation et des surfaces de durcissement existent. Promouvoir après que des exécutions régulières de scénarios de mise à niveau et de sécurité ont prouvé l'absence de régressions de configuration.

Couverture Expérimentale - 16%Qualité Bêta - 72%Complétude Bêta - 79%Partiel - 5

Politique d'approbation et protections des outils 2 capacités / prises en charge LTS

Alpha50%

Bêta79%

Bêta79%

[Approbations d'exécution](</fr/tools/exec-approvals>), [Approbations](</fr/cli/approvals>), [Demandes d'autorisations de Plugin](</fr/plugins/plugin-permission-requests>), [Contrôles d'audit](</fr/gateway/security/audit-checks>)

Authentification du Gateway et accès à distance 9 capacités / prises en charge LTS

Expérimental0%

Alpha68%

Bêta79%

[Index](</fr/gateway/security>), [Runbook d'exposition](</fr/gateway/security/exposure-runbook>), [Authentification par proxy approuvé](</fr/gateway/trusted-proxy-auth>), [Tailscale](</fr/gateway/tailscale>), [À distance](</fr/gateway/remote>), [Référence de configuration](</fr/gateway/configuration-reference>), [Gateway](</fr/cli/gateway>), [Doctor](</fr/cli/doctor>), [Interface de contrôle](</fr/web/control-ui>), [Contrôle du navigateur](</fr/tools/browser-control>), [Contrôles d'audit](</fr/gateway/security/audit-checks>)

Contrôle d'accès aux canaux 3 capacités / prises en charge LTS

Expérimental0%

Alpha68%

Bêta79%

[Appairage](</fr/channels/pairing>), [Telegram](</fr/channels/telegram>), [Groupes d'accès](</fr/channels/access-groups>), [Contrôles d'audit](</fr/gateway/security/audit-checks>)

Appairage des appareils et de Node 11 capacités / prises en charge LTS

Expérimental0%

Alpha68%

Bêta79%

[Protocole](</fr/gateway/protocol>), [Appareils](</fr/cli/devices>), [Appairage](</fr/channels/pairing>), [Appairage](</fr/gateway/pairing>), [Portées opérateur](</fr/gateway/operator-scopes>), [Interface de contrôle](</fr/web/control-ui>), [Webchat](</fr/web/webchat>), [Approbations](</fr/cli/approvals>)

Confiance des Plugin 2 capacités

Expérimental0%

Alpha68%

Bêta79%

[Manifeste](</fr/plugins/manifest>), [Demandes d'autorisations de Plugin](</fr/plugins/plugin-permission-requests>), [Gérer les Plugin](</fr/plugins/manage-plugins>), [Contrôles d'audit](</fr/gateway/security/audit-checks>)

Hygiène des identifiants et des secrets 5 capacités / prises en charge LTS

Expérimental46%

Bêta79%

Bêta79%

[Authentification](</fr/gateway/authentication>), [Modèles](</fr/cli/models>), [Openai](</fr/providers/openai>), [Oauth](</fr/concepts/oauth>), [Secrets](</fr/gateway/secrets>), [Secrets](</fr/cli/secrets>), [Surface d'identifiants Secretref](</fr/reference/secretref-credential-surface>), [Contrôles d'audit](</fr/gateway/security/audit-checks>)

Automatisation : cron, hooks, tâches, polling - M3 Bêta - 6 domaines

Documenté et utilisable, mais la preuve par scénario doit couvrir la livraison sans surveillance, les nouvelles tentatives et la visibilité des échecs.

Couverture Expérimentale - 2%Qualité Bêta - 72%Complétude Bêta - 79%Aucun

Tâches Cron 15 capacités

Expérimental0%

Bêta79%

Bêta79%

[Tâches Cron](</fr/automation/cron-jobs>), [Cron](</fr/cli/cron>), [Protocole](</fr/gateway/protocol>), [Tâches](</fr/automation/tasks>), [Discord](</fr/channels/discord>)

Entrée d’événements 15 capacités

Expérimental0%

Alpha68%

Bêta79%

[Telegram](</fr/channels/telegram>), [Zalo](</fr/channels/zalo>), [Dépannage](</fr/channels/troubleshooting>), [iMessage depuis Bluebubbles](</fr/channels/imessage-from-bluebubbles>), [Intégration Gmail Pubsub](</fr/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</fr/automation/cron-jobs>), [Webhooks](</fr/cli/webhooks>), [Webhooks](</fr/automation/cron-jobs#webhooks>), [Webhook](</fr/automation/cron-jobs>)

Hooks d’automatisation 11 capacités

Expérimental0%

Alpha68%

Bêta79%

[Hooks](</fr/automation/hooks>), [Hooks](</fr/cli/hooks>), [Hooks](</fr/plugins/hooks>), [Demandes d’autorisations de Plugin](</fr/plugins/plugin-permission-requests>), [Sous-chemins SDK](</fr/plugins/sdk-subpaths>)

Tâches et flux en arrière-plan 10 capacités

Expérimental0%

Alpha68%

Bêta79%

[Tâches](</fr/automation/tasks>), [Index](</fr/automation>), [Tâches](</fr/cli/tasks>), [TaskFlow](</fr/automation/taskflow>), [Runtime SDK](</fr/plugins/sdk-runtime>)

Heartbeat 5 capacités

Expérimental14%

Bêta79%

Bêta79%

[Index](</fr/automation>), [Heartbeat](</fr/gateway/heartbeat>), [Engagements](</fr/concepts/commitments>)

Contrôles d’interrogation 10 capacités

Expérimental0%

Alpha68%

Bêta79%

[Interrogation](</fr/cli/message>), [Message](</fr/cli/message>), [Telegram](</fr/channels/telegram>), [Msteams](</fr/channels/msteams>), [Processus en arrière-plan](</fr/gateway/background-process>)

Compréhension des médias et génération de médias - M2 Alpha - 6 domaines

Une large surface de capacités existe, mais les variations selon les fournisseurs, les limites de fichiers et la parité Node/application font que cette surface n’est pas encore stable.

Couverture Expérimental - 2%Qualité Alpha - 64%Exhaustivité Alpha - 68%Aucun

Ingestion et accès aux médias 8 capacités

Expérimental0%

Alpha61%

Alpha68%

[Vue d’ensemble des médias](</fr/tools/media-overview>), [Compréhension des médias](</fr/nodes/media-understanding>), [Opérations sécurisées sur les fichiers](</fr/gateway/security/secure-file-operations>), [PDF](</fr/tools/pdf>), [Génération d’images](</fr/tools/image-generation>), [QR](</fr/cli/qr>), [LINE](</fr/channels/line>), [WhatsApp](</fr/channels/whatsapp>)

Gestion des médias dans les canaux 5 capacités

Expérimental0%

Alpha61%

Alpha68%

[Images](</fr/nodes/images>), [Vue d’ensemble des médias](</fr/tools/media-overview>), [Discord](</fr/channels/discord>)

Configuration des médias 1 capacité

Expérimental0%

Alpha61%

Alpha68%

[Vue d’ensemble des médias](</fr/tools/media-overview>), [Génération d’images](</fr/tools/image-generation>), [Manifeste](</fr/plugins/manifest>), [Harnais Codex](</fr/plugins/codex-harness>)

Livraison de synthèse vocale 2 capacités

Expérimental0%

Alpha61%

Alpha68%

[TTS](</fr/tools/tts>), [Vue d’ensemble des médias](</fr/tools/media-overview>), [Discord](</fr/channels/discord>)

Compréhension des médias 12 capacités

Expérimental7%

Alpha69%

Alpha69%

[Audio](</fr/nodes/audio>), [Compréhension des médias](</fr/nodes/media-understanding>), [Vue d’ensemble des médias](</fr/tools/media-overview>), [WhatsApp](</fr/channels/whatsapp>), [Images](</fr/nodes/images>), [Inférer](</fr/cli/infer>), [PDF](</fr/tools/pdf>)

Génération de médias 17 capacités

Expérimental5%

Alpha69%

Alpha69%

[Génération d’images](</fr/tools/image-generation>), [Vue d’ensemble des médias](</fr/tools/media-overview>), [Skills](</fr/tools/skills>), [Génération de musique](</fr/tools/music-generation>), [Génération de vidéo](</fr/tools/video-generation>)

Voix et conversation en temps réel - M2 Alpha - 6 domaines

Plusieurs implémentations existent dans Control UI, les applications et les fournisseurs. Des tableaux de score de latence, de modes de défaillance et de configuration sont nécessaires avant la bêta.

Couverture Expérimental - 0%Qualité Alpha - 61%Exhaustivité Alpha - 68%Aucun

Fournisseurs de discussion 7 capacités

Expérimental0%

Alpha61%

Alpha68%

[Openai](</fr/providers/openai>), [Google](</fr/providers/google>), [Plugins de fournisseur SDK](</fr/plugins/sdk-provider-plugins>), [Discussion](</fr/nodes/talk>), [UI de contrôle](</fr/web/control-ui>)

Sessions de discussion en temps réel 11 capacités

Expérimental0%

Alpha61%

Alpha68%

[Discussion](</fr/nodes/talk>), [UI de contrôle](</fr/web/control-ui>)

Voix et transcription 5 capacités

Expérimental0%

Alpha61%

Alpha68%

[Discussion](</fr/nodes/talk>), [Openai](</fr/providers/openai>), [Google](</fr/providers/google>)

Discussion dans l’application native 4 capacités

Expérimental0%

Alpha61%

Alpha68%

[Discussion](</fr/nodes/talk>), [Voicewake](</fr/platforms/mac/voicewake>)

Réveil vocal et routage 4 capacités

Expérimental0%

Alpha61%

Alpha68%

[Voicewake](</fr/nodes/voicewake>), [Voicewake](</fr/platforms/mac/voicewake>), [Superposition vocale](</fr/platforms/mac/voice-overlay>)

Observabilité de la discussion 5 capacités

Expérimental0%

Alpha61%

Alpha68%

[UI de contrôle](</fr/web/control-ui>), [Superposition vocale](</fr/platforms/mac/voice-overlay>), [Discussion](</fr/nodes/talk>)

TUI - M2 Alpha - 5 domaines

Présent dans les docs et le source, mais moins visible comme workflow utilisateur principal. Nécessite une définition explicite des scénarios.

Couverture Expérimental - 0%Qualité Alpha - 59%Complétude Alpha - 66%Aucun

Modes d'exécution 14 capacités

Expérimental0%

Alpha59%

Alpha66%

[TUI](</fr/cli/tui>), [TUI](</fr/web/tui>), [Index](</fr/cli>)

Entrée et commandes 8 capacités

Expérimental0%

Alpha59%

Alpha66%

[TUI](</fr/web/tui>)

Gestion des sessions 3 capacités

Expérimental0%

Alpha59%

Alpha66%

[TUI](</fr/web/tui>), [Sessions](</fr/cli/sessions>)

Exécution du shell local 4 capacités

Expérimental0%

Alpha59%

Alpha66%

[TUI](</fr/web/tui>), [TUI](</fr/cli/tui>)

Rendu et sécurité des sorties 4 capacités

Expérimental0%

Alpha59%

Alpha66%

[TUI](</fr/web/tui>), [QR](</fr/cli/qr>), [Journaux](</fr/cli/logs>), [Complétion](</fr/cli/completion>)

ClawHub - M2 Alpha - 4 zones

La documentation publique et le concept d'écosystème existent. Nécessite des fiches d'évaluation pour l'installation, la confiance, la mise à jour, la restauration et la compatibilité.

Couverture Expérimental - 0%Qualité Alpha - 58%Exhaustivité Alpha - 62%Aucun

Publication 7 capacités

Expérimental0%

Alpha54%

Alpha55%

[Publication](</fr/clawhub/publishing>), [Création de Skills](</fr/tools/creating-skills>), [Communauté](</fr/plugins/community>)

Découverte du catalogue 5 capacités

Expérimental0%

Alpha61%

Alpha68%

[Plugin](</fr/tools/plugin>), [Plugins](</fr/cli/plugins>), [Skills](</fr/cli/skills>), [Skills](</fr/tools/skills>), [Communauté](</fr/plugins/community>)

Compatibilité et confiance 12 capacités

Expérimental0%

Alpha55%

Alpha56%

[Plugin](</fr/tools/plugin>), [Plugins](</fr/cli/plugins>), [Compatibilité](</fr/plugins/compatibility>), [Inventaire des Plugins](</fr/plugins/plugin-inventory>), [Publication](</fr/clawhub/publishing>), [Skills](</fr/tools/skills>), [Configuration des Skills](</fr/tools/skills-config>)

Cycle de vie et état des Plugins 26 capacités

Expérimental0%

Alpha61%

Alpha68%

[Plugin](</fr/tools/plugin>), [Plugins](</fr/cli/plugins>), [Skills](</fr/cli/skills>), [Skills](</fr/tools/skills>), [Protocole](</fr/gateway/protocol>), [Bundles](</fr/plugins/bundles>), [Résolution des dépendances](</fr/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 domaines

OpenClaw App SDK est un contrat d'application externe distinct, séparé du runtime Gateway et du Plugin SDK. L'évaluation actuelle montre un vrai parcours `@openclaw/sdk`, avec des lacunes concernant le packaging public, la découverte automatique, les approbations, les assistants et la compatibilité.

Couverture expérimentale - 3%Qualité Alpha - 54%Exhaustivité Alpha - 53%Aucun

API client 4 capacités

Expérimental0%

Alpha51%

Alpha50%

[SDK OpenClaw](</fr/gateway/external-apps>), [Conception de l'API du SDK OpenClaw](</fr/gateway/external-apps>)

Accès au Gateway 5 capacités

Expérimental0%

Alpha53%

Alpha54%

[SDK OpenClaw](</fr/gateway/external-apps>), [Conception de l'API du SDK OpenClaw](</fr/gateway/external-apps>), [Protocole](</fr/gateway/protocol>), [Index](</fr/gateway/security>)

Conversations d'agents 6 capacités

Expérimental0%

Alpha52%

Alpha52%

[SDK OpenClaw](</fr/gateway/external-apps>), [Conception de l'API du SDK OpenClaw](</fr/gateway/external-apps>), [Protocole](</fr/gateway/protocol>)

Événements et approbations 5 capacités

Expérimental0%

Alpha52%

Alpha52%

[SDK OpenClaw](</fr/gateway/external-apps>), [Conception de l'API du SDK OpenClaw](</fr/gateway/external-apps>), [Protocole](</fr/gateway/protocol>)

Assistants de ressources 5 capacités

Expérimental17%

Alpha62%

Alpha53%

[SDK OpenClaw](</fr/gateway/external-apps>), [Conception de l'API du SDK OpenClaw](</fr/gateway/external-apps>)

Compatibilité 5 capacités

Expérimental0%

Alpha54%

Alpha55%

[Conception de l'API du SDK OpenClaw](</fr/gateway/external-apps>), [Typebox](</fr/concepts/typebox>), [Protocole](</fr/gateway/protocol>)

### Plateforme

Hôte Gateway Linux - M4 stable - 5 domaines

L'environnement d'exécution Node est recommandé, le service utilisateur systemd est documenté, et les recommandations pour VPS/conteneurs sont étendues.

Couverture expérimentale - 0%Qualité bêta - 75%Exhaustivité stable - 89%Partiel - 4

Configuration et mises à jour de l’hôte 4 capacités / prise en charge LTS

Expérimental0%

Bêta75%

Stable89%

[Index](</fr/install>), [Mise à jour](</fr/install/updating>), [Linux](</fr/platforms/linux>), [Index](</fr/platforms>)

Runtime Gateway et contrôle du service 6 capacités / prise en charge LTS

Expérimental0%

Bêta75%

Stable89%

[Index](</fr/gateway>), [Gateway](</fr/cli/gateway>), [Linux](</fr/platforms/linux>), [VPS](</fr/vps>)

Accès distant et sécurité 6 capacités / prise en charge LTS

Expérimental0%

Bêta75%

Stable89%

[Accès distant](</fr/gateway/remote>), [Tailscale](</fr/gateway/tailscale>), [Guide opérationnel d’exposition](</fr/gateway/security/exposure-runbook>), [Authentification](</fr/gateway/authentication>), [Secrets](</fr/gateway/secrets>)

Diagnostics et réparation 4 capacités / prise en charge LTS

Expérimental0%

Bêta75%

Stable89%

[Statut](</fr/cli/status>), [Journaux](</fr/cli/logs>), [Diagnostic](</fr/cli/doctor>), [Diagnostics](</fr/gateway/diagnostics>), [Index](</fr/gateway>)

Cibles de déploiement 3 capacités

Expérimental0%

Bêta75%

Stable89%

[VPS](</fr/vps>), [Docker](</fr/install/docker>), [Hetzner](</fr/install/hetzner>), [Digitalocean](</fr/install/digitalocean>), [Kubernetes](</fr/install/kubernetes>), [Podman](</fr/install/podman>)

macOS Gateway host - M4 Stable - 7 areas

Le chemin du service LaunchAgent, les modes Gateway local et distant, l’installation de la CLI et l’intégration à l’application sont documentés.

Couverture expérimentale - 0%Qualité bêta - 74%Complétude stable - 88%Aucune

Configuration CLI 4 capacités

Expérimental0%

Bêta74%

Stable88%

[Macos](</fr/platforms/macos>), [Gateway intégré](</fr/platforms/mac/bundled-gateway>), [Installateur](</fr/install/installer>), [Node](</fr/install/node>)

Intégration du Gateway local 9 capacités

Expérimental0%

Bêta74%

Stable88%

[Macos](</fr/platforms/macos>), [Gateway intégré](</fr/platforms/mac/bundled-gateway>), [Distant](</fr/platforms/mac/remote>), [Index](</fr/gateway>), [Gateway](</fr/cli/gateway>), [Bonjour](</fr/gateway/bonjour>)

Mode Gateway distant 5 capacités

Expérimental0%

Bêta74%

Stable88%

[Distant](</fr/platforms/mac/remote>), [Distant](</fr/gateway/remote>), [Tailscale](</fr/gateway/tailscale>)

Cycle de vie du service Gateway 10 capacités

Expérimental0%

Bêta74%

Stable88%

[Macos](</fr/platforms/macos>), [Gateway intégré](</fr/platforms/mac/bundled-gateway>), [Gateway](</fr/cli/gateway>), [Index](</fr/gateway>), [Mise à jour](</fr/cli/update>), [Mise à jour](</fr/install/updating>), [Désinstallation](</fr/install/uninstall>), [Dépannage](</fr/gateway/troubleshooting>)

Diagnostics et observabilité 4 capacités

Expérimental0%

Bêta74%

Stable88%

[Gateway intégré](</fr/platforms/mac/bundled-gateway>), [Macos](</fr/platforms/macos>), [Gateway](</fr/cli/gateway>), [Doctor](</fr/gateway/doctor>), [Dépannage](</fr/gateway/troubleshooting>)

Autorisations et capacités natives 4 capacités

Expérimental0%

Bêta74%

Stable88%

[Macos](</fr/platforms/macos>), [Distant](</fr/platforms/mac/remote>)

Profils et isolation 5 capacités

Expérimental0%

Bêta74%

Stable88%

[Gateways multiples](</fr/gateway/multiple-gateways>), [Index](</fr/gateway>), [Gateway](</fr/cli/gateway>)

Hébergement Docker et Podman - M3 Bêta - 4 domaines

La documentation d’installation existe et ces chemins de déploiement sont courants. À promouvoir après que les tests smoke de publication récurrents auront capturé le comportement de mise à niveau et des volumes.

Couverture Expérimental - 7%Qualité Bêta - 71%Exhaustivité Bêta - 79%Aucun

Configuration du conteneur 6 capacités

Expérimental0%

Alpha68%

Beta79%

[Docker](</fr/install/docker>), [Podman](</fr/install/podman>)

Opérations de conteneur 11 capacités

Expérimental0%

Alpha68%

Beta79%

[Podman](</fr/install/podman>), [Exécution de VM Docker](</fr/install/docker-vm-runtime>), [Docker](</fr/install/docker>), [Hetzner](</fr/install/hetzner>), [Hostinger](</fr/install/hostinger>)

Publication et validation des images 5 capacités

Expérimental29%

Beta79%

Beta79%

[Docker](</fr/install/docker>), [Exécution de VM Docker](</fr/install/docker-vm-runtime>), [Validation complète de publication](</fr/reference/full-release-validation>)

Bac à sable et outillage de l’agent 3 capacités

Expérimental0%

Alpha68%

Beta79%

[Docker](</fr/install/docker>), [Exécution de VM Docker](</fr/install/docker-vm-runtime>)

Windows via WSL2 - M3 Beta - 6 domaines

Parcours Windows recommandé, avec indications pour systemd/service utilisateur et documentation de la chaîne de démarrage. À promouvoir après des scorecards répétées d’installation/mise à jour.

Couverture Expérimental - 6%Qualité Alpha - 69%Complétude Beta - 79%Partiel - 5

Configuration WSL 6 capacités / prise en charge LTS

Expérimental0%

Alpha67%

Beta79%

[Windows](</fr/platforms/windows>), [Bien démarrer](</fr/start/getting-started>)

CLI 8 capacités / prise en charge LTS

Expérimental0%

Alpha67%

Beta79%

[Windows](</fr/platforms/windows>), [Bien démarrer](</fr/start/getting-started>), [Mise à jour](</fr/install/updating>), [Configuration initiale](</fr/cli/onboard>), [Diagnostic](</fr/cli/doctor>), [État](</fr/cli/status>), [Journaux](</fr/cli/logs>)

Cycle de vie du service Gateway 10 capacités / prise en charge LTS

Expérimental0%

Alpha67%

Beta79%

[Windows](</fr/platforms/windows>), [Index](</fr/gateway>), [Diagnostic](</fr/gateway/doctor>)

Accès et exposition du Gateway 11 capacités / prise en charge LTS

Expérimental0%

Alpha67%

Beta79%

[Authentification](</fr/gateway/authentication>), [Secrets](</fr/gateway/secrets>), [À distance](</fr/gateway/remote>), [Guide opérationnel d’exposition](</fr/gateway/security/exposure-runbook>), [Windows](</fr/platforms/windows>)

Diagnostics et réparation 6 capacités / prise en charge LTS

Expérimental38%

Beta79%

Beta79%

[Windows](</fr/platforms/windows>), [État](</fr/cli/status>), [Journaux](</fr/cli/logs>), [Diagnostic](</fr/cli/doctor>), [Diagnostic](</fr/gateway/doctor>)

Navigateur et interface utilisateur de contrôle 6 capacités

Expérimental0%

Alpha67%

Beta79%

[Dépannage du CDP distant Windows WSL2 pour le navigateur](</fr/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Navigateur](</fr/tools/browser>), [Interface utilisateur de contrôle](</fr/web/control-ui>)

Raspberry Pi et petits appareils Linux - M3 Beta - 4 domaines

La documentation de la plateforme existe et le chemin Gateway est basé sur Linux. Une preuve de smoke test de version propre au matériel est nécessaire pour passer au niveau supérieur.

Couverture Expérimental - 0%Qualité Alpha - 67%Exhaustivité Beta - 79%Aucune

Configuration et compatibilité 12 capacités

Expérimental0%

Alpha67%

Bêta79%

[Raspberry Pi](</fr/install/raspberry-pi>), [Index](</fr/install>), [FAQ première exécution](</fr/help/faq-first-run>), [FAQ](</fr/help/faq>), [Linux](</fr/platforms/linux>), [Programme d’installation](</fr/install/installer>)

Accès distant et authentification 9 capacités

Expérimental0%

Alpha67%

Bêta79%

[Raspberry Pi](</fr/install/raspberry-pi>), [Authentification](</fr/gateway/authentication>), [Secrets](</fr/gateway/secrets>), [Association](</fr/gateway/pairing>), [Appareils](</fr/cli/devices>), [Distant](</fr/gateway/remote>), [Tailscale](</fr/gateway/tailscale>)

Runtime du Gateway 10 capacités

Expérimental0%

Alpha67%

Bêta79%

[Index](</fr/gateway>), [Gateway](</fr/cli/gateway>), [Raspberry Pi](</fr/install/raspberry-pi>), [Linux](</fr/platforms/linux>), [Vps](</fr/vps>)

Performances et diagnostics 5 capacités

Expérimental0%

Alpha67%

Bêta79%

[Raspberry Pi](</fr/install/raspberry-pi>), [Linux](</fr/platforms/linux>), [État de santé](</fr/gateway/health>), [Diagnostics](</fr/gateway/diagnostics>)

Application compagnon macOS - M3 Bêta - 8 domaines

L’application riche de barre de menus, les autorisations, le mode Node, Canvas, le réveil vocal, WebChat et le mode distant existent. L’ensemble évolue encore assez rapidement pour éviter Stable.

Couverture Expérimental - 0%Qualité Alpha - 66%Complétude Bêta - 78%Aucune

Canvas 4 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[Canvas](</fr/platforms/mac/canvas>), [Macos](</fr/platforms/macos>), [Webchat](</fr/web/webchat>)

Configuration locale 7 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[Gateway groupé](</fr/platforms/mac/bundled-gateway>), [Macos](</fr/platforms/macos>), [Processus enfant](</fr/platforms/mac/child-process>), [Configuration de développement](</fr/platforms/mac/dev-setup>)

État et paramètres 5 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[Barre de menus](</fr/platforms/mac/menu-bar>), [Icône](</fr/platforms/mac/icon>), [Macos](</fr/platforms/macos>), [Santé](</fr/platforms/mac/health>), [Journalisation](</fr/platforms/mac/logging>), [Distant](</fr/platforms/mac/remote>)

Fonctionnalités natives 5 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[Macos](</fr/platforms/macos>), [Xpc](</fr/platforms/mac/xpc>), [Autorisations](</fr/platforms/mac/permissions>), [Signature](</fr/platforms/mac/signing>), [Peekaboo](</fr/platforms/mac/peekaboo>)

Connexions distantes 3 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[Distant](</fr/platforms/mac/remote>), [Macos](</fr/platforms/macos>), [Distant](</fr/gateway/remote>)

Voix et conversation 3 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[Voicewake](</fr/platforms/mac/voicewake>), [Superposition vocale](</fr/platforms/mac/voice-overlay>), [Conversation](</fr/nodes/talk>), [Macos](</fr/platforms/macos>)

WebChat 3 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[Webchat](</fr/platforms/mac/webchat>), [Macos](</fr/platforms/macos>), [Webchat](</fr/web/webchat>)

WebChat distant 5 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[Webchat](</fr/platforms/mac/webchat>), [Distant](</fr/gateway/remote>), [Distant](</fr/platforms/mac/remote>)

Android app - M2 Alpha - 7 areas

Le parcours public Google Play existe, mais la documentation de l’application décrit encore la reconstruction comme extrêmement alpha et signale le travail de durcissement de la version.

Couverture expérimentale - 0%Qualité alpha - 59%Complétude alpha - 66%Aucun

Capture multimédia 1 capacité

Expérimental0%

Alpha59%

Alpha66%

[Android](</fr/platforms/android>), [Caméra](</fr/nodes/camera>)

Chat mobile 1 capacité

Expérimental0%

Alpha59%

Alpha66%

[Android](</fr/platforms/android>)

Configuration de la connexion 1 capacité

Expérimental0%

Alpha59%

Alpha66%

[Android](</fr/platforms/android>), [Bonjour](</fr/gateway/bonjour>), [Appairage](</fr/gateway/pairing>)

Distribution 3 capacités

Expérimental0%

Alpha59%

Alpha66%

[Android](</fr/platforms/android>)

Paramètres 1 capacité

Expérimental0%

Alpha59%

Alpha66%

[Android](</fr/platforms/android>)

Voix 1 capacité

Expérimental0%

Alpha59%

Alpha66%

[Android](</fr/platforms/android>), [Parler](</fr/nodes/talk>)

Runtime de l’appareil 2 capacités

Expérimental0%

Alpha59%

Alpha66%

[Android](</fr/platforms/android>), [Dépannage](</fr/nodes/troubleshooting>), [Protocole](</fr/gateway/protocol>)

Windows natif - M2 Alpha - 4 domaines

Les flux principaux CLI/Gateway fonctionnent, mais la documentation recommande toujours WSL2 pour l’expérience complète et répertorie les réserves propres au mode natif.

Couverture Expérimental - 0%Qualité Alpha - 58%Exhaustivité Alpha - 66%Partiel - 1

CLI 9 capacités / prises en charge LTS

Expérimental0%

Alpha54%

Alpha64%

[Index](</fr/install>), [Programme d’installation](</fr/install/installer>), [Windows](</fr/platforms/windows>), [Premiers pas](</fr/start/getting-started>), [Onboard](</fr/cli/onboard>)

Gestion du Gateway 11 capacités

Expérimental0%

Alpha59%

Alpha66%

[Windows](</fr/platforms/windows>), [Index](</fr/gateway>), [Gateway](</fr/cli/gateway>), [Doctor](</fr/cli/doctor>)

Mise en réseau 4 capacités

Expérimental0%

Alpha59%

Alpha66%

[Windows](</fr/platforms/windows>), [Index](</fr/gateway>), [Gateway](</fr/cli/gateway>)

Mises à jour 4 capacités

Expérimental0%

Alpha59%

Alpha66%

[Mise à jour](</fr/install/updating>), [CI](</fr/ci>)

Hébergement Kubernetes - M2 Alpha - 4 domaines

L’hébergement Kubernetes est un chemin de déploiement de cluster distinct basé sur Kustomize. La notation actuelle montre un véritable chemin de déploiement minimal, avec des lacunes concernant la CI propre à Kubernetes, le packaging ingress/TLS/NetworkPolicy, la sauvegarde/restauration et le renforcement de l’exposition en production.

Couverture expérimentale - 0 %Qualité Alpha - 55 %Complétude Alpha - 61 %Aucun

Configuration du déploiement 5 fonctionnalités

Expérimental0 %

Alpha55 %

Alpha61 %

[Kubernetes](</fr/install/kubernetes>), [Index](</fr/install>)

Configuration et secrets 5 fonctionnalités

Expérimental0 %

Alpha55 %

Alpha61 %

[Kubernetes](</fr/install/kubernetes>), [Secrets](</fr/gateway/secrets>), [Environnement](</fr/help/environment>)

Accès et exposition 5 fonctionnalités

Expérimental0 %

Alpha55 %

Alpha61 %

[Kubernetes](</fr/install/kubernetes>), [Authentification](</fr/gateway/authentication>), [À distance](</fr/gateway/remote>), [Runbook d’exposition](</fr/gateway/security/exposure-runbook>)

Cycle de vie du cluster 5 fonctionnalités

Expérimental0 %

Alpha55 %

Alpha61 %

[Kubernetes](</fr/install/kubernetes>), [Index](</fr/gateway>)

Application iOS - M1 expérimental - 8 domaines

Aperçu interne / super-alpha. Les flux TestFlight et de push appuyés par relais existent, mais il n’y a pas encore de distribution publique.

Couverture expérimentale - 0%Qualité expérimentale - 41%Exhaustivité expérimentale - 44%Aucun

Médias et partage 1 capacité

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>), [Caméra](</fr/nodes/camera>)

Canvas et écran 1 capacité

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>), [Canvas](</fr/plugins/reference/canvas>)

Chat et sessions 1 capacité

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>), [Chat web](</fr/web/webchat>), [Protocole](</fr/gateway/protocol>)

Configuration et diagnostics du Gateway 7 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>), [Jumelage](</fr/channels/pairing>)

Distribution 1 capacité

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>)

Commandes de l’appareil 2 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>), [Protocole](</fr/gateway/protocol>)

Notifications et arrière-plan 1 capacité

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>), [Configuration](</fr/gateway/configuration>)

Voix 1 capacité

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>), [Parole](</fr/nodes/talk>)

Chemin d'installation Nix - M1 expérimental - 5 zones

Flux d’installation facultatif. Nécessite une promesse de support plus claire avant la promotion en alpha/bêta.

Couverture expérimentale - 0%Qualité expérimentale - 41%Exhaustivité expérimentale - 44%Aucun

Transfert d’installation 4 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Nix](</fr/install/nix>), [Index](</fr/install>), [Répertoire des docs](</fr/start/docs-directory>)

Cycle de vie des Plugin 4 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Gérer les Plugin](</fr/plugins/manage-plugins>), [Plugin](</fr/tools/plugin>), [Nix](</fr/install/nix>)

Activation et expérience utilisateur de l’application 7 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Nix](</fr/install/nix>)

Configuration et état 7 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Nix](</fr/install/nix>), [Configuration](</fr/cli/setup>), [Environnement](</fr/help/environment>)

Runtime de service et protections 8 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Nix](</fr/install/nix>), [Configuration](</fr/cli/setup>), [Doctor](</fr/cli/doctor>), [Mise à jour](</fr/cli/update>)

surfaces d’accompagnement watchOS - M1 Expérimental - 5 domaines

La source comporte des surfaces d’app/extension Watch ; la documentation publique ne les présente pas encore comme une fonctionnalité utilisateur.

Couverture expérimentale - 0%Qualité expérimentale - 41%Complétude expérimentale - 44%Aucun

Livraison et récupération 7 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>)

Approbations d’exécution 3 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Approbations d’exécution](</fr/tools/exec-approvals>), [Ios](</fr/platforms/ios>)

Distribution et support 6 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>)

Notifications et réponses 7 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>)

Interface utilisateur de l’app Watch 3 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Ios](</fr/platforms/ios>)

Application d’accompagnement Linux - M0 planifié - 5 domaines

La documentation indique que les applications d’accompagnement Linux natives sont prévues ; Gateway est aujourd’hui le chemin Linux pris en charge.

Couverture expérimentale - 0%Qualité expérimentale - 19%Complétude expérimentale - 21%Aucun

Distribution de l’application 3 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Linux](</fr/platforms/linux>), [Index](</fr/platforms>), [Index](</fr/install>)

Connectivité Gateway 4 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Linux](</fr/platforms/linux>), [Index](</fr/gateway>), [Appairage](</fr/gateway/pairing>), [Accès distant](</fr/gateway/remote>)

Chat et sessions 3 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Linux](</fr/platforms/linux>), [Protocole](</fr/gateway/protocol>), [Webchat](</fr/web/webchat>)

Capacités de bureau 9 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Linux](</fr/platforms/linux>), [Approbations d’exécution](</fr/tools/exec-approvals>), [Secrets](</fr/gateway/secrets>), [Index](</fr/nodes>), [Exec](</fr/tools/exec>), [Talk](</fr/nodes/talk>), [Caméra](</fr/nodes/camera>)

État et diagnostics 7 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Linux](</fr/platforms/linux>), [Openclaw](</fr/start/openclaw>), [Doctor](</fr/gateway/doctor>)

Application compagnon native Windows - M0 planifié - 5 domaines

Planifié uniquement.

Couverture expérimentale - 0%Qualité expérimentale - 19%Complétude expérimentale - 21%Aucun

Installation et mises à jour 4 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Windows](</fr/platforms/windows>), [Index](</fr/install>)

Connexion au Gateway 3 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Windows](</fr/platforms/windows>), [Index](</fr/gateway>), [Appairage](</fr/gateway/pairing>), [À distance](</fr/gateway/remote>)

Sessions de chat 2 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Windows](</fr/platforms/windows>), [Protocole](</fr/gateway/protocol>)

État et réparation 5 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Windows](</fr/platforms/windows>), [Doctor](</fr/gateway/doctor>), [Index](</fr/gateway>)

Outils de bureau et autorisations 10 capacités

Expérimental0%

Expérimental19%

Expérimental21%

[Windows](</fr/platforms/windows>), [Index](</fr/nodes>), [Exec](</fr/tools/exec>), [Approbations Exec](</fr/tools/exec-approvals>), [Index](</fr/gateway/security>)

### Canal

Discord - M4 Stable - 6 domaines

Documentation approfondie et large couverture fonctionnelle. Les parcours voix/délégation doivent rester évalués séparément comme bêta/alpha.

Couverture expérimentale - 0%Qualité bêta - 73%Complétude stable - 87%Partiel - 4

Configuration et opérations des canaux 10 capacités / pris en charge par LTS

Expérimental0%

Bêta73%

Stable87%

[Discord](</fr/channels/discord>), [Discord](</fr/plugins/reference/discord>), [Fly](</fr/install/fly>), [Commandes Slash](</fr/tools/slash-commands>), [Santé](</fr/gateway/health>), [Canaux](</fr/cli/channels>), [Canaux de configuration](</fr/gateway/config-channels>)

Accès et identité 6 capacités / pris en charge par LTS

Expérimental0%

Bêta73%

Stable87%

[Discord](</fr/channels/discord>), [Appairage](</fr/channels/pairing>), [Groupes d’accès](</fr/channels/access-groups>), [Groupes](</fr/channels/groups>)

Routage et livraison des conversations 12 capacités / pris en charge par LTS

Expérimental0%

Bêta73%

Stable87%

[Discord](</fr/channels/discord>), [Routage des canaux](</fr/channels/channel-routing>), [Groupes](</fr/channels/groups>), [Groupes d’accès](</fr/channels/access-groups>), [Agents ACP](</fr/tools/acp-agents>), [Sous-agents](</fr/tools/subagents>)

Médias et contenu enrichi 1 capacité / pris en charge par LTS

Expérimental0%

Bêta73%

Stable87%

[Discord](</fr/channels/discord>)

Contrôles natifs et approbations 5 capacités

Expérimental0%

Bêta73%

Stable87%

[Discord](</fr/channels/discord>), [Commandes Slash](</fr/tools/slash-commands>)

Voix et appels en temps réel 5 capacités

Expérimental0%

Bêta73%

Stable87%

[Discord](</fr/channels/discord>), [Openai](</fr/providers/openai>), [Elevenlabs](</fr/providers/elevenlabs>), [Automatisation QA E2E](</fr/concepts/qa-e2e-automation>), [Canaux de configuration](</fr/gateway/config-channels>)

Telegram - M3 Bêta - 5 domaines

Le canal principal est suffisamment mature pour une utilisation régulière, mais les cas limites à forte variance concernant l’UX et les médias nécessitent des preuves de scénarios récurrentes.

Couverture Expérimental - 0%Qualité Alpha - 68%Complétude Bêta - 78%Complet - 5

Configuration et opérations des canaux 10 fonctionnalités / prises en charge par LTS

Expérimental0%

Alpha66%

Bêta78%

[Telegram](</fr/channels/telegram>), [Configuration des canaux](</fr/gateway/config-channels>), [Canaux](</fr/cli/channels>)

Accès et identité 10 fonctionnalités / prises en charge par LTS

Expérimental0%

Alpha66%

Bêta78%

[Telegram](</fr/channels/telegram>), [Association](</fr/channels/pairing>), [Groupes d’accès](</fr/channels/access-groups>), [Groupes](</fr/channels/groups>), [Multi-agent](</fr/concepts/multi-agent>)

Routage et livraison des conversations 1 fonctionnalité / prise en charge par LTS

Expérimental0%

Alpha66%

Bêta78%

[Telegram](</fr/channels/telegram>), [Groupes](</fr/channels/groups>), [Multi-agent](</fr/concepts/multi-agent>)

Médias et contenu enrichi 1 fonctionnalité / prise en charge par LTS

Expérimental0%

Alpha66%

Bêta78%

[Telegram](</fr/channels/telegram>), [Localisation](</fr/channels/location>)

Contrôles natifs et approbations 9 fonctionnalités / prises en charge par LTS

Expérimental0%

Bêta77%

Bêta79%

[Telegram](</fr/channels/telegram>), [Approbations d’exécution](</fr/tools/exec-approvals>), [Réactions](</fr/tools/reactions>)

Slack - M3 Bêta - 5 domaines

Documentation de canal et surface de routage de premier ordre. Nécessite des fiches d’évaluation de scénarios d’installation et d’administration d’espace de travail.

Couverture expérimentale - 0%Qualité Alpha - 66%Exhaustivité Bêta - 78%Complet - 5

Configuration et opérations des canaux 10 fonctionnalités / pris en charge par LTS

Expérimental0%

Alpha66%

Beta78%

[Slack](</fr/channels/slack>), [Secrets](</fr/gateway/secrets>), [Automatisation QA E2E](</fr/concepts/qa-e2e-automation>), [Dépannage](</fr/channels/troubleshooting>)

Accès et identité 1 fonctionnalité / pris en charge par LTS

Expérimental0%

Alpha66%

Beta78%

[Slack](</fr/channels/slack>), [Appairage](</fr/channels/pairing>)

Routage et livraison des conversations 5 fonctionnalités / pris en charge par LTS

Expérimental0%

Alpha66%

Beta78%

[Slack](</fr/channels/slack>), [Protection contre les boucles de bot](</fr/channels/bot-loop-protection>), [Appairage](</fr/channels/pairing>)

Médias et contenu enrichi 1 fonctionnalité / pris en charge par LTS

Expérimental0%

Alpha66%

Beta78%

[Slack](</fr/channels/slack>), [Automatisation QA E2E](</fr/concepts/qa-e2e-automation>)

Contrôles natifs et approbations 8 fonctionnalités / pris en charge par LTS

Expérimental0%

Alpha66%

Beta78%

[Slack](</fr/channels/slack>), [Commandes slash](</fr/tools/slash-commands>), [Approbations d'exécution](</fr/tools/exec-approvals>)

iMessage et BlueBubbles - M3 Beta - 5 domaines

Les exécutions iMessage prises en charge passent par imsg sur un hôte macOS Messages connecté ; les configurations BlueBubbles héritées nécessitent une migration. Gardez visibles les autorisations macOS, l’enveloppe SSH, l’API SIP/privée et les mises en garde relatives à la migration.

Couverture Expérimental - 0%Qualité Alpha - 66%Exhaustivité Beta - 78%Aucune

Configuration et opérations des canaux 11 capacités

Expérimental0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</fr/announcements/bluebubbles-imessage>), [Imessage depuis Bluebubbles](</fr/channels/imessage-from-bluebubbles>), [Configurer les canaux](</fr/gateway/config-channels>), [Imessage](</fr/channels/imessage>)

Accès et identité 6 capacités

Expérimental0%

Alpha66%

Beta78%

[Imessage](</fr/channels/imessage>), [Imessage depuis Bluebubbles](</fr/channels/imessage-from-bluebubbles>), [Configurer les canaux](</fr/gateway/config-channels>)

Routage et livraison des conversations 4 capacités

Expérimental0%

Alpha66%

Beta78%

[Imessage](</fr/channels/imessage>)

Médias et contenu enrichi 7 capacités

Expérimental0%

Alpha66%

Beta78%

[Imessage](</fr/channels/imessage>), [Imessage depuis Bluebubbles](</fr/channels/imessage-from-bluebubbles>), [Configurer les canaux](</fr/gateway/config-channels>)

Contrôles natifs et approbations 3 capacités

Expérimental0%

Alpha66%

Beta78%

[Imessage](</fr/channels/imessage>)

WhatsApp - M3 Beta - 5 domaines

Le chemin principal est important et documenté ; la volatilité en amont de Baileys/session le maintient en dessous de Stable.

Couverture Expérimental - 0%Qualité Alpha - 66%Complétude Beta - 78%Aucune

Configuration et opérations des canaux 5 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[WhatsApp](</fr/channels/whatsapp>), [Configuration des canaux](</fr/gateway/config-channels>), [WhatsApp](</fr/plugins/reference/whatsapp>), [Automatisation QA E2E](</fr/concepts/qa-e2e-automation>), [Doctor](</fr/gateway/doctor>)

Accès et identité 7 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[WhatsApp](</fr/channels/whatsapp>), [Configuration des canaux](</fr/gateway/config-channels>), [Automatisation QA E2E](</fr/concepts/qa-e2e-automation>), [Appairage](</fr/channels/pairing>)

Routage et livraison des conversations 4 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[WhatsApp](</fr/channels/whatsapp>), [Messages de groupe](</fr/channels/group-messages>)

Médias et contenu enrichi 2 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[WhatsApp](</fr/channels/whatsapp>)

Contrôles natifs et approbations 2 fonctionnalités

Expérimental0%

Alpha66%

Bêta78%

[WhatsApp](</fr/channels/whatsapp>)

Matrice - M2 Alpha - 6 domaines

Pris en charge via le plugin groupé. Nécessite des tableaux de bord de maturité pour le pont, l’authentification et le cycle de vie des salons.

Couverture expérimentale - 0%Qualité Alpha - 60%Complétude Alpha - 67%Aucune

Configuration et opérations des canaux 5 capacités

Expérimental0%

Alpha60%

Alpha67%

[Matrix](</fr/channels/matrix>), [Migration de Matrix](</fr/channels/matrix-migration>)

Accès et identité 7 capacités

Expérimental0%

Alpha60%

Alpha67%

[Matrix](</fr/channels/matrix>), [Groupes](</fr/channels/groups>), [Protection contre les boucles de bots](</fr/channels/bot-loop-protection>)

Routage et livraison des conversations 1 capacité

Expérimental0%

Alpha60%

Alpha67%

[Matrix](</fr/channels/matrix>)

Médias et contenu enrichi 1 capacité

Expérimental0%

Alpha60%

Alpha67%

[Matrix](</fr/channels/matrix>)

Contrôles natifs et approbations 6 capacités

Expérimental0%

Alpha60%

Alpha67%

[Matrix](</fr/channels/matrix>)

Chiffrement et vérification 3 capacités

Expérimental0%

Alpha60%

Alpha67%

[Matrix](</fr/channels/matrix>), [Migration de Matrix](</fr/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 domaines

Canal documenté, mais la configuration entreprise/administrateur augmente le risque de maturité.

Couverture expérimentale - 0%Qualité alpha - 59%Complétude alpha - 66%Aucune

Configuration et opérations des canaux 16 capacités

Expérimental0%

Alpha59%

Alpha66%

[Googlechat](</fr/channels/googlechat>), [Googlechat](</fr/plugins/reference/googlechat>), [Configuration des canaux](</fr/gateway/config-channels>), [Référence de la CLI de l’assistant](</fr/start/wizard-cli-reference>), [Secrets](</fr/gateway/secrets>), [Surface des identifiants Secretref](</fr/reference/secretref-credential-surface>), [Santé](</fr/gateway/health>), [Inventaire des Plugin](</fr/plugins/plugin-inventory>), [Index](</fr/channels>)

Accès et identité 11 capacités

Expérimental0%

Alpha59%

Alpha66%

[Googlechat](</fr/channels/googlechat>), [Appairage](</fr/channels/pairing>), [Groupes d’accès](</fr/channels/access-groups>), [Configuration des canaux](</fr/gateway/config-channels>), [Protection contre les boucles de bot](</fr/channels/bot-loop-protection>), [Routage des canaux](</fr/channels/channel-routing>)

Routage et livraison des conversations 1 capacité

Expérimental0%

Alpha59%

Alpha66%

[Googlechat](</fr/channels/googlechat>), [Protection contre les boucles de bot](</fr/channels/bot-loop-protection>), [Groupes d’accès](</fr/channels/access-groups>), [Routage des canaux](</fr/channels/channel-routing>)

Médias et contenu enrichi 1 capacité

Expérimental0%

Alpha59%

Alpha66%

[Googlechat](</fr/channels/googlechat>), [Message](</fr/cli/message>), [Compréhension des médias](</fr/nodes/media-understanding>), [Surface des identifiants Secretref](</fr/reference/secretref-credential-surface>)

Contrôles et approbations natifs 16 capacités

Expérimental0%

Alpha59%

Alpha66%

[Googlechat](</fr/channels/googlechat>), [Message](</fr/cli/message>), [Compréhension des médias](</fr/nodes/media-understanding>), [Surface des identifiants Secretref](</fr/reference/secretref-credential-surface>), [Réactions](</fr/tools/reactions>), [Commandes slash](</fr/tools/slash-commands>), [Configuration des agents](</fr/gateway/config-agents>), [Refactorisation du cycle de vie des messages](</fr/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 areas

Les flux d’authentification et d’administration d’entreprise nécessitent une preuve de scénario explicite.

Couverture expérimentale - 0%Qualité Alpha - 59%Complétude Alpha - 66%Aucun

Configuration et opérations des canaux 9 capacités

Expérimental0%

Alpha59%

Alpha66%

[Msteams](</fr/channels/msteams>), [Msteams](</fr/plugins/reference/msteams>), [Configuration des canaux](</fr/gateway/config-channels>), [Santé](</fr/gateway/health>)

Accès et identité 9 capacités

Expérimental0%

Alpha59%

Alpha66%

[Msteams](</fr/channels/msteams>), [Appairage](</fr/channels/pairing>), [Groupes d’accès](</fr/channels/access-groups>)

Routage et livraison des conversations 5 capacités

Expérimental0%

Alpha59%

Alpha66%

[Msteams](</fr/channels/msteams>), [Groupes](</fr/channels/groups>), [Routage des canaux](</fr/channels/channel-routing>)

Médias et contenu enrichi 5 capacités

Expérimental0%

Alpha59%

Alpha66%

[Msteams](</fr/channels/msteams>)

Contrôles natifs et approbations 5 capacités

Expérimental0%

Alpha59%

Alpha66%

[Msteams](</fr/channels/msteams>), [Approbations Exec avancées](</fr/tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 domaines

La documentation du canal pris en charge existe ; il faut des preuves plus solides d’installation et de reconnexion.

Couverture Expérimental - 0%Qualité Alpha - 59%Exhaustivité Alpha - 66%Aucun

Configuration et opérations des canaux 7 capacités

Expérimental0%

Alpha59%

Alpha66%

[Signal](</fr/channels/signal>), [Signal](</fr/plugins/reference/signal>)

Accès et identité 6 capacités

Expérimental0%

Alpha59%

Alpha66%

[Signal](</fr/channels/signal>)

Routage et livraison des conversations 1 capacité

Expérimental0%

Alpha59%

Alpha66%

[Signal](</fr/channels/signal>)

Médias et contenu enrichi 7 capacités

Expérimental0%

Alpha59%

Alpha66%

[Signal](</fr/channels/signal>)

Contrôles natifs et approbations 3 capacités

Expérimental0%

Alpha59%

Alpha66%

[Signal](</fr/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canaux régionaux - M2 Alpha - 4 domaines

Couverture régionale importante, mais le niveau de prise en charge publique doit être calibré selon le type de compte, l’approbation en amont et les preuves des mainteneurs.

Couverture expérimentale - 0%Qualité Alpha - 55%Exhaustivité Alpha - 58%Aucun

Configuration et opérations des canaux 6 capacités

Expérimental0%

Alpha61%

Alpha68%

[Index](</fr/channels>), [Appairage](</fr/channels/pairing>), [Feishu](</fr/plugins/reference/feishu>), [Internes de l’architecture](</fr/plugins/architecture-internals>)

Accès et identité 1 capacité

Expérimental0%

Alpha53%

Alpha54%

Aucune documentation liée

Routage et livraison des conversations 1 capacité

Expérimental0%

Alpha53%

Alpha54%

Aucune documentation liée

Médias et contenu enrichi 1 capacité

Expérimental0%

Alpha53%

Alpha54%

Aucune documentation liée

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 domaines

Les surfaces prises en charge existent, mais la maturité varie probablement selon la couverture amont et celle des mainteneurs. À évaluer individuellement plus tard.

Couverture Expérimental - 0%Qualité Alpha - 53%Complétude Alpha - 54%Aucun

Configuration et opérations des canaux 1 capacité

Expérimental0%

Alpha53%

Alpha54%

Aucune documentation liée

Accès et identité 1 capacité

Expérimental0%

Alpha53%

Alpha54%

Aucune documentation liée

Routage et livraison des conversations 1 capacité

Expérimental0%

Alpha53%

Alpha54%

Aucune documentation liée

Médias et contenu riche 1 capacité

Expérimental0%

Alpha53%

Alpha54%

Aucune documentation liée

Canal d’appel vocal - M1 Expérimental - 5 domaines

Chemin optionnel/Plugin avec un comportement complexe en temps réel. Nécessite une fiche d’évaluation de scénario avant la bêta publique.

Couverture Expérimental - 0%Qualité Expérimental - 41%Complétude Expérimental - 44%Aucun

Configuration et opérations des canaux 2 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Appel vocal](</fr/cli/voicecall>), [Appel vocal](</fr/plugins/voice-call>), [Protocole](</fr/gateway/protocol>)

Accès et identité 1 capacité

Expérimental0%

Expérimental41%

Expérimental44%

[Appel vocal](</fr/plugins/voice-call>), [Appel vocal](</fr/cli/voicecall>)

Routage et livraison des conversations 1 capacité

Expérimental0%

Expérimental41%

Expérimental44%

[Appel vocal](</fr/plugins/voice-call>)

Médias et contenu enrichi 2 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Appel vocal](</fr/plugins/voice-call>), [Inventaire des Plugins](</fr/plugins/plugin-inventory>)

Voix et appels en temps réel 2 capacités

Expérimental0%

Expérimental41%

Expérimental44%

[Appel vocal](</fr/plugins/voice-call>)

### Fournisseur et outil

Automatisation du navigateur, exec et outils de sandbox - M3 bêta - 3 domaines

Les outils principaux sont documentés, mais la sécurité de l’hôte et l’expérience utilisateur des autorisations doivent rester sous examen actif dans la scorecard.

Couverture Expérimental - 21%Qualité Bêta - 75%Exhaustivité Bêta - 79%Partiel - 2

Automatisation du navigateur 8 capacités

Expérimental13%

Bêta79%

Bêta79%

[Contrôle du navigateur](</fr/tools/browser-control>), [Tests](</fr/help/testing>), [Navigateur](</fr/tools/browser>), [Index](</fr/gateway/security>), [Contrôles d’audit](</fr/gateway/security/audit-checks>)

Invocation et exécution d’outils 6 capacités / pris en charge par LTS

Alpha50%

Bêta79%

Bêta79%

[Exec](</fr/tools/exec>), [Processus en arrière-plan](</fr/gateway/background-process>), [API HTTP d’invocation des outils](</fr/gateway/tools-invoke-http-api>), [Périmètres opérateur](</fr/gateway/operator-scopes>), [Protocole](</fr/gateway/protocol>), [Approbations Exec](</fr/tools/exec-approvals>), [Approbations Exec avancées](</fr/tools/exec-approvals-advanced>), [Élévation](</fr/tools/elevated>)

Bac à sable et politique des outils 6 capacités / pris en charge par LTS

Expérimental0%

Alpha68%

Bêta79%

[Mise en bac à sable](</fr/gateway/sandboxing>), [Bac à sable vs politique des outils vs élévation](</fr/gateway/sandbox-vs-tool-policy-vs-elevated>), [Outils de bac à sable multi-agent](</fr/tools/multi-agent-sandbox-tools>), [Référence du harness Codex](</fr/plugins/codex-harness-reference>), [Configuration des outils](</fr/gateway/config-tools>)

OpenAI and Codex provider path - M3 Beta - 5 areas

Documentation approfondie, parcours OAuth/abonnement, voix en temps réel, image et comportement de compatibilité. Les changements fréquents côté fournisseur empêchent le passage en stable sans preuve par scorecard de version.

Couverture expérimentale - 26%Qualité bêta - 74%Exhaustivité bêta - 79%Partiel - 3

Modèle et authentification 6 capacités / pris en charge par LTS

Expérimental44%

Beta79%

Beta79%

[Openai](</fr/providers/openai>), [Harnais Codex](</fr/plugins/codex-harness>), [Modèles](</fr/concepts/models>), [Oauth](</fr/concepts/oauth>), [Référence du harnais Codex](</fr/plugins/codex-harness-reference>), [Surveillance de l’authentification](</fr/gateway/authentication>)

Réponses et compatibilité des outils 4 capacités / pris en charge par LTS

Expérimental40%

Beta79%

Beta79%

[Openai](</fr/providers/openai>), [API HTTP Openresponses](</fr/gateway/openresponses-http-api>), [API HTTP Openai](</fr/gateway/openai-http-api>), [Plugins natifs Codex](</fr/plugins/codex-native-plugins>)

Harnais Codex natif 2 capacités / pris en charge par LTS

Expérimental44%

Beta79%

Beta79%

[Harnais Codex](</fr/plugins/codex-harness>), [Environnement d’exécution du harnais Codex](</fr/plugins/codex-harness-runtime>), [Référence du harnais Codex](</fr/plugins/codex-harness-reference>), [Plugins natifs Codex](</fr/plugins/codex-native-plugins>)

Image et entrée multimodale 2 capacités

Expérimental0%

Alpha67%

Beta79%

[Openai](</fr/providers/openai>), [Génération d’images](</fr/tools/image-generation>), [Images](</fr/nodes/images>)

Voix et audio en temps réel 2 capacités

Expérimental0%

Alpha67%

Beta79%

[Openai](</fr/providers/openai>), [Discord](</fr/channels/discord>), [Appel vocal](</fr/plugins/voice-call>)

Outils de recherche Web - M3 Beta - 4 domaines

Plusieurs fournisseurs et documentations existent. Nécessite une preuve de quota, d’erreur et de SSRF par famille de fournisseurs.

Couverture Expérimental - 9%Qualité Beta - 74%Exhaustivité Beta - 79%Aucun

Fournisseurs de recherche 19 capacités

Expérimental11%

Bêta79%

Bêta79%

[Web](</fr/tools/web>), [Brave Search](</fr/tools/brave-search>), [Tavily](</fr/tools/tavily>), [Exa Search](</fr/tools/exa-search>), [Firecrawl](</fr/tools/firecrawl>), [Recherche Perplexity](</fr/tools/perplexity-search>), [Recherche Duckduckgo](</fr/tools/duckduckgo-search>), [Recherche Searxng](</fr/tools/searxng-search>), [Recherche Gemini](</fr/tools/gemini-search>), [Recherche Grok](</fr/tools/grok-search>), [Recherche Kimi](</fr/tools/kimi-search>), [Recherche Minimax](</fr/tools/minimax-search>), [Recherche Ollama](</fr/tools/ollama-search>), [Sous-chemins SDK](</fr/plugins/sdk-subpaths>), [Vue d’ensemble du SDK](</fr/plugins/sdk-overview>), [Manifeste](</fr/plugins/manifest>)

Configuration et diagnostics 9 capacités

Expérimental0%

Alpha68%

Bêta79%

[Web](</fr/tools/web>), [Récupération Web](</fr/tools/web-fetch>), [FAQ](</fr/help/faq>), [Coûts d’utilisation de l’API](</fr/reference/api-usage-costs>), [Brave Search](</fr/tools/brave-search>), [Recherche Perplexity](</fr/tools/perplexity-search>), [Tavily](</fr/tools/tavily>), [Firecrawl](</fr/tools/firecrawl>)

Sécurité réseau 4 capacités

Expérimental0%

Alpha68%

Bêta79%

[Web](</fr/tools/web>), [Récupération Web](</fr/tools/web-fetch>), [Firecrawl](</fr/tools/firecrawl>), [Recherche Searxng](</fr/tools/searxng-search>)

Disponibilité et récupération des outils 11 capacités

Expérimental25%

Bêta79%

Bêta79%

[Outils de configuration](</fr/gateway/config-tools>), [Récupération Web](</fr/tools/web-fetch>), [Web](</fr/tools/web>), [FAQ](</fr/help/faq>)

Chemin du fournisseur Anthropic - M3 Bêta - 5 domaines

Fournisseur de modèles de premier plan. Nécessite une preuve récurrente des scénarios d’authentification, de catalogue et d’appel d’outil.

Couverture expérimentale - 0%Qualité Bêta - 71%Complétude Bêta - 78%Aucune

Authentification et récupération des fournisseurs 9 capacités

Expérimental0%

Alpha66%

Beta78%

[Anthropic](</fr/providers/anthropic>), [Doctor](</fr/gateway/doctor>), [Exemples de configuration](</fr/gateway/configuration-examples>), [Dépannage](</fr/gateway/troubleshooting>), [Mise en cache des prompts](</fr/reference/prompt-caching>)

Sélection du modèle et du runtime 10 capacités

Expérimental0%

Beta78%

Beta79%

[Anthropic](</fr/providers/anthropic>), [Agents de configuration](</fr/gateway/config-agents>), [Modèles](</fr/concepts/models>), [Backends CLI](</fr/gateway/cli-backends>)

Transport des requêtes et sémantique des tours 10 capacités

Expérimental0%

Beta77%

Beta79%

[Anthropic](</fr/providers/anthropic>), [Mise en cache des prompts](</fr/reference/prompt-caching>), [Dépannage](</fr/gateway/troubleshooting>), [Backends CLI](</fr/gateway/cli-backends>), [Fournisseurs de modèles](</fr/concepts/model-providers>)

Cache de prompts et contexte 5 capacités

Expérimental0%

Alpha66%

Beta78%

[Anthropic](</fr/providers/anthropic>), [Mise en cache des prompts](</fr/reference/prompt-caching>), [Dépannage](</fr/gateway/troubleshooting>), [Heartbeat](</fr/gateway/heartbeat>)

Entrées multimédias 4 capacités

Expérimental0%

Alpha66%

Beta78%

[Anthropic](</fr/providers/anthropic>), [Agents de configuration](</fr/gateway/config-agents>)

Chemin du fournisseur Google - M3 Beta - 5 domaines

Fournisseur de premier ordre avec des surfaces de modèle et temps réel. Nécessite une évaluation Live/Talk distincte.

Couverture Expérimental - 0%Qualité Alpha - 66%Complétude Beta - 78%Aucun

Configuration du fournisseur et identifiants 10 capacités

Expérimental0%

Alpha66%

Bêta78%

[Google](</fr/providers/google>), [Fournisseurs de modèles](</fr/concepts/model-providers>)

Routage des modèles et endpoints 10 capacités

Expérimental0%

Alpha66%

Bêta78%

[Google](</fr/providers/google>), [Fournisseurs de modèles](</fr/concepts/model-providers>), [Google](</fr/plugins/reference/google>), [Recherche Gemini](</fr/tools/gemini-search>)

Runtime Gemini direct 9 capacités

Expérimental0%

Alpha66%

Bêta78%

[Google](</fr/providers/google>), [Fournisseurs de modèles](</fr/concepts/model-providers>), [FAQ sur les modèles](</fr/help/faq-models>), [Tests en direct](</fr/help/testing-live>)

Médias, recherche et temps réel 10 capacités

Expérimental0%

Alpha66%

Bêta78%

[Google](</fr/plugins/reference/google>), [Google](</fr/providers/google>)

Mise en cache des prompts 5 capacités

Expérimental0%

Alpha66%

Bêta78%

[Mise en cache des prompts](</fr/reference/prompt-caching>), [Google](</fr/providers/google>), [Fournisseurs de modèles](</fr/concepts/model-providers>), [Utilisation des tokens](</fr/reference/token-use>)

Chemin du fournisseur OpenRouter - M3 Bêta - 4 domaines

Le chemin fournisseur unifié est documenté et utile, mais le comportement propre à chaque modèle varie.

Couverture expérimentale - 0%Qualité Alpha - 66%Complétude Bêta - 78%Aucun

Configuration et authentification des fournisseurs 14 capacités

Expérimental0%

Alpha66%

Bêta78%

[Openrouter](</fr/providers/openrouter>), [Fournisseurs de modèles](</fr/concepts/model-providers>), [Configurer](</fr/cli/configure>), [Authentification](</fr/gateway/authentication>), [Environnement](</fr/help/environment>), [Modèles](</fr/cli/models>), [Modèles](</fr/concepts/models>)

Environnement d’exécution de chat et normalisation 15 capacités

Expérimental0%

Alpha66%

Bêta78%

[Openrouter](</fr/providers/openrouter>), [Fournisseurs de modèles](</fr/concepts/model-providers>), [Mise en cache des prompts](</fr/reference/prompt-caching>)

Récupération et diagnostics des fournisseurs 5 capacités

Expérimental0%

Alpha66%

Bêta78%

[Basculement de modèle](</fr/concepts/model-failover>), [Openrouter](</fr/providers/openrouter>), [Modèles](</fr/cli/models>)

Génération de médias et parole 7 capacités

Expérimental0%

Alpha66%

Bêta78%

[Openrouter](</fr/providers/openrouter>), [Génération d’images](</fr/tools/image-generation>), [Génération de musique](</fr/tools/music-generation>), [Vue d’ensemble des médias](</fr/tools/media-overview>), [Génération de vidéos](</fr/tools/video-generation>), [Synthèse vocale](</fr/tools/tts>)

Outils de génération d’images, de vidéos et de musique - M2 Alpha - 5 domaines

La capacité existe chez plusieurs fournisseurs, mais la qualité, la latence et la compatibilité des paramètres varient trop pour une bêta sans preuve par fournisseur.

Couverture expérimentale - 0%Qualité Alpha - 61%Complétude Alpha - 68%Aucun

Routage et découverte des médias 4 capacités

Expérimental0%

Alpha61%

Alpha68%

[Agents de configuration](</fr/gateway/config-agents>), [Génération d’images](</fr/tools/image-generation>), [Génération de vidéos](</fr/tools/video-generation>), [Génération de musique](</fr/tools/music-generation>)

Cycle de vie et livraison des tâches 12 capacités

Expérimental0%

Alpha61%

Alpha68%

[Vue d’ensemble des médias](</fr/tools/media-overview>), [Génération d’images](</fr/tools/image-generation>), [Génération de vidéos](</fr/tools/video-generation>), [Génération de musique](</fr/tools/music-generation>)

Génération d’images 9 capacités

Expérimental0%

Alpha61%

Alpha68%

[Génération d’images](</fr/tools/image-generation>), [Infer](</fr/cli/infer>), [Vue d’ensemble des médias](</fr/tools/media-overview>)

Génération de vidéos 11 capacités

Expérimental0%

Alpha61%

Alpha68%

[Génération de vidéos](</fr/tools/video-generation>), [Runway](</fr/providers/runway>), [Pixverse](</fr/providers/pixverse>), [Fal](</fr/providers/fal>), [Openrouter](</fr/providers/openrouter>)

Génération de musique 6 capacités

Expérimental0%

Alpha61%

Alpha68%

[Génération de musique](</fr/tools/music-generation>)

Fournisseurs de modèles locaux : Ollama, vLLM, SGLang, LM Studio - M2 Alpha - 5 domaines

Utile et documenté, mais la variabilité des environnements est élevée.

Couverture expérimentale - 0%Qualité Alpha - 61%Complétude Alpha - 68%Aucun

Configuration, cycle de vie et diagnostics des fournisseurs 12 capacités

Expérimental0%

Alpha61%

Alpha68%

[Modèles locaux](</fr/gateway/local-models>), [Lmstudio](</fr/providers/lmstudio>), [Ollama](</fr/providers/ollama>), [Vllm](</fr/providers/vllm>), [Services de modèles locaux](</fr/gateway/local-model-services>), [Agents de configuration](</fr/gateway/config-agents>), [Dépannage](</fr/gateway/troubleshooting>), [Doctor](</fr/gateway/doctor>)

Plugins de fournisseurs natifs 10 capacités

Expérimental0%

Alpha61%

Alpha68%

[Ollama](</fr/providers/ollama>), [Lmstudio](</fr/providers/lmstudio>)

Compatibilité du runtime compatible avec OpenAI 8 capacités

Expérimental0%

Alpha61%

Alpha68%

[Vllm](</fr/providers/vllm>), [Sglang](</fr/providers/sglang>), [Modèles locaux](</fr/gateway/local-models>), [Lmstudio](</fr/providers/lmstudio>)

Mémoire locale et embeddings 5 capacités

Expérimental0%

Alpha61%

Alpha68%

[Mémoire](</fr/concepts/memory>), [Doctor](</fr/gateway/doctor>)

Sécurité réseau et contrôles des prompts 2 capacités

Expérimental0%

Alpha61%

Alpha68%

[Index](</fr/gateway/security>), [Outils de configuration](</fr/gateway/config-tools>), [Modèles locaux](</fr/gateway/local-models>)

Fournisseurs hébergés de longue traîne - M2 Alpha - 3 zones

De nombreuses pages de documentation/référence existent ; le score doit être généré à partir des métadonnées des fournisseurs et de la couverture des tests smoke en direct.

Couverture Expérimental - 0%Qualité Alpha - 61%Complétude Alpha - 68%Aucun

Fournisseurs de LLM hébergés 12 capacités

Expérimental0%

Alpha61%

Alpha68%

[Index](</fr/providers>), [Fournisseurs de modèles](</fr/concepts/model-providers>), [Tests en direct](</fr/help/testing-live>), [Intégration](</fr/cli/onboard>)

Fournisseurs de médias hébergés 8 capacités

Expérimental0%

Alpha61%

Alpha68%

[Manifeste](</fr/plugins/manifest>), [Tests en direct](</fr/help/testing-live>), [Index](</fr/providers>)

Opérations des fournisseurs 12 capacités

Expérimental0%

Alpha61%

Alpha68%

[Index](</fr/providers>), [Fournisseurs de modèles](</fr/concepts/model-providers>), [Manifeste](</fr/plugins/manifest>), [Tests en direct](</fr/help/testing-live>), [Modèles](</fr/cli/models>)

Was this useful?YesNo

Open issue