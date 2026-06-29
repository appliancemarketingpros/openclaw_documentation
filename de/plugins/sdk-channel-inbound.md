---
title: API für eingehende Kanäle
source_url: https://docs.openclaw.ai/de/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel-Plugins sollten Empfangspfade mit den Begriffen inbound und message modellieren:

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

Verwenden Sie `openclaw/plugin-sdk/channel-inbound` für die Normalisierung eingehender Ereignisse, Formatierung, Roots und Orchestrierung. Verwenden Sie `openclaw/plugin-sdk/channel-outbound` für natives Senden, Empfangsbestätigungen, dauerhafte Zustellung und Live-Vorschauverhalten.

## Kernhilfen

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: projiziert normalisierte Channel-Fakten in den Prompt-/Sitzungskontext. Verwenden Sie `channelContext`, um sender/chat-Metadaten im Besitz des Channels an den Plugin-Hook `ctx.channelContext` weiterzugeben; erweitern Sie `PluginHookChannelSenderContext` oder `PluginHookChannelChatContext` aus diesem Unterpfad für channelspezifische Felder.
  * `runChannelInboundEvent(...)`: führt Ingest, Klassifizierung, Preflight, Auflösung, Aufzeichnung, Dispatch und Finalisierung für ein eingehendes Plattformereignis aus.
  * `dispatchChannelInboundReply(...)`: zeichnet eine bereits zusammengestellte eingehende Antwort auf und dispatcht sie mit einem Zustellungsadapter.


Die injizierte Plugin-Laufzeit stellt dieselben High-Level-Hilfen unter `runtime.channel.inbound.*` für gebündelte/native Channels bereit, die bereits das Laufzeitobjekt erhalten.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

Kompatibilitäts-Dispatcher sollten Eingaben für `dispatchChannelInboundReply(...)` zusammenstellen und die Plattformzustellung im Zustellungsadapter belassen. Neue Sendepfade sollten Message-Adapter und dauerhafte Message-Hilfen bevorzugen.

## Migration

Die alten Laufzeit-Aliasse `runtime.channel.turn.*` wurden entfernt. Verwenden Sie:

  * `runtime.channel.inbound.run(...)` für rohe eingehende Ereignisse.
  * `runtime.channel.inbound.dispatchReply(...)` für zusammengestellte Antwortkontexte.
  * `runtime.channel.inbound.buildContext(...)` für eingehende Kontext-Payloads.
  * `runtime.channel.inbound.runPreparedReply(...)` nur für vorbereitete Dispatch-Pfade im Besitz des Channels, die bereits ihre eigene Dispatch-Closure zusammenstellen.


Neuer Plugin-Code sollte keine Channel-APIs mit `turn` im Namen einführen. Halten Sie Modell- oder Agent-Turn-Vokabular in Agent-/Provider-Code; Channel-Plugins verwenden Begriffe wie inbound, message, delivery und reply.

Was this useful?YesNo

Open issue