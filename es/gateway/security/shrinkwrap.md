---
title: npm shrinkwrap
source_url: https://docs.openclaw.ai/es/gateway/security/shrinkwrap
scraped_at: 2026-06-29
---

Gateway & OpsGateway

Las copias de trabajo del código fuente de OpenClaw usan `pnpm-lock.yaml`. Los paquetes npm publicados de OpenClaw usan `npm-shrinkwrap.json`, el lockfile de dependencias publicable de npm, por lo que las instalaciones de paquetes usan el grafo de dependencias revisado durante el lanzamiento.

## La versión sencilla

Shrinkwrap es un recibo del árbol de dependencias que se distribuye con un paquete npm. Le indica a npm qué versiones exactas de paquetes transitivos debe instalar.

Para los lanzamientos de OpenClaw, eso significa:

  * el paquete publicado no le pide a npm que invente un grafo de dependencias nuevo en el momento de la instalación;
  * los cambios de dependencias son más fáciles de revisar porque aparecen en un lockfile;
  * la validación del lanzamiento puede probar el mismo grafo que instalarán los usuarios;
  * las sorpresas de tamaño del paquete o de dependencias nativas son más fáciles de detectar antes de publicar.


Shrinkwrap no es un sandbox. No hace que una dependencia sea segura por sí mismo, y no sustituye el aislamiento del host, `openclaw security audit`, la procedencia del paquete ni las pruebas smoke de instalación.

El modelo mental breve:

Archivo | Dónde importa | Qué significa  
---|---|---  
`pnpm-lock.yaml` | Copia de trabajo del código fuente de OpenClaw | Grafo de dependencias del mantenedor  
`npm-shrinkwrap.json` | Paquete npm publicado | Grafo de instalación npm para usuarios  
`package-lock.json` | Aplicaciones npm locales | No es el contrato de publicación de OpenClaw  
  
## Por qué OpenClaw lo usa

OpenClaw es un Gateway, host de Plugin, enrutador de modelos y runtime de agentes. Una instalación predeterminada puede afectar el tiempo de inicio, el uso de disco, las descargas de paquetes nativos y la exposición de la cadena de suministro.

Shrinkwrap le da a la revisión del lanzamiento un límite estable:

  * los revisores pueden ver el movimiento de dependencias transitivas;
  * los validadores de paquetes pueden rechazar desviaciones inesperadas del lockfile;
  * la aceptación de paquetes puede probar instalaciones con el grafo que se publicará;
  * los paquetes de Plugin pueden llevar su propio grafo de dependencias bloqueado en lugar de depender de que el paquete raíz sea dueño de las dependencias exclusivas del Plugin.


El objetivo no es "más lockfiles." El objetivo son instalaciones de lanzamiento reproducibles con propiedad clara.

## Detalles técnicos

El paquete npm raíz `openclaw` y los paquetes npm de Plugin propiedad de OpenClaw incluyen `npm-shrinkwrap.json` cuando se publican. Los paquetes de Plugin adecuados propiedad de OpenClaw también pueden publicarse con `bundledDependencies` explícitas, de modo que sus archivos de dependencias de runtime se transporten en el tarball del Plugin en lugar de depender solo de la resolución en tiempo de instalación.

Mantén el límite así:

bashCopy code
[code]
    pnpm deps:shrinkwrap:generatepnpm deps:shrinkwrap:check
[/code]

El generador resuelve el formato de lock publicable de npm, pero rechaza versiones de paquetes generadas que no estén ya presentes en `pnpm-lock.yaml`. Eso mantiene intacto el límite de edad de dependencias, overrides y revisión de parches de pnpm.

Usa comandos solo de raíz únicamente cuando actualices intencionalmente el paquete raíz sin tocar paquetes de Plugin:

bashCopy code
[code]
    pnpm deps:shrinkwrap:root:generatepnpm deps:shrinkwrap:root:check
[/code]

Revisa estos archivos como sensibles para la seguridad:

  * `pnpm-lock.yaml`
  * `npm-shrinkwrap.json`
  * payloads de dependencias de Plugin empaquetadas
  * cualquier diff de `package-lock.json`


Los validadores de paquetes de OpenClaw requieren shrinkwrap en nuevos tarballs del paquete raíz. La ruta de publicación npm de Plugin comprueba el shrinkwrap local del Plugin, instala dependencias empaquetadas locales del paquete, y luego empaqueta o publica. Los validadores de paquetes rechazan `package-lock.json` para paquetes publicados de OpenClaw.

Para inspeccionar un paquete raíz publicado:

bashCopy code
[code]
    npm pack openclaw@<version> --json --pack-destination /tmp/openclaw-packtar -tf /tmp/openclaw-pack/openclaw-<version>.tgz | grep '^package/npm-shrinkwrap.json$'
[/code]

Para inspeccionar un paquete de Plugin propiedad de OpenClaw:

bashCopy code
[code]
    npm pack @openclaw/discord@<version> --json --pack-destination /tmp/openclaw-plugin-packtar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/npm-shrinkwrap.json$'tar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/node_modules/'
[/code]

Contexto: [npm-shrinkwrap.json](<https://docs.npmjs.com/cli/v11/configuring-npm/npm-shrinkwrap-json>).

Was this useful?YesNo

Open issue