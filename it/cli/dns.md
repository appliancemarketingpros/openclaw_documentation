---
title: DNS
source_url: https://docs.openclaw.ai/it/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

Strumenti di supporto DNS per il rilevamento su rete geografica (Tailscale + CoreDNS). Attualmente incentrati su macOS + Homebrew CoreDNS.

Correlati:

  * Rilevamento Gateway: [Rilevamento](</it/gateway/discovery>)
  * Configurazione del rilevamento su rete geografica: [Configurazione](</it/gateway/configuration>)


## Configurazione

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Pianifica o applica la configurazione di CoreDNS per il rilevamento DNS-SD unicast.

Opzioni:

  * `--domain <domain>`: dominio di rilevamento su rete geografica (per esempio `openclaw.internal`)
  * `--apply`: installa o aggiorna la configurazione di CoreDNS e riavvia il servizio (richiede sudo; solo macOS)


Cosa mostra:

  * dominio di rilevamento risolto
  * percorso del file di zona
  * IP tailnet correnti
  * configurazione di rilevamento consigliata per `openclaw.json`
  * valori di nameserver/dominio Split DNS di Tailscale da impostare


Note:

  * Senza `--apply`, il comando è solo uno strumento di pianificazione e stampa la configurazione consigliata.
  * Se `--domain` è omesso, OpenClaw usa `discovery.wideArea.domain` dalla configurazione.
  * `--apply` attualmente supporta solo macOS e richiede Homebrew CoreDNS.
  * `--apply` inizializza il file di zona se necessario, assicura che la stanza di importazione di CoreDNS esista e riavvia il servizio brew `coredns`.


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Rilevamento](</it/gateway/discovery>)


Was this useful?YesNo