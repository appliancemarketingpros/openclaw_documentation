---
title: Data e hora
source_url: https://docs.openclaw.ai/pt-BR/date-time
scraped_at: 2026-05-25
---

OpenClaw usa por padrão **horário local do host para carimbos de data/hora de transporte** e **fuso horário do usuário apenas no prompt do sistema**. Os carimbos de data/hora do provedor são preservados para que as ferramentas mantenham sua semântica nativa (o horário atual está disponível via `session_status`).

## Envelopes de mensagens (local por padrão)

Mensagens recebidas são envolvidas com um carimbo de data/hora (precisão de minuto):

CodeCopy code
[code]
    [Provider ... 2026-01-05 16:26 PST] message text
[/code]

Esse carimbo de data/hora do envelope é **local do host por padrão** , independentemente do fuso horário do provedor.

Você pode substituir esse comportamento:

json5Copy code
[code]
    {  agents: {    defaults: {      envelopeTimezone: "local", // "utc" | "local" | "user" | IANA timezone      envelopeTimestamp: "on", // "on" | "off"      envelopeElapsed: "on", // "on" | "off"    },  },}
[/code]

  * `envelopeTimezone: "utc"` usa UTC.
  * `envelopeTimezone: "local"` usa o fuso horário do host.
  * `envelopeTimezone: "user"` usa `agents.defaults.userTimezone` (recorre ao fuso horário do host).
  * Use um fuso horário IANA explícito (por exemplo, `"America/Chicago"`) para uma zona fixa.
  * `envelopeTimestamp: "off"` remove carimbos de data/hora absolutos dos cabeçalhos de envelope.
  * `envelopeElapsed: "off"` remove sufixos de tempo decorrido (o estilo `+2m`).


### Exemplos

**Local (padrão):**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 PST] hello
[/code]

**Fuso horário do usuário:**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 CST] hello
[/code]

**Tempo decorrido habilitado:**

CodeCopy code
[code]
    [WhatsApp +1555 +30s 2026-01-18T05:19Z] follow-up
[/code]

## Prompt do sistema: data e hora atuais

Se o fuso horário do usuário for conhecido, o prompt do sistema incluirá uma seção dedicada **Data e hora atuais** com **somente o fuso horário** (sem formato de relógio/hora) para manter o cache de prompt estável:

CodeCopy code
[code]
    Time zone: America/Chicago
[/code]

Quando o agente precisar do horário atual, use a ferramenta `session_status`; o cartão de status inclui uma linha de carimbo de data/hora.

## Linhas de eventos do sistema (locais por padrão)

Eventos do sistema enfileirados inseridos no contexto do agente recebem um prefixo com um carimbo de data/hora usando a mesma seleção de fuso horário dos envelopes de mensagens (padrão: local do host).

CodeCopy code
[code]
    System: [2026-01-12 12:19:17 PST] Model switched.
[/code]

### Configurar fuso horário + formato do usuário

json5Copy code
[code]
    {  agents: {    defaults: {      userTimezone: "America/Chicago",      timeFormat: "auto", // auto | 12 | 24    },  },}
[/code]

  * `userTimezone` define o **fuso horário local do usuário** para o contexto do prompt.
  * `timeFormat` controla a **exibição em 12h/24h** no prompt. `auto` segue as preferências do SO.


## Detecção de formato de hora (automática)

Quando `timeFormat: "auto"`, o OpenClaw inspeciona a preferência do SO (macOS/Windows) e recorre à formatação de localidade. O valor detectado é **armazenado em cache por processo** para evitar chamadas repetidas ao sistema.

## Payloads de ferramentas + conectores (hora bruta do provedor + campos normalizados)

Ferramentas de canal retornam **carimbos de data/hora nativos do provedor** e adicionam campos normalizados para consistência:

  * `timestampMs`: milissegundos desde a época Unix (UTC)
  * `timestampUtc`: string UTC ISO 8601


Campos brutos do provedor são preservados para que nada seja perdido.

  * Slack: strings semelhantes à época Unix da API
  * Discord: carimbos de data/hora ISO em UTC
  * Telegram/WhatsApp: carimbos de data/hora numéricos/ISO específicos do provedor


Se precisar do horário local, converta-o downstream usando o fuso horário conhecido.

## Documentos relacionados

  * [Prompt do sistema](</pt-BR/concepts/system-prompt>)
  * [Fusos horários](</pt-BR/concepts/timezone>)
  * [Mensagens](</pt-BR/concepts/messages>)


Was this useful?YesNo