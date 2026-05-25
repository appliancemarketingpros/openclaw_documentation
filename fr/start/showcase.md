---
title: vitrine
source_url: https://docs.openclaw.ai/fr/start/showcase
scraped_at: 2026-05-25
---

Les projets OpenClaw ne sont pas des démos gadgets. Des personnes livrent des boucles de revue de PR, des apps mobiles, de l’automatisation domestique, des systèmes vocaux, des devtools et des flux riches en mémoire depuis les canaux qu’elles utilisent déjà — des builds natifs au chat sur Telegram, WhatsApp, Discord et terminaux ; de la vraie automatisation pour la réservation, les achats et le support sans attendre une API ; et des intégrations avec le monde physique via imprimantes, aspirateurs, caméras et systèmes domestiques.

## Vidéos

Commencez ici si vous voulez le chemin le plus court entre « qu’est-ce que c’est ? » et « ok, j’ai compris ».

[**Guide complet de configuration** VelvetShark, 28 minutes. Installer, intégrer, et arriver à un premier assistant fonctionnel de bout en bout. ](<https://www.youtube.com/watch?v=SaWSPZoPX34>) [**Montage vitrine de la communauté** Un passage plus rapide à travers de vrais projets, surfaces et flux de travail construits autour d’OpenClaw. ](<https://www.youtube.com/watch?v=mMSKQvlmFuQ>) [**Projets en conditions réelles** Exemples de la communauté, des boucles de codage natives au chat jusqu’au matériel et à l’automatisation personnelle. ](<https://www.youtube.com/watch?v=5kkIJNUGFho>)

## Nouveautés depuis Discord

Projets remarquables récents dans le codage, les devtools, le mobile et la création de produits natifs au chat.

[**Revue de PR vers retour Telegram** **@bangnokia** • `review` `github` `telegram` OpenCode termine la modification, ouvre une PR, OpenClaw examine le diff et répond dans Telegram avec des suggestions plus un verdict clair de fusion. ![Retour de revue de PR OpenClaw livré dans Telegram](/assets/showcase/pr-review-telegram.jpg) ](<https://x.com/i/status/2010878524543131691>) [**Skill cave à vin en quelques minutes** **@prades_maxime** • `skills` `local` `csv` A demandé à « Robby » (@openclaw) un skill local de cave à vin. Il demande un export CSV d’exemple et un chemin de stockage, puis construit et teste le skill (962 bouteilles dans l’exemple). ![OpenClaw construisant un skill local de cave à vin à partir d’un CSV](/assets/showcase/wine-cellar-skill.jpg) ](<https://x.com/i/status/2010916352454791216>) [**Pilote automatique Tesco Shop** **@marchattonhere** • `automation` `browser` `shopping` Plan de repas hebdomadaire, achats habituels, réservation d’un créneau de livraison, confirmation de commande. Pas d’API, juste du contrôle navigateur. ![Automatisation Tesco shop via chat](/assets/showcase/tesco-shop.jpg) ](<https://x.com/i/status/2009724862470689131>) [**SNAG capture d’écran vers Markdown** **@am-will** • `devtools` `screenshots` `markdown` Définissez un raccourci sur une région d’écran, utilisez Gemini vision, obtenez instantanément du Markdown dans votre presse-papiers. ![Outil SNAG capture d’écran vers markdown](/assets/showcase/snag.png) ](<https://github.com/am-will/snag>) [**Agents UI** **@kitze** • `ui` `skills` `sync` App de bureau pour gérer skills et commandes sur Agents, Claude, Codex et OpenClaw. ![App Agents UI](/assets/showcase/agents-ui.jpg) ](<https://releaseflow.net/kitze/agents-ui>) [**Notes vocales Telegram (papla.media)** **Communauté** • `voice` `tts` `telegram` Enveloppe le TTS papla.media et envoie les résultats comme notes vocales Telegram (sans lecture automatique agaçante). ![Sortie de note vocale Telegram depuis le TTS](/assets/showcase/papla-tts.jpg) ](<https://papla.media/docs>) [**CodexMonitor** **@odrobnik** • `devtools` `codex` `brew` Helper installé via Homebrew pour lister, inspecter et surveiller les sessions locales OpenAI Codex (CLI + VS Code). ![CodexMonitor sur ClawHub](/assets/showcase/codexmonitor.png) ](<https://clawhub.ai/odrobnik/codexmonitor>) [**Contrôle d’imprimante 3D Bambu** **@tobiasbischoff** • `hardware` `3d-printing` `skill` Contrôlez et dépannez les imprimantes BambuLab : état, travaux, caméra, AMS, calibration, etc. ![Skill Bambu CLI sur ClawHub](/assets/showcase/bambu-cli.png) ](<https://clawhub.ai/tobiasbischoff/bambu-cli>) [**Transports de Vienne (Wiener Linien)** **@hjanuschka** • `travel` `transport` `skill` Départs en temps réel, perturbations, état des ascenseurs et itinéraires pour les transports publics de Vienne. ![Skill Wiener Linien sur ClawHub](/assets/showcase/wienerlinien.png) ](<https://clawhub.ai/hjanuschka/wienerlinien>) **Repas scolaires ParentPay** **@George5562** • `automation` `browser` `parenting` Réservation automatisée des repas scolaires au Royaume-Uni via ParentPay. Utilise les coordonnées de la souris pour cliquer de manière fiable sur les cellules du tableau. [**Téléversement R2 (Send Me My Files)** **@julianengel** • `files` `r2` `presigned-urls` Téléverse vers Cloudflare R2/S3 et génère des liens de téléchargement presignés sécurisés. Utile pour les instances OpenClaw distantes. ](<https://clawhub.ai/skills/r2-upload>) **App iOS via Telegram** **@coard** • `ios` `xcode` `testflight` A construit une app iOS complète avec cartes et enregistrement vocal, déployée sur TestFlight entièrement via le chat Telegram. ![App iOS sur TestFlight](/assets/showcase/ios-testflight.jpg) **Assistant santé Oura Ring** **@AS** • `health` `oura` `calendar` Assistant santé IA personnel intégrant les données Oura ring avec le calendrier, les rendez-vous et le planning de salle de sport. ![Assistant santé Oura ring](/assets/showcase/oura-health.png) [**Kev's Dream Team (14+ agents)** **@adam91holt** • `multi-agent` `orchestration` Plus de 14 agents sous une même gateway avec un orchestrateur Opus 4.5 déléguant à des workers Codex. Voir le [texte technique](<https://github.com/adam91holt/orchestrated-ai-articles>) et [Clawdspace](<https://github.com/adam91holt/clawdspace>) pour le sandboxing d’agent. ](<https://github.com/adam91holt/orchestrated-ai-articles>) [**CLI Linear** **@NessZerra** • `devtools` `linear` `cli` CLI pour Linear qui s’intègre aux flux de travail agentiques (Claude Code, OpenClaw). Gérez les tickets, projets et flux de travail depuis le terminal. ](<https://github.com/Finesssee/linear-cli>) [**CLI Beeper** **@jules** • `messaging` `beeper` `cli` Lire, envoyer et archiver des messages via Beeper Desktop. Utilise l’API MCP locale de Beeper pour que les agents puissent gérer toutes vos discussions (iMessage, WhatsApp, etc.) au même endroit. ](<https://github.com/blqke/beepcli>)

## Automatisation et flux de travail

Planification, contrôle du navigateur, boucles de support et le côté « fais simplement la tâche à ma place » du produit.

[**Contrôle de purificateur d’air Winix** **@antonplex** • `automation` `hardware` `air-quality` Claude Code a découvert et confirmé les contrôles du purificateur, puis OpenClaw prend le relais pour gérer la qualité de l’air de la pièce. ![Contrôle du purificateur d’air Winix via OpenClaw](/assets/showcase/winix-air-purifier.jpg) ](<https://x.com/antonplex/status/2010518442471006253>) [**Jolies photos du ciel par caméra** **@signalgaining** • `automation` `camera` `skill` Déclenché par une caméra de toit : demandez à OpenClaw de prendre une photo du ciel chaque fois qu’il est beau. Il a conçu un skill et pris la photo. ![Capture du ciel par caméra de toit réalisée par OpenClaw](/assets/showcase/roof-camera-sky.jpg) ](<https://x.com/signalgaining/status/2010523120604746151>) [**Scène de briefing visuel du matin** **@buddyhadry** • `automation` `briefing` `telegram` Un prompt planifié génère chaque matin une image de scène (météo, tâches, date, publication favorite ou citation) via une persona OpenClaw. ](<https://x.com/buddyhadry/status/2010005331925954739>) [**Réservation de terrain de padel** **@joshp123** • `automation` `booking` `cli` Vérificateur de disponibilité Playtomic plus CLI de réservation. Ne manquez plus jamais un terrain libre. ![capture d’écran padel-cli](/assets/showcase/padel-screenshot.jpg) ](<https://github.com/joshp123/padel-cli>) **Collecte comptable** **Communauté** • `automation` `email` `pdf` Collecte les PDF depuis les emails, prépare les documents pour un conseiller fiscal. Comptabilité mensuelle en pilote automatique. [**Mode dev canapé** **@davekiss** • `telegram` `migration` `astro` A reconstruit tout un site personnel via Telegram en regardant Netflix — Notion vers Astro, 18 articles migrés, DNS vers Cloudflare. N’a jamais ouvert d’ordinateur portable. ](<https://davekiss.com>) **Agent de recherche d’emploi** **@attol8** • `automation` `api` `skill` Recherche des offres d’emploi, les compare aux mots-clés du CV et renvoie des opportunités pertinentes avec liens. Construit en 30 minutes avec l’API JSearch. [**Constructeur de skill Jira** **@jdrhyne** • `jira` `skill` `devtools` OpenClaw s’est connecté à Jira, puis a généré un nouveau skill à la volée (avant qu’il n’existe sur ClawHub). ](<https://x.com/jdrhyne/status/2008336434827002232>) [**Skill Todoist via Telegram** **@iamsubhrajyoti** • `todoist` `skill` `telegram` A automatisé des tâches Todoist et a fait générer le skill directement par OpenClaw dans le chat Telegram. ](<https://x.com/iamsubhrajyoti/status/2009949389884920153>) **Analyse TradingView** **@bheem1798** • `finance` `browser` `automation` Se connecte à TradingView via automatisation de navigateur, capture des graphiques et effectue une analyse technique à la demande. Pas d’API nécessaire — juste du contrôle navigateur. **Auto-support Slack** **@henrymascot** • `slack` `automation` `support` Surveille un canal Slack d’entreprise, répond utilement et transfère les notifications vers Telegram. A corrigé de manière autonome un bug de production dans une app déployée sans qu’on le lui demande.

## Connaissance et mémoire

Systèmes qui indexent, recherchent, mémorisent et raisonnent sur les connaissances personnelles ou d’équipe.

[**xuezh apprentissage du chinois** **@joshp123** • `learning` `voice` `skill` Moteur d’apprentissage du chinois avec retour sur la prononciation et flux d’étude via OpenClaw. ![retour sur la prononciation xuezh](/assets/showcase/xuezh-pronunciation.jpeg) ](<https://github.com/joshp123/xuezh>) **Coffre mémoire WhatsApp** **Communauté** • `memory` `transcription` `indexing` Ingère des exports WhatsApp complets, transcrit plus de 1 000 notes vocales, recoupe avec les journaux git, produit des rapports Markdown liés. [**Recherche sémantique Karakeep** **@jamesbrooksco** • `search` `vector` `bookmarks` Ajoute la recherche vectorielle aux signets Karakeep à l’aide de Qdrant plus des embeddings OpenAI ou Ollama. ](<https://github.com/jamesbrooksco/karakeep-semantic-search>) **Mémoire Inside-Out-2** **Communauté** • `memory` `beliefs` `self-model` Gestionnaire de mémoire séparé qui transforme les fichiers de session en souvenirs, puis en croyances, puis en un modèle de soi évolutif.

## Voix et téléphone

Points d’entrée centrés sur la parole, ponts téléphoniques et flux riches en transcription.

[**Pont téléphonique Clawdia** **@alejandroOPI** • `voice` `vapi` `bridge` Pont HTTP de l’assistant vocal Vapi vers OpenClaw. Appels téléphoniques quasi temps réel avec votre agent. ](<https://github.com/alejandroOPI/clawdia-bridge>) [**Transcription OpenRouter** **@obviyus** • `transcription` `multilingual` `skill` Transcription audio multilingue via OpenRouter (Gemini, etc.). Disponible sur ClawHub. ](<https://clawhub.ai/obviyus/openrouter-transcribe>)

## Infrastructure et déploiement

Packaging, déploiement et intégrations qui rendent OpenClaw plus facile à exécuter et à étendre.

[**Add-on Home Assistant** **@ngutman** • `homeassistant` `docker` `raspberry-pi` Gateway OpenClaw exécutée sur Home Assistant OS avec prise en charge du tunnel SSH et état persistant. ](<https://github.com/ngutman/openclaw-ha-addon>) [**Skill Home Assistant** **ClawHub** • `homeassistant` `skill` `automation` Contrôler et automatiser les appareils Home Assistant en langage naturel. ](<https://clawhub.ai/skills/homeassistant>) [**Packaging Nix** **@openclaw** • `nix` `packaging` `deployment` Configuration OpenClaw nixifiée avec tout inclus pour des déploiements reproductibles. ](<https://github.com/openclaw/nix-openclaw>) [**Calendrier CalDAV** **ClawHub** • `calendar` `caldav` `skill` Skill calendrier utilisant khal et vdirsyncer. Intégration de calendrier auto-hébergé. ](<https://clawhub.ai/skills/caldav-calendar>)

## Maison et matériel

Le côté monde physique d’OpenClaw : maisons, capteurs, caméras, aspirateurs et autres appareils.

[**Automatisation GoHome** **@joshp123** • `home` `nix` `grafana` Automatisation domestique native Nix avec OpenClaw comme interface, plus des tableaux de bord Grafana. ![Tableau de bord GoHome Grafana](/assets/showcase/gohome-grafana.png) ](<https://github.com/joshp123/gohome>) [**Aspirateur Roborock** **@joshp123** • `vacuum` `iot` `plugin` Contrôlez votre aspirateur robot Roborock par conversation naturelle. ![État Roborock](/assets/showcase/roborock-screenshot.jpg) ](<https://github.com/joshp123/gohome/tree/main/plugins/roborock>)

## Projets communautaires

Des choses qui ont grandi au-delà d’un seul flux de travail pour devenir des produits ou écosystèmes plus larges.

[**Marketplace StarSwap** **Communauté** • `marketplace` `astronomy` `webapp` Marketplace complète de matériel d’astronomie. Construite avec et autour de l’écosystème OpenClaw. ](<https://star-swap.com/>)

## Soumettre votre projet

* ### Partagez-le

Publiez dans [#self-promotion sur Discord](<https://discord.gg/clawd>) ou [tweet @openclaw](<https://x.com/openclaw>).

* ### Inclure les détails

Dites-nous ce qu’il fait, ajoutez un lien vers le dépôt ou la démo, et partagez une capture d’écran si vous en avez une.

* ### Être mis en avant

Nous ajouterons les projets remarquables à cette page.

## Liens associés

  * [Premiers pas](</fr/start/getting-started>)
  * [OpenClaw](</fr/start/openclaw>)


Was this useful?YesNo