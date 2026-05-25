---
title: Instalar
source_url: https://docs.openclaw.ai/es/install
scraped_at: 2026-05-25
---

## Requisitos del sistema

  * **Node 24** (recomendado) o Node 22.16+ - el script de instalación se encarga de esto automáticamente
  * **macOS, Linux o Windows** \- se admiten tanto Windows nativo como WSL2; WSL2 es más estable. Consulta [Windows](</es/platforms/windows>).
  * `pnpm` solo es necesario si compilas desde el código fuente


## Recomendado: script de instalación

La forma más rápida de instalar. Detecta tu sistema operativo, instala Node si es necesario, instala OpenClaw e inicia la incorporación.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

Para instalar sin ejecutar la incorporación:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

Para ver todas las marcas y opciones de CI/automatización, consulta [Detalles internos del instalador](</es/install/installer>).

## Métodos de instalación alternativos

### Instalador de prefijo local (`install-cli.sh`)

Usa esto cuando quieras mantener OpenClaw y Node bajo un prefijo local como `~/.openclaw`, sin depender de una instalación de Node de todo el sistema:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Admite instalaciones con npm de forma predeterminada, además de instalaciones desde git checkout bajo el mismo flujo de prefijo. Referencia completa: [Detalles internos del instalador](</es/install/installer#install-clish>).

¿Ya está instalado? Cambia entre instalaciones de paquete y de git con `openclaw update --channel dev` y `openclaw update --channel stable`. Consulta [Actualizar](</es/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm o bun

Si ya administras Node por tu cuenta:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Troubleshooting: sharp build errors (npm)

Si `sharp` falla debido a una libvips instalada globalmente:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### Desde el código fuente

Para colaboradores o cualquier persona que quiera ejecutar desde un checkout local:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

O salta el enlace y usa `pnpm openclaw ...` desde dentro del repositorio. Consulta [Configuración](</es/start/setup>) para ver los flujos de trabajo de desarrollo completos.

### Instalar desde GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Contenedores y gestores de paquetes

[**Docker** Implementaciones en contenedores o sin interfaz gráfica. ](</es/install/docker>) [**Podman** Alternativa de contenedor sin root a Docker. ](</es/install/podman>) [**Nix** Instalación declarativa mediante Nix flake. ](</es/install/nix>) [**Ansible** Aprovisionamiento automatizado de flotas. ](</es/install/ansible>) [**Bun** Uso solo de CLI mediante el entorno de ejecución Bun. ](</es/install/bun>)

## Verificar la instalación

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Si quieres un inicio gestionado después de la instalación:

  * macOS: LaunchAgent mediante `openclaw onboard --install-daemon` u `openclaw gateway install`
  * Linux/WSL2: servicio de usuario systemd mediante los mismos comandos
  * Windows nativo: primero Scheduled Task, con un elemento de inicio de sesión por usuario en la carpeta Startup como alternativa si se deniega la creación de la tarea


## Alojamiento e implementación

Implementa OpenClaw en un servidor en la nube o VPS:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9lcy9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Actualizar, migrar o desinstalar [**Updating** Mantén OpenClaw actualizado. ](</es/install/updating>) [**Migrating** Traslada a una máquina nueva. ](</es/install/migrating>) [**Uninstall** Elimina OpenClaw por completo. ](</es/install/uninstall>) Solución de problemas: `openclaw` no encontrado Si la instalación se realizó correctamente pero `openclaw` no se encuentra en tu terminal: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Si `$(npm prefix -g)/bin` no está en tu `$PATH`, agrégalo al archivo de inicio de tu shell (`~/.zshrc` o `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Luego abre una terminal nueva. Consulta [Configuración de Node](</es/install/node>) para obtener más detalles. ](</es/install/northflank>) Was this useful?YesNo ](</es/install/render>)](</es/install/railway>)](</es/install/azure>)](</es/install/gcp>)](</es/install/hetzner>)](</es/install/kubernetes>)](</es/install/docker-vm-runtime>)](</es/vps>)