---
title: Resolución de dependencias de Plugin
source_url: https://docs.openclaw.ai/es/plugins/dependency-resolution
scraped_at: 2026-05-25
---

OpenClaw mantiene el trabajo de dependencias de Plugin en el momento de instalación/actualización. La carga en tiempo de ejecución no ejecuta gestores de paquetes, repara árboles de dependencias ni muta el directorio de paquetes de OpenClaw.

## División de responsabilidades

Los paquetes de Plugin son propietarios de su grafo de dependencias:

  * las dependencias de tiempo de ejecución viven en `dependencies` u `optionalDependencies` del paquete de Plugin
  * las importaciones de SDK/núcleo son peer o importaciones suministradas por OpenClaw
  * los plugins de desarrollo local traen sus propias dependencias ya instaladas
  * los plugins de npm y git se instalan en raíces de paquetes propiedad de OpenClaw


OpenClaw solo es propietario del ciclo de vida del Plugin:

  * descubrir el origen del Plugin
  * instalar o actualizar el paquete cuando se solicite explícitamente
  * registrar los metadatos de instalación
  * cargar el punto de entrada del Plugin
  * fallar con un error accionable cuando falten dependencias


## Raíces de instalación

OpenClaw usa raíces estables por origen:

  * los paquetes npm se instalan bajo `~/.openclaw/npm`
  * los paquetes git se clonan bajo `~/.openclaw/git`
  * las instalaciones locales/de ruta/de archivo se copian o referencian sin reparar dependencias


Las instalaciones npm se ejecutan en la raíz npm con:

bashCopy code
[code]
    cd ~/.openclaw/npmnpm install --omit=dev --omit=peer --legacy-peer-deps --ignore-scripts --no-audit --no-fund
[/code]

`openclaw plugins install npm-pack:<path.tgz>` usa esa misma raíz npm administrada para un tarball npm-pack local. OpenClaw lee los metadatos npm del tarball, lo añade a la raíz administrada como una dependencia `file:` copiada, ejecuta la instalación npm normal y luego verifica los metadatos del lockfile instalado antes de confiar en el Plugin. Esto está pensado para la aceptación de paquetes y la prueba de candidatos de lanzamiento, donde un artefacto pack local debe comportarse como el artefacto de registro que simula.

npm puede elevar dependencias transitivas a `~/.openclaw/npm/node_modules` junto al paquete de Plugin. OpenClaw escanea la raíz npm administrada antes de confiar en la instalación y usa npm para eliminar paquetes administrados por npm durante la desinstalación, de modo que las dependencias de tiempo de ejecución elevadas permanecen dentro del límite de limpieza administrado.

Los plugins que importan `openclaw/plugin-sdk/*` declaran `openclaw` como una dependencia peer. OpenClaw no permite que npm instale una copia separada del paquete host desde el registro en la raíz administrada, porque los paquetes host obsoletos pueden afectar la resolución peer de npm durante instalaciones posteriores de plugins. Las instalaciones npm administradas omiten la resolución/materialización peer de npm para la raíz compartida y OpenClaw reafirma los enlaces `node_modules/openclaw` locales al Plugin para los paquetes instalados que declaran el peer host después de instalar, actualizar o desinstalar.

Las instalaciones git clonan o actualizan el repositorio y luego ejecutan:

bashCopy code
[code]
    npm install --omit=dev --ignore-scripts --no-audit --no-fund
[/code]

El Plugin instalado se carga entonces desde ese directorio de paquete, por lo que la resolución de `node_modules` local al paquete y principal funciona igual que para un paquete Node normal.

## Plugins locales

Los plugins locales se tratan como directorios controlados por el desarrollador. OpenClaw no ejecuta `npm install`, `pnpm install` ni reparación de dependencias para ellos. Si un Plugin local tiene dependencias, instálalas en ese Plugin antes de cargarlo.

Los plugins TypeScript locales de terceros pueden usar la ruta de emergencia de Jiti. Los plugins JavaScript empaquetados y los plugins internos incluidos se cargan mediante import/require nativo en lugar de Jiti.

## Inicio y recarga

El inicio de Gateway y la recarga de configuración nunca instalan dependencias de Plugin. Leen los registros de instalación de Plugin, calculan el punto de entrada y lo cargan.

Si falta una dependencia en tiempo de ejecución, el Plugin no se carga y el error debe dirigir al operador a una corrección explícita:

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins install <source>openclaw doctor --fix
[/code]

`doctor --fix` puede limpiar el estado de dependencias heredado generado por OpenClaw y recuperar plugins descargables que faltan en los registros de instalación locales cuando la configuración los referencia. Doctor no repara dependencias para un Plugin local ya instalado.

## Plugins incluidos

Los plugins incluidos ligeros y críticos para el núcleo se envían como parte de OpenClaw. Deben no tener un árbol de dependencias de tiempo de ejecución pesado o moverse a un paquete descargable en ClawHub/npm.

Para la lista generada actual de plugins que se envían en el paquete principal, se instalan externamente o permanecen solo como código fuente, consulta [Inventario de Plugin](</es/plugins/plugin-inventory>).

Los manifiestos de plugins incluidos no deben solicitar preparación de dependencias. La funcionalidad grande u opcional de un Plugin debe empaquetarse como un Plugin normal e instalarse mediante la misma ruta npm/git/ClawHub que los plugins de terceros.

En checkouts de código fuente, OpenClaw trata el repositorio como un monorepo pnpm. Después de `pnpm install`, los plugins incluidos se cargan desde `extensions/<id>`, por lo que las dependencias workspace locales al paquete están disponibles y las ediciones se recogen directamente. El desarrollo en checkout de código fuente es solo pnpm; `npm install` simple en la raíz del repositorio no es una forma compatible de preparar dependencias de plugins incluidos.

Forma de instalación | Ubicación del Plugin incluido | Propietario de dependencias  
---|---|---  
`npm install -g openclaw` | Árbol de tiempo de ejecución compilado dentro del paquete | Paquete OpenClaw y flujos explícitos de instalación/actualización/doctor de Plugin  
Checkout git más `pnpm install` | Paquetes workspace `extensions/<id>` | El workspace pnpm, incluidas las dependencias propias de cada paquete de Plugin  
`openclaw plugins install ...` | Raíz de Plugin npm/git/ClawHub administrada | El flujo de instalación/actualización de Plugin  
  
## Limpieza heredada

Las versiones anteriores de OpenClaw generaban raíces de dependencias de plugins incluidos al iniciar o durante la reparación de doctor. La limpieza actual de doctor elimina esos directorios y symlinks obsoletos cuando se usa `--fix`, incluidas raíces antiguas `plugin-runtime-deps`, symlinks de paquetes con prefijo global de Node que apuntan a destinos `plugin-runtime-deps` podados, manifiestos `.openclaw-runtime-deps*`, `node_modules` de Plugin generados, directorios de etapa de instalación y stores pnpm locales al paquete. El postinstall empaquetado también elimina esos symlinks globales antes de podar las raíces de destino heredadas para que las actualizaciones no dejen importaciones de paquetes ESM colgantes.

Estas rutas son solo restos heredados. Las instalaciones nuevas no deben crearlas.

Was this useful?YesNo