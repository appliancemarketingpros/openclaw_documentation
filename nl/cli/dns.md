---
title: DNS
source_url: https://docs.openclaw.ai/nl/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

DNS-helpers voor wide-area-detectie (Tailscale + CoreDNS). Momenteel gericht op macOS + Homebrew CoreDNS.

Gerelateerd:

  * Gateway-detectie: [Detectie](</nl/gateway/discovery>)
  * Configuratie voor wide-area-detectie: [Configuratie](</nl/gateway/configuration>)


## Instellen

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Plan de CoreDNS-installatie voor unicast DNS-SD-detectie of pas deze toe.

Opties:

  * `--domain <domain>`: domein voor wide-area-detectie (bijvoorbeeld `openclaw.internal`)
  * `--apply`: installeer of werk de CoreDNS-config bij en herstart de service (vereist sudo; alleen macOS)


Wat het toont:

  * opgelost detectiedomein
  * pad naar zonebestand
  * huidige tailnet-IP's
  * aanbevolen `openclaw.json`-detectieconfig
  * de in te stellen waarden voor Tailscale Split DNS-naamserver/domein


Opmerkingen:

  * Zonder `--apply` is de opdracht alleen een planningshelper en drukt deze de aanbevolen installatie af.
  * Als `--domain` wordt weggelaten, gebruikt OpenClaw `discovery.wideArea.domain` uit de configuratie.
  * `--apply` ondersteunt momenteel alleen macOS en verwacht Homebrew CoreDNS.
  * `--apply` initialiseert het zonebestand indien nodig, zorgt dat de CoreDNS-importstanza bestaat en herstart de `coredns` brew-service.


## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Detectie](</nl/gateway/discovery>)


Was this useful?YesNo