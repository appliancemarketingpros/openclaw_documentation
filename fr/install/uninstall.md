---
title: Désinstaller
source_url: https://docs.openclaw.ai/fr/install/uninstall
scraped_at: 2026-05-25
---

Deux chemins :

  * **Chemin simple** si `openclaw` est toujours installé.
  * **Suppression manuelle du service** si la CLI a disparu mais que le service fonctionne encore.


## Chemin simple (CLI toujours installée)

Recommandé : utilisez le programme de désinstallation intégré :

bashCopy code
[code]
    openclaw uninstall
[/code]

Non interactif (automatisation / npx) :

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Étapes manuelles (même résultat) :

  1. Arrêter le service gateway :

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Désinstaller le service gateway (launchd/systemd/schtasks) :

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Supprimer l’état + la configuration :

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Si vous avez défini `OPENCLAW_CONFIG_PATH` vers un emplacement personnalisé hors du répertoire d’état, supprimez également ce fichier.

  4. Supprimer votre espace de travail (facultatif, supprime les fichiers d’agent) :

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Supprimer l’installation de la CLI (choisissez celle que vous avez utilisée) :

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Si vous avez installé l’application macOS :

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Remarques :

  * Si vous avez utilisé des profils (`--profile` / `OPENCLAW_PROFILE`), répétez l’étape 3 pour chaque répertoire d’état (les valeurs par défaut sont `~/.openclaw-<profile>`).
  * En mode distant, le répertoire d’état se trouve sur l’**hôte gateway** , donc exécutez aussi les étapes 1 à 4 là-bas.


## Suppression manuelle du service (CLI non installée)

Utilisez ceci si le service gateway continue à fonctionner alors que `openclaw` est absent.

### macOS (launchd)

Le label par défaut est `ai.openclaw.gateway` (ou `ai.openclaw.<profile>` ; les anciens `com.openclaw.*` peuvent encore exister) :

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Si vous avez utilisé un profil, remplacez le label et le nom du plist par `ai.openclaw.<profile>`. Supprimez tout plist hérité `com.openclaw.*` si présent.

### Linux (unité utilisateur systemd)

Le nom d’unité par défaut est `openclaw-gateway.service` (ou `openclaw-gateway-<profile>.service`) :

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (tâche planifiée)

Le nom de tâche par défaut est `OpenClaw Gateway` (ou `OpenClaw Gateway (<profile>)`). Le script de tâche se trouve dans votre répertoire d’état.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Si vous avez utilisé un profil, supprimez le nom de tâche correspondant et `~\.openclaw-<profile>\gateway.cmd`.

## Installation normale vs extraction source

### Installation normale ([install.sh](<http://install.sh>) / npm / pnpm / bun)

Si vous avez utilisé `https://openclaw.ai/install.sh` ou `install.ps1`, la CLI a été installée avec `npm install -g openclaw@latest`. Supprimez-la avec `npm rm -g openclaw` (ou `pnpm remove -g` / `bun remove -g` si vous l’avez installée de cette manière).

### Extraction source (git clone)

Si vous exécutez depuis une extraction de dépôt (`git clone` \+ `openclaw ...` / `bun run openclaw ...`) :

  1. Désinstallez le service gateway **avant** de supprimer le dépôt (utilisez le chemin simple ci-dessus ou la suppression manuelle du service).
  2. Supprimez le répertoire du dépôt.
  3. Supprimez l’état + l’espace de travail comme indiqué ci-dessus.


## Voir aussi

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Guide de migration](</fr/install/migrating>)


Was this useful?YesNo