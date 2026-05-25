---
title: StepFun
source_url: https://docs.openclaw.ai/es/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw incluye un plugin de proveedor StepFun integrado con dos identificadores de proveedor:

  * `stepfun` para el endpoint estándar
  * `stepfun-plan` para el endpoint Step Plan


## Resumen de región y endpoint

Endpoint | China (`.com`) | Global (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Variable de entorno de autenticación: `STEPFUN_API_KEY`

## Catálogo integrado

Standard (`stepfun`):

Referencia de modelo | Contexto | Salida máxima | Notas  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Modelo estándar predeterminado  
  
Step Plan (`stepfun-plan`):

Referencia de modelo | Contexto | Salida máxima | Notas  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Modelo Step Plan predeterminado  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Modelo Step Plan adicional  
  
## Primeros pasos

Elige tu superficie de proveedor y sigue los pasos de configuración.

### Standard

**Ideal para:** uso de propósito general mediante el endpoint StepFun estándar.

* ### Elige la región de tu endpoint

Opción de autenticación | Endpoint | Región  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | Internacional  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | China  
* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

O para el endpoint de China:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Alternativa no interactiva

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verifica que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Referencias de modelo

  * Modelo predeterminado: `stepfun/step-3.5-flash`


### Step Plan

**Ideal para:** endpoint de razonamiento Step Plan.

* ### Elige la región de tu endpoint

Opción de autenticación | Endpoint | Región  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | Internacional  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | China  
* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

O para el endpoint de China:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Alternativa no interactiva

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verifica que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Referencias de modelo

  * Modelo predeterminado: `stepfun-plan/step-3.5-flash`
  * Modelo alternativo: `stepfun-plan/step-3.5-flash-2603`


## Configuración avanzada

Configuración completa: proveedor Standard json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Configuración completa: proveedor Step Plan json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Notas

  * El proveedor viene integrado con OpenClaw, por lo que no hay un paso separado para instalar plugins.
  * `step-3.5-flash-2603` actualmente solo está expuesto en `stepfun-plan`.
  * Un único flujo de autenticación escribe perfiles que coinciden con la región para `stepfun` y `stepfun-plan`, por lo que ambas superficies pueden descubrirse juntas.
  * Usa `openclaw models list` y `openclaw models set <provider/model>` para inspeccionar o cambiar modelos.


## Relacionado

[**Selección de modelos** Resumen de todos los proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Referencia de configuración** Esquema de configuración completo para proveedores, modelos y plugins. ](</es/gateway/configuration-reference>) [**Selección de modelos** Cómo elegir y configurar modelos. ](</es/concepts/models>) [**Plataforma StepFun** Gestión de claves de API y documentación de StepFun. ](<https://platform.stepfun.com>)

Was this useful?YesNo