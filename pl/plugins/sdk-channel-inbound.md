---
title: Interfejs API przychodzący kanału
source_url: https://docs.openclaw.ai/pl/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Wtyczki kanałów powinny modelować ścieżki odbioru rzeczownikami związanymi z przychodzącymi zdarzeniami i wiadomościami:

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

Używaj `openclaw/plugin-sdk/channel-inbound` do normalizacji zdarzeń przychodzących, formatowania, korzeni i orkiestracji. Używaj `openclaw/plugin-sdk/channel-outbound` do natywnego wysyłania, potwierdzeń odbioru, trwałego dostarczania i działania podglądu na żywo.

## Główne helpery

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: rzutuje znormalizowane fakty kanału na kontekst promptu/sesji. Użyj `channelContext`, aby przekazać należące do kanału metadane nadawcy/czatu do hooka wtyczki `ctx.channelContext`; rozszerz `PluginHookChannelSenderContext` lub `PluginHookChannelChatContext` z tej ścieżki podrzędnej o pola specyficzne dla kanału.
  * `runChannelInboundEvent(...)`: uruchamia pobieranie, klasyfikację, kontrolę wstępną, rozwiązywanie, rejestrowanie, wysyłkę i finalizację dla jednego przychodzącego zdarzenia platformy.
  * `dispatchChannelInboundReply(...)`: rejestruje i wysyła już złożoną odpowiedź przychodzącą za pomocą adaptera dostarczania.


Wstrzyknięte środowisko uruchomieniowe wtyczki udostępnia te same wysokopoziomowe helpery pod `runtime.channel.inbound.*` dla kanałów dołączonych/natywnych, które już otrzymują obiekt środowiska uruchomieniowego.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

Dispatchery zgodności powinny składać dane wejściowe `dispatchChannelInboundReply(...)` i utrzymywać dostarczanie platformowe w adapterze dostarczania. Nowe ścieżki wysyłania powinny preferować adaptery wiadomości i trwałe helpery wiadomości.

## Migracja

Stare aliasy środowiska uruchomieniowego `runtime.channel.turn.*` zostały usunięte. Używaj:

  * `runtime.channel.inbound.run(...)` dla surowych zdarzeń przychodzących.
  * `runtime.channel.inbound.dispatchReply(...)` dla złożonych kontekstów odpowiedzi.
  * `runtime.channel.inbound.buildContext(...)` dla ładunków kontekstu przychodzącego.
  * `runtime.channel.inbound.runPreparedReply(...)` tylko dla należących do kanału przygotowanych ścieżek wysyłki, które już składają własne domknięcie wysyłki.


Nowy kod wtyczki nie powinien wprowadzać interfejsów API kanału nazwanych `turn`. Słownictwo tur modelu lub agenta trzymaj w kodzie agenta/dostawcy; wtyczki kanałów używają terminów dotyczących danych przychodzących, wiadomości, dostarczania i odpowiedzi.

Was this useful?YesNo

Open issue