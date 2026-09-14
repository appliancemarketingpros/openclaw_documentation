---
title: Azure OpenAI endpoints
source_url: https://docs.openclaw.ai/providers/openai/azure
scraped_at: 2026-09-14
---

ModelsProviders

## Azure OpenAI endpoints

The bundled `openai` provider can target an Azure OpenAI resource for image generation by overriding the base URL. On the image-generation path, OpenClaw detects Azure hostnames on `models.providers.openai.baseUrl` and switches to Azure's request shape automatically.

Use Azure OpenAI when:

  * You already have an Azure OpenAI subscription, quota, or enterprise agreement
  * You need regional data residency or compliance controls Azure provides
  * You want to keep traffic inside an existing Azure tenancy


### Configuration

For Azure image generation through the bundled `openai` provider, point `models.providers.openai.baseUrl` at your Azure resource and set `apiKey` to the Azure OpenAI key (not an OpenAI Platform key):

json5Copy code
[code]
    {  models: {    providers: {      openai: {        baseUrl: "https://<your-resource>.openai.azure.com",        apiKey: "<azure-openai-api-key>",      },    },  },}
[/code]

OpenClaw recognizes these Azure host suffixes for the Azure image-generation route:

  * `*.openai.azure.com`
  * `*.services.ai.azure.com`
  * `*.cognitiveservices.azure.com`


For image-generation requests on a recognized Azure host, OpenClaw:

  * Sends the `api-key` header instead of `Authorization: Bearer`
  * Uses deployment-scoped paths (`/openai/deployments/{deployment}/...`)
  * Appends `?api-version=...` to each request
  * Uses a 600s default request timeout for Azure image-generation calls. Per-call `timeoutMs` values still override this default.


Other base URLs (public OpenAI, OpenAI-compatible proxies) keep the standard OpenAI image request shape.

### API version

Set `AZURE_OPENAI_API_VERSION` to pin a specific Azure preview or GA version for the Azure image-generation path:

bashCopy code
[code]
    export AZURE_OPENAI_API_VERSION="2024-12-01-preview"
[/code]

The default is `2024-12-01-preview` when the variable is unset.

### Model names are deployment names

Azure OpenAI binds models to deployments. For Azure image-generation requests routed through the bundled `openai` provider, the `model` field in OpenClaw must be the **Azure deployment name** you configured in the Azure portal, not the public OpenAI model id.

If you create a deployment called `gpt-image-2-prod` that serves `gpt-image-2`:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2-prod prompt="A clean poster" size=1024x1024 count=1
[/code]

The same deployment-name rule applies to any image-generation call routed through the bundled `openai` provider.

### Regional availability

Azure image generation is currently available only in a subset of regions (for example `eastus2`, `swedencentral`, `polandcentral`, `westus3`, `uaenorth`). Check Microsoft's current region list before creating a deployment, and confirm the specific model is offered in your region.

### Parameter differences

Azure OpenAI and public OpenAI do not always accept the same image parameters. Azure may reject options public OpenAI allows (for example certain `background` values on `gpt-image-2`) or expose them only on specific model versions. These differences come from Azure and the underlying model, not OpenClaw. If an Azure request fails with a validation error, check the parameter set supported by your specific deployment and API version in the Azure portal.

Was this useful?YesNo

Open issue