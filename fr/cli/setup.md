---
title: Configuration
source_url: https://docs.openclaw.ai/fr/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Initialisez la configuration de base et l’espace de travail de l’agent. Lorsqu’un indicateur d’onboarding est présent, exécute également l’assistant.

## Options

Indicateur | Description  
---|---  
`--workspace <dir>` | Répertoire d’espace de travail de l’agent (par défaut `~/.openclaw/workspace`; stocké dans `agents.defaults.workspace`).  
`--wizard` | Exécuter l’onboarding interactif.  
`--non-interactive` | Exécuter l’onboarding sans invites.  
`--mode <mode>` | Mode d’onboarding : `local` ou `remote`.  
`--import-from <provider>` | Fournisseur de migration à exécuter pendant l’onboarding.  
`--import-source <path>` | Répertoire d’origine de l’agent source pour `--import-from`.  
`--import-secrets` | Importer les secrets pris en charge pendant la migration d’onboarding.  
`--remote-url <url>` | URL WebSocket du Gateway distant.  
`--remote-token <token>` | Jeton du Gateway distant (facultatif).  
  
### Déclenchement automatique de l’assistant

`openclaw setup` exécute l’assistant lorsque l’un de ces indicateurs est explicitement présent, même sans `--wizard` :

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Exemples

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Notes

  * `openclaw setup` simple initialise la configuration et l’espace de travail sans exécuter le flux d’onboarding complet.
  * Après une configuration simple, exécutez `openclaw onboard` pour le parcours guidé complet, `openclaw configure` pour des changements ciblés, ou `openclaw channels add` pour ajouter des comptes de canaux.
  * Si un état Hermes est détecté, l’onboarding interactif peut proposer automatiquement la migration. L’onboarding d’importation nécessite une configuration fraîche ; utilisez [Migrer](</fr/cli/migrate>) pour les plans d’essai à blanc, les sauvegardes et le mode d’écrasement en dehors de l’onboarding.


## Connexe

  * [Référence CLI](</fr/cli>)
  * [Onboarding (CLI)](</fr/start/wizard>)
  * [Bien démarrer](</fr/start/getting-started>)
  * [Vue d’ensemble de l’installation](</fr/install>)


Was this useful?YesNo