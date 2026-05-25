---
title: Configuración
source_url: https://docs.openclaw.ai/es/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Inicializa la configuración base y el espacio de trabajo del agente. Si hay alguna opción de incorporación presente, también ejecuta el asistente.

## Opciones

Opción | Descripción  
---|---  
`--workspace <dir>` | Directorio del espacio de trabajo del agente (predeterminado `~/.openclaw/workspace`; se almacena como `agents.defaults.workspace`).  
`--wizard` | Ejecuta la incorporación interactiva.  
`--non-interactive` | Ejecuta la incorporación sin solicitudes.  
`--mode <mode>` | Modo de incorporación: `local` o `remote`.  
`--import-from <provider>` | Proveedor de migración que se ejecutará durante la incorporación.  
`--import-source <path>` | Directorio principal del agente de origen para `--import-from`.  
`--import-secrets` | Importa secretos compatibles durante la migración de incorporación.  
`--remote-url <url>` | URL WebSocket del Gateway remoto.  
`--remote-token <token>` | Token del Gateway remoto (opcional).  
  
### Activación automática del asistente

`openclaw setup` ejecuta el asistente cuando cualquiera de estas opciones está presente explícitamente, incluso sin `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Ejemplos

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Notas

  * `openclaw setup` simple inicializa la configuración y el espacio de trabajo sin ejecutar el flujo de incorporación completo.
  * Después del setup simple, ejecuta `openclaw onboard` para el recorrido guiado completo, `openclaw configure` para cambios específicos o `openclaw channels add` para agregar cuentas de canal.
  * Si se detecta el estado de Hermes, la incorporación interactiva puede ofrecer la migración automáticamente. La importación durante la incorporación requiere un setup nuevo; usa [Migrar](</es/cli/migrate>) para planes de prueba, copias de seguridad y modo de sobrescritura fuera de la incorporación.


## Relacionado

  * [Referencia de la CLI](</es/cli>)
  * [Incorporación (CLI)](</es/start/wizard>)
  * [Primeros pasos](</es/start/getting-started>)
  * [Resumen de instalación](</es/install>)


Was this useful?YesNo