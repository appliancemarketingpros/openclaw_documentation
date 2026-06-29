---
title: npm shrinkwrap
source_url: https://docs.openclaw.ai/pt-BR/gateway/security/shrinkwrap
scraped_at: 2026-06-29
---

Gateway & OpsGateway

OpenClaw checkouts de código-fonte usam `pnpm-lock.yaml`. Pacotes npm publicados do OpenClaw usam `npm-shrinkwrap.json`, o lockfile de dependências publicável do npm, para que as instalações de pacotes usem o grafo de dependências revisado durante o lançamento.

## A versão simples

Shrinkwrap é um recibo da árvore de dependências que acompanha um pacote npm. Ele informa ao npm quais versões exatas de pacotes transitivos instalar.

Para lançamentos do OpenClaw, isso significa:

  * o pacote publicado não pede ao npm para inventar um grafo de dependências novo no momento da instalação;
  * mudanças de dependências ficam mais fáceis de revisar porque aparecem em um lockfile;
  * a validação de lançamento pode testar o mesmo grafo que os usuários instalarão;
  * surpresas de tamanho de pacote ou dependências nativas ficam mais fáceis de identificar antes da publicação.


Shrinkwrap não é uma sandbox. Ele não torna uma dependência segura por si só, e não substitui isolamento do host, `openclaw security audit`, proveniência de pacotes ou testes básicos de instalação.

O modelo mental curto:

Arquivo | Onde importa | O que significa  
---|---|---  
`pnpm-lock.yaml` | Checkout de código-fonte do OpenClaw | Grafo de dependências do mantenedor  
`npm-shrinkwrap.json` | Pacote npm publicado | Grafo de instalação npm para usuários  
`package-lock.json` | Apps npm locais | Não é o contrato de publicação do OpenClaw  
  
## Por que o OpenClaw o usa

OpenClaw é um Gateway, host de Plugin, roteador de modelos e runtime de agentes. Uma instalação padrão pode afetar tempo de inicialização, uso de disco, downloads de pacotes nativos e exposição à cadeia de suprimentos.

Shrinkwrap dá à revisão de lançamento um limite estável:

  * revisores conseguem ver movimentação de dependências transitivas;
  * validadores de pacote conseguem rejeitar desvios inesperados de lockfile;
  * a aceitação de pacote pode testar instalações com o grafo que será enviado;
  * pacotes de Plugin podem carregar seu próprio grafo de dependências bloqueado em vez de depender do pacote raiz para possuir dependências usadas apenas pelo Plugin.


O objetivo não é "mais lockfiles." O objetivo é ter instalações de lançamento reprodutíveis com propriedade clara.

## Detalhes técnicos

O pacote npm raiz `openclaw` e pacotes npm de Plugin pertencentes ao OpenClaw incluem `npm-shrinkwrap.json` quando são publicados. Pacotes de Plugin adequados pertencentes ao OpenClaw também podem ser publicados com `bundledDependencies` explícitas, para que seus arquivos de dependências de runtime sejam carregados no tarball do Plugin em vez de depender apenas da resolução no momento da instalação.

Mantenha o limite assim:

bashCopy code
[code]
    pnpm deps:shrinkwrap:generatepnpm deps:shrinkwrap:check
[/code]

O gerador resolve o formato de lock publicável do npm, mas rejeita versões de pacotes geradas que ainda não estejam presentes em `pnpm-lock.yaml`. Isso mantém intacto o limite de idade de dependências, overrides e revisão de patches do pnpm.

Use comandos apenas da raiz somente quando estiver atualizando intencionalmente o pacote raiz sem tocar em pacotes de Plugin:

bashCopy code
[code]
    pnpm deps:shrinkwrap:root:generatepnpm deps:shrinkwrap:root:check
[/code]

Revise estes arquivos como sensíveis à segurança:

  * `pnpm-lock.yaml`
  * `npm-shrinkwrap.json`
  * payloads de dependências de Plugin empacotadas
  * qualquer diff de `package-lock.json`


Validadores de pacote do OpenClaw exigem shrinkwrap em novos tarballs do pacote raiz. O caminho de publicação npm de Plugin verifica o shrinkwrap local do Plugin, instala dependências empacotadas locais do pacote e então empacota ou publica. Validadores de pacote rejeitam `package-lock.json` para pacotes publicados do OpenClaw.

Para inspecionar um pacote raiz publicado:

bashCopy code
[code]
    npm pack openclaw@<version> --json --pack-destination /tmp/openclaw-packtar -tf /tmp/openclaw-pack/openclaw-<version>.tgz | grep '^package/npm-shrinkwrap.json$'
[/code]

Para inspecionar um pacote de Plugin pertencente ao OpenClaw:

bashCopy code
[code]
    npm pack @openclaw/discord@<version> --json --pack-destination /tmp/openclaw-plugin-packtar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/npm-shrinkwrap.json$'tar -tf /tmp/openclaw-plugin-pack/openclaw-discord-<version>.tgz | grep '^package/node_modules/'
[/code]

Contexto: [npm-shrinkwrap.json](<https://docs.npmjs.com/cli/v11/configuring-npm/npm-shrinkwrap-json>).

Was this useful?YesNo

Open issue