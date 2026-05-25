---
title: Desinstalar
source_url: https://docs.openclaw.ai/pt-BR/install/uninstall
scraped_at: 2026-05-25
---

Dois caminhos:

  * **Caminho fácil** se `openclaw` ainda estiver instalado.
  * **Remoção manual do serviço** se a CLI já tiver sido removida, mas o serviço ainda estiver em execução.


## Caminho fácil (CLI ainda instalada)

Recomendado: use o desinstalador interno:

bashCopy code
[code]
    openclaw uninstall
[/code]

Não interativo (automação / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Etapas manuais (mesmo resultado):

  1. Pare o serviço gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Desinstale o serviço gateway (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Exclua estado + configuração:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Se você definiu `OPENCLAW_CONFIG_PATH` para um local personalizado fora do diretório de estado, exclua esse arquivo também.

  4. Exclua seu workspace (opcional, remove arquivos do agente):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Remova a instalação da CLI (escolha a que você usou):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Se você instalou o app do macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Observações:

  * Se você usou perfis (`--profile` / `OPENCLAW_PROFILE`), repita a etapa 3 para cada diretório de estado (os padrões são `~/.openclaw-<profile>`).
  * No modo remoto, o diretório de estado fica no **host do gateway** , então execute as etapas 1-4 lá também.


## Remoção manual do serviço (CLI não instalada)

Use isto se o serviço gateway continuar em execução, mas `openclaw` estiver ausente.

### macOS (launchd)

O rótulo padrão é `ai.openclaw.gateway` (ou `ai.openclaw.<profile>`; o legado `com.openclaw.*` ainda pode existir):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Se você usou um perfil, substitua o rótulo e o nome do plist por `ai.openclaw.<profile>`. Remova quaisquer plists legados `com.openclaw.*` se existirem.

### Linux (unidade de usuário systemd)

O nome padrão da unidade é `openclaw-gateway.service` (ou `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Tarefa Agendada)

O nome padrão da tarefa é `OpenClaw Gateway` (ou `OpenClaw Gateway (<profile>)`). O script da tarefa fica no seu diretório de estado.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Se você usou um perfil, exclua o nome de tarefa correspondente e `~\.openclaw-<profile>\gateway.cmd`.

## Instalação normal vs checkout do código-fonte

### Instalação normal ([install.sh](<http://install.sh>) / npm / pnpm / bun)

Se você usou `https://openclaw.ai/install.sh` ou `install.ps1`, a CLI foi instalada com `npm install -g openclaw@latest`. Remova com `npm rm -g openclaw` (ou `pnpm remove -g` / `bun remove -g` se você instalou dessa forma).

### Checkout do código-fonte (git clone)

Se você executa a partir de um checkout do repositório (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Desinstale o serviço gateway **antes** de excluir o repositório (use o caminho fácil acima ou a remoção manual do serviço).
  2. Exclua o diretório do repositório.
  3. Remova estado + workspace como mostrado acima.


## Relacionado

  * [Visão geral da instalação](</pt-BR/install>)
  * [Guia de migração](</pt-BR/install/migrating>)


Was this useful?YesNo