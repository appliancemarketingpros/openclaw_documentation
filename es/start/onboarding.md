---
title: Configuración inicial (aplicación para macOS)
source_url: https://docs.openclaw.ai/es/start/onboarding
scraped_at: 2026-05-25
---

Este documento describe el flujo de configuración de primer uso **actual**. El objetivo es una experiencia fluida de "día 0": elegir dónde se ejecuta el Gateway, conectar la autenticación, ejecutar el asistente y dejar que el agente se inicialice por sí mismo. Para una descripción general de las rutas de incorporación, consulta [Descripción general de la incorporación](</es/start/onboarding-overview>).

* ### Aprobar advertencia de macOS

![](/assets/macos-onboarding/01-macos-warning.jpeg)
* ### Aprobar búsqueda de redes locales

![](/assets/macos-onboarding/02-local-networks.jpeg)
* ### Bienvenida y aviso de seguridad

Lee el aviso de seguridad mostrado y decide en consecuencia ![](/assets/macos-onboarding/03-security-notice.png)

Modelo de confianza de seguridad:

  * De forma predeterminada, OpenClaw es un agente personal: un único límite de operador de confianza.
  * Las configuraciones compartidas/multiusuario requieren endurecimiento (separar límites de confianza, mantener el acceso a herramientas al mínimo y seguir [Seguridad](</es/gateway/security>)).
  * La incorporación local ahora establece de forma predeterminada las configuraciones nuevas en `tools.profile: "coding"` para que las configuraciones locales nuevas mantengan las herramientas de sistema de archivos/runtime sin forzar el perfil `full` sin restricciones.
  * Si se habilitan hooks/webhooks u otros feeds de contenido no confiable, usa un nivel de modelo moderno y potente, y mantén una política de herramientas/sandboxing estricta.


* ### Local vs remoto

![](/assets/macos-onboarding/04-choose-gateway.png)

¿Dónde se ejecuta el **Gateway**?

  * **Este Mac (solo local):** la incorporación puede configurar la autenticación y escribir credenciales localmente.
  * **Remoto (por SSH/Tailnet):** la incorporación **no** configura la autenticación local; las credenciales deben existir en el host del gateway.
  * **Configurar más tarde:** omite la configuración y deja la app sin configurar.


* ### Permisos

Elige qué permisos quieres conceder a OpenClaw ![](/assets/macos-onboarding/05-permissions.png)

La incorporación solicita los permisos de TCC necesarios para:

  * Automatización (AppleScript)
  * Notificaciones
  * Accesibilidad
  * Grabación de pantalla
  * Micrófono
  * Reconocimiento de voz
  * Cámara
  * Ubicación


* ### CLI

* ### Chat de incorporación (sesión dedicada)

Después de la configuración, la app abre una sesión de chat de incorporación dedicada para que el agente pueda presentarse y guiar los siguientes pasos. Esto mantiene la guía de primer uso separada de tu conversación normal. Consulta [Inicialización](</es/start/bootstrapping>) para saber qué ocurre en el host del gateway durante la primera ejecución del agente.

## Relacionado

  * [Descripción general de la incorporación](</es/start/onboarding-overview>)
  * [Primeros pasos](</es/start/getting-started>)


Was this useful?YesNo