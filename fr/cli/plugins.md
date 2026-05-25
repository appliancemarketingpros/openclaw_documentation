---
title: Plugins
source_url: https://docs.openclaw.ai/fr/cli/plugins
scraped_at: 2026-05-25
---

Gérer les plugins du Gateway, les packs de hooks et les bundles compatibles.

[**Système de Plugin** Guide utilisateur pour installer, activer et dépanner les plugins. ](</fr/tools/plugin>) [**Gérer les plugins** Exemples rapides pour installer, lister, mettre à jour, désinstaller et publier. ](</fr/plugins/manage-plugins>) [**Bundles de Plugin** Modèle de compatibilité des bundles. ](</fr/plugins/bundles>) [**Manifeste de Plugin** Champs du manifeste et schéma de configuration. ](</fr/plugins/manifest>) [**Sécurité** Renforcement de la sécurité pour les installations de plugins. ](</fr/gateway/security>)

## Commandes

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

Pour analyser une installation, une inspection, une désinstallation ou une actualisation de registre lente, exécutez la commande avec `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1`. La trace écrit les durées des phases sur stderr et garde la sortie JSON analysable. Voir [Débogage](</fr/help/debugging#plugin-lifecycle-trace>).

### Installation

bashCopy code
[code]
    openclaw plugins search "calendar"                   # search ClawHub pluginsopenclaw plugins install <package>                      # npm by defaultopenclaw plugins install clawhub:<package>              # ClawHub onlyopenclaw plugins install npm:<package>                  # npm onlyopenclaw plugins install npm-pack:<path.tgz>            # local npm pack through npm install semanticsopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # overwrite existing installopenclaw plugins install <package> --pin                # pin versionopenclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # local pathopenclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

Les mainteneurs qui testent des installations au moment de la configuration peuvent remplacer les sources d’installation automatique de plugins avec des variables d’environnement protégées. Voir [Remplacements d’installation de plugins](</fr/plugins/install-overrides>).

`plugins search` interroge ClawHub pour les packages de plugins installables et affiche des noms de packages prêts à installer. Il recherche des packages de plugins de code et de bundles de plugins, pas des Skills. Utilisez `openclaw skills search` pour les Skills ClawHub.

Includes de configuration et réparation de configuration invalide

Si votre section `plugins` est adossée à un `$include` à fichier unique, `plugins install/update/enable/disable/uninstall` écrit dans ce fichier inclus et laisse `openclaw.json` intact. Les includes racine, les tableaux d’includes et les includes avec remplacements frères échouent de manière fermée au lieu d’être aplatis. Voir [Includes de configuration](</fr/gateway/configuration>) pour les formes prises en charge.

Si la configuration est invalide pendant l’installation, `plugins install` échoue normalement de manière fermée et vous indique d’exécuter d’abord `openclaw doctor --fix`. Pendant le démarrage du Gateway et le rechargement à chaud, une configuration de plugin invalide échoue de manière fermée comme toute autre configuration invalide ; `openclaw doctor --fix` peut mettre en quarantaine l’entrée de plugin invalide. La seule exception documentée au moment de l’installation est un chemin étroit de récupération de plugin groupé pour les plugins qui optent explicitement pour `openclaw.install.allowInvalidConfigRecovery`.

\--force et réinstallation vs mise à jour

`--force` réutilise la cible d’installation existante et écrase en place un plugin ou un pack de hooks déjà installé. Utilisez-le lorsque vous réinstallez intentionnellement le même id depuis un nouveau chemin local, une archive, un package ClawHub ou un artefact npm. Pour les mises à niveau courantes d’un plugin npm déjà suivi, préférez `openclaw plugins update <id-or-npm-spec>`.

Si vous exécutez `plugins install` pour un id de plugin déjà installé, OpenClaw s’arrête et vous oriente vers `plugins update <id-or-npm-spec>` pour une mise à niveau normale, ou vers `plugins install <package> --force` lorsque vous voulez réellement écraser l’installation actuelle depuis une source différente.

Portée de --pin

`--pin` s’applique uniquement aux installations npm. Il n’est pas pris en charge avec les installations `git:` ; utilisez une référence git explicite telle que `git:github.com/acme/plugin@v1.2.3` lorsque vous voulez une source épinglée. Il n’est pas pris en charge avec `--marketplace`, car les installations marketplace conservent les métadonnées de source marketplace au lieu d’une spec npm.

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` est une option de dernier recours pour les faux positifs du scanner intégré de code dangereux. Elle permet à l’installation de continuer même lorsque le scanner intégré signale des résultats `critical`, mais elle ne contourne **pas** les blocages de politique de hooks `before_install` du plugin et ne contourne **pas** les échecs d’analyse.

Ce flag CLI s’applique aux flux d’installation/mise à jour de plugins. Les installations de dépendances de Skills appuyées par le Gateway utilisent le remplacement de requête correspondant `dangerouslyForceUnsafeInstall`, tandis que `openclaw skills install` reste un flux séparé de téléchargement/installation de Skills ClawHub.

Si un plugin que vous avez publié sur ClawHub est bloqué par une analyse de registre, utilisez les étapes éditeur dans [ClawHub](</fr/clawhub/security>).

Packs de hooks et specs npm

`plugins install` est aussi la surface d’installation pour les packs de hooks qui exposent `openclaw.hooks` dans `package.json`. Utilisez `openclaw hooks` pour une visibilité filtrée des hooks et l’activation par hook, pas pour l’installation de packages.

Les specs npm sont **uniquement registre** (nom du package + **version exacte** ou **dist-tag** facultatif). Les specs Git/URL/fichier et les plages semver sont rejetées. Les installations de dépendances s’exécutent localement au projet avec `--ignore-scripts` par sécurité, même lorsque votre shell possède des paramètres d’installation npm globaux. Les racines npm de plugins gérées héritent des `overrides` npm au niveau package d’OpenClaw ; les épingles de sécurité de l’hôte s’appliquent donc aussi aux dépendances de plugins hissées.

Utilisez `npm:<package>` lorsque vous voulez rendre la résolution npm explicite. Les specs de packages nues s’installent aussi directement depuis npm pendant la transition de lancement.

Les specs nues et `@latest` restent sur la piste stable. Les versions de correction OpenClaw horodatées comme `2026.5.3-1` sont des versions stables pour cette vérification. Si npm résout l’une ou l’autre vers une préversion, OpenClaw s’arrête et vous demande d’y adhérer explicitement avec une balise de préversion comme `@beta`/`@rc` ou une version de préversion exacte comme `@1.2.3-beta.4`.

Si une spec d’installation nue correspond à un id de plugin officiel (par exemple `diffs`), OpenClaw installe directement l’entrée du catalogue. Pour installer un package npm portant le même nom, utilisez une spec portée explicite (par exemple `@scope/diffs`).

Dépôts Git

Utilisez `git:<repo>` pour installer directement depuis un dépôt git. Les formes prises en charge incluent `git:github.com/owner/repo`, `git:owner/repo`, les URL de clone complètes `https://`, `ssh://`, `git://`, `file://` et `git@host:owner/repo.git`. Ajoutez `@<ref>` ou `#<ref>` pour extraire une branche, une balise ou un commit avant l’installation.

Les installations Git clonent dans un répertoire temporaire, extraient la référence demandée lorsqu’elle est présente, puis utilisent l’installateur de répertoire de plugin normal. Cela signifie que la validation du manifeste, l’analyse de code dangereux, le travail d’installation du gestionnaire de packages et les enregistrements d’installation se comportent comme pour les installations npm. Les installations git enregistrées incluent l’URL/la ref source ainsi que le commit résolu, afin que `openclaw plugins update` puisse résoudre à nouveau la source plus tard.

Après une installation depuis git, utilisez `openclaw plugins inspect <id> --runtime --json` pour vérifier les enregistrements runtime comme les méthodes Gateway et les commandes CLI. Si le plugin a enregistré une racine CLI avec `api.registerCli`, exécutez cette commande directement via la CLI racine d’OpenClaw, par exemple `openclaw demo-plugin ping`.

Archives

Archives prises en charge : `.zip`, `.tgz`, `.tar.gz`, `.tar`. Les archives de plugins OpenClaw natifs doivent contenir un `openclaw.plugin.json` valide à la racine du plugin extrait ; les archives qui contiennent uniquement `package.json` sont rejetées avant qu’OpenClaw écrive les enregistrements d’installation.

Utilisez `npm-pack:<path.tgz>` lorsque le fichier est une archive tar npm-pack et que vous voulez tester le même chemin d’installation de racine npm gérée que celui utilisé par les installations de registre, y compris la vérification de `package-lock.json`, l’analyse des dépendances hissées et les enregistrements d’installation npm. Les chemins d’archive simples s’installent toujours comme archives locales sous la racine extensions des plugins.

Les installations marketplace Claude sont également prises en charge.

Les installations ClawHub utilisent un localisateur explicite `clawhub:<package>` :

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

Les specs de plugins nues compatibles npm s’installent depuis npm par défaut pendant la transition de lancement :

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

Utilisez `npm:` pour rendre la résolution npm uniquement explicite :

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw vérifie la compatibilité annoncée de l’API de plugin / Gateway minimum avant l’installation. Lorsque la version ClawHub sélectionnée publie un artefact ClawPack, OpenClaw télécharge le `.tgz` empaqueté npm versionné, vérifie l’en-tête de condensat ClawHub et le condensat de l’artefact, puis l’installe via le chemin d’archive normal. Les anciennes versions de ClawHub sans métadonnées ClawPack s’installent encore via l’ancien chemin de vérification des archives de paquet. Les installations enregistrées conservent leurs métadonnées de source ClawHub, le type d’artefact, l’intégrité npm, le shasum npm, le nom de tarball et les informations de condensat ClawPack pour les mises à jour ultérieures. Les installations ClawHub non versionnées conservent une spécification enregistrée non versionnée afin que `openclaw plugins update` puisse suivre les nouvelles versions ClawHub ; les sélecteurs explicites de version ou d’étiquette tels que `clawhub:pkg@1.2.3` et `clawhub:pkg@beta` restent épinglés à ce sélecteur.

#### Raccourci de marketplace

Utilisez le raccourci `plugin@marketplace` lorsque le nom de marketplace existe dans le cache de registre local de Claude à `~/.claude/plugins/known_marketplaces.json` :

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

Utilisez `--marketplace` lorsque vous voulez transmettre explicitement la source de marketplace :

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### Marketplace sources

  * un nom de marketplace connu de Claude provenant de `~/.claude/plugins/known_marketplaces.json`
  * une racine de marketplace locale ou un chemin `marketplace.json`
  * un raccourci de dépôt GitHub tel que `owner/repo`
  * une URL de dépôt GitHub telle que `https://github.com/owner/repo`
  * une URL git


### Remote marketplace rules

Pour les marketplaces distantes chargées depuis GitHub ou git, les entrées de plugin doivent rester dans le dépôt de marketplace cloné. OpenClaw accepte les sources par chemin relatif depuis ce dépôt et rejette les sources de plugin HTTP(S), les chemins absolus, git, GitHub et autres sources sans chemin dans les manifestes distants.

Pour les chemins et archives locaux, OpenClaw détecte automatiquement :

  * les plugins OpenClaw natifs (`openclaw.plugin.json`)
  * les bundles compatibles Codex (`.codex-plugin/plugin.json`)
  * les bundles compatibles Claude (`.claude-plugin/plugin.json` ou la disposition par défaut des composants Claude)
  * les bundles compatibles Cursor (`.cursor-plugin/plugin.json`)


### Lister

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

Afficher uniquement les plugins activés.

Basculer de la vue en tableau vers des lignes de détail par plugin avec les métadonnées source/origine/version/activation.

Inventaire lisible par machine, avec diagnostics de registre et état d’installation des dépendances de paquet.

`plugins search` est une recherche distante dans le catalogue ClawHub. Elle n’inspecte pas l’état local, ne modifie pas la configuration, n’installe pas de paquets et ne charge pas le code de runtime du plugin. Les résultats de recherche incluent le nom de paquet ClawHub, la famille, le canal, la version, le résumé et une indication d’installation telle que `openclaw plugins install clawhub:<package>`.

Pour le travail sur des plugins intégrés dans une image Docker empaquetée, montez par liaison le répertoire source du plugin sur le chemin source empaqueté correspondant, par exemple `/app/extensions/synology-chat`. OpenClaw découvrira cette superposition source montée avant `/app/dist/extensions/synology-chat` ; un simple répertoire source copié reste inerte afin que les installations empaquetées normales utilisent toujours le dist compilé.

Pour le débogage des hooks de runtime :

  * `openclaw plugins inspect <id> --runtime --json` affiche les hooks enregistrés et les diagnostics d’une passe d’inspection avec module chargé. L’inspection de runtime n’installe jamais les dépendances ; utilisez `openclaw doctor --fix` pour nettoyer l’état hérité des dépendances ou récupérer les plugins téléchargeables manquants qui sont référencés par la configuration.
  * `openclaw gateway status --deep --require-rpc` confirme le Gateway accessible, les indications de service/processus, le chemin de configuration et l’état de santé RPC.
  * Les hooks de conversation non intégrés (`llm_input`, `llm_output`, `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `before_agent_finalize`, `agent_end`) nécessitent `plugins.entries.<id>.hooks.allowConversationAccess=true`.


Utilisez `--link` pour éviter de copier un répertoire local (ajoute à `plugins.load.paths`) :

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### Index des plugins

Les métadonnées d’installation des plugins sont un état géré par machine, pas une configuration utilisateur. Les installations et mises à jour les écrivent dans `plugins/installs.json` sous le répertoire d’état OpenClaw actif. Sa carte de premier niveau `installRecords` est la source durable des métadonnées d’installation, y compris les enregistrements de manifestes de plugins cassés ou manquants. Le tableau `plugins` est le cache de registre à froid dérivé des manifestes. Le fichier inclut un avertissement de ne pas le modifier et est utilisé par `openclaw plugins update`, la désinstallation, les diagnostics et le registre de plugins à froid.

Lorsque OpenClaw voit des enregistrements hérités livrés `plugins.installs` dans la configuration, les lectures de runtime les traitent comme entrée de compatibilité sans réécrire `openclaw.json`. Les écritures explicites de plugins et `openclaw doctor --fix` déplacent ces enregistrements dans l’index des plugins et suppriment la clé de configuration lorsque les écritures de configuration sont autorisées ; si l’une ou l’autre écriture échoue, les enregistrements de configuration sont conservés afin que les métadonnées d’installation ne soient pas perdues.

### Désinstaller

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall` supprime les enregistrements de plugin de `plugins.entries`, de l’index persistant des plugins, des entrées de liste d’autorisation/refus des plugins et des entrées liées `plugins.load.paths` le cas échéant. Sauf si `--keep-files` est défini, la désinstallation supprime aussi le répertoire d’installation géré suivi lorsqu’il se trouve dans la racine des extensions de plugins d’OpenClaw. Pour les plugins de mémoire active, l’emplacement mémoire est réinitialisé à `memory-core`.

### Mettre à jour

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

Les mises à jour s’appliquent aux installations de plugins suivies dans l’index de plugins géré et aux installations de packs de hooks suivies dans `hooks.internal.installs`.

Resolving plugin id vs npm spec

Lorsque vous transmettez un identifiant de plugin, OpenClaw réutilise la spécification d’installation enregistrée pour ce plugin. Cela signifie que les dist-tags précédemment stockés tels que `@beta` et les versions exactes épinglées continuent d’être utilisés lors des exécutions ultérieures de `update <id>`.

Pour les installations npm, vous pouvez également transmettre une spécification de paquet npm explicite avec un dist-tag ou une version exacte. OpenClaw résout ce nom de paquet vers l’enregistrement de plugin suivi, met à jour ce plugin installé et enregistre la nouvelle spécification npm pour les futures mises à jour basées sur l’identifiant.

Transmettre le nom du paquet npm sans version ni étiquette se résout aussi vers l’enregistrement de plugin suivi. Utilisez cela lorsqu’un plugin était épinglé à une version exacte et que vous voulez le remettre sur la ligne de publication par défaut du registre.

Beta channel updates

`openclaw plugins update` réutilise la spécification de plugin suivie sauf si vous transmettez une nouvelle spécification. `openclaw update` connaît en plus le canal de mise à jour OpenClaw actif : sur le canal bêta, les enregistrements de plugins npm et ClawHub de ligne par défaut essaient d’abord `@beta`, puis se replient sur la spécification par défaut/latest enregistrée si aucune publication bêta du plugin n’existe. Ce repli est signalé comme avertissement et ne fait pas échouer la mise à jour du noyau. Les versions exactes et les étiquettes explicites restent épinglées à ce sélecteur.

Version checks and integrity drift

Avant une mise à jour npm en direct, OpenClaw vérifie la version du paquet installé par rapport aux métadonnées du registre npm. Si la version installée et l’identité d’artefact enregistrée correspondent déjà à la cible résolue, la mise à jour est ignorée sans téléchargement, réinstallation ni réécriture de `openclaw.json`.

Lorsqu’un hachage d’intégrité stocké existe et que le hachage de l’artefact récupéré change, OpenClaw traite cela comme une dérive d’artefact npm. La commande interactive `openclaw plugins update` affiche les hachages attendu et réel et demande confirmation avant de continuer. Les assistants de mise à jour non interactifs échouent de manière fermée sauf si l’appelant fournit une politique de continuation explicite.

\--dangerously-force-unsafe-install on update

`--dangerously-force-unsafe-install` est également disponible sur `plugins update` comme dérogation de dernier recours pour les faux positifs de l’analyse de code dangereux intégrée pendant les mises à jour de plugins. Il ne contourne toujours pas les blocages de politique `before_install` du plugin ni le blocage en cas d’échec d’analyse, et il s’applique uniquement aux mises à jour de plugins, pas aux mises à jour de packs de hooks.

### Inspecter

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspecter affiche l’identité, l’état de chargement, la source, les capacités de manifeste, les indicateurs de politique, les diagnostics, les métadonnées d’installation, les capacités de bundle et toute prise en charge détectée de serveur MCP ou LSP sans importer le runtime du plugin par défaut. Ajoutez `--runtime` pour charger le module du plugin et inclure les hooks, outils, commandes, services, méthodes de Gateway et routes HTTP enregistrés. L’inspection de runtime signale directement les dépendances de plugin manquantes ; les installations et réparations restent dans `openclaw plugins install`, `openclaw plugins update` et `openclaw doctor --fix`.

Les commandes CLI appartenant à un plugin sont généralement installées comme groupes de commandes racine `openclaw`, mais les plugins peuvent aussi enregistrer des commandes imbriquées sous un parent du noyau tel que `openclaw nodes`. Après que `inspect --runtime` affiche une commande sous `cliCommands`, exécutez-la au chemin indiqué ; par exemple, un plugin qui enregistre `demo-git` peut être vérifié avec `openclaw demo-git ping`.

Chaque plugin est classé selon ce qu’il enregistre réellement au runtime :

  * **plain-capability** — un type de capacité (par exemple, un Plugin uniquement fournisseur)
  * **hybrid-capability** — plusieurs types de capacités (par exemple, texte + parole + images)
  * **hook-only** — uniquement des hooks, sans capacités ni surfaces
  * **non-capability** — outils/commandes/services, mais sans capacités


Consultez [Formes de Plugin](</fr/plugins/architecture#plugin-shapes>) pour en savoir plus sur le modèle de capacités.

### Doctor

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor` signale les erreurs de chargement des Plugins, les diagnostics de manifeste/découverte et les avis de compatibilité. Quand tout est correct, il affiche `No plugin issues detected.`

Si un Plugin configuré est présent sur le disque mais bloqué par les contrôles de sécurité des chemins du chargeur, la validation de configuration conserve l’entrée du Plugin et la signale comme `present but blocked`. Corrigez le diagnostic de Plugin bloqué précédent, comme la propriété du chemin ou des permissions accessibles en écriture à tous, au lieu de supprimer la configuration `plugins.entries.<id>` ou `plugins.allow`.

Pour les échecs de forme de module, comme des exports `register`/`activate` manquants, relancez avec `OPENCLAW_PLUGIN_LOAD_DEBUG=1` afin d’inclure un résumé compact de la forme des exports dans la sortie de diagnostic.

### Registre

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

Le registre local des Plugins est le modèle de lecture à froid persistant d’OpenClaw pour l’identité des Plugins installés, leur activation, les métadonnées de source et la propriété des contributions. Le démarrage normal, la recherche du propriétaire du fournisseur, la classification de la configuration des canaux et l’inventaire des Plugins peuvent le lire sans importer de modules d’exécution de Plugin.

Utilisez `plugins registry` pour vérifier si le registre persistant est présent, à jour ou obsolète. Utilisez `--refresh` pour le reconstruire à partir de l’index persistant des Plugins, de la politique de configuration et des métadonnées de manifeste/package. Il s’agit d’un chemin de réparation, pas d’un chemin d’activation à l’exécution.

`openclaw doctor --fix` répare aussi les dérives npm gérées adjacentes au registre : si un package `@openclaw/*` orphelin ou récupéré sous la racine npm gérée des Plugins masque un Plugin groupé, doctor supprime ce package obsolète et reconstruit le registre afin que le démarrage valide le manifeste groupé. Doctor relie aussi le package hôte `openclaw` aux Plugins npm gérés qui déclarent `peerDependencies.openclaw`, afin que les imports d’exécution locaux au package, tels que `openclaw/plugin-sdk/*`, se résolvent après des mises à jour ou des réparations npm.

### Marketplace

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

La liste du Marketplace accepte un chemin de Marketplace local, un chemin `marketplace.json`, un raccourci GitHub comme `owner/repo`, une URL de dépôt GitHub ou une URL git. `--json` affiche le libellé de source résolu ainsi que le manifeste Marketplace analysé et les entrées de Plugins.

## Associé

  * [Créer des Plugins](</fr/plugins/building-plugins>)
  * [Référence CLI](</fr/cli>)
  * [ClawHub](</fr/clawhub>)


Was this useful?YesNo