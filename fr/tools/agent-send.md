---
title: Envoi de l’agent
source_url: https://docs.openclaw.ai/fr/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` exécute un seul tour d’agent depuis la ligne de commande sans nécessiter de message de discussion entrant. Utilisez-le pour les workflows scriptés, les tests et la livraison programmatique.

## Démarrage rapide

* ### Exécuter un tour d’agent simple

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Cela envoie le message via le Gateway et affiche la réponse.

* ### Cibler un agent ou une session spécifique

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Livrer la réponse à un canal

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Options

Option | Description  
---|---  
`--message \<text\>` | Message à envoyer (obligatoire)  
`--to \<dest\>` | Déduire la clé de session à partir d’une cible (téléphone, identifiant de discussion)  
`--agent \<id\>` | Cibler un agent configuré (utilise sa session `main`)  
`--session-id \<id\>` | Réutiliser une session existante par identifiant  
`--local` | Forcer le runtime intégré local (ignorer le Gateway)  
`--deliver` | Envoyer la réponse à un canal de discussion  
`--channel \<name\>` | Canal de livraison (whatsapp, telegram, discord, slack, etc.)  
`--reply-to \<target\>` | Remplacement de la cible de livraison  
`--reply-channel \<name\>` | Remplacement du canal de livraison  
`--reply-account \<id\>` | Remplacement de l’identifiant du compte de livraison  
`--thinking \<level\>` | Définir le niveau de raisonnement pour le profil de modèle sélectionné  
`--verbose \<on|full|off\>` | Définir le niveau de verbosité  
`--timeout \<seconds\>` | Remplacer le délai d’expiration de l’agent  
`--json` | Produire du JSON structuré  
  
## Comportement

  * Par défaut, la CLI passe **par le Gateway**. Ajoutez `--local` pour forcer le runtime intégré sur la machine actuelle.
  * Si le Gateway est inaccessible, la CLI **se rabat** sur l’exécution intégrée locale.
  * Sélection de session : `--to` déduit la clé de session (les cibles de groupe/canal préservent l’isolation ; les discussions directes sont regroupées dans `main`).
  * Les options de raisonnement et de verbosité persistent dans le magasin de session.
  * Sortie : texte brut par défaut, ou `--json` pour une charge utile structurée + métadonnées.
  * Avec `--json --deliver`, le JSON inclut l’état de livraison pour les envois envoyés, supprimés, partiels et échoués. Consultez [État de livraison JSON](</fr/cli/agent#json-delivery-status>).


## Exemples

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Associés

[**Référence de la CLI d’agent** Référence complète des options et indicateurs de `openclaw agent`. ](</fr/cli/agent>) [**Sous-agents** Lancement de sous-agents en arrière-plan. ](</fr/tools/subagents>) [**Sessions** Fonctionnement des clés de session et résolution de `--to`, `--agent` et `--session-id`. ](</fr/concepts/session>) [**Commandes slash** Catalogue de commandes natives utilisé dans les sessions d’agent. ](</fr/tools/slash-commands>)

Was this useful?YesNo