---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/it/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud viene distribuito come Plugin provider in bundle in OpenClaw. Offre accesso a Tencent Hy3 preview tramite l'endpoint TokenHub (`tencent-tokenhub`) usando un'API compatibile con OpenAI.

Proprietà | Valore  
---|---  
ID provider | `tencent-tokenhub`  
Plugin | in bundle, `enabledByDefault: true`  
Variabile env di autenticazione | `TOKENHUB_API_KEY`  
Flag di onboarding | `--auth-choice tokenhub-api-key`  
Flag CLI diretto | `--tokenhub-api-key <key>`  
API | compatibile con OpenAI (`openai-completions`)  
URL base predefinito | `https://tokenhub.tencentmaas.com/v1`  
URL base globale | `https://tokenhub-intl.tencentmaas.com/v1` (override)  
Modello predefinito | `tencent-tokenhub/hy3-preview`  
  
## Avvio rapido

* ### Crea una chiave API TokenHub

Crea una chiave API in Tencent Cloud TokenHub. Se scegli un ambito di accesso limitato per la chiave, includi **Hy3 preview** nei modelli consentiti.

* ### Esegui l'onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Verifica il modello

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Configurazione non interattiva

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catalogo integrato

Riferimento modello | Nome | Input | Contesto | Output massimo | Note  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | text | 256,000 | 64,000 | Predefinito; supporta il ragionamento  
  
Hy3 preview è il grande modello linguistico MoE di Tencent Hunyuan per ragionamento, istruzioni con contesto lungo, codice e flussi di lavoro con agenti. Gli esempi compatibili con OpenAI di Tencent usano `hy3-preview` come ID modello e supportano la chiamata di strumenti standard per chat completions oltre a `reasoning_effort`.

## Prezzi a livelli

Il catalogo in bundle include metadati di costo a livelli che scalano con la lunghezza della finestra di input, quindi le stime dei costi vengono popolate senza override manuali.

Intervallo token di input | Tariffa input | Tariffa output | Lettura cache  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
Le tariffe sono per milione di token in USD come pubblicizzato da Tencent. Sovrascrivi i prezzi in `models.providers.tencent-tokenhub` solo quando ti serve una superficie diversa.

## Configurazione avanzata

Override dell'endpoint

OpenClaw usa per impostazione predefinita l'endpoint Tencent Cloud `https://tokenhub.tencentmaas.com/v1`. Tencent documenta anche un endpoint TokenHub internazionale:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Sovrascrivi l'endpoint solo quando il tuo account o la tua regione TokenHub lo richiede.

Disponibilità dell'ambiente per il daemon

Se il Gateway viene eseguito come servizio gestito (launchd, systemd, Docker), `TOKENHUB_API_KEY` deve essere visibile a quel processo. Impostala in `~/.openclaw/.env` o tramite `env.shellEnv` affinché gli ambienti launchd, systemd o Docker exec possano leggerla.

## Correlati

[**Provider di modelli** Scelta dei provider, riferimenti modello e comportamento di failover. ](</it/concepts/model-providers>) [**Riferimento di configurazione** Schema di configurazione completo, incluse le impostazioni dei provider. ](</it/gateway/configuration>) [**Tencent TokenHub** Pagina prodotto TokenHub di Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**Scheda modello Hy3 preview** Dettagli e benchmark di Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo