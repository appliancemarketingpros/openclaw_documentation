---
title: Cartão de pontuação de maturidade
source_url: https://docs.openclaw.ai/pt-BR/maturity/scorecard
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Scorecard de maturidade

prontidão para lançamento - gerado a partir de taxonomia + evidências de QA

Uma visão prática do que está pronto, do que foi comprovado e do que ainda precisa de trabalho.

50 superfícies - 281 áreas de capacidade - cobertura determinística mais qualidade e completude revisadas por humanos.

Navegar pelas superfícies / Inspecionar evidências de QA / [Ler a taxonomia](</pt-BR/maturity/taxonomy>)

## Para que serve esta página

Use esta página para responder a uma pergunta: quais superfícies do OpenClaw são escolhas confiáveis para um lançamento, e quais evidências sustentam esse julgamento? A cobertura vem de evidências determinísticas de QA; a qualidade e a completude são mantidas como pontuações de maturidade revisadas.

## Visão geral

67% Pontuação de maturidade

Alpha Qualidade + completude Cobertura Experimental - 4% Qualidade Alpha - 63% Completude Beta - 70%

A cobertura é deliberadamente orientada por evidências: uma área não se torna "pronta" só porque a implementação existe. Ela não é uma entrada para a pontuação de maturidade, mas o OpenClaw busca manter a cobertura de ponta a ponta acima de 90% para recursos maduros, Estáveis ou melhores ao longo do tempo.

## Faixas de pontuação

Experimental0-50%

Alpha50-70%

Beta70-80%

Estável80-95%

Clawesome95-100%

## Explorador de superfícies

As superfícies são ordenadas por nível de maturidade, completude e qualidade. O suporte LTS é mostrado ao lado de cada linha para facilitar a comparação das opções prontas para lançamento.

### Todas as superfícies

[CLIM4Estável7 áreas](</pt-BR/maturity/taxonomy#cli>)

CoberturaExperimental4%

QualidadeEstável83%

CompletudeEstável90%

Parcial - 6

[runtime do GatewayM4Estável13 áreas](</pt-BR/maturity/taxonomy#gateway-runtime>)

CoberturaExperimental6%

QualidadeEstável81%

CompletudeEstável89%

Parcial - 12

[host Linux do GatewayM4Estável5 áreas](</pt-BR/maturity/taxonomy#linux-gateway-host>)

CoberturaExperimental0%

QualidadeBeta75%

CompletudeEstável89%

Parcial - 4

[host macOS do GatewayM4Estável7 áreas](</pt-BR/maturity/taxonomy#macos-gateway-host>)

CoberturaExperimental0%

QualidadeBeta74%

CompletudeEstável88%

Nenhum

[DiscordM4Estável6 áreas](</pt-BR/maturity/taxonomy#discord>)

CoberturaExperimental0%

QualidadeBeta73%

CompletudeEstável87%

Parcial - 4

[Runtime do agenteM3Beta9 áreas](</pt-BR/maturity/taxonomy#agent-runtime>)

CoberturaExperimental33%

QualidadeBeta78%

CompletudeBeta79%

Parcial - 6

[Mecanismo de sessão, memória e contextoM3Beta9 áreas](</pt-BR/maturity/taxonomy#session-memory-and-context-engine>)

CoberturaExperimental30%

QualidadeBeta77%

CompletudeBeta79%

Parcial - 6

[Framework de canaisM3Beta8 áreas](</pt-BR/maturity/taxonomy#channel-framework>)

CoberturaExperimental13%

QualidadeBeta76%

CompletudeBeta79%

Parcial - 5

[Automação de navegador, exec e ferramentas de sandboxM3Beta3 áreas](</pt-BR/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CoberturaExperimental21%

QualidadeBeta75%

CompletudeBeta79%

Parcial - 2

[ObservabilidadeM3Beta5 áreas](</pt-BR/maturity/taxonomy#observability>)

CoberturaExperimental18%

QualidadeBeta75%

CompletudeBeta79%

Parcial - 3

[Caminho de provedor OpenAI e CodexM3Beta5 áreas](</pt-BR/maturity/taxonomy#openai-and-codex-provider-path>)

CoberturaExperimental26%

QualidadeBeta74%

CompletudeBeta79%

Parcial - 3

[Aplicativo Web do GatewayM3Beta6 áreas](</pt-BR/maturity/taxonomy#gateway-web-app>)

CoberturaExperimental4%

QualidadeBeta74%

CompletudeBeta79%

Nenhum

[Ferramentas de busca na WebM3Beta4 áreas](</pt-BR/maturity/taxonomy#web-search-tools>)

CoberturaExperimental9%

QualidadeBeta74%

CompletudeBeta79%

Nenhum

[PluginsM3Beta9 áreas](</pt-BR/maturity/taxonomy#plugins>)

CoberturaExperimental12%

QualidadeBeta72%

CompletudeBeta79%

Parcial - 7

[Segurança, autenticação, emparelhamento e segredosM3Beta6 áreas](</pt-BR/maturity/taxonomy#security-auth-pairing-and-secrets>)

CoberturaExperimental16%

QualidadeBeta72%

CompletudeBeta79%

Parcial - 5

[Automação: Cron, hooks, tarefas, pollingM3Beta6 áreas](</pt-BR/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CoberturaExperimental2%

QualidadeBeta72%

CompletudeBeta79%

Nenhum

[Hospedagem Docker e PodmanM3Beta4 áreas](</pt-BR/maturity/taxonomy#docker-and-podman-hosting>)

CoberturaExperimental7%

QualidadeBeta71%

CompletudeBeta79%

Nenhum

[Windows via WSL2M3Beta6 áreas](</pt-BR/maturity/taxonomy#windows-via-wsl2>)

CoberturaExperimental6%

QualidadeAlpha69%

CompletudeBeta79%

Parcial - 5

[Raspberry Pi e pequenos dispositivos LinuxM3Beta4 áreas](</pt-BR/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CoberturaExperimental0%

QualidadeAlfa67%

CompletudeBeta79%

Nenhum

[Caminho do provedor AnthropicM3Beta5 áreas](</pt-BR/maturity/taxonomy#anthropic-provider-path>)

CoberturaExperimental0%

QualidadeBeta71%

CompletudeBeta78%

Nenhum

[TelegramM3Beta5 áreas](</pt-BR/maturity/taxonomy#telegram>)

CoberturaExperimental0%

QualidadeAlfa68%

CompletudeBeta78%

Completo - 5

[SlackM3Beta5 áreas](</pt-BR/maturity/taxonomy#slack>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Completo - 5

[Caminho do provedor GoogleM3Beta5 áreas](</pt-BR/maturity/taxonomy#google-provider-path>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Nenhum

[iMessage e BlueBubblesM3Beta5 áreas](</pt-BR/maturity/taxonomy#imessage-and-bluebubbles>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Nenhum

[App complementar para macOSM3Beta8 áreas](</pt-BR/maturity/taxonomy#macos-companion-app>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Nenhum

[Caminho do provedor OpenRouterM3Beta4 áreas](</pt-BR/maturity/taxonomy#openrouter-provider-path>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Nenhum

[WhatsAppM3Beta5 áreas](</pt-BR/maturity/taxonomy#whatsapp>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Nenhum

[Compreensão de mídia e geração de mídiaM2Alfa6 áreas](</pt-BR/maturity/taxonomy#media-understanding-and-media-generation>)

CoberturaExperimental2%

QualidadeAlfa64%

CompletudeAlfa68%

Nenhum

[Ferramentas de geração de imagem, vídeo e músicaM2Alfa5 áreas](</pt-BR/maturity/taxonomy#image-video-and-music-generation-tools>)

CoberturaExperimental0%

QualidadeAlfa61%

CompletudeAlfa68%

Nenhum

[Provedores de modelos locais: Ollama, vLLM, SGLang, LM StudioM2Alfa5 áreas](</pt-BR/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CoberturaExperimental0%

QualidadeAlfa61%

CompletudeAlfa68%

Nenhum

[Provedores hospedados de cauda longaM2Alfa3 áreas](</pt-BR/maturity/taxonomy#long-tail-hosted-providers>)

CoberturaExperimental0%

QualidadeAlfa61%

CompletudeAlfa68%

Nenhum

[Voz e conversa em tempo realM2Alfa6 áreas](</pt-BR/maturity/taxonomy#voice-and-realtime-talk>)

CoberturaExperimental0%

QualidadeAlfa61%

CompletudeAlfa68%

Nenhum

[MatrixM2Alfa6 áreas](</pt-BR/maturity/taxonomy#matrix>)

CoberturaExperimental0%

QualidadeAlfa60%

CompletudeAlfa67%

Nenhum

[Aplicativo AndroidM2Alfa7 áreas](</pt-BR/maturity/taxonomy#android-app>)

CoberturaExperimental0%

QualidadeAlfa59%

CompletudeAlfa66%

Nenhum

[Google ChatM2Alfa5 áreas](</pt-BR/maturity/taxonomy#google-chat>)

CoberturaExperimental0%

QualidadeAlfa59%

CompletudeAlfa66%

Nenhum

[Microsoft TeamsM2Alfa5 áreas](</pt-BR/maturity/taxonomy#microsoft-teams>)

CoberturaExperimental0%

QualidadeAlfa59%

CompletudeAlfa66%

Nenhum

[SignalM2Alfa5 áreas](</pt-BR/maturity/taxonomy#signal>)

CoberturaExperimental0%

QualidadeAlfa59%

CompletudeAlfa66%

Nenhum

[TUIM2Alfa5 áreas](</pt-BR/maturity/taxonomy#tui>)

CoberturaExperimental0%

QualidadeAlpha59%

CompletudeAlpha66%

Nenhum

[Windows nativoM2Alpha4 áreas](</pt-BR/maturity/taxonomy#native-windows>)

CoberturaExperimental0%

QualidadeAlpha58%

CompletudeAlpha66%

Parcial - 1

[ClawHubM2Alpha4 áreas](</pt-BR/maturity/taxonomy#clawhub>)

CoberturaExperimental0%

QualidadeAlpha58%

CompletudeAlpha62%

Nenhum

[Hospedagem KubernetesM2Alpha4 áreas](</pt-BR/maturity/taxonomy#kubernetes-hosting>)

CoberturaExperimental0%

QualidadeAlpha55%

CompletudeAlpha61%

Nenhum

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canais regionaisM2Alpha4 áreas](</pt-BR/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CoberturaExperimental0%

QualidadeAlpha55%

CompletudeAlpha58%

Nenhum

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 áreas](</pt-BR/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CoberturaExperimental0%

QualidadeAlpha53%

CompletudeAlpha54%

Nenhum

[OpenClaw App SDKM2Alpha6 áreas](</pt-BR/maturity/taxonomy#openclaw-app-sdk>)

CoberturaExperimental3%

QualidadeAlfa54%

CompletudeAlfa53%

Nenhum

[app para iOSM1Experimental8 áreas](</pt-BR/maturity/taxonomy#ios-app>)

CoberturaExperimental0%

QualidadeExperimental41%

CompletudeExperimental44%

Nenhum

[caminho de instalação do NixM1Experimental5 áreas](</pt-BR/maturity/taxonomy#nix-install-path>)

CoberturaExperimental0%

QualidadeExperimental41%

CompletudeExperimental44%

Nenhum

[canal de chamada de vozM1Experimental5 áreas](</pt-BR/maturity/taxonomy#voice-call-channel>)

CoberturaExperimental0%

QualidadeExperimental41%

CompletudeExperimental44%

Nenhum

[superfícies complementares do watchOSM1Experimental5 áreas](</pt-BR/maturity/taxonomy#watchos-companion-surfaces>)

CoberturaExperimental0%

QualidadeExperimental41%

CompletudeExperimental44%

Nenhum

[app complementar para LinuxM0Planejado5 áreas](</pt-BR/maturity/taxonomy#linux-companion-app>)

CoberturaExperimental0%

QualidadeExperimental19%

CompletudeExperimental21%

Nenhum

[app complementar nativo para WindowsM0Planejado5 áreas](</pt-BR/maturity/taxonomy#native-windows-companion-app>)

CoberturaExperimental0%

QualidadeExperimental19%

CompletudeExperimental21%

Nenhum

### Núcleo

[CLIM4Estável7 áreas](</pt-BR/maturity/taxonomy#cli>)

CoberturaExperimental4%

QualidadeEstável83%

CompletudeEstável90%

Parcial - 6

[Runtime do GatewayM4Estável13 áreas](</pt-BR/maturity/taxonomy#gateway-runtime>)

CoberturaExperimental6%

QualidadeEstável81%

CompletudeEstável89%

Parcial - 12

[Runtime do agenteM3Beta9 áreas](</pt-BR/maturity/taxonomy#agent-runtime>)

CoberturaExperimental33%

QualidadeBeta78%

CompletudeBeta79%

Parcial - 6

[Mecanismo de sessão, memória e contextoM3Beta9 áreas](</pt-BR/maturity/taxonomy#session-memory-and-context-engine>)

CoberturaExperimental30%

QualidadeBeta77%

CompletudeBeta79%

Parcial - 6

[Framework de canaisM3Beta8 áreas](</pt-BR/maturity/taxonomy#channel-framework>)

CoberturaExperimental13%

QualidadeBeta76%

CompletudeBeta79%

Parcial - 5

[ObservabilidadeM3Beta5 áreas](</pt-BR/maturity/taxonomy#observability>)

CoberturaExperimental18%

QualidadeBeta75%

CompletudeBeta79%

Parcial - 3

[Aplicativo web do GatewayM3Beta6 áreas](</pt-BR/maturity/taxonomy#gateway-web-app>)

CoberturaExperimental4%

QualidadeBeta74%

CompletudeBeta79%

Nenhum

[PluginsM3Beta9 áreas](</pt-BR/maturity/taxonomy#plugins>)

CoberturaExperimental12%

QualidadeBeta72%

CompletudeBeta79%

Parcial - 7

[Segurança, autenticação, pareamento e segredosM3Beta6 áreas](</pt-BR/maturity/taxonomy#security-auth-pairing-and-secrets>)

CoberturaExperimental16%

QualidadeBeta72%

CompletudeBeta79%

Parcial - 5

[Automação: Cron, ganchos, tarefas, sondagemM3Beta6 áreas](</pt-BR/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CoberturaExperimental2%

QualidadeBeta72%

CompletudeBeta79%

Nenhum

[Compreensão e geração de mídiaM2Alpha6 áreas](</pt-BR/maturity/taxonomy#media-understanding-and-media-generation>)

CoberturaExperimental2%

QualidadeAlpha64%

CompletudeAlpha68%

Nenhum

[Voz e conversa em tempo realM2Alpha6 áreas](</pt-BR/maturity/taxonomy#voice-and-realtime-talk>)

CoberturaExperimental0%

QualidadeAlpha61%

CompletudeAlpha68%

Nenhum

[TUIM2Alfa5 áreas](</pt-BR/maturity/taxonomy#tui>)

CoberturaExperimental0%

QualidadeAlfa59%

CompletudeAlfa66%

Nenhum

[ClawHubM2Alfa4 áreas](</pt-BR/maturity/taxonomy#clawhub>)

CoberturaExperimental0%

QualidadeAlfa58%

CompletudeAlfa62%

Nenhum

[OpenClaw App SDKM2Alfa6 áreas](</pt-BR/maturity/taxonomy#openclaw-app-sdk>)

CoberturaExperimental3%

QualidadeAlfa54%

CompletudeAlfa53%

Nenhum

### Plataforma

[host Gateway LinuxM4Estável5 áreas](</pt-BR/maturity/taxonomy#linux-gateway-host>)

CoberturaExperimental0%

QualidadeBeta75%

CompletudeEstável89%

Parcial - 4

[host Gateway macOSM4Estável7 áreas](</pt-BR/maturity/taxonomy#macos-gateway-host>)

CoberturaExperimental0%

QualidadeBeta74%

CompletudeEstável88%

Nenhum

[Hospedagem Docker e PodmanM3Beta4 áreas](</pt-BR/maturity/taxonomy#docker-and-podman-hosting>)

CoberturaExperimental7%

QualidadeBeta71%

CompletudeBeta79%

Nenhum

[Windows via WSL2M3Beta6 áreas](</pt-BR/maturity/taxonomy#windows-via-wsl2>)

CoberturaExperimental6%

QualidadeAlfa69%

CompletudeBeta79%

Parcial - 5

[Raspberry Pi e pequenos dispositivos LinuxM3Beta4 áreas](</pt-BR/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CoberturaExperimental0%

QualidadeAlfa67%

CompletudeBeta79%

Nenhum

[aplicativo complementar para macOSM3Beta8 áreas](</pt-BR/maturity/taxonomy#macos-companion-app>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Nenhum

[aplicativo AndroidM2Alfa7 áreas](</pt-BR/maturity/taxonomy#android-app>)

CoberturaExperimental0%

QualidadeAlfa59%

CompletudeAlfa66%

Nenhum

[Windows nativoM2Alfa4 áreas](</pt-BR/maturity/taxonomy#native-windows>)

CoberturaExperimental0%

QualidadeAlfa58%

CompletudeAlfa66%

Parcial - 1

[hospedagem KubernetesM2Alfa4 áreas](</pt-BR/maturity/taxonomy#kubernetes-hosting>)

CoberturaExperimental0%

QualidadeAlfa55%

CompletudeAlfa61%

Nenhum

[aplicativo iOSM1Experimental8 áreas](</pt-BR/maturity/taxonomy#ios-app>)

CoberturaExperimental0%

QualidadeExperimental41%

CompletudeExperimental44%

Nenhum

[Caminho de instalação do NixM1Experimental5 áreas](</pt-BR/maturity/taxonomy#nix-install-path>)

CoberturaExperimental0%

QualidadeExperimental41%

CompletudeExperimental44%

Nenhum

[Superfícies complementares do watchOSM1Experimental5 áreas](</pt-BR/maturity/taxonomy#watchos-companion-surfaces>)

CoberturaExperimental0%

QualidadeExperimental41%

CompletudeExperimental44%

Nenhum

[Aplicativo complementar para LinuxM0Planejado5 áreas](</pt-BR/maturity/taxonomy#linux-companion-app>)

CoberturaExperimental0%

QualidadeExperimental19%

CompletudeExperimental21%

Nenhum

[Aplicativo complementar nativo para WindowsM0Planejado5 áreas](</pt-BR/maturity/taxonomy#native-windows-companion-app>)

CoberturaExperimental0%

QualidadeExperimental19%

CompletudeExperimental21%

Nenhum

### Canal

[DiscordM4Estável6 áreas](</pt-BR/maturity/taxonomy#discord>)

CoberturaExperimental0%

QualidadeBeta73%

CompletudeEstável87%

Parcial - 4

[TelegramM3Beta5 áreas](</pt-BR/maturity/taxonomy#telegram>)

CoberturaExperimental0%

QualidadeAlfa68%

CompletudeBeta78%

Completo - 5

[SlackM3Beta5 áreas](</pt-BR/maturity/taxonomy#slack>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Completo - 5

[iMessage e BlueBubblesM3Beta5 áreas](</pt-BR/maturity/taxonomy#imessage-and-bluebubbles>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Nenhum

[WhatsAppM3Beta5 áreas](</pt-BR/maturity/taxonomy#whatsapp>)

CoberturaExperimental0%

QualidadeAlfa66%

CompletudeBeta78%

Nenhum

[MatrixM2Alfa6 áreas](</pt-BR/maturity/taxonomy#matrix>)

CoberturaExperimental0%

QualidadeAlfa60%

CompletudeAlfa67%

Nenhum

[Google ChatM2Alfa5 áreas](</pt-BR/maturity/taxonomy#google-chat>)

CoberturaExperimental0%

QualidadeAlfa59%

CompletudeAlfa66%

Nenhum

[Microsoft TeamsM2Alfa5 áreas](</pt-BR/maturity/taxonomy#microsoft-teams>)

CoberturaExperimental0%

QualidadeAlfa59%

CompletudeAlpha66%

Nenhum

[SignalM2Alpha5 áreas](</pt-BR/maturity/taxonomy#signal>)

CoberturaExperimental0%

QualidadeAlpha59%

CompletudeAlpha66%

Nenhum

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canais regionaisM2Alpha4 áreas](</pt-BR/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CoberturaExperimental0%

QualidadeAlpha55%

CompletudeAlpha58%

Nenhum

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 áreas](</pt-BR/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CoberturaExperimental0%

QualidadeAlpha53%

CompletudeAlpha54%

Nenhum

[Canal de chamadas de vozM1Experimental5 áreas](</pt-BR/maturity/taxonomy#voice-call-channel>)

CoberturaExperimental0%

QualidadeExperimental41%

CompletudeExperimental44%

Nenhum

### Provedor e ferramenta

[Automação de navegador, exec e ferramentas de sandboxM3Beta3 áreas](</pt-BR/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CoberturaExperimental21%

QualidadeBeta75%

CompletudeBeta79%

Parcial - 2

[Caminho de provedor OpenAI e CodexM3Beta5 áreas](</pt-BR/maturity/taxonomy#openai-and-codex-provider-path>)

CoberturaExperimental26%

QualidadeBeta74%

IntegridadeBeta79%

Parcial - 3

[Ferramentas de pesquisa na WebM3Beta4 áreas](</pt-BR/maturity/taxonomy#web-search-tools>)

CoberturaExperimental9%

QualidadeBeta74%

IntegridadeBeta79%

Nenhum

[Caminho do provedor AnthropicM3Beta5 áreas](</pt-BR/maturity/taxonomy#anthropic-provider-path>)

CoberturaExperimental0%

QualidadeBeta71%

IntegridadeBeta78%

Nenhum

[Caminho do provedor GoogleM3Beta5 áreas](</pt-BR/maturity/taxonomy#google-provider-path>)

CoberturaExperimental0%

QualidadeAlpha66%

IntegridadeBeta78%

Nenhum

[Caminho do provedor OpenRouterM3Beta4 áreas](</pt-BR/maturity/taxonomy#openrouter-provider-path>)

CoberturaExperimental0%

QualidadeAlpha66%

IntegridadeBeta78%

Nenhum

[Ferramentas de geração de imagem, vídeo e músicaM2Alpha5 áreas](</pt-BR/maturity/taxonomy#image-video-and-music-generation-tools>)

CoberturaExperimental0%

QualidadeAlpha61%

IntegridadeAlpha68%

Nenhum

[Provedores de modelos locais: Ollama, vLLM, SGLang, LM StudioM2Alpha5 áreas](</pt-BR/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CoberturaExperimental0%

QualidadeAlpha61%

IntegridadeAlpha68%

Nenhum

[Provedores hospedados de cauda longaM2Alfa3 áreas](</pt-BR/maturity/taxonomy#long-tail-hosted-providers>)

CoberturaExperimental0%

QualidadeAlfa61%

CompletudeAlfa68%

Nenhum

## Resumo de evidências de QA

As verificações abaixo mostram quais áreas do scorecard foram exercitadas pelas evidências do perfil de QA.

Validação completa da taxonomia 2026-06-23T07:24:36.128Z 96 verificações - 94 aprovadas, 2 bloqueadas 0 de 281 (0%) áreas - 20 de 1675 (1.2%) recursos - 77 de 1665 (4.6%) IDs de cobertura

### Prontidão por área

Abra uma superfície para inspecionar o estado das evidências de cada categoria. A lista permanece recolhida para que a página continue útil em uma visão rápida.

Runtime do agente - 9 áreas

8 parcialmente revisadas / 1 precisa de revisão

Execução de turno do agente Parcialmente revisada - Validação completa da taxonomia

0 de 3 (0%) / 7 de 24 (29.2%) 17 lacunas de capacidade

Runtimes externos e subagentes Parcialmente revisada - Validação completa da taxonomia

0 de 4 (0%) / 3 de 10 (30%) 7 lacunas de capacidade

Execução de provedor hospedado Parcialmente revisada - Validação completa da taxonomia

1 de 5 (20%) / 1 de 5 (20%) 4 lacunas de capacidade

Provedores locais e auto-hospedados Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Seleção de modelo e runtime Parcialmente revisada - Validação completa da taxonomia

0 de 4 (0%) / 2 de 8 (25%) 6 lacunas de capacidade

Autenticação do provedor Parcialmente revisada - Validação completa da taxonomia

0 de 10 (0%) / 4 de 17 (23.5%) 13 lacunas de capacidade

Streaming e progresso Parcialmente revisada - Validação completa da taxonomia

0 de 2 (0%) / 5 de 9 (55.6%) 4 lacunas de capacidade

Chamadas de ferramentas e tratamento de respostas Parcialmente revisada - Validação completa da taxonomia

0 de 3 (0%) / 15 de 23 (65.2%) 8 lacunas de capacidade

Controles de execução de ferramentas Parcialmente revisada - Validação completa da taxonomia

0 de 6 (0%) / 6 de 12 (50%) 6 lacunas de capacidade

Aplicativo Android - 7 áreas

7 precisam de revisão

Configuração da conexão Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Runtime do dispositivo Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Distribuição Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Captura de mídia Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Chat móvel Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Configurações Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Voz Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Caminho do provedor Anthropic - 5 áreas

5 precisam de revisão

Entradas de mídia Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Seleção de modelo e runtime Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 12 (0%) 12 lacunas de capacidade

Cache de prompt e contexto Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Autenticação e recuperação do provedor Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Transporte de requisição e semântica de turno Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Automação: cron, hooks, tarefas, polling - 6 áreas

5 precisam de revisão / 1 parcialmente revisado

Hooks de automação Precisa de revisão - Validação completa da taxonomia

0 de 11 (0%) / 0 de 11 (0%) 11 lacunas de capacidade

Tarefas e fluxos em segundo plano Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Tarefas Cron Precisa de revisão - Validação completa da taxonomia

0 de 15 (0%) / 0 de 15 (0%) 15 lacunas de capacidade

Entrada de eventos Precisa de revisão - Validação completa da taxonomia

0 de 15 (0%) / 0 de 15 (0%) 15 lacunas de capacidade

Heartbeat Parcialmente revisado - Validação completa da taxonomia

0 de 5 (0%) / 1 de 7 (14.3%) 6 lacunas de capacidade

Controles de polling Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Automação de navegador, exec e ferramentas de sandbox - 3 áreas

2 parcialmente revisados / 1 precisa de revisão

Automação de navegador Parcialmente revisado - Validação completa da taxonomia

1 de 8 (12.5%) / 1 de 8 (12.5%) 7 lacunas de capacidade

Política de sandbox e ferramentas Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Invocação e execução de ferramentas Parcialmente revisado - Validação completa da taxonomia

2 de 6 (33.3%) / 4 de 8 (50%) 4 lacunas de capacidade

Aplicativo Web do Gateway - 6 áreas

3 precisam de revisão / 3 parcialmente revisados

Acesso e confiança do navegador Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Conversa em tempo real no navegador Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

UI do navegador Parcialmente revisado - Validação completa da taxonomia

0 de 10 (0%) / 1 de 12 (8.3%) 11 lacunas de capacidade

Configuração Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Console do operador Parcialmente revisado - Validação completa da taxonomia

0 de 10 (0%) / 1 de 12 (8.3%) 11 lacunas de capacidade

Conversas do WebChat Parcialmente revisado - Validação completa da taxonomia

0 de 15 (0%) / 2 de 20 (10%) 18 lacunas de capacidade

Framework de canais - 8 áreas

4 precisam de revisão / 4 parcialmente revisados

Comandos de ações e aprovações de canais Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Configuração de canais Parcialmente revisado - Validação completa da taxonomia

0 de 5 (0%) / 1 de 7 (14.3%) 6 lacunas de capacidade

Roteamento e entrega de conversas Parcialmente revisado - Validação completa da taxonomia

0 de 10 (0%) / 5 de 27 (18.5%) 22 lacunas de capacidade

Comportamento de thread de grupo e sala ambiente Parcialmente revisado - Validação completa da taxonomia

0 de 5 (0%) / 4 de 11 (36.4%) 7 lacunas de capacidade

Portões de acesso de entrada e identidade Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Anexos de mídia e dados avançados de canais Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Entrega de saída e pipeline de respostas Parcialmente revisado - Validação completa da taxonomia

0 de 4 (0%) / 8 de 21 (38.1%) 13 lacunas de capacidade

Integridade de status e controles do operador Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

ClawHub - 4 áreas

4 precisam de revisão

Descoberta de catálogo Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Compatibilidade e confiança Precisa de revisão - Validação completa da taxonomia

0 de 12 (0%) / 0 de 12 (0%) 12 lacunas de capacidade

Ciclo de vida e integridade do Plugin Precisa de revisão - Validação completa da taxonomia

0 de 26 (0%) / 0 de 26 (0%) 26 lacunas de capacidade

Publicação Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

CLI - 7 áreas

5 precisam de revisão / 2 parcialmente revisadas

Observabilidade da CLI Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Configuração da CLI Parcialmente revisada - Validação completa da taxonomia

1 de 6 (16.7%) / 1 de 6 (16.7%) 5 lacunas de capacidade

Doctor Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Gerenciamento do serviço Gateway Parcialmente revisada - Validação completa da taxonomia

0 de 5 (0%) / 1 de 7 (14.3%) 6 lacunas de capacidade

Integração e configuração de autenticação Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Configuração de Plugin e canal Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Atualizações e upgrades Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Discord - 6 áreas

6 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Configuração e operações de canal Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 12 (0%) / 0 de 12 (0%) 12 lacunas de capacidade

Mídia e conteúdo rico Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Controles nativos e aprovações Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Voz e chamadas em tempo real Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Hospedagem Docker e Podman - 4 áreas

3 precisam de revisão / 1 parcialmente revisada

Sandbox e ferramentas do agente Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Operações de contêiner Precisa de revisão - Validação completa da taxonomia

0 de 11 (0%) / 0 de 11 (0%) 11 lacunas de capacidade

Configuração de contêiner Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Lançamento e validação de imagem Parcialmente revisada - Validação completa da taxonomia

1 de 5 (20%) / 2 de 7 (28.6%) 5 lacunas de capacidade

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canais regionais - 4 áreas

4 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Configuração e operações de canal Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Mídia e conteúdo avançado Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

runtime do Gateway - 13 áreas

9 precisam de revisão / 4 parcialmente revisadas

Aprovações e execução remota Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Autenticação e pareamento de dispositivos Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Ciclo de vida do Gateway Parcialmente revisado - Validação completa da taxonomia

0 de 7 (0%) / 4 de 12 (33.3%) 8 lacunas de capacidade

APIs RPC e eventos do Gateway Parcialmente revisado - Validação completa da taxonomia

0 de 20 (0%) / 2 de 22 (9.1%) 20 lacunas de capacidade

Saúde, diagnóstico e reparo Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Superfície web hospedada Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

APIs HTTP Parcialmente revisado - Validação completa da taxonomia

1 de 4 (25%) / 1 de 4 (25%) 3 lacunas de capacidade

Acesso e descoberta de rede Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Nós e capacidades remotas Precisa de revisão - Validação completa da taxonomia

0 de 8 (0%) / 0 de 8 (0%) 8 lacunas de capacidade

Compatibilidade de protocolo Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Funções e permissões Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Controles de segurança Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Conexão WebSocket Parcialmente revisado - Validação completa da taxonomia

1 de 8 (12.5%) / 1 de 8 (12.5%) 7 lacunas de capacidade

Google Chat - 5 áreas

5 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 11 (0%) / 0 de 11 (0%) 11 lacunas de capacidade

Configuração e operações de canal Precisa de revisão - Validação completa da taxonomia

0 de 16 (0%) / 0 de 16 (0%) 16 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Mídia e conteúdo avançado Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Controles nativos e aprovações Precisa de revisão - Validação completa da taxonomia

0 de 16 (0%) / 0 de 16 (0%) 16 lacunas de capacidade

Caminho do provedor Google - 5 áreas

5 precisam de revisão

Runtime direto do Gemini Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Mídia, pesquisa e tempo real Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Roteamento de modelos e endpoints Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Cache de prompts Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Configuração e credenciais do provedor Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Ferramentas de geração de imagens, vídeos e música - 5 áreas

5 precisam de revisão

Geração de imagens Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Roteamento e descoberta de mídia Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Geração de música Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Ciclo de vida e entrega de tarefas Precisa de revisão - Validação completa da taxonomia

0 de 12 (0%) / 0 de 12 (0%) 12 lacunas de capacidade

Geração de vídeo Precisa de revisão - Validação completa da taxonomia

0 de 11 (0%) / 0 de 11 (0%) 11 lacunas de capacidade

iMessage e BlueBubbles - 5 áreas

5 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Configuração e operações do canal Precisa de revisão - Validação completa da taxonomia

0 de 11 (0%) / 0 de 11 (0%) 11 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Mídia e conteúdo avançado Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Controles nativos e aprovações Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Aplicativo iOS - 8 áreas

8 precisam de revisão

Canvas e tela Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Chat e sessões Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Comandos do dispositivo Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Distribuição Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Configuração e diagnósticos do Gateway Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Mídia e compartilhamento Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Notificações e segundo plano Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Voz Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Hospedagem Kubernetes - 4 áreas

4 precisam de revisão

Acesso e exposição Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Ciclo de vida do cluster Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Configuração e segredos Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Configuração da implantação Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

App complementar Linux - 5 áreas

5 precisam de revisão

Distribuição do app Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Chat e sessões Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Capacidades de desktop Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Conectividade do Gateway Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Status e diagnósticos Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Host Gateway Linux - 5 áreas

5 precisam de revisão

Destinos de implantação Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Diagnósticos e reparo Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Ambiente de execução do Gateway e controle de serviço Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Configuração e atualizações do host Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Acesso remoto e segurança Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Provedores de modelos locais: Ollama, vLLM, SGLang, LM Studio - 5 áreas

5 precisam de revisão

Memória local e incorporações Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Plugins de provedores nativos Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Segurança de rede e controles de prompt Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Compatibilidade com ambientes de execução compatíveis com OpenAI Precisa de revisão - Validação completa da taxonomia

0 de 8 (0%) / 0 de 8 (0%) 8 lacunas de capacidade

Configuração, ciclo de vida e diagnósticos de provedores Precisa de revisão - Validação completa da taxonomia

0 de 12 (0%) / 0 de 12 (0%) 12 lacunas de capacidade

Provedores hospedados de cauda longa - 3 áreas

3 precisam de revisão

Provedores de LLM hospedados Precisa de revisão - Validação completa da taxonomia

0 de 12 (0%) / 0 de 12 (0%) 12 lacunas de capacidade

Provedores de mídia hospedados Precisa de revisão - Validação completa da taxonomia

0 de 8 (0%) / 0 de 8 (0%) 8 lacunas de capacidade

Operações de provedores Precisa de revisão - Validação completa da taxonomia

0 de 12 (0%) / 0 de 12 (0%) 12 lacunas de capacidade

app complementar do macOS - 8 áreas

8 precisam de revisão

Canvas Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Configuração local Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Capacidades nativas Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Conexões remotas Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

WebChat remoto Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Status e configurações Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Voz e conversa Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

WebChat Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

host Gateway do macOS - 7 áreas

7 precisam de revisão

Configuração da CLI Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Diagnóstico e observabilidade Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Ciclo de vida do serviço Gateway Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Integração local do Gateway Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Permissões e capacidades nativas Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Perfis e isolamento Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Modo Gateway remoto Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Matrix - 6 áreas

6 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Configuração e operações do canal Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Criptografia e verificação Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Mídia e conteúdo avançado Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Controles e aprovações nativos Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - 4 áreas

4 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Configuração e operações do canal Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Mídia e conteúdo rico Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Compreensão de mídia e geração de mídia - 6 áreas

4 precisam de revisão / 2 parcialmente revisadas

Tratamento de mídia do canal Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Configuração de mídia Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Geração de mídia Parcialmente revisado - Validação completa da taxonomia

1 de 17 (5.9%) / 1 de 19 (5.3%) 18 lacunas de capacidade

Entrada e acesso de mídia Precisa de revisão - Validação completa da taxonomia

0 de 8 (0%) / 0 de 8 (0%) 8 lacunas de capacidade

Compreensão de mídia Parcialmente revisado - Validação completa da taxonomia

0 de 12 (0%) / 1 de 14 (7.1%) 13 lacunas de capacidade

Entrega de conversão de texto em fala Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Microsoft Teams - 5 áreas

5 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Configuração e operações do canal Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Mídia e conteúdo rico Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Controles nativos e aprovações Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Windows nativo - 4 áreas

4 precisam de revisão

CLI Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Gerenciamento do Gateway Precisa de revisão - Validação completa da taxonomia

0 de 11 (0%) / 0 de 11 (0%) 11 lacunas de capacidade

Rede Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Atualizações Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Aplicativo complementar nativo para Windows - 5 áreas

5 precisam de revisão

Sessões de chat Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Ferramentas e permissões de desktop Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Conexão do Gateway Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Instalação e atualizações Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Status e reparo Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Caminho de instalação do Nix - 5 áreas

5 precisam de revisão

Ativação e UX do aplicativo Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Configuração e estado Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Transferência de instalação Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Ciclo de vida do Plugin Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Tempo de execução do serviço e proteções Precisa de revisão - Validação completa da taxonomia

0 de 8 (0%) / 0 de 8 (0%) 8 lacunas de capacidade

Caminho de provedores OpenAI e Codex - 5 áreas

2 precisam de revisão / 3 parcialmente revisadas

Entrada de imagem e multimodal Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Modelo e autenticação Parcialmente revisado - Validação completa da taxonomia

1 de 6 (16.7%) / 4 de 9 (44.4%) 5 lacunas de capacidade

Harness nativo do Codex Parcialmente revisado - Validação completa da taxonomia

0 de 2 (0%) / 4 de 9 (44.4%) 5 lacunas de capacidade

Compatibilidade de respostas e ferramentas Parcialmente revisado - Validação completa da taxonomia

1 de 4 (25%) / 2 de 5 (40%) 3 lacunas de capacidade

Voz e áudio em tempo real Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

SDK de aplicativos OpenClaw - 6 áreas

5 precisam de revisão / 1 parcialmente revisada

Conversas de agentes Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

API de cliente Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Compatibilidade Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Eventos e aprovações Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Acesso ao Gateway Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Auxiliares de recursos Parcialmente revisado - Validação completa da taxonomia

0 de 5 (0%) / 1 de 6 (16.7%) 5 lacunas de capacidade

Caminho do provedor OpenRouter - 4 áreas

4 precisam de revisão

Runtime de chat e normalização Precisa de revisão - Validação completa da taxonomia

0 de 15 (0%) / 0 de 15 (0%) 15 lacunas de capacidade

Geração de mídia e fala Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Recuperação e diagnósticos do provedor Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Configuração e autenticação do provedor Precisa de revisão - Validação completa da taxonomia

0 de 14 (0%) / 0 de 14 (0%) 14 lacunas de capacidade

Plugins - 9 áreas

6 precisam de revisão / 3 parcialmente revisadas

Autoria e empacotamento de plugins Precisa de revisão - Validação completa da taxonomia

0 de 8 (0%) / 0 de 8 (0%) 8 lacunas de capacidade

Plugins incluídos Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Plugin Canvas Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Plugins de canais Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Instalação e execução de plugins Parcialmente revisado - Validação completa da taxonomia

0 de 6 (0%) / 7 de 20 (35%) 13 lacunas de capacidade

Aprovações de Plugin Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Plugins de provedor e ferramentas Parcialmente revisado - Validação completa da taxonomia

1 de 6 (16.7%) / 9 de 21 (42.9%) 12 lacunas de capacidade

Publicação de plugins Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Teste de plugins Parcialmente revisado - Validação completa da taxonomia

0 de 6 (0%) / 3 de 11 (27.3%) 8 lacunas de capacidade

Raspberry Pi e pequenos dispositivos Linux - 4 áreas

4 precisam de revisão

Runtime do Gateway Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Desempenho e diagnósticos Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Acesso remoto e autenticação Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Configuração e compatibilidade Precisa de revisão - Validação completa da taxonomia

0 de 12 (0%) / 0 de 12 (0%) 12 lacunas de capacidade

Segurança, autenticação, pareamento e segredos - 6 áreas

2 parcialmente revisadas / 4 precisam de revisão

Política de aprovação e proteções de ferramentas Parcialmente revisado - Validação completa da taxonomia

0 de 2 (0%) / 3 de 6 (50%) 3 lacunas de capacidade

Controle de acesso a canais Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Higiene de credenciais e segredos Parcialmente revisado - Validação completa da taxonomia

0 de 5 (0%) / 5 de 11 (45.5%) 6 lacunas de capacidade

Pareamento de dispositivos e Node Precisa de revisão - Validação completa da taxonomia

0 de 11 (0%) / 0 de 11 (0%) 11 lacunas de capacidade

Autenticação do Gateway e acesso remoto Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Confiança em Plugin Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Sessão, memória e motor de contexto - 9 áreas

2 precisam de revisão / 7 parcialmente revisadas

Gerenciamento de sessões da CLI e transcrições Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Motor de contexto Parcialmente revisada - Validação completa da taxonomia

0 de 2 (0%) / 4 de 7 (57,1%) 3 lacunas de capacidade

Prompts e contexto principais Parcialmente revisada - Validação completa da taxonomia

0 de 2 (0%) / 3 de 8 (37,5%) 5 lacunas de capacidade

Histórico entre clientes e paridade de sessões Parcialmente revisada - Validação completa da taxonomia

0 de 2 (0%) / 2 de 5 (40%) 3 lacunas de capacidade

Diagnósticos, manutenção e recuperação Parcialmente revisada - Validação completa da taxonomia

0 de 3 (0%) / 4 de 10 (40%) 6 lacunas de capacidade

Memória Parcialmente revisada - Validação completa da taxonomia

0 de 5 (0%) / 6 de 13 (46,2%) 7 lacunas de capacidade

Roteamento de sessões Parcialmente revisada - Validação completa da taxonomia

0 de 2 (0%) / 1 de 4 (25%) 3 lacunas de capacidade

Gerenciamento de tokens Parcialmente revisada - Validação completa da taxonomia

0 de 3 (0%) / 2 de 10 (20%) 8 lacunas de capacidade

Persistência de transcrições Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Signal - 5 áreas

5 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Configuração e operações do canal Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Mídia e conteúdo avançado Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Controles nativos e aprovações Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Slack - 5 áreas

5 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Configuração e operações do canal Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Mídia e conteúdo avançado Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Controles nativos e aprovações Precisa de revisão - Validação completa da taxonomia

0 de 8 (0%) / 0 de 8 (0%) 8 lacunas de capacidade

Telegram - 5 áreas

5 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Configuração e operações do canal Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Mídia e conteúdo avançado Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Controles nativos e aprovações Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Observabilidade - 5 áreas

3 parcialmente revisadas / 2 precisam de revisão

Coleta de diagnósticos Parcialmente revisada - Validação completa da taxonomia

1 de 8 (12.5%) / 3 de 10 (30%) 7 lacunas de capacidade

Integridade e reparo Parcialmente revisada - Validação completa da taxonomia

1 de 12 (8.3%) / 5 de 18 (27.8%) 13 lacunas de capacidade

Registro em logs Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Diagnósticos de sessão Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Exportação de telemetria Parcialmente revisada - Validação completa da taxonomia

1 de 13 (7.7%) / 7 de 21 (33.3%) 14 lacunas de capacidade

TUI - 5 áreas

5 precisam de revisão

Entrada e comandos Precisa de revisão - Validação completa da taxonomia

0 de 8 (0%) / 0 de 8 (0%) 8 lacunas de capacidade

Execução de shell local Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Renderização e segurança da saída Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Modos de runtime Precisa de revisão - Validação completa da taxonomia

0 de 14 (0%) / 0 de 14 (0%) 14 lacunas de capacidade

Gerenciamento de sessão Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Voz e conversa em tempo real - 6 áreas

6 precisam de revisão

Conversa no app nativo Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Sessões de conversa em tempo real Precisa de revisão - Validação completa da taxonomia

0 de 11 (0%) / 0 de 11 (0%) 11 lacunas de capacidade

Fala e transcrição Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Observabilidade da conversa Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Provedores de conversa Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Ativação por voz e roteamento Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Canal de chamadas de voz - 5 áreas

5 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Configuração e operações do canal Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 1 (0%) / 0 de 1 (0%) 1 lacuna de capacidade

Mídia e conteúdo avançado Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Voz e chamadas em tempo real Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

superfícies complementares do watchOS - 5 áreas

5 precisam de revisão

Entrega e recuperação Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Distribuição e suporte Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

Aprovações executivas Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Notificações e respostas Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

UI do app Watch Precisa de revisão - Validação completa da taxonomia

0 de 3 (0%) / 0 de 3 (0%) 3 lacunas de capacidade

Ferramentas de pesquisa na Web - 4 áreas

2 precisam de revisão / 2 parcialmente revisadas

Segurança de rede Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Provedores de pesquisa Parcialmente revisado - Validação completa da taxonomia

2 de 19 (10.5%) / 2 de 19 (10.5%) 17 lacunas de capacidade

Configuração e diagnóstico Precisa de revisão - Validação completa da taxonomia

0 de 9 (0%) / 0 de 9 (0%) 9 lacunas de capacidade

Disponibilidade e busca de ferramentas Parcialmente revisado - Validação completa da taxonomia

2 de 11 (18.2%) / 3 de 12 (25%) 9 lacunas de capacidade

WhatsApp - 5 áreas

5 precisam de revisão

Acesso e identidade Precisa de revisão - Validação completa da taxonomia

0 de 7 (0%) / 0 de 7 (0%) 7 lacunas de capacidade

Configuração e operações do canal Precisa de revisão - Validação completa da taxonomia

0 de 5 (0%) / 0 de 5 (0%) 5 lacunas de capacidade

Roteamento e entrega de conversas Precisa de revisão - Validação completa da taxonomia

0 de 4 (0%) / 0 de 4 (0%) 4 lacunas de capacidade

Mídia e conteúdo rico Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Controles nativos e aprovações Precisa de revisão - Validação completa da taxonomia

0 de 2 (0%) / 0 de 2 (0%) 2 lacunas de capacidade

Windows via WSL2 - 6 áreas

5 precisam de revisão / 1 parcialmente revisada

Navegador e UI de controle Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

CLI Precisa de revisão - Validação completa da taxonomia

0 de 8 (0%) / 0 de 8 (0%) 8 lacunas de capacidade

Diagnóstico e reparo Parcialmente revisado - Validação completa da taxonomia

1 de 6 (16.7%) / 3 de 8 (37.5%) 5 lacunas de capacidade

Acesso e exposição do Gateway Precisa de revisão - Validação completa da taxonomia

0 de 11 (0%) / 0 de 11 (0%) 11 lacunas de capacidade

Ciclo de vida do serviço Gateway Precisa de revisão - Validação completa da taxonomia

0 de 10 (0%) / 0 de 10 (0%) 10 lacunas de capacidade

Configuração do WSL Precisa de revisão - Validação completa da taxonomia

0 de 6 (0%) / 0 de 6 (0%) 6 lacunas de capacidade

> Última atualização: 2026-06-22

Was this useful?YesNo

Open issue