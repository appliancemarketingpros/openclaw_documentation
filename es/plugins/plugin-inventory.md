---
title: Inventario de Plugin
source_url: https://docs.openclaw.ai/es/plugins/plugin-inventory
scraped_at: 2026-05-25
---

# Inventario de Plugin

Esta página se genera a partir de `extensions/*/package.json`, `openclaw.plugin.json` y las exclusiones de `files` del paquete npm raíz. Regénérala con:

bashCopy code
[code]
    pnpm plugins:inventory:gen
[/code]

## Definiciones

  * **Paquete npm principal:** integrado en el paquete npm `openclaw` y disponible sin instalar un plugin por separado.
  * **Paquete externo oficial:** plugin mantenido por OpenClaw omitido del paquete npm principal, conservado en este inventario oficial e instalado bajo demanda mediante ClawHub y/o npm.
  * **Solo checkout del código fuente:** plugin local del repositorio omitido de los artefactos npm publicados y no anunciado como paquete instalable.


Los checkouts del código fuente son diferentes de las instalaciones de npm: después de `pnpm install`, los plugins incluidos se cargan desde `extensions/<id>`, por lo que las ediciones locales y las dependencias del workspace locales del paquete están disponibles.

## Instalar un plugin

Usa la columna **Distribución** para decidir si hace falta instalar. Los plugins que indican `included in OpenClaw` ya están presentes en el paquete principal. Los paquetes externos oficiales necesitan una instalación y luego un reinicio del Gateway.

Por ejemplo, Discord es un paquete externo oficial:

bashCopy code
[code]
    openclaw plugins install @openclaw/discordopenclaw gateway restartopenclaw plugins inspect discord --runtime --json
[/code]

Las especificaciones de paquete simples prueban primero ClawHub y luego recurren a npm. Para forzar una fuente, usa `clawhub:@openclaw/discord` o `npm:@openclaw/discord`. Después de instalar, sigue la documentación de configuración del plugin, como [Discord](</es/channels/discord>), para agregar credenciales y configuración del canal. Consulta [Administrar plugins](</es/plugins/manage-plugins>) para ver comandos de actualización, desinstalación y publicación.

## Paquete npm principal

Plugin | Descripción | Distribución | Superficie  
---|---|---|---  
[alibaba](</es/plugins/reference/alibaba>) | Agrega soporte para proveedores de generación de video. | `@openclaw/alibaba-provider` |   
incluido en OpenClaw | contracts: videoGenerationProviders |  |   
[amazon-bedrock](</es/plugins/reference/amazon-bedrock>) | Agrega soporte para el proveedor de modelos Amazon Bedrock a OpenClaw. | `@openclaw/amazon-bedrock-provider` |   
incluido en OpenClaw | providers: amazon-bedrock; contracts: memoryEmbeddingProviders |  |   
[amazon-bedrock-mantle](</es/plugins/reference/amazon-bedrock-mantle>) | Agrega soporte para el proveedor de modelos Amazon Bedrock Mantle a OpenClaw. | `@openclaw/amazon-bedrock-mantle-provider` |   
incluido en OpenClaw | providers: amazon-bedrock-mantle |  |   
[anthropic](</es/plugins/reference/anthropic>) | Agrega soporte para el proveedor de modelos Anthropic a OpenClaw. | `@openclaw/anthropic-provider` |   
incluido en OpenClaw | providers: anthropic; contracts: mediaUnderstandingProviders |  |   
[anthropic-vertex](</es/plugins/reference/anthropic-vertex>) | Agrega soporte para el proveedor de modelos Anthropic Vertex a OpenClaw. | `@openclaw/anthropic-vertex-provider` |   
incluido en OpenClaw | providers: anthropic-vertex |  |   
[arcee](</es/plugins/reference/arcee>) | Agrega soporte para el proveedor de modelos Arcee a OpenClaw. | `@openclaw/arcee-provider` |   
incluido en OpenClaw | providers: arcee |  |   
[azure-speech](</es/plugins/reference/azure-speech>) | Texto a voz de Azure AI Speech (MP3, notas de voz nativas Ogg/Opus, telefonía PCM). | `@openclaw/azure-speech` |   
incluido en OpenClaw | contracts: speechProviders |  |   
[bonjour](</es/plugins/reference/bonjour>) | Anuncia el gateway local de OpenClaw mediante Bonjour/mDNS. | `@openclaw/bonjour` |   
incluido en OpenClaw | plugin |  |   
[browser](</es/plugins/reference/browser>) | Agrega herramientas invocables por agentes. | `@openclaw/browser-plugin` |   
incluido en OpenClaw | contracts: tools; skills |  |   
[byteplus](</es/plugins/reference/byteplus>) | Agrega soporte para los proveedores de modelos BytePlus y BytePlus Plan a OpenClaw. | `@openclaw/byteplus-provider` |   
incluido en OpenClaw | providers: byteplus, byteplus-plan; contracts: videoGenerationProviders |  |   
[canvas](</es/plugins/reference/canvas>) | Superficies experimentales de control de Canvas y renderizado A2UI para nodos emparejados. | `@openclaw/canvas-plugin` |   
incluido en OpenClaw | contracts: tools |  |   
[cerebras](</es/plugins/reference/cerebras>) | Agrega soporte para el proveedor de modelos Cerebras a OpenClaw. | `@openclaw/cerebras-provider` |   
incluido en OpenClaw | providers: cerebras |  |   
[chutes](</es/plugins/reference/chutes>) | Agrega soporte para el proveedor de modelos Chutes a OpenClaw. | `@openclaw/chutes-provider` |   
incluido en OpenClaw | providers: chutes |  |   
[clickclack](</es/plugins/reference/clickclack>) | Agrega la superficie del canal Clickclack para enviar y recibir mensajes de OpenClaw. | `@openclaw/clickclack` |   
incluido en OpenClaw | channels: clickclack |  |   
[cloudflare-ai-gateway](</es/plugins/reference/cloudflare-ai-gateway>) | Agrega soporte para el proveedor de modelos Cloudflare AI Gateway a OpenClaw. | `@openclaw/cloudflare-ai-gateway-provider` |   
incluido en OpenClaw | providers: cloudflare-ai-gateway |  |   
[comfy](</es/plugins/reference/comfy>) | Agrega soporte para el proveedor de modelos ComfyUI a OpenClaw. | `@openclaw/comfy-provider` |   
incluido en OpenClaw | providers: comfy; contracts: imageGenerationProviders, musicGenerationProviders, videoGenerationProviders |  |   
[copilot-proxy](</es/plugins/reference/copilot-proxy>) | Agrega soporte para el proveedor de modelos Copilot Proxy a OpenClaw. | `@openclaw/copilot-proxy` |   
incluido en OpenClaw | providers: copilot-proxy |  |   
[deepgram](</es/plugins/reference/deepgram>) | Agrega soporte para proveedores de comprensión de medios. Agrega soporte para proveedores de transcripción en tiempo real. | `@openclaw/deepgram-provider` |   
incluido en OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders |  |   
[deepinfra](</es/plugins/reference/deepinfra>) | Agrega soporte para el proveedor de modelos DeepInfra a OpenClaw. | `@openclaw/deepinfra-provider` |   
incluido en OpenClaw | providers: deepinfra; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, speechProviders, videoGenerationProviders |  |   
[deepseek](</es/plugins/reference/deepseek>) | Agrega compatibilidad con el proveedor de modelos DeepSeek a OpenClaw. | `@openclaw/deepseek-provider` |   
incluido en OpenClaw | providers: deepseek |  |   
[document-extract](</es/plugins/reference/document-extract>) | Extrae texto e imágenes alternativas de páginas de adjuntos de documentos locales. | `@openclaw/document-extract-plugin` |   
incluido en OpenClaw | contracts: documentExtractors |  |   
[duckduckgo](</es/plugins/reference/duckduckgo>) | Agrega compatibilidad con proveedores de búsqueda web. | `@openclaw/duckduckgo-plugin` |   
incluido en OpenClaw | contracts: webSearchProviders |  |   
[elevenlabs](</es/plugins/reference/elevenlabs>) | Agrega compatibilidad con proveedores de comprensión de medios. Agrega compatibilidad con proveedores de transcripción en tiempo real. Agrega compatibilidad con proveedores de texto a voz. | `@openclaw/elevenlabs-speech` |   
incluido en OpenClaw | contracts: mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders |  |   
[exa](</es/plugins/reference/exa>) | Agrega compatibilidad con proveedores de búsqueda web. | `@openclaw/exa-plugin` |   
incluido en OpenClaw | contracts: webSearchProviders |  |   
[fal](</es/plugins/reference/fal>) | Agrega compatibilidad con el proveedor de modelos fal a OpenClaw. | `@openclaw/fal-provider` |   
incluido en OpenClaw | providers: fal; contracts: imageGenerationProviders, videoGenerationProviders |  |   
[file-transfer](</es/plugins/reference/file-transfer>) | Obtiene, lista y escribe archivos en nodos emparejados mediante comandos de nodo dedicados. Evita el truncamiento de stdout de bash usando base64 sobre node.invoke para binarios de hasta 16 MB. | `@openclaw/file-transfer` |   
incluido en OpenClaw | contracts: tools |  |   
[firecrawl](</es/plugins/reference/firecrawl>) | Agrega herramientas invocables por agentes. Agrega compatibilidad con proveedores de obtención web. Agrega compatibilidad con proveedores de búsqueda web. | `@openclaw/firecrawl-plugin` |   
incluido en OpenClaw | contracts: tools, webFetchProviders, webSearchProviders |  |   
[fireworks](</es/plugins/reference/fireworks>) | Agrega compatibilidad con el proveedor de modelos Fireworks a OpenClaw. | `@openclaw/fireworks-provider` |   
incluido en OpenClaw | providers: fireworks |  |   
[github-copilot](</es/plugins/reference/github-copilot>) | Agrega compatibilidad con el proveedor de modelos GitHub Copilot a OpenClaw. | `@openclaw/github-copilot-provider` |   
incluido en OpenClaw | providers: github-copilot; contracts: memoryEmbeddingProviders |  |   
[google](</es/plugins/reference/google>) | Agrega compatibilidad con los proveedores de modelos Google, Google Gemini CLI y Google Vertex a OpenClaw. | `@openclaw/google-plugin` |   
incluido en OpenClaw | providers: google, google-gemini-cli, google-vertex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, musicGenerationProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[gradium](</es/plugins/reference/gradium>) | Agrega compatibilidad con proveedores de texto a voz. | `@openclaw/gradium-speech` |   
incluido en OpenClaw | contracts: speechProviders |  |   
[groq](</es/plugins/reference/groq>) | Agrega compatibilidad con el proveedor de modelos Groq a OpenClaw. | `@openclaw/groq-provider` |   
incluido en OpenClaw | providers: groq; contracts: mediaUnderstandingProviders |  |   
[huggingface](</es/plugins/reference/huggingface>) | Agrega compatibilidad con el proveedor de modelos Hugging Face a OpenClaw. | `@openclaw/huggingface-provider` |   
incluido en OpenClaw | providers: huggingface |  |   
[imessage](</es/plugins/reference/imessage>) | Agrega la superficie de canal de iMessage para enviar y recibir mensajes de OpenClaw. | `@openclaw/imessage` |   
incluido en OpenClaw | channels: imessage |  |   
[inworld](</es/plugins/reference/inworld>) | Texto a voz en streaming de Inworld (MP3, OGG_OPUS, PCM telefónico). | `@openclaw/inworld-speech` |   
incluido en OpenClaw | contracts: speechProviders |  |   
[irc](</es/plugins/reference/irc>) | Agrega la superficie de canal de IRC para enviar y recibir mensajes de OpenClaw. | `@openclaw/irc` |   
incluido en OpenClaw | channels: irc |  |   
[kilocode](</es/plugins/reference/kilocode>) | Agrega compatibilidad con el proveedor de modelos Kilocode a OpenClaw. | `@openclaw/kilocode-provider` |   
incluido en OpenClaw | providers: kilocode |  |   
[kimi](</es/plugins/reference/kimi>) | Agrega compatibilidad con los proveedores de modelos Kimi y Kimi Coding a OpenClaw. | `@openclaw/kimi-provider` |   
incluido en OpenClaw | providers: kimi, kimi-coding |  |   
[litellm](</es/plugins/reference/litellm>) | Agrega compatibilidad con el proveedor de modelos LiteLLM a OpenClaw. | `@openclaw/litellm-provider` |   
incluido en OpenClaw | providers: litellm; contracts: imageGenerationProviders |  |   
[llm-task](</es/plugins/reference/llm-task>) | Herramienta LLM genérica solo JSON para tareas estructuradas invocable desde flujos de trabajo. | `@openclaw/llm-task` |   
incluido en OpenClaw | contracts: tools |  |   
[lmstudio](</es/plugins/reference/lmstudio>) | Añade soporte de proveedor de modelos de LM Studio a OpenClaw. | `@openclaw/lmstudio-provider` |   
incluido en OpenClaw | providers: lmstudio; contracts: memoryEmbeddingProviders |  |   
[mattermost](</es/plugins/reference/mattermost>) | Añade la superficie de canal de Mattermost para enviar y recibir mensajes de OpenClaw. | `@openclaw/mattermost` |   
incluido en OpenClaw | channels: mattermost |  |   
[memory-core](</es/plugins/reference/memory-core>) | Añade soporte de proveedor de embeddings de memoria. Añade herramientas invocables por agentes. | `@openclaw/memory-core` |   
incluido en OpenClaw | contracts: memoryEmbeddingProviders, tools |  |   
[memory-wiki](</es/plugins/reference/memory-wiki>) | Compilador de wiki persistente y bóveda de conocimiento compatible con Obsidian para OpenClaw. | `@openclaw/memory-wiki` |   
incluido en OpenClaw | contracts: tools; skills |  |   
[microsoft](</es/plugins/reference/microsoft>) | Añade soporte de proveedor de texto a voz. | `@openclaw/microsoft-speech` |   
incluido en OpenClaw | contracts: speechProviders |  |   
[microsoft-foundry](</es/plugins/reference/microsoft-foundry>) | Añade soporte de proveedor de modelos de Microsoft Foundry a OpenClaw. | `@openclaw/microsoft-foundry` |   
incluido en OpenClaw | providers: microsoft-foundry |  |   
[migrate-claude](</es/plugins/reference/migrate-claude>) | Importa instrucciones de Claude Code y Claude Desktop, servidores MCP, Skills y configuración segura a OpenClaw. | `@openclaw/migrate-claude` |   
incluido en OpenClaw | contracts: migrationProviders |  |   
[migrate-hermes](</es/plugins/reference/migrate-hermes>) | Importa configuración, memorias, Skills y credenciales compatibles de Hermes a OpenClaw. | `@openclaw/migrate-hermes` |   
incluido en OpenClaw | contracts: migrationProviders |  |   
[minimax](</es/plugins/reference/minimax>) | Añade soporte de proveedor de modelos de MiniMax y MiniMax Portal a OpenClaw. | `@openclaw/minimax-provider` |   
incluido en OpenClaw | providers: minimax, minimax-portal; contracts: imageGenerationProviders, mediaUnderstandingProviders, musicGenerationProviders, speechProviders, videoGenerationProviders, webSearchProviders |  |   
[mistral](</es/plugins/reference/mistral>) | Añade soporte de proveedor de modelos de Mistral a OpenClaw. | `@openclaw/mistral-provider` |   
incluido en OpenClaw | providers: mistral; contracts: mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders |  |   
[moonshot](</es/plugins/reference/moonshot>) | Añade soporte de proveedor de modelos de Moonshot a OpenClaw. | `@openclaw/moonshot-provider` |   
incluido en OpenClaw | providers: moonshot; contracts: mediaUnderstandingProviders, webSearchProviders |  |   
[nvidia](</es/plugins/reference/nvidia>) | Añade soporte de proveedor de modelos de NVIDIA a OpenClaw. | `@openclaw/nvidia-provider` |   
incluido en OpenClaw | providers: nvidia |  |   
[oc-path](</es/plugins/reference/oc-path>) | Añade la CLI de rutas de openclaw para direccionamiento de archivos de espacio de trabajo `oc://`. | `@openclaw/oc-path` |   
incluido en OpenClaw | plugin |  |   
[ollama](</es/plugins/reference/ollama>) | Añade soporte de proveedor de modelos de Ollama a OpenClaw. | `@openclaw/ollama-provider` |   
incluido en OpenClaw | providers: ollama; contracts: memoryEmbeddingProviders, webSearchProviders |  |   
[open-prose](</es/plugins/reference/open-prose>) | Paquete de Skills de OpenProse VM con un comando de barra diagonal /prose. | `@openclaw/open-prose` |   
incluido en OpenClaw | skills |  |   
[openai](</es/plugins/reference/openai>) | Añade soporte de proveedor de modelos de OpenAI y OpenAI Codex a OpenClaw. | `@openclaw/openai-provider` |   
incluido en OpenClaw | providers: openai, openai-codex; contracts: imageGenerationProviders, mediaUnderstandingProviders, memoryEmbeddingProviders, realtimeTranscriptionProviders, realtimeVoiceProviders, speechProviders, videoGenerationProviders |  |   
[opencode](</es/plugins/reference/opencode>) | Añade soporte de proveedor de modelos de OpenCode a OpenClaw. | `@openclaw/opencode-provider` |   
incluido en OpenClaw | providers: opencode; contracts: mediaUnderstandingProviders |  |   
[opencode-go](</es/plugins/reference/opencode-go>) | Añade soporte de proveedor de modelos de OpenCode Go a OpenClaw. | `@openclaw/opencode-go-provider` |   
incluido en OpenClaw | providers: opencode-go; contracts: mediaUnderstandingProviders |  |   
[openrouter](</es/plugins/reference/openrouter>) | Añade soporte de proveedor de modelos de OpenRouter a OpenClaw. | `@openclaw/openrouter-provider` |   
incluido en OpenClaw | providers: openrouter; contracts: imageGenerationProviders, mediaUnderstandingProviders, speechProviders, videoGenerationProviders |  |   
[openshell](</es/plugins/reference/openshell>) | Backend de sandbox impulsado por OpenShell con espacios de trabajo locales replicados y ejecución de comandos basada en SSH. | `@openclaw/openshell-sandbox` |   
incluido en OpenClaw | plugin |  |   
[perplexity](</es/plugins/reference/perplexity>) | Añade soporte de proveedor de búsqueda web. | `@openclaw/perplexity-plugin` |   
incluido en OpenClaw | contracts: webSearchProviders |  |   
[qianfan](</es/plugins/reference/qianfan>) | Añade compatibilidad con el proveedor de modelos Qianfan a OpenClaw. | `@openclaw/qianfan-provider` |   
incluido en OpenClaw | providers: qianfan |  |   
[qwen](</es/plugins/reference/qwen>) | Añade compatibilidad con los proveedores de modelos Qwen, Qwen Cloud, Model Studio y DashScope a OpenClaw. | `@openclaw/qwen-provider` |   
incluido en OpenClaw | providers: qwen, qwencloud, modelstudio, dashscope; contracts: mediaUnderstandingProviders, videoGenerationProviders |  |   
[runway](</es/plugins/reference/runway>) | Añade compatibilidad con proveedores de generación de video. | `@openclaw/runway-provider` |   
incluido en OpenClaw | contracts: videoGenerationProviders |  |   
[searxng](</es/plugins/reference/searxng>) | Añade compatibilidad con proveedores de búsqueda web. | `@openclaw/searxng-plugin` |   
incluido en OpenClaw | contracts: webSearchProviders |  |   
[senseaudio](</es/plugins/reference/senseaudio>) | Añade compatibilidad con proveedores de comprensión de medios. | `@openclaw/senseaudio-provider` |   
incluido en OpenClaw | contracts: mediaUnderstandingProviders |  |   
[sglang](</es/plugins/reference/sglang>) | Añade compatibilidad con el proveedor de modelos SGLang a OpenClaw. | `@openclaw/sglang-provider` |   
incluido en OpenClaw | providers: sglang |  |   
[signal](</es/plugins/reference/signal>) | Añade la superficie de canal de Signal para enviar y recibir mensajes de OpenClaw. | `@openclaw/signal` |   
incluido en OpenClaw | channels: signal |  |   
[skill-workshop](</es/plugins/reference/skill-workshop>) | Captura flujos de trabajo repetibles como Skills del espacio de trabajo, con revisión pendiente, escrituras seguras y actualización del prompt de Skill. | `@openclaw/skill-workshop` |   
incluido en OpenClaw | contracts: tools |  |   
[slack](</es/plugins/reference/slack>) | Añade la superficie de canal de Slack para enviar y recibir mensajes de OpenClaw. | `@openclaw/slack` |   
incluido en OpenClaw | channels: slack |  |   
[stepfun](</es/plugins/reference/stepfun>) | Añade compatibilidad con los proveedores de modelos StepFun y StepFun Plan a OpenClaw. | `@openclaw/stepfun-provider` |   
incluido en OpenClaw | providers: stepfun, stepfun-plan |  |   
[synthetic](</es/plugins/reference/synthetic>) | Añade compatibilidad con el proveedor de modelos Synthetic a OpenClaw. | `@openclaw/synthetic-provider` |   
incluido en OpenClaw | providers: synthetic |  |   
[tavily](</es/plugins/reference/tavily>) | Añade herramientas invocables por agentes. Añade compatibilidad con proveedores de búsqueda web. | `@openclaw/tavily-plugin` |   
incluido en OpenClaw | contracts: tools, webSearchProviders; skills |  |   
[telegram](</es/plugins/reference/telegram>) | Añade la superficie de canal de Telegram para enviar y recibir mensajes de OpenClaw. | `@openclaw/telegram` |   
incluido en OpenClaw | channels: telegram |  |   
[tencent](</es/plugins/reference/tencent>) | Añade compatibilidad con el proveedor de modelos Tencent TokenHub a OpenClaw. | `@openclaw/tencent-provider` |   
incluido en OpenClaw | providers: tencent-tokenhub |  |   
[together](</es/plugins/reference/together>) | Añade compatibilidad con el proveedor de modelos Together a OpenClaw. | `@openclaw/together-provider` |   
incluido en OpenClaw | providers: together; contracts: videoGenerationProviders |  |   
[tokenjuice](</es/plugins/reference/tokenjuice>) | Compacta los resultados de las herramientas exec y bash con reductores de tokenjuice. | `@openclaw/tokenjuice` |   
incluido en OpenClaw | contracts: agentToolResultMiddleware |  |   
[tts-local-cli](</es/plugins/reference/tts-local-cli>) | Añade compatibilidad con proveedores de texto a voz. | `@openclaw/tts-local-cli` |   
incluido en OpenClaw | contracts: speechProviders |  |   
[venice](</es/plugins/reference/venice>) | Añade compatibilidad con el proveedor de modelos Venice a OpenClaw. | `@openclaw/venice-provider` |   
incluido en OpenClaw | providers: venice |  |   
[vercel-ai-gateway](</es/plugins/reference/vercel-ai-gateway>) | Añade compatibilidad con el proveedor de modelos Vercel AI Gateway a OpenClaw. | `@openclaw/vercel-ai-gateway-provider` |   
incluido en OpenClaw | providers: vercel-ai-gateway |  |   
[vllm](</es/plugins/reference/vllm>) | Añade compatibilidad con el proveedor de modelos vLLM a OpenClaw. | `@openclaw/vllm-provider` |   
incluido en OpenClaw | providers: vllm |  |   
[volcengine](</es/plugins/reference/volcengine>) | Añade compatibilidad con los proveedores de modelos Volcengine y Volcengine Plan a OpenClaw. | `@openclaw/volcengine-provider` |   
incluido en OpenClaw | providers: volcengine, volcengine-plan; contracts: speechProviders |  |   
[voyage](</es/plugins/reference/voyage>) | Añade compatibilidad con proveedores de embeddings de memoria. | `@openclaw/voyage-provider` |   
incluido en OpenClaw | contracts: memoryEmbeddingProviders |  |   
[vydra](</es/plugins/reference/vydra>) | Añade compatibilidad con el proveedor de modelos Vydra a OpenClaw. | `@openclaw/vydra-provider` |   
incluido en OpenClaw | providers: vydra; contracts: imageGenerationProviders, speechProviders, videoGenerationProviders |  |   
[web-readability](</es/plugins/reference/web-readability>) | Extrae contenido de artículos legible de respuestas de obtención web HTML locales. | `@openclaw/web-readability-plugin` |   
incluido en OpenClaw | contracts: webContentExtractors |  |   
[webhooks](</es/plugins/reference/webhooks>) | Webhooks entrantes autenticados que vinculan la automatización externa con TaskFlows de OpenClaw. | `@openclaw/webhooks` |   
incluido en OpenClaw | plugin |  |   
[xai](</es/plugins/reference/xai>) | Añade compatibilidad con el proveedor de modelos xAI a OpenClaw. | `@openclaw/xai-plugin` |   
incluido en OpenClaw | providers: xai; contracts: imageGenerationProviders, mediaUnderstandingProviders, realtimeTranscriptionProviders, speechProviders, tools, videoGenerationProviders, webSearchProviders |  |   
[xiaomi](</es/plugins/reference/xiaomi>) | Añade compatibilidad con el proveedor de modelos Xiaomi a OpenClaw. | `@openclaw/xiaomi-provider` |   
incluido en OpenClaw | providers: xiaomi; contracts: speechProviders |  |   
[zai](</es/plugins/reference/zai>) | Añade compatibilidad con el proveedor de modelos [Z.AI](<http://Z.AI>) a OpenClaw. | `@openclaw/zai-provider` |   
incluido en OpenClaw | providers: zai; contracts: mediaUnderstandingProviders |  |   
  
## Paquetes externos oficiales

Plugin | Descripción | Distribución | Superficie  
---|---|---|---  
[acpx](</es/plugins/reference/acpx>) | Backend de tiempo de ejecución ACP integrado con gestión de sesión y transporte propia del Plugin. | `@openclaw/acpx` |   
npm; ClawHub | skills |  |   
[brave](</es/plugins/reference/brave>) | Añade compatibilidad con proveedores de búsqueda web. | `@openclaw/brave-plugin` |   
npm; ClawHub | contracts: webSearchProviders |  |   
[codex](</es/plugins/reference/codex>) | Arnés de app-server de Codex y catálogo de modelos GPT gestionado por Codex. | `@openclaw/codex` |   
npm; ClawHub | providers: codex; contracts: mediaUnderstandingProviders, migrationProviders |  |   
[diagnostics-otel](</es/plugins/reference/diagnostics-otel>) | Exportador OpenTelemetry de diagnósticos de OpenClaw. | `@openclaw/diagnostics-otel` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-otel` | plugin |  |   
[diagnostics-prometheus](</es/plugins/reference/diagnostics-prometheus>) | Exportador Prometheus de diagnósticos de OpenClaw. | `@openclaw/diagnostics-prometheus` |   
npm; ClawHub: `clawhub:@openclaw/diagnostics-prometheus` | plugin |  |   
[diffs](</es/plugins/reference/diffs>) | Visor de diffs de solo lectura y renderizador de archivos para agentes. | `@openclaw/diffs` |   
npm; ClawHub | contracts: tools; skills |  |   
[discord](</es/plugins/reference/discord>) | Añade la superficie de canal de Discord para enviar y recibir mensajes de OpenClaw. | `@openclaw/discord` |   
npm; ClawHub | channels: discord |  |   
[feishu](</es/plugins/reference/feishu>) | Añade la superficie de canal de Feishu para enviar y recibir mensajes de OpenClaw. | `@openclaw/feishu` |   
npm; ClawHub | channels: feishu; contracts: tools; skills |  |   
[google-meet](</es/plugins/reference/google-meet>) | Únete a llamadas de Google Meet mediante transportes de Chrome o Twilio. | `@openclaw/google-meet` |   
npm; ClawHub | contracts: tools |  |   
[googlechat](</es/plugins/reference/googlechat>) | Añade la superficie de canal de Google Chat para enviar y recibir mensajes de OpenClaw. | `@openclaw/googlechat` |   
npm; ClawHub | channels: googlechat |  |   
[line](</es/plugins/reference/line>) | Añade la superficie de canal de LINE para enviar y recibir mensajes de OpenClaw. | `@openclaw/line` |   
npm; ClawHub | channels: line |  |   
[lobster](</es/plugins/reference/lobster>) | Herramienta de flujo de trabajo tipada con aprobaciones reanudables. | `@openclaw/lobster` |   
npm; ClawHub | contracts: tools |  |   
[matrix](</es/plugins/reference/matrix>) | Añade la superficie de canal de Matrix para enviar y recibir mensajes de OpenClaw. | `@openclaw/matrix` |   
ClawHub: `clawhub:@openclaw/matrix`; npm | channels: matrix |  |   
[memory-lancedb](</es/plugins/reference/memory-lancedb>) | Añade herramientas invocables por agentes. | `@openclaw/memory-lancedb` |   
npm; ClawHub | contracts: tools |  |   
[msteams](</es/plugins/reference/msteams>) | Añade la superficie de canal de Microsoft Teams para enviar y recibir mensajes de OpenClaw. | `@openclaw/msteams` |   
npm; ClawHub | channels: msteams |  |   
[nextcloud-talk](</es/plugins/reference/nextcloud-talk>) | Añade la superficie de canal de Nextcloud Talk para enviar y recibir mensajes de OpenClaw. | `@openclaw/nextcloud-talk` |   
npm; ClawHub | channels: nextcloud-talk |  |   
[nostr](</es/plugins/reference/nostr>) | Añade la superficie de canal de Nostr para enviar y recibir mensajes de OpenClaw. | `@openclaw/nostr` |   
npm; ClawHub | channels: nostr |  |   
[qqbot](</es/plugins/reference/qqbot>) | Añade la superficie de canal de QQ Bot para enviar y recibir mensajes de OpenClaw. | `@openclaw/qqbot` |   
npm; ClawHub | channels: qqbot; contracts: tools; skills |  |   
[synology-chat](</es/plugins/reference/synology-chat>) | Añade la superficie de canal de Synology Chat para enviar y recibir mensajes de OpenClaw. | `@openclaw/synology-chat` |   
npm; ClawHub | channels: synology-chat |  |   
[tlon](</es/plugins/reference/tlon>) | Añade la superficie de canal de Tlon para enviar y recibir mensajes de OpenClaw. | `@openclaw/tlon` |   
npm; ClawHub | channels: tlon; contracts: tools; skills |  |   
[twitch](</es/plugins/reference/twitch>) | Añade la superficie de canal de Twitch para enviar y recibir mensajes de OpenClaw. | `@openclaw/twitch` |   
npm; ClawHub | channels: twitch |  |   
[voice-call](</es/plugins/reference/voice-call>) | Añade herramientas invocables por agentes. | `@openclaw/voice-call` |   
npm; ClawHub | contracts: tools |  |   
[whatsapp](</es/plugins/reference/whatsapp>) | Añade la superficie de canal de WhatsApp para enviar y recibir mensajes de OpenClaw. | `@openclaw/whatsapp` |   
npm; ClawHub | channels: whatsapp |  |   
[zalo](</es/plugins/reference/zalo>) | Añade la superficie de canal de Zalo para enviar y recibir mensajes de OpenClaw. | `@openclaw/zalo` |   
npm; ClawHub | channels: zalo |  |   
[zalouser](</es/plugins/reference/zalouser>) | Añade la superficie de canal de Zalo Personal para enviar y recibir mensajes de OpenClaw. | `@openclaw/zalouser` |   
npm; ClawHub | channels: zalouser; contracts: tools |  |   
  
## Solo checkout de código fuente

Plugin | Descripción | Distribución | Superficie  
---|---|---|---  
[qa-channel](</es/plugins/reference/qa-channel>) | Añade la superficie de canal de QA Channel para enviar y recibir mensajes de OpenClaw. | `@openclaw/qa-channel` |   
solo checkout de código fuente | channels: qa-channel |  |   
[qa-lab](</es/plugins/reference/qa-lab>) | Plugin de laboratorio de QA de OpenClaw con interfaz de depurador privada y ejecutor de escenarios. | `@openclaw/qa-lab` |   
solo checkout de código fuente | plugin |  |   
[qa-matrix](</es/plugins/reference/qa-matrix>) | Ejecutor y sustrato de transporte de QA de Matrix. | `@openclaw/qa-matrix` |   
solo checkout de código fuente | plugin |  |   
  
Was this useful?YesNo