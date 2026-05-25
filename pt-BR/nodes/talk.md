---
title: Modo de conversa
source_url: https://docs.openclaw.ai/pt-BR/nodes/talk
scraped_at: 2026-05-25
---

O modo Talk tem duas formas de runtime:

  * O Talk nativo do macOS/iOS/Android usa reconhecimento de fala local, chat do Gateway e TTS `talk.speak`. Os nós anunciam a capacidade `talk` e declaram os comandos `talk.*` compatíveis.
  * O Talk no navegador usa `talk.client.create` para sessões `webrtc` e `provider-websocket` pertencentes ao cliente, ou `talk.session.create` para sessões `gateway-relay` pertencentes ao Gateway. `managed-room` é reservado para transferência do Gateway e salas de walkie-talkie.
  * Clientes somente de transcrição usam `talk.session.create({ mode: "transcription", transport: "gateway-relay", brain: "none" })`, depois `talk.session.appendAudio`, `talk.session.cancelTurn` e `talk.session.close` quando precisam de legendas ou ditado sem uma resposta de voz do assistente.


O Talk nativo é um ciclo contínuo de conversa por voz:

  1. Ouvir fala
  2. Enviar a transcrição ao modelo por meio da sessão ativa
  3. Aguardar a resposta
  4. Reproduzi-la pelo provedor de Talk configurado (`talk.speak`)


O Talk em tempo real no navegador encaminha chamadas de ferramentas do provedor por `talk.client.toolCall`; clientes de navegador não chamam `chat.send` diretamente para consultas em tempo real.

O Talk somente de transcrição emite o mesmo envelope comum de eventos do Talk que sessões em tempo real e STT/TTS, mas usa `mode: "transcription"` e `brain: "none"`. Ele é destinado a legendas, ditado e captura de fala somente para observação; notas de voz enviadas avulsamente ainda usam o caminho de mídia/áudio.

## Comportamento (macOS)

  * **Sobreposição sempre ativa** enquanto o modo Talk estiver ativado.
  * Transições de fase **Ouvindo → Pensando → Falando**.
  * Em uma **pausa curta** (janela de silêncio), a transcrição atual é enviada.
  * As respostas são **escritas no WebChat** (igual a digitar).
  * **Interromper ao falar** (ativado por padrão): se o usuário começar a falar enquanto o assistente estiver falando, interrompemos a reprodução e registramos o timestamp da interrupção para o próximo prompt.


## Diretivas de voz nas respostas

O assistente pode prefixar sua resposta com uma **única linha JSON** para controlar a voz:

jsonCopy code
[code]
    { "voice": "<voice-id>", "once": true }
[/code]

Regras:

  * Apenas a primeira linha não vazia.
  * Chaves desconhecidas são ignoradas.
  * `once: true` aplica-se somente à resposta atual.
  * Sem `once`, a voz se torna o novo padrão do modo Talk.
  * A linha JSON é removida antes da reprodução TTS.


Chaves compatíveis:

  * `voice` / `voice_id` / `voiceId`
  * `model` / `model_id` / `modelId`
  * `speed`, `rate` (WPM), `stability`, `similarity`, `style`, `speakerBoost`
  * `seed`, `normalize`, `lang`, `output_format`, `latency_tier`
  * `once`


## Configuração (`~/.openclaw/openclaw.json`)

json5Copy code
[code]
    {  talk: {    provider: "elevenlabs",    providers: {      elevenlabs: {        voiceId: "elevenlabs_voice_id",        modelId: "eleven_v3",        outputFormat: "mp3_44100_128",        apiKey: "elevenlabs_api_key",      },      mlx: {        modelId: "mlx-community/Soprano-80M-bf16",      },      system: {},    },    speechLocale: "ru-RU",    silenceTimeoutMs: 1500,    interruptOnSpeech: true,    realtime: {      provider: "openai",      providers: {        openai: {          apiKey: "openai_api_key",          model: "gpt-realtime-2",          voice: "cedar",        },      },      instructions: "Speak warmly and keep answers brief.",      mode: "realtime",      transport: "webrtc",      brain: "agent-consult",    },  },}
[/code]

Padrões:

  * `interruptOnSpeech`: true
  * `silenceTimeoutMs`: quando não definido, o Talk mantém a janela de pausa padrão da plataforma antes de enviar a transcrição (`700 ms no macOS e Android, 900 ms no iOS`)
  * `provider`: seleciona o provedor de Talk ativo. Use `elevenlabs`, `mlx` ou `system` para os caminhos de reprodução locais do macOS.
  * `providers.<provider>.voiceId`: faz fallback para `ELEVENLABS_VOICE_ID` / `SAG_VOICE_ID` para ElevenLabs (ou para a primeira voz do ElevenLabs quando a chave de API está disponível).
  * `providers.elevenlabs.modelId`: usa `eleven_v3` por padrão quando não definido.
  * `providers.mlx.modelId`: usa `mlx-community/Soprano-80M-bf16` por padrão quando não definido.
  * `providers.elevenlabs.apiKey`: faz fallback para `ELEVENLABS_API_KEY` (ou para o perfil de shell do Gateway, se disponível).
  * `consultThinkingLevel`: substituição opcional do nível de raciocínio para a execução completa do agente OpenClaw por trás de chamadas `openclaw_agent_consult` em tempo real.
  * `consultFastMode`: substituição opcional do modo rápido para chamadas `openclaw_agent_consult` em tempo real.
  * `realtime.provider`: seleciona o provedor ativo de voz em tempo real para navegador/servidor. Use `openai` para WebRTC, `google` para WebSocket do provedor, ou um provedor somente de ponte por meio do relay do Gateway.
  * `realtime.providers.<provider>` armazena a configuração em tempo real pertencente ao provedor. O navegador recebe apenas credenciais de sessão efêmeras ou restritas, nunca uma chave de API padrão.
  * `realtime.providers.openai.voice`: id de voz integrado do OpenAI Realtime. As vozes atuais de `gpt-realtime-2` são `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`, `marin` e `cedar`; `marin` e `cedar` são recomendadas para a melhor qualidade.
  * `realtime.brain`: `agent-consult` roteia chamadas de ferramentas em tempo real pela política do Gateway; `direct-tools` é um comportamento de compatibilidade exclusivo do proprietário; `none` é para transcrição ou orquestração externa.
  * `realtime.instructions`: acrescenta instruções de sistema voltadas ao provedor ao prompt em tempo real integrado do OpenClaw. Use para estilo e tom de voz; o OpenClaw mantém a orientação padrão de `openclaw_agent_consult`.
  * `talk.catalog` expõe os modos, transportes, estratégias de brain, formatos de áudio em tempo real e flags de capacidade válidos de cada provedor para que clientes Talk próprios evitem combinações incompatíveis.
  * Provedores de transcrição por streaming são descobertos por `talk.catalog.transcription`. O relay atual do Gateway usa a configuração do provedor de streaming de Voice Call até que a superfície dedicada de configuração de transcrição do Talk seja adicionada.
  * `speechLocale`: id de localidade BCP 47 opcional para reconhecimento de fala do Talk no dispositivo em iOS/macOS. Deixe sem definir para usar o padrão do dispositivo.
  * `outputFormat`: usa `pcm_44100` por padrão no macOS/iOS e `pcm_24000` no Android (defina `mp3_*` para forçar streaming MP3)


## UI do macOS

  * Alternância na barra de menus: **Talk**
  * Aba de configuração: grupo **Talk Mode** (id de voz + alternância de interrupção)
  * Sobreposição: 
    * **Ouvindo** : a nuvem pulsa com o nível do microfone
    * **Pensando** : animação afundando
    * **Falando** : anéis radiantes
    * Clicar na nuvem: parar de falar
    * Clicar no X: sair do modo Talk


## UI do Android

  * Alternância na aba de voz: **Talk**
  * **Mic** manual e **Talk** são modos de captura em runtime mutuamente exclusivos.
  * O Mic manual para quando o app sai do primeiro plano ou o usuário sai da aba de voz.
  * O modo Talk continua em execução até ser desativado ou até o nó Android desconectar, e usa o tipo de serviço em primeiro plano de microfone do Android enquanto está ativo.


## Observações

  * Requer permissões de Fala + Microfone.
  * O Talk nativo usa a sessão ativa do Gateway e só faz fallback para sondagem de histórico quando eventos de resposta não estão disponíveis.
  * O Talk em tempo real no navegador usa `talk.client.toolCall` para `openclaw_agent_consult` em vez de expor `chat.send` a sessões de navegador pertencentes ao provedor.
  * O Talk somente de transcrição usa `talk.session.create`, `talk.session.appendAudio`, `talk.session.cancelTurn` e `talk.session.close`; clientes assinam `talk.event` para atualizações parciais/finais da transcrição.
  * O gateway resolve a reprodução do Talk por `talk.speak` usando o provedor de Talk ativo. O Android faz fallback para TTS local do sistema somente quando esse RPC está indisponível.
  * A reprodução local MLX no macOS usa o helper `openclaw-mlx-tts` incluído quando presente, ou um executável no `PATH`. Defina `OPENCLAW_MLX_TTS_BIN` para apontar para um binário helper personalizado durante o desenvolvimento.
  * `stability` para `eleven_v3` é validado como `0.0`, `0.5` ou `1.0`; outros modelos aceitam `0..1`.
  * `latency_tier` é validado como `0..4` quando definido.
  * O Android oferece suporte aos formatos de saída `pcm_16000`, `pcm_22050`, `pcm_24000` e `pcm_44100` para streaming AudioTrack de baixa latência.


## Relacionado

  * [Ativação por voz](</pt-BR/nodes/voicewake>)
  * [Áudio e notas de voz](</pt-BR/nodes/audio>)
  * [Compreensão de mídia](</pt-BR/nodes/media-understanding>)


Was this useful?YesNo