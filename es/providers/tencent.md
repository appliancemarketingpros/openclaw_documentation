---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/es/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud se distribuye como un Plugin proveedor incluido en OpenClaw. Proporciona acceso a Tencent Hy3 preview mediante el endpoint TokenHub (`tencent-tokenhub`) usando una API compatible con OpenAI.

Propiedad | Valor  
---|---  
ID de proveedor | `tencent-tokenhub`  
Plugin | incluido, `enabledByDefault: true`  
Variable env de autenticación | `TOKENHUB_API_KEY`  
Flag de onboarding | `--auth-choice tokenhub-api-key`  
Flag directo de CLI | `--tokenhub-api-key <key>`  
API | compatible con OpenAI (`openai-completions`)  
URL base predeterminada | `https://tokenhub.tencentmaas.com/v1`  
URL base global | `https://tokenhub-intl.tencentmaas.com/v1` (sobrescritura)  
Modelo predeterminado | `tencent-tokenhub/hy3-preview`  
  
## Inicio rápido

* ### Crea una clave de API de TokenHub

Crea una clave de API en Tencent Cloud TokenHub. Si eliges un ámbito de acceso limitado para la clave, incluye **Hy3 preview** en los modelos permitidos.

* ### Ejecuta el onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Flag directoCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Solo envCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Verifica el modelo

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Configuración no interactiva

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catálogo integrado

Ref. de modelo | Nombre | Entrada | Contexto | Salida máxima | Notas  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | texto | 256,000 | 64,000 | Predeterminado; con razonamiento habilitado  
  
Hy3 preview es el modelo de lenguaje MoE grande de Tencent Hunyuan para razonamiento, seguimiento de instrucciones con contexto largo, código y flujos de trabajo de agentes. Los ejemplos compatibles con OpenAI de Tencent usan `hy3-preview` como ID de modelo y admiten llamadas a herramientas estándar de chat completions, además de `reasoning_effort`.

## Precios por niveles

El catálogo incluido se distribuye con metadatos de coste por niveles que escalan con la longitud de la ventana de entrada, por lo que las estimaciones de coste se completan sin sobrescrituras manuales.

Rango de tokens de entrada | Tarifa de entrada | Tarifa de salida | Lectura de caché  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
Las tarifas son por millón de tokens en USD, según lo anunciado por Tencent. Sobrescribe los precios en `models.providers.tencent-tokenhub` solo cuando necesites una superficie diferente.

## Configuración avanzada

Sobrescritura de endpoint

OpenClaw usa de forma predeterminada el endpoint de Tencent Cloud `https://tokenhub.tencentmaas.com/v1`. Tencent también documenta un endpoint internacional de TokenHub:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Sobrescribe el endpoint solo cuando tu cuenta o región de TokenHub lo requiera.

Disponibilidad del entorno para el daemon

Si el Gateway se ejecuta como un servicio administrado (launchd, systemd, Docker), `TOKENHUB_API_KEY` debe ser visible para ese proceso. Configúralo en `~/.openclaw/.env` o mediante `env.shellEnv` para que los entornos de launchd, systemd o Docker exec puedan leerlo.

## Relacionado

[**Proveedores de modelos** Elección de proveedores, refs. de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Referencia de configuración** Esquema de configuración completo, incluidos los ajustes de proveedor. ](</es/gateway/configuration>) [**Tencent TokenHub** Página de producto TokenHub de Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**Ficha del modelo Hy3 preview** Detalles y benchmarks de Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo