---
title: Répertoire
source_url: https://docs.openclaw.ai/fr/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

Recherches dans l’annuaire pour les canaux qui les prennent en charge (contacts/pairs, groupes et « moi »).

## Options courantes

  * `--channel <name>` : identifiant/alias du canal (obligatoire lorsque plusieurs canaux sont configurés ; automatique lorsqu’un seul est configuré)
  * `--account <id>` : identifiant du compte (par défaut : valeur par défaut du canal)
  * `--json` : sortie JSON


## Notes

  * `directory` est conçu pour vous aider à trouver des identifiants que vous pouvez coller dans d’autres commandes (en particulier `openclaw message send --target ...`).
  * Pour de nombreux canaux, les résultats reposent sur la configuration (listes d’autorisation / groupes configurés) plutôt que sur un annuaire fournisseur en direct.
  * Les Plugins de canal installés peuvent tout de même omettre la prise en charge de l’annuaire ; dans ce cas, la commande signale l’opération d’annuaire non prise en charge au lieu de réinstaller le Plugin.
  * La sortie par défaut est `id` (et parfois `name`) séparé par une tabulation ; utilisez `--json` pour les scripts.


## Utiliser les résultats avec `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## Formats d’identifiant (par canal)

  * WhatsApp : `+15551234567` (DM), `1234567890-1234567890@g.us` (groupe), `120363123456789@newsletter` (cible sortante Canal/Newsletter)
  * Telegram : `@username` ou identifiant numérique de discussion ; les groupes utilisent des identifiants numériques
  * Slack : `user:U…` et `channel:C…`
  * Discord : `user:<id>` et `channel:<id>`
  * Matrix (Plugin) : `user:@user:server`, `room:!roomId:server` ou `#alias:server`
  * Microsoft Teams (Plugin) : `user:<id>` et `conversation:<id>`
  * Zalo (Plugin) : identifiant utilisateur (Bot API)
  * Zalo Personal / `zalouser` (Plugin) : identifiant de fil (DM/groupe) depuis `zca` (`me`, `friend list`, `group list`)


## Soi-même (« moi »)

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## Pairs (contacts/utilisateurs)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## Groupes

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## Connexe

  * [Référence CLI](</fr/cli>)


Was this useful?YesNo