---
title: Plugins
source_url: https://docs.openclaw.ai/es/cli/plugins
scraped_at: 2026-05-25
---

Gestiona Plugins del Gateway, paquetes de hooks y bundles compatibles.

[**Sistema de Plugins** Guía para usuarios finales sobre cómo instalar, activar y solucionar problemas de plugins. ](</es/tools/plugin>) [**Gestionar plugins** Ejemplos rápidos para instalar, listar, actualizar, desinstalar y publicar. ](</es/plugins/manage-plugins>) [**Bundles de Plugins** Modelo de compatibilidad de bundles. ](</es/plugins/bundles>) [**Manifiesto de Plugin** Campos del manifiesto y esquema de configuración. ](</es/plugins/manifest>) [**Seguridad** Refuerzo de seguridad para instalaciones de plugins. ](</es/gateway/security>)

## Comandos

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

Para investigar instalaciones, inspecciones, desinstalaciones o actualizaciones del registro lentas, ejecuta el comando con `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1`. La traza escribe los tiempos de las fases en stderr y mantiene la salida JSON analizable. Consulta [Depuración](</es/help/debugging#plugin-lifecycle-trace>).

### Instalar

bashCopy code
[code]
    openclaw plugins search "calendar"                   # search ClawHub pluginsopenclaw plugins install <package>                      # npm by defaultopenclaw plugins install clawhub:<package>              # ClawHub onlyopenclaw plugins install npm:<package>                  # npm onlyopenclaw plugins install npm-pack:<path.tgz>            # local npm pack through npm install semanticsopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # overwrite existing installopenclaw plugins install <package> --pin                # pin versionopenclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # local pathopenclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

Los mantenedores que prueben instalaciones en tiempo de configuración pueden anular las fuentes automáticas de instalación de plugins con variables de entorno protegidas. Consulta [Anulaciones de instalación de plugins](</es/plugins/install-overrides>).

`plugins search` consulta ClawHub en busca de paquetes de plugin instalables e imprime nombres de paquete listos para instalar. Busca paquetes de plugins de código y plugins de bundle, no Skills. Usa `openclaw skills search` para Skills de ClawHub.

Includes de configuración y reparación de configuración no válida

Si tu sección `plugins` está respaldada por un `$include` de un solo archivo, `plugins install/update/enable/disable/uninstall` escribe en ese archivo incluido y deja `openclaw.json` intacto. Los includes raíz, los arrays de includes y los includes con anulaciones hermanas fallan de forma cerrada en lugar de aplanarse. Consulta [Includes de configuración](</es/gateway/configuration>) para ver las formas admitidas.

Si la configuración no es válida durante la instalación, `plugins install` normalmente falla de forma cerrada y te indica que primero ejecutes `openclaw doctor --fix`. Durante el inicio del Gateway y la recarga en caliente, la configuración no válida de plugins falla de forma cerrada como cualquier otra configuración no válida; `openclaw doctor --fix` puede poner en cuarentena la entrada de plugin no válida. La única excepción documentada en tiempo de instalación es una ruta estrecha de recuperación de plugins incluidos para plugins que optan explícitamente por `openclaw.install.allowInvalidConfigRecovery`.

\--force y reinstalar frente a actualizar

`--force` reutiliza el destino de instalación existente y sobrescribe en el lugar un plugin o paquete de hooks ya instalado. Úsalo cuando estés reinstalando intencionadamente el mismo id desde una nueva ruta local, archivo, paquete de ClawHub o artefacto de npm. Para actualizaciones rutinarias de un plugin npm ya rastreado, prefiere `openclaw plugins update <id-or-npm-spec>`.

Si ejecutas `plugins install` para un id de plugin que ya está instalado, OpenClaw se detiene y te dirige a `plugins update <id-or-npm-spec>` para una actualización normal, o a `plugins install <package> --force` cuando realmente quieres sobrescribir la instalación actual desde una fuente diferente.

Alcance de --pin

`--pin` se aplica solo a instalaciones npm. No es compatible con instalaciones `git:`; usa una ref de git explícita como `git:github.com/acme/plugin@v1.2.3` cuando quieras una fuente fijada. No es compatible con `--marketplace`, porque las instalaciones de marketplace conservan metadatos de fuente del marketplace en lugar de una especificación npm.

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` es una opción de emergencia para falsos positivos en el escáner integrado de código peligroso. Permite que la instalación continúe incluso cuando el escáner integrado informa hallazgos `critical`, pero **no** omite los bloqueos de política del hook `before_install` del plugin y **no** omite fallos de escaneo.

Esta marca de CLI se aplica a los flujos de instalación/actualización de plugins. Las instalaciones de dependencias de Skills respaldadas por Gateway usan la anulación de solicitud correspondiente `dangerouslyForceUnsafeInstall`, mientras que `openclaw skills install` sigue siendo un flujo independiente de descarga/instalación de Skills de ClawHub.

Si un plugin que publicaste en ClawHub está bloqueado por un escaneo del registro, usa los pasos para publicadores en [ClawHub](</es/clawhub/security>).

Paquetes de hooks y especificaciones npm

`plugins install` también es la superficie de instalación para paquetes de hooks que exponen `openclaw.hooks` en `package.json`. Usa `openclaw hooks` para visibilidad filtrada de hooks y activación por hook, no para instalación de paquetes.

Las especificaciones npm son **solo de registro** (nombre de paquete + **versión exacta** opcional o **dist-tag**). Las especificaciones Git/URL/archivo y los rangos semver se rechazan. Las instalaciones de dependencias se ejecutan de forma local al proyecto con `--ignore-scripts` por seguridad, incluso cuando tu shell tiene ajustes globales de instalación npm. Las raíces npm gestionadas de plugins heredan los `overrides` npm de nivel de paquete de OpenClaw, por lo que las fijaciones de seguridad del host también se aplican a dependencias de plugins elevadas.

Usa `npm:<package>` cuando quieras hacer explícita la resolución de npm. Las especificaciones de paquete sin prefijo también se instalan directamente desde npm durante la transición de lanzamiento.

Las especificaciones sin prefijo y `@latest` permanecen en la rama estable. Las versiones de corrección con sello de fecha de OpenClaw, como `2026.5.3-1`, son versiones estables para esta comprobación. Si npm resuelve cualquiera de ellas a una versión preliminar, OpenClaw se detiene y te pide que aceptes explícitamente con una etiqueta de versión preliminar como `@beta`/`@rc` o una versión preliminar exacta como `@1.2.3-beta.4`.

Si una especificación de instalación sin prefijo coincide con un id de plugin oficial (por ejemplo, `diffs`), OpenClaw instala directamente la entrada del catálogo. Para instalar un paquete npm con el mismo nombre, usa una especificación con ámbito explícita (por ejemplo, `@scope/diffs`).

Repositorios Git

Usa `git:<repo>` para instalar directamente desde un repositorio git. Las formas admitidas incluyen `git:github.com/owner/repo`, `git:owner/repo`, URLs completas `https://`, `ssh://`, `git://`, `file://` y URLs de clonación `git@host:owner/repo.git`. Añade `@<ref>` o `#<ref>` para hacer checkout de una rama, etiqueta o commit antes de instalar.

Las instalaciones Git clonan en un directorio temporal, hacen checkout de la ref solicitada cuando está presente y luego usan el instalador normal del directorio de plugins. Eso significa que la validación del manifiesto, el escaneo de código peligroso, el trabajo de instalación del gestor de paquetes y los registros de instalación se comportan como instalaciones npm. Las instalaciones git registradas incluyen la URL/ref de origen y el commit resuelto para que `openclaw plugins update` pueda volver a resolver la fuente más adelante.

Después de instalar desde git, usa `openclaw plugins inspect <id> --runtime --json` para verificar registros en tiempo de ejecución, como métodos del Gateway y comandos CLI. Si el plugin registró una raíz CLI con `api.registerCli`, ejecuta ese comando directamente mediante la CLI raíz de OpenClaw, por ejemplo `openclaw demo-plugin ping`.

Archivos

Archivos admitidos: `.zip`, `.tgz`, `.tar.gz`, `.tar`. Los archivos de plugins nativos de OpenClaw deben contener un `openclaw.plugin.json` válido en la raíz del plugin extraído; los archivos que solo contienen `package.json` se rechazan antes de que OpenClaw escriba registros de instalación.

Usa `npm-pack:<path.tgz>` cuando el archivo sea un tarball de npm-pack y quieras probar la misma ruta de instalación de raíz npm gestionada que usan las instalaciones de registro, incluida la verificación de `package-lock.json`, el escaneo de dependencias elevadas y los registros de instalación npm. Las rutas de archivo simples siguen instalándose como archivos locales bajo la raíz de extensions de plugins.

Las instalaciones del marketplace de Claude también son compatibles.

Las instalaciones de ClawHub usan un localizador explícito `clawhub:<package>`:

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

Las especificaciones de plugins seguras para npm sin prefijo se instalan desde npm de forma predeterminada durante la transición de lanzamiento:

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

Usa `npm:` para hacer explícita la resolución solo de npm:

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw comprueba la API de plugin anunciada / compatibilidad mínima del Gateway antes de instalar. Cuando la versión seleccionada de ClawHub publica un artefacto ClawPack, OpenClaw descarga el `.tgz` versionado de paquete npm, verifica el encabezado de resumen de ClawHub y el resumen del artefacto, y luego lo instala mediante la ruta normal de archivo. Las versiones anteriores de ClawHub sin metadatos de ClawPack siguen instalándose mediante la ruta heredada de verificación de archivos de paquete. Las instalaciones registradas conservan sus metadatos de origen de ClawHub, tipo de artefacto, integridad npm, shasum npm, nombre del tarball y datos del resumen de ClawPack para actualizaciones posteriores. Las instalaciones de ClawHub sin versión conservan una especificación registrada sin versión para que `openclaw plugins update` pueda seguir versiones más recientes de ClawHub; los selectores explícitos de versión o etiqueta como `clawhub:pkg@1.2.3` y `clawhub:pkg@beta` permanecen fijados a ese selector.

#### Abreviatura de marketplace

Usa la abreviatura `plugin@marketplace` cuando el nombre del marketplace exista en la caché del registro local de Claude en `~/.claude/plugins/known_marketplaces.json`:

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

Usa `--marketplace` cuando quieras pasar explícitamente el origen del marketplace:

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### Marketplace sources

  * un nombre de marketplace conocido por Claude de `~/.claude/plugins/known_marketplaces.json`
  * una raíz de marketplace local o una ruta `marketplace.json`
  * una abreviatura de repositorio de GitHub como `owner/repo`
  * una URL de repositorio de GitHub como `https://github.com/owner/repo`
  * una URL git


### Remote marketplace rules

Para marketplaces remotos cargados desde GitHub o git, las entradas de plugins deben permanecer dentro del repositorio de marketplace clonado. OpenClaw acepta orígenes de ruta relativa desde ese repositorio y rechaza orígenes de plugins HTTP(S), de ruta absoluta, git, GitHub y otros orígenes que no sean rutas desde manifiestos remotos.

Para rutas locales y archivos, OpenClaw detecta automáticamente:

  * plugins nativos de OpenClaw (`openclaw.plugin.json`)
  * paquetes compatibles con Codex (`.codex-plugin/plugin.json`)
  * paquetes compatibles con Claude (`.claude-plugin/plugin.json` o el diseño de componentes predeterminado de Claude)
  * paquetes compatibles con Cursor (`.cursor-plugin/plugin.json`)


### Listar

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

Muestra solo plugins activados.

Cambia de la vista de tabla a líneas de detalle por plugin con metadatos de origen/procedencia/versión/activación.

Inventario legible por máquina, además de diagnósticos del registro y estado de instalación de dependencias de paquete.

`plugins search` es una búsqueda remota en el catálogo de ClawHub. No inspecciona el estado local, no modifica la configuración, no instala paquetes ni carga código de tiempo de ejecución del plugin. Los resultados de búsqueda incluyen el nombre del paquete de ClawHub, familia, canal, versión, resumen y una sugerencia de instalación como `openclaw plugins install clawhub:<package>`.

Para trabajar con plugins incluidos dentro de una imagen Docker empaquetada, monta con bind el directorio de código fuente del plugin sobre la ruta de código fuente empaquetada correspondiente, como `/app/extensions/synology-chat`. OpenClaw detectará esa superposición de código fuente montada antes de `/app/dist/extensions/synology-chat`; un directorio de código fuente copiado sin más permanece inerte, de modo que las instalaciones empaquetadas normales siguen usando el dist compilado.

Para depurar hooks de tiempo de ejecución:

  * `openclaw plugins inspect <id> --runtime --json` muestra los hooks registrados y diagnósticos de una pasada de inspección con el módulo cargado. La inspección de tiempo de ejecución nunca instala dependencias; usa `openclaw doctor --fix` para limpiar estado de dependencias heredado o recuperar plugins descargables faltantes referenciados por la configuración.
  * `openclaw gateway status --deep --require-rpc` confirma el Gateway alcanzable, pistas de servicio/proceso, ruta de configuración y salud de RPC.
  * Los hooks de conversación no incluidos (`llm_input`, `llm_output`, `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `before_agent_finalize`, `agent_end`) requieren `plugins.entries.<id>.hooks.allowConversationAccess=true`.


Usa `--link` para evitar copiar un directorio local (lo añade a `plugins.load.paths`):

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### Índice de plugins

Los metadatos de instalación de plugins son estado gestionado por máquina, no configuración de usuario. Las instalaciones y actualizaciones lo escriben en `plugins/installs.json` bajo el directorio de estado activo de OpenClaw. Su mapa de nivel superior `installRecords` es la fuente duradera de metadatos de instalación, incluidos registros de manifiestos de plugins rotos o faltantes. El arreglo `plugins` es la caché de registro en frío derivada del manifiesto. El archivo incluye una advertencia de no editar y lo usan `openclaw plugins update`, desinstalación, diagnósticos y el registro de plugins en frío.

Cuando OpenClaw ve registros heredados enviados de `plugins.installs` en la configuración, las lecturas de tiempo de ejecución los tratan como entrada de compatibilidad sin reescribir `openclaw.json`. Las escrituras explícitas de plugins y `openclaw doctor --fix` mueven esos registros al índice de plugins y eliminan la clave de configuración cuando las escrituras de configuración están permitidas; si alguna escritura falla, los registros de configuración se conservan para que los metadatos de instalación no se pierdan.

### Desinstalar

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall` elimina registros de plugins de `plugins.entries`, el índice de plugins persistido, entradas de listas de permitir/denegar de plugins y entradas enlazadas de `plugins.load.paths` cuando corresponda. A menos que se establezca `--keep-files`, la desinstalación también elimina el directorio de instalación gestionado rastreado cuando está dentro de la raíz de extensiones de plugins de OpenClaw. Para plugins de memoria activa, el espacio de memoria se restablece a `memory-core`.

### Actualizar

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

Las actualizaciones se aplican a instalaciones de plugins rastreadas en el índice de plugins gestionados y a instalaciones de hook-packs rastreadas en `hooks.internal.installs`.

Resolving plugin id vs npm spec

Cuando pasas un id de plugin, OpenClaw reutiliza la especificación de instalación registrada para ese plugin. Eso significa que dist-tags almacenadas previamente como `@beta` y versiones exactas fijadas seguirán usándose en ejecuciones posteriores de `update <id>`.

Para instalaciones npm, también puedes pasar una especificación explícita de paquete npm con una dist-tag o versión exacta. OpenClaw resuelve ese nombre de paquete de vuelta al registro de plugin rastreado, actualiza ese plugin instalado y registra la nueva especificación npm para futuras actualizaciones basadas en id.

Pasar el nombre del paquete npm sin versión ni etiqueta también resuelve de vuelta al registro de plugin rastreado. Usa esto cuando un plugin se fijó a una versión exacta y quieres moverlo de vuelta a la línea de publicación predeterminada del registro.

Beta channel updates

`openclaw plugins update` reutiliza la especificación de plugin rastreada salvo que pases una especificación nueva. `openclaw update` además conoce el canal de actualización activo de OpenClaw: en el canal beta, los registros de plugins npm y ClawHub de línea predeterminada prueban primero `@beta` y luego vuelven a la especificación predeterminada/latest registrada si no existe una versión beta del plugin. Esa alternativa se informa como advertencia y no hace fallar la actualización del núcleo. Las versiones exactas y etiquetas explícitas permanecen fijadas a ese selector.

Version checks and integrity drift

Antes de una actualización npm en vivo, OpenClaw compara la versión del paquete instalado con los metadatos del registro npm. Si la versión instalada y la identidad registrada del artefacto ya coinciden con el destino resuelto, la actualización se omite sin descargar, reinstalar ni reescribir `openclaw.json`.

Cuando existe un hash de integridad almacenado y el hash del artefacto obtenido cambia, OpenClaw lo trata como deriva del artefacto npm. El comando interactivo `openclaw plugins update` imprime los hashes esperado y real, y pide confirmación antes de continuar. Los ayudantes de actualización no interactivos fallan de forma cerrada salvo que el llamador proporcione una política explícita de continuación.

\--dangerously-force-unsafe-install on update

`--dangerously-force-unsafe-install` también está disponible en `plugins update` como anulación de emergencia para falsos positivos del escaneo integrado de código peligroso durante actualizaciones de plugins. Aun así, no omite bloqueos de política `before_install` del plugin ni bloqueos por fallo de escaneo, y solo se aplica a actualizaciones de plugins, no a actualizaciones de hook-packs.

### Inspeccionar

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspect muestra identidad, estado de carga, origen, capacidades del manifiesto, banderas de política, diagnósticos, metadatos de instalación, capacidades de paquete y cualquier soporte detectado de servidor MCP o LSP sin importar el tiempo de ejecución del plugin de forma predeterminada. Añade `--runtime` para cargar el módulo del plugin e incluir hooks registrados, herramientas, comandos, servicios, métodos de Gateway y rutas HTTP. La inspección de tiempo de ejecución informa directamente dependencias faltantes del plugin; las instalaciones y reparaciones permanecen en `openclaw plugins install`, `openclaw plugins update` y `openclaw doctor --fix`.

Los comandos CLI propiedad del plugin suelen instalarse como grupos de comandos raíz de `openclaw`, pero los plugins también pueden registrar comandos anidados bajo un padre del núcleo como `openclaw nodes`. Después de que `inspect --runtime` muestre un comando bajo `cliCommands`, ejecútalo en la ruta indicada; por ejemplo, un plugin que registra `demo-git` puede verificarse con `openclaw demo-git ping`.

Cada plugin se clasifica según lo que realmente registra en tiempo de ejecución:

  * **capacidad-simple** — un tipo de capacidad (p. ej., un plugin solo de proveedor)
  * **capacidad-híbrida** — varios tipos de capacidad (p. ej., texto + voz + imágenes)
  * **solo-hooks** — solo hooks, sin capacidades ni superficies
  * **sin-capacidad** — herramientas/comandos/servicios, pero sin capacidades


Consulta [formas de Plugin](</es/plugins/architecture#plugin-shapes>) para obtener más información sobre el modelo de capacidades.

### Doctor

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor` informa errores de carga de plugins, diagnósticos de manifiesto/descubrimiento y avisos de compatibilidad. Cuando todo está correcto, imprime `No plugin issues detected.`

Si un plugin configurado está presente en disco pero bloqueado por las comprobaciones de seguridad de rutas del cargador, la validación de configuración conserva la entrada del plugin y la informa como `present but blocked`. Corrige el diagnóstico anterior de plugin bloqueado, como la propiedad de la ruta o permisos de escritura global, en lugar de eliminar la configuración `plugins.entries.<id>` o `plugins.allow`.

Para fallos de forma de módulo, como exportaciones `register`/`activate` faltantes, vuelve a ejecutar con `OPENCLAW_PLUGIN_LOAD_DEBUG=1` para incluir un resumen compacto de la forma de exportación en la salida de diagnóstico.

### Registro

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

El registro local de plugins es el modelo persistido de lectura en frío de OpenClaw para la identidad de plugins instalados, habilitación, metadatos de origen y propiedad de contribuciones. El inicio normal, la búsqueda de propietario del proveedor, la clasificación de configuración de canales y el inventario de plugins pueden leerlo sin importar módulos de runtime de plugins.

Usa `plugins registry` para inspeccionar si el registro persistido está presente, actualizado u obsoleto. Usa `--refresh` para reconstruirlo a partir del índice persistido de plugins, la política de configuración y los metadatos de manifiesto/paquete. Esta es una ruta de reparación, no una ruta de activación en runtime.

`openclaw doctor --fix` también repara la desviación de npm gestionado adyacente al registro: si un paquete `@openclaw/*` huérfano o recuperado bajo la raíz npm de plugins gestionados oculta un plugin incluido, doctor elimina ese paquete obsoleto y reconstruye el registro para que el inicio valide contra el manifiesto incluido. Doctor también vuelve a enlazar el paquete host `openclaw` en los plugins npm gestionados que declaran `peerDependencies.openclaw`, de modo que las importaciones de runtime locales del paquete, como `openclaw/plugin-sdk/*`, se resuelvan después de actualizaciones o reparaciones de npm.

### Marketplace

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

La lista de Marketplace acepta una ruta local de marketplace, una ruta `marketplace.json`, una abreviatura de GitHub como `owner/repo`, una URL de repositorio de GitHub o una URL de git. `--json` imprime la etiqueta de origen resuelta junto con el manifiesto de marketplace analizado y las entradas de plugins.

## Relacionado

  * [Crear plugins](</es/plugins/building-plugins>)
  * [Referencia de CLI](</es/cli>)
  * [ClawHub](</es/clawhub>)


Was this useful?YesNo