---
title: Cuadro de evaluación de madurez
source_url: https://docs.openclaw.ai/es/maturity/scorecard
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Cuadro de puntuación de madurez

preparación para el lanzamiento - generado a partir de la taxonomía + evidencia de QA

Una vista práctica de lo que está listo, lo que está probado y lo que aún necesita trabajo.

50 superficies - 281 áreas de capacidad - cobertura determinista más calidad e integridad revisadas por humanos.

Explorar superficies / Inspeccionar evidencia de QA / [Leer la taxonomía](</es/maturity/taxonomy>)

## Para qué sirve esta página

Usa esta página para responder una pregunta: ¿qué superficies de OpenClaw son opciones creíbles para un lanzamiento y qué evidencia respalda ese juicio? La cobertura proviene de evidencia determinista de QA; la calidad y la integridad se mantienen como puntuaciones de madurez revisadas.

## De un vistazo

67% Puntuación de madurez

Alfa Calidad + integridad Cobertura Experimental - 4% Calidad Alfa - 63% Integridad Beta - 70%

La cobertura se guía deliberadamente por la evidencia: un área no pasa a estar "lista" solo porque la implementación exista. No es una entrada para la puntuación de madurez, pero OpenClaw busca mantener con el tiempo la cobertura de extremo a extremo por encima del 90% para funciones maduras de nivel Estable o superior.

## Bandas de puntuación

Experimental0-50%

Alfa50-70%

Beta70-80%

Estable80-95%

Clawesome95-100%

## Explorador de superficies

Las superficies se ordenan por nivel de madurez, integridad y calidad. El soporte LTS se muestra junto a cada fila para que las opciones listas para lanzamiento sean fáciles de comparar.

### Todas las superficies

[CLIM4Estable7 áreas](</es/maturity/taxonomy#cli>)

CoberturaExperimental4%

CalidadEstable83%

CompletitudEstable90%

Parcial - 6

[Entorno de ejecución de GatewayM4Estable13 áreas](</es/maturity/taxonomy#gateway-runtime>)

CoberturaExperimental6%

CalidadEstable81%

CompletitudEstable89%

Parcial - 12

[Host de Gateway en LinuxM4Estable5 áreas](</es/maturity/taxonomy#linux-gateway-host>)

CoberturaExperimental0%

CalidadBeta75%

CompletitudEstable89%

Parcial - 4

[Host de Gateway en macOSM4Estable7 áreas](</es/maturity/taxonomy#macos-gateway-host>)

CoberturaExperimental0%

CalidadBeta74%

CompletitudEstable88%

Ninguno

[DiscordM4Estable6 áreas](</es/maturity/taxonomy#discord>)

CoberturaExperimental0%

CalidadBeta73%

CompletitudEstable87%

Parcial - 4

[Entorno de ejecución de agenteM3Beta9 áreas](</es/maturity/taxonomy#agent-runtime>)

CoberturaExperimental33%

CalidadBeta78%

CompletitudBeta79%

Parcial - 6

[Motor de sesión, memoria y contextoM3Beta9 áreas](</es/maturity/taxonomy#session-memory-and-context-engine>)

CoberturaExperimental30%

CalidadBeta77%

IntegridadBeta79%

Parcial - 6

[Marco de canalesM3Beta8 áreas](</es/maturity/taxonomy#channel-framework>)

CoberturaExperimental13%

CalidadBeta76%

IntegridadBeta79%

Parcial - 5

[Herramientas de automatización del navegador, exec y sandboxM3Beta3 áreas](</es/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CoberturaExperimental21%

CalidadBeta75%

IntegridadBeta79%

Parcial - 2

[ObservabilidadM3Beta5 áreas](</es/maturity/taxonomy#observability>)

CoberturaExperimental18%

CalidadBeta75%

IntegridadBeta79%

Parcial - 3

[Ruta de proveedor de OpenAI y CodexM3Beta5 áreas](</es/maturity/taxonomy#openai-and-codex-provider-path>)

CoberturaExperimental26%

CalidadBeta74%

IntegridadBeta79%

Parcial - 3

[Aplicación web de GatewayM3Beta6 áreas](</es/maturity/taxonomy#gateway-web-app>)

CoberturaExperimental4%

CalidadBeta74%

IntegridadBeta79%

Ninguno

[Herramientas de búsqueda webM3Beta4 áreas](</es/maturity/taxonomy#web-search-tools>)

CoberturaExperimental9%

CalidadBeta74%

CompletitudBeta79%

Ninguno

[PluginsM3Beta9 áreas](</es/maturity/taxonomy#plugins>)

CoberturaExperimental12%

CalidadBeta72%

CompletitudBeta79%

Parcial - 7

[Seguridad, autenticación, emparejamiento y secretosM3Beta6 áreas](</es/maturity/taxonomy#security-auth-pairing-and-secrets>)

CoberturaExperimental16%

CalidadBeta72%

CompletitudBeta79%

Parcial - 5

[Automatización: cron, hooks, tareas, sondeoM3Beta6 áreas](</es/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CoberturaExperimental2%

CalidadBeta72%

CompletitudBeta79%

Ninguno

[Alojamiento de Docker y PodmanM3Beta4 áreas](</es/maturity/taxonomy#docker-and-podman-hosting>)

CoberturaExperimental7%

CalidadBeta71%

CompletitudBeta79%

Ninguno

[Windows mediante WSL2M3Beta6 áreas](</es/maturity/taxonomy#windows-via-wsl2>)

CoberturaExperimental6%

CalidadAlpha69%

CompletitudBeta79%

Parcial - 5

[Raspberry Pi y dispositivos Linux pequeñosM3Beta4 áreas](</es/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CoberturaExperimental0%

CalidadAlfa67%

CompletitudBeta79%

Ninguno

[Ruta del proveedor AnthropicM3Beta5 áreas](</es/maturity/taxonomy#anthropic-provider-path>)

CoberturaExperimental0%

CalidadBeta71%

CompletitudBeta78%

Ninguno

[TelegramM3Beta5 áreas](</es/maturity/taxonomy#telegram>)

CoberturaExperimental0%

CalidadAlfa68%

CompletitudBeta78%

Completo - 5

[SlackM3Beta5 áreas](</es/maturity/taxonomy#slack>)

CoberturaExperimental0%

CalidadAlfa66%

CompletitudBeta78%

Completo - 5

[Ruta del proveedor GoogleM3Beta5 áreas](</es/maturity/taxonomy#google-provider-path>)

CoberturaExperimental0%

CalidadAlfa66%

CompletitudBeta78%

Ninguno

[iMessage y BlueBubblesM3Beta5 áreas](</es/maturity/taxonomy#imessage-and-bluebubbles>)

CoberturaExperimental0%

CalidadAlfa66%

CompletitudBeta78%

Ninguno

[App complementaria de macOSM3Beta8 áreas](</es/maturity/taxonomy#macos-companion-app>)

CoberturaExperimental0%

CalidadAlfa66%

CompletitudBeta78%

Ninguno

[Ruta del proveedor OpenRouterM3Beta4 áreas](</es/maturity/taxonomy#openrouter-provider-path>)

CoberturaExperimental0%

CalidadAlfa66%

CompletitudBeta78%

Ninguno

[WhatsAppM3Beta5 áreas](</es/maturity/taxonomy#whatsapp>)

CoberturaExperimental0%

CalidadAlfa66%

CompletitudBeta78%

Ninguno

[Comprensión de medios y generación de mediosM2Alfa6 áreas](</es/maturity/taxonomy#media-understanding-and-media-generation>)

CoberturaExperimental2%

CalidadAlfa64%

CompletitudAlfa68%

Ninguno

[Herramientas de generación de imágenes, video y músicaM2Alfa5 áreas](</es/maturity/taxonomy#image-video-and-music-generation-tools>)

CoberturaExperimental0%

CalidadAlfa61%

CompletitudAlfa68%

Ninguno

[Proveedores de modelos locales: Ollama, vLLM, SGLang, LM StudioM2Alfa5 áreas](</es/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CoberturaExperimental0%

CalidadAlfa61%

CompletitudAlfa68%

Ninguno

[Proveedores alojados de cola largaM2Alfa3 áreas](</es/maturity/taxonomy#long-tail-hosted-providers>)

CoberturaExperimental0%

CalidadAlfa61%

CompletitudAlfa68%

Ninguno

[Voz y conversación en tiempo realM2Alfa6 áreas](</es/maturity/taxonomy#voice-and-realtime-talk>)

CoberturaExperimental0%

CalidadAlfa61%

ExhaustividadAlfa68%

Ninguno

[MatrixM2Alfa6 áreas](</es/maturity/taxonomy#matrix>)

CoberturaExperimental0%

CalidadAlfa60%

ExhaustividadAlfa67%

Ninguno

[Aplicación AndroidM2Alfa7 áreas](</es/maturity/taxonomy#android-app>)

CoberturaExperimental0%

CalidadAlfa59%

ExhaustividadAlfa66%

Ninguno

[Google ChatM2Alfa5 áreas](</es/maturity/taxonomy#google-chat>)

CoberturaExperimental0%

CalidadAlfa59%

ExhaustividadAlfa66%

Ninguno

[Microsoft TeamsM2Alfa5 áreas](</es/maturity/taxonomy#microsoft-teams>)

CoberturaExperimental0%

CalidadAlfa59%

ExhaustividadAlfa66%

Ninguno

[SignalM2Alfa5 áreas](</es/maturity/taxonomy#signal>)

CoberturaExperimental0%

CalidadAlfa59%

ExhaustividadAlfa66%

Ninguno

[TUIM2Alfa5 áreas](</es/maturity/taxonomy#tui>)

CoberturaExperimental0%

CalidadAlfa59%

CompletitudAlfa66%

Ninguno

[Windows nativoM2Alfa4 áreas](</es/maturity/taxonomy#native-windows>)

CoberturaExperimental0%

CalidadAlfa58%

CompletitudAlfa66%

Parcial - 1

[ClawHubM2Alfa4 áreas](</es/maturity/taxonomy#clawhub>)

CoberturaExperimental0%

CalidadAlfa58%

CompletitudAlfa62%

Ninguno

[Alojamiento de KubernetesM2Alfa4 áreas](</es/maturity/taxonomy#kubernetes-hosting>)

CoberturaExperimental0%

CalidadAlfa55%

CompletitudAlfa61%

Ninguno

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canales regionalesM2Alfa4 áreas](</es/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CoberturaExperimental0%

CalidadAlfa55%

CompletitudAlfa58%

Ninguno

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alfa4 áreas](</es/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CoberturaExperimental0%

CalidadAlfa53%

CompletitudAlfa54%

Ninguno

[SDK de aplicaciones de OpenClawM2Alfa6 áreas](</es/maturity/taxonomy#openclaw-app-sdk>)

CoberturaExperimental3%

CalidadAlfa54%

CompletitudAlfa53%

Ninguno

[app para iOSM1Experimental8 áreas](</es/maturity/taxonomy#ios-app>)

CoberturaExperimental0%

CalidadExperimental41%

CompletitudExperimental44%

Ninguno

[ruta de instalación de NixM1Experimental5 áreas](</es/maturity/taxonomy#nix-install-path>)

CoberturaExperimental0%

CalidadExperimental41%

CompletitudExperimental44%

Ninguno

[canal de llamada de vozM1Experimental5 áreas](</es/maturity/taxonomy#voice-call-channel>)

CoberturaExperimental0%

CalidadExperimental41%

CompletitudExperimental44%

Ninguno

[superficies complementarias de watchOSM1Experimental5 áreas](</es/maturity/taxonomy#watchos-companion-surfaces>)

CoberturaExperimental0%

CalidadExperimental41%

CompletitudExperimental44%

Ninguno

[app complementaria de LinuxM0Planificado5 áreas](</es/maturity/taxonomy#linux-companion-app>)

CoberturaExperimental0%

CalidadExperimental19%

CompletitudExperimental21%

Ninguno

[app complementaria nativa de WindowsM0Planificado5 áreas](</es/maturity/taxonomy#native-windows-companion-app>)

CoberturaExperimental0%

CalidadExperimental19%

CompletitudExperimental21%

Ninguno

### Núcleo

[CLIM4Estable7 áreas](</es/maturity/taxonomy#cli>)

CoberturaExperimental4%

CalidadEstable83%

CompletitudEstable90%

Parcial - 6

[Runtime de GatewayM4Estable13 áreas](</es/maturity/taxonomy#gateway-runtime>)

CoberturaExperimental6%

CalidadEstable81%

CompletitudEstable89%

Parcial - 12

[Runtime de agenteM3Beta9 áreas](</es/maturity/taxonomy#agent-runtime>)

CoberturaExperimental33%

CalidadBeta78%

CompletitudBeta79%

Parcial - 6

[Motor de sesión, memoria y contextoM3Beta9 áreas](</es/maturity/taxonomy#session-memory-and-context-engine>)

CoberturaExperimental30%

CalidadBeta77%

CompletitudBeta79%

Parcial - 6

[Framework de canalesM3Beta8 áreas](</es/maturity/taxonomy#channel-framework>)

CoberturaExperimental13%

CalidadBeta76%

CompletitudBeta79%

Parcial - 5

[ObservabilidadM3Beta5 áreas](</es/maturity/taxonomy#observability>)

CoberturaExperimental18%

CalidadBeta75%

CompletitudBeta79%

Parcial - 3

[Aplicación web de GatewayM3Beta6 áreas](</es/maturity/taxonomy#gateway-web-app>)

CoberturaExperimental4%

CalidadBeta74%

CompletitudBeta79%

Ninguno

[PluginsM3Beta9 áreas](</es/maturity/taxonomy#plugins>)

CoberturaExperimental12%

CalidadBeta72%

CompletitudBeta79%

Parcial - 7

[Seguridad, autenticación, emparejamiento y secretosM3Beta6 áreas](</es/maturity/taxonomy#security-auth-pairing-and-secrets>)

CoberturaExperimental16%

CalidadBeta72%

CompletitudBeta79%

Parcial - 5

[Automatización: Cron, hooks, tareas, sondeoM3Beta6 áreas](</es/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CoberturaExperimental2%

CalidadBeta72%

CompletitudBeta79%

Ninguno

[Comprensión de medios y generación de mediosM2Alpha6 áreas](</es/maturity/taxonomy#media-understanding-and-media-generation>)

CoberturaExperimental2%

CalidadAlpha64%

CompletitudAlpha68%

Ninguno

[Voz y conversación en tiempo realM2Alpha6 áreas](</es/maturity/taxonomy#voice-and-realtime-talk>)

CoberturaExperimental0%

CalidadAlpha61%

CompletitudAlpha68%

Ninguno

[TUIM2Alfa5 áreas](</es/maturity/taxonomy#tui>)

CoberturaExperimental0%

CalidadAlfa59%

CompletitudAlfa66%

Ninguno

[ClawHubM2Alfa4 áreas](</es/maturity/taxonomy#clawhub>)

CoberturaExperimental0%

CalidadAlfa58%

CompletitudAlfa62%

Ninguno

[OpenClaw App SDKM2Alfa6 áreas](</es/maturity/taxonomy#openclaw-app-sdk>)

CoberturaExperimental3%

CalidadAlfa54%

CompletitudAlfa53%

Ninguno

### Plataforma

[host Gateway de LinuxM4Estable5 áreas](</es/maturity/taxonomy#linux-gateway-host>)

CoberturaExperimental0%

CalidadBeta75%

CompletitudEstable89%

Parcial - 4

[host Gateway de macOSM4Estable7 áreas](</es/maturity/taxonomy#macos-gateway-host>)

CoberturaExperimental0%

CalidadBeta74%

CompletitudEstable88%

Ninguno

[alojamiento de Docker y PodmanM3Beta4 áreas](</es/maturity/taxonomy#docker-and-podman-hosting>)

CoberturaExperimental7%

CalidadBeta71%

CompletitudBeta79%

Ninguno

[Windows mediante WSL2M3Beta6 áreas](</es/maturity/taxonomy#windows-via-wsl2>)

CoberturaExperimental6%

CalidadAlpha69%

IntegridadBeta79%

Parcial - 5

[Raspberry Pi y dispositivos Linux pequeñosM3Beta4 áreas](</es/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CoberturaExperimental0%

CalidadAlpha67%

IntegridadBeta79%

Ninguno

[aplicación complementaria de macOSM3Beta8 áreas](</es/maturity/taxonomy#macos-companion-app>)

CoberturaExperimental0%

CalidadAlpha66%

IntegridadBeta78%

Ninguno

[aplicación para AndroidM2Alpha7 áreas](</es/maturity/taxonomy#android-app>)

CoberturaExperimental0%

CalidadAlpha59%

IntegridadAlpha66%

Ninguno

[Windows nativoM2Alpha4 áreas](</es/maturity/taxonomy#native-windows>)

CoberturaExperimental0%

CalidadAlpha58%

IntegridadAlpha66%

Parcial - 1

[alojamiento en KubernetesM2Alpha4 áreas](</es/maturity/taxonomy#kubernetes-hosting>)

CoberturaExperimental0%

CalidadAlpha55%

IntegridadAlpha61%

Ninguno

[aplicación para iOSM1Experimental8 áreas](</es/maturity/taxonomy#ios-app>)

CoberturaExperimental0%

CalidadExperimental41%

IntegridadExperimental44%

Ninguno

[Ruta de instalación de NixM1Experimental5 áreas](</es/maturity/taxonomy#nix-install-path>)

CoberturaExperimental0%

CalidadExperimental41%

IntegridadExperimental44%

Ninguno

[Superficies complementarias de watchOSM1Experimental5 áreas](</es/maturity/taxonomy#watchos-companion-surfaces>)

CoberturaExperimental0%

CalidadExperimental41%

IntegridadExperimental44%

Ninguno

[Aplicación complementaria de LinuxM0Planificado5 áreas](</es/maturity/taxonomy#linux-companion-app>)

CoberturaExperimental0%

CalidadExperimental19%

IntegridadExperimental21%

Ninguno

[Aplicación complementaria nativa de WindowsM0Planificado5 áreas](</es/maturity/taxonomy#native-windows-companion-app>)

CoberturaExperimental0%

CalidadExperimental19%

IntegridadExperimental21%

Ninguno

### Canal

[DiscordM4Estable6 áreas](</es/maturity/taxonomy#discord>)

CoberturaExperimental0%

CalidadBeta73%

IntegridadEstable87%

Parcial - 4

[TelegramM3Beta5 áreas](</es/maturity/taxonomy#telegram>)

CoberturaExperimental0%

CalidadAlfa68%

IntegridadBeta78%

Completo - 5

[SlackM3Beta5 áreas](</es/maturity/taxonomy#slack>)

CoberturaExperimental0%

CalidadAlfa66%

IntegridadBeta78%

Completo - 5

[iMessage y BlueBubblesM3Beta5 áreas](</es/maturity/taxonomy#imessage-and-bluebubbles>)

CoberturaExperimental0%

CalidadAlfa66%

IntegridadBeta78%

Ninguno

[WhatsAppM3Beta5 áreas](</es/maturity/taxonomy#whatsapp>)

CoberturaExperimental0%

CalidadAlfa66%

IntegridadBeta78%

Ninguno

[MatrixM2Alfa6 áreas](</es/maturity/taxonomy#matrix>)

CoberturaExperimental0%

CalidadAlfa60%

IntegridadAlfa67%

Ninguno

[Google ChatM2Alfa5 áreas](</es/maturity/taxonomy#google-chat>)

CoberturaExperimental0%

CalidadAlfa59%

IntegridadAlfa66%

Ninguno

[Microsoft TeamsM2Alfa5 áreas](</es/maturity/taxonomy#microsoft-teams>)

CoberturaExperimental0%

CalidadAlfa59%

CompletitudAlpha66%

Ninguno

[SignalM2Alpha5 áreas](</es/maturity/taxonomy#signal>)

CoberturaExperimental0%

CalidadAlpha59%

CompletitudAlpha66%

Ninguno

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canales regionalesM2Alpha4 áreas](</es/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CoberturaExperimental0%

CalidadAlpha55%

CompletitudAlpha58%

Ninguno

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 áreas](</es/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CoberturaExperimental0%

CalidadAlpha53%

CompletitudAlpha54%

Ninguno

[Canal de llamadas de vozM1Experimental5 áreas](</es/maturity/taxonomy#voice-call-channel>)

CoberturaExperimental0%

CalidadExperimental41%

CompletitudExperimental44%

Ninguno

### Proveedor y herramienta

[Automatización del navegador, exec y herramientas de sandboxM3Beta3 áreas](</es/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CoberturaExperimental21%

CalidadBeta75%

CompletitudBeta79%

Parcial - 2

[Ruta del proveedor de OpenAI y CodexM3Beta5 áreas](</es/maturity/taxonomy#openai-and-codex-provider-path>)

CoberturaExperimental26%

CalidadBeta74%

CompletitudBeta79%

Parcial - 3

[Herramientas de búsqueda webM3Beta4 áreas](</es/maturity/taxonomy#web-search-tools>)

CoberturaExperimental9%

CalidadBeta74%

CompletitudBeta79%

Ninguno

[Ruta del proveedor AnthropicM3Beta5 áreas](</es/maturity/taxonomy#anthropic-provider-path>)

CoberturaExperimental0%

CalidadBeta71%

CompletitudBeta78%

Ninguno

[Ruta del proveedor GoogleM3Beta5 áreas](</es/maturity/taxonomy#google-provider-path>)

CoberturaExperimental0%

CalidadAlfa66%

CompletitudBeta78%

Ninguno

[Ruta del proveedor OpenRouterM3Beta4 áreas](</es/maturity/taxonomy#openrouter-provider-path>)

CoberturaExperimental0%

CalidadAlfa66%

CompletitudBeta78%

Ninguno

[Herramientas de generación de imágenes, video y músicaM2Alfa5 áreas](</es/maturity/taxonomy#image-video-and-music-generation-tools>)

CoberturaExperimental0%

CalidadAlfa61%

CompletitudAlfa68%

Ninguno

[Proveedores de modelos locales: Ollama, vLLM, SGLang, LM StudioM2Alfa5 áreas](</es/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CoberturaExperimental0%

CalidadAlfa61%

CompletitudAlfa68%

Ninguno

[Proveedores alojados de larga colaM2Alfa3 áreas](</es/maturity/taxonomy#long-tail-hosted-providers>)

CoberturaExperimental0%

CalidadAlfa61%

CompletitudAlfa68%

Ninguno

## Resumen de evidencia de QA

Las comprobaciones siguientes muestran qué áreas del cuadro de puntuación fueron ejercitadas por la evidencia del perfil de QA.

Validación completa de la taxonomía 2026-06-23T07:24:36.128Z 96 comprobaciones - 94 superadas, 2 bloqueadas 0 de 281 (0%) áreas - 20 de 1675 (1.2%) funciones - 77 de 1665 (4.6%) IDs de cobertura

### Preparación por área

Abre una superficie para inspeccionar el estado de la evidencia de cada categoría. La lista permanece contraída para que la página siga siendo útil de un vistazo.

Entorno de ejecución de agentes - 9 áreas

8 revisadas parcialmente / 1 necesita revisión

Ejecución de turnos de agente Revisado parcialmente - Validación completa de taxonomía

0 de 3 (0%) / 7 de 24 (29.2%) 17 brechas de capacidad

Entornos de ejecución externos y subagentes Revisado parcialmente - Validación completa de taxonomía

0 de 4 (0%) / 3 de 10 (30%) 7 brechas de capacidad

Ejecución de proveedores alojados Revisado parcialmente - Validación completa de taxonomía

1 de 5 (20%) / 1 de 5 (20%) 4 brechas de capacidad

Proveedores locales y autoalojados Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Selección de modelo y entorno de ejecución Revisado parcialmente - Validación completa de taxonomía

0 de 4 (0%) / 2 de 8 (25%) 6 brechas de capacidad

Autenticación de proveedor Revisado parcialmente - Validación completa de taxonomía

0 de 10 (0%) / 4 de 17 (23.5%) 13 brechas de capacidad

Transmisión en tiempo real y progreso Revisado parcialmente - Validación completa de taxonomía

0 de 2 (0%) / 5 de 9 (55.6%) 4 brechas de capacidad

Llamadas a herramientas y manejo de respuestas Revisado parcialmente - Validación completa de taxonomía

0 de 3 (0%) / 15 de 23 (65.2%) 8 brechas de capacidad

Controles de ejecución de herramientas Revisado parcialmente - Validación completa de taxonomía

0 de 6 (0%) / 6 de 12 (50%) 6 brechas de capacidad

App de Android - 7 áreas

7 necesitan revisión

Configuración de conexión Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Entorno de ejecución del dispositivo Necesita revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Distribución Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Captura multimedia Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Chat móvil Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Configuración Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Voz Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Ruta del proveedor Anthropic - 5 áreas

5 necesitan revisión

Entradas multimedia Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Selección de modelo y entorno de ejecución Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 12 (0%) 12 brechas de capacidad

Caché de prompts y contexto Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Autenticación y recuperación de proveedor Necesita revisión - Validación completa de taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Transporte de solicitudes y semántica de turnos Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Automatización: Cron, hooks, tareas, sondeo - 6 áreas

5 necesitan revisión / 1 revisada parcialmente

Hooks de automatización Necesita revisión - Validación completa de taxonomía

0 de 11 (0%) / 0 de 11 (0%) 11 brechas de capacidad

Tareas y flujos en segundo plano Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Trabajos Cron Necesita revisión - Validación completa de taxonomía

0 de 15 (0%) / 0 de 15 (0%) 15 brechas de capacidad

Entrada de eventos Necesita revisión - Validación completa de taxonomía

0 de 15 (0%) / 0 de 15 (0%) 15 brechas de capacidad

Heartbeat Revisada parcialmente - Validación completa de taxonomía

0 de 5 (0%) / 1 de 7 (14.3%) 6 brechas de capacidad

Controles de sondeo Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Automatización del navegador, exec y herramientas de sandbox - 3 áreas

2 revisadas parcialmente / 1 necesita revisión

Automatización del navegador Revisada parcialmente - Validación completa de taxonomía

1 de 8 (12.5%) / 1 de 8 (12.5%) 7 brechas de capacidad

Sandbox y política de herramientas Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Invocación y ejecución de herramientas Revisada parcialmente - Validación completa de taxonomía

2 de 6 (33.3%) / 4 de 8 (50%) 4 brechas de capacidad

Aplicación web de Gateway - 6 áreas

3 necesitan revisión / 3 revisadas parcialmente

Acceso y confianza del navegador Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Conversación en tiempo real del navegador Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Interfaz de usuario del navegador Revisada parcialmente - Validación completa de taxonomía

0 de 10 (0%) / 1 de 12 (8.3%) 11 brechas de capacidad

Configuración Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Consola de operador Revisada parcialmente - Validación completa de taxonomía

0 de 10 (0%) / 1 de 12 (8.3%) 11 brechas de capacidad

Conversaciones de WebChat Revisada parcialmente - Validación completa de taxonomía

0 de 15 (0%) / 2 de 20 (10%) 18 brechas de capacidad

Framework de canales - 8 áreas

4 necesitan revisión / 4 revisadas parcialmente

Comandos y aprobaciones de acciones de canal Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Configuración de canales Revisada parcialmente - Validación completa de taxonomía

0 de 5 (0%) / 1 de 7 (14.3%) 6 brechas de capacidad

Enrutamiento y entrega de conversaciones Revisada parcialmente - Validación completa de taxonomía

0 de 10 (0%) / 5 de 27 (18.5%) 22 brechas de capacidad

Comportamiento de hilos de grupo y salas ambientales Revisada parcialmente - Validación completa de taxonomía

0 de 5 (0%) / 4 de 11 (36.4%) 7 brechas de capacidad

Acceso entrante y controles de identidad Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Adjuntos multimedia y datos enriquecidos de canal Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Entrega saliente y canalización de respuestas Revisada parcialmente - Validación completa de taxonomía

0 de 4 (0%) / 8 de 21 (38.1%) 13 brechas de capacidad

Estado de salud y controles de operador Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 6 (0%) 6 brechas de capacidad

ClawHub - 4 áreas

4 necesitan revisión

Descubrimiento de catálogo Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Compatibilidad y confianza Necesita revisión - Validación completa de taxonomía

0 de 12 (0%) / 0 de 12 (0%) 12 brechas de capacidad

Ciclo de vida y estado del Plugin Necesita revisión - Validación completa de taxonomía

0 de 26 (0%) / 0 de 26 (0%) 26 brechas de capacidad

Publicación Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

CLI - 7 áreas

5 necesitan revisión / 2 revisadas parcialmente

Observabilidad de CLI Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Configuración de CLI Revisado parcialmente - Validación completa de taxonomía

1 de 6 (16.7%) / 1 de 6 (16.7%) 5 brechas de capacidad

Doctor Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Gestión del servicio Gateway Revisado parcialmente - Validación completa de taxonomía

0 de 5 (0%) / 1 de 7 (14.3%) 6 brechas de capacidad

Incorporación y configuración de autenticación Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Configuración de Plugin y canal Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Actualizaciones y mejoras Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Discord - 6 áreas

6 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Configuración y operaciones de canal Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de taxonomía

0 de 12 (0%) / 0 de 12 (0%) 12 brechas de capacidad

Contenido multimedia y enriquecido Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Controles nativos y aprobaciones Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Voz y llamadas en tiempo real Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Alojamiento con Docker y Podman - 4 áreas

3 necesitan revisión / 1 revisada parcialmente

Sandbox y herramientas del agente Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Operaciones de contenedores Necesita revisión - Validación completa de taxonomía

0 de 11 (0%) / 0 de 11 (0%) 11 brechas de capacidad

Configuración de contenedores Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Lanzamiento y validación de imágenes Revisado parcialmente - Validación completa de taxonomía

1 de 5 (20%) / 2 de 7 (28.6%) 5 brechas de capacidad

Feishu, bot de QQ, WeChat, Yuanbao, Zalo, Zalo Personal, canales regionales - 4 áreas

4 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de la taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Runtime de Gateway - 13 áreas

9 necesitan revisión / 4 revisadas parcialmente

Aprobaciones y ejecución remota Necesita revisión - Validación completa de la taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Autenticación y emparejamiento de dispositivos Necesita revisión - Validación completa de la taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Ciclo de vida de Gateway Revisado parcialmente - Validación completa de la taxonomía

0 de 7 (0%) / 4 de 12 (33.3%) 8 brechas de capacidad

API RPC y eventos de Gateway Revisado parcialmente - Validación completa de la taxonomía

0 de 20 (0%) / 2 de 22 (9.1%) 20 brechas de capacidad

Estado, diagnósticos y reparación Necesita revisión - Validación completa de la taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Superficie web alojada Necesita revisión - Validación completa de la taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

API HTTP Revisado parcialmente - Validación completa de la taxonomía

1 de 4 (25%) / 1 de 4 (25%) 3 brechas de capacidad

Acceso y descubrimiento de red Necesita revisión - Validación completa de la taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Nodos y capacidades remotas Necesita revisión - Validación completa de la taxonomía

0 de 8 (0%) / 0 de 8 (0%) 8 brechas de capacidad

Compatibilidad del protocolo Necesita revisión - Validación completa de la taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Roles y permisos Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Controles de seguridad Necesita revisión - Validación completa de la taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Conexión WebSocket Revisado parcialmente - Validación completa de la taxonomía

1 de 8 (12.5%) / 1 de 8 (12.5%) 7 brechas de capacidad

Google Chat - 5 áreas

5 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de la taxonomía

0 de 11 (0%) / 0 de 11 (0%) 11 brechas de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de la taxonomía

0 de 16 (0%) / 0 de 16 (0%) 16 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Controles nativos y aprobaciones Necesita revisión - Validación completa de la taxonomía

0 de 16 (0%) / 0 de 16 (0%) 16 brechas de capacidad

Ruta del proveedor Google - 5 áreas

5 necesitan revisión

Entorno de ejecución directo de Gemini Necesita revisión - Validación completa de taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Medios, búsqueda y tiempo real Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Enrutamiento de modelos y puntos de conexión Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Caché de prompts Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Configuración del proveedor y credenciales Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Herramientas de generación de imágenes, video y música - 5 áreas

5 necesitan revisión

Generación de imágenes Necesita revisión - Validación completa de taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Enrutamiento y descubrimiento de medios Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Generación de música Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Ciclo de vida y entrega de tareas Necesita revisión - Validación completa de taxonomía

0 de 12 (0%) / 0 de 12 (0%) 12 brechas de capacidad

Generación de video Necesita revisión - Validación completa de taxonomía

0 de 11 (0%) / 0 de 11 (0%) 11 brechas de capacidad

iMessage y BlueBubbles - 5 áreas

5 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de taxonomía

0 de 11 (0%) / 0 de 11 (0%) 11 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Controles y aprobaciones nativos Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Aplicación iOS - 8 áreas

8 necesitan revisión

Lienzo y pantalla Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Chat y sesiones Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Comandos del dispositivo Necesita revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Distribución Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Configuración y diagnóstico del Gateway Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Medios y uso compartido Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Notificaciones y segundo plano Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Voz Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Alojamiento en Kubernetes - 4 áreas

4 necesitan revisión

Acceso y exposición Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Ciclo de vida del clúster Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Configuración y secretos Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Configuración del despliegue Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Aplicación complementaria para Linux - 5 áreas

5 necesitan revisión

Distribución de la aplicación Necesita revisión - Validación completa de la taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Chat y sesiones Necesita revisión - Validación completa de la taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Capacidades de escritorio Necesita revisión - Validación completa de la taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Conectividad de Gateway Necesita revisión - Validación completa de la taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Estado y diagnósticos Necesita revisión - Validación completa de la taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Host de Gateway en Linux - 5 áreas

5 necesitan revisión

Destinos de despliegue Necesita revisión - Validación completa de la taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Diagnóstico y reparación Necesita revisión - Validación completa de la taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Runtime de Gateway y control del servicio Necesita revisión - Validación completa de la taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Configuración y actualizaciones del host Necesita revisión - Validación completa de la taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Acceso remoto y seguridad Necesita revisión - Validación completa de la taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Proveedores de modelos locales: Ollama, vLLM, SGLang, LM Studio - 5 áreas

5 necesitan revisión

Memoria local y embeddings Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Plugins nativos de proveedor Necesita revisión - Validación completa de la taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Seguridad de red y controles de prompts Necesita revisión - Validación completa de la taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Compatibilidad del runtime compatible con OpenAI Necesita revisión - Validación completa de la taxonomía

0 de 8 (0%) / 0 de 8 (0%) 8 brechas de capacidad

Configuración, ciclo de vida y diagnósticos del proveedor Necesita revisión - Validación completa de la taxonomía

0 de 12 (0%) / 0 de 12 (0%) 12 brechas de capacidad

Proveedores alojados de larga cola - 3 áreas

3 necesitan revisión

Proveedores de LLM alojados Necesita revisión - Validación completa de la taxonomía

0 de 12 (0%) / 0 de 12 (0%) 12 brechas de capacidad

Proveedores de medios alojados Necesita revisión - Validación completa de la taxonomía

0 de 8 (0%) / 0 de 8 (0%) 8 brechas de capacidad

Operaciones de proveedor Necesita revisión - Validación completa de la taxonomía

0 de 12 (0%) / 0 de 12 (0%) 12 brechas de capacidad

aplicación complementaria de macOS - 8 áreas

8 requieren revisión

Lienzo Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Configuración local Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Capacidades nativas Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Conexiones remotas Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

WebChat remoto Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Estado y configuración Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Voz y conversación Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

WebChat Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

host Gateway de macOS - 7 áreas

7 requieren revisión

Configuración de CLI Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Diagnóstico y observabilidad Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Ciclo de vida del servicio Gateway Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Integración con Gateway local Necesita revisión - Validación completa de taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Permisos y capacidades nativas Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Perfiles y aislamiento Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Modo Gateway remoto Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Matrix - 6 áreas

6 requieren revisión

Acceso e identidad Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Cifrado y verificación Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Controles y aprobaciones nativos Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - 4 áreas

4 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Comprensión de medios y generación de medios - 6 áreas

4 necesitan revisión / 2 parcialmente revisadas

Gestión de medios del canal Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Configuración de medios Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Generación de medios Parcialmente revisada - Validación completa de la taxonomía

1 de 17 (5.9%) / 1 de 19 (5.3%) 18 brechas de capacidad

Ingesta y acceso a medios Necesita revisión - Validación completa de la taxonomía

0 de 8 (0%) / 0 de 8 (0%) 8 brechas de capacidad

Comprensión de medios Parcialmente revisada - Validación completa de la taxonomía

0 de 12 (0%) / 1 de 14 (7.1%) 13 brechas de capacidad

Entrega de texto a voz Necesita revisión - Validación completa de la taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Microsoft Teams - 5 áreas

5 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de la taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de la taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Controles y aprobaciones nativos Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Windows nativo - 4 áreas

4 necesitan revisión

CLI Necesita revisión - Validación completa de la taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Gestión de Gateway Necesita revisión - Validación completa de la taxonomía

0 de 11 (0%) / 0 de 11 (0%) 11 brechas de capacidad

Redes Necesita revisión - Validación completa de la taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Actualizaciones Necesita revisión - Validación completa de la taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Aplicación complementaria nativa de Windows - 5 áreas

5 requieren revisión

Sesiones de chat Requiere revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Herramientas de escritorio y permisos Requiere revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Conexión de Gateway Requiere revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Instalación y actualizaciones Requiere revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Estado y reparación Requiere revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Ruta de instalación de Nix - 5 áreas

5 requieren revisión

Activación y UX de la aplicación Requiere revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Configuración y estado Requiere revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Transferencia de instalación Requiere revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Ciclo de vida de Plugin Requiere revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Entorno de ejecución del servicio y protecciones Requiere revisión - Validación completa de taxonomía

0 de 8 (0%) / 0 de 8 (0%) 8 brechas de capacidad

Ruta de proveedor de OpenAI y Codex - 5 áreas

2 requieren revisión / 3 revisadas parcialmente

Entrada de imágenes y multimodal Requiere revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Modelo y autenticación Revisado parcialmente - Validación completa de taxonomía

1 de 6 (16.7%) / 4 de 9 (44.4%) 5 brechas de capacidad

Harness nativo de Codex Revisado parcialmente - Validación completa de taxonomía

0 de 2 (0%) / 4 de 9 (44.4%) 5 brechas de capacidad

Respuestas y compatibilidad de herramientas Revisado parcialmente - Validación completa de taxonomía

1 de 4 (25%) / 2 de 5 (40%) 3 brechas de capacidad

Voz y audio en tiempo real Requiere revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

SDK de la aplicación OpenClaw - 6 áreas

5 requieren revisión / 1 revisada parcialmente

Conversaciones de agentes Requiere revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

API de cliente Requiere revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Compatibilidad Requiere revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Eventos y aprobaciones Requiere revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Acceso a Gateway Requiere revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Ayudantes de recursos Revisado parcialmente - Validación completa de taxonomía

0 de 5 (0%) / 1 de 6 (16.7%) 5 brechas de capacidad

Ruta del proveedor OpenRouter - 4 áreas

4 necesitan revisión

Runtime de chat y normalización Necesita revisión - Validación completa de taxonomía

0 de 15 (0%) / 0 de 15 (0%) 15 brechas de capacidad

Generación de medios y voz Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Recuperación y diagnóstico del proveedor Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Configuración y autenticación del proveedor Necesita revisión - Validación completa de taxonomía

0 de 14 (0%) / 0 de 14 (0%) 14 brechas de capacidad

Plugins - 9 áreas

6 necesitan revisión / 3 revisadas parcialmente

Creación y empaquetado de plugins Necesita revisión - Validación completa de taxonomía

0 de 8 (0%) / 0 de 8 (0%) 8 brechas de capacidad

Plugins incluidos Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Plugin Canvas Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Plugins de canal Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Instalación y ejecución de plugins Revisado parcialmente - Validación completa de taxonomía

0 de 6 (0%) / 7 de 20 (35%) 13 brechas de capacidad

Aprobaciones de Plugin Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Plugins de proveedor y herramientas Revisado parcialmente - Validación completa de taxonomía

1 de 6 (16.7%) / 9 de 21 (42.9%) 12 brechas de capacidad

Publicación de plugins Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Pruebas de plugins Revisado parcialmente - Validación completa de taxonomía

0 de 6 (0%) / 3 de 11 (27.3%) 8 brechas de capacidad

Raspberry Pi y dispositivos Linux pequeños - 4 áreas

4 necesitan revisión

Runtime de Gateway Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Rendimiento y diagnóstico Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Acceso remoto y autenticación Necesita revisión - Validación completa de taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Configuración y compatibilidad Necesita revisión - Validación completa de taxonomía

0 de 12 (0%) / 0 de 12 (0%) 12 brechas de capacidad

Seguridad, autenticación, emparejamiento y secretos - 6 áreas

2 revisadas parcialmente / 4 necesitan revisión

Política de aprobación y salvaguardas de herramientas Revisado parcialmente - Validación completa de taxonomía

0 de 2 (0%) / 3 de 6 (50%) 3 brechas de capacidad

Control de acceso de canales Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Higiene de credenciales y secretos Revisado parcialmente - Validación completa de taxonomía

0 de 5 (0%) / 5 de 11 (45.5%) 6 brechas de capacidad

Emparejamiento de dispositivos y Node Necesita revisión - Validación completa de taxonomía

0 de 11 (0%) / 0 de 11 (0%) 11 brechas de capacidad

Autenticación de Gateway y acceso remoto Necesita revisión - Validación completa de taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Confianza en Plugin Necesita revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Sesión, memoria y motor de contexto - 9 áreas

2 necesitan revisión / 7 revisadas parcialmente

Gestión de sesiones y transcripciones de la CLI Necesita revisión - Validación completa de la taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Motor de contexto Revisada parcialmente - Validación completa de la taxonomía

0 de 2 (0%) / 4 de 7 (57.1%) 3 brechas de capacidad

Indicaciones principales y contexto Revisada parcialmente - Validación completa de la taxonomía

0 de 2 (0%) / 3 de 8 (37.5%) 5 brechas de capacidad

Historial entre clientes y paridad de sesiones Revisada parcialmente - Validación completa de la taxonomía

0 de 2 (0%) / 2 de 5 (40%) 3 brechas de capacidad

Diagnóstico, mantenimiento y recuperación Revisada parcialmente - Validación completa de la taxonomía

0 de 3 (0%) / 4 de 10 (40%) 6 brechas de capacidad

Memoria Revisada parcialmente - Validación completa de la taxonomía

0 de 5 (0%) / 6 de 13 (46.2%) 7 brechas de capacidad

Enrutamiento de sesiones Revisada parcialmente - Validación completa de la taxonomía

0 de 2 (0%) / 1 de 4 (25%) 3 brechas de capacidad

Gestión de tokens Revisada parcialmente - Validación completa de la taxonomía

0 de 3 (0%) / 2 de 10 (20%) 8 brechas de capacidad

Persistencia de transcripciones Necesita revisión - Validación completa de la taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Signal - 5 áreas

5 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de la taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de la taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de la taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Controles y aprobaciones nativos Necesita revisión - Validación completa de la taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Slack - 5 áreas

5 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de la taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de la taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Controles y aprobaciones nativos Necesita revisión - Validación completa de la taxonomía

0 de 8 (0%) / 0 de 8 (0%) 8 brechas de capacidad

Telegram - 5 áreas

5 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de la taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de la taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de la taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Controles y aprobaciones nativos Necesita revisión - Validación completa de la taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Observabilidad - 5 áreas

3 revisadas parcialmente / 2 necesitan revisión

Recopilación de diagnósticos Revisado parcialmente - Validación completa de taxonomía

1 de 8 (12.5%) / 3 de 10 (30%) 7 brechas de capacidad

Estado y reparación Revisado parcialmente - Validación completa de taxonomía

1 de 12 (8.3%) / 5 de 18 (27.8%) 13 brechas de capacidad

Registro Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Diagnósticos de sesión Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Exportación de telemetría Revisado parcialmente - Validación completa de taxonomía

1 de 13 (7.7%) / 7 de 21 (33.3%) 14 brechas de capacidad

TUI - 5 áreas

5 necesitan revisión

Entrada y comandos Necesita revisión - Validación completa de taxonomía

0 de 8 (0%) / 0 de 8 (0%) 8 brechas de capacidad

Ejecución de shell local Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Renderizado y seguridad de la salida Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Modos de ejecución Necesita revisión - Validación completa de taxonomía

0 de 14 (0%) / 0 de 14 (0%) 14 brechas de capacidad

Gestión de sesiones Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Voz y conversación en tiempo real - 6 áreas

6 necesitan revisión

Conversación en aplicación nativa Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Sesiones de conversación en tiempo real Necesita revisión - Validación completa de taxonomía

0 de 11 (0%) / 0 de 11 (0%) 11 brechas de capacidad

Voz y transcripción Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Observabilidad de conversaciones Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Proveedores de conversación Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Activación por voz y enrutamiento Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Canal de llamadas de voz - 5 áreas

5 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de taxonomía

0 de 1 (0%) / 0 de 1 (0%) 1 brecha de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Voz y llamadas en tiempo real Necesita revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

superficies complementarias de watchOS - 5 áreas

5 necesitan revisión

Entrega y recuperación Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Distribución y soporte Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

Aprobaciones ejecutivas Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Notificaciones y respuestas Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Interfaz de usuario de la app Watch Necesita revisión - Validación completa de taxonomía

0 de 3 (0%) / 0 de 3 (0%) 3 brechas de capacidad

Herramientas de búsqueda web - 4 áreas

2 necesitan revisión / 2 revisadas parcialmente

Seguridad de red Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Proveedores de búsqueda Revisado parcialmente - Validación completa de taxonomía

2 de 19 (10.5%) / 2 de 19 (10.5%) 17 brechas de capacidad

Configuración y diagnósticos Necesita revisión - Validación completa de taxonomía

0 de 9 (0%) / 0 de 9 (0%) 9 brechas de capacidad

Disponibilidad y obtención de herramientas Revisado parcialmente - Validación completa de taxonomía

2 de 11 (18.2%) / 3 de 12 (25%) 9 brechas de capacidad

WhatsApp - 5 áreas

5 necesitan revisión

Acceso e identidad Necesita revisión - Validación completa de taxonomía

0 de 7 (0%) / 0 de 7 (0%) 7 brechas de capacidad

Configuración y operaciones del canal Necesita revisión - Validación completa de taxonomía

0 de 5 (0%) / 0 de 5 (0%) 5 brechas de capacidad

Enrutamiento y entrega de conversaciones Necesita revisión - Validación completa de taxonomía

0 de 4 (0%) / 0 de 4 (0%) 4 brechas de capacidad

Medios y contenido enriquecido Necesita revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Controles y aprobaciones nativos Necesita revisión - Validación completa de taxonomía

0 de 2 (0%) / 0 de 2 (0%) 2 brechas de capacidad

Windows mediante WSL2 - 6 áreas

5 necesitan revisión / 1 revisada parcialmente

Navegador e interfaz de usuario de control Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

CLI Necesita revisión - Validación completa de taxonomía

0 de 8 (0%) / 0 de 8 (0%) 8 brechas de capacidad

Diagnóstico y reparación Revisado parcialmente - Validación completa de taxonomía

1 de 6 (16.7%) / 3 de 8 (37.5%) 5 brechas de capacidad

Acceso y exposición del Gateway Necesita revisión - Validación completa de taxonomía

0 de 11 (0%) / 0 de 11 (0%) 11 brechas de capacidad

Ciclo de vida del servicio Gateway Necesita revisión - Validación completa de taxonomía

0 de 10 (0%) / 0 de 10 (0%) 10 brechas de capacidad

Configuración de WSL Necesita revisión - Validación completa de taxonomía

0 de 6 (0%) / 0 de 6 (0%) 6 brechas de capacidad

> Última actualización: 2026-06-22

Was this useful?YesNo

Open issue