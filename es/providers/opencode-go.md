---
title: OpenCode Go
source_url: https://docs.openclaw.ai/es/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go es el catálogo Go dentro de [OpenCode](</es/providers/opencode>). Usa la misma `OPENCODE_API_KEY` que el catálogo Zen, pero mantiene el identificador de proveedor en ejecución `opencode-go` para que el enrutamiento por modelo aguas arriba siga siendo correcto.

Propiedad | Valor  
---|---  
Proveedor en ejecución | `opencode-go`  
Autenticación | `OPENCODE_API_KEY`  
Configuración principal | [OpenCode](</es/providers/opencode>)  
  
## Catálogo integrado

OpenClaw obtiene la mayoría de las filas del catálogo Go del registro integrado de modelos pi y complementa las filas actuales aguas arriba mientras el registro se pone al día. Ejecuta `openclaw models list --provider opencode-go` para ver la lista actual de modelos.

El proveedor incluye:

Referencia de modelo | Nombre  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (límites 3x)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Primeros pasos

### Interactivo

* ### Ejecutar la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### Establecer un modelo Go como predeterminado

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verificar que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### No interactivo

* ### Pasar la clave directamente

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Verificar que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Ejemplo de configuración

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Configuración avanzada

Comportamiento de enrutamiento

OpenClaw gestiona el enrutamiento por modelo automáticamente cuando la referencia del modelo usa `opencode-go/...`. No se requiere configuración adicional del proveedor.

Convención de referencias en ejecución

Las referencias en ejecución se mantienen explícitas: `opencode/...` para Zen, `opencode-go/...` para Go. Esto mantiene correcto el enrutamiento por modelo aguas arriba en ambos catálogos.

Credenciales compartidas

La misma `OPENCODE_API_KEY` la usan tanto el catálogo Zen como el catálogo Go. Introducir la clave durante la configuración almacena credenciales para ambos proveedores en ejecución.

## Relacionado

[**OpenCode (principal)** Incorporación compartida, visión general del catálogo y notas avanzadas. ](</es/providers/opencode>) [**Selección de modelos** Elección de proveedores, referencias de modelos y comportamiento de respaldo. ](</es/concepts/model-providers>)

Was this useful?YesNo