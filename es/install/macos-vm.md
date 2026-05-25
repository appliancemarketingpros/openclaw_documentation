---
title: Máquinas virtuales de macOS
source_url: https://docs.openclaw.ai/es/install/macos-vm
scraped_at: 2026-05-25
---

## Valor predeterminado recomendado (la mayoría de los usuarios)

  * **VPS Linux pequeño** para un Gateway siempre activo y de bajo costo. Consulta [Alojamiento VPS](</es/vps>).
  * **Hardware dedicado** (Mac mini o equipo Linux) si quieres control total y una **IP residencial** para automatización del navegador. Muchos sitios bloquean las IP de centros de datos, por lo que la navegación local suele funcionar mejor.
  * **Híbrido:** mantén el Gateway en un VPS económico y conecta tu Mac como **Node** cuando necesites automatización de navegador/UI. Consulta [Nodes](</es/nodes>) y [Gateway remoto](</es/gateway/remote>).


Usa una VM de macOS cuando necesites específicamente capacidades exclusivas de macOS, como iMessage, o quieras un aislamiento estricto de tu Mac diario.

## Opciones de VM de macOS

### VM local en tu Mac con Apple Silicon (Lume)

Ejecuta OpenClaw en una VM de macOS aislada en tu Mac con Apple Silicon existente usando [Lume](<https://cua.ai/docs/lume>).

Esto te da:

  * Entorno macOS completo en aislamiento (tu host se mantiene limpio)
  * Compatibilidad con iMessage mediante `imsg` (la ruta local predeterminada es imposible en Linux/Windows)
  * Restablecimiento instantáneo clonando VM
  * Sin hardware adicional ni costos de nube


### Proveedores de Mac alojados (nube)

Si quieres macOS en la nube, los proveedores de Mac alojados también funcionan:

  * [MacStadium](<https://www.macstadium.com/>) (Mac alojados)
  * Otros proveedores de Mac alojados también funcionan; sigue su documentación de VM + SSH


Una vez que tengas acceso SSH a una VM de macOS, continúa en el paso 6 a continuación.

* * *

## Ruta rápida (Lume, usuarios experimentados)

  1. Instala Lume
  2. `lume create openclaw --os macos --ipsw latest`
  3. Completa el Asistente de configuración, habilita Inicio de sesión remoto (SSH)
  4. `lume run openclaw --no-display`
  5. Entra por SSH, instala OpenClaw, configura canales
  6. Listo


* * *

## Lo que necesitas (Lume)

  * Mac con Apple Silicon (M1/M2/M3/M4)
  * macOS Sequoia o posterior en el host
  * ~60 GB de espacio libre en disco por VM
  * ~20 minutos


* * *

## 1) Instalar Lume

bashCopy code
[code]
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
[/code]

Si `~/.local/bin` no está en tu PATH:

bashCopy code
[code]
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc && source ~/.zshrc
[/code]

Verifica:

bashCopy code
[code]
    lume --version
[/code]

Documentación: [Instalación de Lume](<https://cua.ai/docs/lume/guide/getting-started/installation>)

* * *

## 2) Crear la VM de macOS

bashCopy code
[code]
    lume create openclaw --os macos --ipsw latest
[/code]

Esto descarga macOS y crea la VM. Se abre automáticamente una ventana VNC.

* * *

## 3) Completar el Asistente de configuración

En la ventana VNC:

  1. Selecciona idioma y región
  2. Omite el Apple ID (o inicia sesión si quieres iMessage más adelante)
  3. Crea una cuenta de usuario (recuerda el nombre de usuario y la contraseña)
  4. Omite todas las funciones opcionales


Cuando termine la configuración, habilita SSH:

  1. Abre Configuración del Sistema → General → Compartir
  2. Habilita "Inicio de sesión remoto"


* * *

## 4) Obtener la dirección IP de la VM

bashCopy code
[code]
    lume get openclaw
[/code]

Busca la dirección IP (normalmente `192.168.64.x`).

* * *

## 5) Entrar por SSH a la VM

bashCopy code
[code]
    ssh youruser@192.168.64.X
[/code]

Reemplaza `youruser` por la cuenta que creaste y la IP por la IP de tu VM.

* * *

## 6) Instalar OpenClaw

Dentro de la VM:

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Sigue las indicaciones de incorporación para configurar tu proveedor de modelos (Anthropic, OpenAI, etc.).

* * *

## 7) Configurar canales

Edita el archivo de configuración:

bashCopy code
[code]
    nano ~/.openclaw/openclaw.json
[/code]

Añade tus canales:

json5Copy code
[code]
    {  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551234567"],    },    telegram: {      botToken: "YOUR_BOT_TOKEN",    },  },}
[/code]

Luego inicia sesión en WhatsApp (escanea el QR):

bashCopy code
[code]
    openclaw channels login
[/code]

* * *

## 8) Ejecutar la VM sin interfaz gráfica

Detén la VM y reiníciala sin pantalla:

bashCopy code
[code]
    lume stop openclawlume run openclaw --no-display
[/code]

La VM se ejecuta en segundo plano. El daemon de OpenClaw mantiene el Gateway en ejecución.

Para comprobar el estado:

bashCopy code
[code]
    ssh youruser@192.168.64.X "openclaw status"
[/code]

* * *

## Extra: integración con iMessage

Esta es la función estrella de ejecutar en macOS. Usa [iMessage](</es/channels/imessage>) con `imsg` para añadir Mensajes a OpenClaw.

Dentro de la VM:

  1. Inicia sesión en Mensajes.
  2. Instala `imsg`.
  3. Concede Acceso total al disco y permiso de Automatización al proceso que ejecuta OpenClaw/`imsg`.
  4. Verifica la compatibilidad con RPC con `imsg rpc --help`.


Añade esto a tu configuración de OpenClaw:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "imsg",      dbPath: "~/Library/Messages/chat.db",    },  },}
[/code]

Reinicia el Gateway. Ahora tu agente puede enviar y recibir iMessages.

Detalles completos de configuración: [Canal iMessage](</es/channels/imessage>)

* * *

## Guardar una imagen dorada

Antes de personalizar más, crea una instantánea de tu estado limpio:

bashCopy code
[code]
    lume stop openclawlume clone openclaw openclaw-golden
[/code]

Restablece en cualquier momento:

bashCopy code
[code]
    lume stop openclaw && lume delete openclawlume clone openclaw-golden openclawlume run openclaw --no-display
[/code]

* * *

## Ejecución 24/7

Mantén la VM en ejecución:

  * Manteniendo tu Mac enchufado
  * Deshabilitando el reposo en Configuración del Sistema → Economizador
  * Usando `caffeinate` si es necesario


Para un funcionamiento realmente siempre activo, considera un Mac mini dedicado o un VPS pequeño. Consulta [Alojamiento VPS](</es/vps>).

* * *

## Solución de problemas

Problema | Solución  
---|---  
No puedes entrar por SSH a la VM | Comprueba que "Inicio de sesión remoto" esté habilitado en Configuración del Sistema de la VM  
No aparece la IP de la VM | Espera a que la VM arranque por completo y ejecuta `lume get openclaw` de nuevo  
No se encuentra el comando Lume | Añade `~/.local/bin` a tu PATH  
El QR de WhatsApp no se escanea | Asegúrate de haber iniciado sesión en la VM (no en el host) al ejecutar `openclaw channels login`  
  
* * *

## Documentación relacionada

  * [Alojamiento VPS](</es/vps>)
  * [Nodes](</es/nodes>)
  * [Gateway remoto](</es/gateway/remote>)
  * [Canal iMessage](</es/channels/imessage>)
  * [Inicio rápido de Lume](<https://cua.ai/docs/lume/guide/getting-started/quickstart>)
  * [Referencia de la CLI de Lume](<https://cua.ai/docs/lume/reference/cli-reference>)
  * [Configuración de VM desatendida](<https://cua.ai/docs/lume/guide/fundamentals/unattended-setup>) (avanzado)
  * [Aislamiento con Docker](</es/install/docker>) (enfoque de aislamiento alternativo)


Was this useful?YesNo