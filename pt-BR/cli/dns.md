---
title: DNS
source_url: https://docs.openclaw.ai/pt-BR/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

Auxiliares de DNS para descoberta de área ampla (Tailscale + CoreDNS). Atualmente focado em macOS + Homebrew CoreDNS.

Relacionado:

  * Descoberta do Gateway: [Descoberta](</pt-BR/gateway/discovery>)
  * Configuração de descoberta de área ampla: [Configuração](</pt-BR/gateway/configuration>)


## Configuração

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Planeje ou aplique a configuração do CoreDNS para descoberta DNS-SD unicast.

Opções:

  * `--domain <domain>`: domínio de descoberta de área ampla (por exemplo, `openclaw.internal`)
  * `--apply`: instala ou atualiza a configuração do CoreDNS e reinicia o serviço (requer sudo; somente macOS)


O que ele mostra:

  * domínio de descoberta resolvido
  * caminho do arquivo de zona
  * IPs atuais da tailnet
  * configuração de descoberta recomendada para `openclaw.json`
  * os valores de servidor de nomes/domínio de Split DNS do Tailscale a definir


Observações:

  * Sem `--apply`, o comando é apenas um auxiliar de planejamento e imprime a configuração recomendada.
  * Se `--domain` for omitido, o OpenClaw usa `discovery.wideArea.domain` da configuração.
  * Atualmente, `--apply` oferece suporte somente ao macOS e espera Homebrew CoreDNS.
  * `--apply` inicializa o arquivo de zona se necessário, garante que a estrofe de importação do CoreDNS exista e reinicia o serviço brew `coredns`.


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Descoberta](</pt-BR/gateway/discovery>)


Was this useful?YesNo