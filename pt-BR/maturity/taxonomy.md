---
title: Taxonomia de maturidade
source_url: https://docs.openclaw.ai/pt-BR/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Taxonomia de maturidade

o modelo por trás do scorecard

Superfícies > categorias > capacidades > evidências.

50 superfícies agrupadas em 4 famílias, com cada categoria vinculada à documentação canônica e aos IDs de cobertura de QA.

Navegar pelas áreas do produto / Abrir taxonomia detalhada / [Ver pontuações](</pt-BR/maturity/scorecard>)

## Como ler esta página

Uma superfície é uma área do produto, como runtime do Gateway, Discord ou o app para macOS. Cada superfície contém categorias, e cada categoria contém as verificações em nível de capacidade cobertas pelos cenários de QA. Use o scorecard para julgamento em nível de release; use esta página para inspecionar o modelo por baixo dele.

## Níveis de maturidade

M0PlanejadoA direção é conhecida, mas não existe nenhum caminho de usuário com suporte.Promoção: problema de design, responsável e superfície-alvo existem.

M1ExperimentalImplementado com ressalvas, flags, builds a partir do código-fonte ou fluxos apenas para mantenedores.Promoção: mantenedor consegue executar o cenário a partir da main atual.

M2AlfaUsuários reais podem experimentar, mas mudanças incompatíveis e UX incompleta são esperadas.Promoção: configuração documentada, testes básicos, ressalvas conhecidas e pelo menos uma prova em ambiente real.

M3BetaExiste um caminho público, e o fluxo principal é utilizável com ressalvas delimitadas.Promoção: documentação de instalação/atualização, testes de regressão, runbook de suporte e prova de cenário bem-sucedida no ambiente esperado.

M4EstávelCaminho recomendado para usuários normais. Falhas são tratadas como regressões.Promoção: gate de release, caminho de doctor/solução de problemas, documentação ampla e provas repetidas no mundo real.

M5ClawesomePolido, agradável, bem instrumentado e competitivo com o melhor fluxo comparável.Promoção: estável mais aprovação no scorecard de usuário com usuários representativos.

## Áreas do produto

### Núcleo

CLI M4Estável7 áreas - 90% concluído Runtime do Gateway M4Estável13 áreas - 89% concluído Runtime do agente M3Beta9 áreas - 79% concluído Sessão, memória e mecanismo de contexto M3Beta9 áreas - 79% concluído Framework de canais M3Beta8 áreas - 79% concluído Observabilidade M3Beta5 áreas - 79% concluído App web do Gateway M3Beta6 áreas - 79% concluído Plugins M3Beta9 áreas - 79% concluído Segurança, autenticação, pareamento e segredos M3Beta6 áreas - 79% concluído Automação: cron, ganchos, tarefas, consulta periódica M3Beta6 áreas - 79% concluído Compreensão e geração de mídia M2Alpha6 áreas - 68% concluído Voz e conversa em tempo real M2Alpha6 áreas - 68% concluído TUI M2Alpha5 áreas - 66% concluído ClawHub M2Alpha4 áreas - 62% concluído SDK do aplicativo OpenClaw M2Alpha6 áreas - 53% concluído

### Plataforma

Host Linux do Gateway M4Estável5 áreas - 89% concluído Host macOS do Gateway M4Estável7 áreas - 88% concluído Hospedagem com Docker e Podman M3Beta4 áreas - 79% concluído Windows via WSL2 M3Beta6 áreas - 79% concluído Raspberry Pi e dispositivos Linux pequenos M3Beta4 áreas - 79% concluído Aplicativo complementar para macOS M3Beta8 áreas - 78% concluído Aplicativo Android M2Alpha7 áreas - 66% concluído Windows nativo M2Alpha4 áreas - 66% concluído Hospedagem Kubernetes M2Alpha4 áreas - 61% concluído app iOS M1Experimental8 áreas - 44% concluído Caminho de instalação Nix M1Experimental5 áreas - 44% concluído Superfícies complementares watchOS M1Experimental5 áreas - 44% concluído App complementar Linux M0Planejado5 áreas - 21% concluído App complementar Windows nativo M0Planejado5 áreas - 21% concluído

### Canal

Discord M4Estável6 áreas - 87% concluído Telegram M3Beta5 áreas - 78% concluído Slack M3Beta5 áreas - 78% concluído iMessage e BlueBubbles M3Beta5 áreas - 78% concluído WhatsApp M3Beta5 áreas - 78% concluído Matrix M2Alpha6 áreas - 67% concluído Google Chat M2Alpha5 áreas - 66% concluído Microsoft Teams M2Alpha5 áreas - 66% concluído Signal M2Alpha5 áreas - 66% concluído Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canais regionais M2Alpha4 áreas - 58% concluído Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alpha4 áreas - 54% concluído Canal de chamadas de voz M1Experimental5 áreas - 44% concluído

### Provedor e ferramenta

Automação de navegador, exec e ferramentas de sandbox M3Beta3 áreas - 79% concluído Caminho de provedor OpenAI e Codex M3Beta5 áreas - 79% concluído Ferramentas de pesquisa na Web M3Beta4 áreas - 79% concluído Caminho de provedor Anthropic M3Beta5 áreas - 78% concluído Caminho de provedor Google M3Beta5 áreas - 78% concluído Caminho de provedor OpenRouter M3Beta4 áreas - 78% concluído Ferramentas de geração de imagem, vídeo e música M2Alpha5 áreas - 68% concluído Provedores locais de modelos: Ollama, vLLM, SGLang, LM Studio M2Alpha5 áreas - 68% concluído Provedores hospedados de cauda longa M2Alpha3 áreas - 68% concluído

## Detalhes

### Núcleo

CLI - M4 Estável - 7 áreas

Os caminhos normais de configuração e reparo são documentados nos documentos de instalação, CLI e Gateway. Caminhos específicos de plataforma para Windows são acompanhados nas linhas Windows via WSL2 e Windows nativo.

Cobertura Experimental - 4%Qualidade Estável - 83%Completude Estável - 90%Parcial - 6

Configuração da CLI 6 capacidades / compatível com LTS

Experimental17%

Estável89%

Estável90%

[Índice](</pt-BR/install>), [Instalador](</pt-BR/install/installer>), [Node](</pt-BR/install/node>), [Atualização](</pt-BR/install/updating>)

Configuração de integração inicial e autenticação 5 capacidades / compatível com LTS

Experimental0%

Beta75%

Estável89%

[Integração inicial](</pt-BR/cli/onboard>), [Configurar](</pt-BR/cli/configure>), [Visão geral da integração inicial](</pt-BR/start/onboarding-overview>)

Configuração de Plugin e canal 5 capacidades

Experimental0%

Beta75%

Estável89%

[Integração inicial](</pt-BR/cli/onboard>), [Plugins](</pt-BR/cli/plugins>), [Canais](</pt-BR/cli/channels>)

Gerenciamento do serviço Gateway 5 capacidades / compatível com LTS

Experimental14%

Estável87%

Estável90%

[Gateway](</pt-BR/cli/gateway>), [Atualização](</pt-BR/install/updating>), [Solução de problemas](</pt-BR/gateway/troubleshooting>)

Observabilidade da CLI 5 capacidades / compatível com LTS

Experimental0%

Estável89%

Estável90%

[Status](</pt-BR/cli/status>), [Saúde](</pt-BR/cli/health>), [Logs](</pt-BR/cli/logs>), [Diagnósticos](</pt-BR/gateway/diagnostics>)

Doctor 10 capacidades / compatível com LTS

Experimental0%

Estável89%

Estável90%

[Doctor](</pt-BR/cli/doctor>), [Doctor](</pt-BR/gateway/doctor>), [Segredos](</pt-BR/gateway/secrets>), [Solução de problemas](</pt-BR/gateway/troubleshooting>)

Atualizações e upgrades 5 capacidades / compatível com LTS

Experimental0%

Beta75%

Estável89%

[Atualização](</pt-BR/install/updating>), [Atualizar](</pt-BR/cli/update>), [Solução de problemas](</pt-BR/gateway/troubleshooting>)

Gateway runtime - M4 Stable - 13 areas

A arquitetura central, autenticação, pareamento, documentação do protocolo, documentação do daemon e runbooks da CLI são amplos e atuais.

Cobertura Experimental - 6%Qualidade Estável - 81%Completude Estável - 89%Parcial - 12

Aprovações e execução remota 6 recursos / com suporte LTS

Experimental0%

Beta75%

Estável89%

[Protocolo](</pt-BR/gateway/protocol>), [Índice](</pt-BR/gateway/security>)

APIs HTTP 4 recursos / com suporte LTS

Experimental25%

Estável90%

Estável90%

[Índice](</pt-BR/gateway>), [API HTTP da OpenAI](</pt-BR/gateway/openai-http-api>), [API HTTP da OpenResponses](</pt-BR/gateway/openresponses-http-api>), [API HTTP de invocação de ferramentas](</pt-BR/gateway/tools-invoke-http-api>), [Hooks](</pt-BR/automation/hooks>), [Índice](</pt-BR/web>)

Superfície web hospedada 4 recursos / com suporte LTS

Experimental0%

Estável89%

Estável90%

[Índice](</pt-BR/gateway>), [Arquitetura](</pt-BR/concepts/architecture>), [UI de controle](</pt-BR/web/control-ui>), [Chat web](</pt-BR/web/webchat>), [Canvas](</pt-BR/refactor/canvas>)

APIs RPC e eventos do Gateway 20 recursos / com suporte LTS

Experimental9%

Estável90%

Estável90%

[Protocolo](</pt-BR/gateway/protocol>), [Índice](</pt-BR/gateway>), [Arquitetura](</pt-BR/concepts/architecture>)

Autenticação e pareamento de dispositivos 10 recursos / com suporte LTS

Experimental0%

Beta75%

Estável89%

[Protocolo](</pt-BR/gateway/protocol>), [Pareamento](</pt-BR/gateway/pairing>), [Índice](</pt-BR/gateway/security>)

Acesso e descoberta de rede 6 recursos / com suporte LTS

Experimental0%

Beta75%

Estável89%

[Índice](</pt-BR/gateway>), [Descoberta](</pt-BR/gateway/discovery>), [Protocolo](</pt-BR/gateway/protocol>)

Nodes e recursos remotos 8 recursos

Experimental0%

Beta75%

Estável89%

[Protocolo](</pt-BR/gateway/protocol>), [Arquitetura](</pt-BR/concepts/architecture>), [Índice](</pt-BR/nodes>)

Integridade, diagnóstico e reparo 7 recursos / com suporte LTS

Experimental0%

Beta75%

Estável89%

[Índice](</pt-BR/gateway>), [Diagnósticos](</pt-BR/gateway/diagnostics>), [Doctor](</pt-BR/gateway/doctor>)

Compatibilidade de protocolo 7 capacidades / com suporte a LTS

Experimental0%

Beta75%

Estável89%

[Protocolo](</pt-BR/gateway/protocol>), [Arquitetura](</pt-BR/concepts/architecture>), [Typebox](</pt-BR/concepts/typebox>), [Protocolo de ponte](</pt-BR/gateway/bridge-protocol>)

Funções e permissões 5 capacidades / com suporte a LTS

Experimental0%

Beta75%

Estável89%

[Protocolo](</pt-BR/gateway/protocol>), [Índice](</pt-BR/gateway/security>)

Ciclo de vida do Gateway 7 capacidades / com suporte a LTS

Experimental33%

Estável90%

Estável90%

[Índice](</pt-BR/gateway>), [Arquitetura](</pt-BR/concepts/architecture>)

Controles de segurança 6 capacidades / com suporte a LTS

Experimental0%

Beta75%

Estável89%

[Índice](</pt-BR/gateway/security>), [Protocolo](</pt-BR/gateway/protocol>), [Descoberta](</pt-BR/gateway/discovery>)

Conexão WebSocket 8 capacidades / com suporte a LTS

Experimental13%

Estável90%

Estável90%

[Protocolo](</pt-BR/gateway/protocol>), [Arquitetura](</pt-BR/concepts/architecture>)

Tempo de execução do agente - M3 Beta - 9 áreas

O loop principal, os modelos, o roteamento de provedores e o streaming de ferramentas são recursos de primeira classe, mas o comportamento dos provedores muda semanalmente e exige comprovação por cenário a cada lançamento.

Cobertura Experimental - 33%Qualidade Beta - 78%Completude Beta - 79%Parcial - 6

Execução de turnos do agente 3 capacidades / com suporte LTS

Experimental29%

Beta79%

Beta79%

[Loop do agente](</pt-BR/concepts/agent-loop>), [Agente](</pt-BR/cli/agent>), [Runtimes de agente](</pt-BR/concepts/agent-runtimes>)

Runtimes externos e subagentes 4 capacidades

Experimental30%

Beta79%

Beta79%

[Runtimes de agente](</pt-BR/concepts/agent-runtimes>), [Anthropic](</pt-BR/providers/anthropic>), [Google](</pt-BR/providers/google>), [Subagentes](</pt-BR/tools/subagents>)

Execução por provedores hospedados 5 capacidades / com suporte LTS

Experimental20%

Beta79%

Beta79%

[Openai](</pt-BR/providers/openai>), [Anthropic](</pt-BR/providers/anthropic>), [Google](</pt-BR/providers/google>), [Modelos](</pt-BR/concepts/models>)

Provedores locais e auto-hospedados 5 capacidades

Experimental0%

Alpha68%

Beta79%

[Ollama](</pt-BR/providers/ollama>), [Modelos](</pt-BR/concepts/models>), [Agente](</pt-BR/cli/agent>)

Seleção de modelo e runtime 4 capacidades / com suporte LTS

Experimental25%

Beta79%

Beta79%

[Modelos](</pt-BR/concepts/models>), [Modelos](</pt-BR/cli/models>), [Openai](</pt-BR/providers/openai>), [Runtimes de agente](</pt-BR/concepts/agent-runtimes>)

Autenticação de provedor 10 capacidades / com suporte LTS

Experimental24%

Beta79%

Beta79%

[Modelos](</pt-BR/concepts/models>), [Agente](</pt-BR/cli/agent>), [Modelos](</pt-BR/cli/models>), [Openai](</pt-BR/providers/openai>), [Anthropic](</pt-BR/providers/anthropic>), [Google](</pt-BR/providers/google>), [Subagentes](</pt-BR/tools/subagents>)

Streaming e progresso 2 capacidades

Alpha56%

Beta79%

Beta79%

[Streaming](</pt-BR/concepts/streaming>), [Loop do agente](</pt-BR/concepts/agent-loop>)

Chamadas de ferramenta e tratamento de respostas 3 capacidades / com suporte LTS

Alpha65%

Beta79%

Beta79%

[Loop do agente](</pt-BR/concepts/agent-loop>), [Ollama](</pt-BR/providers/ollama>)

Controles de execução de ferramentas 6 capacidades / com suporte LTS

Alfa50%

Beta79%

Beta79%

[Política de sandbox vs. ferramentas vs. elevado](</pt-BR/gateway/sandbox-vs-tool-policy-vs-elevated>), [Loop do agente](</pt-BR/concepts/agent-loop>), [Subagentes](</pt-BR/tools/subagents>)

Sessão, memória e mecanismo de contexto - M3 Beta - 9 áreas

Documentação sólida e implementação ativa. A maturidade depende da durabilidade da transcrição, da qualidade da Compaction e da paridade entre clientes.

Cobertura Experimental - 30%Qualidade Beta - 77%Completude Beta - 79%Parcial - 6

Gerenciamento de sessões e transcritos da CLI 2 capacidades / compatível com LTS

Experimental0%

Alfa68%

Beta79%

[Sessão](</pt-BR/concepts/session>), [Compaction de gerenciamento de sessões](</pt-BR/reference/session-management-compaction>), [Sessões](</pt-BR/cli/sessions>)

Gerenciamento de tokens 3 capacidades / compatível com LTS

Experimental20%

Beta79%

Beta79%

[Compaction](</pt-BR/concepts/compaction>), [Contexto](</pt-BR/concepts/context>), [Compaction de gerenciamento de sessões](</pt-BR/reference/session-management-compaction>)

Mecanismo de contexto 2 capacidades / compatível com LTS

Alfa57%

Beta79%

Beta79%

[Contexto](</pt-BR/concepts/context>), [Mecanismo de contexto](</pt-BR/concepts/context-engine>), [Ambiente do mecanismo de contexto do Codex](</pt-BR/plan/codex-context-engine-harness>)

Paridade de histórico e sessões entre clientes 2 capacidades

Experimental40%

Beta79%

Beta79%

[Chat web](</pt-BR/web/webchat>), [Android](</pt-BR/platforms/android>), [Roteamento de canais](</pt-BR/channels/channel-routing>)

Diagnóstico, manutenção e recuperação 3 capacidades

Experimental40%

Beta79%

Beta79%

[Diagnóstico](</pt-BR/gateway/diagnostics>), [Compaction de gerenciamento de sessões](</pt-BR/reference/session-management-compaction>), [Flags](</pt-BR/diagnostics/flags>)

Prompts e contexto centrais 2 capacidades / compatível com LTS

Experimental38%

Beta79%

Beta79%

[Contexto](</pt-BR/concepts/context>), [Higiene de transcritos](</pt-BR/reference/transcript-hygiene>), [Discord](</pt-BR/channels/discord>)

Memória 5 capacidades

Experimental46%

Beta79%

Beta79%

[Configuração de memória](</pt-BR/reference/memory-config>), [Qmd de memória](</pt-BR/concepts/memory-qmd>), [Memória](</pt-BR/concepts/memory>), [Discord](</pt-BR/channels/discord>)

Roteamento de sessões 2 capacidades / compatível com LTS

Experimental25%

Beta79%

Beta79%

[Sessão](</pt-BR/concepts/session>), [Roteamento de canais](</pt-BR/channels/channel-routing>), [Discord](</pt-BR/channels/discord>)

Persistência de transcrições 2 capacidades / com suporte LTS

Experimental0%

Alfa68%

Beta79%

[Compaction de gerenciamento de sessões](</pt-BR/reference/session-management-compaction>), [Higiene de transcrições](</pt-BR/reference/transcript-hygiene>)

Framework de canais - M3 Beta - 8 áreas

Muitos canais compartilham contratos de entrega e roteamento do Gateway, mas o comportamento dos canais varia conforme a API upstream e as restrições de política da conta.

Cobertura experimental - 13%Qualidade Beta - 76%Completude Beta - 79%Parcial - 5

Comandos de Ações e Aprovações de Canais 5 capacidades

Experimental0%

Beta79%

Beta79%

[Grupos](</pt-BR/channels/groups>), [Discord](</pt-BR/channels/discord>), [Google Chat](</pt-BR/channels/googlechat>), [Signal](</pt-BR/channels/signal>), [Matrix](</pt-BR/channels/matrix>)

Configuração de Canais 5 capacidades / com suporte LTS

Experimental14%

Beta79%

Beta79%

[Índice](</pt-BR/channels>), [Pareamento](</pt-BR/channels/pairing>), [Solução de problemas](</pt-BR/channels/troubleshooting>), [Plugins de Canal do SDK](</pt-BR/plugins/sdk-channel-plugins>)

Comportamento de Threads de Grupo e Salas Ambiente 5 capacidades

Experimental36%

Beta79%

Beta79%

[Grupos](</pt-BR/channels/groups>), [Mensagens de Grupo](</pt-BR/channels/group-messages>), [Eventos de Sala Ambiente](</pt-BR/channels/ambient-room-events>), [Grupos de Transmissão](</pt-BR/channels/broadcast-groups>), [Discord](</pt-BR/channels/discord>)

Acesso de Entrada e Portões de Identidade 5 capacidades / com suporte LTS

Experimental0%

Alfa68%

Beta79%

[Grupos de Acesso](</pt-BR/channels/access-groups>), [Grupos](</pt-BR/channels/groups>), [Discord](</pt-BR/channels/discord>), [LINE](</pt-BR/channels/line>)

Anexos de Mídia e Dados Avançados de Canal 4 capacidades

Experimental0%

Alfa68%

Beta79%

[LINE](</pt-BR/channels/line>), [Signal](</pt-BR/channels/signal>), [Google Chat](</pt-BR/channels/googlechat>), [Matrix](</pt-BR/channels/matrix>), [Discord](</pt-BR/channels/discord>)

Entrega de Saída e Pipeline de Resposta 4 capacidades / com suporte LTS

Experimental38%

Beta79%

Beta79%

[Grupos](</pt-BR/channels/groups>), [Eventos de Sala Ambiente](</pt-BR/channels/ambient-room-events>), [Discord](</pt-BR/channels/discord>), [Matrix](</pt-BR/channels/matrix>), [Canais de Configuração](</pt-BR/gateway/config-channels>)

Roteamento e Entrega de Conversas 10 capacidades / com suporte LTS

Experimental19%

Beta79%

Beta79%

[Roteamento de Canais](</pt-BR/channels/channel-routing>), [Grupos](</pt-BR/channels/groups>), [Discord](</pt-BR/channels/discord>), [Matrix](</pt-BR/channels/matrix>), [Solução de problemas](</pt-BR/channels/troubleshooting>), [Referência de Configuração](</pt-BR/gateway/configuration-reference>)

Integridade de Status e Controles do Operador 4 capacidades / com suporte LTS

Experimental0%

Beta79%

Beta79%

[Saúde](</pt-BR/gateway/health>), [Referência de configuração](</pt-BR/gateway/configuration-reference>), [Solução de problemas](</pt-BR/channels/troubleshooting>), [Discord](</pt-BR/channels/discord>)

Observability - M3 Beta - 5 areas

OTel, Prometheus, registro de logs e documentação de diagnósticos existem. Precisa de uma revisão pública de maturidade sobre "o que os operadores devem verificar primeiro".

Cobertura Experimental - 18%Qualidade Beta - 75%Completude Beta - 79%Parcial - 3

Saúde e Reparo 12 capacidades / com suporte LTS

Experimental28%

Beta79%

Beta79%

[Saúde](</pt-BR/gateway/health>), [Telegram](</pt-BR/channels/telegram>), [Doctor](</pt-BR/cli/doctor>), [Doctor](</pt-BR/gateway/doctor>), [Subcaminhos do SDK](</pt-BR/plugins/sdk-subpaths>), [Saúde](</pt-BR/cli/health>), [Protocolo](</pt-BR/gateway/protocol>)

Registro de logs 5 capacidades / com suporte LTS

Experimental0%

Alpha68%

Beta79%

[Registro de logs](</pt-BR/logging>), [Registro de logs](</pt-BR/gateway/logging>), [Logs](</pt-BR/cli/logs>)

Coleta de diagnósticos 8 capacidades

Experimental30%

Beta79%

Beta79%

[Diagnósticos](</pt-BR/gateway/diagnostics>), [Saúde](</pt-BR/gateway/health>), [Harness do Codex](</pt-BR/plugins/codex-harness>), [Protocolo](</pt-BR/gateway/protocol>)

Exportação de telemetria 13 capacidades

Experimental33%

Beta79%

Beta79%

[Hooks](</pt-BR/plugins/hooks>), [Opentelemetry](</pt-BR/gateway/opentelemetry>), [Registro de logs](</pt-BR/logging>), [Subcaminhos do SDK](</pt-BR/plugins/sdk-subpaths>), [Diagnostics Otel](</pt-BR/plugins/reference/diagnostics-otel>), [Prometheus](</pt-BR/gateway/prometheus>), [Diagnostics Prometheus](</pt-BR/plugins/reference/diagnostics-prometheus>)

Diagnósticos de sessão 4 capacidades / com suporte LTS

Experimental0%

Alpha68%

Beta79%

[Opentelemetry](</pt-BR/gateway/opentelemetry>), [Prometheus](</pt-BR/gateway/prometheus>), [Diagnósticos](</pt-BR/gateway/diagnostics>), [Protocolo](</pt-BR/gateway/protocol>)

Aplicativo Web do Gateway - M3 Beta - 6 áreas

A interface Web está documentada com fluxos de pareamento, chat, PWA, Talk, push e Gateway remoto. Promova após os scorecards entre navegadores e de PWA móvel.

Cobertura Experimental - 4%Qualidade Beta - 74%Completude Beta - 79%Nenhum

Conversa em Tempo Real no Navegador 5 capacidades

Experimental0%

Alfa68%

Beta79%

[IU de Controle](</pt-BR/web/control-ui>), [Protocolo](</pt-BR/gateway/protocol>), [Conversa](</pt-BR/nodes/talk>)

Acesso e Confiança no Navegador 5 capacidades

Experimental0%

Alfa68%

Beta79%

[IU de Controle](</pt-BR/web/control-ui>), [Painel](</pt-BR/web/dashboard>), [Tailscale](</pt-BR/gateway/tailscale>), [Remoto](</pt-BR/gateway/remote>)

Configuração 5 capacidades

Experimental0%

Alfa68%

Beta79%

[IU de Controle](</pt-BR/web/control-ui>), [Configuração](</pt-BR/gateway/configuration>)

IU do Navegador 10 capacidades

Experimental8%

Beta79%

Beta79%

[IU de Controle](</pt-BR/web/control-ui>), [Índice](</pt-BR/web>), [Painel](</pt-BR/web/dashboard>), [Protocolo](</pt-BR/gateway/protocol>)

Conversas do WebChat 15 capacidades

Experimental10%

Beta79%

Beta79%

[IU de Controle](</pt-BR/web/control-ui>), [Webchat](</pt-BR/web/webchat>), [Primeiros passos](</pt-BR/start/getting-started>), [Roteamento de canais](</pt-BR/channels/channel-routing>), [Operações seguras de arquivos](</pt-BR/gateway/security/secure-file-operations>)

Console do Operador 10 capacidades

Experimental8%

Beta79%

Beta79%

[IU de Controle](</pt-BR/web/control-ui>), [Integridade](</pt-BR/gateway/health>), [Protocolo](</pt-BR/gateway/protocol>), [Painel](</pt-BR/web/dashboard>)

Plugins - M3 Beta - 9 áreas

Há documentação ampla e forte evidência interna de tempo de execução em manifestos, descoberta, carregamento, arquitetura de provedores/ferramentas e limites de aprovação. Mantenha a linha em beta até que a API pública do SDK/subcaminhos e a prova de distribuição externa sejam mais fortes.

Cobertura Experimental - 12%Qualidade Beta - 72%Completude Beta - 79%Parcial - 7

Criação e empacotamento de plugins 8 recursos / com suporte LTS

Experimental0%

Alfa68%

Beta79%

[Criação de plugins](</pt-BR/plugins/building-plugins>), [Visão geral do SDK](</pt-BR/plugins/sdk-overview>), [Pontos de entrada do SDK](</pt-BR/plugins/sdk-entrypoints>), [Subcaminhos do SDK](</pt-BR/plugins/sdk-subpaths>), [Manifesto](</pt-BR/plugins/manifest>), [Referência](</pt-BR/plugins/reference>)

Plugins incluídos 5 recursos / com suporte LTS

Experimental0%

Alfa68%

Beta79%

[Inventário de plugins](</pt-BR/plugins/plugin-inventory>), [Plugins](</pt-BR/cli/plugins>), [Detalhes internos da arquitetura](</pt-BR/plugins/architecture-internals>)

Plugin Canvas 6 recursos

Experimental0%

Alfa68%

Beta79%

[Canvas](</pt-BR/plugins/reference/canvas>), [Canvas](</pt-BR/refactor/canvas>), [Referência de configuração](</pt-BR/gateway/configuration-reference>)

Instalação e execução de plugins 6 recursos / com suporte LTS

Experimental35%

Beta79%

Beta79%

[Arquitetura](</pt-BR/plugins/architecture>), [Detalhes internos da arquitetura](</pt-BR/plugins/architecture-internals>), [Plugins](</pt-BR/cli/plugins>)

Plugins de canal 5 recursos / com suporte LTS

Experimental0%

Alfa68%

Beta79%

[Plugins de canal do SDK](</pt-BR/plugins/sdk-channel-plugins>), [Entrada de canal do SDK](</pt-BR/plugins/sdk-channel-inbound>), [Saída de canal do SDK](</pt-BR/plugins/sdk-channel-outbound>)

Plugins de provedor e ferramenta 6 recursos / com suporte LTS

Experimental43%

Beta79%

Beta79%

[Plugins de provedor do SDK](</pt-BR/plugins/sdk-provider-plugins>), [Plugins de ferramenta](</pt-BR/plugins/tool-plugins>), [Adição de recursos](</pt-BR/plugins/adding-capabilities>)

Aprovações de Plugin 6 recursos / com suporte LTS

Experimental0%

Alfa68%

Beta79%

[Solicitações de permissão de Plugin](</pt-BR/plugins/plugin-permission-requests>), [Aprovações de execução](</pt-BR/tools/exec-approvals>), [Plugins de canal do SDK](</pt-BR/plugins/sdk-channel-plugins>)

Publicação de plugins 6 recursos / com suporte LTS

Experimental0%

Alfa68%

Beta79%

[Plugins](</pt-BR/cli/plugins>), [Compatibilidade](</pt-BR/plugins/compatibility>), [Publicação](</pt-BR/clawhub/publishing>)

Testar plugins 6 capacidades

Experimental27%

Beta79%

Beta79%

[Testes de SDK](</pt-BR/plugins/sdk-testing>), [Configuração do SDK](</pt-BR/plugins/sdk-setup>), [Harness do Codex](</pt-BR/plugins/codex-harness>)

Segurança, autenticação, pareamento e segredos - M3 Beta - 6 áreas

Existem boa documentação e superfícies de hardening. Promova depois que execuções regulares de cenários de atualização/segurança comprovarem que não há regressões de configuração.

Cobertura Experimental - 16%Qualidade Beta - 72%Completude Beta - 79%Parcial - 5

Política de aprovação e salvaguardas de ferramentas 2 capacidades / compatível com LTS

Alpha50%

Beta79%

Beta79%

[Aprovações de execução](</pt-BR/tools/exec-approvals>), [Aprovações](</pt-BR/cli/approvals>), [Solicitações de permissão de Plugin](</pt-BR/plugins/plugin-permission-requests>), [Verificações de auditoria](</pt-BR/gateway/security/audit-checks>)

Autenticação do Gateway e acesso remoto 9 capacidades / compatível com LTS

Experimental0%

Alpha68%

Beta79%

[Índice](</pt-BR/gateway/security>), [Runbook de exposição](</pt-BR/gateway/security/exposure-runbook>), [Autenticação de proxy confiável](</pt-BR/gateway/trusted-proxy-auth>), [Tailscale](</pt-BR/gateway/tailscale>), [Remoto](</pt-BR/gateway/remote>), [Referência de configuração](</pt-BR/gateway/configuration-reference>), [Gateway](</pt-BR/cli/gateway>), [Doctor](</pt-BR/cli/doctor>), [Interface de controle](</pt-BR/web/control-ui>), [Controle do navegador](</pt-BR/tools/browser-control>), [Verificações de auditoria](</pt-BR/gateway/security/audit-checks>)

Controle de acesso de canais 3 capacidades / compatível com LTS

Experimental0%

Alpha68%

Beta79%

[Pareamento](</pt-BR/channels/pairing>), [Telegram](</pt-BR/channels/telegram>), [Grupos de acesso](</pt-BR/channels/access-groups>), [Verificações de auditoria](</pt-BR/gateway/security/audit-checks>)

Pareamento de dispositivo e Node 11 capacidades / compatível com LTS

Experimental0%

Alpha68%

Beta79%

[Protocolo](</pt-BR/gateway/protocol>), [Dispositivos](</pt-BR/cli/devices>), [Pareamento](</pt-BR/channels/pairing>), [Pareamento](</pt-BR/gateway/pairing>), [Escopos de operador](</pt-BR/gateway/operator-scopes>), [Interface de controle](</pt-BR/web/control-ui>), [Webchat](</pt-BR/web/webchat>), [Aprovações](</pt-BR/cli/approvals>)

Confiança de Plugin 2 capacidades

Experimental0%

Alpha68%

Beta79%

[Manifesto](</pt-BR/plugins/manifest>), [Solicitações de permissão de Plugin](</pt-BR/plugins/plugin-permission-requests>), [Gerenciar Plugins](</pt-BR/plugins/manage-plugins>), [Verificações de auditoria](</pt-BR/gateway/security/audit-checks>)

Higiene de credenciais e segredos 5 capacidades / compatível com LTS

Experimental46%

Beta79%

Beta79%

[Autenticação](</pt-BR/gateway/authentication>), [Modelos](</pt-BR/cli/models>), [Openai](</pt-BR/providers/openai>), [Oauth](</pt-BR/concepts/oauth>), [Segredos](</pt-BR/gateway/secrets>), [Segredos](</pt-BR/cli/secrets>), [Superfície de credenciais Secretref](</pt-BR/reference/secretref-credential-surface>), [Verificações de auditoria](</pt-BR/gateway/security/audit-checks>)

Automação: cron, hooks, tarefas, polling - M3 Beta - 6 áreas

Documentado e utilizável, mas a comprovação por cenários deve cobrir entrega sem supervisão, novas tentativas e visibilidade de falhas.

Cobertura Experimental - 2%Qualidade Beta - 72%Completude Beta - 79%Nenhuma

Tarefas Cron 15 capacidades

Experimental0%

Beta79%

Beta79%

[Tarefas Cron](</pt-BR/automation/cron-jobs>), [Cron](</pt-BR/cli/cron>), [Protocolo](</pt-BR/gateway/protocol>), [Tarefas](</pt-BR/automation/tasks>), [Discord](</pt-BR/channels/discord>)

Entrada de eventos 15 capacidades

Experimental0%

Alfa68%

Beta79%

[Telegram](</pt-BR/channels/telegram>), [Zalo](</pt-BR/channels/zalo>), [Solução de problemas](</pt-BR/channels/troubleshooting>), [iMessage a partir do BlueBubbles](</pt-BR/channels/imessage-from-bluebubbles>), [Integração Gmail Pub/Sub](</pt-BR/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pub/Sub](</pt-BR/automation/cron-jobs>), [Webhooks](</pt-BR/cli/webhooks>), [Webhooks](</pt-BR/automation/cron-jobs#webhooks>), [Webhook](</pt-BR/automation/cron-jobs>)

Hooks de automação 11 capacidades

Experimental0%

Alfa68%

Beta79%

[Hooks](</pt-BR/automation/hooks>), [Hooks](</pt-BR/cli/hooks>), [Hooks](</pt-BR/plugins/hooks>), [Solicitações de permissão de Plugin](</pt-BR/plugins/plugin-permission-requests>), [Subcaminhos do SDK](</pt-BR/plugins/sdk-subpaths>)

Tarefas e fluxos em segundo plano 10 capacidades

Experimental0%

Alfa68%

Beta79%

[Tarefas](</pt-BR/automation/tasks>), [Índice](</pt-BR/automation>), [Tarefas](</pt-BR/cli/tasks>), [TaskFlow](</pt-BR/automation/taskflow>), [Runtime do SDK](</pt-BR/plugins/sdk-runtime>)

Heartbeat 5 capacidades

Experimental14%

Beta79%

Beta79%

[Índice](</pt-BR/automation>), [Heartbeat](</pt-BR/gateway/heartbeat>), [Compromissos](</pt-BR/concepts/commitments>)

Controles de sondagem 10 capacidades

Experimental0%

Alfa68%

Beta79%

[Sondagem](</pt-BR/cli/message>), [Mensagem](</pt-BR/cli/message>), [Telegram](</pt-BR/channels/telegram>), [Msteams](</pt-BR/channels/msteams>), [Processo em segundo plano](</pt-BR/gateway/background-process>)

Compreensão de mídia e geração de mídia - M2 Alfa - 6 áreas

Uma ampla superfície de capacidades existe, mas a variação entre provedores, os limites de arquivos e a paridade entre Node/aplicativo fazem com que isso ainda não seja estável.

Cobertura Experimental - 2%Qualidade Alfa - 64%Completude Alfa - 68%Nenhum

Ingestão e acesso de mídia 8 recursos

Experimental0%

Alpha61%

Alpha68%

[Visão geral de mídia](</pt-BR/tools/media-overview>), [Compreensão de mídia](</pt-BR/nodes/media-understanding>), [Operações de arquivo seguras](</pt-BR/gateway/security/secure-file-operations>), [Pdf](</pt-BR/tools/pdf>), [Geração de imagens](</pt-BR/tools/image-generation>), [Qr](</pt-BR/cli/qr>), [LINE](</pt-BR/channels/line>), [WhatsApp](</pt-BR/channels/whatsapp>)

Manipulação de mídia de canais 5 recursos

Experimental0%

Alpha61%

Alpha68%

[Imagens](</pt-BR/nodes/images>), [Visão geral de mídia](</pt-BR/tools/media-overview>), [Discord](</pt-BR/channels/discord>)

Configuração de mídia 1 recurso

Experimental0%

Alpha61%

Alpha68%

[Visão geral de mídia](</pt-BR/tools/media-overview>), [Geração de imagens](</pt-BR/tools/image-generation>), [Manifesto](</pt-BR/plugins/manifest>), [Harness do Codex](</pt-BR/plugins/codex-harness>)

Entrega de conversão de texto em fala 2 recursos

Experimental0%

Alpha61%

Alpha68%

[Tts](</pt-BR/tools/tts>), [Visão geral de mídia](</pt-BR/tools/media-overview>), [Discord](</pt-BR/channels/discord>)

Compreensão de mídia 12 recursos

Experimental7%

Alpha69%

Alpha69%

[Áudio](</pt-BR/nodes/audio>), [Compreensão de mídia](</pt-BR/nodes/media-understanding>), [Visão geral de mídia](</pt-BR/tools/media-overview>), [WhatsApp](</pt-BR/channels/whatsapp>), [Imagens](</pt-BR/nodes/images>), [Inferir](</pt-BR/cli/infer>), [Pdf](</pt-BR/tools/pdf>)

Geração de mídia 17 recursos

Experimental5%

Alpha69%

Alpha69%

[Geração de imagens](</pt-BR/tools/image-generation>), [Visão geral de mídia](</pt-BR/tools/media-overview>), [Skills](</pt-BR/tools/skills>), [Geração de música](</pt-BR/tools/music-generation>), [Geração de vídeo](</pt-BR/tools/video-generation>)

Voz e conversa em tempo real - M2 Alpha - 6 áreas

Existem várias implementações no Control UI, em apps e em provedores. Precisa de scorecards de latência, modos de falha e configuração antes do beta.

Cobertura Experimental - 0%Qualidade Alpha - 61%Completude Alpha - 68%Nenhum

Provedores de Conversa 7 capacidades

Experimental0%

Alpha61%

Alpha68%

[Openai](</pt-BR/providers/openai>), [Google](</pt-BR/providers/google>), [Plugins de Provedor do SDK](</pt-BR/plugins/sdk-provider-plugins>), [Conversa](</pt-BR/nodes/talk>), [IU de Controle](</pt-BR/web/control-ui>)

Sessões de Conversa em Tempo Real 11 capacidades

Experimental0%

Alpha61%

Alpha68%

[Conversa](</pt-BR/nodes/talk>), [IU de Controle](</pt-BR/web/control-ui>)

Fala e Transcrição 5 capacidades

Experimental0%

Alpha61%

Alpha68%

[Conversa](</pt-BR/nodes/talk>), [Openai](</pt-BR/providers/openai>), [Google](</pt-BR/providers/google>)

Conversa em App Nativo 4 capacidades

Experimental0%

Alpha61%

Alpha68%

[Conversa](</pt-BR/nodes/talk>), [Voicewake](</pt-BR/platforms/mac/voicewake>)

Ativação por Voz e Roteamento 4 capacidades

Experimental0%

Alpha61%

Alpha68%

[Voicewake](</pt-BR/nodes/voicewake>), [Voicewake](</pt-BR/platforms/mac/voicewake>), [Sobreposição de Voz](</pt-BR/platforms/mac/voice-overlay>)

Observabilidade de Conversa 5 capacidades

Experimental0%

Alpha61%

Alpha68%

[IU de Controle](</pt-BR/web/control-ui>), [Sobreposição de Voz](</pt-BR/platforms/mac/voice-overlay>), [Conversa](</pt-BR/nodes/talk>)

TUI - M2 Alpha - 5 áreas

Presente na documentação e no código-fonte, mas menos visível como fluxo de trabalho principal do usuário. Precisa de definição explícita de cenário.

Cobertura Experimental - 0%Qualidade Alpha - 59%Completude Alpha - 66%Nenhum

Modos de Runtime 14 capacidades

Experimental0%

Alpha59%

Alpha66%

[Tui](</pt-BR/cli/tui>), [Tui](</pt-BR/web/tui>), [Índice](</pt-BR/cli>)

Entrada e Comandos 8 capacidades

Experimental0%

Alpha59%

Alpha66%

[Tui](</pt-BR/web/tui>)

Gerenciamento de Sessões 3 capacidades

Experimental0%

Alpha59%

Alpha66%

[Tui](</pt-BR/web/tui>), [Sessões](</pt-BR/cli/sessions>)

Execução de Shell Local 4 capacidades

Experimental0%

Alpha59%

Alpha66%

[Tui](</pt-BR/web/tui>), [Tui](</pt-BR/cli/tui>)

Segurança de Renderização e Saída 4 capacidades

Experimental0%

Alpha59%

Alpha66%

[Tui](</pt-BR/web/tui>), [Qr](</pt-BR/cli/qr>), [Logs](</pt-BR/cli/logs>), [Conclusão](</pt-BR/cli/completion>)

ClawHub - M2 Alpha - 4 áreas

A documentação pública e o conceito de ecossistema existem. Precisa de scorecards de instalação, confiança, atualização, rollback e compatibilidade.

Cobertura Experimental - 0%Qualidade Alpha - 58%Completude Alpha - 62%Nenhum

Publicação 7 capacidades

Experimental0%

Alpha54%

Alpha55%

[Publicação](</pt-BR/clawhub/publishing>), [Criando Skills](</pt-BR/tools/creating-skills>), [Comunidade](</pt-BR/plugins/community>)

Descoberta de Catálogo 5 capacidades

Experimental0%

Alpha61%

Alpha68%

[Plugin](</pt-BR/tools/plugin>), [Plugins](</pt-BR/cli/plugins>), [Skills](</pt-BR/cli/skills>), [Skills](</pt-BR/tools/skills>), [Comunidade](</pt-BR/plugins/community>)

Compatibilidade e Confiança 12 capacidades

Experimental0%

Alpha55%

Alpha56%

[Plugin](</pt-BR/tools/plugin>), [Plugins](</pt-BR/cli/plugins>), [Compatibilidade](</pt-BR/plugins/compatibility>), [Inventário de Plugins](</pt-BR/plugins/plugin-inventory>), [Publicação](</pt-BR/clawhub/publishing>), [Skills](</pt-BR/tools/skills>), [Configuração de Skills](</pt-BR/tools/skills-config>)

Ciclo de Vida e Integridade de Plugins 26 capacidades

Experimental0%

Alpha61%

Alpha68%

[Plugin](</pt-BR/tools/plugin>), [Plugins](</pt-BR/cli/plugins>), [Skills](</pt-BR/cli/skills>), [Skills](</pt-BR/tools/skills>), [Protocolo](</pt-BR/gateway/protocol>), [Pacotes](</pt-BR/plugins/bundles>), [Resolução de Dependências](</pt-BR/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 áreas

O OpenClaw App SDK é um contrato de app externo distinto, separado do runtime do Gateway e do Plugin SDK. A pontuação atual mostra um caminho real de `@openclaw/sdk` com lacunas em empacotamento público, descoberta automática, aprovações, helpers e compatibilidade.

Cobertura Experimental - 3%Qualidade Alpha - 54%Completude Alpha - 53%Nenhum

API de cliente 4 capacidades

Experimental0%

Alpha51%

Alpha50%

[Openclaw Sdk](</pt-BR/gateway/external-apps>), [Design de API do Openclaw Sdk](</pt-BR/gateway/external-apps>)

Acesso ao Gateway 5 capacidades

Experimental0%

Alpha53%

Alpha54%

[Openclaw Sdk](</pt-BR/gateway/external-apps>), [Design de API do Openclaw Sdk](</pt-BR/gateway/external-apps>), [Protocolo](</pt-BR/gateway/protocol>), [Índice](</pt-BR/gateway/security>)

Conversas de agentes 6 capacidades

Experimental0%

Alpha52%

Alpha52%

[Openclaw Sdk](</pt-BR/gateway/external-apps>), [Design de API do Openclaw Sdk](</pt-BR/gateway/external-apps>), [Protocolo](</pt-BR/gateway/protocol>)

Eventos e aprovações 5 capacidades

Experimental0%

Alpha52%

Alpha52%

[Openclaw Sdk](</pt-BR/gateway/external-apps>), [Design de API do Openclaw Sdk](</pt-BR/gateway/external-apps>), [Protocolo](</pt-BR/gateway/protocol>)

Auxiliares de recursos 5 capacidades

Experimental17%

Alpha62%

Alpha53%

[Openclaw Sdk](</pt-BR/gateway/external-apps>), [Design de API do Openclaw Sdk](</pt-BR/gateway/external-apps>)

Compatibilidade 5 capacidades

Experimental0%

Alpha54%

Alpha55%

[Design de API do Openclaw Sdk](</pt-BR/gateway/external-apps>), [Typebox](</pt-BR/concepts/typebox>), [Protocolo](</pt-BR/gateway/protocol>)

### Plataforma

Host de Gateway Linux - M4 Stable - 5 áreas

O runtime Node é recomendado, o serviço de usuário systemd está documentado, e a orientação para VPS/contêiner é ampla.

Cobertura Experimental - 0%Qualidade Beta - 75%Completude Stable - 89%Parcial - 4

Configuração do host e atualizações 4 capacidades / com suporte a LTS

Experimental0%

Beta75%

Estável89%

[Índice](</pt-BR/install>), [Atualização](</pt-BR/install/updating>), [Linux](</pt-BR/platforms/linux>), [Índice](</pt-BR/platforms>)

Ambiente de execução do Gateway e controle de serviço 6 capacidades / com suporte a LTS

Experimental0%

Beta75%

Estável89%

[Índice](</pt-BR/gateway>), [Gateway](</pt-BR/cli/gateway>), [Linux](</pt-BR/platforms/linux>), [VPS](</pt-BR/vps>)

Acesso remoto e segurança 6 capacidades / com suporte a LTS

Experimental0%

Beta75%

Estável89%

[Remoto](</pt-BR/gateway/remote>), [Tailscale](</pt-BR/gateway/tailscale>), [Runbook de exposição](</pt-BR/gateway/security/exposure-runbook>), [Autenticação](</pt-BR/gateway/authentication>), [Segredos](</pt-BR/gateway/secrets>)

Diagnóstico e reparo 4 capacidades / com suporte a LTS

Experimental0%

Beta75%

Estável89%

[Status](</pt-BR/cli/status>), [Logs](</pt-BR/cli/logs>), [Doctor](</pt-BR/cli/doctor>), [Diagnóstico](</pt-BR/gateway/diagnostics>), [Índice](</pt-BR/gateway>)

Destinos de implantação 3 capacidades

Experimental0%

Beta75%

Estável89%

[VPS](</pt-BR/vps>), [Docker](</pt-BR/install/docker>), [Hetzner](</pt-BR/install/hetzner>), [Digitalocean](</pt-BR/install/digitalocean>), [Kubernetes](</pt-BR/install/kubernetes>), [Podman](</pt-BR/install/podman>)

host do Gateway macOS - M4 Estável - 7 áreas

O caminho de serviço LaunchAgent, os modos de Gateway local/remoto, a instalação da CLI e a integração com o aplicativo estão documentados.

Cobertura Experimental - 0%Qualidade Beta - 74%Completude Estável - 88%Nenhum

Configuração da CLI 4 capacidades

Experimental0%

Beta74%

Estável88%

[Macos](</pt-BR/platforms/macos>), [Gateway incluído](</pt-BR/platforms/mac/bundled-gateway>), [Instalador](</pt-BR/install/installer>), [Node](</pt-BR/install/node>)

Integração do Gateway local 9 capacidades

Experimental0%

Beta74%

Estável88%

[Macos](</pt-BR/platforms/macos>), [Gateway incluído](</pt-BR/platforms/mac/bundled-gateway>), [Remoto](</pt-BR/platforms/mac/remote>), [Índice](</pt-BR/gateway>), [Gateway](</pt-BR/cli/gateway>), [Bonjour](</pt-BR/gateway/bonjour>)

Modo de Gateway remoto 5 capacidades

Experimental0%

Beta74%

Estável88%

[Remoto](</pt-BR/platforms/mac/remote>), [Remoto](</pt-BR/gateway/remote>), [Tailscale](</pt-BR/gateway/tailscale>)

Ciclo de vida do serviço Gateway 10 capacidades

Experimental0%

Beta74%

Estável88%

[Macos](</pt-BR/platforms/macos>), [Gateway incluído](</pt-BR/platforms/mac/bundled-gateway>), [Gateway](</pt-BR/cli/gateway>), [Índice](</pt-BR/gateway>), [Atualização](</pt-BR/cli/update>), [Atualização](</pt-BR/install/updating>), [Desinstalação](</pt-BR/install/uninstall>), [Solução de problemas](</pt-BR/gateway/troubleshooting>)

Diagnóstico e observabilidade 4 capacidades

Experimental0%

Beta74%

Estável88%

[Gateway incluído](</pt-BR/platforms/mac/bundled-gateway>), [Macos](</pt-BR/platforms/macos>), [Gateway](</pt-BR/cli/gateway>), [Diagnóstico](</pt-BR/gateway/doctor>), [Solução de problemas](</pt-BR/gateway/troubleshooting>)

Permissões e capacidades nativas 4 capacidades

Experimental0%

Beta74%

Estável88%

[Macos](</pt-BR/platforms/macos>), [Remoto](</pt-BR/platforms/mac/remote>)

Perfis e isolamento 5 capacidades

Experimental0%

Beta74%

Estável88%

[Vários Gateways](</pt-BR/gateway/multiple-gateways>), [Índice](</pt-BR/gateway>), [Gateway](</pt-BR/cli/gateway>)

Hospedagem com Docker e Podman - M3 Beta - 4 áreas

A documentação de instalação existe e cobre caminhos comuns de implantação. Promova depois que smokes recorrentes de lançamento capturarem o comportamento de atualização e volume.

Cobertura Experimental - 7%Qualidade Beta - 71%Completude Beta - 79%Nenhum

Configuração de contêineres 6 capacidades

Experimental0%

Alfa68%

Beta79%

[Docker](</pt-BR/install/docker>), [Podman](</pt-BR/install/podman>)

Operações de contêineres 11 capacidades

Experimental0%

Alfa68%

Beta79%

[Podman](</pt-BR/install/podman>), [Docker Vm Runtime](</pt-BR/install/docker-vm-runtime>), [Docker](</pt-BR/install/docker>), [Hetzner](</pt-BR/install/hetzner>), [Hostinger](</pt-BR/install/hostinger>)

Lançamento e validação de imagens 5 capacidades

Experimental29%

Beta79%

Beta79%

[Docker](</pt-BR/install/docker>), [Docker Vm Runtime](</pt-BR/install/docker-vm-runtime>), [Validação completa da versão](</pt-BR/reference/full-release-validation>)

Sandbox e ferramentas de agente 3 capacidades

Experimental0%

Alfa68%

Beta79%

[Docker](</pt-BR/install/docker>), [Docker Vm Runtime](</pt-BR/install/docker-vm-runtime>)

Windows via WSL2 - M3 Beta - 6 areas

Caminho recomendado para Windows com orientação de systemd/serviço de usuário e documentação da cadeia de inicialização. Promova após avaliações repetidas de instalação/atualização.

Cobertura Experimental - 6%Qualidade Alfa - 69%Integralidade Beta - 79%Parcial - 5

Configuração do WSL 6 recursos / com suporte LTS

Experimental0%

Alfa67%

Beta79%

[Windows](</pt-BR/platforms/windows>), [Primeiros passos](</pt-BR/start/getting-started>)

CLI 8 recursos / com suporte LTS

Experimental0%

Alfa67%

Beta79%

[Windows](</pt-BR/platforms/windows>), [Primeiros passos](</pt-BR/start/getting-started>), [Atualização](</pt-BR/install/updating>), [Integração inicial](</pt-BR/cli/onboard>), [Doctor](</pt-BR/cli/doctor>), [Status](</pt-BR/cli/status>), [Logs](</pt-BR/cli/logs>)

Ciclo de vida do serviço Gateway 10 recursos / com suporte LTS

Experimental0%

Alfa67%

Beta79%

[Windows](</pt-BR/platforms/windows>), [Índice](</pt-BR/gateway>), [Doctor](</pt-BR/gateway/doctor>)

Acesso e exposição do Gateway 11 recursos / com suporte LTS

Experimental0%

Alfa67%

Beta79%

[Autenticação](</pt-BR/gateway/authentication>), [Segredos](</pt-BR/gateway/secrets>), [Remoto](</pt-BR/gateway/remote>), [Runbook de exposição](</pt-BR/gateway/security/exposure-runbook>), [Windows](</pt-BR/platforms/windows>)

Diagnóstico e reparo 6 recursos / com suporte LTS

Experimental38%

Beta79%

Beta79%

[Windows](</pt-BR/platforms/windows>), [Status](</pt-BR/cli/status>), [Logs](</pt-BR/cli/logs>), [Doctor](</pt-BR/cli/doctor>), [Doctor](</pt-BR/gateway/doctor>)

Navegador e interface de controle 6 recursos

Experimental0%

Alfa67%

Beta79%

[Solução de problemas de CDP remoto do navegador no WSL2 Windows](</pt-BR/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Navegador](</pt-BR/tools/browser>), [Interface de controle](</pt-BR/web/control-ui>)

Raspberry Pi and small Linux devices - M3 Beta - 4 areas

A documentação da plataforma existe e o caminho do Gateway é baseado em Linux. Precisa de prova de smoke de release específica para hardware para avançar mais.

Cobertura Experimental - 0%Qualidade Alfa - 67%Completude Beta - 79%Nenhum

Configuração e compatibilidade 12 recursos

Experimental0%

Alpha67%

Beta79%

[Raspberry Pi](</pt-BR/install/raspberry-pi>), [Índice](</pt-BR/install>), [FAQ da primeira execução](</pt-BR/help/faq-first-run>), [FAQ](</pt-BR/help/faq>), [Linux](</pt-BR/platforms/linux>), [Instalador](</pt-BR/install/installer>)

Acesso remoto e autenticação 9 recursos

Experimental0%

Alpha67%

Beta79%

[Raspberry Pi](</pt-BR/install/raspberry-pi>), [Autenticação](</pt-BR/gateway/authentication>), [Segredos](</pt-BR/gateway/secrets>), [Pareamento](</pt-BR/gateway/pairing>), [Dispositivos](</pt-BR/cli/devices>), [Remoto](</pt-BR/gateway/remote>), [Tailscale](</pt-BR/gateway/tailscale>)

Runtime do Gateway 10 recursos

Experimental0%

Alpha67%

Beta79%

[Índice](</pt-BR/gateway>), [Gateway](</pt-BR/cli/gateway>), [Raspberry Pi](</pt-BR/install/raspberry-pi>), [Linux](</pt-BR/platforms/linux>), [VPS](</pt-BR/vps>)

Desempenho e diagnósticos 5 recursos

Experimental0%

Alpha67%

Beta79%

[Raspberry Pi](</pt-BR/install/raspberry-pi>), [Linux](</pt-BR/platforms/linux>), [Saúde](</pt-BR/gateway/health>), [Diagnósticos](</pt-BR/gateway/diagnostics>)

Aplicativo complementar para macOS - M3 Beta - 8 áreas

O aplicativo avançado de barra de menus, permissões, modo Node, Canvas, ativação por voz, WebChat e modo remoto existem. Ainda muda rápido o suficiente para evitar Stable.

Cobertura Experimental - 0%Qualidade Alpha - 66%Completude Beta - 78%Nenhum

Tela 4 capacidades

Experimental0%

Alpha66%

Beta78%

[Tela](</pt-BR/platforms/mac/canvas>), [Macos](</pt-BR/platforms/macos>), [Webchat](</pt-BR/web/webchat>)

Configuração Local 7 capacidades

Experimental0%

Alpha66%

Beta78%

[Gateway Incluído](</pt-BR/platforms/mac/bundled-gateway>), [Macos](</pt-BR/platforms/macos>), [Processo Filho](</pt-BR/platforms/mac/child-process>), [Configuração de Desenvolvimento](</pt-BR/platforms/mac/dev-setup>)

Status e Configurações 5 capacidades

Experimental0%

Alpha66%

Beta78%

[Barra de Menu](</pt-BR/platforms/mac/menu-bar>), [Ícone](</pt-BR/platforms/mac/icon>), [Macos](</pt-BR/platforms/macos>), [Integridade](</pt-BR/platforms/mac/health>), [Logs](</pt-BR/platforms/mac/logging>), [Remoto](</pt-BR/platforms/mac/remote>)

Capacidades Nativas 5 capacidades

Experimental0%

Alpha66%

Beta78%

[Macos](</pt-BR/platforms/macos>), [Xpc](</pt-BR/platforms/mac/xpc>), [Permissões](</pt-BR/platforms/mac/permissions>), [Assinatura](</pt-BR/platforms/mac/signing>), [Peekaboo](</pt-BR/platforms/mac/peekaboo>)

Conexões Remotas 3 capacidades

Experimental0%

Alpha66%

Beta78%

[Remoto](</pt-BR/platforms/mac/remote>), [Macos](</pt-BR/platforms/macos>), [Remoto](</pt-BR/gateway/remote>)

Voz e Conversa 3 capacidades

Experimental0%

Alpha66%

Beta78%

[Voicewake](</pt-BR/platforms/mac/voicewake>), [Sobreposição de Voz](</pt-BR/platforms/mac/voice-overlay>), [Conversa](</pt-BR/nodes/talk>), [Macos](</pt-BR/platforms/macos>)

WebChat 3 capacidades

Experimental0%

Alpha66%

Beta78%

[Webchat](</pt-BR/platforms/mac/webchat>), [Macos](</pt-BR/platforms/macos>), [Webchat](</pt-BR/web/webchat>)

WebChat Remoto 5 capacidades

Experimental0%

Alpha66%

Beta78%

[Webchat](</pt-BR/platforms/mac/webchat>), [Remoto](</pt-BR/gateway/remote>), [Remoto](</pt-BR/platforms/mac/remote>)

Aplicativo Android - M2 Alpha - 7 áreas

O caminho público do Google Play existe, mas a documentação do aplicativo ainda descreve a reconstrução como extremamente alpha e destaca o trabalho de fortalecimento da versão.

Cobertura Experimental - 0%Qualidade Alpha - 59%Completude Alpha - 66%Nenhum

Captura de mídia 1 recursos

Experimental0%

Alpha59%

Alpha66%

[Android](</pt-BR/platforms/android>), [Câmera](</pt-BR/nodes/camera>)

Chat móvel 1 recursos

Experimental0%

Alpha59%

Alpha66%

[Android](</pt-BR/platforms/android>)

Configuração de conexão 1 recursos

Experimental0%

Alpha59%

Alpha66%

[Android](</pt-BR/platforms/android>), [Bonjour](</pt-BR/gateway/bonjour>), [Pareamento](</pt-BR/gateway/pairing>)

Distribuição 3 recursos

Experimental0%

Alpha59%

Alpha66%

[Android](</pt-BR/platforms/android>)

Configurações 1 recursos

Experimental0%

Alpha59%

Alpha66%

[Android](</pt-BR/platforms/android>)

Voz 1 recursos

Experimental0%

Alpha59%

Alpha66%

[Android](</pt-BR/platforms/android>), [Falar](</pt-BR/nodes/talk>)

Runtime do dispositivo 2 recursos

Experimental0%

Alpha59%

Alpha66%

[Android](</pt-BR/platforms/android>), [Solução de problemas](</pt-BR/nodes/troubleshooting>), [Protocolo](</pt-BR/gateway/protocol>)

Windows nativo - M2 Alpha - 4 áreas

Os fluxos principais de CLI/Gateway funcionam, mas a documentação ainda recomenda WSL2 para a experiência completa e lista ressalvas nativas.

Cobertura Experimental - 0%Qualidade Alpha - 58%Completude Alpha - 66%Parcial - 1

CLI 9 capacidades / com suporte LTS

Experimental0%

Alfa54%

Alfa64%

[Índice](</pt-BR/install>), [Instalador](</pt-BR/install/installer>), [Windows](</pt-BR/platforms/windows>), [Primeiros passos](</pt-BR/start/getting-started>), [Onboard](</pt-BR/cli/onboard>)

Gerenciamento do Gateway 11 capacidades

Experimental0%

Alfa59%

Alfa66%

[Windows](</pt-BR/platforms/windows>), [Índice](</pt-BR/gateway>), [Gateway](</pt-BR/cli/gateway>), [Doctor](</pt-BR/cli/doctor>)

Rede 4 capacidades

Experimental0%

Alfa59%

Alfa66%

[Windows](</pt-BR/platforms/windows>), [Índice](</pt-BR/gateway>), [Gateway](</pt-BR/cli/gateway>)

Atualizações 4 capacidades

Experimental0%

Alfa59%

Alfa66%

[Atualização](</pt-BR/install/updating>), [Ci](</pt-BR/ci>)

Hospedagem Kubernetes - M2 Alfa - 4 áreas

A hospedagem Kubernetes é um caminho distinto de implantação em cluster baseado em Kustomize. A pontuação atual mostra um caminho real de implantação mínima com lacunas em CI específico para Kubernetes, empacotamento de ingress/TLS/NetworkPolicy, backup/restauração e fortalecimento da exposição em produção.

Cobertura Experimental - 0%Qualidade Alpha - 55%Completude Alpha - 61%Nenhum

Configuração de Implantação 5 recursos

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</pt-BR/install/kubernetes>), [Índice](</pt-BR/install>)

Configuração e Segredos 5 recursos

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</pt-BR/install/kubernetes>), [Segredos](</pt-BR/gateway/secrets>), [Ambiente](</pt-BR/help/environment>)

Acesso e Exposição 5 recursos

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</pt-BR/install/kubernetes>), [Autenticação](</pt-BR/gateway/authentication>), [Remoto](</pt-BR/gateway/remote>), [Runbook de Exposição](</pt-BR/gateway/security/exposure-runbook>)

Ciclo de Vida do Cluster 5 recursos

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</pt-BR/install/kubernetes>), [Índice](</pt-BR/gateway>)

app iOS - M1 Experimental - 8 áreas

Prévia interna / super-alpha. Existem fluxos de push via TestFlight e relay, mas ainda não há distribuição pública.

Cobertura Experimental - 0%Qualidade Experimental - 41%Completude Experimental - 44%Nenhum

Mídia e compartilhamento 1 capacidade

Experimental0%

Experimental41%

Experimental44%

[Ios](</pt-BR/platforms/ios>), [Câmera](</pt-BR/nodes/camera>)

Canvas e tela 1 capacidade

Experimental0%

Experimental41%

Experimental44%

[Ios](</pt-BR/platforms/ios>), [Canvas](</pt-BR/plugins/reference/canvas>)

Chat e sessões 1 capacidade

Experimental0%

Experimental41%

Experimental44%

[Ios](</pt-BR/platforms/ios>), [Webchat](</pt-BR/web/webchat>), [Protocolo](</pt-BR/gateway/protocol>)

Configuração e diagnósticos do Gateway 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[Ios](</pt-BR/platforms/ios>), [Pareamento](</pt-BR/channels/pairing>)

Distribuição 1 capacidade

Experimental0%

Experimental41%

Experimental44%

[Ios](</pt-BR/platforms/ios>)

Comandos do dispositivo 2 capacidades

Experimental0%

Experimental41%

Experimental44%

[Ios](</pt-BR/platforms/ios>), [Protocolo](</pt-BR/gateway/protocol>)

Notificações e segundo plano 1 capacidade

Experimental0%

Experimental41%

Experimental44%

[Ios](</pt-BR/platforms/ios>), [Configuração](</pt-BR/gateway/configuration>)

Voz 1 capacidade

Experimental0%

Experimental41%

Experimental44%

[Ios](</pt-BR/platforms/ios>), [Fala](</pt-BR/nodes/talk>)

Caminho de instalação do Nix - M1 Experimental - 5 áreas

Fluxo de instalação opcional. Precisa de uma promessa de suporte mais clara antes da promoção para alfa/beta.

Cobertura Experimental - 0%Qualidade Experimental - 41%Completude Experimental - 44%Nenhum

Transferência da instalação 4 capacidades

Experimental0%

Experimental41%

Experimental44%

[Nix](</pt-BR/install/nix>), [Índice](</pt-BR/install>), [Diretório de documentação](</pt-BR/start/docs-directory>)

Ciclo de vida do Plugin 4 capacidades

Experimental0%

Experimental41%

Experimental44%

[Gerenciar Plugins](</pt-BR/plugins/manage-plugins>), [Plugin](</pt-BR/tools/plugin>), [Nix](</pt-BR/install/nix>)

Ativação e UX do app 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[Nix](</pt-BR/install/nix>)

Configuração e estado 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[Nix](</pt-BR/install/nix>), [Configuração](</pt-BR/cli/setup>), [Ambiente](</pt-BR/help/environment>)

Runtime de serviço e proteções 8 capacidades

Experimental0%

Experimental41%

Experimental44%

[Nix](</pt-BR/install/nix>), [Configuração](</pt-BR/cli/setup>), [Doctor](</pt-BR/cli/doctor>), [Atualização](</pt-BR/cli/update>)

superfícies complementares do watchOS - M1 Experimental - 5 áreas

A fonte tem superfícies de app/extensão Watch; a documentação pública ainda não apresenta isso como um recurso de usuário.

Cobertura Experimental - 0%Qualidade Experimental - 41%Completude Experimental - 44%Nenhum

Entrega e recuperação 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[iOS](</pt-BR/platforms/ios>)

Aprovações de execução 3 capacidades

Experimental0%

Experimental41%

Experimental44%

[Aprovações de execução](</pt-BR/tools/exec-approvals>), [iOS](</pt-BR/platforms/ios>)

Distribuição e suporte 6 capacidades

Experimental0%

Experimental41%

Experimental44%

[iOS](</pt-BR/platforms/ios>)

Notificações e respostas 7 capacidades

Experimental0%

Experimental41%

Experimental44%

[iOS](</pt-BR/platforms/ios>)

UI do app para Watch 3 capacidades

Experimental0%

Experimental41%

Experimental44%

[iOS](</pt-BR/platforms/ios>)

App complementar para Linux - M0 planejado - 5 áreas

A documentação informa que apps complementares nativos para Linux estão planejados; Gateway é o caminho Linux compatível hoje.

Cobertura Experimental - 0%Qualidade Experimental - 19%Completude Experimental - 21%Nenhum

Distribuição do aplicativo 3 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</pt-BR/platforms/linux>), [Índice](</pt-BR/platforms>), [Índice](</pt-BR/install>)

Conectividade do Gateway 4 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</pt-BR/platforms/linux>), [Índice](</pt-BR/gateway>), [Pareamento](</pt-BR/gateway/pairing>), [Remoto](</pt-BR/gateway/remote>)

Chat e sessões 3 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</pt-BR/platforms/linux>), [Protocolo](</pt-BR/gateway/protocol>), [Webchat](</pt-BR/web/webchat>)

Capacidades de desktop 9 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</pt-BR/platforms/linux>), [Aprovações de exec](</pt-BR/tools/exec-approvals>), [Segredos](</pt-BR/gateway/secrets>), [Índice](</pt-BR/nodes>), [Exec](</pt-BR/tools/exec>), [Falar](</pt-BR/nodes/talk>), [Câmera](</pt-BR/nodes/camera>)

Status e diagnósticos 7 capacidades

Experimental0%

Experimental19%

Experimental21%

[Linux](</pt-BR/platforms/linux>), [OpenClaw](</pt-BR/start/openclaw>), [Doctor](</pt-BR/gateway/doctor>)

Aplicativo complementar nativo para Windows - M0 planejado - 5 áreas

Apenas planejado.

Cobertura experimental - 0%Qualidade experimental - 19%Completude experimental - 21%Nenhum

Instalação e Atualizações 4 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</pt-BR/platforms/windows>), [Índice](</pt-BR/install>)

Conexão do Gateway 3 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</pt-BR/platforms/windows>), [Índice](</pt-BR/gateway>), [Pareamento](</pt-BR/gateway/pairing>), [Remoto](</pt-BR/gateway/remote>)

Sessões de Chat 2 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</pt-BR/platforms/windows>), [Protocolo](</pt-BR/gateway/protocol>)

Status e Reparo 5 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</pt-BR/platforms/windows>), [Diagnóstico](</pt-BR/gateway/doctor>), [Índice](</pt-BR/gateway>)

Ferramentas e Permissões de Desktop 10 capacidades

Experimental0%

Experimental19%

Experimental21%

[Windows](</pt-BR/platforms/windows>), [Índice](</pt-BR/nodes>), [Exec](</pt-BR/tools/exec>), [Aprovações do Exec](</pt-BR/tools/exec-approvals>), [Índice](</pt-BR/gateway/security>)

### Canal

Discord - M4 Estável - 6 áreas

Documentação profunda e ampla cobertura de recursos. Caminhos de voz/delegação devem continuar pontuados separadamente como beta/alfa.

Cobertura Experimental - 0%Qualidade Beta - 73%Completude Estável - 87%Parcial - 4

Configuração e operações de canais 10 capacidades / com suporte LTS

Experimental0%

Beta73%

Estável87%

[Discord](</pt-BR/channels/discord>), [Discord](</pt-BR/plugins/reference/discord>), [Fly](</pt-BR/install/fly>), [Comandos de barra](</pt-BR/tools/slash-commands>), [Saúde](</pt-BR/gateway/health>), [Canais](</pt-BR/cli/channels>), [Canais de configuração](</pt-BR/gateway/config-channels>)

Acesso e identidade 6 capacidades / com suporte LTS

Experimental0%

Beta73%

Estável87%

[Discord](</pt-BR/channels/discord>), [Emparelhamento](</pt-BR/channels/pairing>), [Grupos de acesso](</pt-BR/channels/access-groups>), [Grupos](</pt-BR/channels/groups>)

Roteamento e entrega de conversas 12 capacidades / com suporte LTS

Experimental0%

Beta73%

Estável87%

[Discord](</pt-BR/channels/discord>), [Roteamento de canais](</pt-BR/channels/channel-routing>), [Grupos](</pt-BR/channels/groups>), [Grupos de acesso](</pt-BR/channels/access-groups>), [Agentes ACP](</pt-BR/tools/acp-agents>), [Subagentes](</pt-BR/tools/subagents>)

Mídia e conteúdo rico 1 capacidade / com suporte LTS

Experimental0%

Beta73%

Estável87%

[Discord](</pt-BR/channels/discord>)

Controles e aprovações nativos 5 capacidades

Experimental0%

Beta73%

Estável87%

[Discord](</pt-BR/channels/discord>), [Comandos de barra](</pt-BR/tools/slash-commands>)

Voz e chamadas em tempo real 5 capacidades

Experimental0%

Beta73%

Estável87%

[Discord](</pt-BR/channels/discord>), [OpenAI](</pt-BR/providers/openai>), [ElevenLabs](</pt-BR/providers/elevenlabs>), [Automação de QA E2E](</pt-BR/concepts/qa-e2e-automation>), [Canais de configuração](</pt-BR/gateway/config-channels>)

Telegram - M3 Beta - 5 áreas

O canal principal é maduro o suficiente para uso regular, mas a UX de alta variância e os casos extremos de mídia precisam de comprovação recorrente por cenários.

Cobertura Experimental - 0%Qualidade Alpha - 68%Completude Beta - 78%Completo - 5

Configuração e operações de canais 10 capacidades / com suporte LTS

Experimental0%

Alpha66%

Beta78%

[Telegram](</pt-BR/channels/telegram>), [Canais de configuração](</pt-BR/gateway/config-channels>), [Canais](</pt-BR/cli/channels>)

Acesso e identidade 10 capacidades / com suporte LTS

Experimental0%

Alpha66%

Beta78%

[Telegram](</pt-BR/channels/telegram>), [Pareamento](</pt-BR/channels/pairing>), [Grupos de acesso](</pt-BR/channels/access-groups>), [Grupos](</pt-BR/channels/groups>), [Multiagente](</pt-BR/concepts/multi-agent>)

Roteamento e entrega de conversas 1 capacidade / com suporte LTS

Experimental0%

Alpha66%

Beta78%

[Telegram](</pt-BR/channels/telegram>), [Grupos](</pt-BR/channels/groups>), [Multiagente](</pt-BR/concepts/multi-agent>)

Mídia e conteúdo rico 1 capacidade / com suporte LTS

Experimental0%

Alpha66%

Beta78%

[Telegram](</pt-BR/channels/telegram>), [Localização](</pt-BR/channels/location>)

Controles nativos e aprovações 9 capacidades / com suporte LTS

Experimental0%

Beta77%

Beta79%

[Telegram](</pt-BR/channels/telegram>), [Aprovações de execução](</pt-BR/tools/exec-approvals>), [Reações](</pt-BR/tools/reactions>)

Slack - M3 Beta - 5 áreas

Documentação de canal e superfície de roteamento de primeira classe. Precisa de scorecards de cenários de instalação/administração do workspace.

Cobertura Experimental - 0%Qualidade Alpha - 66%Completude Beta - 78%Completo - 5

Configuração e operações de canais 10 recursos / com suporte LTS

Experimental0%

Alpha66%

Beta78%

[Slack](</pt-BR/channels/slack>), [Slack](</pt-BR/plugins/reference/slack>), [Segredos](</pt-BR/gateway/secrets>), [Automação E2E de QA](</pt-BR/concepts/qa-e2e-automation>), [Solução de problemas](</pt-BR/channels/troubleshooting>)

Acesso e identidade 1 recurso / com suporte LTS

Experimental0%

Alpha66%

Beta78%

[Slack](</pt-BR/channels/slack>), [Emparelhamento](</pt-BR/channels/pairing>)

Roteamento e entrega de conversas 5 recursos / com suporte LTS

Experimental0%

Alpha66%

Beta78%

[Slack](</pt-BR/channels/slack>), [Proteção contra loops de bots](</pt-BR/channels/bot-loop-protection>), [Emparelhamento](</pt-BR/channels/pairing>)

Mídia e conteúdo avançado 1 recurso / com suporte LTS

Experimental0%

Alpha66%

Beta78%

[Slack](</pt-BR/channels/slack>), [Automação E2E de QA](</pt-BR/concepts/qa-e2e-automation>)

Controles e aprovações nativos 8 recursos / com suporte LTS

Experimental0%

Alpha66%

Beta78%

[Slack](</pt-BR/channels/slack>), [Comandos slash](</pt-BR/tools/slash-commands>), [Aprovações de execução](</pt-BR/tools/exec-approvals>)

iMessage e BlueBubbles - M3 Beta - 5 áreas

O iMessage com suporte é executado por meio do imsg em um host macOS Messages conectado; configurações legadas do BlueBubbles exigem migração. Mantenha visíveis as ressalvas sobre permissões do macOS, wrapper SSH, SIP/API privada e migração.

Cobertura Experimental - 0%Qualidade Alpha - 66%Completude Beta - 78%Nenhum

Configuração e operações de canal 11 capacidades

Experimental0%

Alfa66%

Beta78%

[Bluebubbles Imessage](</pt-BR/announcements/bluebubbles-imessage>), [Imessage do Bluebubbles](</pt-BR/channels/imessage-from-bluebubbles>), [Configurar canais](</pt-BR/gateway/config-channels>), [Imessage](</pt-BR/channels/imessage>)

Acesso e identidade 6 capacidades

Experimental0%

Alfa66%

Beta78%

[Imessage](</pt-BR/channels/imessage>), [Imessage do Bluebubbles](</pt-BR/channels/imessage-from-bluebubbles>), [Configurar canais](</pt-BR/gateway/config-channels>)

Roteamento e entrega de conversas 4 capacidades

Experimental0%

Alfa66%

Beta78%

[Imessage](</pt-BR/channels/imessage>)

Mídia e conteúdo rico 7 capacidades

Experimental0%

Alfa66%

Beta78%

[Imessage](</pt-BR/channels/imessage>), [Imessage do Bluebubbles](</pt-BR/channels/imessage-from-bluebubbles>), [Configurar canais](</pt-BR/gateway/config-channels>)

Controles nativos e aprovações 3 capacidades

Experimental0%

Alfa66%

Beta78%

[Imessage](</pt-BR/channels/imessage>)

WhatsApp - M3 Beta - 5 áreas

O caminho principal é importante e documentado; a volatilidade upstream do Baileys/sessão o mantém abaixo de Estável.

Cobertura Experimental - 0%Qualidade Alfa - 66%Completude Beta - 78%Nenhum

Configuração e operações de canais 5 capacidades

Experimental0%

Alfa66%

Beta78%

[WhatsApp](</pt-BR/channels/whatsapp>), [Configurar canais](</pt-BR/gateway/config-channels>), [WhatsApp](</pt-BR/plugins/reference/whatsapp>), [Automação de QA E2E](</pt-BR/concepts/qa-e2e-automation>), [Doctor](</pt-BR/gateway/doctor>)

Acesso e identidade 7 capacidades

Experimental0%

Alfa66%

Beta78%

[WhatsApp](</pt-BR/channels/whatsapp>), [Configurar canais](</pt-BR/gateway/config-channels>), [Automação de QA E2E](</pt-BR/concepts/qa-e2e-automation>), [Pareamento](</pt-BR/channels/pairing>)

Roteamento e entrega de conversas 4 capacidades

Experimental0%

Alfa66%

Beta78%

[WhatsApp](</pt-BR/channels/whatsapp>), [Mensagens em grupo](</pt-BR/channels/group-messages>)

Mídia e conteúdo rico 2 capacidades

Experimental0%

Alfa66%

Beta78%

[WhatsApp](</pt-BR/channels/whatsapp>)

Controles nativos e aprovações 2 capacidades

Experimental0%

Alfa66%

Beta78%

[WhatsApp](</pt-BR/channels/whatsapp>)

Matrix - M2 Alfa - 6 áreas

Compatível por meio de Plugin incluído. Precisa de scorecards de ponte, autenticação e ciclo de vida de salas.

Cobertura Experimental - 0%Qualidade Alfa - 60%Completude Alfa - 67%Nenhum

Configuração e operações de canais 5 capacidades

Experimental0%

Alfa60%

Alfa67%

[Matrix](</pt-BR/channels/matrix>), [Migração do Matrix](</pt-BR/channels/matrix-migration>)

Acesso e identidade 7 capacidades

Experimental0%

Alfa60%

Alfa67%

[Matrix](</pt-BR/channels/matrix>), [Grupos](</pt-BR/channels/groups>), [Proteção contra loops de bots](</pt-BR/channels/bot-loop-protection>)

Roteamento e entrega de conversas 1 capacidade

Experimental0%

Alfa60%

Alfa67%

[Matrix](</pt-BR/channels/matrix>)

Mídia e conteúdo rico 1 capacidade

Experimental0%

Alfa60%

Alfa67%

[Matrix](</pt-BR/channels/matrix>)

Controles nativos e aprovações 6 capacidades

Experimental0%

Alfa60%

Alfa67%

[Matrix](</pt-BR/channels/matrix>)

Criptografia e verificação 3 capacidades

Experimental0%

Alfa60%

Alfa67%

[Matrix](</pt-BR/channels/matrix>), [Migração do Matrix](</pt-BR/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 areas

Canal documentado, mas a configuração corporativa/administrativa aumenta o risco de maturidade.

Cobertura Experimental - 0%Qualidade Alfa - 59%Completude Alfa - 66%Nenhum

Configuração e operações de canais 16 capacidades

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</pt-BR/channels/googlechat>), [Googlechat](</pt-BR/plugins/reference/googlechat>), [Configuração de canais](</pt-BR/gateway/config-channels>), [Referência da CLI do assistente](</pt-BR/start/wizard-cli-reference>), [Segredos](</pt-BR/gateway/secrets>), [Superfície de credenciais Secretref](</pt-BR/reference/secretref-credential-surface>), [Saúde](</pt-BR/gateway/health>), [Inventário de Plugins](</pt-BR/plugins/plugin-inventory>), [Índice](</pt-BR/channels>)

Acesso e identidade 11 capacidades

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</pt-BR/channels/googlechat>), [Pareamento](</pt-BR/channels/pairing>), [Grupos de acesso](</pt-BR/channels/access-groups>), [Configuração de canais](</pt-BR/gateway/config-channels>), [Proteção contra loop de bots](</pt-BR/channels/bot-loop-protection>), [Roteamento de canais](</pt-BR/channels/channel-routing>)

Roteamento e entrega de conversas 1 capacidade

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</pt-BR/channels/googlechat>), [Proteção contra loop de bots](</pt-BR/channels/bot-loop-protection>), [Grupos de acesso](</pt-BR/channels/access-groups>), [Roteamento de canais](</pt-BR/channels/channel-routing>)

Mídia e conteúdo avançado 1 capacidade

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</pt-BR/channels/googlechat>), [Mensagem](</pt-BR/cli/message>), [Compreensão de mídia](</pt-BR/nodes/media-understanding>), [Superfície de credenciais Secretref](</pt-BR/reference/secretref-credential-surface>)

Controles nativos e aprovações 16 capacidades

Experimental0%

Alfa59%

Alfa66%

[Googlechat](</pt-BR/channels/googlechat>), [Mensagem](</pt-BR/cli/message>), [Compreensão de mídia](</pt-BR/nodes/media-understanding>), [Superfície de credenciais Secretref](</pt-BR/reference/secretref-credential-surface>), [Reações](</pt-BR/tools/reactions>), [Comandos de barra](</pt-BR/tools/slash-commands>), [Configuração de agentes](</pt-BR/gateway/config-agents>), [Refatoração do ciclo de vida de mensagens](</pt-BR/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alfa - 5 áreas

Fluxos empresariais de autenticação/administração precisam de prova explícita de cenário.

Cobertura Experimental - 0%Qualidade Alfa - 59%Completude Alfa - 66%Nenhum

Configuração e operações de canais 9 recursos

Experimental0%

Alpha59%

Alpha66%

[Msteams](</pt-BR/channels/msteams>), [Msteams](</pt-BR/plugins/reference/msteams>), [Configuração de canais](</pt-BR/gateway/config-channels>), [Integridade](</pt-BR/gateway/health>)

Acesso e identidade 9 recursos

Experimental0%

Alpha59%

Alpha66%

[Msteams](</pt-BR/channels/msteams>), [Pareamento](</pt-BR/channels/pairing>), [Grupos de acesso](</pt-BR/channels/access-groups>)

Roteamento e entrega de conversas 5 recursos

Experimental0%

Alpha59%

Alpha66%

[Msteams](</pt-BR/channels/msteams>), [Grupos](</pt-BR/channels/groups>), [Roteamento de canais](</pt-BR/channels/channel-routing>)

Mídia e conteúdo rico 5 recursos

Experimental0%

Alpha59%

Alpha66%

[Msteams](</pt-BR/channels/msteams>)

Controles e aprovações nativos 5 recursos

Experimental0%

Alpha59%

Alpha66%

[Msteams](</pt-BR/channels/msteams>), [Aprovações de execução avançadas](</pt-BR/tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 áreas

Existem documentos do canal compatível; precisa de provas mais robustas de instalação e reconexão.

Cobertura Experimental - 0%Qualidade Alpha - 59%Completude Alpha - 66%Nenhum

Configuração e operações de canais 7 capacidades

Experimental0%

Alfa59%

Alfa66%

[Signal](</pt-BR/channels/signal>), [Signal](</pt-BR/plugins/reference/signal>)

Acesso e identidade 6 capacidades

Experimental0%

Alfa59%

Alfa66%

[Signal](</pt-BR/channels/signal>)

Roteamento e entrega de conversas 1 capacidade

Experimental0%

Alfa59%

Alfa66%

[Signal](</pt-BR/channels/signal>)

Mídia e conteúdo rico 7 capacidades

Experimental0%

Alfa59%

Alfa66%

[Signal](</pt-BR/channels/signal>)

Controles e aprovações nativos 3 capacidades

Experimental0%

Alfa59%

Alfa66%

[Signal](</pt-BR/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, canais regionais - M2 Alfa - 4 áreas

Cobertura regional importante, mas o nível de suporte público deve ser calibrado por tipo de conta, aprovação upstream e prova do mantenedor.

Cobertura Experimental - 0%Qualidade Alfa - 55%Completude Alfa - 58%Nenhum

Configuração e operações de canais 6 capacidades

Experimental0%

Alfa61%

Alfa68%

[Índice](</pt-BR/channels>), [Pareamento](</pt-BR/channels/pairing>), [Feishu](</pt-BR/plugins/reference/feishu>), [Internos da arquitetura](</pt-BR/plugins/architecture-internals>)

Acesso e identidade 1 capacidade

Experimental0%

Alfa53%

Alfa54%

Nenhuma documentação vinculada

Roteamento e entrega de conversas 1 capacidade

Experimental0%

Alfa53%

Alfa54%

Nenhuma documentação vinculada

Mídia e conteúdo rico 1 capacidade

Experimental0%

Alfa53%

Alfa54%

Nenhuma documentação vinculada

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alfa - 4 áreas

Existem superfícies compatíveis, mas a maturidade provavelmente varia conforme a cobertura do upstream e dos mantenedores. Avalie individualmente mais tarde.

Cobertura Experimental - 0%Qualidade Alfa - 53%Completude Alfa - 54%Nenhum

Configuração e Operações de Canal 1 recurso

Experimental0%

Alpha53%

Alpha54%

Nenhuma documentação vinculada

Acesso e Identidade 1 recurso

Experimental0%

Alpha53%

Alpha54%

Nenhuma documentação vinculada

Roteamento e Entrega de Conversas 1 recurso

Experimental0%

Alpha53%

Alpha54%

Nenhuma documentação vinculada

Mídia e Conteúdo Rico 1 recurso

Experimental0%

Alpha53%

Alpha54%

Nenhuma documentação vinculada

Canal de Chamada de Voz - M1 Experimental - 5 áreas

Caminho opcional/de Plugin com comportamento complexo em tempo real. Precisa de scorecard de cenários antes do beta público.

Cobertura Experimental - 0%Qualidade Experimental - 41%Completude Experimental - 44%Nenhum

Configuração e operações de canais 2 capacidades

Experimental0%

Experimental41%

Experimental44%

[Chamada de voz](</pt-BR/cli/voicecall>), [Chamada de voz](</pt-BR/plugins/voice-call>), [Protocolo](</pt-BR/gateway/protocol>)

Acesso e identidade 1 capacidade

Experimental0%

Experimental41%

Experimental44%

[Chamada de voz](</pt-BR/plugins/voice-call>), [Chamada de voz](</pt-BR/cli/voicecall>)

Roteamento e entrega de conversas 1 capacidade

Experimental0%

Experimental41%

Experimental44%

[Chamada de voz](</pt-BR/plugins/voice-call>)

Mídia e conteúdo rico 2 capacidades

Experimental0%

Experimental41%

Experimental44%

[Chamada de voz](</pt-BR/plugins/voice-call>), [Inventário de Plugins](</pt-BR/plugins/plugin-inventory>)

Voz e chamadas em tempo real 2 capacidades

Experimental0%

Experimental41%

Experimental44%

[Chamada de voz](</pt-BR/plugins/voice-call>)

### Provedor e ferramenta

Automação de navegador, exec e ferramentas de sandbox - M3 Beta - 3 áreas

As ferramentas principais estão documentadas, mas a segurança do host e a UX de permissões devem permanecer sob revisão ativa do scorecard.

Cobertura Experimental - 21%Qualidade Beta - 75%Completude Beta - 79%Parcial - 2

Automação do navegador 8 capacidades

Experimental13%

Beta79%

Beta79%

[Controle do navegador](</pt-BR/tools/browser-control>), [Testes](</pt-BR/help/testing>), [Navegador](</pt-BR/tools/browser>), [Índice](</pt-BR/gateway/security>), [Verificações de auditoria](</pt-BR/gateway/security/audit-checks>)

Invocação e execução de ferramentas 6 capacidades / com suporte LTS

Alfa50%

Beta79%

Beta79%

[Exec](</pt-BR/tools/exec>), [Processo em segundo plano](</pt-BR/gateway/background-process>), [API HTTP de invocação de ferramentas](</pt-BR/gateway/tools-invoke-http-api>), [Escopos de operador](</pt-BR/gateway/operator-scopes>), [Protocolo](</pt-BR/gateway/protocol>), [Aprovações do Exec](</pt-BR/tools/exec-approvals>), [Aprovações avançadas do Exec](</pt-BR/tools/exec-approvals-advanced>), [Elevado](</pt-BR/tools/elevated>)

Sandbox e política de ferramentas 6 capacidades / com suporte LTS

Experimental0%

Alfa68%

Beta79%

[Sandboxing](</pt-BR/gateway/sandboxing>), [Sandbox vs. política de ferramentas vs. elevado](</pt-BR/gateway/sandbox-vs-tool-policy-vs-elevated>), [Ferramentas de sandbox multiagente](</pt-BR/tools/multi-agent-sandbox-tools>), [Referência do harness Codex](</pt-BR/plugins/codex-harness-reference>), [Ferramentas de configuração](</pt-BR/gateway/config-tools>)

Caminho do provedor OpenAI e Codex - M3 Beta - 5 áreas

Documentação aprofundada, caminho de OAuth/assinatura, voz em tempo real, imagem e comportamento de compatibilidade. A instabilidade do provedor impede que isto chegue a Estável sem comprovação do scorecard de lançamento.

Cobertura Experimental - 26%Qualidade Beta - 74%Completude Beta - 79%Parcial - 3

Modelo e Auth 6 recursos / compatível com LTS

Experimental44%

Beta79%

Beta79%

[Openai](</pt-BR/providers/openai>), [Harness Codex](</pt-BR/plugins/codex-harness>), [Modelos](</pt-BR/concepts/models>), [Oauth](</pt-BR/concepts/oauth>), [Referência do Harness Codex](</pt-BR/plugins/codex-harness-reference>), [Monitoramento de Auth](</pt-BR/gateway/authentication>)

Compatibilidade de respostas e ferramentas 4 recursos / compatível com LTS

Experimental40%

Beta79%

Beta79%

[Openai](</pt-BR/providers/openai>), [API HTTP Openresponses](</pt-BR/gateway/openresponses-http-api>), [API HTTP Openai](</pt-BR/gateway/openai-http-api>), [Plugins nativos do Codex](</pt-BR/plugins/codex-native-plugins>)

Harness Codex nativo 2 recursos / compatível com LTS

Experimental44%

Beta79%

Beta79%

[Harness Codex](</pt-BR/plugins/codex-harness>), [Runtime do Harness Codex](</pt-BR/plugins/codex-harness-runtime>), [Referência do Harness Codex](</pt-BR/plugins/codex-harness-reference>), [Plugins nativos do Codex](</pt-BR/plugins/codex-native-plugins>)

Entrada de imagem e multimodal 2 recursos

Experimental0%

Alpha67%

Beta79%

[Openai](</pt-BR/providers/openai>), [Geração de imagens](</pt-BR/tools/image-generation>), [Imagens](</pt-BR/nodes/images>)

Voz e áudio em tempo real 2 recursos

Experimental0%

Alpha67%

Beta79%

[Openai](</pt-BR/providers/openai>), [Discord](</pt-BR/channels/discord>), [Chamada de voz](</pt-BR/plugins/voice-call>)

Ferramentas de busca na Web - M3 Beta - 4 áreas

Existem vários provedores e docs. Exige prova de cota/erro/SSRF por família de provedores.

Cobertura Experimental - 9%Qualidade Beta - 74%Completude Beta - 79%Nenhum

Provedores de busca 19 capacidades

Experimental11%

Beta79%

Beta79%

[Web](</pt-BR/tools/web>), [Busca Brave](</pt-BR/tools/brave-search>), [Tavily](</pt-BR/tools/tavily>), [Busca Exa](</pt-BR/tools/exa-search>), [Firecrawl](</pt-BR/tools/firecrawl>), [Busca Perplexity](</pt-BR/tools/perplexity-search>), [Busca Duckduckgo](</pt-BR/tools/duckduckgo-search>), [Busca Searxng](</pt-BR/tools/searxng-search>), [Busca Gemini](</pt-BR/tools/gemini-search>), [Busca Grok](</pt-BR/tools/grok-search>), [Busca Kimi](</pt-BR/tools/kimi-search>), [Busca Minimax](</pt-BR/tools/minimax-search>), [Busca Ollama](</pt-BR/tools/ollama-search>), [Subcaminhos do Sdk](</pt-BR/plugins/sdk-subpaths>), [Visão geral do Sdk](</pt-BR/plugins/sdk-overview>), [Manifesto](</pt-BR/plugins/manifest>)

Configuração e diagnósticos 9 capacidades

Experimental0%

Alpha68%

Beta79%

[Web](</pt-BR/tools/web>), [Busca Web](</pt-BR/tools/web-fetch>), [Perguntas frequentes](</pt-BR/help/faq>), [Custos de uso da API](</pt-BR/reference/api-usage-costs>), [Busca Brave](</pt-BR/tools/brave-search>), [Busca Perplexity](</pt-BR/tools/perplexity-search>), [Tavily](</pt-BR/tools/tavily>), [Firecrawl](</pt-BR/tools/firecrawl>)

Segurança de rede 4 capacidades

Experimental0%

Alpha68%

Beta79%

[Web](</pt-BR/tools/web>), [Busca Web](</pt-BR/tools/web-fetch>), [Firecrawl](</pt-BR/tools/firecrawl>), [Busca Searxng](</pt-BR/tools/searxng-search>)

Disponibilidade e busca de ferramentas 11 capacidades

Experimental25%

Beta79%

Beta79%

[Ferramentas de configuração](</pt-BR/gateway/config-tools>), [Busca Web](</pt-BR/tools/web-fetch>), [Web](</pt-BR/tools/web>), [Perguntas frequentes](</pt-BR/help/faq>)

Caminho do provedor Anthropic - M3 Beta - 5 áreas

Provedor de modelos de primeira classe. Precisa de comprovação recorrente de cenários de autenticação/catálogo/chamada de ferramenta.

Cobertura Experimental - 0%Qualidade Beta - 71%Completude Beta - 78%Nenhum

Autenticação e recuperação de provedores 9 capacidades

Experimental0%

Alpha66%

Beta78%

[Anthropic](</pt-BR/providers/anthropic>), [Doctor](</pt-BR/gateway/doctor>), [Exemplos de configuração](</pt-BR/gateway/configuration-examples>), [Solução de problemas](</pt-BR/gateway/troubleshooting>), [Cache de prompts](</pt-BR/reference/prompt-caching>)

Seleção de modelo e tempo de execução 10 capacidades

Experimental0%

Beta78%

Beta79%

[Anthropic](</pt-BR/providers/anthropic>), [Agentes de configuração](</pt-BR/gateway/config-agents>), [Modelos](</pt-BR/concepts/models>), [Backends de CLI](</pt-BR/gateway/cli-backends>)

Transporte de solicitações e semântica de turnos 10 capacidades

Experimental0%

Beta77%

Beta79%

[Anthropic](</pt-BR/providers/anthropic>), [Cache de prompts](</pt-BR/reference/prompt-caching>), [Solução de problemas](</pt-BR/gateway/troubleshooting>), [Backends de CLI](</pt-BR/gateway/cli-backends>), [Provedores de modelos](</pt-BR/concepts/model-providers>)

Cache de prompts e contexto 5 capacidades

Experimental0%

Alpha66%

Beta78%

[Anthropic](</pt-BR/providers/anthropic>), [Cache de prompts](</pt-BR/reference/prompt-caching>), [Solução de problemas](</pt-BR/gateway/troubleshooting>), [Heartbeat](</pt-BR/gateway/heartbeat>)

Entradas de mídia 4 capacidades

Experimental0%

Alpha66%

Beta78%

[Anthropic](</pt-BR/providers/anthropic>), [Agentes de configuração](</pt-BR/gateway/config-agents>)

Google provider path - M3 Beta - 5 areas

Provedor de primeira classe com superfícies de modelo e tempo real. Precisa de pontuação separada para Live/Talk.

Cobertura Experimental - 0%Qualidade Alpha - 66%Completude Beta - 78%Nenhum

Configuração de provedor e credenciais 10 capacidades

Experimental0%

Alpha66%

Beta78%

[Google](</pt-BR/providers/google>), [Provedores de modelo](</pt-BR/concepts/model-providers>)

Roteamento de modelos e endpoints 10 capacidades

Experimental0%

Alpha66%

Beta78%

[Google](</pt-BR/providers/google>), [Provedores de modelo](</pt-BR/concepts/model-providers>), [Google](</pt-BR/plugins/reference/google>), [Pesquisa Gemini](</pt-BR/tools/gemini-search>)

Runtime direto do Gemini 9 capacidades

Experimental0%

Alpha66%

Beta78%

[Google](</pt-BR/providers/google>), [Provedores de modelo](</pt-BR/concepts/model-providers>), [Perguntas frequentes sobre modelos](</pt-BR/help/faq-models>), [Testes ao vivo](</pt-BR/help/testing-live>)

Mídia, pesquisa e tempo real 10 capacidades

Experimental0%

Alpha66%

Beta78%

[Google](</pt-BR/plugins/reference/google>), [Google](</pt-BR/providers/google>)

Cache de prompt 5 capacidades

Experimental0%

Alpha66%

Beta78%

[Cache de prompt](</pt-BR/reference/prompt-caching>), [Google](</pt-BR/providers/google>), [Provedores de modelo](</pt-BR/concepts/model-providers>), [Uso de tokens](</pt-BR/reference/token-use>)

Caminho do provedor OpenRouter - M3 Beta - 4 áreas

O caminho unificado de provedor está documentado e é valioso, mas o comportamento específico por modelo varia.

Cobertura Experimental - 0%Qualidade Alpha - 66%Completude Beta - 78%Nenhum

Configuração e autenticação de provedor 14 recursos

Experimental0%

Alpha66%

Beta78%

[Openrouter](</pt-BR/providers/openrouter>), [Provedores de modelos](</pt-BR/concepts/model-providers>), [Configurar](</pt-BR/cli/configure>), [Autenticação](</pt-BR/gateway/authentication>), [Ambiente](</pt-BR/help/environment>), [Modelos](</pt-BR/cli/models>), [Modelos](</pt-BR/concepts/models>)

Runtime de chat e normalização 15 recursos

Experimental0%

Alpha66%

Beta78%

[Openrouter](</pt-BR/providers/openrouter>), [Provedores de modelos](</pt-BR/concepts/model-providers>), [Cache de prompts](</pt-BR/reference/prompt-caching>)

Recuperação e diagnóstico de provedores 5 recursos

Experimental0%

Alpha66%

Beta78%

[Failover de modelo](</pt-BR/concepts/model-failover>), [Openrouter](</pt-BR/providers/openrouter>), [Modelos](</pt-BR/cli/models>)

Geração de mídia e fala 7 recursos

Experimental0%

Alpha66%

Beta78%

[Openrouter](</pt-BR/providers/openrouter>), [Geração de imagens](</pt-BR/tools/image-generation>), [Geração de música](</pt-BR/tools/music-generation>), [Visão geral de mídia](</pt-BR/tools/media-overview>), [Geração de vídeo](</pt-BR/tools/video-generation>), [Tts](</pt-BR/tools/tts>)

Ferramentas de geração de imagem, vídeo e música - M2 Alpha - 5 áreas

O recurso existe em vários provedores, mas qualidade, latência e compatibilidade de parâmetros variam demais para beta sem comprovação por provedor.

Cobertura Experimental - 0%Qualidade Alpha - 61%Completude Alpha - 68%Nenhum

Roteamento e Descoberta de Mídia 4 capacidades

Experimental0%

Alfa61%

Alfa68%

[Agentes de Configuração](</pt-BR/gateway/config-agents>), [Geração de Imagens](</pt-BR/tools/image-generation>), [Geração de Vídeos](</pt-BR/tools/video-generation>), [Geração de Música](</pt-BR/tools/music-generation>)

Ciclo de Vida e Entrega de Tarefas 12 capacidades

Experimental0%

Alfa61%

Alfa68%

[Visão Geral de Mídia](</pt-BR/tools/media-overview>), [Geração de Imagens](</pt-BR/tools/image-generation>), [Geração de Vídeos](</pt-BR/tools/video-generation>), [Geração de Música](</pt-BR/tools/music-generation>)

Geração de Imagens 9 capacidades

Experimental0%

Alfa61%

Alfa68%

[Geração de Imagens](</pt-BR/tools/image-generation>), [Infer](</pt-BR/cli/infer>), [Visão Geral de Mídia](</pt-BR/tools/media-overview>)

Geração de Vídeos 11 capacidades

Experimental0%

Alfa61%

Alfa68%

[Geração de Vídeos](</pt-BR/tools/video-generation>), [Runway](</pt-BR/providers/runway>), [Pixverse](</pt-BR/providers/pixverse>), [Fal](</pt-BR/providers/fal>), [Openrouter](</pt-BR/providers/openrouter>)

Geração de Música 6 capacidades

Experimental0%

Alfa61%

Alfa68%

[Geração de Música](</pt-BR/tools/music-generation>)

Provedores de modelos locais: Ollama, vLLM, SGLang, LM Studio - M2 Alfa - 5 áreas

Útil e documentado, mas a variação de ambiente é alta.

Cobertura Experimental - 0%Qualidade Alfa - 61%Completude Alfa - 68%Nenhum

Configuração, ciclo de vida e diagnósticos de provedores 12 capacidades

Experimental0%

Alfa61%

Alfa68%

[Modelos locais](</pt-BR/gateway/local-models>), [Lmstudio](</pt-BR/providers/lmstudio>), [Ollama](</pt-BR/providers/ollama>), [Vllm](</pt-BR/providers/vllm>), [Serviços de modelos locais](</pt-BR/gateway/local-model-services>), [Agentes de configuração](</pt-BR/gateway/config-agents>), [Solução de problemas](</pt-BR/gateway/troubleshooting>), [Doctor](</pt-BR/gateway/doctor>)

Plugins de provedores nativos 10 capacidades

Experimental0%

Alfa61%

Alfa68%

[Ollama](</pt-BR/providers/ollama>), [Lmstudio](</pt-BR/providers/lmstudio>)

Compatibilidade de runtime compatível com OpenAI 8 capacidades

Experimental0%

Alfa61%

Alfa68%

[Vllm](</pt-BR/providers/vllm>), [Sglang](</pt-BR/providers/sglang>), [Modelos locais](</pt-BR/gateway/local-models>), [Lmstudio](</pt-BR/providers/lmstudio>)

Memória local e embeddings 5 capacidades

Experimental0%

Alfa61%

Alfa68%

[Memória](</pt-BR/concepts/memory>), [Doctor](</pt-BR/gateway/doctor>)

Segurança de rede e controles de prompt 2 capacidades

Experimental0%

Alfa61%

Alfa68%

[Índice](</pt-BR/gateway/security>), [Ferramentas de configuração](</pt-BR/gateway/config-tools>), [Modelos locais](</pt-BR/gateway/local-models>)

Provedores hospedados de cauda longa - M2 Alfa - 3 áreas

Existem muitas páginas de documentação/referência; a pontuação deve ser gerada a partir dos metadados dos provedores, além da cobertura de smoke ao vivo.

Cobertura Experimental - 0%Qualidade Alfa - 61%Completude Alfa - 68%Nenhum

Provedores de LLM hospedados 12 capacidades

Experimental0%

Alfa61%

Alfa68%

[Índice](</pt-BR/providers>), [Provedores de modelos](</pt-BR/concepts/model-providers>), [Testes ao vivo](</pt-BR/help/testing-live>), [Integração inicial](</pt-BR/cli/onboard>)

Provedores de mídia hospedados 8 capacidades

Experimental0%

Alfa61%

Alfa68%

[Manifesto](</pt-BR/plugins/manifest>), [Testes ao vivo](</pt-BR/help/testing-live>), [Índice](</pt-BR/providers>)

Operações de provedores 12 capacidades

Experimental0%

Alfa61%

Alfa68%

[Índice](</pt-BR/providers>), [Provedores de modelos](</pt-BR/concepts/model-providers>), [Manifesto](</pt-BR/plugins/manifest>), [Testes ao vivo](</pt-BR/help/testing-live>), [Modelos](</pt-BR/cli/models>)

Was this useful?YesNo

Open issue