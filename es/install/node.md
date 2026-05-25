---
title: Node.js
source_url: https://docs.openclaw.ai/es/install/node
scraped_at: 2026-05-25
---

OpenClaw requiere **Node 22.16 o posterior**. **Node 24 es el runtime predeterminado y recomendado** para instalaciones, CI y flujos de trabajo de lanzamiento. Node 22 sigue siendo compatible a través de la línea LTS activa. El [script de instalación](</es/install#alternative-install-methods>) detectará e instalará Node automáticamente; esta página es para cuando quieres configurar Node por tu cuenta y asegurarte de que todo esté conectado correctamente (versiones, PATH, instalaciones globales).

## Verifica tu versión

bashCopy code
[code]
    node -v
[/code]

Si esto imprime `v24.x.x` o superior, estás usando el valor predeterminado recomendado. Si imprime `v22.16.x` o superior, estás en la ruta compatible de Node 22 LTS, pero aun así recomendamos actualizar a Node 24 cuando sea conveniente. Si Node no está instalado o la versión es demasiado antigua, elige un método de instalación a continuación.

## Instalar Node

### macOS

**Homebrew** (recomendado):

bashCopy code
[code]
    brew install node
[/code]

O descarga el instalador de macOS desde [nodejs.org](<https://nodejs.org/>).

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

O usa un gestor de versiones (consulta abajo).

### Windows

**winget** (recomendado):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

O descarga el instalador de Windows desde [nodejs.org](<https://nodejs.org/>).

Uso de un gestor de versiones (nvm, fnm, mise, asdf)

Los gestores de versiones te permiten cambiar fácilmente entre versiones de Node. Opciones populares:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- rápido, multiplataforma
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- ampliamente usado en macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- políglota (Node, Python, Ruby, etc.)


Ejemplo con fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Solución de problemas

### `openclaw: command not found`

Esto casi siempre significa que el directorio bin global de npm no está en tu PATH.

* ### Encuentra tu prefijo global de npm

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Verifica si está en tu PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

Busca `<npm-prefix>/bin` (macOS/Linux) o `<npm-prefix>` (Windows) en la salida.

* ### Agrégalo al archivo de inicio de tu shell

### macOS / Linux

Agrega a `~/.zshrc` o `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Luego abre una nueva terminal (o ejecuta `rehash` en zsh / `hash -r` en bash).

### Windows

Agrega la salida de `npm prefix -g` al PATH del sistema mediante Configuración → Sistema → Variables de entorno.

### Errores de permisos en `npm install -g` (Linux)

Si ves errores `EACCES`, cambia el prefijo global de npm a un directorio en el que el usuario pueda escribir:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Agrega la línea `export PATH=...` a tu `~/.bashrc` o `~/.zshrc` para hacerla permanente.

## Relacionado

  * [Resumen de instalación](</es/install>) \- todos los métodos de instalación
  * [Actualización](</es/install/updating>) \- mantener OpenClaw al día
  * [Primeros pasos](</es/start/getting-started>) \- primeros pasos después de la instalación


Was this useful?YesNo