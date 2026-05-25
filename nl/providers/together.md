---
title: Together AI
source_url: https://docs.openclaw.ai/nl/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) biedt toegang tot toonaangevende open-sourcemodellen, waaronder Llama, DeepSeek, Kimi en meer, via een uniforme API.

Eigenschap | Waarde  
---|---  
Provider | `together`  
Auth | `TOGETHER_API_KEY`  
API | OpenAI-compatibel  
Basis-URL | `https://api.together.xyz/v1`  
  
## Aan de slag

* ### Haal een API-sleutel op

Maak een API-sleutel aan op [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Voer onboarding uit

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Stel een standaardmodel in

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Niet-interactief voorbeeld

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Ingebouwde catalogus

OpenClaw levert deze gebundelde Together-catalogus mee:

Modelref | Naam | Invoer | Context | Opmerkingen  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | tekst, beeld | 262,144 | Standaardmodel; reasoning ingeschakeld  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | tekst | 202,752 | Tekstmodel voor algemeen gebruik  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | tekst | 131,072 | Snel instructiemodel  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | tekst, beeld | 10,000,000 | Multimodaal  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | tekst, beeld | 20,000,000 | Multimodaal  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | tekst | 131,072 | Algemeen tekstmodel  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | tekst | 131,072 | Reasoning-model  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | tekst | 262,144 | Secundair Kimi-tekstmodel  
  
## Video genereren

De gebundelde `together`-Plugin registreert ook video genereren via de gedeelde tool `video_generate`.

Eigenschap | Waarde  
---|---  
Standaardvideomodel | `together/Wan-AI/Wan2.2-T2V-A14B`  
Modi | tekst-naar-video, enkele afbeeldingsreferentie  
Ondersteunde parameters | `aspectRatio`, `resolution`  
  
Om Together als standaardvideoprovider te gebruiken:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Omgevingsnotitie

Als de Gateway als daemon draait (launchd/systemd), zorg er dan voor dat `TOGETHER_API_KEY` beschikbaar is voor dat proces (bijvoorbeeld in `~/.openclaw/.env` of via `env.shellEnv`).

Probleemoplossing

  * Controleer of je sleutel werkt: `openclaw models list --provider together`
  * Als modellen niet verschijnen, controleer dan of de API-sleutel in de juiste omgeving voor je Gateway-proces is ingesteld.
  * Modelrefs gebruiken de vorm `together/<model-id>`.


## Gerelateerd

[**Modelselectie** Providerregels, modelrefs en failovergedrag. ](</nl/concepts/model-providers>) [**Video genereren** Gedeelde parameters voor de tool voor video genereren en providerselectie. ](</nl/tools/video-generation>) [**Configuratiereferentie** Volledig configuratieschema inclusief providerinstellingen. ](</nl/gateway/configuration-reference>) [**Together AI** Together AI-dashboard, API-documentatie en prijzen. ](<https://together.ai>)

Was this useful?YesNo