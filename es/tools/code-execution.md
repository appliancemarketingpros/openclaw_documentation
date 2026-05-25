---
title: Ejecución de código
source_url: https://docs.openclaw.ai/es/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` ejecuta análisis de Python remoto en sandbox en la API Responses de xAI. Lo registra el plugin `xai` incluido (bajo el contrato `tools`) y se despacha al mismo endpoint `https://api.x.ai/v1/responses` que usa `x_search`.

Propiedad | Valor  
---|---  
Nombre de la herramienta | `code_execution`  
Plugin de proveedor | `xai` (incluido, `enabledByDefault: true`)  
Autenticación | Perfil de autenticación de xAI, `XAI_API_KEY`, o `plugins.entries.xai.config.webSearch.apiKey`  
Modelo predeterminado | `grok-4-1-fast`  
Tiempo de espera predeterminado | 30 segundos  
`maxTurns` predeterminado | sin establecer (xAI aplica su propio límite interno)  
  
Esto es distinto de [`exec`](</es/tools/exec>) local:

  * `exec` ejecuta comandos de shell en tu máquina o nodo emparejado.
  * `code_execution` ejecuta Python en el sandbox remoto de xAI.


Usa `code_execution` para:

  * Cálculos.
  * Tabulación.
  * Estadísticas rápidas.
  * Análisis de estilo gráfico.
  * Analizar datos devueltos por `x_search` o `web_search`.


**No** lo uses cuando necesites archivos locales, tu shell, tu repositorio o dispositivos emparejados. Usa [`exec`](</es/tools/exec>) para eso.

## Configuración

* ### Proporciona una clave de API de xAI

Run `openclaw onboard --auth-choice xai-api-key` for `code_execution` and `x_search`, or set `XAI_API_KEY` / configure the key under the xAI plugin when you also want Grok web search to use the same credential:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

O mediante configuración:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Habilita y ajusta code_execution

La herramienta está controlada por `plugins.entries.xai.config.codeExecution.enabled`. El valor predeterminado es desactivado.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Reinicia el Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` aparece en la lista de herramientas del agente una vez que el plugin xAI vuelve a registrarse con `enabled: true`.

## Cómo usarlo

Pide de forma natural y explicita la intención del análisis:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

La herramienta toma internamente un único parámetro `task`, así que el agente debe enviar la solicitud completa de análisis y cualquier dato en línea en un solo prompt.

## Errores

Cuando la herramienta se ejecuta sin autenticación, devuelve un error estructurado `missing_xai_api_key` que apunta al perfil de autenticación, la variable de entorno y las opciones de configuración. El error es JSON, no una excepción lanzada, por lo que el agente puede autocorregirse:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Límites

  * Esto es ejecución remota de xAI, no ejecución de procesos locales.
  * Trata los resultados como análisis efímero, no como una sesión persistente de notebook.
  * No asumas acceso a archivos locales ni a tu área de trabajo.
  * Para datos recientes de X, usa primero [`x_search`](</es/tools/web#x_search>) y canaliza el resultado a `code_execution`.


## Relacionado

[**Herramienta Exec** Ejecución de shell local en tu máquina o nodo emparejado. ](</es/tools/exec>) [**Aprobaciones de exec** Política de permitir/denegar para la ejecución de shell. ](</es/tools/exec-approvals>) [**Herramientas web** `web_search`, `x_search` y `web_fetch`. ](</es/tools/web>) [**Proveedor xAI** Modelos Grok, búsqueda web/X y configuración de ejecución de código. ](</es/providers/xai>)

Was this useful?YesNo