---
title: DNS
source_url: https://docs.openclaw.ai/fr/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

Assistants DNS pour la découverte étendue (Tailscale + CoreDNS). Actuellement centré sur macOS + Homebrew CoreDNS.

Connexe :

  * Découverte du Gateway : [Découverte](</fr/gateway/discovery>)
  * Configuration de la découverte étendue : [Configuration](</fr/gateway/configuration>)


## Configuration

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Planifier ou appliquer la configuration de CoreDNS pour la découverte DNS-SD unicast.

Options :

  * `--domain <domain>` : domaine de découverte étendue (par exemple `openclaw.internal`)
  * `--apply` : installer ou mettre à jour la configuration de CoreDNS et redémarrer le service (nécessite sudo ; macOS uniquement)


Ce qu’elle affiche :

  * domaine de découverte résolu
  * chemin du fichier de zone
  * adresses IP actuelles du réseau Tailscale
  * configuration de découverte `openclaw.json` recommandée
  * les valeurs de serveur de noms/domaine Split DNS Tailscale à définir


Notes :

  * Sans `--apply`, la commande est uniquement un assistant de planification et affiche la configuration recommandée.
  * Si `--domain` est omis, OpenClaw utilise `discovery.wideArea.domain` depuis la configuration.
  * `--apply` prend actuellement en charge uniquement macOS et s’attend à Homebrew CoreDNS.
  * `--apply` initialise le fichier de zone si nécessaire, garantit que la strophe d’importation CoreDNS existe, et redémarre le service brew `coredns`.


## Connexe

  * [Référence CLI](</fr/cli>)
  * [Découverte](</fr/gateway/discovery>)


Was this useful?YesNo