---
title: DNS
source_url: https://docs.openclaw.ai/uk/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

DNS-помічники для широкомасштабного виявлення (Tailscale + CoreDNS). Наразі зосереджено на macOS + Homebrew CoreDNS.

Пов’язане:

  * Виявлення Gateway: [Виявлення](</uk/gateway/discovery>)
  * Конфігурація широкомасштабного виявлення: [Конфігурація](</uk/gateway/configuration>)


## Налаштування

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Планує або застосовує налаштування CoreDNS для виявлення unicast DNS-SD.

Параметри:

  * `--domain <domain>`: домен широкомасштабного виявлення (наприклад, `openclaw.internal`)
  * `--apply`: установити або оновити конфігурацію CoreDNS і перезапустити сервіс (потрібен sudo; лише macOS)


Що показує:

  * визначений домен виявлення
  * шлях до файлу зони
  * поточні IP-адреси tailnet
  * рекомендовану конфігурацію виявлення `openclaw.json`
  * значення nameserver/domain для Tailscale Split DNS, які потрібно встановити


Примітки:

  * Без `--apply` команда є лише помічником для планування й виводить рекомендоване налаштування.
  * Якщо `--domain` пропущено, OpenClaw використовує `discovery.wideArea.domain` з конфігурації.
  * `--apply` наразі підтримує лише macOS і очікує Homebrew CoreDNS.
  * `--apply` за потреби ініціалізує файл зони, забезпечує наявність stanza імпорту CoreDNS і перезапускає brew-сервіс `coredns`.


## Пов’язане

  * [Довідка CLI](</uk/cli>)
  * [Виявлення](</uk/gateway/discovery>)


Was this useful?YesNo