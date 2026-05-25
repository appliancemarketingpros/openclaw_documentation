---
title: Banco de dados de modelos de dispositivos
source_url: https://docs.openclaw.ai/pt-BR/reference/device-models
scraped_at: 2026-05-25
---

O app complementar para macOS mostra nomes amigáveis de modelos de dispositivos Apple na UI de **Instâncias** mapeando identificadores de modelo da Apple (por exemplo, `iPad16,6`, `Mac16,6`) para nomes legíveis por humanos.

O mapeamento é incorporado como JSON em:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Fonte de dados

Atualmente incorporamos o mapeamento do repositório sob licença MIT:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Para manter builds determinísticos, os arquivos JSON são fixados em commits específicos upstream (registrados em `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Atualizando o banco de dados

  1. Escolha os commits upstream que você quer fixar (um para iOS, um para macOS).
  2. Atualize os hashes de commit em `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Baixe novamente os arquivos JSON, fixados nesses commits:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Garanta que `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` ainda corresponda ao upstream (substitua-o se a licença upstream mudar).
  5. Verifique se o app macOS compila sem problemas (sem avisos):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Relacionado

  * [Nodes](</pt-BR/nodes>)
  * [Solução de problemas de Node](</pt-BR/nodes/troubleshooting>)


Was this useful?YesNo