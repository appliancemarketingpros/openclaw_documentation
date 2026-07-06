---
title: Attacher la CLI
source_url: https://docs.openclaw.ai/fr/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` lance Claude Code avec une configuration MCP temporaire stricte liée à une session Gateway.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Options :

  * `--session <key>` lie l’autorisation à une session Gateway. Par défaut, utilise la session principale.
  * `--ttl <ms>` demande un TTL d’autorisation positif en millisecondes. Le Gateway applique son propre plafond.
  * `--bin <path>` sélectionne le binaire Claude Code. Par défaut, utilise `claude`.
  * `--print-config` écrit le fichier `.mcp.json` temporaire, affiche la commande de lancement et l’environnement, et laisse l’autorisation active jusqu’à l’expiration du TTL.


Le jeton porteur est transmis par des variables d’environnement, et non par argv. OpenClaw lance Claude Code avec `--strict-mcp-config --mcp-config <path>` afin que les serveurs MCP Claude ambiants ne rejoignent pas la session attachée. Les lancements normaux révoquent l’autorisation lorsque le processus Claude Code se termine.

Voir aussi : [CLI Gateway](</fr/cli/gateway>), [CLI MCP](</fr/cli/mcp>) et [CLI ACP](</fr/cli/acp>).

Was this useful?YesNo

Open issue