---
title: Desinstalar
source_url: https://docs.openclaw.ai/es/install/uninstall
scraped_at: 2026-05-25
---

Hay dos rutas:

  * **Ruta fácil** si `openclaw` sigue instalado.
  * **Eliminación manual del servicio** si la CLI ya no está, pero el servicio sigue ejecutándose.


## Ruta fácil (la CLI sigue instalada)

Recomendado: usa el desinstalador integrado:

bashCopy code
[code]
    openclaw uninstall
[/code]

Modo no interactivo (automatización / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Pasos manuales (mismo resultado):

  1. Detén el servicio Gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Desinstala el servicio Gateway (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Elimina estado + configuración:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Si estableciste `OPENCLAW_CONFIG_PATH` en una ubicación personalizada fuera del directorio de estado, elimina también ese archivo.

  4. Elimina tu espacio de trabajo (opcional, quita archivos del agente):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Elimina la instalación de la CLI (elige la que usaste):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Si instalaste la app de macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Notas:

  * Si usaste perfiles (`--profile` / `OPENCLAW_PROFILE`), repite el paso 3 para cada directorio de estado (los valores predeterminados son `~/.openclaw-<profile>`).
  * En modo remoto, el directorio de estado vive en el **host Gateway** , así que ejecuta también allí los pasos 1-4.


## Eliminación manual del servicio (la CLI no está instalada)

Usa esto si el servicio Gateway sigue ejecutándose pero falta `openclaw`.

### macOS (launchd)

La etiqueta predeterminada es `ai.openclaw.gateway` (o `ai.openclaw.<profile>`; la heredada `com.openclaw.*` aún puede existir):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Si usaste un perfil, reemplaza la etiqueta y el nombre del plist por `ai.openclaw.<profile>`. Elimina cualquier plist heredado `com.openclaw.*` si existe.

### Linux (unidad de usuario systemd)

El nombre de unidad predeterminado es `openclaw-gateway.service` (o `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (tarea programada)

El nombre de tarea predeterminado es `OpenClaw Gateway` (o `OpenClaw Gateway (<profile>)`). El script de la tarea vive bajo tu directorio de estado.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Si usaste un perfil, elimina el nombre de tarea correspondiente y `~\.openclaw-<profile>\gateway.cmd`.

## Instalación normal vs checkout del código fuente

### Instalación normal ([install.sh](<http://install.sh>) / npm / pnpm / bun)

Si usaste `https://openclaw.ai/install.sh` o `install.ps1`, la CLI se instaló con `npm install -g openclaw@latest`. Elimínala con `npm rm -g openclaw` (o `pnpm remove -g` / `bun remove -g` si la instalaste de esa forma).

### Checkout del código fuente (git clone)

Si ejecutas desde un checkout del repositorio (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Desinstala el servicio Gateway **antes** de eliminar el repositorio (usa la ruta fácil anterior o la eliminación manual del servicio).
  2. Elimina el directorio del repositorio.
  3. Elimina estado + espacio de trabajo como se muestra arriba.


## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Guía de migración](</es/install/migrating>)


Was this useful?YesNo