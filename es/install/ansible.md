---
title: Ansible
source_url: https://docs.openclaw.ai/es/install/ansible
scraped_at: 2026-05-25
---

Implementa OpenClaw en servidores de producción con **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- un instalador automatizado con una arquitectura centrada en la seguridad.

## Requisitos previos

Requisito | Detalles  
---|---  
**SO** | Debian 11+ o Ubuntu 20.04+  
**Acceso** | Privilegios root o sudo  
**Red** | Conexión a Internet para la instalación de paquetes  
**Ansible** | 2.14+ (instalado automáticamente por el script de inicio rápido)  
  
## Qué obtienes

  * **Seguridad centrada en el firewall** \-- aislamiento con UFW + Docker (solo SSH + Tailscale accesibles)
  * **VPN Tailscale** \-- acceso remoto seguro sin exponer servicios públicamente
  * **Docker** \-- contenedores de sandbox aislados, enlaces solo a localhost
  * **Defensa en profundidad** \-- arquitectura de seguridad de 4 capas
  * **Integración con systemd** \-- inicio automático al arrancar con endurecimiento
  * **Configuración con un solo comando** \-- implementación completa en minutos


## Inicio rápido

Instalación con un solo comando:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Qué se instala

El playbook de Ansible instala y configura:

  1. **Tailscale** \-- VPN de malla para acceso remoto seguro
  2. **Firewall UFW** \-- solo puertos SSH + Tailscale
  3. **Docker CE + Compose V2** \-- para el backend de sandbox predeterminado del agente
  4. **Node.js 24 + pnpm** \-- dependencias de runtime (Node 22 LTS, actualmente `22.16+`, sigue siendo compatible)
  5. **OpenClaw** \-- basado en host, no contenedorizado
  6. **Servicio systemd** \-- inicio automático con endurecimiento de seguridad


## Configuración posterior a la instalación

* ### Cambiar al usuario openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Ejecutar el asistente de incorporación

El script posterior a la instalación te guía para configurar los ajustes de OpenClaw.

* ### Conectar proveedores de mensajería

Inicia sesión en WhatsApp, Telegram, Discord o Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Verificar la instalación

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Conectarse a Tailscale

Únete a tu malla VPN para acceso remoto seguro.

### Comandos rápidos

bashCopy code
[code]
    # Comprobar el estado del serviciosudo systemctl status openclaw # Ver logs en vivosudo journalctl -u openclaw -f # Reiniciar el gatewaysudo systemctl restart openclaw # Inicio de sesión del proveedor (ejecutar como usuario openclaw)sudo -i -u openclawopenclaw channels login
[/code]

## Arquitectura de seguridad

La implementación usa un modelo de defensa de 4 capas:

  1. **Firewall (UFW)** \-- solo SSH (22) + Tailscale (41641/udp) expuestos públicamente
  2. **VPN (Tailscale)** \-- Gateway accesible solo mediante la malla VPN
  3. **Aislamiento de Docker** \-- la cadena iptables DOCKER-USER evita la exposición de puertos externos
  4. **Endurecimiento de systemd** \-- NoNewPrivileges, PrivateTmp, usuario sin privilegios


Para verificar tu superficie externa de ataque:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Solo el puerto 22 (SSH) debería estar abierto. Todos los demás servicios (Gateway, Docker) están bloqueados.

Docker se instala para sandboxes de agentes (ejecución aislada de herramientas), no para ejecutar el Gateway en sí. Consulta [Sandbox multiagente y herramientas](</es/tools/multi-agent-sandbox-tools>) para la configuración del sandbox.

## Instalación manual

Si prefieres control manual sobre la automatización:

* ### Instalar requisitos previos

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Clonar el repositorio

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Instalar colecciones de Ansible

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Ejecutar el playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Como alternativa, ejecútalo directamente y luego ejecuta manualmente el script de configuración después:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Luego ejecutar: /tmp/openclaw-setup.sh
[/code]

## Actualización

El instalador de Ansible configura OpenClaw para actualizaciones manuales. Consulta [Actualización](</es/install/updating>) para ver el flujo de actualización estándar.

Para volver a ejecutar el playbook de Ansible (por ejemplo, para cambios de configuración):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Esto es idempotente y seguro de ejecutar varias veces.

## Solución de problemas

El firewall bloquea mi conexión

  * Asegúrate de poder acceder mediante la VPN Tailscale primero
  * El acceso SSH (puerto 22) siempre está permitido
  * El Gateway solo es accesible mediante Tailscale por diseño

El servicio no se inicia bashCopy code
[code]
    # Comprobar logssudo journalctl -u openclaw -n 100 # Verificar permisossudo ls -la /opt/openclaw # Probar inicio manualsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Problemas con el sandbox de Docker bashCopy code
[code]
    # Verificar que Docker se está ejecutandosudo systemctl status docker # Comprobar la imagen del sandboxsudo docker images | grep openclaw-sandbox # Crear la imagen del sandbox si falta (requiere checkout del código fuente)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# Para instalaciones npm sin checkout del código fuente, consulta# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Falla el inicio de sesión del proveedor

Asegúrate de ejecutar como el usuario `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Configuración avanzada

Para ver la arquitectura de seguridad detallada y la solución de problemas, consulta el repositorio openclaw-ansible:

  * [Arquitectura de seguridad](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Detalles técnicos](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Guía de solución de problemas](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Relacionado

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- guía completa de implementación
  * [Docker](</es/install/docker>) \-- configuración de Gateway contenedorizado
  * [Sandboxing](</es/gateway/sandboxing>) \-- configuración del sandbox de agentes
  * [Sandbox multiagente y herramientas](</es/tools/multi-agent-sandbox-tools>) \-- aislamiento por agente


Was this useful?YesNo