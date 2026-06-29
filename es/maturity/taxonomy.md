---
title: Taxonomía de madurez
source_url: https://docs.openclaw.ai/es/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Taxonomía de madurez

el modelo detrás del cuadro de puntuación

Superficies > categorías > capacidades > evidencia.

50 superficies agrupadas en 4 familias, con cada categoría vinculada a la documentación canónica y a los ID de cobertura de QA.

Explorar áreas del producto / Abrir taxonomía detallada / [Ver puntuaciones](</es/maturity/scorecard>)

## Cómo leer esta página

Una superficie es un área del producto, como el entorno de ejecución de Gateway, Discord o la app de macOS. Cada superficie contiene categorías, y cada categoría contiene las comprobaciones a nivel de capacidad que cubren los escenarios de QA. Usa el cuadro de puntuación para el juicio a nivel de versión; usa esta página para inspeccionar el modelo que lo sustenta.

## Niveles de madurez

M0PlanificadoLa dirección está definida, pero no existe una ruta de usuario compatible.Promoción: existen un issue de diseño, un propietario y una superficie objetivo.

M1ExperimentalImplementado con advertencias, flags, compilaciones desde código fuente o flujos solo para mantenedores.Promoción: el mantenedor puede ejecutar el escenario desde la rama main actual.

M2AlfaLos usuarios reales pueden probarlo, pero se esperan cambios incompatibles y una UX incompleta.Promoción: configuración documentada, pruebas básicas, advertencias conocidas y al menos una prueba en un entorno real.

M3BetaExiste una ruta pública y el flujo de trabajo principal es usable con advertencias acotadas.Promoción: documentación de instalación/actualización, pruebas de regresión, runbook de soporte y prueba de escenario satisfactoria en el entorno esperado.

M4EstableRuta recomendada para usuarios normales. Los fallos se tratan como regresiones.Promoción: puerta de versión, ruta de doctor/solución de problemas, documentación amplia y pruebas repetidas en el mundo real.

M5ClawesomePulido, agradable, bien instrumentado y competitivo con el mejor flujo de trabajo comparable.Promoción: Estable más aprobación del cuadro de puntuación de usuarios entre usuarios representativos.

## Áreas del producto

### Core

CLI M4Estable7 áreas - 90% completado Entorno de ejecución de Gateway M4Estable13 áreas - 89% completado Entorno de ejecución de agentes M3Beta9 áreas - 79% completado Motor de sesión, memoria y contexto M3Beta9 áreas - 79% completado Framework de canales M3Beta8 áreas - 79% completado Observabilidad M3Beta5 áreas - 79% completado App web de Gateway M3Beta6 áreas - 79% completado Plugins M3Beta9 áreas - 79% completo Seguridad, autenticación, vinculación y secretos M3Beta6 áreas - 79% completo Automatización: cron, hooks, tareas, sondeo M3Beta6 áreas - 79% completo Comprensión de medios y generación de medios M2Alpha6 áreas - 68% completo Voz y conversación en tiempo real M2Alpha6 áreas - 68% completo TUI M2Alpha5 áreas - 66% completo ClawHub M2Alpha4 áreas - 62% completo SDK de OpenClaw App M2Alpha6 áreas - 53% completo

### Plataforma

Host de Gateway en Linux M4Estable5 áreas - 89% completo Host de Gateway en macOS M4Estable7 áreas - 88% completo Alojamiento con Docker y Podman M3Beta4 áreas - 79% completo Windows mediante WSL2 M3Beta6 áreas - 79% completo Raspberry Pi y dispositivos Linux pequeños M3Beta4 áreas - 79% completo App complementaria para macOS M3Beta8 áreas - 78% completo App para Android M2Alpha7 áreas - 66% completo Windows nativo M2Alfa4 áreas - 66% completo Alojamiento en Kubernetes M2Alfa4 áreas - 61% completo aplicación iOS M1Experimental8 áreas - 44% completo Ruta de instalación de Nix M1Experimental5 áreas - 44% completo superficies complementarias de watchOS M1Experimental5 áreas - 44% completo aplicación complementaria para Linux M0Planificado5 áreas - 21% completo aplicación complementaria nativa para Windows M0Planificado5 áreas - 21% completo

### Canal

Discord M4Estable6 áreas - 87% completo Telegram M3Beta5 áreas - 78% completo Slack M3Beta5 áreas - 78% completo iMessage y BlueBubbles M3Beta5 áreas - 78% completo WhatsApp M3Beta5 áreas - 78% completo Matrix M2Alfa6 áreas - 67% completo Google Chat M2Alfa5 áreas - 66% completo Microsoft Teams M2Alfa5 áreas - 66% completo Signal M2Alfa5 áreas - 66% completo Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canales regionales M2Alfa4 áreas - 58% completo Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alfa4 áreas - 54% completo Canal de llamadas de voz M1Experimental5 áreas - 44% completo

### Proveedor y herramienta

Herramientas de automatización del navegador, exec y sandbox M3Beta3 áreas - 79% completo Ruta de proveedor de OpenAI y Codex M3Beta5 áreas - 79% completo Herramientas de búsqueda web M3Beta4 áreas - 79% completo Ruta de proveedor de Anthropic M3Beta5 áreas - 78% completo Ruta de proveedor de Google M3Beta5 áreas - 78% completo Ruta de proveedor de OpenRouter M3Beta4 áreas - 78% completo Herramientas de generación de imágenes, video y música M2Alfa5 áreas - 68% completo Proveedores de modelos locales: Ollama, vLLM, SGLang, LM Studio M2Alfa5 áreas - 68% completo Proveedores alojados de larga cola M2Alfa3 áreas - 68% completo

## Detalles

### Núcleo

CLI - M4 Estable - 7 áreas

Las rutas normales de configuración y reparación están documentadas en la documentación de instalación, CLI y Gateway. Las rutas específicas de Windows por plataforma se controlan en las filas Windows mediante WSL2 y Windows nativo.

Cobertura Experimental - 4%Calidad Estable - 83%Completitud Estable - 90%Parcial - 6

Configuración de CLI 6 capacidades / compatible con LTS

Experimental17%

Estable89%

Estable90%

[Índice](</es/install>), [Instalador](</es/install/installer>), [Node](</es/install/node>), [Actualización](</es/install/updating>)

Incorporación y configuración de autenticación 5 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Incorporar](</es/cli/onboard>), [Configurar](</es/cli/configure>), [Descripción general de la incorporación](</es/start/onboarding-overview>)

Configuración de Plugin y canal 5 capacidades

Experimental0%

Beta75%

Estable89%

[Incorporar](</es/cli/onboard>), [Plugins](</es/cli/plugins>), [Canales](</es/cli/channels>)

Gestión del servicio Gateway 5 capacidades / compatible con LTS

Experimental14%

Estable87%

Estable90%

[Gateway](</es/cli/gateway>), [Actualización](</es/install/updating>), [Solución de problemas](</es/gateway/troubleshooting>)

Observabilidad de CLI 5 capacidades / compatible con LTS

Experimental0%

Estable89%

Estable90%

[Estado](</es/cli/status>), [Salud](</es/cli/health>), [Registros](</es/cli/logs>), [Diagnósticos](</es/gateway/diagnostics>)

Doctor 10 capacidades / compatible con LTS

Experimental0%

Estable89%

Estable90%

[Doctor](</es/cli/doctor>), [Doctor](</es/gateway/doctor>), [Secretos](</es/gateway/secrets>), [Solución de problemas](</es/gateway/troubleshooting>)

Actualizaciones y mejoras 5 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Actualización](</es/install/updating>), [Actualizar](</es/cli/update>), [Solución de problemas](</es/gateway/troubleshooting>)

Gateway runtime - M4 Stable - 13 areas

La arquitectura central, la autenticación, el emparejamiento, la documentación del protocolo, la documentación del daemon y los runbooks de CLI son amplios y actuales.

Cobertura Experimental - 6%Calidad Estable - 81%Integridad Estable - 89%Parcial - 12

Aprobaciones y ejecución remota 6 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Protocolo](</es/gateway/protocol>), [Índice](</es/gateway/security>)

APIs HTTP 4 capacidades / compatible con LTS

Experimental25%

Estable90%

Estable90%

[Índice](</es/gateway>), [API HTTP de Openai](</es/gateway/openai-http-api>), [API HTTP de Openresponses](</es/gateway/openresponses-http-api>), [API HTTP de invocación de herramientas](</es/gateway/tools-invoke-http-api>), [Hooks](</es/automation/hooks>), [Índice](</es/web>)

Superficie web alojada 4 capacidades / compatible con LTS

Experimental0%

Estable89%

Estable90%

[Índice](</es/gateway>), [Arquitectura](</es/concepts/architecture>), [IU de control](</es/web/control-ui>), [Chat web](</es/web/webchat>), [Lienzo](</es/refactor/canvas>)

APIs RPC y eventos de Gateway 20 capacidades / compatible con LTS

Experimental9%

Estable90%

Estable90%

[Protocolo](</es/gateway/protocol>), [Índice](</es/gateway>), [Arquitectura](</es/concepts/architecture>)

Autenticación y emparejamiento de dispositivos 10 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Protocolo](</es/gateway/protocol>), [Emparejamiento](</es/gateway/pairing>), [Índice](</es/gateway/security>)

Acceso a la red y descubrimiento 6 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Índice](</es/gateway>), [Descubrimiento](</es/gateway/discovery>), [Protocolo](</es/gateway/protocol>)

Nodos y capacidades remotas 8 capacidades

Experimental0%

Beta75%

Estable89%

[Protocolo](</es/gateway/protocol>), [Arquitectura](</es/concepts/architecture>), [Índice](</es/nodes>)

Estado, diagnóstico y reparación 7 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Índice](</es/gateway>), [Diagnósticos](</es/gateway/diagnostics>), [Doctor](</es/gateway/doctor>)

Compatibilidad del protocolo 7 capacidades / con soporte LTS

Experimental0%

Beta75%

Estable89%

[Protocolo](</es/gateway/protocol>), [Arquitectura](</es/concepts/architecture>), [Typebox](</es/concepts/typebox>), [Protocolo de puente](</es/gateway/bridge-protocol>)

Roles y permisos 5 capacidades / con soporte LTS

Experimental0%

Beta75%

Estable89%

[Protocolo](</es/gateway/protocol>), [Índice](</es/gateway/security>)

Ciclo de vida del Gateway 7 capacidades / con soporte LTS

Experimental33%

Estable90%

Estable90%

[Índice](</es/gateway>), [Arquitectura](</es/concepts/architecture>)

Controles de seguridad 6 capacidades / con soporte LTS

Experimental0%

Beta75%

Estable89%

[Índice](</es/gateway/security>), [Protocolo](</es/gateway/protocol>), [Descubrimiento](</es/gateway/discovery>)

Conexión WebSocket 8 capacidades / con soporte LTS

Experimental13%

Estable90%

Estable90%

[Protocolo](</es/gateway/protocol>), [Arquitectura](</es/concepts/architecture>)

Runtime del agente - M3 Beta - 9 áreas

El bucle principal, los modelos, el enrutamiento de proveedores y la transmisión de herramientas son capacidades de primer nivel, pero el comportamiento de los proveedores cambia semanalmente y requiere pruebas de escenarios en cada lanzamiento.

Cobertura experimental - 33%Calidad Beta - 78%Completitud Beta - 79%Parcial - 6

Ejecución de turnos de agente 3 capacidades / con soporte LTS

Experimental29%

Beta79%

Beta79%

[Bucle de agente](</es/concepts/agent-loop>), [Agente](</es/cli/agent>), [Entornos de ejecución de agentes](</es/concepts/agent-runtimes>)

Entornos de ejecución externos y subagentes 4 capacidades

Experimental30%

Beta79%

Beta79%

[Entornos de ejecución de agentes](</es/concepts/agent-runtimes>), [Anthropic](</es/providers/anthropic>), [Google](</es/providers/google>), [Subagentes](</es/tools/subagents>)

Ejecución con proveedores alojados 5 capacidades / con soporte LTS

Experimental20%

Beta79%

Beta79%

[Openai](</es/providers/openai>), [Anthropic](</es/providers/anthropic>), [Google](</es/providers/google>), [Modelos](</es/concepts/models>)

Proveedores locales y autoalojados 5 capacidades

Experimental0%

Alfa68%

Beta79%

[Ollama](</es/providers/ollama>), [Modelos](</es/concepts/models>), [Agente](</es/cli/agent>)

Selección de modelo y entorno de ejecución 4 capacidades / con soporte LTS

Experimental25%

Beta79%

Beta79%

[Modelos](</es/concepts/models>), [Modelos](</es/cli/models>), [Openai](</es/providers/openai>), [Entornos de ejecución de agentes](</es/concepts/agent-runtimes>)

Autenticación de proveedores 10 capacidades / con soporte LTS

Experimental24%

Beta79%

Beta79%

[Modelos](</es/concepts/models>), [Agente](</es/cli/agent>), [Modelos](</es/cli/models>), [Openai](</es/providers/openai>), [Anthropic](</es/providers/anthropic>), [Google](</es/providers/google>), [Subagentes](</es/tools/subagents>)

Transmisión y progreso 2 capacidades

Alfa56%

Beta79%

Beta79%

[Transmisión](</es/concepts/streaming>), [Bucle de agente](</es/concepts/agent-loop>)

Llamadas a herramientas y gestión de respuestas 3 capacidades / con soporte LTS

Alfa65%

Beta79%

Beta79%

[Bucle de agente](</es/concepts/agent-loop>), [Ollama](</es/providers/ollama>)

Controles de ejecución de herramientas 6 capacidades / con soporte LTS

Alfa50%

Beta79%

Beta79%

[Sandbox frente a política de herramientas frente a elevado](</es/gateway/sandbox-vs-tool-policy-vs-elevated>), [Bucle de agente](</es/concepts/agent-loop>), [Subagentes](</es/tools/subagents>)

Sesión, memoria y motor de contexto - M3 Beta - 9 áreas

Documentación sólida e implementación activa. La madurez depende de la durabilidad de la transcripción, la calidad de Compaction y la paridad entre clientes.

Cobertura Experimental - 30%Calidad Beta - 77%Completitud Beta - 79%Parcial - 6

Gestión de sesiones y transcripciones de CLI 2 capacidades / compatible con LTS

Experimental0%

Alfa68%

Beta79%

[Sesión](</es/concepts/session>), [Compaction de gestión de sesiones](</es/reference/session-management-compaction>), [Sesiones](</es/cli/sessions>)

Gestión de tokens 3 capacidades / compatible con LTS

Experimental20%

Beta79%

Beta79%

[Compaction](</es/concepts/compaction>), [Contexto](</es/concepts/context>), [Compaction de gestión de sesiones](</es/reference/session-management-compaction>)

Motor de contexto 2 capacidades / compatible con LTS

Alfa57%

Beta79%

Beta79%

[Contexto](</es/concepts/context>), [Motor de contexto](</es/concepts/context-engine>), [Arnés del motor de contexto de Codex](</es/plan/codex-context-engine-harness>)

Paridad de historial y sesiones entre clientes 2 capacidades

Experimental40%

Beta79%

Beta79%

[Chat web](</es/web/webchat>), [Android](</es/platforms/android>), [Enrutamiento de canales](</es/channels/channel-routing>)

Diagnóstico, mantenimiento y recuperación 3 capacidades

Experimental40%

Beta79%

Beta79%

[Diagnóstico](</es/gateway/diagnostics>), [Compaction de gestión de sesiones](</es/reference/session-management-compaction>), [Indicadores](</es/diagnostics/flags>)

Prompts y contexto principales 2 capacidades / compatible con LTS

Experimental38%

Beta79%

Beta79%

[Contexto](</es/concepts/context>), [Higiene de transcripciones](</es/reference/transcript-hygiene>), [Discord](</es/channels/discord>)

Memoria 5 capacidades

Experimental46%

Beta79%

Beta79%

[Configuración de memoria](</es/reference/memory-config>), [Qmd de memoria](</es/concepts/memory-qmd>), [Memoria](</es/concepts/memory>), [Discord](</es/channels/discord>)

Enrutamiento de sesiones 2 capacidades / compatible con LTS

Experimental25%

Beta79%

Beta79%

[Sesión](</es/concepts/session>), [Enrutamiento de canales](</es/channels/channel-routing>), [Discord](</es/channels/discord>)

Persistencia de transcripciones 2 capacidades / con soporte LTS

Experimental0%

Alpha68%

Beta79%

[Compaction de gestión de sesiones](</es/reference/session-management-compaction>), [Higiene de transcripciones](</es/reference/transcript-hygiene>)

Marco de canales - M3 Beta - 8 áreas

Muchos canales comparten los contratos de entrega y enrutamiento de Gateway, pero el comportamiento del canal varía según la API de origen y las restricciones de políticas de cuenta.

Cobertura Experimental - 13%Calidad Beta - 76%Completitud Beta - 79%Parcial - 5

Acciones, comandos y aprobaciones de canales 5 capacidades

Experimental0%

Beta79%

Beta79%

[Grupos](</es/channels/groups>), [Discord](</es/channels/discord>), [Googlechat](</es/channels/googlechat>), [Signal](</es/channels/signal>), [Matrix](</es/channels/matrix>)

Configuración de canales 5 capacidades / con soporte LTS

Experimental14%

Beta79%

Beta79%

[Índice](</es/channels>), [Emparejamiento](</es/channels/pairing>), [Solución de problemas](</es/channels/troubleshooting>), [Plugins de canales del SDK](</es/plugins/sdk-channel-plugins>)

Comportamiento de hilos de grupo y salas ambientales 5 capacidades

Experimental36%

Beta79%

Beta79%

[Grupos](</es/channels/groups>), [Mensajes de grupo](</es/channels/group-messages>), [Eventos de sala ambiental](</es/channels/ambient-room-events>), [Grupos de difusión](</es/channels/broadcast-groups>), [Discord](</es/channels/discord>)

Acceso entrante y controles de identidad 5 capacidades / con soporte LTS

Experimental0%

Alfa68%

Beta79%

[Grupos de acceso](</es/channels/access-groups>), [Grupos](</es/channels/groups>), [Discord](</es/channels/discord>), [Line](</es/channels/line>)

Adjuntos multimedia y datos enriquecidos de canales 4 capacidades

Experimental0%

Alfa68%

Beta79%

[Line](</es/channels/line>), [Signal](</es/channels/signal>), [Googlechat](</es/channels/googlechat>), [Matrix](</es/channels/matrix>), [Discord](</es/channels/discord>)

Entrega saliente y canalización de respuestas 4 capacidades / con soporte LTS

Experimental38%

Beta79%

Beta79%

[Grupos](</es/channels/groups>), [Eventos de sala ambiental](</es/channels/ambient-room-events>), [Discord](</es/channels/discord>), [Matrix](</es/channels/matrix>), [Canales de configuración](</es/gateway/config-channels>)

Enrutamiento y entrega de conversaciones 10 capacidades / con soporte LTS

Experimental19%

Beta79%

Beta79%

[Enrutamiento de canales](</es/channels/channel-routing>), [Grupos](</es/channels/groups>), [Discord](</es/channels/discord>), [Matrix](</es/channels/matrix>), [Solución de problemas](</es/channels/troubleshooting>), [Referencia de configuración](</es/gateway/configuration-reference>)

Estado, salud y controles de operador 4 capacidades / con soporte LTS

Experimental0%

Beta79%

Beta79%

[Salud](</es/gateway/health>), [Referencia de configuración](</es/gateway/configuration-reference>), [Solución de problemas](</es/channels/troubleshooting>), [Discord](</es/channels/discord>)

Observability - M3 Beta - 5 areas

Existen documentos de OTel, Prometheus, registro y diagnóstico. Necesita una revisión de madurez pública sobre "lo que los operadores deben mirar primero".

Cobertura Experimental - 18%Calidad Beta - 75%Completitud Beta - 79%Parcial - 3

Salud y reparación 12 capacidades / con soporte LTS

Experimental28%

Beta79%

Beta79%

[Salud](</es/gateway/health>), [Telegram](</es/channels/telegram>), [Doctor](</es/cli/doctor>), [Doctor](</es/gateway/doctor>), [Subrutas del SDK](</es/plugins/sdk-subpaths>), [Salud](</es/cli/health>), [Protocolo](</es/gateway/protocol>)

Registro 5 capacidades / con soporte LTS

Experimental0%

Alpha68%

Beta79%

[Registro](</es/logging>), [Registro](</es/gateway/logging>), [Registros](</es/cli/logs>)

Recopilación de diagnósticos 8 capacidades

Experimental30%

Beta79%

Beta79%

[Diagnósticos](</es/gateway/diagnostics>), [Salud](</es/gateway/health>), [Arnés de Codex](</es/plugins/codex-harness>), [Protocolo](</es/gateway/protocol>)

Exportación de telemetría 13 capacidades

Experimental33%

Beta79%

Beta79%

[Hooks](</es/plugins/hooks>), [Opentelemetry](</es/gateway/opentelemetry>), [Registro](</es/logging>), [Subrutas del SDK](</es/plugins/sdk-subpaths>), [Otel de diagnósticos](</es/plugins/reference/diagnostics-otel>), [Prometheus](</es/gateway/prometheus>), [Prometheus de diagnósticos](</es/plugins/reference/diagnostics-prometheus>)

Diagnósticos de sesión 4 capacidades / con soporte LTS

Experimental0%

Alpha68%

Beta79%

[Opentelemetry](</es/gateway/opentelemetry>), [Prometheus](</es/gateway/prometheus>), [Diagnósticos](</es/gateway/diagnostics>), [Protocolo](</es/gateway/protocol>)

Aplicación web Gateway - M3 Beta - 6 áreas

La interfaz web está documentada con flujos de emparejamiento, chat, PWA, Talk, push y Gateway remoto. Promocionar después de las tarjetas de puntuación entre navegadores y de PWA móvil.

Cobertura Experimental - 4%Calidad Beta - 74%Completitud Beta - 79%Ninguna

Conversación en tiempo real del navegador 5 capacidades

Experimental0%

Alfa68%

Beta79%

[IU de control](</es/web/control-ui>), [Protocolo](</es/gateway/protocol>), [Conversación](</es/nodes/talk>)

Acceso y confianza del navegador 5 capacidades

Experimental0%

Alfa68%

Beta79%

[IU de control](</es/web/control-ui>), [Panel](</es/web/dashboard>), [Tailscale](</es/gateway/tailscale>), [Remoto](</es/gateway/remote>)

Configuración 5 capacidades

Experimental0%

Alfa68%

Beta79%

[IU de control](</es/web/control-ui>), [Configuración](</es/gateway/configuration>)

Interfaz de usuario del navegador 10 capacidades

Experimental8%

Beta79%

Beta79%

[IU de control](</es/web/control-ui>), [Índice](</es/web>), [Panel](</es/web/dashboard>), [Protocolo](</es/gateway/protocol>)

Conversaciones de WebChat 15 capacidades

Experimental10%

Beta79%

Beta79%

[IU de control](</es/web/control-ui>), [Webchat](</es/web/webchat>), [Primeros pasos](</es/start/getting-started>), [Enrutamiento de canales](</es/channels/channel-routing>), [Operaciones seguras de archivos](</es/gateway/security/secure-file-operations>)

Consola del operador 10 capacidades

Experimental8%

Beta79%

Beta79%

[IU de control](</es/web/control-ui>), [Estado](</es/gateway/health>), [Protocolo](</es/gateway/protocol>), [Panel](</es/web/dashboard>)

Plugins - M3 Beta - 9 áreas

Existen documentación amplia y evidencia interna sólida del runtime en manifiestos, descubrimiento, carga, arquitectura de proveedores/herramientas y límites de aprobación. Mantén la fila en beta hasta que la prueba de la API/subrutas del SDK público y la distribución externa sea más sólida.

Cobertura Experimental - 12%Calidad Beta - 72%Completitud Beta - 79%Parcial - 7

Creación y empaquetado de plugins 8 capacidades / compatible con LTS

Experimental0%

Alfa68%

Beta79%

[Creación de plugins](</es/plugins/building-plugins>), [Resumen del SDK](</es/plugins/sdk-overview>), [Puntos de entrada del SDK](</es/plugins/sdk-entrypoints>), [Subrutas del SDK](</es/plugins/sdk-subpaths>), [Manifiesto](</es/plugins/manifest>), [Referencia](</es/plugins/reference>)

Plugins incluidos 5 capacidades / compatible con LTS

Experimental0%

Alfa68%

Beta79%

[Inventario de plugins](</es/plugins/plugin-inventory>), [Plugins](</es/cli/plugins>), [Elementos internos de arquitectura](</es/plugins/architecture-internals>)

Plugin de Canvas 6 capacidades

Experimental0%

Alfa68%

Beta79%

[Canvas](</es/plugins/reference/canvas>), [Canvas](</es/refactor/canvas>), [Referencia de configuración](</es/gateway/configuration-reference>)

Instalación y ejecución de plugins 6 capacidades / compatible con LTS

Experimental35%

Beta79%

Beta79%

[Arquitectura](</es/plugins/architecture>), [Elementos internos de arquitectura](</es/plugins/architecture-internals>), [Plugins](</es/cli/plugins>)

Plugins de canal 5 capacidades / compatible con LTS

Experimental0%

Alfa68%

Beta79%

[Plugins de canal del SDK](</es/plugins/sdk-channel-plugins>), [Entrada de canal del SDK](</es/plugins/sdk-channel-inbound>), [Salida de canal del SDK](</es/plugins/sdk-channel-outbound>)

Plugins de proveedor y herramientas 6 capacidades / compatible con LTS

Experimental43%

Beta79%

Beta79%

[Plugins de proveedor del SDK](</es/plugins/sdk-provider-plugins>), [Plugins de herramientas](</es/plugins/tool-plugins>), [Adición de capacidades](</es/plugins/adding-capabilities>)

Aprobaciones de plugins 6 capacidades / compatible con LTS

Experimental0%

Alfa68%

Beta79%

[Solicitudes de permisos de plugins](</es/plugins/plugin-permission-requests>), [Aprobaciones de exec](</es/tools/exec-approvals>), [Plugins de canal del SDK](</es/plugins/sdk-channel-plugins>)

Publicación de plugins 6 capacidades / compatible con LTS

Experimental0%

Alfa68%

Beta79%

[Plugins](</es/cli/plugins>), [Compatibilidad](</es/plugins/compatibility>), [Publicación](</es/clawhub/publishing>)

Prueba de plugins 6 capacidades

Experimental27%

Beta79%

Beta79%

[Pruebas del SDK](</es/plugins/sdk-testing>), [Configuración del SDK](</es/plugins/sdk-setup>), [Arnés de Codex](</es/plugins/codex-harness>)

Seguridad, autenticación, emparejamiento y secretos - M3 Beta - 6 áreas

Existen buena documentación y superficies de endurecimiento. Promover después de que las ejecuciones regulares de escenarios de actualización/seguridad demuestren que no hay regresiones de configuración.

Cobertura Experimental - 16%Calidad Beta - 72%Integridad Beta - 79%Parcial - 5

Política de aprobación y salvaguardas de herramientas 2 capacidades / compatible con LTS

Alpha50%

Beta79%

Beta79%

[Aprobaciones de ejecución](</es/tools/exec-approvals>), [Aprobaciones](</es/cli/approvals>), [Solicitudes de permisos de Plugin](</es/plugins/plugin-permission-requests>), [Comprobaciones de auditoría](</es/gateway/security/audit-checks>)

Autenticación del Gateway y acceso remoto 9 capacidades / compatible con LTS

Experimental0%

Alpha68%

Beta79%

[Índice](</es/gateway/security>), [Runbook de exposición](</es/gateway/security/exposure-runbook>), [Autenticación de proxy de confianza](</es/gateway/trusted-proxy-auth>), [Tailscale](</es/gateway/tailscale>), [Remoto](</es/gateway/remote>), [Referencia de configuración](</es/gateway/configuration-reference>), [Gateway](</es/cli/gateway>), [Doctor](</es/cli/doctor>), [IU de control](</es/web/control-ui>), [Control del navegador](</es/tools/browser-control>), [Comprobaciones de auditoría](</es/gateway/security/audit-checks>)

Control de acceso del canal 3 capacidades / compatible con LTS

Experimental0%

Alpha68%

Beta79%

[Emparejamiento](</es/channels/pairing>), [Telegram](</es/channels/telegram>), [Grupos de acceso](</es/channels/access-groups>), [Comprobaciones de auditoría](</es/gateway/security/audit-checks>)

Emparejamiento de dispositivos y Node 11 capacidades / compatible con LTS

Experimental0%

Alpha68%

Beta79%

[Protocolo](</es/gateway/protocol>), [Dispositivos](</es/cli/devices>), [Emparejamiento](</es/channels/pairing>), [Emparejamiento](</es/gateway/pairing>), [Ámbitos del operador](</es/gateway/operator-scopes>), [IU de control](</es/web/control-ui>), [Webchat](</es/web/webchat>), [Aprobaciones](</es/cli/approvals>)

Confianza de Plugin 2 capacidades

Experimental0%

Alpha68%

Beta79%

[Manifiesto](</es/plugins/manifest>), [Solicitudes de permisos de Plugin](</es/plugins/plugin-permission-requests>), [Gestionar Plugins](</es/plugins/manage-plugins>), [Comprobaciones de auditoría](</es/gateway/security/audit-checks>)

Higiene de credenciales y secretos 5 capacidades / compatible con LTS

Experimental46%

Beta79%

Beta79%

[Autenticación](</es/gateway/authentication>), [Modelos](</es/cli/models>), [Openai](</es/providers/openai>), [Oauth](</es/concepts/oauth>), [Secretos](</es/gateway/secrets>), [Secretos](</es/cli/secrets>), [Superficie de credenciales Secretref](</es/reference/secretref-credential-surface>), [Comprobaciones de auditoría](</es/gateway/security/audit-checks>)

Automatización: cron, hooks, tareas, sondeo - M3 Beta - 6 áreas

Documentado y utilizable, pero la prueba de escenarios debería cubrir la entrega desatendida, los reintentos y la visibilidad de los fallos.

Cobertura Experimental - 2%Calidad Beta - 72%Integridad Beta - 79%Ninguno

Trabajos Cron 15 capacidades

Experimental0%

Beta79%

Beta79%

[Trabajos Cron](</es/automation/cron-jobs>), [Cron](</es/cli/cron>), [Protocolo](</es/gateway/protocol>), [Tareas](</es/automation/tasks>), [Discord](</es/channels/discord>)

Ingreso de eventos 15 capacidades

Experimental0%

Alfa68%

Beta79%

[Telegram](</es/channels/telegram>), [Zalo](</es/channels/zalo>), [Solución de problemas](</es/channels/troubleshooting>), [iMessage desde Bluebubbles](</es/channels/imessage-from-bluebubbles>), [Integración Pub/Sub de Gmail](</es/automation/cron-jobs#gmail-pubsub-integration>), [Pub/Sub de Gmail](</es/automation/cron-jobs>), [Webhooks](</es/cli/webhooks>), [Webhooks](</es/automation/cron-jobs#webhooks>), [Webhook](</es/automation/cron-jobs>)

Ganchos de automatización 11 capacidades

Experimental0%

Alfa68%

Beta79%

[Ganchos](</es/automation/hooks>), [Ganchos](</es/cli/hooks>), [Ganchos](</es/plugins/hooks>), [Solicitudes de permisos de Plugin](</es/plugins/plugin-permission-requests>), [Subrutas del SDK](</es/plugins/sdk-subpaths>)

Tareas y flujos en segundo plano 10 capacidades

Experimental0%

Alfa68%

Beta79%

[Tareas](</es/automation/tasks>), [Índice](</es/automation>), [Tareas](</es/cli/tasks>), [TaskFlow](</es/automation/taskflow>), [Entorno de ejecución del SDK](</es/plugins/sdk-runtime>)

Heartbeat 5 capacidades

Experimental14%

Beta79%

Beta79%

[Índice](</es/automation>), [Heartbeat](</es/gateway/heartbeat>), [Compromisos](</es/concepts/commitments>)

Controles de sondeo 10 capacidades

Experimental0%

Alfa68%

Beta79%

[Sondeo](</es/cli/message>), [Mensaje](</es/cli/message>), [Telegram](</es/channels/telegram>), [Msteams](</es/channels/msteams>), [Proceso en segundo plano](</es/gateway/background-process>)

Comprensión y generación de medios - M2 Alfa - 6 áreas

Existe una amplia superficie de capacidades, pero la variación entre proveedores, los límites de archivos y la paridad entre Node y la aplicación hacen que aún no sea estable.

Cobertura Experimental - 2%Calidad Alfa - 64%Integridad Alfa - 68%Ninguna

Ingesta y acceso a medios 8 capacidades

Experimental0%

Alfa61%

Alfa68%

[Resumen de medios](</es/tools/media-overview>), [Comprensión de medios](</es/nodes/media-understanding>), [Operaciones seguras con archivos](</es/gateway/security/secure-file-operations>), [Pdf](</es/tools/pdf>), [Generación de imágenes](</es/tools/image-generation>), [Qr](</es/cli/qr>), [LINE](</es/channels/line>), [WhatsApp](</es/channels/whatsapp>)

Manejo de medios en canales 5 capacidades

Experimental0%

Alfa61%

Alfa68%

[Imágenes](</es/nodes/images>), [Resumen de medios](</es/tools/media-overview>), [Discord](</es/channels/discord>)

Configuración de medios 1 capacidad

Experimental0%

Alfa61%

Alfa68%

[Resumen de medios](</es/tools/media-overview>), [Generación de imágenes](</es/tools/image-generation>), [Manifest](</es/plugins/manifest>), [Arnés de Codex](</es/plugins/codex-harness>)

Entrega de texto a voz 2 capacidades

Experimental0%

Alfa61%

Alfa68%

[Tts](</es/tools/tts>), [Resumen de medios](</es/tools/media-overview>), [Discord](</es/channels/discord>)

Comprensión de medios 12 capacidades

Experimental7%

Alfa69%

Alfa69%

[Audio](</es/nodes/audio>), [Comprensión de medios](</es/nodes/media-understanding>), [Resumen de medios](</es/tools/media-overview>), [WhatsApp](</es/channels/whatsapp>), [Imágenes](</es/nodes/images>), [Inferir](</es/cli/infer>), [Pdf](</es/tools/pdf>)

Generación de medios 17 capacidades

Experimental5%

Alfa69%

Alfa69%

[Generación de imágenes](</es/tools/image-generation>), [Resumen de medios](</es/tools/media-overview>), [Skills](</es/tools/skills>), [Generación de música](</es/tools/music-generation>), [Generación de video](</es/tools/video-generation>)

Voz y conversación en tiempo real - M2 Alfa - 6 áreas

Existen varias implementaciones en Control UI, aplicaciones y proveedores. Necesita tablas de puntuación de latencia, modos de fallo y configuración antes de la beta.

Cobertura Experimental - 0%Calidad Alfa - 61%Completitud Alfa - 68%Ninguno

Proveedores de Talk 7 capacidades

Experimental0%

Alpha61%

Alpha68%

[Openai](</es/providers/openai>), [Google](</es/providers/google>), [Plugins de proveedor del SDK](</es/plugins/sdk-provider-plugins>), [Talk](</es/nodes/talk>), [IU de control](</es/web/control-ui>)

Sesiones de Talk en tiempo real 11 capacidades

Experimental0%

Alpha61%

Alpha68%

[Talk](</es/nodes/talk>), [IU de control](</es/web/control-ui>)

Voz y transcripción 5 capacidades

Experimental0%

Alpha61%

Alpha68%

[Talk](</es/nodes/talk>), [Openai](</es/providers/openai>), [Google](</es/providers/google>)

Talk en aplicación nativa 4 capacidades

Experimental0%

Alpha61%

Alpha68%

[Talk](</es/nodes/talk>), [Voicewake](</es/platforms/mac/voicewake>)

Activación por voz y enrutamiento 4 capacidades

Experimental0%

Alpha61%

Alpha68%

[Voicewake](</es/nodes/voicewake>), [Voicewake](</es/platforms/mac/voicewake>), [Superposición de voz](</es/platforms/mac/voice-overlay>)

Observabilidad de Talk 5 capacidades

Experimental0%

Alpha61%

Alpha68%

[IU de control](</es/web/control-ui>), [Superposición de voz](</es/platforms/mac/voice-overlay>), [Talk](</es/nodes/talk>)

TUI - M2 Alpha - 5 áreas

Presente en la documentación y en el código fuente, pero menos visible como flujo de trabajo principal para el usuario. Necesita una definición explícita de escenarios.

Cobertura Experimental - 0%Calidad Alpha - 59%Completitud Alpha - 66%Ninguno

Modos de ejecución 14 capacidades

Experimental0%

Alfa59%

Alfa66%

[Tui](</es/cli/tui>), [Tui](</es/web/tui>), [Índice](</es/cli>)

Entrada y comandos 8 capacidades

Experimental0%

Alfa59%

Alfa66%

[Tui](</es/web/tui>)

Gestión de sesiones 3 capacidades

Experimental0%

Alfa59%

Alfa66%

[Tui](</es/web/tui>), [Sesiones](</es/cli/sessions>)

Ejecución de shell local 4 capacidades

Experimental0%

Alfa59%

Alfa66%

[Tui](</es/web/tui>), [Tui](</es/cli/tui>)

Renderizado y seguridad de salida 4 capacidades

Experimental0%

Alfa59%

Alfa66%

[Tui](</es/web/tui>), [Qr](</es/cli/qr>), [Registros](</es/cli/logs>), [Finalización](</es/cli/completion>)

ClawHub - M2 Alfa - 4 áreas

Existen documentación pública y concepto de ecosistema. Necesita cuadros de mando de instalación, confianza, actualización, reversión y compatibilidad.

Cobertura Experimental - 0%Calidad Alfa - 58%Completitud Alfa - 62%Ninguno

Publicación 7 capacidades

Experimental0%

Alfa54%

Alfa55%

[Publicación](</es/clawhub/publishing>), [Creación de Skills](</es/tools/creating-skills>), [Comunidad](</es/plugins/community>)

Descubrimiento de catálogo 5 capacidades

Experimental0%

Alfa61%

Alfa68%

[Plugin](</es/tools/plugin>), [Plugins](</es/cli/plugins>), [Skills](</es/cli/skills>), [Skills](</es/tools/skills>), [Comunidad](</es/plugins/community>)

Compatibilidad y confianza 12 capacidades

Experimental0%

Alfa55%

Alfa56%

[Plugin](</es/tools/plugin>), [Plugins](</es/cli/plugins>), [Compatibilidad](</es/plugins/compatibility>), [Inventario de Plugins](</es/plugins/plugin-inventory>), [Publicación](</es/clawhub/publishing>), [Skills](</es/tools/skills>), [Configuración de Skills](</es/tools/skills-config>)

Ciclo de vida y estado de Plugin 26 capacidades

Experimental0%

Alfa61%

Alfa68%

[Plugin](</es/tools/plugin>), [Plugins](</es/cli/plugins>), [Skills](</es/cli/skills>), [Skills](</es/tools/skills>), [Protocolo](</es/gateway/protocol>), [Paquetes](</es/plugins/bundles>), [Resolución de dependencias](</es/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alfa - 6 áreas

OpenClaw App SDK es un contrato de app externa distinto, separado del tiempo de ejecución de Gateway y de Plugin SDK. La puntuación actual muestra una ruta `@openclaw/sdk` real con brechas en el empaquetado público, el autodescubrimiento, las aprobaciones, las utilidades y la compatibilidad.

Cobertura experimental - 3%Calidad alfa - 54%Integridad alfa - 53%Ninguno

API de cliente 4 capacidades

Experimental0%

Alpha51%

Alpha50%

[Openclaw Sdk](</es/gateway/external-apps>), [Diseño de API de Openclaw Sdk](</es/gateway/external-apps>)

Acceso al Gateway 5 capacidades

Experimental0%

Alpha53%

Alpha54%

[Openclaw Sdk](</es/gateway/external-apps>), [Diseño de API de Openclaw Sdk](</es/gateway/external-apps>), [Protocolo](</es/gateway/protocol>), [Índice](</es/gateway/security>)

Conversaciones de agentes 6 capacidades

Experimental0%

Alpha52%

Alpha52%

[Openclaw Sdk](</es/gateway/external-apps>), [Diseño de API de Openclaw Sdk](</es/gateway/external-apps>), [Protocolo](</es/gateway/protocol>)

Eventos y aprobaciones 5 capacidades

Experimental0%

Alpha52%

Alpha52%

[Openclaw Sdk](</es/gateway/external-apps>), [Diseño de API de Openclaw Sdk](</es/gateway/external-apps>), [Protocolo](</es/gateway/protocol>)

Ayudantes de recursos 5 capacidades

Experimental17%

Alpha62%

Alpha53%

[Openclaw Sdk](</es/gateway/external-apps>), [Diseño de API de Openclaw Sdk](</es/gateway/external-apps>)

Compatibilidad 5 capacidades

Experimental0%

Alpha54%

Alpha55%

[Diseño de API de Openclaw Sdk](</es/gateway/external-apps>), [Typebox](</es/concepts/typebox>), [Protocolo](</es/gateway/protocol>)

### Plataforma

Host de Gateway en Linux - M4 estable - 5 áreas

Se recomienda el runtime de Node, el servicio de usuario de systemd está documentado y la guía para VPS/contenedores es amplia.

Cobertura Experimental - 0%Calidad Beta - 75%Integridad estable - 89%Parcial - 4

Configuración y actualizaciones del host 4 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Índice](</es/install>), [Actualización](</es/install/updating>), [Linux](</es/platforms/linux>), [Índice](</es/platforms>)

Entorno de ejecución de Gateway y control del servicio 6 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Índice](</es/gateway>), [Gateway](</es/cli/gateway>), [Linux](</es/platforms/linux>), [VPS](</es/vps>)

Acceso remoto y seguridad 6 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Remoto](</es/gateway/remote>), [Tailscale](</es/gateway/tailscale>), [Runbook de exposición](</es/gateway/security/exposure-runbook>), [Autenticación](</es/gateway/authentication>), [Secretos](</es/gateway/secrets>)

Diagnóstico y reparación 4 capacidades / compatible con LTS

Experimental0%

Beta75%

Estable89%

[Estado](</es/cli/status>), [Registros](</es/cli/logs>), [Doctor](</es/cli/doctor>), [Diagnóstico](</es/gateway/diagnostics>), [Índice](</es/gateway>)

Destinos de implementación 3 capacidades

Experimental0%

Beta75%

Estable89%

[VPS](</es/vps>), [Docker](</es/install/docker>), [Hetzner](</es/install/hetzner>), [DigitalOcean](</es/install/digitalocean>), [Kubernetes](</es/install/kubernetes>), [Podman](</es/install/podman>)

macOS Gateway host - M4 Stable - 7 areas

La ruta del servicio LaunchAgent, los modos de Gateway local/remoto, la instalación de la CLI y la integración de la aplicación están documentados.

Cobertura experimental - 0%Calidad beta - 74%Completitud estable - 88%Ninguno

Configuración de CLI 4 capacidades

Experimental0%

Beta74%

Estable88%

[Macos](</es/platforms/macos>), [Gateway incluido](</es/platforms/mac/bundled-gateway>), [Instalador](</es/install/installer>), [Node](</es/install/node>)

Integración con Gateway local 9 capacidades

Experimental0%

Beta74%

Estable88%

[Macos](</es/platforms/macos>), [Gateway incluido](</es/platforms/mac/bundled-gateway>), [Remoto](</es/platforms/mac/remote>), [Índice](</es/gateway>), [Gateway](</es/cli/gateway>), [Bonjour](</es/gateway/bonjour>)

Modo de Gateway remoto 5 capacidades

Experimental0%

Beta74%

Estable88%

[Remoto](</es/platforms/mac/remote>), [Remoto](</es/gateway/remote>), [Tailscale](</es/gateway/tailscale>)

Ciclo de vida del servicio Gateway 10 capacidades

Experimental0%

Beta74%

Estable88%

[Macos](</es/platforms/macos>), [Gateway incluido](</es/platforms/mac/bundled-gateway>), [Gateway](</es/cli/gateway>), [Índice](</es/gateway>), [Actualizar](</es/cli/update>), [Actualización](</es/install/updating>), [Desinstalar](</es/install/uninstall>), [Solución de problemas](</es/gateway/troubleshooting>)

Diagnóstico y observabilidad 4 capacidades

Experimental0%

Beta74%

Estable88%

[Gateway incluido](</es/platforms/mac/bundled-gateway>), [Macos](</es/platforms/macos>), [Gateway](</es/cli/gateway>), [Doctor](</es/gateway/doctor>), [Solución de problemas](</es/gateway/troubleshooting>)

Permisos y capacidades nativas 4 capacidades

Experimental0%

Beta74%

Estable88%

[Macos](</es/platforms/macos>), [Remoto](</es/platforms/mac/remote>)

Perfiles y aislamiento 5 capacidades

Experimental0%

Beta74%

Estable88%

[Múltiples Gateways](</es/gateway/multiple-gateways>), [Índice](</es/gateway>), [Gateway](</es/cli/gateway>)

Alojamiento en Docker y Podman - M3 Beta - 4 áreas

Existen documentos de instalación y son rutas de implementación habituales. Promocionar después de que las pruebas de humo recurrentes de lanzamiento capturen el comportamiento de actualización y volúmenes.

Cobertura experimental - 7%Calidad Beta - 71%Integridad Beta - 79%Ninguna

Configuración de contenedores 6 capacidades

Experimental0%

Alfa68%

Beta79%

[Docker](</es/install/docker>), [Podman](</es/install/podman>)

Operaciones de contenedores 11 capacidades

Experimental0%

Alfa68%

Beta79%

[Podman](</es/install/podman>), [Entorno de ejecución de VM de Docker](</es/install/docker-vm-runtime>), [Docker](</es/install/docker>), [Hetzner](</es/install/hetzner>), [Hostinger](</es/install/hostinger>)

Publicación y validación de imágenes 5 capacidades

Experimental29%

Beta79%

Beta79%

[Docker](</es/install/docker>), [Entorno de ejecución de VM de Docker](</es/install/docker-vm-runtime>), [Validación completa de la versión](</es/reference/full-release-validation>)

Sandbox y herramientas de agentes 3 capacidades

Experimental0%

Alfa68%

Beta79%

[Docker](</es/install/docker>), [Entorno de ejecución de VM de Docker](</es/install/docker-vm-runtime>)

Windows mediante WSL2 - Beta M3 - 6 áreas

Ruta recomendada para Windows con orientación sobre systemd/servicios de usuario y documentación de la cadena de arranque. Promocionar después de scorecards repetidos de instalación/actualización.

Cobertura Experimental - 6%Calidad Alfa - 69%Completitud Beta - 79%Parcial - 5

Configuración de WSL 6 capacidades / con soporte LTS

Experimental0%

Alfa67%

Beta79%

[Windows](</es/platforms/windows>), [Primeros pasos](</es/start/getting-started>)

CLI 8 capacidades / con soporte LTS

Experimental0%

Alfa67%

Beta79%

[Windows](</es/platforms/windows>), [Primeros pasos](</es/start/getting-started>), [Actualización](</es/install/updating>), [Onboard](</es/cli/onboard>), [Doctor](</es/cli/doctor>), [Estado](</es/cli/status>), [Registros](</es/cli/logs>)

Ciclo de vida del servicio Gateway 10 capacidades / con soporte LTS

Experimental0%

Alfa67%

Beta79%

[Windows](</es/platforms/windows>), [Índice](</es/gateway>), [Doctor](</es/gateway/doctor>)

Acceso y exposición del Gateway 11 capacidades / con soporte LTS

Experimental0%

Alfa67%

Beta79%

[Autenticación](</es/gateway/authentication>), [Secretos](</es/gateway/secrets>), [Remoto](</es/gateway/remote>), [Runbook de exposición](</es/gateway/security/exposure-runbook>), [Windows](</es/platforms/windows>)

Diagnóstico y reparación 6 capacidades / con soporte LTS

Experimental38%

Beta79%

Beta79%

[Windows](</es/platforms/windows>), [Estado](</es/cli/status>), [Registros](</es/cli/logs>), [Doctor](</es/cli/doctor>), [Doctor](</es/gateway/doctor>)

Navegador e interfaz de control 6 capacidades

Experimental0%

Alfa67%

Beta79%

[Solución de problemas de CDP remoto de Windows WSL2 del navegador](</es/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Navegador](</es/tools/browser>), [Interfaz de control](</es/web/control-ui>)

Raspberry Pi y dispositivos Linux pequeños - M3 Beta - 4 áreas

Existen documentos de plataforma y la ruta del Gateway está basada en Linux. Necesita prueba de smoke de lanzamiento específica de hardware para avanzar más.

Cobertura Experimental - 0%Calidad Alfa - 67%Completitud Beta - 79%Ninguno

Configuración y compatibilidad 12 capacidades

Experimental0%

Alpha67%

Beta79%

[Raspberry Pi](</es/install/raspberry-pi>), [Índice](</es/install>), [Preguntas frecuentes del primer inicio](</es/help/faq-first-run>), [Preguntas frecuentes](</es/help/faq>), [Linux](</es/platforms/linux>), [Instalador](</es/install/installer>)

Acceso remoto y autenticación 9 capacidades

Experimental0%

Alpha67%

Beta79%

[Raspberry Pi](</es/install/raspberry-pi>), [Autenticación](</es/gateway/authentication>), [Secretos](</es/gateway/secrets>), [Emparejamiento](</es/gateway/pairing>), [Dispositivos](</es/cli/devices>), [Remoto](</es/gateway/remote>), [Tailscale](</es/gateway/tailscale>)

Runtime de Gateway 10 capacidades

Experimental0%

Alpha67%

Beta79%

[Índice](</es/gateway>), [Gateway](</es/cli/gateway>), [Raspberry Pi](</es/install/raspberry-pi>), [Linux](</es/platforms/linux>), [Vps](</es/vps>)

Rendimiento y diagnósticos 5 capacidades

Experimental0%

Alpha67%

Beta79%

[Raspberry Pi](</es/install/raspberry-pi>), [Linux](</es/platforms/linux>), [Salud](</es/gateway/health>), [Diagnósticos](</es/gateway/diagnostics>)

Aplicación complementaria para macOS - M3 Beta - 8 áreas

Existen una aplicación completa de barra de menús, permisos, modo Node, Canvas, activación por voz, WebChat y modo remoto. Aún cambia lo bastante rápido como para evitar Stable.

Cobertura Experimental - 0%Calidad Alpha - 66%Completitud Beta - 78%Ninguna

Lienzo 4 capacidades

Experimental0%

Alfa66%

Beta78%

[Lienzo](</es/platforms/mac/canvas>), [Macos](</es/platforms/macos>), [Webchat](</es/web/webchat>)

Configuración local 7 capacidades

Experimental0%

Alfa66%

Beta78%

[Gateway incluido](</es/platforms/mac/bundled-gateway>), [Macos](</es/platforms/macos>), [Proceso hijo](</es/platforms/mac/child-process>), [Configuración de desarrollo](</es/platforms/mac/dev-setup>)

Estado y configuración 5 capacidades

Experimental0%

Alfa66%

Beta78%

[Barra de menús](</es/platforms/mac/menu-bar>), [Icono](</es/platforms/mac/icon>), [Macos](</es/platforms/macos>), [Salud](</es/platforms/mac/health>), [Registro](</es/platforms/mac/logging>), [Remoto](</es/platforms/mac/remote>)

Capacidades nativas 5 capacidades

Experimental0%

Alfa66%

Beta78%

[Macos](</es/platforms/macos>), [Xpc](</es/platforms/mac/xpc>), [Permisos](</es/platforms/mac/permissions>), [Firma](</es/platforms/mac/signing>), [Peekaboo](</es/platforms/mac/peekaboo>)

Conexiones remotas 3 capacidades

Experimental0%

Alfa66%

Beta78%

[Remoto](</es/platforms/mac/remote>), [Macos](</es/platforms/macos>), [Remoto](</es/gateway/remote>)

Voz y conversación 3 capacidades

Experimental0%

Alfa66%

Beta78%

[Voicewake](</es/platforms/mac/voicewake>), [Superposición de voz](</es/platforms/mac/voice-overlay>), [Hablar](</es/nodes/talk>), [Macos](</es/platforms/macos>)

WebChat 3 capacidades

Experimental0%

Alfa66%

Beta78%

[Webchat](</es/platforms/mac/webchat>), [Macos](</es/platforms/macos>), [Webchat](</es/web/webchat>)

WebChat remoto 5 capacidades

Experimental0%

Alfa66%

Beta78%

[Webchat](</es/platforms/mac/webchat>), [Remoto](</es/gateway/remote>), [Remoto](</es/platforms/mac/remote>)

Aplicación para Android - M2 Alfa - 7 áreas

Existe una ruta pública de Google Play, pero la documentación de la aplicación todavía describe la reconstrucción como extremadamente alfa y señala trabajo de robustecimiento para el lanzamiento.

Cobertura Experimental - 0%Calidad Alfa - 59%Completitud Alfa - 66%Ninguno

Captura multimedia 1 capacidades

Experimental0%

Alpha59%

Alpha66%

[Android](</es/platforms/android>), [Cámara](</es/nodes/camera>)

Chat móvil 1 capacidades

Experimental0%

Alpha59%

Alpha66%

[Android](</es/platforms/android>)

Configuración de conexión 1 capacidades

Experimental0%

Alpha59%

Alpha66%

[Android](</es/platforms/android>), [Bonjour](</es/gateway/bonjour>), [Emparejamiento](</es/gateway/pairing>)

Distribución 3 capacidades

Experimental0%

Alpha59%

Alpha66%

[Android](</es/platforms/android>)

Configuración 1 capacidades

Experimental0%

Alpha59%

Alpha66%

[Android](</es/platforms/android>)

Voz 1 capacidades

Experimental0%

Alpha59%

Alpha66%

[Android](</es/platforms/android>), [Hablar](</es/nodes/talk>)

Tiempo de ejecución del dispositivo 2 capacidades

Experimental0%

Alpha59%

Alpha66%

[Android](</es/platforms/android>), [Solución de problemas](</es/nodes/troubleshooting>), [Protocolo](</es/gateway/protocol>)

Windows nativo - M2 Alpha - 4 áreas

Los flujos principales de CLI/Gateway funcionan, pero la documentación todavía recomienda WSL2 para la experiencia completa y enumera advertencias nativas.

Cobertura Experimental - 0%Calidad Alpha - 58%Integridad Alpha - 66%Parcial - 1

CLI 9 capacidades / compatible con LTS

Experimental0%

Alpha54%

Alpha64%

[Índice](</es/install>), [Instalador](</es/install/installer>), [Windows](</es/platforms/windows>), [Primeros pasos](</es/start/getting-started>), [Incorporación](</es/cli/onboard>)

Gestión de Gateway 11 capacidades

Experimental0%

Alpha59%

Alpha66%

[Windows](</es/platforms/windows>), [Índice](</es/gateway>), [Gateway](</es/cli/gateway>), [Doctor](</es/cli/doctor>)

Redes 4 capacidades

Experimental0%

Alpha59%

Alpha66%

[Windows](</es/platforms/windows>), [Índice](</es/gateway>), [Gateway](</es/cli/gateway>)

Actualizaciones 4 capacidades

Experimental0%

Alpha59%

Alpha66%

[Actualización](</es/install/updating>), [CI](</es/ci>)

Alojamiento en Kubernetes - M2 Alpha - 4 áreas

El alojamiento en Kubernetes es una ruta diferenciada de despliegue de clúster basada en Kustomize. La puntuación actual muestra una ruta de despliegue mínima real con brechas en torno a CI específico de Kubernetes, empaquetado de ingress/TLS/NetworkPolicy, copia de seguridad/restauración y endurecimiento de la exposición en producción.

Cobertura Experimental - 0%Calidad Alfa - 55%Completitud Alfa - 61%Ninguno

Configuración de despliegue 5 capacidades

Experimental0%

Alfa55%

Alfa61%

[Kubernetes](</es/install/kubernetes>), [Índice](</es/install>)

Configuración y secretos 5 capacidades

Experimental0%

Alfa55%

Alfa61%

[Kubernetes](</es/install/kubernetes>), [Secretos](</es/gateway/secrets>), [Entorno](</es/help/environment>)

Acceso y exposición 5 capacidades

Experimental0%

Alfa55%

Alfa61%

[Kubernetes](</es/install/kubernetes>), [Autenticación](</es/gateway/authentication>), [Remoto](</es/gateway/remote>), [Guía operativa de exposición](</es/gateway/security/exposure-runbook>)

Ciclo de vida del clúster 5 capacidades

Experimental0%

Alfa55%

Alfa61%

[Kubernetes](</es/install/kubernetes>), [Índice](</es/gateway>)

Aplicación iOS - M1 Experimental - 8 áreas

Vista previa interna / super-alfa. Existen flujos de TestFlight y de notificaciones push respaldadas por retransmisión, pero aún no hay distribución pública.

Cobertura Experimental - 0%Calidad Experimental - 41%Completitud Experimental - 44%Ninguno

Medios y uso compartido 1 capacidad

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>), [Cámara](</es/nodes/camera>)

Lienzo y pantalla 1 capacidad

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>), [Canvas](</es/plugins/reference/canvas>)

Chat y sesiones 1 capacidad

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>), [Webchat](</es/web/webchat>), [Protocolo](</es/gateway/protocol>)

Configuración y diagnóstico del Gateway 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>), [Emparejamiento](</es/channels/pairing>)

Distribución 1 capacidad

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>)

Comandos del dispositivo 2 capacidades

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>), [Protocolo](</es/gateway/protocol>)

Notificaciones y segundo plano 1 capacidad

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>), [Configuración](</es/gateway/configuration>)

Voz 1 capacidad

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>), [Hablar](</es/nodes/talk>)

Ruta de instalación de Nix - M1 Experimental - 5 áreas

Flujo de instalación opcional. Necesita una promesa de soporte más clara antes de la promoción a alfa/beta.

Cobertura Experimental - 0%Calidad Experimental - 41%Integridad Experimental - 44%Ninguno

Traspaso de instalación 4 capacidades

Experimental0%

Experimental41%

Experimental44%

[Nix](</es/install/nix>), [Índice](</es/install>), [Directorio de documentos](</es/start/docs-directory>)

Ciclo de vida de Plugin 4 capacidades

Experimental0%

Experimental41%

Experimental44%

[Gestionar Plugins](</es/plugins/manage-plugins>), [Plugin](</es/tools/plugin>), [Nix](</es/install/nix>)

Activación y experiencia de usuario de la app 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[Nix](</es/install/nix>)

Configuración y estado 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[Nix](</es/install/nix>), [Configuración](</es/cli/setup>), [Entorno](</es/help/environment>)

Runtime de servicio y protecciones 8 capacidades

Experimental0%

Experimental41%

Experimental44%

[Nix](</es/install/nix>), [Configuración](</es/cli/setup>), [Doctor](</es/cli/doctor>), [Actualización](</es/cli/update>)

superficies complementarias de watchOS - M1 Experimental - 5 áreas

La fuente tiene superficies de app/extensión Watch; la documentación pública aún no presenta esto como una función para usuarios.

Cobertura Experimental - 0%Calidad Experimental - 41%Completitud Experimental - 44%Ninguno

Entrega y recuperación 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>)

Aprobaciones de ejecución 3 capacidades

Experimental0%

Experimental41%

Experimental44%

[Aprobaciones de ejecución](</es/tools/exec-approvals>), [Ios](</es/platforms/ios>)

Distribución y soporte 6 capacidades

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>)

Notificaciones y respuestas 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>)

Interfaz de usuario de la app del reloj 3 capacidades

Experimental0%

Experimental41%

Experimental44%

[Ios](</es/platforms/ios>)

Aplicación complementaria de Linux - M0 planificado - 5 áreas

La documentación indica que las aplicaciones complementarias nativas de Linux están planificadas; Gateway es la vía compatible de Linux actualmente.

Cobertura experimental - 0%Calidad experimental - 19%Integridad experimental - 21%Ninguna

Distribución de la app 3 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</es/platforms/linux>), [Índice](</es/platforms>), [Índice](</es/install>)

Conectividad del Gateway 4 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</es/platforms/linux>), [Índice](</es/gateway>), [Emparejamiento](</es/gateway/pairing>), [Remoto](</es/gateway/remote>)

Chat y sesiones 3 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</es/platforms/linux>), [Protocolo](</es/gateway/protocol>), [Webchat](</es/web/webchat>)

Capacidades de escritorio 9 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</es/platforms/linux>), [Aprobaciones de Exec](</es/tools/exec-approvals>), [Secretos](</es/gateway/secrets>), [Índice](</es/nodes>), [Exec](</es/tools/exec>), [Hablar](</es/nodes/talk>), [Cámara](</es/nodes/camera>)

Estado y diagnósticos 7 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</es/platforms/linux>), [Openclaw](</es/start/openclaw>), [Doctor](</es/gateway/doctor>)

App complementaria nativa de Windows - M0 Planificada - 5 áreas

Solo planificada.

Cobertura Experimental - 0%Calidad Experimental - 19%Integridad Experimental - 21%Ninguno

Instalación y actualizaciones 4 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</es/platforms/windows>), [Índice](</es/install>)

Conexión del Gateway 3 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</es/platforms/windows>), [Índice](</es/gateway>), [Emparejamiento](</es/gateway/pairing>), [Remoto](</es/gateway/remote>)

Sesiones de chat 2 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</es/platforms/windows>), [Protocolo](</es/gateway/protocol>)

Estado y reparación 5 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</es/platforms/windows>), [Doctor](</es/gateway/doctor>), [Índice](</es/gateway>)

Herramientas de escritorio y permisos 10 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</es/platforms/windows>), [Índice](</es/nodes>), [Exec](</es/tools/exec>), [Aprobaciones de Exec](</es/tools/exec-approvals>), [Índice](</es/gateway/security>)

### Canal

Discord - M4 estable - 6 áreas

Documentación profunda y amplia cobertura de funciones. Las rutas de voz/delegación deben seguir puntuándose por separado como beta/alfa.

Cobertura experimental - 0%Calidad beta - 73%Completitud estable - 87%Parcial - 4

Configuración y operaciones de canales 10 capacidades / con soporte LTS

Experimental0%

Beta73%

Estable87%

[Discord](</es/channels/discord>), [Discord](</es/plugins/reference/discord>), [Fly](</es/install/fly>), [Comandos slash](</es/tools/slash-commands>), [Salud](</es/gateway/health>), [Canales](</es/cli/channels>), [Canales de configuración](</es/gateway/config-channels>)

Acceso e identidad 6 capacidades / con soporte LTS

Experimental0%

Beta73%

Estable87%

[Discord](</es/channels/discord>), [Emparejamiento](</es/channels/pairing>), [Grupos de acceso](</es/channels/access-groups>), [Grupos](</es/channels/groups>)

Enrutamiento y entrega de conversaciones 12 capacidades / con soporte LTS

Experimental0%

Beta73%

Estable87%

[Discord](</es/channels/discord>), [Enrutamiento de canales](</es/channels/channel-routing>), [Grupos](</es/channels/groups>), [Grupos de acceso](</es/channels/access-groups>), [Agentes ACP](</es/tools/acp-agents>), [Subagentes](</es/tools/subagents>)

Medios y contenido enriquecido 1 capacidad / con soporte LTS

Experimental0%

Beta73%

Estable87%

[Discord](</es/channels/discord>)

Controles nativos y aprobaciones 5 capacidades

Experimental0%

Beta73%

Estable87%

[Discord](</es/channels/discord>), [Comandos slash](</es/tools/slash-commands>)

Voz y llamadas en tiempo real 5 capacidades

Experimental0%

Beta73%

Estable87%

[Discord](</es/channels/discord>), [Openai](</es/providers/openai>), [Elevenlabs](</es/providers/elevenlabs>), [Automatización E2E de QA](</es/concepts/qa-e2e-automation>), [Canales de configuración](</es/gateway/config-channels>)

Telegram - M3 Beta - 5 áreas

El canal principal es lo bastante maduro para uso regular, pero la UX de alta variabilidad y los casos límite de medios necesitan pruebas de escenarios recurrentes.

Cobertura Experimental - 0%Calidad Alfa - 68%Completitud Beta - 78%Completo - 5

Configuración y operaciones de canales 10 capacidades / compatible con LTS

Experimental0%

Alpha66%

Beta78%

[Telegram](</es/channels/telegram>), [Configurar canales](</es/gateway/config-channels>), [Canales](</es/cli/channels>)

Acceso e identidad 10 capacidades / compatible con LTS

Experimental0%

Alpha66%

Beta78%

[Telegram](</es/channels/telegram>), [Emparejamiento](</es/channels/pairing>), [Grupos de acceso](</es/channels/access-groups>), [Grupos](</es/channels/groups>), [Multiagente](</es/concepts/multi-agent>)

Enrutamiento y entrega de conversaciones 1 capacidades / compatible con LTS

Experimental0%

Alpha66%

Beta78%

[Telegram](</es/channels/telegram>), [Grupos](</es/channels/groups>), [Multiagente](</es/concepts/multi-agent>)

Multimedia y contenido enriquecido 1 capacidades / compatible con LTS

Experimental0%

Alpha66%

Beta78%

[Telegram](</es/channels/telegram>), [Ubicación](</es/channels/location>)

Controles nativos y aprobaciones 9 capacidades / compatible con LTS

Experimental0%

Beta77%

Beta79%

[Telegram](</es/channels/telegram>), [Aprobaciones de exec](</es/tools/exec-approvals>), [Reacciones](</es/tools/reactions>)

Slack - M3 Beta - 5 áreas

Documentación de canal de primera clase y superficie de enrutamiento. Necesita scorecards de escenarios de instalación/administración de workspace.

Cobertura Experimental - 0%Calidad Alpha - 66%Completitud Beta - 78%Completo - 5

Configuración y operaciones de canales 10 capacidades / compatible con LTS

Experimental0%

Alfa66%

Beta78%

[Slack](</es/channels/slack>), [Secretos](</es/gateway/secrets>), [Automatización E2E de QA](</es/concepts/qa-e2e-automation>), [Solución de problemas](</es/channels/troubleshooting>)

Acceso e identidad 1 capacidad / compatible con LTS

Experimental0%

Alfa66%

Beta78%

[Slack](</es/channels/slack>), [Emparejamiento](</es/channels/pairing>)

Enrutamiento y entrega de conversaciones 5 capacidades / compatible con LTS

Experimental0%

Alfa66%

Beta78%

[Slack](</es/channels/slack>), [Protección contra bucles de bots](</es/channels/bot-loop-protection>), [Emparejamiento](</es/channels/pairing>)

Medios y contenido enriquecido 1 capacidad / compatible con LTS

Experimental0%

Alfa66%

Beta78%

[Slack](</es/channels/slack>), [Automatización E2E de QA](</es/concepts/qa-e2e-automation>)

Controles nativos y aprobaciones 8 capacidades / compatible con LTS

Experimental0%

Alfa66%

Beta78%

[Slack](</es/channels/slack>), [Comandos slash](</es/tools/slash-commands>), [Aprobaciones de ejecución](</es/tools/exec-approvals>)

iMessage y BlueBubbles - M3 Beta - 5 áreas

iMessage compatible se ejecuta mediante imsg en un host de Mensajes de macOS con sesión iniciada; las configuraciones heredadas de BlueBubbles requieren migración. Mantén visibles los permisos de macOS, el wrapper SSH, la API SIP/privada y las advertencias de migración.

Cobertura Experimental - 0%Calidad Alfa - 66%Integridad Beta - 78%Ninguna

Configuración y operaciones de canales 11 capacidades

Experimental0%

Alfa66%

Beta78%

[Bluebubbles iMessage](</es/announcements/bluebubbles-imessage>), [iMessage desde Bluebubbles](</es/channels/imessage-from-bluebubbles>), [Configurar canales](</es/gateway/config-channels>), [iMessage](</es/channels/imessage>)

Acceso e identidad 6 capacidades

Experimental0%

Alfa66%

Beta78%

[iMessage](</es/channels/imessage>), [iMessage desde Bluebubbles](</es/channels/imessage-from-bluebubbles>), [Configurar canales](</es/gateway/config-channels>)

Enrutamiento y entrega de conversaciones 4 capacidades

Experimental0%

Alfa66%

Beta78%

[iMessage](</es/channels/imessage>)

Medios y contenido enriquecido 7 capacidades

Experimental0%

Alfa66%

Beta78%

[iMessage](</es/channels/imessage>), [iMessage desde Bluebubbles](</es/channels/imessage-from-bluebubbles>), [Configurar canales](</es/gateway/config-channels>)

Controles nativos y aprobaciones 3 capacidades

Experimental0%

Alfa66%

Beta78%

[iMessage](</es/channels/imessage>)

WhatsApp - M3 Beta - 5 áreas

La ruta principal es importante y está documentada; la volatilidad de Baileys/sesiones upstream la mantiene por debajo de estable.

Cobertura Experimental - 0%Calidad Alfa - 66%Completitud Beta - 78%Ninguno

Configuración y operaciones de canales 5 capacidades

Experimental0%

Alpha66%

Beta78%

[WhatsApp](</es/channels/whatsapp>), [Configurar canales](</es/gateway/config-channels>), [WhatsApp](</es/plugins/reference/whatsapp>), [Automatización de QA E2E](</es/concepts/qa-e2e-automation>), [Doctor](</es/gateway/doctor>)

Acceso e identidad 7 capacidades

Experimental0%

Alpha66%

Beta78%

[WhatsApp](</es/channels/whatsapp>), [Configurar canales](</es/gateway/config-channels>), [Automatización de QA E2E](</es/concepts/qa-e2e-automation>), [Emparejamiento](</es/channels/pairing>)

Enrutamiento y entrega de conversaciones 4 capacidades

Experimental0%

Alpha66%

Beta78%

[WhatsApp](</es/channels/whatsapp>), [Mensajes de grupo](</es/channels/group-messages>)

Medios y contenido enriquecido 2 capacidades

Experimental0%

Alpha66%

Beta78%

[WhatsApp](</es/channels/whatsapp>)

Controles y aprobaciones nativos 2 capacidades

Experimental0%

Alpha66%

Beta78%

[WhatsApp](</es/channels/whatsapp>)

Matrix - M2 Alpha - 6 áreas

Compatible mediante Plugin incluido. Necesita cuadros de puntuación para puente, autenticación y ciclo de vida de salas.

Cobertura Experimental - 0%Calidad Alpha - 60%Completitud Alpha - 67%Ninguno

Configuración y operaciones de canales 5 capacidades

Experimental0%

Alpha60%

Alpha67%

[Matrix](</es/channels/matrix>), [Migración de Matrix](</es/channels/matrix-migration>)

Acceso e identidad 7 capacidades

Experimental0%

Alpha60%

Alpha67%

[Matrix](</es/channels/matrix>), [Grupos](</es/channels/groups>), [Protección contra bucles de bots](</es/channels/bot-loop-protection>)

Enrutamiento y entrega de conversaciones 1 capacidades

Experimental0%

Alpha60%

Alpha67%

[Matrix](</es/channels/matrix>)

Medios y contenido enriquecido 1 capacidades

Experimental0%

Alpha60%

Alpha67%

[Matrix](</es/channels/matrix>)

Controles y aprobaciones nativos 6 capacidades

Experimental0%

Alpha60%

Alpha67%

[Matrix](</es/channels/matrix>)

Cifrado y verificación 3 capacidades

Experimental0%

Alpha60%

Alpha67%

[Matrix](</es/channels/matrix>), [Migración de Matrix](</es/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 áreas

Canal documentado, pero la configuración empresarial/de administración aumenta el riesgo de madurez.

Cobertura Experimental - 0%Calidad Alpha - 59%Completitud Alpha - 66%Ninguna

Configuración y operaciones de canales 16 capacidades

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</es/channels/googlechat>), [Googlechat](</es/plugins/reference/googlechat>), [Configuración de canales](</es/gateway/config-channels>), [Referencia de CLI del asistente](</es/start/wizard-cli-reference>), [Secretos](</es/gateway/secrets>), [Superficie de credenciales Secretref](</es/reference/secretref-credential-surface>), [Salud](</es/gateway/health>), [Inventario de plugins](</es/plugins/plugin-inventory>), [Índice](</es/channels>)

Acceso e identidad 11 capacidades

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</es/channels/googlechat>), [Emparejamiento](</es/channels/pairing>), [Grupos de acceso](</es/channels/access-groups>), [Configuración de canales](</es/gateway/config-channels>), [Protección contra bucles de bots](</es/channels/bot-loop-protection>), [Enrutamiento de canales](</es/channels/channel-routing>)

Enrutamiento y entrega de conversaciones 1 capacidades

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</es/channels/googlechat>), [Protección contra bucles de bots](</es/channels/bot-loop-protection>), [Grupos de acceso](</es/channels/access-groups>), [Enrutamiento de canales](</es/channels/channel-routing>)

Medios y contenido enriquecido 1 capacidades

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</es/channels/googlechat>), [Mensaje](</es/cli/message>), [Comprensión de medios](</es/nodes/media-understanding>), [Superficie de credenciales Secretref](</es/reference/secretref-credential-surface>)

Controles y aprobaciones nativos 16 capacidades

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</es/channels/googlechat>), [Mensaje](</es/cli/message>), [Comprensión de medios](</es/nodes/media-understanding>), [Superficie de credenciales Secretref](</es/reference/secretref-credential-surface>), [Reacciones](</es/tools/reactions>), [Comandos de barra](</es/tools/slash-commands>), [Configuración de agentes](</es/gateway/config-agents>), [Refactorización del ciclo de vida de mensajes](</es/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alfa - 5 áreas

Los flujos empresariales de autenticación y administración necesitan prueba explícita de escenarios.

Cobertura Experimental - 0%Calidad Alfa - 59%Completitud Alfa - 66%Ninguna

Configuración y operaciones de canales 9 capacidades

Experimental0%

Alfa59%

Alfa66%

[Msteams](</es/channels/msteams>), [Msteams](</es/plugins/reference/msteams>), [Configuración de canales](</es/gateway/config-channels>), [Estado](</es/gateway/health>)

Acceso e identidad 9 capacidades

Experimental0%

Alfa59%

Alfa66%

[Msteams](</es/channels/msteams>), [Emparejamiento](</es/channels/pairing>), [Grupos de acceso](</es/channels/access-groups>)

Enrutamiento y entrega de conversaciones 5 capacidades

Experimental0%

Alfa59%

Alfa66%

[Msteams](</es/channels/msteams>), [Grupos](</es/channels/groups>), [Enrutamiento de canales](</es/channels/channel-routing>)

Contenido multimedia y enriquecido 5 capacidades

Experimental0%

Alfa59%

Alfa66%

[Msteams](</es/channels/msteams>)

Controles nativos y aprobaciones 5 capacidades

Experimental0%

Alfa59%

Alfa66%

[Msteams](</es/channels/msteams>), [Aprobaciones de ejecución avanzadas](</es/tools/exec-approvals-advanced>)

Signal - M2 Alfa - 5 áreas

Existe documentación del canal compatible; necesita pruebas más sólidas de instalación y reconexión.

Cobertura Experimental - 0%Calidad Alfa - 59%Completitud Alfa - 66%Ninguno

Configuración y operaciones de canales 7 capacidades

Experimental0%

Alpha59%

Alpha66%

[Signal](</es/channels/signal>), [Signal](</es/plugins/reference/signal>)

Acceso e identidad 6 capacidades

Experimental0%

Alpha59%

Alpha66%

[Signal](</es/channels/signal>)

Enrutamiento y entrega de conversaciones 1 capacidad

Experimental0%

Alpha59%

Alpha66%

[Signal](</es/channels/signal>)

Medios y contenido enriquecido 7 capacidades

Experimental0%

Alpha59%

Alpha66%

[Signal](</es/channels/signal>)

Controles nativos y aprobaciones 3 capacidades

Experimental0%

Alpha59%

Alpha66%

[Signal](</es/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canales regionales - M2 Alpha - 4 áreas

Cobertura regional importante, pero el nivel de soporte público debe calibrarse según el tipo de cuenta, la aprobación upstream y la prueba de mantenedores.

Cobertura Experimental - 0%Calidad Alpha - 55%Completitud Alpha - 58%Ninguno

Configuración y operaciones de canales 6 capacidades

Experimental0%

Alpha61%

Alpha68%

[Índice](</es/channels>), [Emparejamiento](</es/channels/pairing>), [Feishu](</es/plugins/reference/feishu>), [Internos de arquitectura](</es/plugins/architecture-internals>)

Acceso e identidad 1 capacidad

Experimental0%

Alpha53%

Alpha54%

Sin documentación vinculada

Enrutamiento y entrega de conversaciones 1 capacidad

Experimental0%

Alpha53%

Alpha54%

Sin documentación vinculada

Medios y contenido enriquecido 1 capacidad

Experimental0%

Alpha53%

Alpha54%

Sin documentación vinculada

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 áreas

Existen superficies compatibles, pero la madurez probablemente varía según la cobertura del proveedor upstream y del mantenedor. Puntuar individualmente más adelante.

Cobertura Experimental - 0%Calidad Alpha - 53%Integridad Alpha - 54%Ninguna

Configuración y operaciones de canal 1 capacidades

Experimental0%

Alfa53%

Alfa54%

Sin documentación enlazada

Acceso e identidad 1 capacidades

Experimental0%

Alfa53%

Alfa54%

Sin documentación enlazada

Enrutamiento y entrega de conversaciones 1 capacidades

Experimental0%

Alfa53%

Alfa54%

Sin documentación enlazada

Medios y contenido enriquecido 1 capacidades

Experimental0%

Alfa53%

Alfa54%

Sin documentación enlazada

Canal de llamadas de voz - M1 Experimental - 5 áreas

Ruta opcional/de plugin con comportamiento complejo en tiempo real. Necesita una tarjeta de puntuación de escenarios antes de la beta pública.

Cobertura Experimental - 0%Calidad Experimental - 41%Completitud Experimental - 44%Ninguno

Configuración y operaciones de canales 2 capacidades

Experimental0%

Experimental41%

Experimental44%

[Llamada de voz](</es/cli/voicecall>), [Llamada de voz](</es/plugins/voice-call>), [Protocolo](</es/gateway/protocol>)

Acceso e identidad 1 capacidad

Experimental0%

Experimental41%

Experimental44%

[Llamada de voz](</es/plugins/voice-call>), [Llamada de voz](</es/cli/voicecall>)

Enrutamiento y entrega de conversaciones 1 capacidad

Experimental0%

Experimental41%

Experimental44%

[Llamada de voz](</es/plugins/voice-call>)

Multimedia y contenido enriquecido 2 capacidades

Experimental0%

Experimental41%

Experimental44%

[Llamada de voz](</es/plugins/voice-call>), [Inventario de Plugins](</es/plugins/plugin-inventory>)

Voz y llamadas en tiempo real 2 capacidades

Experimental0%

Experimental41%

Experimental44%

[Llamada de voz](</es/plugins/voice-call>)

### Proveedor y herramienta

Automatización del navegador, exec y herramientas de sandbox - M3 Beta - 3 áreas

Las herramientas principales están documentadas, pero la seguridad del host y la experiencia de usuario de permisos deben permanecer bajo revisión activa del cuadro de mando.

Cobertura Experimental - 21%Calidad Beta - 75%Completitud Beta - 79%Parcial - 2

Automatización del navegador 8 capacidades

Experimental13%

Beta79%

Beta79%

[Control del navegador](</es/tools/browser-control>), [Pruebas](</es/help/testing>), [Navegador](</es/tools/browser>), [Índice](</es/gateway/security>), [Comprobaciones de auditoría](</es/gateway/security/audit-checks>)

Invocación y ejecución de herramientas 6 capacidades / compatibles con LTS

Alpha50%

Beta79%

Beta79%

[Exec](</es/tools/exec>), [Proceso en segundo plano](</es/gateway/background-process>), [API HTTP de invocación de herramientas](</es/gateway/tools-invoke-http-api>), [Ámbitos de operador](</es/gateway/operator-scopes>), [Protocolo](</es/gateway/protocol>), [Aprobaciones de Exec](</es/tools/exec-approvals>), [Aprobaciones avanzadas de Exec](</es/tools/exec-approvals-advanced>), [Elevado](</es/tools/elevated>)

Sandbox y política de herramientas 6 capacidades / compatibles con LTS

Experimental0%

Alpha68%

Beta79%

[Sandboxing](</es/gateway/sandboxing>), [Sandbox frente a política de herramientas frente a elevado](</es/gateway/sandbox-vs-tool-policy-vs-elevated>), [Herramientas de sandbox multiagente](</es/tools/multi-agent-sandbox-tools>), [Referencia del arnés de Codex](</es/plugins/codex-harness-reference>), [Herramientas de configuración](</es/gateway/config-tools>)

Ruta de proveedores de OpenAI y Codex - M3 Beta - 5 áreas

Documentación profunda, ruta de OAuth/suscripción, voz en tiempo real, imagen y comportamiento de compatibilidad. La rotación de proveedores impide que esto sea Stable sin prueba del scorecard de lanzamiento.

Cobertura Experimental - 26%Calidad Beta - 74%Integridad Beta - 79%Parcial - 3

Modelo y autenticación 6 capacidades / compatible con LTS

Experimental44%

Beta79%

Beta79%

[Openai](</es/providers/openai>), [Arnés Codex](</es/plugins/codex-harness>), [Modelos](</es/concepts/models>), [Oauth](</es/concepts/oauth>), [Referencia del arnés Codex](</es/plugins/codex-harness-reference>), [Supervisión de autenticación](</es/gateway/authentication>)

Compatibilidad de respuestas y herramientas 4 capacidades / compatible con LTS

Experimental40%

Beta79%

Beta79%

[Openai](</es/providers/openai>), [API HTTP de Openresponses](</es/gateway/openresponses-http-api>), [API HTTP de Openai](</es/gateway/openai-http-api>), [Plugins nativos de Codex](</es/plugins/codex-native-plugins>)

Arnés nativo de Codex 2 capacidades / compatible con LTS

Experimental44%

Beta79%

Beta79%

[Arnés Codex](</es/plugins/codex-harness>), [Runtime del arnés Codex](</es/plugins/codex-harness-runtime>), [Referencia del arnés Codex](</es/plugins/codex-harness-reference>), [Plugins nativos de Codex](</es/plugins/codex-native-plugins>)

Entrada de imagen y multimodal 2 capacidades

Experimental0%

Alpha67%

Beta79%

[Openai](</es/providers/openai>), [Generación de imágenes](</es/tools/image-generation>), [Imágenes](</es/nodes/images>)

Voz y audio en tiempo real 2 capacidades

Experimental0%

Alpha67%

Beta79%

[Openai](</es/providers/openai>), [Discord](</es/channels/discord>), [Llamada de voz](</es/plugins/voice-call>)

Herramientas de búsqueda web - M3 Beta - 4 áreas

Existen varios proveedores y documentación. Necesita prueba de cuota/error/SSRF por familia de proveedores.

Cobertura Experimental - 9%Calidad Beta - 74%Integridad Beta - 79%Ninguna

Proveedores de búsqueda 19 capacidades

Experimental11%

Beta79%

Beta79%

[Web](</es/tools/web>), [Brave Search](</es/tools/brave-search>), [Tavily](</es/tools/tavily>), [Exa Search](</es/tools/exa-search>), [Firecrawl](</es/tools/firecrawl>), [Perplexity Search](</es/tools/perplexity-search>), [Duckduckgo Search](</es/tools/duckduckgo-search>), [Searxng Search](</es/tools/searxng-search>), [Gemini Search](</es/tools/gemini-search>), [Grok Search](</es/tools/grok-search>), [Kimi Search](</es/tools/kimi-search>), [Minimax Search](</es/tools/minimax-search>), [Ollama Search](</es/tools/ollama-search>), [Subrutas de Sdk](</es/plugins/sdk-subpaths>), [Resumen de Sdk](</es/plugins/sdk-overview>), [Manifiesto](</es/plugins/manifest>)

Configuración y diagnóstico 9 capacidades

Experimental0%

Alpha68%

Beta79%

[Web](</es/tools/web>), [Obtención web](</es/tools/web-fetch>), [Preguntas frecuentes](</es/help/faq>), [Costos de uso de la API](</es/reference/api-usage-costs>), [Brave Search](</es/tools/brave-search>), [Perplexity Search](</es/tools/perplexity-search>), [Tavily](</es/tools/tavily>), [Firecrawl](</es/tools/firecrawl>)

Seguridad de red 4 capacidades

Experimental0%

Alpha68%

Beta79%

[Web](</es/tools/web>), [Obtención web](</es/tools/web-fetch>), [Firecrawl](</es/tools/firecrawl>), [Searxng Search](</es/tools/searxng-search>)

Disponibilidad y obtención de herramientas 11 capacidades

Experimental25%

Beta79%

Beta79%

[Herramientas de configuración](</es/gateway/config-tools>), [Obtención web](</es/tools/web-fetch>), [Web](</es/tools/web>), [Preguntas frecuentes](</es/help/faq>)

Ruta de proveedor Anthropic - M3 Beta - 5 áreas

Proveedor de modelos de primera clase. Necesita pruebas recurrentes de escenarios de autenticación, catálogo y llamadas a herramientas.

Cobertura Experimental - 0%Calidad Beta - 71%Integridad Beta - 78%Ninguno

Autenticación y recuperación de proveedores 9 capacidades

Experimental0%

Alpha66%

Beta78%

[Anthropic](</es/providers/anthropic>), [Doctor](</es/gateway/doctor>), [Ejemplos de configuración](</es/gateway/configuration-examples>), [Solución de problemas](</es/gateway/troubleshooting>), [Almacenamiento en caché de prompts](</es/reference/prompt-caching>)

Selección de modelos y runtime 10 capacidades

Experimental0%

Beta78%

Beta79%

[Anthropic](</es/providers/anthropic>), [Configurar agentes](</es/gateway/config-agents>), [Modelos](</es/concepts/models>), [Backends de CLI](</es/gateway/cli-backends>)

Transporte de solicitudes y semántica de turnos 10 capacidades

Experimental0%

Beta77%

Beta79%

[Anthropic](</es/providers/anthropic>), [Almacenamiento en caché de prompts](</es/reference/prompt-caching>), [Solución de problemas](</es/gateway/troubleshooting>), [Backends de CLI](</es/gateway/cli-backends>), [Proveedores de modelos](</es/concepts/model-providers>)

Caché de prompts y contexto 5 capacidades

Experimental0%

Alpha66%

Beta78%

[Anthropic](</es/providers/anthropic>), [Almacenamiento en caché de prompts](</es/reference/prompt-caching>), [Solución de problemas](</es/gateway/troubleshooting>), [Heartbeat](</es/gateway/heartbeat>)

Entradas multimedia 4 capacidades

Experimental0%

Alpha66%

Beta78%

[Anthropic](</es/providers/anthropic>), [Configurar agentes](</es/gateway/config-agents>)

Ruta del proveedor Google - M3 Beta - 5 áreas

Proveedor de primera clase con superficies de modelo y tiempo real. Necesita puntuación separada para Live/Talk.

Cobertura Experimental - 0%Calidad Alpha - 66%Integridad Beta - 78%Ninguno

Configuración de proveedores y credenciales 10 capacidades

Experimental0%

Alpha66%

Beta78%

[Google](</es/providers/google>), [Proveedores de modelos](</es/concepts/model-providers>)

Enrutamiento de modelos y endpoints 10 capacidades

Experimental0%

Alpha66%

Beta78%

[Google](</es/providers/google>), [Proveedores de modelos](</es/concepts/model-providers>), [Google](</es/plugins/reference/google>), [Búsqueda de Gemini](</es/tools/gemini-search>)

Runtime directo de Gemini 9 capacidades

Experimental0%

Alpha66%

Beta78%

[Google](</es/providers/google>), [Proveedores de modelos](</es/concepts/model-providers>), [Preguntas frecuentes sobre modelos](</es/help/faq-models>), [Pruebas en vivo](</es/help/testing-live>)

Multimedia, búsqueda y tiempo real 10 capacidades

Experimental0%

Alpha66%

Beta78%

[Google](</es/plugins/reference/google>), [Google](</es/providers/google>)

Almacenamiento en caché de prompts 5 capacidades

Experimental0%

Alpha66%

Beta78%

[Almacenamiento en caché de prompts](</es/reference/prompt-caching>), [Google](</es/providers/google>), [Proveedores de modelos](</es/concepts/model-providers>), [Uso de tokens](</es/reference/token-use>)

Ruta del proveedor OpenRouter - M3 Beta - 4 áreas

La ruta unificada de proveedores está documentada y es valiosa, pero el comportamiento específico de cada modelo varía.

Cobertura Experimental - 0%Calidad Alpha - 66%Completitud Beta - 78%Ninguno

Configuración y autenticación de proveedores 14 capacidades

Experimental0%

Alfa66%

Beta78%

[Openrouter](</es/providers/openrouter>), [Proveedores de modelos](</es/concepts/model-providers>), [Configurar](</es/cli/configure>), [Autenticación](</es/gateway/authentication>), [Entorno](</es/help/environment>), [Modelos](</es/cli/models>), [Modelos](</es/concepts/models>)

Runtime de chat y normalización 15 capacidades

Experimental0%

Alfa66%

Beta78%

[Openrouter](</es/providers/openrouter>), [Proveedores de modelos](</es/concepts/model-providers>), [Caché de prompts](</es/reference/prompt-caching>)

Recuperación y diagnóstico de proveedores 5 capacidades

Experimental0%

Alfa66%

Beta78%

[Conmutación por error de modelos](</es/concepts/model-failover>), [Openrouter](</es/providers/openrouter>), [Modelos](</es/cli/models>)

Generación de medios y voz 7 capacidades

Experimental0%

Alfa66%

Beta78%

[Openrouter](</es/providers/openrouter>), [Generación de imágenes](</es/tools/image-generation>), [Generación de música](</es/tools/music-generation>), [Resumen de medios](</es/tools/media-overview>), [Generación de video](</es/tools/video-generation>), [Tts](</es/tools/tts>)

Image, video, and music generation tools - M2 Alpha - 5 areas

La capacidad existe en todos los proveedores, pero la calidad, la latencia y la compatibilidad de parámetros varían demasiado para beta sin pruebas por proveedor.

Cobertura experimental - 0%Calidad Alpha - 61%Completitud Alpha - 68%Ninguno

Enrutamiento y descubrimiento de medios 4 capacidades

Experimental0%

Alfa61%

Alfa68%

[Agentes de configuración](</es/gateway/config-agents>), [Generación de imágenes](</es/tools/image-generation>), [Generación de video](</es/tools/video-generation>), [Generación de música](</es/tools/music-generation>)

Ciclo de vida y entrega de tareas 12 capacidades

Experimental0%

Alfa61%

Alfa68%

[Resumen de medios](</es/tools/media-overview>), [Generación de imágenes](</es/tools/image-generation>), [Generación de video](</es/tools/video-generation>), [Generación de música](</es/tools/music-generation>)

Generación de imágenes 9 capacidades

Experimental0%

Alfa61%

Alfa68%

[Generación de imágenes](</es/tools/image-generation>), [Infer](</es/cli/infer>), [Resumen de medios](</es/tools/media-overview>)

Generación de video 11 capacidades

Experimental0%

Alfa61%

Alfa68%

[Generación de video](</es/tools/video-generation>), [Runway](</es/providers/runway>), [Pixverse](</es/providers/pixverse>), [Fal](</es/providers/fal>), [Openrouter](</es/providers/openrouter>)

Generación de música 6 capacidades

Experimental0%

Alfa61%

Alfa68%

[Generación de música](</es/tools/music-generation>)

Proveedores de modelos locales: Ollama, vLLM, SGLang, LM Studio - M2 Alfa - 5 áreas

Útil y documentado, pero la variación entre entornos es alta.

Cobertura Experimental - 0%Calidad Alfa - 61%Completitud Alfa - 68%Ninguno

Configuración, ciclo de vida y diagnósticos de proveedores 12 capacidades

Experimental0%

Alpha61%

Alpha68%

[Modelos locales](</es/gateway/local-models>), [Lmstudio](</es/providers/lmstudio>), [Ollama](</es/providers/ollama>), [Vllm](</es/providers/vllm>), [Servicios de modelos locales](</es/gateway/local-model-services>), [Configurar agentes](</es/gateway/config-agents>), [Solución de problemas](</es/gateway/troubleshooting>), [Doctor](</es/gateway/doctor>)

Plugins de proveedores nativos 10 capacidades

Experimental0%

Alpha61%

Alpha68%

[Ollama](</es/providers/ollama>), [Lmstudio](</es/providers/lmstudio>)

Compatibilidad del runtime compatible con OpenAI 8 capacidades

Experimental0%

Alpha61%

Alpha68%

[Vllm](</es/providers/vllm>), [Sglang](</es/providers/sglang>), [Modelos locales](</es/gateway/local-models>), [Lmstudio](</es/providers/lmstudio>)

Memoria local e incrustaciones 5 capacidades

Experimental0%

Alpha61%

Alpha68%

[Memoria](</es/concepts/memory>), [Doctor](</es/gateway/doctor>)

Seguridad de red y controles de prompts 2 capacidades

Experimental0%

Alpha61%

Alpha68%

[Índice](</es/gateway/security>), [Configurar herramientas](</es/gateway/config-tools>), [Modelos locales](</es/gateway/local-models>)

Proveedores alojados de larga cola - M2 Alpha - 3 áreas

Existen muchas páginas de documentación/referencia; la puntuación debe generarse a partir de los metadatos de proveedores más la cobertura de pruebas de humo en vivo.

Cobertura Experimental - 0%Calidad Alfa - 61%Completitud Alfa - 68%Ninguno

Proveedores de LLM alojados 12 capacidades

Experimental0%

Alfa61%

Alfa68%

[Índice](</es/providers>), [Proveedores de modelos](</es/concepts/model-providers>), [Pruebas en vivo](</es/help/testing-live>), [Incorporación](</es/cli/onboard>)

Proveedores de medios alojados 8 capacidades

Experimental0%

Alfa61%

Alfa68%

[Manifiesto](</es/plugins/manifest>), [Pruebas en vivo](</es/help/testing-live>), [Índice](</es/providers>)

Operaciones de proveedores 12 capacidades

Experimental0%

Alfa61%

Alfa68%

[Índice](</es/providers>), [Proveedores de modelos](</es/concepts/model-providers>), [Manifiesto](</es/plugins/manifest>), [Pruebas en vivo](</es/help/testing-live>), [Modelos](</es/cli/models>)

Was this useful?YesNo

Open issue