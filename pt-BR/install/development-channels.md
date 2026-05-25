---
title: Canais de lançamento
source_url: https://docs.openclaw.ai/pt-BR/install/development-channels
scraped_at: 2026-05-25
---

OpenClaw disponibiliza três canais de atualização:

  * **stable** : dist-tag do npm `latest`. Recomendado para a maioria dos usuários.
  * **beta** : dist-tag do npm `beta` quando está atual; se beta estiver ausente ou for mais antigo que a versão estável mais recente, o fluxo de atualização volta para `latest`.
  * **dev** : ponteiro móvel de `main` (git). dist-tag do npm: `dev` (quando publicado). A branch `main` é para experimentação e desenvolvimento ativo. Ela pode conter recursos incompletos ou alterações incompatíveis. Não a use em gateways de produção.


Normalmente publicamos builds estáveis primeiro em **beta** , testamos lá e então executamos uma etapa explícita de promoção que move a build validada para `latest` sem alterar o número da versão. Mantenedores também podem publicar uma versão estável diretamente em `latest` quando necessário. Dist-tags são a fonte da verdade para instalações via npm.

## Alternando canais

bashCopy code
[code]
    openclaw update --channel stableopenclaw update --channel betaopenclaw update --channel dev
[/code]

`--channel` persiste sua escolha na configuração (`update.channel`) e alinha o método de instalação:

  * **`stable`** (instalações por pacote): atualiza via dist-tag do npm `latest`.
  * **`beta`** (instalações por pacote): prefere a dist-tag do npm `beta`, mas volta para `latest` quando `beta` está ausente ou é mais antiga que a tag estável atual.
  * **`stable`** (instalações por git): faz checkout da tag git estável mais recente.
  * **`beta`** (instalações por git): prefere a tag git beta mais recente, mas volta para a tag git estável mais recente quando beta está ausente ou é mais antiga.
  * **`dev`** : garante um checkout git (padrão `~/openclaw`, substitua com `OPENCLAW_GIT_DIR`), alterna para `main`, faz rebase sobre o upstream, compila e instala a CLI global a partir desse checkout.


## Direcionamento pontual para versão ou tag

Use `--tag` para direcionar uma dist-tag, versão ou especificação de pacote específica para uma única atualização **sem** alterar seu canal persistido:

bashCopy code
[code]
    # Instalar uma versão específicaopenclaw update --tag 2026.4.1-beta.1 # Instalar a partir da dist-tag beta (pontual, não persiste)openclaw update --tag beta # Instalar a partir da branch main do GitHub (tarball npm)openclaw update --tag main # Instalar uma especificação de pacote npm específicaopenclaw update --tag openclaw@2026.4.1-beta.1
[/code]

Observações:

  * `--tag` se aplica **somente a instalações por pacote (npm)**. Instalações por git a ignoram.
  * A tag não é persistida. Seu próximo `openclaw update` usa seu canal configurado como de costume.
  * Proteção contra downgrade: se a versão de destino for mais antiga que sua versão atual, o OpenClaw solicita confirmação (ignore com `--yes`).
  * `--channel beta` é diferente de `--tag beta`: o fluxo de canal pode voltar para stable/latest quando beta está ausente ou é mais antigo, enquanto `--tag beta` direciona a dist-tag bruta `beta` para essa execução única.


## Simulação

Pré-visualize o que `openclaw update` faria sem fazer alterações:

bashCopy code
[code]
    openclaw update --dry-runopenclaw update --channel beta --dry-runopenclaw update --tag 2026.4.1-beta.1 --dry-runopenclaw update --dry-run --json
[/code]

A simulação mostra o canal efetivo, a versão de destino, as ações planejadas e se uma confirmação de downgrade seria necessária.

## Plugins e canais

Quando você alterna canais com `openclaw update`, o OpenClaw também sincroniza fontes de plugins:

  * `dev` prefere plugins incluídos a partir do checkout git.
  * `stable` e `beta` restauram pacotes de plugins instalados via npm.
  * Plugins instalados via npm são atualizados depois que a atualização do núcleo é concluída.


## Verificando o status atual

bashCopy code
[code]
    openclaw update status
[/code]

Mostra o canal ativo, o tipo de instalação (git ou pacote), a versão atual e a origem (configuração, tag git, branch git ou padrão).

## Boas práticas de criação de tags

  * Crie tags para versões nas quais você quer que checkouts git parem (`vYYYY.M.D` para stable, `vYYYY.M.D-beta.N` para beta).
  * `vYYYY.M.D.beta.N` também é reconhecido por compatibilidade, mas prefira `-beta.N`.
  * Tags legadas `vYYYY.M.D-<patch>` ainda são reconhecidas como estáveis (não beta).
  * Mantenha tags imutáveis: nunca mova nem reutilize uma tag.
  * Dist-tags do npm continuam sendo a fonte da verdade para instalações via npm: 
    * `latest` -> stable
    * `beta` -> build candidata ou build estável publicada primeiro em beta
    * `dev` -> snapshot de main (opcional)


## Disponibilidade do app macOS

Builds beta e dev podem **não** incluir uma versão do app macOS. Isso é aceitável:

  * A tag git e a dist-tag do npm ainda podem ser publicadas.
  * Mencione "sem build macOS para este beta" nas notas de versão ou no changelog.


## Relacionado

  * [Atualização](</pt-BR/install/updating>)
  * [Detalhes internos do instalador](</pt-BR/install/installer>)


Was this useful?YesNo