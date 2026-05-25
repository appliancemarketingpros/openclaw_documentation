---
title: Hostinger
source_url: https://docs.openclaw.ai/es/install/hostinger
scraped_at: 2026-05-25
---

Ejecuta un Gateway persistente de OpenClaw en [Hostinger](<https://www.hostinger.com/openclaw>) mediante un despliegue gestionado **1-Clic** o una instalación en **VPS**.

## Requisitos previos

  * Cuenta de Hostinger ([registro](<https://www.hostinger.com/openclaw>))
  * Aproximadamente 5-10 minutos


## Opción A: OpenClaw con 1-Clic

La forma más rápida de empezar. Hostinger se encarga de la infraestructura, Docker y las actualizaciones automáticas.

* ### Comprar y lanzar

  1. En la [página de OpenClaw de Hostinger](<https://www.hostinger.com/openclaw>), elige un plan de OpenClaw gestionado y completa la compra.


* ### Seleccionar un canal de mensajería

Elige uno o varios canales para conectar:

  * **WhatsApp** \-- escanea el código QR que se muestra en el asistente de configuración.
  * **Telegram** \-- pega el token del bot de [BotFather](<https://t.me/BotFather>).


* ### Completar la instalación

Haz clic en **Finish** para desplegar la instancia. Cuando esté lista, accede al dashboard de OpenClaw desde **OpenClaw Overview** en hPanel.

## Opción B: OpenClaw en VPS

Más control sobre tu servidor. Hostinger despliega OpenClaw mediante Docker en tu VPS y tú lo gestionas a través de **Docker Manager** en hPanel.

* ### Comprar un VPS

  1. En la [página de OpenClaw de Hostinger](<https://www.hostinger.com/openclaw>), elige un plan de OpenClaw en VPS y completa la compra.


* ### Configurar OpenClaw

Una vez aprovisionado el VPS, rellena los campos de configuración:

  * **Gateway token** \-- se genera automáticamente; guárdalo para usarlo más tarde.
  * **WhatsApp number** \-- tu número con el código de país (opcional).
  * **Telegram bot token** \-- de [BotFather](<https://t.me/BotFather>) (opcional).
  * **API keys** \-- solo son necesarias si no seleccionaste créditos de Ready-to-Use AI durante la compra.


* ### Iniciar OpenClaw

Haz clic en **Deploy**. Una vez en ejecución, abre el dashboard de OpenClaw desde hPanel haciendo clic en **Open**.

Los registros, reinicios y actualizaciones se gestionan directamente desde la interfaz de Docker Manager en hPanel. Para actualizar, pulsa **Update** en Docker Manager y eso descargará la imagen más reciente.

## Verificar tu configuración

Envía "Hi" a tu asistente en el canal que conectaste. OpenClaw responderá y te guiará por las preferencias iniciales.

## Solución de problemas

**El dashboard no carga** \-- Espera unos minutos a que el contenedor termine de aprovisionarse. Revisa los registros de Docker Manager en hPanel.

**El contenedor de Docker sigue reiniciándose** \-- Abre los registros de Docker Manager y busca errores de configuración (tokens ausentes, claves de API no válidas).

**El bot de Telegram no responde** \-- Envía tu mensaje con el código de vinculación desde Telegram directamente como un mensaje dentro de tu chat de OpenClaw para completar la conexión.

## Siguientes pasos

  * [Canales](</es/channels>) \-- conecta Telegram, WhatsApp, Discord y más
  * [Configuración del Gateway](</es/gateway/configuration>) \-- todas las opciones de configuración


## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Alojamiento VPS](</es/vps>)
  * [DigitalOcean](</es/install/digitalocean>)


Was this useful?YesNo