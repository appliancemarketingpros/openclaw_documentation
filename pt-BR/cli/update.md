---
title: Atualizar
source_url: https://docs.openclaw.ai/pt-BR/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

Atualize o OpenClaw com segurança e alterne entre canais stable/beta/dev.

Se você instalou via **npm/pnpm/bun** (instalação global, sem metadados do git), as atualizações acontecem pelo fluxo do gerenciador de pacotes em [Atualização](</pt-BR/install/updating>).

## Uso

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Opções

  * `--no-restart`: ignora a reinicialização do serviço Gateway após uma atualização bem-sucedida. Atualizações pelo gerenciador de pacotes que reiniciam o Gateway verificam se o serviço reiniciado informa a versão atualizada esperada antes de o comando ser concluído com sucesso.
  * `--channel <stable|beta|dev>`: define o canal de atualização (git + npm; persistido na configuração).
  * `--tag <dist-tag|version|spec>`: substitui o destino do pacote apenas para esta atualização. Para instalações por pacote, `main` mapeia para `github:openclaw/openclaw#main`.
  * `--dry-run`: visualiza as ações de atualização planejadas (fluxo de canal/tag/destino/reinicialização) sem gravar configuração, instalar, sincronizar plugins ou reiniciar.
  * `--json`: imprime JSON `UpdateRunResult` legível por máquina, incluindo `postUpdate.plugins.warnings` quando plugins gerenciados corrompidos ou não carregáveis precisam de reparo após a atualização principal ser concluída, detalhes de fallback de plugins do canal beta quando um plugin não tem release beta, e `postUpdate.plugins.integrityDrifts` quando deriva de artefato de plugin npm é detectada durante a sincronização de plugins pós-atualização.
  * `--timeout <seconds>`: tempo limite por etapa (o padrão é 1800s).
  * `--yes`: ignora prompts de confirmação (por exemplo, confirmação de downgrade).


`openclaw update` não tem uma flag `--verbose`. Use `--dry-run` para visualizar as ações planejadas de canal/tag/instalação/reinicialização, `--json` para resultados legíveis por máquina e `openclaw update status --json` quando você só precisa de detalhes de canal e disponibilidade. Se você está depurando logs do Gateway durante uma atualização, a verbosidade do console e o nível de log em arquivo são separados: Gateway `--verbose` afeta a saída de terminal/WebSocket, enquanto logs em arquivo exigem `logging.level: "debug"` ou `"trace"` na configuração. Consulte [Logs do Gateway](</pt-BR/gateway/logging>).

## `update status`

Mostra o canal de atualização ativo + tag/branch/SHA do git (para checkouts de código-fonte), além da disponibilidade de atualização.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Opções:

  * `--json`: imprime JSON de status legível por máquina.
  * `--timeout <seconds>`: tempo limite para verificações (o padrão é 3s).


## `update wizard`

Fluxo interativo para escolher um canal de atualização e confirmar se deve reiniciar o Gateway após a atualização (o padrão é reiniciar). Se você selecionar `dev` sem um checkout git, ele oferece a criação de um.

Opções:

  * `--timeout <seconds>`: tempo limite para cada etapa de atualização (padrão `1800`)


## O que ele faz

Quando você troca de canal explicitamente (`--channel ...`), o OpenClaw também mantém o método de instalação alinhado:

  * `dev` → garante um checkout git (padrão: `~/openclaw`, substitua com `OPENCLAW_GIT_DIR`), atualiza-o e instala a CLI global a partir desse checkout.
  * `stable` → instala a partir do npm usando `latest`.
  * `beta` → prefere a dist-tag npm `beta`, mas faz fallback para `latest` quando beta está ausente ou é mais antiga que a release stable atual.


O atualizador automático do núcleo do Gateway (quando habilitado via configuração) inicia o caminho de atualização da CLI fora do manipulador de requisições do Gateway ativo. Atualizações `update.run` do plano de controle pelo gerenciador de pacotes forçam uma reinicialização de atualização não adiada e sem cooldown após a troca do pacote, porque o processo antigo do Gateway ainda pode ter chunks em memória que apontam para arquivos removidos pelo novo pacote.

Para instalações por gerenciador de pacotes, `openclaw update` resolve a versão do pacote de destino antes de invocar o gerenciador de pacotes. Instalações globais npm usam uma instalação em estágio: o OpenClaw instala o novo pacote em um prefixo npm temporário, verifica o inventário `dist` empacotado ali e então troca essa árvore de pacote limpa para o prefixo global real. Se a verificação falhar, doctor pós-atualização, sincronização de plugins e trabalho de reinicialização não são executados a partir da árvore suspeita. Mesmo quando a versão instalada já corresponde ao destino, o comando atualiza a instalação global do pacote e então executa sincronização de plugins, atualização de conclusão de comando principal e trabalho de reinicialização. Isso mantém sidecars empacotados e registros de plugins pertencentes ao canal alinhados com a build instalada do OpenClaw, enquanto deixa rebuilds completos de conclusão de comandos de plugins para execuções explícitas de `openclaw completion --write-state`.

Quando um serviço Gateway gerenciado local está instalado e a reinicialização está habilitada, atualizações pelo gerenciador de pacotes param o serviço em execução antes de substituir a árvore do pacote, depois atualizam os metadados do serviço a partir da instalação atualizada, reiniciam o serviço e verificam se o Gateway reiniciado informa a versão esperada antes de relatar sucesso. No macOS, a verificação pós-atualização também verifica se o LaunchAgent está carregado/em execução para o perfil ativo e se a porta local loopback configurada está saudável. Se o plist estiver instalado, mas o launchd não o estiver supervisionando, o OpenClaw refaz o bootstrap do LaunchAgent automaticamente e então executa novamente as verificações de prontidão de integridade/versão/canal. Um bootstrap novo carrega o job RunAtLoad diretamente, então a recuperação de atualização não executa imediatamente `kickstart -k` no Gateway recém-iniciado. Se o Gateway ainda não ficar saudável, o comando sai com valor diferente de zero e imprime o caminho do log de reinicialização mais instruções explícitas de reinicialização, reinstalação e rollback de pacote. Com `--no-restart`, a substituição do pacote ainda é executada, mas o serviço gerenciado não é parado nem reiniciado, então o Gateway em execução pode manter o código antigo até você reiniciá-lo manualmente.

## Fluxo de checkout git

### Seleção de canal

  * `stable`: faz checkout da tag não beta mais recente, depois executa build e doctor.
  * `beta`: prefere a tag `-beta` mais recente, mas faz fallback para a tag stable mais recente quando beta está ausente ou é mais antiga.
  * `dev`: faz checkout de `main`, depois executa fetch e rebase.


### Etapas de atualização

* ### Verificar worktree limpa

Não requer alterações não commitadas.

* ### Trocar canal

Alterna para o canal selecionado (tag ou branch).

* ### Buscar upstream

Apenas dev.

* ### Build de preflight (apenas dev)

Executa a build TypeScript em uma worktree temporária. Se a ponta falhar, volta até 10 commits para encontrar o commit mais novo que compila. Defina `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` para também executar lint durante este preflight; o lint é executado em modo serial restrito porque hosts de atualização de usuários frequentemente são menores que executores de CI.

* ### Rebase

Faz rebase sobre o commit selecionado (apenas dev).

* ### Instalar dependências

Usa o gerenciador de pacotes do repositório. Para checkouts pnpm, o atualizador inicializa `pnpm` sob demanda (via `corepack` primeiro, depois um fallback temporário `npm install pnpm@11`) em vez de executar `npm run build` dentro de um workspace pnpm.

* ### Compilar Control UI

Compila o gateway e a Control UI.

* ### Executar doctor

`openclaw doctor` é executado como a verificação final de atualização segura.

* ### Sincronizar plugins

Sincroniza plugins com o canal ativo. Dev usa plugins empacotados; stable e beta usam npm. Atualiza instalações rastreadas de plugins.

No canal de atualização beta, instalações rastreadas de plugins npm e ClawHub que seguem a linha padrão/latest tentam primeiro uma release `@beta` do plugin. Se o plugin não tiver release beta, o OpenClaw faz fallback para a spec default/latest registrada e relata isso como um aviso. Para plugins npm, o OpenClaw também faz fallback quando o pacote beta existe, mas falha na validação de instalação. Esses avisos de fallback de plugins não fazem a atualização principal falhar. Versões exatas e tags explícitas não são reescritas.

## Atalho `--update`

`openclaw --update` é reescrito para `openclaw update` (útil para shells e scripts de inicialização).

## Relacionado

  * `openclaw doctor` (oferece executar a atualização primeiro em checkouts git)
  * [Canais de desenvolvimento](</pt-BR/install/development-channels>)
  * [Atualização](</pt-BR/install/updating>)
  * [Referência da CLI](</pt-BR/cli>)


Was this useful?YesNo