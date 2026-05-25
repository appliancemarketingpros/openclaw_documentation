---
title: Plataformas
source_url: https://docs.openclaw.ai/es/platforms
scraped_at: 2026-05-25
---

El núcleo de OpenClaw está escrito en TypeScript. **Node es el runtime recomendado**. Bun no se recomienda para el Gateway: hay problemas conocidos con los canales de WhatsApp y Telegram; consulta [Bun (experimental)](</es/install/bun>) para obtener más detalles.

Existen aplicaciones complementarias para macOS (aplicación de barra de menús) y nodos móviles (iOS/Android). Las aplicaciones complementarias para Windows y Linux están planificadas, pero el Gateway es totalmente compatible hoy. También están planificadas aplicaciones complementarias nativas para Windows; se recomienda usar el Gateway mediante WSL2.

## Elige tu sistema operativo

  * macOS: [macOS](</es/platforms/macos>)
  * iOS: [iOS](</es/platforms/ios>)
  * Android: [Android](</es/platforms/android>)
  * Windows: [Windows](</es/platforms/windows>)
  * Linux: [Linux](</es/platforms/linux>)


## VPS y alojamiento

  * Centro de VPS: [Alojamiento VPS](</es/vps>)
  * [Fly.io](<http://Fly.io>): [Fly.io](</es/install/fly>)
  * Hetzner (Docker): [Hetzner](</es/install/hetzner>)
  * GCP (Compute Engine): [GCP](</es/install/gcp>)
  * Azure (VM Linux): [Azure](</es/install/azure>)
  * exe.dev (VM + proxy HTTPS): [exe.dev](</es/install/exe-dev>)


## Enlaces comunes

  * Guía de instalación: [Primeros pasos](</es/start/getting-started>)
  * Guía operativa del Gateway: [Gateway](</es/gateway>)
  * Configuración del Gateway: [Configuración](</es/gateway/configuration>)
  * Estado del servicio: `openclaw gateway status`


## Instalación del servicio Gateway (CLI)

Usa una de estas opciones (todas compatibles):

  * Asistente (recomendado): `openclaw onboard --install-daemon`
  * Directa: `openclaw gateway install`
  * Flujo de configuración: `openclaw configure` → selecciona **Servicio Gateway**
  * Reparar/migrar: `openclaw doctor` (ofrece instalar o corregir el servicio)


El destino del servicio depende del sistema operativo:

  * macOS: LaunchAgent (`ai.openclaw.gateway` o `ai.openclaw.<profile>`; heredado `com.openclaw.*`)
  * Linux/WSL2: servicio de usuario systemd (`openclaw-gateway[-<profile>].service`)
  * Windows nativo: tarea programada (`OpenClaw Gateway` o `OpenClaw Gateway (<profile>)`), con una alternativa de elemento de inicio de sesión por usuario en la carpeta Inicio si se deniega la creación de la tarea


## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Aplicación para macOS](</es/platforms/macos>)
  * [Aplicación para iOS](</es/platforms/ios>)


Was this useful?YesNo