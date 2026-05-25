---
title: DNS
source_url: https://docs.openclaw.ai/es/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

Utilidades de DNS para el descubrimiento de área amplia (Tailscale + CoreDNS). Actualmente centrado en macOS + CoreDNS de Homebrew.

Relacionado:

  * Descubrimiento de Gateway: [Descubrimiento](</es/gateway/discovery>)
  * Configuración del descubrimiento de área amplia: [Configuración](</es/gateway/configuration>)


## Configuración inicial

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Planifica o aplica la configuración de CoreDNS para el descubrimiento DNS-SD de unidifusión.

Opciones:

  * `--domain <domain>`: dominio de descubrimiento de área amplia (por ejemplo, `openclaw.internal`)
  * `--apply`: instala o actualiza la configuración de CoreDNS y reinicia el servicio (requiere sudo; solo macOS)


Lo que muestra:

  * dominio de descubrimiento resuelto
  * ruta del archivo de zona
  * IP actuales de tailnet
  * configuración de descubrimiento recomendada para `openclaw.json`
  * los valores de servidor de nombres/dominio de Split DNS de Tailscale que se deben establecer


Notas:

  * Sin `--apply`, el comando solo es una utilidad de planificación e imprime la configuración recomendada.
  * Si se omite `--domain`, OpenClaw usa `discovery.wideArea.domain` de la configuración.
  * `--apply` actualmente solo admite macOS y espera CoreDNS de Homebrew.
  * `--apply` inicializa el archivo de zona si es necesario, garantiza que exista la estrofa de importación de CoreDNS y reinicia el servicio brew `coredns`.


## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Descubrimiento](</es/gateway/discovery>)


Was this useful?YesNo