---
title: ClawDock
source_url: https://docs.openclaw.ai/fr/install/clawdock
scraped_at: 2026-05-25
---

ClawDock est une petite couche d’assistance shell pour les installations OpenClaw basées sur Docker.

Elle vous fournit des commandes courtes comme `clawdock-start`, `clawdock-dashboard` et `clawdock-fix-token` au lieu d’invocations plus longues de type `docker compose ...`.

Si vous n’avez pas encore configuré Docker, commencez par [Docker](</fr/install/docker>).

## Installation

Utilisez le chemin canonique de l’assistant :

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Si vous aviez précédemment installé ClawDock depuis `scripts/shell-helpers/clawdock-helpers.sh`, réinstallez-le depuis le nouveau chemin `scripts/clawdock/clawdock-helpers.sh`. L’ancien chemin brut GitHub a été supprimé.

## Ce que vous obtenez

### Opérations de base

Command | Description  
---|---  
`clawdock-start` | Démarrer le Gateway  
`clawdock-stop` | Arrêter le Gateway  
`clawdock-restart` | Redémarrer le Gateway  
`clawdock-status` | Vérifier l’état du conteneur  
`clawdock-logs` | Suivre les journaux du Gateway  
  
### Accès au conteneur

Command | Description  
---|---  
`clawdock-shell` | Ouvrir un shell dans le conteneur du Gateway  
`clawdock-cli <command>` | Exécuter des commandes CLI OpenClaw dans Docker  
`clawdock-exec <command>` | Exécuter une commande arbitraire dans le conteneur  
  
### Interface Web et appairage

Command | Description  
---|---  
`clawdock-dashboard` | Ouvrir l’URL de la Control UI  
`clawdock-devices` | Lister les appairages d’appareils en attente  
`clawdock-approve <id>` | Approuver une demande d’appairage  
  
### Configuration et maintenance

Command | Description  
---|---  
`clawdock-fix-token` | Configurer le jeton du Gateway dans le conteneur  
`clawdock-update` | Tirer, reconstruire et redémarrer  
`clawdock-rebuild` | Reconstruire uniquement l’image Docker  
`clawdock-clean` | Supprimer les conteneurs et les volumes  
  
### Utilitaires

Command | Description  
---|---  
`clawdock-health` | Exécuter un contrôle de santé du Gateway  
`clawdock-token` | Afficher le jeton du Gateway  
`clawdock-cd` | Aller au répertoire du projet OpenClaw  
`clawdock-config` | Ouvrir `~/.openclaw`  
`clawdock-show-config` | Afficher les fichiers de configuration avec les valeurs masquées  
`clawdock-workspace` | Ouvrir le répertoire de l’espace de travail  
  
## Premier parcours

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

Si le navigateur indique qu’un appairage est requis :

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Configuration et secrets

ClawDock fonctionne avec la même séparation de configuration Docker que celle décrite dans [Docker](</fr/install/docker>) :

  * `<project>/.env` pour les valeurs propres à Docker, comme le nom de l’image, les ports et le jeton du Gateway
  * `~/.openclaw/.env` pour les clés de fournisseurs et les jetons de bots basés sur l’environnement
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` pour l’authentification OAuth/API-key de fournisseur stockée
  * `~/.openclaw/openclaw.json` pour la configuration du comportement


Utilisez `clawdock-show-config` lorsque vous voulez inspecter rapidement les fichiers `.env` et `openclaw.json`. Il masque les valeurs `.env` dans sa sortie affichée.

## Voir aussi

[**Docker** Installation Docker canonique pour OpenClaw. ](</fr/install/docker>) [**Runtime de VM Docker** Runtime de VM géré par Docker pour une isolation renforcée. ](</fr/install/docker-vm-runtime>) [**Mise à jour** Mise à jour du paquet OpenClaw et des services gérés. ](</fr/install/updating>)

Was this useful?YesNo