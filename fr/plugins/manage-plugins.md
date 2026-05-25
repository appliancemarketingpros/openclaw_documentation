---
title: Gérer les plugins
source_url: https://docs.openclaw.ai/fr/plugins/manage-plugins
scraped_at: 2026-05-25
---

La plupart des workflows de plugins tiennent en quelques commandes : rechercher, installer, redémarrer le Gateway, vérifier, puis désinstaller lorsque vous n’avez plus besoin du plugin.

## Lister les plugins

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Utilisez `--json` pour les scripts. Cela inclut les diagnostics du registre et le `dependencyStatus` statique de chaque plugin lorsque le package du plugin déclare des `dependencies` ou des `optionalDependencies`.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` est une vérification d’inventaire à froid. Elle indique ce qu’OpenClaw peut découvrir à partir de la config, des manifestes et du registre de plugins ; elle ne prouve pas qu’un processus Gateway déjà en cours d’exécution a importé le runtime du plugin.

## Installer des plugins

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Après avoir installé le code du plugin, redémarrez le Gateway qui sert vos canaux :

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Utilisez `inspect --runtime` lorsque vous avez besoin d’une preuve que le plugin a enregistré des surfaces runtime telles que des outils, hooks, services, méthodes Gateway ou commandes CLI appartenant au plugin.

## Mettre à jour des plugins

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Si un plugin a été installé depuis un dist-tag npm tel que `@beta`, les appels ultérieurs à `update <plugin-id>` réutilisent ce tag enregistré. Passer une spec npm explicite bascule l’installation suivie vers cette spec pour les futures mises à jour.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

La deuxième commande ramène un plugin vers la ligne de publication par défaut du registre lorsqu’il était auparavant épinglé à une version exacte ou à un tag.

Lorsque `openclaw update` s’exécute sur le canal bêta, les enregistrements de plugins npm et ClawHub sur la ligne par défaut essaient d’abord la publication `@beta` du plugin correspondant. Si cette publication bêta n’existe pas, OpenClaw se rabat sur la spec par défaut/la plus récente enregistrée. Pour les plugins npm, OpenClaw se rabat aussi lorsque le package bêta existe mais échoue à la validation d’installation. Les versions exactes et les tags explicites tels que `@rc` ou `@beta` sont conservés.

## Désinstaller des plugins

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

La désinstallation supprime l’entrée de config du plugin, l’enregistrement d’index du plugin, les entrées de liste d’autorisation/refus et les chemins de chargement liés le cas échéant. Les répertoires d’installation gérés sont supprimés sauf si vous passez `--keep-files`.

En mode Nix (`OPENCLAW_NIX_MODE=1`), les commandes d’installation, de mise à jour, de désinstallation, d’activation et de désactivation des plugins sont désactivées. Gérez plutôt ces choix dans la source Nix de l’installation ; pour nix-openclaw, utilisez le [Quick Start](<https://github.com/openclaw/nix-openclaw#quick-start>) orienté agent.

## Publier des plugins

Vous pouvez publier des plugins externes sur [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>), ou les deux.

### Publier sur ClawHub

ClawHub est la principale surface publique de découverte des plugins OpenClaw. Il donne aux utilisateurs des métadonnées consultables, un historique des versions et des résultats d’analyse du registre avant l’installation.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Les utilisateurs installent depuis ClawHub avec :

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

La forme nue vérifie toujours ClawHub en premier.

### Publier sur [npmjs.com](<http://npmjs.com>)

Les plugins npm natifs doivent inclure un manifeste de plugin et des métadonnées de point d’entrée OpenClaw dans `package.json`.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Les utilisateurs installent uniquement depuis npm avec :

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Si le même package est également disponible sur ClawHub, `npm:` ignore la recherche ClawHub et force la résolution npm.

## Choix de la source

  * **ClawHub** : à utiliser lorsque vous voulez une découverte native OpenClaw, des résumés d’analyse, des versions et des conseils d’installation.
  * **[npmjs.com](<http://npmjs.com>)** : à utiliser lorsque vous livrez déjà des packages JavaScript ou avez besoin de workflows dist-tags/registre privé npm.
  * **Git** : à utiliser lorsque vous voulez installer directement depuis une branche, un tag ou un commit.
  * **Chemin local** : à utiliser lorsque vous développez ou testez un plugin sur la même machine.


## Connexe

  * [Plugins](</fr/tools/plugin>) \- vue d’ensemble et dépannage
  * [`openclaw plugins`](</fr/cli/plugins>) \- référence CLI complète
  * [ClawHub](</fr/clawhub/cli>) \- publication et opérations de registre
  * [Créer des plugins](</fr/plugins/building-plugins>) \- créer un package de plugin
  * [Manifeste de plugin](</fr/plugins/manifest>) \- manifeste et métadonnées de package


Was this useful?YesNo