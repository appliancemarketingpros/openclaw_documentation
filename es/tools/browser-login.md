---
title: Inicio de sesión en el navegador
source_url: https://docs.openclaw.ai/es/tools/browser-login
scraped_at: 2026-05-25
---

## Inicio de sesión manual (recomendado)

Cuando un sitio requiere inicio de sesión, **inicia sesión manualmente** en el perfil del navegador del **host** (el navegador de openclaw).

**No** le des al modelo tus credenciales. Los inicios de sesión automatizados suelen activar defensas antibot y pueden bloquear la cuenta.

Volver a la documentación principal del navegador: [Navegador](</es/tools/browser>).

## ¿Qué perfil de Chrome se usa?

OpenClaw controla un **perfil de Chrome dedicado** (llamado `openclaw`, con interfaz de usuario en tono naranja). Es independiente de tu perfil de navegador diario.

Para las llamadas de herramienta del navegador del agente:

  * Opción predeterminada: el agente debe usar su navegador `openclaw` aislado.
  * Usa `profile="user"` solo cuando las sesiones con inicio de sesión existentes importen y el usuario esté frente a la computadora para hacer clic o aprobar cualquier solicitud de conexión.
  * Si tienes varios perfiles de navegador de usuario, especifica el perfil explícitamente en lugar de adivinar.


Dos formas sencillas de acceder:

  1. **Pide al agente que abra el navegador** y luego inicia sesión tú.
  2. **Ábrelo mediante la CLI** :

bashCopy code
[code]
    openclaw browser startopenclaw browser open https://x.com
[/code]

Si tienes varios perfiles, pasa `--browser-profile <name>` (el valor predeterminado es `openclaw`).

## X/Twitter: flujo recomendado

  * **Leer/buscar/hilos:** usa el navegador del **host** (inicio de sesión manual).
  * **Publicar actualizaciones:** usa el navegador del **host** (inicio de sesión manual).


## Aislamiento + acceso al navegador del host

Las sesiones de navegador aisladas tienen **más probabilidades** de activar la detección de bots. Para X/Twitter (y otros sitios estrictos), prefiere el navegador del **host**.

Si el agente está aislado, la herramienta de navegador usa el aislamiento de forma predeterminada. Para permitir el control del host:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        browser: {          allowHostControl: true,        },      },    },  },}
[/code]

Luego abre tú el navegador del host (las invocaciones de la CLI siempre se ejecutan contra el navegador del host):

bashCopy code
[code]
    openclaw browser open https://x.com --browser-profile openclaw
[/code]

Las llamadas de la herramienta `browser` del agente pueden entonces dirigirse al host una vez que `sandbox.browser.allowHostControl: true` esté configurado. Como alternativa, desactiva el aislamiento para el agente que publica actualizaciones.

## Relacionado

  * [Navegador](</es/tools/browser>)
  * [Solución de problemas del navegador en Linux](</es/tools/browser-linux-troubleshooting>)
  * [Solución de problemas del navegador en WSL2](</es/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo