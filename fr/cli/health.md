---
title: Santé
source_url: https://docs.openclaw.ai/fr/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Récupère l’état de santé depuis le Gateway en cours d’exécution.

## Options

Indicateur | Valeur par défaut | Description  
---|---|---  
`--json` | `false` | Afficher du JSON lisible par machine plutôt que du texte.  
`--timeout <ms>` | `10000` | Délai d’expiration de la connexion en millisecondes.  
`--verbose` | `false` | Journalisation détaillée. Force une sonde en direct et développe la sortie par agent.  
`--debug` | `false` | Alias de `--verbose`.  
  
Exemples :

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Remarques :

  * Par défaut, `openclaw health` demande au Gateway en cours d’exécution son instantané d’état de santé. Lorsque le Gateway dispose déjà d’un instantané récent mis en cache, il peut renvoyer cette charge utile mise en cache et l’actualiser en arrière-plan.
  * `--verbose` force une sonde en direct, affiche les détails de connexion au Gateway et développe la sortie lisible par l’utilisateur pour tous les comptes et agents configurés.
  * La sortie inclut les magasins de sessions par agent lorsque plusieurs agents sont configurés.


## Voir aussi

  * [Référence CLI](</fr/cli>)
  * [État de santé du Gateway](</fr/gateway/health>)


Was this useful?YesNo