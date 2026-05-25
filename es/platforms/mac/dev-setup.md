---
title: Configuración de desarrollo en macOS
source_url: https://docs.openclaw.ai/es/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# Configuración de desarrollo para macOS

Compila y ejecuta la aplicación de OpenClaw para macOS desde el código fuente.

## Requisitos previos

Antes de compilar la aplicación, asegúrate de tener instalado lo siguiente:

  1. **Xcode 26.2+** : Necesario para el desarrollo en Swift.
  2. **Node.js 24 y pnpm** : Recomendado para el Gateway, la CLI y los scripts de empaquetado. Node 22 LTS, actualmente `22.16+`, sigue siendo compatible por motivos de compatibilidad.


## 1\. Instalar dependencias

Instala las dependencias de todo el proyecto:

bashCopy code
[code]
    pnpm install
[/code]

## 2\. Compilar y empaquetar la aplicación

Para compilar la aplicación de macOS y empaquetarla en `dist/OpenClaw.app`, ejecuta:

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

Si no tienes un certificado de Apple Developer ID, el script usará automáticamente **firma ad-hoc** (`-`).

Para modos de ejecución de desarrollo, opciones de firma y solución de problemas con el Team ID, consulta el README de la aplicación de macOS: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **Nota** : Las aplicaciones firmadas ad-hoc pueden activar avisos de seguridad. Si la aplicación se cierra inmediatamente con "Abort trap 6", consulta la sección Solución de problemas.

## 3\. Instalar la CLI

La aplicación de macOS espera una instalación global de la CLI `openclaw` para gestionar tareas en segundo plano.

**Para instalarla (recomendado):**

  1. Abre la aplicación OpenClaw.
  2. Ve a la pestaña de configuración **General**.
  3. Haz clic en **"Instalar CLI"**.


También puedes instalarla manualmente:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

`pnpm add -g openclaw@<version>` y `bun add -g openclaw@<version>` también funcionan. Para el entorno de ejecución del Gateway, Node sigue siendo la ruta recomendada.

## Solución de problemas

### Error de compilación: incompatibilidad de cadena de herramientas o SDK

La compilación de la aplicación de macOS espera el SDK de macOS más reciente y la cadena de herramientas de Swift 6.2.

**Dependencias del sistema (obligatorias):**

  * **Última versión de macOS disponible en Actualización de software** (requerida por los SDK de Xcode 26.2)
  * **Xcode 26.2** (cadena de herramientas de Swift 6.2)


**Comprobaciones:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

Si las versiones no coinciden, actualiza macOS/Xcode y vuelve a ejecutar la compilación.

### La aplicación se bloquea al conceder permisos

Si la aplicación se bloquea cuando intentas permitir el acceso a **Reconocimiento de voz** o **Micrófono** , puede deberse a una caché TCC dañada o a una incompatibilidad de firma.

**Corrección:**

  1. Restablece los permisos TCC:

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. Si eso falla, cambia temporalmente el `BUNDLE_ID` en [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) para forzar un "inicio limpio" desde macOS.


### Gateway "Iniciando..." indefinidamente

Si el estado del Gateway se queda en "Iniciando...", comprueba si un proceso zombi está ocupando el puerto:

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # If you're not using a LaunchAgent (dev mode / manual runs), find the listener:lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

Si una ejecución manual está ocupando el puerto, detén ese proceso (Ctrl+C). Como último recurso, termina el PID que encontraste arriba.

## Relacionado

  * [Aplicación de macOS](</es/platforms/macos>)
  * [Resumen de instalación](</es/install>)


Was this useful?YesNo