---
title: Raft
source_url: https://docs.openclaw.ai/pl/channels/raft
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

Obsługa Raft łączy agenta OpenClaw z zewnętrznym agentem Raft za pośrednictwem lokalnego Raft CLI. Raft wysyła uwierzytelnione wskazówki wybudzania do Gateway. Następnie agent używa Raft CLI do sprawdzania i wysyłania wiadomości.

## Instalacja

Raft jest oficjalnym zewnętrznym pluginem. Zainstaluj go na hoście Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

Szczegóły: [Pluginy](</pl/tools/plugin>)

## Wymagania wstępne

  * Obszar roboczy Raft z zewnętrznym agentem.
  * Raft CLI zainstalowany na tym samym hoście co OpenClaw Gateway.
  * Profil Raft CLI, który jest już zalogowany i powiązany z tym zewnętrznym agentem.


Plugin nie przechowuje poświadczeń Raft. Raft CLI przechowuje to uwierzytelnienie we własnym profilu.

## Konfiguracja

Ustaw profil w konfiguracji:

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

Dla konta domyślnego możesz zamiast tego ustawić `RAFT_PROFILE` w środowisku Gateway:

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

Użyj nazwanego konta, gdy jeden Gateway łączy się z więcej niż jednym zewnętrznym agentem Raft:

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

Interaktywny przepływ konfiguracji zapisuje ten sam profil:

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## Jak to działa

Gdy Gateway się uruchamia, plugin:

  1. Otwiera punkt końcowy HTTP wybudzania dostępny tylko przez local loopback na efemerycznym porcie.
  2. Uruchamia `raft --profile <profile> agent bridge` z tym punktem końcowym i tokenem przypisanym do procesu.
  3. Akceptuje tylko uwierzytelnione, pozbawione treści wskazówki wybudzania z tożsamością powtórzenia z lokalnego mostu.
  4. Wymaga jednego z `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id` lub `id`.
  5. Deduplikuje ostatnie ponowione dostarczenia wybudzania według identyfikatora zdarzenia mostu, także między restartami Gateway.
  6. Zwraca stabilną sesję uruchomieniową dla bieżącego mostu oraz pustą partię opróżniania aktywności dla protokołu Raft CLI.
  7. Uruchamia jedną serializowaną turę agenta OpenClaw dla każdego zaakceptowanego wybudzenia.


Most odpowiada za ponowne próby dostarczania i ponowne połączenia Raft. Tura OpenClaw otrzymuje tylko powiadomienie o wybudzeniu, a nie skopiowaną treść wiadomości Raft. Używa CLI do odczytu oczekujących wiadomości i wysłania odpowiedzi:

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## Weryfikacja

Sprawdź, czy OpenClaw może znaleźć CLI i ma skonfigurowany profil:

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

Następnie wyślij wiadomość do zewnętrznego agenta Raft. Dziennik Gateway powinien pokazać uruchomienie mostu Raft, a potem przychodzące wybudzenie. Agent powinien użyć skonfigurowanego profilu Raft do sprawdzenia oczekujących wiadomości.

## Rozwiązywanie problemów

Raft CLI is missing

Zainstaluj Raft CLI na hoście Gateway i udostępnij `raft` w `PATH` usługi. Zweryfikuj to za pomocą `raft --help`, a następnie zrestartuj Gateway.

The bridge exits immediately

Sprawdź, czy skonfigurowany profil jest zalogowany i należy do zamierzonego zewnętrznego agenta Raft. Uruchom `raft --profile <profile> agent bridge` bezpośrednio, aby zobaczyć diagnostykę CLI.

A wake arrives but no Raft response is sent

Jest to oczekiwane, gdy agent nie wywołuje Raft CLI. Most wybudzania nie przenosi treści wiadomości ani automatycznych odpowiedzi końcowych. Sprawdź politykę narzędzi agenta i upewnij się, że może uruchamiać `raft --profile <profile> message check` oraz `message send`.

## Odnośniki

  * [Raft](<https://raft.build/>)
  * [Dokumentacja Raft](<https://docs.raft.build/welcome/>)
  * [Integracja Hermes Raft](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue