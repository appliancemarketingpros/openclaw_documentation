---
title: Inicialización del agente
source_url: https://docs.openclaw.ai/es/start/bootstrapping
scraped_at: 2026-05-25
---

La inicialización es el ritual de **primera ejecución** que prepara un espacio de trabajo de agente y recopila detalles de identidad. Ocurre después de la incorporación, cuando el agente se inicia por primera vez.

## Qué hace la inicialización

En la primera ejecución del agente, OpenClaw inicializa el espacio de trabajo (predeterminado `~/.openclaw/workspace`):

  * Siembra `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.
  * Ejecuta un breve ritual de preguntas y respuestas (una pregunta a la vez).
  * Escribe la identidad y las preferencias en `IDENTITY.md`, `USER.md`, `SOUL.md`.
  * Elimina `BOOTSTRAP.md` al finalizar para que solo se ejecute una vez.


Para ejecuciones con modelos integrados/locales, OpenClaw mantiene `BOOTSTRAP.md` fuera del contexto privilegiado del sistema. En la primera ejecución interactiva principal, aun así pasa el contenido del archivo en el prompt de usuario para que los modelos que no llaman de forma fiable a la herramienta `read` puedan completar el ritual. Si la ejecución actual no puede acceder de forma segura al espacio de trabajo, el agente recibe una nota de inicialización limitada en lugar de un saludo genérico.

## Omitir la inicialización

Para omitir esto en un espacio de trabajo presembrado, ejecuta `openclaw onboard --skip-bootstrap`.

## Dónde se ejecuta

La inicialización siempre se ejecuta en el **host del Gateway**. Si la app de macOS se conecta a un Gateway remoto, el espacio de trabajo y los archivos de inicialización residen en esa máquina remota.

## Documentación relacionada

  * Incorporación de la app de macOS: [Incorporación](</es/start/onboarding>)
  * Diseño del espacio de trabajo: [Espacio de trabajo del agente](</es/concepts/agent-workspace>)


Was this useful?YesNo