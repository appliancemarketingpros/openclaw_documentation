---
title: Serveur Linux
source_url: https://docs.openclaw.ai/fr/vps
scraped_at: 2026-05-25
---

Exécutez le Gateway OpenClaw sur n'importe quel serveur Linux ou VPS cloud. Cette page vous aide à choisir un fournisseur, explique le fonctionnement des déploiements cloud et couvre l’optimisation Linux générique applicable partout.

## Choisir un fournisseur

[**Railway** [**Northflank** [**DigitalOcean** [**Oracle Cloud** [**Fly.io** [**Hetzner** [**Hostinger** [**GCP** [**Azure** [**exe.dev** [**Raspberry Pi** **AWS (EC2 / Lightsail / offre gratuite)** fonctionne également très bien. Un tutoriel vidéo de la communauté est disponible sur [x.com/techfrenAJ/status/2014934471095812547](<https://x.com/techfrenAJ/status/2014934471095812547>) (ressource communautaire -- peut devenir indisponible). Fonctionnement des configurations cloud

  * Le **Gateway s’exécute sur le VPS** et possède l’état + l’espace de travail.
  * Vous vous connectez depuis votre ordinateur portable ou votre téléphone via l’**interface utilisateur de contrôle** ou **Tailscale/SSH**.
  * Traitez le VPS comme la source de vérité et **sauvegardez** régulièrement l’état + l’espace de travail.
  * Valeur par défaut sécurisée : gardez le Gateway sur l’interface de bouclage et accédez-y via un tunnel SSH ou Tailscale Serve. Si vous l’associez à `lan` ou `tailnet`, exigez `gateway.auth.token` ou `gateway.auth.password`.

Pages connexes : [accès distant au Gateway](</fr/gateway/remote>), [hub des plateformes](</fr/platforms>). Sécuriser d’abord l’accès administrateur Avant d’installer OpenClaw sur un VPS public, décidez comment vous voulez administrer la machine elle-même.

  * Si vous voulez un accès administrateur limité au tailnet, installez d’abord Tailscale, joignez le VPS à votre tailnet, vérifiez une deuxième session SSH via l’IP Tailscale ou le nom MagicDNS, puis restreignez le SSH public.
  * Si vous n’utilisez pas Tailscale, appliquez le durcissement équivalent à votre chemin SSH avant d’exposer davantage de services.
  * Cela est distinct de l’accès au Gateway. Vous pouvez toujours garder OpenClaw lié à l’interface de bouclage et utiliser un tunnel SSH ou Tailscale Serve pour le tableau de bord.

Les options Gateway propres à Tailscale se trouvent dans [Tailscale](</fr/gateway/tailscale>). Agent d’entreprise partagé sur un VPS Exécuter un seul agent pour une équipe est une configuration valide lorsque chaque utilisateur appartient au même périmètre de confiance et que l’agent est réservé à un usage professionnel.

  * Gardez-le sur un environnement d’exécution dédié (VPS/VM/conteneur + utilisateur/comptes OS dédiés).
  * Ne connectez pas cet environnement d’exécution à des comptes Apple/Google personnels ni à des profils personnels de navigateur/gestionnaire de mots de passe.
  * Si les utilisateurs sont adversaires entre eux, séparez-les par gateway/hôte/utilisateur OS.

Détails du modèle de sécurité : [Sécurité](</fr/gateway/security>). Utiliser des nœuds avec un VPS Vous pouvez garder le Gateway dans le cloud et associer des **nœuds** sur vos appareils locaux (Mac/iOS/Android/headless). Les nœuds fournissent les capacités locales écran/caméra/canvas et `system.run` pendant que le Gateway reste dans le cloud. Docs : [Nœuds](</fr/nodes>), [CLI des nœuds](</fr/cli/nodes>). Optimisation du démarrage pour les petites VM et les hôtes ARM Si les commandes CLI semblent lentes sur des VM peu puissantes (ou des hôtes ARM), activez le cache de compilation des modules de Node : bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF'export NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

  * `NODE_COMPILE_CACHE` améliore les temps de démarrage des commandes répétées.
  * `OPENCLAW_NO_RESPAWN=1` évite un surcoût de démarrage supplémentaire dû à un chemin d’auto-relance.
  * La première exécution d’une commande prépare le cache ; les exécutions suivantes sont plus rapides.
  * Pour les spécificités de Raspberry Pi, consultez [Raspberry Pi](</fr/install/raspberry-pi>).

Liste de contrôle d’optimisation systemd (facultatif) Pour les hôtes VM utilisant `systemd`, envisagez :

  * Ajouter des variables d’environnement de service pour un chemin de démarrage stable : 
    * `OPENCLAW_NO_RESPAWN=1`
    * `NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache`
  * Garder le comportement de redémarrage explicite : 
    * `Restart=always`
    * `RestartSec=2`
    * `TimeoutStartSec=90`
  * Préférer des disques adossés à un SSD pour les chemins d’état/cache afin de réduire les pénalités de démarrage à froid liées aux E/S aléatoires.

Pour le chemin standard `openclaw onboard --install-daemon`, modifiez l’unité utilisateur : bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Si vous avez délibérément installé une unité système à la place, modifiez `openclaw-gateway.service` via `sudo systemctl edit openclaw-gateway.service`. Comment les politiques `Restart=` aident la récupération automatisée : [systemd peut automatiser la récupération des services](<https://www.redhat.com/en/blog/systemd-automate-recovery>). Pour le comportement OOM sous Linux, la sélection du processus enfant victime et les diagnostics `exit 137`, consultez [pression mémoire Linux et arrêts OOM](</fr/platforms/linux#memory-pressure-and-oom-kills>). Connexe

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [DigitalOcean](</fr/install/digitalocean>)
  * [Fly.io](</fr/install/fly>)
  * [Hetzner](</fr/install/hetzner>)

](</fr/install/raspberry-pi>) Was this useful?YesNo ](</fr/install/exe-dev>)](</fr/install/azure>)](</fr/install/gcp>)](</fr/install/hostinger>)](</fr/install/hetzner>)](</fr/install/fly>)](</fr/install/oracle>)](</fr/install/digitalocean>)](</fr/install/northflank>)](</fr/install/railway>)