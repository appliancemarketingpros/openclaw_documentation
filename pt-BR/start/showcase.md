---
title: Showcase
source_url: https://docs.openclaw.ai/pt-BR/start/showcase
scraped_at: 2026-05-25
---

Projetos OpenClaw não são demos de brinquedo. As pessoas estão colocando em produção loops de revisão de PR, aplicativos móveis, automação residencial, sistemas de voz, devtools e fluxos pesados de memória a partir dos canais que já usam — builds nativos de chat em Telegram, WhatsApp, Discord e terminais; automação real para reserva, compras e suporte sem esperar por uma API; e integrações com o mundo físico usando impressoras, aspiradores, câmeras e sistemas residenciais.

## Vídeos

Comece aqui se quiser o caminho mais curto entre "o que é isso?" e "ok, entendi".

[**Passo a passo completo de configuração** VelvetShark, 28 minutos. Instalação, onboarding e primeiro assistente funcional de ponta a ponta. ](<https://www.youtube.com/watch?v=SaWSPZoPX34>) [**Reel de showcase da comunidade** Uma passada mais rápida por projetos reais, superfícies e fluxos de trabalho construídos em torno do OpenClaw. ](<https://www.youtube.com/watch?v=mMSKQvlmFuQ>) [**Projetos no mundo real** Exemplos da comunidade, de loops de codificação nativos de chat a hardware e automação pessoal. ](<https://www.youtube.com/watch?v=5kkIJNUGFho>)

## Novidades do Discord

Destaques recentes em codificação, devtools, mobile e construção de produtos nativos de chat.

[**Revisão de PR com feedback no Telegram** **@bangnokia** • `review` `github` `telegram` OpenCode finaliza a mudança, abre um PR, o OpenClaw revisa o diff e responde no Telegram com sugestões e um veredito claro de merge. ![Feedback de revisão de PR do OpenClaw entregue no Telegram](/assets/showcase/pr-review-telegram.jpg) ](<https://x.com/i/status/2010878524543131691>) [**Skill de adega em minutos** **@prades_maxime** • `skills` `local` `csv` Pediu ao "Robby" (@openclaw) uma skill local de adega. Ela solicita um CSV de exemplo e um caminho de armazenamento, depois cria e testa a skill (962 garrafas no exemplo). ![OpenClaw criando uma skill local de adega a partir de CSV](/assets/showcase/wine-cellar-skill.jpg) ](<https://x.com/i/status/2010916352454791216>) [**Piloto automático para compras no Tesco** **@marchattonhere** • `automation` `browser` `shopping` Plano semanal de refeições, itens habituais, reservar janela de entrega, confirmar pedido. Sem APIs, apenas controle de navegador. ![Automação de compras no Tesco via chat](/assets/showcase/tesco-shop.jpg) ](<https://x.com/i/status/2009724862470689131>) [**SNAG screenshot-to-Markdown** **@am-will** • `devtools` `screenshots` `markdown` Atalho para uma região da tela, visão Gemini, Markdown instantâneo na área de transferência. ![Ferramenta SNAG de screenshot para markdown](/assets/showcase/snag.png) ](<https://github.com/am-will/snag>) [**Agents UI** **@kitze** • `ui` `skills` `sync` Aplicativo desktop para gerenciar skills e comandos entre Agents, Claude, Codex e OpenClaw. ![Aplicativo Agents UI](/assets/showcase/agents-ui.jpg) ](<https://releaseflow.net/kitze/agents-ui>) [**Notas de voz no Telegram (papla.media)** **Comunidade** • `voice` `tts` `telegram` Encapsula TTS do papla.media e envia resultados como notas de voz do Telegram (sem autoplay irritante). ![Saída de nota de voz do Telegram a partir de TTS](/assets/showcase/papla-tts.jpg) ](<https://papla.media/docs>) [**CodexMonitor** **@odrobnik** • `devtools` `codex` `brew` Helper instalável via Homebrew para listar, inspecionar e observar sessões locais do OpenAI Codex (CLI + VS Code). ![CodexMonitor no ClawHub](/assets/showcase/codexmonitor.png) ](<https://clawhub.ai/odrobnik/codexmonitor>) [**Controle de impressora 3D Bambu** **@tobiasbischoff** • `hardware` `3d-printing` `skill` Controle e solução de problemas de impressoras BambuLab: status, jobs, câmera, AMS, calibração e mais. ![Skill Bambu CLI no ClawHub](/assets/showcase/bambu-cli.png) ](<https://clawhub.ai/tobiasbischoff/bambu-cli>) [**Transporte de Viena (Wiener Linien)** **@hjanuschka** • `travel` `transport` `skill` Partidas em tempo real, interrupções, status de elevadores e rotas para o transporte público de Viena. ![Skill Wiener Linien no ClawHub](/assets/showcase/wienerlinien.png) ](<https://clawhub.ai/hjanuschka/wienerlinien>) **Refeições escolares no ParentPay** **@George5562** • `automation` `browser` `parenting` Reserva automatizada de refeições escolares no Reino Unido via ParentPay. Usa coordenadas do mouse para clicar com confiabilidade em células de tabela. [**Upload para R2 (Send Me My Files)** **@julianengel** • `files` `r2` `presigned-urls` Faz upload para Cloudflare R2/S3 e gera links de download pré-assinados seguros. Útil para instâncias remotas do OpenClaw. ](<https://clawhub.ai/skills/r2-upload>) **App iOS via Telegram** **@coard** • `ios` `xcode` `testflight` Criou um aplicativo iOS completo com mapas e gravação de voz, implantado no TestFlight inteiramente via chat no Telegram. ![Aplicativo iOS no TestFlight](/assets/showcase/ios-testflight.jpg) **Assistente de saúde com Oura Ring** **@AS** • `health` `oura` `calendar` Assistente pessoal de saúde com IA integrando dados do Oura ring com calendário, compromissos e agenda da academia. ![Assistente de saúde com Oura ring](/assets/showcase/oura-health.png) [**Kev's Dream Team (14+ agentes)** **@adam91holt** • `multi-agent` `orchestration` Mais de 14 agentes sob um gateway com um orquestrador Opus 4.5 delegando a workers Codex. Veja o [texto técnico](<https://github.com/adam91holt/orchestrated-ai-articles>) e o [Clawdspace](<https://github.com/adam91holt/clawdspace>) para sandboxing de agentes. ](<https://github.com/adam91holt/orchestrated-ai-articles>) [**Linear CLI** **@NessZerra** • `devtools` `linear` `cli` CLI para Linear que se integra a fluxos de trabalho agentic (Claude Code, OpenClaw). Gerencie issues, projetos e fluxos a partir do terminal. ](<https://github.com/Finesssee/linear-cli>) [**Beeper CLI** **@jules** • `messaging` `beeper` `cli` Lê, envia e arquiva mensagens via Beeper Desktop. Usa a API MCP local do Beeper para que agentes possam gerenciar todos os seus chats (iMessage, WhatsApp e mais) em um só lugar. ](<https://github.com/blqke/beepcli>)

## Automação e fluxos de trabalho

Agendamento, controle de navegador, loops de suporte e o lado "simplesmente faça a tarefa por mim" do produto.

[**Controle de purificador de ar Winix** **@antonplex** • `automation` `hardware` `air-quality` Claude Code descobriu e confirmou os controles do purificador e, depois, o OpenClaw assume para gerenciar a qualidade do ar do ambiente. ![Controle de purificador de ar Winix via OpenClaw](/assets/showcase/winix-air-purifier.jpg) ](<https://x.com/antonplex/status/2010518442471006253>) [**Fotos bonitas do céu com câmera** **@signalgaining** • `automation` `camera` `skill` Acionado por uma câmera no telhado: peça ao OpenClaw para tirar uma foto do céu sempre que ele estiver bonito. Ele projetou uma skill e tirou a foto. ![Foto do céu capturada por uma câmera no telhado via OpenClaw](/assets/showcase/roof-camera-sky.jpg) ](<https://x.com/signalgaining/status/2010523120604746151>) [**Cena visual de briefing matinal** **@buddyhadry** • `automation` `briefing` `telegram` Um prompt agendado gera uma imagem de cena toda manhã (clima, tarefas, data, post favorito ou citação) por meio de uma persona do OpenClaw. ](<https://x.com/buddyhadry/status/2010005331925954739>) [**Reserva de quadra de padel** **@joshp123** • `automation` `booking` `cli` Verificador de disponibilidade do Playtomic mais CLI de reserva. Nunca mais perca uma quadra vaga. ![Captura de tela do padel-cli](/assets/showcase/padel-screenshot.jpg) ](<https://github.com/joshp123/padel-cli>) **Entrada contábil** **Comunidade** • `automation` `email` `pdf` Coleta PDFs por e-mail e prepara documentos para um consultor tributário. Contabilidade mensal no piloto automático. [**Modo dev do sofá** **@davekiss** • `telegram` `migration` `astro` Reconstruiu um site pessoal inteiro via Telegram enquanto assistia Netflix — Notion para Astro, 18 posts migrados, DNS para Cloudflare. Nunca abriu um laptop. ](<https://davekiss.com>) **Agente de busca de emprego** **@attol8** • `automation` `api` `skill` Pesquisa vagas, cruza com palavras-chave do CV e retorna oportunidades relevantes com links. Criado em 30 minutos usando a API JSearch. [**Construtor de skill para Jira** **@jdrhyne** • `jira` `skill` `devtools` O OpenClaw se conectou ao Jira e depois gerou uma nova skill em tempo real (antes mesmo de ela existir no ClawHub). ](<https://x.com/jdrhyne/status/2008336434827002232>) [**Skill Todoist via Telegram** **@iamsubhrajyoti** • `todoist` `skill` `telegram` Automatizou tarefas do Todoist e fez o OpenClaw gerar a skill diretamente no chat do Telegram. ](<https://x.com/iamsubhrajyoti/status/2009949389884920153>) **Análise no TradingView** **@bheem1798** • `finance` `browser` `automation` Faz login no TradingView por automação de navegador, captura screenshots de gráficos e executa análise técnica sob demanda. Sem API — apenas controle de navegador. **Suporte automático no Slack** **@henrymascot** • `slack` `automation` `support` Observa um canal de Slack da empresa, responde de forma útil e encaminha notificações para o Telegram. Corrigiu autonomamente um bug de produção em um app implantado sem que ninguém pedisse.

## Conhecimento e memória

Sistemas que indexam, pesquisam, lembram e raciocinam sobre conhecimento pessoal ou de equipe.

[**xuezh aprendizado de chinês** **@joshp123** • `learning` `voice` `skill` Motor de aprendizado de chinês com feedback de pronúncia e fluxos de estudo via OpenClaw. ![Feedback de pronúncia do xuezh](/assets/showcase/xuezh-pronunciation.jpeg) ](<https://github.com/joshp123/xuezh>) **Cofre de memória do WhatsApp** **Comunidade** • `memory` `transcription` `indexing` Ingere exports completos do WhatsApp, transcreve mais de 1k notas de voz, cruza com logs de git e gera relatórios em markdown com links. [**Busca semântica no Karakeep** **@jamesbrooksco** • `search` `vector` `bookmarks` Adiciona busca vetorial aos bookmarks do Karakeep usando Qdrant mais embeddings da OpenAI ou Ollama. ](<https://github.com/jamesbrooksco/karakeep-semantic-search>) **Memória estilo Divertida Mente 2** **Comunidade** • `memory` `beliefs` `self-model` Gerenciador de memória separado que transforma arquivos de sessão em memórias, depois em crenças e depois em um modelo de eu em evolução.

## Voz e telefone

Pontos de entrada com foco em fala, bridges telefônicas e fluxos pesados de transcrição.

[**Bridge telefônica Clawdia** **@alejandroOPI** • `voice` `vapi` `bridge` Bridge HTTP do assistente de voz Vapi para OpenClaw. Chamadas telefônicas quase em tempo real com seu agente. ](<https://github.com/alejandroOPI/clawdia-bridge>) [**Transcrição via OpenRouter** **@obviyus** • `transcription` `multilingual` `skill` Transcrição de áudio multilíngue via OpenRouter (Gemini e outros). Disponível no ClawHub. ](<https://clawhub.ai/obviyus/openrouter-transcribe>)

## Infraestrutura e implantação

Empacotamento, implantação e integrações que tornam o OpenClaw mais fácil de executar e estender.

[**Add-on do Home Assistant** **@ngutman** • `homeassistant` `docker` `raspberry-pi` Gateway OpenClaw em execução no Home Assistant OS com suporte a túnel SSH e estado persistente. ](<https://github.com/ngutman/openclaw-ha-addon>) [**Skill do Home Assistant** **ClawHub** • `homeassistant` `skill` `automation` Controle e automatize dispositivos do Home Assistant via linguagem natural. ](<https://clawhub.ai/skills/homeassistant>) [**Empacotamento Nix** **@openclaw** • `nix` `packaging` `deployment` Configuração OpenClaw com Nix e baterias incluídas para implantações reproduzíveis. ](<https://github.com/openclaw/nix-openclaw>) [**Calendário CalDAV** **ClawHub** • `calendar` `caldav` `skill` Skill de calendário usando khal e vdirsyncer. Integração de calendário auto-hospedada. ](<https://clawhub.ai/skills/caldav-calendar>)

## Casa e hardware

O lado físico do OpenClaw: casas, sensores, câmeras, aspiradores e outros dispositivos.

[**Automação GoHome** **@joshp123** • `home` `nix` `grafana` Automação residencial nativa de Nix com OpenClaw como interface, além de dashboards no Grafana. ![Dashboard GoHome no Grafana](/assets/showcase/gohome-grafana.png) ](<https://github.com/joshp123/gohome>) [**Aspirador Roborock** **@joshp123** • `vacuum` `iot` `plugin` Controle seu aspirador robô Roborock por meio de conversa natural. ![Status do Roborock](/assets/showcase/roborock-screenshot.jpg) ](<https://github.com/joshp123/gohome/tree/main/plugins/roborock>)

## Projetos da comunidade

Coisas que cresceram além de um fluxo de trabalho isolado e se tornaram produtos ou ecossistemas mais amplos.

[**Marketplace StarSwap** **Comunidade** • `marketplace` `astronomy` `webapp` Marketplace completo de equipamentos de astronomia. Construído com e em torno do ecossistema OpenClaw. ](<https://star-swap.com/>)

## Envie seu projeto

* ### Compartilhe

Publique em [#self-promotion no Discord](<https://discord.gg/clawd>) ou [tweet para @openclaw](<https://x.com/openclaw>).

* ### Inclua detalhes

Conte o que ele faz, coloque o link do repositório ou da demo e compartilhe uma captura de tela, se tiver.

* ### Apareça aqui

Adicionaremos projetos de destaque a esta página.

## Relacionado

  * [Primeiros passos](</pt-BR/start/getting-started>)
  * [OpenClaw](</pt-BR/start/openclaw>)


Was this useful?YesNo