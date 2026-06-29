---
title: Plugin Codex Supervisor
source_url: https://docs.openclaw.ai/es/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin Codex Supervisor

Supervisa las sesiones del servidor de aplicaciones de Codex desde OpenClaw.

## Distribución

  * Paquete: `@openclaw/codex-supervisor`
  * Ruta de instalación: incluido en OpenClaw


## Superficie

contratos: herramientas

## Listado de sesiones

`codex_sessions_list` se limita de forma predeterminada a las sesiones de Codex cargadas. Define `include_stored` para incluir el historial almacenado; el plugin usa la ruta de listado exclusiva de la base de datos de estado del servidor de aplicaciones de Codex y limita los resultados almacenados a 200 de forma predeterminada. Pasa `max_stored_sessions` para reducir o aumentar ese límite, hasta 1000.

Was this useful?YesNo

Open issue