---
title: Mettre à jour
source_url: https://docs.openclaw.ai/fr/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

Mettez à jour OpenClaw en toute sécurité et basculez entre les canaux stable/beta/dev.

Si vous avez installé via **npm/pnpm/bun** (installation globale, sans métadonnées git), les mises à jour s’effectuent via le flux du gestionnaire de paquets dans [Mise à jour](</fr/install/updating>).

## Utilisation

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Options

  * `--no-restart` : ignore le redémarrage du service Gateway après une mise à jour réussie. Les mises à jour par gestionnaire de paquets qui redémarrent bien le Gateway vérifient que le service redémarré signale la version mise à jour attendue avant que la commande réussisse.
  * `--channel <stable|beta|dev>` : définit le canal de mise à jour (git + npm ; conservé dans la configuration).
  * `--tag <dist-tag|version|spec>` : remplace la cible du paquet pour cette mise à jour uniquement. Pour les installations par paquet, `main` correspond à `github:openclaw/openclaw#main`.
  * `--dry-run` : affiche un aperçu des actions de mise à jour prévues (canal/tag/cible/flux de redémarrage) sans écrire la configuration, installer, synchroniser les plugins ni redémarrer.
  * `--json` : affiche le JSON `UpdateRunResult` lisible par machine, incluant `postUpdate.plugins.warnings` lorsque des plugins gérés corrompus ou impossibles à charger doivent être réparés après la réussite de la mise à jour du cœur, les détails de repli des plugins du canal bêta lorsqu’un plugin n’a pas de version bêta, et `postUpdate.plugins.integrityDrifts` lorsqu’une dérive d’artefact de plugin npm est détectée pendant la synchronisation des plugins après mise à jour.
  * `--timeout <seconds>` : délai d’expiration par étape (1800 s par défaut).
  * `--yes` : ignore les invites de confirmation (par exemple la confirmation de rétrogradation).


`openclaw update` n’a pas d’option `--verbose`. Utilisez `--dry-run` pour prévisualiser les actions de canal/tag/installation/redémarrage prévues, `--json` pour des résultats lisibles par machine, et `openclaw update status --json` lorsque vous avez seulement besoin des détails de canal et de disponibilité. Si vous déboguez les journaux du Gateway autour d’une mise à jour, la verbosité de la console et le niveau des journaux fichier sont distincts : `--verbose` du Gateway affecte la sortie terminal/WebSocket, tandis que les journaux fichier exigent `logging.level: "debug"` ou `"trace"` dans la configuration. Consultez [Journalisation du Gateway](</fr/gateway/logging>).

## `update status`

Affiche le canal de mise à jour actif + le tag/la branche/le SHA git (pour les extractions source), ainsi que la disponibilité des mises à jour.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Options :

  * `--json` : affiche le JSON d’état lisible par machine.
  * `--timeout <seconds>` : délai d’expiration des vérifications (3 s par défaut).


## `update wizard`

Flux interactif pour choisir un canal de mise à jour et confirmer s’il faut redémarrer le Gateway après la mise à jour (le redémarrage est la valeur par défaut). Si vous sélectionnez `dev` sans extraction git, il propose d’en créer une.

Options :

  * `--timeout <seconds>` : délai d’expiration pour chaque étape de mise à jour (`1800` par défaut)


## Ce que cela fait

Lorsque vous changez explicitement de canal (`--channel ...`), OpenClaw maintient aussi la méthode d’installation alignée :

  * `dev` → garantit une extraction git (par défaut : `~/openclaw`, remplaçable avec `OPENCLAW_GIT_DIR`), la met à jour, puis installe la CLI globale depuis cette extraction.
  * `stable` → installe depuis npm avec `latest`.
  * `beta` → privilégie le dist-tag npm `beta`, mais se replie sur `latest` lorsque beta est absent ou plus ancien que la version stable actuelle.


Le programme de mise à jour automatique du cœur du Gateway (lorsqu’il est activé via la configuration) lance le chemin de mise à jour de la CLI en dehors du gestionnaire de requêtes du Gateway actif. Les mises à jour par gestionnaire de paquets `update.run` du plan de contrôle forcent un redémarrage de mise à jour non différé et sans période de refroidissement après le remplacement du paquet, car l’ancien processus Gateway peut encore avoir en mémoire des fragments pointant vers des fichiers supprimés par le nouveau paquet.

Pour les installations par gestionnaire de paquets, `openclaw update` résout la version du paquet cible avant d’appeler le gestionnaire de paquets. Les installations globales npm utilisent une installation intermédiaire : OpenClaw installe le nouveau paquet dans un préfixe npm temporaire, y vérifie l’inventaire `dist` empaqueté, puis remplace l’arborescence propre de ce paquet dans le vrai préfixe global. Si la vérification échoue, le doctor après mise à jour, la synchronisation des plugins et le travail de redémarrage ne s’exécutent pas depuis l’arborescence suspecte. Même lorsque la version installée correspond déjà à la cible, la commande actualise l’installation globale du paquet, puis exécute la synchronisation des plugins, une actualisation de l’achèvement des commandes du cœur et le travail de redémarrage. Cela garde les sidecars empaquetés et les enregistrements de plugins détenus par le canal alignés avec la version OpenClaw installée, tout en laissant les reconstructions complètes d’achèvement des commandes de plugins aux exécutions explicites de `openclaw completion --write-state`.

Lorsqu’un service Gateway géré local est installé et que le redémarrage est activé, les mises à jour par gestionnaire de paquets arrêtent le service en cours avant de remplacer l’arborescence du paquet, puis actualisent les métadonnées du service depuis l’installation mise à jour, redémarrent le service et vérifient que le Gateway redémarré signale la version attendue avant d’indiquer la réussite. Sur macOS, la vérification après mise à jour vérifie aussi que le LaunchAgent est chargé/en cours d’exécution pour le profil actif et que le port local loopback configuré est sain. Si le plist est installé mais que launchd ne le supervise pas, OpenClaw réamorce automatiquement le LaunchAgent, puis relance les vérifications de santé/version/canal. Un amorçage frais charge directement la tâche RunAtLoad, donc la récupération de mise à jour ne lance pas immédiatement `kickstart -k` sur le Gateway nouvellement démarré. Si le Gateway ne devient toujours pas sain, la commande quitte avec un code non nul et affiche le chemin du journal de redémarrage ainsi que des instructions explicites de redémarrage, réinstallation et retour arrière du paquet. Avec `--no-restart`, le remplacement du paquet s’exécute toujours, mais le service géré n’est ni arrêté ni redémarré ; le Gateway en cours d’exécution peut donc conserver l’ancien code jusqu’à ce que vous le redémarriez manuellement.

## Flux d’extraction git

### Sélection du canal

  * `stable` : extrait le dernier tag non bêta, puis construit et exécute doctor.
  * `beta` : privilégie le dernier tag `-beta`, mais se replie sur le dernier tag stable lorsque beta est absent ou plus ancien.
  * `dev` : extrait `main`, puis récupère et rebase.


### Étapes de mise à jour

* ### Vérifier que l’arborescence de travail est propre

Exige l’absence de modifications non validées.

* ### Changer de canal

Bascule vers le canal sélectionné (tag ou branche).

* ### Récupérer l’amont

Dev uniquement.

* ### Construction préalable (dev uniquement)

Exécute la construction TypeScript dans une arborescence de travail temporaire. Si la pointe échoue, remonte jusqu’à 10 commits pour trouver le commit constructible le plus récent. Définissez `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` pour exécuter aussi le lint pendant cette vérification préalable ; le lint s’exécute en mode série contraint, car les hôtes de mise à jour utilisateur sont souvent plus petits que les exécuteurs CI.

* ### Rebase

Rebase sur le commit sélectionné (dev uniquement).

* ### Installer les dépendances

Utilise le gestionnaire de paquets du dépôt. Pour les extractions pnpm, le programme de mise à jour amorce `pnpm` à la demande (d’abord via `corepack`, puis avec un repli temporaire `npm install pnpm@11`) au lieu d’exécuter `npm run build` dans un espace de travail pnpm.

* ### Construire l’interface de contrôle

Construit le gateway et l’interface de contrôle.

* ### Exécuter doctor

`openclaw doctor` s’exécute comme vérification finale de mise à jour sûre.

* ### Synchroniser les plugins

Synchronise les plugins avec le canal actif. Dev utilise les plugins groupés ; stable et beta utilisent npm. Met à jour les installations de plugins suivies.

Sur le canal de mise à jour beta, les installations de plugins npm et ClawHub suivies qui suivent la ligne default/latest essaient d’abord une version `@beta` du plugin. Si le plugin n’a pas de version bêta, OpenClaw se replie sur la spécification default/latest enregistrée et le signale comme avertissement. Pour les plugins npm, OpenClaw se replie aussi lorsque le paquet beta existe mais échoue à la validation d’installation. Ces avertissements de repli de plugin ne font pas échouer la mise à jour du cœur. Les versions exactes et les tags explicites ne sont pas réécrits.

## Raccourci `--update`

`openclaw --update` est réécrit en `openclaw update` (utile pour les shells et les scripts de lancement).

## Connexe

  * `openclaw doctor` (propose d’exécuter d’abord la mise à jour sur les extractions git)
  * [Canaux de développement](</fr/install/development-channels>)
  * [Mise à jour](</fr/install/updating>)
  * [Référence CLI](</fr/cli>)


Was this useful?YesNo