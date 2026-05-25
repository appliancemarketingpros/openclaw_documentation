---
title: Texto para fala
source_url: https://docs.openclaw.ai/pt-BR/tools/tts
scraped_at: 2026-05-25
---

OpenClaw pode converter respostas de saída em áudio em **14 provedores de fala** e entregar mensagens de voz nativas no Feishu, Matrix, Telegram e WhatsApp, anexos de áudio em todos os outros lugares, e fluxos PCM/Ulaw para telefonia e Talk.

TTS é a metade de saída de fala do modo `stt-tts` do Talk. Sessões Talk `realtime` nativas do provedor sintetizam fala dentro do provedor em tempo real em vez de chamar este caminho de TTS, enquanto sessões `transcription` não sintetizam uma resposta de voz do assistente.

## Início rápido

* ### Escolha um provedor

OpenAI e ElevenLabs são as opções hospedadas mais confiáveis. Microsoft e Local CLI funcionam sem uma chave de API. Consulte a matriz de provedores para ver a lista completa.

* ### Defina a chave de API

Exporte a variável de ambiente do seu provedor (por exemplo `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). Microsoft e Local CLI não precisam de chave.

* ### Habilite na configuração

Defina `messages.tts.auto: "always"` e `messages.tts.provider`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Experimente no chat

`/tts status` mostra o estado atual. `/tts audio Hello from OpenClaw` envia uma resposta de áudio avulsa.

## Provedores compatíveis

Provedor | Autenticação | Observações  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (também `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Saída nativa de recado de voz Ogg/Opus e telefonia.  
**DeepInfra** | `DEEPINFRA_API_KEY` | TTS compatível com OpenAI. Padrão: `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` ou `XI_API_KEY` | Clonagem de voz, multilíngue, determinístico via `seed`; transmitido para reprodução de voz no Discord.  
**Google Gemini** | `GEMINI_API_KEY` ou `GOOGLE_API_KEY` | TTS em lote da API Gemini; consciente de persona via `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | Saída de recado de voz e telefonia.  
**Inworld** | `INWORLD_API_KEY` | API de TTS por streaming. Recado de voz Opus nativo e telefonia PCM.  
**Local CLI** | nenhuma | Executa um comando local de TTS configurado.  
**Microsoft** | nenhuma | TTS neural público do Edge via `node-edge-tts`. Melhor esforço, sem SLA.  
**MiniMax** | `MINIMAX_API_KEY` (ou Token Plan: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | API T2A v2. Padrão: `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | Também usado para resumo automático; oferece suporte a `instructions` de persona.  
**OpenRouter** | `OPENROUTER_API_KEY` (pode reutilizar `models.providers.openrouter.apiKey`) | Modelo padrão `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` ou `BYTEPLUS_SEED_SPEECH_API_KEY` (AppID/token legado: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | API HTTP BytePlus Seed Speech.  
**Vydra** | `VYDRA_API_KEY` | Provedor compartilhado de imagem, vídeo e fala.  
**xAI** | `XAI_API_KEY` | TTS em lote da xAI. Recado de voz Opus nativo **não** é compatível.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | TTS MiMo por meio de conclusões de chat da Xiaomi.  
  
Se vários provedores estiverem configurados, o selecionado será usado primeiro e os outros serão opções de fallback. O resumo automático usa `summaryModel` (ou `agents.defaults.model.primary`), então esse provedor também deve estar autenticado se você mantiver os resumos habilitados.

## Configuração

A configuração de TTS fica em `messages.tts` em `~/.openclaw/openclaw.json`. Escolha uma predefinição e adapte o bloco do provedor:

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      voice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      voiceName: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      voiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      voiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (sem chave)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      voice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      voiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      voice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      voice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      voice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      voiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      voice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

### Substituições de voz por agente

Use `agents.list[].tts` quando um agente deve falar com um provedor, voz, modelo, persona ou modo de TTS automático diferente. O bloco do agente faz mesclagem profunda sobre `messages.tts`, então as credenciais do provedor podem permanecer na configuração global do provedor:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

Para fixar uma persona por agente, defina `agents.list[].tts.persona` junto com a configuração do provedor — ela substitui o `messages.tts.persona` global apenas para esse agente.

Ordem de precedência para respostas automáticas, `/tts audio`, `/tts status` e a ferramenta de agente `tts`:

  1. `messages.tts`
  2. `agents.list[].tts` ativo
  3. substituição de canal, quando o canal oferece suporte a `channels.<channel>.tts`
  4. substituição de conta, quando o canal passa `channels.<channel>.accounts.<id>.tts`
  5. preferências locais de `/tts` para este host
  6. diretivas inline `[[tts:...]]` quando substituições de modelo estão habilitadas


Substituições de canal e conta usam o mesmo formato de `messages.tts` e fazem deep merge sobre as camadas anteriores, para que credenciais compartilhadas de provedor possam permanecer em `messages.tts` enquanto um canal ou conta de bot altera apenas voz, modelo, persona ou modo automático:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## Personas

Uma **persona** é uma identidade falada estável que pode ser aplicada deterministicamente entre provedores. Ela pode preferir um provedor, definir intenção de prompt independente de provedor e carregar vinculações específicas de provedor para vozes, modelos, templates de prompt, seeds e configurações de voz.

### Persona mínima

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### Persona completa (prompt independente de provedor)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### Resolução de persona

A persona ativa é selecionada deterministicamente:

  1. preferência local `/tts persona <id>`, se definida.
  2. `messages.tts.persona`, se definido.
  3. Nenhuma persona.


A seleção de provedor executa explícitos primeiro:

  1. Substituições diretas (CLI, Gateway, Talk, diretivas TTS permitidas).
  2. preferência local `/tts provider <id>`.
  3. `provider` da persona ativa.
  4. `messages.tts.provider`.
  5. Seleção automática do registro.


Para cada tentativa de provedor, o OpenClaw combina configurações nesta ordem:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. Substituições confiáveis da requisição
  4. Substituições permitidas de diretivas TTS emitidas pelo modelo


### Como os provedores usam prompts de persona

Os campos de prompt de persona (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) são **independentes de provedor**. Cada provedor decide como usá-los:

Google Gemini

Encapsula campos de prompt de persona em uma estrutura de prompt TTS do Gemini **somente quando** a configuração efetiva do provedor Google define `promptTemplate: "audio-profile-v1"` ou `personaPrompt`. Os campos antigos `audioProfile` e `speakerName` ainda são prefixados como texto de prompt específico do Google. Tags de áudio inline, como `[whispers]` ou `[laughs]`, dentro de um bloco `[[tts:text]]` são preservadas dentro da transcrição do Gemini; o OpenClaw não gera essas tags.

OpenAI

Mapeia campos de prompt de persona para o campo `instructions` da requisição **somente quando** nenhuma `instructions` explícita do OpenAI estiver configurada. `instructions` explícitas sempre vencem.

Outros provedores

Usam apenas as vinculações de persona específicas do provedor em `personas.<id>.providers.<provider>`. Campos de prompt de persona são ignorados, a menos que o provedor implemente seu próprio mapeamento de prompt de persona.

### Política de fallback

`fallbackPolicy` controla o comportamento quando uma persona **não tem vinculação** para o provedor tentado:

Política | Comportamento  
---|---  
`preserve-persona` | **Padrão.** Campos de prompt independentes de provedor permanecem disponíveis; o provedor pode usá-los ou ignorá-los.  
`provider-defaults` | A persona é omitida da preparação do prompt para essa tentativa; o provedor usa seus padrões neutros enquanto o fallback para outros provedores continua.  
`fail` | Ignora essa tentativa de provedor com `reasonCode: "not_configured"` e `personaBinding: "missing"`. Provedores de fallback ainda são tentados.  
  
A requisição TTS inteira só falha quando **todos** os provedores tentados são ignorados ou falham.

A seleção de provedor da sessão Talk é escopada à sessão. Um cliente Talk deve escolher ids de provedor, ids de modelo, ids de voz e localidades a partir de `talk.catalog` e passá-los pela sessão Talk ou pela requisição de handoff. Abrir uma sessão de voz não deve alterar `messages.tts` nem os padrões globais de provedores do Talk.

## Diretivas orientadas por modelo

Por padrão, o assistente **pode** emitir diretivas `[[tts:...]]` para substituir voz, modelo ou velocidade em uma única resposta, além de um bloco opcional `[[tts:text]]...[[/tts:text]]` para dicas expressivas que devem aparecer apenas no áudio:

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

Quando `messages.tts.auto` é `"tagged"`, **diretivas são obrigatórias** para acionar áudio. A entrega de blocos em streaming remove as diretivas do texto visível antes que o canal as veja, mesmo quando divididas entre blocos adjacentes.

`provider=...` é ignorado, a menos que `modelOverrides.allowProvider: true`. Quando uma resposta declara `provider=...`, as outras chaves nessa diretiva são analisadas apenas por esse provedor; chaves sem suporte são removidas e relatadas como avisos de diretiva TTS.

**Chaves de diretiva disponíveis:**

  * `provider` (id de provedor registrado; requer `allowProvider: true`)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (volume MiniMax, 0–10)
  * `pitch` (tom inteiro MiniMax, −12 a 12; valores fracionários são truncados)
  * `emotion` (tag de emoção Volcengine)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**Desabilitar substituições de modelo completamente:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**Permitir troca de provedor enquanto mantém outros ajustes configuráveis:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Comandos slash

Comando único `/tts`. No Discord, o OpenClaw também registra `/voice` porque `/tts` é um comando integrado do Discord — o texto `/tts ...` ainda funciona.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

Notas de comportamento:

  * `/tts on` grava a preferência local de TTS como `always`; `/tts off` grava como `off`.
  * `/tts chat on|off|default` grava uma substituição de TTS automático escopada à sessão para o chat atual.
  * `/tts persona <id>` grava a preferência local de persona; `/tts persona off` a limpa.
  * `/tts latest` lê a resposta mais recente do assistente da transcrição da sessão atual e a envia como áudio uma vez. Ele armazena apenas um hash dessa resposta na entrada da sessão para suprimir envios de voz duplicados.
  * `/tts audio` gera uma resposta de áudio avulsa (não ativa o TTS).
  * `limit` e `summary` são armazenados em **preferências locais** , não na configuração principal.
  * `/tts status` inclui diagnósticos de fallback para a tentativa mais recente — `Fallback: <primary> -> <used>`, `Attempts: ...` e detalhes por tentativa (`provider:outcome(reasonCode) latency`).
  * `/status` mostra o modo TTS ativo, além de provedor, modelo, voz e metadados sanitizados de endpoint personalizado configurados quando TTS está habilitado.


## Preferências por usuário

Comandos slash gravam substituições locais em `prefsPath`. O padrão é `~/.openclaw/settings/tts.json`; substitua com a variável de ambiente `OPENCLAW_TTS_PREFS` ou `messages.tts.prefsPath`.

Campo armazenado | Efeito  
---|---  
`auto` | Substituição local de TTS automático (`always`, `off`, …)  
`provider` | Substituição local do provedor primário  
`persona` | Substituição local de persona  
`maxLength` | Limite de resumo (padrão `1500` chars)  
`summarize` | Alternância de resumo (padrão `true`)  
  
Eles substituem a configuração efetiva de `messages.tts` mais o bloco `agents.list[].tts` ativo para esse host.

## Formatos de saída (fixos)

A entrega de voz TTS é orientada pela capacidade do canal. Plugins de canal anunciam se TTS em estilo de voz deve solicitar aos provedores um destino `voice-note` nativo ou manter a síntese normal de `audio-file` e apenas marcar a saída compatível para entrega por voz.

  * **Canais compatíveis com notas de voz** : respostas em nota de voz preferem Opus (`opus_48000_64` da ElevenLabs, `opus` da OpenAI). 
    * 48 kHz / 64 kbps é uma boa relação para mensagens de voz.
  * **Feishu / WhatsApp** : quando uma resposta em nota de voz é produzida como MP3/WebM/WAV/M4A ou outro arquivo provavelmente de áudio, o Plugin de canal a transcodifica para Ogg/Opus em 48 kHz com `ffmpeg` antes de enviar a mensagem de voz nativa. O WhatsApp envia o resultado pelo payload `audio` do Baileys com `ptt: true` e `audio/ogg; codecs=opus`. Se a conversão falhar, o Feishu recebe o arquivo original como anexo; o envio pelo WhatsApp falha em vez de publicar um payload PTT incompatível.
  * **Outros canais** : MP3 (`mp3_44100_128` da ElevenLabs, `mp3` da OpenAI). 
    * 44,1 kHz / 128 kbps é o equilíbrio padrão para clareza de fala.
  * **MiniMax** : MP3 (modelo `speech-2.8-hd`, taxa de amostragem de 32 kHz) para anexos de áudio normais. Para destinos de nota de voz anunciados pelo canal, o OpenClaw transcodifica o MP3 da MiniMax para Opus em 48 kHz com `ffmpeg` antes da entrega quando o canal anuncia transcoding.
  * **Xiaomi MiMo** : MP3 por padrão, ou WAV quando configurado. Para destinos de nota de voz anunciados pelo canal, o OpenClaw transcodifica a saída da Xiaomi para Opus em 48 kHz com `ffmpeg` antes da entrega quando o canal anuncia transcoding.
  * **CLI local** : usa o `outputFormat` configurado. Destinos de nota de voz são convertidos para Ogg/Opus, e a saída de telefonia é convertida para PCM mono bruto de 16 kHz com `ffmpeg`.
  * **Google Gemini** : a TTS da API Gemini retorna PCM bruto de 24 kHz. O OpenClaw o encapsula como WAV para anexos de áudio, transcodifica para Opus em 48 kHz para destinos de nota de voz e retorna PCM diretamente para Talk/telefonia.
  * **Gradium** : WAV para anexos de áudio, Opus para destinos de nota de voz e `ulaw_8000` a 8 kHz para telefonia.
  * **Inworld** : MP3 para anexos de áudio normais, `OGG_OPUS` nativo para destinos de nota de voz e `PCM` bruto a 22050 Hz para Talk/telefonia.
  * **xAI** : MP3 por padrão; `responseFormat` pode ser `mp3`, `wav`, `pcm`, `mulaw` ou `alaw`. O OpenClaw usa o endpoint REST TTS em lote da xAI e retorna um anexo de áudio completo; o WebSocket de TTS por streaming da xAI não é usado por este caminho de provedor. O formato nativo Opus para nota de voz não é compatível com este caminho.
  * **Microsoft** : usa `microsoft.outputFormat` (padrão `audio-24khz-48kbitrate-mono-mp3`). 
    * O transporte incluído aceita um `outputFormat`, mas nem todos os formatos estão disponíveis no serviço.
    * Os valores de formato de saída seguem os formatos de saída do Microsoft Speech (incluindo Ogg/WebM Opus).
    * O `sendVoice` do Telegram aceita OGG/MP3/M4A; use OpenAI/ElevenLabs se precisar de mensagens de voz Opus garantidas.
    * Se o formato de saída Microsoft configurado falhar, o OpenClaw tenta novamente com MP3.


Os formatos de saída da OpenAI/ElevenLabs são fixos por canal (veja acima).

## Comportamento de Auto-TTS

Quando `messages.tts.auto` está habilitado, o OpenClaw:

  * Ignora TTS se a resposta já contém mídia ou uma diretiva `MEDIA:`.
  * Ignora respostas muito curtas (menos de 10 caracteres).
  * Resume respostas longas quando resumos estão habilitados, usando `summaryModel` (ou `agents.defaults.model.primary`).
  * Anexa o áudio gerado à resposta.
  * Em `mode: "final"`, ainda envia TTS somente com áudio para respostas finais transmitidas por streaming depois que o stream de texto é concluído; a mídia gerada passa pela mesma normalização de mídia do canal que anexos normais de resposta.


Se a resposta exceder `maxLength` e o resumo estiver desativado (ou não houver chave de API para o modelo de resumo), o áudio será ignorado e a resposta de texto normal será enviada.

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## Formatos de saída por canal

Destino | Formato  
---|---  
Feishu / Matrix / Telegram / WhatsApp | Respostas em nota de voz preferem **Opus** (`opus_48000_64` da ElevenLabs, `opus` da OpenAI). 48 kHz / 64 kbps equilibram clareza e tamanho.  
Outros canais | **MP3** (`mp3_44100_128` da ElevenLabs, `mp3` da OpenAI). 44,1 kHz / 128 kbps padrão para fala.  
Talk / telefonia | **PCM** nativo do provedor (Inworld 22050 Hz, Google 24 kHz), ou `ulaw_8000` da Gradium para telefonia.  
  
Observações por provedor:

  * **Transcoding do Feishu / WhatsApp:** quando uma resposta em nota de voz chega como MP3/WebM/WAV/M4A, o Plugin de canal transcodifica para Ogg/Opus em 48 kHz com `ffmpeg`. O WhatsApp envia pelo Baileys com `ptt: true` e `audio/ogg; codecs=opus`. Se a conversão falhar: o Feishu recorre a anexar o arquivo original; o envio pelo WhatsApp falha em vez de publicar um payload PTT incompatível.
  * **MiniMax / Xiaomi MiMo:** MP3 padrão (32 kHz para MiniMax `speech-2.8-hd`); transcodificado para Opus em 48 kHz para destinos de nota de voz via `ffmpeg`.
  * **CLI local:** usa o `outputFormat` configurado. Destinos de nota de voz são convertidos para Ogg/Opus, e a saída de telefonia para PCM mono bruto de 16 kHz.
  * **Google Gemini:** retorna PCM bruto de 24 kHz. O OpenClaw encapsula como WAV para anexos, transcodifica para Opus em 48 kHz para destinos de nota de voz e retorna PCM diretamente para Talk/telefonia.
  * **Inworld:** anexos MP3, nota de voz `OGG_OPUS` nativa, `PCM` bruto a 22050 Hz para Talk/telefonia.
  * **xAI:** MP3 por padrão; `responseFormat` pode ser `mp3|wav|pcm|mulaw|alaw`. Usa o endpoint REST em lote da xAI — TTS por WebSocket de streaming **não** é usado. O formato nativo Opus para nota de voz **não** é compatível.
  * **Microsoft:** usa `microsoft.outputFormat` (padrão `audio-24khz-48kbitrate-mono-mp3`). O `sendVoice` do Telegram aceita OGG/MP3/M4A; use OpenAI/ElevenLabs se precisar de mensagens de voz Opus garantidas. Se o formato Microsoft configurado falhar, o OpenClaw tenta novamente com MP3.


Os formatos de saída da OpenAI e da ElevenLabs são fixos por canal conforme listado acima.

## Referência de campos

messages.tts.* de nível superior

Modo Auto-TTS. `inbound` só envia áudio depois de uma mensagem de voz de entrada; `tagged` só envia áudio quando a resposta inclui diretivas `[[tts:...]]` ou um bloco `[[tts:text]]`.

Alternância legada. `openclaw doctor --fix` migra isto para `auto`.

`"all"` inclui respostas de ferramenta/bloco além das respostas finais.

ID do provedor de fala. Quando não definido, o OpenClaw usa o primeiro provedor configurado na ordem de seleção automática do registro. `provider: "edge"` legado é reescrito para `"microsoft"` por `openclaw doctor --fix`.

ID da persona ativa em `personas`. Normalizado para minúsculas.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> Identidade falada estável. Campos: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`. Veja Personas.

Modelo barato para resumo automático; o padrão é `agents.defaults.model.primary`. Aceita `provider/model` ou um alias de modelo configurado.

Permite que o modelo emita diretivas TTS. `enabled` usa `true` por padrão; `allowProvider` usa `false` por padrão.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> Configurações pertencentes ao provedor, indexadas por ID do provedor de fala. Blocos diretos legados (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) são reescritos por `openclaw doctor --fix`; faça commit apenas de `messages.tts.providers.<id>`.

Limite rígido para caracteres de entrada de TTS. `/tts audio` falha se for excedido.

Tempo limite da requisição em milissegundos.

Sobrescreve o caminho JSON de preferências locais (provedor/limite/resumo). Padrão `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` ou `SPEECH_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Região do Azure Speech (por exemplo, `eastus`). Env: `AZURE_SPEECH_REGION` ou `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci Sobrescrita opcional do endpoint do Azure Speech (alias `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ShortName da voz do Azure. Padrão `en-US-JennyNeural`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Código de idioma SSML. Padrão `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg `X-Microsoft-OutputFormat` do Azure para áudio padrão. Padrão `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg `X-Microsoft-OutputFormat` do Azure para saída de nota de voz. Padrão `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Recorre a `ELEVENLABS_API_KEY` ou `XI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci ID do modelo (por exemplo, `eleven_multilingual_v2`, `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (cada um `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = normal).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg ISO 639-1 de 2 letras (por exemplo, `en`, `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI Inteiro `0..4294967295` para determinismo em regime de melhor esforço. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Recorre a `GEMINI_API_KEY` / `GOOGLE_API_KEY`. Se omitido, TTS pode reutilizar `models.providers.google.apiKey` antes do fallback de env. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Modelo TTS do Gemini. Padrão `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg Nome de voz pré-criada do Gemini. Padrão `Kore`. Alias: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn Defina como `audio-profile-v1` para encapsular campos de prompt da persona ativa em uma estrutura determinística de prompt TTS do Gemini. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Apenas `https://generativelanguage.googleapis.com` é aceito. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Padrão `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Padrão Emma (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Inworld principal

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Padrão `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI Padrão `inworld-tts-1.5-max`. Também: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Padrão `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi Temperatura de amostragem `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

CLI local (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg Argumentos do comando. Compatível com placeholders `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic Formato de saída esperado da CLI. Padrão `mp3` para anexos de áudio. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Tempo limite do comando em milissegundos. Padrão `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (sem chave de API)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Nome da voz neural da Microsoft (por exemplo, `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Código de idioma (por exemplo, `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Formato de saída da Microsoft. Padrão `audio-24khz-48kbitrate-mono-mp3`. Nem todos os formatos são compatíveis com o transporte integrado baseado no Edge. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg Strings percentuais (por exemplo, `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk Alias legado. Execute `openclaw doctor --fix` para reescrever a configuração persistida para `providers.microsoft`. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Recorre a `MINIMAX_API_KEY`. Autenticação Token Plan via `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY` ou `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Padrão `https://api.minimax.io`. Env: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Padrão `speech-2.8-hd`. Env: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Padrão `English_expressive_narrator`. Env: `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. Padrão `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. Padrão `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Inteiro `-12..12`. Padrão `0`. Valores fracionários são truncados antes da solicitação. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Recorre a `OPENAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci ID do modelo TTS da OpenAI (por exemplo, `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Nome da voz (por exemplo, `alloy`, `cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg Campo `instructions` explícito da OpenAI. Quando definido, campos de prompt de persona **não** são mapeados automaticamente. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Campos JSON extras mesclados aos corpos de solicitação `/audio/speech` após os campos TTS gerados da OpenAI. Use isso para endpoints compatíveis com OpenAI, como Kokoro, que exigem chaves específicas do provedor, como `lang`; chaves de protótipo inseguras são ignoradas. OPENCLAW_DOCS_MARKER:paramClose:

Substitui o endpoint TTS da OpenAI. Ordem de resolução: configuração → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Valores não padrão são tratados como endpoints TTS compatíveis com OpenAI, portanto nomes personalizados de modelo e voz são aceitos.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `OPENROUTER_API_KEY`. Pode reutilizar `models.providers.openrouter.apiKey`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Padrão `https://openrouter.ai/api/v1`. O legado `https://openrouter.ai/v1` é normalizado. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Padrão `hexgrad/kokoro-82m`. Alias: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Padrão `af_alloy`. Alias: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw Padrão `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `VOLCENGINE_TTS_API_KEY` ou `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI Padrão `seed-tts-1.0`. Env: `VOLCENGINE_TTS_RESOURCE_ID`. Use `seed-tts-2.0` quando seu projeto tiver direito de uso do TTS 2.0. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg Cabeçalho de chave do aplicativo. Padrão `aGjiRDfUWi`. Env: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Substitui o endpoint HTTP TTS do Seed Speech. Env: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Tipo de voz. Padrão `en_female_anna_mars_bigtts`. Env: `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ Campos legados do Volcengine Speech Console. Env: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (padrão `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Padrão `https://api.x.ai/v1`. Env: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Padrão `eve`. Vozes ativas: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci Código de idioma BCP-47 ou `auto`. Padrão `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw Padrão `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Padrão `https://api.xiaomimimo.com/v1`. Env: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Padrão `mimo-v2.5-tts`. Env: `XIAOMI_TTS_MODEL`. Também é compatível com `mimo-v2-tts`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Padrão `mimo_default`. Env: `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic Padrão `mp3`. Env: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## Ferramenta do agente

A ferramenta `tts` converte texto em fala e retorna um anexo de áudio para entrega da resposta. No Feishu, Matrix, Telegram e WhatsApp, o áudio é entregue como mensagem de voz, em vez de anexo de arquivo. Feishu e WhatsApp podem transcodificar a saída TTS que não seja Opus nesse caminho quando `ffmpeg` está disponível.

O WhatsApp envia áudio por meio do Baileys como uma nota de voz PTT (`audio` com `ptt: true`) e envia texto visível **separadamente** do áudio PTT porque os clientes nem sempre renderizam legendas em notas de voz.

A ferramenta aceita os campos opcionais `channel` e `timeoutMs`; `timeoutMs` é um tempo limite de solicitação do provedor por chamada, em milissegundos.

## RPC do Gateway

Método | Finalidade  
---|---  
`tts.status` | Ler o estado TTS atual e a última tentativa.  
`tts.enable` | Definir a preferência automática local como `always`.  
`tts.disable` | Definir a preferência automática local como `off`.  
`tts.convert` | Conversão avulsa de texto → áudio.  
`tts.setProvider` | Definir a preferência local de provedor.  
`tts.setPersona` | Definir a preferência local de persona.  
`tts.providers` | Listar provedores configurados e status.  
  
## Links de serviço

  * [Guia de texto para fala da OpenAI](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [Referência da API de áudio da OpenAI](<https://platform.openai.com/docs/api-reference/audio>)
  * [Texto para fala REST do Azure Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Provedor Azure Speech](</pt-BR/providers/azure-speech>)
  * [Texto para fala da ElevenLabs](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [Autenticação da ElevenLabs](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</pt-BR/providers/gradium>)
  * [API TTS da Inworld](<https://docs.inworld.ai/tts/tts>)
  * [API MiniMax T2A v2](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [API HTTP TTS da Volcengine](</pt-BR/providers/volcengine#text-to-speech>)
  * [Síntese de fala do Xiaomi MiMo](</pt-BR/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Formatos de saída do Microsoft Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [Texto para fala da xAI](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## Relacionado

  * [Visão geral de mídia](</pt-BR/tools/media-overview>)
  * [Geração de música](</pt-BR/tools/music-generation>)
  * [Geração de vídeo](</pt-BR/tools/video-generation>)
  * [Comandos de barra](</pt-BR/tools/slash-commands>)
  * [Plugin de chamada de voz](</pt-BR/plugins/voice-call>)


Was this useful?YesNo