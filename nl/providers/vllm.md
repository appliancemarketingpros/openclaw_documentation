---
title: vLLM
source_url: https://docs.openclaw.ai/nl/providers/vllm
scraped_at: 2026-05-25
---

vLLM kan open-source- en sommige aangepaste modellen aanbieden via een **OpenAI-compatibele** HTTP-API. OpenClaw maakt verbinding met vLLM via de `openai-completions`-API.

OpenClaw kan ook beschikbare modellen van vLLM **automatisch ontdekken** wanneer je je aanmeldt met `VLLM_API_KEY` (elke waarde werkt als je server geen auth afdwingt). Gebruik `vllm/*` in `agents.defaults.models` om ontdekking dynamisch te houden wanneer je ook een aangepaste vLLM-basis-URL configureert.

OpenClaw behandelt `vllm` als een lokale OpenAI-compatibele provider die gestreamde gebruiksboekhouding ondersteunt, zodat tokenaantallen voor status/context kunnen worden bijgewerkt vanuit `stream_options.include_usage`-responses.

Eigenschap | Waarde  
---|---  
Provider-ID | `vllm`  
API | `openai-completions` (OpenAI-compatibel)  
Auth | `VLLM_API_KEY`-omgevingsvariabele  
Standaard basis-URL | `http://127.0.0.1:8000/v1`  
  
## Aan de slag

* ### Start vLLM with an OpenAI-compatible server

Je basis-URL moet `/v1`-eindpunten beschikbaar maken (bijv. `/v1/models`, `/v1/chat/completions`). vLLM draait meestal op:

CodeCopy code
[code]
    http://127.0.0.1:8000/v1
[/code]

* ### Set the API key environment variable

Elke waarde werkt als je server geen auth afdwingt:

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

* ### Select a model

Vervang dit door een van je vLLM-model-ID's:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vllm/your-model-id" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

## Modelontdekking (impliciete provider)

Wanneer `VLLM_API_KEY` is ingesteld (of er een auth-profiel bestaat) en je **geen** `models.providers.vllm` definieert, bevraagt OpenClaw:

CodeCopy code
[code]
    GET http://127.0.0.1:8000/v1/models
[/code]

en zet de geretourneerde ID's om in modelvermeldingen.

## Expliciete configuratie (handmatige modellen)

Gebruik expliciete configuratie wanneer:

  * vLLM op een andere host of poort draait
  * Je `contextWindow`\- of `maxTokens`-waarden wilt vastzetten
  * Je server een echte API-sleutel vereist (of je headers wilt beheren)
  * Je verbinding maakt met een vertrouwd loopback-, LAN- of Tailscale-vLLM-eindpunt

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300, // Optional: extend connect/header/body/request timeout for slow local models        models: [          {            id: "your-model-id",            name: "Local vLLM Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

Om deze provider dynamisch te houden zonder elk model handmatig te vermelden, voeg je een provider-wildcard toe aan de zichtbare modelcatalogus:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/*": {},      },    },  },}
[/code]

## Geavanceerde configuratie

Proxy-style behavior

vLLM wordt behandeld als een proxy-achtige OpenAI-compatibele `/v1`-backend, niet als een native OpenAI-eindpunt. Dit betekent:

Gedrag | Toegepast?  
---|---  
Native OpenAI-requestvorming | Nee  
`service_tier` | Niet verzonden  
Responses `store` | Niet verzonden  
Prompt-cachehints | Niet verzonden  
OpenAI-reasoning-compatibele payloadvorming | Niet toegepast  
Verborgen OpenClaw-attributieheaders | Niet geïnjecteerd op aangepaste basis-URL's  
Qwen thinking controls

Voor Qwen-modellen die via vLLM worden aangeboden, stel je `params.qwenThinkingFormat: "chat-template"` in op de modelvermelding wanneer de server Qwen-chat-template-kwargs verwacht. OpenClaw wijst `/think off` toe aan:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "preserve_thinking": true  }}
[/code]

Niet-`off`-denkniveaus verzenden `enable_thinking: true`. Als je eindpunt in plaats daarvan DashScope-achtige flags op topniveau verwacht, gebruik dan `params.qwenThinkingFormat: "top-level"` om `enable_thinking` in de requestroot te verzenden. Snake-case `params.qwen_thinking_format` wordt ook geaccepteerd.

Nemotron 3 thinking controls

vLLM/Nemotron 3 kan chat-template-kwargs gebruiken om te bepalen of reasoning wordt geretourneerd als verborgen reasoning of als zichtbare antwoordtekst. Wanneer een OpenClaw-sessie `vllm/nemotron-3-*` gebruikt met denken uit, verzendt de gebundelde vLLM-Plugin:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "force_nonempty_content": true  }}
[/code]

Om deze waarden aan te passen, stel je `chat_template_kwargs` in onder de modelparams. Als je ook `params.extra_body.chat_template_kwargs` instelt, heeft die waarde uiteindelijke voorrang omdat `extra_body` de laatste override van de request-body is.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/nemotron-3-super": {          params: {            chat_template_kwargs: {              enable_thinking: false,              force_nonempty_content: true,            },          },        },      },    },  },}
[/code]

Qwen tool calls appear as text

Controleer eerst of vLLM is gestart met de juiste tool-callparser en chat-template voor het model. vLLM documenteert bijvoorbeeld `hermes` voor Qwen2.5- modellen en `qwen3_xml` voor Qwen3-Coder-modellen.

Symptomen:

  * Skills of tools worden nooit uitgevoerd
  * de assistent print ruwe JSON/XML zoals `{"name":"read","arguments":...}`
  * vLLM retourneert een lege `tool_calls`-array wanneer OpenClaw `tool_choice: "auto"` verzendt


Sommige Qwen/vLLM-combinaties retourneren alleen gestructureerde tool calls wanneer de request `tool_choice: "required"` gebruikt. Forceer voor die modelvermeldingen het OpenAI-compatibele requestveld met `params.extra_body`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/Qwen-Qwen2.5-Coder-32B-Instruct": {          params: {            extra_body: {              tool_choice: "required",            },          },        },      },    },  },}
[/code]

Vervang `Qwen-Qwen2.5-Coder-32B-Instruct` door de exacte id die wordt geretourneerd door:

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

Je kunt dezelfde override toepassen vanuit de CLI:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"vllm/Qwen-Qwen2.5-Coder-32B-Instruct":{"params":{"extra_body":{"tool_choice":"required"}}}}' --strict-json --merge
[/code]

Dit is een opt-in compatibiliteitsworkaround. Hierdoor vereist elke modelbeurt met tools een tool call, dus gebruik dit alleen voor een speciale lokale modelvermelding waarbij dat gedrag acceptabel is. Gebruik dit niet als globale standaard voor alle vLLM-modellen en gebruik geen proxy die willekeurige assistenttekst blind omzet in uitvoerbare tool calls.

Custom base URL

Als je vLLM-server op een niet-standaard host of poort draait, stel je `baseUrl` in de expliciete providerconfiguratie in:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:9000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [          {            id: "my-custom-model",            name: "Remote vLLM Model",            reasoning: false,            input: ["text"],            contextWindow: 64000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Probleemoplossing

Slow first response or remote server timeout

Stel voor grote lokale modellen, externe LAN-hosts of tailnet-links een requesttimeout met providerscope in:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [{ id: "your-model-id", name: "Local vLLM Model" }],      },    },  },}
[/code]

`timeoutSeconds` is alleen van toepassing op HTTP-requests voor vLLM-modellen, inclusief het opzetten van de verbinding, responseheaders, bodystreaming en de totale bewaakte-fetch-afbreking. Geef hier de voorkeur aan voordat je `agents.defaults.timeoutSeconds` verhoogt, dat de hele agentrun beheert.

Server not reachable

Controleer of de vLLM-server draait en toegankelijk is:

bashCopy code
[code]
    curl http://127.0.0.1:8000/v1/models
[/code]

Als je een verbindingsfout ziet, controleer dan de host, poort en of vLLM is gestart met de OpenAI-compatibele servermodus. Voor expliciete loopback-, LAN- of Tailscale-eindpunten stel je ook `models.providers.vllm.request.allowPrivateNetwork: true` in; provider- requests blokkeren standaard private-netwerk-URL's tenzij de provider expliciet wordt vertrouwd.

Auth errors on requests

Als requests mislukken met auth-fouten, stel dan een echte `VLLM_API_KEY` in die overeenkomt met je serverconfiguratie, of configureer de provider expliciet onder `models.providers.vllm`.

No models discovered

Automatische ontdekking vereist dat `VLLM_API_KEY` is ingesteld. Als je `models.providers.vllm` hebt gedefinieerd, gebruikt OpenClaw alleen je gedeclareerde modellen tenzij `agents.defaults.models` `"vllm/*": {}` bevat.

Tools render as raw text

Als een Qwen-model JSON/XML-toolsyntaxis print in plaats van een Skill uit te voeren, controleer dan de Qwen-richtlijnen in Geavanceerde configuratie hierboven. De gebruikelijke oplossing is:

  * start vLLM met de juiste parser/template voor dat model
  * bevestig de exacte model-id met `openclaw models list --provider vllm`
  * voeg alleen een speciale per-model-override `params.extra_body.tool_choice: "required"` toe als `tool_choice: "auto"` nog steeds lege of tekst-only tool calls retourneert


## Gerelateerd

[**Model selection** Providers, modelrefs en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**OpenAI** Native OpenAI-provider en OpenAI-compatibel routegedrag. ](</nl/providers/openai>) [**OAuth and auth** Auth-details en regels voor hergebruik van referenties. ](</nl/gateway/authentication>) [**Troubleshooting** Veelvoorkomende problemen en hoe je ze oplost. ](</nl/help/troubleshooting>)

Was this useful?YesNo