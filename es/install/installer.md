---
title: Aspectos internos del instalador
source_url: https://docs.openclaw.ai/es/install/installer
scraped_at: 2026-05-25
---

OpenClaw incluye tres scripts de instalación, servidos desde `openclaw.ai`.

Script | Plataforma | Qué hace  
---|---|---  
`install.sh` | macOS / Linux / WSL | Instala Node si es necesario, instala OpenClaw mediante npm (predeterminado) o git, y puede ejecutar la incorporación.  
`install-cli.sh` | macOS / Linux / WSL | Instala Node + OpenClaw en un prefijo local (`~/.openclaw`) con modos de npm o copia de trabajo de git. No requiere root.  
`install.ps1` | Windows (PowerShell) | Instala Node si es necesario, instala OpenClaw mediante npm (predeterminado) o git, y puede ejecutar la incorporación.  
  
## Comandos rápidos

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### Flujo ([install.sh](<http://install.sh>))

* ### Detectar sistema operativo

Compatible con macOS y Linux (incluido WSL). Si se detecta macOS, instala Homebrew si falta.

* ### Asegurar Node.js 24 de forma predeterminada

Comprueba la versión de Node e instala Node 24 si es necesario (Homebrew en macOS, scripts de configuración de NodeSource en Linux apt/dnf/yum). OpenClaw sigue siendo compatible con Node 22 LTS, actualmente `22.16+`, por compatibilidad.

* ### Asegurar Git

Instala Git si falta.

* ### Instalar OpenClaw

  * Método `npm` (predeterminado): instalación global de npm
  * Método `git`: clona/actualiza el repositorio, instala dependencias con pnpm, compila y luego instala el wrapper en `~/.local/bin/openclaw`


* ### Tareas posteriores a la instalación

  * Actualiza un servicio Gateway cargado en la medida de lo posible (`openclaw gateway install --force`, luego reinicia)
  * Ejecuta `openclaw doctor --non-interactive` en actualizaciones e instalaciones con git (en la medida de lo posible)
  * Intenta la incorporación cuando corresponde (TTY disponible, incorporación no deshabilitada, y las comprobaciones de bootstrap/configuración pasan)
  * Establece `SHARP_IGNORE_GLOBAL_LIBVIPS=1` de forma predeterminada


### Detección de copia de trabajo de código fuente

Si se ejecuta dentro de una copia de trabajo de OpenClaw (`package.json` \+ `pnpm-workspace.yaml`), el script ofrece:

  * usar la copia de trabajo (`git`), o
  * usar la instalación global (`npm`)


Si no hay TTY disponible y no se ha definido ningún método de instalación, usa `npm` de forma predeterminada y muestra una advertencia.

El script sale con el código `2` para una selección de método no válida o valores de `--install-method` no válidos.

### Ejemplos ([install.sh](<http://install.sh>))

### Predeterminado

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Omitir incorporación

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Instalación con Git

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main mediante npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Ejecución de prueba

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Referencia de flags Flag | Descripción  
---|---  
`--install-method npm|git` | Elige el método de instalación (predeterminado: `npm`). Alias: `--method`  
`--npm` | Atajo para el método npm  
`--git` | Atajo para el método git. Alias: `--github`  
`--version <version|dist-tag|spec>` | Versión de npm, dist-tag o especificación de paquete (predeterminado: `latest`)  
`--beta` | Usa el dist-tag beta si está disponible; de lo contrario, vuelve a `latest`  
`--git-dir <path>` | Directorio de la copia de trabajo (predeterminado: `~/openclaw`). Alias: `--dir`  
`--no-git-update` | Omite `git pull` para una copia de trabajo existente  
`--no-prompt` | Deshabilita los prompts  
`--no-onboard` | Omite la incorporación  
`--onboard` | Habilita la incorporación  
`--dry-run` | Imprime las acciones sin aplicar cambios  
`--verbose` | Habilita la salida de depuración (`set -x`, registros de npm de nivel notice)  
`--help` | Muestra el uso (`-h`)  
Referencia de variables de entorno Variable | Descripción  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Método de instalación  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | Versión de npm, dist-tag o especificación de paquete  
`OPENCLAW_BETA=0|1` | Usa beta si está disponible  
`OPENCLAW_GIT_DIR=<path>` | Directorio de la copia de trabajo  
`OPENCLAW_GIT_UPDATE=0|1` | Alterna actualizaciones de git  
`OPENCLAW_NO_PROMPT=1` | Deshabilita los prompts  
`OPENCLAW_NO_ONBOARD=1` | Omite la incorporación  
`OPENCLAW_DRY_RUN=1` | Modo de ejecución de prueba  
`OPENCLAW_VERBOSE=1` | Modo de depuración  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Nivel de registro de npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Controla el comportamiento de sharp/libvips (predeterminado: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Flujo ([install-cli.sh](<http://install-cli.sh>))

* ### Instalar runtime local de Node

Descarga un tarball fijado y compatible de Node LTS (la versión está incrustada en el script y se actualiza de forma independiente) en `<prefix>/tools/node-v<version>` y verifica SHA-256.

* ### Asegurar Git

Si falta Git, intenta instalarlo mediante apt/dnf/yum en Linux o Homebrew en macOS.

* ### Instalar OpenClaw bajo el prefijo

  * Método `npm` (predeterminado): instala bajo el prefijo con npm y luego escribe el wrapper en `<prefix>/bin/openclaw`
  * Método `git`: clona/actualiza una copia de trabajo (predeterminado `~/openclaw`) y aun así escribe el wrapper en `<prefix>/bin/openclaw`


* ### Actualizar servicio Gateway cargado

Si un servicio Gateway ya está cargado desde ese mismo prefijo, el script ejecuta `openclaw gateway install --force`, luego `openclaw gateway restart`, y comprueba el estado del Gateway en la medida de lo posible.

### Ejemplos ([install-cli.sh](<http://install-cli.sh>))

### Predeterminado

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Prefijo personalizado + versión

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Instalación con Git

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### Salida JSON de automatización

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Ejecutar incorporación

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Referencia de flags Flag | Descripción  
---|---  
`--prefix <path>` | Prefijo de instalación (predeterminado: `~/.openclaw`)  
`--install-method npm|git` | Elige el método de instalación (predeterminado: `npm`). Alias: `--method`  
`--npm` | Atajo para el método npm  
`--git`, `--github` | Atajo para el método git  
`--git-dir <path>` | Directorio de la copia de trabajo de git (predeterminado: `~/openclaw`). Alias: `--dir`  
`--version <ver>` | Versión de OpenClaw o dist-tag (predeterminado: `latest`)  
`--node-version <ver>` | Versión de Node (predeterminado: `22.22.0`)  
`--json` | Emite eventos NDJSON  
`--onboard` | Ejecuta `openclaw onboard` después de la instalación  
`--no-onboard` | Omite la incorporación (predeterminado)  
`--set-npm-prefix` | En Linux, fuerza el prefijo de npm a `~/.npm-global` si el prefijo actual no tiene permisos de escritura  
`--help` | Muestra el uso (`-h`)  
Referencia de variables de entorno Variable | Descripción  
---|---  
`OPENCLAW_PREFIX=<path>` | Prefijo de instalación  
`OPENCLAW_INSTALL_METHOD=git|npm` | Método de instalación  
`OPENCLAW_VERSION=<ver>` | Versión de OpenClaw o dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Versión de Node  
`OPENCLAW_GIT_DIR=<path>` | Directorio de checkout de Git para instalaciones con git  
`OPENCLAW_GIT_UPDATE=0|1` | Activa o desactiva las actualizaciones de git para checkouts existentes  
`OPENCLAW_NO_ONBOARD=1` | Omitir onboarding  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Nivel de registro de npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Controla el comportamiento de sharp/libvips (predeterminado: `1`)  
  
* * *

## install.ps1

### Flujo (install.ps1)

* ### Asegurar el entorno de PowerShell + Windows

Requiere PowerShell 5+.

* ### Asegurar Node.js 24 de forma predeterminada

Si falta, intenta instalarlo mediante winget, luego Chocolatey y luego Scoop. Node 22 LTS, actualmente `22.16+`, sigue siendo compatible por compatibilidad.

* ### Instalar OpenClaw

  * Método `npm` (predeterminado): instalación global de npm usando el `-Tag` seleccionado, iniciada desde un directorio temporal de instalador con permisos de escritura para que las shells abiertas en carpetas protegidas como `C:\` sigan funcionando
  * Método `git`: clona/actualiza el repositorio, instala/compila con pnpm e instala el wrapper en `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Tareas posteriores a la instalación

  * Agrega el directorio bin necesario al PATH del usuario cuando sea posible
  * Actualiza un servicio de Gateway cargado con el mejor esfuerzo (`openclaw gateway install --force`, luego reinicio)
  * Ejecuta `openclaw doctor --non-interactive` en actualizaciones e instalaciones con git (mejor esfuerzo)


* ### Gestionar fallos

Las instalaciones con `iwr ... | iex` y scriptblock informan un error terminante sin cerrar la sesión actual de PowerShell. Las instalaciones directas con `powershell -File` / `pwsh -File` siguen saliendo con código distinto de cero para automatización.

### Ejemplos (install.ps1)

### Predeterminado

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Instalación con git

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### main de GitHub mediante npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Directorio git personalizado

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Ejecución de prueba

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Traza de depuración

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Referencia de flags Flag | Descripción  
---|---  
`-InstallMethod npm|git` | Método de instalación (predeterminado: `npm`)  
`-Tag <tag|version|spec>` | dist-tag, versión o especificación de paquete de npm (predeterminado: `latest`)  
`-GitDir <path>` | Directorio de checkout (predeterminado: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Omitir onboarding  
`-NoGitUpdate` | Omitir `git pull`  
`-DryRun` | Imprimir solo las acciones  
Referencia de variables de entorno Variable | Descripción  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Método de instalación  
`OPENCLAW_GIT_DIR=<path>` | Directorio de checkout  
`OPENCLAW_NO_ONBOARD=1` | Omitir onboarding  
`OPENCLAW_GIT_UPDATE=0` | Desactivar git pull  
`OPENCLAW_DRY_RUN=1` | Modo de ejecución de prueba  
  
* * *

## CI y automatización

Usa flags/variables de entorno no interactivos para ejecuciones predecibles.

### install.sh (npm no interactivo)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (git no interactivo)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (omitir onboarding)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Solución de problemas

¿Por qué se requiere Git?

Git es necesario para el método de instalación `git`. Para instalaciones con `npm`, Git también se comprueba/instala para evitar fallos `spawn git ENOENT` cuando las dependencias usan URL de git.

¿Por qué npm da EACCES en Linux?

Algunas configuraciones de Linux apuntan el prefijo global de npm a rutas propiedad de root. `install.sh` puede cambiar el prefijo a `~/.npm-global` y anexar exportaciones de PATH a los archivos rc de la shell (cuando esos archivos existen).

Problemas de sharp/libvips

Los scripts establecen de forma predeterminada `SHARP_IGNORE_GLOBAL_LIBVIPS=1` para evitar que sharp se compile contra libvips del sistema. Para sobrescribirlo:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Instala Git for Windows, vuelve a abrir PowerShell y ejecuta de nuevo el instalador.

Windows: "openclaw is not recognized"

Ejecuta `npm config get prefix` y agrega ese directorio a tu PATH de usuario (no se necesita el sufijo `\bin` en Windows), luego vuelve a abrir PowerShell.

Windows: cómo obtener salida detallada del instalador

`install.ps1` no expone actualmente un interruptor `-Verbose`. Usa el rastreo de PowerShell para diagnósticos a nivel de script:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw no se encuentra después de la instalación

Normalmente es un problema de PATH. Consulta [solución de problemas de Node.js](</es/install/node#troubleshooting>).

## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Actualización](</es/install/updating>)
  * [Desinstalación](</es/install/uninstall>)


Was this useful?YesNo