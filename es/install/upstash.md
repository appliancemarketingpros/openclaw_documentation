---
title: Caja de Upstash
source_url: https://docs.openclaw.ai/es/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Ejecuta un Gateway de OpenClaw persistente en Upstash Box, un entorno Linux administrado con soporte de ciclo de vida keep-alive.

Usa un túnel SSH para acceder al panel. No expongas el puerto del Gateway directamente a Internet público.

## Requisitos previos

  * Cuenta de Upstash
  * Upstash Box con keep-alive
  * Cliente SSH en tu máquina local


## Crear una Box

Crea una Box con keep-alive en Upstash Console. Anota el ID de la Box, como `right-flamingo-14486`, y la clave API de tu Box.

Upstash mantiene su guía actual de OpenClaw Box en [Configuración de OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Conectarse con un túnel SSH

Reenvía el puerto del panel de OpenClaw a tu máquina local. Usa la clave API de tu Box como contraseña SSH cuando se te solicite:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Las opciones keepalive reducen las caídas del túnel por inactividad durante la incorporación.

## Instalar OpenClaw

Dentro de la Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Ejecutar la incorporación

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Sigue las indicaciones. Copia la URL y el token del panel cuando finalice la incorporación.

## Iniciar el Gateway

Configura el Gateway para la red de la Box e inícialo en segundo plano:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

Con el túnel SSH activo, abre la URL del panel localmente:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Reinicio automático

Configura este comando como script de inicialización de la Box para que el Gateway se reinicie cuando la Box se inicie:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Solución de problemas

Si SSH se congela durante la incorporación, vuelve a conectarte con una configuración SSH limpia y keepalives:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Esto omite la configuración local obsoleta de `~/.ssh/config` y mantiene el túnel activo durante períodos de inactividad de la red.

## Relacionado

  * [Acceso remoto](</es/gateway/remote>)
  * [Seguridad del Gateway](</es/gateway/security>)
  * [Actualizar OpenClaw](</es/install/updating>)


Was this useful?YesNo

Open issue