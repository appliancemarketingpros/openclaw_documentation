---
title: Cohere
source_url: https://docs.openclaw.ai/es/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) proporciona inferencia compatible con OpenAI mediante su API de compatibilidad. OpenClaw incluye el proveedor Cohere durante su transición de externalización y también lo publica como plugin externo oficial con el catálogo de modelos Command A.

Propiedad | Valor  
---|---  
ID de proveedor | `cohere`  
Plugin | incluido durante la transición; paquete externo oficial  
Variable de entorno auth | `COHERE_API_KEY`  
Marca de onboarding | `--auth-choice cohere-api-key`  
Marca directa de CLI | `--cohere-api-key <key>`  
API | compatible con OpenAI (`openai-completions`)  
URL base | `https://api.cohere.ai/compatibility/v1`  
Modelo predeterminado | `cohere/command-a-03-2025`  
  
## Primeros pasos

  1. Cohere está incluido en los paquetes actuales de OpenClaw. Si no está disponible, instala el paquete externo y reinicia el Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Crea una clave de API de Cohere.
  3. Ejecuta el onboarding:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Confirma que el catálogo esté disponible:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

El modelo predeterminado se establece solo cuando no hay ningún modelo principal ya configurado.

## Configuración solo con entorno

Haz que `COHERE_API_KEY` esté disponible para el proceso del Gateway y luego selecciona el modelo de Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Relacionado

  * [Proveedores de modelos](</es/concepts/model-providers>)
  * [CLI de modelos](</es/cli/models>)
  * [Directorio de proveedores](</es/providers>)


Was this useful?YesNo

Open issue