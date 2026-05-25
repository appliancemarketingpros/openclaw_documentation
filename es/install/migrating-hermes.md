---
title: Migración desde Hermes
source_url: https://docs.openclaw.ai/es/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw importa el estado de Hermes mediante un proveedor de migración incluido. El proveedor previsualiza todo antes de cambiar el estado, redacta los secretos en los planes y los informes, y crea una copia de seguridad verificada antes de aplicar los cambios.

## Dos formas de importar

### Asistente de incorporación

La ruta más rápida. El asistente detecta Hermes en `~/.hermes` y muestra una vista previa antes de aplicar los cambios.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

O apunta a una fuente específica:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Usa `openclaw migrate` para ejecuciones con scripts o repetibles. Consulta [`openclaw migrate`](</es/cli/migrate>) para ver la referencia completa.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

Añade `--from <path>` cuando Hermes esté fuera de `~/.hermes`.

## Qué se importa

Configuración del modelo

  * Selección de modelo predeterminada desde `config.yaml` de Hermes.
  * Proveedores de modelos configurados y endpoints personalizados compatibles con OpenAI desde `providers` y `custom_providers`.

Servidores MCP

Definiciones de servidores MCP desde `mcp_servers` o `mcp.servers`.

Archivos del espacio de trabajo

  * `SOUL.md` y `AGENTS.md` se copian en el espacio de trabajo del agente de OpenClaw.
  * `memories/MEMORY.md` y `memories/USER.md` se **añaden** a los archivos de memoria correspondientes de OpenClaw en lugar de sobrescribirlos.

Configuración de memoria

Valores predeterminados de configuración de memoria para la memoria basada en archivos de OpenClaw. Los proveedores de memoria externos, como Honcho, se registran como elementos de archivo o de revisión manual para que puedas moverlos deliberadamente.

Skills

Las Skills con un archivo `SKILL.md` bajo `skills/<name>/` se copian junto con los valores de configuración por Skill desde `skills.config`.

Claves de API (opcional)

Establece `--include-secrets` para importar las claves `.env` admitidas: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Sin la marca, los secretos nunca se copian.

## Qué queda solo como archivo

El proveedor copia estos elementos en el directorio del informe de migración para revisión manual, pero **no** los carga en la configuración ni en las credenciales activas de OpenClaw:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw se niega a ejecutar o confiar automáticamente en este estado porque los formatos y los supuestos de confianza pueden divergir entre sistemas. Mueve manualmente lo que necesites después de revisar el archivo.

## Flujo recomendado

* ### Previsualiza el plan

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

El plan enumera todo lo que cambiará, incluidos conflictos, elementos omitidos y cualquier elemento sensible. La salida del plan redacta las claves anidadas que parezcan secretas.

* ### Aplica con copia de seguridad

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw crea y verifica una copia de seguridad antes de aplicar los cambios. Si necesitas importar claves de API, añade `--include-secrets`.

* ### Ejecuta doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</es/gateway/doctor>) vuelve a aplicar cualquier migración de configuración pendiente y comprueba si se introdujeron problemas durante la importación.

* ### Reinicia y verifica

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Confirma que el Gateway esté en buen estado y que el modelo, la memoria y las Skills importados estén cargados.

## Manejo de conflictos

La aplicación se niega a continuar cuando el plan informa conflictos (un archivo o valor de configuración ya existe en el destino).

En una instalación nueva de OpenClaw, los conflictos son inusuales. Suelen aparecer cuando vuelves a ejecutar la importación en una configuración que ya tiene ediciones del usuario.

Si surge un conflicto a mitad de la aplicación (por ejemplo, una condición de carrera inesperada en un archivo de configuración), Hermes marca los elementos de configuración dependientes restantes como `skipped` con el motivo `blocked by earlier apply conflict` en lugar de escribirlos parcialmente. El informe de migración registra cada elemento bloqueado para que puedas resolver el conflicto original y volver a ejecutar la importación.

## Secretos

Los secretos nunca se importan de forma predeterminada.

  * Ejecuta primero `openclaw migrate apply hermes --yes` para importar el estado no secreto.
  * Si también quieres copiar las claves `.env` admitidas, vuelve a ejecutar con `--include-secrets`.
  * Para credenciales gestionadas por SecretRef, configura la fuente de SecretRef después de que finalice la importación.


## Salida JSON para automatización

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

Con `--json` y sin `--yes`, la aplicación imprime el plan y no muta el estado. Este es el modo más seguro para CI y scripts compartidos.

## Solución de problemas

La aplicación se niega por conflictos

Inspecciona la salida del plan. Cada conflicto identifica la ruta de origen y el destino existente. Decide por elemento si omitirlo, editar el destino o volver a ejecutar con `--overwrite`.

Hermes está fuera de ~/.hermes

Pasa `--from /actual/path` (CLI) o `--import-source /actual/path` (incorporación).

La incorporación se niega a importar en una configuración existente

Las importaciones de incorporación requieren una configuración nueva. Restablece el estado y vuelve a incorporarlo, o usa `openclaw migrate apply hermes` directamente, que admite `--overwrite` y control explícito de copias de seguridad.

Las claves de API no se importaron

`--include-secrets` es obligatorio, y solo se reconocen las claves enumeradas arriba. Otras variables en `.env` se ignoran.

## Relacionado

  * [`openclaw migrate`](</es/cli/migrate>): referencia completa de CLI, contrato de Plugin y formas JSON.
  * [Incorporación](</es/cli/onboard>): flujo del asistente y marcas no interactivas.
  * [Migración](</es/install/migrating>): mover una instalación de OpenClaw entre máquinas.
  * [Doctor](</es/gateway/doctor>): comprobación de estado posterior a la migración.
  * [Espacio de trabajo del agente](</es/concepts/agent-workspace>): dónde residen `SOUL.md`, `AGENTS.md` y los archivos de memoria.


Was this useful?YesNo