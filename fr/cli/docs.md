---
title: Documentation
source_url: https://docs.openclaw.ai/fr/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

Recherchez dans l’index de documentation OpenClaw en direct depuis le terminal. La commande lance un shell vers le point de terminaison public de recherche MCP de la documentation hébergée par Mintlify à l’adresse `https://docs.openclaw.ai/mcp.SearchOpenClaw` et affiche les résultats dans votre terminal.

## Utilisation

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

Arguments :

Argument | Description  
---|---  
`[query...]` | Requête de recherche en texte libre. Les requêtes de plusieurs mots sont jointes avec des espaces et envoyées comme une seule requête.  
  
## Exemples

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

Sans requête, `openclaw docs` affiche l’URL du point d’entrée de la documentation ainsi qu’un exemple de commande de recherche au lieu de lancer une recherche.

## Fonctionnement

`openclaw docs` invoque la CLI `mcporter` pour appeler l’outil MCP de recherche de la documentation, puis analyse les blocs `Title: / Link: / Content:` de la sortie de l’outil en une liste de résultats.

Pour résoudre `mcporter`, OpenClaw vérifie dans l’ordre :

  1. `mcporter` dans `PATH` (utilisé directement s’il est présent).
  2. `pnpm dlx mcporter ...` si `pnpm` est installé.
  3. `npx -y mcporter ...` si `npx` est installé.


Si aucun n’est disponible, la commande échoue avec une indication pour installer `pnpm` (`npm install -g pnpm`).

L’appel de recherche utilise un délai d’expiration fixe de 30 secondes. Les extraits de résultats sont tronqués à environ 220 caractères par entrée.

## Sortie

Dans un terminal riche (TTY), les résultats s’affichent sous forme d’en-tête suivi d’une liste à puces. Chaque puce affiche le titre de la page, l’URL liée de la documentation, et un court extrait à la ligne suivante. Les résultats vides affichent « Aucun résultat. ».

Dans une sortie non riche (redirigée, `--no-color`, scripts), les mêmes données s’affichent en Markdown :

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## Codes de sortie

Code | Signification  
---|---  
`0` | La recherche a réussi (y compris les réponses sans résultat).  
`1` | L’appel de l’outil MCP a échoué ; stderr est affiché en ligne.  
  
## Associé

  * [Référence CLI](</fr/cli>)
  * [Documentation en direct](<https://docs.openclaw.ai>)


Was this useful?YesNo