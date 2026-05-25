---
title: Substituições de instalação de Plugin
source_url: https://docs.openclaw.ai/pt-BR/plugins/install-overrides
scraped_at: 2026-05-25
---

As substituições de instalação de Plugin permitem que mantenedores testem instalações de Plugin em tempo de configuração usando um pacote npm específico ou um tarball local gerado com npm-pack. Elas são apenas para E2E e validação de pacote. Usuários normais devem instalar plugins com [`openclaw plugins install`](</pt-BR/cli/plugins>).

## Ambiente

As substituições ficam desativadas a menos que ambas as variáveis sejam definidas:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

O mapa de substituições é JSON indexado por id de Plugin. Os valores aceitam:

  * `npm:<registry-spec>` para pacotes de registro e versões ou tags exatas
  * `npm-pack:<path.tgz>` para tarballs locais produzidos por `npm pack`


Caminhos `npm-pack:` relativos são resolvidos a partir do diretório de trabalho atual.

## Comportamento

Quando um fluxo em tempo de configuração solicita a instalação de um Plugin cujo id aparece no mapa, o OpenClaw usa a origem de substituição em vez da origem npm do catálogo, empacotada ou padrão. Isso se aplica ao onboarding e a outros fluxos que usam o instalador de Plugin compartilhado em tempo de configuração.

As substituições ainda impõem o id de Plugin esperado. Um tarball mapeado para `codex` deve instalar um Plugin cujo id de manifesto seja `codex`.

As substituições não herdam o status oficial de origem confiável. Mesmo quando a entrada do catálogo normalmente representa um pacote de propriedade do OpenClaw, uma substituição é tratada como entrada de teste fornecida pelo operador.

Arquivos `.env` do workspace não podem habilitar substituições de instalação. Defina essas variáveis no shell confiável, job de CI ou comando de teste remoto que inicia o OpenClaw.

## E2E de pacote

Use um diretório de estado isolado para que instalações de pacote e registros de instalação não toquem seu estado normal do OpenClaw:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Verifique o pacote instalado sob o diretório de estado:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

Para E2E com provedor ao vivo, carregue a chave real de API a partir de um shell confiável ou segredo de CI antes de iniciar o comando de teste. Não imprima chaves; reporte apenas a origem e se a chave estava presente.

Was this useful?YesNo