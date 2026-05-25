---
title: DigitalOcean
source_url: https://docs.openclaw.ai/es/install/digitalocean
scraped_at: 2026-05-25
---

Ejecuta un Gateway de OpenClaw persistente en un Droplet de DigitalOcean (~$6/mes para el plan Basic de 1 GB).

DigitalOcean es la ruta VPS de pago más sencilla. Si prefieres opciones más económicas o gratuitas:

  * [Hetzner](</es/install/hetzner>) — 3,79 €/mes, más núcleos/RAM por dólar.
  * [Oracle Cloud](</es/install/oracle>) — ARM Always Free (hasta 4 OCPU, 24 GB de RAM), pero el registro puede ser delicado y es solo ARM.


## Requisitos previos

  * Cuenta de DigitalOcean ([registro](<https://cloud.digitalocean.com/registrations/new>))
  * Par de claves SSH (o disposición a usar autenticación con contraseña)
  * Unos 20 minutos


## Configuración

* ### Crear un Droplet

  1. Inicia sesión en [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Haz clic en **Create > Droplets**.
  3. Elige: 
     * **Región:** La más cercana a ti
     * **Imagen:** Ubuntu 24.04 LTS
     * **Tamaño:** Basic, Regular, 1 vCPU / 1 GB de RAM / SSD de 25 GB
     * **Autenticación:** Clave SSH (recomendado) o contraseña
  4. Haz clic en **Create Droplet** y anota la dirección IP.


* ### Conectar e instalar

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Usa la shell root solo para el arranque inicial del sistema. Ejecuta los comandos de OpenClaw como el usuario no root `openclaw` para que el estado resida en `/home/openclaw/.openclaw/` y el Gateway se instale como servicio systemd de ese usuario.

* ### Ejecutar la incorporación

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

El asistente te guía por la autenticación del modelo, la configuración del canal, la generación del token del Gateway y la instalación del daemon (systemd).

* ### Agregar swap (recomendado para Droplets de 1 GB)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Verificar el gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Acceder a la interfaz de control

El gateway se enlaza a loopback de forma predeterminada. Elige una de estas opciones.

**Opción A: túnel SSH (la más sencilla)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Luego abre `http://localhost:18789`.

**Opción B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Luego abre `https://<magicdns>/` desde cualquier dispositivo de tu tailnet.

Tailscale Serve autentica el tráfico de la interfaz de control y WebSocket mediante encabezados de identidad de tailnet, lo que presupone que el propio host del gateway es de confianza. Los endpoints de la API HTTP siguen el modo normal de autenticación del gateway (token/contraseña) de todos modos. Para exigir credenciales explícitas de secreto compartido sobre Serve, establece `gateway.auth.allowTailscale: false` y usa `gateway.auth.mode: "token"` o `"password"`.

**Opción C: enlace a tailnet (sin Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Luego abre `http://<tailscale-ip>:18789` (requiere token).

## Persistencia y copias de seguridad

El estado de OpenClaw reside en:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` por agente, estado de canales/proveedores y datos de sesión.
  * `~/.openclaw/workspace/` — el espacio de trabajo del agente ([SOUL.md](<http://SOUL.md>), memoria, artefactos).


Estos sobreviven a los reinicios del Droplet. Para crear una instantánea portable:

bashCopy code
[code]
    openclaw backup create
[/code]

Las instantáneas de DigitalOcean respaldan todo el Droplet; `openclaw backup create` es portable entre hosts.

## Consejos para 1 GB de RAM

El Droplet de $6 solo tiene 1 GB de RAM. Para que todo funcione con fluidez:

  * Asegúrate de que el paso de swap anterior esté en `/etc/fstab` para que sobreviva a los reinicios.
  * Prefiere modelos basados en API (Claude, GPT) frente a modelos locales: la inferencia local de LLM no cabe en 1 GB.
  * Establece `agents.defaults.model.primary` en un modelo más pequeño si encuentras errores OOM con prompts grandes.
  * Monitoriza con `free -h` y `htop`.


## Solución de problemas

**El Gateway no arranca** \-- Ejecuta `openclaw doctor --non-interactive` y revisa los registros con `journalctl --user -u openclaw-gateway.service -n 50`.

**El puerto ya está en uso** \-- Ejecuta `lsof -i :18789` para encontrar el proceso y luego detenlo.

**Sin memoria** \-- Verifica que el swap esté activo con `free -h`. Si sigues encontrando OOM, usa modelos basados en API (Claude, GPT) en lugar de modelos locales, o actualiza a un Droplet de 2 GB.

## Próximos pasos

  * [Canales](</es/channels>) \-- conecta Telegram, WhatsApp, Discord y más
  * [Configuración del Gateway](</es/gateway/configuration>) \-- todas las opciones de configuración
  * [Actualización](</es/install/updating>) \-- mantén OpenClaw actualizado


## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Fly.io](</es/install/fly>)
  * [Hetzner](</es/install/hetzner>)
  * [Alojamiento VPS](</es/vps>)


Was this useful?YesNo