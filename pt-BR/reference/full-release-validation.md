---
title: Validação completa de release
source_url: https://docs.openclaw.ai/pt-BR/reference/full-release-validation
scraped_at: 2026-05-25
---

`Full Release Validation` é o guarda-chuva de lançamento. Ele é o único ponto de entrada manual para prova de pré-lançamento, mas a maior parte do trabalho acontece em workflows filhos para que uma caixa com falha possa ser executada novamente sem reiniciar o lançamento inteiro.

Execute-o a partir de uma referência confiável de workflow, normalmente `main`, e passe a branch de lançamento, tag ou SHA completo do commit como `ref`:

bashCopy code
[code]
    gh workflow run full-release-validation.yml \  --ref main \  -f ref=release/YYYY.M.D \  -f provider=openai \  -f mode=both \  -f release_profile=stable
[/code]

Workflows filhos usam a referência confiável de workflow para o harness e o input `ref` para o candidato em teste. Isso mantém a nova lógica de validação disponível ao validar uma branch ou tag de lançamento mais antiga.

Por padrão, `release_profile=stable` executa as faixas bloqueadoras de lançamento e ignora o soak exaustivo live/Docker. Passe `run_release_soak=true` para incluir as faixas de soak em uma execução estável. `release_profile=full` sempre habilita as faixas de soak para que o perfil consultivo amplo nunca perca cobertura silenciosamente.

O Package Acceptance normalmente cria o tarball candidato a partir do `ref` resolvido, incluindo execuções com SHA completo disparadas com `pnpm ci:full-release`. Após uma publicação beta, passe `release_package_spec=openclaw@YYYY.M.D-beta.N` para reutilizar o pacote npm publicado nas verificações de lançamento, Package Acceptance, cross-OS, Docker de caminho de lançamento e Telegram de pacote. Use `package_acceptance_package_spec` somente quando o Package Acceptance deve provar intencionalmente um pacote diferente.

## Estágios de nível superior

Estágio | Detalhes  
---|---  
Resolução do alvo | **Job:** `Resolve target ref`  
**Workflow filho:** nenhum |   
**Prova:** resolve a branch de lançamento, tag ou SHA completo do commit e registra os inputs selecionados. |   
**Reexecução:** execute novamente o guarda-chuva se isto falhar. |   
Vitest e CI normal | **Job:** `Run normal full CI`  
**Workflow filho:** `CI` |   
**Prova:** grafo manual completo de CI contra a referência alvo, incluindo faixas Linux Node, shards de Plugin agrupados, contratos de canal, compatibilidade com Node 22, `check`, `check-additional`, smoke de build, verificações de docs, Skills Python, Windows, macOS, i18n da Control UI e Android via guarda-chuva. |   
**Reexecução:** `rerun_group=ci`. |   
Pré-lançamento de Plugin | **Job:** `Run plugin prerelease validation`  
**Workflow filho:** `Plugin Prerelease` |   
**Prova:** verificações estáticas de Plugin somente de lançamento, cobertura de Plugin agêntico, shards completos de lote de Plugin, faixas Docker de pré-lançamento de Plugin e um artefato não bloqueante `plugin-inspector-advisory` para triagem de compatibilidade. |   
**Reexecução:** `rerun_group=plugin-prerelease`. |   
Verificações de lançamento | **Job:** `Run release/live/Docker/QA validation`  
**Workflow filho:** `OpenClaw Release Checks` |   
**Prova:** smoke de instalação, verificações de pacote cross-OS, Package Acceptance, paridade do QA Lab, Matrix live e Telegram live. Com `run_release_soak=true` ou `release_profile=full`, também executa suítes live/E2E exaustivas e chunks Docker de caminho de lançamento. |   
**Reexecução:** `rerun_group=release-checks` ou um identificador mais estreito de release-checks. |   
Artefato de pacote | **Job:** `Prepare release package artifact`  
**Workflow filho:** nenhum |   
**Prova:** cria o tarball pai `release-package-under-test` cedo o bastante para verificações voltadas a pacote que não precisam esperar por `OpenClaw Release Checks`. |   
**Reexecução:** execute novamente o guarda-chuva ou forneça `release_package_spec` para reexecuções de pacote publicado. |   
Telegram de pacote | **Job:** `Run package Telegram E2E`  
**Workflow filho:** `NPM Telegram Beta E2E` |   
**Prova:** prova de pacote Telegram baseada em artefato pai para `rerun_group=all` com `release_profile=full`, ou prova Telegram de pacote publicado quando `release_package_spec` ou `npm_telegram_package_spec` está definido. |   
**Reexecução:** `rerun_group=npm-telegram` com `release_package_spec` ou `npm_telegram_package_spec`. |   
Verificador guarda-chuva | **Job:** `Verify full validation`  
**Workflow filho:** nenhum |   
**Prova:** verifica novamente as conclusões registradas das execuções filhas e acrescenta tabelas dos jobs mais lentos a partir dos workflows filhos. |   
**Reexecução:** execute novamente somente este job após reexecutar um filho com falha até ficar verde. |   
  
Para `ref=main` e `rerun_group=all`, um guarda-chuva mais novo substitui um mais antigo. Quando o pai é cancelado, seu monitor cancela qualquer workflow filho que ele já tenha disparado. Execuções de validação de branch e tag de lançamento não cancelam umas às outras por padrão.

## Estágios das verificações de lançamento

`OpenClaw Release Checks` é o maior workflow filho. Ele resolve o alvo uma vez e prepara um artefato compartilhado `release-package-under-test` quando estágios voltados a pacote ou Docker precisam dele.

Estágio | Detalhes  
---|---  
Destino do lançamento | **Job:** `Resolve target ref`  
**Workflow de apoio:** nenhum |   
**Testes:** ref selecionada, SHA esperado opcional, perfil, grupo de nova execução e filtro de suíte live focada. |   
**Nova execução:** `rerun_group=release-checks`. |   
Artefato de pacote | **Job:** `Prepare release package artifact`  
**Workflow de apoio:** nenhum |   
**Testes:** empacota ou resolve um tarball candidato e envia `release-package-under-test` para verificações downstream voltadas a pacote. |   
**Nova execução:** o pacote afetado, grupo cross-OS ou live/E2E. |   
Smoke de instalação | **Job:** `Run install smoke`  
**Workflow de apoio:** `Install Smoke` |   
**Testes:** caminho completo de instalação com reutilização da imagem smoke do Dockerfile raiz, instalação de pacote QR, smokes Docker de raiz e Gateway, testes Docker do instalador, smoke de provider de imagem com instalação global via Bun e E2E rápido de instalação/desinstalação de plugin incluído. |   
**Nova execução:** `rerun_group=install-smoke`. |   
Cross-OS | **Job:** `cross_os_release_checks`  
**Workflow de apoio:** `OpenClaw Cross-OS Release Checks (Reusable)` |   
**Testes:** lanes de instalação limpa e upgrade no Linux, Windows e macOS para o provider e modo selecionados, usando o tarball candidato mais um pacote de baseline. |   
**Nova execução:** `rerun_group=cross-os`. |   
E2E de repo e live | **Job:** `Run repo/live E2E validation`  
**Workflow de apoio:** `OpenClaw Live And E2E Checks (Reusable)` |   
**Testes:** E2E de repositório, cache live, streaming por websocket da OpenAI, shards de provider live nativo e Plugin, e harnesses live com Docker para modelo/backend/Gateway selecionados por `release_profile`. |   
**Execuções:** `run_release_soak=true`, `release_profile=full` ou `rerun_group=live-e2e` focado. |   
**Nova execução:** `rerun_group=live-e2e`, opcionalmente com `live_suite_filter`. |   
Caminho de lançamento Docker | **Job:** `Run Docker release-path validation`  
**Workflow de apoio:** `OpenClaw Live And E2E Checks (Reusable)` |   
**Testes:** chunks Docker do caminho de lançamento contra o artefato de pacote compartilhado. |   
**Execuções:** `run_release_soak=true`, `release_profile=full` ou `rerun_group=live-e2e` focado. |   
**Nova execução:** `rerun_group=live-e2e`. |   
Aceitação de pacote | **Job:** `Run package acceptance`  
**Workflow de apoio:** `Package Acceptance` |   
**Testes:** fixtures offline de pacote de plugin, atualização de plugin, aceitação de pacote do Telegram com mock da OpenAI e verificações de sobrevivência de upgrade publicado contra o mesmo tarball. Verificações bloqueantes de lançamento usam o baseline publicado mais recente padrão; verificações de soak expandem para toda release npm estável a partir de `2026.4.23`, inclusive, mais fixtures de problemas reportados. |   
**Nova execução:** `rerun_group=package`. |   
Paridade de QA | **Job:** `Run QA Lab parity lane` e `Run QA Lab parity report`  
**Workflow de apoio:** jobs diretos |   
**Testes:** pacotes de paridade agêntica do candidato e do baseline, depois o relatório de paridade. |   
**Nova execução:** `rerun_group=qa-parity` ou `rerun_group=qa`. |   
Matrix live de QA | **Job:** `Run QA Lab live Matrix lane`  
**Workflow de apoio:** job direto |   
**Testes:** perfil de QA Matrix live rápido no ambiente `qa-live-shared`. |   
**Nova execução:** `rerun_group=qa-live` ou `rerun_group=qa`. |   
Telegram live de QA | **Job:** `Run QA Lab live Telegram lane`  
**Workflow de apoio:** job direto |   
**Testes:** QA live do Telegram com leases de credenciais de CI do Convex. |   
**Nova execução:** `rerun_group=qa-live` ou `rerun_group=qa`. |   
Verificador de lançamento | **Job:** `Verify release checks`  
**Workflow de apoio:** nenhum |   
**Testes:** jobs obrigatórios de verificações de lançamento para o grupo de nova execução selecionado. |   
**Nova execução:** executar novamente depois que os jobs filhos focados passarem. |   
  
## Chunks do caminho de lançamento Docker

O estágio do caminho de lançamento Docker executa estes chunks quando `live_suite_filter` está vazio:

Chunk | Cobertura  
---|---  
`core` | Lanes smoke do caminho de lançamento Docker do core.  
`package-update-openai` | Comportamento de instalação/atualização do pacote OpenAI, instalação sob demanda do Codex e chamadas de ferramenta de Chat Completions.  
`package-update-anthropic` | Comportamento de instalação e atualização do pacote Anthropic.  
`package-update-core` | Comportamento de pacote e atualização neutro em relação a provider.  
`plugins-runtime-plugins` | Lanes de runtime de Plugin que exercitam comportamento de plugin.  
`plugins-runtime-services` | Lanes de runtime de plugin com serviços de apoio e live; inclui OpenWebUI quando solicitado.  
`plugins-runtime-install-a` até `plugins-runtime-install-h` | Lotes de instalação/runtime de plugin divididos para validação paralela de lançamento.  
  
Use `docker_lanes=<lane[,lane]>` direcionado no workflow live/E2E reutilizável quando apenas uma lane Docker falhar. Os artefatos de lançamento incluem comandos de nova execução por lane com artefato de pacote e entradas de reutilização de imagem quando disponíveis.

## Perfis de lançamento

`release_profile` controla principalmente a amplitude de live/provider dentro das verificações de lançamento. Ele não remove CI completo normal, Plugin Prerelease, smoke de instalação, aceitação de pacote ou QA Lab. Para `stable`, E2E exaustivo de repo/live e chunks do caminho de lançamento Docker são cobertura de soak e são executados quando `run_release_soak=true`. `full` força a cobertura de soak e também faz a execução guarda-chuva rodar E2E de pacote do Telegram contra o artefato de pacote de lançamento pai quando `rerun_group=all`, para que um candidato completo de pré-publicação não pule silenciosamente essa lane de pacote do Telegram.

Perfil | Uso pretendido | Cobertura live/provider incluída  
---|---|---  
`minimum` | Smoke mais rápido crítico para lançamento. | Caminho live OpenAI/core, modelos live Docker para OpenAI, core do Gateway nativo, perfil de Gateway OpenAI nativo, Plugin OpenAI nativo e Gateway OpenAI live Docker.  
`stable` | Perfil padrão de aprovação de lançamento. | `minimum` mais smoke Anthropic, Google, MiniMax, backend, harness de teste live nativo, backend CLI live Docker, bind ACP Docker, harness Codex Docker e um shard smoke OpenCode Go.  
`full` | Varredura consultiva ampla. | `stable` mais providers consultivos, shards live de plugin e shards live de mídia.  
  
## Adições somente em full

Estas suítes são ignoradas por `stable` e incluídas por `full`:

Área | Cobertura somente em full  
---|---  
Modelos live Docker | OpenCode Go, OpenRouter, xAI, [Z.ai](<http://Z.ai>) e Fireworks.  
Gateway live Docker | Providers consultivos divididos em shards DeepSeek/Fireworks, OpenCode Go/OpenRouter e xAI/Z.ai.  
Perfis de provider do Gateway nativo | Shards completos Anthropic Opus e Sonnet/Haiku, Fireworks, DeepSeek, shards completos de modelos OpenCode Go, OpenRouter, xAI e [Z.ai](<http://Z.ai>).  
Shards live de Plugin nativo | Plugins A-K, L-N, O-Z outros, Moonshot e xAI.  
Shards live de mídia nativa | Grupos de áudio, música Google, música MiniMax e vídeo A-D.  
  
`stable` inclui `native-live-src-gateway-profiles-anthropic-smoke` e `native-live-src-gateway-profiles-opencode-go-smoke`; `full` usa os shards mais amplos de modelos Anthropic e OpenCode Go em vez disso. Novas execuções focadas ainda podem usar os identificadores agregados `native-live-src-gateway-profiles-anthropic` ou `native-live-src-gateway-profiles-opencode-go`.

## Novas execuções focadas

Use `rerun_group` para evitar repetir caixas de lançamento não relacionadas:

Identificador | Escopo  
---|---  
`all` | Todos os estágios da Validação de lançamento completa.  
`ci` | Apenas o filho manual de CI completa.  
`plugin-prerelease` | Apenas o filho de pré-lançamento de Plugin.  
`release-checks` | Todos os estágios das Verificações de lançamento do OpenClaw.  
`install-smoke` | Smoke de instalação até as verificações de lançamento.  
`cross-os` | Verificações de lançamento entre sistemas operacionais.  
`live-e2e` | Validação de E2E repo/ao vivo e do caminho de lançamento com Docker.  
`package` | Aceitação de pacote.  
`qa` | Paridade de QA mais lanes de QA ao vivo.  
`qa-parity` | Apenas lanes e relatório de paridade de QA.  
`qa-live` | Apenas Matrix e Telegram ao vivo de QA.  
`npm-telegram` | E2E de Telegram do pacote publicado; requer `release_package_spec` ou `npm_telegram_package_spec`.  
  
Use `live_suite_filter` com `rerun_group=live-e2e` quando uma suíte ao vivo falhar. IDs de filtro válidos são definidos no workflow reutilizável ao vivo/E2E, incluindo `docker-live-models`, `live-gateway-docker`, `live-gateway-anthropic-docker`, `live-gateway-google-docker`, `live-gateway-minimax-docker`, `live-gateway-advisory-docker`, `live-cli-backend-docker`, `live-acp-bind-docker` e `live-codex-harness-docker`.

O identificador `live-gateway-advisory-docker` é um identificador de reexecução agregado para seus três shards de provedores, então ele ainda se expande para todos os jobs de Gateway Docker consultivos.

Use `cross_os_suite_filter` com `rerun_group=cross-os` quando uma lane entre sistemas operacionais falhar. O filtro aceita um ID de SO, um ID de suíte ou um par SO/suíte, por exemplo `windows/packaged-upgrade`, `windows` ou `packaged-fresh`. Resumos entre sistemas operacionais incluem tempos por fase para lanes de upgrade empacotado, e comandos de longa duração imprimem linhas de Heartbeat para que uma atualização do Windows travada fique visível antes do tempo limite do job.

Lanes de verificação de lançamento de QA são consultivas. Uma falha apenas de QA é relatada como aviso e não bloqueia o verificador de verificações de lançamento; reexecute `rerun_group=qa`, `qa-parity` ou `qa-live` quando precisar de novas evidências de QA.

## Evidências a manter

Mantenha o resumo `Full Release Validation` como o índice no nível do lançamento. Ele vincula IDs de execução filhos e inclui tabelas dos jobs mais lentos. Para falhas, inspecione primeiro o workflow filho e depois reexecute o menor identificador correspondente acima.

Artefatos úteis:

  * `release-package-under-test` da Validação de lançamento completa pai e `OpenClaw Release Checks`
  * Artefatos do caminho de lançamento com Docker em `.artifacts/docker-tests/`
  * `package-under-test` da Aceitação de pacote e artefatos de aceitação do Docker
  * Artefatos de verificação de lançamento entre sistemas operacionais para cada SO e suíte
  * Artefatos de paridade de QA, Matrix e Telegram


## Arquivos de workflow

  * `.github/workflows/full-release-validation.yml`
  * `.github/workflows/openclaw-release-checks.yml`
  * `.github/workflows/openclaw-live-and-e2e-checks-reusable.yml`
  * `.github/workflows/plugin-prerelease.yml`
  * `.github/workflows/install-smoke.yml`
  * `.github/workflows/openclaw-cross-os-release-checks-reusable.yml`
  * `.github/workflows/package-acceptance.yml`


Was this useful?YesNo