---
title: Aplicación para Linux
source_url: https://docs.openclaw.ai/es/platforms/linux
scraped_at: 2026-05-25
---

Gateway es totalmente compatible con Linux. **Node es el entorno de ejecución recomendado**. Bun no se recomienda para Gateway (errores de WhatsApp/Telegram).

Hay aplicaciones complementarias nativas para Linux planificadas. Las contribuciones son bienvenidas si quieres ayudar a crear una.

## Ruta rápida para principiantes (VPS)

  1. Instala Node 24 (recomendado; Node 22 LTS, actualmente `22.16+`, sigue funcionando por compatibilidad)
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. Desde tu portátil: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. Abre `http://127.0.0.1:18789/` y autentícate con el secreto compartido configurado (token de forma predeterminada; contraseña si configuras `gateway.auth.mode: "password"`)


Guía completa del servidor Linux: [Servidor Linux](</es/vps>). Ejemplo de VPS paso a paso: [exe.dev](</es/install/exe-dev>)

## Instalación

  * [Primeros pasos](</es/start/getting-started>)
  * [Instalación y actualizaciones](</es/install/updating>)
  * Flujos opcionales: [Bun (experimental)](</es/install/bun>), [Nix](</es/install/nix>), [Docker](</es/install/docker>)


## Gateway

  * [Runbook de Gateway](</es/gateway>)
  * [Configuración](</es/gateway/configuration>)


## Instalación del servicio Gateway (CLI)

Usa uno de estos:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

O:

CodeCopy code
[code]
    openclaw gateway install
[/code]

O:

CodeCopy code
[code]
    openclaw configure
[/code]

Selecciona **Servicio Gateway** cuando se te solicite.

Reparar/migrar:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Control del sistema (unidad de usuario systemd)

OpenClaw instala un servicio systemd de **usuario** de forma predeterminada. Usa un servicio de **sistema** para servidores compartidos o siempre activos. `openclaw gateway install` y `openclaw onboard --install-daemon` ya generan la unidad canónica actual para ti; escribe una manualmente solo cuando necesites una configuración personalizada de sistema/gestor de servicios. La guía completa del servicio está en el [runbook de Gateway](</es/gateway>).

Configuración mínima:

Crea `~/.config/systemd/user/openclaw-gateway[-<profile>].service`:

CodeCopy code
[code]
    [Unit]Description=OpenClaw Gateway (profile: <profile>, v<version>)After=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

Actívalo:

CodeCopy code
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
[/code]

## Presión de memoria y finalizaciones por OOM

En Linux, el kernel elige una víctima OOM cuando un cgroup de host, VM o contenedor se queda sin memoria. Gateway puede ser una mala víctima porque posee sesiones y conexiones de canales de larga duración. Por ello, OpenClaw sesga los procesos secundarios transitorios para que sean finalizados antes que Gateway cuando sea posible.

Para los procesos secundarios de Linux aptos, OpenClaw inicia el proceso secundario mediante un breve envoltorio `/bin/sh` que eleva el `oom_score_adj` propio del proceso secundario a `1000`, y luego hace `exec` del comando real. Esta es una operación sin privilegios porque el proceso secundario solo aumenta su propia probabilidad de finalización por OOM.

Las superficies de procesos secundarios cubiertas incluyen:

  * procesos secundarios de comandos gestionados por el supervisor,
  * procesos secundarios de shell PTY,
  * procesos secundarios de servidor MCP stdio,
  * procesos de navegador/Chrome iniciados por OpenClaw.


El envoltorio es solo para Linux y se omite cuando `/bin/sh` no está disponible. También se omite si el entorno del proceso secundario establece `OPENCLAW_CHILD_OOM_SCORE_ADJ=0`, `false`, `no` u `off`.

Para verificar un proceso secundario:

bashCopy code
[code]
    cat /proc/<child-pid>/oom_score_adj
[/code]

El valor esperado para los procesos secundarios cubiertos es `1000`. El proceso Gateway debe conservar su puntuación normal, normalmente `0`.

Esto no sustituye el ajuste normal de memoria. Si un VPS o contenedor finaliza repetidamente procesos secundarios, aumenta el límite de memoria, reduce la concurrencia o añade controles de recursos más estrictos, como `MemoryMax=` de systemd o límites de memoria a nivel de contenedor.

## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Servidor Linux](</es/vps>)
  * [Raspberry Pi](</es/install/raspberry-pi>)


Was this useful?YesNo