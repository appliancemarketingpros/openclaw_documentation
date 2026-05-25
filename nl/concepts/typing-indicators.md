---
title: Typindicatoren
source_url: https://docs.openclaw.ai/nl/concepts/typing-indicators
scraped_at: 2026-05-25
---

Typindicatoren worden naar het chatkanaal verzonden terwijl een uitvoering actief is. Gebruik `agents.defaults.typingMode` om te bepalen **wanneer** typen begint en `typingIntervalSeconds` om te bepalen **hoe vaak** dit wordt vernieuwd.

## Standaardwaarden

Wanneer `agents.defaults.typingMode` **niet is ingesteld** , behoudt OpenClaw het oude gedrag:

  * **Directe chats** : typen begint meteen zodra de modellus begint.
  * **Groepschats met een vermelding** : typen begint meteen.
  * **Groepschats zonder vermelding** : typen begint pas wanneer berichttekst begint te streamen.
  * **Heartbeat-uitvoeringen** : typen begint wanneer de Heartbeat-uitvoering begint als het opgeloste Heartbeat-doel een chat is die typen ondersteunt en typen niet is uitgeschakeld.


## Modi

Stel `agents.defaults.typingMode` in op een van:

  * `never` \- nooit een typindicator.
  * `instant` \- begin met typen **zodra de modellus begint** , zelfs als de uitvoering later alleen de stille antwoordtoken retourneert.
  * `thinking` \- begin met typen bij de **eerste redeneerdelta** (vereist `reasoningLevel: "stream"` voor de uitvoering).
  * `message` \- begin met typen bij de **eerste niet-stille tekstdelta** (negeert de stille token `NO_REPLY`).


Volgorde van "hoe vroeg het wordt geactiveerd": `never` → `message` → `thinking` → `instant`

## Configuratie

Stel de standaardwaarde op agentniveau in:

json5Copy code
[code]
    {  agents: {    defaults: {      typingMode: "thinking",      typingIntervalSeconds: 6,    },  },}
[/code]

Overschrijf de modus of cadans per sessie:

json5Copy code
[code]
    {  session: {    typingMode: "message",    typingIntervalSeconds: 4,  },}
[/code]

## Opmerkingen

  * De modus `message` toont geen typen voor antwoorden die alleen stil zijn wanneer de volledige payload de exacte stille token is (bijvoorbeeld `NO_REPLY` / `no_reply`, hoofdletterongevoelig gematcht).
  * `thinking` wordt alleen geactiveerd als de uitvoering redenering streamt (`reasoningLevel: "stream"`). Als het model geen redeneerdelta's uitstuurt, begint typen niet.
  * Heartbeat-typen is een levendigheidssignaal voor het opgeloste bezorgdoel. Het begint bij de start van de Heartbeat-uitvoering in plaats van de streamtiming van `message` of `thinking` te volgen. Stel `typingMode: "never"` in om het uit te schakelen.
  * Heartbeats tonen geen typen wanneer `target: "none"`, wanneer het doel niet kan worden opgelost, wanneer chatbezorging is uitgeschakeld voor de Heartbeat, of wanneer het kanaal typen niet ondersteunt.
  * `typingIntervalSeconds` bepaalt de **vernieuwingscadans** , niet de starttijd. De standaardwaarde is 6 seconden.


## Gerelateerd

[**Aanwezigheid** Hoe de Gateway verbonden clients bijhoudt en ze toont op het macOS-tabblad Instances. ](</nl/concepts/presence>) [**Streaming en opdelen in chunks** Uitgaand streaminggedrag, chunkgrenzen en kanaalspecifieke bezorging. ](</nl/concepts/streaming>)

Was this useful?YesNo