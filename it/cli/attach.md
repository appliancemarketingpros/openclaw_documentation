---
title: Collega la CLI
source_url: https://docs.openclaw.ai/it/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` avvia Claude Code con una configurazione MCP temporanea rigorosa associata a una sessione Gateway.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

Opzioni:

  * `--session <key>` associa l'autorizzazione a una sessione Gateway. Il valore predefinito è la sessione principale.
  * `--ttl <ms>` richiede un TTL positivo dell'autorizzazione in millisecondi. Il Gateway applica il proprio limite massimo.
  * `--bin <path>` seleziona il binario Claude Code. Il valore predefinito è `claude`.
  * `--print-config` scrive il file temporaneo `.mcp.json`, stampa il comando di avvio e l'ambiente, e mantiene attiva l'autorizzazione fino alla scadenza del TTL.


Il token bearer viene passato tramite variabili d'ambiente, non tramite argv. OpenClaw avvia Claude Code con `--strict-mcp-config --mcp-config <path>` in modo che i server MCP Claude dell'ambiente non si uniscano alla sessione collegata. Gli avvii normali revocano l'autorizzazione quando il processo Claude Code termina.

Vedi anche: [CLI Gateway](</it/cli/gateway>), [CLI MCP](</it/cli/mcp>) e [CLI ACP](</it/cli/acp>).

Was this useful?YesNo

Open issue