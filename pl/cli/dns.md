---
title: DNS
source_url: https://docs.openclaw.ai/pl/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

Pomocnicze narzędzia DNS do wykrywania szerokoobszarowego (Tailscale + CoreDNS). Obecnie skupione na macOS + Homebrew CoreDNS.

Powiązane:

  * Wykrywanie Gateway: [Wykrywanie](</pl/gateway/discovery>)
  * Konfiguracja wykrywania szerokoobszarowego: [Konfiguracja](</pl/gateway/configuration>)


## Konfiguracja

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Zaplanuj lub zastosuj konfigurację CoreDNS na potrzeby wykrywania unicast DNS-SD.

Opcje:

  * `--domain <domain>`: domena wykrywania szerokoobszarowego (na przykład `openclaw.internal`)
  * `--apply`: zainstaluj lub zaktualizuj konfigurację CoreDNS i uruchom ponownie usługę (wymaga sudo; tylko macOS)


Co pokazuje:

  * rozpoznana domena wykrywania
  * ścieżka pliku strefy
  * bieżące adresy IP tailnetu
  * zalecana konfiguracja wykrywania `openclaw.json`
  * wartości serwera nazw/domeny Tailscale Split DNS do ustawienia


Uwagi:

  * Bez `--apply` polecenie służy tylko do planowania i wypisuje zalecaną konfigurację.
  * Jeśli `--domain` zostanie pominięte, OpenClaw używa `discovery.wideArea.domain` z konfiguracji.
  * `--apply` obecnie obsługuje tylko macOS i oczekuje Homebrew CoreDNS.
  * `--apply` w razie potrzeby inicjuje plik strefy, upewnia się, że istnieje wpis importu CoreDNS, i uruchamia ponownie usługę brew `coredns`.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Wykrywanie](</pl/gateway/discovery>)


Was this useful?YesNo