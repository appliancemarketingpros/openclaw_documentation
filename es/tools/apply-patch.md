---
title: herramienta apply_patch
source_url: https://docs.openclaw.ai/es/tools/apply-patch
scraped_at: 2026-05-25
---

Aplica cambios en archivos usando un formato de parche estructurado. Esto es ideal para ediciones de varios archivos o varios bloques donde una sola llamada a `edit` sería frágil.

La herramienta acepta una única cadena `input` que envuelve una o más operaciones de archivo:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Parámetros

  * `input` (obligatorio): Contenido completo del parche, incluidos `*** Begin Patch` y `*** End Patch`.


## Notas

  * Las rutas de parche admiten rutas relativas (desde el directorio del espacio de trabajo) y rutas absolutas.
  * `tools.exec.applyPatch.workspaceOnly` tiene el valor predeterminado `true` (contenido dentro del espacio de trabajo). Establécelo en `false` solo si quieres intencionalmente que `apply_patch` escriba o elimine fuera del directorio del espacio de trabajo.
  * Usa `*** Move to:` dentro de un bloque `*** Update File:` para cambiar el nombre de archivos.
  * `*** End of File` marca una inserción solo de EOF cuando sea necesario.
  * Disponible de forma predeterminada para los modelos OpenAI y OpenAI Codex. Establece `tools.exec.applyPatch.enabled: false` para deshabilitarlo.
  * Opcionalmente, limita por modelo mediante `tools.exec.applyPatch.allowModels`.
  * La configuración solo está bajo `tools.exec`.


## Ejemplo

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Relacionado

[**Diffs** Visor de diffs de solo lectura para presentar cambios. ](</es/tools/diffs>) [**Exec tool** Ejecución de comandos de shell desde el agente. ](</es/tools/exec>) [**Code execution** Análisis remoto de Python en sandbox con xAI. ](</es/tools/code-execution>)

Was this useful?YesNo