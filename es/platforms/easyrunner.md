---
title: EasyRunner
source_url: https://docs.openclaw.ai/es/platforms/easyrunner
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

EasyRunner puede alojar el Gateway de OpenClaw como una pequeña aplicación en contenedor detrás de su proxy Caddy. Esta guía presupone un host EasyRunner que ejecuta aplicaciones Compose compatibles con Podman y expone HTTPS mediante Caddy.

## Antes de empezar

  * Un servidor EasyRunner con un dominio dirigido a él.
  * Una imagen de contenedor de OpenClaw compilada o publicada.
  * Un volumen de configuración persistente para `/home/node/.openclaw`.
  * Un volumen de espacio de trabajo persistente para `/workspace`.
  * Un token o contraseña de Gateway seguro.


Mantén la autenticación de dispositivos activada cuando sea posible. Si tu despliegue de proxy inverso no puede transportar correctamente la identidad del dispositivo, corrige primero la configuración de proxy de confianza; usa omisiones de autenticación peligrosas solo en una red completamente privada y controlada por el operador.

## Aplicación Compose

Crea una aplicación EasyRunner con un archivo Compose con esta forma:

yamlCopy code
[code]
    services:  openclaw:    image: ghcr.io/openclaw/openclaw:latest    restart: unless-stopped    environment:      OPENCLAW_GATEWAY_TOKEN: ${OPENCLAW_GATEWAY_TOKEN}      OPENCLAW_HOME: /home/node      OPENCLAW_STATE_DIR: /home/node/.openclaw      OPENCLAW_CONFIG_PATH: /home/node/.openclaw/openclaw.json      OPENCLAW_WORKSPACE_DIR: /workspace    volumes:      - openclaw-config:/home/node/.openclaw      - openclaw-workspace:/workspace    labels:      caddy: openclaw.example.com      caddy.reverse_proxy: "{{upstreams 1455}}"    command: ["openclaw", "gateway", "--bind", "lan", "--port", "1455"] volumes:  openclaw-config:  openclaw-workspace:
[/code]

Sustituye `openclaw.example.com` por el nombre de host de tu Gateway. Almacena `OPENCLAW_GATEWAY_TOKEN` en el gestor de secretos/entorno de EasyRunner en lugar de confirmarlo en la definición de la aplicación.

## Configurar OpenClaw

Dentro del volumen de configuración persistente, mantén el Gateway accesible solo a través del proxy y exige autenticación:

json5Copy code
[code]
    {  gateway: {    bind: "lan",    port: 1455,    auth: {      token: "${OPENCLAW_GATEWAY_TOKEN}",    },  },}
[/code]

Si Caddy termina TLS para el Gateway, configura los ajustes de proxy de confianza para la ruta exacta del proxy en lugar de desactivar las comprobaciones de autenticación globalmente. Consulta [Autenticación de proxy de confianza](</es/gateway/trusted-proxy-auth>).

## Verificar

Desde tu estación de trabajo:

bashCopy code
[code]
    openclaw gateway probe --url https://openclaw.example.com --token <token>openclaw gateway status --url https://openclaw.example.com --token <token>
[/code]

Desde el host EasyRunner, revisa los registros de la aplicación para confirmar que haya un Gateway en escucha y que no haya fallos de inicio de SecretRef, Plugin ni autenticación de canales.

## Actualizaciones y copias de seguridad

  * Descarga o compila la nueva imagen de OpenClaw y, a continuación, vuelve a desplegar la aplicación EasyRunner.
  * Haz una copia de seguridad del volumen `openclaw-config` antes de actualizar.
  * Haz una copia de seguridad de `openclaw-workspace` si los agentes escriben allí datos de proyecto duraderos.
  * Ejecuta `openclaw doctor` después de actualizaciones importantes para detectar migraciones de configuración y advertencias de servicio.


## Solución de problemas

  * `gateway probe` no puede conectarse: confirma que el nombre de host de Caddy apunte a la aplicación y que el contenedor escuche en `0.0.0.0:1455`.
  * La autenticación falla: rota el token en los secretos de EasyRunner y en el comando del cliente local a la vez.
  * Los archivos pertenecen a root después de una restauración: repara los volúmenes montados para que el usuario del contenedor pueda escribir en `/home/node/.openclaw` y `/workspace`.
  * Fallan los Plugins de navegador o de canales: comprueba si los binarios externos requeridos, la salida de red y las credenciales montadas están disponibles dentro del contenedor.


Was this useful?YesNo

Open issue