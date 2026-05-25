---
title: Anulaciones de instalación de Plugin
source_url: https://docs.openclaw.ai/es/plugins/install-overrides
scraped_at: 2026-05-25
---

Las anulaciones de instalación de Plugin permiten a los mantenedores probar instalaciones de Plugin durante la configuración contra un paquete npm específico o un tarball local de npm-pack. Son solo para E2E y validación de paquetes. Los usuarios normales deben instalar Plugins con [`openclaw plugins install`](</es/cli/plugins>).

## Entorno

Las anulaciones están deshabilitadas salvo que ambas variables estén definidas:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

El mapa de anulaciones es JSON con claves por id de Plugin. Los valores admiten:

  * `npm:<registry-spec>` para paquetes de registro y versiones exactas o etiquetas
  * `npm-pack:<path.tgz>` para tarballs locales producidos por `npm pack`


Las rutas relativas `npm-pack:` se resuelven desde el directorio de trabajo actual.

## Comportamiento

Cuando un flujo durante la configuración solicita instalar un Plugin cuyo id aparece en el mapa, OpenClaw usa el origen de anulación en lugar del origen de catálogo, incluido, o predeterminado de npm. Esto se aplica al onboarding y a otros flujos que usan el instalador de Plugin compartido durante la configuración.

Las anulaciones siguen imponiendo el id de Plugin esperado. Un tarball asignado a `codex` debe instalar un Plugin cuyo id de manifiesto sea `codex`.

Las anulaciones no heredan el estado oficial de origen de confianza. Incluso cuando la entrada del catálogo normalmente representa un paquete propiedad de OpenClaw, una anulación se trata como entrada de prueba proporcionada por el operador.

Los archivos `.env` del workspace no pueden habilitar anulaciones de instalación. Defina estas variables en el shell de confianza, el trabajo de CI o el comando de prueba remoto que inicia OpenClaw.

## E2E de paquete

Use un directorio de estado aislado para que las instalaciones de paquetes y los registros de instalación no toquen su estado normal de OpenClaw:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Verifique el paquete instalado bajo el directorio de estado:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

Para E2E de proveedor en vivo, cargue la clave de API real desde un shell de confianza o un secreto de CI antes de iniciar el comando de prueba. No imprima claves; informe solo el origen y si la clave estaba presente.

Was this useful?YesNo