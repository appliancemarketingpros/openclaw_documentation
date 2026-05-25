---
title: Automação da CLI
source_url: https://docs.openclaw.ai/pt-BR/start/wizard-cli-automation
scraped_at: 2026-05-25
---

Use `--non-interactive` para automatizar `openclaw onboard`.

## Exemplo básico não interativo

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

Adicione `--json` para obter um resumo legível por máquina.

Use `--skip-bootstrap` quando sua automação pré-popula arquivos do workspace e não quer que o onboarding crie os arquivos de bootstrap padrão.

Use `--secret-input-mode ref` para armazenar referências baseadas em env em perfis de autenticação em vez de valores em texto simples. A seleção interativa entre referências env e referências configuradas do provedor (`file` ou `exec`) está disponível no fluxo de onboarding.

No modo `ref` não interativo, as variáveis de env do provedor devem estar definidas no ambiente do processo. Passar flags de chave inline sem a variável de env correspondente agora falha rapidamente.

Exemplo:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## Exemplos específicos de provedor

Exemplo de chave de API da Anthropic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemplo do Gemini bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemplo da Z.AI bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemplo do Vercel AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemplo do Cloudflare AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemplo do Moonshot bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemplo do Mistral bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemplo do Synthetic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemplo do OpenCode bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Troque para `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` para o catálogo Go.

Exemplo do Ollama bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemplo de provedor personalizado bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` é opcional. Se omitido, o onboarding verifica `CUSTOM_API_KEY`. O OpenClaw marca IDs comuns de modelos de visão como compatíveis com imagem automaticamente. Adicione `--custom-image-input` para IDs de visão personalizados desconhecidos, ou `--custom-text-input` para forçar metadados somente texto.

Variante em modo ref:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Nesse modo, o onboarding armazena `apiKey` como `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.

O setup-token da Anthropic continua disponível como um caminho de token de onboarding compatível, mas o OpenClaw agora prefere reutilizar a Claude CLI quando disponível. Para produção, prefira uma chave de API da Anthropic.

## Adicionar outro agente

Use `openclaw agents add <name>` para criar um agente separado com seu próprio workspace, sessões e perfis de autenticação. Executar sem `--workspace` inicia o assistente.

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

O que ele define:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Observações:

  * Workspaces padrão seguem `~/.openclaw/workspace-<agentId>`.
  * Adicione `bindings` para rotear mensagens de entrada (o assistente pode fazer isso).
  * Flags não interativas: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Documentação relacionada

  * Hub de onboarding: [Onboarding (CLI)](</pt-BR/start/wizard>)
  * Referência completa: [Referência de configuração da CLI](</pt-BR/start/wizard-cli-reference>)
  * Referência do comando: [`openclaw onboard`](</pt-BR/cli/onboard>)


Was this useful?YesNo