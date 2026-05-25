---
title: DNS
source_url: https://docs.openclaw.ai/de/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

DNS-Helfer für Wide-Area-Erkennung (Tailscale + CoreDNS). Derzeit auf macOS + Homebrew CoreDNS ausgerichtet.

Verwandt:

  * Gateway-Erkennung: [Erkennung](</de/gateway/discovery>)
  * Wide-Area-Erkennungskonfiguration: [Konfiguration](</de/gateway/configuration>)


## Einrichtung

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

CoreDNS-Einrichtung für Unicast-DNS-SD-Erkennung planen oder anwenden.

Optionen:

  * `--domain <domain>`: Wide-Area-Erkennungsdomain (zum Beispiel `openclaw.internal`)
  * `--apply`: CoreDNS-Konfiguration installieren oder aktualisieren und den Dienst neu starten (erfordert sudo; nur macOS)


Angezeigte Informationen:

  * aufgelöste Erkennungsdomain
  * Zone-Dateipfad
  * aktuelle Tailnet-IPs
  * empfohlene `openclaw.json`-Erkennungskonfiguration
  * die festzulegenden Tailscale-Split-DNS-Nameserver-/Domainwerte


Hinweise:

  * Ohne `--apply` dient der Befehl nur als Planungshilfe und gibt die empfohlene Einrichtung aus.
  * Wenn `--domain` ausgelassen wird, verwendet OpenClaw `discovery.wideArea.domain` aus der Konfiguration.
  * `--apply` unterstützt derzeit nur macOS und erwartet Homebrew CoreDNS.
  * `--apply` initialisiert bei Bedarf die Zone-Datei, stellt sicher, dass die CoreDNS-Import-Anweisung vorhanden ist, und startet den Brew-Dienst `coredns` neu.


## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Erkennung](</de/gateway/discovery>)


Was this useful?YesNo