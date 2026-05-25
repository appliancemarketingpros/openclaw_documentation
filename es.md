---
title: OpenClaw
source_url: https://docs.openclaw.ai/es
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"¡EXFOLIA! ¡EXFOLIA!"_ — Una langosta espacial, probablemente

**Gateway para cualquier sistema operativo para agentes de IA en Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo y más.**

Envía un mensaje y recibe una respuesta del agente desde tu bolsillo. Ejecuta un Gateway en canales integrados, plugins de canal incluidos, WebChat y nodos móviles.

[**Primeros pasos** Instala OpenClaw y pon en marcha el Gateway en minutos. ](</es/start/getting-started>) [**Ejecutar la incorporación** Configuración guiada con `openclaw onboard` y flujos de emparejamiento. ](</es/start/wizard>) [**Abrir la interfaz de control** Inicia el panel del navegador para chat, configuración y sesiones. ](</es/web/control-ui>)

## ¿Qué es OpenClaw?

OpenClaw es un **gateway autohospedado** que conecta tus aplicaciones de chat y superficies de canal favoritas —canales integrados más plugins de canal incluidos o externos como Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo y más— con agentes de codificación de IA como Pi. Ejecutas un único proceso Gateway en tu propia máquina (o en un servidor), y se convierte en el puente entre tus aplicaciones de mensajería y un asistente de IA siempre disponible.

**¿Para quién es?** Para desarrolladores y usuarios avanzados que quieren un asistente personal de IA al que puedan enviar mensajes desde cualquier lugar, sin ceder el control de sus datos ni depender de un servicio alojado.

**¿Qué lo hace diferente?**

  * **Autohospedado** : se ejecuta en tu hardware, con tus reglas
  * **Multicanal** : un Gateway sirve simultáneamente canales integrados más plugins de canal incluidos o externos
  * **Nativo para agentes** : creado para agentes de codificación con uso de herramientas, sesiones, memoria y enrutamiento multiagente
  * **Código abierto** : con licencia MIT e impulsado por la comunidad


**¿Qué necesitas?** Node 24 (recomendado), o Node 22 LTS (`22.16+`) para compatibilidad, una clave de API de tu proveedor elegido y 5 minutos. Para obtener la mejor calidad y seguridad, usa el modelo de última generación más potente disponible.

## Cómo funciona
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

El Gateway es la única fuente de verdad para sesiones, enrutamiento y conexiones de canales.

## Capacidades clave

[**Gateway multicanal** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat y más con un único proceso Gateway. ](</es/channels>) [**Canales de Plugin** Los plugins incluidos añaden Matrix, Nostr, Twitch, Zalo y más en las versiones actuales normales. ](</es/tools/plugin>) [**Enrutamiento multiagente** Sesiones aisladas por agente, espacio de trabajo o remitente. ](</es/concepts/multi-agent>) [**Soporte multimedia** Envía y recibe imágenes, audio y documentos. ](</es/nodes/images>) [**Interfaz de control web** Panel del navegador para chat, configuración, sesiones y nodos. ](</es/web/control-ui>) [**Nodos móviles** Empareja nodos iOS y Android para Canvas, cámara y flujos de trabajo con voz. ](</es/nodes>)

## Inicio rápido

* ### Instalar OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Incorporar e instalar el servicio

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Chatear

Abre la interfaz de control en tu navegador y envía un mensaje:

bashCopy code
[code]
    openclaw dashboard
[/code]

O conecta un canal ([Telegram](</es/channels/telegram>) es el más rápido) y chatea desde tu teléfono.

¿Necesitas la instalación completa y la configuración de desarrollo? Consulta [Primeros pasos](</es/start/getting-started>).

## Panel

Abre la interfaz de control en el navegador después de que se inicie el Gateway.

  * Valor local predeterminado: <http://127.0.0.1:18789/>
  * Acceso remoto: [Superficies web](</es/web>) y [Tailscale](</es/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Configuración (opcional)

La configuración se encuentra en `~/.openclaw/openclaw.json`.

  * Si **no haces nada** , OpenClaw usa el binario Pi incluido en modo RPC con sesiones por remitente.
  * Si quieres restringirlo, empieza con `channels.whatsapp.allowFrom` y (para grupos) reglas de mención.


Ejemplo:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Empieza aquí

[**Centros de documentación** Toda la documentación y las guías, organizadas por caso de uso. ](</es/start/hubs>) [**Configuración** Ajustes principales del Gateway, tokens y configuración del proveedor. ](</es/gateway/configuration>) [**Acceso remoto** Patrones de acceso SSH y tailnet. ](</es/gateway/remote>) [**Canales** Configuración específica de canal para Feishu, Microsoft Teams, WhatsApp, Telegram, Discord y más. ](</es/channels/telegram>) [**Nodos** Nodos iOS y Android con emparejamiento, Canvas, cámara y acciones de dispositivo. ](</es/nodes>) [**Ayuda** Punto de entrada para soluciones comunes y resolución de problemas. ](</es/help>)

## Más información

[**Lista completa de funciones** Capacidades completas de canales, enrutamiento y multimedia. ](</es/concepts/features>) [**Enrutamiento multiagente** Aislamiento de espacios de trabajo y sesiones por agente. ](</es/concepts/multi-agent>) [**Seguridad** Tokens, listas de permitidos y controles de seguridad. ](</es/gateway/security>) [**Resolución de problemas** Diagnósticos del Gateway y errores comunes. ](</es/gateway/troubleshooting>) [**Acerca de y créditos** Orígenes del proyecto, colaboradores y licencia. ](</es/reference/credits>)

Was this useful?YesNo