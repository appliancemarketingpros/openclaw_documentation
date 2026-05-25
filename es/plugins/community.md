---
title: Plugins de la comunidad
source_url: https://docs.openclaw.ai/es/plugins/community
scraped_at: 2026-05-25
---

Los plugins de la comunidad son paquetes de terceros que extienden OpenClaw con nuevos canales, herramientas, proveedores u otras capacidades. La comunidad los crea y mantiene; normalmente se publican en [ClawHub](</es/clawhub>) y se instalan con un solo comando. Npm sigue siendo el valor predeterminado de lanzamiento para especificaciones de paquete simples mientras se despliegan las instalaciones de paquetes de ClawHub.

ClawHub es la superficie canónica de descubrimiento para plugins de la comunidad. No abras PRs solo de documentación únicamente para agregar tu plugin aquí con fines de descubrimiento; publícalo en ClawHub en su lugar.

bashCopy code
[code]
    openclaw plugins install clawhub:<package-name>
[/code]

Usa `openclaw plugins install <package-name>` para paquetes alojados en npm.

## Plugins listados

### Apify

Extrae datos de cualquier sitio web con más de 20.000 scrapers listos para usar. Permite que tu agente extraiga datos de Instagram, Facebook, TikTok, YouTube, Google Maps, Google Search, sitios de comercio electrónico y más, solo con pedirlo.

  * **npm:** `@apify/apify-openclaw-plugin`
  * **repositorio:** [github.com/apify/apify-openclaw-plugin](<https://github.com/apify/apify-openclaw-plugin>)

bashCopy code
[code]
    openclaw plugins install @apify/apify-openclaw-plugin
[/code]

### Codex App Server Bridge

Puente independiente de OpenClaw para conversaciones de Codex App Server. Vincula un chat a un hilo de Codex, habla con él usando texto sin formato y contrólalo con comandos nativos del chat para reanudar, planificar, revisar, seleccionar modelo, Compaction y más.

  * **npm:** `openclaw-codex-app-server`
  * **repositorio:** [github.com/pwrdrvr/openclaw-codex-app-server](<https://github.com/pwrdrvr/openclaw-codex-app-server>)

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

### DingTalk

Integración de robot empresarial usando modo Stream. Admite mensajes de texto, imágenes y archivos mediante cualquier cliente de DingTalk.

  * **npm:** `@largezhou/ddingtalk`
  * **repositorio:** [github.com/largezhou/openclaw-dingtalk](<https://github.com/largezhou/openclaw-dingtalk>)

bashCopy code
[code]
    openclaw plugins install @largezhou/ddingtalk
[/code]

### Lossless Claw (LCM)

Plugin Lossless Context Management para OpenClaw. Resumen de conversaciones basado en DAG con Compaction incremental: conserva la fidelidad completa del contexto mientras reduce el uso de tokens.

  * **npm:** `@martian-engineering/lossless-claw`
  * **repositorio:** [github.com/Martian-Engineering/lossless-claw](<https://github.com/Martian-Engineering/lossless-claw>)

bashCopy code
[code]
    openclaw plugins install @martian-engineering/lossless-claw
[/code]

### Opik

Plugin oficial que exporta trazas de agentes a Opik. Supervisa el comportamiento del agente, el costo, los tokens, los errores y más.

  * **npm:** `@opik/opik-openclaw`
  * **repositorio:** [github.com/comet-ml/opik-openclaw](<https://github.com/comet-ml/opik-openclaw>)

bashCopy code
[code]
    openclaw plugins install @opik/opik-openclaw
[/code]

### Prometheus Avatar

Dale a tu agente de OpenClaw un avatar Live2D con sincronización labial en tiempo real, expresiones de emoción y texto a voz. Incluye herramientas de creación para generación de recursos con IA y despliegue con un clic en Prometheus Marketplace. Actualmente está en alfa.

  * **npm:** `@prometheusavatar/openclaw-plugin`
  * **repositorio:** [github.com/myths-labs/prometheus-avatar](<https://github.com/myths-labs/prometheus-avatar>)

bashCopy code
[code]
    openclaw plugins install @prometheusavatar/openclaw-plugin
[/code]

### QQbot

Conecta OpenClaw a QQ mediante la QQ Bot API. Admite chats privados, menciones de grupo, mensajes de canal y medios enriquecidos, incluidos voz, imágenes, videos y archivos.

Las versiones actuales de OpenClaw incluyen QQ Bot. Usa la configuración incluida en [QQ Bot](</es/channels/qqbot>) para instalaciones normales; instala este plugin externo solo cuando quieras intencionadamente el paquete independiente mantenido por Tencent.

  * **npm:** `@tencent-connect/openclaw-qqbot`
  * **repositorio:** [github.com/tencent-connect/openclaw-qqbot](<https://github.com/tencent-connect/openclaw-qqbot>)

bashCopy code
[code]
    openclaw plugins install @tencent-connect/openclaw-qqbot
[/code]

### wecom

Plugin de canal WeCom para OpenClaw del equipo Tencent WeCom. Impulsado por conexiones persistentes WebSocket de WeCom Bot, admite mensajes directos y chats de grupo, respuestas en streaming, mensajería proactiva, procesamiento de imágenes/archivos, formato Markdown, control de acceso integrado y Skills de documentos/reuniones/mensajería.

  * **npm:** `@wecom/wecom-openclaw-plugin`
  * **repositorio:** [github.com/WecomTeam/wecom-openclaw-plugin](<https://github.com/WecomTeam/wecom-openclaw-plugin>)

bashCopy code
[code]
    openclaw plugins install @wecom/wecom-openclaw-plugin
[/code]

### Yuanbao

Plugin de canal Yuanbao para OpenClaw del equipo Tencent Yuanbao. Impulsado por conexiones persistentes WebSocket, admite mensajes directos y chats de grupo, respuestas en streaming, mensajería proactiva, procesamiento de imágenes/archivos/audio/video, formato Markdown, control de acceso integrado y menús de comandos slash.

  * **npm:** `openclaw-plugin-yuanbao`
  * **repositorio:** [github.com/YuanbaoTeam/yuanbao-openclaw-plugin](<https://github.com/YuanbaoTeam/yuanbao-openclaw-plugin>)

bashCopy code
[code]
    openclaw plugins install openclaw-plugin-yuanbao
[/code]

## Envía tu plugin

Damos la bienvenida a plugins de la comunidad que sean útiles, estén documentados y sean seguros de operar.

* ### Publica en ClawHub o npm

Tu plugin debe poder instalarse mediante `openclaw plugins install \<package-name\>`. Publícalo en [ClawHub](</es/clawhub>), salvo que necesites específicamente una distribución solo por npm. Consulta [Crear Plugins](</es/plugins/building-plugins>) para la guía completa.

* ### Alójalo en GitHub

El código fuente debe estar en un repositorio público con documentación de configuración y un rastreador de incidencias.

* ### Usa PRs de documentación solo para cambios en la documentación fuente

No necesitas un PR de documentación solo para hacer que tu plugin sea descubrible. Publícalo en ClawHub en su lugar.

Abre un PR de documentación solo cuando la documentación fuente de OpenClaw necesite un cambio de contenido real, como corregir instrucciones de instalación o agregar documentación entre repositorios que pertenezca al conjunto principal de documentación.

## Nivel de calidad

Requisito | Por qué  
---|---  
Publicado en ClawHub o npm | Los usuarios necesitan que `openclaw plugins install` funcione  
Repositorio público de GitHub | Revisión de código, seguimiento de incidencias, transparencia  
Documentación de configuración y uso | Los usuarios necesitan saber cómo configurarlo  
Mantenimiento activo | Actualizaciones recientes o gestión receptiva de incidencias  
  
Los envoltorios de bajo esfuerzo, la propiedad poco clara o los paquetes sin mantenimiento pueden rechazarse.

## Relacionado

  * [Instalar y Configurar Plugins](</es/tools/plugin>) — cómo instalar cualquier plugin
  * [Crear Plugins](</es/plugins/building-plugins>) — crea el tuyo
  * [Manifiesto de Plugin](</es/plugins/manifest>) — esquema del manifiesto


Was this useful?YesNo