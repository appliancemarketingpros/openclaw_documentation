---
title: Conventions des espaces réservés secrets
source_url: https://docs.openclaw.ai/fr/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Conventions relatives aux espaces réservés de secrets

Utilisez des espaces réservés lisibles par des humains, mais qui ne ressemblent pas à de vrais secrets.

## Style recommandé

  * Préférez des valeurs descriptives comme `example-openai-key-not-real` ou `example-discord-bot-token`.
  * Pour les extraits shell, préférez `${OPENAI_API_KEY}` aux chaînes intégrées ressemblant à des jetons.
  * Gardez les exemples manifestement fictifs et limités à leur objectif (fournisseur, canal, type d’authentification).


## Évitez ces motifs dans la documentation

  * Texte littéral d’en-tête ou de pied de clé privée PEM.
  * Préfixes ressemblant à des identifiants actifs, par exemple `sk-...`, `xoxb-...`, `AKIA...`.
  * Jetons bearer d’apparence réaliste copiés depuis des journaux d’exécution.


## Exemple

bashCopy code
[code]
    # Bonexport OPENAI_API_KEY="example-openai-key-not-real" # Mieux (quand la documentation porte sur le câblage env)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue