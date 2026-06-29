---
title: Qwen OAuth / Portal
source_url: https://docs.openclaw.ai/es/providers/qwen-oauth
scraped_at: 2026-06-29
---

ModelsProviders

`qwen-oauth` es el id de proveedor de Qwen Portal. Apunta al endpoint de Qwen Portal y mantiene las configuraciones antiguas de Qwen OAuth / portal accesibles mediante un id de proveedor distinto.

Usa este proveedor cuando tengas específicamente un token actual de Qwen Portal para `https://portal.qwen.ai/v1`, o cuando estés migrando una configuración antigua de Qwen Portal / Qwen CLI y quieras mantener esas credenciales separadas del proveedor canónico de Qwen Cloud. No es la primera opción recomendada para nuevos usuarios de Qwen.

Para nuevas configuraciones de Qwen Cloud, prefiere [Qwen](</es/providers/qwen>) con el endpoint Standard de ModelStudio, salvo que tengas específicamente un token actual de Qwen Portal.

## Configuración

Proporciona tu token del portal durante la incorporación:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-oauth
[/code]

O define:

bashCopy code
[code]
    export QWEN_API_KEY="<your-qwen-portal-token>" # pragma: allowlist secret
[/code]

## Valores predeterminados

  * Proveedor: `qwen-oauth`
  * Alias: `qwen-portal`, `qwen-cli`
  * URL base: `https://portal.qwen.ai/v1`
  * Variable de entorno: `QWEN_API_KEY`
  * Estilo de API: compatible con OpenAI
  * Modelo predeterminado: `qwen-oauth/qwen3.5-plus`


## En qué se diferencia de Qwen

OpenClaw tiene dos ids de proveedor orientados a Qwen:

Proveedor | Familia de endpoints | Ideal para  
---|---|---  
`qwen` | Endpoints de Qwen Cloud / Alibaba DashScope y Coding Plan | Nuevas configuraciones con clave de API, Standard de pago por uso, Coding Plan, funciones multimodales de DashScope  
`qwen-oauth` | Endpoint de Qwen Portal en `portal.qwen.ai/v1` | Tokens existentes de Qwen Portal y configuraciones heredadas de Qwen OAuth / CLI  
  
Ambos proveedores usan formatos de solicitud compatibles con OpenAI, pero son superficies de autenticación separadas. Un token almacenado para `qwen-oauth` no debe tratarse como una clave de DashScope o ModelStudio, y una nueva clave de DashScope debe usar en su lugar el proveedor canónico `qwen`.

## Cuándo elegir Qwen OAuth / Portal

  * Ya tienes un token funcional de Qwen Portal.
  * Estás conservando un flujo de trabajo heredado de Qwen OAuth o Qwen CLI mientras migras al modelo de proveedores de OpenClaw.
  * Necesitas probar específicamente la compatibilidad con el endpoint de Qwen Portal.


Elige [Qwen](</es/providers/qwen>) para configuraciones nuevas, opciones de endpoint más amplias, Standard ModelStudio, Coding Plan y el catálogo completo del Plugin de Qwen.

## Modelos

El catálogo del Plugin de Qwen inicializa el valor predeterminado de Qwen Portal:

  * `qwen-oauth/qwen3.5-plus`


La disponibilidad depende de la cuenta y el token actuales de Qwen Portal. Si tu cuenta usa claves de API de ModelStudio / DashScope en su lugar, configura el proveedor canónico `qwen`:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-keyopenclaw models set qwen/qwen3-coder-plus
[/code]

## Migración

Es posible que los perfiles heredados de Qwen Portal OAuth no se puedan actualizar. Si un perfil del portal deja de funcionar, vuelve a autenticarte con un token actual o cambia al proveedor Standard de Qwen:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Standard global de ModelStudio usa:

textCopy code
[code]
    https://dashscope-intl.aliyuncs.com/compatible-mode/v1
[/code]

## Solución de problemas

  * Errores de actualización de Portal OAuth: es posible que los perfiles heredados de Qwen Portal OAuth no se puedan actualizar. Vuelve a ejecutar la incorporación con un token actual.
  * Errores de endpoint incorrecto: confirma que la referencia del modelo empiece por `qwen-oauth/` cuando uses un token del portal. Usa referencias `qwen/` solo para el proveedor canónico de Qwen.
  * Confusión con `QWEN_API_KEY`: ambas páginas de Qwen mencionan esta variable de entorno, pero la incorporación almacena las credenciales bajo el id de proveedor seleccionado. Prefiere la incorporación cuando mantengas `qwen` y `qwen-oauth` disponibles en la misma máquina.


## Relacionado

  * [Qwen](</es/providers/qwen>)
  * [Alibaba Model Studio](</es/providers/alibaba>)
  * [Proveedores de modelos](</es/concepts/model-providers>)
  * [Todos los proveedores](</es/providers>)


Was this useful?YesNo

Open issue