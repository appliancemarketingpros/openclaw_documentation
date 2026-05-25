---
title: Aprovações
source_url: https://docs.openclaw.ai/pt-BR/cli/approvals
scraped_at: 2026-05-25
---

# `openclaw approvals`

Gerencie aprovações de exec para o **host local** , **host do Gateway** ou um **host Node**. Por padrão, os comandos têm como destino o arquivo local de aprovações no disco. Use `--gateway` para direcionar ao Gateway, ou `--node` para direcionar a um Node específico.

Alias: `openclaw exec-approvals`

Relacionado:

  * Aprovações de exec: [Aprovações de exec](</pt-BR/tools/exec-approvals>)
  * Nodes: [Nodes](</pt-BR/nodes>)


## `openclaw exec-policy`

`openclaw exec-policy` é o comando local de conveniência para manter a configuração solicitada de `tools.exec.*` e o arquivo local de aprovações do host alinhados em uma única etapa.

Use-o quando você quiser:

  * inspecionar a política local solicitada, o arquivo de aprovações do host e a mesclagem efetiva
  * aplicar um preset local como YOLO ou deny-all
  * sincronizar `tools.exec.*` local e `~/.openclaw/exec-approvals.json` local


Exemplos:

bashCopy code
[code]
    openclaw exec-policy showopenclaw exec-policy show --json openclaw exec-policy preset yoloopenclaw exec-policy preset cautious --json openclaw exec-policy set --host gateway --security full --ask off --ask-fallback full
[/code]

Modos de saída:

  * sem `--json`: imprime a visualização de tabela legível por humanos
  * `--json`: imprime saída estruturada legível por máquina


Escopo atual:

  * `exec-policy` é **somente local**
  * ele atualiza juntos o arquivo de configuração local e o arquivo local de aprovações
  * ele **não** envia a política para o host do Gateway nem para um host Node
  * `--host node` é rejeitado neste comando porque aprovações de exec de Node são buscadas do Node em tempo de execução e devem ser gerenciadas por meio de comandos de aprovações direcionados ao Node
  * `openclaw exec-policy show` marca escopos `host=node` como gerenciados pelo Node em tempo de execução, em vez de derivar uma política efetiva do arquivo local de aprovações


Se você precisar editar diretamente aprovações de hosts remotos, continue usando `openclaw approvals set --gateway` ou `openclaw approvals set --node <id|name|ip>`.

## Comandos comuns

bashCopy code
[code]
    openclaw approvals getopenclaw approvals get --node <id|name|ip>openclaw approvals get --gateway
[/code]

`openclaw approvals get` agora mostra a política efetiva de exec para destinos locais, de Gateway e de Node:

  * política solicitada de `tools.exec`
  * política do arquivo de aprovações do host
  * resultado efetivo após a aplicação das regras de precedência


A precedência é intencional:

  * o arquivo de aprovações do host é a fonte da verdade aplicável
  * a política solicitada de `tools.exec` pode restringir ou ampliar a intenção, mas o resultado efetivo ainda é derivado das regras do host
  * `--node` combina o arquivo de aprovações do host Node com a política `tools.exec` do Gateway, porque ambos ainda se aplicam em tempo de execução
  * se a configuração do Gateway estiver indisponível, a CLI usa como fallback o snapshot de aprovações do Node e observa que a política final em tempo de execução não pôde ser calculada


## Substituir aprovações a partir de um arquivo

bashCopy code
[code]
    openclaw approvals set --file ./exec-approvals.jsonopenclaw approvals set --stdin <<'EOF'{ version: 1, defaults: { security: "full", ask: "off" } }EOFopenclaw approvals set --node <id|name|ip> --file ./exec-approvals.jsonopenclaw approvals set --gateway --file ./exec-approvals.json
[/code]

`set` aceita JSON5, não apenas JSON estrito. Use `--file` ou `--stdin`, não ambos.

## Exemplo de "nunca solicitar" / YOLO

Para um host que nunca deve parar em aprovações de exec, defina os padrões de aprovações do host como `full` \+ `off`:

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Variante para Node:

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Isso altera apenas o **arquivo de aprovações do host**. Para manter alinhada a política solicitada do OpenClaw, defina também:

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask off
[/code]

Por que `tools.exec.host=gateway` neste exemplo:

  * `host=auto` ainda significa "sandbox quando disponível, caso contrário gateway".
  * YOLO diz respeito a aprovações, não a roteamento.
  * Se você quiser exec no host mesmo quando um sandbox estiver configurado, torne a escolha do host explícita com `gateway` ou `/exec host=gateway`.


Isso corresponde ao comportamento atual de YOLO com padrão de host. Restrinja-o se quiser aprovações.

Atalho local:

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

Esse atalho local atualiza juntos a configuração local solicitada de `tools.exec.*` e os padrões locais de aprovações. Em intenção, ele é equivalente à configuração manual em duas etapas acima, mas somente para a máquina local.

## Auxiliares de allowlist

bashCopy code
[code]
    openclaw approvals allowlist add "~/Projects/**/bin/rg"openclaw approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"openclaw approvals allowlist add --agent "*" "/usr/bin/uname" openclaw approvals allowlist remove "~/Projects/**/bin/rg"
[/code]

## Opções comuns

`get`, `set` e `allowlist add|remove` são compatíveis com:

  * `--node <id|name|ip>`
  * `--gateway`
  * opções compartilhadas de RPC de Node: `--url`, `--token`, `--timeout`, `--json`


Observações sobre direcionamento:

  * sem flags de destino significa o arquivo local de aprovações no disco
  * `--gateway` tem como destino o arquivo de aprovações do host do Gateway
  * `--node` tem como destino um host Node após resolver ID, nome, IP ou prefixo do ID


`allowlist add|remove` também é compatível com:

  * `--agent <id>` (o padrão é `*`)


## Observações

  * `--node` usa o mesmo resolvedor de `openclaw nodes` (id, name, ip ou prefixo do id).
  * `--agent` usa `"*"` como padrão, o que se aplica a todos os agentes.
  * O host Node deve anunciar `system.execApprovals.get/set` (aplicativo macOS ou host Node headless).
  * Arquivos de aprovações são armazenados por host em `~/.openclaw/exec-approvals.json`.


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Aprovações de exec](</pt-BR/tools/exec-approvals>)


Was this useful?YesNo