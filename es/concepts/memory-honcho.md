---
title: Memoria Honcho
source_url: https://docs.openclaw.ai/es/concepts/memory-honcho
scraped_at: 2026-05-25
---

[Honcho](<https://honcho.dev>) agrega memoria nativa de IA a OpenClaw. Conserva las conversaciones en un servicio dedicado y construye modelos de usuario y agente con el tiempo, dando a tu agente contexto entre sesiones que va más allá de los archivos Markdown del espacio de trabajo.

## Qué proporciona

  * **Memoria entre sesiones** \-- las conversaciones se conservan después de cada turno, por lo que el contexto se mantiene entre restablecimientos de sesión, Compaction y cambios de canal.
  * **Modelado de usuario** \-- Honcho mantiene un perfil para cada usuario (preferencias, hechos, estilo de comunicación) y para el agente (personalidad, comportamientos aprendidos).
  * **Búsqueda semántica** \-- búsqueda sobre observaciones de conversaciones pasadas, no solo sobre la sesión actual.
  * **Conciencia de múltiples agentes** \-- los agentes padre rastrean automáticamente los subagentes generados, y los padres se agregan como observadores en las sesiones hijas.


## Herramientas disponibles

Honcho registra herramientas que el agente puede usar durante la conversación:

**Recuperación de datos (rápida, sin llamada al LLM):**

Herramienta | Qué hace  
---|---  
`honcho_context` | Representación completa del usuario entre sesiones  
`honcho_search_conclusions` | Búsqueda semántica sobre conclusiones almacenadas  
`honcho_search_messages` | Buscar mensajes entre sesiones (filtrar por remitente, fecha)  
`honcho_session` | Historial y resumen de la sesión actual  
  
**Preguntas y respuestas (impulsado por LLM):**

Herramienta | Qué hace  
---|---  
`honcho_ask` | Hacer preguntas sobre el usuario. `depth='quick'` para hechos, `'thorough'` para síntesis  
  
## Primeros pasos

Instala el Plugin y ejecuta la configuración:

bashCopy code
[code]
    openclaw plugins install @honcho-ai/openclaw-honchoopenclaw honcho setupopenclaw gateway --force
[/code]

El comando de configuración solicita tus credenciales de API, escribe la configuración y opcionalmente migra archivos de memoria existentes del espacio de trabajo.

## Configuración

Los ajustes viven bajo `plugins.entries["openclaw-honcho"].config`:

json5Copy code
[code]
    {  plugins: {    entries: {      "openclaw-honcho": {        config: {          apiKey: "your-api-key", // omit for self-hosted          workspaceId: "openclaw", // memory isolation          baseUrl: "https://api.honcho.dev",        },      },    },  },}
[/code]

Para instancias autoalojadas, apunta `baseUrl` a tu servidor local (por ejemplo `http://localhost:8000`) y omite la clave API.

## Migrar memoria existente

Si tienes archivos de memoria existentes del espacio de trabajo (`USER.md`, `MEMORY.md`, `IDENTITY.md`, `memory/`, `canvas/`), `openclaw honcho setup` los detecta y ofrece migrarlos.

## Cómo funciona

Después de cada turno de IA, la conversación se conserva en Honcho. Tanto los mensajes del usuario como los del agente se observan, lo que permite a Honcho construir y perfeccionar sus modelos con el tiempo.

Durante la conversación, las herramientas de Honcho consultan el servicio en la fase `before_prompt_build`, inyectando contexto relevante antes de que el modelo vea el prompt. Esto garantiza límites de turno precisos y una recuperación relevante.

## Honcho frente a la memoria integrada

| Integrada / QMD | Honcho  
---|---|---  
**Almacenamiento** | Archivos Markdown del espacio de trabajo | Servicio dedicado (local o alojado)  
**Entre sesiones** | Mediante archivos de memoria | Automático, integrado  
**Modelado de usuario** | Manual (escribir en `MEMORY.md`) | Perfiles automáticos  
**Búsqueda** | Vector + palabra clave (híbrida) | Semántica sobre observaciones  
**Múltiples agentes** | Sin seguimiento | Conciencia padre/hijo  
**Dependencias** | Ninguna (integrada) o binario QMD | Instalación de Plugin  
  
Honcho y el sistema de memoria integrado pueden funcionar juntos. Cuando QMD está configurado, se habilitan herramientas adicionales para buscar en archivos Markdown locales junto con la memoria entre sesiones de Honcho.

## Comandos CLI

bashCopy code
[code]
    openclaw honcho setup                        # Configurar clave API y migrar archivosopenclaw honcho status                       # Comprobar estado de conexiónopenclaw honcho ask <question>               # Consultar a Honcho sobre el usuarioopenclaw honcho search <query> [-k N] [-d D] # Búsqueda semántica sobre la memoria
[/code]

## Más información

  * [Código fuente del Plugin](<https://github.com/plastic-labs/openclaw-honcho>)
  * [Documentación de Honcho](<https://docs.honcho.dev>)
  * [Guía de integración de Honcho con OpenClaw](<https://docs.honcho.dev/v3/guides/integrations/openclaw>)
  * [Memory](</es/concepts/memory>) \-- resumen de memoria de OpenClaw
  * [Context Engines](</es/concepts/context-engine>) \-- cómo funcionan los motores de contexto del Plugin


## Relacionado

  * [Resumen de memoria](</es/concepts/memory>)
  * [Motor de memoria integrado](</es/concepts/memory-builtin>)
  * [Motor de memoria QMD](</es/concepts/memory-qmd>)


Was this useful?YesNo