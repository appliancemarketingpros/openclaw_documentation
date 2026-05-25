---
title: Gerenciar plugins
source_url: https://docs.openclaw.ai/pt-BR/plugins/manage-plugins
scraped_at: 2026-05-25
---

A maioria dos fluxos de trabalho de plugins consiste em poucos comandos: pesquisar, instalar, reiniciar o Gateway, verificar e desinstalar quando você não precisar mais do plugin.

## Listar plugins

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Use `--json` para scripts. Ele inclui diagnósticos do registro e o `dependencyStatus` estático de cada plugin quando o pacote do plugin declara `dependencies` ou `optionalDependencies`.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` é uma verificação de inventário fria. Ela mostra o que o OpenClaw consegue descobrir a partir da configuração, dos manifestos e do registro de plugins; ela não prova que um processo do Gateway já em execução importou o runtime do plugin.

## Instalar plugins

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Depois de instalar o código do plugin, reinicie o Gateway que atende seus canais:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Use `inspect --runtime` quando precisar provar que o plugin registrou superfícies de runtime como ferramentas, hooks, serviços, métodos do Gateway ou comandos de CLI pertencentes ao plugin.

## Atualizar plugins

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Se um plugin foi instalado a partir de uma dist-tag do npm, como `@beta`, chamadas posteriores de `update <plugin-id>` reutilizam essa tag registrada. Passar uma especificação npm explícita altera a instalação rastreada para essa especificação em atualizações futuras.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

O segundo comando move um plugin de volta para a linha de lançamento padrão do registro quando ele estava anteriormente fixado em uma versão exata ou tag.

Quando `openclaw update` é executado no canal beta, registros de plugins npm e ClawHub da linha padrão tentam primeiro o lançamento `@beta` correspondente do plugin. Se esse lançamento beta não existir, o OpenClaw volta para a especificação padrão/latest registrada. Para plugins npm, o OpenClaw também volta quando o pacote beta existe, mas falha na validação de instalação. Versões exatas e tags explícitas, como `@rc` ou `@beta`, são preservadas.

## Desinstalar plugins

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

A desinstalação remove a entrada de configuração do plugin, o registro de índice do plugin, entradas de lista de permissão/bloqueio e caminhos de carregamento vinculados quando aplicável. Diretórios de instalação gerenciados são removidos, a menos que você passe `--keep-files`.

No modo Nix (`OPENCLAW_NIX_MODE=1`), os comandos de instalar, atualizar, desinstalar, habilitar e desabilitar plugins ficam desabilitados. Gerencie essas escolhas na origem Nix da instalação; para nix-openclaw, use o [Início rápido](<https://github.com/openclaw/nix-openclaw#quick-start>) com foco no agente.

## Publicar plugins

Você pode publicar plugins externos no [ClawHub](<https://clawhub.ai>), em [npmjs.com](<http://npmjs.com>) ou em ambos.

### Publicar no ClawHub

O ClawHub é a principal superfície pública de descoberta para plugins do OpenClaw. Ele oferece aos usuários metadados pesquisáveis, histórico de versões e resultados de varredura do registro antes da instalação.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Usuários instalam a partir do ClawHub com:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

A forma sem prefixo ainda verifica o ClawHub primeiro.

### Publicar em [npmjs.com](<http://npmjs.com>)

Plugins npm nativos devem incluir um manifesto de plugin e metadados de ponto de entrada do OpenClaw em `package.json`.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Usuários instalam apenas via npm com:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Se o mesmo pacote também estiver disponível no ClawHub, `npm:` ignora a consulta ao ClawHub e força a resolução via npm.

## Escolha da origem

  * **ClawHub** : use quando quiser descoberta nativa do OpenClaw, resumos de varredura, versões e dicas de instalação.
  * **[npmjs.com](<http://npmjs.com>)** : use quando você já distribui pacotes JavaScript ou precisa de fluxos de trabalho de dist-tags/registro privado do npm.
  * **Git** : use quando quiser instalar diretamente a partir de uma branch, tag ou commit.
  * **Caminho local** : use quando estiver desenvolvendo ou testando um plugin na mesma máquina.


## Relacionado

  * [Plugins](</pt-BR/tools/plugin>) \- visão geral e solução de problemas
  * [`openclaw plugins`](</pt-BR/cli/plugins>) \- referência completa da CLI
  * [ClawHub](</pt-BR/clawhub/cli>) \- publicação e operações de registro
  * [Criação de plugins](</pt-BR/plugins/building-plugins>) \- crie um pacote de plugin
  * [Manifesto do plugin](</pt-BR/plugins/manifest>) \- metadados de manifesto e pacote


Was this useful?YesNo