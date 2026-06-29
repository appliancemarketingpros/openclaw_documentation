---
title: DNS
source_url: https://docs.openclaw.ai/ru/cli/dns
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw dns`

DNS-помощники для обнаружения в глобальной сети (Tailscale + CoreDNS). Сейчас ориентированы на macOS + Homebrew CoreDNS.

Связано:

  * Обнаружение Gateway: [Обнаружение](</ru/gateway/discovery>)
  * Конфигурация обнаружения в глобальной сети: [Конфигурация](</ru/gateway/configuration>)


## Настройка

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Спланировать или применить настройку CoreDNS для обнаружения через одноадресный DNS-SD.

Параметры:

  * `--domain <domain>`: домен обнаружения в глобальной сети (например, `openclaw.internal`)
  * `--apply`: установить или обновить конфигурацию CoreDNS и перезапустить службу (требуется sudo; только macOS)


Что выводится:

  * разрешенный домен обнаружения
  * путь к файлу зоны
  * текущие IP-адреса tailnet
  * рекомендуемая конфигурация обнаружения `openclaw.json`
  * значения сервера имен/домена Tailscale Split DNS, которые нужно задать


Примечания:

  * Без `--apply` команда служит только помощником для планирования и выводит рекомендуемую настройку.
  * Если `--domain` не указан, OpenClaw использует `discovery.wideArea.domain` из конфигурации.
  * `--apply` сейчас поддерживает только macOS и ожидает Homebrew CoreDNS.
  * `--apply` при необходимости инициализирует файл зоны, проверяет наличие директивы импорта CoreDNS и перезапускает brew-службу `coredns`.


## Связано

  * [Справочник CLI](</ru/cli>)
  * [Обнаружение](</ru/gateway/discovery>)


Was this useful?YesNo

Open issue