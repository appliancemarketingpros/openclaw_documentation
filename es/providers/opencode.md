---
title: OpenCode
source_url: https://docs.openclaw.ai/es/providers/opencode
scraped_at: 2026-05-25
---

OpenCode expone dos catálogos alojados en OpenClaw:

Catalog | Prefix | Runtime provider  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Ambos catálogos usan la misma clave de API de OpenCode. OpenClaw mantiene separados los id de proveedor de tiempo de ejecución para que el enrutamiento ascendente por modelo siga siendo correcto, pero la incorporación y la documentación los tratan como una sola configuración de OpenCode.

## Primeros pasos

### Catálogo Zen

**Ideal para:** el proxy multimodelo curado de OpenCode (Claude, GPT, Gemini).

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

O pasa la clave directamente:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Establece un modelo Zen como predeterminado

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Verifica que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Catálogo Go

**Ideal para:** la gama Kimi, GLM y MiniMax alojada por OpenCode.

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

O pasa la clave directamente:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Establece un modelo Go como predeterminado

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verifica que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Ejemplo de configuración

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Catálogos integrados

### Zen

Property | Value  
---|---  
Runtime provider | `opencode`  
Example models | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Property | Value  
---|---  
Runtime provider | `opencode-go`  
Example models | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Configuración avanzada

Alias de claves de API

`OPENCODE_ZEN_API_KEY` también es compatible como alias de `OPENCODE_API_KEY`.

Credenciales compartidas

Introducir una clave de OpenCode durante la configuración almacena credenciales para ambos proveedores de tiempo de ejecución. No necesitas incorporar cada catálogo por separado.

Facturación y panel

Inicias sesión en OpenCode, agregas los datos de facturación y copias tu clave de API. La facturación y la disponibilidad del catálogo se gestionan desde el panel de OpenCode.

Comportamiento de repetición de Gemini

Las referencias de OpenCode respaldadas por Gemini permanecen en la ruta proxy-Gemini, por lo que OpenClaw mantiene allí el saneamiento de firmas de pensamiento de Gemini sin habilitar la validación nativa de repetición de Gemini ni las reescrituras de arranque.

Comportamiento de repetición no Gemini

Las referencias de OpenCode no Gemini mantienen la política mínima de repetición compatible con OpenAI.

## Relacionado

[**Selección de modelos** Elegir proveedores, referencias de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Referencia de configuración** Referencia completa de configuración para agentes, modelos y proveedores. ](</es/gateway/configuration-reference>)

Was this useful?YesNo