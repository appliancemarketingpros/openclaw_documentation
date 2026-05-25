---
title: Administrar plugins
source_url: https://docs.openclaw.ai/es/plugins/manage-plugins
scraped_at: 2026-05-25
---

La mayoría de los flujos de trabajo de plugins son unos pocos comandos: buscar, instalar, reiniciar el Gateway, verificar y desinstalar cuando ya no necesites el plugin.

## Listar plugins

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Usa `--json` para scripts. Incluye diagnósticos del registro y el `dependencyStatus` estático de cada plugin cuando el paquete del plugin declara `dependencies` u `optionalDependencies`.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` es una comprobación de inventario en frío. Muestra lo que OpenClaw puede descubrir a partir de la configuración, los manifiestos y el registro de plugins; no demuestra que un proceso Gateway ya en ejecución haya importado el runtime del plugin.

## Instalar plugins

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Después de instalar el código del plugin, reinicia el Gateway que sirve tus canales:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Usa `inspect --runtime` cuando necesites una prueba de que el plugin registró superficies de runtime como herramientas, hooks, servicios, métodos de Gateway o comandos de CLI propiedad del plugin.

## Actualizar plugins

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Si un plugin se instaló desde un dist-tag de npm como `@beta`, las llamadas posteriores a `update <plugin-id>` reutilizan esa etiqueta registrada. Pasar una especificación npm explícita cambia la instalación rastreada a esa especificación para futuras actualizaciones.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

El segundo comando devuelve un plugin a la línea de versiones predeterminada del registro cuando antes estaba fijado a una versión o etiqueta exacta.

Cuando `openclaw update` se ejecuta en el canal beta, los registros de plugins de npm y ClawHub en la línea predeterminada intentan primero la versión `@beta` del plugin correspondiente. Si esa versión beta no existe, OpenClaw vuelve a la especificación predeterminada/latest registrada. Para plugins de npm, OpenClaw también vuelve atrás cuando el paquete beta existe pero no supera la validación de instalación. Las versiones exactas y las etiquetas explícitas como `@rc` o `@beta` se conservan.

## Desinstalar plugins

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

La desinstalación elimina la entrada de configuración del plugin, el registro del índice de plugins, las entradas de listas de permitidos/denegados y las rutas de carga enlazadas cuando corresponde. Los directorios de instalación gestionados se eliminan salvo que pases `--keep-files`.

En modo Nix (`OPENCLAW_NIX_MODE=1`), los comandos para instalar, actualizar, desinstalar, habilitar y deshabilitar plugins están desactivados. Gestiona esas opciones en la fuente de Nix de la instalación; para nix-openclaw, usa el [Inicio rápido](<https://github.com/openclaw/nix-openclaw#quick-start>) centrado en agentes.

## Publicar plugins

Puedes publicar plugins externos en [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>) o ambos.

### Publicar en ClawHub

ClawHub es la superficie pública principal de descubrimiento para plugins de OpenClaw. Ofrece a los usuarios metadatos buscables, historial de versiones y resultados de escaneo del registro antes de la instalación.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Los usuarios instalan desde ClawHub con:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

La forma sin prefijo sigue comprobando ClawHub primero.

### Publicar en [npmjs.com](<http://npmjs.com>)

Los plugins npm nativos deben incluir un manifiesto de plugin y metadatos de punto de entrada de OpenClaw en `package.json`.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Los usuarios instalan solo desde npm con:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Si el mismo paquete también está disponible en ClawHub, `npm:` omite la búsqueda en ClawHub y fuerza la resolución mediante npm.

## Elección de fuente

  * **ClawHub** : úsalo cuando quieras descubrimiento nativo de OpenClaw, resúmenes de escaneo, versiones y sugerencias de instalación.
  * **[npmjs.com](<http://npmjs.com>)** : úsalo cuando ya distribuyas paquetes JavaScript o necesites flujos de trabajo de dist-tags/registro privado de npm.
  * **Git** : úsalo cuando quieras instalar directamente desde una rama, etiqueta o commit.
  * **Ruta local** : úsala cuando estés desarrollando o probando un plugin en la misma máquina.


## Relacionado

  * [Plugins](</es/tools/plugin>) \- resumen y solución de problemas
  * [`openclaw plugins`](</es/cli/plugins>) \- referencia completa de la CLI
  * [ClawHub](</es/clawhub/cli>) \- publicación y operaciones del registro
  * [Crear plugins](</es/plugins/building-plugins>) \- crear un paquete de plugin
  * [Manifiesto de plugin](</es/plugins/manifest>) \- manifiesto y metadatos de paquete


Was this useful?YesNo