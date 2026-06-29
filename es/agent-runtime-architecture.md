---
title: Arquitectura del entorno de ejecución del agente
source_url: https://docs.openclaw.ai/es/agent-runtime-architecture
scraped_at: 2026-06-29
---

ReferenceTechnical reference

OpenClaw gestiona directamente el runtime de agente integrado. El código del runtime vive en `src/agents/`, los auxiliares de modelos/proveedores viven en `src/llm/` y los contratos orientados a plugins se exponen mediante los barrels `openclaw/plugin-sdk/*`.

## Diseño del runtime

  * `src/agents/embedded-agent-runner/`: bucle de intentos del agente integrado, adaptadores de streams de proveedores, compaction, selección de modelos y cableado de sesiones.
  * `src/agents/sessions/`: persistencia de sesiones, carga de extensiones, descubrimiento de recursos, Skills, prompts, temas y renderizadores de herramientas respaldados por TUI.
  * `packages/agent-core/`: núcleo de agente reutilizable, tipos de arnés de bajo nivel, mensajes, auxiliares de compaction, plantillas de prompts y contratos de herramientas/sesiones.
  * `src/agents/runtime/`: fachada de OpenClaw para `@openclaw/agent-core` y utilidades de proxy local.
  * `src/agents/agent-tools*.ts`: definiciones de herramientas, esquemas, políticas, adaptadores de hooks previos/posteriores y soporte de edición en host gestionados por OpenClaw.
  * `src/agents/agent-hooks/`: hooks de runtime integrados, como protecciones de compaction y poda de contexto.
  * `src/llm/`: registro de modelos/proveedores, auxiliares de transporte e implementaciones de streams específicas de proveedores.


## Límites

El código central llama al runtime integrado mediante módulos de OpenClaw y barrels del SDK, no mediante paquetes de agente externos antiguos. Los plugins usan entrypoints documentados de `openclaw/plugin-sdk/*` y no importan elementos internos de `src/**`.

`@earendil-works/pi-tui` sigue siendo una dependencia TUI de terceros. El TUI local y los renderizadores de sesión lo usan como kit de componentes de terminal; internalizarlo sería un esfuerzo de vendorización aparte.

## Manifiestos

Los paquetes de recursos declaran recursos de OpenClaw en los metadatos del paquete:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["extensions/index.ts"],    "skills": ["skills/*.md"],    "prompts": ["prompts/*.md"],    "themes": ["themes/*.json"]  }}
[/code]

El gestor de paquetes también descubre los directorios convencionales `extensions/`, `skills/`, `prompts/` y `themes/`.

## Selección de runtime

El id predeterminado del runtime integrado es `openclaw`. Los arneses de plugins pueden registrar ids de runtime adicionales. `auto` selecciona un arnés de plugin compatible cuando existe uno y, en caso contrario, usa el runtime integrado de OpenClaw.

## Relacionado

  * [Flujo de trabajo del runtime de agente de OpenClaw](</es/openclaw-agent-runtime>)
  * [Runtimes de agente](</es/concepts/agent-runtimes>)


Was this useful?YesNo

Open issue